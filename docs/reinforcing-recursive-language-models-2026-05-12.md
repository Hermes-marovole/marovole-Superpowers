# Reinforcing Recursive Language Models

> alphaXiv 官方技术博客 | 作者：Daniel Kim, Rehaan Ahmad | 2026-05-12

---

## 执行摘要

alphaXiv 团队发布了一项关于**通过强化学习（RL）微调4B小模型，使其成为原生递归语言模型（RLM）**的研究。他们的核心发现是：不需要分别训练父模型和子模型的策略，而是用**单一共享策略**让同一个4B模型同时扮演任务分解器（parent decomposer）和子智能体（child sub-agent）的双重角色。在跨科学论文的证据选择任务上，这个RL微调后的4B RLM在**质量上匹配 Claude Sonnet 4.6**，但**墙钟时间仅为7秒**（Sonnet 版本超过60秒），运行成本大幅降低。

---

## 核心亮点

### 1. 什么是递归语言模型（RLM）

递归语言模型是一种**推理策略，而非架构变革**。它将极长的用户输入（上下文）视为环境的一部分，而非直接塞进模型的上下文窗口。模型通过 Python REPL 环境**程序化地检查、分解和递归调用自己**来处理这些长上下文，最终回答用户查询。

REPL 环境提供的核心函数：
- `FINAL(answer)` / `FINAL_VAR(var_name)` — 标记结束并返回最终答案
- `rlm_query(prompt, context=None)` — 派生单个子 RLM，运行新的 agent loop
- `rlm_query_batched(prompts, context_list=None)` — 并行派生多个子 RLM

### 2. RL 微调如何让4B模型学会递归行为

作者的核心突破在于：**RL 可以让小模型学习任务特定的 RLM 行为，这种行为无法通过提示词或监督微调（SFT）激发**。

关键训练设计：
- **冷启动 SFT**：先用大模型（Qwen3.5-397B-A17B-Instruct）生成教师轨迹，在小数据集上 SFT，让 4B 模型先学会 REPL 环境的基本操作
- **逐步训练（Stepwise Training）**：RLM 的每一轮对话都重新构建，不共享前缀。每个轮次产生 N 个训练样本，所有轮次共享最终的优势 A
- **单一共享策略**：不分别训练父模型和子模型，一个模型同时扮演双重角色，子 RLM 的 rollout 继承父 RLM 的优势
- **评分卡套目判官（Rubric-based LLM Judges）**：因为可验证奖励（如 F1）太噪音，改用评分卡套目判官更稳健地分配奖励

### 3. 子模型继承父模型优势（Advantage Inheritance）

这是最具创新性的方法论贡献。

**GRPO 目标扩展到递归树**：
- 每个查询采样 G 个父 RLM rollout
- 只有父 RLM 接收可验证奖励 r_g
- 组内相对优势计算：A_g = (r_g - mean) / std
- **每个子 RLM 继承其父亲的优势：A_{g,i} := A_g**
- 子损失贡献加上归一化项 1/k_g，确保深度平衡

目标公式可递归扩展到任意深度：
```
L_subtree(y, A) = L_node(y, A) + (1/k_y) * Σ L_subtree(y_i, A)
```

### 4. 实验设计：跨科学论文的证据选择

**任务目标**：给定一个问题和一组 arXiv 论文，从论文中找出能回答该问题的原文片段。

**数据集**：
- 选取 arXiv 论文，检索最多9篇语义相似论文构成组
- OCR 模型将论文分段
- 边界模型生成问题并选择相关段落
- 共1000个查询，每组最多10篇论文，每组最多3个问题
- 测试时使用 PDF 解析库的噪音文本（模拟真实生产环境）

**递归策略**：
- 父 RLM：检索标题，判断哪些论文值得深入探索
- 并行派生子 RLM（每篇论文一个）提取相关片段
- 父 RLM 合并所有子结果

### 5. 实验结果

**单论文任务**（无子调用）：
- Qwen3.5-4B 评分从约0.6 提升到 **0.80**，**匹配 Claude Sonnet 4.6 基准**

**多论文任务**（含递归子调用）：
- 评分从 ~0.30 提升到 ~0.60，接近 Sonnet 4.6 的0.65
- 在同样的 RLM 架构下，**RL 微调后的4B模型超过 GPT-5.4-mini 和 Gemini-3-Flash**
- **墙钟时间：4B版本仅7秒，Sonnet 版本超过60秒**
- 运行在单个 8xH200 节点上，最多 512 并发 rollout

### 6. 关键发现与限制

**发现**：
- SFT 冷启动是必要的：没有 SFT 阶段，4B 模型的 pass@16 为0，因为 RLM 任务对小模型来说已经超出其能力边界
- 简化提示词实验（从1500 tokens减到200 tokens）结果略低且更不稳定，说明现有模型仍需要详细策略提示

**往后看的方向**：
- **更精细的信用分配**：当前子模型简单继承父优势，未来可以为不同深度设计多层奖励
- **策略自发现**：未来目标是让 RLM 自己发现解决问题的策略，而非依赖人类编写的详细提示
- **规模化**：目前的模型还不够大，大规模 RLM 训练将是下一个里程碑

---

## 延伸思考

### 为什么这件事很重要

RLM 代表了 LLM 推理的下一个阶段。从 CoT 到 ReAct 再到 RLM，每一步都是**在不增加模型参数的情况下扩展有效上下文长度**。而这篇工作的特殊之处在于，它证明了**RL 微调可以让小模型学会这种复杂的推理行为**，而不是只有大模型才行。这意味着企业可以用极低的部署成本构建生产级的长上下文处理系统。

### 与 RAG 的关系

作者明确指出 RAG 并不适合这个任务，因为需要动态返回长度和数量不确定的原文片段，而不是固定大小的 top-k。但二者并非互斥：RAG 索引的切片可以作为 REPL 中的另一个工具，与 `search` 和 `extract_section` 并存。

### 与原始 RLM 论文的区别

原始 RLM 论文（Zhang et al., arXiv 2512.24601）使用 SFT 训练 Qwen3-8B学会 REPL 环境操作，但未针对特定任务训练。这篇工作则**用 RL 针对证据选择任务微调 4B 模型**，让它在真实生产任务上达到大模型质量。

---

## 背景信息

- **来源博客**：https://alphaxiv.org/blog/reinforcement-learning-for-rlms
- **作者**：Daniel Kim, Rehaan Ahmad (alphaXiv)
- **发布日期**：2026-05-12
- **原始 RLM 论文**：[Recursive Language Models](https://arxiv.org/abs/2512.24601) — Zhang et al.
- **代码开源**：https://github.com/NovaSky-AI/SkyRL/pull/1596
- **训练配置**：https://github.com/NovaSky-AI/SkyRL/blob/main/examples/train/rlm/run_multi_paper_rlm.sh
- **X 原帖**：https://x.com/askalphaxiv/status/2054236405308739859

---

来自翡冷翠
