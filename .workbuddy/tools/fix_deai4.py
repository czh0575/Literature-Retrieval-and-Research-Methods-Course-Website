# -*- coding: utf-8 -*-
"""去 AI 味第四批：
1) 把 126 个标题笼统的容器改成结合内容的标题；
2) 修正 interface.md 的编号缺口（6.2.2 起 → 6.2.1 起）并同步交叉引用；
3) 收敛剩余的比喻用词。

用法：python fix_deai4.py [apply]
"""
import os
import re
import sys

ROOT = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
APPLY = len(sys.argv) > 1 and sys.argv[1] == 'apply'

# (文件, 行号, 新标题)
TITLES = [
    ('05-cnki-retrieval/cnki-interface.md', 38, '先用一个核心词探热度'),
    ('05-cnki-retrieval/cnki-interface.md', 55, '默认字段是“主题”，不是“全文”'),
    ('05-cnki-retrieval/cnki-interface.md', 189, '检索式存下来复用'),
    ('05-cnki-retrieval/cnki-interface.md', 216, '被引高不等于适合你的题目'),
    ('05-cnki-retrieval/cnki-interface.md', 228, '检索历史留作轨迹证明'),
    ('05-cnki-retrieval/core-journals.md', 61, '先勾 CSSCI 与北大核心两类'),
    ('05-cnki-retrieval/core-journals.md', 85, '核心筛选放在第三轮'),
    ('05-cnki-retrieval/core-journals.md', 109, '核心标识的位置与文案有差异'),
    ('05-cnki-retrieval/core-journals.md', 206, '给文献打层次标签'),
    ('05-cnki-retrieval/core-journals.md', 237, '做一张筛选记录卡'),
    ('05-cnki-retrieval/keyword-system.md', 18, '开工前先花十分钟写词表'),
    ('05-cnki-retrieval/keyword-system.md', 58, '功能词不要当检索词'),
    ('05-cnki-retrieval/keyword-system.md', 112, '用结果页关键词反哺词表'),
    ('05-cnki-retrieval/keyword-system.md', 200, '用两次结果数的落差判断边界'),
    ('05-cnki-retrieval/keyword-system.md', 240, '核心词太少与只用上位词常同时出现'),
    ('05-cnki-retrieval/research-trace.md', 14, '先收敛再追脉络'),
    ('05-cnki-retrieval/research-trace.md', 50, '参考文献与引证文献必须走到'),
    ('05-cnki-retrieval/research-trace.md', 70, '引证多不等于权威'),
    ('05-cnki-retrieval/research-trace.md', 105, '可视化前先把检索式放宽'),
    ('05-cnki-retrieval/research-trace.md', 120, '补词要分辨真同义与假相关'),
    ('05-cnki-retrieval/research-trace.md', 137, '趋势图进开题报告要注明来源'),
    ('05-cnki-retrieval/research-trace.md', 151, '学位论文与综述的结论要回溯原始研究'),
    ('05-cnki-retrieval/research-trace.md', 187, '同时锁定 2–3 个锚点'),
    ('05-cnki-retrieval/research-trace.md', 207, '示例只为演示归类方法'),
    ('05-cnki-retrieval/research-trace.md', 230, '分簇后先命名，再决定读哪一簇'),
    ('05-cnki-retrieval/retrieval-log.md', 12, '题录必须来自导出，不要手敲'),
    ('05-cnki-retrieval/retrieval-log.md', 33, '勾选后不要关页面或刷新'),
    ('05-cnki-retrieval/retrieval-log.md', 51, '导出前再核对已选数量'),
    ('05-cnki-retrieval/retrieval-log.md', 70, '给 Zotero 用就优先选 RIS'),
    ('05-cnki-retrieval/retrieval-log.md', 85, '机器格式与 GB/T 7714 文本各存一份'),
    ('05-cnki-retrieval/retrieval-log.md', 96, 'GB/T 7714 文本不能当导入文件'),
    ('05-cnki-retrieval/retrieval-log.md', 115, '导出后立刻核对三栏'),
    ('05-cnki-retrieval/retrieval-log.md', 130, '“网络首发”文献怎么引用'),
    ('05-cnki-retrieval/retrieval-log.md', 147, '导出即核对'),
    ('05-cnki-retrieval/retrieval-log.md', 186, '两份备份文件的分工'),
    ('05-cnki-retrieval/retrieval-log.md', 190, '去重要合并，不要覆盖'),
    ('05-cnki-retrieval/retrieval-log.md', 223, '示例数字要换成你自己检索到的'),
    ('05-cnki-retrieval/screening-and-export.md', 18, '快速判断不能替代全文核对'),
    ('05-cnki-retrieval/screening-and-export.md', 40, '三遍筛选的结果分别留档'),
    ('05-cnki-retrieval/screening-and-export.md', 190, '优先记“数据与样本”“研究方法”两栏'),
    ('05-cnki-retrieval/screening-and-export.md', 211, '被引次数不是相关性的证据'),
    ('05-cnki-retrieval/screening-and-export.md', 247, '“方法相关”类文献最有价值'),
    ('05-cnki-retrieval/screening-and-export.md', 261, '排除标准要能陈述出来'),
    ('05-cnki-retrieval/screening-and-export.md', 276, '必须收录与自己结论相反的研究'),
    ('05-cnki-retrieval/screening-and-export.md', 290, 'A 档文献控制在 15–25 篇'),
    ('05-cnki-retrieval/search-strategy.md', 77, '精确用引号，覆盖用 OR'),
    ('05-cnki-retrieval/search-strategy.md', 185, '给引用链记下来源'),
    ('05-cnki-retrieval/search-strategy.md', 221, '每次只改一个条件'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 23, '现在说的 SCI 多指 SCIE'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 38, '收录看索引，水平看分区，质量看单篇'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 69, 'JCR 与 WoS 需要机构权限'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 86, '只为确认收录走 WoS，要截图再走 JCR'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 115, '分区必须点明学科类别'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 153, '先问清用 JCR 分区还是中科院分区'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 166, '先求相关，再求层级'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 181, '不要把 SSCI 筛选放在第一步'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 226, '论文里怎么写外文文献的层级'),
    ('05-foreign-retrieval/sci-ssci-and-jcr.md', 230, 'ESCI 不要写成 SSCI'),
    ('05-foreign-retrieval/trace-and-cheatsheet.md', 43, '不要用 h-index 判断单篇文献'),
    ('05-foreign-retrieval/trace-and-cheatsheet.md', 49, '正式引用前核对出版信息'),
    ('05-foreign-retrieval/trace-and-cheatsheet.md', 71, '三个平台的分工组合'),
    ('05-foreign-retrieval/trace-and-cheatsheet.md', 100, '最易错的两处：通配符与年字段'),
    ('05-foreign-retrieval/trace-and-cheatsheet.md', 144, '下载不了多半是订阅范围问题'),
    ('05-foreign-retrieval/trace-and-cheatsheet.md', 196, '自动生成后仍要人工校对'),
    ('05-foreign-retrieval/trace-and-cheatsheet.md', 200, '全文只能使用一种参考文献格式'),
    ('05-foreign-retrieval/wos-retrieval.md', 14, '只用一个外文库就选 WoS 核心合集'),
    ('05-foreign-retrieval/wos-retrieval.md', 32, 'ScienceDirect 能搜到不等于 SCI/SSCI 收录'),
    ('05-foreign-retrieval/wos-retrieval.md', 45, '校外访问走机构授权入口'),
    ('05-foreign-retrieval/wos-retrieval.md', 66, '界面布局随版本变化'),
    ('05-foreign-retrieval/wos-retrieval.md', 120, '字段代码只在高级检索里生效'),
    ('05-foreign-retrieval/wos-retrieval.md', 151, '先检索，再按 WoS Index 过滤'),
    ('05-foreign-retrieval/wos-retrieval.md', 190, '被引量不能跨学科横向比较'),
    ('05-foreign-retrieval/wos-retrieval.md', 203, '做一次完整的滚雪球'),
    ('05-foreign-retrieval/wos-retrieval.md', 218, '提醒邮件依赖机构账号'),
    ('05-foreign-retrieval/wos-retrieval.md', 234, '导出到 Zotero 的三点注意'),
    ('06-zotero/capture-and-download.md', 10, '全文下载的版权边界'),
    ('06-zotero/capture-and-download.md', 136, '网页快照不能当全文引用'),
    ('06-zotero/capture-and-download.md', 260, '英文库不需要茉莉花'),
    ('06-zotero/capture-and-download.md', 291, '先手动验证权限，再查插件'),
    ('06-zotero/capture-and-download.md', 331, '带 PDF 是硬性要求'),
    ('06-zotero/install-and-connector.md', 10, '下载只认官方渠道'),
    ('06-zotero/install-and-connector.md', 30, '版本号与 macOS 首次打开的提示'),
    ('06-zotero/install-and-connector.md', 61, '安装位置与安装类型'),
    ('06-zotero/install-and-connector.md', 73, '跳过向导后怎么补做'),
    ('06-zotero/install-and-connector.md', 95, '账号用邮箱注册'),
    ('06-zotero/install-and-connector.md', 114, '把连接器固定在工具栏'),
    ('06-zotero/install-and-connector.md', 139, '点连接器没反应的排查顺序'),
    ('06-zotero/install-and-connector.md', 159, '社区插件的来源与版本适配'),
    ('06-zotero/install-and-connector.md', 199, '没有“更新翻译器”入口怎么办'),
    ('06-zotero/install-and-connector.md', 214, '自检第 5 项不过就先修插件'),
    ('06-zotero/install-and-connector.md', 257, '连接器只作用于装了它的浏览器'),
    ('06-zotero/install-and-connector.md', 279, '不要在无痕窗口抓文献'),
    ('06-zotero/install-and-connector.md', 294, '卸载程序不等于删除数据目录'),
    ('06-zotero/install-and-connector.md', 316, '把数据目录路径记下来'),
    ('06-zotero/install-and-connector.md', 327, '没勾“同步附件”的后果'),
    ('06-zotero/install-and-connector.md', 341, '下载插件前先读兼容性说明'),
    ('06-zotero/install-and-connector.md', 373, '字段完整才继续往下抓'),
    ('06-zotero/install-and-connector.md', 395, '本页不要求下到 PDF'),
    ('06-zotero/interface.md', 26, '左栏选范围，中间选条目，右栏改细节'),
    ('06-zotero/interface.md', 43, '“设置”在不同版本的名字'),
    ('06-zotero/interface.md', 61, '绿色加号长按可展开条目类型'),
    ('06-zotero/interface.md', 77, '从分类移除不等于删除条目'),
    ('06-zotero/interface.md', 107, '批量拖入分类更快'),
    ('06-zotero/interface.md', 124, '字段随条目类型变化'),
    ('06-zotero/interface.md', 137, '给每篇打一个状态标签'),
    ('06-zotero/interface.md', 151, '布局菜单名称因版本而异'),
    ('06-zotero/interface.md', 179, '插件菜单仍是英文属正常'),
    ('06-zotero/interface.md', 200, '作者字段最易出错'),
    ('06-zotero/interface.md', 268, '“创建副本”与重复条目的区别'),
    ('06-zotero/interface.md', 279, '别把文献存进群组库'),
    ('06-zotero/interface.md', 297, '快捷键以菜单标注为准'),
    ('06-zotero/interface.md', 361, '菜单路径以当前版本为准'),
    ('06-zotero/what-is-zotero.md', 27, '文献到多大规模就该上工具'),
    ('06-zotero/what-is-zotero.md', 41, '安装包只从官网或中文社区下载'),
    ('06-zotero/what-is-zotero.md', 52, '数据目录位置要提前知道'),
    ('06-zotero/what-is-zotero.md', 65, '跨平台不等于拷文件就能用'),
    ('06-zotero/what-is-zotero.md', 130, '某一步没产出，先查输入'),
    ('06-zotero/what-is-zotero.md', 159, '三件套的最低组合'),
    ('06-zotero/what-is-zotero.md', 172, '连接器提示 not running 的常见原因'),
    ('06-zotero/what-is-zotero.md', 187, '选型前先问图书馆'),
    ('06-zotero/what-is-zotero.md', 206, '答辩后导出 BibTeX 与 RIS 留存'),
    ('06-zotero/what-is-zotero.md', 222, '知网全文依赖机构订阅'),
    ('06-zotero/what-is-zotero.md', 235, '判断认证是否成功的最简办法'),
    ('06-zotero/what-is-zotero.md', 288, '菜单路径均指中文界面'),
    ('06-zotero/what-is-zotero.md', 333, '迁移后中文文献最常出错'),
    ('06-zotero/what-is-zotero.md', 353, '收藏中文社区与官方文档'),
]

# 比喻用词收敛
WORD_FIXES = [
    ('05-cnki-retrieval/cnki-interface.md',
     '| 参考文献 | 该文引用了谁——顺藤摸瓜找更早的经典 |',
     '| 参考文献 | 该文引用了谁，可据此往回找更早的经典 |'),
    ('05-cnki-retrieval/cnki-interface.md',
     '| 引证文献 / 被引 | 谁引用了它——找更新的后续研究 |',
     '| 引证文献 / 被引 | 谁引用了它，可据此找更新的后续研究 |'),
    ('05-foreign-retrieval/sciencedirect-refine.md',
     '| ⑥ Cited by | 被引与引文网络 | 顺藤摸瓜找相关文献 |',
     '| ⑥ Cited by | 被引与引文网络 | 沿引文网络找相关文献 |'),
    ('05-foreign-retrieval/sciencedirect-refine.md',
     '它的参考文献里有没有我可以顺藤摸瓜的“种子文献”？',
     '它的参考文献里有没有可以顺着往下找的“种子文献”？'),
    ('05-foreign-retrieval/sciencedirect-refine.md',
     '::: tip 顺藤摸瓜也要回到对照表',
     '::: tip 沿引用关系扩展后仍要回到对照表'),
]

# interface.md 编号：6.2.2–6.2.20 → 6.2.1–6.2.19
MAP_62 = {n: n - 1 for n in range(2, 21)}


def do_titles():
    ok = bad = 0
    cache = {}
    for rel, ln, title in TITLES:
        p = os.path.join(ROOT, rel.replace('/', os.sep))
        if p not in cache:
            cache[p] = open(p, encoding='utf-8').read().split('\n')
        lines = cache[p]
        if ln - 1 >= len(lines) or not lines[ln - 1].startswith(':::'):
            print('  [不是容器] %s L%d  %s' % (rel, ln, lines[ln - 1][:40] if ln - 1 < len(lines) else ''))
            bad += 1
            continue
        kind = 'tip' if lines[ln - 1].startswith('::: tip') else 'warning'
        lines[ln - 1] = '::: %s %s' % (kind, title)
        ok += 1
    if APPLY:
        for p, lines in cache.items():
            open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
    print('容器标题：改写 %d 处，异常 %d 处' % (ok, bad))


def do_words():
    ok = bad = 0
    for rel, old, new in WORD_FIXES:
        p = os.path.join(ROOT, rel.replace('/', os.sep))
        t = open(p, encoding='utf-8').read()
        if old not in t:
            print('  [未命中] %s :: %s' % (rel, old[:44]))
            bad += 1
            continue
        t = t.replace(old, new)
        if APPLY:
            open(p, 'w', encoding='utf-8', newline='').write(t)
        ok += 1
    print('比喻收敛：成功 %d 处，未命中 %d 处' % (ok, bad))


def do_renumber_62():
    tok = re.compile(r'6\.2\.(\d+)(?:\.(\d+))?')

    def rep(m):
        a = int(m.group(1))
        if a in MAP_62:
            return '6.2.%d%s' % (MAP_62[a], ('.' + m.group(2)) if m.group(2) else '')
        return m.group(0)

    p = os.path.join(ROOT, '06-zotero', 'interface.md')
    t = open(p, encoding='utf-8').read()
    t2 = tok.sub(rep, t)
    if APPLY:
        open(p, 'w', encoding='utf-8', newline='').write(t2)
    print('interface.md 编号重排完成')

    # 跨文件引用
    p2 = os.path.join(ROOT, '06-zotero', 'capture-and-download.md')
    t3 = open(p2, encoding='utf-8').read()
    n = len(re.findall(r'6\.2\.\d+', t3))
    if n:
        print('  跨文件引用 6.2.x 共 %d 处，按同一映射处理' % n)
        t4 = tok.sub(rep, t3)
        if APPLY:
            open(p2, 'w', encoding='utf-8', newline='').write(t4)


if __name__ == '__main__':
    print('=== 试运行 ===' if not APPLY else '=== 写入 ===')
    do_titles()
    do_words()
    do_renumber_62()
