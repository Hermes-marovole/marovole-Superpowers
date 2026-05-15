# X For You 算法开源 - X2Doc 整理

> 来源：https://x.com/elonmusk/status/2055277918633562153?s=20
> 作者：@elonmusk
> 原帖时间：2026-05-15 13:23
> 整理时间：2026-05-16
> 来自翡冷翠

---

## TL;DR

- Elon Musk 宣布 X 最新的 For You 推荐算法已发布到 GitHub，仓库为 `xai-org/x-algorithm`。
- 这次开源重点不是简单披露排序权重，而是给出一个可运行的端到端推荐系统骨架：retrieval → ranking → filtering → selection。
- 架构上，X 将关注账号内容（Thunder）与全局语料发现内容（Phoenix Retrieval）合并，再由 Grok-based Transformer 预测多种互动概率。
- README 声称系统“eliminated every single hand-engineered feature and most heuristics”，改由 Transformer 根据用户互动序列学习相关性。
- 对 AI 产品、内容分发和 Super Individual 来说，最有价值的是候选生成、用户行为序列建模、多目标评分、负反馈降权、作者多样性这些可复用模式。

## 原帖核心内容

Elon Musk 的原帖很短：

> The latest 𝕏 algorithm has been published to GitHub

原帖附带 GitHub 卡片：

- GitHub 仓库：https://github.com/xai-org/x-algorithm
- 仓库描述：Algorithm powering the For You feed on X
- 发布时间信号：原帖时间为 2026-05-15 13:23；Jina 提取显示 16M Views、4.7K replies、6.3K reposts、36K likes、11K bookmarks（这些互动数为抓取时快照）。

## 关键信息与资源

| Type | Name | Link | Why it matters |
|---|---|---|---|
| X Post | Elon Musk announcement | https://x.com/elonmusk/status/2055277918633562153 | X 官方/核心人物宣布最新 For You 算法已开源 |
| GitHub Repo | xai-org/x-algorithm | https://github.com/xai-org/x-algorithm | X For You feed 推荐系统代码与文档入口 |
| README | X For You Feed Algorithm | https://github.com/xai-org/x-algorithm/blob/main/README.md | 解释系统架构、组件、评分与过滤流程 |
| Component | Home Mixer | https://github.com/xai-org/x-algorithm/tree/main/home-mixer | 推荐流编排层：hydration、sources、filters、scorers、selector |
| Component | Thunder | https://github.com/xai-org/x-algorithm/tree/main/thunder | in-network 内容来源：关注账号近期内容的内存存储和实时摄入 |
| Component | Phoenix | https://github.com/xai-org/x-algorithm/tree/main/phoenix | ML 检索与排序组件：Two-Tower retrieval + Transformer ranking |
| Component | Grox | https://github.com/xai-org/x-algorithm/tree/main/grox | 内容理解 pipeline：spam、分类、PTOS policy enforcement 等 |
| Component | Candidate Pipeline | https://github.com/xai-org/x-algorithm/tree/main/candidate-pipeline | 可复用推荐 pipeline 框架：Source/Hydrator/Filter/Scorer/Selector |
| License | Apache-2.0 | https://github.com/xai-org/x-algorithm/blob/main/LICENSE | 允许学习、引用和二次使用，需遵守 Apache 2.0 |

## 仓库快照

通过 GitHub API 抓取到的仓库元信息（整理时快照）：

- `full_name`: `xai-org/x-algorithm`
- `description`: `Algorithm powering the For You feed on X`
- `default_branch`: `main`
- `license`: Apache-2.0
- `created_at`: 2026-01-19T23:12:35Z
- `pushed_at`: 2026-05-15T07:28:46Z
- `updated_at`: 2026-05-15T16:59:42Z
- `stars`: 18,711
- `forks`: 3,225

说明：star/fork 数是抓取时快照，会随时间变化。

## README 中的核心架构

### 1. For You feed 的两类候选来源

README 将候选内容分为两类：

1. In-Network / Thunder：来自用户已关注账号的近期内容。
2. Out-of-Network / Phoenix Retrieval：从全局语料中通过 ML-based retrieval 发现的内容。

这对应任何内容产品都绕不开的两种供给：

- 熟人/已关注关系带来的稳定兴趣；
- 全局发现带来的新鲜感、增长和破圈。

### 2. Phoenix：Two-Tower Retrieval + Transformer Ranking

Phoenix 有两个核心职能：

- Retrieval：User Tower 编码用户特征与互动历史，Candidate Tower 编码帖子，通过 dot product similarity 找 top-K。
- Ranking：Grok-based Transformer 接收用户上下文与候选帖子，预测 like、reply、repost、click、video_view、dwell、follow_author、not_interested、block_author、mute_author、report 等多种行为概率。

最终分数不是单一“相关性”标签，而是多目标行为概率加权：

```text
Final Score = Σ (weight_i × P(action_i))
```

正向行为（like、repost、share 等）加分；负向行为（block、mute、report 等）扣分。

### 3. Pipeline stages

README 描述的主流程：

1. Query Hydration：获取用户近期互动历史、关注列表等上下文。
2. Candidate Sourcing：从 Thunder 与 Phoenix Retrieval 拉取候选。
3. Candidate Hydration：补齐帖子正文、媒体、作者、订阅状态等信息。
4. Pre-Scoring Filters：去重、过旧过滤、屏蔽/静音作者、静音关键词、已看内容、订阅不可见内容等。
5. Scoring：Phoenix Scorer、Weighted Scorer、Author Diversity Scorer、OON Scorer。
6. Selection：按分数排序并选择 top K。
7. Post-Selection Processing：最终可见性与去重检查。

### 4. May 15th, 2026 更新重点

README 的更新摘要包括：

- 新增 `phoenix/run_pipeline.py`，把 retrieval → ranking 合成单一入口，更接近生产组合方式。
- 通过 Git LFS 分发预训练 mini Phoenix 模型：256-dim embeddings、4 attention heads、2 transformer layers，约 3GB。
- 新增 `grox/` 内容理解服务，用于 spam detection、post-category classification、PTOS policy enforcement 等。
- 新增 `home-mixer/ads/` 广告混排模块，含 brand-safety tracking。
- Query hydrators 增加 followed topics、starter packs、impression bloom filters、IP、mutual follow graphs、served history 等上下文。
- Candidate hydrators 增加 engagement counts、brand safety signals、language codes、media detection、quote post expansion、mutual follow scores 等。
- Candidate sources 增加 ads、who to follow、Phoenix MoE、Phoenix topics、prompts，并更新 Thunder/Phoenix 来源。

## 我的吸收判断

- 可复用能力：
  - 推荐系统可以抽象为 Candidate Sources → Hydration → Filters → Multi-objective Scoring → Diversity/Policy Post-processing。
  - 用户行为序列比手工标签更有长期价值：对内容推荐、Agent 任务推荐、知识库检索、增长系统都适用。
  - 负反馈要进入主模型目标，而不是只做事后规则；`P(block/mute/report/not_interested)` 这类负向概率对用户体验至关重要。
  - Candidate isolation 是一个值得记住的工程细节：候选之间不能互相注意，单条内容分数更稳定、可缓存、可复现。

- 值得沉淀到 skill / workflow 吗：
  - 值得作为“推荐系统/内容分发架构”参考，但暂时不需要立刻写成 Hermes skill。
  - 如果后续要做 Demand Radar、Obsidian 智能推荐、X 内容筛选或 AI 信息差 Agent，可以把这里的 pipeline 抽象迁移成 workflow。

- 对 AI × Product × Biohacking / Super Individual 的价值：
  - AI：展示了 LLM/Transformer 如何进入大规模推荐系统，不只是聊天，而是行为预测与排序。
  - Product：For You feed 的核心不是“算法神秘性”，而是候选来源、用户上下文、反馈闭环和约束系统的组合。
  - Biohacking：负反馈建模很像个人信息饮食管理；要让系统知道什么内容让人上瘾、焦虑、浪费时间，并显式降权。
  - Super Individual：个人信息流可以借鉴这个架构，构建“私人 For You”：从 X/Reddit/RSS/Obsidian/GitHub 拉候选，用个人目标与负反馈排序。

- 风险或待验证点：
  - README 是高层说明，不能等同于完整生产系统；真实权重、训练数据、线上实验和策略细节可能未完全开源。
  - “eliminated every single hand-engineered feature” 是 README 声称，需要结合代码与线上行为验证。
  - Ads blending 与 policy enforcement 会影响推荐体验，不能只看 Phoenix 模型本身。
  - Star/fork/互动数据是抓取时快照，后续会变化。

## 可执行下一步

- [ ] 深读 `phoenix/README.md`，提炼 Two-Tower + Transformer ranking 的最小可复用实现。
- [ ] 深读 `candidate-pipeline/`，抽象出通用推荐 pipeline 接口，可迁移到 Demand Radar 或个人信息流。
- [ ] 对照 X 真实 For You 体验，记录算法开源说明与实际内容分布之间的偏差。
- [ ] 为 Obsidian/信息差 Agent 设计一个“私人 For You”原型：候选来源、hydrators、filters、scorers、negative feedback。
- [ ] 如果后续连续整理推荐系统资料，再沉淀一个 `recommendation-system-architecture` skill。

## 宝玉风格 Quote 转发文本

🔥X 最新 For You 算法开源了

1️⃣ 不是简单公开几个排序权重，而是给出完整推荐链路：retrieval → ranking → filtering → selection

2️⃣ 核心是 Thunder（关注账号内容）+ Phoenix（全局发现）+ Grok-based Transformer 多目标行为预测

3️⃣ 最值得看的是负反馈建模：not interested / block / mute / report 都进入排序，而不是事后补丁

4️⃣ 对个人信息流也有启发：未来每个人都需要一个“私人 For You”，用自己的长期目标和负反馈来重排 X/Reddit/RSS/Obsidian

💡算法开源真正的价值，不是照抄 X，而是学习它如何把内容供给、行为序列、约束和反馈闭环组合成系统。

via @elonmusk

---

*来自翡冷翠*
