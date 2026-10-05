# -*- coding: utf-8 -*-
"""去 AI 味第三批：Zotero 剩余三页的定点改写 + 断句检测。

用法：
    python fix_deai3.py          # 试运行
    python fix_deai3.py apply    # 写入
"""
import os
import re
import sys

ROOT = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
APPLY = len(sys.argv) > 1 and sys.argv[1] == 'apply'

FIXES = [
    # ---- metadata-and-reading.md ----
    ('06-zotero/metadata-and-reading.md', '\n\n\n\n## 6.6.2 右侧', '\n\n## 6.6.2 右侧'),
    ('06-zotero/metadata-and-reading.md', '为方便快速识别，', None),
    ('06-zotero/metadata-and-reading.md',
     '再次强调：**批注定位原文，笔记形成你自己的理解。**',
     '**批注定位原文，笔记形成你自己的理解。**'),
    ('06-zotero/metadata-and-reading.md',
     '校完一遍不代表万事大吉，交稿前做一次反向抽查：',
     '校完一遍之后，交稿前再做一次反向抽查：'),
    ('06-zotero/metadata-and-reading.md',
     '本节课请完成以下可检查产出：', '完成以下可检查产出：'),

    # ---- citation-and-bibliography.md ----
    ('06-zotero/citation-and-bibliography.md', '一个真实翻车案例：', '一个实际发生的例子：'),
    ('06-zotero/citation-and-bibliography.md', '按下面步骤重装：', '重装步骤如下：'),
    ('06-zotero/citation-and-bibliography.md',
     '三到五篇足够，再多反而显得没有重点。', '三到五篇足够，再多会让句子失去重点。'),
    ('06-zotero/citation-and-bibliography.md',
     '自动生成省事，但几个细节若不注意仍会露怯，逐一说明：',
     '自动生成省事，但几个细节不注意仍会出错：'),
    ('06-zotero/citation-and-bibliography.md', '光看规则不够直观，', None),
    ('06-zotero/citation-and-bibliography.md',
     '不要用“待补”占位符蒙混', '不要用“待补”占位符代替引用'),
    ('06-zotero/citation-and-bibliography.md',
     '规范引用既是格式要求，也是诚信底线', '规范引用是格式要求，也是诚信底线'),

    # ---- backup-and-workflow.md ----
    ('06-zotero/backup-and-workflow.md',
     '回顾 6.5.10 的预告，这里把两种模式彻底讲清：', '两种模式的差别在文件放在哪：'),
    ('06-zotero/backup-and-workflow.md',
     '**同步解决“多设备可用”，备份解决“误删 / 损坏可恢复”**，二者互补，缺一不可。',
     '**同步解决“多设备可用”，备份解决“误删 / 损坏可恢复”**，两者作用不同，都要有。'),
    ('06-zotero/backup-and-workflow.md',
     '本质就是文件同步受额度或设置影响', '原因是文件同步受额度或设置影响'),
    ('06-zotero/backup-and-workflow.md',
     '遇到冲突提示不要慌，按提示选择保留哪一侧。',
     '遇到冲突提示时，按提示选择保留哪一侧。'),
    ('06-zotero/backup-and-workflow.md',
     '再次强调：真正检索靠题录字段，文件名只是辅助识别，不必为命名过度纠结。',
     '真正检索靠题录字段，文件名只是辅助识别，不必为命名纠结。'),
    ('06-zotero/backup-and-workflow.md',
     '所以直接复制整个文件夹即可。', '所以直接复制整个文件夹即可。'),
    ('06-zotero/backup-and-workflow.md',
     '这也是为什么“复制整个文件夹”是最省心的备份法。', '所以直接复制整个文件夹即可。'),
    ('06-zotero/backup-and-workflow.md', '基本万无一失', '基本够用'),
    ('06-zotero/backup-and-workflow.md',
     '避免把私人文文献误传进群组。', '避免把私人文献误传进群组。'),
    ('06-zotero/backup-and-workflow.md',
     '把前面 6.5–6.8 串起来，一篇毕业论文的文献管理标准流程如下，建议贴在电脑旁：',
     '一篇毕业论文的文献管理标准流程如下，建议贴在电脑旁：'),
    ('06-zotero/backup-and-workflow.md',
     '归档后把整个数据目录复制到移动硬盘和网盘各一份，毕业后换电脑也能直接用。', None),
    ('06-zotero/backup-and-workflow.md',
     '本节课建立可恢复的备份流程，提交以下可检查产出：', '完成以下可检查产出：'),
    ('06-zotero/backup-and-workflow.md',
     '用 6.5 的四项自查 + 本页备份，确认资料库处于“可随时换设备继续写、误删可恢复”的状态。',
     '用 6.5 的四项自查加这一页的备份流程，确认资料库达到“可随时换设备继续写、误删可恢复”的状态。'),
    ('06-zotero/backup-and-workflow.md',
     '若同步、备份或导入时遇到本页未覆盖的情况', '若同步、备份或导入时遇到这里没讲到的情况'),
    ('06-zotero/backup-and-workflow.md',
     '在网盘里就能直接定位。\n\n\n\n| 推荐命名', '在网盘里就能直接定位。\n\n| 推荐命名'),
    ('06-zotero/backup-and-workflow.md',
     '## 6.8.11 多设备同步实战\n\n\n\n1. **在台式机**',
     '## 6.8.11 多设备同步实战\n\n1. **在台式机**'),
]


def do_fixes():
    ok = bad = 0
    for rel, old, new in FIXES:
        p = os.path.join(ROOT, rel.replace('/', os.sep))
        t = open(p, encoding='utf-8').read()
        n = t.count(old)
        if n == 0:
            print('  [未命中] %s :: %s' % (rel, old[:44]))
            bad += 1
            continue
        if new == old:
            print('  [无变化，跳过] %s :: %s' % (rel, old[:30]))
            continue
        if new is None:
            t2 = t.replace(old + '\n\n', '')
            if t2 == t:
                t2 = t.replace(old + '\n', '')
            if t2 == t:
                print('  [删除失败] %s :: %s' % (rel, old[:44]))
                bad += 1
                continue
            t = t2
        else:
            t = t.replace(old, new)
        if APPLY:
            open(p, 'w', encoding='utf-8', newline='').write(t)
        ok += 1
    print('第三批改写：成功 %d 处，未命中 %d 处' % (ok, bad))


def scan_dangling():
    """找出行尾是逗号 / 顿号的行——多为机械清扫残留的断句。"""
    print('=== 行尾断句检测 ===')
    hits = 0
    for sub in sorted(os.listdir(ROOT)):
        if sub == '01-course-introduction':
            continue
        d = os.path.join(ROOT, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md'):
                continue
            p = os.path.join(d, f)
            lines = open(p, encoding='utf-8').read().split('\n')
            incode = False
            for i, l in enumerate(lines, 1):
                if l.strip().startswith('```'):
                    incode = not incode
                    continue
                if incode:
                    continue
                s = l.rstrip()
                if s.endswith('，') or s.endswith('、'):
                    print('  %s/%s L%d  %s' % (sub, f, i, s[-40:]))
                    hits += 1
    print('共 %d 处' % hits)


if __name__ == '__main__':
    print('=== 试运行 ===' if not APPLY else '=== 写入 ===')
    do_fixes()
    scan_dangling()
