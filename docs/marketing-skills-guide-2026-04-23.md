# Marketing Skills - AI 增长工程技能库完整指南

> 来源：[X/Twitter @tuturetom](https://x.com/tuturetom/status/2047300357202588150?s=20)  
> 项目地址：[GitHub - coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)  
> 整理时间：2026-04-23  
> 来自翡冷翠

---

## 简介

**Marketing Skills** 是一个专为 AI Agent（Claude Code、OpenAI Codex、Cursor、Windsurf 等）设计的增长工程技能库，由 Corey Haines 创建。该项目短时间内飙升 **23.4k+ stars**，成为营销领域最受欢迎的 AI Agent 技能集合之一。

核心价值：**让人人都能成为增长工程师** —— 通过预置的技能文件，让 AI Agent 自动帮你完成文案撰写、SEO 优化、转化率优化（CRO）、数据分析、增长工程等全链路营销任务。

---

## 什么是 Skills？

Skills 是 Markdown 格式的文件，为 AI Agent 提供特定任务的专业知识和工作流程。将这些技能文件添加到项目后，AI Agent 可以识别你正在进行的营销任务，并自动应用正确的框架和最佳实践。

### 技能协作架构

所有技能都围绕 `product-marketing-context`（产品营销上下文）技能构建——每个技能都会先读取该文件来理解你的产品、受众和定位，然后再执行任务。

```
                        ┌──────────────────────────────────────┐
                        │      product-marketing-context       │
                        │    (read by all other skills first)  │
                        └──────────────────┬───────────────────┘
                                           │
    ┌──────────────┬─────────────┬──────────┼──────────┬──────────────┬──────────────┐
    ▼              ▼             ▼         ▼          ▼              ▼              ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────────┐ ┌───────────┐
│  SEO &   │ │   CRO    │ │Content & │ │  Paid &  │ │ Growth & │ │  Sales &    │ │ Strategy  │
│ Content  │ │          │ │   Copy   │ │Measurement│ │Retention │ │    GTM      │ │           │
└──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └─────────────┘ └───────────┘
```

---

## 38 个可用技能清单

| 技能名称 | 类别 | 用途描述 |
|----------|------|----------|
| [ab-test-setup](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ab-test-setup) | 测试 | 设计、规划或实施 A/B 测试，建立增长实验体系 |
| [ad-creative](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ad-creative) | 付费广告 | 生成、迭代或扩展广告创意——标题、描述、主文案 |
| [ai-seo](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ai-seo) | SEO | 为 AI 搜索引擎优化内容，获取 LLM 引用和 AI 生成答案中的曝光 |
| [analytics-tracking](https://github.com/coreyhaines31/marketingskills/tree/main/skills/analytics-tracking) | 测量 | 设置、改进或审计分析追踪和数据测量 |
| [aso-audit](https://github.com/coreyhaines31/marketingskills/tree/main/skills/aso-audit) | SEO | 审计或优化 App Store / Google Play 应用商店列表 |
| [churn-prevention](https://github.com/coreyhaines31/marketingskills/tree/main/skills/churn-prevention) | 留存 | 降低流失率，建立取消流程、挽回优惠、失败支付恢复 |
| [cold-email](https://github.com/coreyhaines31/marketingskills/tree/main/skills/cold-email) | 内容 | 撰写 B2B 冷邮件和跟进序列，提高回复率 |
| [community-marketing](https://github.com/coreyhaines31/marketingskills/tree/main/skills/community-marketing) | 增长 | 建立和利用在线社区推动产品增长和品牌忠诚度 |
| [competitor-alternatives](https://github.com/coreyhaines31/marketingskills/tree/main/skills/competitor-alternatives) | SEO | 创建竞品对比或替代页面，用于 SEO 和销售支持 |
| [competitor-profiling](https://github.com/coreyhaines31/marketingskills/tree/main/skills/competitor-profiling) | 策略 | 从 URL 研究、分析竞争对手 |
| [content-strategy](https://github.com/coreyhaines31/marketingskills/tree/main/skills/content-strategy) | 内容 | 规划内容策略，决定创建什么内容、覆盖什么主题 |
| [copy-editing](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copy-editing) | 内容 | 编辑、审查或改进现有营销文案，刷新过时内容 |
| [copywriting](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copywriting) | 内容 | 为任何页面撰写、重写或改进营销文案 |
| [customer-research](https://github.com/coreyhaines31/marketingskills/tree/main/skills/customer-research) | 策略 | 进行、分析或综合客户研究 |
| [directory-submissions](https://github.com/coreyhaines31/marketingskills/tree/main/skills/directory-submissions) | 增长 | 提交产品到创业、SaaS、AI、Agent 等目录 |
| [email-sequence](https://github.com/coreyhaines31/marketingskills/tree/main/skills/email-sequence) | 内容 | 创建或优化邮件序列、滴灌活动、自动化邮件流 |
| [form-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/form-cro) | CRO | 优化非注册表单——线索捕获、联系表单等 |
| [free-tool-strategy](https://github.com/coreyhaines31/marketingskills/tree/main/skills/free-tool-strategy) | 增长 | 规划、评估或构建免费工具用于营销目的 |
| [launch-strategy](https://github.com/coreyhaines31/marketingskills/tree/main/skills/launch-strategy) | 策略 | 规划产品发布、功能公告或发布策略 |
| [lead-magnets](https://github.com/coreyhaines31/marketingskills/tree/main/skills/lead-magnets) | 增长 | 创建、规划或优化线索磁铁（lead magnet） |
| [marketing-ideas](https://github.com/coreyhaines31/marketingskills/tree/main/skills/marketing-ideas) | 策略 | 为 SaaS 或软件产品获取营销创意和策略（含 140 个想法） |
| [marketing-psychology](https://github.com/coreyhaines31/marketingskills/tree/main/skills/marketing-psychology) | 策略 | 将心理学原理、心理模型或行为科学应用于营销 |
| [onboarding-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/onboarding-cro) | CRO | 优化注册后引导、用户激活、首次体验 |
| [page-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/page-cro) | CRO | 优化任何营销页面——首页、落地页、定价页等 |
| [paid-ads](https://github.com/coreyhaines31/marketingskills/tree/main/skills/paid-ads) | 付费 | Google Ads、Meta、LinkedIn、Twitter/X 等付费广告 |
| [paywall-upgrade-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/paywall-upgrade-cro) | CRO | 创建或优化应用内付费墙、升级页面、追加销售弹窗 |
| [popup-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/popup-cro) | CRO | 创建或优化弹窗、模态框、叠加层、滑入框 |
| [pricing-strategy](https://github.com/coreyhaines31/marketingskills/tree/main/skills/pricing-strategy) | 策略 | 定价决策、包装、货币化策略 |
| [product-marketing-context](https://github.com/coreyhaines31/marketingskills/tree/main/skills/product-marketing-context) | 基础 | 创建或更新产品营销上下文文档（所有技能的基础） |
| [programmatic-seo](https://github.com/coreyhaines31/marketingskills/tree/main/skills/programmatic-seo) | SEO | 使用模板和数据大规模创建 SEO 页面 |
| [referral-program](https://github.com/coreyhaines31/marketingskills/tree/main/skills/referral-program) | 增长 | 创建、优化或分析推荐计划、联盟计划 |
| [revops](https://github.com/coreyhaines31/marketingskills/tree/main/skills/revops) | 销售 | 收入运营、线索生命周期管理、营销到销售交接 |
| [sales-enablement](https://github.com/coreyhaines31/marketingskills/tree/main/skills/sales-enablement) | 销售 | 创建销售资料、演示文稿、单页、异议处理文档 |
| [schema-markup](https://github.com/coreyhaines31/marketingskills/tree/main/skills/schema-markup) | SEO | 添加、修复或优化结构化数据和 Schema 标记 |
| [seo-audit](https://github.com/coreyhaines31/marketingskills/tree/main/skills/seo-audit) | SEO | 审计、审查或诊断网站的 SEO 问题 |
| [signup-flow-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/signup-flow-cro) | CRO | 优化注册、账户创建、试用激活流程 |
| [site-architecture](https://github.com/coreyhaines31/marketingskills/tree/main/skills/site-architecture) | SEO | 规划、映射或重组网站页面层次、导航、URL 结构 |
| [social-content](https://github.com/coreyhaines31/marketingskills/tree/main/skills/social-content) | 内容 | 创建、安排或优化 LinkedIn、Twitter/X、Instagram 等社交内容 |

---

## 六大技能类别详解

### 1. 转化率优化 (CRO)

包含 6 个技能，覆盖从首次访问到付费转化的全流程：

| 技能 | 适用场景 |
|------|----------|
| **page-cro** | 优化任何营销页面（首页、落地页、定价页、功能页） |
| **signup-flow-cro** | 优化注册流程、账户创建、试用激活 |
| **onboarding-cro** | 优化注册后引导、用户激活、首次体验 |
| **form-cro** | 优化线索捕获表单、联系表单（非注册表单） |
| **popup-cro** | 创建/优化弹窗、模态框、叠加层、横幅 |
| **paywall-upgrade-cro** | 优化应用内付费墙、升级页面、追加销售 |

**page-cro 核心框架：**
- **价值主张清晰度**（最高影响）：访客能否在 5 秒内理解这是什么、为什么应该关注
- **标题有效性**：是否传达了核心价值主张？是否足够具体？
- **CTA 布局、文案和层级**：主要行动是否清晰可见？按钮文案是否传达价值？
- **视觉层次和可扫描性**：扫描者能否获取主要信息？
- **信任信号和社交证明**：客户 logo、推荐语、案例研究、评论分数
- **异议处理**：价格/价值担忧、"这适合我吗？"、实施难度
- **摩擦点**：表单字段过多、步骤不清晰、移动端体验问题

---

### 2. 内容与文案

| 技能 | 适用场景 |
|------|----------|
| **copywriting** | 撰写任何营销页面的文案——首页、落地页、定价页 |
| **copy-editing** | 编辑、审查或改进现有文案 |
| **cold-email** | B2B 冷邮件和跟进序列 |
| **email-sequence** | 自动化邮件流、生命周期邮件 |
| **social-content** | LinkedIn、Twitter/X、Instagram 等社交内容 |

**copywriting 核心原则：**
- **清晰胜过巧妙**：如果必须在清晰和创意之间选择，选清晰
- **利益胜过功能**：功能是它做什么，利益是这对客户意味着什么
- **具体胜过模糊**："将周报从 4 小时缩短到 15 分钟" > "节省工作流程时间"
- **客户语言胜过公司语言**：使用客户实际使用的词汇
- **主动胜过被动**："我们生成报告" > "报告被生成"
- **展示胜过讲述**：描述结果而不是使用副词

**文案质量快速检查清单：**
- [ ] 可能让外人困惑的行话？
- [ ] 试图表达太多的句子？
- [ ] 被动语态结构？
- [ ] 感叹号？（删除它们）
- [ ] 没有实质内容的营销流行词？

---

### 3. SEO 与发现

| 技能 | 适用场景 |
|------|----------|
| **seo-audit** | 技术和页面 SEO 审计 |
| **ai-seo** | AI 搜索优化（AEO、GEO、LLMO） |
| **programmatic-seo** | 规模化页面生成 |
| **site-architecture** | 页面层次、导航、URL 结构 |
| **competitor-alternatives** | 竞品对比和替代页面 |
| **schema-markup** | 结构化数据标记 |

**seo-audit 优先级框架：**
1. **可抓取性和索引**（Google 能找到和索引吗？）
2. **技术基础**（网站快速且功能正常吗？）
3. **页面优化**（内容优化了吗？）
4. **内容质量**（值得排名吗？）
5. **权威和链接**（有可信度吗？）

**技术审计要点：**
- robots.txt 检查（意外阻止、重要页面允许）
- XML Sitemap（存在、可访问、提交到 Search Console、包含规范 URL）
- 网站架构（重要页面距首页 3 次点击内、逻辑层次、内链结构）
- 索引状态（site:domain.com 检查、Search Console 覆盖率报告）
- 核心网页指标（LCP < 2.5s、INP < 200ms、CLS < 0.1）

---

### 4. 付费广告与分发

| 技能 | 适用场景 |
|------|----------|
| **paid-ads** | Google、Meta、LinkedIn、Twitter/X 广告活动 |
| **ad-creative** | 批量广告创意生成和迭代 |
| **social-content** | 社交媒体排期和策略 |

---

### 5. 测量与测试

| 技能 | 适用场景 |
|------|----------|
| **analytics-tracking** | 事件追踪设置（GA4 等） |
| **ab-test-setup** | 实验设计和增长实验体系 |

---

### 6. 留存与增长工程

| 技能 | 适用场景 |
|------|----------|
| **churn-prevention** | 取消流程、挽回优惠、催缴、支付恢复 |
| **free-tool-strategy** | 营销工具和计算器 |
| **referral-program** | 推荐和联盟计划 |

---

## 安装方法（6 种方式）

### 方式 1：CLI 安装（推荐）

使用 [npx skills](https://github.com/vercel-labs/skills) 直接安装：

```bash
# 安装所有技能
npx skills add coreyhaines31/marketingskills

# 安装特定技能
npx skills add coreyhaines31/marketingskills --skill page-cro copywriting

# 列出可用技能
npx skills add coreyhaines31/marketingskills --list
```

自动安装到 `.agents/skills/` 目录（并创建符号链接到 `.claude/skills/` 以兼容 Claude Code）。

### 方式 2：Claude Code 插件

```bash
# 添加市场
/plugin marketplace add coreyhaines31/marketingskills

# 安装所有营销技能
/plugin install marketing-skills
```

### 方式 3：克隆并复制

```bash
git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/
```

### 方式 4：Git 子模块

```bash
git submodule add https://github.com/coreyhaines31/marketingskills.git .agents/marketingskills
```

然后引用 `.agents/marketingskills/skills/` 中的技能。

### 方式 5：Fork 并自定义

1. Fork 该仓库
2. 根据你的具体需求自定义技能
3. 将 fork 克隆到你的项目中

### 方式 6：SkillKit（多 Agent）

使用 [SkillKit](https://github.com/rohitg00/skillkit) 在多个 AI Agent（Claude Code、Cursor、Copilot 等）间安装技能：

```bash
# 安装所有技能
npx skillkit install coreyhaines31/marketingskills

# 安装特定技能
npx skillkit install coreyhaines31/marketingskills --skill page-cro copywriting
```

---

## 使用方法

安装后，直接让 Agent 帮你完成营销任务：

| 你说 | Agent 使用的技能 |
|------|-----------------|
| "帮我优化这个落地页的转化率" | `page-cro` |
| "为我的 SaaS 写首页文案" | `copywriting` |
| "设置 GA4 注册追踪" | `analytics-tracking` |
| "创建一个 5 封邮件的欢迎序列" | `email-sequence` |

也可以直接调用技能：

```
/page-cro
/email-sequence
/seo-audit
```

---

## 项目统计与活跃度

| 指标 | 数值 |
|------|------|
| ⭐ Stars | 23.4k+ |
| 🍴 Forks | 3.8k |
| 📦 Commits | 249 |
| 🌿 Branches | 29 |
| 🏷️ Tags | 9 |
| 📝 Issues | 5 |
| 🔀 Pull Requests | 8 |
| 📅 最近更新 | 2026-04-22 (v1.8.0) |

---

## 相关资源

### 作者与相关项目

- **Corey Haines**：[corey.co](https://corey.co?ref=marketingskills) - 技能库创建者
- **Conversion Factory**：[conversionfactory.co](https://conversionfactory.co?ref=marketingskills) - Corey 的转化率优化和增长策略机构
- **Swipe Files**：[swipefiles.com](https:// swipefiles.com?ref=marketingskills) - 营销学习资源
- **Magister**：[magistermarketing.com](https://magistermarketing.com?ref=marketingskills) - 使用这些技能的自主 AI CMO Agent
- **Coding for Marketers**：[codingformarketers.com](https://codingformarketers.com?ref=marketingskills) - 营销人员编程指南

### 工具链

- [Agent Skills Spec](https://agentskills.io) - Agent 技能规范
- [npx skills](https://github.com/vercel-labs/skills) - Vercel 的技能安装工具
- [SkillKit](https://github.com/rohitg00/skillkit) - 多 Agent 技能管理工具

---

## 迁移指南：从 v1.0 升级

技能现在使用 `.agents/` 而不是 `.claude/` 存放产品营销上下文文件。迁移现有上下文文件：

```bash
mkdir -p .agents
mv .claude/product-marketing-context.md .agents/product-marketing-context.md
```

技能仍会检查 `.claude/` 作为回退，所以不迁移也不会出错。

---

## 贡献

发现可以改进技能的方法？有新的技能建议？欢迎提交 PR 和 Issue！

详见 [CONTRIBUTING.md](https://github.com/coreyhaines31/marketingskills/blob/main/CONTRIBUTING.md)

---

## 许可证

[MIT](https://github.com/coreyhaines31/marketingskills/blob/main/LICENSE) - 可自由使用

---

## 快速参考：常用技能调用示例

### 转化率优化

```
"分析我的落地页转化率为什么低"
→ 使用 page-cro 技能

"注册流程太长了，怎么简化？"
→ 使用 signup-flow-cro 技能

"用户注册后第二天就流失了"
→ 使用 onboarding-cro 技能
```

### 文案撰写

```
"帮我写个 SaaS 首页标题"
→ 使用 copywriting 技能

"这封冷邮件没人回复，怎么改？"
→ 使用 cold-email 技能

"编辑这篇博客文章"
→ 使用 copy-editing 技能
```

### SEO

```
"为什么我的网站在 Google 排名很低？"
→ 使用 seo-audit 技能

"怎么让我的内容被 AI 搜索引擎引用？"
→ 使用 ai-seo 技能

"怎么大规模创建 SEO 页面？"
→ 使用 programmatic-seo 技能
```

### 增长

```
"给我 10 个营销创意"
→ 使用 marketing-ideas 技能（内置 140 个想法）

"用户流失率太高了"
→ 使用 churn-prevention 技能

"怎么设计一个推荐计划？"
→ 使用 referral-program 技能
```

---

*来自翡冷翠*
