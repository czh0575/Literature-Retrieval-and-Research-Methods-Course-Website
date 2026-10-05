# -*- coding: utf-8 -*-
"""检查剩余 ASCII 引号是否都位于代码块或行内代码中（递归扫描指定目录）。"""
import os
import re

DOCS = r"F:\02教学\教学课程\文献检索与研究方法\课件\web\docs"
SUBS = ["course/05-cnki-retrieval", "course/05-foreign-retrieval", "course/06-zotero",
        "course/07-opening-report"]
bad = 0
for sub in SUBS:
    for dirpath, _dirnames, filenames in os.walk(os.path.join(DOCS, sub)):
        rel = os.path.relpath(dirpath, DOCS).replace("\\", "/")
        for f in sorted(filenames):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dirpath, f)
            t = open(p, encoding="utf-8").read()
            if '"' not in t:
                continue
            print("=== %s/%s" % (rel, f))
            inblock = False
            for i, line in enumerate(t.split("\n"), 1):
                if line.strip().startswith("```"):
                    inblock = not inblock
                    continue
                if '"' not in line:
                    continue
                if inblock:
                    kind = "代码块  "
                elif re.search(r"`[^`]*\"[^`]*`", line):
                    kind = "行内代码"
                else:
                    kind = "正文！！"
                    bad += 1
                print("   %s L%-4d %s" % (kind, i, line.strip()[:88]))
print("\n正文中剩余 ASCII 引号的行数：%d" % bad)
