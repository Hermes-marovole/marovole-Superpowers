# Dokobot 网页搜索技能使用指南

> 来源：https://dokobot.ai/zh-CN/skill/173023680392200192  
> 作者：Dokobot  
> 整理时间：2026-04-27

## 执行摘要

**技能名称**：网页搜索 (web-search)  
**当前版本**：v1.1.0  
**下载量**：65+  
**核心优势**：基于本地 Chrome 浏览器的免费网页搜索，无需 API 密钥，零成本，无速率限制

---

## 技能详情

### 基本信息

| 属性 | 内容 |
|------|------|
| 技能 ID | 173023680392200192 |
| 版本 | v1.1.0 |
| 作者 | Dokobot |
| 官方 X | [@dokobot](https://x.com/dokobot) |
| 更新日期 | 2026/4/23 |
| 版本说明 | Rewrite search to local readpage mode |

### 安装与卸载

**安装命令**：
```bash
dokobot install-skill --id 173023680392200192
```

**卸载命令**：
```bash
dokobot uninstall-skill --id 173023680392200192
```

**前置要求**：
- 完成 [Dokobot 安装引导](https://dokobot.ai/zh-CN/guide)
- CLI 版本需 v2.9.0 以上

---

## 使用方式

### 基础用法

安装完成后，在 Dokobot CLI 中使用 `/web-search` 命令：

```bash
# 搜索技术话题
/web-search Rust Web 框架 2025

# 搜索时事政策
/web-search 最新 AI 监管政策
```

### 底层原理

该技能的核心原理是通过 `dokobot read --local` 命令直接读取搜索引擎结果页面：

1. **构造搜索 URL** — 将查询词编码后构建搜索引擎 URL
2. **本地浏览器渲染** — 使用本地 Chrome 浏览器渲染完整页面（包括 JavaScript）
3. **结构化提取** — Dokobot 提取搜索结果为结构化文本

```bash
# 直接调用底层命令
dokobot read --local 'https://www.google.com/search?q=your+query+here'
```

---

## 支持的搜索引擎

| 搜索引擎 | URL 模式 | 适用场景 |
|----------|----------|----------|
| **Google** | `https://www.google.com/search?q=your+query` | 默认选择，适合大多数搜索 |
| **Bing** | `https://www.bing.com/search?q=your+query` | 微软生态，部分场景更稳定 |
| **DuckDuckGo** | `https://duckduckgo.com/?q=your+query` | 隐私优先，无追踪 |
| **Baidu** | `https://www.baidu.com/s?wd=your+query` | 中文内容优先 |
| **Yandex** | `https://yandex.com/search/?text=your+query` | 俄语/东欧内容 |
| **Sogou** | `https://www.sogou.com/web?query=your+query` | 中文内容备选 |

**建议**：
- 一般查询默认使用 Google
- 中文内容可切换至 Baidu 或 Sogou 获得更好结果

---

## 查询构造指南

### URL 编码规则

- 空格替换为 `+` 或 `%20`
- 特殊字符需进行 URL 编码

### 常用搜索语法

```bash
# 简单查询
dokobot read --local 'https://www.google.com/search?q=rust+web+frameworks+2025'

# 精确短语（使用引号）
dokobot read --local 'https://www.google.com/search?q=%22exact+phrase%22'

# 站点限定搜索
dokobot read --local 'https://www.google.com/search?q=site%3Agithub.com+dokobot'

# 排除特定词
dokobot read --local 'https://www.google.com/search?q=python+web+framework+-django'

# 近期结果（过去一年）
dokobot read --local 'https://www.google.com/search?q=llm+benchmarks&tbs=qdr:y'
```

### 多语言搜索

```bash
# 中文搜索
dokobot read --local 'https://www.baidu.com/s?wd=Rust+Web框架+对比+2025'

# 日文搜索
dokobot read --local 'https://www.google.co.jp/search?q=Rust+Webフレームワーク+比較'
```

**注意**：浏览器的区域设置和登录状态会影响搜索结果。

---

## 典型工作流程

```bash
# Step 1: 执行搜索
/web-search best rust web frameworks 2025
# 或
dokobot read --local 'https://www.google.com/search?q=best+rust+web+frameworks+2025'

# Step 2: 从结果中选择最相关的 URL 并深入阅读
dokobot read --local 'https://example.com/rust-frameworks-comparison'

# Step 3: 如有需要，细化查询再次搜索
dokobot read --local 'https://www.google.com/search?q=actix-web+vs+axum+performance'
```

---

## 使用技巧

| 技巧 | 说明 |
|------|------|
| **始终使用 `--local`** | 免费、快速、无限制，且能利用浏览器的登录状态和区域设置 |
| **Google 是默认选择** | 适合大多数查询，但适时切换搜索引擎 |
| **先读结果页** | 先读取搜索结果页面，再选择具体 URL 深入阅读 —— 不要猜测 URL |
| **迭代优化查询** | 根据发现的内容不断细化搜索词 |
| **善用搜索运算符** | `site:`、 `"精确短语"`、 `-排除词` 等提高精确度 |
| **控制请求频率** | 如果搜索引擎显示验证码，请切换引擎或等待后再试 |

---

## 局限性与注意事项

1. **结果受环境因素影响**：搜索结果取决于浏览器的区域设置、地理位置和登录状态
2. **验证码风险**：同一搜索引擎频繁快速搜索可能出现验证码 — 建议切换引擎或等待
3. **动态加载内容**：部分搜索引擎动态加载结果 — dokobot 已处理 JavaScript 渲染，但无限滚动结果可能需要滚动操作

---

## 版本更新历史

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| v1.1.0 | 2026/4/23 | 重写搜索为本地 readpage 模式 |

---

## 相关资源

- **Dokobot 官网**：https://dokobot.ai/zh-CN
- **技能广场**：https://dokobot.ai/zh-CN/skill
- **安装引导**：https://dokobot.ai/zh-CN/guide
- **官方 X/Twitter**：https://x.com/dokobot

---

*来自翡冷翠*
