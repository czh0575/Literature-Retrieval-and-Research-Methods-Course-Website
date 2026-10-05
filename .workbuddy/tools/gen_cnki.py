# -*- coding: utf-8 -*-
"""知网（CNKI）检索部分界面示意图生成脚本。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa

ROOT = r"F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\public\images"
OUT = os.path.join(ROOT, "cnki")


def W934(s, x, y, rows, cols, widths, header=True, size=12, rh=27, head_fill=BAR2,
         head_color=TXT, align=None):
    """简易表格绘制。"""
    total = sum(widths)
    s.rect(x, y, total, rh * len(rows), fill="#ffffff", stroke=BORDER2, rx=6)
    for r, row in enumerate(rows):
        ry = y + r * rh
        if r == 0 and header:
            s.rect(x, ry, total, rh, fill=head_fill, rx=0)
        elif r % 2 == 0:
            s.rect(x, ry, total, rh, fill=GREY_L)
        cx = x
        for c, cell in enumerate(row):
            a = (align[c] if align and c < len(align) else "start")
            tx = cx + 10 if a == "start" else (cx + widths[c] / 2 if a == "center" else cx + widths[c] - 10)
            s.text(tx, ry + rh / 2 + size * 0.36, cell, size=size,
                   fill=head_color if (r == 0 and header) else TXT2,
                   weight="700" if (r == 0 and header) else "400", anchor=a)
            cx += widths[c]
        if r:
            s.line(x, ry, x + total, ry, stroke=BORDER2)
    return y + rh * len(rows)


# ---------------------------------------------------------------- c01 首页
def c01():
    s = S(960, 560)
    cx, cy, cw, ch = s.window(30, 24, 900, 510, title="中国知网", url="https://www.cnki.net/")
    s.sitebar(cx, cy, cw, 36, brand="CNKI 中国知网")
    nav = ["首页", "文献", "知识元", "引文", "期刊", "工具书", "学术会议", "专利", "更多"]
    nx = cx + 170
    for n in nav:
        s.text(nx, cy + 23, n, size=12.5, fill=TXT2)
        nx += tw(n, 12.5) + 22

    # 检索区
    top = cy + 36
    s.rect(cx, top, cw, 250, fill="#f7fafd")
    tabs = [("文献", True), ("知识元", False), ("引文", False)]
    tx = cx + 250
    for label, on in tabs:
        s.text(tx, top + 42, label, size=14, fill=BLUE if on else TXT2,
               weight="700" if on else "400")
        if on:
            s.rect(tx - 12, top + 52, tw(label, 14) + 24, 3, fill=BLUE, rx=1.5)
        tx += tw(label, 14) + 62

    s.rect(cx + 150, top + 74, 600, 46, fill="#ffffff", stroke=BLUE_B, rx=6)
    s.line(cx + 246, top + 82, cx + 246, top + 112, stroke=BORDER2)
    s.text(cx + 164, top + 103, "主题", size=13, fill=TXT2)
    s.caret(cx + 206, top + 98, 6)
    s.text(cx + 262, top + 103, "研发费用加计扣除  企业创新", size=13.5, fill=TXT)
    s.rect(cx + 600, top + 74, 150, 46, fill=BLUE, rx=6)
    s.text(cx + 675, top + 103, "检　索", size=14.5, fill="#ffffff", anchor="middle", weight="700")

    s.text(cx + 150, top + 148, "高级检索", size=12, fill=BLUE)
    s.text(cx + 214, top + 148, "专业检索", size=12, fill=BLUE)
    s.text(cx + 278, top + 148, "句子检索", size=12, fill=BLUE)
    s.text(cx + 350, top + 148, "检索历史", size=12, fill=TXT2)

    s.line(cx + 150, top + 168, cx + 750, top + 168, stroke=BORDER2)
    s.text(cx + 150, top + 192, "检索历史：", size=12, fill=TXT3)
    hx = cx + 226
    for h in ["税收优惠 企业创新", "加计扣除 研发投入", "税收营商环境"]:
        hx = s.chip(hx, top + 178, h, fill="#ffffff", color=TXT2, size=11) + 8
    s.rect(cx + 150, top + 214, 600, 22, fill="none")
    s.text(cx + 150, top + 228, "最近检索 3 条，点击可直接复现上一次检索条件", size=11, fill=TXT3)

    # 标注
    s.badge(cx + 128, top + 52, 1)
    s.badge(cx + 128, top + 97, 2)
    s.badge(cx + 770, top + 97, 3)
    s.badge(cx + 324, top + 148, 4)
    s.note(cx + 60, top + 258, 250,
           ["① 检索类型：文献 / 知识元 / 引文",
            "② 检索框：默认按“主题”检索",
            "③ 检索按钮：执行检索",
            "④ 高级检索：多条件组合入口"],
           title="界面要点", fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "c01-cnki-home.svg"))


# ------------------------------------------------- c02 检索结果页布局
def c02():
    s = S(990, 650)
    cx, cy, cw, ch = s.window(24, 20, 942, 580, title="检索结果", url="https://kns.cnki.net/kns8/defaultresult")
    s.rect(cx, cy, cw, 48, fill="#f7f9fb")
    s.line(cx, cy + 48, cx + cw, cy + 48, stroke=BORDER2)
    s.rect(cx + 14, cy + 9, 400, 30, fill="#ffffff", stroke=BORDER2, rx=4)
    s.text(cx + 26, cy + 29, "主题：研发费用加计扣除 AND 企业创新", size=12.5, fill=TXT)
    s.rect(cx + 424, cy + 9, 66, 30, fill=BLUE, rx=4)
    s.text(cx + 457, cy + 29, "检索", size=12.5, fill="#ffffff", anchor="middle")
    s.text(cx + 506, cy + 29, "高级检索", size=12, fill=BLUE)
    s.text(cx + 566, cy + 29, "检索历史", size=12, fill=TXT2)

    top = cy + 48
    s.text(cx + 16, top + 26, "找到 1,842 条结果", size=13.5, fill=TXT, weight="700")
    s.text(cx + 140, top + 26, "检索用时 0.081 秒", size=11.5, fill=TXT3)
    for i, (t, on) in enumerate([("相关度", True), ("发表时间", False), ("被引", False), ("下载", False)]):
        bx = cx + 250 + i * 74
        s.rect(bx, top + 11, 66, 24, fill=BLUE_L if on else "#ffffff",
               stroke=BLUE if on else BORDER2, rx=4)
        s.text(bx + 33, top + 27, t, size=11.5, fill=BLUE if on else TXT2, anchor="middle")
    s.text(cx + cw - 150, top + 26, "每页 20 条", size=11.5, fill=TXT2)
    s.check(cx + 16, top + 42, 13)
    s.text(cx + 36, top + 53, "全选", size=11.5, fill=TXT2)
    s.text(cx + 80, top + 53, "导出与分析", size=11.5, fill=BLUE)
    s.text(cx + 158, top + 53, "批量下载", size=11.5, fill=BLUE)
    s.line(cx, top + 64, cx + cw, top + 64, stroke=BORDER2)

    # 左侧分组筛选
    lw = 196
    s.rect(cx, top + 64, lw, ch - 64 - 48, fill="#fafbfd")
    s.line(cx + lw, top + 64, cx + lw, cy + ch, stroke=BORDER2)
    groups = [("来源类别", ["北大核心", "CSSCI", "AMI 综合评价", "CSCD", "SCI 来源期刊"]),
              ("学科", ["企业经济", "财政与税收", "宏观经济管理"]),
              ("发表年度", ["2024", "2023", "2022", "2021"]),
              ("文献类型", ["学术期刊", "学位论文", "会议论文"])]
    gy = top + 84
    for gi, (g, items) in enumerate(groups):
        s.text(cx + 14, gy, g, size=12, fill=TXT, weight="700")
        s.caret(cx + lw - 22, gy - 4, 5)
        gy += 10
        for it in items:
            s.check(cx + 16, gy + 3, 12, on=(gi == 0 and it in ("北大核心", "CSSCI")))
            s.text(cx + 36, gy + 13, it, size=11.5, fill=TXT2)
            gy += 22
        gy += 12
        if gi < 3:
            s.line(cx + 14, gy - 8, cx + lw - 14, gy - 8, stroke=BORDER2)

    # 右侧结果列表
    rx = cx + lw + 16
    rw = cw - lw - 32
    ry = top + 78
    papers = [
        ("研发费用加计扣除政策与企业创新投入——基于双重差分法的经验证据",
         "张伟, 李娜, 王强", "税务研究", "2023, (05): 12-20", "被引 34", "下载 2,105", ["北大核心", "CSSCI"]),
        ("税收优惠、融资约束与高新技术企业研发投入",
         "陈晓明", "财政研究", "2022, (11): 45-58", "被引 61", "下载 3,472", ["北大核心", "CSSCI"]),
        ("加计扣除比例调整对企业创新绩效的影响研究",
         "刘洋, 赵敏", "中央财经大学学报", "2024, (02): 33-46", "被引 8", "下载 912", ["北大核心"]),
    ]
    for i, (t, au, src, vol, c1, c2, tags) in enumerate(papers):
        s.rect(rx, ry, rw, 118, fill="#ffffff", stroke=BORDER2, rx=6)
        s.check(rx + 10, ry + 14, 13)
        s.text(rx + 34, ry + 25, t, size=13.5, fill=BLUE, weight="500")
        s.text(rx + 34, ry + 47, au, size=11.5, fill=TXT2)
        s.text(rx + 34, ry + 67, src + "，" + vol, size=11.5, fill=TXT2)
        tx = rx + 34
        for tg in tags:
            tx = s.tag(tx, ry + 78, tg, fill=ORANGE_L, color=ORANGE, size=10) + 6
        s.text(rx + rw - 200, ry + 92, c1 + "　" + c2, size=11, fill=TXT3)
        for k, ic in enumerate(["☆", "❝", "⤓"]):
            s.circle(rx + rw - 62 + k * 20, ry + 26, 9, fill="#ffffff", stroke=BORDER2)
            s.text(rx + rw - 62 + k * 20, ry + 30, ic, size=11, fill=TXT3, anchor="middle")
        ry += 128

    # 分页
    s.text(cx + cw / 2 - 60, cy + ch - 22, "1", size=11.5, fill="#ffffff", anchor="middle")
    s.rect(cx + cw / 2 - 74, cy + ch - 34, 28, 24, fill=BLUE, rx=4)
    for i, n in enumerate(["2", "3", "4", "…", "93"]):
        bx = cx + cw / 2 - 36 + i * 30
        s.rect(bx, cy + ch - 34, 26, 24, fill="#ffffff", stroke=BORDER2, rx=4)
        s.text(bx + 13, cy + ch - 18, n, size=11.5, fill=TXT2, anchor="middle")

    s.badge(cx + 310, cy + 24, 1)
    s.badge(cx + 8, top + 88, 2)
    s.badge(rx - 10, ry - 118 + 24, 3)
    s.badge(rx - 10, ry - 8 + 10, 4)
    s.badge(cx + cw / 2 - 8, cy + ch - 22, 7)
    s.note(cx + 620, cy + ch - 96, 330,
           ["① 检索区：修改检索式并复现",
            "② 排序方式：相关度 / 时间 / 被引 / 下载",
            "③ 左侧分组筛选：来源类别、学科、年度、类型",
            "④ 文献列表：题名、作者、来源、引证数据、核心标识",
            "⑤ 底部：分页浏览"],
           title="结果页七个区域", fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "c02-cnki-result-page.svg"))


# ------------------------------------------------- c03 高级检索
def c03():
    s = S(960, 520)
    cx, cy, cw, ch = s.window(30, 24, 900, 470, title="高级检索", url="https://kns.cnki.net/kns8/AdvSearch")
    s.rect(cx, cy, cw, 36, fill="#f7f9fb")
    s.line(cx, cy + 36, cx + cw, cy + 36, stroke=BORDER2)
    for i, t in enumerate(["高级检索", "专业检索", "作者发文检索", "句子检索", "一框式检索"]):
        s.text(cx + 22 + i * 104, cy + 24, t, size=13, fill=BLUE if i == 0 else TXT2,
               weight="700" if i == 0 else "400")
    s.rect(cx + 12, cy + 30, 78, 3, fill=BLUE, rx=1.5)

    top = cy + 50
    fields = ["主题", "篇名", "关键词", "摘要", "全文", "参考文献"]
    s.text(cx + 18, top + 18, "检索条件", size=12, fill=TXT3)
    s.rect(cx + 88, top + 4, 34, 22, fill="#ffffff", stroke=BORDER2, rx=4)
    s.text(cx + 105, top + 19, "×", size=12, fill=TXT3, anchor="middle")

    rows = [("AND", "主题", "研发费用加计扣除", True),
            ("AND", "主题", "企业创新", True),
            ("OR", "篇名", "加计扣除 政策 效果", True),
            ("AND", "来源类别", "北大核心 CSSCI 中文核心期刊要目", False)]
    ry = top + 36
    for i, (logic, fld, val, use) in enumerate(rows):
        s.rect(cx + 58, ry + 3, 54, 26, fill="#ffffff", stroke=BORDER2, rx=4)
        s.text(cx + 85, ry + 20, logic, size=12, fill=TXT2, anchor="middle")
        s.caret(cx + 104, ry + 15, 5)
        s.rect(cx + 120, ry + 3, 92, 26, fill="#ffffff", stroke=BORDER2, rx=4)
        s.text(cx + 132, ry + 20, fld, size=12, fill=TXT)
        s.caret(cx + 196, ry + 15, 5)
        s.rect(cx + 220, ry + 3, 420, 26, fill="#ffffff", stroke=BORDER2, rx=4)
        s.text(cx + 232, ry + 20, val, size=12, fill=TXT)
        s.text(cx + 660, ry + 20, "＋  －", size=13, fill=TXT3)
        ry += 36
    s.text(cx + 88, ry + 16, "＋ 添加检索行", size=12, fill=BLUE)

    # 限定区
    ty = ry + 36
    s.line(cx + 18, ty, cx + cw - 18, ty, stroke=BORDER2)
    s.text(cx + 18, ty + 24, "发表时间：", size=12, fill=TXT2)
    s.field(cx + 96, ty + 10, 76, 24, "2015-01-01", size=11.5)
    s.text(cx + 180, ty + 24, "—", size=12, fill=TXT3)
    s.field(cx + 194, ty + 10, 76, 24, "2026-12-31", size=11.5)
    s.caret(cx + 285, ty + 19, 5)
    s.text(cx + 320, ty + 24, "来源类别：", size=12, fill=TXT2)
    sx = cx + 400
    for it, on in [("北大核心", True), ("CSSCI", True), ("AMI 综合评价", True), ("CSCD", False), ("SCI", False)]:
        s.check(sx, ty + 13, 12, on=on)
        s.text(sx + 18, ty + 24, it, size=11.5, fill=TXT2)
        sx += tw(it, 11.5) + 44
    s.text(cx + 18, ty + 56, "文献类型：", size=12, fill=TXT2)
    sx = cx + 96
    for it, on in [("学术期刊", True), ("学位论文", False), ("会议论文", False), ("报纸", False)]:
        s.check(sx, ty + 45, 12, on=on)
        s.text(sx + 18, ty + 56, it, size=11.5, fill=TXT2)
        sx += tw(it, 11.5) + 44
    s.text(cx + 18, ty + 88, "支持基金：", size=12, fill=TXT2)
    s.field(cx + 96, ty + 74, 300, 24, "国家自然科学基金 / 国家社会科学基金", size=11.5, placeholder=True)

    s.rect(cx + 470, ty + 74, 100, 30, fill=BLUE, rx=5)
    s.text(cx + 520, ty + 94, "检　索", size=13.5, fill="#ffffff", anchor="middle", weight="700")
    s.rect(cx + 582, ty + 74, 100, 30, fill="#ffffff", stroke=BORDER, rx=5)
    s.text(cx + 632, ty + 94, "清除条件", size=12.5, fill=TXT2, anchor="middle")

    s.badge(cx + 105, top + 16, 1)
    s.badge(cx + 212, top + 16, 2)
    s.badge(cx + 712, top + 16, 3)
    s.badge(cx + 388, ty + 24, 4)
    s.badge(cx + 520, ty + 94, 5)
    s.note(cx + 18, cy + ch - 84, 862,
           ["① 多行检索框：每行一个概念，行数按概念块数量决定　② 字段下拉：主题 / 篇名 / 关键词 / 摘要 / 全文",
            "③ 行间逻辑关系：同一概念的不同说法之间用 OR，不同概念之间用 AND，排除用 NOT",
            "④ 来源类别与时间范围属于“限定条件”，建议第一轮不要加　⑤ 检索按钮执行检索"],
           title="高级检索面板的用法", fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "c03-cnki-advanced-search.svg"))


# ------------------------------------------------- c04 关键词金字塔
def c04():
    s = S(900, 500)
    s.text(30, 38, "关键词金字塔：五层结构", size=17, fill=TXT, weight="700")
    s.text(30, 62, "从一个论文题目出发，把“知道的东西”变成“能检索的词”", size=12.5, fill=TXT3)

    layers = [
        ("上位概念", "税收优惠 / 税收政策", "#e8f2ff", BLUE),
        ("核心概念", "研发费用加计扣除", "#d6e8ff", BLUE),
        ("同义表达", "加计扣除 / 加计扣除政策 / 研发加计扣除", "#dff3e6", GREEN),
        ("相关概念", "企业创新 / 研发投入 / 创新绩效 / 融资约束", "#fff2dc", ORANGE),
        ("英文对应词", "R&D tax credit / super deduction / innovation input", "#f2ecfd", PURPLE),
    ]
    y = 92
    hs = 46
    cx = 570
    for i, (name, words, bgc, fg) in enumerate(layers):
        w = 250 + i * 42 if i < 3 else 250 + 3 * 42
        x = cx - w / 2
        s.rect(x, y, w, hs, fill=bgc, rx=8)
        s.text(cx, y + 21, name, size=13, fill=fg, weight="700", anchor="middle")
        s.text(cx, y + 38, words, size=11.5, fill=TXT2, anchor="middle")
        # 左侧作用说明
        s.line(240, y + hs / 2, x - 14, y + hs / 2, stroke=TXT4, dash="3 3")
        role = ["扩大检索范围", "保证相关性", "发现不同表述", "补齐机制与研究视角", "换库检索的前提"][i]
        s.text(232, y + hs / 2 + 4, role, size=11.5, fill=TXT3, anchor="end")
        # 右侧编号
        s.badge(cx + w / 2 + 22, y + hs / 2, i + 1, r=10, size=11)
        y += hs + 12
        if i < len(layers) - 1:
            s.arrow(cx, y - 10, cx, y - 2, color=TXT4, sw=1.4)

    s.rect(30, y + 8, 840, 56, fill=YELLOW_L, stroke=YEL_B, rx=8)
    s.text(46, y + 30, "使用顺序：先用①②把范围框住，再用③④把文献找全，最后用⑤去外文库检索。", size=12.5, fill="#8a6100")
    s.text(46, y + 50, "每一层都要写进关键词表，并注明来源；来源不清楚的词不要放进正式检索式。", size=12, fill="#8a6100")
    s.watermark("概念示意图")
    return save(s, os.path.join(OUT, "c04-keyword-pyramid.svg"))


# ------------------------------------------------- c05 关键词表样例
def c05():
    s = S(940, 430)
    s.text(28, 36, "关键词表样例", size=17, fill=TXT, weight="700")
    s.text(28, 58, "论文题目：研发费用加计扣除对高新技术企业创新投入的影响", size=12.5, fill=TXT3)
    rows = [
        ["概念角色", "关键词", "来源或依据"],
        ["核心政策", "研发费用加计扣除；加计扣除；税收优惠", "论文题目；财税〔2015〕119 号文件"],
        ["研究对象", "高新技术企业；制造业企业；A 股上市公司", "题目；国家统计局行业分类"],
        ["结果变量", "创新投入；研发投入强度；专利申请数", "文献中反复出现的指标"],
        ["机制词", "融资约束；现金流；税负；税收负担", "理论类与综述类文献"],
        ["情境限定", "2015—2024 年；中国；制造业", "数据可得性与政策实施时间"],
        ["同义词（新发现）", "加计扣除比例；研发费用归集；创新绩效", "第一轮检索结果的标题与关键词栏"],
    ]
    W934(s, 28, 74, rows, 3, [130, 380, 374], rh=32)
    s.note(28, 312, 884,
           ["· 词表控制在 20 个词以内，能组合出 3 组检索式即可开始第一轮检索。",
            "· “来源或依据”一列不能空：写不出来源的词，说明你还没有在任何文献里见过它。",
            "· 第一轮检索结束后要把新发现的表达补回本表，词表是活的，不是一次写完。"],
           title="填表要求", fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark("表格示意图")
    return save(s, os.path.join(OUT, "c05-keyword-table.svg"))


# ------------------------------------------------- c06 结果条目
def c06():
    s = S(940, 380)
    s.text(28, 34, "一条检索结果上能读到的信息", size=16.5, fill=TXT, weight="700")
    s.rect(28, 52, 884, 210, fill="#ffffff", stroke=BORDER, rx=8)
    s.check(46, 70, 14)
    s.text(72, 82, "研发费用加计扣除政策与企业创新投入——基于双重差分法的经验证据",
           size=15, fill=BLUE, weight="500")
    s.text(72, 108, "张伟, 李娜, 王强", size=12, fill=TXT2)
    s.text(200, 108, "（浙江越秀外国语学院 国际商学院）", size=11.5, fill=TXT3)
    s.text(72, 130, "税务研究", size=12.5, fill=BLUE)
    s.text(133, 130, "，2023, (05): 12-20", size=12, fill=TXT2)
    tx = 72
    for tg, f, c in [("北大核心", ORANGE_L, ORANGE), ("CSSCI", ORANGE_L, ORANGE), ("AMI 核心", ORANGE_L, ORANGE)]:
        tx = s.tag(tx, 142, tg, fill=f, color=c, size=10.5) + 6
    s.text(72, 184, "被引 34　下载 2,105　参考文献 42 篇　基金：国家社会科学基金项目",
           size=11.5, fill=TXT2)
    s.text(72, 208, "摘要：本文以 2015 年研发费用加计扣除政策扩围为准自然实验，基于 A 股高新技术企业",
           size=11.5, fill=TXT3)
    s.text(72, 226, "面板数据，采用双重差分法检验政策对企业创新投入的影响及融资约束的中介机制……",
           size=11.5, fill=TXT3)
    for k, ic in enumerate(["☆", "❝", "⤓", "✦"]):
        s.circle(838 + 0, 74 + k * 26, 9, fill="#ffffff", stroke=BORDER2)
        s.text(838, 78 + k * 26, ic, size=11, fill=TXT3, anchor="middle")

    items = [
        ("①", 60, 76, "题名（蓝色可点击）", "判断研究主题与研究方法"),
        ("②", 60, 108, "作者与作者单位", "识别团队、是否同一单位有系列研究"),
        ("③", 60, 130, "来源期刊与年份卷期页码", "定位期刊层次、整理题录要用的字段"),
        ("④", 300, 142, "核心期刊标识", "一眼看出是否 CSSCI / 北大核心"),
        ("⑤", 60, 184, "被引、下载、参考文献数、基金", "辅助判断文献影响力与权威程度"),
        ("⑥", 60, 214, "摘要预览", "点开后快速判断是否与自己相关"),
        ("⑦", 860, 78, "收藏 / 引用 / 下载 / 分享按钮", "导出题录、下载全文的入口"),
    ]
    y = 288
    for i, (n, x, yy, t, use) in enumerate(items):
        col = i // 4
        row = i % 4
        bx = 28 + col * 452
        by = y + row * 24
        s.text(bx, by, n, size=12.5, fill=ORANGE, weight="700")
        s.text(bx + 22, by, t, size=12, fill=TXT, weight="500")
        s.text(bx + 220, by, "→ " + use, size=11.5, fill=TXT3)
    s.watermark()
    return save(s, os.path.join(OUT, "c06-result-item.svg"))


# ------------------------------------------------- c07 来源类别筛选
def c07():
    s = S(880, 600)
    s.text(28, 34, "在检索结果页按“来源类别”定位核心期刊", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "路径：检索结果页 → 左侧分组筛选 → 来源类别 → 勾选相应类别", size=12.5, fill=TXT3)

    s.rect(28, 74, 330, 480, fill="#fafbfd", stroke=BORDER, rx=8)
    s.text(46, 102, "分组筛选", size=13.5, fill=TXT, weight="700")
    s.line(44, 116, 342, 116, stroke=BORDER2)
    s.text(46, 138, "来源类别", size=12.5, fill=TXT, weight="700")
    s.caret(318, 134, 5)
    items = [("北大核心（中文核心期刊要目总览）", True),
             ("CSSCI（中文社会科学引文索引）", True),
             ("CSSCI 扩展版", False),
             ("CSCD（中国科学引文数据库）", False),
             ("AMI 综合评价（核心及以上）", True),
             ("SCI 来源期刊", False),
             ("EI 来源期刊", False)]
    y = 154
    for t, on in items:
        s.check(48, y, 12, on=on)
        s.text(70, y + 10, t, size=11, fill=TXT2)
        y += 22
    y += 6
    s.line(44, y, 342, y, stroke=BORDER2)
    s.text(46, y + 24, "学科", size=12.5, fill=TXT, weight="700")
    s.caret(318, y + 20, 5)
    for i, t in enumerate(["企业经济", "财政与税收", "宏观经济管理"]):
        s.check(48, y + 36 + i * 22, 12, False)
        s.text(70, y + 46 + i * 22, t, size=11, fill=TXT2)
    y3 = y + 36 + 3 * 22 + 24
    s.line(44, y3 - 22, 342, y3 - 22, stroke=BORDER2)
    s.text(46, y3 + 2, "文献类型", size=12.5, fill=TXT, weight="700")
    s.caret(318, y3 - 2, 5)
    for i, t in enumerate(["学术期刊", "学位论文", "会议论文"]):
        s.check(48, y3 + 16 + i * 22, 12, False)
        s.text(70, y3 + 26 + i * 22, t, size=11, fill=TXT2)

    rx = 380
    s.rect(rx, 74, 472, 480, fill="#ffffff", stroke=BORDER2, rx=8)
    s.text(rx + 18, 102, "筛选后的结果（示意）", size=13, fill=TXT, weight="700")
    s.text(rx + 18, 124, "结果数由 1,842 条降至 216 条", size=11.5, fill=ORANGE)
    yy = 140
    for i in range(6):
        s.line(rx + 18, yy, rx + 454, yy, stroke=BORDER2)
        s.text(rx + 18, yy + 22, "研发费用加计扣除与企业创新投入：基于" + ["双重差分", "断点回归", "倾向得分匹配",
                                                        "面板门槛", "工具变量", "动态GMM"][i] + "方法的证据",
               size=12, fill=BLUE)
        s.text(rx + 18, yy + 42, ["税务研究", "财政研究", "中央财经大学学报", "税收经济研究",
                                  "数量经济技术经济研究", "中国工业经济"][i] + "　2023, (05): 12-20",
               size=11, fill=TXT2)
        tx2 = rx + 18
        for tg, f, c in [("北大核心", ORANGE_L, ORANGE), ("CSSCI", ORANGE_L, ORANGE)]:
            tx2 = s.tag(tx2, yy + 50, tg, fill=f, color=c, size=9.5, h=15) + 5
        yy += 66

    s.badge(346, 140, 1)
    s.badge(360, 102, 2)
    s.watermark()
    return save(s, os.path.join(OUT, "c07-source-filter.svg"))


# ------------------------------------------------- c08 期刊导航
def c08():
    s = S(940, 460)
    s.text(28, 34, "期刊导航：按学科浏览并核实期刊", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "路径：知网首页 → 期刊 → 期刊导航 → 选择学科或输入刊名", size=12.5, fill=TXT3)
    s.rect(28, 74, 884, 48, fill="#ffffff", stroke=BORDER, rx=8)
    s.field(46, 86, 420, 26, "输入刊名、ISSN 或主办单位，例如：税务研究", size=12, placeholder=True)
    s.rect(478, 86, 84, 26, fill=BLUE, rx=4)
    s.text(520, 103, "检索", size=12, fill="#ffffff", anchor="middle")
    s.text(586, 103, "学科分类浏览：经济与管理科学 ▾", size=12, fill=BLUE)
    s.text(800, 103, "核心期刊标识 ▾", size=12, fill=BLUE)

    head = ["期刊名称", "主办单位", "收录标识", "复合影响因子", "发文量（近 5 年）"]
    rows = [head]
    data = [("税务研究", "中国税务杂志社", "北大核心 / CSSCI / AMI 核心", "较高", "▇▇▇▇▇"),
            ("国际税收", "中国税务杂志社", "北大核心 / CSSCI 扩展", "中等", "▇▇▇▇"),
            ("财政研究", "中国财政学会", "北大核心 / CSSCI / AMI 权威", "较高", "▇▇▇▇"),
            ("税收经济研究", "国家税务总局税务干部学院", "北大核心", "中等", "▇▇▇"),
            ("中央财经大学学报", "中央财经大学", "北大核心 / CSSCI", "较高", "▇▇▇▇"),
            ("地方财政研究", "辽宁省财政科学研究所", "北大核心 / CSSCI 扩展", "中等", "▇▇▇")]
    rows.extend(data)
    W934(s, 28, 136, rows, 5, [170, 230, 230, 114, 140], rh=34)
    s.note(28, 380, 884,
           ["· 收录标识与影响因子以知网期刊导航或学校图书馆公布的最新信息为准，本图仅为界面位置示意。",
            "· 影响因子只反映期刊整体被引情况，不能用来评价某一篇论文的质量。",
            "· 核实期刊时重点看三件事：收录体系、学科类目、近三年是否还在发同方向的文章。"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "c08-journal-nav.svg"))


# ------------------------------------------------- c09 摘要展开
def c09():
    s = S(940, 470)
    s.text(28, 34, "展开摘要：判断“要不要读全文”的关键一步", size=16.5, fill=TXT, weight="700")
    s.rect(28, 52, 884, 300, fill="#ffffff", stroke=BORDER, rx=8)
    s.check(48, 70, 14)
    s.text(74, 82, "税收优惠、融资约束与高新技术企业研发投入", size=15, fill=BLUE, weight="500")
    s.text(74, 106, "陈晓明", size=12, fill=TXT2)
    s.text(134, 106, "财政研究，2022, (11): 45-58", size=12, fill=TXT2)
    s.line(48, 122, 892, 122, stroke=BORDER2)
    s.text(48, 146, "摘要", size=12.5, fill=TXT, weight="700")
    s.para(104, 146, [
        "本文以 2015 年研发费用加计扣除政策扩围为准自然实验，选取 2012—2020 年 A 股上市",
        "公司为样本，采用双重差分模型检验税收优惠对企业研发投入的影响，并检验融资约束的中介",
        "作用。研究发现：加计扣除政策显著提高了处理组企业的研发投入强度，且这一效应在融资约束",
        "较强的中小企业中更为明显；机制检验表明，政策通过缓解融资约束提升了企业研发意愿。",
    ], size=12, fill=TXT2)
    s.text(48, 232, "关键词", size=12.5, fill=TXT, weight="700")
    kx = 104
    for k in ["研发费用加计扣除", "融资约束", "企业创新", "双重差分"]:
        kx = s.chip(kx, 218, k, fill=BLUE_L, color=BLUE, size=11, h=20, pad=8) + 8
    s.line(48, 252, 892, 252, stroke=BORDER2)
    s.text(48, 276, "引证信息：被引 61　下载 3,472　参考文献 45　共引文献 128　同被引文献 96",
           size=11.5, fill=TXT2)
    s.text(48, 300, "相似文献 / 相关文献 / 读者推荐：点开可沿主题继续扩展",
           size=11.5, fill=BLUE)
    s.text(48, 326, "基金：国家社会科学基金一般项目（编号略）", size=11.5, fill=TXT3)

    s.badge(16, 146, 1)
    s.badge(16, 228, 2)
    s.badge(16, 276, 3)
    s.badge(16, 300, 4)
    s.note(28, 366, 884,
           ["① 摘要：先看结论句，再回看数据与方法　② 关键词：与自己的词表逐词对照，命中越多越相关",
            "③ 引证信息：被引与下载反映影响，参考文献数量反映文献的综述厚度　④ 相似文献：不必换关键词也能继续扩展"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "c09-cnki-abstract-expanded.svg"))


# ------------------------------------------------- c10 导出题录
def c10():
    s = S(940, 500)
    s.rect(0, 0, 940, 500, fill="#5b6470", op=0.35)
    s.rect(120, 40, 700, 420, fill="#ffffff", stroke=BORDER, rx=10)
    s.rect(120, 40, 700, 46, fill=BAR, rx=10)
    s.rect(120, 74, 700, 12, fill=BAR)
    s.text(146, 69, "导出文献", size=14, fill=TXT, weight="700")
    s.text(796, 69, "✕", size=14, fill=TXT3, anchor="middle")
    s.line(120, 86, 820, 86, stroke=BORDER)

    s.text(146, 116, "已选文献 10 条", size=12, fill=TXT2)
    s.text(146, 140, "导出格式", size=12.5, fill=TXT, weight="700")
    fmts = [("GB/T 7714-2015 参考文献格式", "格式化文本，用于手工核对或直接粘贴", True),
            ("EndNote", "机器格式，可导入 EndNote / Zotero", True),
            ("RefWorks", "机器格式，可导入 RefWorks", False),
            ("NoteExpress", "机器格式，可导入 NoteExpress", False),
            ("NoteFirst", "机器格式，可导入 NoteFirst", False),
            ("自定义", "字段可选，用于特殊情况", False),
            ("查新（引文格式）", "用于开题与查新报告", False)]
    y = 152
    for t, d, on in fmts:
        s.rect(146, y, 300, 36, fill=BLUE_L if on else "#ffffff",
               stroke=BLUE if on else BORDER2, rx=5)
        s.radio(164, y + 18, 6, on=on)
        s.text(182, y + 16, t, size=12, fill=TXT, weight="500")
        s.text(182, y + 30, d, size=10.5, fill=TXT3)
        y += 42

    s.rect(470, 140, 320, 240, fill="#fafbfd", stroke=BORDER2, rx=8)
    s.text(486, 162, "已选文献（示意）", size=12, fill=TXT, weight="700")
    for i in range(6):
        s.check(488, 174 + i * 32, 12, on=True)
        s.text(508, 185 + i * 32, "研发费用加计扣除" + ["政策与", "", "与企业", "对", "与", "影响"][i] + "企业创新" + ["投入", "效率", "研发", "创新产出", "绩效", "机制"][i],
               size=11.5, fill=TXT2)
        s.text(508, 199 + i * 32, "税务研究　2023, (05)", size=10.5, fill=TXT3)
    s.rect(470, 392, 130, 30, fill=BLUE, rx=5)
    s.text(535, 412, "导　出", size=13, fill="#ffffff", anchor="middle", weight="700")
    s.rect(612, 392, 100, 30, fill="#ffffff", stroke=BORDER, rx=5)
    s.text(662, 412, "取　消", size=12.5, fill=TXT2, anchor="middle")
    s.note(146, 452, 640, [], title="", fill="none", stroke="none")
    s.text(146, 452 - 8, "对照说明：给 Zotero 用的是机器格式（EndNote / RefWorks 等）；GB/T 7714 文本只用于核对与粘贴。",
           size=11.5, fill=ORANGE)
    s.badge(130, 140, 1)
    s.badge(454, 162, 2)
    s.badge(454, 407, 3)
    s.watermark()
    return save(s, os.path.join(OUT, "c10-export-dialog.svg"))


# ------------------------------------------------- c11 可视化分析
def c11():
    s = S(940, 470)
    s.text(28, 34, "可视化分析：把一组文献看成一幅地图", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "路径：检索结果页 → 可视化分析 → 关键词共现网络 / 文献互引网络 / 年度趋势", size=12.5, fill=TXT3)

    s.rect(28, 74, 560, 300, fill="#ffffff", stroke=BORDER2, rx=8)
    s.text(46, 100, "关键词共现网络（示意）", size=12.5, fill=TXT, weight="700")
    nodes = [("研发费用加计扣除", 300, 210, 46, BLUE),
             ("企业创新", 430, 150, 36, GREEN),
             ("融资约束", 180, 160, 30, ORANGE),
             ("税收优惠", 250, 120, 34, BLUE),
             ("创新绩效", 430, 260, 28, GREEN),
             ("中小企业", 170, 260, 26, PURPLE),
             ("税负", 350, 300, 24, ORANGE),
             ("高新技术企业", 330, 90, 30, BLUE)]
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 4), (2, 5), (3, 7), (1, 7)]
    for a, b in edges:
        s.line(nodes[a][1], nodes[a][2], nodes[b][1], nodes[b][2], stroke=BORDER, sw=1.4)
    for name, nx, ny, r, c in nodes:
        s.circle(nx, ny, r, fill=c, op=0.16)
        s.circle(nx, ny, r, fill="none", stroke=c, sw=1.4)
        s.text(nx, ny + 4, name, size=10.5, fill=c, anchor="middle", weight="500")

    s.rect(608, 74, 304, 300, fill="#ffffff", stroke=BORDER2, rx=8)
    s.text(626, 100, "发表年度趋势（示意）", size=12.5, fill=TXT, weight="700")
    base = 330
    s.line(640, base, 890, base, stroke=BORDER)
    s.line(640, base, 640, 130, stroke=BORDER)
    vals = [18, 26, 34, 42, 58, 76, 92, 118, 146]
    bw = 20
    for i, v in enumerate(vals):
        x = 654 + i * 26
        h = (v / 160.0) * 180
        s.rect(x, base - h, bw, h, fill=BLUE if i < 8 else ORANGE, rx=3, op=0.85)
    for i, yr in enumerate(["17", "18", "19", "20", "21", "22", "23", "24", "25"]):
        s.text(664 + i * 26, base + 16, yr, size=9.5, fill=TXT3, anchor="middle")
    s.text(626, 350, "近三年发文量持续上升，说明该选题仍在升温", size=11.5, fill=ORANGE)

    s.note(28, 388, 884,
           ["· 共现网络：节点越大表示该关键词在文献中出现越多；连线越粗表示两个概念同时出现的次数越多。",
            "· 读图只回答两个问题：领域的主流概念是什么？还有哪些概念与自己相关却不在词表里？",
            "· 年度趋势用来说明选题的时效性，可作为开题报告中“研究必要性”的依据之一。"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark("界面位置与网络结构为示意")
    return save(s, os.path.join(OUT, "c11-visual-analysis.svg"))


# ------------------------------------------------- c12 三轮检索
def c12():
    s = S(940, 480)
    s.text(28, 36, "三轮检索法：从“发现词”到“锁定证据”", size=17, fill=TXT, weight="700")
    s.text(28, 58, "同一组关键词，分三轮逐步收敛，每轮只改一类条件", size=12.5, fill=TXT3)
    rounds = [
        ("第一轮", "发现词", BLUE, BLUE_L,
         ["字段：主题", "关键词：只放核心词 1—2 个", "限定：不加任何条件",
          "排序：被引量从高到低", "产出：新出现的同义表达", "结果量：数百至数千条"]),
        ("第二轮", "提高相关性", GREEN, GREEN_L,
         ["字段：主题 + 篇名组合", "关键词：核心词 + 同义词（OR）", "限定：只加时间范围",
          "排序：相关度", "产出：20—40 条候选文献", "结果量：数十至数百条"]),
        ("第三轮", "锁定证据", ORANGE, ORANGE_L,
         ["字段：篇名 / 关键词", "关键词：概念块之间用 AND", "限定：来源类别 + 学科 + 文献类型",
          "排序：被引 + 时间对照看", "产出：10—20 篇核心文献集", "结果量：数条至数十条"]),
    ]
    x = 28
    for i, (tag, name, c, cl, lines) in enumerate(rounds):
        s.rect(x, 84, 280, 300, fill="#ffffff", stroke=BORDER2, rx=10)
        s.rect(x, 84, 280, 52, fill=cl, rx=10)
        s.rect(x, 122, 280, 14, fill=cl)
        s.text(x + 20, 116, tag, size=17, fill=c, weight="700")
        s.text(x + 100, 116, name, size=15, fill=c, weight="700")
        y = 168
        for ln in lines:
            s.circle(x + 24, y - 4, 2.6, fill=c)
            s.text(x + 38, y, ln, size=11.5, fill=TXT2)
            y += 30
        if i < 2:
            s.arrow(x + 288, 234, x + 330, 234, color=TXT4, sw=2)
        x += 340
    s.note(28, 400, 884,
           ["· 每一轮结束都要把新发现的词补进关键词表，并记下结果数与保留数。",
            "· 如果第一轮就没有结果，说明关键词用错了表述，应改成上位概念再试一次。",
            "· 三轮的记录合起来就是检索日志，可以直接用于开题报告的文献来源说明。"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark("概念示意图")
    return save(s, os.path.join(OUT, "c12-three-rounds.svg"))


# ------------------------------------------------- c13 摘要解剖
def c13():
    s = S(940, 480)
    s.text(28, 36, "摘要的五要素：把一段话拆成五类信息", size=17, fill=TXT, weight="700")
    s.text(28, 58, "读摘要的目标不是“读懂”，而是“判断它能不能用在我的哪一部分”", size=12.5, fill=TXT3)

    s.rect(28, 80, 884, 176, fill="#ffffff", stroke=BORDER, rx=8)
    lines = [
        ("本文以 2015 年研发费用加计扣除政策扩围为准自然实验，", 0),
        ("选取 2012—2020 年 A 股上市公司为样本，采用双重差分模型检验税收优惠对企业研发投入的影响，", 1),
        ("并检验融资约束的中介作用。研究发现：加计扣除政策显著提高了处理组企业的研发投入强度，", 2),
        ("且这一效应在中小企业中更为明显；政策通过缓解融资约束提升企业研发意愿。", 3),
        ("研究结论对完善研发费用加计扣除政策具有参考意义。", 4),
    ]
    cols = [BLUE, BLUE, GREEN, ORANGE, PURPLE]
    names = ["研究问题 / 情境", "数据与样本", "研究方法", "主要结论", "政策含义"]
    y = 112
    for txt, k in lines:
        s.rect(48, y - 16, 520, 26, fill=cols[k], op=0.09, rx=4)
        s.rect(48, y - 16, 4, 26, fill=cols[k], rx=2)
        s.text(62, y + 2, txt, size=12, fill=TXT)
        s.line(578, y - 3, 596, y - 3, stroke=cols[k], sw=1.4)
        s.text(604, y + 2, names[k], size=11.5, fill=cols[k], weight="700")
        y += 30

    s.rect(28, 268, 884, 56, fill=YELLOW_L, stroke=YEL_B, rx=8)
    s.text(48, 292, "读完摘要要能立刻回答三个问题：它研究的是不是我的研究对象？它的结论能支撑我的哪个论点？",
           size=12, fill="#8a6100")
    s.text(48, 312, "如果三个问题有两个答不上来，就不必下载全文，只需留下题录备查。", size=12, fill="#8a6100")

    rows = [["摘要里的信息", "提取后填到哪里", "典型判断"],
            ["研究问题 / 情境", "文献综述的“研究背景”段落", "与我选题在同一政策背景下 → 背景相关"],
            ["数据与样本", "研究设计部分的样本说明", "样本年份、行业与我一致 → 可作对照"],
            ["研究方法", "研究方法部分的可行性依据", "方法我学得会 → 收入方法库"],
            ["主要结论", "文献综述的“已有研究结论”", "结论与我预期一致或相反 → 需重点讨论"],
            ["政策含义", "对策建议部分的依据", "可直接引申到我的政策建议 → 有价值"]]
    W934(s, 28, 340, rows, 3, [170, 330, 384], rh=24)
    s.watermark("概念示意图")
    return save(s, os.path.join(OUT, "c13-cnki-abstract-anatomy.svg"))


if __name__ == "__main__":
    for f in (c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13):
        print(f.__name__, "->", f())
