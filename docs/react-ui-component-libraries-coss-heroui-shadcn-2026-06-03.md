# 最漂亮最简洁的 React UI 组件库：COSS UI vs HeroUI vs shadcn/UI

> 来源：[Viking @vikingmute 推文](https://x.com/vikingmute/status/2061979261637181775) — "最近一个月看来看去，觉得最漂亮最简洁的组件库就这两个了"
> 整理时间：2026-06-03
> 来自翡冷翠

---

## 简介

独立开发者 Viking（作品 [TinyShip](http://tinyship.cn)、[简单简历](http://easycv.cn)）在 2026 年 6 月分享了他最近一个月调研后的 UI 组件库推荐。他认为 **COSS UI** 和 **HeroUI** 是目前最漂亮、最简洁的两个 React 组件库——如果你已经用厌了 shadcn/UI 的默认样式，这两个值得尝试。

Viking 个人更偏爱 **COSS UI**，原因是：简洁、美观、组件全、细节考究，且对 AI 非常友好。

本文将这三个库的完整信息做系统整理，方便你在选型时快速对比。

---

## 三库对比总览

| 维度 | COSS UI | HeroUI (v3) | shadcn/ui |
|------|---------|-------------|-----------|
| **定位** | Cal.com 官方设计系统 | 现代全功能 React 组件库 | 开源代码优先的组件分发平台 |
| **前身/背景** | Origin UI（被 Cal.com 收购） | NextUI（更名为 HeroUI） | 2023 年发布，迅速成为主流 |
| **GitHub Stars** | ~9.8k | ~29,500 | ~115,500 |
| **技术栈** | React 19 + Base UI + Tailwind v4 | React 19 + React Aria + Tailwind v4 | React 19 + Radix/Base UI + Tailwind v4 |
| **分发模式** | Copy-paste（代码归你） | npm 包（自动更新） | Copy-paste + 官方 CLI |
| **组件数量** | 50+ | 70+ | 411+（含 blocks/charts/hooks） |
| **主题系统** | 内置主题 + 自定义 CSS 变量 | 10+ 预设主题 + 交互式主题构建器 | 主题变量 + v0 可视化构建器 |
| **AI 友好度** | ⭐⭐⭐⭐⭐（llms.txt + Skills） | ⭐⭐⭐⭐⭐（AI-native API + Chat） | ⭐⭐⭐⭐⭐（Skills + MCP Server） |
| **移动端** | 暂无 | HeroUI Native（React Native） | 暂无原生支持 |
| **生产成熟度** | Early Access（Cal.com 自用） | 成熟稳定，活跃维护 | 非常成熟，生态最大 |
| **Viking 评分** | ⭐⭐⭐⭐⭐（个人首选） | ⭐⭐⭐⭐⭐（色彩活泼） | 基准参考（用厌了可换） |

---

## COSS UI — Viking 的首选

> "基于 BaseUI，简洁、美观、组件全，细节非常考究，还有 skills 等等资源，对 AI 非常友好。"
> — Viking

### 核心信息

- **官网**：https://coss.com/ui
- **GitHub**：https://github.com/cosscom/coss（~9.8k ⭐）
- **文档**：https://coss.com/ui/docs
- **背景**：Cal.com 官方设计系统，由 Origin UI 演化而来
- **状态**：Early Access（Cal.com 内部生产验证中）

### 设计理念

1. **Copy-paste  ethos** — 代码复制到你项目中，没有黑盒包，你完全拥有代码
2. **Built for Humans and AI** — 组件写法清晰、可读、可预测，让 LLM 能理解和修改
3. **三层架构**：
   - **Primitives** — 无样式、无障碍的 Base UI 基础块
   - **Particles** — 预组装组件（表单、表格、日期选择器）
   - **Atoms** — API 增强的 Particles，集成外部服务
4. **COSS（Commercial Open Source Software）** — 商业开源软件哲学

### 技术栈

| 层级 | 技术 |
|------|------|
| 框架 | React 19.2.6, Next.js 16.2.5 |
| 基础组件 | Base UI 1.4.1（MUI 出品，无样式原语） |
| 样式 | Tailwind CSS v4.1.17 |
| 语言 | TypeScript 5.9.3 |
| 工具链 | Bun + Turborepo, Biome（lint/format） |
| 文档 | Fumadocs |
| 依赖 | TanStack React Table, Jotai, Lucide/Hugeicons/Remixicon |

### 完整组件清单（50+）

Accordion, Alert, Alert Dialog, Autocomplete, Avatar, Badge, Breadcrumb, Button, Calendar, Card, Checkbox, Checkbox Group, Collapsible, Combobox, Command, Date Picker, Dialog, Drawer, Empty, Field, Fieldset, Form, Frame, Group, Input, Input Group, Kbd, Label, Menu, Meter, Number Field, OTP Field, Pagination, Popover, Preview Card, Progress, Radio Group, Scroll Area, Select, Separator, Sheet, Sidebar, Skeleton, Slider, Spinner, Switch, Table, Tabs, Textarea, Toast, Toggle, Toggle Group, Toolbar, Tooltip

### AI 友好特性

- **`llms.txt`** — https://coss.com/ui/llms.txt 提供结构化 LLM 上下文，包含所有组件文档
- **Skills 资源** — 提供 AI 辅助开发的配套资源
- **可预测模式** — 组件结构一致，便于 AI 理解和修改

### Viking 推荐理由

> "简洁、美观、组件全，细节非常考究" — COSS UI 的默认审美水准很高，不需要大量二次调整就能做出干净、专业的界面。对独立开发者来说，这意味着更少的设计决策疲劳。

---

## HeroUI (v3) — 色彩鲜艳的活力之选

> "色彩鲜艳、更活泼，theme 丰富可定制化也很强"
> — Viking

### 核心信息

- **官网**：https://heroui.com
- **GitHub**：https://github.com/heroui-inc/heroui（~29,500 ⭐）
- **文档**：https://heroui.com/docs/react/getting-started
- **前身**：NextUI（2025 年更名为 HeroUI）
- **Roadmap**：https://herouiv3.featurebase.app/roadmap

### 设计理念

1. **Beautiful by default** — 开箱即用，动画流畅，视觉效果精致
2. **Accessible by default** — 基于 Adobe React Aria 构建，WCAG 合规、键盘导航、焦点管理、屏幕阅读器支持
3. **A living library** — 作为 npm 包分发，自动获得更新、bug 修复和新功能
4. **Deep customization** — 每个组件由可自定义的 parts/slots 组成，通过 Tailwind utilities、CSS 变量、BEM 修饰符或组合修改
5. **AI-native** — 为 AI 辅助开发设计，API 可预测、完全类型化

### 技术栈

| 层级 | 技术 |
|------|------|
| 核心 | React 19, React Aria Components（Adobe） |
| 样式 | Tailwind CSS v4 |
| 构建 | TypeScript, tsup, pnpm, Turbo |
| 测试 | Jest, React Testing Library, Storybook |
| 渲染 | 支持 Server Components，Tree-shakeable |

### 预设主题（10+）

| 主题 | 风格 |
|------|------|
| default | 默认 |
| sky | 天蓝 |
| lavender | 薰衣草紫 |
| mint | 薄荷绿 |
| netflix | Netflix 红黑 |
| black | 纯黑极简 |
| spotify | Spotify 绿黑 |
| coinbase | Coinbase 蓝 |
| airbnb | Airbnb 粉红 |
| discord | Discord 紫黑 |

### 完整组件清单（70+）

**Collections**：Dropdown, ListBox, TagGroup  
**Colors**：ColorArea, ColorField, ColorPicker, ColorSlider, ColorSwatch, ColorSwatchPicker  
**Controls**：Slider, Switch  
**Data Display**：Badge, Chip, Table  
**Date & Time**：Calendar, DateField, DatePicker, DateRangePicker, RangeCalendar, TimeField  
**Feedback**：Alert, Meter, ProgressBar, ProgressCircle, Skeleton, Spinner  
**Forms**：Checkbox, CheckboxGroup, Description, ErrorMessage, FieldError, Fieldset, Form, Input, InputGroup, InputOTP, Label, NumberField, RadioGroup, SearchField, TextField, TextArea  
**Layout**：Card, Separator, Surface, Toolbar  
**Media**：Avatar  
**Navigation**：Accordion, Breadcrumbs, Disclosure, DisclosureGroup, Link, Pagination, Tabs  
**Overlays**：AlertDialog, Drawer, Modal, Popover, Toast, Tooltip  
**Pickers**：Autocomplete, ComboBox, Select  
**Typography**：Kbd  
**Utilities**：ScrollShadow  
**移动端（HeroUI Native）**：React Native 组件库

### 生态系统

- **HeroUI v3** — Web 端 React 组件
- **HeroUI Native** — React Native 移动端组件
- **HeroUI Chat** — 自然语言生成 App（Text-to-App）
- **UI for LLMs** — LLM 专用 UI 平台和 MCP（即将推出）

### Viking 推荐理由

> "色彩鲜艳、更活泼" — HeroUI 的默认主题比 shadcn/UI 更有视觉张力，预设主题丰富（Netflix、Spotify、Airbnb 等），适合需要强烈品牌风格的 SaaS 产品。

---

## shadcn/ui — 基准参考

> "如果大家用厌了 shadcn/UI 的默认样式，可以试试这两个组件库"
> — Viking

### 核心信息

- **官网**：https://ui.shadcn.com
- **GitHub**：https://github.com/shadcn-ui/ui（~115,500 ⭐）
- **CLI**：`npx shadcn@latest`
- **最新版本**：shadcn@4.10.0（2026-06）

### 设计理念

1. **Open Code** — 组件复制到源码，非黑盒导入
2. **Composition** — 基于 Radix/Base UI 原语的共享、可组合接口
3. **Distribution** — 扁平文件注册表 + CLI 跨项目分发代码
4. **Beautiful Defaults** — 使用 CSS 变量的极简统一美学
5. **AI-Ready** — Skills 包 + MCP Server 支持 LLM/AI 助手集成

### 技术栈

React 19, Next.js 16, Tailwind CSS v4, Radix UI（统一包）+ Base UI（`@base-ui/react`）, `class-variance-authority`, `lucide-react`, `next-themes`, `recharts`, React Hook Form / TanStack Form / Formisch

### 2026 年新特性

- **Blocks** — 页面级区块（header、dashboard、settings 等）
- **Charts** — 基于 Recharts 的图表组件
- **shadcn/create** — 可视化主题构建器
- **Registry v2** — GitHub 注册表、命名空间、认证
- **Skills + MCP Server** — AI 集成
- **v0 集成** — AI 生成 UI 并直接导入
- **Figma Plugin** — 设计到代码
- **`npx shadcn eject`** — 从现有包中弹出组件源码

### 已知局限

- 无自动上游更新（自定义后需手动 diff/merge）
- 生态锁定在 React + Tailwind
- 组件数量少于成熟企业级库
- 默认风格极简，深度定制需 Tailwind  expertise
- 社区注册表质量参差不齐

---

## 选型建议

### 选择 COSS UI，如果你：

- ✅ 喜欢 Viking 的审美偏好——简洁、干净、细节考究
- ✅ 使用 AI 辅助开发（llms.txt 和可预测组件模式是巨大优势）
- ✅ 想要 copy-paste 模式，完全掌控代码
- ✅ 做 SaaS / B2B 工具，需要专业克制的界面
- ✅ 项目基于 Next.js / React

### 选择 HeroUI，如果你：

- ✅ 需要更活泼、更有视觉张力的默认风格
- ✅ 想要丰富的预设主题（Netflix、Spotify 等风格）
- ✅ 需要移动端支持（HeroUI Native）
- ✅ 想要 npm 包自动更新，而非手动管理源码
- ✅ 对颜色选择器、时间选择器等特殊组件有需求
- ✅ 对 Adobe React Aria 的无障碍能力有信任

### 继续使用 shadcn/ui，如果你：

- ✅ 已经深度集成，换库成本高
- ✅ 需要最大的生态（411+ 组件、blocks、charts、hooks、themes）
- ✅ 依赖 v0 / Figma Plugin 等 AI 设计工具链
- ✅ 团队已熟悉其工作流

---

## 快速上手命令

### COSS UI
```bash
# 访问官网获取安装指引
# https://coss.com/ui/docs/get-started
# 目前 Early Access，可能需要申请或关注 GitHub 更新
```

### HeroUI
```bash
# 安装 HeroUI v3
npm install @heroui/react

# 或使用 CLI
npx heroui@latest init

# 文档
# https://heroui.com/docs/react/getting-started
```

### shadcn/ui
```bash
# 初始化
npx shadcn@latest init

# 添加组件
npx shadcn@latest add button card table

# 文档
# https://ui.shadcn.com/docs
```

---

## 资源汇总

### GitHub 仓库

| 项目 | 链接 | Stars |
|------|------|-------|
| COSS UI | https://github.com/cosscom/coss | ~9.8k |
| HeroUI | https://github.com/heroui-inc/heroui | ~29.5k |
| shadcn/ui | https://github.com/shadcn-ui/ui | ~115.5k |

### 官方文档

| 库 | 文档链接 |
|----|----------|
| COSS UI | https://coss.com/ui/docs |
| HeroUI v3 | https://heroui.com/docs/react/getting-started |
| HeroUI Native | https://heroui.com/docs/native/getting-started |
| shadcn/ui | https://ui.shadcn.com/docs |

### 值得关注的人/账号

- **[@vikingmute](https://x.com/vikingmute)** — Viking，独立开发者，TinyShip / 简单简历作者，前端审美品味值得信赖
- **[@coss_ui](https://x.com/coss_ui)** — COSS UI 官方账号
- **[@hero_ui](https://x.com/hero_ui)** — HeroUI 官方账号

---

*来自翡冷翠*
