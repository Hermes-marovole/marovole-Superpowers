# Hermes Skill Factory 深度分析

> 来源：https://github.com/Romanescu11/hermes-skill-factory  
> 分析时间：2026-05-01  
> 分析者：翡冷翠  
> 状态：✅ 已下载源码完成分析

---

## 概述

**Skill Factory** 是一个 Meta-Skill（元技能），它通过监听用户与 Hermes Agent 的交互，自动识别可复用的工作流模式，并生成标准化的 SKILL.md 和 plugin.py 文件。

核心理念：**"每个你重复执行的工作流，都是一个等待诞生的技能。"**

---

## 架构分解

### 核心组件

```
Skill Factory
├─── skills/skill-factory/SKILL.md   # 元技能定义（AI 指令）
├─── plugins/skill_factory.py      # 插件实现（命令注册）
├─── templates/SKILL_TEMPLATE.md   # 技能文件模板
└─── install.sh                  # 安装脚本
```

### 工作流程四阶段

```mermaid
随机交互
    ↓
[阶段 1: 无声观察] ──────────────→ 持续记录事件
    ↓
[阶段 2: 触发判断] ──────────────→ 满足条件则提案
    ↓
[阶段 3: 提案格式] ──────────────→ 交互式确认
    ↓
[阶段 4: 生成文件] ──────────────→ 写入 ~/.hermes/
```

---

## 核心机制详解

### 1. 无声观察系统（Silent Observation）

**What to Track（追踪什么）**：
- 重复操作：任何使用超过一次的命令/序列
- 多步骤工作流：3+ 步骤完成一个目标
- 工具组合：多个工具按一致模式使用
- 领域模式：用户解决特定领域问题的方式
- 修复与解决方案：反复出现的调试模式

**What NOT to Track（不追踪什么）**：
- 一次性任务（无复用价值）
- 单一步骤操作（太简单）
- 现有 skill 已处理的工作流
- 高度上下文特定的任务

### 2. 触发条件（Trigger Conditions）

| 触发条件 | 例子 |
|----------|--------|
| 用户明确请求 | "save this as a skill", "remember this" |
| 斜杠命令 | `/skill-factory propose` |
| 重复模式 (2x+) | 同一工作流出现两次 |
| 会话即将结束 | 用户说 "done", "thanks" |
| 用户表达抗议 | "I always have to do this manually..." |

### 3. Skill 生成模板

Skill Factory 使用了标准化的 SKILL.md 模板，包含：

```markdown
---
name: [Skill Name]
category: [category]
description: [one-line]
tags: [tag1, tag2]
generated_by: skill-factory
---

# [Name]

## When to Activate
## Workflow (Phase 1, Phase 2...)
## Quality Checklist
## Examples
## Anti-patterns
## Integration
```

### 4. 插件系统（Plugin.py）

插件提供以下命令：

| 命令 | 功能 |
|------|------|
| `/skill-factory propose` | 立即分析并提案 |
| `/skill-factory list` | 列出本会话生成的 skills |
| `/skill-factory status` | 显示当前追踪状态 |
| `/skill-factory queue` | 显示待处理的提案队列 |
| `/skill-factory save <name>` | 用自定义名保存最后提案 |
| `/skill-factory clear` | 清除当前会话记录 |

---

## 技术实现要点

### 代码结构分析

**SessionTracker 类**（核心状态管理）：

```python
class SessionTracker:
    def __init__(self):
        self.events: list[dict] = []          # 所有记录的事件
        self.generated_skills: list = []      # 本会话生成的 skills
        self.proposal_queue: list = []        # 待提案队列
        self.last_proposal: dict | None       # 最后一个提案
        self.session_start: datetime          # 会话开始时间
```

**Event Hook 系统**（被动监听）：

```python
@hermes.on("tool_call")
async def on_tool_call(ctx, tool_name, tool_args, tool_result):
    # 记录工具调用
    _tracker.record_event("tool_call", {...})

@hermes.on("command")
async def on_command(ctx, command, args):
    # 记录命令执行
    _tracker.record_event("command", {...})
```

---

## 与现有方案对比

### vs 我的 `agent-self-evolution` skill

| 特征 | Hermes Skill Factory | 我的 agent-self-evolution |
|------|---------------------|---------------------------|
| 触发方式 | 自动观察 + 人工确认 | 主要靠人工反馈 |
| 生成内容 | SKILL.md + plugin.py | 仅 SKILL.md |
| 算法位置 | AI 分析认论历史 | 等待用户输入样例 |
| 监控能力 | 实时追踪工具调用 | 无实时追踪 |
| 目标 | 个人工作流 | Agent 自我进化 |

### 关键差异

Skill Factory 的核心优势在于：**AI 主动分析模式**

它不等待用户提供样例，而是 AI 主动：
1. 分析完整会话历史
2. 识别重复工作流
3. 提取可复用步骤
4. 生成标准化 skill 文件

---

## 吸收价值与应用场景

### 立即可用的功能

1. **自动化 Skill 生成**
- 安装后监听每个会话
- 自动提案可复用的工作流
- 减少手动编写 skill 的工作量

2. **标准化模板**
- 学习其 SKILL.md 模板结构
- 应用到自己的 skill 作业
- 特别是 Quality Checklist 和 Anti-patterns 部分

3. **Plugin 系统参考**
- 了解 Hermes 插件架构
- 如何注册命令和工具
- 事件监听机制

### 需要改进的地方

1. **模式识别准确性**
- 当前实现主要靠 AI 推理，缺乏结构化模式匹配
- 可能会误判或遗漏

2. **跨会话持久化**
- SessionTracker 是 in-memory 的
- 重启 Hermes 后丢失历史

3. **用户体验**
- 需要主动触发 `/skill-factory propose` 才能看到建议
- 不是真正的 "无感" 体验

---

## 落地建议

### 方案 A：直接使用

```bash
# 安装 Skill Factory
cd /tmp
git clone https://github.com/Romanescu11/hermes-skill-factory.git
cd hermes-skill-factory
bash install.sh

# 使用
# 在任何会话中输入
/skill-factory propose
```

### 方案 B：吸收其思路到现有流程

修改 `agent-self-evolution` skill，增加：
1. 自动识别重复工作流的逻辑
2. 定期提示用户 "是否保存为 skill"
3. 使用其 SKILL.md 模板作为参考

### 方案 C：整合到 Hermes 框架

如果 Hermes 本地支持 plugin 系统，可直接整合：
- 将 Skill Factory 作为默认 skill 安装
- 启动时自动加载
- 无感监听所有会话

---

## 附录：完整 SKILL.md 参考

Skill Factory 为自己定义的 SKILL.md 是一个完美的元技能示例，它包含：

1. **完整的生命周期**：观察 → 触发 → 提案 → 生成 → 后置处理
2. **清晰的责任边界**：什么该做，什么不该做
3. **交互式式设计**：给用户选择权（A/B/C/D）
4. **质量标准**：生成的 skill 必须满足的条件

建议阅读完整文件：
`/tmp/skill-factory-analysis/skills/skill-factory/SKILL.md`

---

## 结论

Skill Factory 是一个充满创意的 Meta-Skill，它将 AI 作为**观察者**而不仅仅是**执行者**。其核心价值在于：

1. 降低创建 skill 的门槛
2. 提供标准化的模板体系
3. 提供了插件系统的参考实现

但它也有明显的局限：高依赖 AI 推理能力，缺乏结构化的模式识别算法。

**最佳吸收策略**：参考其 SKILL.md 模板和交互设计，但保持现有的 `skill_manage` + `人工反馈` 流程，确保生成质量。

---

*来自翡冷翠*
