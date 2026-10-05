# -*- coding: utf-8 -*-
"""去 AI 味：机械性替换（带 dry-run 复核）。

只处理确定性高、不需要上下文判断的部分：
  A. 元评论引导句整句删除（「下面给出……」「下面分三点说明……」「本节讲清楚……」「本章讲解……」）
  B. 句首过渡连接词删除（此外，/因此，/也就是说，/值得注意的是）
  C. 判词替换（本质上 / 意味着什么 / 至关重要 / 不可或缺 / 影响深远）
  D. 正文中的解释性破折号 —— 】 → 逗号或句号（题名、表格占位、代码内不动）
"""
import os
import re
import sys

DOCS = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
SKIP = {'01-course-introduction'}

# A. 整句删除的元评论引导语（匹配到第一个 。或 ：为止）
META_RE = re.compile(
    r'(?P<sent>'
    r'下面(?:给出|用表格逐一说明|分[一二三四五六七八九十\d]+点说明|分四个场景讲清|简述)[^。：\n]{0,60}[。：]'
    r'|本章讲解[^。\n]{0,90}。'
    r'|本节(?:讲清楚|先讲)[^。\n]{0,90}。'
    r'|本页(?:给出|讲)[^。\n]{0,60}[。：]'
    r')'
)

# C. 判词（整词替换，需上下文判断的先只报告）
WORD_MAP = [
    ('，本质上都不是', '，都不是'),
    ('本质上都不是', '都不是'),
    ('本质上，', ''),
    ('本质上', ''),
    ('影响深远', '作用明显'),
]

# B. 句首连接词
CONN_RE = re.compile(r'(?m)(?<=[。！？\n])(此外|因此|也就是说|值得注意的是|不难发现|综上所述|总而言之|由此可见|换言之|换句话说)[，,]')

# D. 破折号
DASH_LINE_SKIP = re.compile(r'^\s*[|#>`:]')
JUDGE_BEFORE = ('是', '为', '在于', '就是', '核心', '区别')


def fix_dash(line):
    """把正文里的解释性破折号改成合适的标点。"""
    # 跳过破折号位于书名号内的行（真实论文题名）
    for m in re.finditer(r'——', line):
        seg_start = line.rfind('《', 0, m.start())
        seg_end = line.rfind('》', 0, m.start())
        if seg_start > seg_end:
            return line
    out = []
    i = 0
    while i < len(line):
        if line.startswith('——', i):
            # 破折号后紧跟加粗/引号列举，且前面是一个完整分句 → 用句号
            prev = line[max(0, i - 3):i]
            tail = line[i + 2:]
            if re.match(r'^(\*\*|“|\(|（)', tail) and re.search(r'[。；！]', line[:i]):
                out.append('。' if not line[:i].rstrip().endswith(('。', '；')) else '')
            elif any(prev.rstrip().endswith(w) for w in JUDGE_BEFORE):
                out.append('：')
            elif re.match(r'^[\u4e00-\u9fff]{2,4}（', tail) and '：' in line[:i]:
                out.append('：')
            else:
                out.append('，')
            i += 2
        else:
            out.append(line[i])
            i += 1
    s = ''.join(out)
    s = re.sub(r'，+', '，', s)
    s = re.sub(r'：(?=，)', '', s)
    s = re.sub(r'^，', '', s)
    return s


def in_code_mask(lines):
    mask = []
    inb = False
    for ln in lines:
        if ln.strip().startswith('```'):
            inb = not inb
            mask.append(False)
            continue
        mask.append(not inb)
    return mask


def process(path, apply_):
    raw = open(path, encoding='utf-8').read()
    fm_end = raw.find('\n---', 4)
    fm = raw[:fm_end + 4] if raw.startswith('---') else ''
    body = raw[len(fm):]
    changes = []

    # A 元评论
    for m in list(META_RE.finditer(body)):
        changes.append(('A-元评论', m.group('sent').strip()))
    if apply_:
        body = META_RE.sub('', body)

    # B 连接词
    for m in list(CONN_RE.finditer(body)):
        changes.append(('B-连接词', m.group(0).strip()))
    if apply_:
        body = CONN_RE.sub('', body)

    # C 判词
    for a, b in WORD_MAP:
        for m in re.finditer(re.escape(a), body):
            changes.append(('C-判词', a + '  ->  ' + (b if b else '(删)')))
    if apply_:
        for a, b in WORD_MAP:
            body = body.replace(a, b)

    # D 破折号
    lines = body.split('\n')
    mask = in_code_mask(lines)
    dash_hits = []
    for i, ln in enumerate(lines):
        if not mask[i] or '——' not in ln:
            continue
        if DASH_LINE_SKIP.match(ln):
            continue
        plain = re.sub(r'`[^`\n]*`', '', ln)
        if '——' not in plain:
            continue
        dash_hits.append((i, ln))
    for i, ln in dash_hits:
        changes.append(('D-破折号', ln.strip()[:120]))
    if apply_:
        for i, ln in dash_hits:
            lines[i] = fix_dash(ln)
        body = '\n'.join(lines)

    if apply_:
        open(path, 'w', encoding='utf-8', newline='').write(fm + body)
    return changes


def main():
    apply_ = len(sys.argv) > 1 and sys.argv[1] == 'apply'
    total = {}
    for sub in sorted(os.listdir(DOCS)):
        if sub in SKIP:
            continue
        d = os.path.join(DOCS, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md'):
                continue
            p = os.path.join(d, f)
            ch = process(p, apply_)
            if ch:
                print('\n##### %s/%s' % (sub, f))
                for kind, s in ch:
                    total[kind] = total.get(kind, 0) + 1
                    print('   [%s] %s' % (kind, s[:130]))
    print('\n=== 合计 ===')
    for k, v in sorted(total.items()):
        print('  %-12s %d' % (k, v))
    print('模式：%s' % ('已写入' if apply_ else 'DRY-RUN（未写入）'))


if __name__ == '__main__':
    main()
