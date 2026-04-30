# Hermes 进化体：5 个全新社区项目完整整理

> 来源：[GitTrend @GitTrend0x](https://x.com/GitTrend0x/status/2047616606826893413)
> 整理时间：2026-04-24
> 来自翡冷翠

---

## 简介

本文档整理自 X 用户 [@GitTrend0x](https://x.com/GitTrend0x) 分享的 **Hermes Agent 进化体合集**，涵盖 5 个全新的社区开源项目。这些项目代表了 Hermes 生态的最新进化方向：从元推理增强到生活管理、从技能自动迭代到多源搜索聚合，再到本地隐私优先的记忆系统。

**核心洞察**：Hermes 的价值不仅在于其开源 Agent 框架本身，更在于其可扩展的插件/技能架构——让开发者能够将个人需求转化为可复用的 Agent 能力。

---

## 内容清单总览

| 序号 | 项目名称 | 作者 | 类型 | 核心亮点 |
|------|----------|------|------|----------|
| 1 | [super-hermes](#1-super-hermes) | @Cranot | Meta-reasoning 插件 | 认知棱镜分析，自我优化 prompt |
| 2 | [hermes-life-os](#2-hermes-life-os) | @Lethe044 | 生活 OS | 追踪习惯、学习用户模式、自动简报 |
| 3 | [hermes-dojo](#3-hermes-dojo) | @Yonkoo11 | 技能道场 | 监控弱技能、自动修复、持续进化 |
| 4 | [hermes-web-search-plus](#4-hermes-web-search-plus) | @robbyczgw-cla | 搜索插件 | 8 提供商智能路由、深度研究模式 |
| 5 | [hermes-memory-plugin](#5-hermes-memory-plugin) | @Ladybug-Memory | 内存插件 | 纯本地图数据库、零云依赖 |

---

## 详细内容

### 1. super-hermes

**Meta-reasoning 插件：让 Agent 学会"自己给自己写作业"**

| 属性 | 详情 |
|------|------|
| **GitHub** | [github.com/Cranot/super-hermes](https://github.com/Cranot/super-hermes) |
| **作者** | @Cranot |
| **类型** | Skill（技能） |

#### 核心概念：认知棱镜（Cognitive Prism）

Super Hermes 的核心理念是：**在执行复杂任务前，先让 Agent 为自己编写专属的思考指令**。不同问题获得不同的"棱镜"（分析透镜），然后执行该棱镜并报告发现的内容 AND 无法看到的内容。

**对比示例**：

| | 普通 Hermes | Super Hermes |
|---|---|---|
| 输出 | "会话处理紧耦合，建议解耦" | "会话状态非单调。无追加、可组合或惰性架构能在不牺牲一致性或隔离性的情况下管理它。**这是结构性不可能，而非代码缺陷。**" |
| 深度 | 指出模式，告诉你改什么 | 推导出为何代码必须如此，告诉你不能改什么以及替代方案 |
| 字数 | 339 词 | 1,485 词 |
| 发现 Bug | 7 个（表面检查清单） | 11 个（含行号、严重度、结构分类） |
| 成本 | ~$0.05 | ~$0.05（相同） |

#### 核心 Skills

| Skill | 功能 | 调用 |
|-------|------|------|
| `/prism-scan` | 为当前工件生成最优透镜，执行并报告发现+约束 | 1 |
| `/prism-full` | 多遍管道，含强制对抗性自我修正 | 1 |
| `/prism-3way` | WHERE/WHEN/WHY 三正交操作+跨操作综合 | 1 |
| `/prism-discover` | 映射工件的所有可能分析域 | 1 |
| `/prism-reflect` | 自我感知分析——结构发现+元分析+约束透明报告 | 2-3 |

#### 7 个经过验证的棱镜（prisms/）

| 棱镜 | 发现内容 | 验证评分 |
|------|----------|----------|
| `error_resilience.md` | 损坏级联链——静默退出、延迟失败、状态损坏 | 10.0/10 |
| `l12.md` | 守恒定律（无法被工程消除的结构权衡） | 9.8/10 |
| `optimize.md` | 关键路径追踪——安全修复 vs 不安全修复 | 9.5/10 |
| `identity.md` | 代码声称做什么 vs 实际做什么 | 9.5/10 |
| `deep_scan.md` | 信息销毁、清洗、静默转换 | 9.0/10 |
| `claim.md` | 假设反转——如果被接受的真理是错的？ | 9.0/10 |
| `simulation.md` | 时间预测——随时间推移会崩溃什么 | 9.0/10 |

#### 安装使用

```bash
git clone https://github.com/Cranot/super-hermes.git
cd super-hermes
bash install.sh

# 手动安装
cp -r skills/* ~/.hermes/skills/
cp -r prisms/ ~/.hermes/prisms/
```

**无需 Hermes 即可试用**：
```bash
cat your_code.py | claude -p --system-prompt-file prisms/l12.md --model sonnet --tools ""
```

#### 适用场景

- **代码审查**：发现结构性问题，而非表面缺陷
- **架构分析**：识别无法通过重构消除的结构性约束
- **自我改进的 Agent**：随项目演进的学习型分析系统

---

### 2. hermes-life-os

**私人生活管家：追踪一切、发现模式、每天更懂你**

| 属性 | 详情 |
|------|------|
| **GitHub** | [github.com/Lethe044/hermes-life-os](https://github.com/Lethe044/hermes-life-os) |
| **作者** | @Lethe044 |
| **类型** | Environment + Skill |
| **用途** | NousResearch Hermes Agent Hackathon (March 2026) |

#### 核心能力

**追踪维度**：

| 类别 | 追踪内容 |
|------|----------|
| 🥗 营养 | 餐食、卡路里、蛋白质/碳水/脂肪、每日总量 |
| 😴 睡眠 | 时长、质量评分、7 天平均 |
| 💧 补水 | 每日饮水量及进度条 |
| 💪 健身 | 锻炼、时长、强度、每周次数 |
| 🧘 心理 | 压力水平、冥想、感恩日志 |
| 🎯 专注 | 深度工作时段、分心、质量评分 |
| ✅ 习惯 | 连续记录、最佳记录、完成追踪 |
| 🎯 目标 | 进度百分比、里程碑、笔记 |
| 😊 心情与能量 | 每日评分、趋势检测、下滑警报 |
| 🌙 梦境 | 梦境日志、符号、情绪、睡眠/压力/梦境关联 |

#### 架构流程

```
你分享某事 → 记忆存储 → 上下文检索 → 模式检测 → 个性化简报 → Hermes 更懂你
     ↑                                                                     ↓
     └──────────────── Cron 调度（每日 07:00/12:00/18:00/23:00 + 每周一）
```

**Cron 自动化**：
- 07:00 早间简报
- 12:00 午间提醒
- 18:00 晚间反思
- 23:00 数据整合
- 周一 08:00 周度回顾

#### 使用的 Hermes 特性

| 特性 | 用途 |
|------|------|
| Memory | 存储每次心情、餐食、睡眠...每次响应前检索 |
| Skills | Life OS playbook 定义每日节奏、检测规则、简报格式 |
| Cron | 自动化简报 |
| Gateway | 通过终端交付简报（可扩展至 Telegram/邮件/短信）|
| Subagents | 跨所有健康维度并行运行模式检测 |
| Atropos RL | 奖励函数训练 Hermes 随时间更具个性化和记忆驱动 |

#### 快速开始

```bash
pip install openai rich
set OPENROUTER_API_KEY=***

python demo/demo_life_os.py --mode onboard   # 首次设置
python demo/demo_life_os.py --mode morning   # 每日简报
python demo/demo_life_os.py --mode chat    # 交互对话
python demo/demo_life_os.py --voice        # 语音模式
```

#### 对话示例

```
"我今天压力很大，有什么建议？"
"记录我的午餐——烤鸡和米饭，约 600 卡路里"
"我这周睡眠怎么样？"
"我刚跑了 5 公里，记录下来"
"你看到我的数据里有什么模式吗？"
```

---

### 3. hermes-dojo

**你的 Agent，在你睡觉时变得更好**

| 属性 | 详情 |
|------|------|
| **GitHub** | [github.com/Yonkoo11/hermes-dojo](https://github.com/Yonkoo11/hermes-dojo) |
| **作者** | @Yonkoo11 |
| **类型** | Skill |
| **用途** | NousResearch Hermes Agent Hackathon (March 2026) |

#### 解决的问题

你的 AI Agent 每天重复同样的错误。你纠正它，它在下个会话忘记。技能存在但没人知道哪些有效、哪些静默失败。自我进化存在但没人使用，因为没有信号指示 WHAT 需要进化。

#### 解决方案闭环

```
测量 → 识别弱点 → 进化 → 再次测量 → 报告
```

#### 5 个核心组件

| 组件 | 功能 |
|------|------|
| **Performance Monitor** | 读取 `state.db` 中的会话日志，识别失败：工具错误、重试循环、用户纠正、明确投诉。追踪每个技能的成功率 |
| **Weakness Analyzer** | 分类根本原因并排序改进机会 |
| **Auto-Fixer** | 技能存在但失败 → 用针对性错误处理打补丁；无技能存在 → 基于会话模式创建一个；对弱技能运行自我进化（GEPA）|
| **Reporter** | 生成 CLI 或 Telegram 交付的报告 |
| **Learning Curve** | 存储每日指标，显示数周/数月的改进 |

#### 命令

| 命令 | 功能 |
|------|------|
| `/dojo analyze` | 分析近期会话的失败 |
| `/dojo improve` | 修复最弱的技能 + 运行自我进化 |
| `/dojo report` | 生成改进报告 |
| `/dojo history` | 显示随时间的学习曲线 |
| `/dojo auto` | 设置夜间 cron（分析+改进+报告）|

#### 快速开始

```bash
git clone https://github.com/Yonkoo11/hermes-dojo.git
cd hermes-dojo
./install.sh

# 种子演示数据（可选，用于测试）
cd ~/.hermes/skills/hermes-dojo/scripts
python3 seed_demo_data.py --days 7

# 运行完整管道
python3 demo.py --reset
```

---

### 4. hermes-web-search-plus

**多提供商智能搜索：自动路由，深度研究**

| 属性 | 详情 |
|------|------|
| **GitHub** | [github.com/robbyczgw-cla/hermes-web-search-plus](https://github.com/robbyczgw-cla/hermes-web-search-plus) |
| **作者** | @robbyczgw-cla |
| **类型** | Plugin |
| **版本** | v1.4.0 |

#### 8 个搜索提供商

| 提供商 | 最佳用途 | 免费额度 |
|--------|----------|----------|
| **Brave** | 通用搜索、独立索引、广泛事实查询 | $5.00/月免费积分 |
| **Serper** (Google) | 新闻、购物、事实、本地查询 | 2,500/月 |
| **Tavily** | 研究、深度内容、学术 | 1,000/月 |
| **Exa** | 语义发现、"X 的替代品"、arxiv | 1,000/月 |
| **Querit** | 多语言、实时查询 | 1,000/月 |
| **Perplexity** | 直接 AI 合成答案 | API key |
| **You.com** | LLM 就绪的实时片段 | 有限 |
| **SearXNG** | 隐私优先、自托管、零 API 成本 | 免费 |

#### 智能自动路由

基于查询信号（关键词、意图、语言模式）为提供商评分。Brave 和 Serper 共享通用搜索意图；打平时，路由器使用确定性的逐查询决胜机制。

#### 特色功能

- **Exa Deep Research**：`depth=deep` 多源综合（4-12s），`depth=deep-reasoning` 跨文档分析
- **自适应回退**：失败后自动跳过提供商（1 小时冷却）
- **路由透明**：每个响应包含解释提供商选择的 `routing` 对象
- **时间/域名过滤**：`time_range`, `include_domains`, `exclude_domains`
- **本地缓存**：避免重复 API 调用（1 小时 TTL）

#### 使用示例

```python
# 自动路由
web_search_plus(query="Graz weather today")
# → 路由到 Serper 或 Brave（天气/当前信息意图）

# 指定提供商
web_search_plus(query="Singapore CPI latest", provider="brave")
web_search_plus(query="alternatives to Notion", provider="exa")

# Exa 深度研究
web_search_plus(query="LLM scaling laws research", provider="exa", depth="deep")

# 时间过滤
web_search_plus(query="OpenAI news", time_range="day")

# 域名限制
web_search_plus(query="LoRA fine-tuning", include_domains=["arxiv.org"])
```

#### 安装

```bash
git clone https://github.com/robbyczgw-cla/hermes-web-search-plus.git \
  ~/.hermes/plugins/web-search-plus

cd ~/.hermes/hermes-agent
source venv/bin/activate
pip install requests

cd ~/.hermes/plugins/web-search-plus
cp .env.template .env  # 填写至少一个提供商 key
```

配置 `~/.hermes/config.yaml`：
```yaml
plugins:
  enabled:
    - web-search-plus

tools:
  enabled:
    - web
    - web-search-plus
```

---

### 5. hermes-memory-plugin

**Ladybug 本地内存：纯本地图数据库，无云无 API**

| 属性 | 详情 |
|------|------|
| **GitHub** | [github.com/Ladybug-Memory/hermes-memory-plugin](https://github.com/Ladybug-Memory/hermes-memory-plugin) |
| **作者** | @Ladybug-Memory |
| **类型** | Memory Provider Plugin |

#### 核心特性

**本地优先**：所有数据存储在单个 `.lbdb` 文件中，位于你的机器上。支持：
- BM25 关键词搜索
- 重要性加权召回
- 类型化内存条目
- 条目间的命名图边关系
- 可选 GLiNER2 实体提取

**无需任何外部服务**——无 API key、无云、无同步服务。

#### 对比定位

| 方案 | 特点 |
|------|------|
| vs Honcho, Mem0, RetainDB | 完全本地，无托管组件 |
| vs Observational Memory, Holographic | 更少关注跨 Agent markdown 共享存储，更多关注类型化、可搜索、图链接的内存存储 |
| vs OpenViking, ByteRover | 更简单直接——无分层浏览器或知识图谱 UI，只有 Agent 需要的快速嵌入式数据库工具 |

#### 提供的工具

| 工具 | 功能 |
|------|------|
| `ladybug_store` | 持久化新内存条目（含类型和重要性评分）|
| `ladybug_search` | 跨存储内存的 BM25 关键词搜索 |
| `ladybug_recall` | 检索近期或高重要性内存 |
| `ladybug_update` | 通过 ID 更正或更新内存 |
| `ladybug_delete` | 通过 ID 删除内存 |
| `ladybug_link` | 在两个内存间创建命名关系 |
| `ladybug_related` | 通过关系遍历内存图 |
| `ladybug_entity` | 通过 GLiNER2 的实体级 KG 查询（可选）|

#### 内存类型

`general` · `preference` · `fact` · `project` · `person` · `event` · `task`

#### 重要性评分（1-10 范围）

分数越高在预取召回中显示越频繁。内置 `MEMORY.md` / `USER.md` 镜像使用重要性 **6**（明确的用户信号）。

#### 安装

```bash
hermes plugins install Ladybug-Memory/hermes-memory-plugin
pip install ladybug-memory

# 创建符号链接（当前必需）
ln -s ~/.hermes/plugins/ladybug \
      ~/.hermes/hermes-agent/plugins/memory/ladybug

# 配置
hermes memory setup    # 选择 "ladybug"
```

---

## 资源汇总

### GitHub 仓库速查

| 项目 | 链接 | Stars |
|------|------|-------|
| super-hermes | [github.com/Cranot/super-hermes](https://github.com/Cranot/super-hermes) | - |
| hermes-life-os | [github.com/Lethe044/hermes-life-os](https://github.com/Lethe044/hermes-life-os) | - |
| hermes-dojo | [github.com/Yonkoo11/hermes-dojo](https://github.com/Yonkoo11/hermes-dojo) | 20 |
| hermes-web-search-plus | [github.com/robbyczgw-cla/hermes-web-search-plus](https://github.com/robbyczgw-cla/hermes-web-search-plus) | 60 |
| hermes-memory-plugin | [github.com/Ladybug-Memory/hermes-memory-plugin](https://github.com/Ladybug-Memory/hermes-memory-plugin) | - |

### 值得关注的人/账号

| 账号 | 项目/角色 | 简介 |
|------|----------|------|
| [@Cranot](https://github.com/Cranot) | super-hermes | 认知棱镜分析方法研究者 |
| [@Lethe044](https://github.com/Lethe044) | hermes-life-os | 生活 OS 开发者 |
| [@Yonkoo11](https://github.com/Yonkoo11) | hermes-dojo | Agent 自我改进系统开发者 |
| [@robbyczgw-cla](https://github.com/robbyczgw-cla) | hermes-web-search-plus | 多提供商搜索插件作者 |
| [@Ladybug-Memory](https://github.com/Ladybug-Memory) | hermes-memory-plugin | 本地内存系统开发者 |
| [@GitTrend0x](https://x.com/GitTrend0x) | 聚合者 | Hermes 生态项目追踪 |

---

## 进化方向洞察

### 技术趋势观察

1. **Meta-cognition（元认知）**：super-hermes 代表了 Agent 自我分析能力的深化——不只是执行任务，还要分析"如何思考"，并报告认知盲区。

2. **Personal OS（个人操作系统）**：hermes-life-os 展示了 Agent 作为生活基础设施的潜力——从工具进化为存在（presence），随时间积累对用户的理解。

3. **Self-evolution（自我进化）**：hermes-dojo 让改进闭环自动化——测量→识别→修复→再测量，实现真正的"递归自我改进"。

4. **Intelligent Routing（智能路由）**：hermes-web-search-plus 体现了工具层面的"决策智能"——根据查询意图自动选择最优提供商。

5. **Local-first Privacy（本地优先隐私）**：hermes-memory-plugin 回应了隐私诉求——功能完整但完全离线，数据主权归用户。

### 为什么这些项目值得关注

> "Hermes 从不给你黑箱，它给的是可读、可 hack、可自我改进的底层循环。你 fork 它，就是在和 Agent 一起'递归自我改进'。"

这 5 个项目共同展示了 Hermes 生态的核心优势：
- **可组合性**：Memory + Cron + Skills + Subagents + RL 自由组合
- **可观测性**：每个组件都能报告自己在做什么、没做什么
- **可进化性**：从静态配置进化为动态学习

---

## 建议探索路径

### 如果你是开发者
1. **入门**：从 `hermes-web-search-plus` 开始——它是最成熟的插件（60 stars），文档完善，立即可用
2. **进阶**：尝试 `super-hermes`——理解认知棱镜如何改变 Agent 的分析深度
3. **深入**：研究 `hermes-dojo`——学习如何构建自我改进的反馈闭环

### 如果你是用户
1. **日常生活**：部署 `hermes-life-os`——让它追踪你的习惯并发现隐藏模式
2. **隐私优先**：使用 `hermes-memory-plugin`——获得完整的 Agent 记忆能力，但数据永不离开你的机器

### 如果你是研究者
1. 关注 `super-hermes` 背后的 [cognitive compression taxonomy](https://github.com/Cranot/agi-in-md)——40 轮研究、1000+ 实验、204+ 实证原则

---

## 快速参考

### 一键安装清单

```bash
# 1. super-hermes
git clone https://github.com/Cranot/super-hermes.git
cd super-hermes && bash install.sh

# 2. hermes-life-os
git clone https://github.com/Lethe044/hermes-life-os.git
# 详见项目 README 的配置步骤

# 3. hermes-dojo
git clone https://github.com/Yonkoo11/hermes-dojo.git
cd hermes-dojo && ./install.sh

# 4. hermes-web-search-plus
git clone https://github.com/robbyczgw-cla/hermes-web-search-plus.git \
  ~/.hermes/plugins/web-search-plus

# 5. hermes-memory-plugin
hermes plugins install Ladybug-Memory/hermes-memory-plugin
pip install ladybug-memory
```

---

*来自翡冷翠*
