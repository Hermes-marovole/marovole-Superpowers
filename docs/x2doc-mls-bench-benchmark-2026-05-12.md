# MLS-Bench：AI 自主科研能力基准测试 - X2Doc 整理

> 来源：https://x.com/sheriyuo/status/2054077027071009082?s=20
> 作者：Xiuyu Li (@sheriyuo)
> 发布时间：2026-05-12 13:51 CST
> 整理时间：2026-05-12
> 来自翡冷翠

---

## TL;DR

- **MLS-Bench** 是一个评估 AI 系统能否发明可泛化、可扩展 ML 方法的全新基准测试，由 UC Berkeley、Princeton、Tsinghua 等机构联合推出。
- 包含 **140 个任务、12 个领域**（RL、机器人、CV、优化、MLsys、可信学习等），不是 leaderboard gaming，而是考验真正的科研能力。
- **Lite 子集（30 任务）首批结果**：GPT-5.5 Pro 与 Claude Opus 4.7 并列第一（36.1%），GLM 5.1 意外排第 4（29.8%），DeepSeek-V4 Flash（28.5%）超越 GPT-5.5（27.1%）。
- 核心发现：当前 coding agents 远未达到可靠超越人类方法的水平，**工程式调优远比真正的科研发明容易**。
- 对 AI Coding Agent 赛道有重要信号意义：SWE 编码之外的 Auto Research 是下一个主要战场，但瓶颈不在算力/搜索，而在科学洞察力。

---

## 原帖核心内容

Xiuyu Li 转发 Wenhao Chai 的 MLS-Bench 论文 announcement，重点提炼了 benchmark 的差异化价值和首批模型排名：

> DeepSeek-V4 Flash > GPT-5.5 🥳
> But GLM-5.1: who are you🤯
>
> Why this benchmark: it rewards methods that have truly stood the test of time and scale.
>
> MLS-Bench is especially interesting since it is not about squeezing a single dataset with hand-tuned tricks. It is about atomic, generalizable ML science improvements that can transfer across models, datasets, and tasks. That feels much closer to real research than leaderboard gaming.
>
> Also, the benchmark is broad enough to cover 145 tasks across 12 categories, including RL, robotics, CV, optimization, MLsys, and trustworthy learning. In other words, this is the kind of eval where strong performance actually means something.

---

## MLS-Bench-Lite Intelligence 排名（30 任务子集）

| 排名 | 模型 | 平均分（标准化） |
|:---:|:---|:---:|
| 1 (tie) | GPT-5.5 Pro | 36.1% |
| 1 (tie) | Claude Opus 4.7 | 36.1% |
| 3 | Claude Opus 4.6 | 35.9% |
| 4 | **GLM 5.1** | **29.8%** |
| 5 | DeepSeek-V4 Pro | 29.0% |
| 6 | **DeepSeek-V4 Flash** | **28.5%** |
| 7 | GPT-5.5 | 27.1% |
| 8 | Gemini 3.1 Pro | 26.6% |
| 9 | GPT-5.4 | 25.8% |
| 10 | DeepSeek-V3.2 | 25.7% |
| 11 | Gemini 3.1 Flash | 23.7% |
| 12 | Qwen 3.6 Max | 22.6% |
| 13 (tie) | Claude Sonnet 4.6 | 21.2% |
| 13 (tie) | Kimi K2.6 | 21.2% |
| 15 | Qwen 3.6 Plus | 19.5% |

> 注：所有模型得分均低于 40%，说明 MLS-Bench 对当前 AI 系统来说极具挑战性。

---

## 关键信息与资源

| Type | Name | Link | Why it matters |
|:---|:---|:---|:---|
| 论文 | MLS-Bench: A Holistic and Rigorous Assessment of AI Systems on Building Better AI | [arXiv:2605.08678](https://arxiv.org/abs/2605.08678) | 核心论文，定义了 Auto Research 的 evaluation 框架 |
| 代码 | MLS-Bench GitHub | [github.com/Imbernoulli/MLS-Bench](https://github.com/Imbernoulli/MLS-Bench) | 开源 benchmark 代码和数据集 |
| 网站 | MLS-Bench 社区平台 | [mls-bench.com](https://mls-bench.com) | 可提交结果、查看排行榜 |
| 原帖 | Xiuyu Li 的 X 帖子 | [x.com/sheriyuo/...](https://x.com/sheriyuo/status/2054077027071009082) | 首批 benchmark 排名的曝光源 |
| 引用帖 | Wenhao Chai 的 announcement | [x.com/wenhaocha1/...](https://x.com/wenhaocha1/status/2054020662541574488) | 论文作者官方发布，含项目背景 |

---

## 论文核心发现（来自 Wenhao Chai 的 announcement）

Wenhao Chai（Princeton PhD，即将加入 Google DeepMind）阐述了 MLS-Bench 的定位：

1. **Auto Research 是 SWE Coding 之外的下一个主要市场**，但更难、更有挑战性。
2. **区分两类 Auto Research**：
   - **工程型**（如 MLE-Bench、PostTrainBench）：agents 被要求在特定工程目标上调优，不考核可迁移性。
   - **科研型**（MLS-Bench）：要求 agent 改进 ML 系统的某个组件，并证明改进能在受控环境下泛化和扩展。
3. **当前 agents 远未达到稳定超越人类设计方法的水平**，工程式调优对它们来说比真正的科研发明容易得多。
4. **瓶颈不在算力、搜索或上下文，而在科学洞察力**——即规划、验证和扩展假设的能力。

论文引用 Richard Sutton 的 The Bitter Lesson：
> "We want AI agents that can discover like we can, not which contain what we have discovered."

---

## 我的吸收判断

- **可复用能力**：
  - MLS-Bench 的 evaluation 框架可直接用于评估 Neumina Agent 或公司内部 coding agent 的科研辅助能力。
  - 区分 "工程型" 与 "科研型" auto research 的框架对产品设计有启发：当前大多数 AI coding 工具（包括 Codex/Claude Code）本质上仍是工程型，科研型能力仍是蓝海。
- **值得沉淀到 skill / workflow 吗**：
  - 是。可作为 `agent-workflow-system` 和 `ai-coding-agent-model-config` 的参考输入，用于选型评估。
  - 可纳入团队 AI Coding SOP 的模型选型参考数据。
- **对 AI × Product × Biohacking / Super Individual 的价值**：
  - DeepSeek-V4 Flash 在该 benchmark 上超越 GPT-5.5，进一步验证了我日常用 DS V4 Flash 做主力模型的判断。
  - GLM 5.1 的意外表现值得关注，可能意味着国产模型在科研推理场景有独特优势。
  - 对 Super Individual 而言：如果未来的 personal agent 需要具备 "科研发明" 能力而非仅仅 "代码工程" 能力，MLS-Bench 定义的能力边界就是需要追赶的目标。
- **风险或待验证点**：
  - 这是 **Lite 子集（30 任务）** 的结果，完整 140 任务的结果尚未公开。
  - 图表中的模型命名（如 "Gemini 31 Flash" 缺少小数点）可能是 OCR/渲染问题，需要以官方 leaderboard 为准。
  - 论文声称 agents 在工程调优上表现更好，但未明确给出各 agent 框架（如 OpenAI 的 deep research vs 自主 coding agent）的对比数据。

---

## 可执行下一步

- [ ] 访问 [mls-bench.com](https://mls-bench.com) 查看最新完整 leaderboard，验证 Lite 子集结果。
- [ ] 阅读 arXiv 论文全文，重点看 test-time scaling、adaptive compute allocation、context provision 的消融实验。
- [ ] 在团队 AI Coding SOP 中补充 MLS-Bench 作为模型科研能力选型参考。
- [ ] 评估 Neumina Agent 的 "神农"（科研助手）模块是否可借鉴 MLS-Bench 的任务设计思路。
- [ ] 追踪 Wenhao Chai / Princeton 团队在 auto research 方向的后续工作。

---

*来自翡冷翠*
