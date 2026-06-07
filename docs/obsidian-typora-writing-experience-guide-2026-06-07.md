# Obsidian → Typora 式写作体验配置指南

> **来源**: https://x.com/Pluvio9yte/status/2063301694428217823?s=20
> **作者**: 雪踏乌云 (@Pluvio9yte)
> **整理时间**: 2026-06-07
> **来自翡冷翠**

---

## 简介

本文是 X 用户 @Pluvio9yte 分享的 **Obsidian 深度配置教程**，核心目标只有一个：

> **把 Obsidian 从「知识图谱模式」切回「标准 Markdown 写作模式」**，让写作体验尽可能接近 Typora。

Obsidian 的默认形态是知识库工具（Wikilink、反链、图谱、vault 结构），如果你从 Typora 迁移过来，真正不适应的不是功能不够，而是**工作方式完全不同**。只要关掉几个关键开关、调整几个核心配置，Obsidian 就能变成一个「增强版 Typora」。

---

## 核心目标

| 目标 | 说明 |
|------|------|
| 写作体验 | 尽量接近 Typora |
| Markdown 兼容性 | 100% — 文件在任何工具（Typora/VSCode/GitHub/静态博客）都能正常打开 |
| 插件依赖 | 尽量少，避免升级时插件链断裂 |

**配置取舍：**
- Typora 输入体验：85%–90%
- 图片体验：90%
- Markdown 兼容性：100%
- 知识图谱能力：基本放弃

---

## 关键配置（必做五步）

### Step 1: 关闭 Wikilinks（最重要）

**路径**: `Settings → Files & Links → Use Wikilinks`

**必须关闭。**

| Wikilinks 关闭前 | 关闭后（标准 Markdown） |
|------------------|------------------------|
| `[[note]]` | `[note](note.md)` |
| `![[image.png]]` | `![](images/image.png)` |

只要还在用 `[[ ]]`，文件就强绑定 Obsidian。Typora 和 VSCode 打开时体验都会打折。

---

### Step 2: 改用相对路径

**路径**: `Settings → Files & Links → New link format`

**选择**: `Relative path to file`

笔记引用保持普通文件系统逻辑，不依赖 Obsidian vault 解析。对写作者来说，比「最短路径」或「仅文件名」更稳定，也更适合 Git、博客系统、Typora 和 VSCode。

---

### Step 3: 统一图片目录

**路径**: `Settings → Files & Links → Default location for new attachments`

**推荐设置**:
- `In subfolder under current folder`
- Folder name: `images`

最终文件结构：

```
/vault
  note.md
  /images
    img1.png
    img2.png
```

这比 Obsidian 默认的 `![[img1.png]]` 更通用，更适合以后迁移。粘贴图片后图片自动进入 `images/`，正文生成 `![](images/img1.png)`。

---

### Step 4: 关闭严格换行

**路径**: `Settings → Editor → Strict line breaks`

**关闭。**

Typora 用户习惯自然换行，不需要严格遵守 Markdown 的双空格换行规则。

---

### Step 5: 开启自动更新链接

**路径**: `Settings → Files & Links → Automatically update internal links`

**开启。**

移动或重命名文件时 Obsidian 会自动更新已有链接，减少断链。

---

## 推荐插件（三类，极简原则）

**作者原则**：少装插件，只补关键体验。插件链越复杂，未来升级越容易坏。

### 1. Paste image rename
粘贴图片后自动重命名，避免 `Pasted image 202606012314.png`。  
**推荐命名规则**:

```
{{fileName}}-{{DATE:YYYYMMDDHHmmss}}
```

示例：当前笔记叫「写作工具」，粘贴图片后生成 → `写作工具-20260607123456.png`

---

### 2. Attachment Management
负责后续管理附件、整理引用、清理冗余图片。

---

### 3. QuickAdd
用于快速新建笔记、套模板、固定写作入口。对长期使用很有帮助。

---

## 快捷键映射（同步 Typora 肌肉记忆）

**路径**: `Settings → Hotkeys`

| 功能 | Typora 默认 | Obsidian 映射 |
|------|------------|---------------|
| H1 | `Cmd/Ctrl + 1` | 映射为 Heading 1 |
| H2 | `Cmd/Ctrl + 2` | 映射为 Heading 2 |
| H3 | `Cmd/Ctrl + 3` | 映射为 Heading 3 |
| 加粗 | `Cmd/Ctrl + B` | Bold |
| 斜体 | `Cmd/Ctrl + I` | Italic |
| 链接 | `Cmd/Ctrl + K` | Insert link |
| 代码块 | `Cmd/Ctrl + Shift + K` | Insert code block |

---

## 写作规范（长期稳定的核心）

> 真正长期稳定的关键，不是插件，而是写作规范。

| 规范 | 做法 |
|------|------|
| 永远不用 `[[ ]]` | 只用标准 Markdown 链接 |
| 永远不用 `![[image.png]]` | 只用 `![](images/image.png)` |
| 尽量不用 Obsidian 特殊语法 | 保持文件通用性 |
| 图片进 images/ 子目录 | 统一管理，方便迁移 |

**统一写法**:

```markdown
[链接文字](note.md)
![](images/image.png)
```

这样写出来的文件，以后用 Typora、VSCode、GitHub、静态博客或任何 Markdown 工具都能正常打开。

---

## 核心结论

> 如果你想把 Obsidian 当知识库，那就接受它的 wikilink、反链和图谱体系。
>
> 但如果你想要的是「Typora 式 Markdown 写作体验」，就应该反过来配置：
> **关闭 Wikilinks → 相对路径 → images 目录 → 标准 Markdown → 少量稳定插件补齐。**

**一句话**：这样配置后，Obsidian 更像一个「增强版 Typora」，而不是一个被插件链绑住的复杂知识库。

---

## 快速检查清单

- [ ] `Settings → Files & Links → Use Wikilinks` → **关闭**
- [ ] `Settings → Files & Links → New link format` → 选 **Relative path to file**
- [ ] `Settings → Files & Links → Default location for new attachments` → `In subfolder under current folder` → folder name `images`
- [ ] `Settings → Editor → Strict line breaks` → **关闭**
- [ ] `Settings → Files & Links → Automatically update internal links` → **开启**
- [ ] 安装 **Paste image rename** 插件，配置命名规则 `{{fileName}}-{{DATE:YYYYMMDDHHmmss}}`
- [ ] 安装 **Attachment Management** 插件
- [ ] 安装 **QuickAdd** 插件（可选但推荐）
- [ ] `Settings → Hotkeys` → 按 Typora 映射调整快捷键
- [ ] 写作规范：永远不用 `[[ ]]` 和 `![[...]]`，只用标准 Markdown

---

*来自翡冷翠*