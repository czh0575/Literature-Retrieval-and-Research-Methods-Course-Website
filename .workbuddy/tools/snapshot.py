# -*- coding: utf-8 -*-
"""记录讲义的结构指纹，用于改写前后比对，确保内容未被破坏。"""
import os
import re
import sys
import json

DOCS = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
SKIP = {'01-course-introduction'}


def strip_code(text):
    return re.sub(r'```[\s\S]*?```', lambda m: '\n' * m.group(0).count('\n'), text)


def fingerprint(path):
    raw = open(path, encoding='utf-8').read()
    # 去掉代码块正文，但保留围栏
    fences = len(re.findall(r'^```', raw, re.M))
    body = strip_code(raw)
    lines = body.split('\n')
    heads = [l.strip() for l in lines if re.match(r'^#{1,6}\s', l.strip())]
    imgs = re.findall(r'!\[[^\]]*\]\((/images/[^)]+)\)', raw)
    caps = re.findall(r'^\*图 [^*]+\*$', body, re.M)
    conts = re.findall(r'^:::[ \t]*(\w+)', body, re.M)
    # 表格：连续以 | 开头的行块，取每块的行数
    tables = []
    cur = 0
    for l in lines:
        if l.strip().startswith('|'):
            cur += 1
        else:
            if cur:
                tables.append(cur)
            cur = 0
    if cur:
        tables.append(cur)
    # 列表项与非空段落
    bullets = sum(1 for l in lines if re.match(r'^\s*(?:[-*+]|\d+\.)\s+\S', l))
    paras = [l.strip() for l in lines if l.strip() and not l.strip().startswith(('#', '|', '>', ':'))]
    paras = [p for p in paras if not re.match(r'^\s*(?:[-*+]|\d+\.)\s', p)]
    links = sorted(set(re.findall(r'https?://[^\s)>」]+', raw)))
    xref = sorted(set(re.findall(r'参见\s*[\d.]+', raw)))
    return {
        'lines': len(raw.split('\n')),
        'headings': heads,
        'images': imgs,
        'captions': caps,
        'containers': conts,
        'tables': tables,
        'bullets': bullets,
        'para_count': len(paras),
        'para_chars': sum(len(p) for p in paras),
        'fences': fences,
        'links': links,
        'xref': xref,
    }


def collect(only=None):
    out = {}
    for sub in sorted(os.listdir(DOCS)):
        if sub in SKIP or (only and sub != only):
            continue
        d = os.path.join(DOCS, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith('.md'):
                out['%s/%s' % (sub, f)] = fingerprint(os.path.join(d, f))
    return out


def compare(a, b):
    """a=旧, b=新"""
    KNOWN = {'tip', 'warning', 'details', 'info', 'danger', 'note', 'important', 'caution'}
    problems = []
    for k in sorted(a):
        if k not in b:
            problems.append('文件消失: %s' % k)
            continue
        o, n = a[k], b[k]
        oc = [c for c in o['containers'] if c in KNOWN]
        nc = [c for c in n['containers'] if c in KNOWN]
        if o['headings'] != n['headings']:
            problems.append('%s 标题变化:\n    旧 %s\n    新 %s' % (k, o['headings'], n['headings']))
        if o['images'] != n['images']:
            problems.append('%s 图片引用变化: 旧 %s / 新 %s' % (k, o['images'], n['images']))
        if o['captions'] != n['captions']:
            problems.append('%s 图注变化:\n    旧 %s\n    新 %s' % (k, o['captions'], n['captions']))
        if sorted(oc) != sorted(nc):
            problems.append('%s 容器类型变化: 旧 %s / 新 %s' % (k, sorted(oc), sorted(nc)))
        if o['tables'] != n['tables']:
            problems.append('%s 表格行数变化: 旧 %s / 新 %s' % (k, o['tables'], n['tables']))
        if o['fences'] != n['fences']:
            problems.append('%s 代码围栏数变化: 旧 %d / 新 %d' % (k, o['fences'], n['fences']))
        if o['links'] != n['links']:
            problems.append('%s 网址集合变化:\n    旧 %s\n    新 %s' % (k, o['links'], n['links']))
        if o['xref'] != n['xref']:
            problems.append('%s 交叉引用变化: 旧 %s / 新 %s' % (k, o['xref']))
        if abs(o['bullets'] - n['bullets']) > max(3, o['bullets'] * 0.12):
            problems.append('%s 列表项数变化较大: 旧 %d / 新 %d' % (k, o['bullets'], n['bullets']))
        if o['lines'] and abs(o['lines'] - n['lines']) > o['lines'] * 0.25:
            problems.append('%s 行数变化较大: 旧 %d / 新 %d' % (k, o['lines'], n['lines']))
        if o['para_chars'] and abs(o['para_chars'] - n['para_chars']) > o['para_chars'] * 0.25:
            problems.append('%s 正文字数变化较大: 旧 %d / 新 %d' % (k, o['para_chars'], n['para_chars']))
    for k in sorted(b):
        if k not in a:
            problems.append('新增文件: %s' % k)
    return problems


if __name__ == '__main__':
    mode = sys.argv[1]
    only = sys.argv[2] if len(sys.argv) > 2 else None
    path = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\.workbuddy\snapshot_%s.json' % mode
    if mode == 'before':
        data = collect(only)
        json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('已记录 %d 个文件 -> %s' % (len(data), path))
    else:
        old = json.load(open(r'F:\02教学\教学课程\文献检索与研究方法\课件\web\.workbuddy\snapshot_before.json', encoding='utf-8'))
        new = collect(only)
        probs = compare(old, new)
        print('=== 结构比对：%d 个文件 ===' % len(new))
        if probs:
            for p in probs:
                print('  [!]', p)
        else:
            print('  全部一致，内容结构未被破坏')
        print()
        print('=== 逐页字数变化 ===')
        for k in sorted(new):
            o, n = old.get(k, {}), new[k]
            if not o:
                continue
            d = n['para_chars'] - o['para_chars']
            print('  %-46s %5d -> %5d  (%+d, %+.0f%%)' % (k, o['para_chars'], n['para_chars'], d, d / max(o['para_chars'], 1) * 100))
