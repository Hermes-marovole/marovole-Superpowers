# DeepSeek 论文全集汇总报告

> **搜索时间**: 2026年4月30日  
> **来源**: arXiv、GitHub、Hugging Face、官方渠道  
> **收集者**: Worker Agent  
> **整理**: PM Agent

---

## 📊 执行摘要

本次搜索共收集到 **DeepSeek 官方发表的 15 篇核心技术论文**，以及 **arXiv 上引用/提及 DeepSeek 的 117 篇相关研究论文**，总计 **120+ 篇论文**。

### 核心发现

| 类别 | 数量 | 说明 |
|------|------|------|
| 官方技术报告 | 15 篇 | DeepSeek 团队正式发布 |
| 引用/相关研究 | 117+ 篇 | 其他研究者引用 DeepSeek 的论文 |
| **总计** | **120+ 篇** | 持续更新中 |

### 技术演进时间线

```
2024-01: DeepSeek LLM (基础语言模型)
2024-01: DeepSeek-Coder (代码模型)
2024-02: DeepSeekMath (数学推理)
2024-05: DeepSeek-V2 (MLA架构引入)
2024-06: DeepSeek-Coder-V2
2024-12: DeepSeek-V3 (671B MoE)
2024-12: DeepSeek-VL2 (视觉语言)
2025-01: DeepSeek-R1 (推理模型，强化学习)
2025-01: Janus-Pro (多模态)
2025-04: DeepSeek-Prover-V2 (定理证明)
2025-05: DeepSeek-V3 架构解析
2025-12: DeepSeek-V3.2
2026-04: DeepSeek-V4
```

---

## 📚 DeepSeek 官方技术报告（15篇）

### 语言模型系列

#### 1. DeepSeek LLM
- **论文**: DeepSeek LLM: Scaling Open-Source Language Models with Longtermism
- **arXiv**: [2401.02954](https://arxiv.org/abs/2401.02954)
- **发布时间**: 2024年1月
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-LLM
- **核心内容**: 在2万亿英中文token上训练，开源 7B/67B Base 和 Chat 模型

#### 2. DeepSeek-V2
- **论文**: DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model
- **arXiv**: [2405.04434](https://arxiv.org/abs/2405.04434)
- **发布时间**: 2024年5月
- **核心创新**: **Multi-Head Latent Attention (MLA)** 架构首次提出，高效 KV Cache 压缩

#### 3. DeepSeek-V3 ⭐
- **论文**: DeepSeek-V3 Technical Report
- **arXiv**: [2412.19437](https://arxiv.org/abs/2412.19437)
- **发布时间**: 2024年12月
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-V3
- **核心内容**: 
  - 671B 总参数的 MoE 模型，每 token 激活 37B
  - 14.8T tokens 预训练
  - 仅使用 2.664M H800 GPU 小时完成训练
  - **Auxiliary-Loss-Free 负载均衡策略**
  - **FP8 混合精度训练**
  - 性能匹敌 GPT-4、Claude 等闭源模型

#### 4. DeepSeek-V3.2
- **论文**: DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models
- **arXiv**: [2512.02556](https://arxiv.org/abs/2512.02556)
- **发布时间**: 2025年12月
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-V3.2

#### 5. DeepSeek-V4 ⭐
- **论文**: DeepSeek-V4 Technical Report
- **发布时间**: 2026年4月
- **HuggingFace**: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- **PDF**: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf

---

### 推理模型系列

#### 6. DeepSeek-R1 ⭐⭐
- **论文**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **arXiv**: [2501.12948](https://arxiv.org/abs/2501.12948)
- **发布时间**: 2025年1月
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-R1
- **Nature报道**: https://www.nature.com/articles/d41586-025-00011-2
- **核心突破**:
  - **DeepSeek-R1-Zero**: 纯强化学习训练，无需监督微调 (SFT)
  - **DeepSeek-R1**: 多阶段训练，包含冷启动数据
  - 展示了推理能力可通过纯 RL 激励而非人类标注数据
  - 支持模型自我改进和涌现推理行为

#### 7. DeepSeek-Prover-V2
- **论文**: DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition
- **arXiv**: [2504.21801](https://arxiv.org/abs/2504.21801)
- **发布时间**: 2025年4月
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-Prover-V2

---

### 代码模型系列

#### 8. DeepSeek-Coder
- **论文**: DeepSeek-Coder: When the Large Language Model Meets Programming
- **arXiv**: [2401.14196](https://arxiv.org/abs/2401.14196)
- **发布时间**: 2024年1月
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-Coder
- **训练数据**: 2T tokens (87% 代码 + 13% 自然语言)

#### 9. DeepSeek-Coder-V2
- **论文**: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence
- **arXiv**: [2406.11931](https://arxiv.org/abs/2406.11931)
- **发布时间**: 2024年6月
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-Coder-V2

---

### 数学推理系列

#### 10. DeepSeekMath
- **论文**: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
- **arXiv**: [2402.03300](https://arxiv.org/abs/2402.03300)
- **发布时间**: 2024年2月
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-Math
- **基础**: 在 DeepSeek-Coder-v1.5 7B 上继续预训练
- **DeepSeek-Math-V2 PDF**: https://github.com/deepseek-ai/DeepSeek-Math-V2/blob/main/DeepSeekMath_V2.pdf

---

### 多模态系列

#### 11. DeepSeek-VL
- **论文**: DeepSeek-VL: Towards Real-World Vision-Language Understanding
- **发布时间**: 2024年
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-VL

#### 12. DeepSeek-VL2
- **论文**: DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding
- **arXiv**: [2412.10302](https://arxiv.org/abs/2412.10302)
- **发布时间**: 2024年12月

#### 13. Janus-Pro
- **论文**: Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling
- **arXiv**: [2501.17811](https://arxiv.org/abs/2501.17811)
- **发布时间**: 2025年1月
- **GitHub**: https://github.com/deepseek-ai/Janus

---

### 架构基础

#### 14. DeepSeekMoE
- **论文**: DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models
- **arXiv**: [2401.06066](https://arxiv.org/abs/2401.06066)
- **发布时间**: 2024年1月
- **收录**: ACL 2024
- **核心**: 细粒度专家分割和共享专家隔离

---

### 架构解析

#### 15. Insights into DeepSeek-V3
- **论文**: Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures
- **arXiv**: [2505.09343](https://arxiv.org/abs/2505.09343)
- **发布时间**: 2025年5月

---

## 🔬 关键技术创新汇总

| 技术名称 | 首次出现 | 描述 |
|----------|----------|------|
| **MLA** | DeepSeek-V2 | Multi-Head Latent Attention，高效 KV 缓存压缩 |
| **DeepSeekMoE** | DeepSeekMoE | 细粒度混合专家架构 |
| **Auxiliary-Loss-Free** | DeepSeek-V3 | 无辅助损失的负载均衡策略 |
| **MTP** | DeepSeek-V3 | Multi-Token Prediction，多 token 预测训练 |
| **RL-based Reasoning** | DeepSeek-R1 | 纯强化学习激励推理能力 |
| **FP8 Training** | DeepSeek-V3 | FP8 混合精度训练 |

---

## 🔗 官方资源链接

### GitHub 组织
- **主页面**: https://github.com/deepseek-ai
- **仓库数量**: 33+ 个开源仓库

### Hugging Face
- **组织页面**: https://huggingface.co/deepseek-ai
- **论文集合**: https://huggingface.co/deepseek-ai/papers

### 官方文档
- **API 文档**: https://api-docs.deepseek.com/
- **新闻发布**: https://api-docs.deepseek.com/news/

---

## 📦 主要开源代码仓库

| 仓库 | 描述 | 链接 |
|------|------|------|
| DeepSeek-V3 | 671B MoE 语言模型 | https://github.com/deepseek-ai/DeepSeek-V3 |
| DeepSeek-V4 | V4 系列模型 | https://github.com/deepseek-ai/DeepSeek-V4 |
| DeepSeek-R1 | 推理模型 | https://github.com/deepseek-ai/DeepSeek-R1 |
| DeepSeek-Coder | 代码模型 | https://github.com/deepseek-ai/DeepSeek-Coder |
| DeepSeek-Coder-V2 | 第二代代码模型 | https://github.com/deepseek-ai/DeepSeek-Coder-V2 |
| DeepSeek-VL | 视觉语言模型 | https://github.com/deepseek-ai/DeepSeek-VL |
| Janus | 多模态理解生成 | https://github.com/deepseek-ai/Janus |
| DeepSeek-Math | 数学推理 | https://github.com/deepseek-ai/DeepSeek-Math |
| DreamCraft3D | 3D 内容生成 | https://github.com/deepseek-ai/DreamCraft3D |
| DeepSeek-Prover-V2 | 定理证明 | https://github.com/deepseek-ai/DeepSeek-Prover-V2 |
| FlashMLA | MLA 解码内核 | https://github.com/deepseek-ai/FlashMLA |
| DeepGEMM | FP8 GEMM 库 | https://github.com/deepseek-ai/DeepGEMM |
| DualPipe | 双向管道并行 | https://github.com/deepseek-ai/DualPipe |
| 3FS | 高性能文件系统 | https://github.com/deepseek-ai/3FS |
| Engram | 记忆架构研究 | https://github.com/deepseek-ai/Engram |

---

## 📝 BibTeX 引用格式

### DeepSeek-V3
```bibtex
@article{deepseek-v3-2024,
  title={DeepSeek-V3 Technical Report},
  author={DeepSeek-AI and Aixin Liu and Bei Feng and Bing Xue and Bingxuan Wang and others},
  journal={arXiv preprint arXiv:2412.19437},
  year={2024},
  url={https://arxiv.org/abs/2412.19437}
}
```

### DeepSeek-R1
```bibtex
@article{deepseek-r1-2025,
  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},
  author={DeepSeek-AI and Daya Guo and Dejian Yang and Haowei Zhang and Junxiao Song and others},
  journal={arXiv preprint arXiv:2501.12948},
  year={2025},
  url={https://arxiv.org/abs/2501.12948}
}
```

---

## 📄 完整论文清单（120篇）

详见附件文件：
- `deepseek_papers_complete.json` - JSON 格式完整数据
- `deepseek_papers_final_report.md` - 包含 117 篇引用论文的详细清单

---

## 💡 总结与建议

### DeepSeek 论文特点

1. **系统性强**: 从基础架构（MoE、MLA）到具体模型（V2、V3、R1）有完整技术演进路径
2. **开源彻底**: 所有主要模型都开源，并配有详细技术文档
3. **创新突出**: MLA、Auxiliary-Loss-Free、纯 RL 推理等技术均为业界首创
4. **性价比极致**: V3 论文展示了如何用极低成本（2.664M H800 小时）训练出匹敌 GPT-4 的模型

### 推荐阅读顺序

1. **入门**: DeepSeek-V3 Technical Report → 了解整体架构
2. **深入**: DeepSeek-R1 → 了解推理能力训练方法
3. **基础**: DeepSeekMoE + DeepSeek-V2 → 了解核心技术 MLA
4. **应用**: DeepSeek-Coder / DeepSeekMath → 了解领域特化模型

---

*来自翡冷翠*
*整理时间: 2026年4月30日*
