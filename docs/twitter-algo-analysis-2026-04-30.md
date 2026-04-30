# Twitter 推荐算法深度解析 - 工程与架构完整指南

> **来源**: [awesome-twitter-algo](https://github.com/igorbrigadir/awesome-twitter-algo)  
> **作者**: Igor Brigadir & Vicki Boykis  
> **整理时间**: 2026-04-30  
> 来自翡冷翠

---

## 简介

这是Twitter（现X）2023年开源推荐系统代码的深度注解版本。由Igor Brigadir和Vicki Boykis两位工程师从推荐系统工程(recsys)视角，对复杂的代码库进行结构化解读和上下文补充。

文档核心价值在于：**将难以直接理解的原始代码转化为有工程意义的系统设计知识**，帮助读者理解工业级推荐系统如何从每天5亿条推文中筛选出约1500条候选内容，最终呈现给用户"For You"时间线。

---

## 内容清单总览

| 序号 | 主题 | 类型 | 核心亮点 |
|------|------|------|----------|
| 1 | 推荐系统整体架构 | 架构设计 | 四阶段pipeline：候选生成→排序→过滤→展示 |
| 2 | GraphJet 图推荐引擎 | 开源项目 | 实时内存图处理，单服务器每秒处理100万边 |
| 3 | SimClusters 社区发现 | 算法/论文 | 10亿用户x10万维度的社区Embedding |
| 4 | TwHIN 异构信息网络 | 算法/论文 | 多实体多关系图神经网络 |
| 5 | 候选生成器对比 | 技术分析 | GraphJet vs SimClusters vs TwHIN vs RealGraph |
| 6 | 双阶段排序系统 | 模型设计 | Light Ranker(逻辑回归) + Heavy Ranker(MaskNet) |
| 7 | 多目标打分公式 | 工程细节 | 10个行为预测值的加权计算 |
| 8 | 多样性与公平性控制 | 产品策略 | Author Diversity、Feedback Fatigue、Blue Verified加成 |

---

## 详细内容

### 1. 推荐系统整体架构

**来源**: Twitter Engineering Blog  
**链接**: https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm  
**类型**: 架构设计

#### 核心内容

Twitter "For You"时间线推荐遵循标准的推荐系统四阶段pipeline：

```
┌─────────────────────────────────────────────────────────────────┐
│                    Twitter 推荐系统架构                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│  │ 候选生成    │ → │  排序    │ → │  过滤    │ → │ 展示排序 │  │
│  │ Candidates  │    │ Ranking │    │ Filter  │    │ Ordering│  │
│  └─────────────┘    └─────────┘    └─────────┘    └─────────┘  │
│                                                                 │
│  • ~1500候选      • Light Ranker  • Visibility   • Author Div  │
│  • 多源聚合        • Heavy Ranker • 安全过滤      • Blue Boost  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**关键数据点**:
- 每天约5亿条新推文进入系统
- 候选生成阶段筛选出约1500条候选
- In-Network(关注)与Out-of-Network(未关注)内容各占约50%

#### 关键资源

- **架构图**: https://whimsical.com/twitter-archtecture-PoR7TJb1eac2UofLVSY28e
- **主仓库**: https://github.com/twitter/the-algorithm
- **ML仓库**: https://github.com/twitter/the-algorithm-ml

---

### 2. GraphJet - 实时图推荐引擎

**来源**: Twitter GitHub  
**链接**: https://github.com/twitter/GraphJet  
**论文**: http://www.vldb.org/pvldb/vol9/p1281-sharma.pdf  
**类型**: 开源项目/学术研究

#### 核心内容

GraphJet是Twitter开发的**实时内存图处理库**，核心设计思想是"反传统"：

> *"当业界都在构建分布式图存储时，Twitter选择了单服务器全内存的方案。"*

**技术特点**:
- **存储**: 实时二分图(bipartite graph)存储在内存中
- **吞吐量**: 单服务器每秒摄入100万条图边，计算500个推荐/秒
- **输入**: 从Kafka读取用户-推文交互数据(点击、点赞、转发、回复、发推)
- **算法**: 实现两种随机游走算法
  - Circle of Trust (Twitter内部)
  - SALSA (Stochastic Approach for Link-Structure Analysis)

**演进历程**:
1. **2010年**: Cassovary + WTF (Who to Follow) - 仅做用户推荐
2. **2012年**: 迁移到Hadoop MapReduce
3. **MagicRecs**: 补充Hadoop方案
4. **GraphJet**: 统一实时推荐基础设施

#### 适用场景

适合需要**实时个性化内容推荐**的场景，特别是：
- 社交网络的"你可能感兴趣的内容"
- 基于协同过滤的推荐
- 需要低延迟(毫秒级)的推荐查询

---

### 3. SimClusters - 社区发现Embedding

**来源**: Twitter GitHub / ACM RecSys  
**链接**: https://github.com/twitter/the-algorithm/tree/main/simclusters-ann  
**论文**: https://dl.acm.org/doi/10.1145/3394486.3403370  
**类型**: 算法实现/学术研究

#### 核心内容

SimClusters是Twitter的**社区发现Embedding系统**，核心创新在于用ANN(近似最近邻)代替传统矩阵分解：

> *"传统矩阵分解计算成本太高，SimClusters用社区结构+ANN实现了可扩展的表示学习。"*

**技术架构**:
```
┌──────────────────────────────────────────────────┐
│              SimClusters 两阶段处理               │
├──────────────────────────────────────────────────┤
│                                                  │
│  Stage 1 (MR Job)       Stage 2 (并行计算)       │
│  ┌──────────────┐      ┌──────────────────┐     │
│  │ 用户-用户图   │      │ 目标表示计算      │     │
│  │ → 社区发现   │  →   │ User Interest    │     │
│  │              │      │ Representations  │     │
│  └──────────────┘      └──────────────────┘     │
│                                                  │
│  • 算法: Metropolis-Hastings                    │
│  • 规模: 10亿用户 x 10万社区维度                 │
│  • 优势: 长尾内容友好                            │
│                                                  │
└──────────────────────────────────────────────────┘
```

**工程实现**:
- **离线**: Hadoop MapReduce计算社区和Embedding
- **在线**: SimClusters ANN服务提供实时相似内容查询
- **实时组件**: Heron流作业维护SimClusters与推文的映射关系

#### 适用场景

- 兴趣社区 discovery
- 跨领域推荐(推文、话题、事件、用户)
- 需要捕捉"社区影响力"的推荐

---

### 4. TwHIN - Twitter异构信息网络

**来源**: Twitter GitHub / arXiv  
**链接**: https://github.com/twitter/the-algorithm-ml/tree/main/projects/twhin  
**论文**: https://arxiv.org/pdf/2202.05387.pdf  
**类型**: 算法实现/学术研究

#### 核心内容

TwHIN (Twitter Heterogeneous Information Network)是Twitter的**异构图神经网络**实现：

**实体类型(Nodes)**:
- User (用户)
- Tweet (推文)
- Advertiser (广告主)
- Ad (广告)

**关系类型(Edges)**:
- Follow (关注)
- Authors (发布)
- Favourites (点赞)
- Replies (回复)
- Retweets (转发)
- Promotes (推广)
- Clicks (点击)

**两种网络变体**:

1. **TwHIN-Follow**: 以用户-用户关注图为核心
   - 2.61亿边，1550万顶点
   - HuggingFace数据集: `Twitter/TwitterFollowGraph`

2. **TwHIN-Engagement**: 以用户-推文交互为核心
   - 670万用户节点，1300万推文节点，2.83亿边
   - HuggingFace数据集: `Twitter/TwitterFaveGraph`

**训练资源**:
- 16x A100 GPUs
- 1.4TB RAM

#### 适用场景

- 需要建模多种实体和关系的推荐系统
- 广告推荐(结合User/Tweet/Advertiser/Ad)
- 多目标多行为预测

---

### 5. 候选生成器技术对比

| 特性 | GraphJet | SimClusters | TwHIN | RealGraph |
|------|----------|-------------|-------|-----------|
| **核心方法** | 图随机游走 | 社区发现+ANN | 异构图网络 | XGBoost |
| **实时性** | 实时(内存) | 准实时 | 离线+在线 | 准实时 |
| **数据规模** | 单机内存 | 10亿用户 | 多实体 | 关注+交互用户 |
| **推荐类型** | 内容推荐 | 内容/话题/用户 | 多实体推荐 | 互动预测 |
| **算法** | SALSA随机游走 | Metropolis-Hastings | 图神经网络 | XGBoost |
| **基础设施** | Kafka + 内存 | Hadoop + Heron | 16xA100 | BigQuery ML |

---

### 6. 双阶段排序系统

**来源**: Twitter ML Repo  
**链接**: https://github.com/twitter/the-algorithm-ml/tree/main/projects/home/recap  
**类型**: 模型设计

#### 核心内容

Twitter采用**双阶段排序**平衡计算成本与精度：

```
┌──────────────────────────────────────────────────────────────┐
│                    双阶段排序流程                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   ~1500 候选                                                  │
│       ↓                                                      │
│   ┌──────────────────┐                                       │
│   │  Light Ranker    │  ← 逻辑回归 (Logistic Regression)     │
│   │  轻量排序器       │     快速筛选                          │
│   └──────────────────┘                                       │
│       ↓ ~数百条                                              │
│   ┌──────────────────┐                                       │
│   │  Heavy Ranker    │  ← MaskNet 神经网络                   │
│   │  重量排序器       │     精排                              │
│   └──────────────────┘                                       │
│       ↓                                                      │
│   最终展示排序                                                 │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Light Ranker**:
- 模型: 逻辑回归
- 目的: 快速筛选，减少Heavy Ranker的计算量
- 特点: In-Network和Out-of-Network使用不同模型
- 训练: TWML (Twitter's deprecated ML framework)

**Heavy Ranker**:
- 模型: Parallel MaskNet
- 输入: 大量社交信号和Embedding特征
- 重要发现: *"排名算法中没有基于内容的Embedding"* - 主要依赖社交信号

---

### 7. 多目标打分公式

**来源**: Twitter ML Repo  
**链接**: https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md  
**类型**: 工程细节

#### 核心内容

Heavy Ranker预测10种用户行为概率，加权求和得到最终分数：

| 行为预测 | 权重 | 说明 |
|---------|------|------|
| 点赞(Favorite) | 0.5 | 最基础的正向信号 |
| 点击对话并回复/点赞 | 11 | 深度参与 |
| 点击对话停留≥2分钟 | 11 | 防止评论诱导 |
| 负反馈(隐藏/静音/屏蔽) | -74 | 强烈的负面信号 |
| 打开作者主页并互动 | 12 | 对作者感兴趣 |
| 回复推文 | 27 | 对话参与 |
| 回复被作者回复 | 75 | 高质量对话 |
| 举报推文 | -369 | 最严重的负面信号 |
| 转发 | 1 | 扩散行为 |
| 视频观看≥50% | 0.005 | 视频完成度 |

**打分公式**:
```
Score = P(fav)×0.5 + max(P(click_reply), P(click_stay_2min))×11 
      + P(negative)×(-74) + P(visit_author)×12 + P(reply)×27 
      + P(author_reply_to_me)×75 + P(report)×(-369) 
      + P(retweet)×1 + P(video_half)×0.005
```

**关键洞察**:
1. **鼓励对话**: 回复权重(27) + 被作者回复权重(75) = Twitter想成为"互联网广场"
2. **防御评论诱导**: 停留≥2分钟才计分，防止"点击标题党即离开"
3. **视频完成度权重极低**(0.005): 不同于TikTok的隐式反馈学习
4. **负反馈惩罚重**: 举报(-369)远高于普通负反馈(-74)

---

### 8. 多样性与公平性控制

**来源**: Twitter GitHub  
**类型**: 产品策略

#### 核心内容

打完分后，系统还会应用多种heuristics调整最终展示：

**1. Author Diversity - 作者多样性**
- 避免连续展示同一作者的推文
- 公式: `score * ((1 - 0.25) * Math.pow(0.5, position) + 0.25)`
- 同一feed中已出现过的作者，分数折半(有下限)

**2. Content Balance - 内容平衡**
- 平衡In-Network(关注)和Out-of-Network(未关注)内容
- 默认各占约50%

**3. Feedback-based Fatigue - 反馈疲劳**
- 对收到负反馈的内容/作者降权
- 14天内负反馈: 可能直接过滤
- 14-154天负反馈: 权重递减
- 对"给该内容点赞的用户"也提供负反馈选项

**4. Social Proof - 社交证明**
- Out-of-Network内容需要二度连接(朋友互动过)
- 纯陌生人内容获得0.75的降权系数

**5. Twitter Blue加成**
- In-Network认证用户: **4倍**分数加成
- Out-of-Network认证用户: **2倍**分数加成
- 注意: 认证用户未关注时反而获得更大加成

---

## 资源汇总

### GitHub 仓库

| 项目 | 链接 | 简介 |
|------|------|------|
| awesome-twitter-algo | https://github.com/igorbrigadir/awesome-twitter-algo | 本注解文档 |
| the-algorithm | https://github.com/twitter/the-algorithm | Twitter主算法仓库 |
| the-algorithm-ml | https://github.com/twitter/the-algorithm-ml | Twitter ML算法仓库 |
| GraphJet | https://github.com/twitter/GraphJet | 实时图推荐引擎 |
| Scalding | https://github.com/twitter/scalding | Spark前身，Twitter开发 |
| Cassovary | https://github.com/twitter/cassovary | 内存图处理引擎 |

### 学术论文

| 论文 | 链接 | 主题 |
|------|------|------|
| GraphJet | http://www.vldb.org/pvldb/vol9/p1281-sharma.pdf | 实时图推荐 |
| SimClusters | https://dl.acm.org/doi/10.1145/3394486.3403370 | 社区发现Embedding |
| TwHIN | https://arxiv.org/pdf/2202.05387.pdf | 异构信息网络 |
| WTF | https://web.stanford.edu/~rezab/papers/wtf_overview.pdf | 用户推荐系统 |
| MaskNet | https://arxiv.org/abs/2102.07619 | 精排模型架构 |

### 官方博客

| 文章 | 链接 | 主题 |
|------|------|------|
| 算法开源公告 | https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm | 整体架构 |
| Snowflake | https://blog.twitter.com/engineering/en_us/a/2010/announcing-snowflake | ID生成系统 |
| Earlybird | https://blog.twitter.com/engineering/en_us/a/2011/the-engineering-behind-twitter-s-new-search-experience | 搜索索引 |
| Heron | https://blog.twitter.com/engineering/en_us/topics/open-source/2018/heron-donated-to-apache-software-foundation | 流处理框架 |
| Manhattan | https://blog.twitter.com/engineering/en_us/a/2014/manhattan-our-real-time-multi-tenant-distributed-database-for-twitter-scale | 分布式数据库 |

### 推荐系统学习资源

| 资源 | 链接 | 类型 |
|------|------|------|
| Karl Higley的博客 | https://practicalrecs.com/the-rest-of-the-owl.html | 博客 |
| Google Recsys课程 | https://developers.google.com/machine-learning/recommendation | 教程 |
| ACM Recsys | https://recsys.acm.org/ | 学术会议 |
| Recsys Handbook | https://link.springer.com/book/10.1007/978-1-0716-2197-4 | 教材 |
| NVIDIA Merlin | https://medium.com/nvidia-merlin/recommender-systems-not-just-recommender-models-485c161c755e | 架构指南 |

---

## 建议学习路径

### 路径A: 快速了解(30分钟)
1. 阅读本文档的"整体架构"和"多目标打分"章节
2. 浏览架构图(Whimsical链接)
3. 理解"四阶段pipeline"概念

### 路径B: 工程深入(2-3小时)
1. 完成路径A
2. 深入阅读GraphJet/SimClusters/TwHIN技术细节
3. 下载相关论文阅读
4. 查看GitHub上的关键代码文件

### 路径C: 动手实践(1-2天)
1. 完成路径B
2. 克隆twitter/the-algorithm仓库
3. 使用HuggingFace上的TwHIN数据集做实验
4. 尝试在自己的数据集上实现简化版的候选生成+排序流程

---

## 附录：Twitter内部术语速查

| 术语 | 全称 | 含义 |
|------|------|------|
| Twepoch | Twitter Epoch | 2010-11-04开始的时间戳基准(1288834974657) |
| Snowflake | - | Twitter的分布式ID生成系统 |
| WTF | Who to Follow | 用户推荐服务 |
| DDG | Duck Duck Goose | Twitter的A/B测试平台 |
| Earlybird | - | 基于Lucene的实时搜索索引 |
| GraphJet | - | 实时图推荐引擎 |
| SimClusters | Similar Clusters | 社区发现Embedding系统 |
| TwHIN | Twitter HIN | 异构信息网络 |
| ANN | Approximate Nearest Neighbors | 近似最近邻 |
| MR | MapReduce | Hadoop批处理作业 |
| Heron | - | 实时流处理框架(类似Flink) |
| Finagle | - | RPC服务框架 |
| Manhattan | - | 分布式数据库 |
| Strato | - | 虚拟数据库(微服务驱动) |
| UUM | Unregretted User Minutes | Twitter声称优化的核心指标 |

---

## 常见偏见与操控争议

**去Boosting竞争对手链接**
- 代码中存在`OutOfNetworkCompetitorURLFilter`，但未公开具体配置
- 长期传闻YouTube链接被大幅降权

**Elon Musk特殊处理**
- 开源初期代码中有针对Elon账户的特殊feature flag
- 开源2小时后被移除
- 官方解释: 仅用于内部A/B测试监控

**乌克兰相关内容**
- 存在`UkraineCrisisTopic`安全标签
- 功能: 对乌克兰危机相关Space进行特殊审核标记

---

*来自翡冷翠*
