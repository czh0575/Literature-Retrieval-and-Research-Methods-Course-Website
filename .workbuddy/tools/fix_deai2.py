# -*- coding: utf-8 -*-
"""去 AI 味：逐处定点改写 + 删除重复的「衔接」脚手架小节并重排编号。

用法：
    python fix_deai2.py         # 试运行，只报告
    python fix_deai2.py apply   # 实际写入
"""
import os
import re
import sys

ROOT = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
APPLY = len(sys.argv) > 1 and sys.argv[1] == 'apply'

# ---------------------------------------------------------------- 定点改写
# (相对路径, 原文, 新文)   新文为 None 表示整行删除（连同行后空行）
FIXES = [
    # ---- 05-cnki-retrieval ----
    ('05-cnki-retrieval/cnki-interface.md',
     '本节的目标是：在你动手之前，先认清楚', '动手之前，先认清楚'),
    ('05-cnki-retrieval/cnki-interface.md',
     '初学者常因混用字段导致结果量无法解释，请务必先确认每个词用的是哪个字段。',
     '初学者常因混用字段导致结果量无法解释，先确认每个词用的是哪个字段。'),
    ('05-cnki-retrieval/cnki-interface.md',
     '是 4.3 之后做“滚雪球检索”的利器：找到一篇核心文献后', '找到一篇核心文献后'),
    ('05-cnki-retrieval/cnki-interface.md',
     '往往比单纯关键词检索更高效。', '往往比单纯关键词检索更高效，这条路径在 4.3 还会再用到。'),
    ('05-cnki-retrieval/cnki-interface.md',
     '，下一节（4.3）将基于它们做三轮检索的逐轮优化。', '，4.3 的三轮检索优化要用到它们。'),

    ('05-cnki-retrieval/core-journals.md',
     '不属于期刊体系但不可或缺', '不在期刊体系内，但写制度背景时要用'),
    ('05-cnki-retrieval/core-journals.md',
     '下面以“研发费用加计扣除与企业创新”为例，演示从检索结果到核心文献的完整筛选路径。',
     '以“研发费用加计扣除与企业创新”为例，看一遍从检索结果到核心文献的完整筛选路径。'),

    ('05-cnki-retrieval/keyword-system.md',
     '下面用三个真实选题示范拆解方法。', '三个例子示范拆解过程。'),
    ('05-cnki-retrieval/keyword-system.md',
     '下面用“研发费用加计扣除”题做边界示范：', '以“研发费用加计扣除”题做边界示范：'),
    ('05-cnki-retrieval/keyword-system.md',
     '这就是下一节（4.2）要输入知网高级检索面板的式子。',
     '这个式子可以直接输入 4.2 的知网高级检索面板。'),
    ('05-cnki-retrieval/keyword-system.md',
     '作为下一节（4.2）输入知网的准备。', '作为输入 4.2 知网检索面板的准备。'),
    ('05-cnki-retrieval/keyword-system.md',
     '完成后，请同桌互相检查：对方的关键词表里是否出现了“只用上位词”或“把结论词当检索词”的情况。下一节（4.2）将把这些组合真正输入知网界面。',
     '完成后与同桌互相检查：对方的关键词表里是否出现了“只用上位词”或“把结论词当检索词”的情况。4.2 会把这些组合真正输入知网检索面板。'),

    ('05-cnki-retrieval/research-trace.md',
     '这正是新选题的温床。', '也是新选题的来源。'),

    ('05-cnki-retrieval/screening-and-export.md',
     '学生面对的通常不是几篇文献，而是几十篇甚至上百篇候选文献。',
     '学生面对的通常是几十篇甚至上百篇候选文献。'),
    ('05-cnki-retrieval/screening-and-export.md',
     '下面以税收学方向真实风格的论文标题为例，演示如何“读出信息”与“承认读不出信息”。', None),
    ('05-cnki-retrieval/screening-and-export.md',
     '下面以“研发费用加计扣除”主题的虚拟但贴近真实的摘要为例，逐句标注所属要素。',
     '以“研发费用加计扣除”主题的虚拟但贴近真实的摘要为例，逐句标注所属要素。'),

    ('05-cnki-retrieval/search-strategy.md',
     '这篇文献不是随便搜到的，而是通过核心文献的引用网络定位的',
     '这篇文献是通过核心文献的引用网络定位的'),
    ('05-cnki-retrieval/search-strategy.md',
     '足以支撑下一节（4.4）筛选核心期刊文献。', '足以支撑 4.4 的核心期刊筛选。'),

    # ---- 05-foreign-retrieval ----
    ('05-foreign-retrieval/preparation.md',
     '光说“要回验”仍嫌抽象，下面用两个真实场景演示如何判断一个英文词是否地道，以及回验失败时应如何纠偏。',
     '判断一个英文词是否地道、回验失败时如何纠偏，看两个真实场景。'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md',
     '一个记忆口诀：**收录看', '三条判断线索：**收录看'),
    ('05-foreign-retrieval/sciencedirect-refine.md',
     '它是引用与题录导出时不可或缺的信息。', '引用和导出题录都要用到它。'),
    ('05-foreign-retrieval/sciencedirect-refine.md',
     '本页给出的英文原名（Advanced search、Refine by、Export、Cite 等）相对稳定',
     '英文原名（Advanced search、Refine by、Export、Cite 等）相对稳定'),
    ('05-foreign-retrieval/sciencedirect-refine.md',
     '判断并精读一篇文献后，它往往不是终点，而是“种子”。ScienceDirect 详情页提供两类顺藤摸瓜的入口。',
     '判断并精读一篇文献后，这篇文献还能继续带来新的文献。ScienceDirect 详情页提供两类沿引用关系扩展的入口。'),
    ('05-foreign-retrieval/sciencedirect-search.md',
     '本章先说明它是什么、如何访问，再逐项拆解其高级检索面板与检索语法。', ''),
    ('05-foreign-retrieval/sciencedirect-search.md',
     '若你是第一次使用，可按以下步骤定位到高级检索入口：', None),
    ('05-foreign-retrieval/sciencedirect-search.md',
     '请务必按上表拆成多行。', '必须按上表拆成多行。'),
    ('05-foreign-retrieval/sciencedirect-search.md',
     '下一节将在此基础上做结果精炼与全文获取。', ''),
    ('05-foreign-retrieval/trace-and-cheatsheet.md',
     '当你把一个数据库里调好的检索式换到另一个库时，遵循以下步骤：',
     '把一个数据库里调好的检索式换到另一个库时，需要逐项改写：'),
    ('05-foreign-retrieval/trace-and-cheatsheet.md',
     '把 5.1—5.6 的内容串起来，外文文献搜集可归纳为一条标准流程：',
     '外文文献搜集的完整流程可以归为七步：'),
    ('05-foreign-retrieval/trace-and-cheatsheet.md',
     '一张流程图式 checklist', '流程速查'),
    ('05-foreign-retrieval/wos-retrieval.md',
     '本节给出的英文名称', '这些英文名称'),

    # ---- 06-zotero ----
    ('06-zotero/backup-and-workflow.md',
     '建议你自己在存入网盘前用“作者-年份-关键词”规则命名（如“张伟-2020-加计扣除创新.pdf”），便于在网盘里直接定位。',
     '存入网盘前自己用“作者-年份-关键词”规则命名（如“张伟-2020-加计扣除创新.pdf”），在网盘里就能直接定位。'),
    ('06-zotero/backup-and-workflow.md',
     '归档完成后，这份资料库在毕业多年后仍能随时调出，支撑你后续的求职、读研或工作参考，它是你大学阶段学术能力的可检索档案，值得认真维护。',
     '归档后把整个数据目录复制到移动硬盘和网盘各一份，毕业后换电脑也能直接用。'),
    ('06-zotero/backup-and-workflow.md',
     '把本页的备份流程养成习惯，你的文献资产就能长期安全、随取随用。',
     '把这条备份流程固定下来，文献就不容易丢。'),
    ('06-zotero/backup-and-workflow.md',
     '至此，第六章 Zotero 文献管理的全部内容（6.5–6.8）构成一个从“收文献”到“写论文”的完整闭环，可直接支撑你的毕业论文写作。',
     None),
    ('06-zotero/capture-and-download.md',
     '做完本页，你应该能为毕业论文建起第一批文献条目。',
     '做完这一页，你能为毕业论文建起第一批文献条目。'),
    ('06-zotero/capture-and-download.md',
     '贵在每批都记，而不是期末补一张。本页先记第一批，后面 6.5、6.6 继续沿用同一张表。',
     '贵在每批都记，而不是期末补一张。先记第一批，6.5、6.6 继续沿用同一张表。'),
    ('06-zotero/install-and-connector.md',
     '四张图齐备即本页过关。', '四张图齐备即达到要求。'),
    ('06-zotero/interface.md',
     '哪个区域放文献、哪个改字段、哪个挂 PDF，下面逐个说清。学完本页，你应该能在不查菜单的情况下，凭直觉找到“新建分类”“加标签”“看附件”的位置。',
     None),
    ('06-zotero/interface.md',
     'Item Type 一列能帮你一眼发现被误识别成网页的条目，是 6.4 抓取后快速自检的利器。',
     'Item Type 一列能帮你一眼发现被误识别成网页的条目。'),
    ('06-zotero/interface.md',
     '若你还未安装 Zotero，可先保存本页的六区域速查表作为替代产出',
     '若你还未安装 Zotero，可先保存六区域速查表作为替代产出'),
    ('06-zotero/library-organization.md',
     '光讲规则不够直观，下面用 5 篇“研发费用加计扣除”主题的真实场景文献，演示分类与标签如何同时作用。',
     '用 5 篇“研发费用加计扣除”主题的真实场景文献，看分类与标签如何同时作用。'),
    ('06-zotero/library-organization.md',
     '## 6.5.11 附件命名与“链接附件”预告', '## 6.5.11 附件命名与“链接附件”'),
    ('06-zotero/library-organization.md',
     '资料库组织得好不好，用下面四条当场检验：', '资料库组织得好不好，用四条标准当场检验：'),
    ('06-zotero/library-organization.md',
     '即便理解了分类与标签，初学者仍容易踩下面几个坑，逐一对照避免：',
     '即便理解了分类与标签，初学者仍容易踩下面几个坑：'),
    ('06-zotero/library-organization.md',
     '四条都通过，说明资料库已经具备支撑一篇毕业论文的秩序。',
     '四条都通过，说明资料库已经达到能支撑一篇毕业论文的程度。'),
    ('06-zotero/metadata-and-reading.md',
     '下面再给一篇“政策文件类”的简短示例，说明非实证文献也能用三层结构：',
     '非实证文献也能用三层结构。看一个“政策文件类”的简短示例：'),
    ('06-zotero/what-is-zotero.md',
     '请务必从官网或 Zotero 中文社区', '安装包只从官网或 Zotero 中文社区'),
    ('06-zotero/what-is-zotero.md',
     '分类（Collection）只是“看数据的窗口”。', '分类（Collection）只是一个视图。'),
    ('06-zotero/what-is-zotero.md',
     '| 编号 | 核心能力 | 一句话说明 | 税收学论文中的例子 |',
     '| 编号 | 核心能力 | 简要说明 | 税收学论文中的例子 |'),
    ('06-zotero/what-is-zotero.md',
     '下面把 Zotero 不擅长的事也列清楚。知道边界，才能把工具用在合适的地方。',
     'Zotero 也有做不到的事。分清边界，才能把它用在合适的地方。'),
    ('06-zotero/what-is-zotero.md',
     '下面用一个完整小案例，把五项核心能力串成一条线。细节操作都在后续页面，这里只看流向。',
     '一个完整的小案例，把五项核心能力串成一条线。具体操作在后面各页，这里只看流向。'),
    ('06-zotero/what-is-zotero.md',
     '跨软件迁移后，中文文献的字段（作者、期刊名）最常出错，请务必按 6.6 的方法逐条校对。不要把“导入成功”误当成“数据正确”。',
     '跨软件迁移后，中文文献的字段（作者、期刊名）最常出错，导入后按 6.6 的方法逐条校对。不要把“导入成功”当成“数据正确”。'),
    ('06-zotero/what-is-zotero.md',
     '即构成本页的可交付产出。', '就是这一页的可交付产出。'),
    ('06-zotero/what-is-zotero.md',
     '第 6 章各页之间的先后关系如下：', '第 6 章各页的先后关系：'),
    ('06-zotero/what-is-zotero.md',
     '本页结束后，请完成以下可检查的产出。', '本页结束后完成以下可检查的产出。'),
]

# ------------------------------------------------- 结构性删除 + 编号重排
# 删除整节：(相对路径, 起始行文本，含标题)
DEL_BLOCKS = [
    # capture-and-download.md：两个内容重复的「衔接」小节
    ('06-zotero/capture-and-download.md',
     '## 6.4.7 与其他章节的衔接',
     '## 6.4.8 拖动识别的进阶技巧'),
    ('06-zotero/capture-and-download.md',
     '## 6.4.15 与 6.5 / 6.6 的衔接',
     '## 6.4.16 抓取时的网络与权限自检'),
    # install-and-connector.md：两处纯预告小节
    ('06-zotero/install-and-connector.md',
     '## 6.3.18 与 6.4 的衔接',
     '## 6.3.19 确认数据目录位置（为备份做准备）'),
    ('06-zotero/install-and-connector.md',
     '### 6.3.24.3 与下一页的衔接',
     '### 6.3.24.4 版本信息记录建议'),
]

# 编号重排映射：capture-and-download 删掉 6.4.7 与 6.4.15
MAP_CAPTURE = {8: 7, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 16: 14, 17: 15, 18: 16}
# install-and-connector 删掉 6.3.18 与 6.3.24.3
MAP_INSTALL_MAJOR = {19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23}
MAP_INSTALL_MINOR_24 = {1: 1, 2: 2, 4: 3, 5: 4}


def do_fixes():
    ok = bad = 0
    for rel, old, new in FIXES:
        p = os.path.join(ROOT, rel.replace('/', os.sep))
        t = open(p, encoding='utf-8').read()
        n = t.count(old)
        if n == 0:
            print('  [未命中] %s :: %s' % (rel, old[:46]))
            bad += 1
            continue
        if n > 1:
            print('  [多处 %d] %s :: %s' % (n, rel, old[:46]))
        if new is None:
            # 整行删除，并去掉一个紧随的空行
            t = t.replace(old + '\n\n', '')
            t = t.replace(old + '\n', '')
            if old in t:
                print('  [删除失败] %s :: %s' % (rel, old[:46]))
                bad += 1
                continue
        else:
            t = t.replace(old, new)
        if APPLY:
            open(p, 'w', encoding='utf-8', newline='').write(t)
        ok += 1
    print('定点改写：成功 %d 处，未命中 %d 处' % (ok, bad))


def do_blocks():
    for rel, start, end in DEL_BLOCKS:
        p = os.path.join(ROOT, rel.replace('/', os.sep))
        t = open(p, encoding='utf-8').read()
        i = t.find(start)
        j = t.find(end)
        if i < 0 or j < 0 or j <= i:
            print('  [区间未找到] %s :: %s -> %s' % (rel, start[:24], end[:24]))
            continue
        removed = t[i:j]
        t = t[:i] + t[j:]
        if APPLY:
            open(p, 'w', encoding='utf-8', newline='').write(t)
        print('  [已删] %s  %s  （%d 行）' % (rel, start[:26], removed.count('\n')))


def do_renumber():
    tok = re.compile(r'6\.4\.(\d+)(?:\.(\d+))?')

    def rep_capture(m):
        a = int(m.group(1))
        if a in MAP_CAPTURE:
            return '6.4.%d%s' % (MAP_CAPTURE[a], ('.' + m.group(2)) if m.group(2) else '')
        return m.group(0)

    p = os.path.join(ROOT, '06-zotero', 'capture-and-download.md')
    t = open(p, encoding='utf-8').read()
    t2, n1 = tok.subn(rep_capture, t)

    tok3 = re.compile(r'6\.3\.(\d+)(?:\.(\d+))?')

    def rep_install(m):
        a = int(m.group(1))
        if a not in MAP_INSTALL_MAJOR:
            return m.group(0)
        na = MAP_INSTALL_MAJOR[a]
        if m.group(2) is None:
            return '6.3.%d' % na
        b = int(m.group(2))
        nb = MAP_INSTALL_MINOR_24.get(b, b) if a == 24 else b
        return '6.3.%d.%d' % (na, nb)

    p3 = os.path.join(ROOT, '06-zotero', 'install-and-connector.md')
    t3 = open(p3, encoding='utf-8').read()
    t4, n2 = tok3.subn(rep_install, t3)

    # capture-and-download 里对 install 章节的交叉引用
    n3 = t2.count('6.3.21')
    t5 = t2.replace('6.3.21', '6.3.20')

    if APPLY:
        open(p, 'w', encoding='utf-8', newline='').write(t5)
        open(p3, 'w', encoding='utf-8', newline='').write(t4)
    print('编号重排：capture-and-download %d 处，install-and-connector %d 处，跨文件交叉引用 %d 处' % (
        n1, n2, n3))


if __name__ == '__main__':
    print('=== 定点改写 ===' if APPLY else '=== 试运行 ===')
    do_fixes()
    print('=== 删除重复小节 ===')
    do_blocks()
    print('=== 编号重排 ===')
    do_renumber()
