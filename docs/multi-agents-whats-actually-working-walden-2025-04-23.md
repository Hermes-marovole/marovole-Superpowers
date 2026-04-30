# Multi-Agents: What's Actually Working

> 来源：https://x.com/walden_yan/status/2047054401341370639  
> 作者：Walden Yan (Cognition AI)  
> 原文：https://cognition.ai/blog/dont-build-multi-agents  
> 整理时间：2025-04-23  
> 来自翡冷翠

---

## 简介

本文档整理了 Walden Yan（Cognition AI 工程师，Devin 的创造者）关于**多代理系统（Multi-Agent Systems）**的最新思考。10个月前，他写了《Don't Build Multi-Agents》反对构建多代理系统；现在，他更新了观点：发现了**真正有效的多代理模式**。

核心洞察：**从 "Prompt Engineering" 转向 "Context Engineering"，找到多代理系统的正确打开方式。**

---

## 核心观点演变

### 10个月前的立场：Don't Build Multi-Agents

Walden 当时的担忧：
- 并行代理会做出关于风格、边界情况、代码模式的隐式选择
- 这些决策往往相互冲突，导致脆弱的产品
- 多代理架构看似诱人，但非常脆弱

### 现在的更新：What's Actually Working

经过 10 个月的实践，Cognition 发现了一类**确实有效的多代理模式**：

> **多个代理为任务贡献智能，但写入操作保持单线程（single-threaded）。**

这意味着：
- ✅ 可以有多代理参与思考和分析
- ❌ 但不能有多代理并行写入/修改代码

---

## 关键概念：Context Engineering（上下文工程）

### 从 Prompt Engineering 到 Context Engineering

| Prompt Engineering | Context Engineering |
|---------------------|---------------------|
| 关注如何写好提示词 | 关注如何给模型正确的上下文 |
| 技巧如 "你是一个资深工程师" | 动态系统中自动完成 |
| 假设模型能力固定 | 假设模型会变得越来越强 |

> **Context Engineering 是构建 AI 代理的工程师的第一要务。**

### 为什么 Context Engineering 在多代理中更难？

**原则 1：尽可能共享上下文**
- 确保代理看到相同的信息源
- 保持在同一页面（todo list、plan files）
- 共享对整体任务的相同先验知识
- 帮助它们必要时进行沟通

**原则 2：操作携带隐式决策**
- 当一个代理做出某些更改或编辑时，它可能做出隐式选择（风格、代码模式、边界情况处理方式）
- 这些隐式选择可能与其他并行代理的隐式选择冲突
- 导致决策在多代理世界中变得分散

---

## 过去 10 个月发生了什么变化？

### 变化 1：模型变得更自然 "Agentic"

现在的模型：
- 直观理解工具使用
- 了解自己的上下文限制
- 知道如何为协作者（人类或其他）提炼上下文

### 变化 2：Agent 使用量爆炸式增长

Cognition 的数据：
- 即使是最大的企业客户（传统上对新技术的采用较为谨慎）
- 过去 6 个月 Devin 使用量增长了 **~8 倍**

### 变化 3：推拉效应催生多代理

**推力（Push）：**
- 能力增强 → 用户自然实验更多多代理设置
- 代理使用量大 → 瓶颈出现在代理周围的一切：管理、规划、审查
- 示例：用 Devin 管理其他 Devin 的脚本；编码代理与审查代理来回迭代

**拉力（Pull）：**
- 代理使用量爆炸 → 成本爆炸
- 新的 Mythos 级别更大更强的模型即将到来
- 问题：如何以更低成本获得前沿能力？
- 答案可能是：多代理系统

---

## 现实世界的多代理案例

### 令人印象深刻的演示（但有局限）

| 项目 | 规模 | 特点 |
|------|------|------|
| 构建 Web 浏览器 | 200k LOC | 简单、可验证的成功标准 |
| 构建 C 编译器 | 100k LOC | 简单、可验证的成功标准 |
| 优化 LLM 训练脚本 | 10k+ 迭代 | 简单、可验证的成功标准 |

**共同点**：都有简单、可验证的成功标准。

**现实软件的不同**：需要能够扩展人类品味和决策的系统。

### Cognition 的实践实验

#### 实验 1：单线程写入 + 多代理贡献智能

**架构：**
```
主代理（负责写入）
    ↓
调用子代理 A（只读分析）
调用子代理 B（只读搜索）
调用子代理 C（只读建议）
    ↓
整合结果，单线程写入
```

**关键约束：**
- 子代理不直接修改代码
- 子代理提供分析、建议、上下文
- 主代理保持对写入的控制权

#### 实验 2：Devin 的 Deepwiki 子代理

Devin 可以调用 Deepwiki 子代理获取代码库上下文。

**局限：**
- 这类子代理更像是"工具调用"而非真正的多代理协作
- 只读操作，不参与决策过程

#### 实验 3：审查代理 + 编码代理迭代

**模式：**
1. 编码代理编写代码
2. 审查代理检查并提出建议
3. 编码代理根据建议修改
4. 循环直到满意

**成功要素：**
- 写入操作始终是单线程的
- 审查代理只有"建议权"，没有"写入权"

---

## 有效的多代理模式总结

### ✅ 有效的模式

| 模式 | 描述 | 为什么有效 |
|------|------|-----------|
| **只读子代理** | 搜索、分析、建议 | 不冲突，不制造隐式决策 |
| **单线程写入** | 只有一个代理能修改 | 避免决策分散 |
| **审查-修改循环** | 审查代理 → 编码代理 → 审查代理... | 建议权与写入权分离 |
| **智能分发** | 主代理分发任务，子代理返回结果 | 主代理保持控制 |

### ❌ 无效的模式

| 模式 | 描述 | 为什么无效 |
|------|------|-----------|
| **并行写入代理群** | 多个代理同时修改代码 | 隐式决策冲突 |
| **分治合并** | 分任务 → 并行处理 → 合并结果 | 合并时代理不理解彼此的风格选择 |
| **完全自治代理群** | 代理自主决定做什么 | 决策分散，缺乏协调 |

---

## 给构建者的建议

### 如果你正在考虑多代理

1. **先问自己：真的需要吗？**
   - 单代理 + 好工具 往往就够了
   - 多代理增加复杂性

2. **如果确实需要，遵守约束：**
   - 写入操作单线程
   - 子代理只读或只建议
   - 充分共享上下文

3. **从简单开始：**
   - 先做单代理版本
   - 识别瓶颈
   - 再考虑是否引入多代理

### Context Engineering 检查清单

- [ ] 所有代理看到相同的信息源
- [ ] 使用共享的 todo list / plan files
- [ ] 代理了解整体任务目标
- [ ] 需要时代理能够沟通
- [ ] 写入操作是单线程的
- [ ] 避免了隐式决策冲突

---

## 相关资源

### 核心文章

| 文章 | 作者 | 链接 | 主题 |
|------|------|------|------|
| Don't Build Multi-Agents | Walden Yan | https://cognition.ai/blog/dont-build-multi-agents | 为什么多代理很难 |
| Multi-Agents: What's Actually Working | Walden Yan | X 帖子 | 什么模式确实有效 |
| Building Effective Agents | Anthropic | https://www.anthropic.com/engineering/building-effective-agents | 构建有效代理的最佳实践 |
| How we built our multi-agent research system | Anthropic | https://www.anthropic.com/engineering/building-c-compiler | 多代理研究系统案例 |

### 参考实现

| 项目 | 链接 | 说明 |
|------|------|------|
| OpenAI Swarm | https://github.com/openai/swarm | 多代理框架（Walden 认为方向可能有问题）|
| Microsoft AutoGen | https://github.com/microsoft/autogen | 多代理框架（Walden 认为方向可能有问题）|
| Devin | https://devin.ai | Cognition 的 AI 软件工程师 |

### 相关讨论

| 资源 | 链接 |
|------|------|
| LangChain: How and when to build multi-agent systems | https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems |
| Anthropic vs Cognition on Multi-Agents (YouTube) | https://www.youtube.com/watch?v=JYaGAqvPfYA |

---

## 核心洞察速记

**一句话总结：**

> 多代理系统的正确打开方式是：**多个代理贡献智能，但写入保持单线程。**

**关键转变：**

> 从 "Prompt Engineering" 转向 "Context Engineering"。

**为什么之前反对，现在支持：**

> 不是多代理本身错了，而是 **"并行写入代理群"** 这个模式错了。

**给工程师的第一要务：**

> Context Engineering — 确保代理有正确的上下文。

---

## 扩展思考

### 与我们的 Hermes 系统的关系

这套方法论与我们的 Hermes Agent 架构高度相关：

1. **PM Agent + Worker Agent 分工**
   - PM Agent（主代理）：负责决策、协调、写入
   - Worker Agent（子代理）：负责执行、研究、分析
   - 符合"单线程写入 + 多代理贡献智能"模式

2. **Context Engineering 实践**
   - 使用共享的 SOUL.md 文件
   - 任务分派时传递完整上下文
   - 结果汇总时保持一致性

3. **避免的模式**
   - Worker Agent 不直接做最终决策
   - PM Agent 保持对输出的控制权

### 未来方向

根据 Walden 的洞察，我们可以考虑：

1. **只读研究子代理**
   - 专门用于深度研究的 Worker Agent
   - 返回结构化研究结果
   - PM Agent 做最终整合

2. **审查-迭代循环**
   - 生成内容后，用另一个 Agent 审查
   - 根据反馈迭代改进
   - 保持单线程写入原则

3. **成本优化**
   - 简单任务用轻量级模型
   - 复杂任务才用强模型
   - 多代理系统可能成为降低成本的方案

---

## 结语

Walden Yan 的这两篇文章（10个月前的反对和现在的更新）展示了 AI Agent 领域的快速演进。

**关键教训：**
- 不要轻易否定一个技术方向
- 找到正确的约束条件，复杂系统才能工作
- Context Engineering 比 Prompt Engineering 更根本

**对于我们的系统：**
现有的 PM Agent + Worker Agent 架构已经符合"单线程写入 + 多代理贡献智能"的有效模式。继续强化 Context Engineering，确保信息充分共享，是我们应该坚持的方向。

---

*来自翡冷翠*
