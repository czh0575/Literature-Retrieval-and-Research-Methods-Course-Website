---
title: Web of Science：检索与精炼
description: 介绍 Web of Science 核心合集的检索界面、字段语法、结果精炼与引文追踪方法，帮助税收学本科生确认文献收录层级并获取题录。
---

# 5.4 Web of Science：检索与精炼

## 5.4.1 Web of Science 是什么：引文索引数据库的定位

Web of Science（简称 WoS）是科睿唯安（Clarivate）出品的引文索引数据库。它与全文数据库（如 ScienceDirect）的定位不同：ScienceDirect 解决“能不能看到这篇文章的全文”，Web of Science 解决另外三件事：这篇文章发表在什么层次的期刊上、被谁引用过，以及某个主题领域的文献如何相互关联。

WoS 的核心是**引文索引**。它把每一篇论文的参考文献结构化地记录下来，使研究者既能顺着参考文献“往回”追溯学术源头，也能通过被引情况“往后”追踪研究进展。对撰写本科毕业论文的税收学专业学生而言，WoS 最大的实用价值不在于“搜到文章”，而在于“确认层级”与“追踪脉络”：你可以用它判断一篇外文文献究竟发表在 SCI、SSCI 还是 ESCI 收录期刊上，也可以通过被引网络找到该领域真正有影响力的研究。

::: tip 只用一个外文库就选 WoS 核心合集
如果只用一个外文数据库，优先选 Web of Science 核心合集（Web of Science Core Collection）。它覆盖多学科、多出版社，且提供统一的收录标识与引文分析功能，是确认期刊层级最权威的入口之一。
:::

## 5.4.2 为什么用 WoS 而不只用 ScienceDirect

ScienceDirect 是爱思唯尔（Elsevier）旗下的全文平台，只收录 Elsevier 及其合作出版社的出版物。它的优点是有全文、界面友好，但局限也很明显：

| 维度 | ScienceDirect | Web of Science |
| --- | --- | --- |
| 覆盖范围 | 仅 Elsevier 等少数出版社 | 多学科、跨出版社的引文索引 |
| 能否看全文 | 能（机构订阅范围内） | 多数只提供题录与摘要，全文需跳转 |
| 收录层级判断 | 不直接提供 SCI/SSCI 标识 | 直接提供 Web of Science Index 标识 |
| 被引与引文网络 | 仅限本平台文献的引用 | 跨平台的被引、同被引与引文报告 |
| 适用阶段 | 找全文、读文章 | 确认层级、追踪脉络、查全查准 |

一个合理的分工是：在 ScienceDirect 上做主题检索并获取全文；在 Web of Science 上确认这些文献的期刊归属与收录层级，并通过被引关系扩展文献。二者互补，而非替代。

::: warning ScienceDirect 能搜到不等于 SCI/SSCI 收录
很多同学误以为“在 ScienceDirect 能搜到的就是 SCI/SSCI”。这是错的。ScienceDirect 同时收录大量未被 SCI/SSCI 收录的期刊、会议论文与图书章节。一篇文献是否属 SCI/SSCI 收录，必须以 Web of Science 或 Journal Citation Reports 的标识为准。
:::

## 5.4.3 进入方式

多数高校图书馆都订购了 Web of Science 核心合集。标准进入路径为：学校图书馆首页 → 数据库导航（或“电子资源”） → 外文数据库 → 找到 Web of Science（科睿唯安） → 点击进入核心合集（Web of Science Core Collection）。

进入后，注意区分两个范围：

- **所有数据库（All Databases）**：包含 WoS 平台下的多个子库，范围更大但噪音也更多。
- **Web of Science 核心合集（Web of Science Core Collection）**：这是最常用、最权威的子集，包含 SCI-Expanded、SSCI、A&HCI、ESCI、CPCI 等引文索引。本章所有“收录判定”操作都应在核心合集下进行。

::: warning 校外访问走机构授权入口
校外访问通常通过学校 VPN 或图书馆提供的“校外访问系统”（如 WebVPN、CARSI 统一认证）实现。若在校外直接打开 <https://www.webofscience.com> 却无法下载或显示“无权限”，请先确认是否已通过本校的授权入口登录，而不是直接在公网注册个人账号。
:::

## 5.4.4 检索界面构成

进入核心合集后，默认落在 Documents（文献）检索页。该页自上而下由若干区块构成。

![Web of Science 检索界面](/images/foreign/f06-wos-home.svg)

*图 5-7 Web of Science 检索界面。①文档检索 ②字段下拉 ③检索框 ④添加检索行 ⑤时间范围。*

各区块的功能如下：

1. 顶部标签栏：Documents（文献检索，最常用）、Publications（出版物/期刊检索，用于查期刊收录）、Authors（作者检索）、Organizations（机构检索）等。
2. **字段下拉（Field dropdown）**：决定检索词匹配的位置，如 Topic、Title、Author、Publication Titles、Year Published、Affiliation、DOI 等。
3. **检索框（Search box）**：输入检索词或检索式。
4. **Add row（添加检索行）**：增加一行条件，行与行之间用 AND / OR / NOT 连接。
5. **时间范围（Timespan）**：限定出版年区间，如 2019—2025。
6. **检索按钮（Search）**：执行检索。

::: warning 界面布局随版本变化
界面布局随版本更新会调整，按钮的英文名称也可能变化。这些英文名称（Documents、Add row、Refine results、Search）为常见表述，具体位置以你登录时实际看到的页面为准。若找不到对应入口，优先使用页面顶部的搜索框与左侧的精炼面板。
:::

## 5.4.5 常用字段与检索语法

在 WoS 中，检索式由“字段代码 + 检索词 + 运算符”构成。最常用的是 **TS=（Topic，主题）**，它覆盖标题、摘要、作者关键词（Author Keywords）与关键词-plus（Keywords Plus）四个位置，是兼顾“查全”与“查准”的首选字段。

| 字段代码 | 含义 | 适用场景 |
| --- | --- | --- |
| TS= | Topic（标题+摘要+作者关键词+Keywords Plus） | 主题检索首选，求全求准兼顾 |
| TI= | Title（题名） | 已知道题名片段，或想提高查准率 |
| AB= | Abstract（摘要） | 仅在摘要出现，缩小范围 |
| AK= | Author Keywords（作者关键词） | 关注作者自标关键词 |
| AU= | Author（作者） | 追踪某位学者 |
| SO= | Publication Titles（来源出版物/期刊名） | 限定某本期刊 |
| PY= | Year Published（出版年） | 限定年份，如 PY=2023 |
| DOI= | 数字对象唯一标识 | 已知 DOI 精确命中 |
| OG= | Organization-Enhanced / Affiliation（机构） | 限定某机构，如 universities in China |

WoS 支持的运算符包括：

- **AND**：同时包含，缩小范围（如 corporate tax AND tax avoidance）。
- **OR**：包含任一，扩大范围（如 “value added tax” OR VAT）。
- **NOT**：排除，慎用以免误删相关文献。
- **NEAR/n**：两词相隔不超过 n 个词，且顺序不限，适合短语邻近检索（如 tax NEAR/3 evasion）。
- **SAME**：两词出现在同一句子的同一地址字段中，多用于机构、国家限定。
- **精确短语**：用双引号 `" "` 包裹，如 `"tax competition"`。
- **通配符**：`*` 代表零个或多个字符（如 tax* 可匹配 tax、taxation、taxing）；`?` 代表单个字符（如 wom?n 匹配 woman/women）。

::: details 展开：税收学场景下的三个完整检索式
以下检索式均可在核心合集的检索框中直接粘贴运行（注意句末不要带分号）：

1. 主题双概念检索（企业避税与税收筹划）：

   ```
   TS=("corporate tax" AND "tax avoidance")
   ```

2. 增值税与中小企业（用 OR 合并同义表述）：

   ```
   TS=(("value added tax" OR VAT) AND ("small business" OR SME OR "small and medium enterprise"))
   ```

3. 税收竞争与外商直接投资（限定近五年、并用 NEAR 控制邻近）：

   ```
   TS=("tax competition" AND "foreign direct investment") AND PY=(2019-2025)
   ```

如需进一步限定期刊层级，不要急于在检索式中写死，建议先用上述检索式得到结果，再到左侧 Refine results 面板用 Web of Science Index 筛选（见 5.4.6）。
:::

::: warning 字段代码只在高级检索里生效
WoS 的字段代码（如 TS=、TI=）只在“高级检索（Advanced Search）”或“检索框中直接书写带等号表达式”时生效。若你在下拉框里选了 Topic 再填词，则无需写 TS=，系统会自动套用。两种方式效果一致，但高级检索允许你一次性写出完整复合式，更适合复杂主题。
:::

## 5.4.6 结果页构成与精炼

执行检索后进入结果页。页面左侧为 **Refine results（精炼结果）** 面板，右侧为文献列表。

![Web of Science 精炼结果](/images/foreign/f07-wos-refine.svg)

*图 5-8 WoS 结果页与 Refine results 面板。*

Refine results 提供多维度筛选，最常用的几项如下：

| 精炼项 | 说明 | 本科检索常用度 |
| --- | --- | --- |
| Publication Years | 按出版年区间收拢 | 高 |
| Document Types | Article、Review Article、Proceeding Paper、Editorial 等 | 高 |
| Web of Science Categories | WoS 学科类目 | 中 |
| **Web of Science Index** | **SCI-Expanded、SSCI、ESCI、A&HCI、CPCI 等** | **极高** |
| Open Access | 是否开放获取 | 中（便于获取全文） |
| Funding Agencies | 资助机构 | 低 |
| Affiliations | 作者机构 | 中 |
| Countries/Regions | 国家/地区 | 中 |
| Languages | 文献语言 | 低 |
| Editors | 编辑 | 低 |
| Source Titles | 来源期刊 | 中 |
| Research Areas | 研究领域 | 中 |

其中，**Web of Science Index 是判定文献收录层级最直接的一栏**。勾选 SSCI，列表即只保留社会科学引文索引收录的文献；勾选 SCI-Expanded，则只保留科学引文索引扩展版文献。经管法类外文文献通常关注 SSCI 与 SCIE，艺术人文类关注 A&HCI，新兴或区域性期刊可能仅被 ESCI 收录。

::: tip 先检索，再按 WoS Index 过滤
一条经验法则：先用主题检索得到较大结果集，再在 Refine results 中勾选 Web of Science Index 的 SSCI（或 SCIE）进行过滤。这样你既能看到“全量”，也能一键切到“已收录”的可靠子集，避免一开始就把检索式限定过死而漏掉关键文献。
:::

## 5.4.7 排序策略：什么时候用 Citations，什么时候用 Date

结果页顶部有 **Sort by（排序）** 下拉，常见选项为：

- **Relevance（相关度）**：默认排序，按与检索词的匹配程度排列，适合初筛。
- **Date（日期，最新在前）**：适合追踪最近 1—2 年的最新进展，写文献综述的“研究现状”部分时优先用。
- **Citations（被引次数，Times Cited）**：按被引次数从高到低，适合找“经典文献”与领域奠基性论文。
- **Usage Count（使用次数）**：按近期被浏览/下载次数，反映近期热度。
- **Recently Added（最近收录）**：按进入数据库的时间，适合持续跟踪。

选择建议：

1. 想找**领域内的经典与被广泛认可的文献** → 用 Citations 排序，从前几篇读起。
2. 想找**最新政策响应与前沿方法** → 用 Date 排序，关注近三年。
3. 初筛阶段 → 用 Relevance 快速定位最贴合主题的若干篇。

::: details 展开：税收学选题下的排序示例
假设你的题目是“数字服务税对跨国企业投资的影响”。先用 TS=(“digital services tax” AND “foreign investment”) 检索，得到约数百条结果。此时：

- 切到 **Citations** 排序，前几条通常是 OECD、欧盟委员会或顶尖期刊关于数字税经济效应的奠基性研究，应优先精读。
- 再切到 **Date** 排序，关注 2023 年以后的文献，能看到各国立法落地后的实证反应，正是你的论文需要“最新”支撑的部分。
:::

## 5.4.8 一条记录的详情页能读到什么

点击任意结果条目，进入该文献的**详情页（Full Record）**。对本科生最有价值的字段包括：

- **作者（Authors）与来源期刊（Source Title）**：确认文献出处与层级。
- **摘要（Abstract）**：判断是否与你的选题相关。
- **Keywords 与 Keywords Plus**：作者自标关键词与 WoS 算法提取的关键词，可用于扩展你的检索词表。
- **Times Cited（被引次数）**：该文献被多少后续文献引用，是衡量影响力的粗略指标。
- **References（参考文献）**：该文献引用了谁，是“往回追”的入口。
- **Related Records（相关记录）**：与本文共享较多参考文献的文献，常用于“同被引”扩展。
- **Citation Network（引证关系图）**：可视化展示本文在引文网络中的位置。

::: warning 被引量不能跨学科横向比较
Times Cited 高只说明“被引用多”，不直接等于“方法可靠”或“结论适用于你的研究”。跨学科学术影响力差异极大，税收学一篇实证论文的被引量通常远低于热门生命科学论文，不能用绝对数值横向比较。
:::

## 5.4.9 从一条记录追出更多文献

详情页提供了三条扩展路径，与你在知网中“参考文献—引证文献—同被引”的逻辑一致：

1. **Cited References（引用的参考文献）**：点击可查看本文引用的全部文献，用于“往回追”源头。若其中某篇多次出现，说明它是领域内的基础文献。
2. **Citing Articles（施引文献 / 被引文献）**：点击查看“谁引用了这篇”，用于“往后追”最新进展。这是追踪某主题演化最有效的手段。
3. **Related Records（相关记录）**：基于“共被引”推荐文献，用于“横向追”同类项。
4. **Citation Report（引文报告）**：可在结果集或某主题上生成年度被引趋势图，帮助判断该方向是“上升期”还是“平稳期”。

::: tip 做一次完整的滚雪球
做一次完整的“滚雪球（snowballing）”：从 1 篇高度相关的 SSCI 文献出发，先看它的 Cited References 找 3—5 篇更早的经典，再看它的 Citing Articles 找 3—5 篇最新跟进，往往比单纯关键词检索更系统。
:::

## 5.4.10 保存检索式与创建跟踪

如果你希望长期关注某个主题，可使用 **Saved Searches and Alerts（保存的检索与提醒）**：

1. 在结果页或检索框旁找到 **Search History**（检索历史）或 **Save Search** 入口。
2. 为当前检索式命名（如 `VAT_SME_2025`），选择保存。
3. 勾选 **Create alert（创建提醒）**，设置推送频率（如每周、每月）。
4. 绑定邮箱（通常为学校邮箱），WoS 会在有新匹配文献时自动发送邮件。

这项功能对本科论文尤其有用：从选题到定稿往往跨度数月，定期推送能让你不错过关键的新发表文献。

::: warning 提醒邮件依赖机构账号
提醒邮件的发送依赖你在本机构授权下的账号。若换电脑或清除浏览器后未重新登录机构账号，提醒可能失效。建议将核心检索式手动记录在笔记本或文献管理软件中，作为备份。
:::

## 5.4.11 导出题录

选定若干文献后，使用 **Export（导出）** 功能获取题录，以便导入 Zotero 等管理工具：

1. 在结果列表中勾选目标文献（或全选当前页）。
2. 点击 **Export**，选择格式：
   - **RIS**：通用引文交换格式，是导入 Zotero 的推荐格式。
   - **BibTeX**：常用于 LaTeX 写作环境。
   - **Plain Text / Tab Delimited / Excel**：便于快速浏览与人工整理。
   - **EndNote Online / 直接发送至 Zotero（若机构开通）**：一键推送。
3. 确认导出字段包含作者、题名、来源、年、卷期、页码、DOI 等。

::: warning 导出到 Zotero 的三点注意
- 给 Zotero 用，**优先选 RIS**。它是跨平台通用格式，Zotero 导入后类型识别最准确。
- 若你同时也在用 EndNote，不要混淆两种格式；RIS 与 EndNote 的 .enw 不同，导入前确认目标软件接受哪种。
- 通过“网页快照”方式把 WoS 页面存进 Zotero，会得到“网页”类型的条目，丢失结构化题录。务必用导出 RIS 再导入，而不是截图或收藏网页。
:::

## 5.4.12 常见问题与故障速查表

| 现象 | 可能原因 | 处理方式 |
| --- | --- | --- |
| 检索结果为 0 | 检索式过严、通配符误用、拼写错 | 去掉 NOT、放宽字段为 TS=、检查拼写与引号 |
| 同词在 WoS 与 ScienceDirect 结果差很大 | 两者覆盖范围与索引不同 | 属正常，WoS 跨出版社，ScienceDirect 仅 Elsevier |
| 核心合集 vs 所有数据库 | 范围不同，噪音不同 | 收录判定务必用“核心合集” |
| 全文下载按钮灰掉 | 机构未订阅该刊 | 用文献传递或转 Google Scholar 找开放版本 |
| 检索式复制自别处却报错 | 字段代码/通配符不通用 | 按本库语法逐项改写，不可直接粘贴 |
| Times Cited 显示 0 | 刚发表或未被引 | 用 Date 排序确认是否新文献 |
| 导出后中文乱码 | 编码问题 | 用 UTF-8 打开，或选 Excel 格式 |
| 找不到 Refine 面板 | 界面版本差异 | 以当前实际页面左侧/上方筛选区为准 |

::: details 展开：为什么同一个词在 WoS 和 ScienceDirect 结果差别很大
根本原因在于两者的“收录边界”不同。WoS 核心合集是一个**引文索引**，它遴选了全球多学科的期刊、会议与图书，但每一类收录都有入选标准；ScienceDirect 是一个**全文平台**，只要属于 Elsevier 出版体系就会被纳入，无论是否进入 SCI/SSCI。因此：

- 同一个主题词，在 ScienceDirect 可能返回大量 Elsevier 期刊文章，但不一定都在 SSCI；
- 在 WoS 可能返回包括 Springer、Wiley、Taylor & Francis 等多家出版社的文章，且能直接标出收录索引。

正确的做法是把它们当作两个互补工具，而不是互相校验的“同一数据库”。
:::

## 课堂实操

请在本校 Web of Science 核心合集中完成以下任务，并保留操作痕迹（截图或记录检索式）作为提交成果：

1. 用 **TS=** 构造一个“双概念”检索式，主题须与你的毕业论文方向相关。例如税收竞争方向可写：

   ```
   TS=("tax competition" AND "foreign direct investment")
   ```

   若你的方向是增值税，可改写为 `TS=(("value added tax" OR VAT) AND ("small business" OR SME))`。

2. 在结果页左侧 **Refine results** 中勾选 **Web of Science Index = SSCI**（如你的主题更偏自然科学方法，可改选 SCIE），使列表仅保留 SSCI 收录文献。

3. 在筛选后的结果中，按 **Citations** 排序取前 2 篇、按 **Date** 排序取近三年 3 篇，共导出 **5 条 RIS 题录** 到本地，文件名记为 `WoS_SSCI_5ris.ris`。

4. 提交内容：①你的完整检索式；②筛选所用的收录索引项；③5 条 RIS 题录文件（或其中 1 条的完整元数据截图，含来源期刊名与 Times Cited）。
