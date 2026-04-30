# Hermes Agent 配置 GPT-image-2 生图功能完整教程

> 来源：[AI产品黄叔 @PMbackttfuture](https://x.com/pmbackttfuture/status/2047562135987741009)
> 整理时间：2026-04-24
> 来自翡冷翠

---

## 简介

Hermes Agent 接入 Codex 后，可以方便地使用 GPT-image-2 进行图像生成。本教程详细介绍如何配置 Hermes Agent 的图像生成功能，实现通过飞书/ Telegram 等渠道直接让 Agent 生成图片。

---

## 前置条件

- 已安装并配置 Hermes Agent
- 已接入 Codex（OpenAI Codex CLI）
- 有可用的 ChatGPT/Codex OAuth 账户（无需额外 API key）

---

## 配置步骤

### 步骤 1：打开 Hermes 工具配置

在终端执行以下命令：

```bash
hermes tools
```

### 步骤 2：选择重新配置工具

在交互式菜单中，选择：

```
Reconfigure an existing tool's provider or API key
```

### 步骤 3：选择图像生成工具

继续选择：

```
Image Generation
```

### 步骤 4：选择 OpenAI (Codex auth) 方案

在提供商选项中，选择：

```
→ (●) OpenAI (Codex auth) [free] — gpt-image-2 via ChatGPT/Codex OAuth — no API key required
```

**说明**：此方案通过 ChatGPT/Codex 的 OAuth 认证直接使用 GPT-image-2，**无需额外配置 API key**，完全免费。

### 步骤 5：重启 Gateway

配置完成后，必须重启 Hermes Gateway 以使更改生效：

```bash
hermes gateway restart
```

---

## 使用方法

重启完成后，即可在飞书、Telegram 或其他接入的渠道中直接让 Hermes Agent 生成图片。

### 示例指令

可以直接发送自然语言指令，例如：

- "帮我生成一张美女图片"
- "画一只可爱的猫"
- "生成一张科技风格的背景图"

### 输出选项

GPT-image-2 通常会提供**三档图片选项**（不同质量/速度档位）：

| 档位 | 特点 | 适用场景 |
|------|------|----------|
| 快速档 | 生成速度最快，质量可接受 | 快速验证、草稿、实时交互 |
| 标准档 | 平衡速度与质量 | 一般用途 |
| 高质量档 | 最佳画质，生成较慢 | 最终成品、高质量需求 |

**建议**：日常使用中可直接选择**最快的档位**，效果已经相当不错。

---

## 完整配置流程图

```
┌─────────────────────────────────────┐
│  终端执行: hermes tools              │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│  选择: Reconfigure an existing      │
│        tool's provider or API key   │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│  选择: Image Generation             │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│  选择: OpenAI (Codex auth) [free]   │
│        gpt-image-2 via ChatGPT/     │
│        Codex OAuth                  │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│  终端执行: hermes gateway restart    │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│  在飞书/Telegram 发送生图指令        │
│  例如: "帮我生成一张美女图片"        │
└─────────────────────────────────────┘
```

---

## 常见问题

### Q: 配置后仍然无法生图？

**A**: 请确认：
1. 是否正确执行了 `hermes gateway restart`
2. Gateway 是否成功重启（可查看日志确认）
3. 是否有有效的 Codex OAuth 会话

### Q: 生成图片需要付费吗？

**A**: 使用 `OpenAI (Codex auth)` 方案**完全免费**，通过 Codex 的 OAuth 认证调用 GPT-image-2，不消耗额外 API 额度。

### Q: 可以在哪些平台使用？

**A**: 配置完成后，任何已接入 Hermes Agent 的渠道都可以使用：
- Telegram
- 飞书
- 钉钉
- 其他自定义渠道

### Q: 生成速度如何？

**A**: GPT-image-2 提供三档速度选项，最快档位可实现接近实时的图像生成体验。

---

## 相关资源

### 提示词资源

如需高质量的 GPT-image-2 提示词，可参考以下资源：

| 资源名称 | 链接 | 说明 |
|----------|------|------|
| awesome-gpt-image-2 | https://github.com/YouMind-OpenLab/awesome-gpt-image-2 | 500+ 高质量提示词合集 |

### 提示词技巧

- **人像摄影**：指定风格、光线、背景、表情
- **海报设计**：说明用途、风格、主色调、文字需求
- **UI Mockup**：描述平台、风格、功能模块
- **角色设定**：详细描述外貌、服装、姿态、场景

---

## 作者信息

- **原作者**：AI产品黄叔 [@PMbackttfuture](https://x.com/PMbackttfuture)
- **简介**：两家大厂 AI 产品顾问
- **社群**：zaoxiaban.top

---

*来自翡冷翠*
