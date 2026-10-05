# -*- coding: utf-8 -*-
"""Zotero 文献管理部分界面示意图生成脚本。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa

ROOT = r"F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\public\images"
OUT = os.path.join(ROOT, "zotero")

ZOT = "#8b1f1f"     # Zotero 品牌红
ZOT_L = "#fbeaea"
CNKI = "#1a5fb4"
CNKI_L = "#e9f1fb"


def appshell(s, x, y, w, h, menubar=True, toolbar=True, title="Zotero"):
    cx, cy, cw, ch = s.window(x, y, w, h, title=title, app=True)
    yy = cy
    if menubar:
        s.rect(cx, yy, cw, 28, fill="#ffffff")
        s.line(cx, yy + 28, cx + cw, yy + 28, stroke=BORDER2)
        mx = cx + 16
        for m in ["文件", "编辑", "视图", "工具", "帮助"]:
            s.text(mx, yy + 19, m, size=12, fill=TXT2)
            mx += tw(m, 12) + 22
        s.text(cx + cw - 240, yy + 19, "我的文库", size=11.5, fill=TXT3)
        yy += 28
    if toolbar:
        s.rect(cx, yy, cw, 34, fill=BAR2)
        s.line(cx, yy + 34, cx + cw, yy + 34, stroke=BORDER)
        icons = [("＋", GREEN, "新建条目"), ("▣", "#e8b400", "新建分类"),
                 ("⚯", TXT2, "添加附件"), ("✎", TXT2, "添加笔记"),
                 ("⌕", TXT2, "查找可用 PDF"), ("↻", GREEN, "同步")]
        ix = cx + 14
        for g, c, tip in icons:
            s.circle(ix + 9, yy + 17, 10, fill=c, op=0.18)
            s.text(ix + 9, yy + 22, g, size=11.5, fill=c, anchor="middle")
            ix += 26
        s.rect(cx + cw - 190, yy + 7, 174, 21, fill="#ffffff", stroke=BORDER, rx=11)
        s.text(cx + cw - 178, yy + 22, "搜索我的文库…", size=10.5, fill=TXT3)
        yy += 34
    return cx, yy, cw, (cy + h - 38) - yy


# ------------------------------------------------- z01 官网下载页
def z01():
    s = S(960, 500)
    cx, cy, cw, ch = s.window(30, 24, 900, 450, title="Zotero",
                              url="https://www.zotero.org/download/")
    s.sitebar(cx, cy, cw, 38, brand="Zotero", brand_color=ZOT)
    for i, t in enumerate(["Home", "Groups", "Documentation", "Forums", "Get Involved"]):
        s.text(cx + 160 + i * 128, cy + 24, t, size=12, fill=TXT2)

    top = cy + 38
    s.text(cx + 30, top + 40, "Download", size=20, fill=TXT, weight="700")
    s.text(cx + 30, top + 66, "Zotero 免费、开源，主程序与浏览器连接器需要分别安装",
           size=12, fill=TXT3)

    s.rect(cx + 30, top + 84, 400, 190, fill="#ffffff", stroke=BORDER, rx=8)
    s.text(cx + 50, top + 112, "1  Zotero（主程序）", size=13.5, fill=TXT, weight="700")
    s.text(cx + 50, top + 134, "管理资料库、阅读与批注、生成参考文献", size=11.5, fill=TXT3)
    for i, (os_, ver) in enumerate([("Windows", "64-bit"), ("macOS", "Universal"),
                                    ("Linux", "64-bit")]):
        s.rect(cx + 50, top + 150 + i * 32, 360, 26, fill=GREY_L, stroke=BORDER2, rx=5)
        s.text(cx + 64, top + 168 + i * 32, "Download for " + os_, size=11.5, fill=TXT2)
        s.text(cx + 396, top + 168 + i * 32, ver, size=10.5, fill=TXT3, anchor="end")

    s.rect(cx + 454, top + 84, 416, 190, fill="#ffffff", stroke=BORDER, rx=8)
    s.text(cx + 474, top + 112, "2  Zotero Connector（浏览器连接器）", size=13.5,
           fill=TXT, weight="700")
    s.text(cx + 474, top + 134, "负责从网页一键抓取题录与全文，必须单独安装", size=11.5, fill=TXT3)
    for i, (br, note) in enumerate([("Chrome / Edge", "应用商店安装"),
                                    ("Firefox", "附加组件安装"),
                                    ("Safari", "系统扩展安装")]):
        s.rect(cx + 474, top + 150 + i * 32, 376, 26, fill=GREY_L, stroke=BORDER2, rx=5)
        s.text(cx + 488, top + 168 + i * 32, "Install " + br, size=11.5, fill=TXT2)
        s.text(cx + 836, top + 168 + i * 32, note, size=10.5, fill=TXT3, anchor="end")

    s.badge(cx + 16, top + 108, 1)
    s.badge(cx + 440, top + 108, 2)
    s.note(cx + 30, top + 292, 840,
           ["· 两个都要装：只装主程序就只能手敲题录；只装连接器则抓下来的内容无处存放。",
            "· 版本会持续更新，安装时以官网当前提供的版本与按钮文字为准。",
            "· 主程序与连接器建议同时升级到新版本，避免接口不匹配导致抓取失败。"],
           title="下载页要点", fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "z01-zotero-download-page.svg"))


# ------------------------------------------------- z02 安装向导
def z02():
    s = S(880, 440)
    s.rect(0, 0, 880, 440, fill=BG)
    s.rect(120, 60, 640, 320, fill="#ffffff", stroke=BORDER, rx=10)
    s.rect(120, 60, 640, 44, fill=BAR, rx=10)
    s.rect(120, 92, 640, 12, fill=BAR)
    s.text(144, 90, "Zotero 安装向导", size=13.5, fill=TXT, weight="700")
    s.line(120, 104, 760, 104, stroke=BORDER)
    s.text(148, 146, "欢迎使用 Zotero 安装向导", size=16, fill=TXT, weight="700")
    s.text(148, 174, "向导将引导你完成安装。安装前建议关闭正在运行的浏览器，", size=12, fill=TXT2)
    s.text(148, 194, "以便自动配置浏览器连接器。", size=12, fill=TXT2)
    s.line(148, 216, 732, 216, stroke=BORDER2)
    for i, (t, d) in enumerate([("安装位置", "C:\\Program Files\\Zotero"),
                                ("安装类型", "Standard（推荐）"),
                                ("附加选项", "☑ 安装浏览器连接器　☑ 创建桌面快捷方式")]):
        s.text(148, 244 + i * 30, t, size=12, fill=TXT, weight="700")
        s.text(280, 244 + i * 30, d, size=12, fill=TXT2)
    s.rect(520, 330, 100, 32, fill=GREY_L, stroke=BORDER, rx=5)
    s.text(570, 351, "Back", size=12, fill=TXT2, anchor="middle")
    s.rect(632, 330, 100, 32, fill=BLUE, rx=5)
    s.text(682, 351, "Install", size=12.5, fill="#ffffff", anchor="middle", weight="600")
    s.badge(104, 244, 1)
    s.badge(104, 274, 2)
    s.badge(104, 304, 3)
    s.note(40, 116, 66, [], title="", fill="none", stroke="none")
    s.text(40, 400, "① 安装位置用默认值即可　② 安装类型选 Standard　③ 勾选安装浏览器连接器，能省去后面单独配置的步骤",
           size=11.5, fill=TXT3)
    s.watermark()
    return save(s, os.path.join(OUT, "z02-install-wizard.svg"))


# ------------------------------------------------- z03 主界面
def z03():
    s = S(1020, 660)
    cx, cy, cw, ch = appshell(s, 24, 20, 972, 620)

    lw, mw = 236, 372
    rw = cw - lw - mw - 2
    rx0 = cx + lw
    rx2 = cx + lw + mw

    # 左栏
    s.rect(cx, cy, lw, ch, fill="#fafbfd")
    s.line(rx0, cy, rx0, cy + ch, stroke=BORDER)
    s.text(cx + 14, cy + 24, "我的文库", size=12.5, fill=TXT, weight="700")
    tree = [("课程：文献检索与研究方法", 0, False),
            ("检索方法与规范", 1, False),
            ("毕业论文：加计扣除与企业创新", 0, True),
            ("01 政策与背景", 1, True),
            ("02 理论与机制", 1, True),
            ("03 实证与数据方法", 1, False),
            ("04 国外经验与比较", 1, False),
            ("05 待读文献", 1, False),
            ("重复条目", 0, False),
            ("未分类条目", 0, False),
            ("回收站", 0, False)]
    ty = cy + 44
    for name, lv, on in tree:
        if on:
            s.rect(cx + 4, ty - 13, lw - 8, 22, fill=BLUE_L, rx=4)
        if lv == 0:
            s.caret(cx + 12, ty - 8, 5)
            s.text(cx + 26, ty, name, size=11.5, fill=BLUE if on else TXT2,
                   weight="700" if on else "400")
        else:
            s.text(cx + 40, ty, name, size=11.5, fill=BLUE if on else TXT2,
                   weight="600" if on else "400")
        ty += 24
    s.line(cx + 10, cy + ch - 116, cx + lw - 10, cy + ch - 116, stroke=BORDER2)
    s.text(cx + 14, cy + ch - 96, "标签过滤器", size=11.5, fill=TXT, weight="700")
    tgx = cx + 14
    tgy = cy + ch - 80
    for i, (t, c) in enumerate([("已读", GREEN), ("阅读中", ORANGE), ("未读", TXT3),
                                ("重要", RED), ("综述", PURPLE), ("实证", BLUE),
                                ("政策", GREEN), ("机制", ORANGE)]):
        w = tw(t, 10) + 14
        if tgx + w > cx + lw - 12:
            tgx = cx + 14
            tgy += 20
        s.rect(tgx, tgy, w, 17, fill=c, op=0.14, rx=8)
        s.text(tgx + w / 2, tgy + 12, t, size=10, fill=c, anchor="middle")
        tgx += w + 5

    # 中间栏
    s.rect(rx0, cy, mw, ch, fill="#ffffff")
    s.line(rx2, cy, rx2, cy + ch, stroke=BORDER)
    cols = [("标题", 0), ("创建者", 148), ("年份", 250), ("出版物", 288)]
    for name, dx in cols:
        s.text(rx0 + 12 + dx, cy + 24, name, size=11, fill=TXT2, weight="700")
    s.line(rx0, cy + 32, rx2, cy + 32, stroke=BORDER)
    items = [("研发费用加计扣除政策与企业创新投入", "张伟 等", "2023", "税务研究", True, True),
             ("税收优惠、融资约束与高新技术企业研发投入", "陈晓明", "2022", "财政研究", False, True),
             ("加计扣除比例调整对企业创新绩效的影响", "刘洋 等", "2024", "中央财经大学学报", False, True),
             ("R&D tax credits and firm innovation", "Smith J 等", "2024", "Research Policy", False, True),
             ("中国税收优惠政策的创新效应研究", "王芳", "2021", "博士学位论文", False, False),
             ("研发费用加计扣除政策执行问题研究", "李强", "2023", "税收经济研究", False, True)]
    iy = cy + 48
    for i, (t, au, yr, pub, on, has_pdf) in enumerate(items):
        if on:
            s.rect(rx0 + 2, iy - 14, mw - 4, 22, fill=BLUE)
        tc = "#ffffff" if on else TXT
        s.rect(rx0 + 12, iy - 9, 16, 12, fill="none", stroke=tc, sw=1)
        s.text(rx0 + 14, iy, "▤", size=8, fill=tc)
        s.text(rx0 + 34, iy, t[:22], size=11, fill=tc)
        s.text(rx0 + 160, iy, au, size=10.5, fill="#ffffff" if on else TXT2)
        s.text(rx0 + 262, iy, yr, size=10.5, fill="#ffffff" if on else TXT2)
        s.text(rx0 + 300, iy, pub[:12], size=10.5, fill="#ffffff" if on else TXT2)
        if has_pdf:
            s.text(rx2 - 22, iy, "⚯", size=11, fill="#ffffff" if on else TXT3)
        iy += 26

    # 右栏
    s.rect(rx2, cy, rw, ch, fill="#ffffff")
    tabs = ["信息", "摘要", "附件", "笔记", "标签", "相关"]
    tx = rx2 + 12
    for i, t in enumerate(tabs):
        s.text(tx, cy + 24, t, size=11, fill=BLUE if i == 0 else TXT2,
               weight="700" if i == 0 else "400")
        if i == 0:
            s.rect(rx2 + 8, cy + 30, 30, 2.5, fill=BLUE)
        tx += tw(t, 11) + 18
    s.line(rx2, cy + 34, rx2 + rw, cy + 34, stroke=BORDER2)
    fields = [("条目类型", "期刊论文"), ("标题", "研发费用加计扣除政策与企业创新投入"),
              ("作者", "张伟　李娜　王强"), ("出版物", "税务研究"),
              ("卷 / 期", "— / 05"), ("页码", "12-20"),
              ("日期", "2023-05-15"), ("DOI", "10.xxxx/xxxxx"),
              ("语言", "zh-CN"), ("摘要", "本文以 2015 年政策扩围为准自然实验…")]
    fy = cy + 58
    for k, v in fields:
        s.text(rx2 + 12, fy, k, size=10.5, fill=TXT3)
        s.text(rx2 + 86, fy, v, size=11, fill=TXT2)
        s.line(rx2 + 10, fy + 7, rx2 + rw - 10, fy + 7, stroke=BORDER2, sw=0.8)
        fy += 26

    # 编号标注
    s.badge(cx + 8, cy - 46, 1)
    s.badge(cx + 8, cy - 12, 2)
    s.badge(cx + lw + 10, cy - 12, 3)
    s.badge(rx0 + 10, cy - 12, 4)
    s.badge(rx2 + 10, cy - 12, 5)
    s.badge(cx + 10, cy + ch - 100, 6)
    s.badge(rx2 + 10, cy + ch - 12, 7)

    s.note(cx + cw - 302, cy + 330, 290,
           ["① 菜单栏：文件 / 编辑 / 视图 / 工具 / 帮助",
            "② 工具栏：新建条目、新建分类、添加附件、",
            "　　添加笔记、查找可用 PDF、同步、搜索框",
            "③ 左栏：我的文库与分类树；底部为标签过滤器",
            "④ 中间栏：条目列表（标题 / 创建者 / 年份 / 出版物）",
            "⑤ 右栏：信息 / 摘要 / 附件 / 笔记 / 标签 / 相关",
            "⑥ 标签过滤器：点击标签即筛选当前视图",
            "⑦ 右下角预览区：摘要或附件预览"],
           title="六个区域速认", fill="#ffffff", stroke=BORDER2, tcolor=TXT2, size=11, lh=17)
    s.watermark()
    return save(s, os.path.join(OUT, "z03-main-window.svg"))


# ------------------------------------------------- z04 连接器安装
def z04():
    s = S(940, 500)
    cx, cy, cw, ch = s.window(28, 24, 884, 450, title="扩展程序",
                              url="chrome://extensions/")
    top = cy
    s.rect(cx, top, cw, 42, fill="#f7f9fb")
    s.line(cx, top + 42, cx + cw, top + 42, stroke=BORDER2)
    s.text(cx + 20, top + 27, "扩展程序", size=15, fill=TXT, weight="700")
    s.text(cx + 500, top + 27, "开发者模式", size=11.5, fill=TXT2)
    s.rect(cx + 570, top + 14, 34, 18, fill="#ffffff", stroke=BORDER, rx=9)

    s.rect(cx + 20, top + 58, 560, 120, fill="#ffffff", stroke=BLUE, rx=8)
    s.rect(cx + 36, top + 76, 40, 40, fill=ZOT_L, rx=8)
    s.text(cx + 56, top + 102, "Z", size=19, fill=ZOT, anchor="middle", weight="700")
    s.text(cx + 92, top + 92, "Zotero Connector", size=14, fill=TXT, weight="700")
    s.text(cx + 92, top + 112, "Save to Zotero", size=11.5, fill=TXT3)
    s.text(cx + 92, top + 134, "版本 5.0.x　大小 3.2 MB", size=11, fill=TXT3)
    s.rect(cx + 470, top + 82, 94, 26, fill=BLUE, rx=5)
    s.text(cx + 517, top + 100, "已启用", size=11.5, fill="#ffffff", anchor="middle")
    s.text(cx + 470, top + 130, "详情　移除", size=11, fill=TXT3)

    s.text(cx + 20, top + 208, "安装路径：浏览器扩展商店 → 搜索 Zotero Connector → 添加到浏览器",
           size=12, fill=TXT2)
    s.text(cx + 20, top + 234, "固定图标：点击浏览器工具栏的扩展图标 → 点击 Zotero Connector 右侧的图钉",
           size=12, fill=TXT2)
    s.rect(cx + 20, top + 256, 560, 150, fill=ZOT_L, stroke="#f0cccc", rx=8)
    s.text(cx + 40, top + 284, "三种浏览器对应三个不同的商店", size=12.5, fill=ZOT, weight="700")
    for i, t in enumerate(["Chrome / Edge：Chrome 应用商店 或 Edge 加载项商店",
                           "Firefox：Firefox 附加组件（addons.mozilla.org）",
                           "Safari：需要开启系统扩展权限，macOS 上操作路径不同"]):
        s.text(cx + 40, top + 310 + i * 24, "· " + t, size=11.5, fill="#7a2020")
    s.rect(cx + 616, top + 58, 248, 348, fill="#fafbfd", stroke=BORDER2, rx=8)
    s.text(cx + 634, top + 84, "工具栏图标位置", size=12, fill=TXT, weight="700")
    s.rect(cx + 634, top + 98, 212, 30, fill="#ffffff", stroke=BORDER, rx=15)
    for i, g in enumerate(["⌂", "☆", "⚙", "◍"]):
        s.circle(cx + 652 + i * 30, top + 113, 10, fill=GREY_L)
        s.text(cx + 652 + i * 30, top + 118, g, size=11, fill=TXT3, anchor="middle")
    s.circle(cx + 826, top + 113, 12, fill=ZOT)
    s.text(cx + 826, top + 118, "Z", size=13, fill="#ffffff", anchor="middle", weight="700")
    s.text(cx + 634, top + 150, "点击图钉即可固定，", size=11, fill=TXT3)
    s.text(cx + 634, top + 168, "固定后图标会常驻工具栏。", size=11, fill=TXT3)
    s.line(cx + 634, top + 186, cx + 846, top + 186, stroke=BORDER2)
    s.text(cx + 634, top + 212, "自检三问：", size=11.5, fill=TXT, weight="700")
    for i, t in enumerate(["图标是否常驻工具栏？", "在知网页面图标是否变色？", "点击后是否弹出保存窗口？"]):
        s.text(cx + 640, top + 236 + i * 22, "□ " + t, size=11, fill=TXT2)
    s.badge(cx + 8, top + 96, 1)
    s.badge(cx + 604, top + 84, 2)
    s.watermark()
    return save(s, os.path.join(OUT, "z04-connector-install.svg"))


# ------------------------------------------------- z05 工具栏图标状态
def z05():
    s = S(940, 500)
    s.text(28, 34, "浏览器工具栏上的 Zotero 连接器：三种状态", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "图标的样子会变，变化本身就说明了当前页面能不能抓", size=12.5, fill=TXT3)

    rows = [("灰色 / 空心", "当前页面没有可识别的文献信息", "回到文献详情页或结果列表页再试", TXT3),
            ("图书 / 页面图标", "识别到单个条目，点击可保存这一条", "点击 → 选择分类 → 保存", GREEN),
            ("文件夹图标", "识别到列表页，可以批量勾选多条", "点击 → 勾选文献 → 选择分类 → 保存", BLUE)]
    y = 84
    for i, (state, mean, how, c) in enumerate(rows):
        s.rect(28, y, 884, 84, fill="#ffffff", stroke=BORDER2, rx=8)
        s.rect(28, y, 5, 84, fill=c, rx=2.5)
        s.circle(78, y + 42, 16, fill=c, op=0.15)
        s.text(78, y + 48, ["◌", "▤", "▣"][i], size=15, fill=c, anchor="middle")
        s.text(112, y + 34, state, size=13, fill=TXT, weight="700")
        s.text(112, y + 58, mean, size=11.5, fill=TXT2)
        s.text(600, y + 34, "操作：", size=11, fill=TXT3)
        s.text(640, y + 34, how, size=11.5, fill=TXT2)
        y += 96

    s.rect(28, y + 4, 884, 96, fill="#fafbfd", stroke=BORDER, rx=8)
    s.text(48, y + 30, "在知网页面点击连接器后弹出的窗口", size=12.5, fill=TXT, weight="700")
    s.rect(300, y + 16, 340, 68, fill="#ffffff", stroke=BORDER, rx=8)
    s.text(320, y + 40, "保存到 Zotero", size=12, fill=TXT, weight="700")
    s.check(320, y + 50, 12, on=True)
    s.text(338, y + 61, "我的文库", size=11, fill=TXT2)
    s.check(320, y + 68, 12, on=True)
    s.text(338, y + 79, "毕业论文：加计扣除与企业创新", size=11, fill=TXT2)
    s.rect(556, y + 60, 68, 22, fill=BLUE, rx=4)
    s.text(590, y + 75, "完成", size=11, fill="#ffffff", anchor="middle")
    s.text(48, y + 56, "勾选目标分类后点“完成”，", size=11.5, fill=TXT2)
    s.text(48, y + 76, "条目就会出现在 Zotero 中间栏。", size=11.5, fill=TXT2)
    s.text(660, y + 56, "若窗口中没有想要的分类，", size=11, fill=TXT3)
    s.text(660, y + 76, "先在 Zotero 里新建分类再抓取。", size=11, fill=TXT3)
    s.watermark()
    return save(s, os.path.join(OUT, "z05-connector-toolbar.svg"))


# ------------------------------------------------- z06 茉莉花插件安装
def z06():
    s = S(960, 626)
    cx, cy, cw, ch = appshell(s, 24, 20, 912, 500, title="Zotero")
    lw, mw = 210, 300
    rw = cw - lw - mw - 2
    rx0 = cx + lw
    rx2 = cx + lw + mw
    s.rect(cx, cy, lw, ch, fill="#fafbfd")
    s.line(rx0, cy, rx0, cy + ch, stroke=BORDER)
    for i, t in enumerate(["我的文库", "课程资料", "毕业论文"]):
        s.text(cx + 16, cy + 30 + i * 24, t, size=11.5, fill=TXT2, weight="700" if i == 0 else "400")
    s.rect(rx0, cy, mw, ch, fill="#ffffff")
    s.line(rx2, cy, rx2, cy + ch, stroke=BORDER)
    s.rect(rx2, cy, rw, ch, fill="#ffffff")

    # 插件管理弹窗
    s.rect(cx + 150, cy + 30, 620, 400, fill="#ffffff", stroke=BORDER, rx=8)
    s.rect(cx + 150, cy + 30, 620, 40, fill=BAR, rx=8)
    s.rect(cx + 150, cy + 58, 620, 12, fill=BAR)
    s.text(cx + 172, cy + 56, "插件", size=13, fill=TXT, weight="700")
    s.text(cx + 726, cy + 56, "⚙", size=14, fill=TXT2, anchor="middle")
    s.line(cx + 150, cy + 70, cx + 770, cy + 70, stroke=BORDER)

    s.text(cx + 172, cy + 96, "茉莉花（Jasminum）", size=12.5, fill=TXT, weight="700")
    s.text(cx + 330, cy + 96, "1.0.x", size=11, fill=TXT3)
    s.text(cx + 172, cy + 116, "中文文献增强：抓取知网元数据、下载 PDF、拆分作者姓名",
           size=11, fill=TXT2)
    s.rect(cx + 680, cy + 84, 70, 24, fill=GREY_L, stroke=BORDER, rx=4)
    s.text(cx + 715, cy + 100, "选项", size=11, fill=TXT2, anchor="middle")
    s.line(cx + 172, cy + 134, cx + 748, cy + 134, stroke=BORDER2)
    s.text(cx + 172, cy + 160, "Zotero 中文社区插件商店（可选）", size=12.5, fill=TXT, weight="700")
    s.text(cx + 172, cy + 180, "1.0.x", size=11, fill=TXT3)
    s.line(cx + 172, cy + 198, cx + 748, cy + 198, stroke=BORDER2)

    # 齿轮菜单
    s.rect(cx + 626, cy + 52, 168, 96, fill="#ffffff", stroke=BORDER, rx=6)
    for i, (t, on) in enumerate([("Install Plugin From File…", True),
                                 ("Check for Updates", False),
                                 ("Reset Translators", False),
                                 ("Disable All Plugins", False)]):
        if on:
            s.rect(cx + 628, cy + 54 + i * 23, 164, 22, fill=BLUE_L)
        s.text(cx + 638, cy + 69 + i * 23, t, size=10.5, fill=BLUE if on else TXT2)

    steps = ["1  到 Zotero 中文社区或 GitHub 仓库下载与当前版本匹配的 .xpi 文件",
             "2  Zotero 菜单：工具 → 插件",
             "3  点击插件面板右上角齿轮 → Install Plugin From File…",
             "4  选择刚下载的 .xpi 文件并确认",
             "5  重启 Zotero，回到插件面板确认已启用"]
    yy = cy + 276
    for t in steps:
        s.text(cx + 172, yy, t, size=11.5, fill=TXT2)
        yy += 26
    s.rect(cx + 172, cy + 412, 576, 0, fill="none")
    s.badge(cx + 136, cy + 58, 1)
    s.note(cx + 150, cy + 428, 620,
           ["第三方插件由社区维护，务必从官方仓库或中文社区下载，不要使用来源不明的安装包；",
            "Zotero 大版本升级后插件可能暂时不兼容，需要等待作者适配或重新安装。"],
           fill=YELLOW_L, stroke=YEL_B, tcolor="#8a6100", size=11, lh=17)
    s.watermark()
    return save(s, os.path.join(OUT, "z06-jasminum-install.svg"))


# ------------------------------------------------- z07 保存弹窗
def z07():
    s = S(940, 460)
    s.rect(0, 0, 940, 460, fill=BG)
    s.rect(60, 30, 560, 400, fill="#ffffff", stroke=BORDER, rx=8)
    s.text(84, 62, "检索结果（知网）", size=13, fill=TXT2, weight="700")
    for i in range(5):
        s.text(84, 92 + i * 26, "□ 研发费用加计扣除与" + ["企业创新", "研发投入", "创新绩效",
                                                          "中小企业", "税收征管"][i] + "研究",
               size=11.5, fill=TXT2)
    s.rect(60, 30, 560, 400, fill="#8892a0", op=0.45)

    s.rect(400, 130, 480, 260, fill="#ffffff", stroke=BORDER, rx=10)
    s.rect(400, 130, 480, 42, fill=BAR, rx=10)
    s.rect(400, 160, 480, 12, fill=BAR)
    s.text(422, 157, "选择分类", size=13, fill=TXT, weight="700")
    s.text(858, 157, "✕", size=13, fill=TXT3, anchor="middle")
    s.line(400, 172, 880, 172, stroke=BORDER)
    s.rect(418, 188, 444, 128, fill="#fafbfd", stroke=BORDER2, rx=6)
    nodes = [("我的文库", 0, False), ("课程：文献检索与研究方法", 1, False),
             ("毕业论文：加计扣除与企业创新", 1, False), ("　01 政策与背景", 2, False),
             ("　02 理论与机制", 2, True), ("　03 实证与数据方法", 2, False),
             ("　04 国外经验与比较", 2, False)]
    ny = 208
    for t, lv, on in nodes:
        s.check(432 + lv * 16, ny - 10, 12, on=on)
        s.text(452 + lv * 16, ny, t, size=11, fill=TXT2)
        ny += 16
    s.text(418, 338, "勾选多个分类时，条目会同时出现在这些分类里（不产生副本）", size=10.5, fill=TXT3)
    s.rect(700, 352, 76, 26, fill=BLUE, rx=5)
    s.text(738, 370, "完成", size=12, fill="#ffffff", anchor="middle", weight="600")
    s.rect(786, 352, 76, 26, fill="#ffffff", stroke=BORDER, rx=5)
    s.text(824, 370, "取消", size=12, fill=TXT2, anchor="middle")

    s.badge(390, 151, 1)
    s.badge(390, 232, 2)
    s.badge(390, 356, 3)
    s.note(60, 350, 300,
           ["① 弹出窗口标题为“选择分类”",
            "② 勾选保存目标分类，可多选",
            "③ 点“完成”后回到 Zotero 查看条目"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2, size=11)
    s.watermark()
    return save(s, os.path.join(OUT, "z07-cnki-save-dialog.svg"))


# ------------------------------------------------- z08 拖动识别
def z08():
    s = S(1020, 640)
    s.text(28, 34, "拖动识别：把知网文献拖进 Zotero", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "左右分屏，按住条目标题直接拖过去即可，落点决定结果", size=12.5, fill=TXT3)

    # 左：浏览器
    bx, by, bw, bh = 28, 84, 470, 380
    s.rect(bx, by, bw, bh, fill="#ffffff", stroke=BORDER, rx=8)
    s.rect(bx, by, bw, 30, fill=BAR, rx=8)
    s.rect(bx, by + 20, bw, 10, fill=BAR)
    s.text(bx + 14, by + 20, "知网检索结果页", size=11, fill=TXT2)
    s.line(bx, by + 30, bx + bw, by + 30, stroke=BORDER)
    s.rect(bx + 10, by + 40, bw - 20, 24, fill="#f7f9fb")
    s.text(bx + 20, by + 56, "找到 1,842 条结果　相关度 ▾", size=10.5, fill=TXT3)
    iy = by + 78
    for i in range(4):
        s.rect(bx + 10, iy, bw - 20, 68, fill="#ffffff", stroke=BORDER2, rx=5)
        t = ["研发费用加计扣除政策与企业创新投入——基于双重差分法的经验证据",
             "税收优惠、融资约束与高新技术企业研发投入",
             "加计扣除比例调整对企业创新绩效的影响研究",
             "研发费用加计扣除政策的执行问题与优化建议"][i]
        tcol = BLUE
        s.rect(bx + 10, iy, bw - 20, 68, fill=BLUE_L if i == 0 else "#ffffff", rx=5)
        s.text(bx + 20, iy + 22, t[:26], size=10.5, fill=tcol)
        s.text(bx + 20, iy + 40, "税务研究　2023, (05): 12-20", size=10, fill=TXT2)
        s.text(bx + 20, iy + 56, "被引 34　下载 2,105", size=10, fill=TXT3)
        iy += 74
    s.rect(bx + 10, by + 60, bw - 20, 76, fill="none", stroke=ORANGE, sw=2, dash="6 4", rx=5)

    # 右：Zotero
    zx, zy, zw, zh = 596, 84, 396, 380
    zcx, zcy, zcw, zch = s.window(zx, zy, zw, zh, title="Zotero", app=True)
    s.rect(zcx, zcy, zcw, 30, fill=BAR2)
    s.line(zcx, zcy + 30, zcx + zcw, zcy + 30, stroke=BORDER)
    for i, g in enumerate(["＋", "▣", "⚯", "✎", "⌕", "↻"]):
        s.circle(zcx + 20 + i * 26, zcy + 15, 9, fill=GREY_L)
        s.text(zcx + 20 + i * 26, zcy + 20, g, size=11, fill=TXT2, anchor="middle")
    s.rect(zcx, zcy + 30, 128, zch - 30, fill="#fafbfd")
    s.line(zcx + 128, zcy + 30, zcx + 128, zcy + zch, stroke=BORDER)
    for i, t in enumerate(["我的文库", "课程资料", "毕业论文", "　政策与背景", "　理论与机制"]):
        s.text(zcx + 10, zcy + 52 + i * 20, t, size=10, fill=TXT2)
    s.rect(zcx + 128, zcy + 30, zcw - 128, zch - 30, fill="#ffffff")
    s.rect(zcx + 128, zcy + 30, zcw - 128, 24, fill="#fdfdfd")
    s.text(zcx + 140, zcy + 47, "标题", size=10, fill=TXT3)
    s.text(zcx + 300, zcy + 47, "年份", size=10, fill=TXT3)
    s.line(zcx + 128, zcy + 54, zcx + zcw, zcy + 54, stroke=BORDER2)
    for i, t in enumerate(["学位论文・财税政策研究", "加计扣除与企业创新（待读）",
                           "中国税收优惠政策汇编"]):
        s.text(zcx + 140, zcy + 76 + i * 22, t, size=10, fill=TXT2)
    s.rect(zcx + 130, zcy + 60, zcw - 134, 84, fill="none", stroke=GREEN, sw=2, dash="6 4", rx=5)

    s.arrow(bx + bw - 6, by + 96, zx - 6, zy + 100, color=ORANGE, sw=2.6)
    s.text(bx + bw + 6, by + 78, "拖到中间栏空白处", size=11, fill=ORANGE, weight="700")
    s.text(bx + bw + 6, by + 92, "→ 自动创建条目并抓取题录", size=10.5, fill=TXT2)

    cards = [("落点一：中间栏空白处", "新建条目，并从网页抓取题录", ORANGE),
             ("落点二：已有条目上", "把 PDF 作为附件挂到该条目下，不新建条目", GREEN),
             ("落点三：左栏某个分类上", "新建条目并直接归入该分类", BLUE),
             ("落点四：拖动本地 PDF 文件", "自动联网识别题录；识别失败需手工补字段", PURPLE)]
    cy2 = 480
    for i, (t, d, c) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = 28 + col * 484
        y = cy2 + row * 62
        s.rect(x, y, 460, 52, fill="#ffffff", stroke=BORDER2, rx=8)
        s.rect(x, y, 4, 52, fill=c, rx=2)
        s.text(x + 18, y + 22, t, size=12, fill=TXT, weight="700")
        s.text(x + 18, y + 40, d, size=11, fill=TXT2)
    s.note(28, 608, 932, [], title="", fill="none", stroke="none")
    s.watermark()
    return save(s, os.path.join(OUT, "z08-drag-to-identify.svg"))


# ------------------------------------------------- z09 知网下载 PDF
def z09():
    s = S(960, 520)
    s.text(28, 34, "在知网下载全文，并挂到 Zotero 条目上", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "三条路径：插件下载 / 手工下载后拖入 / 查找可用 PDF", size=12.5, fill=TXT3)

    bx, by, bw, bh = 28, 84, 540, 300
    s.rect(bx, by, bw, bh, fill="#ffffff", stroke=BORDER, rx=8)
    s.rect(bx, by, bw, 30, fill=BAR, rx=8)
    s.rect(bx, by + 20, bw, 10, fill=BAR)
    s.text(bx + 14, by + 20, "知网文献详情页", size=11, fill=TXT2)
    s.line(bx, by + 30, bx + bw, by + 30, stroke=BORDER)
    s.text(bx + 20, by + 62, "研发费用加计扣除政策与企业创新投入", size=13, fill=BLUE, weight="500")
    s.text(bx + 20, by + 84, "张伟, 李娜, 王强　税务研究　2023, (05): 12-20", size=10.5, fill=TXT2)
    s.line(bx + 20, by + 98, bx + bw - 20, by + 98, stroke=BORDER2)
    s.rect(bx + 20, by + 110, 112, 32, fill=CNKI, rx=5)
    s.text(bx + 76, by + 131, "PDF 下载", size=12, fill="#ffffff", anchor="middle", weight="600")
    s.rect(bx + 142, by + 110, 112, 32, fill="#ffffff", stroke=CNKI, rx=5)
    s.text(bx + 198, by + 131, "CAJ 下载", size=12, fill=CNKI, anchor="middle", weight="600")
    s.text(bx + 270, by + 131, "HTML 阅读", size=11.5, fill=TXT2)
    s.text(bx + 20, by + 166, "提示：知网全文需要机构订阅，请先登录并确认处于学校许可范围内。",
           size=10.5, fill=TXT3)
    s.rect(bx + 20, by + 188, bw - 40, 90, fill=YELLOW_L, stroke=YEL_B, rx=6)
    s.text(bx + 36, by + 212, "CAJ 与 PDF 的区别", size=11.5, fill="#8a6100", weight="700")
    s.text(bx + 36, by + 232, "CAJ 是知网自有格式，Zotero 内置阅读器无法直接打开；", size=10.5, fill="#8a6100")
    s.text(bx + 36, by + 250, "能用 PDF 就用 PDF，只有 CAJ 时可用 CAJViewer 转出 PDF。", size=10.5, fill="#8a6100")

    zx, zy = 596, 84
    s.rect(zx, zy, 336, 300, fill="#ffffff", stroke=BORDER, rx=8)
    s.text(zx + 16, zy + 28, "Zotero：右键菜单中的条目操作", size=11.5, fill=TXT, weight="700")
    s.line(zx + 16, zy + 40, zx + 320, zy + 40, stroke=BORDER2)
    for i, (t, on) in enumerate([("添加附件", False), ("添加笔记", False),
                                 ("抓取知网元数据（茉莉花）", True),
                                 ("下载 PDF（茉莉花）", True),
                                 ("查找可用的 PDF", True),
                                 ("抓取 PDF 元数据", True),
                                 ("移至回收站", False)]):
        if on:
            s.rect(zx + 8, zy + 52 + i * 28, 320, 24, fill=BLUE_L, rx=4)
        s.text(zx + 20, zy + 68 + i * 28, t, size=11, fill=BLUE if on else TXT2)
    s.text(zx + 16, zy + 268, "带高亮的三项由茉莉花插件提供", size=10.5, fill=TXT3)
    s.line(zx + 16, zy + 278, zx + 320, zy + 278, stroke=BORDER2)

    s.badge(bx + 8, by + 127, 1)
    s.badge(zx + 4, zy + 127, 2)
    s.note(28, 400, 904,
           ["路径一：登录知网 → 详情页下载 PDF → 把 PDF 从“下载”文件夹拖到 Zotero 中对应条目上（作为附件）。",
            "路径二：在 Zotero 中选中条目 → 右键 → 使用茉莉花插件的“下载 PDF”，由插件请求知网接口下载并自动挂为附件。",
            "路径三：右键 → “查找可用的 PDF”，由 Zotero 在公开来源里检索，中文文献成功率有限。"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.text(28, 500, "使用提醒：全文下载仅限本人学习研究，不得批量下载或传播，否则可能导致学校 IP 被数据库封禁。",
           size=11.5, fill=RED)
    s.watermark()
    return save(s, os.path.join(OUT, "z09-cnki-download-pdf.svg"))


# ------------------------------------------------- z10 分类树
def z10():
    s = S(940, 470)
    s.text(28, 34, "左栏资料库与分类树", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "分类按“研究任务”划分，层级不超过三层", size=12.5, fill=TXT3)
    s.rect(28, 78, 420, 372, fill="#fafbfd", stroke=BORDER, rx=8)
    tree = [("我的文库", 0, False, True), ("课程：文献检索与研究方法", 1, False, False),
            ("01 检索方法与规范", 2, False, False), ("02 学术道德与引用", 2, False, False),
            ("03 文献综述写作", 2, False, False),
            ("毕业论文：研发费用加计扣除与企业创新", 1, True, False),
            ("01 政策与背景", 2, True, False), ("02 理论与机制", 2, True, False),
            ("03 实证与数据方法", 2, False, False), ("04 国外经验与比较", 2, False, False),
            ("05 待读文献", 2, False, False),
            ("重复条目", 0, False, False), ("未分类条目", 0, False, False),
            ("回收站", 0, False, False)]
    y = 106
    for name, lv, on, bold in tree:
        if on:
            s.rect(36, y - 14, 400, 22, fill=BLUE_L, rx=4)
        if lv == 0:
            s.caret(44, y - 9, 5)
            s.text(60, y, name, size=12, fill=BLUE if on else TXT, weight="700")
        elif lv == 1:
            s.caret(62, y - 9, 5)
            s.text(78, y, name, size=11.5, fill=BLUE if on else TXT2, weight="700")
        else:
            s.rect(82, y - 11, 11, 11, fill="#f5d28a" if not on else "#ffffff",
                   stroke=ORANGE if not on else BLUE, rx=2)
            s.text(102, y, name, size=11.5, fill=BLUE if on else TXT2)
        y += 24

    s.rect(468, 78, 444, 176, fill="#ffffff", stroke=BORDER2, rx=8)
    s.text(488, 106, "分类与标签的分工", size=12.5, fill=TXT, weight="700")
    rows = [("分类 Collection", "回答“属于哪个研究任务”", "同一层级内是排他的"),
            ("标签 Tag", "回答“现在什么状态、用在哪里”", "每条可以有多个")]
    ry = 126
    for a, b, c in rows:
        s.text(488, ry, a, size=11.5, fill=BLUE, weight="700")
        s.text(488, ry + 20, b, size=11, fill=TXT2)
        s.text(488, ry + 38, c, size=11, fill=TXT3)
        ry += 62
    s.rect(468, 270, 444, 180, fill="#ffffff", stroke=BORDER2, rx=8)
    s.text(488, 298, "操作要点", size=12.5, fill=TXT, weight="700")
    for i, t in enumerate(["· 新建分类：工具栏黄色文件夹按钮或右键“新建分类”",
                           "· 拖拽条目到分类：按住 Ctrl/Cmd 拖 = 加入而不移出原分类",
                           "· 从分类移除：右键“从分类中移除”，条目仍保留在我的文库",
                           "· 删除分类不会删除条目，删除条目才会进回收站",
                           "· 分类名不要用“新建分类 1”，要写清研究任务"]):
        s.text(488, 326 + i * 24, t, size=11, fill=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "z10-collections-tree.svg"))


# ------------------------------------------------- z11 标签面板
def z11():
    s = S(940, 562)
    s.text(28, 34, "标签体系与标签过滤器", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "标签按用途分三类，控制在十几个以内", size=12.5, fill=TXT3)

    groups = [("阅读状态", GREEN, ["未读", "阅读中", "已读", "重要"]),
              ("文献类型", PURPLE, ["综述", "理论", "实证", "政策文件", "学位论文"]),
              ("使用位置", BLUE, ["背景", "机制", "方法", "对策", "文献综述"])]
    y = 84
    for name, c, tags in groups:
        s.text(28, y + 18, name, size=12.5, fill=c, weight="700")
        tx = 130
        for t in tags:
            tx = s.chip(tx, y, t, fill=c, color="#ffffff", size=11, h=24, pad=10) + 8
        y += 44
    s.line(28, y + 4, 912, y + 4, stroke=BORDER2)

    s.rect(28, y + 20, 430, 300, fill="#fafbfd", stroke=BORDER, rx=8)
    s.text(46, y + 46, "左下角标签过滤器", size=12, fill=TXT, weight="700")
    s.text(46, y + 66, "按标签名排序 ▾", size=10.5, fill=TXT3)
    ty = y + 82
    for t, c, cnt in [("已读", GREEN, 36), ("阅读中", ORANGE, 8), ("未读", TXT3, 22),
                      ("重要", RED, 6), ("实证", BLUE, 24), ("综述", PURPLE, 7),
                      ("政策文件", GREEN, 11), ("机制", ORANGE, 15), ("方法", BLUE, 13)]:
        s.rect(46, ty, 10, 10, fill=c, rx=2)
        s.text(64, ty + 10, t, size=11.5, fill=TXT2)
        s.text(170, ty + 10, str(cnt) + " 条", size=10.5, fill=TXT3)
        if t in ("已读", "实证"):
            s.circle(200, ty + 5, 8, fill=c, op=0.18)
            s.text(200, ty + 9, "✓", size=9, fill=c, anchor="middle")
        ty += 22
    s.text(46, ty + 26, "点击标签即筛选；再点一次取消", size=10.5, fill=TXT3)
    s.text(46, ty + 44, "按住 Ctrl 可多选标签（交集筛选）", size=10.5, fill=TXT3)

    s.rect(478, y + 20, 434, 300, fill="#ffffff", stroke=BORDER2, rx=8)
    s.text(498, y + 46, "标签的四个操作入口", size=12.5, fill=TXT, weight="700")
    steps = [("在右栏“标签”页添加", "选中条目 → 右栏标签页 → 添加 → 输入标签名"),
             ("拖到左下角标签上", "把条目拖到某个标签名上，直接加上该标签"),
             ("右键标签 → 分配颜色", "给常用标签配色，筛选时更容易识别"),
             ("重命名 / 删除标签", "右键标签选择重命名或删除；删除不会删条目")]
    sy = y + 72
    for t, d in steps:
        s.rect(498, sy, 394, 52, fill=GREY_L, rx=6)
        s.text(512, sy + 22, t, size=11.5, fill=TXT, weight="700")
        s.text(512, sy + 40, d, size=10.5, fill=TXT2)
        sy += 60
    s.watermark()
    return save(s, os.path.join(OUT, "z11-tags-panel.svg"))


# ------------------------------------------------- z12 信息栏字段
def z12():
    s = S(960, 560)
    s.text(28, 34, "右栏“信息”面板：题录字段逐个看", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "字段随“条目类型”变化；校对题录就是在这里改", size=12.5, fill=TXT3)
    s.rect(28, 78, 520, 462, fill="#ffffff", stroke=BORDER, rx=8)
    for i, t in enumerate(["信息", "摘要", "附件", "笔记", "标签", "相关"]):
        s.text(48 + i * 60, 106, t, size=11.5, fill=BLUE if i == 0 else TXT2,
               weight="700" if i == 0 else "400")
    s.rect(44, 114, 30, 2.5, fill=BLUE)
    s.line(44, 120, 532, 120, stroke=BORDER2)
    fields = [("条目类型", "期刊论文", True), ("标题", "研发费用加计扣除政策与企业创新投入", False),
              ("作者", "张伟　李娜　王强", False), ("出版物", "税务研究", False),
              ("卷", "—", False), ("期", "05", False), ("页码", "12-20", False),
              ("日期", "2023-05-15", False), ("DOI", "10.xxxx/xxxxx", False),
              ("URL", "https://kns.cnki.net/…", False), ("语言", "zh-CN", False),
              ("期刊缩写", "—", False), ("ISSN", "1003-448X", False),
              ("其它", "—", False)]
    fy = 148
    for k, v, is_sel in fields:
        s.text(48, fy, k, size=11, fill=TXT3)
        if is_sel:
            s.rect(150, fy - 15, 368, 22, fill="#ffffff", stroke=BLUE, rx=3)
        s.text(158, fy, v, size=11.5, fill=TXT2 if v != "—" else TXT4)
        s.line(150, fy + 8, 518, fy + 8, stroke=BORDER2, sw=0.8)
        fy += 27

    items = [("条目类型", "期刊论文 / 学位论文 / 会议论文 / 图书 / 网页，选错会改变可用字段"),
             ("作者", "注意区分“姓名”与“机构”两种作者类型；用上下箭头调整顺序"),
             ("出版物", "填期刊全称，不要用简称"),
             ("卷 / 期 / 页码", "中文期刊常只标期号；页码不要带多余符号"),
             ("日期", "格式为 YYYY-MM-DD，知网导出的日期偶有出错"),
             ("DOI", "没有可留空，不要填数据库链接"),
             ("语言", "填 zh-CN 或 en，影响后续排序与样式")]
    y = 84
    for k, d in items:
        s.text(576, y, k, size=12, fill=TXT, weight="700")
        s.text(576, y + 18, d, size=11, fill=TXT2)
        y += 64
    s.watermark()
    return save(s, os.path.join(OUT, "z12-metadata-panel.svg"))


# ------------------------------------------------- z13 PDF 阅读器
def z13():
    s = S(1000, 600)
    cx, cy, cw, ch = s.window(20, 16, 960, 560, title="阅读器", app=True)
    s.rect(cx, cy, cw, 36, fill=BAR2)
    s.line(cx, cy + 36, cx + cw, cy + 36, stroke=BORDER)
    tools = [("✎", "选择文字"), ("▮", "高亮"), ("_", "下划线"), ("▤", "便签"),
             ("⬚", "区域截图"), ("⊞", "显示缩略图"), ("⌕", "查找")]
    for i, (g, tip) in enumerate(tools):
        on = i in (1, 3, 4)
        if on:
            s.rect(cx + 14 + i * 32, cy + 7, 28, 22, fill=BLUE_L, rx=5)
        s.text(cx + 28 + i * 32, cy + 22, g, size=12, fill=BLUE if on else TXT2, anchor="middle")
    for i, c in enumerate([YEL_B, "#b7e2a8", "#ffc8c8", BLUE_B]):
        s.circle(cx + 300 + i * 24, cy + 18, 8, fill=c)
        if i == 0:
            s.circle(cx + 300, cy + 18, 11, fill="none", stroke=TXT2, sw=1.4)
    s.text(cx + 420, cy + 23, "第 3 / 18 页", size=11, fill=TXT2)
    s.text(cx + cw - 40, cy + 23, "✕", size=13, fill=TXT3, anchor="middle")

    # 页面区
    px, py, pw, ph = cx + 96, cy + 52, cw - 96 - 240, ch - 68
    s.rect(px, py, pw, ph, fill="#f3f4f6")
    s.rect(px + 24, py + 14, pw - 48, ph - 28, fill="#ffffff", stroke=BORDER2)
    ly = py + 46
    for i in range(3):
        s.text(px + 46, ly, "1." + str(i + 1) + "  Previous literature has documented "
               "the effect of tax incentives on innovation.", size=9.5, fill=TXT3)
        ly += 20
    s.rect(px + 42, ly - 12, pw - 130, 20, fill=YEL_B, op=0.7, rx=3)
    s.text(px + 46, ly + 2, "2.1  Policy background：2015 年研发费用加计扣除政策扩围，", size=9.5, fill=TXT)
    ly += 22
    s.text(px + 46, ly, "将适用范围由科技型中小企业扩大至全部企业。", size=9.5, fill=TXT)
    ly += 30
    for i in range(4):
        s.text(px + 46, ly, "We find a significant and positive effect on R&D "
               "expenditure of eligible firms.", size=9.5, fill=TXT3)
        ly += 20
    s.rect(px + 42, ly - 12, pw - 200, 20, fill="#b7e2a8", op=0.6, rx=3)
    s.text(px + 46, ly + 2, "表 2 基准回归结果：加计扣除对企业研发投入的影响", size=9.5, fill=TXT)

    # 批注侧栏
    ax = cx + cw - 240
    s.rect(ax, cy + 36, 240, ch - 36, fill="#fafbfd")
    s.line(ax, cy + 36, ax, cy + ch, stroke=BORDER)
    s.text(ax + 14, cy + 60, "批注", size=11.5, fill=TXT, weight="700")
    s.text(ax + 190, cy + 60, "＋", size=12, fill=TXT3, anchor="middle")
    s.line(ax + 14, cy + 72, ax + 226, cy + 72, stroke=BORDER2)
    anns = [("高亮", YEL_B, "2.1 Policy background：2015 年研发费用加计扣除政策扩围……"),
            ("便签", ORANGE, "自己的判断：政策时间点与我设定的一致，可作准自然实验依据"),
            ("区域截图", GREEN, "表 2 基准回归结果，记下系数与显著性"),
            ("下划线", BLUE_B, "We find a significant and positive effect …")]
    ay = cy + 88
    for idx, (kind, c, txt) in enumerate(anns):
        s.rect(ax + 12, ay, 216, 74, fill="#ffffff", stroke=BORDER2, rx=6)
        s.rect(ax + 12, ay, 4, 74, fill=c, rx=2)
        s.text(ax + 24, ay + 18, kind, size=10, fill=TXT3)
        s.text(ax + 24, ay + 36, txt[:20], size=10, fill=TXT2)
        if len(txt) > 20:
            s.text(ax + 24, ay + 52, txt[20:40], size=10, fill=TXT2)
        s.text(ax + 24, ay + 68, "第 " + str(3 + idx) + " 页", size=9.5, fill=TXT3)
        ay += 82

    s.badge(cx - 8, cy + 18, 1)
    s.badge(ax - 8, cy + 60, 2)
    s.badge(px + 20, py + ph - 20, 3)
    s.watermark()
    return save(s, os.path.join(OUT, "z13-pdf-reader.svg"))


# ------------------------------------------------- z14 笔记
def z14():
    s = S(940, 480)
    s.text(28, 34, "从批注到笔记：条目与子条目的结构", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "笔记挂在条目下面，可以随条目一起导出与备份", size=12.5, fill=TXT3)

    s.rect(28, 78, 520, 240, fill="#ffffff", stroke=BORDER, rx=8)
    s.text(46, 106, "中间栏：条目与子条目", size=12, fill=TXT, weight="700")
    s.line(46, 118, 530, 118, stroke=BORDER2)
    tree = [("研发费用加计扣除政策与企业创新投入", 0, True, "⚯"),
            ("阅读笔记：政策背景与识别策略", 1, False, "✎"),
            ("阅读笔记：变量与数据来源", 1, False, "✎"),
            ("税收优惠、融资约束与高新技术企业研发投入", 0, False, "⚯"),
            ("阅读笔记：机制检验部分", 1, False, "✎"),
            ("加计扣除比例调整对企业创新绩效的影响", 0, False, "⚯")]
    y = 142
    for t, lv, on, ic in tree:
        if on:
            s.rect(40, y - 14, 486, 22, fill=BLUE)
        if lv:
            s.path("M %d %d l 6 5 l -6 5" % (60, y - 9), fill="none", stroke=TXT3, sw=1.4)
        s.text(76 + lv * 20, y, ic, size=10, fill="#ffffff" if on else TXT3)
        s.text(94 + lv * 20, y, t, size=11, fill="#ffffff" if on else TXT2)
        y += 28
    s.text(46, 300, "三角箭头展开后可看到该条目下的全部笔记", size=10.5, fill=TXT3)

    s.rect(568, 78, 344, 240, fill="#ffffff", stroke=BORDER2, rx=8)
    s.text(586, 106, "笔记的三层结构", size=12, fill=TXT, weight="700")
    layers = [("① 内容摘要", "作者研究了什么、用什么材料、得出什么结论", BLUE),
              ("② 证据摘录", "可核对的原文、页码、表格位置（标明是原文）", GREEN),
              ("③ 我的判断", "对我选题有什么用、有什么局限、能否比较", ORANGE)]
    ly = 124
    for t, d, c in layers:
        s.rect(586, ly, 308, 58, fill=GRAY if False else GREY_L, rx=6)
        s.rect(586, ly, 4, 58, fill=c, rx=2)
        s.text(600, ly + 22, t, size=11.5, fill=c, weight="700")
        s.text(600, ly + 42, d[:26], size=10.5, fill=TXT2)
        if len(d) > 26:
            s.text(600, ly + 54, d[26:], size=10.5, fill=TXT2)
        ly += 66

    s.rect(28, 336, 884, 118, fill=YELLOW_L, stroke=YEL_B, rx=8)
    s.text(48, 362, "笔记示例（节选）", size=12, fill="#8a6100", weight="700")
    s.text(48, 384, "【内容摘要】以 2015 年加计扣除政策扩围为准自然实验，用 2012—2020 年 A 股高新技术企业面板数据，DID 检验政策对研发投入的影响。",
           size=11, fill="#8a6100")
    s.text(48, 404, "【证据摘录】原文第 8 页：“政策显著提高了处理组企业的研发投入强度，且在融资约束较强的中小企业中更明显。”",
           size=11, fill="#8a6100")
    s.text(48, 424, "【我的判断】政策时点与本文一致，可作为政策背景论据；但样本为上市公司，小微企业结论需谨慎外推，可作为本文局限讨论。",
           size=11, fill="#8a6100")
    s.watermark()
    return save(s, os.path.join(OUT, "z14-item-notes.svg"))


# ------------------------------------------------- z15 Word 选项卡
def z15():
    s = S(960, 506)
    cx, cy, cw, ch = s.window(28, 24, 904, 420, title="论文初稿.docx - Word",
                              app=False, url="")
    s.rect(cx, cy, cw, 30, fill="#f3f6fa")
    for i, t in enumerate(["开始", "插入", "设计", "布局", "引用", "邮件", "审阅", "视图", "Zotero"]):
        on = t == "Zotero"
        s.rect(cx + 12 + i * 56, cy + 3, 52, 24, fill=BLUE_L if on else "none", rx=4)
        s.text(cx + 38 + i * 56, cy + 20, t, size=11.5, fill=BLUE if on else TXT2,
               weight="700" if on else "400")
    top = cy + 30
    s.rect(cx, top, cw, 74, fill="#f7f9fb")
    s.line(cx, top + 74, cx + cw, top + 74, stroke=BORDER)
    btns = [("Add/Edit Citation", BLUE, "#ffffff", "插入 / 编辑文内引用"),
            ("Add Note", "#ffffff", TXT2, "插入脚注式说明"),
            ("Add/Edit Bibliography", "#ffffff", TXT2, "生成参考文献表"),
            ("Document Preferences", "#ffffff", TXT2, "选择引用样式"),
            ("Refresh", "#ffffff", TXT2, "刷新引用"),
            ("Unlink Citations", "#ffffff", TXT2, "解除域代码（谨慎）")]
    bx = cx + 24
    for label, bg, fg, tip in btns:
        w = max(tw(label, 11) + 24, 110)
        s.rect(bx, top + 10, w, 30, fill=bg, stroke=None if bg == BLUE else BORDER, rx=5)
        s.text(bx + w / 2, top + 30, label, size=11, fill=fg, anchor="middle",
               weight="600" if bg == BLUE else "400")
        s.text(bx + w / 2, top + 58, tip, size=10, fill=TXT3, anchor="middle")
        bx += w + 12

    s.rect(cx + 40, top + 100, cw - 80, 200, fill="#ffffff", stroke=BORDER2, rx=4)
    s.text(cx + 60, top + 132, "二、文献综述", size=13, fill=TXT, weight="700")
    s.text(cx + 60, top + 160, "已有研究普遍认为，研发费用加计扣除政策对企业创新投入具有显著促进作用（张伟等，2023）。",
           size=11.5, fill=TXT2)
    s.text(cx + 60, top + 184, "但也有研究指出，政策效果受到企业规模与融资约束的影响（陈晓明，2022）。",
           size=11.5, fill=TXT2)
    s.rect(cx + 400, top + 148, 128, 18, fill=GREY_L, stroke=BORDER2, rx=3)
    s.text(cx + 464, top + 161, "Zotero 域代码", size=9.5, fill=TXT3, anchor="middle")
    s.badge(cx + 16, top + 24, 1)
    s.badge(cx + 16, top + 122, 2)
    s.note(cx + 40, top + 312, cw - 80,
           ["① Zotero 选项卡只在 Word / WPS 中安装插件后出现，第一项「Add/Edit Citation」用于插入文内引用。",
            "② 灰色底纹表示这是 Zotero 生成的域代码，不是手打的文字；改题录后点 Refresh 即可全文更新。"],
           fill="#ffffff", stroke=BORDER2, tcolor=TXT2)
    s.watermark()
    return save(s, os.path.join(OUT, "z15-word-tab.svg"))


# ------------------------------------------------- z16 参考文献表
def z16():
    s = S(940, 520)
    s.text(28, 34, "自动生成的参考文献表（GB/T 7714-2015 样式）", size=16.5, fill=TXT, weight="700")
    s.text(28, 56, "由正文中实际引用的条目生成，条目顺序随引用顺序自动调整", size=12.5, fill=TXT3)
    s.rect(28, 78, 884, 300, fill="#ffffff", stroke=BORDER, rx=8)
    s.text(60, 112, "参考文献", size=14, fill=TXT, weight="700")
    refs = [
        "[1] 张伟, 李娜, 王强. 研发费用加计扣除政策与企业创新投入——基于双重差分法的经验证据[J]. 税务研究, 2023(05): 12-20.",
        "[2] 陈晓明. 税收优惠、融资约束与高新技术企业研发投入[J]. 财政研究, 2022(11): 45-58.",
        "[3] 刘洋, 赵敏. 加计扣除比例调整对企业创新绩效的影响研究[J]. 中央财经大学学报, 2024(02): 33-46.",
        "[4] SMITH J, WANG L, ROSSI M. R&D tax credits and firm innovation: Evidence from a quasi-natural",
        "     experiment[J]. Research Policy, 2024, 53(3): 104-126.",
        "[5] 王芳. 中国税收优惠政策的创新效应研究[D]. 北京: 中国人民大学, 2021.",
    ]
    y = 146
    for r in refs:
        s.text(60, y, r, size=11.5, fill=TXT2)
        y += 26
    s.line(28, 300, 912, 300, stroke=BORDER2)
    s.text(60, 330, "说明：上述条目由 Zotero 依据文库中的题录自动排版，中文用“等”还是全列、",
           size=11.5, fill=TXT3)
    s.text(60, 350, "英文作者是否大写、卷期页码的连接符，都由所选样式决定。", size=11.5, fill=TXT3)

    s.rect(28, 396, 884, 110, fill=YELLOW_L, stroke=YEL_B, rx=8)
    s.text(48, 420, "定稿前的双向核对法", size=12, fill="#8a6100", weight="700")
    s.text(48, 442, "从正文随机抽 10 条引用 → 在文末找到对应条目；再从文末随机抽 10 条文献 → 回到正文确认确实引用过。",
           size=11.5, fill="#8a6100")
    s.text(48, 462, "两个方向都要查，才能同时排除“正文引了但文末没有”和“文末列了但正文没引”两类错误。",
           size=11.5, fill="#8a6100")
    s.watermark()
    return save(s, os.path.join(OUT, "z16-bibliography.svg"))


# ------------------------------------------------- z17 同步设置
def z17():
    s = S(940, 480)
    s.rect(0, 0, 940, 480, fill=BG)
    s.rect(120, 30, 700, 420, fill="#ffffff", stroke=BORDER, rx=10)
    s.rect(120, 30, 700, 42, fill=BAR, rx=10)
    s.rect(120, 60, 700, 12, fill=BAR)
    s.text(146, 57, "设置", size=13, fill=TXT, weight="700")
    s.line(120, 72, 820, 72, stroke=BORDER)
    tabs = ["常规", "同步", "引用", "导出", "高级"]
    for i, t in enumerate(tabs):
        s.text(146 + i * 74, 100, t, size=11.5, fill=BLUE if t == "同步" else TXT2,
               weight="700" if t == "同步" else "400")
    s.rect(144, 108, 26, 2.5, fill=BLUE)
    s.line(120, 120, 820, 120, stroke=BORDER2)

    s.text(146, 150, "Zotero 同步", size=12.5, fill=TXT, weight="700")
    s.check(146, 162, 13, on=True)
    s.text(168, 173, "同步我的文库（题录、笔记、标签、分类结构）", size=11.5, fill=TXT2)
    s.text(168, 196, "账号：student@example.com", size=11, fill=TXT3)
    s.line(146, 216, 794, 216, stroke=BORDER2)

    s.text(146, 244, "文件同步（附件 PDF）", size=12.5, fill=TXT, weight="700")
    for i, (t, on, d) in enumerate([("Zotero 官方存储", True, "免费额度有限，超出需付费扩容"),
                                    ("WebDAV", False, "可用坚果云等支持 WebDAV 的服务"),
                                    ("不同步附件", False, "只同步题录，附件依赖本地备份")]):
        s.radio(158, 264 + i * 46, 6, on=on)
        s.text(176, 268 + i * 46, t, size=11.5, fill=TXT, weight="500")
        s.text(330, 268 + i * 46, d, size=11, fill=TXT3)
    s.line(146, 400, 794, 400, stroke=BORDER2)
    s.text(146, 424, "附件保存位置：数据目录内（默认）　　☐ 链接附件使用相对路径", size=11.5, fill=TXT2)
    s.badge(110, 173, 1)
    s.badge(110, 268, 2)
    s.badge(110, 424, 3)
    s.watermark()
    return save(s, os.path.join(OUT, "z17-sync-preferences.svg"))


# ------------------------------------------------- z18 重复条目
def z18():
    s = S(940, 470)
    cx, cy, cw, ch = appshell(s, 24, 20, 892, 430, title="Zotero")
    lw = 200
    rx0 = cx + lw
    s.rect(cx, cy, lw, ch, fill="#fafbfd")
    s.line(rx0, cy, rx0, cy + ch, stroke=BORDER)
    for i, t in enumerate(["我的文库", "课程资料", "毕业论文", "重复条目", "未分类条目", "回收站"]):
        on = t == "重复条目"
        if on:
            s.rect(cx + 4, cy + 20 + i * 24 - 13, lw - 8, 22, fill=BLUE_L, rx=4)
        s.text(cx + 16, cy + 20 + i * 24, t, size=11.5, fill=BLUE if on else TXT2,
               weight="700" if on else "400")
    s.rect(rx0, cy, cw - lw, ch, fill="#ffffff")
    s.text(rx0 + 14, cy + 20, "重复条目（部分示意）", size=11.5, fill=TXT, weight="700")
    s.line(rx0, cy + 32, rx0 + cw - lw, cy + 32, stroke=BORDER2)
    groups = [("研发费用加计扣除政策与企业创新投入", "张伟 等　税务研究　2023　DOI 一致"),
              ("研发费用加计扣除政策与企业创新投入（版本二）", "作者字段不完整　缺页码"),
              ("税收优惠、融资约束与高新技术企业研发投入", "陈晓明　财政研究　2022"),
              ("税收优惠、融资约束与高新技术企业研发投入（重复导入）", "无 DOI　附件缺失")]
    y = cy + 50
    for i, (t, d) in enumerate(groups):
        first = i % 2 == 0
        s.rect(rx0 + 10, y, cw - lw - 20, 62, fill=BLUE_L if first else "#ffffff",
               stroke=BORDER2, rx=6)
        s.text(rx0 + 24, y + 24, t, size=11.5, fill=TXT, weight="500")
        s.text(rx0 + 24, y + 44, d, size=10.5, fill=TXT3)
        if not first:
            s.rect(rx0 + cw - lw - 116, y + 18, 92, 26, fill=BLUE, rx=5)
            s.text(rx0 + cw - lw - 70, y + 36, "合并条目", size=10.5, fill="#ffffff",
                   anchor="middle")
        else:
            s.text(rx0 + cw - lw - 116, y + 36, "保留此条", size=10.5, fill=GREEN, weight="700")
        y += 72
    s.text(24, 452, "使用「工具 → 重复条目检查」或左栏“重复条目”视图，先保留字段更完整的条目，再合并附件与笔记。",
           size=11, fill=TXT3)
    s.watermark()
    return save(s, os.path.join(OUT, "z18-duplicate-merge.svg"))


# ------------------------------------------------- z19 完整工作流
def z19():
    s = S(1000, 400)
    s.text(28, 40, "从检索到定稿：Zotero 的完整工作流", size=17, fill=TXT, weight="700")
    s.text(28, 62, "八个环节，每一步都留下可检查的产物", size=12.5, fill=TXT3)
    steps = [("1", "检索", "知网 / 外文库\n三轮检索法", BLUE),
             ("2", "导出题录", "导出机器格式\n（EndNote / RIS）", BLUE),
             ("3", "导入", "连接器抓取\n或导入题录文件", ZOT),
             ("4", "核对", "校对字段\n修正条目类型", ZOT),
             ("5", "归档", "挂接 PDF\n归入分类加标签", ORANGE),
             ("6", "阅读批注", "高亮 / 便签\n三层结构笔记", ORANGE),
             ("7", "写作引用", "Word 插入引用\n生成文献表", GREEN),
             ("8", "备份", "同步 + 本地导出\n定期恢复演练", GREEN)]
    x = 28
    for i, (n, t, d, c) in enumerate(steps):
        s.rect(x, 100, 106, 178, fill="#ffffff", stroke=BORDER2, rx=10)
        s.rect(x, 100, 106, 6, fill=c, rx=3)
        s.circle(x + 22, 132, 13, fill=c)
        s.text(x + 22, 137, n, size=12, fill="#ffffff", anchor="middle", weight="700")
        s.text(x + 46, 137, t, size=13, fill=TXT, weight="700")
        for j, ln in enumerate(d.split("\n")):
            s.text(x + 14, 168 + j * 18, ln, size=10.5, fill=TXT2)
        s.line(x + 14, 206, x + 92, 206, stroke=BORDER2)
        outs = [["检索日志", "关键词表"], ["题录文件", ".enw / .ris"], ["条目", "附件"],
                ["字段完整", "类型正确"], ["分类", "标签"], ["批注", "笔记"],
                ["文内引用", "参考文献表"], ["同步记录", "备份包"]][i]
        for j, t2 in enumerate(outs):
            s.text(x + 14, 226 + j * 20, "· " + t2, size=10, fill=TXT3)
        if i < 7:
            s.arrow(x + 108, 190, x + 122, 190, color=TXT4, sw=1.8)
        x += 122
    s.rect(28, 300, 944, 66, fill=YELLOW_L, stroke=YEL_B, rx=8)
    s.text(48, 326, "两条最容易断掉的环节：第 4 步“核对”——不校对就引用，错误会被放大到整篇论文；",
           size=11.5, fill="#8a6100")
    s.text(48, 348, "第 8 步“备份”——只同步题录没备份附件，换电脑后全文依然会丢。", size=11.5, fill="#8a6100")
    s.watermark("概念示意图")
    return save(s, os.path.join(OUT, "z19-workflow.svg"))


# ------------------------------------------------- z21 四个组成
def z21():
    s = S(960, 470)
    s.text(28, 40, "Zotero 的四个组成部分", size=17, fill=TXT, weight="700")
    s.text(28, 62, "四者分工不同，缺一个就会有一类事情做不了", size=12.5, fill=TXT3)
    boxes = [("Zotero 主程序", "资料库本体", ["存题录、附件、笔记", "阅读与批注", "分类与标签"],
              ZOT, "桌面程序"),
             ("Zotero Connector", "浏览器连接器", ["从网页抓取题录", "识别文献类型", "下载全文（配合插件）"],
              BLUE, "浏览器扩展"),
             ("文字处理器插件", "Word / WPS 插件", ["插入文内引用", "生成参考文献表", "随题录更新刷新"],
              GREEN, "随主程序安装"),
             ("Zotero 账号与云", "同步与备份", ["跨设备同步题录", "同步附件（空间有限）", "群组协作"],
              PURPLE, "需要注册")]
    x = 28
    for i, (t, sub, items, c, tag) in enumerate(boxes):
        s.rect(x, 92, 218, 226, fill="#ffffff", stroke=BORDER2, rx=10)
        s.rect(x, 92, 218, 8, fill=c, rx=4)
        s.circle(x + 30, 128, 15, fill=c, op=0.14)
        s.text(x + 30, 134, ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ"][i], size=12, fill=c, anchor="middle", weight="700")
        s.text(x + 54, 124, t, size=13, fill=TXT, weight="700")
        s.text(x + 54, 142, sub, size=10.5, fill=TXT3)
        s.line(x + 16, 160, x + 202, 160, stroke=BORDER2)
        for j, t2 in enumerate(items):
            s.circle(x + 22, 182 + j * 28, 2.4, fill=c)
            s.text(x + 34, 186 + j * 28, t2, size=11, fill=TXT2)
        s.rect(x + 16, 274, 118, 22, fill=c, op=0.1, rx=11)
        s.text(x + 75, 289, tag, size=10, fill=c, anchor="middle")
        if i < 3:
            s.arrow(x + 220, 205, x + 232, 205, color=TXT4, sw=1.8)
        x += 234
    s.rect(28, 336, 904, 108, fill="#fafbfd", stroke=BORDER, rx=8)
    s.text(48, 362, "最常见的两种漏装", size=12, fill=TXT, weight="700")
    s.text(48, 386, "① 只装主程序不装连接器 → 每条文献都要手敲作者、卷期、页码，工作量翻十倍，且容易出错。",
           size=11.5, fill=TXT2)
    s.text(48, 410, "② 只装连接器不装主程序（或没打开主程序）→ 点击图标后无处可存，抓取会失败或只生成网页快照。",
           size=11.5, fill=TXT2)
    s.watermark("概念示意图")
    return save(s, os.path.join(OUT, "z21-zotero-components.svg"))


if __name__ == "__main__":
    for f in (z01, z02, z03, z04, z05, z06, z07, z08, z09, z10, z11,
              z12, z13, z14, z15, z16, z17, z18, z19, z21):
        print(f.__name__, "->", f())
