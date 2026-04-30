# 用 Codex HyperFrames 插件 + 5.5 模型生成产品介绍视频

> 来源：[BECOOL 的 X 帖子](https://x.com/becool_me/status/2047435777122951244)  
> 整理时间：2026-04-24  
> 来自翡冷翠

---

## 简介

本案例展示了如何使用 **OpenAI Codex 的 HyperFrames 插件** 结合 **最新 5.5 模型** 快速生成产品介绍视频。作者 [@becool_me](https://x.com/becool_me) 以其实际项目 [favicon.im](https://favicon.im) 为例，演示了 AI 辅助视频创作的工作流。

---

## 核心工具

### 1. HyperFrames 插件

HyperFrames 是 Codex 的插件之一，专门用于视频生成和编辑。它允许用户通过自然语言描述来创建和修改视频内容。

**主要功能：**
- 自动生成产品介绍视频
- 支持 UI 元素定位和动画
- 可调整元素位置、重叠关系
- 与 Codex 5.5 模型深度集成

### 2. Codex 5.5 模型

OpenAI Codex 的最新版本 5.5 模型，在代码理解和多媒体生成方面具有显著提升：
- 更强的 UI/UX 理解能力
- 改进的视觉元素定位精度
- 更快的视频渲染速度

---

## 案例：favicon.im 产品介绍视频

### 项目介绍

**favicon.im** 是作者 BECOOL 开发的公共服务，用于快速获取任意网站的 favicon 图标。

**核心功能：**
- 输入域名即可获取网站图标
- 支持默认尺寸（16x16~32x32）和大尺寸版本
- 免费 API，无需 API 密钥
- 每月处理 30M+ 请求
- 由 Cloudflare 全球边缘网络提供 99.9% 可用性

**使用示例：**
```html
<!-- 默认尺寸 -->
<img src="https://favicon.im/example.com" alt="favicon" loading="lazy" />

<!-- 大尺寸 -->
<img src="https://favicon.im/example.com?larger=true" alt="favicon large" loading="lazy" />
```

### 视频制作流程

根据作者分享的经验，制作流程如下：

1. **准备素材**：整理产品截图、网站界面、功能演示
2. **编写 Prompt**：描述视频风格、展示顺序、动画效果
3. **使用 HyperFrames 生成**：在 Codex 中调用插件生成初稿
4. **细节调整**：根据生成结果微调 UI 元素位置，解决重叠问题
5. **导出成品**：获得最终产品介绍视频

**关键技巧：**
- 在 Prompt 中明确指定 UI 元素的层级关系
- 使用 5.5 模型的视觉理解能力来优化布局
- 生成后人工检查并调整位置重叠问题

---

## BECOOL 的其他项目

作者 [@becool_me](https://x.com/becool_me) / [@we_webmaster](https://x.com/we_webmaster) 开发了多个实用的开发者工具：

| 项目 | 链接 | 功能简介 |
|------|------|----------|
| **favicon.im** | https://favicon.im | 网站图标获取服务 |
| **query.domains** | https://query.domains | 批量域名可用性查询 + Whois |
| **datetime.app** | https://datetime.app | 精确日期时间查询 |
| **small.im** | https://small.im | 图片压缩与格式转换 |
| **temp.now** | https://temp.now | 临时邮箱服务 |
| **ip.network** | https://ip.network | IP 地址查询 |
| **base64.sh** | https://base64.sh | Base64 编解码工具 |
| **screenshot.domains** | https://screenshot.domains | 网站截图获取 |
| **qrcode.fun** | https://qrcode.fun | 免费二维码生成器 |
| **dns.fish** | https://dns.fish | 域名 DNS 查询 |
| **redirectcheck.org** | https://redirectcheck.org | 重定向检查工具 |
| **pdftolink.app** | https://pdftolink.app | PDF 转链接服务 |

---

## 相关资源

### Favicon.im 文档
- **官网**：https://favicon.im/zh/
- **API 文档**：https://favicon.im/zh/api
- **博客**：https://favicon.im/zh/blog

### Codex 相关
- **GitHub**: https://github.com/heygen-com/hyperframes/tree/main/.codex-plugin
- **HyperFrames 插件**：可在 Codex 插件市场搜索安装

### 技术参考
- **阮一峰周刊收录**：https://github.com/ruanyf/weekly/issues/5026
- **掘金教程**：https://juejin.cn/post/7437391772064825356

---

## 适用场景

此工作流特别适合以下场景：

1. **产品发布**：快速制作产品介绍视频用于社交媒体宣传
2. **功能演示**：展示 SaaS 产品的新功能特性
3. **营销素材**：生成网站、落地页的视频内容
4. **教程制作**：制作产品使用教程和指南

---

## 快速参考

### favicon.im API 速查

| 功能 | URL 格式 | 示例 |
|------|----------|------|
| 获取图标 | `https://favicon.im/{domain}` | `https://favicon.im/google.com` |
| 大尺寸 | `?larger=true` | `https://favicon.im/google.com?larger=true` |
| 自定义默认图标 | `?default-avatar={url}` | 404 时返回指定图标 |
| 严格 404 | `?throw-error-on-404=true` | 便于 onerror 处理 |

### Next.js 配置
```javascript
// next.config.js
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'favicon.im',
      },
    ],
  },
}
```

---

*来自翡冷翠*
