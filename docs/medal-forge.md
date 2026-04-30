# Medal Forge - SVG 转 3D 奖章生成器

> **来源**：https://github.com/CatsJuice/medal-forge  
> **在线演示**：https://medal.oooo.so/  
> **作者**：[@CatsJuice](https://github.com/CatsJuice)  
> **整理时间**：2025-04-28  
> 来自翡冷翠

---

## 简介

Medal Forge 是一个基于 Next.js 的开源原型工具，专注于将上传的 **SVG 矢量图形** 转换为简单的 **3D 奖章、徽章和金属牌模型**。无需复杂的 3D 建模软件，只需上传 SVG 文件即可获得可导出的 3D 模型。

---

## 核心功能

| 功能 | 说明 |
|------|------|
| **SVG 上传** | 支持文件上传或直接粘贴 SVG 代码 |
| **实时预览** | 直接预览 SVG 图层的 3D 挤出效果 |
| **本地存储** | 作品自动保存到 IndexedDB，支持从侧边栏加载历史作品 |
| **导出功能** | 支持导出 JSON（含原始 SVG 源文件）和 GLB 3D 模型 |
| **代码生成** | 一键复制 React/Three.js 代码片段 |

### 图层编辑能力

- **多选操作**：Cmd/Ctrl+点击多选、Shift+点击范围选择、Cmd/Ctrl+A 全选、Esc 清空
- **精细调整**：
  - 每个形状的厚度（Thickness）
  - 倒角/斜面（Bevel）
  - 材质（Material）
  - 颜色（Color）
  - 精度（Precision）
  - 可见性（Visibility）
  - 前后高度偏移（Front/Back Height Offset）
- **颜色重置**：一键将选中形状颜色恢复为原始 SVG 颜色

---

## 技术栈

| 技术 | 用途 |
|------|------|
| **Next.js** | React 全栈框架 |
| **TypeScript** | 类型安全（占比 86.6%）|
| **Three.js / React-Three** | 3D 渲染 |
| **IndexedDB** | 本地数据持久化 |
| **GLB 导出** | 标准 3D 模型格式 |

---

## 快速开始

### 本地安装

```bash
# 克隆仓库
git clone https://github.com/CatsJuice/medal-forge.git
cd medal-forge

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

### 使用方法

1. 打开浏览器访问 `http://localhost:3000`
2. 上传或粘贴你的 SVG 设计
3. 在右侧图层列表中选择要调整的图层
4. 调整厚度、倒角、材质等参数
5. 预览 3D 效果
6. 导出 GLB 模型或复制 React/Three 代码

---

## 项目结构

```
medal-forge/
├── app/              # Next.js App Router 页面
├── components/       # React 组件
├── lib/              # 工具函数和核心逻辑
├── public/           # 静态资源
├── README.md         # 项目文档
├── package.json      # 依赖配置
└── next.config.ts    # Next.js 配置
```

---

## 使用场景

- 🏅 **活动奖章设计** - 快速生成活动纪念徽章的 3D 预览
- 🎖️ **NFT/数字藏品** - 将 SVG 艺术转换为 3D 模型导出
- 🏷️ **产品铭牌** - 设计金属质感的产品标签/铭牌
- 🎨 **原型设计** - 快速验证 2D 设计在 3D 空间的效果
- 🧪 **Three.js 学习** - 查看生成的 React/Three 代码片段学习 3D 编程

---

## 项目数据

| 指标 | 数值 |
|------|------|
| Stars | 49 |
| Forks | 4 |
| Contributors | 1 (@CatsJuice) |
| 主要语言 | TypeScript (86.6%) |
| 创建时间 | 2026-04-27 |

---

## 相关资源

- **GitHub 仓库**：https://github.com/CatsJuice/medal-forge
- **在线演示**：https://medal.oooo.so/
- **作者主页**：https://github.com/CatsJuice

---

## 注意事项

- 这是一个原型/概念验证项目，功能聚焦且简洁
- SVG 复杂度会影响 3D 转换效果，建议使用简洁的矢量图形
- 导出的 GLB 模型可用于 Blender、Unity、Three.js 等 3D 工作流

---

*来自翡冷翠*
