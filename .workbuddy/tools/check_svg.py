# -*- coding: utf-8 -*-
"""校验生成的 SVG：XML 合法性 + 文本是否越界。"""
import os
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import tw

ROOT = r"F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\public\images"

bad = 0
for sub in ("cnki", "foreign", "zotero", "opening"):
    d = os.path.join(ROOT, sub)
    if not os.path.isdir(d):
        print("MISSING DIR", d)
        continue
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"):
            continue
        p = os.path.join(d, fn)
        try:
            tree = ET.parse(p)
        except Exception as e:
            print("[XMLERR] %s/%s -> %s" % (sub, fn, e))
            bad += 1
            continue
        root = tree.getroot()
        W = float(root.get("width"))
        H = float(root.get("height"))
        issues = []
        for t in root.iter("{http://www.w3.org/2000/svg}text"):
            s = t.text or ""
            size = float(t.get("font-size", 12))
            x = float(t.get("x", 0))
            y = float(t.get("y", 0))
            anchor = t.get("text-anchor", "start")
            w = tw(s, size)
            if anchor == "middle":
                x0, x1 = x - w / 2, x + w / 2
            elif anchor == "end":
                x0, x1 = x - w, x
            else:
                x0, x1 = x, x + w
            if x1 > W - 2 or x0 < 1:
                issues.append("text out of box x=[%.0f,%.0f] W=%.0f : %s" % (x0, x1, W, s[:28]))
            if y > H - 2 or y < 9:
                issues.append("text out of box y=%.0f H=%.0f : %s" % (y, H, s[:28]))
        if issues:
            bad += 1
            print("[OVERFLOW] %s/%s" % (sub, fn))
            for i in issues[:6]:
                print("    " + i)

print("\n检查完成，问题文件数:", bad)
