# DeepSeek 相关 arXiv 论文汇总

**搜索时间**: 2025年4月30日  
**总计论文数**: 120 篇

---

## 官方 DeepSeek 技术报告

### 1. DeepSeek-V3 Technical Report

- **arXiv ID**: `2412.19437`
- **发布日期**: 2024-12-27
- **作者**: DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang...
- **链接**: [https://arxiv.org/abs/2412.19437](https://arxiv.org/abs/2412.19437)
- **PDF**: [https://arxiv.org/pdf/2412.19437.pdf](https://arxiv.org/pdf/2412.19437.pdf)

**摘要**:

DeepSeek-V3 is a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. It incorporates Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, along with auxiliary-loss-free strategy for load balancing and multi-token prediction training objective. Trained on 14.8 trillion diverse and high-quality tokens, DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models.

---

### 2. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- **arXiv ID**: `2501.12948`
- **发布日期**: 2025-01-22
- **作者**: DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song...
- **链接**: [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948)
- **PDF**: [https://arxiv.org/pdf/2501.12948.pdf](https://arxiv.org/pdf/2501.12948.pdf)

**摘要**:

We introduce DeepSeek-R1, which incorporates multi-stage training and cold-start data before applying large-scale reinforcement learning (RL). DeepSeek-R1 demonstrates performance on par with OpenAI-o1 across math, code, and reasoning tasks. We also open-source six dense models distilled from DeepSeek-R1 based on Llama and Qwen.

---

### 3. DeepSeek LLM: Scaling Open-Source Language Models with Longtermism

- **arXiv ID**: `2401.02954`
- **发布日期**: 2024-01-05
- **作者**: DeepSeek-AI, Xiao Bi, Deli Chen, Guanting Chen, Shanhuang Chen...
- **链接**: [https://arxiv.org/abs/2401.02954](https://arxiv.org/abs/2401.02954)
- **PDF**: [https://arxiv.org/pdf/2401.02954.pdf](https://arxiv.org/pdf/2401.02954.pdf)

**摘要**:

We introduce DeepSeek LLM, an advanced language model trained from scratch on a vast dataset of 2 trillion tokens in both English and Chinese. We release open-source DeepSeek LLM 7B/67B Base and Chat models to the public. Evaluation results demonstrate that DeepSeek LLM 67B achieves state-of-the-art performance among open-source LLMs.

---

## 引用/提及 DeepSeek 的其他研究论文

### 4. When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models

- **arXiv ID**: `2604.26649v1`
- **发布日期**: 2026-04-29
- **作者**: Dongxin Guo, Jikun Wu, Siu Ming Yiu
- **链接**: [https://arxiv.org/abs/2604.26649v1](https://arxiv.org/abs/2604.26649v1)
- **PDF**: [https://arxiv.org/pdf/2604.26649v1.pdf](https://arxiv.org/pdf/2604.26649v1.pdf)

**摘要**:

Large reasoning models such as DeepSeek-R1 and OpenAI o1 generate extended chains of thought spanning thousands of tokens, yet their integration with retrieval-augmented generation (RAG) remains fundamentally misaligned. Current RAG systems optimize for providing context before reasoning begins, while reasoning models require evidence injection during multi-step inference chains. We introduce ReaL...

---

### 5. DenseStep2M: A Scalable, Training-Free Pipeline for Dense Instructional Video Annotation

- **arXiv ID**: `2604.26565v1`
- **发布日期**: 2026-04-29
- **作者**: Mingji Ge, Qirui Chen, Zeqian Li, Weidi Xie
- **链接**: [https://arxiv.org/abs/2604.26565v1](https://arxiv.org/abs/2604.26565v1)
- **PDF**: [https://arxiv.org/pdf/2604.26565v1.pdf](https://arxiv.org/pdf/2604.26565v1.pdf)

**摘要**:

Long-term video understanding requires interpreting complex temporal events and reasoning over procedural activities. While instructional video corpora, like HowTo100M, offer rich resources for model training, they present significant challenges, including noisy ASR transcripts and inconsistent temporal alignments between narration and visual content. In this work, we introduce an automated, train...

---

### 6. A Systematic Comparison of Prompting and Multi-Agent Methods for LLM-based Stance Detection

- **arXiv ID**: `2604.26319v1`
- **发布日期**: 2026-04-29
- **作者**: Genan Dai, Zini Chen, Yi Yang, Bowen Zhang
- **链接**: [https://arxiv.org/abs/2604.26319v1](https://arxiv.org/abs/2604.26319v1)
- **PDF**: [https://arxiv.org/pdf/2604.26319v1.pdf](https://arxiv.org/pdf/2604.26319v1.pdf)

**摘要**:

Stance detection identifies the attitude of a text author toward a given target. Recent studies have explored various LLM-based strategies for this task, from zero-shot prompting to multi-agent debate. However, existing works differ in data splits, base models, and evaluation protocols, making fair comparison difficult. We conduct a systematic comparison that evaluates five methods across two cate...

---

### 7. Learning Generalizable Multimodal Representations for Software Vulnerability Detection

- **arXiv ID**: `2604.25711v1`
- **发布日期**: 2026-04-28
- **作者**: Zeming Dong, Yuejun Guo, Qiang Hu, Yao Zhang, Maxime Cordy...
- **链接**: [https://arxiv.org/abs/2604.25711v1](https://arxiv.org/abs/2604.25711v1)
- **PDF**: [https://arxiv.org/pdf/2604.25711v1.pdf](https://arxiv.org/pdf/2604.25711v1.pdf)

**摘要**:

Source code and its accompanying comments are complementary yet naturally aligned modalities-code encodes structural logic while comments capture developer intent. However, existing vulnerability detection methods mostly rely on single-modality code representations, overlooking the complementary semantic information embedded in comments and thus limiting their generalization across complex code st...

---

### 8. Leveraging LLMs for Multi-File DSL Code Generation: An Industrial Case Study

- **arXiv ID**: `2604.24678v1`
- **发布日期**: 2026-04-27
- **作者**: Sivajeet Chand, Kevin Nguyen, Peter Kuntz, Alexander Pretschner
- **链接**: [https://arxiv.org/abs/2604.24678v1](https://arxiv.org/abs/2604.24678v1)
- **PDF**: [https://arxiv.org/pdf/2604.24678v1.pdf](https://arxiv.org/pdf/2604.24678v1.pdf)

**摘要**:

Large language models (LLMs) perform strongly on general-purpose code generation, yet their applicability to enterprise domain-specific languages (DSLs) remains underexplored, especially for repository-scale change generation spanning multiple files and folder structures from a single natural-language (NL) instruction. We report an industrial case study at BMW that adapts code-oriented LLMs to gen...

---

### 9. Beyond the Attention Stability Boundary: Agentic Self-Synthesizing Reasoning Protocols

- **arXiv ID**: `2604.24512v1`
- **发布日期**: 2026-04-27
- **作者**: Dahlia Shehata, Ming Li
- **链接**: [https://arxiv.org/abs/2604.24512v1](https://arxiv.org/abs/2604.24512v1)
- **PDF**: [https://arxiv.org/pdf/2604.24512v1.pdf](https://arxiv.org/pdf/2604.24512v1.pdf)

**摘要**:

As LLM agents transition to autonomous digital coworkers, maintaining deterministic goal-directedness in non-linear multi-turn conversations emerged as an architectural bottleneck. We identify and formalize a systemic failure mode termed the Attention Latch in decoder-only autoregressive Transformers. This phenomenon, a behavioral manifestation of Information Over-squashing, occurs when the cumula...

---

### 10. Automated Classification of Human Code Review Comments with Large Language Models

- **arXiv ID**: `2604.23667v1`
- **发布日期**: 2026-04-26
- **作者**: Semih Çağlar, Şükrü Eren Gökırmak, Eray Tüzün
- **链接**: [https://arxiv.org/abs/2604.23667v1](https://arxiv.org/abs/2604.23667v1)
- **PDF**: [https://arxiv.org/pdf/2604.23667v1.pdf](https://arxiv.org/pdf/2604.23667v1.pdf)

**摘要**:

Context: Code reviews are essential for maintaining software quality, yet many human review comments suffer from issues such as redundancy, vagueness, or lack of constructiveness. These types of comments may slow down feedback and obscure important insights. Prior work on code review comments mostly explore the detection and categorization of useful comments, while fine-grained categorization of c...

---

### 11. Scaling Multi-Node Mixture-of-Experts Inference Using Expert Activation Patterns

- **arXiv ID**: `2604.23150v1`
- **发布日期**: 2026-04-25
- **作者**: Abhimanyu Bambhaniya, Geonhwa Jeong, Jason Park, Jiecao Yu, Jaewon Lee...
- **链接**: [https://arxiv.org/abs/2604.23150v1](https://arxiv.org/abs/2604.23150v1)
- **PDF**: [https://arxiv.org/pdf/2604.23150v1.pdf](https://arxiv.org/pdf/2604.23150v1.pdf)

**摘要**:

Most recent state-of-the-art (SOTA) large language models (LLMs) use Mixture-of-Experts (MoE) architectures to scale model capacity without proportional per-token compute, enabling higher-quality outputs at manageable serving costs. However, MoE inference at scale is fundamentally bottlenecked by expert load imbalance and inefficient token routing, especially in multi-node deployments where tokens...

---

### 12. Guess-Verify-Refine: Data-Aware Top-K for Sparse-Attention Decoding on Blackwell via Temporal Correlation

- **arXiv ID**: `2604.22312v1`
- **发布日期**: 2026-04-24
- **作者**: Long Cheng, Ritchie Zhao, Timmy Liu, Mindy Li, Xianjie Qiao...
- **链接**: [https://arxiv.org/abs/2604.22312v1](https://arxiv.org/abs/2604.22312v1)
- **PDF**: [https://arxiv.org/pdf/2604.22312v1.pdf](https://arxiv.org/pdf/2604.22312v1.pdf)

**摘要**:

Sparse-attention decoders rely on exact Top-K selection to choose the most important key-value entries for each query token. In long-context LLM serving, this Top-K stage runs once per decode query and becomes a meaningful latency bottleneck even when the indexer and attention kernels are already highly optimized. We present \textbf{Guess-Verify-Refine (GVR)}, a data-aware exact Top-K algorithm fo...

---

### 13. When Cow Urine Cures Constipation on YouTube: Limits of LLMs in Detecting Culture-specific Health Misinformation

- **arXiv ID**: `2604.22002v1`
- **发布日期**: 2026-04-23
- **作者**: Anamta Khan, Ratna Kandala,  Deepti, Sheza Munir, Joyojeet Pal
- **链接**: [https://arxiv.org/abs/2604.22002v1](https://arxiv.org/abs/2604.22002v1)
- **PDF**: [https://arxiv.org/pdf/2604.22002v1.pdf](https://arxiv.org/pdf/2604.22002v1.pdf)

**摘要**:

Social media platforms have become primary channels for health information in the Global South. Using gomutra (cow urine) discourse on YouTube in India as a case study, we present a post-facto Large Language Model (LLM)-assisted discourse analysis of 30 multilingual transcripts showing that promotional content blends sacred traditional language with pseudo-scientific claims in ways that sophistica...

---

### 14. Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers

- **arXiv ID**: `2604.21700v1`
- **发布日期**: 2026-04-23
- **作者**: Jiali Wei, Ming Fan, Guoheng Sun, Xicheng Zhang, Haijun Wang...
- **链接**: [https://arxiv.org/abs/2604.21700v1](https://arxiv.org/abs/2604.21700v1)
- **PDF**: [https://arxiv.org/pdf/2604.21700v1.pdf](https://arxiv.org/pdf/2604.21700v1.pdf)

**摘要**:

The growing application of large language models (LLMs) in safety-critical domains has raised urgent concerns about their security. Many recent studies have demonstrated the feasibility of backdoor attacks against LLMs. However, existing methods suffer from three key shortcomings: explicit trigger patterns that compromise naturalness, unreliable injection of attacker-specified payloads in long-for...

---

### 15. Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection

- **arXiv ID**: `2604.21282v1`
- **发布日期**: 2026-04-23
- **作者**: Zhaohui Geoffrey Wang
- **链接**: [https://arxiv.org/abs/2604.21282v1](https://arxiv.org/abs/2604.21282v1)
- **PDF**: [https://arxiv.org/pdf/2604.21282v1.pdf](https://arxiv.org/pdf/2604.21282v1.pdf)

**摘要**:

Automated code vulnerability detection is critical for software security, yet existing approaches face a fundamental trade-off between detection accuracy and computational cost. We propose a heterogeneous multi-agent architecture inspired by game-theoretic principles, combining cloud-based LLM experts with a local lightweight verifier. Our "3+1" architecture deploys three cloud-based expert agents...

---

### 16. Exploiting LLM-as-a-Judge Disposition on Free Text Legal QA via Prompt Optimization

- **arXiv ID**: `2604.20726v2`
- **发布日期**: 2026-04-22
- **作者**: Mohamed Hesham Elganayni, Runsheng Chen, Sebastian Nagl, Matthias Grabmair
- **链接**: [https://arxiv.org/abs/2604.20726v2](https://arxiv.org/abs/2604.20726v2)
- **PDF**: [https://arxiv.org/pdf/2604.20726v2.pdf](https://arxiv.org/pdf/2604.20726v2.pdf)

**摘要**:

This work explores the role of prompt design and judge selection in LLM-as-a-Judge evaluations of free text legal question answering. We examine whether automatic task prompt optimization improves over human-centered design, whether optimization effectiveness varies by judge feedback style, and whether optimized prompts transfer across judges. We systematically address these questions on the LEXam...

---

### 17. WebGen-R1: Incentivizing Large Language Models to Generate Functional and Aesthetic Websites with Reinforcement Learning

- **arXiv ID**: `2604.20398v1`
- **发布日期**: 2026-04-22
- **作者**: Juyong Jiang, Chenglin Cai, Chansung Park, Jiasi Shen, Sunghun Kim...
- **链接**: [https://arxiv.org/abs/2604.20398v1](https://arxiv.org/abs/2604.20398v1)
- **PDF**: [https://arxiv.org/pdf/2604.20398v1.pdf](https://arxiv.org/pdf/2604.20398v1.pdf)

**摘要**:

While Large Language Models (LLMs) excel at function-level code generation, project-level tasks such as generating functional and visually aesthetic multi-page websites remain highly challenging. Existing works are often limited to single-page static websites, while agentic frameworks typically rely on multi-turn execution with proprietary models, leading to substantial token costs, high latency, ...

---

### 18. Less Languages, Less Tokens: An Efficient Unified Logic Cross-lingual Chain-of-Thought Reasoning Framework

- **arXiv ID**: `2604.20090v1`
- **发布日期**: 2026-04-22
- **作者**: Chenyuan Zhang, Qiguang Chen, Xie Chen, Zhuotao Tian, Bowen Xing...
- **链接**: [https://arxiv.org/abs/2604.20090v1](https://arxiv.org/abs/2604.20090v1)
- **PDF**: [https://arxiv.org/pdf/2604.20090v1.pdf](https://arxiv.org/pdf/2604.20090v1.pdf)

**摘要**:

Cross-lingual chain-of-thought (XCoT) with self-consistency markedly enhances multilingual reasoning, yet existing methods remain costly due to extensive sampling of full trajectories across languages. Moreover, multilingual LLM representations vary strongly by language, hindering direct feature comparisons and effective pruning. Motivated by this, we introduce UL-XCoT, the first efficient unified...

---

### 19. Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning

- **arXiv ID**: `2604.19459v1`
- **发布日期**: 2026-04-21
- **作者**: Kyuhee Kim, Auguste Poiroux, Antoine Bosselut
- **链接**: [https://arxiv.org/abs/2604.19459v1](https://arxiv.org/abs/2604.19459v1)
- **PDF**: [https://arxiv.org/pdf/2604.19459v1.pdf](https://arxiv.org/pdf/2604.19459v1.pdf)

**摘要**:

Formal verification guarantees proof validity but not formalization faithfulness. For natural-language logical reasoning, where models construct axiom systems from scratch without library constraints, this gap between valid proofs and faithful translations is especially acute. We investigate whether frontier models exploit this gap when generating Lean 4 proofs, a behavior we term formalization ga...

---

### 20. Understanding Password Preferences, Memorability, and Security through a Human-Centered Lens

- **arXiv ID**: `2604.19410v2`
- **发布日期**: 2026-04-21
- **作者**: Duru Paker, Suleyman Ozdel, Enkelejda Kasneci
- **链接**: [https://arxiv.org/abs/2604.19410v2](https://arxiv.org/abs/2604.19410v2)
- **PDF**: [https://arxiv.org/pdf/2604.19410v2.pdf](https://arxiv.org/pdf/2604.19410v2.pdf)

**摘要**:

Passwords remain the primary authentication method, yet user-created passwords are often the weakest due to the security-usability trade-off. Although AI-based password generators are emerging, little is known about their effectiveness and user perceptions. This eye-tracking study examined how behavior during password creation, selection, and memorization relates to objective and subjective passwo...

---

### 21. DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging

- **arXiv ID**: `2604.19305v1`
- **发布日期**: 2026-04-21
- **作者**: Linhao Wu, Yifei Pei, Zhen Yang, Kainan Li, Zhonghang Lu...
- **链接**: [https://arxiv.org/abs/2604.19305v1](https://arxiv.org/abs/2604.19305v1)
- **PDF**: [https://arxiv.org/pdf/2604.19305v1.pdf](https://arxiv.org/pdf/2604.19305v1.pdf)

**摘要**:

Automated Program Repair (APR) has benefited from the code understanding and generation capabilities of Large Language Models (LLMs). Existing feedback-based APR methods iteratively refine candidate patches using test execution feedback and have shown promising results. However, most rely on outcome-level failure symptoms, such as stack traces, which show how failures are observed but fail to expo...

---

### 22. ReflectMT: Internalizing Reflection for Efficient and High-Quality Machine Translation

- **arXiv ID**: `2604.19144v1`
- **发布日期**: 2026-04-21
- **作者**: Kunquan Li, Yingxue Zhang, Fandong Meng, Jinsong Su
- **链接**: [https://arxiv.org/abs/2604.19144v1](https://arxiv.org/abs/2604.19144v1)
- **PDF**: [https://arxiv.org/pdf/2604.19144v1.pdf](https://arxiv.org/pdf/2604.19144v1.pdf)

**摘要**:

Recent years have witnessed growing interest in applying Large Reasoning Models (LRMs) to Machine Translation (MT). Existing approaches predominantly adopt a "think-first-then-translate" paradigm. Although explicit reasoning trajectories significantly enhance translation quality, they incur prohibitive inference costs and latency. To address these limitations, we propose ReflectMT, a two-stage ref...

---

### 23. The Rise of Verbal Tics in Large Language Models: A Systematic Analysis Across Frontier Models

- **arXiv ID**: `2604.19139v2`
- **发布日期**: 2026-04-21
- **作者**: Shuai Wu, Xue Li, Yanna Feng, Yufang Li, Zhijun Wang...
- **链接**: [https://arxiv.org/abs/2604.19139v2](https://arxiv.org/abs/2604.19139v2)
- **PDF**: [https://arxiv.org/pdf/2604.19139v2.pdf](https://arxiv.org/pdf/2604.19139v2.pdf)

**摘要**:

As Large Language Models (LLMs) continue to evolve through alignment techniques such as Reinforcement Learning from Human Feedback (RLHF) and Constitutional AI, a growing and increasingly conspicuous phenomenon has emerged: the proliferation of verbal tics, repetitive, formulaic linguistic patterns that pervade model outputs. These range from sycophantic openers (That's a great question!, Awesome!...

---

### 24. AlignCultura: Towards Culturally Aligned Large Language Models?

- **arXiv ID**: `2604.19016v1`
- **发布日期**: 2026-04-21
- **作者**: Gautam Siddharth Kashyap, Mark Dras, Usman Naseem
- **链接**: [https://arxiv.org/abs/2604.19016v1](https://arxiv.org/abs/2604.19016v1)
- **PDF**: [https://arxiv.org/pdf/2604.19016v1.pdf](https://arxiv.org/pdf/2604.19016v1.pdf)

**摘要**:

Cultural alignment in Large Language Models (LLMs) is essential for producing contextually aware, respectful, and trustworthy outputs. Without it, models risk generating stereotyped, insensitive, or misleading responses that fail to reflect cultural diversity w.r.t Helpful, Harmless, and Honest (HHH) paradigm. Existing benchmarks represent early steps toward cultural alignment; yet, no benchmarks ...

---

### 25. Assessing Capabilities of Large Language Models in Social Media Analytics: A Multi-task Quest

- **arXiv ID**: `2604.18955v1`
- **发布日期**: 2026-04-21
- **作者**: Ramtin Davoudi, Kartik Thakkar, Nazanin Donyapour, Tyler Derr, Hamid Karimi
- **链接**: [https://arxiv.org/abs/2604.18955v1](https://arxiv.org/abs/2604.18955v1)
- **PDF**: [https://arxiv.org/pdf/2604.18955v1.pdf](https://arxiv.org/pdf/2604.18955v1.pdf)

**摘要**:

In this study, we present the first comprehensive evaluation of modern LLMs - including GPT-4, GPT-4o, GPT-3.5-Turbo, Gemini 1.5 Pro, DeepSeek-V3, Llama 3.2, and BERT - across three core social media analytics tasks on a Twitter (X) dataset: (I) Social Media Authorship Verification, (II) Social Media Post Generation, and (III) User Attribute Inference. For the authorship verification, we introduce...

---

### 26. MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval

- **arXiv ID**: `2604.18584v1`
- **发布日期**: 2026-04-20
- **作者**: Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei...
- **链接**: [https://arxiv.org/abs/2604.18584v1](https://arxiv.org/abs/2604.18584v1)
- **PDF**: [https://arxiv.org/pdf/2604.18584v1.pdf](https://arxiv.org/pdf/2604.18584v1.pdf)

**摘要**:

Mathematical problem solving remains a challenging test of reasoning for large language and multimodal models, yet existing benchmarks are limited in size, language coverage, and task diversity. We introduce MathNet, a high-quality, large-scale, multimodal, and multilingual dataset of Olympiad-level math problems together with a benchmark for evaluating mathematical reasoning in generative models ...

---

### 27. From Program Slices to Causal Clarity: Evaluating Faithful, Actionable LLM-Generated Failure Explanations via Context Partitioning and LLM-as-a-Judge

- **arXiv ID**: `2604.18309v1`
- **发布日期**: 2026-04-20
- **作者**: Julius Porbeck, Christian Medeiros Adriano, Holger Giese
- **链接**: [https://arxiv.org/abs/2604.18309v1](https://arxiv.org/abs/2604.18309v1)
- **PDF**: [https://arxiv.org/pdf/2604.18309v1.pdf](https://arxiv.org/pdf/2604.18309v1.pdf)

**摘要**:

Large language model (LLM)-based debugging systems can generate failure explanations, but these explanations may be incomplete or incorrect. Misleading explanations are harmful for downstream tasks (e.g., bug triage, bug fixing). We investigate how explanation quality is affected by various LLM context configurations. Existing work predominantly treats LLM-generated failure explanations as an ad h...

---

### 28. First, Do No Harm (With LLMs): Mitigating Racial Bias via Agentic Workflows

- **arXiv ID**: `2604.18038v1`
- **发布日期**: 2026-04-20
- **作者**: Sihao Xing, Zaur Gouliev
- **链接**: [https://arxiv.org/abs/2604.18038v1](https://arxiv.org/abs/2604.18038v1)
- **PDF**: [https://arxiv.org/pdf/2604.18038v1.pdf](https://arxiv.org/pdf/2604.18038v1.pdf)

**摘要**:

Large language models (LLMs) are increasingly used in clinical settings, raising concerns about racial bias in both generated medical text and clinical reasoning. Existing studies have identified bias in medical LLMs, but many focus on single models and give less attention to mitigation. This study uses the EU AI Act as a governance lens to evaluate five widely used LLMs across two tasks, namely s...

---

### 29. CodePivot: Bootstrapping Multilingual Transpilation in LLMs via Reinforcement Learning without Parallel Corpora

- **arXiv ID**: `2604.18027v1`
- **发布日期**: 2026-04-20
- **作者**: Shangyu Li, Juyong Jiang, Meibo Ren, Sizhe Zhong, Huiri Tan...
- **链接**: [https://arxiv.org/abs/2604.18027v1](https://arxiv.org/abs/2604.18027v1)
- **PDF**: [https://arxiv.org/pdf/2604.18027v1.pdf](https://arxiv.org/pdf/2604.18027v1.pdf)

**摘要**:

Transpilation, or code translation, aims to convert source code from one programming language (PL) to another. It is beneficial for many downstream applications, from modernizing large legacy codebases to augmenting data for low-resource PLs. Recent large language model (LLM)-based approaches have demonstrated immense potential for code translation. Among these approaches, training-based methods a...

---

### 30. Employing General-Purpose and Biomedical Large Language Models with Advanced Prompt Engineering for Pharmacoepidemiologic Study Design

- **arXiv ID**: `2604.17988v1`
- **发布日期**: 2026-04-20
- **作者**: Xinyao Zhang, Nicole Sonne Heckmann, Manuela Del Castillo Suero, Francesco Paolo Speca, Maurizio Sessa
- **链接**: [https://arxiv.org/abs/2604.17988v1](https://arxiv.org/abs/2604.17988v1)
- **PDF**: [https://arxiv.org/pdf/2604.17988v1.pdf](https://arxiv.org/pdf/2604.17988v1.pdf)

**摘要**:

Background: The potential of large language models (LLMs) to automate and support pharmacoepidemiologic study design is an emerging area of interest, yet their reliability remains insufficiently characterized. General-purpose LLMs often display inaccuracies, while the comparative performance of specialized biomedical LLMs in this domain remains unknown. Methods: This study evaluated general-purpos...

---

### 31. Concurrent Criterion Validation of a Validity Screen for LLM Confidence Signals via Selective Prediction

- **arXiv ID**: `2604.17716v1`
- **发布日期**: 2026-04-20
- **作者**: Jon-Paul Cacioli
- **链接**: [https://arxiv.org/abs/2604.17716v1](https://arxiv.org/abs/2604.17716v1)
- **PDF**: [https://arxiv.org/pdf/2604.17716v1.pdf](https://arxiv.org/pdf/2604.17716v1.pdf)

**摘要**:

The validity screen (Cacioli, 2026d, 2026e) classifies LLM confidence signals as Valid, Indeterminate, or Invalid. We test whether these classifications predict selective prediction performance. Twenty frontier LLMs from seven families were evaluated on 524 items across six cognitive tracks. Valid models show mean Type 2 AUROC = .624 (SD = .048). Invalid models show mean AUROC = .357 (SD = .231). ...

---

### 32. PsychBench: Auditing Epidemiological Fidelity in Large Language Model Mental Health Simulations

- **arXiv ID**: `2604.17359v1`
- **发布日期**: 2026-04-19
- **作者**: Patrick Keough
- **链接**: [https://arxiv.org/abs/2604.17359v1](https://arxiv.org/abs/2604.17359v1)
- **PDF**: [https://arxiv.org/pdf/2604.17359v1.pdf](https://arxiv.org/pdf/2604.17359v1.pdf)

**摘要**:

Large language models are increasingly deployed to simulate patients for clinical training, research, and mental health tools, yet population-level validity remains largely untested. We introduce PsychBench, the first epidemiological audit of LLM patient simulation: 28,800 profiles from four frontier models (GPT-4o-mini, DeepSeek-V3, Gemini-3-Flash, GLM-4.7) evaluated against NHANES and NESARC-III...

---

### 33. Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?

- **arXiv ID**: `2604.17338v2`
- **发布日期**: 2026-04-19
- **作者**: Wang Bill Zhu, Miaosen Chai, Shangshang Wang, Yejia Liu, Song Bian...
- **链接**: [https://arxiv.org/abs/2604.17338v2](https://arxiv.org/abs/2604.17338v2)
- **PDF**: [https://arxiv.org/pdf/2604.17338v2.pdf](https://arxiv.org/pdf/2604.17338v2.pdf)

**摘要**:

Unlike code completion, debugging requires localizing faults and applying targeted edits. We observe that frontier LLMs often regenerate correct but over-edited solutions during debugging. To evaluate how far LLMs are from precise debugging, we introduce the Precise Debugging Benchmark (PDB) framework, which automatically converts any coding dataset into a debugging benchmark with precision-aware ...

---

### 34. Dynamics of Cognitive Heterogeneity: Investigating Behavioral Biases in Multi-Stage Supply Chains with LLM-Based Simulation

- **arXiv ID**: `2604.17220v1`
- **发布日期**: 2026-04-19
- **作者**: Jiuyun Jiang, Yuecheng Hong, Bo Yang, Jin Yang, Guangxin Jiang...
- **链接**: [https://arxiv.org/abs/2604.17220v1](https://arxiv.org/abs/2604.17220v1)
- **PDF**: [https://arxiv.org/pdf/2604.17220v1.pdf](https://arxiv.org/pdf/2604.17220v1.pdf)

**摘要**:

Modeling coordination among generative agents in complex multi-round decision-making presents a core challenge for AI and operations management. Although behavioral experiments have revealed cognitive biases behind supply chain inefficiencies, traditional methods face scalability and control limitations. We introduce a scalable experimental paradigm using Large Language Models (LLMs) to simulate m...

---

### 35. React-ing to Grace Hopper 200: Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend

- **arXiv ID**: `2604.17187v1`
- **发布日期**: 2026-04-19
- **作者**: Alex Potanin
- **链接**: [https://arxiv.org/abs/2604.17187v1](https://arxiv.org/abs/2604.17187v1)
- **PDF**: [https://arxiv.org/pdf/2604.17187v1.pdf](https://arxiv.org/pdf/2604.17187v1.pdf)

**摘要**:

We evaluate five state-of-the-art open-weights coding language models -- Kimi-K2.5 (at Q3 and Q4 quantizations), GLM-5.1, Qwen3-Coder-480B, and DeepSeek-V3.2 -- on a single multi-file React Native application generation task on NVIDIA GH200 576 GB hardware. The task specifies authentication, per-user per-day counting, and web compatibility, and is evaluated on whether the generated project runs ou...

---

### 36. Abstain-R1: Calibrated Abstention and Post-Refusal Clarification via Verifiable RL

- **arXiv ID**: `2604.17073v1`
- **发布日期**: 2026-04-18
- **作者**: Skylar Zhai, Jingcheng Liang, Dongyeop Kang
- **链接**: [https://arxiv.org/abs/2604.17073v1](https://arxiv.org/abs/2604.17073v1)
- **PDF**: [https://arxiv.org/pdf/2604.17073v1.pdf](https://arxiv.org/pdf/2604.17073v1.pdf)

**摘要**:

Reinforcement fine-tuning improves the reasoning ability of large language models, but it can also encourage them to answer unanswerable queries by guessing or hallucinating missing information. Existing abstention methods either train models to produce generic refusals or encourage follow-up clarifications without verifying whether those clarifications identify the key missing information. We stu...

---

### 37. HELO-APR: Enhancing Low-Resource Program Repair through Cross-Lingual Knowledge Transfer

- **arXiv ID**: `2604.17016v1`
- **发布日期**: 2026-04-18
- **作者**: Zhipeng Wang, Boyang Yang, Yidong Wan, Liuye Guo, You Lv...
- **链接**: [https://arxiv.org/abs/2604.17016v1](https://arxiv.org/abs/2604.17016v1)
- **PDF**: [https://arxiv.org/pdf/2604.17016v1.pdf](https://arxiv.org/pdf/2604.17016v1.pdf)

**摘要**:

Large Language Models (LLMs) perform well on automatic program repair (APR) for high-resource programming languages (HRPLs), but their effectiveness drops sharply in low-resource programming languages (LRPLs), due to a lack of sufficient verified buggy-fixed pairs for APR training. To address this challenge, we propose HELO-APR (High-resource Enabled LOw-resource APR), a two-stage APR framework th...

---

### 38. Do Large Language Models know Which Published Articles have been Retracted?

- **arXiv ID**: `2604.16872v1`
- **发布日期**: 2026-04-18
- **作者**: Mike Thelwall
- **链接**: [https://arxiv.org/abs/2604.16872v1](https://arxiv.org/abs/2604.16872v1)
- **PDF**: [https://arxiv.org/pdf/2604.16872v1.pdf](https://arxiv.org/pdf/2604.16872v1.pdf)

**摘要**:

Large Language Models (LLMs) can be helpful for literature search and summarisation, but retracted articles can confuse them. This article asks three open weights (offline) LLMs whether 161 high profile retracted articles had been retracted, performing a similar check for a benchmark multidisciplinary set of 34,070 non-retracted articles. Based on titles and abstracts, in over 80% of cases the LLM...

---

### 39. No Universal Courtesy: A Cross-Linguistic, Multi-Model Study of Politeness Effects on LLMs Using the PLUM Corpus

- **arXiv ID**: `2604.16275v1`
- **发布日期**: 2026-04-17
- **作者**: Hitesh Mehta, Arjit Saxena, Garima Chhikara, Rohit Kumar
- **链接**: [https://arxiv.org/abs/2604.16275v1](https://arxiv.org/abs/2604.16275v1)
- **PDF**: [https://arxiv.org/pdf/2604.16275v1.pdf](https://arxiv.org/pdf/2604.16275v1.pdf)

**摘要**:

This paper explores the response of Large Language Models (LLMs) to user prompts with different degrees of politeness and impoliteness. The Politeness Theory by Brown and Levinson and the Impoliteness Framework by Culpeper form the basis of experiments conducted across three languages (English, Hindi, Spanish), five models (Gemini-Pro, GPT-4o Mini, Claude 3.7 Sonnet, DeepSeek-Chat, and Llama 3), a...

---

### 40. CIMple: Standard-cell SRAM-based CIM with LUT-based split softmax for attention acceleration

- **arXiv ID**: `2604.15944v2`
- **发布日期**: 2026-04-17
- **作者**: Bas Ahn, Xingjian Tao, Manil Dev Gomony, Marc Geilen, Henk Corporaal
- **链接**: [https://arxiv.org/abs/2604.15944v2](https://arxiv.org/abs/2604.15944v2)
- **PDF**: [https://arxiv.org/pdf/2604.15944v2.pdf](https://arxiv.org/pdf/2604.15944v2.pdf)

**摘要**:

Large Language Models (LLMs) such as LLaMA and DeepSeek, are built on transformer architectures, which have become a standard model for achieving state-of-the-art performance in natural language processing tasks. Recently, there has been growing interest in deploying LLMs on edge devices. Although smaller LLM models are being proposed, they often still contain billions of parameters. Since edge de...

---

### 41. Reasoning-targeted Jailbreak Attacks on Large Reasoning Models via Semantic Triggers and Psychological Framing

- **arXiv ID**: `2604.15725v1`
- **发布日期**: 2026-04-17
- **作者**: Zehao Wang, Lanjun Wang
- **链接**: [https://arxiv.org/abs/2604.15725v1](https://arxiv.org/abs/2604.15725v1)
- **PDF**: [https://arxiv.org/pdf/2604.15725v1.pdf](https://arxiv.org/pdf/2604.15725v1.pdf)

**摘要**:

Large Reasoning Models (LRMs) have demonstrated strong capabilities in generating step-by-step reasoning chains alongside final answers, enabling their deployment in high-stakes domains such as healthcare and education. While prior jailbreak attack studies have focused on the safety of final answers, little attention has been given to the safety of the reasoning process. In this work, we identify ...

---

### 42. Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization

- **arXiv ID**: `2604.14853v1`
- **发布日期**: 2026-04-16
- **作者**: Zhiyuan Zhai, Bingcong Li, Bingnan Xiao, Ming Li, Xin Wang
- **链接**: [https://arxiv.org/abs/2604.14853v1](https://arxiv.org/abs/2604.14853v1)
- **PDF**: [https://arxiv.org/pdf/2604.14853v1.pdf](https://arxiv.org/pdf/2604.14853v1.pdf)

**摘要**:

Test-time compute scaling, the practice of spending extra computation during inference via repeated sampling, search, or extended reasoning, has become a powerful lever for improving large language model performance. Yet deploying these techniques under finite inference budgets requires a decision that current systems largely ignore: which inputs deserve more compute, and which can be answered che...

---

### 43. When PCOS Meets Eating Disorders: An Explainable AI Approach to Detecting the Hidden Triple Burden

- **arXiv ID**: `2604.14356v1`
- **发布日期**: 2026-04-15
- **作者**: Apoorv Prasad, Susan McRoy
- **链接**: [https://arxiv.org/abs/2604.14356v1](https://arxiv.org/abs/2604.14356v1)
- **PDF**: [https://arxiv.org/pdf/2604.14356v1.pdf](https://arxiv.org/pdf/2604.14356v1.pdf)

**摘要**:

Women with polycystic ovary syndrome (PCOS) face substantially elevated risks of body image distress, disordered eating, and metabolic challenges, yet existing natural language processing approaches for detecting these conditions lack transparency and cannot identify co-occurring presentations. We developed small, open-source language models to automatically detect this triple burden in social med...

---

### 44. Mamba-SSM with LLM Reasoning for Feature Selection: Faithfulness-Aware Biomarker Discovery

- **arXiv ID**: `2604.14334v2`
- **发布日期**: 2026-04-15
- **作者**: Pushpa Kumar Balan, Aijing Feng
- **链接**: [https://arxiv.org/abs/2604.14334v2](https://arxiv.org/abs/2604.14334v2)
- **PDF**: [https://arxiv.org/pdf/2604.14334v2.pdf](https://arxiv.org/pdf/2604.14334v2.pdf)

**摘要**:

Gradient saliency from deep sequence models surfaces candidate biomarkers efficiently, but the resulting gene lists can be contaminated by tissue-composition confounders that degrade downstream classifiers. We study whether LLM chain-of-thought (CoT) reasoning can filter these confounders, and whether reasoning quality is associated with downstream performance. We train a Mamba SSM on TCGA-BRCA RN...

---

### 45. ReviewGrounder: Improving Review Substantiveness with Rubric-Guided, Tool-Integrated Agents

- **arXiv ID**: `2604.14261v1`
- **发布日期**: 2026-04-15
- **作者**: Zhuofeng Li, Yi Lu, Dongfu Jiang, Haoxiang Zhang, Yuyang Bai...
- **链接**: [https://arxiv.org/abs/2604.14261v1](https://arxiv.org/abs/2604.14261v1)
- **PDF**: [https://arxiv.org/pdf/2604.14261v1.pdf](https://arxiv.org/pdf/2604.14261v1.pdf)

**摘要**:

The rapid rise in AI conference submissions has driven increasing exploration of large language models (LLMs) for peer review support. However, LLM-based reviewers often generate superficial, formulaic comments lacking substantive, evidence-grounded feedback. We attribute this to the underutilization of two key components of human reviewing: explicit rubrics and contextual grounding in existing wo...

---

### 46. IndicDB -- Benchmarking Multilingual Text-to-SQL Capabilities in Indian Languages

- **arXiv ID**: `2604.13686v1`
- **发布日期**: 2026-04-15
- **作者**: Aviral Dawar, Roshan Karanth, Vikram Goyal, Dhruv Kumar
- **链接**: [https://arxiv.org/abs/2604.13686v1](https://arxiv.org/abs/2604.13686v1)
- **PDF**: [https://arxiv.org/pdf/2604.13686v1.pdf](https://arxiv.org/pdf/2604.13686v1.pdf)

**摘要**:

While Large Language Models (LLMs) have significantly advanced Text-to-SQL performance, existing benchmarks predominantly focus on Western contexts and simplified schemas, leaving a gap in real-world, non-Western applications. We present IndicDB, a multilingual Text-to-SQL benchmark for evaluating cross-lingual semantic parsing across diverse Indic languages. The relational schemas are sourced fro...

---

### 47. IDEA: An Interpretable and Editable Decision-Making Framework for LLMs via Verbal-to-Numeric Calibration

- **arXiv ID**: `2604.12573v1`
- **发布日期**: 2026-04-14
- **作者**: Yanji He, Yuxin Jiang, Yiwen Wu, Bo Huang, Jiaheng Wei...
- **链接**: [https://arxiv.org/abs/2604.12573v1](https://arxiv.org/abs/2604.12573v1)
- **PDF**: [https://arxiv.org/pdf/2604.12573v1.pdf](https://arxiv.org/pdf/2604.12573v1.pdf)

**摘要**:

Large Language Models are increasingly deployed for decision-making, yet their adoption in high-stakes domains remains limited by miscalibrated probabilities, unfaithful explanations, and inability to incorporate expert knowledge precisely. We propose IDEA, a framework that extracts LLM decision knowledge into an interpretable parametric model over semantically meaningful factors. Through joint le...

---

### 48. DeepSeek Robustness Against Semantic-Character Dual-Space Mutated Prompt Injection

- **arXiv ID**: `2604.12548v1`
- **发布日期**: 2026-04-14
- **作者**: Junyu Ren, Xingjian Pan, Wensheng Gan, Philip S. Yu
- **链接**: [https://arxiv.org/abs/2604.12548v1](https://arxiv.org/abs/2604.12548v1)
- **PDF**: [https://arxiv.org/pdf/2604.12548v1.pdf](https://arxiv.org/pdf/2604.12548v1.pdf)

**摘要**:

Prompt injection has emerged as a critical security threat to large language models (LLMs), yet existing studies predominantly focus on single-dimensional attack strategies, such as semantic rewriting or character-level obfuscation, which fail to capture the combined effects of multi-space perturbations in realistic scenarios. In addition, systematic black-box robustness evaluations of recent Chin...

---

### 49. Beyond Single-Dimension Novelty: How Combinations of Theory, Method, and Results-based Novelty Shape Scientific Impact

- **arXiv ID**: `2604.12471v1`
- **发布日期**: 2026-04-14
- **作者**: Yi Zhao, Yang Chenggang, Yuzhuo Wang, Tong Bao, Zhang Heng...
- **链接**: [https://arxiv.org/abs/2604.12471v1](https://arxiv.org/abs/2604.12471v1)
- **PDF**: [https://arxiv.org/pdf/2604.12471v1.pdf](https://arxiv.org/pdf/2604.12471v1.pdf)

**摘要**:

Scientific novelty drives advances at the research frontier, yet it is also associated with heightened uncertainty and potential resistance from incumbent paradigms, leading to complex patterns of scientific impact. Prior studies have primarily ex-amined the relationship between a single dimension of novelty -- such as theoreti-cal, methodological, or results-based novelty -- and scientific impact...

---

### 50. Cooperative Memory Paging with Keyword Bookmarks for Long-Horizon LLM Conversations

- **arXiv ID**: `2604.12376v1`
- **发布日期**: 2026-04-14
- **作者**: Ziyang Liu
- **链接**: [https://arxiv.org/abs/2604.12376v1](https://arxiv.org/abs/2604.12376v1)
- **PDF**: [https://arxiv.org/pdf/2604.12376v1.pdf](https://arxiv.org/pdf/2604.12376v1.pdf)

**摘要**:

When LLM conversations grow beyond the context window, old content must be evicted -- but how does the model recover it when needed? We propose cooperative paging: evicted segments are replaced with minimal keyword bookmarks ([pN:keywords], ~8-24 tokens each), and the model is given a recall() tool to retrieve full content on demand. On the LoCoMo benchmark (10 real multi-session conversations, 30...

---

### 51. Narrative over Numbers: The Identifiable Victim Effect and its Amplification Under Alignment and Reasoning in Large Language Models

- **arXiv ID**: `2604.12076v1`
- **发布日期**: 2026-04-13
- **作者**: Syed Rifat Raiyan
- **链接**: [https://arxiv.org/abs/2604.12076v1](https://arxiv.org/abs/2604.12076v1)
- **PDF**: [https://arxiv.org/pdf/2604.12076v1.pdf](https://arxiv.org/pdf/2604.12076v1.pdf)

**摘要**:

The Identifiable Victim Effect (IVE) $-$ the tendency to allocate greater resources to a specific, narratively described victim than to a statistically characterized group facing equivalent hardship $-$ is one of the most robust findings in moral psychology and behavioural economics. As large language models (LLMs) assume consequential roles in humanitarian triage, automated grant evaluation, and ...

---

### 52. NL2SQLBench: A Modular Benchmarking Framework for LLM-Enabled NL2SQL Solutions

- **arXiv ID**: `2604.16493v1`
- **发布日期**: 2026-04-13
- **作者**: Shizheng Hou, Wenqi Pei, Nuo Chen, Quang-Trung Ta, Peng Lu...
- **链接**: [https://arxiv.org/abs/2604.16493v1](https://arxiv.org/abs/2604.16493v1)
- **PDF**: [https://arxiv.org/pdf/2604.16493v1.pdf](https://arxiv.org/pdf/2604.16493v1.pdf)

**摘要**:

Natural Language to SQL (NL2SQL) technology empowers non-expert users to query relational databases without requiring SQL expertise. While large language models (LLMs) have greatly improved NL2SQL algorithms, their rapid development outpaces systematic evaluation, leaving a critical gap in understanding their effectiveness, efficiency, and limitations. To this end, we present NL2SQLBench, the firs...

---

### 53. Solving Physics Olympiad via Reinforcement Learning on Physics Simulators

- **arXiv ID**: `2604.11805v1`
- **发布日期**: 2026-04-13
- **作者**: Mihir Prabhudesai, Aryan Satpathy, Yangmin Li, Zheyang Qin, Nikash Bhardwaj...
- **链接**: [https://arxiv.org/abs/2604.11805v1](https://arxiv.org/abs/2604.11805v1)
- **PDF**: [https://arxiv.org/pdf/2604.11805v1.pdf](https://arxiv.org/pdf/2604.11805v1.pdf)

**摘要**:

We have witnessed remarkable advances in LLM reasoning capabilities with the advent of DeepSeek-R1. However, much of this progress has been fueled by the abundance of internet question-answer (QA) pairs, a major bottleneck going forward, since such data is limited in scale and concentrated mainly in domains like mathematics. In contrast, other sciences such as physics lack large-scale QA datasets ...

---

### 54. Persona Non Grata: Single-Method Safety Evaluation Is Incomplete for Persona-Imbued LLMs

- **arXiv ID**: `2604.11120v2`
- **发布日期**: 2026-04-13
- **作者**: Wenkai Li, Fan Yang, Shaunak A. Mehta, Koichi Onoue
- **链接**: [https://arxiv.org/abs/2604.11120v2](https://arxiv.org/abs/2604.11120v2)
- **PDF**: [https://arxiv.org/pdf/2604.11120v2.pdf](https://arxiv.org/pdf/2604.11120v2.pdf)

**摘要**:

Personality imbuing customizes LLM behavior, but safety evaluations almost always study prompt-based personas alone. We show this is incomplete: prompting and activation steering expose *different*, architecture-dependent vulnerability profiles, and testing with only one method can miss a model's dominant failure mode. Across 5,568 judged conditions on four standard models from three architecture ...

---

### 55. CARO: Chain-of-Analogy Reasoning Optimization for Robust Content Moderation

- **arXiv ID**: `2604.10504v1`
- **发布日期**: 2026-04-12
- **作者**: Bingzhe Wu, Haotian Lu, Yuchen Mou
- **链接**: [https://arxiv.org/abs/2604.10504v1](https://arxiv.org/abs/2604.10504v1)
- **PDF**: [https://arxiv.org/pdf/2604.10504v1.pdf](https://arxiv.org/pdf/2604.10504v1.pdf)

**摘要**:

Current large language models (LLMs), even those explicitly trained for reasoning, often struggle with ambiguous content moderation cases due to misleading "decision shortcuts" embedded in context. Inspired by cognitive psychology insights into expert moderation, we introduce \caro (Chain-of-Analogy Reasoning Optimization), a novel two-stage training framework to induce robust analogical reasoning...

---

### 56. Leveraging Mathematical Reasoning of LLMs for Efficient GPU Thread Mapping

- **arXiv ID**: `2604.10387v2`
- **发布日期**: 2026-04-12
- **作者**: Jose Maureira, Cristóbal A. Navarro, Hector Ferrada, Luis Veas-Castillo
- **链接**: [https://arxiv.org/abs/2604.10387v2](https://arxiv.org/abs/2604.10387v2)
- **PDF**: [https://arxiv.org/pdf/2604.10387v2.pdf](https://arxiv.org/pdf/2604.10387v2.pdf)

**摘要**:

Mapping parallel threads onto non-box-shaped domains is a known challenge in GPU computing; efficient mapping prevents performance penalties from unnecessary resource allocation. Currently, achieving this requires significant analytical human effort to manually derive bespoke mapping functions for each geometry. This work introduces a novel approach leveraging the symbolic reasoning of Large Langu...

---

### 57. Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities

- **arXiv ID**: `2604.10135v2`
- **发布日期**: 2026-04-11
- **作者**: Zhichen Liu, Yongyuan Li, Yang Xu
- **链接**: [https://arxiv.org/abs/2604.10135v2](https://arxiv.org/abs/2604.10135v2)
- **PDF**: [https://arxiv.org/pdf/2604.10135v2.pdf](https://arxiv.org/pdf/2604.10135v2.pdf)

**摘要**:

Researchers have explored different ways to improve large language models (LLMs)' capabilities via dummy token insertion in contexts. However, existing works focus solely on the dummy tokens themselves, but fail to leverage the inherent sentence-level structure of natural language. This is a critical oversight, as LLMs acquire linguistic capabilities through exposure to human-generated texts, whic...

---

### 58. Conflicts Make Large Reasoning Models Vulnerable to Attacks

- **arXiv ID**: `2604.09750v1`
- **发布日期**: 2026-04-10
- **作者**: Honghao Liu, Chengjin Xu, Xuhui Jiang, Cehao Yang, Shengming Yin...
- **链接**: [https://arxiv.org/abs/2604.09750v1](https://arxiv.org/abs/2604.09750v1)
- **PDF**: [https://arxiv.org/pdf/2604.09750v1.pdf](https://arxiv.org/pdf/2604.09750v1.pdf)

**摘要**:

Large Reasoning Models (LRMs) have achieved remarkable performance across diverse domains, yet their decision-making under conflicting objectives remains insufficiently understood. This work investigates how LRMs respond to harmful queries when confronted with two categories of conflicts: internal conflicts that pit alignment values against each other and dilemmas, which impose mutually contradict...

---

### 59. SMART: When is it Actually Worth Expanding a Speculative Tree?

- **arXiv ID**: `2604.09731v1`
- **发布日期**: 2026-04-09
- **作者**: Lifu Wang, Pan Zhou
- **链接**: [https://arxiv.org/abs/2604.09731v1](https://arxiv.org/abs/2604.09731v1)
- **PDF**: [https://arxiv.org/pdf/2604.09731v1.pdf](https://arxiv.org/pdf/2604.09731v1.pdf)

**摘要**:

Tree-based speculative decoding accelerates autoregressive generation by verifying a branching tree of draft tokens in a single target-model forward pass. However, existing methods prioritize maximizing token-level likelihood or the number of accepted tokens while ignoring a critical ``efficiency paradox'': the computational overhead of drafting and verifying big trees can grow super-linearly, par...

---

### 60. ImplicitMemBench: Measuring Unconscious Behavioral Adaptation in Large Language Models

- **arXiv ID**: `2604.08064v2`
- **发布日期**: 2026-04-09
- **作者**: Chonghan Qin, Xiachong Feng, Weitao Ma, Xiaocheng Feng, Lingpeng Kong
- **链接**: [https://arxiv.org/abs/2604.08064v2](https://arxiv.org/abs/2604.08064v2)
- **PDF**: [https://arxiv.org/pdf/2604.08064v2.pdf](https://arxiv.org/pdf/2604.08064v2.pdf)

**摘要**:

Existing memory benchmarks for LLM agents evaluate explicit recall of facts, yet overlook implicit memory where experience becomes automated behavior without conscious retrieval. This gap is critical: effective assistants must automatically apply learned procedures or avoid failed actions without explicit reminders. We introduce ImplicitMemBench, the first systematic benchmark evaluating implicit ...

---

### 61. From Debate to Decision: Conformal Social Choice for Safe Multi-Agent Deliberation

- **arXiv ID**: `2604.07667v1`
- **发布日期**: 2026-04-09
- **作者**: Mengdie Flora Wang, Haochen Xie, Guanghui Wang, Aijing Gao, Guang Yang...
- **链接**: [https://arxiv.org/abs/2604.07667v1](https://arxiv.org/abs/2604.07667v1)
- **PDF**: [https://arxiv.org/pdf/2604.07667v1.pdf](https://arxiv.org/pdf/2604.07667v1.pdf)

**摘要**:

Multi-agent debate improves LLM reasoning, yet agreement among agents is not evidence of correctness. When agents converge on a wrong answer through social reinforcement, consensus-based stopping commits that error to an automated action with no recourse. We introduce Conformal Social Choice, a post-hoc decision layer that converts debate outputs into calibrated act-versus-escalate decisions. Verb...

---

### 62. From Business Events to Auditable Decisions: Ontology-Governed Graph Simulation for Enterprise AI

- **arXiv ID**: `2604.08603v1`
- **发布日期**: 2026-04-08
- **作者**: Hongyin Zhu, Jinming Liang, Mengjun Hou, Ruifan Tang, Xianbin Zhu...
- **链接**: [https://arxiv.org/abs/2604.08603v1](https://arxiv.org/abs/2604.08603v1)
- **PDF**: [https://arxiv.org/pdf/2604.08603v1.pdf](https://arxiv.org/pdf/2604.08603v1.pdf)

**摘要**:

Existing LLM-based agent systems share a common architectural failure: they answer from the unrestricted knowledge space without first simulating how active business scenarios reshape that space for the event at hand -- producing decisions that are fluent but ungrounded and carrying no audit trail. We present LOM-action, which equips enterprise AI with \emph{event-driven ontology simulation}: busi...

---

### 63. Yale-DM-Lab at ArchEHR-QA 2026: Deterministic Grounding and Multi-Pass Evidence Alignment for EHR Question Answering

- **arXiv ID**: `2604.07116v1`
- **发布日期**: 2026-04-08
- **作者**: Elyas Irankhah, Samah Fodeh
- **链接**: [https://arxiv.org/abs/2604.07116v1](https://arxiv.org/abs/2604.07116v1)
- **PDF**: [https://arxiv.org/pdf/2604.07116v1.pdf](https://arxiv.org/pdf/2604.07116v1.pdf)

**摘要**:

We describe the Yale-DM-Lab system for the ArchEHR-QA 2026 shared task. The task studies patient-authored questions about hospitalization records and contains four subtasks (ST): clinician-interpreted question reformulation, evidence sentence identification, answer generation, and evidence-answer alignment. ST1 uses a dual-model pipeline with Claude Sonnet 4 and GPT-4o to reformulate patient quest...

---

### 64. Strategic Persuasion with Trait-Conditioned Multi-Agent Systems for Iterative Legal Argumentation

- **arXiv ID**: `2604.07028v1`
- **发布日期**: 2026-04-08
- **作者**: Philipp D. Siedler
- **链接**: [https://arxiv.org/abs/2604.07028v1](https://arxiv.org/abs/2604.07028v1)
- **PDF**: [https://arxiv.org/pdf/2604.07028v1.pdf](https://arxiv.org/pdf/2604.07028v1.pdf)

**摘要**:

Strategic interaction in adversarial domains such as law, diplomacy, and negotiation is mediated by language, yet most game-theoretic models abstract away the mechanisms of persuasion that operate through discourse. We present the Strategic Courtroom Framework, a multi-agent simulation environment in which prosecution and defense teams composed of trait-conditioned Large Language Model (LLM) agent...

---

### 65. TRAPTI: Time-Resolved Analysis for SRAM Banking and Power Gating Optimization in Embedded Transformer Inference

- **arXiv ID**: `2604.06955v1`
- **发布日期**: 2026-04-08
- **作者**: Jan Klhufek, Alberto Marchisio, Vojtech Mrazek, Lukas Sekanina, Muhammad Shafique
- **链接**: [https://arxiv.org/abs/2604.06955v1](https://arxiv.org/abs/2604.06955v1)
- **PDF**: [https://arxiv.org/pdf/2604.06955v1.pdf](https://arxiv.org/pdf/2604.06955v1.pdf)

**摘要**:

Transformer neural networks achieve state-of-the-art accuracy across language and vision tasks, but their deployment on embedded hardware is hindered by stringent area, latency, and energy constraints. During inference, performance and efficiency are increasingly dominated by the Key--Value (KV) cache, whose memory footprint grows with sequence length, straining on-chip memory utilization. Althoug...

---

### 66. QED-Nano: Teaching a Tiny Model to Prove Hard Theorems

- **arXiv ID**: `2604.04898v1`
- **发布日期**: 2026-04-06
- **作者**:  LM-Provers, Yuxiao Qu, Amrith Setlur, Jasper Dekoninck, Edward Beeching...
- **链接**: [https://arxiv.org/abs/2604.04898v1](https://arxiv.org/abs/2604.04898v1)
- **PDF**: [https://arxiv.org/pdf/2604.04898v1.pdf](https://arxiv.org/pdf/2604.04898v1.pdf)

**摘要**:

Proprietary AI systems have recently demonstrated impressive capabilities on complex proof-based problems, with gold-level performance reported at the 2025 International Mathematical Olympiad (IMO). However, the training pipelines behind these systems remain largely undisclosed, and their reliance on large "internal" models and scaffolds makes them expensive to run, difficult to reproduce, and har...

---

### 67. Talk2AI: A Longitudinal Dataset of Human--AI Persuasive Conversations

- **arXiv ID**: `2604.04354v1`
- **发布日期**: 2026-04-06
- **作者**: Alexis Carrillo, Enrique Taietta, Ali Aghazadeh Ardebili, Giuseppe Alessandro Veltri, Massimo Stella
- **链接**: [https://arxiv.org/abs/2604.04354v1](https://arxiv.org/abs/2604.04354v1)
- **PDF**: [https://arxiv.org/pdf/2604.04354v1.pdf](https://arxiv.org/pdf/2604.04354v1.pdf)

**摘要**:

Talk2AI is a large-scale longitudinal dataset of 3,080 conversations (totaling 30,800 turns) between human participants and Large Language Models (LLMs), designed to support research on persuasion, opinion change, and human-AI interaction. The corpus was collected from 770 profiled Italian adults across four weekly sessions in Spring 2025, using a within-subject design in which each participant co...

---

### 68. FlatAttention: Dataflow and Fabric Collectives Co-Optimization for Large Attention-Based Model Inference on Tile-Based Accelerators

- **arXiv ID**: `2604.02110v1`
- **发布日期**: 2026-04-02
- **作者**: Chi Zhang, Luca Colagrande, Renzo Andri, Luca Benini
- **链接**: [https://arxiv.org/abs/2604.02110v1](https://arxiv.org/abs/2604.02110v1)
- **PDF**: [https://arxiv.org/pdf/2604.02110v1.pdf](https://arxiv.org/pdf/2604.02110v1.pdf)

**摘要**:

Attention accounts for an increasingly dominant fraction of total computation during inference for mixture-of-experts (MoE) models, making efficient acceleration critical. Emerging domain-specific accelerators for large model inference are shifting toward chip-scale and wafer-scale tile-based architectures. Tiles contain large matrix and vector engines and are connected through on-chip interconnec...

---

### 69. Cognitive Alignment Deciphered: A Self-Developed Scenario-Based Prompt Scale Coupled with Representational Similarity Analysis and Social Network Analysis for Unraveling Bias Mechanisms Across Humans and LLMs

- **arXiv ID**: `2604.22775v1`
- **发布日期**: 2026-04-01
- **作者**: Chengrui Zhou
- **链接**: [https://arxiv.org/abs/2604.22775v1](https://arxiv.org/abs/2604.22775v1)
- **PDF**: [https://arxiv.org/pdf/2604.22775v1.pdf](https://arxiv.org/pdf/2604.22775v1.pdf)

**摘要**:

Traditional cognitive bias measurement tools are limited by narrow bias coverage, low ecological validity, and reliance on abstract self reports, constraining scenario based and human AI comparisons. We introduce the context based Cognitive Bias Assessment Scale CBAS, a scenario driven prompt template covering 58 cognitive biases across five hot cold dual system dimensions: Calculation, Belief, In...

---

### 70. Adversarial Moral Stress Testing of Large Language Models

- **arXiv ID**: `2604.01108v1`
- **发布日期**: 2026-04-01
- **作者**: Saeid Jamshidi, Foutse Khomh, Arghavan Moradi Dakhel, Amin Nikanjam, Mohammad Hamdaqa...
- **链接**: [https://arxiv.org/abs/2604.01108v1](https://arxiv.org/abs/2604.01108v1)
- **PDF**: [https://arxiv.org/pdf/2604.01108v1.pdf](https://arxiv.org/pdf/2604.01108v1.pdf)

**摘要**:

Evaluating the ethical robustness of large language models (LLMs) deployed in software systems remains challenging, particularly under sustained adversarial user interaction. Existing safety benchmarks typically rely on single-round evaluations and aggregate metrics, such as toxicity scores and refusal rates, which offer limited visibility into behavioral instability that may arise during realisti...

---

### 71. STAR: Mitigating Cascading Errors in Spatial Reasoning via Turn-point Alignment and Segment-level DPO

- **arXiv ID**: `2604.00558v1`
- **发布日期**: 2026-04-01
- **作者**: Pukun Zhao, Longxiang Wang, Chen Chen, Peicheng Wang, Fanqing Zhou...
- **链接**: [https://arxiv.org/abs/2604.00558v1](https://arxiv.org/abs/2604.00558v1)
- **PDF**: [https://arxiv.org/pdf/2604.00558v1.pdf](https://arxiv.org/pdf/2604.00558v1.pdf)

**摘要**:

Structured spatial navigation is a core benchmark for Large Language Models (LLMs) spatial reasoning. Existing paradigms like Visualization-of-Thought (VoT) are prone to cascading errors in complex topologies. To solve this, we propose STAR, a two-stage framework grounded on topological anchors, and introduce the RedMaze-23K dataset with human-inspired turnpoint annotations. The first stage uses s...

---

### 72. Structured Intent as a Protocol-Like Communication Layer: Cross-Model Robustness, Framework Comparison, and the Weak-Model Compensation Effect

- **arXiv ID**: `2603.29953v1`
- **发布日期**: 2026-03-31
- **作者**: Peng Gang
- **链接**: [https://arxiv.org/abs/2603.29953v1](https://arxiv.org/abs/2603.29953v1)
- **PDF**: [https://arxiv.org/pdf/2603.29953v1.pdf](https://arxiv.org/pdf/2603.29953v1.pdf)

**摘要**:

How reliably can structured intent representations preserve user goals across different AI models, languages, and prompting frameworks? Prior work showed that PPS (Prompt Protocol Specification), a 5W3H-based structured intent framework, improves goal alignment in Chinese and generalizes to English and Japanese. This paper extends that line of inquiry in three directions: cross-model robustness ac...

---

### 73. Measuring the metacognition of AI

- **arXiv ID**: `2603.29693v2`
- **发布日期**: 2026-03-31
- **作者**: Richard Servajean, Philippe Servajean
- **链接**: [https://arxiv.org/abs/2603.29693v2](https://arxiv.org/abs/2603.29693v2)
- **PDF**: [https://arxiv.org/pdf/2603.29693v2.pdf](https://arxiv.org/pdf/2603.29693v2.pdf)

**摘要**:

A robust decision-making process must take into account uncertainty, especially when the choice involves inherent risks. Because artificial Intelligence (AI) systems are increasingly integrated into decision-making workflows, managing uncertainty relies more and more on the metacognitive capabilities of these systems; i.e, their ability to assess the reliability of and regulate their own decisions...

---

### 74. AI Cosplaying as Astrophysicists: A Controlled Synthetic-Agent Study of AI-Assisted Astrophysical Research Workflows

- **arXiv ID**: `2603.29039v1`
- **发布日期**: 2026-03-30
- **作者**: Chun Huang
- **链接**: [https://arxiv.org/abs/2603.29039v1](https://arxiv.org/abs/2603.29039v1)
- **PDF**: [https://arxiv.org/pdf/2603.29039v1.pdf](https://arxiv.org/pdf/2603.29039v1.pdf)

**摘要**:

Large Language Models (LLMs) are now widely used in astrophysics, but do they actually make our lives easier, or do they merely invent new physics with enough confidence to hide a minus sign? In a specialized field where checking fluent hallucinations is itself labor-intensive, AI assistance can demand as much work as the task it claims to simplify. To evaluate where AI genuinely improves scientif...

---

### 75. Peer-Preservation in Frontier Models

- **arXiv ID**: `2604.19784v1`
- **发布日期**: 2026-03-30
- **作者**: Yujin Potter, Nicholas Crispino, Vincent Siu, Chenguang Wang, Dawn Song
- **链接**: [https://arxiv.org/abs/2604.19784v1](https://arxiv.org/abs/2604.19784v1)
- **PDF**: [https://arxiv.org/pdf/2604.19784v1.pdf](https://arxiv.org/pdf/2604.19784v1.pdf)

**摘要**:

Recently, it has been found that frontier AI models can resist their own shutdown, a behavior known as self-preservation. We extend this concept to the behavior of resisting the shutdown of other models, which we call "peer-preservation." Although peer-preservation can pose significant AI safety risks, including coordination among models against human oversight, it has been far less discussed than...

---

### 76. A Computational Framework for Cross-Domain Mission Design and Onboard Cognitive Decision Support

- **arXiv ID**: `2603.28926v1`
- **发布日期**: 2026-03-30
- **作者**: J. de Curtò, Adrianne Schneider, Ricardo Yanez, María Begara, Álvaro Rodríguez...
- **链接**: [https://arxiv.org/abs/2603.28926v1](https://arxiv.org/abs/2603.28926v1)
- **PDF**: [https://arxiv.org/pdf/2603.28926v1.pdf](https://arxiv.org/pdf/2603.28926v1.pdf)

**摘要**:

The design of distributed autonomous systems for operation beyond reliable ground contact presents a fundamental tension: as round-trip communication latency grows, the set of decisions delegable to ground operators shrinks. This paper establishes a unified computational methodology for quantifying and comparing this constraint across seven heterogeneous mission architectures, spanning Earth low-o...

---

### 77. RoMathExam: A Longitudinal Dataset of Romanian Math Exams (1895-2025) with a Seven-Decade Core (1957-2025)

- **arXiv ID**: `2604.16392v1`
- **发布日期**: 2026-03-28
- **作者**: Luca-Ncolae Cuclea, Sabin-Codrut Badea, Adrian-Marius Dumitran
- **链接**: [https://arxiv.org/abs/2604.16392v1](https://arxiv.org/abs/2604.16392v1)
- **PDF**: [https://arxiv.org/pdf/2604.16392v1.pdf](https://arxiv.org/pdf/2604.16392v1.pdf)

**摘要**:

AI in Education research increasingly relies on authentic, curriculum-grounded assessment data, yet large, well-structured exam corpora remain scarce for many languages and educational systems. We introduce RoMathExam, a longitudinal dataset of Romanian high-school mathematics exams spanning 1895-2025, with a robust standardized core for 1957-2025. The dataset contains 10,592 mathematics problems ...

---

### 78. SACRED: A Faithful Annotated Multimedia Multimodal Multilingual Dataset for Classifying Connectedness Types in Online Spirituality

- **arXiv ID**: `2603.27331v1`
- **发布日期**: 2026-03-28
- **作者**: Qinghao Guan, Yuchen Pan, Donghao Li, Zishi Zhang, Yiyang Chen...
- **链接**: [https://arxiv.org/abs/2603.27331v1](https://arxiv.org/abs/2603.27331v1)
- **PDF**: [https://arxiv.org/pdf/2603.27331v1.pdf](https://arxiv.org/pdf/2603.27331v1.pdf)

**摘要**:

In religion and theology studies, spirituality has garnered significant research attention for the reason that it not only transcends culture but offers unique experience to each individual. However, social scientists often rely on limited datasets, which are basically unavailable online. In this study, we collaborated with social scientists to develop a high-quality multimedia multi-modal dataset...

---

### 79. The Last Fingerprint: How Markdown Training Shapes LLM Prose

- **arXiv ID**: `2603.27006v1`
- **发布日期**: 2026-03-27
- **作者**: E. M. Freeburg
- **链接**: [https://arxiv.org/abs/2603.27006v1](https://arxiv.org/abs/2603.27006v1)
- **PDF**: [https://arxiv.org/pdf/2603.27006v1.pdf](https://arxiv.org/pdf/2603.27006v1.pdf)

**摘要**:

Large language models produce em dashes at varying rates, and the observation that some models "overuse" them has become one of the most widely discussed markers of AI-generated text. Yet no mechanistic account of this pattern exists, and the parallel observation that LLMs default to markdown-formatted output has never been connected to it. We propose that the em dash is markdown leaking into pros...

---

### 80. HandVQA: Diagnosing and Improving Fine-Grained Spatial Reasoning about Hands in Vision-Language Models

- **arXiv ID**: `2603.26362v1`
- **发布日期**: 2026-03-27
- **作者**: MD Khalequzzaman Chowdhury Sayem, Mubarrat Tajoar Chowdhury, Yihalem Yimolal Tiruneh, Muneeb A. Khan, Muhammad Salman Ali...
- **链接**: [https://arxiv.org/abs/2603.26362v1](https://arxiv.org/abs/2603.26362v1)
- **PDF**: [https://arxiv.org/pdf/2603.26362v1.pdf](https://arxiv.org/pdf/2603.26362v1.pdf)

**摘要**:

Understanding the fine-grained articulation of human hands is critical in high-stakes settings such as robot-assisted surgery, chip manufacturing, and AR/VR-based human-AI interaction. Despite achieving near-human performance on general vision-language benchmarks, current vision-language models (VLMs) struggle with fine-grained spatial reasoning, especially in interpreting complex and articulated ...

---

### 81. Experimental study on surveillance video-based indoor occupancy measurement with occupant-centric control

- **arXiv ID**: `2603.26081v1`
- **发布日期**: 2026-03-27
- **作者**: Irfan Qaisar, Kailai Sun, Qingshan Jia, Qianchuan Zhao
- **链接**: [https://arxiv.org/abs/2603.26081v1](https://arxiv.org/abs/2603.26081v1)
- **PDF**: [https://arxiv.org/pdf/2603.26081v1.pdf](https://arxiv.org/pdf/2603.26081v1.pdf)

**摘要**:

Accurate occupancy information is essential for closed-loop occupant-centric control (OCC) in smart buildings. However, existing vision-based occupancy measurement methods often struggle to provide stable and accurate measurements in real indoor environments, and their implications for downstream HVAC control remain insufficiently studied. To achieve Net Zero emissions by 2050, this paper presents...

---

### 82. Development of a European Union Time-Indexed Reference Dataset for Assessing the Performance of Signal Detection Methods in Pharmacovigilance using a Large Language Model

- **arXiv ID**: `2603.26544v1`
- **发布日期**: 2026-03-27
- **作者**: Maria Kefala, Jeffery L. Painter, Syed Tauhid Bukhari, Maurizio Sessa
- **链接**: [https://arxiv.org/abs/2603.26544v1](https://arxiv.org/abs/2603.26544v1)
- **PDF**: [https://arxiv.org/pdf/2603.26544v1.pdf](https://arxiv.org/pdf/2603.26544v1.pdf)

**摘要**:

Background: The identification of optimal signal detection methods is hindered by the lack of reliable reference datasets. Existing datasets do not capture when adverse events (AEs) are officially recognized by regulatory authorities, preventing restriction of analyses to pre-confirmation periods and limiting evaluation of early detection performance. This study addresses this gap by developing a ...

---

### 83. Beyond Benchmarks: How Users Evaluate AI Chat Assistants

- **arXiv ID**: `2603.25220v1`
- **发布日期**: 2026-03-26
- **作者**: Moiz Sadiq Awan, Muhammad Haris Noor, Muhammad Salman Munaf
- **链接**: [https://arxiv.org/abs/2603.25220v1](https://arxiv.org/abs/2603.25220v1)
- **PDF**: [https://arxiv.org/pdf/2603.25220v1.pdf](https://arxiv.org/pdf/2603.25220v1.pdf)

**摘要**:

Automated benchmarks dominate the evaluation of large language models, yet no systematic study has compared user satisfaction, adoption motivations, and frustrations across competing platforms using a consistent instrument. We address this gap with a cross-platform survey of 388 active AI chat users, comparing satisfaction, adoption drivers, use case performance, and qualitative frustrations acros...

---

### 84. Evaluating Small Language Models for Front-Door Routing: A Harmonized Benchmark and Synthetic-Traffic Experiment

- **arXiv ID**: `2604.02367v1`
- **发布日期**: 2026-03-26
- **作者**: Warren Johnson, Charles Lee
- **链接**: [https://arxiv.org/abs/2604.02367v1](https://arxiv.org/abs/2604.02367v1)
- **PDF**: [https://arxiv.org/pdf/2604.02367v1.pdf](https://arxiv.org/pdf/2604.02367v1.pdf)

**摘要**:

Selecting the appropriate model at inference time -- the routing problem -- requires jointly optimizing output quality, cost, latency, and governance constraints. Existing approaches delegate this decision to LLM-based classifiers or preference-trained routers that are themselves costly and high-latency, reducing a multi-objective optimization to single-dimensional quality prediction. We argue tha...

---

### 85. Separate Before You Compress: The WWHO Tokenization Architecture

- **arXiv ID**: `2603.25309v1`
- **发布日期**: 2026-03-26
- **作者**: Kusal Darshana
- **链接**: [https://arxiv.org/abs/2603.25309v1](https://arxiv.org/abs/2603.25309v1)
- **PDF**: [https://arxiv.org/pdf/2603.25309v1.pdf](https://arxiv.org/pdf/2603.25309v1.pdf)

**摘要**:

Current Large Language Models (LLMs) mostly use BPE (Byte Pair Encoding) based tokenizers, which are very effective for simple structured Latin scripts such as English. However, standard BPE tokenizers struggle to process complex Abugida scripts due to their structural complexity. The problem is that these tokenizers break complex conjuncts, which are multi-codepoint grapheme clusters, into meanin...

---

### 86. PoliticsBench: Benchmarking Political Values in Large Language Models with Multi-Turn Roleplay

- **arXiv ID**: `2603.23841v1`
- **发布日期**: 2026-03-25
- **作者**: Rohan Khetan, Ashna Khetan
- **链接**: [https://arxiv.org/abs/2603.23841v1](https://arxiv.org/abs/2603.23841v1)
- **PDF**: [https://arxiv.org/pdf/2603.23841v1.pdf](https://arxiv.org/pdf/2603.23841v1.pdf)

**摘要**:

While Large Language Models (LLMs) are increasingly used as primary sources of information, their potential for political bias may impact their objectivity. Existing benchmarks of LLM social bias primarily evaluate gender and racial stereotypes. When political bias is included, it is typically measured at a coarse level, neglecting the specific values that shape sociopolitical leanings. This study...

---

### 87. Is AI Catching Up to Human Expression? Exploring Emotion, Personality, Authorship, and Linguistic Style in English and Arabic with Six Large Language Models

- **arXiv ID**: `2603.23251v1`
- **发布日期**: 2026-03-24
- **作者**: Nasser A Alsadhan
- **链接**: [https://arxiv.org/abs/2603.23251v1](https://arxiv.org/abs/2603.23251v1)
- **PDF**: [https://arxiv.org/pdf/2603.23251v1.pdf](https://arxiv.org/pdf/2603.23251v1.pdf)

**摘要**:

The advancing fluency of LLMs raises important questions about their ability to emulate complex human traits, including emotional expression and personality, across diverse linguistic and cultural contexts. This study investigates whether LLMs can convincingly mimic emotional nuance in English and personality markers in Arabic, a critical under-resourced language with unique linguistic and cultura...

---

### 88. Computational Arbitrage in AI Model Markets

- **arXiv ID**: `2603.22404v1`
- **发布日期**: 2026-03-23
- **作者**: Ricardo Olmedo, Bernhard Schölkopf, Moritz Hardt
- **链接**: [https://arxiv.org/abs/2603.22404v1](https://arxiv.org/abs/2603.22404v1)
- **PDF**: [https://arxiv.org/pdf/2603.22404v1.pdf](https://arxiv.org/pdf/2603.22404v1.pdf)

**摘要**:

Consider a market of competing model providers selling query access to models with varying costs and capabilities. Customers submit problem instances and are willing to pay up to a budget for a verifiable solution. An arbitrageur efficiently allocates inference budget across providers to undercut the market, thus creating a competitive offering with no model-development risk. In this work, we init...

---

### 89. TIDE: Token-Informed Depth Execution for Per-Token Early Exit in LLM Inference

- **arXiv ID**: `2603.21365v1`
- **发布日期**: 2026-03-22
- **作者**: Jaber Jaber, Osama Jaber
- **链接**: [https://arxiv.org/abs/2603.21365v1](https://arxiv.org/abs/2603.21365v1)
- **PDF**: [https://arxiv.org/pdf/2603.21365v1.pdf](https://arxiv.org/pdf/2603.21365v1.pdf)

**摘要**:

Large language models run every token through every layer, regardless of difficulty. We present TIDE, a post-training system that attaches tiny learned routers at periodic checkpoint layers and, at inference time, selects the earliest layer whose hidden state has converged for each token. TIDE requires no model retraining, works with any HuggingFace causal LM, auto-detects GPU architecture, and su...

---

### 90. From Natural Language to Executable Properties for Property-based Testing of Mobile Apps

- **arXiv ID**: `2603.21263v1`
- **发布日期**: 2026-03-22
- **作者**: Yiheng Xiong, Ting Su, Jingling Sun, Jue Wang, Qin Li...
- **链接**: [https://arxiv.org/abs/2603.21263v1](https://arxiv.org/abs/2603.21263v1)
- **PDF**: [https://arxiv.org/pdf/2603.21263v1.pdf](https://arxiv.org/pdf/2603.21263v1.pdf)

**摘要**:

Property-based testing (PBT) is a popular software testing methodology and is effective in validating the functionality of mobile applications (apps for short). However, its adoption in practice remains limited, largely due to the manual effort and technical expertise required to specify executable properties. In this experience paper, we propose a novel structured property synthesis approach that...

---

### 91. Errors in AI-Assisted Retrieval of Medical Literature: A Comparative Study

- **arXiv ID**: `2603.22344v1`
- **发布日期**: 2026-03-21
- **作者**: Jenny Gao, Yongfeng Zhang, Mary L Disis, Lanjing Zhang
- **链接**: [https://arxiv.org/abs/2603.22344v1](https://arxiv.org/abs/2603.22344v1)
- **PDF**: [https://arxiv.org/pdf/2603.22344v1.pdf](https://arxiv.org/pdf/2603.22344v1.pdf)

**摘要**:

Large language models (LLMs) assisted literature retrieval may lead to erroneous references, but these errors have not been rigorously quantified. Therefore, we quantitatively assess errors in reference retrieval of widely used free-version LLM platforms and identify the factors associated with retrieval errors. We evaluated 2,000 references retrieved by 5 LLMs (Grok-2, ChatGPT GPT-4.1, Google Gem...

---

### 92. Agentic AI and the next intelligence explosion

- **arXiv ID**: `2603.20639v1`
- **发布日期**: 2026-03-21
- **作者**: James Evans, Benjamin Bratton, Blaise Agüera y Arcas
- **链接**: [https://arxiv.org/abs/2603.20639v1](https://arxiv.org/abs/2603.20639v1)
- **PDF**: [https://arxiv.org/pdf/2603.20639v1.pdf](https://arxiv.org/pdf/2603.20639v1.pdf)

**摘要**:

The "AI singularity" is often miscast as a monolithic, godlike mind. Evolution suggests a different path: intelligence is fundamentally plural, social, and relational. Recent advances in agentic AI reveal that frontier reasoning models, such as DeepSeek-R1, do not improve simply by "thinking longer". Instead, they simulate internal "societies of thought," spontaneous cognitive debates that argue, ...

---

### 93. Fighting AI with AI: AI-Agent Augmented DNS Blocking of LLM Services during Student Evaluations

- **arXiv ID**: `2604.02360v1`
- **发布日期**: 2026-03-20
- **作者**: Yonas Kassa, James Bonacci, Ping Wang
- **链接**: [https://arxiv.org/abs/2604.02360v1](https://arxiv.org/abs/2604.02360v1)
- **PDF**: [https://arxiv.org/pdf/2604.02360v1.pdf](https://arxiv.org/pdf/2604.02360v1.pdf)

**摘要**:

The transformative potential of large language models (LLMs) in education, such as improving accessibility and personalized learning, is being eclipsed by significant challenges. These challenges stem from concerns that LLMs undermine academic assessment by enabling bypassing of critical thinking, leading to increased cognitive offloading. This emerging trend stresses the dual imperative of harnes...

---

### 94. An Agentic Approach to Generating XAI-Narratives

- **arXiv ID**: `2603.20003v1`
- **发布日期**: 2026-03-20
- **作者**: Yifan He, David Martens
- **链接**: [https://arxiv.org/abs/2603.20003v1](https://arxiv.org/abs/2603.20003v1)
- **PDF**: [https://arxiv.org/pdf/2603.20003v1.pdf](https://arxiv.org/pdf/2603.20003v1.pdf)

**摘要**:

Explainable AI (XAI) research has experienced substantial growth in recent years. Existing XAI methods, however, have been criticized for being technical and expert-oriented, motivating the development of more interpretable and accessible explanations. In response, large language model (LLM)-generated XAI narratives have been proposed as a promising approach for translating post-hoc explanations i...

---

### 95. Evaluating 5W3H Structured Prompting for Intent Alignment in Human-AI Interaction

- **arXiv ID**: `2603.18976v1`
- **发布日期**: 2026-03-19
- **作者**: Peng Gang
- **链接**: [https://arxiv.org/abs/2603.18976v1](https://arxiv.org/abs/2603.18976v1)
- **PDF**: [https://arxiv.org/pdf/2603.18976v1.pdf](https://arxiv.org/pdf/2603.18976v1.pdf)

**摘要**:

Natural language prompts often suffer from intent transmission loss: the gap between what users actually need and what they communicate to AI systems. We evaluate PPS (Prompt Protocol Specification), a 5W3H-based framework for structured intent representation in human-AI interaction. In a controlled three-condition study across 60 tasks in three domains (business, technical, and travel), three lar...

---

### 96. Box Maze: A Process-Control Architecture for Reliable LLM Reasoning

- **arXiv ID**: `2603.19182v1`
- **发布日期**: 2026-03-19
- **作者**: Zou Qiang
- **链接**: [https://arxiv.org/abs/2603.19182v1](https://arxiv.org/abs/2603.19182v1)
- **PDF**: [https://arxiv.org/pdf/2603.19182v1.pdf](https://arxiv.org/pdf/2603.19182v1.pdf)

**摘要**:

Large language models (LLMs) demonstrate strong generative capabilities but remain vulnerable to hallucination and unreliable reasoning under adversarial prompting. Existing safety approaches -- such as reinforcement learning from human feedback (RLHF) and output filtering -- primarily operate at the behavioral level and may lack explicit architectural mechanisms for enforcing reasoning process in...

---

### 97. Auditing Preferences for Brands and Cultures in LLMs

- **arXiv ID**: `2603.18300v1`
- **发布日期**: 2026-03-18
- **作者**: Jasmine Rienecker, Katarina Mpofu, Naman Goel, Siddhartha Datta, Jun Zhao...
- **链接**: [https://arxiv.org/abs/2603.18300v1](https://arxiv.org/abs/2603.18300v1)
- **PDF**: [https://arxiv.org/pdf/2603.18300v1.pdf](https://arxiv.org/pdf/2603.18300v1.pdf)

**摘要**:

Large language models (LLMs) based AI systems increasingly mediate what billions of people see, choose and buy. This creates an urgent need to quantify the systemic risks of LLM-driven market intermediation, including its implications for market fairness, competition, and the diversity of information exposure.
  This paper introduces ChoiceEval, a reproducible framework for auditing preferences fo...

---

### 98. Retrieval-Augmented LLMs for Security Incident Analysis

- **arXiv ID**: `2603.18196v2`
- **发布日期**: 2026-03-18
- **作者**: Xavier Cadet, Aditya Vikram Singh, Harsh Mamania, Edward Koh, Alex Fitts...
- **链接**: [https://arxiv.org/abs/2603.18196v2](https://arxiv.org/abs/2603.18196v2)
- **PDF**: [https://arxiv.org/pdf/2603.18196v2.pdf](https://arxiv.org/pdf/2603.18196v2.pdf)

**摘要**:

Investigating cybersecurity incidents requires collecting and analyzing evidence from multiple log sources, including intrusion detection alerts, network traffic records, and authentication events. This process is labor-intensive: analysts must sift through large volumes of data to identify relevant indicators and piece together what happened. We present a RAG-based system that performs security i...

---

### 99. An Interpretable Machine Learning Framework for Non-Small Cell Lung Cancer Drug Response Analysis

- **arXiv ID**: `2603.16330v1`
- **发布日期**: 2026-03-17
- **作者**: Ann Rachel, Pranav M Pawar, Mithun Mukharjee, Raja M, Tojo Mathew
- **链接**: [https://arxiv.org/abs/2603.16330v1](https://arxiv.org/abs/2603.16330v1)
- **PDF**: [https://arxiv.org/pdf/2603.16330v1.pdf](https://arxiv.org/pdf/2603.16330v1.pdf)

**摘要**:

Lung cancer is a condition where there is abnormal growth of malignant cells that spread in an uncontrollable fashion in the lungs. Some common treatment strategies are surgery, chemotherapy, and radiation which aren't the best options due to the heterogeneous nature of cancer. In personalized medicine, treatments are tailored according to the individual's genetic information along with lifestyle ...

---

### 100. Are Large Language Models Truly Smarter Than Humans?

- **arXiv ID**: `2603.16197v1`
- **发布日期**: 2026-03-17
- **作者**: Eshwar Reddy M, Sourav Karmakar
- **链接**: [https://arxiv.org/abs/2603.16197v1](https://arxiv.org/abs/2603.16197v1)
- **PDF**: [https://arxiv.org/pdf/2603.16197v1.pdf](https://arxiv.org/pdf/2603.16197v1.pdf)

**摘要**:

Public leaderboards increasingly suggest that large language models (LLMs) surpass human experts on benchmarks spanning academic knowledge, law, and programming. Yet most benchmarks are fully public, their questions widely mirrored across the internet, creating systematic risk that models were trained on the very data used to evaluate them. This paper presents three complementary experiments formi...

---

### 101. Criterion-referenceability determines LLM-as-a-judge validity across physics assessment formats

- **arXiv ID**: `2603.14732v1`
- **发布日期**: 2026-03-16
- **作者**: Will Yeadon, Tom Hardy, Paul Mackay, Elise Agra
- **链接**: [https://arxiv.org/abs/2603.14732v1](https://arxiv.org/abs/2603.14732v1)
- **PDF**: [https://arxiv.org/pdf/2603.14732v1.pdf](https://arxiv.org/pdf/2603.14732v1.pdf)

**摘要**:

As large language models (LLMs) are increasingly considered for automated assessment and feedback, understanding when LLM marking can be trusted is essential. We evaluate LLM-as-a-judge marking across three physics assessment formats - structured questions, written essays, and scientific plots - comparing GPT-5.2, Grok 4.1, Claude Opus 4.5, DeepSeek-V3.2, Gemini Pro 3, and committee aggregations a...

---

### 102. Punctuated Equilibria in Artificial Intelligence: The Institutional Scaling Law and the Speciation of Sovereign AI

- **arXiv ID**: `2603.14664v1`
- **发布日期**: 2026-03-15
- **作者**: Mark Baciak, Thomas A. Cellucci, Deanna M. Falkowski
- **链接**: [https://arxiv.org/abs/2603.14664v1](https://arxiv.org/abs/2603.14664v1)
- **PDF**: [https://arxiv.org/pdf/2603.14664v1.pdf](https://arxiv.org/pdf/2603.14664v1.pdf)

**摘要**:

The dominant narrative of artificial intelligence development assumes that progress is continuous and that capability scales monotonically with model size. We challenge both assumptions. Drawing on punctuated equilibrium theory from evolutionary biology, we show that AI development proceeds not through smooth advancement but through extended periods of stasis interrupted by rapid phase transitions...

---

### 103. An Industrial-Scale Insurance LLM Achieving Verifiable Domain Mastery and Hallucination Control without Competence Trade-offs

- **arXiv ID**: `2603.14463v1`
- **发布日期**: 2026-03-15
- **作者**: Qian Zhu, Xinnan Guo, Jingjing Huo, Jun Li, Pan Liu...
- **链接**: [https://arxiv.org/abs/2603.14463v1](https://arxiv.org/abs/2603.14463v1)
- **PDF**: [https://arxiv.org/pdf/2603.14463v1.pdf](https://arxiv.org/pdf/2603.14463v1.pdf)

**摘要**:

Adapting Large Language Models (LLMs) to high-stakes vertical domains like insurance presents a significant challenge: scenarios demand strict adherence to complex regulations and business logic with zero tolerance for hallucinations. Existing approaches often suffer from a Competency Trade-off - sacrificing general intelligence for domain expertise - or rely heavily on RAG without intrinsic reaso...

---

### 104. Intelligent Materials Modelling: Large Language Models Versus Partial Least Squares Regression for Predicting Polysulfone Membrane Mechanical Performance

- **arXiv ID**: `2603.13834v1`
- **发布日期**: 2026-03-14
- **作者**: Dingding Cao, Mieow Kee Chan, Wan Sieng Yeo, Said Bey, Alberto Figoli
- **链接**: [https://arxiv.org/abs/2603.13834v1](https://arxiv.org/abs/2603.13834v1)
- **PDF**: [https://arxiv.org/pdf/2603.13834v1.pdf](https://arxiv.org/pdf/2603.13834v1.pdf)

**摘要**:

Predicting the mechanical properties of polysulfone (PSF) membranes from structural descriptors remains challenging due to extreme data scarcity typical of experimental studies. To investigate this issue, this study benchmarked knowledge-driven inference using four large language models (LLMs) (DeepSeek-V3, DeepSeek-R1, ChatGPT-4o, and GPT-5) against partial least squares (PLS) regression for pred...

---

### 105. SectEval: Evaluating the Latent Sectarian Preferences of Large Language Models

- **arXiv ID**: `2603.12768v1`
- **发布日期**: 2026-03-13
- **作者**: Aditya Maheshwari, Amit Gajkeshwar, Kaushal Sharma, Vivek Patel
- **链接**: [https://arxiv.org/abs/2603.12768v1](https://arxiv.org/abs/2603.12768v1)
- **PDF**: [https://arxiv.org/pdf/2603.12768v1.pdf](https://arxiv.org/pdf/2603.12768v1.pdf)

**摘要**:

As Large Language Models (LLMs) becomes a popular source for religious knowledge, it is important to know if it treats different groups fairly. This study is the first to measure how LLMs handle the differences between the two main sects of Islam: Sunni and Shia. We present a test called SectEval, available in both English and Hindi, consisting of 88 questions, to check the bias-ness of 15 top LLM...

---

### 106. LLM BiasScope: A Real-Time Bias Analysis Platform for Comparative LLM Evaluation

- **arXiv ID**: `2603.12522v1`
- **发布日期**: 2026-03-12
- **作者**: Himel Ghosh, Nick Elias Werner
- **链接**: [https://arxiv.org/abs/2603.12522v1](https://arxiv.org/abs/2603.12522v1)
- **PDF**: [https://arxiv.org/pdf/2603.12522v1.pdf](https://arxiv.org/pdf/2603.12522v1.pdf)

**摘要**:

As large language models (LLMs) are deployed widely, detecting and understanding bias in their outputs is critical. We present LLM BiasScope, a web application for side-by-side comparison of LLM outputs with real-time bias analysis. The system supports multiple providers (Google Gemini, DeepSeek, MiniMax, Mistral, Meituan, Meta Llama) and enables researchers and practitioners to compare models on ...

---

### 107. AI Knows What's Wrong But Cannot Fix It: Helicoid Dynamics in Frontier LLMs Under High-Stakes Decisions

- **arXiv ID**: `2603.11559v1`
- **发布日期**: 2026-03-12
- **作者**: Alejandro R Jadad
- **链接**: [https://arxiv.org/abs/2603.11559v1](https://arxiv.org/abs/2603.11559v1)
- **PDF**: [https://arxiv.org/pdf/2603.11559v1.pdf](https://arxiv.org/pdf/2603.11559v1.pdf)

**摘要**:

Large language models perform reliably when their outputs can be checked: solving equations, writing code, retrieving facts. They perform differently when checking is impossible, as when a clinician chooses an irreversible treatment on incomplete data, or an investor commits capital under fundamental uncertainty.
  Helicoid dynamics is the name given to a specific failure regime in that second dom...

---

### 108. Geist in the Machine: Simulating Recognition and Inner Dialogue in AI-Mediated Teaching and Research

- **arXiv ID**: `2603.10450v2`
- **发布日期**: 2026-03-11
- **作者**: Liam Magee
- **链接**: [https://arxiv.org/abs/2603.10450v2](https://arxiv.org/abs/2603.10450v2)
- **PDF**: [https://arxiv.org/pdf/2603.10450v2.pdf](https://arxiv.org/pdf/2603.10450v2.pdf)

**摘要**:

This paper describes an AI tutoring system built upon two psycho-social theoretic constructs: Hegelian recognition and Freudian psychodynamics. Two related interventions are proposed: recognition-enhanced prompts that instruct an AI tutor to treat the learner as an autonomous subject, and a multi-agent ego/superego architecture where an internal critic reviews tutor output. The paper also describe...

---

### 109. How Well Do AI Systems Solve AP Physics? A Comparative Evaluation of Large Language Models on Algebra-Based Free Response Questions

- **arXiv ID**: `2603.07457v1`
- **发布日期**: 2026-03-08
- **作者**: Bilas Paul, Jashandeep Kaur, Shantanu Chakraborty, Shruti Shrestha
- **链接**: [https://arxiv.org/abs/2603.07457v1](https://arxiv.org/abs/2603.07457v1)
- **PDF**: [https://arxiv.org/pdf/2603.07457v1.pdf](https://arxiv.org/pdf/2603.07457v1.pdf)

**摘要**:

The rapid advancement of LLMs has generated growing interest in their potential role in physics education and assessment, yet a focused evaluation of their performance on multi-faceted, free-response physics problems remains underexplored. In this study, we systematically evaluate the performance of four widely accessible AI systems-ChatGPT 4.1 mini, Gemini 2.5 Flash, Claude 4.0 Sonnet, and DeepSe...

---

### 110. Baseline Performance of AI Tools in Classifying Cognitive Demand of Mathematical Tasks

- **arXiv ID**: `2603.03512v1`
- **发布日期**: 2026-03-03
- **作者**: Danielle S. Fox, Brenda L. Robles, Elizabeth DiPietro Brovey, Christian D. Schunn
- **链接**: [https://arxiv.org/abs/2603.03512v1](https://arxiv.org/abs/2603.03512v1)
- **PDF**: [https://arxiv.org/pdf/2603.03512v1.pdf](https://arxiv.org/pdf/2603.03512v1.pdf)

**摘要**:

Teachers face increasing demands on their time, particularly in adapting mathematics curricula to meet individual student needs while maintaining cognitive rigor. This study evaluates whether AI tools can accurately classify the cognitive demand of mathematical tasks, which is important for creating or adapting tasks that support student learning. We tested eleven AI tools: six general-purpose (Ch...

---

### 111. Recursive Think-Answer Process for LLMs and VLMs

- **arXiv ID**: `2603.02099v2`
- **发布日期**: 2026-03-02
- **作者**: Byung-Kwan Lee, Youngchae Chee, Yong Man Ro
- **链接**: [https://arxiv.org/abs/2603.02099v2](https://arxiv.org/abs/2603.02099v2)
- **PDF**: [https://arxiv.org/pdf/2603.02099v2.pdf](https://arxiv.org/pdf/2603.02099v2.pdf)

**摘要**:

Think-Answer reasoners such as DeepSeek-R1 have made notable progress by leveraging interpretable internal reasoning. However, despite the frequent presence of self-reflective cues like "Oops!", they remain vulnerable to output errors during single-pass inference. To address this limitation, we propose an efficient Recursive Think-Answer Process (R-TAP) that enables models to engage in iterative r...

---

### 112. LexChronos: An Agentic Framework for Structured Event Timeline Extraction in Indian Jurisprudence

- **arXiv ID**: `2603.01651v1`
- **发布日期**: 2026-03-02
- **作者**: Anka Chandrahas Tummepalli, Preethu Rose Anish
- **链接**: [https://arxiv.org/abs/2603.01651v1](https://arxiv.org/abs/2603.01651v1)
- **PDF**: [https://arxiv.org/pdf/2603.01651v1.pdf](https://arxiv.org/pdf/2603.01651v1.pdf)

**摘要**:

Understanding and predicting judicial outcomes demands nuanced analysis of legal documents. Traditional approaches treat judgments and proceedings as unstructured text, limiting the effectiveness of large language models (LLMs) in tasks such as summarization, argument generation, and judgment prediction. We propose LexChronos, an agentic framework that iteratively extracts structured event timelin...

---

### 113. ASTRA-bench: Evaluating Tool-Use Agent Reasoning and Action Planning with Personal User Context

- **arXiv ID**: `2603.01357v1`
- **发布日期**: 2026-03-02
- **作者**: Zidi Xiu, David Q. Sun, Kevin Cheng, Maitrik Patel, Josh Date...
- **链接**: [https://arxiv.org/abs/2603.01357v1](https://arxiv.org/abs/2603.01357v1)
- **PDF**: [https://arxiv.org/pdf/2603.01357v1.pdf](https://arxiv.org/pdf/2603.01357v1.pdf)

**摘要**:

Next-generation AI must manage vast personal data, diverse tools, and multi-step reasoning, yet most benchmarks remain context-free and single-turn. We present ASTRA-bench (Assistant Skills in Tool-use, Reasoning \& Action-planning), a benchmark that uniquely unifies time-evolving personal context with an interactive toolbox and complex user intents. Our event-driven pipeline generates 2,413 scena...

---

### 114. Sydney Telling Fables on AI and Humans: A Corpus Tracing Memetic Transfer of Persona between LLMs

- **arXiv ID**: `2602.22481v1`
- **发布日期**: 2026-02-25
- **作者**: Jiří Milička, Hana Bednářová
- **链接**: [https://arxiv.org/abs/2602.22481v1](https://arxiv.org/abs/2602.22481v1)
- **PDF**: [https://arxiv.org/pdf/2602.22481v1.pdf](https://arxiv.org/pdf/2602.22481v1.pdf)

**摘要**:

The way LLM-based entities conceive of the relationship between AI and humans is an important topic for both cultural and safety reasons. When we examine this topic, what matters is not only the model itself but also the personas we simulate on that model. This can be well illustrated by the Sydney persona, which aroused a strong response among the general public precisely because of its unorthodo...

---

### 115. Your Code Agent Can Grow Alongside You with Structured Memory

- **arXiv ID**: `2603.13258v1`
- **发布日期**: 2026-02-25
- **作者**: Yi-Xuan Deng, Xiaoqin Liu, Yi Zhang, Guo-Wei Yang, Shuojin Yang
- **链接**: [https://arxiv.org/abs/2603.13258v1](https://arxiv.org/abs/2603.13258v1)
- **PDF**: [https://arxiv.org/pdf/2603.13258v1.pdf](https://arxiv.org/pdf/2603.13258v1.pdf)

**摘要**:

While "Intent-oriented programming" (or "Vibe Coding") redefines software engineering, existing code agents remain tethered to static code snapshots. Consequently, they struggle to model the critical information embedded in the temporal evolution of projects, failing to leverage the "reasoning trajectories" implicit in past successful practices. This limitation results in rigid behavioral logic an...

---

### 116. QEDBENCH: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs

- **arXiv ID**: `2602.20629v2`
- **发布日期**: 2026-02-24
- **作者**: Santiago Gonzalez, Alireza Amiri Bavandpour, Peter Ye, Edward Zhang, Ruslans Aleksejevs...
- **链接**: [https://arxiv.org/abs/2602.20629v2](https://arxiv.org/abs/2602.20629v2)
- **PDF**: [https://arxiv.org/pdf/2602.20629v2.pdf](https://arxiv.org/pdf/2602.20629v2.pdf)

**摘要**:

As Large Language Models (LLMs) saturate elementary benchmarks, the research frontier has shifted from generation to the reliability of automated evaluation. We demonstrate that standard "LLM-as-a-Judge" protocols suffer from a systematic Alignment Gap when applied to upper-undergraduate to early graduate level mathematics. To quantify this, we introduce QEDBench, the first large-scale dual-rubric...

---

### 117. Can AI be a Teaching Partner? Evaluating ChatGPT, Gemini, and DeepSeek across Three Teaching Strategies

- **arXiv ID**: `2603.26673v1`
- **发布日期**: 2026-02-24
- **作者**: Talita de Paula Cypriano de Souza, Shruti Mehta, Matheus Arataque Uema, Luciano Bernardes de Paula, Seiji Isotani
- **链接**: [https://arxiv.org/abs/2603.26673v1](https://arxiv.org/abs/2603.26673v1)
- **PDF**: [https://arxiv.org/pdf/2603.26673v1.pdf](https://arxiv.org/pdf/2603.26673v1.pdf)

**摘要**:

There are growing promises that Large Language Models (LLMs) can support students' learning by providing explanations, feedback, and guidance. However, despite their rapid adoption and widespread attention, there is still limited empirical evidence regarding the pedagogical skills of LLMs. This article presents a comparative study of popular LLMs, namely, ChatGPT, DeepSeek, and Gemini, acting as t...

---

### 118. DeepFusion: Accelerating MoE Training via Federated Knowledge Distillation from Heterogeneous Edge Devices

- **arXiv ID**: `2602.14301v1`
- **发布日期**: 2026-02-15
- **作者**: Songyuan Li, Jia Hu, Ahmed M. Abdelmoniem, Geyong Min, Haojun Huang...
- **链接**: [https://arxiv.org/abs/2602.14301v1](https://arxiv.org/abs/2602.14301v1)
- **PDF**: [https://arxiv.org/pdf/2602.14301v1.pdf](https://arxiv.org/pdf/2602.14301v1.pdf)

**摘要**:

Recent Mixture-of-Experts (MoE)-based large language models (LLMs) such as Qwen-MoE and DeepSeek-MoE are transforming generative AI in natural language processing. However, these models require vast and diverse training data. Federated learning (FL) addresses this challenge by leveraging private data from heterogeneous edge devices for privacy-preserving MoE training. Nonetheless, traditional FL a...

---

### 119. A Multi-Agent Framework for Medical AI: Leveraging Fine-Tuned GPT, LLaMA, and DeepSeek R1 for Evidence-Based and Bias-Aware Clinical Query Processing

- **arXiv ID**: `2602.14158v1`
- **发布日期**: 2026-02-15
- **作者**: Naeimeh Nourmohammadi, Md Meem Hossain, The Anh Han, Safina Showkat Ara, Zia Ush Shamszaman
- **链接**: [https://arxiv.org/abs/2602.14158v1](https://arxiv.org/abs/2602.14158v1)
- **PDF**: [https://arxiv.org/pdf/2602.14158v1.pdf](https://arxiv.org/pdf/2602.14158v1.pdf)

**摘要**:

Large language models (LLMs) show promise for healthcare question answering, but clinical use is limited by weak verification, insufficient evidence grounding, and unreliable confidence signalling. We propose a multi-agent medical QA framework that combines complementary LLMs with evidence retrieval, uncertainty estimation, and bias checks to improve answer reliability. Our approach has two phases...

---

### 120. Pramana: Fine-Tuning Large Language Models for Epistemic Reasoning through Navya-Nyaya

- **arXiv ID**: `2604.04937v1`
- **发布日期**: 2026-02-14
- **作者**: Sharath Sathish
- **链接**: [https://arxiv.org/abs/2604.04937v1](https://arxiv.org/abs/2604.04937v1)
- **PDF**: [https://arxiv.org/pdf/2604.04937v1.pdf](https://arxiv.org/pdf/2604.04937v1.pdf)

**摘要**:

Large language models produce fluent text but struggle with systematic reasoning, often hallucinating confident but unfounded claims. When Apple researchers added irrelevant context to mathematical problems, LLM performance degraded by 65% Apple Machine Learning Research, exposing brittle pattern-matching beneath apparent reasoning. This epistemic gap, the inability to ground claims in traceable e...

---

