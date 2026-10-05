# -*- coding: utf-8 -*-
"""批量修正示意图脚本中的画布尺寸与个别排版问题。"""
import io
import os

BASE = os.path.dirname(os.path.abspath(__file__))

PATCH = {
    "gen_foreign.py": [
        ("def f02():\n    s = S(960, 520)", "def f02():\n    s = S(960, 600)"),
        ("def f03():\n    s = S(990, 600)", "def f03():\n    s = S(990, 725)"),
        ("def f05():\n    s = S(960, 560)", "def f05():\n    s = S(960, 592)"),
        ("def f06():\n    s = S(960, 470)", "def f06():\n    s = S(960, 522)"),
        ("def f07():\n    s = S(990, 600)", "def f07():\n    s = S(990, 672)"),
        ("def f09():\n    s = S(940, 500)", "def f09():\n    s = S(940, 548)"),
        ("def f10():\n    s = S(940, 470)", "def f10():\n    s = S(940, 548)"),
        ("def f11():\n    s = S(980, 560)", "def f11():\n    s = S(980, 600)"),
        ("def f12():\n    s = S(940, 480)", "def f12():\n    s = S(940, 572)"),
        ('    s.text(cx + cw - 240, top + 62, "Sort by:  Relevance  |  Date  |  Citations", size=11.5, fill=TXT2)',
         '    s.text(cx + cw - 16, top + 62, "Sort by:  Relevance  |  Date  |  Citations", size=11.5,\n           fill=TXT2, anchor="end")'),
    ],
    "gen_zotero.py": [
        ("    return cx, yy, cw, cy + h - yy", "    return cx, yy, cw, (cy + h - 38) - yy"),
        ("def z06():\n    s = S(960, 540)", "def z06():\n    s = S(960, 626)"),
        ("def z11():\n    s = S(940, 480)", "def z11():\n    s = S(940, 562)"),
        ("def z15():\n    s = S(960, 470)", "def z15():\n    s = S(960, 506)"),
        ('    s.note(cx + 150, cy + 420, 620,', '    s.note(cx + 150, cy + 428, 620,'),
    ],
}

for fn, pairs in PATCH.items():
    p = os.path.join(BASE, fn)
    with io.open(p, encoding="utf-8") as f:
        src = f.read()
    for old, new in pairs:
        n = src.count(old)
        if n != 1:
            print("[WARN] %s : %d 次匹配 -> %s" % (fn, n, old[:60].replace("\n", "\\n")))
            continue
        src = src.replace(old, new)
        print("[OK]   %s : %s" % (fn, old[:60].replace("\n", "\\n")))
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(src)
print("补丁执行完毕")
