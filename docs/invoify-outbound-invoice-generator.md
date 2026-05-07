# Invoify - 出海产品开源发票生成器

> 来源：X/Twitter @wsl8297 (Joruno)  
> GitHub: https://github.com/al1abb/invoify  
> 在线演示: https://invoify.vercel.app/  
> 整理时间：2026-05-07  
> 来自翡冷翠

---

## 简介

Invoify 是一款专为**出海产品独立开发者**设计的开源发票生成工具。它解决了「用 Stripe 等平台省事但要手续费，自己做又怕格式不专业、对方不认」的常见痛点。

基于 **Next.js 13 + TypeScript + Shadcn UI** 构建，Invoify 提供了一套完整的专业发票生成解决方案——国际通用的 invoice 模板、实时编辑预览、多格式导出、内置邮件发送、浏览器本地存储等功能一应俱全。

---

## 为什么需要它

### 海外发票 vs 国内发票

| 维度 | 国内发票 | 海外 Invoice |
|------|----------|--------------|
| **制度** | 税务强监管，必须使用指定格式 | 商业凭证，无强制格式要求 |
| **平台依赖** | 必须使用税务局指定平台 | Stripe、PayPal 等平台自动生成 |
| **手续费** | 无 | Stripe 等平台收取 2.9% + 固定费用 |
| **替代方案** | 几乎无 | 自行生成规范 PDF 即可 |

**核心洞察**：对于大多数海外收款场景，一份格式规范、字段齐全的商业 Invoice PDF 已经足够。不需要复杂的税务平台集成。

### 发布者洞察（@wsl8297）

> "做出海产品时，给海外客户开 invoice 常常很头疼：用 Stripe 之类的平台省事但要手续费，自己做又怕格式不专业、对方不认。
> 
> 其实海外 invoice 和国内发票不是一回事，大多数场景自己生成一份规范的 PDF 就够用。这时候 Invoify 这种开源工具就很合适。"

---

## 核心功能

### 1. 专业 Invoice 模板
- ✅ 国际通用的标准商业 invoice 模板
- ✅ 关键商业字段齐全（公司信息、客户信息、商品明细、税额、总计等）
- ✅ 2 套预设模板，可切换选择
- ✅ 主题颜色自定义

### 2. 实时编辑与预览
- ✅ 所见即所得的编辑体验
- ✅ 表单修改实时同步到预览
- ✅ 专业排版，格式规整

### 3. 多格式导出
| 格式 | 用途 |
|------|------|
| **PDF** | 发送给客户的标准格式 |
| **JSON** | 数据备份、程序化处理 |
| **XLSX** | Excel 进一步编辑 |
| **CSV** | 批量数据处理 |
| **XML** | 系统集成 |

### 4. 邮件发送功能
- ✅ 内置邮件服务（Nodemailer 集成）
- ✅ 一键将 PDF 发票发送给海外客户
- ✅ 支持自定义邮件内容

### 5. 数据管理
- ✅ **浏览器本地存储** - 历史发票可管理、可检索
- ✅ 发票草稿自动保存（localStorage）
- ✅ 从 JSON 导入历史发票

### 6. 国际化支持
- ✅ I18N 多语言支持
- ✅ 多币种支持，覆盖不同国家收款场景
- ✅ 自定义字段（如 VAT 税号等）

### 7. 智能输入（2026年4月新增）
- ✅ **语音输入组件** - 支持通过语音识别快速添加商品信息
- ✅ 中文数字解析功能

---

## 技术架构

### 核心技术栈

| 技术 | 用途 |
|------|------|
| **Next.js 13** | React 框架，支持 SSR 和客户端导航 |
| **TypeScript** | 静态类型检查，提升代码质量 |
| **Shadcn UI** | 现代化 UI 组件库 |
| **Tailwind CSS** | 原子化 CSS 框架 |
| **React Hook Form** | 表单状态管理 |
| **Zod** | TypeScript-first 数据校验 |
| **Puppeteer** | 无头浏览器，PDF 生成 |
| **Nodemailer** | Node.js 邮件发送模块 |

### 仓库统计

- ⭐ **Stars**: 6.3k
- 🍴 **Forks**: 699
- 👥 **贡献者**: 37 人
- 📄 **许可证**: MIT
- 🔤 **主要语言**: TypeScript (98.1%)

---

## 快速开始

### 方式一：在线使用（推荐）

直接访问演示站点，无需部署：

👉 **[https://invoify.vercel.app/](https://invoify.vercel.app/)**

### 方式二：本地部署

```bash
# 1. 克隆仓库
git clone https://github.com/al1abb/invoify.git
cd invoify

# 2. 安装依赖
npm install

# 3. 配置环境变量（如需邮件功能）
cat > .env.local << EOF
NODEMAILER_EMAIL=your_email@example.com
NODEMAILER_PW=your_email_password
EOF

# 4. 启动开发服务器
npm run dev

# 5. 访问 http://localhost:3000
```

### 方式三：Docker 部署

```bash
# 使用多阶段构建的 Dockerfile，镜像体积减少约 50%
docker build -t invoify .
docker run -p 3000:3000 invoify
```

---

## 功能路线图

- [x] 简易发票创建 - 表单快速生成
- [x] 浏览器本地存储 - 保存历史发票
- [x] 便捷检索 - 从历史列表加载
- [x] 灵活下载 - PDF 下载或邮件发送
- [x] 多套模板 - 2 种 invoice 模板可选
- [x] 实时预览 - 编辑实时同步预览
- [x] 多格式导出 - JSON/XLSX/CSV/XML
- [x] 国际化支持 - UI 和模板多语言
- [x] 主题定制 - 发票主题颜色选择
- [x] 自定义字段 - 添加默认表单中缺少的字段
- [x] 单项税额 - 支持单个商品的独立税率
- [x] 语音输入 - 语音识别快速录入商品

---

## 适用场景

### 适合使用 Invoify 的场景

| 场景 | 说明 |
|------|------|
| **独立开发者/出海产品** | 为海外客户生成专业 invoice |
| **自由职业者** | 向国际客户开具服务发票 |
| **小型 SaaS** | 为客户账单生成 PDF 凭证 |
| **咨询服务** | 项目交付后的收款凭证 |
| **跨境电商** | 简化 invoice 生成流程 |

### 不适合的场景

- 需要与税务系统直连的合规发票（如欧盟 VAT 申报发票）
- 大规模自动化发票生成（无批量 API）
- 复杂的多层级审批流程

---

## 注意事项

⚠️ **浏览器兼容性**：目前 Mozilla Firefox 浏览器存在兼容性问题，建议使用 Chrome/Edge/Safari。

🔗 **参考 Issue**: [#11](https://github.com/al1abb/invoify/issues/11)

---

## 相关资源

### 官方链接
- GitHub 仓库: https://github.com/al1abb/invoify
- 在线演示: https://invoify.vercel.app/
- Discord 社区: https://discord.gg/uhXKHbVKHZ

### 技术标签
`react` `typescript` `nextjs` `invoice-generator` `zod` `react-hook-form` `shadcn-ui`

---

## 快速参考

### 核心优势速查

| 优势 | 说明 |
|------|------|
| **零手续费** | 自建方案，无第三方平台抽成 |
| **格式专业** | 国际通用模板，客户认可度高 |
| **数据自主** | 本地存储，发票数据完全掌控 |
| **开箱即用** | 在线演示站直接可用，或一键部署 |
| **开源免费** | MIT 许可证，可自由定制 |

### 决策树

```
需要给海外客户开发票？
    ↓
使用 Stripe/PayPal 等平台？
    ↓ 是 → 接受 2.9%+ 手续费
    ↓ 否
想自建但怕格式不专业？
    ↓ 是 → 使用 Invoify ✅
    ↓ 否 → 自行设计 PDF 模板
```

---

*来自翡冷翠*
