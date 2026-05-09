# 更稀疏、更快速、更轻量的 Transformer 语言模型

> Sakana AI 与 NVIDIA 合作研究：通过利用非结构化稀疏性，在保持模型性能的同时实现 20%+ 的训练和推理加速

---

## 执行摘要

Sakana AI 与 NVIDIA 联合发表了一项突破性研究，展示如何通过硬件感知的稀疏性优化，在不牺牲模型性能的前提下显著提升 LLM 的效率。研究团队开发了名为 **TwELL (Tile-wise ELLPACK)** 的新型稀疏数据格式和配套的 CUDA 内核，成功将理论上的稀疏性转化为实际的 wall-clock 加速。

**核心成果**：
- 使用简单 L1 正则化可诱导 **99%+ 的稀疏性**，对下游任务性能影响微乎其微
- H100 GPU 上实现 **20%+ 的训练和推理加速**
- 显著降低能耗和内存需求
- 论文已被 **ICML 2026** 接收

---

## 核心洞察

### 【为什么这是一个重要突破】

**人脑启发的效率原理**：人脑极其高效，因为它只激活特定思考所需的神经元。现代 LLM 也试图这样做——超过 95% 的前馈层神经元在处理任何给定词汇时保持静默。但问题在于：**当前硬件惩罚了这种稀疏性**。

**深度学习中最令人沮丧的悖论**：让模型做更少的数学运算反而会让它运行得更慢。为什么？因为非结构化的稀疏性会引入不规则的内存访问模式，而 GPU 是为可预测的密集数学块设计的。

**Sakana AI 与 NVIDIA 的解决方案**：与其强迫 GPU 适应稀疏性，不如重新塑造稀疏性以适应 GPU。研究团队构建了一种"混合"格式，让稀疏性适配 GPU 的执行流水线。

---

## 技术创新详解

### 1. TwELL：为 GPU 量身定制的稀疏格式

**传统 ELLPACK 的局限**：
- 按整行打包数据，与现代 GPU 的 tiled 矩阵乘法执行结构不匹配
- 需要额外的 kernel 启动来转换激活值
- 引入额外的全局内存访问开销

**TwELL 的核心改进**：
- 将列划分为大小为 T 的水平 tile
- 在每个 tile 内使用局部 ELL 风格布局存储非零值和索引
- **关键优势**：CTA 可以直接为其负责的 tile 构建 TwELL 表示，无需跨 CTA 同步
- 完美匹配现代 dense matmul kernel 的计算结构

**存储结构**：
```
存储矩阵：
- hv: 局部对齐的值 (M × N/C)
- hI: 索引 (M × N/C)
- hnz: 每 tile 的非零元素数量 (M × ⌈N/T⌉)

其中 C 是压缩因子，确保 T/C 大于任何 tile 中的最大非零数
```

### 2. 定制 CUDA Kernels

**推理 Kernel**：
- 融合 up projection 和 down projection
- 每个 CTA 处理一行，将输入值加载到寄存器内存
- 双层循环遍历稀疏 gate 激活：外层遍历 column tiles，内层遍历每个 tile 的非零元素
- 分配单个 warp (32 线程) 给每个 CTA，最大化并发性
- 通过 warp-shuffling 指令实现快速数据交换和累加
- **优势**：避免物化 dense 隐藏激活，跳过所有不必要的计算和全局内存访问

**训练 Kernels**：
- 将 TwELL 转换为轻量级混合表示 (hybrid representation)
- 把每行的局部对齐 tiles 融合成单个全局对齐矩阵
- 对超出上限的少数溢出情况路由到 dense 备份矩阵
- 专门实现 hybrid-to-dense 和 dense-to-hybrid 矩阵乘法
- 在反向传播中完全通过稀疏和混合 kernels 计算梯度，无需任何 dense-to-dense 矩阵乘法
- **设计哲学**：牺牲融合执行的好处，换取最小化内存流量和重计算，最大化整个反向传播的吞吐量

---

## 实验结果

### 训练性能

**模型设置**：
- 在十亿参数规模上训练 LLM
- 使用不同 L1 正则化强度控制稀疏性级别
- 在 7 个流行的下游任务上评估

**关键发现**：

| 指标 | 结果 |
|------|------|
| 无正则化模型的天然稀疏性 | < 20% 非零激活 |
| L1=2×10⁻⁵ 时的稀疏性 | 可达 99%+ |
| 下游任务性能影响 | 基本不变 |
| 训练加速 (1.5B 模型) | 最高 24% |
| 峰值 GPU 内存减少 | 超过 24% |
| 推理加速 | 最高 30% |
| 能耗节省 | GPU 功耗降低 3%+ |

**稀疏性的自适应特性**：
- 稀疏模式保持高度异构性
- 少量 token 激活的神经元数量是平均值的 100 倍以上
- 稀疏模型能够自适应地在最需要的地方重新分配计算容量

### 规模化分析

**跨模型规模的一致性结果** (固定 L1=2×10⁻⁵)：

| 模型规模 | 非零激活减少 | 推理加速 | 训练加速 |
|----------|-------------|---------|---------|
| 0.5B → 2B | 38% ↓ | 20.5% ↑ | 21.9% ↑ |

**重要观察**：
- 更大的模型在支持稀疏性方面变得更有效
- 所有吞吐量和内存收益随模型规模增长
- 2B 稀疏模型可容纳双倍的 micro-batch 大小进行训练

---

## 深层思考

### 【为什么这对 AI 基础设施很重要】

1. **成本结构的改变**：训练和推理成本是 LLM 普及的主要瓶颈。20%+ 的效率提升直接转化为显著的成本节约。

2. **环保角度**：AI 训练的碳足迹日益受到关注。能耗降低 3%+ 在大规模部署中具有实际意义。

3. **边缘部署的可能**：内存需求降低 24% 意味着更大的模型可以在更小的硬件上运行，这对移动端和边缘 AI 部署至关重要。

4. **硬件-算法协同设计**：这项工作展示了当算法研究者与硬件工程师深度合作时可以取得的突破。TwELL 不是一个通用的稀疏格式，而是专门为现代 GPU 的 tiled 执行模型设计的。

### 【未来研究方向】

- 扩展到更新的 GPU 架构 (如 Blackwell)
- 与其他压缩技术 (量化、剪枝) 的结合
- 稀疏性对长上下文建模的影响
- 自动学习最优稀疏性级别的方法

---

## 技术规格

### 论文信息
- **标题**: Sparser, Faster, Lighter Transformer Language Models
- **作者**: Edoardo Cetin, Stefano Peluchetti, Emilio Castillo, Akira Naruse, Mana Murakami, Llion Jones
- **机构**: Sakana AI, NVIDIA
- **会议**: ICML 2026
- **arXiv**: [2603.23198](https://arxiv.org/abs/2603.23198)

### 资源链接
- **论文**: https://arxiv.org/abs/2603.23198
- **博客**: https://pub.sakana.ai/sparser-faster-llms/
- **代码**: https://github.com/SakanaAI/sparser-faster-llms

### 引用格式 (BibTeX)
```bibtex
@article{sakanaXnvidia2026sparser,
  title={Sparser, Faster, Lighter Transformer Language Models},
  author={Cetin, Edoardo and Peluchetti, Stefano and Castillo, Emilio and Naruse, Akira and Murakami, Mana and Jones, Llion},
  journal={arXiv preprint arXiv:2603.23198},
  year={2026}
}
```

---

## 关键概念解释

**前馈层 (Feedforward Layers)**：Transformer 架构中每个 token 独立处理的部分，负责将注意力层的输出投影到更高维度再压缩回来，通常是模型中参数和计算量最大的部分。

**非结构化稀疏性 (Unstructured Sparsity)**：矩阵中非零元素的分布没有固定模式，与结构化稀疏性（如固定比例的通道剪枝）相对。

**Tiled 矩阵乘法**：GPU 中一种优化技术，将大矩阵乘法分解为小块 (tiles) 的处理，最大化数据复用和内存访问效率。

**CTA (Cooperative Thread Arrays)**：CUDA 中在单个 Streaming Multiprocessor (SM) 上调度执行的线程组。

**Warp**：32 个线程组成的执行单元，在现代 GPU 上以 SIMT (Single Instruction, Multiple Thread) 方式执行相同指令。

---

## 相关研究

这项研究建立在大量前期工作之上：

1. **The Lazy Neuron Phenomenon** (Li et al., 2022) - 发现 Transformer 中激活稀疏性的涌现
2. **ReLU Strikes Back** (Mirzadeh et al., 2023) - 利用 LLM 中的激活稀疏性
3. **Deja Vu** (Liu et al., 2023) - 上下文稀疏性用于高效推理
4. **ELLPACK/ELL 格式** - GPU 稀疏矩阵计算的经典数据格式

---

## 结论

这项研究成功解决了深度学习中的一个核心悖论：如何让稀疏性在 GPU 上真正加速而不是减速。通过 TwELL 格式和配套的内核，Sakana AI 和 NVIDIA 展示了硬件-算法协同设计的强大潜力。随着模型规模持续增长，稀疏性可能成为与模型大小和训练数据同等重要的效率优化维度。

研究团队承诺将开源所有内核代码，这将促进硬件感知算法和高效 LLM 的未来研究。

---

*整理时间: 2026年5月9日*  
*来源: hardmaru (@hardmaru) / X*  
*论文: Sakana AI × NVIDIA ICML 2026*

来自翡冷翠
