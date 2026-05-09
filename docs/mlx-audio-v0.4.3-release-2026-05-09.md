# mlx-audio v0.4.3 发布详解

## 执行摘要

Prince Canuma（mlx-audio 与 mlx-vlm 创始人）于 2026 年 5 月 9 日发布了 mlx-audio v0.4.3。这是一次模型、服务器架构与开发体验全面升级的重大版本，带来 6 个全新 TTS 模型、服务器并发优化、实时语音加速等一系列重磅更新。本次发布共有 14 位贡献者参与，其中 8 位为新加入的贡献者。

---

## 核心亮点

### 🎧 六大全新 TTS 模型

| 模型 | 亮点 |
|------|------|
| **Higgs Audio v2** | 支持声音克隆 |
| **OmniVoice** | 覆盖 646+ 种语言 |
| **LongCat-AudioDiT 1B** | 大规模语音合成 |
| **MOSS-TTS-Nano** | 轻量级文本转语音 |
| **Irodori-TTS v2** | 日语 TTS 增强 |
| **MeloTTS-English** | 英语语音合成优化 |

### 🎵 Mel-Band-RoFormer 人声分离

新增 Mel-Band-RoFormer 支持，用于专业级的人声与伴奏分离处理，适用于清唱提取、混音后处理等场景。

### ⚡ 服务器性能飞跃

- **并发请求处理**：支持同时处理多个客户端请求
- **Qwen3 TTS 连续批处理**：显著提升高并发场景下的吞吐量
- **客户端断开处理**：增加网络异常时的鲁棒性

### 🚀 实时语音加速

**Voxtral Realtime** 在 4-bit 量化模式下实现约 **3 倍速度提升**，大幅改善实时对话体验。

### 📚 长文本与批处理优化

- **Parakeet TDT**：长文本表现显著改进
- **Fish Speech S2 Pro**：新增批处理支持，提升大规模生成效率

### 🧘 依赖精简

移除了 5 个外部依赖包：
- `librosa`
- `soundfile`
- `pyloudnorm`
- `pydub`
- `tiktoken`

这使得安装更轻量、部署更快捷、冲突风险更低。

### 🌐 WebM 音频支持

新增对 WebM 格式的原生支持，无需转码即可直接处理 WebM 音频。

---

## 快速开始

```bash
uv pip install -U mlx-audio
```

官方 GitHub 仓库：https://github.com/Blaizzy/mlx-audio

---

## 贡献者

本次发布共 14 位贡献者参与，其中 8 位为新加入的贡献者。特别感谢本次发布的三位 MVP 贡献者：

- [@lllucas](https://x.com/lllucas)
- [@KarnikShreyas](https://x.com/KarnikShreyas)
- [@beshkenadze](https://x.com/beshkenadze)

---

## 关于 mlx-audio

mlx-audio 是基于 Apple MLX 框架的音频处理工具库，专为 Apple Silicon 优化。它支持文本转语音（TTS）、语音识别、音频处理等多种功能，是 macOS 开发者本地部署 AI 音频应用的首选工具之一。

---

*来自翡冷翠*
