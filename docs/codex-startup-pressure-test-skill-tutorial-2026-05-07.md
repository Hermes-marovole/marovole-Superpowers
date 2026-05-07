# Codex Startup Pressure Test Skill：独立开发 Idea 验证利器

> 来源：[Yanhua @yanhua1010](https://x.com/yanhua1010/status/2052038199007186960)  
> 整理时间：2026-05-07  
> 来自翡冷翠

---

## 简介

这是一个专为 Codex 设计的 Skill，用于**残酷地压力测试创业想法**，帮你在浪费时间去构建错误的东西之前，用创始人视角进行诊断。作者 Yanhua 评价这是"今年装到 Codex 里最爽的一个 skill，没有之一"。

**核心定位**：补全独立开发死亡循环中最容易被跳过的一步——**Validation（验证）**。

---

## 独立开发的死亡循环

作者一针见血地指出了独立开发者常陷入的困境：

```
找 idea → 开干 → 没人用 → emo → 重复
```

**核心问题**：99% 的人用"我觉得有用"代替了真正的 validation。

---

## 工具介绍

### 基本信息

| 属性 | 详情 |
|------|------|
| **名称** | codex-startup-pressure-test-skill |
| **作者** | Kappaemme-git |
| **GitHub** | https://github.com/Kappaemme-git/codex-startup-pressure-test-skill |
| **Stars** | 582（不到 1k stars，小但精致） |
| **Forks** | 53 |
| **协议** | MIT |
| **安装命令** | `npx --yes codex-startup-pressure-test-skill@latest` |

### 功能亮点

这个 skill 会以创始人视角对 idea 进行全面压测，覆盖以下 6 个维度：

| 验证维度 | 核心问题 |
|----------|----------|
| ✅ **核心假设** | 你的基础假设是什么？ |
| ✅ **致命缺陷** | 这个想法有什么致命问题？ |
| ✅ **真实痛点** | 这是真需求还是你的幻觉？ |
| ✅ **竞品分析** | 真实竞品是谁？切换成本多高？ |
| ✅ **获客路径** | 前 10 个客户从哪来？ |
| ✅ **MVP 规划** | 2 周内能跑完的最小可行产品是什么？ |

**最终输出**：直接判定 **strong / weak / pivot**（值得做 / 有风险 / 需要转向）

---

## 安装与使用

### 一键安装

```bash
npx --yes codex-startup-pressure-test-skill@latest
```

安装路径：`~/.codex/skills/startup-pressure-test`

**注意**：安装后需要**重启 Codex** 才能识别 skill。

### 基础用法

安装完成后，在 Codex 中使用 `$startup-pressure-test` 触发：

#### 1. 基础压力测试

```
Use $startup-pressure-test to pressure-test this startup idea:

A tool that turns local videos into short clips with local captions for indie hackers and creators posting product demos.
```

#### 2. 残酷模式（更直接）

```
Use $startup-pressure-test to brutally test this startup idea:

...
```

#### 3. 问题验证

```
Use $startup-pressure-test to validate whether this idea solves a real problem people pay for:

...
```

#### 4. 竞品分析

```
Use $startup-pressure-test to map the real competition for this idea:

...
```

#### 5. 获取前 10 个客户

```
Use $startup-pressure-test to find the first 10 customers for this idea:

...
```

#### 6. MVP 规划

```
Use $startup-pressure-test to build a 2-week MVP plan for this idea:

...
```

#### 7. 深度报告

```
Use $startup-pressure-test to do a deep full report on this startup idea:

...
```

### 交互模式

如果直接调用 skill 而不提供 idea，它会主动询问：
- 创业想法是什么？
- 目标客户是谁？
- 客户应该做什么或付什么？

### 多种工作模式

| 模式 | 功能 | 输出重点 |
|------|------|----------|
| `pressure-test` | 基础压测 | 核心假设、致命缺陷、直接判定 |
| `problem-validation` | 问题验证 | 真实痛点、早期采用者、验证标准 |
| `competition-map` | 竞品分析 | 当前行为、直接/间接竞品、切换成本 |
| `first-10-customers` | 获客规划 | 手动获客执行计划 |
| `mvp-plan` | MVP 规划 | 最小 2 周测试方案 |
| `full` | 完整诊断 | 一体化紧凑报告 |

### 输出格式

默认输出为紧凑格式，包含：
- **Verdict**（判定：strong/weak/pivot）
- **Scorecard**（评分卡）
- **Core Assumption**（核心假设）
- **Fatal Flaws**（致命缺陷）
- **Problem Reality**（问题真实性）
- **Competition**（竞争格局）
- **First 10 Customers**（前 10 个客户）
- **MVP**（最小可行产品）

---

## 工作流整合：Reddtrends + 本 Skill + Codex

作者 Yanhua 分享了一个完整的独立开发工作流闭环：

```
Reddtrends 挖掘 Reddit 真实痛点 
    ↓
本 Skill 验证 idea 可行性
    ↓
Codex 写代码落地
```

**第一次实现三段全闭环**：idea → 验证 → 落地

### 工具分工

| 工具 | 解决什么问题 | 对应阶段 |
|------|-------------|----------|
| **Reddtrends** | 发现真实痛点 | 需求挖掘 |
| **本 Skill** | 验证 idea 可行性 | 决策判断 |
| **Codex / Claude Code / Cursor** | 怎么 build | 执行落地 |

**关键洞察**：90% 的独立开发者死在"build 什么"，而不是"怎么 build"。

---

## 手动安装（可选）

如果无法使用 npx，可以手动安装：

```bash
# 克隆仓库
git clone https://github.com/Kappaemme-git/codex-startup-pressure-test-skill.git

# 复制 skill 到 Codex 目录
mkdir -p ~/.codex/skills
cp -R codex-startup-pressure-test-skill/startup-pressure-test ~/.codex/skills/startup-pressure-test

# 重启 Codex
```

验证安装：
```bash
ls ~/.codex/skills/startup-pressure-test
# 应看到：SKILL.md, agents/, references/
```

---

## 故障排查

| 问题 | 解决方案 |
|------|----------|
| Codex 不识别 `$startup-pressure-test` | 重启 Codex |
| 找不到 skill 目录 | 检查 `~/.codex/skills/startup-pressure-test` 是否存在 |

---

## 核心洞察

> "这是我今年装到 Codex 里最爽的一个 skill，没有之一，强烈推荐大家安装一下。"

> "一个不到 1k stars 的小项目，把独立开发最容易死的那一环给补上了。"

> "中间被跳过的很重要的一步叫 validation，99% 的人靠'我觉得有用'代替了它。"

> "Cursor 和 Claude Code 解决'怎么 build'的问题，Reddtrends + 这个 skill 解决'build 什么'。后者才是 90% 独立开发者真正死掉的地方。"

---

## 资源汇总

### 相关链接
| 名称 | 链接 | 说明 |
|------|------|------|
| codex-startup-pressure-test-skill | https://github.com/Kappaemme-git/codex-startup-pressure-test-skill | GitHub 仓库 |
| 原帖 | https://x.com/yanhua1010/status/2052038199007186960 | Yanhua 的 X 帖子 |

### 涉及工具/技术
- **Codex** - OpenAI 的 AI Coding Agent
- **Claude Code** - Anthropic 的 AI Coding Agent
- **Cursor** - AI 驱动的代码编辑器
- **Reddtrends** - Reddit 痛点挖掘工具（作者私有）

### 值得关注
- **@yanhua1010** (Yanhua) - AI Solopreneur | 独立开发 Reddtrends，分享 AI 创业、出海 SaaS、独立开发的真实路径
- **Kappaemme-git** - codex-startup-pressure-test-skill 原作者

---

## 快速参考

### 安装命令
```bash
npx --yes codex-startup-pressure-test-skill@latest
```

### 基础调用模板
```
Use $startup-pressure-test to pressure-test this startup idea:

[你的 idea 描述]
```

### 完整工作流
1. 用 Reddtrends 或其他方式发现潜在痛点
2. 用本 Skill 验证 idea 可行性
3. 根据判定结果（strong/weak/pivot）做决策
4. 用 Codex/Cursor/Claude Code 落地开发

---

*来自翡冷翠*
