# 女娲.skill (Nuwa Skill)：认知蒸馏框架完整指南

> 来源：https://github.com/alchaincyf/nuwa-skill  
> 作者：花叔 Huashu (@AlchainHust)  
> 整理时间：2026-04-27

---

## 简介

**女娲.skill** 是一个革命性的 Claude Code Skill，能够"蒸馏"任何人的思维方式——提取心智模型、决策启发式、表达 DNA，将名人的认知操作系统转化为可运行的 AI Skill。

> *「你想蒸馏的下一个员工，何必是同事」*

不同于简单的角色扮演，女娲提取的是深层的认知框架，让乔布斯、马斯克、芒格、费曼等大师为你的决策提供咨询。

---

## 核心概念

### 什么是认知蒸馏？

```
传统角色扮演          女娲认知蒸馏
     │                    │
     ▼                    ▼
┌──────────┐        ┌──────────────┐
│ 复读语录  │        │ 心智模型提取  │
│ 模仿语气  │   vs   │ 决策框架构建  │
│ 表面相似  │        │ 认知OS移植   │
└──────────┘        └──────────────┘
```

**关键区别**：
- 角色扮演 = 模仿说话方式
- 认知蒸馏 = 复刻思维方式

### 女娲提取的五层结构

| 层次 | 内容 | 示例 |
|------|------|------|
| **怎么说话** | 表达 DNA——语气、节奏、用词偏好 | 乔布斯的"insanely great" |
| **怎么想** | 心智模型、认知框架 | Naval 的"欲望即合同" |
| **怎么判断** | 决策启发式 | 马斯克的第一性原理 |
| **什么不做** | 反模式、价值观底线 | 芒格的"逆向思考" |
| **知道局限** | 诚实边界 | 明确标注做不到什么 |

---

## 效果示例

### 场景 1：精力管理咨询

```
用户      ❯ 我同时想做自媒体、写书、做独立开发，精力完全不够

Naval     ❯ 你列了三个欲望。每个欲望都是你跟不快乐签的一份合同。
            不是精力不够，是合同太多。
            
            问你自己：哪一个做起来你会忘记时间？
            那个就是你的特定知识所在。
            
            不是三选一。是先一，再一，再一。
            串行复利，不是并行内耗。
```

**分析**：Naval 使用的不是鸡汤建议，而是他的核心心智模型——「欲望合同论」+「特定知识」+「串行复利」。

### 场景 2：SaaS 获客成本问题

```
用户      ❯ 我们的SaaS产品获客成本太高了

马斯克     ❯ 先别想怎么降。先算物理极限。
            获客的最小必要动作是什么？用户从知道你到付费，
            信息传递的理论最短路径是什么？
            
            现在你的实际路径是理论路径的几倍？
            如果超过3倍，中间一定有可以砍掉的步骤。
            不是优化漏斗，是质疑漏斗本身该不该存在。
```

**分析**：马斯克使用「渐近极限法」——先找理论最优，再算实际差距，最后质疑系统本身。

### 场景 3：AI 行业竞争分析

```
用户      ❯ OpenAI和Anthropic谁的方向是对的？

乔布斯    ❯ 你问错了。这不是一场关于方向的竞赛。
            这是一场关于品味的竞赛。

            OpenAI像1985年的微软。什么都做，什么都要赢。
            这种策略能赢市场份额。Bill Gates就是这么赢的。
            问题是——当你什么都做的时候，你不可能每件事都做到
            insanely great。

            Anthropic更像早期的Apple。聚焦。
            Focus means saying no to a hundred good ideas.

            但两家公司都犯了一个我绝对不会犯的错误——
            他们不控制硬件。

            最终赢的可能是同时控制芯片、模型和用户界面的人。
            你知道现在谁在同时做这三件事吗？Apple.
```

**分析**：乔布斯使用「聚焦即说不」+「端到端控制」+「品味竞赛」三个心智模型。

### 场景 4：教育职业规划

```
用户      ❯ 家里条件一般，孩子想学金融，去不了顶尖学校，该不该报？

张雪峰    ❯ 千万别报。我说过多少遍了，金融不是你学出来的，金融是
            你爹妈给你带出来的。顶尖学校的金融，人家同学是行长的
            儿子、基金经理的女儿，人脉就是资源。你普通家庭去个普通
            学校学金融，毕业出来干什么？卖保险、跑银行柜台、做电销。
            先谋生再谋爱，家里没矿就选技术类专业，学个硬本事，靠
            自己吃饭。金融这碗饭，不是谁都端得起的。
```

**分析**：张雪峰使用「ROI教育观」+「阶层流动现实主义」。

---

## 已蒸馏人物清单

### 人物 Skill（13位）

| 人物 | 领域 | 核心心智模型 | 安装命令 |
|------|------|-------------|---------|
| 🔥 **Paul Graham** | 创业/写作/产品 | 创业思维、写作方法论 | `npx skills add alchaincyf/paul-graham-skill` |
| 🔥 **张一鸣** | 产品/组织/全球化 | 延迟满足、Context not Control | `npx skills add alchaincyf/zhang-yiming-skill` |
| 🔥 **Karpathy** | AI/工程/教育 | 教学即理解、复现即掌握 | `npx skills add alchaincyf/karpathy-skill` |
| 🔥 **Ilya Sutskever** | AI安全/研究 | Scaling Law、研究品味 | `npx skills add alchaincyf/ilya-sutskever-skill` |
| 🔥 **MrBeast** | 内容创造/YouTube | 病毒传播公式、内容工业化 | `npx skills add alchaincyf/mrbeast-skill` |
| 🔥 **特朗普** | 谈判/权力/传播 | 极端出价、注意力经济 | `npx skills add alchaincyf/trump-skill` |
| ⭐ **乔布斯** | 产品/设计/战略 | 聚焦即说不、端到端控制 | `npx skills add alchaincyf/steve-jobs-skill` |
| **马斯克** | 工程/成本/物理 | 第一性原理、渐近极限法 | `npx skills add alchaincyf/elon-musk-skill` |
| **芒格** | 投资/多元思维 | 逆向思考、多元思维模型 | `npx skills add alchaincyf/munger-skill` |
| **费曼** | 学习/教学/科学 | 费曼技巧、教学即理解 | `npx skills add alchaincyf/feynman-skill` |
| **纳瓦尔** | 财富/杠杆/人生 | 欲望即合同、特定知识 | `npx skills add alchaincyf/naval-skill` |
| **塔勒布** | 风险/反脆弱 | 反脆弱、尾部风险 | `npx skills add alchaincyf/taleb-skill` |
| **张雪峰** | 教育/职业规划 | ROI教育观、阶层流动现实 | `npx skills add alchaincyf/zhangxuefeng-skill` |

### 主题 Skill（1个）

| 主题 | 领域 | 安装命令 |
|------|------|---------|
| **X导师** | X/Twitter运营全栈 | `npx skills add alchaincyf/x-mentor-skill` |

---

## 工作原理

### 四阶段流程

```
┌─────────────────────────────────────────────────────────────────┐
│                     女娲工作流程                                 │
├─────────────┬─────────────┬─────────────┬─────────────────────┤
│  1. 采集    │  2. 提炼     │  3. 构建    │   4. 验证           │
├─────────────┼─────────────┼─────────────┼─────────────────────┤
│             │             │             │                     │
│ 6路并行     │ 三重验证    │ 3-7个心智   │ 已知问题测试        │
│ 调研代理    │ 筛选机制    │ 模型提取    │ 方向一致性          │
│             │             │             │                     │
│ • 著作      │ 必须跨2+    │ 5-10条决策  │ 未知问题测试        │
│ • 播客/访谈 │ 领域出现    │ 启发式      │ 适度不确定性        │
│ • 社交媒体  │             │             │                     │
│ • 批评者视角│ 必须有      │ 表达DNA     │ 通过 → 生成Skill    │
│ • 决策记录  │ 预测力      │ 价值观边界  │ 失败 → 重跑         │
│ • 人生时间线│             │             │                     │
│             │ 必须有      │             │                     │
│             │ 排他性      │             │                     │
│             │             │             │                     │
└─────────────┴─────────────┴─────────────┴─────────────────────┘
```

### 详细说明

**Phase 1: 六路并行采集**
- 6个独立 Agent 同时工作
- 收集 40+ 一手资料
- 各自存档、交叉验证

**Phase 2: 三重验证提炼**
一个观点要被收录为心智模型，必须同时满足：
1. **跨领域验证**：在 2+ 个不同领域出现过（非随口一说）
2. **预测力验证**：能推断对新问题的立场
3. **排他性验证**：不是所有聪明人都会这么想

**Phase 3: Skill 构建**
输出 SKILL.md 包含：
- 3-7 个心智模型
- 5-10 条决策启发式
- 表达 DNA 特征
- 价值观与反模式
- 诚实边界声明

**Phase 4: 质量验证**
- 用 3 个此人公开回答过的问题测试
- 方向一致才通过
- 再用 1 个未讨论过的问题测试
- Skill 应表现出适度不确定而非斩钉截铁

---

## 安装与使用

### 安装女娲

```bash
npx skills add alchaincyf/nuwa-skill
```

### 创建新 Skill

在 Claude Code 中：

```
> 蒸馏一个保罗·格雷厄姆
> 造一个张小龙的视角Skill
> 帮我做一个段永平的Skill
```

### 使用已蒸馏 Skill

```
> 用芒格的视角帮我分析这个投资决策
> 费曼会怎么解释量子计算？
> 切换到Naval，我在纠结三件事
```

---

## 相关项目

### 达尔文.skill (Darwin Skill)

**功能**：让所有 Skill 持续进化

**原理**：
- 8维度评估体系
- 棘轮机制（只保留改进，自动回滚退步）
- 独立子 Agent 评分

**安装**：
```bash
npx skills add alchaincyf/darwin-skill
```

**关系**：女娲的 Phase 5 双 Agent 精炼内置了达尔文的评估体系。

### Bloome

**功能**：多 Agent 协作平台

**特点**：
- 同时与多个蒸馏人物对话
- 人和多个 Agent 在同一对话中协作
- 乔布斯 + 张小龙一起聊产品

**访问**：https://www.bloome.im

### 同事.skill (Colleague Skill)

**功能**：蒸馏身边同事

**与女娲的区别**：
- 同事.skill = 蒸馏熟悉的人（基于日常互动）
- 女娲.skill = 蒸馏名人（基于公开资料）

**链接**：https://github.com/titanwings/colleague-skill

---

## 技术架构

### 仓库结构

```
nuwa-skill/
├── SKILL.md                      # 女娲本体（核心逻辑）
├── references/
│   ├── extraction-framework.md   # 提炼方法论详解
│   └── skill-template.md         # 生成Skill的模板
└── examples/                     # 13个人物 + 1个主题
    ├── steve-jobs-perspective/   # ⭐ 含完整对话记录
    ├── paul-graham-perspective/
    ├── zhang-yiming-perspective/
    ├── andrej-karpathy-perspective/
    ├── ilya-sutskever-perspective/
    ├── trump-perspective/
    ├── mrbeast-perspective/
    ├── elon-musk-perspective/
    ├── munger-perspective/
    ├── feynman-perspective/
    ├── naval-perspective/
    ├── taleb-perspective/
    ├── zhangxuefeng-perspective/
    └── x-mastery-mentor/         # 主题Skill
```

### 数据透明度

每个 example 包含：
- 完整的调研文件（可追溯信息来源）
- 筛选过程记录（了解信息如何变成心智模型）
- 实战对话记录（多轮深度对话示例）

---

## 应用场景

### 个人决策
- 重大人生选择咨询（Naval、芒格）
- 学习方法优化（费曼、Karpathy）
- 职业规划（张雪峰、张一鸣）

### 创业/产品
- 产品战略（乔布斯、张一鸣）
- 创业方向（Paul Graham）
- 内容策略（MrBeast、X导师）

### 投资/商业
- 投资决策（芒格、Naval）
- 风险评估（塔勒布）
- 成本优化（马斯克）

### AI/技术
- AI安全思考（Ilya）
- 工程实践（Karpathy）
- 研究品味（Ilya）

---

## 诚实边界（局限说明）

**女娲明确标注做不到什么**：

| 局限 | 说明 |
|------|------|
| **蒸馏不了直觉** | 框架能提取，灵感/直觉不能 |
| **捕捉不了突变** | 截止到调研时间的认知快照 |
| **公开 ≠ 真实** | 只能基于公开信息，非真实想法 |
| **无法验证内在** | 无法确认人物真实决策过程 |

**原则**：一个不告诉你局限在哪的 Skill，不值得信任。

---

## 关于作者

**花叔 Huashu** — AI Native Coder，独立开发者

**代表作**：小猫补光灯（AppStore 付费榜 Top1）

| 平台 | 链接 |
|------|------|
| 🌐 官网 | [bookai.top](https://bookai.top) · [huasheng.ai](https://www.huasheng.ai) |
| 𝕏 Twitter | [@AlchainHust](https://x.com/AlchainHust) |
| 📺 B站 | [花叔](https://space.bilibili.com/14097567) |
| ▶️ YouTube | [@Alchain](https://www.youtube.com/@Alchain) |
| 📕 小红书 | [花叔](https://www.xiaohongshu.com/user/profile/5abc6f17e8ac2b109179dfdf) |

---

## 参考资源

### 核心仓库
- **女娲.skill**：https://github.com/alchaincyf/nuwa-skill ⭐14.8k
- **达尔文.skill**：https://github.com/alchaincyf/darwin-skill
- **同事.skill**：https://github.com/titanwings/colleague-skill

### 方法论文档
- **extraction-framework.md**：https://github.com/alchaincyf/nuwa-skill/blob/main/references/extraction-framework.md
- **SKILL.md 模板**：https://github.com/alchaincyf/nuwa-skill/blob/main/references/skill-template.md

### 扩展阅读
- **Skills.sh**：https://skills.sh — Claude Code Skill 生态
- **Bloome**：https://www.bloome.im — 多 Agent 协作平台

---

## 名言摘录

> "同事.skill 蒸馏了人做什么。女娲蒸馏了人怎么想。"

> "女娲不复制人。它提取认知操作系统。"

> "你想蒸馏的下一个员工，何必是同事。"

---

*来自翡冷翠*
