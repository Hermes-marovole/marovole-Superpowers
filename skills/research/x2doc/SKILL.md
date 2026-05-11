---
name: x2doc
description: "从 X/Twitter 帖子提取内容整理成文档，并自动生成可直接复制的转发推文。结合 link2doc 的深度文档整理能力与 xrepost 的解读转发能力。"
category: research
tags: [x-twitter, tutorial, documentation, curation, repost, social-media]
---

# X2Doc 组合工作流（X 帖子 → 文档 + 转发推文 + 充实邮件通知）

从 X/Twitter 帖子提取内容整理成文档，自动生成可直接复制发布的转发推文，并发送充实版邮件通知。

**整合 Link2Doc 核心能力**：
- 深度内容策展流程（包含发布者洞察提取）
- 充实版邮件通知（核心价值主张、精选亮点、适用场景）
- 多来源提取策略（X Article、Quote Chain、评论区等）

## 触发方式

用户在 Telegram 中发送：
```
https://x.com/{username}/status/{id} x2doc
```

或：
```
https://x.com/{username}/status/{id} link2doc
```

或：
```
https://x.com/{username}/status/{id} 整理并转发
```

## 输出结构

执行完整流程后，输出包含三部分：

1. **GitHub 文档提交确认** —— 按 link2doc 标准模板
2. **可直接复制的转发推文** —— 按 xrepost 标准格式
3. **邮件发送确认** —— 充实版邮件通知（含附件）

---

## 核心工作流

### Step 0: 理解任务与来源分析

**明确关键信息：**
- 来源链接是什么？（X 帖子、博客、GitHub 等）
- 目标仓库是哪个？（默认：`marovole-Superpowers`，路径 `~/workspace/marovole-Superpowers`，GitHub: `https://github.com/Hermes-marovole/marovole-Superpowers`）
- 文档应放在哪个目录？（默认：`docs/`）
- 是否需要邮件通知？（默认发送给 marovole@gmail.com）

**署名要求（必须遵守）：**
- 文末署名：**"来自翡冷翠"**
- 禁止写："本文由 Neuma AI Agent 整理输出" 等机器人式表述
- 禁止写："本文档由AI助手整理"、"由智子生成"、"PM Agent整理"、"Neuma Inc."等机器式/公司式属名
- **重要区分**：Neuma 是公司名称，但所有产出内容必须以**个人身份（翡冷翠）**署名，不要用公司名义
- 教程内容应面向"任何人"，不限定为"Neuma 团队"

### Step 1: 执行完整 Link2Doc 内容策展

#### 场景 A: X/Twitter 帖子提取

**首选方案：Jina Reader 直接提取**

```python
# 使用 Jina Reader 提取 X 帖子内容
curl -sL "https://r.jina.ai/http://x.com/{username}/status/{id}"
```

**备用方案：浏览器提取**

```python
browser_navigate(url="https://x.com/{username}/status/{id}")
browser_snapshot(full=true)
```

#### 场景 A-1: X/Twitter Articles（长文/长帖）

**推荐首选方案：Jina Reader 直接提取**

```python
# 格式: r.jina.ai/http://x.com/{user}/status/{status_id}
curl -sL "https://r.jina.ai/http://x.com/{user}/status/{status_id}"
```

#### 场景 A-2: X/Twitter Quote Chains（引用链）

**处理策略**：
```python
# 访问初始帖子
browser_navigate(url="https://x.com/...")
snapshot = browser_snapshot(full=true)

# 检查是否有 Quote 引用，递归处理
# 寻找包含 "Quote" 的 link 元素
browser_click(ref="e21")  # 引用链接的 ref
snapshot = browser_snapshot(full=true)
```

#### 场景 A-3: X/Twitter 评论区内容获取

当主贴说"提示词在评论区"但点击后需要登录时：

**处理策略**：
```python
# 使用搜索引擎找第三方镜像站点
web_search(query="{帖子主题} prompt {作者名}")

# 常见第三方镜像站点：
# - AI 提示词库（如 pixps.com）
# - 中文技术社区（即刻、小红书、知乎）
# - AI 工具导航站
```

### Step 2: 发布者洞察提取（关键步骤！）

**这是 Link2Doc 的核心能力**：

```python
# 洞察提取清单
insights_to_extract = {
    "personal_experience": "发布者使用这个工具/方法的实际经历",
    "key_benefit": "相比其他方案的核心优势（省时、省事、效果好等）",
    "why_recommend": "发布者推荐的具体理由",
    "use_case": "发布者描述的具体使用场景",
    "direct_quote": "可以直接引用的发布者原话"
}
```

### Step 3: 构建综合文档

**标准文档结构**：
- 执行摘要
- 核心亮点
- 发布者洞察
- 技术细节
- 延伸思考
- 背景信息
- 属性声明（"来自翡冷翠"）

### Step 4: 提交到 GitHub

```bash
cd ~/workspace/marovole-Superpowers

git add docs/{filename}.md
git commit -m "docs: add {主题} 完整整理 ({日期})"
git push origin main
```

### Step 5: 生成 Repost 推文

**导语结构**：

```
{作者/机构} 发布了/分享了/展示了 {核心事件}。

【1】{第一点标题}
{详细内容}

【2】{第二点标题}
{详细内容}

【3】{第三点标题}
{详细内容}

📄 完整文档：{github_link}
```

### Step 6: 邮件交付（完整实现）

**邮件配置：**
- 主收件人：**marovole@gmail.com**
- 抄送：**hueshadow989@gmail.com**（可选）
**邮件发送策略**（按优先级排序）：

| 方案 | 优先级 | 说明 | 前提条件 |
|-------|--------|------|----------|
| **Resend API** | 高 | 用户自有域名，送达率高 | 需配置 `RESEND_API_KEY` + `RESEND_FROM_EMAIL` |
| **Gmail SMTP** | 中 | Python SMTP，稳定可靠 | 需配置 `GMAIL_APP_PASSWORD` |
| **Apple Mail (osascript)** | 低 | 系统原生，无需额外配置 | Mail.app 已配置账户，macOS 专用 |

**首选方案：Resend API**

```bash
# 环境变量配置（~/.zshrc）
export RESEND_API_KEY='re_xxxxxxxxxxxxxxxxxxxxxxxxxxx'
export RESEND_FROM_EMAIL='yourname@yourdomain.com'
```

**Apple Mail 备用方案（macOS 现场验证可用）**

当 Resend/Gmail 均未配置时，使用 Apple Mail 作为可靠 fallback。这是 macOS 上最稳定的无配置方案。

```python
import subprocess
import os
from datetime import datetime

def send_notification_email_apple_mail(theme, source, item_count, word_count, 
                                        github_link, local_path,
                                        source_author="", repost_content=""):
    """
    通过 Apple Mail 发送完成通知邮件（macOS 专用）
    
    可靠模式：使用 osascript -e 多行链式调用，避免 .scpt 文件的编码问题。
    正文使用 ASCII 英文（避免 AppleScript 中文解析错误），附件为 Markdown 文件。
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # ASCII-only body (AppleScript safe)
    body = f"""Hi,

Your requested document has been curated and submitted to GitHub.

Document: {theme}
Source: {source}
GitHub: {github_link}
Local: {local_path}
Word count: ~{word_count} words

Key highlights:
- {repost_content[:200] if repost_content else "Document attached"}...

The full Markdown file is attached.

--
Curated on {timestamp}
""".strip()
    
    # Escape double quotes for AppleScript
    body_escaped = body.replace('\\', '\\\\').replace('"', '\\"')
    
    # Build osascript -e chain (most reliable on macOS)
    cmd = [
        'osascript',
        '-e', f'set mailContent to "{body_escaped}"',
        '-e', 'tell application "Mail"',
        '-e', f'    set newMessage to make new outgoing message with properties {{subject:"[X Curation] {theme} - {timestamp}", content:mailContent}}',
        '-e', '    tell newMessage',
        '-e', '        make new to recipient with properties {address:"marovole@gmail.com"}',
        '-e', f'        make new attachment with properties {{file name:"{local_path}"}} at after last paragraph',
        '-e', '        send',
        '-e', '    end tell',
        '-e', 'end tell'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    return result.returncode == 0 and result.stdout.strip().lower() == 'true'
```

**关键要点：**
- 使用 `osascript -e` 链式调用，**不要**写入 `.scpt` 文件（编码解析不可靠）
- 邮件正文使用纯 ASCII/英文，避免 AppleScript 引擎解析非 ASCII 字符出错
- 附件是 Markdown 文件，包含完整中文内容，用户阅读无障碍
- 返回 `true` 表示发送成功

**如需中文邮件正文**：加载 `macos-mail-utf8` skill，使用 Python 生成 UTF-8 `.scpt` 文件模式。

**Fallback（所有邮件方案失败时）：**

`send_message` 是原生工具，应作为独立工具调用，不是可导入的 Python 模块。必须同时传入 `action`、`target`、`message` 三个字段：

```json
{
  "action": "send",
  "target": "telegram",
  "message": "📄 「{theme}」文档整理完成\n\n📎 GitHub: {github_link}\n\n💡 {why_valuable[:100]}..."
}
```
---

## Skill 验证与更新记录

**2026-05-09 修复：**
1. **修复 `send_message` 目标平台：** 把 `target="origin"` 改为 `target="telegram"`，解决 "Unknown platform: origin" 错误
2. **修复代码模板错误：** 移除 `from hermes_tools import ...` 虚假导入，将 `terminal(...)` 改为 `subprocess.run`，因为 `terminal` 和 `send_message` 是本地工具而非 Python 模块导入
3. **添加技巧提示：** `send_message` 是原生工具，实际执行时应作为独立工具调用，而非包裹在 Python 函数内

**2026-05-09 重命名：**
- 把技能名从 `x2doc-repost` 简化为 `x2doc`
- 目录、SKILL.md 内所有自引用均已同步更新
- 触发指令：`https://x.com/{user}/status/{id} x2doc`

**2026-05-07 验证与修复：**

1. **邮件发送方案确认**：
   - ClawEmail (`mail-cli`) → 仅用于**接收邮件**（Newsletter 监控、确认邮件检查）
   - 发送邮件 → 使用 `email-with-attachment` 技能（Python SMTP，需 `GMAIL_APP_PASSWORD`）

2. **修复内容**：
   - 原技能中 Step 6 为占位符代码（"implementation pending"）
   - 从 `link2doc` 技能提取完整实现，整合充实版邮件模板
   - 添加 `send_notification_email()` 完整函数（含参数文档、Fallback 处理）

3. **充实版邮件模板特性**：
   - 文档地址（GitHub + 本地）
   - 文档信息（来源、作者、项目数、字数、时间）
   - 核心价值主张（转发内容摘要）
   - 精选亮点（前5项速查）
   - 转发建议
   - 速用场景速查
   - 署名「来自翡冷翠」

4. **Fallback 机制**：
   - 检测 `GMAIL_APP_PASSWORD` 未配置时，自动通过 Telegram 通知
   - 避免流程阻塞，确保用户收到完成提醒

---

## 工具使用陷阱（Pitfalls）

### `send_message` 目标平台值
- ❌ 错误：省略 `target` 或 `action` → 会报 "Both 'target' and 'message' are required when action='send'"
- ❌ 错误：`target="origin"` → 会报 "Unknown platform: origin"
- ✅ 正确：`{"action": "send", "target": "telegram", "message": "..."}` → 发送到 Telegram 主频道

### 工具 vs Python 函数
`terminal`、`send_message`、`web_search` 是 Hermes Agent 的原生工具（native tools），**不是可导入的 Python 模块**。在技能中写代码模板时：
- 如需在 Python 脚本中执行命令，用 `subprocess.run([...])`
- 如需发送消息，应作为独立的工具调用，而非包裹在 def 内部

### 邮件发送环境变量检查
执行前先检查环境变量，未配置时直接 Telegram fallback，避免流程阻塞：
```bash
echo "GMAIL_APP_PASSWORD: ${GMAIL_APP_PASSWORD:-not set}"
echo "RESEND_API_KEY: ${RESEND_API_KEY:-not set}"
```

---

## 纯转发内容输出规范（关键！）

**当用户要求"转发的内容"或"单独发可直接转发内容"时：**

### 必须遵守的规则：
1. **不包含任何额外标记** —— 不要加 `📰 可直接复制发布的转发推文:`、分割线、标题等
2. **不要加完整文档链接** —— 除非用户明确要求
3. **纯文本输出** —— 只有转发内容本身，用户可以直接选中整段复制
4. **不要加任何解释性文字** —— 如"以上是转发内容"等

### 正确输出示例：
```
Anthropic 员工 Thariq 分享了一篇关于 Claude Code 使用 HTML 替代 Markdown 的深度文章。

【为什么 Markdown 不够用了】
Markdown 在简单文档中表现良好，但随着 AI Agent 复杂度提升...

【HTML 能做什么 Markdown 做不到的】
HTML 可以表达几乎任何信息类型...

【实践建议】
如果你也在使用 Claude Code 类的 AI Agent 工具...
```

### 错误输出示例（避免）：
```
📰 可直接复制发布的转发推文:
============================
Anthropic 员工 Thariq...
============================
```

---

## 用户指令响应模式

| 用户指令 | 响应方式 |
|---------|---------|
| `x2doc` | 完整报告（文档+转发+邮件状态） |
| `转发的内容给我` | 仅转发内容，无任何额外标记 |
| `单独发可直接转发内容` | 仅转发内容，无任何额外标记 |
| `不要完整文档这个部分` | 转发内容中移除 GitHub 链接 |
| 手机操作/只能复制整个消息 | 确认纯文本输出，无格式标记 |

---
## Telegram 输出模板

```
📄 文档整理完成

**文档标题**

GitHub: {github_url}
本地: {local_path}

文档概要:
- 来源: {author} (@{username})
- 内容: {brief}
- 文档大小: 约 {word_count} 字

---

📰 可直接复制发布的转发推文:

{作者/机构} 发布了...

【1】...
...

📄 完整文档：{github_link}

---

📧 邮件发送: {状态}
```

---

## 质量检查清单

### 主流程提交前确认：
- [ ] 文档已正确提交到 GitHub
- [ ] 文档末尾署名是"来自翡冷翠"
- [ ] Repost 推文包含 3-4 个解读点
- [ ] 每个解读点有明确的 heading
- [ ] 包含完整文档链接（如需要）
- [ ] 没有 AI/Agent 署名混入推文
- [ ] 语言流畅，符合中文表达习惯
- [ ] **邮件已发送至 marovole@gmail.com**
- [ ] 邮件包含文档附件

### 纯转发内容输出确认（当用户要求"转发的内容"时）：
- [ ] 输出不包含 `📰 可直接复制发布的转发推文:` 等标题
- [ ] 输出不包含分割线 `===` 或 `---`
- [ ] 输出不包含 `📄 完整文档：` 链接（除非用户明确要求）
- [ ] 输出为纯文本，用户可以直接选中整段复制
- [ ] 输出末尾没有"以上是转发内容"等解释性文字
