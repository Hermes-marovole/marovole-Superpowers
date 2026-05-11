# Artificial Analysis Coding Agent Index — X2Doc 整理

> 来源：https://x.com/ArtificialAnlys/status/2053865095076438427?s=20
> 作者：@ArtificialAnlys
> 整理时间：2026-05-11
> 来自翡冷翠

---

## TL;DR

- Artificial Analysis 发布了 **Coding Agent Index**，首次将 **model + harness 组合**作为单元来 benchmark，而非单独测模型
- 使用 3 套任务：SWE-Bench-Pro-Hard-AA（150 任务）、Terminal-Bench v2（84 任务）、SWE-Atlas-QnA（124 技术问答）
- **Opus 4.7 in Cursor CLI 领跑** (61)，GPT-5.5 in Codex / Opus 4.7 in Claude Code 紧跟 (60)
- **开源模型有竞争力但仍落后：**GLM-5.1 in Claude Code 53 分领先，Kimi K2.6 和 DeepSeek V4 Pro 同为 50 分
- **Gemini 3.1 Pro 在自家 CLI 上表现失常** (43)，与其在 Intelligence Index 上的排名形成鲜明对比
- **成本差异 >30x：**Composer 2 in Cursor CLI 仅 $0.07/任务，GPT-5.5 in Codex 和 GLM-5.1 in Claude Code 高达 ~$2.2/任务
- **时间差异 >7x：**Opus 4.7 in Claude Code ~6 分钟/任务 vs Kimi K2.6 ~40 分钟/任务
- **社区共识：**open harnesses（OpenCode、Pi、Droid、Warp、Hermes 等）被大量呼吸叫加入下一轮测试

---

## 原帖核心内容

Artificial Analysis 的核心论点：开发者选 AI 写代码时，同时在选 **模型** 和 **harness**（执行框架）。只测模型不够，必须 benchmark 组合。

### 三套测试集

| 测试集 | 任务数 | 性质 |
|---|---|---|
| SWE-Bench-Pro-Hard-AA | 150 | Scale AI 采样，前沿模型觉得难的真实代码任务 |
| Terminal-Bench v2 | 84 | Laude Institute，系统管理/加密/机器学习等终端任务 |
| SWE-Atlas-QnA | 124 | Scale AI，代码行为、问题根因分析等问答型任务 |

### 综合排名（按 Index 总分）

- **61** — Opus 4.7 in Cursor CLI
- **60** — GPT-5.5 in Codex; Opus 4.7 in Claude Code
- **58** — GPT-5.5 in Cursor CLI
- **53** — GLM-5.1 in Claude Code ★ 开源最高
- **50** — Kimi K2.6 in Claude Code; DeepSeek V4 Pro in Claude Code
- **48** — Composer 2 in Cursor CLI
- **43** — Gemini 3.1 Pro in Gemini CLI ‼️ 明显低于其模型能力

### 成本与效率分析

**单任务 API 成本**（洞察：>30x）：
- 最便宜：Composer 2 in Cursor CLI — **$0.07**
- 低价开源：DeepSeek V4 Pro in Claude Code — **$0.35**
- Kimi K2.6 in Claude Code — **$0.76**
- 最贵：GLM-5.1 in Claude Code **$2.26**，GPT-5.5 in Codex **$2.21**

**Token 用量**（洞察：>3x）：
- GLM-5.1 in Claude Code: 4.8M/任务（部分因进入循环）
- Kimi K2.6: 3.7M; DeepSeek V4 Pro: 3.5M
- GPT-5.5 in Codex: 2.8M
- Opus 4.7 in Claude Code: 1.7M — 最省 token

**Cache hit rate**: 80%–96%，提示 provider 路由和 harness prompt 结构对成本影响显著

**执行时间**（洞察：>7x）：
- 最快：Opus 4.7 in Claude Code — **~6 分钟/任务**
- 最慢：Kimi K2.6 in Claude Code — **~40 分钟/任务**
- 差距主要来自 **平均 turns 数**：Opus 4.7 完成任务所需轮次显著更少

### Cursor Composer 2 的进步

Cursor 自称 Composer 2 基于 Kimi K2.5 构建，经过大量 post-training 增强后：
- 得分 48，接近开源领军
- 价格 $0.07/任务 — 全场最便宜
- 社区释疑：Kimi K2.5 本身未被测试，难以直接证明 "改进幅度"

---

## 关键信息与资源

| Type | Name | Link | Why it matters |
|---|---|---|---|
| Benchmark | Artificial Analysis Coding Agent Index | https://artificialanalysis.ai | 官方测试结果大全，支持按分数/成本/时间/模型/框架筛选 |
| Benchmark | SWE-Bench Pro (Scale AI) | 由 Scale AI 提供基准 | 行业标准代码任务 benchmark |
| Benchmark | Terminal-Bench v2 (Laude Institute) | 由 Laude Institute 提供 | 终端/系统管理类 agent 任务集 |
| Model | GLM-5.1 (Zhipu AI) | 开源权重 | 开源模型在 Claude Code harness 下的最佳表现 |
| Harness | Claude Code (Anthropic) | 参与测试的框架之一 | Opus 4.7 在此框架下时间效率最优 |
| Harness | Cursor CLI | 参与测试的框架之一 | Opus 4.7 在此框架下总分最高 |
| Harness | Gemini CLI | 参与测试的框架之一 | Gemini 3.1 Pro 在自家框架下失常，引发社区质疑 |

---

## 社区反馈精华

**测试方法学争议：**
- 大量用户强烈要求计入 **xhigh/max reasoning level**，当前默认 medium 可能拖累了 GPT-5.5 和 Claude 的潜力
- "引用中转发、从头做起" 的呼声极高，特别是 **Pi.dev、OpenCode、Hermes、Droid、Warp** 等开源 harnesses
- @teortaxesTex 特别点名 DeepSeek V4-Flash 和开源 harnesses

**关键观察：**
- @aneesmerchant: "Harness choice shifts benchmark scores more than model swaps in some combos" — 框架选择在某些情况下比换模型影响更大
- @DealsForge: "Cost per successful task = model score + token usage + retries + rate limits + provider reliability" — 真正的消费者指标
- @synabunAI: "The 7x time gap... breaks the interactive development loop entirely" — 40 分钟 vs 6 分钟不只是成本，是交互开发流的崩溃
- @opencode / @inflectivAI 等正在追求加入下一轮测试

---

## 我的吸收判断

- **可复用能力：** AI Coding 选型决策框架 — 不再只看模型分数，而是综合考量 【模型能力 × harness 效率 × 成本 × 时间】四维度
- **值得沉淀到 skill / workflow 吗：** 是。可扩展为「AI Coding 工具选型速查」skill，贴到 Neuma/Neumina 内部 SOP 和外包管理
- **对 AI × Product × Biohacking / Super Individual 的价值：** 极高。作为全栈工程师和 AI Coding 推广者，这套 benchmark 数据是最好的“工具选型依据”，可用于：
  1. 团队 AI Coding SOP 制定（Codex vs Claude Code vs Cursor 的场景匹配）
  2. 外包/实习生环境统一（避免 "用错组合浪费钱"）
  3. 本地推理加速的参考基准（对比消费级与企业级的性价比）
- **风险或待验证点：**
  - 所有测试均使用 **默认 reasoning level** (medium)，实际中大多数用户会手动切到 xhigh/max，排名可能重大变化
  - Cursor Composer 2 的 "Kimi K2.5 基座 + post-training" 声明未被独立验证
  - 开源 harnesses 未入测试，不能完全代表“自由组合”的潜力
  - 此次测试更值得被视为 **harness 层的 benchmark** 而非稳定终极排名

---

## 可执行下一步

- [ ] 追踪 Artificial Analysis 后续测试，特别是加入 OpenCode、Pi.dev 等开源 harness 后的排名变化
- [ ] 在 Neuma 团队内部建立基于这份数据的 **AI Coding 工具选型决策树**，匹配任务类型到最优 model+harness 组合
- [ ] 测试 Claude Code + Opus 4.7 在本地项目（M2 Max）上的实际体验，验证 "6 分钟/任务" 在中型代码库上的复现性
- [ ] 关注 reasoning level 对结果的影响：如果有 xhigh/max 版本补充数据，更新内部 SOP
- [ ] 将此信息沉淀为客户报告素材（灵知生物在推广 AI Coding 效率时可引用权威第三方数据）

---

*来自翡冷翠*
