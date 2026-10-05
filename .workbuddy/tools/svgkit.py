# -*- coding: utf-8 -*-
"""课程讲义界面示意图生成工具库（SVG）。

用途：为 docs/course 下「文献搜集方法」与「Zotero 文献管理」两部分讲义
绘制与真实界面布局一致的矢量示意图（SVG），输出到 docs/public/images/。
"""
import os

FONT = "'Microsoft YaHei','PingFang SC','Hiragino Sans GB','Segoe UI',Arial,sans-serif"

# 基础色板
BG       = "#eef1f5"   # 画布底色
WIN      = "#ffffff"   # 窗口底色
BAR      = "#f1f3f6"   # 工具条底色
BAR2     = "#e9edf2"
BORDER   = "#d7dce3"
BORDER2  = "#e8ecf1"
TXT      = "#1f2329"
TXT2     = "#5b6470"
TXT3     = "#98a1ab"
TXT4     = "#c3c9d1"
BLUE     = "#1677ff"
BLUE_L   = "#e8f2ff"
BLUE_B   = "#b6d4fb"
ORANGE   = "#fa8c16"
ORANGE_L = "#fff6e8"
ORANGE_B = "#ffd591"
GREEN    = "#16a34a"
GREEN_L  = "#eaf7ee"
RED      = "#d93a3a"
RED_L    = "#fdecec"
PURPLE   = "#7c3aed"
PURPLE_L = "#f2ecfd"
YELLOW_L = "#fffbe6"
YEL_B    = "#ffe58f"
GREY_L   = "#f5f7fa"
INK_D    = "#0f172a"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def tw(s, size):
    """粗略估算文本宽度（CJK 按 1.0em，其余按 0.56em）。"""
    w = 0.0
    for ch in str(s):
        w += size * (1.0 if ord(ch) > 0x2E7F else 0.56)
    return w


class S:
    """一张 SVG 画布。"""

    def __init__(self, w, h, bg=BG):
        self.w = w
        self.h = h
        self.o = ['<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (w, h, bg)]

    # ---------- 基础图元 ----------
    def add(self, s):
        self.o.append(s)
        return self

    def rect(self, x, y, w, h, fill="none", stroke=None, rx=0, sw=1, dash=None, op=None):
        a = '<rect x="%s" y="%s" width="%s" height="%s" fill="%s"' % (x, y, w, h, fill)
        if rx:
            a += ' rx="%s"' % rx
        if stroke:
            a += ' stroke="%s" stroke-width="%s"' % (stroke, sw)
        if dash:
            a += ' stroke-dasharray="%s"' % dash
        if op is not None:
            a += ' opacity="%s"' % op
        return self.add(a + "/>")

    def circle(self, cx, cy, r, fill="none", stroke=None, sw=1, op=None):
        a = '<circle cx="%s" cy="%s" r="%s" fill="%s"' % (cx, cy, r, fill)
        if stroke:
            a += ' stroke="%s" stroke-width="%s"' % (stroke, sw)
        if op is not None:
            a += ' opacity="%s"' % op
        return self.add(a + "/>")

    def ell(self, cx, cy, rx, ry, fill="none", stroke=None, sw=1):
        a = '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s"' % (cx, cy, rx, ry, fill)
        if stroke:
            a += ' stroke="%s" stroke-width="%s"' % (stroke, sw)
        return self.add(a + "/>")

    def line(self, x1, y1, x2, y2, stroke=BORDER2, sw=1, dash=None, op=None):
        a = '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"' % (
            x1, y1, x2, y2, stroke, sw)
        if dash:
            a += ' stroke-dasharray="%s"' % dash
        if op is not None:
            a += ' opacity="%s"' % op
        return self.add(a + "/>")

    def path(self, d, fill="none", stroke=None, sw=1, dash=None, cap="round"):
        a = '<path d="%s" fill="%s"' % (d, fill)
        if stroke:
            a += ' stroke="%s" stroke-width="%s" stroke-linecap="%s"' % (stroke, sw, cap)
        if dash:
            a += ' stroke-dasharray="%s"' % dash
        return self.add(a + "/>")

    def text(self, x, y, s, size=13, fill=TXT, weight="400", anchor="start", op=None, spacing=None):
        a = ('<text x="%s" y="%s" font-size="%s" fill="%s" font-weight="%s" text-anchor="%s"'
             % (x, y, size, fill, weight, anchor))
        if op is not None:
            a += ' opacity="%s"' % op
        if spacing is not None:
            a += ' letter-spacing="%s"' % spacing
        return self.add(a + ">" + esc(s) + "</text>")

    def para(self, x, y, lines, size=12.5, fill=TXT2, lh=None, weight="400"):
        lh = lh or size + 7
        for i, ln in enumerate(lines):
            self.text(x, y + i * lh, ln, size=size, fill=fill, weight=weight)
        return self

    # ---------- 组合图元 ----------
    def badge(self, cx, cy, n, r=11, fill=ORANGE, size=12):
        self.circle(cx, cy, r, fill=fill)
        self.text(cx, cy + size * 0.36, str(n), size=size, fill="#ffffff",
                  weight="700", anchor="middle")
        return self

    def arrow(self, x1, y1, x2, y2, color=ORANGE, sw=2, dash=None):
        import math
        self.line(x1, y1, x2, y2, stroke=color, sw=sw, dash=dash)
        ang = math.atan2(y2 - y1, x2 - x1)
        L, W = 9, 4.6
        p1 = (x2, y2)
        p2 = (x2 - L * math.cos(ang) + W * math.sin(ang), y2 - L * math.sin(ang) - W * math.cos(ang))
        p3 = (x2 - L * math.cos(ang) - W * math.sin(ang), y2 - L * math.sin(ang) + W * math.cos(ang))
        self.path("M %.1f %.1f L %.1f %.1f L %.1f %.1f Z" % (p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]),
                  fill=color)
        return self

    def button(self, x, y, w, h, label, fill=BLUE, color="#ffffff", size=12, rx=4,
               stroke=None, weight="500", icon=None):
        self.rect(x, y, w, h, fill=fill, rx=rx, stroke=stroke, sw=1)
        tx = x + w / 2 + (6 if icon else 0)
        if label:
            self.text(tx, y + h / 2 + size * 0.36, label, size=size, fill=color,
                      weight=weight, anchor="middle")
        if icon:
            self.circle(x + 12, y + h / 2, 5, fill="none", stroke=color, sw=1.4)
        return self

    def field(self, x, y, w, h, text="", size=12.5, rx=4, fill="#ffffff", stroke=BORDER,
              placeholder=False, pad=9):
        self.rect(x, y, w, h, fill=fill, stroke=stroke, rx=rx)
        if text:
            self.text(x + pad, y + h / 2 + size * 0.36, text, size=size,
                      fill=TXT3 if placeholder else TXT)
        return self

    def caret(self, x, y, size=7, color=TXT3, w=1.6):
        self.path("M %s %s l %s %s l %s %s" % (x, y, size, size, size, -size),
                  stroke=color, sw=w)
        return self

    def check(self, x, y, s=13, on=True, color=BLUE):
        self.rect(x, y, s, s, fill=BLUE if on else "#ffffff",
                  stroke=BLUE if on else BORDER, rx=2.5)
        if on:
            self.path("M %.1f %.1f l %.1f %.1f l %.1f %.1f"
                      % (x + s * 0.25, y + s * 0.52, s * 0.22, s * 0.24, s * 0.34, -s * 0.42),
                      stroke="#ffffff", sw=1.8)
        return self

    def radio(self, cx, cy, r=6, on=True, color=BLUE):
        self.circle(cx, cy, r, fill="#ffffff", stroke=color if on else BORDER, sw=1.4)
        if on:
            self.circle(cx, cy, r * 0.48, fill=color)
        return self

    def tag(self, x, y, label, fill=ORANGE_L, color=ORANGE, size=10.5, h=17, rx=3, pad=6,
            stroke=None):
        w = tw(label, size) + pad * 2
        self.rect(x, y, w, h, fill=fill, rx=rx, stroke=stroke, sw=1)
        self.text(x + w / 2, y + h / 2 + size * 0.36, label, size=size, fill=color,
                  anchor="middle", weight="500")
        return x + w

    def chip(self, x, y, label, fill=BLUE_L, color=BLUE, size=11, h=22, rx=11, pad=10):
        w = tw(label, size) + pad * 2
        self.rect(x, y, w, h, fill=fill, rx=rx)
        self.text(x + w / 2, y + h / 2 + size * 0.36, label, size=size, fill=color,
                  anchor="middle")
        return x + w

    def note(self, x, y, w, lines, title=None, fill=YELLOW_L, stroke=YEL_B,
             tcolor="#8a6100", size=12, pad=12, lh=19, rx=8):
        h = pad * 2 + len(lines) * lh + (lh if title else 0)
        self.rect(x, y, w, h, fill=fill, stroke=stroke, rx=rx, sw=1)
        cy = y + pad + size
        if title:
            self.text(x + pad, cy, title, size=size + 0.5, fill=tcolor, weight="700")
            cy += lh
        for ln in lines:
            self.text(x + pad, cy, ln, size=size, fill=tcolor)
            cy += lh
        return h

    # ---------- 窗口外壳 ----------
    def window(self, x, y, w, h, title="", url=None, app=False, rx=9, shadow=True):
        """绘制窗口外壳，返回内容区 (x, y, w, h)。"""
        if shadow:
            self.rect(x + 2, y + 4, w, h, fill="#cbd3dd", rx=rx, op=0.55)
        self.rect(x, y, w, h, fill=WIN, stroke=BORDER, rx=rx)
        if app:
            self.rect(x, y, w, 38, fill=BAR, rx=rx)
            self.rect(x, y + 28, w, 10, fill=BAR)
            for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")):
                self.circle(x + 16 + i * 15, y + 19, 5, fill=c)
            self.text(x + w / 2, y + 23.5, title, size=12, fill=TXT2, anchor="middle")
            self.line(x, y + 38, x + w, y + 38, stroke=BORDER)
            return (x, y + 38, w, h - 38)
        # 浏览器窗口
        bh = 62
        self.rect(x, y, w, 26, fill=BAR, rx=rx)
        self.rect(x, y + 16, w, 20, fill=BAR)
        # 标签页
        self.rect(x + 12, y + 6, 190, 24, fill="#ffffff", rx=6)
        self.text(x + 24, y + 22, title[:22], size=11.5, fill=TXT2)
        for i in range(3):
            self.circle(x + 176 + i * 0, y + 18, 4, fill="none")
        self.rect(x + 210, y + 12, 22, 14, fill="none", stroke=TXT3, rx=2)
        # 地址栏
        self.rect(x + 12, y + 36, w - 24, 20, fill="#ffffff", stroke=BORDER2, rx=10)
        self.rect(x + 22, y + 42, 8, 8, fill="none", stroke=GREEN, rx=2, sw=1.2)
        self.text(x + 38, y + 50, url or "", size=11, fill=TXT2)
        self.rect(x + w - 60, y + 38, 14, 14, fill="none")
        self.line(x, y + bh, x + w, y + bh, stroke=BORDER)
        return (x, y + bh, w, h - bh)

    def toolstrip(self, x, y, w, h=30, fill=BAR2):
        self.rect(x, y, w, h, fill=fill)
        self.line(x, y + h, x + w, y + h, stroke=BORDER)
        return self

    def sitebar(self, x, y, w, h=34, fill="#f7f9fb", brand="", brand_color=BLUE):
        self.rect(x, y, w, h, fill=fill)
        self.line(x, y + h, x + w, y + h, stroke=BORDER2)
        if brand:
            self.rect(x + 16, y + 8, 4, 18, fill=brand_color, rx=2)
            self.text(x + 28, y + 22, brand, size=14, fill=brand_color, weight="700")
        return self

    def watermark(self, label="界面示意图（按真实布局重绘）"):
        self.text(self.w - 12, self.h - 9, label, size=9.5, fill=TXT4, anchor="end")
        return self

    def out(self):
        head = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
                'viewBox="0 0 %d %d" font-family="%s">'
                % (self.w, self.h, self.w, self.h, FONT))
        return head + "".join(self.o) + "</svg>"


def save(s, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s.out())
    return path
