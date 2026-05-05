# CLAUDE.md：Karpathy 编码四条铁律 —— 一个文件让 LLM 编码质量起飞

> 来源：[阿绎 AYi @AYi_AInotes](https://x.com/AYi_AInotes/status/2051321729843069037)  
> 仓库：[forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)  
> 整理时间：2026-05-05  
> 来自翡冷翠

---

## 简介

一个 **100 行的 CLAUDE.md 文件**，一周内 GitHub Trending 第一，暴涨 **4.4 万星**，目前已破 **11 万星**！🔥

这个文件将 Andrej Karpathy（前 OpenAI 创始成员、Tesla AI 总监）反复吐槽的 LLM 编码坏习惯，浓缩成 **4 条铁律**。无需框架、无需依赖、零配置 —— 扔到项目根目录，Claude Code 启动自动读取，代码质量直接起飞。

**核心价值**：
- 以前你要写几百字长 prompt 反复纠正它
- 现在一次配置，全项目终身生效
- 再也不会让它加个输入框，顺便重写整个表单
- 再也不会让它改个 bug，悄悄删掉三行关键注释
- 再也不会让它写个工具函数，给你搞出五层抽象 + 十个配置

---

## 为什么这个仓库如此火爆？

> "全世界的开发者都受够了。受够了哄模型、受够了反复说'别过度设计'、受够了它自作主张改代码。"

这个仓库的爆火，本质是一场**集体反叛** —— 我们不再指望模型自己变聪明，我们直接给它定规矩。

**最狠的是它的杠杆效应**：
- 成本为零
- diff 更干净
- 返工更少
- token 浪费直接砍掉一半
- 还能把团队规范直接追加在后面，实现全局统一

**这才是 AI 时代真正的生产力** —— 不是越来越复杂的 Agent 框架，而是用最简单的方式，解决最痛的问题。

---

## 四条铁律详解

### 1. Think Before Coding（先思考再编码）

**核心原则**：不准默默做假设，模糊就提问，困惑立刻停下

**具体规则**：
- **明确陈述假设** —— 如果不确定，直接询问而不是猜测
- **呈现多种解释** —— 当存在歧义时，列出多种可能，不要默默选择
- **必要时反驳** —— 如果存在更简单的方案，说出来；该拒绝时拒绝
- **困惑时停下** —— 说出哪里不清楚，主动提问澄清

**解决的问题**：模型常常默默选择一个解释并继续，这个原则强制它显式推理

---

### 2. Simplicity First（简约至上）

**核心原则**：只写最小可工作代码，不准搞没人要的抽象和灵活性

**具体规则**：
- 不添加超出需求的额外功能
- 单次使用的代码不创建抽象
- 不添加未被请求的"灵活性"或"可配置性"
- 不处理不可能场景的错误处理
- 如果写了 200 行代码而实际上 50 行就够，重写它

**自检问题**："资深工程师会说这段代码过于复杂吗？" 如果答案是肯定的，简化它。

**解决的问题**：对抗过度工程化的倾向 —— 1000 行的臃肿代码 vs 100 行的简洁方案

---

### 3. Surgical Changes（手术式修改）

**核心原则**：只碰你要求的部分，不准顺便重构邻居代码

**具体规则**：
- 不"改进"相邻的代码、注释或格式
- 不重构没坏的东西
- 匹配现有风格，即使你自己会做得不一样
- 如果注意到无关的死代码，提一下 —— 但不要删除它
- 移除**你的修改**造成的未使用导入/变量/函数
- 不删除预先存在的死代码，除非被明确要求

**检验标准**：每一行变更都应该能直接追溯到用户的请求。

**解决的问题**：模型有时会改变/删除它不够理解的注释和代码作为副作用，即使与任务正交

---

### 4. Goal-Driven Execution（目标驱动执行）

**核心原则**：先写成功标准，每一步都要可验证

**转换示例**：

| 不要说... | 改为... |
|-----------|---------|
| "添加验证" | "为无效输入编写测试，然后让它们通过" |
| "修复这个 bug" | "编写一个能复现它的测试，然后让它通过" |
| "重构 X" | "确保测试在重构前后都能通过" |

**多步骤任务模板**：
```
1. [步骤] → verify: [检查点]
2. [步骤] → verify: [检查点]
3. [步骤] → verify: [检查点]
```

**核心理念**：
> "LLMs 在循环直到达成具体目标方面表现得非常出色...不要告诉它该做什么，给它成功标准然后看着它执行。"

**解决的问题**：弱标准（"让它工作"）需要不断澄清；强标准让 LLM 能够独立循环

---

## CLAUDE.md 完整文件内容

```markdown
# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
```

---

## 使用方法

### 方案 A：Claude Code 插件（推荐）

在 Claude Code 中执行：

```bash
# 添加插件市场
/plugin marketplace add forrestchang/andrej-karpathy-skills

# 安装插件
/plugin install andrej-karpathy-skills@karpathy-skills
```

这种方式将准则安装为 Claude Code 插件，可在**所有项目**中使用。

### 方案 B：CLAUDE.md（按项目）

**新项目**：
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

**已有项目（追加）**：
```bash
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

将 CLAUDE.md 放在项目根目录，Claude Code 启动时会**自动读取**。

---

## Cursor 支持

此仓库包含 Cursor 项目规则（`.cursor/rules/karpathy-guidelines.mdc`），在 Cursor 中打开项目时同样适用。

详见：[CURSOR.md](https://github.com/forrestchang/andrej-karpathy-skills/blob/main/CURSOR.md)

---

## 自定义扩展

这些准则设计为可与项目特定指令合并。例如：

```markdown
## Project-Specific Guidelines

- 使用 TypeScript strict 模式
- 所有 API 端点必须有测试
- 遵循 `src/utils/errors.ts` 中现有的错误处理模式
```

---

## 如何验证它在工作

这些准则正在发挥作用的表现：

- ✅ **diff 中更少的不必要变更** —— 只出现被请求的更改
- ✅ **更少因过度复杂而需要的重写** —— 代码第一次就简洁
- ✅ **澄清问题在实施前出现** —— 而不是出错后才问
- ✅ **干净、最小的 PR** —— 没有顺手的重构或"改进"

---

## 取舍说明

这些准则偏向**谨慎而非速度**。对于琐碎任务（简单的拼写修复、明显的一行代码），使用判断 —— 并非每次更改都需要完整严谨。

目标是减少非平凡工作上的昂贵错误，而不是拖慢简单任务。

---

## Andrej Karpathy 的原始观察

> "模型会代表你做出错误假设并继续执行而不检查。它们不管理困惑，不寻求澄清，不呈现不一致性，不展示取舍，该反驳时不反驳。"

> "它们真的很喜欢把代码和 API 搞得过于复杂，膨胀抽象，不清理死代码... 实现一个臃肿的 1000 行构造，而实际上 100 行就够了。"

> "它们仍然有时会改变/删除它们不够理解的注释和代码作为副作用，即使与任务正交。"

---

## 资源汇总

| 资源 | 链接 | 说明 |
|------|------|------|
| 主仓库 | https://github.com/forrestchang/andrej-karpathy-skills | 11万+ Stars |
| CLAUDE.md 原始文件 | https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md | 可直接下载 |
| 中文 README | https://github.com/forrestchang/andrej-karpathy-skills/blob/main/README.zh.md | 官方中文文档 |
| 示例文档 | https://github.com/forrestchang/andrej-karpathy-skills/blob/main/EXAMPLES.md | 编码原则实例 |
| 作者 X | [@jiayuan_jy](https://x.com/jiayuan_jy) | 仓库作者 |
| 推荐者 X | [@AYi_AInotes](https://x.com/AYi_AInotes) | 原帖作者 |

### 相关项目
- **[Multica](https://github.com/multica-ai/multica)** — 开源平台，用于运行和管理带有可复用技能的编码 Agent

---

## 快速上手

→ **最快开始**：直接下载 CLAUDE.md 到项目根目录  
→ **最全面**：使用 Claude Code 插件方式，全局生效  
→ **多 IDE 支持**：同时支持 Claude Code 和 Cursor

---

*来自翡冷翠*
