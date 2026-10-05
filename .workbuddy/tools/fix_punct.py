# -*- coding: utf-8 -*-
"""统一新讲义的标点：把正文中作为中文引号使用的 ASCII 双引号换成中文引号，
并修正两处笔误。代码块与行内代码内的引号保持不变。
"""
import io
import os
import re

DOCS = r"F:\02教学\教学课程\文献检索与研究方法\课件\web\docs"
TARGETS = [
    "course/05-cnki-retrieval", "course/05-foreign-retrieval", "course/06-zotero",
    "course/07-opening-report",
]

FIXES = [
    ("6.3 装的转换器 + 茉莉花", "6.3 装的连接器 + 茉莉花"),
    ("大量文献请用语连接器批量勾选", "大量文献请用连接器批量勾选"),
]


def convert(text):
    chunks = []
    i = 0
    for m in re.finditer(r"(```.*?```)", text, re.S):
        chunks.append(("t", text[i:m.start()]))
        chunks.append(("c", m.group(1)))
        i = m.end()
    chunks.append(("t", text[i:]))

    res, n = [], 0
    for kind, seg in chunks:
        if kind == "c":
            res.append(seg)
            continue
        j = 0
        subs = []
        for m in re.finditer(r"(`[^`\n]*`)", seg):
            subs.append(("t", seg[j:m.start()]))
            subs.append(("c", m.group(1)))
            j = m.end()
        subs.append(("t", seg[j:]))
        for k, s2 in subs:
            if k == "c":
                res.append(s2)
                continue
            cnt = s2.count('"')
            n += cnt
            parts = s2.split('"')
            buf = []
            for idx, p in enumerate(parts):
                buf.append(p)
                if idx < len(parts) - 1:
                    buf.append("\u201c" if idx % 2 == 0 else "\u201d")
            res.append("".join(buf))
    return "".join(res), n


total = 0
odd = []
for sub in TARGETS:
    for dirpath, _dirnames, filenames in os.walk(os.path.join(DOCS, sub)):
        rel = os.path.relpath(dirpath, DOCS).replace("\\", "/")
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            with io.open(p, encoding="utf-8") as f:
                src = f.read()
            for a, b in FIXES:
                src = src.replace(a, b)
            new, cnt = convert(src)
            with io.open(p, "w", encoding="utf-8") as f:
                f.write(new)
            total += cnt
            left = new.count('"')
            flag = "  <-- 引号未配对，需人工检查" if left % 2 else ""
            if left:
                odd.append((rel, fn, left))
            print("%-46s 转换 %3d 处，剩余 %d%s" % (rel + "/" + fn, cnt, left, flag))

print("\n合计转换 %d 处" % total)
if odd:
    print("仍有直引号的文件：")
    for s, f, c in odd:
        print("  %s/%s 剩余 %d" % (s, f, c))
