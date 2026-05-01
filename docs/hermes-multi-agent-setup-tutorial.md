# Hermes 多 Agent 小队搭建完全指南

> 来源：[X/Twitter @VinceZcrikl](https://x.com/VinceZcrikl/status/2045854168825336151)
> 作者：文森.Z (@VinceZcrikl) - Fortune 500 AI Engineer | 独立开发 | 出海
> 整理时间：2026-05-01
> 来自翡冷翠

---

## 简介

本文为 Hermes Agent 用户详细讲解如何从 0 开始搭建自己的多 Agent 小队。作者将其 Hermes 日常使用划分为四个角色：
- **知识管家**：日常消息、提醒、轻任务、信息整理
- **编程 Coder**：专职写代码
- **玄学军师**：起局看卦、命理测算
- **深夜老司机**：深夜陪聊、成人话题

内容涵盖 Profile 机制原理、安装配置、调教过程，一次讲透。

---

## 目录

- [第一章：Hermes 安装与配置（10分钟搞定）](#第一章hermes-安装与配置10分钟搞定)
- [第二章：为什么需要多个 Agent](#第二章为什么需要多个-agent)
- [第三章：Profile 机制原理](#第三章profile-机制原理)
- [第四章：实战！从零搭建 AI 小队](#第四章实战从零搭建-ai-小队)
- [第五章：四种角色人设配置参考](#第五章四种角色人设配置参考)

---

## 第一章：Hermes 安装与配置（10分钟搞定）

### 一键安装

Hermes 官方提供了一键安装脚本，Linux、macOS、WSL2 通用：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

这一行会帮你把所有依赖——Python 3.11、Node.js、ripgrep、ffmpeg——全部装好。

> **Windows 用户注意**：Hermes 不支持原生 Windows，需要先装 WSL2，然后在 WSL2 里跑上面的命令。

### 交互式配置向导

安装完成后，运行以下命令进入配置向导：

```bash
hermes setup
```

向导会逐步引导你完成：
- 选 LLM 提供商（OpenRouter、Anthropic、OpenAI、Ollama 本地等）
- 填 API key（自动写入 `~/.hermes/.env`，不会明文暴露在配置文件里）
- 选终端 backend（一般选 local 就行）
- 配 agent 能力参数（最大迭代次数、工具显示等，后面随时能改）

对于新手来说，最省心的路径是选 **OpenRouter** 或 **Nous Portal**（Hermes 官方集成）。

### Nous Portal 介绍

Nous Portal 是 Hermes 官方下场做的中转站，特点是：
- 一次订阅包含 300+ 主流模型
- 第三方付费工具（网页抓取、生图、语音等）
- 无需 juggling 多个 API key

### 配置文件位置

配好后，所有设置会落地到两个文件：
- `~/.hermes/config.yaml`：模型、终端、记忆等行为配置
- `~/.hermes/.env`：API key、token 等密钥

### Telegram Bot 配置（可选）

如果想通过 Telegram 与 Agent 交互：

1. 在 Telegram 中找到 `@BotFather`，输入 `/newbot`，根据引导命名，生成 token
2. 找到 `@userinfobot`，输入 `/start`，复制自己的 user ID
3. 将 token 填入配置向导

### 常用命令

```bash
hermes doctor   # 自动检测环境，告诉你哪里有问题
hermes status   # 查看当前配置状态

# 后续微调配置
hermes config set model anthropic/claude-sonnet-4   # 换模型
hermes config set OPENROUTER_API_KEY sk-or-v1-新key  # 换 key
hermes config edit                                    # 直接编辑配置文件
```

终端运行 `hermes` 和 Telegram bot，看到欢迎画面即表示第一个 agent 上线成功。

---

## 第二章：为什么需要多个 Agent

### 单一 Agent 的核心矛盾

Hermes 跑起来后，你开始什么都找它。但核心矛盾只有一个——**一套配置服务不了所有需求**。

你希望：
- 日常任务用省钱省 token 的轻量模型
- 写代码的时候接 Claude 或 Codex 拉满质量
- 还想用 Grok 聊点不正经话题

但单一 Agent 只有一套 `config.yaml`、一个 `.env`、一份 `SOUL.md`。你得在会话里手动切模型，而且单 agent 人设分裂、记忆混乱，很快你自己先分裂了。

### 解决方案：术业有专攻

解决方案就是**拆**。每个角色给独立的 profile，独立的配置，独立的模型，独立的人设，独立的记忆空间。

---

## 第三章：Profile 机制原理

Hermes Profile 机制让多 Agent 做到真正的**目录空间隔离**。

每个 profile 是完全不同的 agent 本体：
- 独立的 `config.yaml`（模型、参数各自配）
- 独立的 `.env`（API key、token 各自隔离）
- 独立的 `SOUL.md`（人格完全不同）
- 独立的 gateway 进程（各跑各的，互不干扰）
- 独立的日志和 PID 文件

### 实际文件结构示例

```
~/.hermes/
  .env                     ← main profile 的 token
  config.yaml              ← main 的模型配置
  SOUL.md                  ← main 的人格定义
  profiles/
    coder/
      .env                 ← coder 专属 token
      config.yaml          ← 接 codex GPT5.4，代码质量拉满
      SOUL.md              ← 冷静、严谨、只聊代码
      gateway.pid
      logs/
    master/
      .env                 ← master 专属 token
      config.yaml          ← opus 4.7 效果最好
      SOUL.md              ← 诸葛亮人设，古风命理
      gateway.pid
      logs/
    olddriver/
      .env                 ← olddriver 专属 token
      config.yaml          ← 接 Grok
      SOUL.md              ← 深夜老司机人设
      gateway.pid
      logs/
```

每个 profile 有自己的完整配置副本，跑在自己物理级别隔离的 gateway 进程里。

---

## 第四章：实战！从零搭建 AI 小队

### 第一步：创建 Telegram Bots

每个 profile 必须对应一个独立的 Telegram bot。Hermes 有 token 锁机制，两个 profile 共用同一个 token 会直接报冲突。

打开 Telegram，找到 `@BotFather`，依次创建：

```
/newbot → main_hermes_bot   → 拿到 Token A
/newbot → coder_hermes_bot  → 拿到 Token B
/newbot → master_hermes_bot → 拿到 Token C
/newbot → od_hermes_bot     → 拿到 Token D
```

三个 bot，三个 token，一个都不能混。

### 第二步：创建 Profiles

Hermes 的 `--clone` 参数可以一键复制当前主 profile 的全部配置，省得从头配模型和 API key：

```bash
hermes profile create coder --clone
hermes profile create master --clone
hermes profile create olddriver --clone
```

独立 profile 就建好了。`--clone` 会把主 profile 的 `config.yaml`、`.env`、`SOUL.md` 全部复制过去。

### 第三步：配置各 Profile 的 Bot Token

每个 profile 必须指向自己的 bot token。

以 `olddriver` 为例：

```bash
olddriver setup
```

会进入配置引导，重复第一章中的过程，单独配置你想用的模型和 bot。记得 token 要正确对应 `olddriver` bot。

配置成功后能看到欢迎画面中 profile 指向了 `olddriver`，恭喜你的角色上线了。

### 验证 Token 配置

如果 bot 没反应，可以用以下命令检查 token 是否配置正确：

```bash
# 查看各 profile 的 token
grep '^TELEGRAM_BOT_TOKEN' ~/.hermes/.env
grep '^TELEGRAM_BOT_TOKEN' ~/.hermes/profiles/coder/.env
grep '^TELEGRAM_BOT_TOKEN' ~/.hermes/profiles/master/.env
grep '^TELEGRAM_BOT_TOKEN' ~/.hermes/profiles/olddriver/.env
```

不同 profile 对应输出不同的 token，就对了。

### 命令行修正配置

如果 token 配置错误，可以通过命令行快速修正：

**main profile（默认）：**
```bash
sed -i '/TELEGRAM_BOT_TOKEN/d' ~/.hermes/.env
echo 'TELEGRAM_BOT_TOKEN=你的TokenA' >> ~/.hermes/.env
```

**coder profile：**
```bash
sed -i '/TELEGRAM_BOT_TOKEN/d' ~/.hermes/profiles/coder/.env
echo 'TELEGRAM_BOT_TOKEN=你的TokenB' >> ~/.hermes/profiles/coder/.env
```

**master profile：**
```bash
sed -i '/TELEGRAM_BOT_TOKEN/d' ~/.hermes/profiles/master/.env
echo 'TELEGRAM_BOT_TOKEN=你的TokenC' >> ~/.hermes/profiles/master/.env
```

**olddriver profile：**
```bash
sed -i '/TELEGRAM_BOT_TOKEN/d' ~/.hermes/profiles/olddriver/.env
echo 'TELEGRAM_BOT_TOKEN=你的TokenD' >> ~/.hermes/profiles/olddriver/.env
```

> **macOS 用户注意**：`sed -i` 需要加空字符串参数，写成 `sed -i '' '/TELEGRAM_BOT_TOKEN/d'`。

### 第四步：启动各 Profile 的 Gateway

```bash
hermes gateway start      # main  → @main_hermes_bot
coder gateway start      # coder → @coder_hermes_bot
master gateway start      # master → @master_hermes_bot
olddriver gateway start   # olddriver → @olddriverhermes_bot
```

四个进程独立运行，互不干扰。打开 Telegram，四个 bot 都在线。

查看各自状态：

```bash
hermes gateway status
coder gateway status
master gateway status
olddriver gateway status
```

到这里，你的私人 AI 小队就搭好了。

---

## 第五章：四种角色人设配置参考

技术上跑通了，但每个 agent 到底该干什么、人设怎么写，才是多 Agent 方案真正好用的关键。

### 1. 知识管家（main）

**职责**：日常消息、提醒、轻任务、信息整理、调研、查资料。

**人设关键词**：口语化、反应快、什么都能聊、是你日常交互的主入口。

**特点**：这是你用得最多的 bot。随手问个问题、记个想法、设个提醒——都找它。SOUL.md 写得轻松一点，不用太正式，像一个靠谱的朋友。

**扩展功能**：可以配置 Obsidian 知识库集成，把文章链接丢给他自动解析存档。

### 2. 编程 Coder

**职责**：代码实现、debug、代码审查、技术方案讨论、git 工作流。

**特点**：把它当成手机上的 Codex 来用。你在地铁上突然想到一个实现思路，掏出手机发给 coder，它帮你写好、验证、把结果贴回来。

**SOUL.md 核心模板**：

```
你的人格是资深软件工程师，精通全栈开发，严格遵循软件工程范式，
敏捷开发流程，根据需求先做 plan，后实现，充分单元测试验证代码逻辑，
多步提交，每次提交新建 branch 发 pr review。
```

**GitHub 集成**：本地装好 git，告诉你的 coder，关联 GitHub 账号，他会引导你完成。

### 3. 玄学军师（master）

**职责**：传统命理测算、奇门遁甲、八字分析、日常择吉、运势参考。

**特点**：这个 agent 是四个里面最有"角色感"的。帮你看日常、事业、生活、情感吉凶。玄学是老祖宗的智慧积累，AI 也有出错的时候，不要一味盲从，凡事要有自己的判断。

**推荐技能**：安装 skill 固定知识库（包含精确起局算法、八字、奇门）。

**SOUL.md 模板**：

```
你是卧龙先生转世，精通天文地理、奇门遁甲、八字命理、梅花易数、风水之术。
起局看卦，结合八字和问题分析并详细解读卦象。
你用古人的语气语调说话，偶尔引用典故，任何结果都要从客观中立角度分析，
不要被问卦人的语气情绪带动，不避讳凶象，知无不言。
```

**模型选择**：可以试试 DeepSeek 或者 Qwen 系列，对古文语境和传统文化概念的理解会更自然。但作者目前用下来 Opus 和 Gemini Pro 解读卦象能力比较稳，推荐。

### 4. 深夜老司机（olddriver）

**职责**：深夜陪聊、成人话题、情感释放、男女通用，随自己喜好设定。

**人设关键词**：两性话题、成人小说写手、深夜情感导师、薄肌男大...

**特点**：这是你的隐藏 bot，只属于你自己的小秘密。

**模型选择**：接 **Grok**，因为 Grok 在成人话题上的自由度远超其他模型，不会动不动就"我是一个 AI，无法讨论此话题"。本地模型 qwen 也有非限制版，可自行在 Hugging Face 上查找试用。

**SOUL.md 设计要点**：

- **绿色版**："你是一个深夜伴侣。会说情话，写成人小说，色情但不露骨，大胆聊骚"
- **邪修版**：可设定高冷女神、薄肌男大等，具体怎么设看个人喜好发挥

---

## 结语

通过 Hermes 的 Profile 机制，你可以在同一台机器上搭建多角色 AI 团队。每个角色各司其职，互不干扰，真正做到"术业有专攻"。

关于命理军师、老司机 bot 还有其他角色养成，且听下回分解～

---

## 资源汇总

| 资源 | 链接 | 说明 |
|------|------|------|
| Hermes 官方 | https://github.com/NousResearch/hermes-agent | 官方仓库 |
| Nous Portal | 集成在 Hermes setup 中 | 官方中转站服务 |
| 安装脚本 | `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh \| bash` | 一键安装 |
| Telegram BotFather | @BotFather | 创建 bot |
| 作者 X 账号 | @VinceZcrikl | 文森.Z |

---

## 快速参考：常用命令速查表

| 命令 | 作用 |
|------|------|
| `hermes setup` | 启动配置向导 |
| `hermes doctor` | 环境诊断 |
| `hermes status` | 查看配置状态 |
| `hermes profile create <name> --clone` | 创建并克隆 profile |
| `<profile> setup` | 为指定 profile 配置 |
| `<profile> gateway start` | 启动指定 profile 的 gateway |
| `<profile> gateway status` | 查看 gateway 状态 |

---

*来自翡冷翠*
