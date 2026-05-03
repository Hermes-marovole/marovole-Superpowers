# Rapid-MLX: Apple Silicon Mac 本地 LLM 推理服务

> 来源：[Geek Lite @QingQ77](https://x.com/QingQ77/status/2050792213727056262)
> 整理时间：2026-05-03
> 来自翠冷翠

---

## 简介

**Rapid-MLX** 是一个基于 Apple MLX 框架的本地 LLM 推理服务，通过 FastAPI 提供 OpenAI 兼容 API。在 Apple Silicon Mac 上，性能比 Ollama 和 llama.cpp 快 2-4 倍，同时原生支持工具调用、提示缓存、多模态等高级功能。

---

## 核心亮点

### 性能优势
- **比 Ollama 快 2-4 倍** - 基于 Apple 原生 MLX 框架优化
- **TTFT 0.08 秒** - 通过 KV 缓存裁剪和 DeltaNet 状态快照大幅压缩首次输出时间

### 功能特性
| 功能 | 说明 |
|------|------|
| **OpenAI 兼容 API** | FastAPI 提供 `/v1/chat/completions` 等标准端点 |
| **工具调用 (Tool Calling)** | 内置 17 种解析器，自动识别 Qwen、DeepSeek、Gemma、GLM 等模型格式 |
| **提示缓存** | 原生支持提示缓存，减少重复计算 |
| **量化自动修复** | 检测到量化损坏输出时自动恢复 |
| **多模态** | 支持视觉、音频等多模态输入 |
| **V 缓存压缩** | 重复语义压缩，降低内存占用 |
| **推理链分离** | 支持运行时开关推理量化级别 |
| **云端路由** | 可跟云端 LLM 模型组合使用 |

### 兼容工具
Rapid-MLX 可直接对接以下 AI 编程工具：
- **Cursor** - AI 代码编辑器
- **Claude Code** - Anthropic 官方 CLI 工具
- **Aider** - AI 对编程助手
- **LangChain** - LLM 应用框架

---

## 技术原理

### MLX 框架
MLX 是 Apple 专为 Apple Silicon 设计的机器学习框架，特点包括：
- 统一内存模型（无需在 CPU/GPU 间复制数据）
- 动态图编译
- 高效率的石墨笔处理器支持

### KV 缓存优化
- **KV 缓存裁剪** - 智能剪枝，保留关键上下文
- **DeltaNet 状态快照** - 快速恢复对话状态

---

## 安装与使用

### 安装方法

```bash
# 从 GitHub 下载
git clone https://github.com/raullenchai/Rapid-MLX.git
cd Rapid-MLX

# 安装依赖
pip install -r requirements.txt

# 启动服务
python server.py
```

### API 调用示例

```python
import openai

# 配置本地 Rapid-MLX 端点
client = openai.OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"
)

# 聊天完成
response = client.chat.completions.create(
    model="mlx-model",
    messages=[{"role": "user", "content": "Hello!"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather information"
        }
    }]
)
```

---

## 支持的模型

Rapid-MLX 自动识别并适配以下模型家族的工具调用格式：
- **Qwen** - 阿里通义千问系列
- **DeepSeek** - DeepSeek Coder/V2 系列
- **Gemma** - Google 开源模型
- **GLM** - 智谱 ChatGLM 系列

---

## 资源汇总

### GitHub 仓库
| 项目 | 链接 | 说明 |
|------|------|------|
| Rapid-MLX | https://github.com/raullenchai/Rapid-MLX | 主仓库 |

### 相关技术
| 技术 | 链接 | 说明 |
|------|------|------|
| MLX | https://github.com/ml-explore/mlx | Apple 机器学习框架 |
| FastAPI | https://fastapi.tiangolo.com | 高性能 Web 框架 |

### 值得关注
- **@QingQ77 (Geek Lite)** - 定期分享最新 AI 开发工具和技术

---

## 适用场景

1. **本地 AI 编程** - 与 Cursor/Claude Code/Aider 配合使用
2. **私有 LLM 部署** - 企业内部本地化部署
3. **低延迟应用** - 需要快速响应的实时应用
4. **边缘计算** - Mac Studio/MBP 作为 LLM 推理节点

---

*来自翠冷翠*
