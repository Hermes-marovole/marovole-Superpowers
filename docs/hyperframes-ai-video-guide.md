# HyperFrames - AI 驱动的 HTML 视频生成框架

> Write HTML. Render video. Built for agents.

**来源：** [X 用户 @xiaoerzhan 分享](https://x.com/xiaoerzhan/status/2046983869363314712) ｜ [GitHub 仓库](https://github.com/heygen-com/hyperframes)

---

## 目录

1. [核心概述](#核心概述)
2. [实战使用指南](#实战使用指南)
3. [项目详情](#项目详情)
4. [相关资源](#相关资源)
5. [学习路径](#学习路径)

---

## 核心概述

**HyperFrames** 是由 **HeyGen** 开源的 AI 原生视频渲染框架，专为 AI Agent 设计，实现「HTML 代码 → MP4 视频」的无缝转换。

### 为什么值得关注

| 特性 | 说明 |
|------|------|
| 🎯 **Agent-First** | 原生支持 Claude Code、OpenAI Codex 等 AI 编程 Agent |
| 🎨 **HTML → Video** | 用熟悉的 Web 技术（CSS/JS/React）编写动画，直接渲染为视频 |
| 🔧 **精细控制** | 完全理解自然语言指令调整（动效、细节、节奏） |
| 🚀 **开源免费** | HeyGen 用此框架制作了自己的产品发布视频 |
| ⚡ **快速启动** | 一行命令 `npx skills add heygen-com/hyperframes` |

### 核心技术原理

```
HTML/CSS/JS 动画代码
        ↓
  [HyperFrames 引擎]
        ↓
    MP4 视频输出
```

---

## 实战使用指南

### 基于 @xiaoerzhan 的实测经验

#### 步骤 1：提供网址和定位
- 给 AI Agent 你的网站地址
- 明确告知网站的定位/品牌调性

#### 步骤 2：选择风格参数
- **调性**：选择适合的品牌风格（科技感/文艺/活力等）
- **配音**：可选是否添加语音
- **特效方向**：预设的视觉风格偏好
- **回答四个关键问题**（系统引导）

#### 步骤 3：迭代优化
- 第一轮生成通常不完美
- 耐心用自然语言指导调整

#### 步骤 4：高级技巧
> **不配音更高级** — 要求提供「实验音乐」配合视觉

#### 步骤 5：精准调试指令

| 调试目标 | 指令示例 |
|----------|----------|
| 加强动效 | "加强动效，让画面更有活力" |
| 丰富细节 | "细节不够丰富，增加纹理质感" |
| 节奏控制 | "节奏卡点，与音乐同步" |
| 材质质感 | "请做一个纸张质感的底" |
| 氛围调整 | "画面太安静，增加动态元素" |

**核心优势**：完全理解自然语言指令，精准执行到位

---

## 项目详情

### 基础信息

| 项目 | 内容 |
|------|------|
| **仓库** | [github.com/heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) |
| **开发方** | HeyGen (知名 AI 视频生成平台) |
| **开源协议** | 开源 |
| **Star 数** | 9.2k+ |
| **Fork 数** | 738 |
| **安装命令** | `npx skills add heygen-com/hyperframes` |

### 支持的 AI Agent

| Agent 类型 | 支持状态 | 安装方式 |
|------------|----------|----------|
| **Claude Code** | ✅ 原生支持 | `npx skills add heygen-com/hyperframes` |
| **OpenAI Codex** | ✅ 支持 | 提供 `.codex-plugin` 插件 |
| **其他 AI Agent** | ✅ 可适配 | Agent-Native 框架设计 |

### 项目结构

```
hyperframes/
├── .claude/           # Claude Code 配置
├── .codex-plugin/     # OpenAI Codex 插件
├── docs/              # 文档
├── packages/          # 核心包
├── registry/          # 技能注册表
├── skills/            # 预设技能
├── AGENTS.md          # Agent 集成指南
├── CLAUDE.md          # Claude 专用配置
├── DESIGN.md          # 设计系统文档
└── README.md          # 项目说明
```

### 核心能力

1. **HTML-Based Compositions**：使用熟悉的 Web 技术栈创建视频合成
2. **Live Preview**：实时预览动画效果
3. **High-Quality Rendering**：高质量 MP4 视频输出
4. **Agent Integration**：与 AI Agent 深度集成
5. **Component System**：可复用的视频组件系统

### 获取源代码

根据原始 X 帖子，转发并评论 "HyperFrames" 并关注账号，可获取完整发布视频的源代码。

---

## 相关资源

### 官方资源

| 资源 | 链接 | 说明 |
|------|------|------|
| GitHub 仓库 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 开源代码 |
| NPM 包 | [hyperframes](https://www.npmjs.com/package/hyperframes) | Node.js 包 |
| HeyGen 官方 | [@HeyGen](https://x.com/HeyGen) | 产品发布账号 |

### 学习材料

| 类型 | 内容 |
|------|------|
| **Agent 指南** | `AGENTS.md` - AI Agent 集成文档 |
| **Claude 配置** | `CLAUDE.md` - Claude Code 专用配置 |
| **设计系统** | `DESIGN.md` - 设计规范与最佳实践 |
| **贡献指南** | `CONTRIBUTING.md` - 参与开源贡献 |

### 社区资源

- **X 讨论**：[@xiaoerzhan](https://x.com/xiaoerzhan) 分享的使用心得
- **GitHub Issues**：[45+ PRs](https://github.com/heygen-com/hyperframes/pulls) 活跃开发中

---

## 学习路径

### 初学者路线

```
1. 安装 Claude Code 或支持 Agent 的编辑器
   ↓
2. 运行 npx skills add heygen-com/hyperframes
   ↓
3. 跟随 Agent 提示创建第一个视频
   ↓
4. 基于模板修改 HTML/CSS 自定义样式
   ↓
5. 迭代优化至满意效果
```

### 进阶路线

```
1. 阅读 DESIGN.md 理解设计系统
   ↓
2. 研究 packages/ 目录下的核心代码
   ↓
3. 创建自定义组件并贡献到 registry
   ↓
4. 集成到自己的产品工作流
   ↓
5. 探索与其他 AI 工具的联动可能性
```

### 应用场景

| 场景 | 应用方式 |
|------|----------|
| **产品发布视频** | 快速生成高质量品牌宣传视频 |
| **社交媒体内容** | 批量生成统一风格的短视频 |
| **演示文稿** | 将 PPT 转换为动态视频演示 |
| **动态海报** | 生成带动画的品牌物料 |
| **实验艺术** | 结合实验音乐创作视觉作品 |

---

## 总结

HyperFrames 代表了 AI 视频生成的新范式：

- **非模板化**：不像传统视频工具依赖预设模板
- **代码优先**：用 Web 技术栈的表达能力
- **Agent-Native**：为 AI 协作而生，自然语言即可精确控制
- **开源生态**：HeyGen 将其产品级工具开源，社区共建

对于熟悉前端开发的创作者，HyperFrames 提供了一个极具潜力的「代码驱动视频」新工作流。

---

*来自翡冷翠*

*最后更新：2026-04-23*
