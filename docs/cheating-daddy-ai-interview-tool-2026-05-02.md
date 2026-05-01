# Cheating Daddy - AI 面试助手工具整理

> 来源：https://x.com/wsl8297/status/2050032502404984940  
> 推文作者：Joruno (@wsl8297)  
> 发布时间：2026-05-01  
> 整理时间：2026-05-02  
> 来自翡冷翠

---

## 简介

**Cheating Daddy** 是一款开源的 AI 面试/会议助手工具，专为线上面试或关键会议场景设计。它能够实时监听屏幕内容和音频对话，通过 Google Gemini 2.0 Flash Live 提供即时 AI 提示，帮助用户在突发问题时快速响应。

---

## 核心信息

| 维度 | 详情 |
|------|------|
| **项目名称** | Cheating Daddy |
| **开发者** | Soham (@sohzm) |
| **开源协议** | GPL-3.0 license |
| **GitHub Stars** | 5.3k+ |
| **Forks** | 896 |
| **下载量** | 60K+ |
| **最新版本** | v0.7.0 |

---

## 主要功能

### 🖼️ 屏幕捕获
- 实时截取屏幕内容并发送给 Google Gemini
- 识别面试题目、编码问题、任何可视化内容

### 🎤 音频捕获
- 实时监听系统音频
- 将语音转换为文字并即时传输给 AI

### 🤖 AI 回复
- 使用 Google Gemini 自动生成回答
- 无需手动输入

### 🔧 多场景配置
- 支持面试、销售电话、谈判、学习等多种模式
- 每种模式优化不同的回复策略

### 📝 自定义上下文
- 添加简历、公司信息、笔记
- 获取针对个人情况定制化的回答

### ⌨️ 快捷键操控
- 通过热键控制所有功能
- 触发截图和回复无需触摸鼠标

---

## 隐身特性

Cheating Daddy 从设计上就考虑了无痕推广的会议/面试场景：

| 隐身功能 | 说明 |
|----------|------|
| 隐藏于 Dock 和系统托盘 | 不在任务栏显示 |
| 屏幕共享不可见 | 屏幕录制无法捕获 |
| 绕过活动监视器 | 进程不被检测 |
| 绕过浏览器监考 | 适配在线考试系统 |
| 透明悬浮层 | 随拖随放，支持点击穿透 |

---

## 支持平台

| 平台 | 状态 |
|------|------|
| macOS | ✅ 支持 (ARM64/Intel) |
| Windows | ✅ 支持 |
| Linux | ⏪ Coming soon |

---

## 安装与使用

### 安装方式

```bash
# 通过 npm 安装
npm install -g cheating-daddy

# 或从 GitHub 下载安装包
# https://github.com/sohzm/cheating-daddy/releases
```

### 配置要求

1. **Google Gemini API Key**
   - 在 Google AI Studio 获取 API Key
   - 免费额度通常足够大多数面试使用

2. **系统权限**
   - macOS: 需要屏幕录制和音频捕获权限
   - Windows: 需要管理员权限

### 快速启动

1. 设置 Gemini API Key
2. 选择场景配置文件（面试/销售/会议/谈判）
3. 使用快捷键 `Ctrl+Enter` 手动触发或自动模式运行

---

## 资源链接

| 资源 | 链接 |
|------|------|
| **GitHub** | https://github.com/sohzm/cheating-daddy |
| **官网** | https://cheatingdaddy.com |
| **Discord** | https://discord.gg/GCBdubnXfJ |
| **X/Twitter** | https://x.com/cheating_daddy |
| **Instagram** | https://instagram.com/cheating_daddy |
| **TikTok** | https://www.tiktok.com/@cheating_daddy |
| **开发者** | https://soham.sh/ |

---

## GitHub 仓库数据

| 指标 | 数据 |
|------|------|
| Stars | 5.3k+ |
| Forks | 896 |
| Issues | 119 |
| Pull Requests | 29 |
| Commits | 83 |
| Branches | 2 |
| Tags | 7 |
| License | GPL-3.0 |
| 最近更新 | 2026-04-27 (cleanup) |

---

## 使用场景

### 适合场景
- 线上技术面试（编码题快速响应）
- 销售电话（实时提供产品信息和话术建议）
- 商务会议（谈判策略即时建议）
- 演示报告（即时补充技术细节）
- 在线学习（实时解答疑惑）

### 使用建议
1. **预先配置场景**：根据面试类型选择合适的配置文件
2. **添加个人上下文**：将简历、项目经历等信息导入系统
3. **熟悉快捷键**：提前练习快捷键操作以减少使用时的分心
4. **测试环境**：在正式场景前先进行测试，确保隐身功能正常

---

## 费用说明

| 项目 | 费用 |
|------|------|
| Cheating Daddy 本身 | 免费开源 |
| 高级功能 | 无付费墙 |
| Gemini API | Google 提供免费额度 |
| 隐藏费用 | 无 |

---

## 注意事项

1. **合规使用**：请确保在允许使用辅助工具的场景下使用
2. **API Key 安全**：勿将 API Key 提交到公共仓库
3. **隐私保护**：工具捕获的屏幕和音频仅发送给 Google Gemini，不会在本地存储

---

## 原推文内容

> 线上面试或关键会议最怕的就是：突然被点名，大脑瞬间空白，想搜资料又不敢动，尴尬到手心冒汗。
> 
> Cheating Daddy 这款开源工具就是为这种时刻准备的：不打断你的节奏，在你需要时悄悄递上 AI 提示。
> 
> 它基于 **Google Gemini 2.0 Flash Live**，能实时理解屏幕内容和音频对话，再按不同场景给出更贴合的建议：面试、销售、会议、演示、谈判，都能快速跟上。

**作者**: Joruno (@wsl8297)  
**身份**: AI 程序员，分享高质量、有趣、实用的 AI 工具  
**推文数据**: 3 回复 | 8 转发 | 71 点赞 | 109 收藏 | 6,333 浏览

---

## 学习/使用建议

1. **立即体验**
   - 访问 https://cheatingdaddy.com 下载适合你的版本
   - 获取 Google Gemini API Key（https://ai.google.dev）
   - 按照官方文档配置并测试

2. **深入学习**
   - 阅读 GitHub README 了解详细功能
   - 加入 Discord 社区获取帮助
   - 查看 Issues 和 PR 了解开发进度

3. **贡献反馈**
   - 如遇到问题，可在 GitHub Issues 提交
   - 有功能建议也可以提交 PR

---

*来自翡冷翠*
