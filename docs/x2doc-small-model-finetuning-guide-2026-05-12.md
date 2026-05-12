# 小模型微调入门实战指南 - X2Doc 整理

> 来源：https://x.com/cjzafir/status/2053847506124206095?s=20
> 作者：@cjzafir (CJ Zafir)
> 发布时间：2026-05-11
> 整理时间：2026-05-12
> 来自翡冷翠

---

## TL;DR

- **从小模型起步**：1B/2B/4B/8B 是最佳学习区间，不要一上来就碰 27B+。
- **用云 GPU 而非买卡**：Google Colab Pro (A100 80GB ~$0.60/hr) 足够跑 9B 以下模型，买卡前先调够 7-10 个模型。
- **AI 生成数据集**：Codex 5.5 做规划 + DeepSeek v4 Pro 生成 rows，效率最高。
- **Unsloth 全链路**：用 Unsloth 的 instruct models 当 base + 它的 notebooks 做参考，丢给 Codex 改配置即可。
- **一天学完核心概念**：SFT、RL(GRPO/DPO/PPO)、LoRA/QLoRA、Quantization、llama.cpp 推理引擎、KV cache。
- **未来是 ELM 时代**：5B-15B 的 Expert Language Models 将取代通用 1T LLM，微调是人人可学的硬技能，企业愿付 $50k+。

---

## 原帖核心内容

CJ Zafir 给出了一套完整的开源小模型微调入门路径，核心逻辑是：**低门槛开始 → 快速迭代 → 理解本质 → 商业化变现**。

### 1. 模型选择：从小做起

> "Start with 1B, 2B, 4B, and 8B models. (Don't start with a 27B model or bigger at first.)"

小模型不仅便宜，更重要的是让整个迭代循环更快：fine-tune 更快、eval 更快、debug 更容易、推理成本更低。

### 2. 硬件策略：租不买

> "Use WebGPU providers. I use Google Colab Pro for any model smaller than 9B. A single A100 80GB costs around $0.60/hr..."

实际支出极低。等你真正调过 7-10 个模型、摸清楚所有细节之后，再考虑买 GPU。

### 3. 数据集生成：Codex × DeepSeek

> "Use Codex 5.5 × DeepSeek v4 Pro to create datasets. Codex to plan, DeepSeek v4 Pro to generate rows."

这是一个双模型协作工作流：
- **Codex 5.5**：负责整体 dataset 结构设计、字段规划、质量检查规则
- **DeepSeek v4 Pro**：负责逐行生成高质量训练数据

评论区补充：至少 20k-30k rows，具体取决于工具数量、是否需要 thinking、tool chaining 复杂度。

### 4. Base Model & Notebook

> "Use Unsloth's instruct models as a base from Hugging Face... Unsloth also provides fast fine-tuning notebooks."

推荐 base models（<8B）：
- Qwen 3.5 4B / 9B
- Gemma4 E4B
- Gemma 3 12B

工作流：拿 Unsloth 的 notebook 丢给 Codex，让它按你的需求改写配置。

### 5. 一天内必须搞懂的概念

- **SFT** (Supervised Fine-Tuning)
- **RL training** (GRPO, DPO, PPO)
- **LoRA / QLoRA**
- **Quantization** (量化类型)
- **Local inference engines** (llama.cpp)
- **KV cache & prompt cache**

### 6. 未来趋势判断

> "Future tech is moving toward small 5B to 15B ELMs (Expert Language Models) rather than general 1T LLMs."

小模型专精特定任务，在成本、隐私、速度上都碾压通用大模型。企业为定制化 AI 模型支付 $50k+ 是常态。

### 7. 企业落地场景（评论区补充）

CJ 在回复中列举的实际企业用例：
- 内部通讯助手 (Slack/Teams)
- 内部数据分析
- OCR (图像转文本、可填写表单)
- 私密竞品调研
- 边缘设备 / IoT / 硬件嵌入式 SLM

---

## 关键信息与资源

| Type | Name | Link | Why it matters |
|---|---|---|---|
| Tool | Unsloth | https://unsloth.ai | 最快的 fine-tuning 框架，提供 instruct models + notebooks |
| Notebook | Unsloth Notebooks | https://github.com/unslothai/notebooks | 250+ fine-tuning & RL notebooks，直接丢给 Codex 改配置 |
| Cloud GPU | Google Colab Pro | https://colab.research.google.com | A100 80GB ~$0.60/hr，足够跑 9B 以下模型 |
| Base Model | Qwen 3.5 4B/9B | https://huggingface.co/Qwen | CJ 推荐 fast learner，适合快速实验 |
| Base Model | Gemma4 E4B / Gemma 3 12B | https://huggingface.co/google | Google 官方轻量模型，边缘部署友好 |
| Mac Tool | mlx-tune | https://github.com/ARahim3/mlx-tune | Apple Silicon Mac 本地 fine-tuning (SFT/DPO/GRPO/Vision) |
| Inference | llama.cpp | https://github.com/ggerganov/llama.cpp | 本地推理引擎，CPU 也能跑量化后小模型 |
| Data Format | JSONL | - | CJ 确认训练数据统一用 jsonl 格式 |

---

## 评论区高价值补充

1. **@DealsForge**: "Most teams should earn the right to move up to larger models." — 小模型是基本功，大模型是升级。
2. **@itsPaulAi**: 询问是否按 query 动态加载不同 fine-tuned 模型 — CJ 确认这是他的实际架构（0.8B custom + 2B + 6B，各自专精一件事）。
3. **@madciapka**: 商业 chatbot 场景如何避免幻觉？CJ 建议学习 embedding models，从文件中提取精确数据而非依赖模型记忆。
4. **@heykomaltiwari**: 用 llama.cpp / vLLM / SGLang / TensorRT-LLM 做推理对比 — latency、tokens/sec、VRAM、并发。推理是企业烧钱的大头。
5. **@JZGibbons**: 实测：0.8B Qwen3.5 + 4000 training inputs (GLM-5 从代码库生成)，CPU 上推理速度惊人。
6. **@bondobull**: 已建立自动化夜间 pipeline，为法律/网络安全/量化金融生成 domain-specific instruction-tuning 数据。
7. **@skyzer4ever**: 导出 Telegram 消息 → 清洗 → fine-tune 匹配个人风格，效果良好。
8. **@martinromanuk**: 用 LF2.5 350m 在 iPhone 上生成定制冥想脚本，超快且可用。

---

## 我的吸收判断

- **可复用能力**：Codex 5.5 × DeepSeek v4 Pro 的双模型数据集生成工作流，可直接复用到 Neumina Agent 的 6 智能体训练数据准备中。
- **值得沉淀到 skill / workflow 吗**：是。"小模型微调入门" 可以成为 Superpowers 中一个独立 skill，覆盖 model selection → dataset generation → fine-tuning → inference → evaluation 的完整链路。
- **对 AI × Product × Biohacking / Super Individual 的价值**：
  - 产品侧：Neumina 的 6 智能体可以走小模型路线，降低推理成本，提升响应速度。
  - 个人品牌：微调是自己的硬技能，未来超级个体的核心技术栈之一。
  - 变现：企业定制化 AI 是 $50k+ 的市场，掌握这套流程等于掌握高价值服务。
- **风险或待验证点**：
  - Codex 5.5 是否允许用于 dataset distillation？评论区 @vincexplorer 指出 OpenAI 可能禁止。需要确认服务条款。
  - 中文小模型的 fine-tuning 生态是否和英文同等成熟？Qwen 系列是中文友好的，但工具和 community 仍以英文为主。
  - 20k-30k rows 的数据集生成成本（API token 费用）需要实测。

---

## 可执行下一步

- [ ] 用 Codex 5.5 + DeepSeek v4 Pro 生成一个 20k rows 的测试数据集（选一个明确任务，如"更年期健康知识问答"）
- [ ] 在 Colab Pro 上跑通第一个 Unsloth fine-tuning notebook（Qwen 3.5 4B）
- [ ] 实测 llama.cpp 本地推理，对比量化前后的 speed 和 quality
- [ ] 确认 OpenAI / Codex 5.5 的服务条款中关于 dataset generation 的限制
- [ ] 将这套流程沉淀为 Superpowers skill：`small-model-finetuning-workflow`

---

*来自翡冷翠*
