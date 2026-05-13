# Qwen 3.6 35B MoE 本地推理优化技术实测对比：TurboQuant vs TriAttention vs MTP

> 来源：Carlo (@Italianclownz) 在 X 上分享的实测数据  
> 原文：https://x.com/italianclownz/status/2054301170605113438  
> 整理日期：2026-05-13  
> 来自翠冷翠

---

## 执行摘要

这是一份在中端消费级硬件（RTX 3060 12GB + i5 8代 + 46GB RAM）上，对 **Qwen 3.6 35B A3B MTP MXFP4_MoE** 模型进行的三种推理优化技术实测对比。测试覆盖了 16K 到 262K 四种上下文长度，核心结论是：**TurboQuant 在所有测试场景下均为最快，是当前本地 LLM 推理量化的最优解。**

---

## 测试背景

### 模型
- **模型：**Qwen 3.6 35B A3B MTP MXFP4_MoE
- **简介：**Qwen 3.6 系列是阿里云通义千问发布的大语言模型。35B 总参数、3B 激活参数的 MoE 架构，支持内置 MTP（多 Token 预测）能力
- **量化格式：**Unsloth GGUF 格式，MXFP4_MoE 精度

### 硬件
- **显卡：**NVIDIA RTX 3060 12GB（内存只有 12GB 的老黄卡）
- **CPU：**Intel i5 8代
- **内存：**46GB RAM
- **软件：**本地 llama.cpp fusion build

### 测试方法
- 测试的是 **Decode Speed** (解码速度)，单位为 tokens/sec，数值越高越好
- 覆盖 4 种上下文长度：16K、65K、131K、262K
- 对比 4 种配置：TurboQuant / TriAttention / MTP / MTP + TriAttention

---

## 核心发现：实测数据

### Decode Speed 对比表（tokens/sec）

| 上下文长度 | TurboQuant | TriAttention | MTP | MTP + TriAttention |
|------------|------------|--------------|-----|--------------------|
| 16K        | **35.37**  | 35.05        | 22.84 | 18.23              |
| 65K        | **34.59**  | 3.43         | 23.14 | 18.33              |
| 131K       | **32.31**  | 30.74        | 21.70 | 16.47              |
| 262K       | 29.41      | **30.09**    | 21.78 | 19.23              |

*波纹表示该配置下的最优值*

### 各配置详情

| 上下文长度 | TurboQuant | TriAttention | MTP | MTP + TriAttention |
|------------|------------|--------------|-----|--------------------|
| 16K        | q8/turbo2 (35.37) | tri q8/turbo2 (35.05) | MTP1 q8/turbo4 (22.84) | MTP1+Tri q8/turbo2 (18.23) |
| 65K        | q8/turbo2 (34.59) | tri q8/turbo2 (3.43)  | MTP1 q4/q4 (23.14)     | MTP1+Tri q8/turbo2 (18.33) |
| 131K       | q8/tbq4 (32.31)   | tri q8/turbo2 (30.74) | MTP1 q8/turbo4 (21.70) | MTP1+Tri q8/turbo2 (16.47) |
| 262K       | q8/tbq4 (29.41)   | tri q8/turbo2 (30.09) | MTP1 q4/q4 (21.78)     | MTP2+Tri q8/turbo2 (19.23) |

### Takeaways（原文）

1. **TurboQuant 是最快的** — 在所有四个上下文长度下均为最优
2. **TriAttention 在 131K 和 262K 时有帮助，但在 65K 时非常慢** — 65K 时仅 3.43 tok/s，接近抛弃
3. **MTP 有效，但在这次短解码测试中未能超越 TurboQuant**

---

## 技术背景解读

### 1. TurboQuant — 量化领域的新选择

**背景**：由 Google Research（Google DeepMind）发布，2026 年 3 月被 ICLR 2026 接收，论文标题为 *TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate* (arXiv:2504.19874)。

**核心原理**：
- 一种**在线向量量化**方法，专门用于 KV Cache 压缩
- **训练无关（training-free）** — 不需要对模型进行微调
- **随机旋转 + 坐标独立量化** — 对高维向量做随机旋转后，利用各坐标独立的 Beta 分布特性，对每个坐标单独应用最优标量量化器
- **3-4 bits KV Cache 压缩**，声称零精度损失，内存减少约 6 倍，注意力计算最高加速 8-13 倍

**开源生态**：
- 最主流的社区实现是 `0xSero/turboquant`，提供 Triton kernels + vLLM 集成，1,300+ stars
- 社区还出现了 `Quansloth` 等向 Unsloth 致敬的本地 GUI 推理工具
- Unsloth 官方尚未原生集成 TurboQuant，但社区已有 llama.cpp 分支实现

**为什么这次实测它能赢**：
TurboQuant 不仅是一种量化方案，更是一套完整的**在线量化管道**：它在保持精度的同时大幅减少了 KV Cache 的内存占用，让模型在稀缺内存的消费级显卡上也能顺利跑起来，而且在各种上下文长度下表现均很稳定。

### 2. TriAttention — 长上下文的 KV 压缩新思路

**背景**：由 MIT CSAIL 的 Weian Mao（毛维安）等人发布，2026 年 4 月出版，论文标题为 *TriAttention: Efficient Long Reasoning with Trigonometric KV Compression* (arXiv:2604.04921)。

**核心原理**：
- 一种**三角级数（Trigonometric Series）KV Cache 压缩**方法
- 专门针对 **RoPE 位置编码**场景中的长上下文推理优化
- 关键发现：在 pre-RoPE 空间中，Query 和 Key 向量在某个稳定非零中心周围高度聚集
- 利用**三角级数**建模这个聚集中心，结合 Q/K norms 作为重要性估计，对 KV cache 进行智能剪枝

**理论性能**：在 AIME25 32K-token 生成任务上，可达 **2.5倍吞吐量提升 + 10.7 倍 KV 内存压缩**，精度与 Full Attention 持平。

**为什么在本次测试中表现嵪峪**：
TriAttention 是一个**专为超长上下文设计**的方案。在这次测试中：
- 16K 时和 TurboQuant 差距很小：35.05 vs 35.37 tok/s
- **65K 时突然坎塔到 3.43 tok/s** — 这说明在某个中等上下文长度，TriAttention 的压缩策略可能触发了效率盲区，或者 llama.cpp 社区实现尚有细节需要优化
- 131K 和 262K 时回归正常，甚至在 262K 时超越 TurboQuant（30.09 vs 29.41）

这意味着 TriAttention 可能有一个**最佳工作区间**，在超长上下文下优势明显，但在短/中等上下文下需要慎重配置。

### 3. MTP — 内置投机解码

**背景**：Multi-Token Prediction（多 Token 预测）是 Qwen 3.5/3.6 系列模型的内置能力。传统模型只预测下一个 token，而 MTP 在训练阶段让模型同时学习预测未来多个位置的 token。

**推理阶段的妙用**：
- 在推理时，这些辅助预测头被复用为**内置的投机解码草稿路径**
- 无需额外下载草稿模型，目标模型自身就是草稿模型
- llama.cpp 已经在 PR #22673 中正式支持 MTP 投机解码

**理论性能**：社区实测显示 Qwen 3.6 系列通常可达 **1.5倍–2.5倍**的解码加速，Qwen 3.6 35B A3B 在 12GB VRAM 上通过 MTP 可达约 80 tok/s。

**为什么未能超越 TurboQuant**：
原文已经给出了合理解释："这是一次**short decode test**。" MTP 的核心优势是通过减少对主模型的调用次数来提升速度，但在短文本生成中，投机解码的接受率可能不足以形成明显优势。在更长的生成任务中，MTP 应该会更有价值。

---

## 幾点深度观察

1. **消费级硬件能跑 35B MoE 是有可能的**  
   RTX 3060 是一款 2021 年发布的老卡，内存仅有 12GB。但通过量化优化（MXFP4_MoE），在本地跑起 35B 活跃参数的 MoE 模型，解码速度还能维持在 20–35 tok/s 的可用水平。这对本地 AI 部署是一个很大的利好信号。

2. **TurboQuant 的“训练无关”特性是其最大杀手锊**  
   对普通用户来说，TurboQuant 不需要改动模型、不需要重新训练，只需要在推理端开启压缩即可。这大大降低了使用门槛。

3. **不同技术有不同的最佳工作区间**  
   - TurboQuant — “通用解”，适用于大多数场景
   - TriAttention — “长上下文专精”，在超长上下文下优势突出，但在短/中等上下文中可能出现效率盲区
   - MTP — “长生成加速器”，在短解码中优势不大，但在长文本生成中可观

4. **量化配置的细节很重要**  
   从配置详情可见，同一种技术在不同上下文下可能采用不同的量化组合（如 TurboQuant 在 131K/262K 用 q8/tbq4，而短上下文用 q8/turbo2）。这说明本地部署时量化参数的调试至关重要。

---

## 实际应用建议

如果你也想在本地部署 Qwen 3.6 等大模型并获得最佳速度：

1. **首选 TurboQuant** — 它在所有测试场景下都是最稳定、最快的选择
2. **如果你主要做超长文本生成（>100K context）** — 可以关注 TriAttention，但需要测试是否触发中短上下文的效率盲区
3. **如果你做长文本生成且有足够 VRAM** — 开启 MTP 作为投机解码，在长生成中可能获得额外加速
4. **硬件越弱，量化越重要** — 这次测试的 12GB VRAM 是很有参考价值的上限，说明量化技术的进步正在不断扩大本地 LLM 的可用范围

---

## 参考链接

- 原帖：https://x.com/italianclownz/status/2054301170605113438
- TurboQuant 论文：https://arxiv.org/abs/2504.19874
- TurboQuant 社区实现：https://github.com/0xSero/turboquant
- TriAttention 论文：https://arxiv.org/abs/2604.04921
- TriAttention GitHub：https://github.com/WeianMao/triattention
- MTP llama.cpp PR：https://github.com/ggml-org/llama.cpp/pull/22673

---

*来自翠冷翠*
