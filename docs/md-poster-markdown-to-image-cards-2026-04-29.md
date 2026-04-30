# 图文排版系统开源 — 把 Markdown 文章转成精美图文卡片，流量翻几十倍

> 来源：[Bill_DO_A_BIT 的 X Article](https://x.com/Bill_Do_A_Bit/status/2049079691731185693)
> 整理时间：2026-04-29
> 来自翡冷翠

---

## 简介

@Bill_Do_A_Bit（多少做点）开源了一套图文排版系统 **md-poster**，能将 Markdown 文章在 30 秒内转为精美的小红书/公众号图文卡片。作者通过这套系统，把公众号三个月 80 粉的困境翻转为一个月涨到 1000+ 粉的增长曲线。同一篇文章，纯文字阅读量一百多，转成图文后能飙到三四千——最高翻 20+ 倍。这套系统已迭代 23+ 篇正式文章，现已 MIT 开源。

--- 

## 核心项目

| 项目 | 链接 | 简介 |
|------|------|------|
| **md-poster** | [github.com/BeardJohnJohn/md-poster](https://github.com/BeardJohnJohn/md-poster) | Markdown → HTML + CSS → Playwright 截图 → PNG 图文卡片，MIT 开源 |

---

## 关键洞察：为什么图文比纯文字流量高几十倍

作者 2026 年 1 月开始写公众号，前三个月只有 80 个粉丝。4 月底突破 1000 粉，其中一个核心变量就是"图文转化"：

- 纯文字长文 → 过一天阅读 100+
- 同样的内容转成图文卡片 → 阅读 3000-4000+
- 倍数范围：最少 5-7 倍，多的时候 20+ 倍
- 二十多篇文章下来，几乎每篇都是这个规律

关键结论：纯文字在信息流里越来越隐形，算法把流量给了图文和视频。你没法改变算法，但可以改变内容的形式。图文就是全平台通行证——公众号、小红书、X、即刻都能发。

---

## 系统架构

```
Markdown 正文 → Python 脚本 → HTML + CSS → Playwright 截图 → PNG 图片
```

全程 3 步，30 秒输出 8 张 PNG 卡片：

1. **安装依赖**：`pip install playwright && playwright install chromium`
2. **生成 HTML**：`python xhs_pages.py`
3. **截图**：`python screenshot.py --auto-height`

输出在 `output/` 目录。

---

## 设计系统

| 参数 | 值 |
|------|------|
| 卡片宽度 | 1080px（小红书原生分辨率） |
| 背景色 | `#F9F9F6`（米白色） |
| 正文字体 | Noto Serif SC（思源宋体） |
| 正文字号 | 34px，行高 2.0 |
| 标题字号 | H1: 56px, H2: 44px |
| 内边距 | 90px |
| 分割线色 | `#E8E6D9` |

这套视觉风格是在 23 篇生产文章中一点一点打磨出来的。

---

## 三种使用方式

### 方法一：AI 帮你排版（最省力）

把你的 Markdown 文章和 `SKILL.md` 一起发给 AI（ChatGPT / Claude / Gemini / 豆包都可以），说：

> "根据这个 SKILL.md 的规范，帮我把这篇文章排版成小红书图文。生成一个 xhs_pages.py 脚本。"

AI 生成完整排版脚本，你只需运行它。这是作者自己现在唯一在用的方式。

### 方法二：修改示例脚本

1. 复制 `examples/basic/xhs_pages.py` 到你的文章目录
2. 修改 Config 区（文章路径、标题、作者、分页定义）
3. 运行生成 HTML，再截图

### 方法三：直接编辑 HTML 模板

打开 `templates/xhs_card_template.html`，替换 `{{PLACEHOLDER}}`，复制 `<div class="card">` 块来增加页数。

---

## 仓库结构

```
md-poster/
├── README.md                        # 中文说明文档
├── README_EN.md                     # 英文说明文档
├── SKILL.md                         # AI 使用手册（教 AI 怎么用这套系统）⭐ 灵魂文件
├── LICENSE                          # MIT 开源协议
├── assets/
│   └── demo-output/                 # 效果展示截图
├── scripts/
│   ├── screenshot.py                # 通用截图脚本（核心）
│   └── setup.sh                     # 一键安装脚本
├── templates/
│   └── xhs_card_template.html       # 卡片 HTML 模板（可直接编辑）
├── examples/
│   ├── basic/                       # 基础示例（可直接跑）
│   │   ├── example_article.md
│   │   └── xhs_pages.py
│   └── real-output/                 # 真实产出样品
└── docs/
    ├── design-system.md             # CSS 设计系统详解
    ├── methodology.md               # 为什么 HTML > Canvas（范式转换）
    └── troubleshooting.md           # 踩坑记录
```

---

## 核心哲学：手动 vs 代码，两条路径

| 路径 | 代表工具 | 核心操作 | 边际成本 |
|------|---------|---------|---------|
| 手动路径 | Canvas / PS / 美图秀秀 | 拖拽、对齐、调字号 | 每多一页成本不变 |
| 代码路径 | HTML + CSS + Playwright | 写规则、跑脚本 | 首次有固定成本，之后趋近于零 |

两条路径的产出物完全一样——都是 PNG 图片。区别在于**两个小时和三十秒**。

但关键洞察是：**AI 时代，代码路径是唯一能被加速的路径。**

- AI 天生擅长写 HTML 和 CSS
- AI 没法帮你在 Canvas 里拖鼠标
- 改风格？改一行 CSS，所有页面同时更新
- 加页数？复制一个 HTML 块就行

从"操作"到"定义规则"——这是一次思维范式的转换。

---

## 分页规则

| 规则 | 值 |
|------|------|
| 每页目标字数 | 700-800 字 |
| 每页目标高度 | ~2000px |
| 最大页数 | 8 页正文（小红书上限 9 张 = 1 封面 + 8 正文） |
| 分页位置 | 在自然断点处（段落间、章节标题前） |

---

## 踩坑铁律（23 篇文章的血泪教训）

| # | 铁律 | 原因 |
|---|------|------|
| 1 | 使用 headless 模式 | 非 headless 会渲染浏览器扩展的蓝色边框 |
| 2 | 首页等 3 秒 | Google Fonts（思源宋体）需要加载时间 |
| 3 | 不要用 `python -c` 内联命令 | Windows 路径含单引号会被 PowerShell 吞掉 |
| 4 | 页脚放在 `.content` 内部 | 放在外面会被截图裁切 |
| 5 | 隐藏所有滚动条 | 需要 CSS 三重覆盖 |
| 6 | 不要让 AI 直接输出 HTML | 中文 token 大，5000 字 HTML 会被截断。让 AI 写 Python 生成器脚本 |
| 7 | 超 8 页时增大每页字数 | 不要删内容，增加页面高度 |

---

## 适用场景与局限

**最适合：**
- 以文字为主体的深度内容、教程类、分析类文章
- 长文转图文分发到小红书/公众号/X/即刻
- 任何需要将文字内容视觉化的场景

**不适合：**
- 大量图片拼贴的视觉类内容（摄影、穿搭）
- 需要手绘/手写体效果的个人化风格

---

## 资源汇总

### 所有 GitHub 仓库

| 项目 | 链接 | 简介 |
|------|------|------|
| md-poster | https://github.com/BeardJohnJohn/md-poster | Markdown → 图文卡片排版系统，MIT 开源 |

### 值得关注的人/账号

- **@Bill_Do_A_Bit** — AI-augmented content creator，md-poster 作者
  - 🐦 X: [@Bill_Do_A_Bit](https://x.com/Bill_Do_A_Bit)
  - 📕 小红书: **Do A Bit 多少做点**
  - 📧 Email: bill.jjxu@gmail.com

### 技术参考

- [Playwright 官方文档](https://playwright.dev/python/)
- [Google Fonts - Noto Serif SC（思源宋体）](https://fonts.google.com/noto/specimen/Noto+Serif+SC)

---

## 适用场景建议

如果你是内容创作者，正在手动给文章做排版——立刻试试这套系统。你的时间应该花在写作和思考，不是拖拽。

如果你是 AI 使用者，这套系统的 `SKILL.md` 是一个极好的参考——它展示了如何把一套手工工作流变成 AI 可以理解和执行的规范文档。

---

*来自翡冷翠*
