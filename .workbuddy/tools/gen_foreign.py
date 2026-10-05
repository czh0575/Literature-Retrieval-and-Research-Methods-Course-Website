# -*- coding: utf-8 -*-
"""外文文献检索部分（ScienceDirect / Web of Science / JCR / Google Scholar）示意图生成脚本。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa

ROOT = r"F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\public\images"
OUT = os.path.join(ROOT, "foreign")

SD = "#eb6a00"      # ScienceDirect 品牌橙
SD_L = "#fff2e6"
WOS = "#4b3a8f"     # Clarivate 系品牌紫
WOS_L = "#efecf9"
GS = "#4285f4"


def table(s, x, y, rows, widths, rh=28, size=11.5, head_fill=BAR2, head_color=TXT):
    total = sum(widths)
    s.rect(x, y, total, rh * len(rows), fill="#ffffff", stroke=BORDER2, rx=6)
    for r, row in enumerate(rows):
        ry = y + r * rh
        if r == 0:
            s.rect(x, ry, total, rh, fill=head_fill)
        elif r % 2 == 0:
            s.rect(x, ry, total, rh, fill=GREY_L)
        cxp = x
        for c, cell in enumerate(row):
            s.text(cxp + 10, ry + rh / 2 + size * 0.36, cell, size=size,
                   fill=head_color if r == 0 else TXT2,
                   weight="700" if r == 0 else "400")
            cxp += widths[c]
        if r:
            s.line(x, ry, x + total, ry, stroke=BORDER2)
    return y + rh * len(rows)


# ------------------------------------------------------- f01 SD 首页
def f01():
    s = S(960, 500)
    cx, cy, cw, ch = s.window(30, 24, 900, 450, title="ScienceDirect",
                              url="https://www.sciencedirect.com/")
    s.sitebar(cx, cy, cw, 38, brand="ScienceDirect", brand_color=SD)
    for i, t in enumerate(["Journals & Books", "Help", "Search", "My account", "Sign in"]):
        s.text(cx + 300 + i * 118, cy + 24, t, size=12, fill=TXT2)

    top = cy + 38
    s.rect(cx, top, cw, 6, fill=SD)
    s.text(cx + 40, top + 74, "Search for peer-reviewed journal articles and book chapters",
           size=15, fill=TXT, weight="700")
    s.field(cx + 40, top + 92, 640, 40, "R&D tax credit innovation", size=14)
    s.rect(cx + 686, top + 92, 110, 40, fill=SD, rx=5)
    s.text(cx + 741, top + 118, "Search", size=14, fill="#ffffff", anchor="middle", weight="700")
    s.text(cx + 40, top + 152, "Advanced search", size=12.5, fill=BLUE)
    s.text(cx + 168, top + 152, "Browse journals and books", size=12.5, fill=BLUE)

    s.line(cx + 40, top + 172, cx + 860, top + 172, stroke=BORDER2)
    s.text(cx + 40, top + 200, "Browse by subject", size=14, fill=TXT, weight="700")
    subs = ["Accounting, Finance", "Business, Management", "Economics, Econometrics",
            "Social Sciences", "Law", "Energy"]
    x = cx + 40
    for i, t in enumerate(subs):
        col = i % 3
        row = i // 3
        bx = cx + 40 + col * 276
        by = top + 216 + row * 44
        s.rect(bx, by, 260, 34, fill=SD_L, rx=6)
        s.text(bx + 14, by + 22, t, size=11.5, fill="#8a4200")

    s.badge(cx + 24, top + 112, 1)
    s.badge(cx + 670, top + 112, 2)
    s.badge(cx + 24, top + 152, 3)
    s.note(cx + 40, top + 306, 820,
           ["① 检索框：输入英文关键词，支持 \" \" 精确短语与 AND / OR / NOT　② Search 按钮执行检索",
            "③ Advanced search：进入高级检索面板，可按字段、期刊、时间限定"],
           title="首页三处入口", fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "f01-sd-home.svg"))


# ------------------------------------------------------- f02 SD 高级检索
def f02():
    s = S(960, 600)
    cx, cy, cw, ch = s.window(30, 24, 900, 470, title="Advanced search",
                              url="https://www.sciencedirect.com/search")
    s.sitebar(cx, cy, cw, 34, brand="ScienceDirect", brand_color=SD)
    top = cy + 34
    s.text(cx + 18, top + 30, "Advanced search", size=16, fill=TXT, weight="700")
    s.line(cx + 18, top + 42, cx + cw - 18, top + 42, stroke=BORDER2)

    s.text(cx + 18, top + 70, "Find articles with these terms", size=12.5, fill=TXT, weight="700")
    s.field(cx + 18, top + 80, 620, 30, "\"R&D tax credit\" AND innovat*", size=12.5)
    s.text(cx + 18, top + 130, "In this journal or book title", size=12.5, fill=TXT2)
    s.field(cx + 18, top + 140, 620, 28, "", size=12.5, placeholder=True)
    s.text(cx + 18, top + 188, "Author(s)", size=12.5, fill=TXT2)
    s.field(cx + 18, top + 198, 300, 28, "", size=12.5, placeholder=True)
    s.text(cx + 336, top + 188, "Author affiliation", size=12.5, fill=TXT2)
    s.field(cx + 336, top + 198, 302, 28, "", size=12.5, placeholder=True)
    s.text(cx + 18, top + 246, "Title, abstract or author-specified keywords", size=12.5, fill=TXT2)
    s.field(cx + 336, top + 236, 302, 28, "R&D tax credit", size=12.5)
    s.text(cx + 18, top + 296, "Years", size=12.5, fill=TXT2)
    s.field(cx + 100, top + 284, 90, 28, "2015", size=12.5)
    s.text(cx + 200, top + 302, "to", size=12, fill=TXT3)
    s.field(cx + 226, top + 284, 90, 28, "2026", size=12.5)
    s.field(cx + 336, top + 284, 302, 28, "Article type: Review articles ▾", size=12.5)

    s.rect(cx + 18, top + 334, 110, 32, fill=SD, rx=5)
    s.text(cx + 73, top + 355, "Search", size=13.5, fill="#ffffff", anchor="middle", weight="700")
    s.rect(cx + 140, top + 334, 130, 32, fill="#ffffff", stroke=BORDER, rx=5)
    s.text(cx + 205, top + 355, "Clear form", size=12.5, fill=TXT2, anchor="middle")
    s.text(cx + 300, top + 355, "Show more options ▾", size=12.5, fill=BLUE)

    s.badge(cx + 660, top + 95, 1)
    s.badge(cx + 660, top + 154, 2)
    s.badge(cx + 660, top + 212, 3)
    s.badge(cx + 660, top + 251, 4)
    s.badge(cx + 660, top + 299, 5)
    s.note(cx + 18, top + 378, 864,
           ["① 主检索框：多个概念用 AND 连接，同义词用 OR 并用括号括起　② 按期刊限定：知道自己要投/要引哪本刊时使用",
            "③ 作者与作者单位：追踪某位学者或某个研究机构　④ 字段限定：Title, abstract or author-specified keywords 相当于知网的“主题”",
            "⑤ 时间范围与文献类型：先不加，结果太多时再加"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "f02-sd-advanced-search.svg"))


# ------------------------------------------------------- f03 SD 结果页
def f03():
    s = S(990, 725)
    cx, cy, cw, ch = s.window(24, 20, 942, 560, title="Search results",
                              url="https://www.sciencedirect.com/search?qs=R%26D+tax+credit")
    s.sitebar(cx, cy, cw, 32, brand="ScienceDirect", brand_color=SD)
    top = cy + 32
    s.rect(cx, top, cw, 40, fill="#f7f9fb")
    s.line(cx, top + 40, cx + cw, top + 40, stroke=BORDER2)
    s.text(cx + 16, top + 26, "R&D tax credit AND innovat*", size=12.5, fill=TXT)
    s.text(cx + 300, top + 26, "Refine by", size=12, fill=TXT2)
    s.text(cx + 400, top + 26, "Advanced search", size=12, fill=BLUE)

    s.text(cx + 16, top + 66, "1,247 results", size=14, fill=TXT, weight="700")
    s.text(cx + 130, top + 66, "Set search alert", size=11.5, fill=BLUE)
    s.text(cx + cw - 210, top + 66, "Sort by:  Relevance  |  Date", size=11.5, fill=TXT2)

    lw = 250
    s.rect(cx, top + 80, lw, ch - 80, fill="#fafbfd")
    s.line(cx + lw, top + 80, cx + lw, cy + ch, stroke=BORDER2)
    gy = top + 104
    groups = [("Year", ["2026 (86)", "2025 (203)", "2024 (245)", "2023 (198)"]),
              ("Article type", ["Review articles (112)", "Research articles (1,081)",
                                "Book chapters (54)"]),
              ("Publication title", ["Journal of Public Economics", "Energy Economics",
                                     "Research Policy"]),
              ("Subject areas", ["Economics and Econometrics", "Business and Management",
                                 "Finance"])]
    for g, items in groups:
        s.text(cx + 14, gy, g, size=12, fill=TXT, weight="700")
        s.caret(cx + lw - 22, gy - 4, 5)
        gy += 12
        for it in items:
            s.check(cx + 16, gy, 12, on=False)
            s.text(cx + 34, gy + 11, it, size=11, fill=TXT2)
            gy += 21
        gy += 14
        s.line(cx + 14, gy - 10, cx + lw - 14, gy - 10, stroke=BORDER2)

    rx = cx + lw + 18
    rw = cw - lw - 36
    ry = top + 92
    papers = [
        ("R&D tax credits and firm innovation: Evidence from a quasi-natural experiment",
         "J. Smith, L. Wang, M. Rossi", "Research Policy", "2024, 53(3): 104-126",
         ["Research article"], "Cited by 42", True),
        ("Do R&D tax incentives crowd out private R&D investment? A review",
         "A. Martinez, K. Tanaka", "Journal of Economic Surveys", "2023, 37(1): 12-48",
         ["Review article"], "Cited by 118", False),
        ("Innovation responses to tax credits: Firm-level evidence",
         "P. Dubois, H. Chen", "Journal of Public Economics", "2025, 231: 105-131",
         ["Research article"], "Cited by 9", True),
    ]
    for i, (t, au, jn, vol, tags, cited, pdf) in enumerate(papers):
        s.rect(rx, ry, rw, 126, fill="#ffffff", stroke=BORDER2, rx=6)
        s.text(rx + 12, ry + 24, t, size=13, fill=BLUE, weight="500")
        s.text(rx + 12, ry + 46, au, size=11.5, fill=TXT2)
        s.text(rx + 12, ry + 66, jn + "，" + vol, size=11.5, fill=TXT2)
        tx = rx + 12
        for tg in tags:
            tx = s.tag(tx, ry + 76, tg, fill=WOS_L, color=WOS, size=10) + 6
        if pdf:
            s.tag(tx, ry + 76, "Open access", fill=GREEN_L, color=GREEN, size=10)
        s.text(rx + 12, ry + 112, cited, size=11, fill=TXT3)
        s.rect(rx + rw - 96, ry + 98, 84, 22, fill="#ffffff", stroke=BORDER, rx=4)
        s.text(rx + rw - 54, ry + 113, "Download PDF", size=10, fill=TXT2, anchor="middle")
        s.text(rx + rw - 40, ry + 24, "Export ▾", size=11, fill=TXT2)
        ry += 136

    s.badge(cx + 8, top + 66, 1)
    s.badge(rx - 12, ry - 136 + 24, 2)
    s.badge(rx - 12, ry - 136 + 86, 3)
    s.badge(cx + 8, top + 104, 4)
    s.badge(rx - 12, ry - 26 + 112, 5)
    s.note(cx + 560, cy + ch - 74, 358,
           ["① 结果数 ② 文献题名（作者、期刊、卷期）",
            "③ 文献类型标签：Review article / Open access",
            "④ 左侧 Refine by：年份、类型、期刊、学科",
            "⑤ Download PDF 与 Export 入口"],
           title="结果页要点", fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "f03-sd-results.svg"))


# ------------------------------------------------------- f04 SD 条目
def f04():
    s = S(940, 420)
    s.text(28, 34, "一条结果条目上能读到的信息", size=16.5, fill=TXT, weight="700")
    s.rect(28, 52, 884, 172, fill="#ffffff", stroke=BORDER, rx=8)
    s.text(48, 84, "R&D tax credits and firm innovation: Evidence from a quasi-natural experiment",
           size=14.5, fill=BLUE, weight="500")
    s.text(48, 110, "J. Smith, L. Wang, M. Rossi", size=12, fill=TXT2)
    s.text(48, 132, "Research Policy", size=12.5, fill=BLUE)
    s.text(160, 132, "，Volume 53, Issue 3, April 2024, Pages 104-126", size=12, fill=TXT2)
    tx = 48
    tx = s.tag(tx, 146, "Research article", fill=WOS_L, color=WOS, size=10.5) + 6
    tx = s.tag(tx, 146, "Open access", fill=GREEN_L, color=GREEN, size=10.5) + 6
    tx = s.tag(tx, 146, "Cited by 42", fill=GREY_L, color=TXT2, size=10.5) + 6
    s.text(48, 194, "Highlights：R&D tax credits raise patent counts by 8% ...", size=11.5, fill=TXT3)
    s.text(48, 212, "Abstract：We exploit a 2015 reform to identify the causal effect ...",
           size=11.5, fill=TXT3)
    s.rect(760, 92, 136, 30, fill=SD, rx=5)
    s.text(828, 112, "Download PDF", size=11.5, fill="#ffffff", anchor="middle", weight="600")
    s.text(828, 148, "View PDF  ▾", size=11.5, fill=TXT2, anchor="middle")
    s.text(828, 176, "Export  ▾", size=11.5, fill=TXT2, anchor="middle")
    s.text(828, 202, "Cite  ▾", size=11.5, fill=TXT2, anchor="middle")

    items = [
        ("①", "题名", "判断主题与研究方法，点开进入详情页"),
        ("②", "作者", "识别研究团队，追同一作者的系列成果"),
        ("③", "期刊名与卷期页码", "题录必备字段；也是判断期刊层次的线索"),
        ("④", "文献类型标签", "Review article 先读，Research article 后读"),
        ("⑤", "Open access / Cited by", "能否免费下载；被引量反映影响力"),
        ("⑥", "Download PDF / Export", "下载全文；导出 RIS 题录给 Zotero"),
    ]
    y = 256
    for i, (n, t, d) in enumerate(items):
        col = i // 3
        row = i % 3
        bx = 28 + col * 452
        by = y + row * 32
        s.circle(bx + 8, by - 4, 10, fill=ORANGE)
        s.text(bx + 8, by, n, size=11, fill="#ffffff", anchor="middle", weight="700")
        s.text(bx + 26, by, t, size=12, fill=TXT, weight="500")
        s.text(bx + 26, by + 17, d, size=11, fill=TXT3)
    s.watermark()
    return save(s, os.path.join(OUT, "f04-sd-result-item.svg"))


# ------------------------------------------------------- f05 SD 文章页
def f05():
    s = S(960, 592)
    cx, cy, cw, ch = s.window(30, 24, 900, 510, title="Article",
                              url="https://www.sciencedirect.com/science/article/pii/S0048...")
    s.sitebar(cx, cy, cw, 32, brand="ScienceDirect", brand_color=SD)
    top = cy + 32
    s.text(cx + 24, top + 34, "R&D tax credits and firm innovation: Evidence from a", size=15,
           fill=TXT, weight="700")
    s.text(cx + 24, top + 56, "quasi-natural experiment", size=15, fill=TXT, weight="700")
    s.text(cx + 24, top + 80, "J. Smith a, L. Wang b, M. Rossi c", size=12, fill=TXT2)
    s.text(cx + 24, top + 100, "Research Policy · Volume 53, Issue 3 · April 2024 · Pages 104-126",
           size=11.5, fill=TXT3)
    s.rect(cx + 640, top + 24, 108, 30, fill=SD, rx=5)
    s.text(cx + 694, top + 44, "Download PDF", size=11, fill="#ffffff", anchor="middle", weight="600")
    s.rect(cx + 756, top + 24, 108, 30, fill="#ffffff", stroke=BORDER, rx=5)
    s.text(cx + 810, top + 44, "Cite  ▾", size=11, fill=TXT2, anchor="middle")
    s.line(cx + 24, top + 116, cx + 864, top + 116, stroke=BORDER2)

    lw = 600
    s.text(cx + 24, top + 144, "Highlights", size=13, fill=TXT, weight="700")
    for i, t in enumerate(["· R&D tax credits increase patent counts by 8%",
                           "· Effects are concentrated in financially constrained firms",
                           "· No evidence of crowding out of private R&D",
                           "· Policy design matters more than credit generosity"]):
        s.text(cx + 36, top + 166 + i * 20, t, size=11.5, fill=TXT2)
    s.text(cx + 24, top + 268, "Abstract", size=13, fill=TXT, weight="700")
    s.para(cx + 24, top + 290, [
        "We exploit a reform that expanded R&D tax credits to identify the causal",
        "effect of fiscal incentives on firm innovation. Using firm-level panel data,",
        "we find that eligible firms increased R&D expenditure and patent filings.",
    ], size=11.5, fill=TXT2, lh=17)
    s.text(cx + 24, top + 356, "Keywords", size=13, fill=TXT, weight="700")
    kx = cx + 24
    for k in ["R&D tax credit", "Innovation", "Tax incentive", "Firm behaviour"]:
        kx = s.chip(kx, top + 366, k, fill=SD_L, color="#8a4200", size=10.5, h=20, pad=8) + 7
    s.text(cx + 24, top + 412, "Introduction", size=12.5, fill=TXT, weight="700")
    s.text(cx + 24, top + 432, "1.1 Background ........................................................................",
           size=11.5, fill=TXT2)
    s.text(cx + 24, top + 452, "1.2 Contribution ......................................................................",
           size=11.5, fill=TXT2)

    s.rect(cx + 648, top + 136, 216, 210, fill="#fafbfd", stroke=BORDER2, rx=8)
    s.text(cx + 664, top + 160, "More info", size=12, fill=TXT, weight="700")
    for i, (k, v) in enumerate([("Cited by", "42"), ("Related articles", "12"),
                                ("Recommended", "10"), ("Cited by (Scopus)", "38")]):
        s.text(cx + 664, top + 186 + i * 26, k, size=11, fill=TXT2)
        s.text(cx + 848, top + 186 + i * 26, v, size=11, fill=BLUE, anchor="end")
    s.line(cx + 664, top + 296, cx + 848, top + 296, stroke=BORDER2)
    s.text(cx + 664, top + 318, "Save to list / Set alert", size=11, fill=BLUE)

    for n, (bx, by) in enumerate([(cx + 8, top + 144), (cx + 8, top + 268), (cx + 8, top + 356),
                                  (cx + 632, top + 44), (cx + 632, top + 160), (cx + 8, top + 412)]):
        s.badge(bx, by - 2, n + 1)
    s.watermark()
    return save(s, os.path.join(OUT, "f05-sd-article.svg"))


# ------------------------------------------------------- f06 WoS 检索
def f06():
    s = S(960, 522)
    cx, cy, cw, ch = s.window(30, 24, 900, 420, title="Web of Science",
                              url="https://www.webofscience.com/wos/woscc/basic-search")
    s.sitebar(cx, cy, cw, 36, brand="Web of Science", brand_color=WOS)
    for i, t in enumerate(["Search", "Research Intelligence", "My Tools", "Sign In"]):
        s.text(cx + 260 + i * 130, cy + 23, t, size=12, fill=TXT2)
    top = cy + 36
    s.rect(cx, top, cw, 34, fill=WOS_L)
    for i, t in enumerate(["Documents", "Cited References", "Structure", "Chemical"]):
        s.text(cx + 24 + i * 130, top + 22, t, size=12.5, fill=WOS if i == 0 else TXT2,
               weight="700" if i == 0 else "400")
    s.rect(cx + 12, top + 30, 84, 3, fill=WOS, rx=1.5)

    s.rect(cx + 16, top + 48, 170, 30, fill="#ffffff", stroke=BORDER, rx=4)
    s.text(cx + 28, top + 67, "Topic", size=12.5, fill=TXT)
    s.caret(cx + 164, top + 62, 6)
    s.line(cx + 186, top + 52, cx + 186, top + 74, stroke=BORDER2)
    s.text(cx + 196, top + 67, "▾  Select a field", size=12, fill=TXT3)
    s.field(cx + 16, top + 86, 640, 32, "TS=(\"R&D tax credit\" OR \"research and development tax credit\") AND innovat*",
            size=12)
    s.text(cx + 16, top + 140, "+ Add row", size=12, fill=WOS)
    s.text(cx + 110, top + 140, "✕ Clear", size=12, fill=TXT2)
    s.text(cx + 196, top + 140, "Search", size=12, fill="#ffffff", anchor="middle")
    s.rect(cx + 180, top + 126, 70, 24, fill=WOS, rx=4)

    s.text(cx + 16, top + 176, "Timespan:", size=12, fill=TXT2)
    for i, t in enumerate(["All years (1990 - 2026)", "Since 2020", "Custom year range"]):
        s.radio(cx + 96 + i * 168, top + 172, 6, on=(i == 0))
        s.text(cx + 110 + i * 168, top + 176, t, size=11.5, fill=TXT2)

    s.rect(cx + 16, top + 200, 868, 96, fill="#fafbfd", stroke=BORDER2, rx=8)
    s.text(cx + 34, top + 226, "常用检索字段（下拉列表）", size=12, fill=TXT, weight="700")
    fl = ["Topic (TS=)", "Title (TI=)", "Author (AU=)", "Publication Titles (SO=)",
          "Year Published (PY=)", "Affiliation (OG=)", "DOI"]
    for i, t in enumerate(fl):
        col = i % 4
        row = i // 4
        s.text(cx + 34 + col * 216, top + 252 + row * 22, "· " + t, size=11, fill=TXT2)

    s.badge(cx + 8, top + 148, 1)
    s.badge(cx + 8, top + 64, 2)
    s.badge(cx + 668, top + 64, 3)
    s.badge(cx + 8, top + 172, 4)
    s.note(cx + 16, top + 312, 868,
           ["① 检索行与字段：Topic 字段（TS=）覆盖标题、摘要、作者关键词与 Keywords Plus，是最常用的求全字段",
            "② 字段下拉：需要精确时改用 Title / Author / Publication Titles　③ 检索框：AND / OR / NOT 必须大写，精确短语用 \" \"",
            "④ 时间范围：先用 All years，结果太多再收窄"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "f06-wos-home.svg"))


# ------------------------------------------------------- f07 WoS 精炼
def f07():
    s = S(990, 672)
    cx, cy, cw, ch = s.window(24, 20, 942, 560, title="Results",
                              url="https://www.webofscience.com/wos/woscc/summary")
    s.sitebar(cx, cy, cw, 30, brand="Web of Science", brand_color=WOS)
    top = cy + 30
    s.rect(cx, top, cw, 34, fill="#f7f9fb")
    s.line(cx, top + 34, cx + cw, top + 34, stroke=BORDER2)
    s.text(cx + 16, top + 22, "TS=(\"R&D tax credit\" ...) AND innovat*", size=11.5, fill=TXT2)
    s.text(cx + 16, top + 62, "1,247 results from Web of Science Core Collection", size=13.5,
           fill=TXT, weight="700")
    s.text(cx + cw - 16, top + 62, "Sort by:  Relevance  |  Date  |  Citations", size=11.5,
           fill=TXT2, anchor="end")
    s.text(cx + 16, top + 84, "☑ Select Page　Export ▾　Add to Marked List", size=11.5, fill=WOS)

    lw = 268
    s.rect(cx, top + 100, lw, ch - 100, fill="#fafbfd")
    s.line(cx + lw, top + 100, cx + lw, cy + ch, stroke=BORDER2)
    s.text(cx + 14, top + 124, "Refine results", size=13, fill=TXT, weight="700")
    gy = top + 152
    groups = [("Web of Science Index", ["SCI-EXPANDED (1,102)", "SSCI (145)", "ESCI (78)",
                                        "CPCI-S (22)"]),
              ("Document Types", ["Article (1,081)", "Review Article (112)",
                                  "Proceedings Paper (31)"]),
              ("Web of Science Categories", ["Economics (412)", "Business (286)",
                                             "Management (231)"]),
              ("Publication Years", ["2026 (86)", "2025 (203)", "2024 (245)"]),
              ("Open Access", ["Open Access (518)", "Free to Read (76)"])]
    for g, items in groups:
        s.text(cx + 14, gy, g, size=11.5, fill=TXT, weight="700")
        gy += 12
        for it in items:
            s.check(cx + 16, gy, 11, on=(g in ("Web of Science Index",) and it.startswith("SSCI")))
            s.text(cx + 33, gy + 10, it, size=10.5, fill=TXT2)
            gy += 19
        gy += 12
        s.line(cx + 14, gy - 8, cx + lw - 14, gy - 8, stroke=BORDER2)

    rx = cx + lw + 16
    rw = cw - lw - 32
    ry = top + 112
    for i in range(4):
        s.rect(rx, ry, rw, 98, fill="#ffffff", stroke=BORDER2, rx=6)
        s.text(rx + 12, ry + 24, "R&D tax credits and firm innovation: Evidence from "
               + ["a quasi-natural experiment", "European firms", "Chinese listed firms",
                  "panel data"][i], size=12.5, fill=BLUE, weight="500")
        s.text(rx + 12, ry + 46, "Smith J; Wang L; Rossi M", size=11, fill=TXT2)
        s.text(rx + 12, ry + 66, "RESEARCH POLICY　Vol. 53　Issue 3　Pages 104-126　2024",
               size=10.5, fill=TXT2)
        tx = rx + 12
        tx = s.tag(tx, ry + 74, "SSCI", fill=WOS_L, color=WOS, size=9.5, h=15) + 5
        tx = s.tag(tx, ry + 74, "Q1", fill=GREEN_L, color=GREEN, size=9.5, h=15) + 5
        tx = s.tag(tx, ry + 74, "Open Access", fill=GREY_L, color=TXT2, size=9.5, h=15)
        s.text(rx + rw - 150, ry + 46, "Citations: 42", size=10.5, fill=TXT3)
        s.text(rx + rw - 90, ry + 66, "Cited References: 58", size=10, fill=TXT3)
        ry += 104

    s.badge(cx + 8, top + 62, 1)
    s.badge(cx + 8, top + 152, 2)
    s.badge(rx - 12, top + 136, 3)
    s.badge(rx - 12, top + 190, 4)
    s.badge(cx + 8, top + 84, 5)
    s.note(cx + 560, cy + ch - 76, 358,
           ["① 结果数与排序方式（Relevance / Date / Citations）",
            "② 精炼面板：Web of Science Index 直接筛 SSCI / SCI-EXPANDED",
            "③ 文献类型：Article 与 Review Article 分开读",
            "④ 条目上的收录与分区标签　⑤ 导出 / 加入标记列表"],
           title="WoS 结果页要点", fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "f07-wos-refine.svg"))


# ------------------------------------------------------- f08 WoS 期刊详情
def f08():
    s = S(940, 470)
    cx, cy, cw, ch = s.window(28, 24, 884, 420, title="Publication",
                              url="https://www.webofscience.com/wos/woscc/...)")
    s.sitebar(cx, cy, cw, 30, brand="Web of Science", brand_color=WOS)
    top = cy + 30
    s.text(cx + 20, top + 34, "RESEARCH POLICY", size=17, fill=TXT, weight="700")
    s.text(cx + 20, top + 56, "ISSN 0048-7333　Publisher: Elsevier", size=11.5, fill=TXT3)
    tx = cx + 20
    tx = s.tag(tx, top + 68, "SCI-EXPANDED", fill=WOS_L, color=WOS, size=10.5) + 6
    tx = s.tag(tx, top + 68, "SSCI", fill=WOS_L, color=WOS, size=10.5) + 6
    tx = s.tag(tx, top + 68, "Indexed in JCR", fill=GREEN_L, color=GREEN, size=10.5)

    s.line(cx + 20, top + 100, cx + cw - 20, top + 100, stroke=BORDER2)
    s.text(cx + 20, top + 128, "Web of Science Categories", size=12.5, fill=TXT, weight="700")
    for i, t in enumerate(["Economics", "Management", "Business"]):
        s.text(cx + 20, top + 152 + i * 22, "· " + t, size=11.5, fill=TXT2)

    s.text(cx + 300, top + 128, "收录信息怎么读", size=12.5, fill=TXT, weight="700")
    s.para(cx + 300, top + 152, [
        "· 出现在 SCI-EXPANDED / SSCI 列表中，",
        "  说明该刊被对应索引收录。",
        "· 一本刊可能同时属于多个类目，",
        "  分区要在每个类目里分别看。",
        "· 收录状态会调整，引用前以最新",
        "  一期 JCR 与 WoS 页面为准。",
    ], size=11.5, fill=TXT2, lh=19)

    s.rect(cx + 20, top + 206, 844, 118, fill="#fafbfd", stroke=BORDER2, rx=8)
    s.text(cx + 38, top + 232, "该刊近年发文与引用概况（示意）", size=12, fill=TXT, weight="700")
    base = top + 300
    s.line(cx + 38, base, cx + 500, base, stroke=BORDER)
    vals = [40, 52, 61, 74, 88, 96]
    for i, v in enumerate(vals):
        x = cx + 56 + i * 72
        h = v * 0.6
        s.rect(x, base - h, 34, h, fill=WOS, op=0.75, rx=3)
        s.text(x + 17, base + 16, str(2021 + i), size=10, fill=TXT3, anchor="middle")
    s.text(cx + 540, top + 232, "同类别期刊中的位置", size=12, fill=TXT, weight="700")
    for i, (q, c, d) in enumerate([("Q1", GREEN, "该类别前 25%"),
                                   ("Q2", BLUE, "25%—50%"),
                                   ("Q3", ORANGE, "50%—75%"),
                                   ("Q4", RED, "75%—100%")]):
        yy = top + 250 + i * 22
        s.rect(cx + 540, yy, 30, 16, fill=c, rx=3)
        s.text(cx + 555, yy + 12, q, size=10, fill="#ffffff", anchor="middle", weight="700")
        s.text(cx + 580, yy + 12, d, size=10.5, fill=TXT2)
        if q == "Q1":
            s.text(cx + 700, yy + 12, "← 本刊所在区间", size=10.5, fill=GREEN, weight="700")
    s.watermark("界面位置与指标数值为示意")
    return save(s, os.path.join(OUT, "f08-wos-journal.svg"))


# ------------------------------------------------------- f09 JCR 分区
def f09():
    s = S(940, 548)
    s.text(28, 34, "JCR 分区与影响因子怎么读", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "关键点：分区是“同一学科类别内部”的相对位置，不是全学科统一分数线",
           size=12.5, fill=TXT3)

    s.rect(28, 74, 884, 168, fill="#ffffff", stroke=BORDER, rx=8)
    s.text(48, 102, "某一学科类别（例如 Economics）内的期刊排名（示意）", size=12.5,
           fill=TXT, weight="700")
    band = [("Q1", 0, 0.25, GREEN, "第 1—25%"),
            ("Q2", 0.25, 0.50, BLUE, "第 25—50%"),
            ("Q3", 0.50, 0.75, ORANGE, "第 50—75%"),
            ("Q4", 0.75, 1.00, RED, "第 75—100%")]
    x0, y0, bw, bh = 48, 122, 844, 46
    for name, a, b, c, d in band:
        x = x0 + bw * a
        s.rect(x, y0, bw * (b - a), bh, fill=c, op=0.18)
        s.rect(x, y0, bw * (b - a), bh, fill="none", stroke=c, sw=1.4)
        s.text(x + bw * (b - a) / 2, y0 + 22, name, size=15, fill=c, anchor="middle", weight="700")
        s.text(x + bw * (b - a) / 2, y0 + 39, d, size=10.5, fill=TXT2, anchor="middle")
    s.text(x0, y0 + 68, "排名靠前（指标高）", size=11, fill=TXT3)
    s.text(x0 + bw, y0 + 68, "排名靠后（指标低）", size=11, fill=TXT3, anchor="end")
    s.text(48, y0 + 92, "Journal Impact Factor (JIF)：某刊前两年论文在统计年的平均被引次数，衡量的是“期刊”而非“某篇论文”。",
           size=11.5, fill=TXT2)

    rows = [["指标", "含义", "使用时的注意点"],
            ["Journal Impact Factor (JIF)", "该刊近年论文的平均被引水平", "只看期刊整体，不能评价单篇文献"],
            ["JIF Quartile（Q1—Q4）", "同一学科类别内按 JIF 四等分", "必须同时说明“哪个类别里的 Q1”"],
            ["JIF Rank / Percentile", "该刊在类别内的排名与百分位", "跨学科比较时不可直接用 JIF"],
            ["JCI", "按类别归一化后的引文指标", "适合跨学科横向比较"],
            ["Category", "该刊所属的学科类别（可多个）", "不同类别里分区可能不同"]]
    table(s, 28, 262, rows, [240, 300, 344], rh=28)
    s.note(28, 456, 884,
           ["· JCR 分区与中科院分区是两套体系，发布方、分类方法与使用习惯都不同，写论文或申报前先问清学院要求哪一种。",
            ""],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark("概念示意图，未标注具体数值")
    return save(s, os.path.join(OUT, "f09-jcr-quartile.svg"))


# ------------------------------------------------------- f10 Google Scholar
def f10():
    s = S(940, 548)
    cx, cy, cw, ch = s.window(28, 24, 884, 420, title="Google 学术搜索",
                              url="https://scholar.google.com/scholar?q=R%26D+tax+credit")
    top = cy
    s.rect(cx, top, cw, 46, fill="#ffffff")
    s.text(cx + 20, top + 32, "Google", size=17, fill=GS, weight="700")
    s.text(cx + 90, top + 32, "学术", size=15, fill=TXT2)
    s.field(cx + 150, top + 10, 520, 28, "R&D tax credit innovation", size=12)
    s.circle(cx + 646, top + 24, 11, fill=GS)
    s.text(cx + 646, top + 29, "⌕", size=12, fill="#ffffff", anchor="middle")
    s.line(cx, top + 46, cx + cw, top + 46, stroke=BORDER2)

    ry = top + 58
    for i in range(3):
        s.text(cx + 20, ry + 18, "R&D tax credits and firm innovation: Evidence from "
               + ["a quasi-natural experiment", "European firms", "panel data"][i],
               size=13.5, fill=GS, weight="500")
        s.text(cx + 20, ry + 38, "J Smith, L Wang, M Rossi - Research Policy, 2024 - Elsevier",
               size=11, fill=GREEN)
        s.text(cx + 20, ry + 56, "We exploit a reform that expanded R&D tax credits to identify ...",
               size=11, fill=TXT2)
        s.text(cx + 20, ry + 78, "被引用次数：42", size=11, fill=TXT2)
        s.text(cx + 130, ry + 78, "相关文章", size=11, fill=GS)
        s.text(cx + 200, ry + 78, "所有 6 个版本", size=11, fill=GS)
        s.line(cx + 20, ry + 92, cx + cw - 20, ry + 92, stroke=BORDER2)
        ry += 102

    s.badge(cx + 8, ry - 306 + 78, 1, r=10, size=10)
    s.badge(cx + 118, ry - 306 + 78, 2, r=10, size=10)
    s.badge(cx + 188, ry - 306 + 78, 3, r=10, size=10)
    s.note(cx + 20, ry + 6, 844,
           ["① “被引用次数”与“引用”：点开后是引用该文的所有文献，是往后追文献最快的入口。",
            "② “相关文章”：不看关键词也能找到主题接近的文献。",
            "③ “所有版本”：同一篇论文可能有预印本、机构库版本与正式出版版本，正式引用要以出版版本为准。"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "f10-scholar-cited.svg"))


# ------------------------------------------------------- f11 语法对照
def f11():
    s = S(980, 600)
    s.text(28, 36, "中外文数据库检索字段与语法对照", size=17, fill=TXT, weight="700")
    s.text(28, 58, "换数据库必须重写检索式：字段代码与通配符并不通用", size=12.5, fill=TXT3)
    rows = [["功能", "知网（CNKI）", "Web of Science", "ScienceDirect"],
            ["主题 / 题录", "SU=", "TS=", "Title, abstract or author-specified keywords"],
            ["篇名", "TI=", "TI=", "Title only"],
            ["摘要", "AB=", "AB=", "无独立字段（并入主题字段）"],
            ["关键词", "KY=", "AK=", "无独立字段（并入主题字段）"],
            ["作者", "AU=", "AU=", "Author"],
            ["机构 / 单位", "AF=（作者单位）", "OG=", "Author affiliation"],
            ["期刊名", "LY=", "SO=", "Journal and book title"],
            ["出版年", "YE=", "PY=", "Years 时间范围控件"],
            ["逻辑与", "AND", "AND", "AND（须大写）"],
            ["逻辑或", "OR", "OR", "OR（须大写）"],
            ["逻辑非", "NOT", "NOT", "NOT（须大写）"],
            ["精确短语", "\"经济高质量发展\"", "\"R&D tax credit\"", "\"R&D tax credit\""],
            ["通配 / 截词", "% 与 +", "* 与 ?", "*"],
            ["括号优先级", "支持", "支持", "支持"]]
    table(s, 28, 74, rows, [140, 260, 220, 332], rh=29, size=11.5)
    s.note(28, 512, 932,
           ["· 通配符差别最容易出错：知网用 % 表示多个字符，WoS 与 ScienceDirect 用 *。",
            "· 逻辑运算符在 WoS 与 ScienceDirect 中必须大写；小写 and 可能被当作普通词处理。"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark("表格示意图")
    return save(s, os.path.join(OUT, "f11-syntax-compare.svg"))


# ------------------------------------------------------- f12 术语映射
def f12():
    s = S(940, 572)
    s.text(28, 36, "从中文议题到英文检索词的对照路径", size=17, fill=TXT, weight="700")
    s.text(28, 58, "不要直接翻译题目，要从已有文献里“捡”英文表达", size=12.5, fill=TXT3)

    s.rect(28, 80, 300, 226, fill=BLUE_L, rx=10)
    s.text(178, 112, "中文议题", size=14, fill=BLUE, anchor="middle", weight="700")
    for i, t in enumerate(["研发费用加计扣除", "税收优惠", "企业创新投入", "税负转嫁", "税收征管效率"]):
        s.rect(52, 130 + i * 34, 252, 26, fill="#ffffff", stroke=BLUE_B, rx=5)
        s.text(178, 148 + i * 34, t, size=11.5, fill=TXT2, anchor="middle")

    arrows = [("① 读中文论文的英文摘要", 0),
              ("② 看知网外文文献题录", 1),
              ("③ 查政策文件官方英译", 2),
              ("④ 用词典 + 回验", 3)]
    for t, i in arrows:
        s.arrow(340, 130 + i * 52 + 14, 400, 130 + i * 52 + 14, color=ORANGE, sw=1.8)
        s.text(370, 124 + i * 52 + 14, t, size=10.5, fill="#8a6100", anchor="middle")

    s.rect(410, 80, 502, 226, fill=GREEN_L, rx=10)
    s.text(661, 112, "英文检索词与同义表达", size=14, fill=GREEN, anchor="middle", weight="700")
    pairs = [("研发费用加计扣除", "R&D tax credit / super deduction"),
             ("税收优惠", "tax incentive / tax preference"),
             ("企业创新投入", "firm innovation / R&D investment"),
             ("税负转嫁", "tax shifting / tax incidence"),
             ("税收征管效率", "tax administration efficiency")]
    for i, (a, b) in enumerate(pairs):
        s.rect(432, 130 + i * 34, 458, 26, fill="#ffffff", stroke="#bfe3cb", rx=5)
        s.text(448, 148 + i * 34, b, size=11.5, fill=TXT2)
        s.text(874, 148 + i * 34, "同义 ✓", size=10.5, fill=GREEN, anchor="end")

    s.rect(28, 322, 884, 62, fill=YELLOW_L, stroke=YEL_B, rx=8)
    s.text(48, 346, "回验方法：把想用的英文词放回英文数据库里搜一遍。如果搜索结果的标题和摘要里几乎不出现这个词，",
           size=12, fill="#8a6100")
    s.text(48, 366, "说明它不是学术界的常用说法，应当换词；这是判断译法是否地道的唯一可靠办法。",
           size=12, fill="#8a6100")

    rows = [["常见误区", "后果", "正确做法"],
            ["把整句中文题目翻译成英文去搜", "结果数为 0 或极少", "拆成概念块，每个块找 1—3 个英文表达"],
            ["只搜缩写（R&D、VAT）", "漏掉全称写法的文献", "缩写与全称都要检索，用 OR 连接"],
            ["只用上位词（taxation）", "结果过多、噪声大", "补充核心词与限定条件"],
            ["忽略英式 / 美式拼写差异", "漏掉一部分文献", "两种拼写都要出现在检索式中"]]
    table(s, 28, 396, rows, [280, 240, 364], rh=28, size=11.5)
    s.watermark("概念示意图")
    return save(s, os.path.join(OUT, "f12-term-mapping.svg"))


if __name__ == "__main__":
    for f in (f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12):
        print(f.__name__, "->", f())
