# -*- coding: utf-8 -*-
"""开题报告撰写部分配图生成脚本（概念示意图）。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa

ROOT = r"F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\public\images"
OUT = os.path.join(ROOT, "opening")

WM = "概念示意图（讲义配图）"

BAND_L = "#f4f8ff"
BAND_L_B = "#c9defb"
BAND_O = "#fff8ef"
BAND_O_B = "#f7d9a8"


def head(s, x, y, w, text, color=BLUE, size=13.5):
    s.rect(x, y, w, 30, fill=color, rx=8, op=0.12)
    s.text(x + 14, y + 20, text, size=size, fill=color, weight="700")
    return y + 30


def card(s, x, y, w, h, title, lines, color=BLUE, tsize=14.5, lh=26, lsize=12):
    s.rect(x, y, w, h, fill="#ffffff", stroke=BORDER2, rx=10)
    s.rect(x, y, w, 6, fill=color, rx=3)
    s.text(x + 18, y + 34, title, size=tsize, fill=color, weight="700")
    for i, ln in enumerate(lines):
        s.text(x + 18, y + 34 + lh * (i + 1) + 6, ln, size=lsize, fill=TXT2)
    return y + h


# ------------------------------------------------- o01 开题报告的七个部分
def o01():
    s = S(960, 700)

    # 上半段
    s.rect(60, 46, 840, 206, fill=BAND_L, stroke=BAND_L_B, rx=10)
    s.text(82, 74, "上半段 · 为什么研究（由背景推到缺口）", size=13, fill=BLUE, weight="700")
    for i, t in enumerate(("一、选题的背景与意义", "二、国内外研究现状、发展动态")):
        y = 92 + i * 62
        s.rect(310, y, 340, 44, fill="#ffffff", stroke=BAND_L_B, rx=8)
        s.text(480, y + 28, t, size=13.5, fill=TXT, anchor="middle", weight="500")
        if i == 0:
            s.arrow(480, y + 44, 480, y + 60, color=BAND_L_B, sw=2)

    s.arrow(480, 198, 480, 268, color=ORANGE, sw=2)

    # 缺口
    s.rect(60, 270, 840, 56, fill=ORANGE_L, stroke=ORANGE_B, rx=10)
    s.text(480, 304, "研究缺口：已有研究的不足与研究价值所在",
           size=14, fill="#b45309", anchor="middle", weight="700")

    s.arrow(480, 326, 480, 342, color=ORANGE, sw=2)

    # 下半段
    s.rect(60, 344, 840, 300, fill=BAND_O, stroke=BAND_O_B, rx=10)
    s.text(82, 372, "下半段 · 怎么研究（由内容到方法与保障）", size=13, fill=ORANGE, weight="700")
    for i, t in enumerate(("三、研究的内容及可行性分析",
                           "四、拟解决的关键问题及难点",
                           "五、研究方法与技术路线")):
        y = 386 + i * 58
        s.rect(310, y, 340, 44, fill="#ffffff", stroke=BAND_O_B, rx=8)
        s.text(480, y + 28, t, size=13.5, fill=TXT, anchor="middle", weight="500")
        if i < 2:
            s.arrow(480, y + 44, 480, y + 56, color=BAND_O_B, sw=2)

    s.arrow(480, 546, 480, 558, color=ORANGE, sw=2)
    s.line(316, 558, 644, 558, stroke=ORANGE, sw=2)
    s.arrow(316, 558, 316, 566, color=ORANGE, sw=2)
    s.arrow(644, 558, 644, 566, color=ORANGE, sw=2)
    for x, t in ((186, "六、研究的总体安排与进度"), (456, "七、主要参考文献")):
        s.rect(x, 568, 260, 44, fill="#ffffff", stroke=BAND_O_B, rx=8)
        s.text(x + 130, 596, t, size=12.5, fill=TXT, anchor="middle")

    s.watermark(WM)
    return save(s, os.path.join(OUT, "o01-framework.svg"))


# ------------------------------------------------- o02 研究背景的三个维度
def o02():
    s = S(960, 500)
    s.text(480, 42, "研究背景的三个维度：国家有政策、社会有需要、学界有需求",
           size=14, fill=TXT, anchor="middle", weight="700")

    cards = [
        (56, BLUE, "Ⅰ", "国家政策", ["相关改革与制度变化", "呈现政策演变脉络", "适当引用，不堆砌口号"]),
        (350, ORANGE, "Ⅱ", "社会需要", ["当下突出的现实问题", "谁受到影响", "用数据与材料支撑"]),
        (644, PURPLE, "Ⅲ", "学界需求", ["研究尚不充分之处", "已有结论的分歧", "由此引出研究缺口"]),
    ]
    for x, c, idx, t, lines in cards:
        s.rect(x, 74, 260, 152, fill="#ffffff", stroke=BORDER2, rx=10)
        s.rect(x, 74, 260, 6, fill=c, rx=3)
        s.circle(x + 34, 114, 15, fill=c, op=0.14)
        s.text(x + 34, 118.5, idx, size=12, fill=c, anchor="middle", weight="700")
        s.text(x + 58, 119, t, size=15, fill=c, weight="700")
        for i, ln in enumerate(lines):
            s.circle(x + 24, 156 + i * 24, 2.4, fill=c)
            s.text(x + 36, 160 + i * 24, ln, size=11.5, fill=TXT2)

    for x in (186, 480, 774):
        s.arrow(x, 228, 480, 286, color=TXT4, sw=1.8)

    s.rect(300, 288, 360, 56, fill=BAND_L, stroke=BAND_L_B, rx=10)
    s.text(480, 322, "研究背景：三条线索汇入同一处", size=13.5, fill=BLUE,
           anchor="middle", weight="700")

    s.arrow(480, 344, 480, 374, color=ORANGE, sw=2)

    s.rect(280, 376, 400, 52, fill=ORANGE_L, stroke=ORANGE_B, rx=10)
    s.text(480, 408, "推导出本文最核心的研究内容", size=13.5, fill="#b45309",
           anchor="middle", weight="700")

    s.watermark(WM)
    return save(s, os.path.join(OUT, "o02-background-dimensions.svg"))


# ------------------------------------------------- o03 文献综述的专题划分
def o03():
    s = S(960, 470)

    # 左：X 对 Y 型
    s.rect(40, 40, 424, 316, fill="#ffffff", stroke=BORDER2, rx=10)
    s.rect(40, 40, 424, 52, fill=BLUE, rx=10, op=0.12)
    s.text(60, 74, "题目形如：X 对 Y 的影响", size=14, fill=BLUE, weight="700")
    items_l = [
        ("① 两头分：X 的经济后果 + Y 的影响因素", 24),
        ("② 加一节机制：把两头接起来", 24),
        ("③ 具体问题具体分析", 24),
        ("· 新范畴 → 先梳理定义与度量", 24),
        ("· 机理不同 → 专设影响机制一节", 24),
        ("· 属某支大类文献 → 先总括再收窄", 24),
        ("④ 上位概念切入：先抬后收", 24),
        ("⑤ 末节固定为文献评述", 24),
    ]
    y = 106
    for t, gap in items_l:
        c = TXT if t[0] in "①②③④⑤" else TXT2
        s.text(62, y, t, size=12.5, fill=c)
        y += gap

    # 右：问题 / 对策型
    s.rect(496, 40, 424, 316, fill="#ffffff", stroke=BORDER2, rx=10)
    s.rect(496, 40, 424, 52, fill=ORANGE, rx=10, op=0.14)
    s.text(516, 74, "题目形如：某问题 / 对策研究", size=14, fill=ORANGE, weight="700")
    items_r = [
        ("① 由大到小，逐层收缩", TXT),
        ("· 税收风险管理的相关研究", TXT2),
        ("· A 行业税收风险管理的相关研究", TXT2),
        ("· 增值税税收风险管理的相关研究", TXT2),
        ("② 或按研究视角切分", TXT),
        ("· 可行性研究　· 态度与动机研究", TXT2),
        ("· 效应研究", TXT2),
        ("③ 末节固定为文献评述", TXT),
    ]
    y = 106
    for t, c in items_r:
        s.text(518, y, t, size=12.5, fill=c)
        y += 31

    # 共同要求
    s.rect(40, 376, 880, 62, fill=YELLOW_L, stroke=YEL_B, rx=10)
    s.text(60, 402, "两条共同要求", size=13, fill="#8a6100", weight="700")
    s.text(60, 426, "① 题目里每加一个限定词，综述就多收缩一层；② 每个专题的结尾都要收束到同一个研究缺口。",
           size=12.5, fill="#8a6100")

    s.watermark(WM)
    return save(s, os.path.join(OUT, "o03-review-topics.svg"))


# ------------------------------------------------- o04 两类选题的章节框架
def o04():
    s = S(960, 560)
    s.text(480, 40, "正文以 5—6 章为宜（不含引言）", size=13,
           fill=TXT2, anchor="middle")

    emp = ["第一章　绪论", "第二章　概念界定与理论分析", "第三章　现状分析",
           "第四章　研究设计与数据来源", "第五章　实证结果与稳健性检验",
           "第六章　结论与对策建议"]
    nor = ["第一章　绪论", "第二章　概念界定与理论基础", "第三章　现状与问题",
           "第四章　原因或机制分析", "第五章　经验借鉴或可行性分析",
           "第六章　结论与对策建议"]

    # 标题
    s.rect(60, 56, 400, 38, fill=BLUE, rx=8, op=0.12)
    s.text(260, 81, "实证分析类", size=14.5, fill=BLUE, anchor="middle", weight="700")
    s.rect(500, 56, 400, 38, fill=ORANGE, rx=8, op=0.14)
    s.text(700, 81, "规范分析类", size=14.5, fill=ORANGE, anchor="middle", weight="700")

    for i in range(6):
        y = 106 + i * 62
        same = i in (0, 5)
        fe = "#f5f7fa" if same else "#eaf3ff"
        fn = "#f5f7fa" if same else "#fff6e8"
        s.rect(60, y, 400, 50, fill=fe, stroke=BORDER2, rx=8)
        s.rect(500, y, 400, 50, fill=fn, stroke=BORDER2, rx=8)
        s.text(80, y + 31, emp[i], size=12.5, fill=TXT)
        s.text(520, y + 31, nor[i], size=12.5, fill=TXT)

    s.rect(60, 480, 840, 56, fill=YELLOW_L, stroke=YEL_B, rx=10)
    s.text(80, 506, "灰色行＝两者相同（绪论与结论）", size=12, fill="#8a6100", weight="700")
    s.text(80, 526, "蓝色／橙色行＝中间章节随选题类型变通：实证重设计与检验，规范重理论与经验借鉴。",
           size=12, fill="#8a6100")

    s.watermark(WM)
    return save(s, os.path.join(OUT, "o04-chapter-structure.svg"))


# ------------------------------------------------- o05 技术路线
def o05():
    s = S(960, 540)
    s.text(60, 42, "阶段", size=13, fill=TXT2, weight="700")
    s.text(600, 42, "用到的数据与方法", size=13, fill=TXT2, weight="700")

    stages = [
        ("提出问题：研究背景与文献综述 → 研究缺口", "文献研究法、知网与 WoS 检索"),
        ("理论分析：理论框架与研究假设", "理论演绎法、波特假说等"),
        ("研究设计：变量定义、模型设定、数据来源", "变量表、双重差分模型"),
        ("数据整理：样本筛选、数据清洗", "CSMAR 数据库、Stata"),
        ("基准回归与检验：描述统计、回归、异质性", "平行趋势、安慰剂检验"),
        ("结论与建议：政策建议、研究局限", "归纳总结法"),
    ]
    for i, (t, m) in enumerate(stages):
        y = 60 + i * 76
        s.rect(56, y, 500, 50, fill="#ffffff", stroke=BAND_L_B, rx=8)
        s.circle(80, y + 25, 13, fill=BLUE, op=0.14)
        s.text(80, y + 30, str(i + 1), size=12, fill=BLUE, anchor="middle", weight="700")
        s.text(102, y + 30, t, size=12.5, fill=TXT)
        s.chip(600, y + 14, m, fill=BLUE_L, color=BLUE, size=11, h=22)
        if i < len(stages) - 1:
            s.arrow(306, y + 50, 306, y + 72, color=BAND_L_B, sw=2)

    s.watermark(WM)
    return save(s, os.path.join(OUT, "o05-roadmap.svg"))


if __name__ == "__main__":
    for f in (o01, o02, o03, o04, o05):
        print(f.__name__, "->", f())
