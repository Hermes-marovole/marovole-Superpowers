# Cloud-Mail: 零成本自建邮箱服务完整指南

> 来源：https://x.com/axiaisacat/status/2048349647949778982  
> 作者：@axiaisacat (Independent developer building AI-powered web products)  
> 整理时间：2026-04-26

---

## 简介

这是一套基于 Cloudflare Workers 部署的零成本自建邮箱服务方案。作者仅花费 20 元购买域名，即可搭建功能完整的私有邮件系统，实现收发邮件、附件处理、群发、Telegram 推送、权限管理等功能，服务器费用为 0 元。

## 核心价值

| 维度 | 传统方案 | Cloud-Mail 方案 |
|------|----------|-----------------|
| 域名成本 | ¥20-100/年 | ¥20/年 |
| 服务器费用 | ¥50-500/月 | ¥0 |
| 邮件数量限制 | 取决于服务商 | 无限制 |
| 隐私保护 | 服务商可见 | 完全私有 |
| 自定义程度 | 受限 | 完全可控 |

---

## 技术架构

### 核心组件

```
┌─────────────────────────────────────────────────────────────┐
│                        用户层                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Web UI   │  │ SMTP客户端│  │ Telegram │  │ API调用  │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
└───────┼──────────────┼─────────────┼─────────────┼────────┘
        │              │             │             │
        └──────────────┴─────────────┴─────────────┘
                          │
                    ┌─────┴─────┐
                    │ Cloudflare│
                    │  Workers  │
                    └─────┬─────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   ┌────┴────┐      ┌────┴────┐      ┌────┴────┐
   │Mailchannels│    │ R2存储  │      │ D1数据库 │
   │(邮件发送) │      │(附件)   │      │(元数据) │
   └─────────┘      └─────────┘      └─────────┘
```

### 技术栈

| 组件 | 服务/技术 | 成本 |
|------|-----------|------|
| 边缘计算 | Cloudflare Workers | 免费 (10万次/天) |
| 邮件发送 | Mailchannels | 免费 |
| 对象存储 | Cloudflare R2 | 免费 (10GB/月) |
| 数据库 | Cloudflare D1 | 免费 (5GB/月) |
| 域名 | 任意域名服务商 | ~¥20/年 |

---

## 功能特性详解

### 1. 收发邮件

通过 Cloudflare Workers 接收 HTTP 请求，调用 Mailchannels API 实现邮件发送。接收邮件可通过 Email Routing 将邮件转发到 Workers 处理。

**发送邮件示例代码：**
```typescript
// 使用 Mailchannels 发送邮件
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const { to, subject, text, html } = await request.json();
    
    const resp = await fetch('https://api.mailchannels.net/tx/v1/send', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({
        personalizations: [{ to: [{ email: to }] }],
        from: { email: env.FROM_EMAIL },
        subject,
        content: [
          { type: 'text/plain', value: text },
          ...(html ? [{ type: 'text/html', value: html }] : [])
        ]
      })
    });
    
    return new Response(JSON.stringify({ success: resp.ok }));
  }
};
```

### 2. 附件处理

使用 Cloudflare R2 对象存储保存附件，通过 Workers 进行上传/下载代理。

**附件上传流程：**
```
1. 客户端 → Workers (multipart/form-data)
2. Workers 验证权限 → 保存到 R2
3. 返回附件 URL/ID
4. 邮件中插入附件链接
```

### 3. 群发功能

支持批量邮件发送，可通过 Mailchannels 的批量 API 或循环单发实现。

**批量发送控制：**
- 速率限制：避免触发 Mailchannels 限制
- 分批处理：大批量分片发送
- 失败重试：自动重试机制

### 4. Telegram 推送

通过 Telegram Bot API 实现新邮件实时推送。

**推送逻辑：**
```typescript
async function notifyTelegram(message: string, env: Env) {
  await fetch(`https://api.telegram.org/bot${env.TG_BOT_TOKEN}/sendMessage`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({
      chat_id: env.TG_CHAT_ID,
      text: message,
      parse_mode: 'Markdown'
    })
  });
}
```

### 5. 权限管理

基于 D1 数据库的用户权限系统：

| 角色 | 权限 |
|------|------|
| Admin | 全部功能、用户管理 |
| User | 收发邮件、查看自己的记录 |
| Guest | 仅发送（受限） |

---

## 部署步骤

### 前置准备

1. **Cloudflare 账号**（免费注册）
2. **域名**（约 ¥20/年，推荐 .com/.net）
3. **Telegram Bot**（通过 @BotFather 创建）

### 步骤 1：初始化项目

```bash
# 安装 Wrangler CLI
npm install -g wrangler

# 登录 Cloudflare
wrangler login

# 创建项目
mkdir cloud-mail && cd cloud-mail
wrangler init
```

### 步骤 2：配置 wrangler.toml

```toml
name = "cloud-mail"
main = "src/index.ts"
compatibility_date = "2026-04-26"

[env.production]
vars = { ENVIRONMENT = "production" }

[[env.production.r2_buckets]]
binding = "ATTACHMENTS"
bucket_name = "mail-attachments"

[[env.production.d1_databases]]
binding = "DB"
database_name = "mail-db"
database_id = "your-database-id"
```

### 步骤 3：绑定域名与 Email Routing

1. 在 Cloudflare Dashboard 添加域名
2. 配置 DNS 记录指向 Workers
3. 启用 Email Routing 功能
4. 设置 catch-all 规则转发到 Workers

### 步骤 4：部署

```bash
# 创建 D1 数据库
wrangler d1 create mail-db

# 创建 R2 Bucket
wrangler r2 bucket create mail-attachments

# 部署
wrangler deploy
```

---

## 参考项目

| 项目 | 链接 | 特点 |
|------|------|------|
| sumitkolhe/cloud-mail | https://github.com/sumitkolhe/cloud-mail | 基础 Mailchannels 集成 |
| fptbb/CloudflareMailsOnGmail | https://github.com/fptbb/CloudflareMailsOnGmail | Gmail 界面集成 |
| yaoyao-moe/cf-mailchannels-sender | https://github.com/yaoyao-moe/cf-mailchannels-sender | 简化发送 Worker |

---

## 成本分析

### 免费额度（Cloudflare Free Plan）

| 服务 | 免费额度 | 超出费用 |
|------|----------|----------|
| Workers | 100,000 请求/天 | $0.30/百万请求 |
| Workers KV | 1GB 存储 | $0.50/GB/月 |
| R2 | 10GB 存储/月 | $0.015/GB/月 |
| D1 | 5GB 存储/月 | 待公布 |
| Mailchannels | 无限（需验证域名） | 免费 |

### 总成本估算

| 项目 | 年费 |
|------|------|
| 域名 (.com) | ~¥70 |
| Cloudflare 服务 | ¥0 |
| Mailchannels | ¥0 |
| **总计** | **~¥70/年** |

---

## 安全建议

1. **验证域名**：在 Mailchannels 验证域名，避免进入垃圾邮件箱
2. **DKIM/SPF**：配置 DNS 记录提高邮件送达率
3. **Rate Limiting**：在 Workers 中实现请求限流
4. **Input Validation**：严格验证邮件地址和内容
5. **Secrets 管理**：使用 Cloudflare Secrets 存储敏感信息

---

## 适用场景

- ✅ 个人私有邮箱（替代 Gmail/Outlook）
- ✅ 网站/应用的事务邮件发送（验证码、通知）
- ✅ 小型团队的内部邮件系统
- ✅ 邮件备份和归档
- ✅ 自动化邮件处理工作流

---

## 局限性

1. **Mailchannels 限制**：免费版有日发送限制
2. **接收邮件复杂**：需要 Email Routing + Workers 配合
3. **无原生 IMAP**：需自行实现或仅通过 API 访问
4. **邮件存储**：需自行管理存储和检索逻辑

---

## 扩展方向

1. **Web UI**：开发 React/Vue 前端界面
2. **移动 App**：封装为 iOS/Android App
3. **AI 集成**：自动分类、智能回复
4. **多域名支持**：支持多个域名共用同一 Workers
5. **邮件模板**：集成模板系统支持营销邮件

---

*来自翡冷翠*
