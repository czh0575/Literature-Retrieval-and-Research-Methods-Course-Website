# -*- coding: utf-8 -*-
"""把 7.3 文献综述单页拆成 7.3.1 / 7.3.2 / 7.3.3 三个独立页面。

原页 literature-review.md 用 ## 7.3.x 分三个小节；本脚本把它们拆成
literature-review/ 目录下的三个页面，页内标题层级各升一级：
    ## 7.3.x 标题  ->  # 7.3.x 标题
    ### 标题       ->  ## 标题
并顺带修正页间交叉引用（三小节 -> 三页、7.3 -> 7.3.1 等）。
"""
import io
import os
import re

BASE = r"F:\02教学\教学课程\文献检索与研究方法\课件\web"
SRC = os.path.join(BASE, "docs", "course", "07-opening-report", "literature-review.md")
OUT_DIR = os.path.join(BASE, "docs", "course", "07-opening-report", "literature-review")

META = {
    "7.3.1": (
        "任务、范围与专题划分",
        "明确文献综述要回答的四个问题、检索范围的四个维度，以及两类选题的专题划分方法",
        "scope-and-topics.md",
    ),
    "7.3.2": (
        "归纳、比较与评述",
        "掌握综、述、评三种动作，学会合并同类观点、写出分歧来源，并用评述段衔接自己的研究",
        "synthesis-and-critique.md",
    ),
    "7.3.3": (
        "从阅读卡片到综述初稿",
        "用六字段阅读卡片和三种段落模板，把零散的阅读笔记组装成可直接修改的综述初稿",
        "cards-to-draft.md",
    ),
}

# 7.3.1 开头的导语（重写：原页导语 + 三页目录）
LEAD = """# 7.3.1 任务、范围与专题划分

文献综述是开题报告里篇幅最大、也最能看出功力的部分，要求不少于两千字，同时是查重的重灾区。它承上启下：向上承接第一部分提出的“研究缺口”，向下支撑第三部分的研究内容。

7.3 一节分三页讲授，按“定范围 → 写段落 → 拼初稿”的顺序排列，建议依序阅读：

- **7.3.1 任务、范围与专题划分**（本页）：综述要回答什么问题，范围怎么定，专题怎么拆。
- **7.3.2 归纳、比较与评述**：每个专题里的文献怎么写，写成一段有归纳、有比较、有评述的文字。
- **7.3.3 从阅读卡片到综述初稿**：怎么把零散的阅读笔记组装成一份可以直接修改的初稿。

本页先解决第一个问题：动手写之前，先想清楚综述要回答什么、材料从哪里来、按什么线索组织。

"""


def main():
    src = io.open(SRC, encoding="utf-8").read()
    fm = re.match(r"^---\n.*?\n---\n", src, flags=re.S)
    body = src[fm.end():]

    parts = re.split(r"^## (7\.3\.\d) (.+?)\s*$", body, flags=re.M)
    # parts = [导语, '7.3.1', 标题, 正文, '7.3.2', 标题, 正文, ...]
    segs = []
    for i in range(1, len(parts), 3):
        num, title, content = parts[i], parts[i + 1], parts[i + 2]
        assert META[num][0] == title, "标题不一致：%s / %s" % (num, title)
        content = re.sub(r"^### ", "## ", content, flags=re.M)
        segs.append((num, content.strip("\n")))

    os.makedirs(OUT_DIR, exist_ok=True)
    written = []
    for num, content in segs:
        title, desc, fname = META[num]

        # 页间交叉引用修正
        content = content.replace("把卡片按 7.3 划分的专题分组", "把卡片按 7.3.1 划分的专题分组")
        content = content.replace(
            "前两小节讲了专题怎么拆、段落怎么写。这一小节解决最后一个问题",
            "前两页讲了专题怎么拆、段落怎么写。这一页解决最后一个问题",
        )
        content = content.replace(
            "专题划分确定之后，接下来是逐个专题把文献写进去。",
            "专题划分确定之后（见 7.3.1），接下来是逐个专题把文献写进去。",
        )

        if num == "7.3.1":
            page = LEAD + content + "\n"
        else:
            page = "# %s %s\n\n%s\n" % (num, title, content)

        page = "---\ntitle: %s\ndescription: %s\n---\n\n%s" % (title, desc, page)
        path = os.path.join(OUT_DIR, fname)
        io.open(path, "w", encoding="utf-8").write(page)
        written.append((num, fname, len(page)))

    for num, fname, n in written:
        print("%s  %-28s %5d 字" % (num, fname, n))


if __name__ == "__main__":
    main()
