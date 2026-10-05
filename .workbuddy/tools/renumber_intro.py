# -*- coding: utf-8 -*-
"""把前三部分的页面编号统一为「部分号.页序号」体系，与第四—七部分一致。

改前：第一部分内编号 1. / 2. / 3.（每个部分各自从 1 开始，重复）
      # 1. 为什么要写毕业论文
      ## 1.1 先想清楚：……

改后：全站唯一的「部分.页」编号
      # 1.1 为什么要写毕业论文
      ## 1.1.1 先想清楚：……

规则：
  一级标题  #   P.S 标题        P=部分号，S=页内顺序
  二级标题  ##  P.S.N 标题      N=页内连续序号（原有跳号一并补平）
  三级标题  ### 标题（不带编号，符合讲义规范）
"""
import io
import os
import re

BASE = r"F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course"

# (相对路径, 部分号, 页内顺序)
PLAN = [
    ("01-course-introduction/why-thesis.md", 1, 1),
    ("01-course-introduction/objectives-and-assessment.md", 1, 2),
    ("01-course-introduction/workflow-and-expectations.md", 1, 3),
    ("02-academic-ethics/misconduct.md", 2, 1),
    ("02-academic-ethics/citation-and-evidence.md", 2, 2),
    ("02-academic-ethics/ai-and-integrity.md", 2, 3),
    ("02-academic-ethics/cases.md", 2, 4),
    ("03-topic-selection/principles.md", 3, 1),
    ("03-topic-selection/tax-directions.md", 3, 2),
    ("03-topic-selection/empirical-topic.md", 3, 3),
    ("03-topic-selection/workflow-and-feasibility.md", 3, 4),
]

H1 = re.compile(r"^# \d+\.\s+(.+?)\s*$", re.M)
H2 = re.compile(r"^## \d+\.\d+\s+(.+?)\s*$", re.M)


def convert(text, p, s):
    """返回 (新文本, 一级标题文本, [(旧编号, 新编号)])"""
    lines = text.split("\n")
    out = []
    h1_text = None
    n = 0
    mapping = []
    for line in lines:
        m = H1.match(line)
        if m:
            h1_text = m.group(1)
            out.append("# %d.%d %s" % (p, s, h1_text))
            continue
        m = H2.match(line)
        if m:
            old = line.split()[1]
            n += 1
            mapping.append((old, "%d.%d.%d" % (p, s, n)))
            out.append("## %d.%d.%d %s" % (p, s, n, m.group(1)))
            continue
        out.append(line)
    return "\n".join(out), h1_text, mapping


def main():
    for rel, p, s in PLAN:
        path = os.path.join(BASE, rel.replace("/", os.sep))
        with io.open(path, encoding="utf-8") as f:
            src = f.read()
        assert H1.search(src), "未找到一级标题：%s" % rel
        new, h1, mapping = convert(src, p, s)
        with io.open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print("=== %s  ->  # %d.%d %s" % (rel, p, s, h1))
        for old, nw in mapping:
            if old != nw:
                print("      %-6s -> %s" % (old, nw))


if __name__ == "__main__":
    main()
