# Quarkdown - 具有超能力的 Markdown

> 来源：[Joruno @wsl8297](https://x.com/wsl8297/status/2048748768544330019)
> 整理时间：2026-04-28
> 来自翡冷翠

---

## 简介

Quarkdown 是一个现代化的基于 Markdown 的排版系统，由开发者 iamgio 创建。它被称为"具有超能力的 Markdown"——在保留 Markdown 轻量语法的同时，将排版、生成和自动化能力直接拉满。

与传统 Markdown 不同，Quarkdown 支持**函数调用、变量定义、逻辑控制**，并且可以将同一项目无缝编译成多种输出格式：学术论文、书籍、知识库或交互式演示文稿。

---

## 核心亮点

| 特性 | 说明 |
|------|------|
| **可写逻辑** | 支持函数和变量，让内容按规则动态生成 |
| **多端输出** | HTML、PDF、演示文稿一键导出 |
| **标准库强大** | 布局、数学公式、条件判断等开箱即用 |
| **实时预览** | 边写边看，改动立即生效 |
| **语法友好** | 比 LaTeX 更易上手，也更易读 |
| **面向长文档** | 章节结构清晰，书籍级排版也能胜任 |

---

## 输出格式支持

Quarkdown 支持通过 `.doctype` 函数切换不同的文档类型：

### 1. 普通文档 (`.doctype {plain}`)
连续流式排版，类似 Notion/Obsidian
- 适用场景：静态网站、知识管理
- 示例：[作者个人网站](https://iamgio.eu/)

### 2. 分页文档 (`.doctype {paged}`)
基于 paged.js 的打印就绪排版
- 适用场景：学术论文、书籍、报告
- 支持专业级排版，类似 LaTeX 输出质量

### 3. 演示文稿 (`.doctype {slides}`)
基于 reveal.js 的交互式幻灯片
- 适用场景：讲座、演讲、技术分享

### 4. 文档网站 (`.doctype {docs}`)
专为 wiki 和技术文档设计
- 适用场景：技术文档、大型知识库
- 示例：[Quarkdown 官方 Wiki](https://quarkdown.com/wiki)

---

## 函数与脚本支持

Quarkdown 最大的特色是将**图灵完备的脚本能力**引入 Markdown：

### 函数定义示例
```quarkdown
.function {greet}
    to from:
    **Hello, .to** from .from!

.greet {world} from:{iamgio}
```

**输出结果：**
> **Hello, world** from iamgio!

### 实际应用示例
```quarkdown
.function {animal}
    name ecosystem picture:
    .row
        .clip {circle}
            .picture

        - **Name**: .name
        - **Ecosystem**: .ecososystem

.animal {Red panda} ecosystem:{Temperate forests}
    ![Red panda](img/red-panda.jpg)

.animal {Sea otter} ecosystem:{Kelp forests}
    ![Sea otter](img/sea-otter.jpg)
```

这个特性让重复性内容的生成变得自动化，特别适用于批量生成结构化文档。

---

## 与同类工具对比

| 特性 | Quarkdown | LaTeX | Typst | AsciiDoc | MDX |
|------|-----------|-------|-------|----------|-----|
| 简洁可读 | ✅ | ❌ | ✅ | ✅ | ✅ |
| 完整文档控制 | ✅ | ✅ | ✅ | ❌ | ❌ |
| 脚本支持 | ✅ | 部分 | ✅ | ❌ | ✅ |
| 书籍/论文导出 | ✅ | ✅ | ✅ | ✅ | 需第三方 |
| 演示文稿导出 | ✅ | ✅ | ✅ | ✅ | 需第三方 |
| 静态网站导出 | ✅ | ❌ | 实验性 | ✅ | ✅ |
| 文档/Wiki导出 | ✅ | ❌ | ❌ | ✅ | ✅ |
| 学习曲线 | 🟢 | 🔴 | 🟠 | 🟢 | 🟢 |

### 语法对比示例

**LaTeX 写法：**
```latex
\tableofcontents
\section{Section}
\subsection{Subsection}
\begin{enumerate}
\item \textbf{First} item
\item \textbf{Second} item
\end{itemize}
\begin{center}
This text is \textit{centered}.
\end{center}
```

**Quarkdown 写法：**
```quarkdown
.tableofcontents
# Section
## Subsection
1. **First** item
2. **Second** item
.center
This text is _centered_.
```

---

## 安装指南

### macOS / Linux

**方式一：安装脚本（推荐）**
```bash
curl -fsSL https://raw.githubusercontent.com/quarkdown-labs/get-quarkdown/refs/heads/main/install.sh | sudo env "PATH=$PATH" bash
```

**方式二：Homebrew**
```bash
brew install quarkdown-labs/quarkdown/quarkdown
```

### Windows

**方式一：PowerShell 安装脚本**
```powershell
irm https://raw.githubusercontent.com/quarkdown-labs/get-quarkdown/refs/heads/main/install.ps1 | iex
```

**方式二：Scoop**
```powershell
scoop bucket add java
scoop bucket add quarkdown https://github.com/quarkdown-labs/scoop-quarkdown
scoop install quarkdown
```

### 系统要求
- **Java 17** 或更高版本
- **Node.js + npm**（仅 PDF 导出需要）
- **Puppeteer**（PDF 导出依赖）

---

## 快速上手

### 1. 创建项目
```bash
quarkdown create my-project
```
启动交互式项目向导，自动生成元数据和初始内容。

### 2. 编译文档
```bash
# 基本编译
quarkdown c file.qd

# 带实时预览
quarkdown c file.qd -p

# 监听文件变化自动重编译
quarkdown c file.qd -w

# 组合：实时预览 + 自动重编译
quarkdown c file.qd -p -w

# 导出 PDF
quarkdown c file.qd --pdf
```

### 3. REPL 交互模式
```bash
quarkdown repl
```
进入交互式环境，边学边试。

---

## 开发工具支持

### VS Code 扩展
- **插件名称**：Quarkdown
- **功能**：语法高亮、实时预览、智能提示
- **下载**：[VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=quarkdown.quarkdown-vscode)

### GitHub Actions 集成
使用 [setup-quarkdown](https://github.com/quarkdown-labs/setup-quarkdown) Action，可在 CI/CD 流程中自动编译文档。

---

## 学习资源

| 资源 | 链接 | 说明 |
|------|------|------|
| **官方文档** | https://quarkdown.com/wiki | 完整语言特性参考 |
| **快速入门** | https://quarkdown.com/wiki/quickstart | 新用户必读 |
| **GitHub 仓库** | https://github.com/iamgio/quarkdown | 源码、示例、Mock 文档 |
| **Mock 示例** | https://github.com/iamgio/quarkdown/tree/main/mock | 完整功能展示文档 |
| **生成示例** | https://github.com/quarkdown-labs/generated | 各种主题组合的 PDF 输出 |

---

## 适用场景

1. **学术写作**：论文、研究报告、学位论文
2. **技术文档**：API 文档、用户手册、Wiki
3. **知识管理**：个人笔记、团队知识库
4. **书籍出版**：自出版、技术书籍
5. **演示文稿**：技术演讲、课程讲义
6. **静态网站**：个人博客、项目主页

---

## 值得关注

- **@wsl8297** (Joruno) - AI 程序员，专注分享高质量 AI 工具教程
- **@iamgio** - Quarkdown 创始人

---

## 快速参考

### 常用命令
```bash
# 创建项目
quarkdown create [directory]

# 编译文件
quarkdown c <file.qd>

# 实时预览
quarkdown c <file.qd> -p -w

# 导出 PDF
quarkdown c <file.qd> --pdf

# 交互模式
quarkdown repl
```

### 文档类型声明
```quarkdown
.doctype {plain}   # 普通流式文档（默认）
.doctype {paged}  # 分页打印文档
.doctype {slides} # 演示文稿
.doctype {docs}   # 文档网站
```

---

*来自翡冷翠*
