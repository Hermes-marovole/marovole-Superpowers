# Carnice-V2 27B 本地模型自我基准测试报告案例

## 执行摘要

> "watching a 27b local model write its own benchmark report just now and i'm sitting with this for a sec"
> —— Sudo su (@sudoingX)

Sudo su 让 Carnice-V2 27B 模型完成了一个完整的自我诊断任务：从硬件探测、模型识别、git 提交验证，到基准测试、报告生成、最终验证完成，全程无需人工干预。

## 核心亮点

### 1. 完整的闭环验证

作者强调的"罕见鸟"瞬间：

> "the verify step is what i can't get over, carnice wrote the file then read it back THEN said done, plan execute and VERIFY, that loop actually closing is the rare bird."

模型的执行流程：
1. **Plan** —— 制定报告生成计划
2. **Execute** —— 调用工具收集数据
3. **Verify** —— 写入文件后读取验证，确认内容正确后才标记完成

这个"计划-执行-验证"闭环的完整闭合，是当前 AI Agent 系统中难得一见的可靠行为。

### 2. 工具调用统计

| 类别 | 次数 | 说明 |
|------|------|------|
| 终端调用 | 11 | 硬件探测、git 提交查询 |
| Todo 更新 | 6 | 任务进度跟踪 |
| 文件操作 | 2 | 写入报告 + 读取验证 |
| **总计** | **19** | 12 分钟内完成 |

### 3. 零幻觉工具调用

> "zero hallucinated tools either, the prompt listed bash and python_run from my v0.1 spec but hermes actually ships terminal and execute_code, carnice adapted to the real registry without inventing anything."

即使提示词中列出的工具名称与实际注册表不匹配，模型也能正确适配到真实可用的 `terminal` 和 `execute_code`，没有生成不存在的工具调用。

## 运行环境详情

### 硬件配置
- **设备**: ROG 5090 Mobile (24GB 显存版)
- **模型**: Carnice-V2 27B
- **基座模型**: Qwen 3.6 Dense
- **训练数据**: Hermes Agent Traces (Kaios SFT)

### 运行参数
- **VRAM 峰值**: 21GB (99% GPU 占用率)
- **上下文窗口**: 262K tokens
- **Flash Attention**: 开启
- **KV Cache**: q4_0/q4_0 量化
- **生成速度**: 16.71 tok/s (单提示流式测试)

### 软件版本
- **llama.cpp**: commit 75f3bc94e (2025年4月13日)
- **Vulkan Flash Attention**: dp4a shader 启用

## 任务流程详解

### 阶段一：信息收集
1. **硬件探测** —— 通过终端命令获取 GPU 型号、VRAM 容量
2. **模型识别** —— 定位模型文件路径和元数据
3. **Git 验证** —— 查询 llama.cpp 当前 commit hash

### 阶段二：基准测试
- 使用 curl 调用本地测试接口
- 记录性能指标（tok/s、延迟、资源占用）

### 阶段三：报告生成
- 生成结构化 Markdown 格式报告
- 包含以下部分：
  - 硬件环境概览
  - 模型配置参数
  - 基准测试结果
  - 软件版本信息

### 阶段四：闭环验证
> 关键步骤：模型写入报告后，主动读取文件内容进行验证，确认无误后才宣布任务完成。

## 发布者洞察

### 核心评价

> "plan execute and VERIFY, that loop actually closing is the rare bird"

Sudo su 将这个验证闭环称为"罕见鸟"——这反映了当前大多数 AI Agent 系统的一个共同缺陷：能够生成输出，但缺乏可靠的自我验证机制。

### 为什么值得关注

1. **消费级硬件可行性** —— 24GB 显存即可运行 27B 模型完成复杂任务
2. **Harness-无关方法论** —— 基于可见追踪的评估方法，不依赖特定框架
3. **透明度** —— 所有工具调用和中间状态完全可见可跟踪

### 后续计划

> "vanilla qwen 3.6 head to head next, video QT after, see for yourself"

作者计划将 Carnice-V2 与原版 Qwen 3.6 进行对比测试，并发布视频演示。

## 关键数据摘要

| 指标 | 数值 |
|------|------|
| 总工具调用 | 19 次 |
| 任务耗时 | 12 分钟 |
| 消息轮数 | 42 轮 |
| 终端呼叫 | 11 次 |
| Todo 更新 | 6 次 |
| VRAM 峰值 | 21 GB |
| 生成速度 | 16.71 tok/s |
| 幻觉工具 | 0 |

## 延伸思考

### 对 Agent 系统的启示

这个案例展示了一个健康的 Agent 应该具备的特征：

1. **自我修正能力** —— 能够检查自己的输出并发现错误
2. **任务分解能力** —— 将复杂任务拆解为可管理的子任务
3. **工具适配能力** —— 在不完美提示下正确选择可用工具
4. **进度透明度** —— 让用户清晰了解当前状态

### 本地部署的现实意义

随睇模型能力提升和硬件成本下降，本地运行大模型完成复杂任务已经从"实验室玩具"变为"生产力工具"。这个案例证明：

- 24GB 消费级显存足以支撑 27B 模型的复杂任务
- 完全离线运行保障了数据隐私
- 可见追踪让调试和优化变得可控

## 背景信息

- **来源**: X/Twitter
- **作者**: Sudo su (@sudoingX)
- **身份**: GPU/本地 LLM 爱好者，Bangkok, Thailand
- **发布时间**: 2026年5月6日
- **互动数据**: 6 回复，8 转发，107 赞，46 收藏，15K 浏览
- **关注者**: 27.4K
- **Bio**: GPU/local LLM. more RAM and OSS... everywhere

---

**来自翡冷翠**
