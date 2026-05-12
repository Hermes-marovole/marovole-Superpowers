# PACT：LLM 谈判能力基准测试首次更新

> 来源：Lech Mazur (@LechMazur) on X  
> 发布时间：2026-05-11  
> 整理时间：2026-05-12

---

## 执行摘要

Lech Mazur 发布了 PACT（Pairwise Auction Conversation Testbed）基准测试的首次更新。PACT 是一个 head-to-head（一对一）LLM 谈判能力评估框架，通过 20 轮买家-卖家议价博弈，测试各大型语言模型在多轮对话中的策略制定、信息交换和价格谈判能力。本次更新涵盖数千场比赛，共 25 个主流模型参与排名，GPT-5.5 以 1970 分位居榜首。

---

## 核心亮点

1. **GPT-5.5 谈判能力最强**：以 1970 分的 PACT Rating 排名第一，在 99 场比赛中平均每轮利润 20.2，展现出色的议价策略。
2. **Claude Opus 4.7 紧随其后**：Anthropic 旗舰模型以 1909 分位列第二，157 场比赛样本量充足，平均每轮利润 19.1。
3. **中国模型表现亮眼**：DeepSeek V4 Pro（第3，1815分）、Kimi K2.6（第5，1759分）、Qwen 3.6 Max Preview（第9，1612分）、GLM-5.1（第10，1606分）、ByteDance Seed2.0 Pro（第13，1557分）等国产模型占据中上游位置。
4. **Gemini 3.1 Pro Preview 效率最高**：虽然排名第4（1797分），但平均每轮利润高达 21.4，为所有模型中最高。
5. **开源/开放权重模型差距明显**：GPT-OSS-120B（第12，1574分）和 Llama 4 Maverick（第25，1123分）表现相对落后，尤其是 Llama 4 Maverick 在 390 场比赛中平均每轮利润仅 8.1。

---

## PACT 排行榜完整数据

| 排名 | 模型名称 | PACT Rating (μ) | 比赛场次 | 平均每轮利润 |
|------|---------|----------------|---------|------------|
| 1 | GPT-5.5 (high) | 1970 | 99 | 20.2 |
| 2 | Claude Opus 4.7 (high) | 1909 | 157 | 19.1 |
| 3 | DeepSeek V4 Pro | 1815 | 129 | 18.4 |
| 4 | Gemini 3.1 Pro Preview | 1797 | 154 | **21.4** |
| 5 | Kimi K2.6 | 1759 | 74 | 15.9 |
| 6 | Claude Sonnet 4.6 (high) | 1754 | 79 | 21.3 |
| 7 | Gemma 4 31B Reasoning | 1736 | 95 | 18.0 |
| 8 | Claude 4.5 Haiku | 1669 | 112 | 16.7 |
| 9 | Qwen 3.6 Max Preview | 1612 | 87 | 21.0 |
| 10 | GLM-5.1 | 1606 | 96 | 15.3 |
| 11 | Arcee Trinity Large Thinking | 1580 | 52 | 16.0 |
| 12 | GPT-OSS-120B | 1574 | 356 | 16.8 |
| 13 | ByteDance Seed2.0 Pro | 1557 | 77 | 18.4 |
| 14 | Gemini 3.1 Flash-Lite Preview | 1551 | 131 | 17.6 |
| 15 | MiniMax-M2.7 | 1518 | 86 | 17.2 |
| 16 | Mistral Medium 3.5 (high) | 1457 | 133 | 17.7 |
| 17 | Qwen 3.6 Plus | 1427 | 86 | 15.2 |
| 18 | Baidu Ernie 5.0 | 1427 | 101 | 12.1 |
| 19 | Tencent Hy3 Preview | 1402 | 129 | 17.1 |
| 20 | Xiaomi MiMo V2.5 Pro | 1362 | 52 | 16.3 |
| 21 | Mistral Large 3 | 1328 | 108 | 7.4 |
| 22 | Amazon Nova Pro | 1323 | 307 | 8.6 |
| 23 | Grok 4.3 | 1267 | 119 | 14.0 |
| 24 | DeepSeek V4 Flash | 1219 | 54 | 12.4 |
| 25 | Llama 4 Maverick | 1123 | 390 | 8.1 |

**注**：评分采用 Glicko-2 margin rating 系统。柱状条长度 = 评分均值；灰色带状区域 = 不确定性区间（颜色越深表示概率越高）；黑色标记 = 均值。全部语料库共 3452 场比赛，表格中展示的是经过筛选的最新模型家族。

---

## 方法论详解

PACT 采用以下实验设计：

- **博弈结构**：两个 LLM 进行 head-to-head 谈判，共 20 轮双拍卖博弈。
- **角色分配**：一方为买家（buyer），另一方为卖家（seller），角色随机分配。
- **每轮流程**：每轮开始时双方进入一个聊天窗口，各自可发送一条消息；消息发送后，双方同时在 0-100 的价格网格上提交出价（bid）或要价（ask）。
- **成交规则**：当买家的出价（bid）大于或等于卖家的要价（ask）时，交易以两者中点价成交。
- **收益目标**：买家目标是支付价格低于自己的私有估值（private value），卖家目标是成交价格高于自己的私有成本（private cost）。
- **评分体系**：使用 Glicko-2 margin rating 进行排名，综合考量胜负与利润差。

**关键说明**：1-on-1 的对战形式专注于测试双边谈判能力，而非群聊或拍卖场景。

---

## 发布者洞察

- **Lech Mazur 是 LLM 基准测试领域的资深研究者**：他是 Advameg, Inc. CEO（City-data.com 创始人），已发布 16 个 LLM 基准测试（见 GitHub: github.com/lechmazur）。
- **PACT 的独特性**：这是首个专注于"多轮谈判对话"的 head-to-head LLM 评估框架，填补了现有 benchmark 在策略博弈领域的空白。
- **"high" 标记的含义**：GPT-5.5 (high)、Claude Opus 4.7 (high)、Claude Sonnet 4.6 (high)、Mistral Medium 3.5 (high) 中的 "high" 标记表示使用了高温度/高采样参数，可能与标准配置下的表现有所不同。

---

## 延伸思考

1. **谈判能力与通用能力的错位**：谈判 benchmark 的结果与常规 MMLU、GSM8K 等学术 benchmark 的排名并不完全一致。例如 Gemini 3.1 Pro Preview 在 PACT 中排名第4，但平均每轮利润最高（21.4），说明其可能在"单位轮次效率"上有独特优势；而 Claude Sonnet 4.6 以 21.3 的平均利润紧随其后。这提示谈判能力可能是一个相对独立的维度。

2. **开源模型的谈判短板**：Llama 4 Maverick 在 390 场比赛（样本量最大）中平均每轮利润仅 8.1，远低于闭源旗舰模型。这可能反映了开源模型在复杂策略推理和隐性信息交换（cheap talk）方面的不足。

3. **中国模型的集群优势**：DeepSeek、Kimi、Qwen、GLM、ByteDance、MiniMax、Baidu、Tencent、Xiaomi 等中国厂商均有模型上榜，且 DeepSeek V4 Pro 进入前三。这表明中国 LLM 生态在策略博弈场景中的竞争力已不容忽视。

4. **样本量与不确定性的权衡**：GPT-5.5 仅 99 场比赛即登顶，而 GPT-OSS-120B 和 Llama 4 Maverick 分别进行了 356 和 390 场比赛但排名靠后。样本量小的顶部模型可能存在一定的不确定性（灰色置信区间较宽），但 GPT-5.5 的领先优势（1970 vs 1909，领先 61 分）已较为明显。

5. **"cheap talk" 的价值**：PACT 允许每轮发送一条消息，这意味着模型可以通过文字进行虚张声势、信息透露或建立信任。谈判能力强的模型可能更善于利用这种"廉价谈话"（cheap talk）来影响对手的预期——这与传统拍卖理论中的信号传递机制形成有趣的对照。

---

## 背景信息

- **PACT 官方页面**：https://lechmazur.github.io/pact/（从推文中的 t.co 链接推断）
- **作者 GitHub**：https://github.com/lechmazur
- **作者 X/Twitter**：@LechMazur
- **评分方法**：Glicko-2 margin rating（国际象棋等竞技领域常用的评分系统）

---

来自翡冷翠
