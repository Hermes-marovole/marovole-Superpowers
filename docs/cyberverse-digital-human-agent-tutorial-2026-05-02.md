# CyberVerse：开源数字人 Agent 平台完整指南

> 来源：[ahhhhfs @abskoop](https://x.com/abskoop/status/2050227450144338002) / [GitHub: dsd2077/CyberVerse](https://github.com/dsd2077/CyberVerse)
> 整理时间：2026-05-02
> 来自翡冷翠

---

## 简介

**CyberVerse** 是一个开源数字人 Agent 平台，支持通过一张照片生成可实时视频通话的 AI 角色。它提供完整的 LLM/TTS/ASR 模块替换能力，适合开发者研究多模态 AI 交互与自托管数字人系统。

> 想拥有自己的 J.A.R.V.I.S. 吗？一个能真正看见你、听见你、并实时回应的 AI？
> 
> **只需一张照片，CyberVerse 就能让他们活过来。**

---

## 核心特性总览

| 特性 | 说明 |
|------|------|
| **实时视频通话** | 非预录制、非回合制，支持无限时长的低延迟视频对话，首帧延迟约 1.5 秒 |
| **Agent 能力** | 不只是能对话的头像，而是真正能干事的 AI Agent |
| **一张照片即活** | 上传单张照片即可创建数字人，支持实时面部动画、自然唇形同步、呼吸微动作 |
| **模块化组装** | 大脑、面容、声音、耳朵——每个组件都是可替换插件，通过 YAML 配置混搭 LLM、TTS、ASR 和头像后端 |

---

## 演示视频

| Alice | Lina |
|-------|------|
| [![](https://github.com/dsd2077/CyberVerse/raw/main/docs/assets/爱丽丝.mov.png)](https://youtu.be/Lk88sew2x4o) | [![](https://github.com/dsd2077/CyberVerse/raw/main/docs/assets/丽娜.mov.png)](https://youtu.be/8jdQ3ThcwgA) |
| [**Alice — YouTube 观看**](https://youtu.be/Lk88sew2x4o) | [**Lina — YouTube 观看**](https://youtu.be/8jdQ3ThcwgA) |

| 小龙女 |
|--------|
| [![](https://github.com/dsd2077/CyberVerse/raw/main/docs/assets/小龙女.mov.png)](https://youtu.be/WjEHUYZx5Gs) |
| [**Xiaolongnü — YouTube 观看**](https://youtu.be/WjEHUYZx5Gs) |

---

## 硬件要求

实时视频对话需要 GPU 加速。以下为 FlashHead 和 LiveAct 头像模型的基准测试：

| 模型 | 画质 | GPU | 数量 | 分辨率 | FPS | 实时？ |
|------|------|-----|------|--------|-----|--------|
| FlashHead 1.3B | Pro | RTX 5090 | 2 | 512×512 | 25+ | ✅ |
| FlashHead 1.3B | Pro | RTX PRO 6000 | 1 | 512×512 | 20 | ✅ |
| FlashHead 1.3B | Pro | RTX 4090 | 1 | 512×512 | ~10.8 | ❌ |
| FlashHead 1.3B | Lite | RTX 4090 | 1 | 512×512 | 25+ | ✅ |
| LiveAct 18B | — | RTX PRO 6000 | 2 | 320×480 | 20 | ✅ |
| LiveAct 18B | — | RTX PRO 6000 | 1 | 256×417 | 20 | ✅ |

> **Pro** 偏向视觉质量；**Lite** 偏向速度。更多 GPU 余量可提升画质；硬件紧张时需降低设置（分辨率、Pro/Lite 等）以保持实时。

---

## 快速开始

### 前置条件

- Node 18+
- Go 1.25（需要 `protoc-gen-go`, `protoc-gen-go-grpc`）
- 支持 CUDA 12.8+ 的 GPU
- FFmpeg（必须包含 `libvpx` 用于视频编码）
- Conda
- Python 3.10+
- PyTorch 2.8 (CUDA 12.8)

验证命令：
```bash
node --version
go version
protoc --version
ffmpeg -version | grep libvpx
conda --version
```

---

### 安装步骤

#### Step 1: 克隆仓库

```bash
git clone https://github.com/dsd2077/CyberVerse.git
cd CyberVerse
```

#### Step 2: 创建 Python 环境

```bash
conda create -n cyberverse python=3.10
conda activate cyberverse

# 安装 PyTorch (CUDA 12.8)
pip3 install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```

#### Step 3: 配置环境变量

```bash
cp infra/.env.example .env
```

编辑 `.env`，填入 API 密钥：
```
DOUBAO_ACCESS_TOKEN=your_doubao_token   # 字节跳动豆包语音 LLM
DOUBAO_APP_ID=your_doubao_app_id
```

> 豆包语音：按 [Volcengine 快速开始](https://www.volcengine.com/docs/6561/2119699?lang=zh) 获取 **App ID** / **API Key** → 填入 `DOUBAO_APP_ID` / `DOUBAO_ACCESS_TOKEN`

服务运行后，可在 Web UI 的 **`/settings`** 页面修改这些值，无需只编辑 `.env`

#### Step 4: 下载模型权重

CyberVerse 目前支持 **FlashHead** 和 **LiveAct**；按需下载即可。

```bash
pip install "huggingface_hub[cli]"
```

**FlashHead (SoulX-FlashHead)**

| 模型组件 | 说明 | 链接 |
|----------|------|------|
| `SoulX-FlashHead-1_3B` | 1.3B FlashHead 权重 | [Hugging Face](https://huggingface.co/Soul-AILab/SoulX-FlashHead-1_3B), [ModelScope](https://modelscope.cn/models/Soul-AILab/SoulX-FlashHead-1_3B) |
| `wav2vec2-base-960h` | 音频特征提取器 | [Hugging Face](https://huggingface.co/facebook/wav2vec2-base-960h) |

```bash
# 中国大陆用户可先用镜像：
# export HF_ENDPOINT=https://hf-mirror.com

huggingface-cli download Soul-AILab/SoulX-FlashHead-1_3B \
  --local-dir ./checkpoints/SoulX-FlashHead-1_3B

huggingface-cli download facebook/wav2vec2-base-960h \
  --local-dir ./checkpoints/wav2vec2-base-960h
```

**LiveAct (SoulX-LiveAct)**

| 模型名 | 下载 |
|--------|------|
| SoulX-LiveAct | [Hugging Face](https://huggingface.co/Soul-AILab/LiveAct), [ModelScope](https://modelscope.cn/models/Soul-AILab/LiveAct) |
| chinese-wav2vec2-base | [Hugging Face](https://huggingface.co/TencentGameMate/chinese-wav2vec2-base) |

```bash
huggingface-cli download Soul-AILab/LiveAct \
  --local-dir ./checkpoints/LiveAct

huggingface-cli download TencentGameMate/chinese-wav2vec2-base \
  --local-dir ./checkpoints/chinese-wav2vec2-base
```

#### Step 5: 更新配置

编辑 `cyberverse_config.yaml`，更新模型路径：

```yaml
inference:
  avatar:
    default: "flash_head"               # 选择启动的头像模型
    runtime:
      cuda_visible_devices: 0      # 共享 GPU ID，多卡如 0,1
      world_size: 1                # 共享 GPU 数量，双卡设为 2
    flash_head:
      checkpoint_dir: "./checkpoints/SoulX-FlashHead-1_3B"
      wav2vec_dir: "./checkpoints/wav2vec2-base-960h"
      model_type: "lite"           # "pro" 更高画质（需更多 GPU）
      # ... 其他参数
    live_act:
      ckpt_dir: "./checkpoints/LiveAct"
      wav2vec_dir: "./checkpoints/chinese-wav2vec2-base"
      # ... 其他参数
```

#### Step 6: 安装 SageAttention & FlashAttention（可选）

```bash
# SageAttention（源码构建）
git clone https://github.com/thu-ml/SageAttention.git
cd SageAttention
export EXT_PARALLEL=4 NVCC_APPEND_FLAGS="--threads 8" MAX_JOBS=32
python setup.py install

# FlashAttention（可选）
pip install ninja
pip install flash_attn==2.8.0.post2 --no-build-isolation
```

> 编译慢可从 [flash-attention releases](https://github.com/Dao-AILab/flash-attention/releases/tag/v2.8.0.post2) 下载预构建 wheel

#### Step 7: 安装项目依赖

```bash
make setup
```

这将安装基础 editable 包、生成 gRPC stubs、安装前端依赖。

```bash
# 安装所有可选依赖
pip install -e ".[all]"

# 或按需选择：
pip install -e ".[voice_llm,flash_head]"
pip install -e ".[live_act]"
```

#### Step 8: 启动服务（3 个终端）

**终端 1** — Python 推理服务：
```bash
conda activate cyberverse
make inference
```

等待直到看到：
- `Active avatar model initialized: <model_name>`
- `CyberVerse Inference Server started on port 50051`

**终端 2** — Go API 服务：
```bash
make server
```

**终端 3** — 前端：
```bash
make frontend
```

#### Step 9: 验证

```bash
# 检查 API 健康
curl -s http://localhost:8080/api/v1/health
```

**检查 8443/TCP 连通性（远程访问）**

当 `streaming_mode: direct` 使用内置 TURN 服务器时，浏览器必须能访问服务器的 `8443/TCP`：

```bash
nc -vz <server-ip> 8443
```

若 8443 不通，可通过 SSH 隧道转发：
```bash
ssh -L 8443:127.0.0.1:8443 user@host -p port
```

要让浏览器直接连接远程服务器而非 SSH 隧道，在 `cyberverse_config.yaml` 中设置 `pipeline.ice_public_ip` 为服务器的公网 IP 或域名。

浏览器打开 [http://localhost:5173](http://localhost:5173/) — 即可开始使用。

---

## 路线图

### 1. 数字人创建平台

- 角色 CRUD（多参考图、活动图、显示模式、人脸裁剪、标签、语音字段、个性、欢迎语、系统提示词）
- 实时头像视频（通过可配置头像插件如 FlashHead、LiveAct）
- WebRTC 实时音视频（直连 P2P 或 LiveKit SFU）
- 可插拔模块（头像、语音 LLM、LLM、TTS、ASR）
- 会话管理：每角色聊天记录持久化
- 语音克隆：支持豆包语音克隆
- 混合输入：同一对话支持语音和文字
- 语音打断、会话暂停/恢复
- 知识导入：支持文档和传记材料用于角色 RAG 问答
- 面对面：用户端摄像头输入，理解动作、手势等视觉线索
- 开发者嵌入：Web 组件或 SDK 集成自托管实例
- 直播输出：音视频广播场景

### 2. 数字人作为 Agent

- **记忆系统**：跨会话长期记忆，集成角色知识库和 RAG
- 工具使用和函数调用
- 工作流执行和任务完成

### 3. Agent 网络

- Agent 间通信
- 多 Agent 协作和委托
- Agent 间共享内存和知识
- 构建开放的互联 Agent 网络

---

## 技术栈与依赖

### 涉及技术
- **Python 3.10+** — 推理后端
- **Go 1.25** — API 服务
- **Node.js 18+** — 前端
- **PyTorch 2.8** — 深度学习框架
- **WebRTC / Pion** — 实时通信
- **gRPC** — 服务间通信
- **Conda** — 环境管理

### 核心模型
- **SoulX-FlashHead** — 1.3B 参数头像模型（Soul AI Lab）
- **SoulX-LiveAct** — 18B 参数头像模型（Soul AI Lab）
- **wav2vec2** — 音频特征提取

### 许可证
GNU General Public License v3.0

---

## 相关资源

| 资源 | 链接 | 说明 |
|------|------|------|
| GitHub 仓库 | https://github.com/dsd2077/CyberVerse | 源码和文档 |
| FlashHead 模型 | https://huggingface.co/Soul-AILab/SoulX-FlashHead-1_3B | 1.3B 头像模型 |
| LiveAct 模型 | https://huggingface.co/Soul-AILab/LiveAct | 18B 头像模型 |
| SoulX-FlashHead | https://github.com/Soul-AILab/SoulX-FlashHead | 头像模型项目 |
| SoulX-LiveAct | https://github.com/Soul-AILab/SoulX-LiveAct | 头像模型项目 |
| Pion WebRTC | https://github.com/pion/webrtc | Go WebRTC 实现 |
| 豆包语音文档 | https://www.volcengine.com/docs/6561/2119699 | Volcengine API |

---

## 快速参考

### 常用命令

```bash
# 环境激活
conda activate cyberverse

# 启动推理服务
make inference

# 启动 API 服务
make server

# 启动前端
make frontend

# 一键安装依赖
make setup

# 健康检查
curl -s http://localhost:8080/api/v1/health

# SSH 隧道（远程 TURN）
ssh -L 8443:127.0.0.1:8443 user@host -p port
```

### 配置要点

```yaml
# cyberverse_config.yaml 关键字段
checkpoint_dir: "./checkpoints/SoulX-FlashHead-1_3B"  # 模型路径
model_type: "lite"                                    # pro/lite 画质选择
cuda_visible_devices: 0                               # GPU 设置
```

---

*来自翡冷翠*
