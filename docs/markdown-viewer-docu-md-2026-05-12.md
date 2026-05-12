# Markdown Viewer（docu.md）：Markdown 转完美 Word 的一站式解决方案

> 来源：https://x.com/meta360dao/status/2054043137148883449  
> 作者：HAI Labs（人本智能实验室）@Meta360DAO  
> 整理时间：2026-05-12

## 执行摘要

Markdown Viewer（官网 https://docu.md）是一款开源免费的浏览器扩展与多平台工具，核心使命是**将 Markdown 文档一键转换为格式完美的 Word 文档**。它解决了 Markdown 用户长期以来的"最后一公里"痛点：写 Markdown 时爽如闪电，但导出为 Word 时却陷入手动截图、调整格式、修复公式等排版地狱。

该工具由 @xicilion（响马）主导开发，目前已在 Chrome、Firefox、VS Code 和移动端（iOS/Android）全面上线，完全免费、本地处理、隐私优先。

---

## 核心亮点

### 🎨 全能图表自动渲染（7 大绘图协议）

| 协议 | 支持的图表类型 | 典型场景 |
|------|--------------|---------|
| **PlantUML** | 类图、时序图、用例图、活动图、组件图 | 软件设计、UML 建模 |
| **Mermaid** | 流程图、时序图、类图、状态图、甘特图、饼图、ER 图 | 技术文档、架构设计 |
| **Vega/Vega-Lite** | 柱状图、折线图、散点图、热力图 | 商业报表、数据分析 |
| **drawio** | 架构图、网络拓扑、UML 图 | 系统设计、技术文档 |
| **Canvas** | 思维导图、知识图谱、概念图 | 头脑风暴、规划板 |
| **Infographic** | 统计图表、信息图、数据可视化 | 数据演示、视觉叙事 |
| **Graphviz DOT** | 有向/无向图、网络拓扑、状态机 | 依赖分析、复杂图结构 |

**效率对比**：复杂时序图（10 个对象）传统方式需 65 分钟（绘制 30min + 修改 20min + 调整 10min + 导出 5min），使用 Markdown Viewer 仅需 6 分钟（写代码 5min + 修改 30 秒 + 导出 1 秒）。

### 📐 LaTeX 公式原生转 Word 可编辑方程

这是 Markdown Viewer 最具差异化的功能之一。与市面上几乎所有竞品不同，它**将 LaTeX 公式转换为 Word 原生公式对象**，而非模糊的图片。

导出后你可以：
- 在 Word 中继续编辑公式
- 调整字体大小
- 修改符号和变量
- 复制到其他文档

**示例**：输入 `\int_0^\infty e^{-x^2}dx` 即可生成完美公式，无需在 Word 公式编辑器中逐点击选符号。

### 🎭 29 款大师级主题一键切换

| 分类 | 主题 |
|------|------|
| 经典 | Default、Academic、Business、Manuscript、Newspaper |
| 阅读 | Palatino、Garamond、Typewriter、Elegant |
| 现代 | Technical、Swiss、Minimal |
| 创意 | Magazine、Century、Handwritten、Verdana |
| 中文 | Heiti、Mixed、Water |
| 趣味 | Rainbow、Starry、Candy、Dinosaur、Space、Garden |
| 自然 | Forest、Ocean、Coral、Sunset |

预览即所得，导出效果与预览完全一致，无需反复调整。

### 🔒 隐私护城河：100% 本地处理

- 所有渲染在本地完成，不上传云端
- 无追踪、无数据收集
- 开源可审计（GPL-3.0 协议）
- 浏览器扩展采用现代 Manifest V3 标准

---

## 平台覆盖

| 平台 | 状态 | 最佳场景 |
|------|------|---------|
| **Chrome 扩展** | ✅ 已发布 | 浏览器中阅读本地/在线 Markdown + 导出 |
| **Firefox 扩展** | ✅ 已发布 | Firefox 用户，功能与 Chrome 一致 |
| **VS Code 扩展** | ✅ 已发布 | 在编辑器内写作 + 实时预览 + 导出 |
| **移动端 App** | ✅ 已发布 | iOS/Android 随身阅读与导出（Flutter 构建）|

安装渠道：
- Chrome Web Store：https://chromewebstore.google.com/detail/markdown-viewer/jekhhoflgcfoikceikgeenibinpojaoi
- Firefox Add-ons：https://addons.mozilla.org/firefox/addon/markdown-viewer-extension/
- VS Code Marketplace：https://marketplace.visualstudio.com/items?itemName=xicilion.markdown-viewer-extension
- Open VSX：https://open-vsx.org/extension/xicilion/markdown-viewer-extension

---

## 真实场景效率对比

### 技术文档：15 个流程图，2 小时 → 5 分钟

**以前**：draw.io 画图 → 导出 PNG → 插入 Word → 调整大小 → 重复 15 次 = **2 小时**
**现在**：写 Mermaid 代码 → 点击下载 = **5 分钟**

### 学术论文：50+ 公式，3 小时 → 10 分钟

**以前**：Word 公式编辑器逐个输入 或 付费工具订阅 = **3 小时 + 付费**
**现在**：直接写 LaTeX 语法 → 点击下载 = **10 分钟 + 免费**

### 团队协作：周报，1 小时 → 1 分钟

**以前**：复制内容 → 设置格式 → 调整列表 → 添加样式 → Excel 图表 + 截图 = **每周 1 小时**
**现在**：打开文件 → 选择主题 → 点击下载 = **1 分钟**

---

## 竞品对比

| 维度 | 手动截图 | CLI 工具 | 在线服务 | 桌面编辑器 | Markdown Viewer |
|------|---------|---------|---------|-----------|-----------------|
| 易用性 | 繁琐 | 需配置 | 需上传 | 需安装 | ✅ 一键完成 |
| Mermaid 支持 | 手动截图 | 需插件 | ✅ 支持 | ✅ 支持 | ✅ 原生支持 |
| 数学公式 | 图片 | 图片 | 图片 | 图片 | ✅ 可编辑 |
| 隐私 | ✅ 本地 | ✅ 本地 | ❌ 云端上传 | ✅ 本地 | ✅ 本地 |
| 主题数量 | - | - | 3-5 款 | 5-10 款 | ✅ 29 款 |
| 离线使用 | ✅ | ✅ | ❌ | ✅ | ✅ |
| GitHub 直接预览 | ❌ | ❌ | ❌ | ❌ | ✅ |
| 价格 | 免费 | 免费 | 付费订阅 | 付费 | ✅ 免费 |

---

## 项目信息

- **官网**：https://docu.md
- **GitHub**：https://github.com/markdown-viewer/markdown-viewer-extension
- **开发者**：@xicilion（响马）
- **协议**：GPL-3.0
- **界面语言**：支持 28 种语言（含简体中文、繁体中文）
- **社区项目**：md2x（Node.js CLI 批量转换工具）

---

## 目标人群推荐

- **科研党/学生**：论文公式与架构图一键搞定
- **技术作家/博主**：技术文档完美输出
- **产品经理/架构师**：Markdown 画图，Word 汇报
- **开发者**：README 直接预览与导出
- **任何使用 Markdown 的人**

---

## 使用建议

1. **Chrome/Firefox 用户**：直接安装扩展，双击本地 `.md` 文件即可预览，一键导出 Word
2. **VS Code 用户**：安装扩展后，在编辑器内直接预览并导出
3. **移动端用户**：App Store / Google Play 搜索 "Markdown Viewer"
4. **需要批量处理**：可搭配社区项目 md2x（Node.js CLI）进行自动化转换

---

*来自翡冷翠*
