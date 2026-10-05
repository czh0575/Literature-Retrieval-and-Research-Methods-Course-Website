# -*- coding: utf-8 -*-
"""最后一批定点润色：消除残留的 AI 腔与破折号改造留下的断句。
只做精确字符串替换，逐个校验命中次数，以字节方式写回以保持 LF 行尾。"""
import os
import sys

DOCS = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
APPLY = len(sys.argv) > 1 and sys.argv[1] == 'apply'

# (相对路径, 原文, 新文)
RULES = [
    # ---------- 知网部分 ----------
    ('05-cnki-retrieval/keyword-system.md',
     '检索（Retrieval）的本质是“带着问题找答案”，而不是“在数据库里随便逛”。',
     '检索（Retrieval）要做的是“带着问题找答案”，不是在数据库里随便逛。'),

    ('05-cnki-retrieval/keyword-system.md',
     '题目是检索的“地图”，关键词是“路标”。地图画好，数据库只是用来验证和补充，而不是用来替你思考。',
     '题目是检索的地图，关键词是路标。地图画好之后，数据库只用来验证和补充，不替你思考。'),

    ('05-cnki-retrieval/keyword-system.md',
     '这里引入“关键词金字塔（Keyword Pyramid）”模型，帮助你在检索时既保证相关性，又避免遗漏新表述。',
     '“关键词金字塔（Keyword Pyramid）”要解决两个问题：保证相关性，不遗漏新表述。'),

    ('05-cnki-retrieval/keyword-system.md',
     '检索的本质是“用作者的词找作者的文”，所以你必须先穷尽作者可能用过的词。',
     '检索就是用作者的词去找作者的文，所以必须先把作者可能用过的词穷尽。'),

    ('05-cnki-retrieval/cnki-interface.md',
     '检索技巧建立在你对界面的准确理解之上。',
     '检索技巧的前提是看懂界面。'),

    ('05-cnki-retrieval/cnki-interface.md',
     '这里是真正“读文献”的入口，也藏着重要的“知网节（CNKI Node）”功能：',
     '这里既是读文献的入口，也是“知网节（CNKI Node）”功能的入口：'),

    ('05-cnki-retrieval/core-journals.md',
     '很多同学误以为“只引核心刊就够”。事实上，本科论文同样需要以下非核心期刊文献：',
     '只引核心刊是不够的。本科论文同样需要以下非核心期刊文献：'),

    ('05-cnki-retrieval/research-trace.md',
     '关键文献的参考文献，是它立论所依赖的“地基”。',
     '关键文献的参考文献是它立论所依赖的基础。'),

    ('05-cnki-retrieval/retrieval-log.md',
     '筛选完成后，下一步是把保留的文献“带走”，即导出题录（Bibliographic Record）。',
     '筛选完成后，要把保留的文献导出成题录（Bibliographic Record）。'),

    # ---------- 外文部分 ----------
    ('05-foreign-retrieval/preparation.md',
     '下面这些“准备误区”在本科生中极为普遍，请逐条自查。',
     '这些“准备误区”在本科生中很普遍，逐条自查。'),

    ('05-foreign-retrieval/sciencedirect-search.md',
     '需要明确一点：ScienceDirect 是“全文数据库”而非“引文索引库”。',
     'ScienceDirect 是全文数据库，不是引文索引库。'),

    ('05-foreign-retrieval/sciencedirect-search.md',
     '无论用快速检索还是高级检索，掌握以下语法都能显著提升检索质量。',
     '以下语法在快速检索和高级检索里都通用，能提高检索质量。'),

    ('05-foreign-retrieval/sciencedirect-search.md',
     '第一次检索的结果往往不完美。与其反复重来，不如用“迭代”思路逐步逼近：先宽后窄、先看量再调质。这套流程不追求一次写对，而强调“看结果数—调写法—再看结果数”的闭环，与 5.1 的金字塔、5.3 的精炼共同构成完整的检索方法论。',
     '第一次检索的结果通常不理想。与其推倒重来，不如按“先宽后窄、先看量再调质”的思路迭代。这套流程的价值在“看结果数—调写法—再看结果数”的循环，它与 5.1 的金字塔、5.3 的精炼一起构成完整的检索方法。'),

    ('05-foreign-retrieval/sciencedirect-refine.md',
     'Refine by 是结果页最有用的“事后筛选”工具。逐项说明如下。',
     'Refine by 是结果页最常用的“事后筛选”工具，各项作用如下。'),

    ('05-foreign-retrieval/sciencedirect-refine.md',
     '当你遇到无权限的 Subscription 文章时，不要放弃。下面六条合法途径按“最省力→最费力”排列。',
     '遇到无权限的 Subscription 文章，还有六条合法途径，按“最省力→最费力”排列。'),

    ('05-foreign-retrieval/wos-retrieval.md',
     '它与普通的全文数据库（如 ScienceDirect）在定位上有本质差别：ScienceDirect 主要解决“能不能看到这篇文章的全文”，而 Web of Science 主要解决三件事。“这篇文章发表在什么层次的期刊上”“这篇文章被谁引用过”“某个主题领域的文献是如何相互关联的”。',
     '它与全文数据库（如 ScienceDirect）的定位不同：ScienceDirect 解决“能不能看到这篇文章的全文”，Web of Science 解决另外三件事：这篇文章发表在什么层次的期刊上、被谁引用过，以及某个主题领域的文献如何相互关联。'),

    ('05-foreign-retrieval/wos-retrieval.md',
     'WoS 的核心资产是**引文索引**。',
     'WoS 的核心是**引文索引**。'),

    ('05-foreign-retrieval/wos-retrieval.md',
     '做一次完整的“ snowballing（滚雪球）”：',
     '做一次完整的“滚雪球（snowballing）”：'),

    ('05-foreign-retrieval/trace-and-cheatsheet.md',
     '是最广为人知的中立学术搜索引擎。',
     '是最常用的中立学术搜索引擎之一。'),

    ('05-foreign-retrieval/trace-and-cheatsheet.md',
     '以下给出两种规范下常见外文文献类型的**格式模板**（用占位符示意，你需替换为真实信息；注意标点、斜体、大小写的规范）。',
     '两种规范下常见外文文献类型的**格式模板**（占位符需替换为真实信息；注意标点、斜体、大小写）。'),

    ('05-foreign-retrieval/trace-and-cheatsheet.md',
     '## 5.6.8 本部分小结：外文文献搜集的完整流程',
     '## 5.6.8 外文文献搜集的完整流程'),

    ('05-foreign-retrieval/trace-and-cheatsheet.md',
     '外文文献搜集的完整流程可以归为七步：',
     '外文文献搜集的完整流程共七步：'),

    ('05-foreign-retrieval/sci-ssci-and-jcr.md',
     '要回答这些问题，首先要分清几组**收录体系（引文索引）**的概念。',
     '回答这些问题，先要分清几组**收录体系（引文索引）**的概念。'),

    ('05-foreign-retrieval/sci-ssci-and-jcr.md',
     '该文使用的微观数据（如某国税收调查）你是否拿不到？若无法复现，引用时需谨慎说明。',
     '该文使用的微观数据（如某国税收调查）你是否拿得到？若拿不到，引用时需说明无法复现。'),
]


def main():
    total = 0
    bad = 0
    for rel, old, new in RULES:
        p = os.path.join(DOCS, rel.replace('/', os.sep))
        if not os.path.isfile(p):
            print('  [缺失文件] %s' % rel)
            bad += 1
            continue
        raw = open(p, 'rb').read().decode('utf-8')
        n = raw.count(old)
        if n == 0:
            print('  [未命中] %s :: %s' % (rel, old[:46]))
            bad += 1
            continue
        if n > 1:
            print('  [命中 %d 次] %s :: %s' % (n, rel, old[:46]))
        raw = raw.replace(old, new)
        if APPLY:
            open(p, 'wb').write(raw.encode('utf-8'))
        print('  [%s] %s  %s' % ('已改' if APPLY else '待改', rel, old[:34]))
        total += 1
    print('---')
    print('规则 %d 条，处理 %d 条，异常 %d 条，模式：%s' % (len(RULES), total, bad, 'APPLY' if APPLY else 'DRY-RUN'))


if __name__ == '__main__':
    main()
