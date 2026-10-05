---
title: 选题的四项原则
description: 从研究性、创新性、时效性和可行性判断论文题目
---

<style scoped>
/* 示例对比卡片 */
.example-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin: 14px 0 22px;
}
.example-card {
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  padding: 14px 16px;
  background: var(--vp-c-bg-soft);
  position: relative;
}
.example-card .tag {
  display: inline-block;
  font-size: 12px;
  line-height: 1;
  padding: 4px 8px;
  border-radius: 999px;
  margin-bottom: 8px;
  font-weight: 600;
}
.example-card.bad { border-left: 4px solid #d9534f; }
.example-card.bad .tag { background: #fdecec; color: #b53028; }
.example-card.good { border-left: 4px solid #2f9e44; }
.example-card.good .tag { background: #e8f6ec; color: #1f7a37; }
.example-card .topic {
  font-weight: 600;
  margin: 4px 0 6px;
  line-height: 1.5;
}
.example-card .why {
  font-size: 13px;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.6;
}
@media (max-width: 640px) {
  .example-grid { grid-template-columns: 1fr; }
}

/* 创新来源清单 */
.idea-list {
  list-style: none;
  padding: 0;
  margin: 12px 0 18px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
.idea-list li {
  border: 1px dashed var(--vp-c-divider);
  border-radius: 8px;
  padding: 10px 12px;
  background: var(--vp-c-bg-soft);
  font-size: 14px;
  line-height: 1.55;
}
.idea-list li b { color: var(--vp-c-brand-1); }
@media (max-width: 640px) {
  .idea-list { grid-template-columns: 1fr; }
}

/* 时效性要点 */
.freshness {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin: 14px 0 18px;
}
.freshness .step {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 12px;
  font-size: 14px;
  line-height: 1.55;
}
.freshness .step .no {
  display: inline-block;
  width: 22px; height: 22px;
  line-height: 22px;
  text-align: center;
  border-radius: 50%;
  background: var(--vp-c-brand-1);
  color: #fff;
  font-weight: 700;
  font-size: 12px;
  margin-right: 6px;
}
@media (max-width: 640px) {
  .freshness { grid-template-columns: 1fr; }
}

/* 可行性 checklist */
.feasibility-table {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0 18px;
  font-size: 14px;
}
.feasibility-table th, .feasibility-table td {
  border: 1px solid var(--vp-c-divider);
  padding: 8px 10px;
  text-align: left;
  vertical-align: top;
}
.feasibility-table th {
  background: var(--vp-c-bg-soft);
  font-weight: 600;
}
.feasibility-table tr.bad-row td:last-child { color: #b53028; }
.feasibility-table tr.good-row td:last-child { color: #1f7a37; }
</style>

# 1. 选题的四项原则

## 1.1 研究性：题目必须包含需要解释的问题

> “某行业税收情况分析”更像资料汇编；“某项税收政策如何影响某类企业的投资决策”才包含待解释的关系。

研究性通常体现在：

- 有明确的问题，而不是只有对象
- 有需要比较、解释或论证的关系
- 需要使用文献、数据或案例来回答

<div class="example-grid">
  <div class="example-card bad">
    <span class="tag">❌ 不够研究性</span>
    <p class="topic">“我国企业所得税优惠政策梳理”</p>
    <p class="why">只有对象和罗列，没有解释“为什么”“怎么样”。接近资料汇编，难以形成研究问题。</p>
  </div>
  <div class="example-card good">
    <span class="tag">✓ 具有研究性</span>
    <p class="topic">“研发费用加计扣除政策对高新技术企业创新投入的影响——基于融资约束的中介效应”</p>
    <p class="why">包含明确的因果关系与可检验的中介机制，需要用数据回答“为什么”与“通过何种路径”。</p>
  </div>
</div>

另一个常见的对比：

<div class="example-grid">
  <div class="example-card bad">
    <span class="tag">❌ 描述型</span>
    <p class="topic">“某省小微企业税收负担现状分析”</p>
    <p class="why">只回答“是什么”，没有解释差异原因或提出可检验假设。</p>
  </div>
  <div class="example-card good">
    <span class="tag">✓ 解释型</span>
    <p class="topic">“增值税起征点提高对小规模纳税人经营活力的影响——基于某省税务登记数据的实证检验”</p>
    <p class="why">包含明确的政策冲击（X）、结果变量（Y）和实证设计，回答“政策是否有效以及如何有效”。</p>
  </div>
</div>

::: tip 如何快速判断
把题目用“X 对 Y 的影响 / 差异 / 机制”翻译一遍。如果翻译不出来，多半还停留在“描述对象”阶段。
:::

## 1.2 创新性：不等于一定要提出惊天动地的新理论

本科论文的创新可以来自：

<ul class="idea-list">
  <li><b>新政策或新制度</b><br>例如：留抵退税扩围、数电发票全面推广、金税四期上线。</li>
  <li><b>新的研究对象或地区</b><br>例如：把已有研究搬到中西部、某个自贸区或县域层面。</li>
  <li><b>新的数据</b><br>例如：使用某年首次披露的微观税务数据、上市公司新合并报表口径。</li>
  <li><b>新的变量度量方式</b><br>例如：用文本挖掘构造“税收征管强度指数”替代传统指标。</li>
  <li><b>对已有结论的重新检验</b><br>例如：在新样本期或不同制度环境下复刻一篇经典研究。</li>
  <li><b>把两个已有研究方向连接起来</b><br>例如：把“数字经济”与“税收征管”联系起来。</li>
</ul>

<div class="example-grid">
  <div class="example-card bad">
    <span class="tag">❌ 缺乏创新点</span>
    <p class="topic">“营改增对服务业税负的影响研究”</p>
    <p class="why">题目本身已存在大量相似研究，且政策时间已超过 8 年，新意有限。</p>
  </div>
  <div class="example-card good">
    <span class="tag">✓ 体现创新</span>
    <p class="topic">“增值税留抵退税政策对先进制造业全要素生产率的影响”</p>
    <p class="why">新政策（2022 年扩围）、新数据来源三者结合，区别于已有文献。</p>
  </div>
</div>

创新性要建立在文献阅读之上。不了解已有研究，就无法判断自己的题目是否重复。

::: warning 常见误区
创新 ≠ 题目“听起来很新”。如果文献综述里已经能找到 5 篇以上相似题目，再“换词不换意”就不再是创新。
:::

## 1.3 时效性：关注现实变化，但不要追逐热词

税收改革、数字经济、绿色发展和地方财政都可能成为研究背景，但热词本身不是研究问题。

判断时效性时要问：

<div class="freshness">
  <div class="step"><span class="no">1</span><b>现实中发生了什么变化？</b><br>如某项新法规、新税率、新系统上线。</div>
  <div class="step"><span class="no">2</span><b>变化带来了什么可观察的问题？</b><br>如企业行为、税收收入、地区差异出现新现象。</div>
  <div class="step"><span class="no">3</span><b>政策是否已实施到足以研究？</b><br>需有足够期数与公开数据，不能刚颁布就做实证。</div>
  <div class="step"><span class="no">4</span><b>是否能够找到连续、可靠的资料？</b><br>年报、统计年鉴、税务局公报、政策原文等。</div>
</div>

<div class="example-grid">
  <div class="example-card bad">
    <span class="tag">❌ 追逐热词</span>
    <p class="topic">“关于数字经济税收问题的研究”</p>
    <p class="why">“数字经济”是大背景，不是研究问题；题目中没有具体对象、变量或政策，难以落地。</p>
  </div>
  <div class="example-card good">
    <span class="tag">✓ 把握时效</span>
    <p class="topic">“数电发票推广对电商企业增值税负的影响”</p>
    <p class="why">将“数字经济”落到具体政策（数电发票）、具体对象（电商企业）、具体时间窗口和数据来源。</p>
  </div>
</div>

## 1.4 可行性：在有限时间内完成

可行性包括：

<table class="feasibility-table">
  <thead>
    <tr>
      <th style="width:24%">可行性维度</th>
      <th>❌ 常见踩坑</th>
      <th>✓ 更稳妥的替代</th>
    </tr>
  </thead>
  <tbody>
    <tr class="bad-row">
      <td>数据是否能够获得</td>
      <td>依赖未公开的税务稽查案卷、单一企业内部台账。</td>
      <td style="color:#1f7a37">使用上市公司年报、CSMAR/Wind 公开数据、地方统计年鉴、税务局公报。</td>
    </tr>
    <tr class="bad-row">
      <td>变量是否能够度量</td>
      <td>“企业税收规避程度”“税收公平感”找不到可操作指标。</td>
      <td style="color:#1f7a37">改为“名义税率与实际税率之差”“有效税率”等可计算指标。</td>
    </tr>
    <tr class="bad-row">
      <td>方法是否掌握或能够学习</td>
      <td>本科阶段硬上 PSM-DID + 中介 + 调节，做不完、做不严谨。</td>
      <td style="color:#1f7a37">先用 OLS / 双重差分打基础，再视掌握程度加入稳健性检验。</td>
    </tr>
    <tr class="bad-row">
      <td>样本是否足够</td>
      <td>把范围限到“某市某区某类企业”，样本只剩几十家。</td>
      <td style="color:#1f7a37">放宽到全省或全国行业层面，或改用案例研究、问卷调查。</td>
    </tr>
    <tr class="bad-row">
      <td>范围是否适合本科论文</td>
      <td>“中国税收制度优化研究”——覆盖全税种全行业。</td>
      <td style="color:#1f7a37">限定到一个税种、一个行业、一个地区或一项政策。</td>
    </tr>
  </tbody>
</table>

一个题目即使很有意义，如果无法取得数据，也不能算是好的毕业论文题目。

::: details 案例：可行性判断的“半小时测试”
拿到一个候选题目后，强迫自己在 30 分钟内做完下面 5 件事：

1. 在知网 / Web of Science 检索出 3–5 篇最相关文献，确认题目不重复；
2. 列出研究所需的 2–3 个核心变量，并写出每个变量的数据来源；
3. 估算样本量和时间跨度（如“2015–2023 年 A 股制造业上市公司 ≈ 1500 家”）；
4. 判断用所学方法是否能在 2 个月内完成数据清洗与建模；
5. 与导师沟通，确认题目方向与其指导范围匹配。

如果其中任何一项回答不清楚，就回到上一步重新调整题目，而不是“先报上去再说”。
:::
