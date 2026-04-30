# 闲鱼 AI 赚钱工具集 - 完整整理

> 来源：https://x.com/WY_mask/status/2048074404870189284
> 整理时间：2026-04-26
> 来自翡冷翠

---

## 简介

本合集整理了 4 个与闲鱼平台相关的 AI 自动化工具，涵盖商品监控、智能客服、多账号管理和 AI 副业赚钱思路。这些工具主要面向希望在闲鱼平台进行系统化运营或寻找 AI 副业机会的用户。

---

## 内容清单总览

| 序号 | 项目名称 | 作者/组织 | 类型 | 核心功能 | Stars |
|------|----------|-----------|------|----------|-------|
| 1 | ai-goofish-monitor | Usagi-org | 监控工具 | 闲鱼商品实时监控、AI 智能分析 | 11.1k |
| 2 | xianyu-auto-reply-fix | GuDong2003 | 管理系统 | 多账号管理、自动回复、自动发货 | 待统计 |
| 3 | XianyuAutoAgent | shaxiu | 客服机器人 | 7×24 小时 AI 自动客服、智能议价 | 待统计 |
| 4 | ai-money-maker-handbook | XiaomingX | 副业指南 | 程序员 AI 副业赚钱思路合集 (425 章) | 待统计 |

---

## 详细内容

### 1. ai-goofish-monitor - 闲鱼智能监控工具

**来源**：[@WY_mask](https://x.com/WY_mask) / GitHub: [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor)

**类型**：监控工具 / 浏览器自动化

**Stars**：11.1k

#### 核心功能
基于 Playwright + AI 实现的闲鱼多任务实时/定时监控与智能分析系统，配备功能完善的后台管理 UI。帮助用户从闲鱼海量商品中快速找到心仪产品，捡漏秒拍必备。

**主要特性：**
- 🔍 **实时监控/定时监控** - 支持多任务并发监控闲鱼商品
- 🤖 **AI 智能分析** - 多模态 AI 分析商品性价比和真实度
- 🔔 **多渠道通知** - 支持 ntfy、Bark、企业微信、Telegram、Webhook 推送
- 🖥️ **Web 管理后台** - FastAPI 后端 + Vue 3 前端，支持任务 CRUD
- 📊 **数据分析** - 商品数据自动存储和分析

#### 技术架构

```
API层 (src/api/routes/)
    ↓
服务层 (src/services/)
    ↓
领域层 (src/domain/)
    ↓
基础设施层 (src/infrastructure/)
```

**核心技术栈：**
- 后端：FastAPI + Python
- 前端：Vue 3 + Vite + shadcn-vue + Tailwind CSS
- 爬虫：Playwright
- 调度：APScheduler
- AI：支持多模态模型（需支持图片上传）

#### 关键入口
- `src/app.py` - FastAPI 应用主入口
- `spider_v2.py` - 爬虫 CLI 入口
- `src/scraper.py` - Playwright 爬虫核心逻辑

#### 部署方式

**Docker 部署（推荐）：**
```bash
git clone https://github.com/Usagi-org/ai-goofish-monitor.git
cd ai-goofish-monitor
docker compose up --build -d
```

**本地开发：**
```bash
# 后端
python -m src.app
# 或
uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload

# 前端
cd web-ui && npm install && npm run dev

# 一键启动
bash start.sh
```

#### 爬虫命令
```bash
python spider_v2.py                          # 运行所有启用任务
python spider_v2.py --task-name "MacBook"    # 运行指定任务
python spider_v2.py --debug-limit 3          # 调试模式，限制商品数
python spider_v2.py --config custom.json     # 自定义配置文件
```

#### 配置说明
**环境变量 (`.env`)：**
- AI 模型：`OPENAI_API_KEY`, `OPENAI_BASE_URL`, `OPENAI_MODEL_NAME`
- 通知：`NTFY_TOPIC_URL`, `BARK_URL`, `WX_BOT_URL`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
- 爬虫：`RUN_HEADLESS`, `LOGIN_IS_EDGE`
- Web 认证：`WEB_USERNAME`, `WEB_PASSWORD`
- 端口：`SERVER_PORT`

**任务配置 (`config.json`)：** 定义监控任务（关键词、价格范围、cron 表达式、AI prompt 文件等）

#### 数据流
1. Web UI / config.json 创建任务
2. SchedulerService 按 cron 触发或手动启动
3. ProcessService 启动 spider_v2.py 子进程
4. scraper.py 使用 Playwright 抓取商品
5. AIAnalysisService 调用多模态模型分析
6. NotificationService 推送符合条件的商品
7. 结果存储：`jsonl/`（数据）、`images/`（图片）、`logs/`（日志）

#### 注意事项
- AI 模型必须支持图片上传（多模态）
- Docker 部署需通过 Web UI 手动更新登录状态（`state.json`）
- 遇到滑动验证码时设置 `RUN_HEADLESS=false` 手动处理
- 生产环境务必修改默认 Web 认证密码

---

### 2. xianyu-auto-reply-fix - 闲鱼多账号智能管理系统

**来源**：[@WY_mask](https://x.com/WY_mask) / GitHub: [GuDong2003/xianyu-auto-reply-fix](https://github.com/GuDong2003/xianyu-auto-reply-fix)

**类型**：管理系统 / 自动化工具

#### 核心功能
一个功能完整的闲鱼管理系统，采用现代化的技术架构，支持多用户、多账号管理，具备智能回复、自动发货、自动确认发货、商品管理等企业级功能。

**⚠️ 重要提示：本项目仅供学习研究使用，严禁商业用途！**

#### 技术架构

**核心技术栈：**
- **后端框架**: FastAPI + Uvicorn + Python 3.11+ 异步编程
- **数据库**: SQLite 3 + 多用户数据隔离 + 自动迁移
- **前端**: Bootstrap 5 + Vanilla JavaScript + Chart.js + 响应式设计
- **通信协议**: WebSocket + SSE + RESTful API + 实时通信
- **自动化能力**: Playwright + DrissionPage + 浏览器自动化
- **部署方式**: Docker + Docker Compose + Nginx（可选）+ 一键部署
- **日志系统**: Loguru + 文件轮转 + 实时收集
- **安全认证**: Bearer Token + 图形验证码 + 邮箱验证 + 权限控制

**系统架构特点：**
- **模块化架构**: 按账号、订单、发货、通知、日志等模块拆分
- **异步处理**: 基于 asyncio 的高性能异步处理
- **多用户隔离**: 完整的数据隔离和权限控制
- **容器化部署**: Docker 容器化部署，支持一键启动
- **实时监控**: WebSocket + SSE 实时通信和状态监控
- **稳定性保障**: 自动重连、异常恢复、自动迁移、日志轮转

#### 核心特性

**🔐 多用户系统**
- 用户注册登录 - 支持邮箱验证码注册、用户名/邮箱登录
- 数据完全隔离 - 每个用户的数据独立存储
- 权限管理 - Bearer Token 认证
- 安全保护 - 防暴力破解、会话管理

**📱 多账号管理**
- 每个用户可管理多个闲鱼账号
- 每个账号独立启用、停用和刷新
- 一键批量擦亮在售商品
- 定时自动擦亮（支持时段和随机延迟配置）

**🤖 智能回复系统**
- 关键词匹配 - 通用关键词和商品专属关键词
- 指定商品回复 - 为特定商品设置专门回复
- 批量导入导出 - Excel 格式关键词批量操作
- AI 智能回复 - 支持上下文理解和多种模型接口
- 图片关键词 - 支持图片关键词和自动发送
- 优先级策略: 指定商品 > 商品专用关键词 > 通用关键词 > 默认回复 > AI回复

**🚚 自动发货功能**
- 智能匹配 - 基于商品信息自动匹配发货规则
- 多规格支持 - 同一商品不同规格自动匹配
- 延时发货 - 支持设置发货延时时间
- 多种触发 - 付款消息、小刀卡片触发
- 多种发货方式 - 文字、批量数据、API、图片

**🛍️ 商品管理**
- 自动收集商品信息
- 多规格商品配置
- 智能去重

**📊 系统监控**
- 实时日志查看
- 安全统计（登录封禁和锁定）
- 健康检查
- 用户、账号、卡券等数据统计

#### 快速开始

**方式一：使用部署脚本（推荐）⭐**

Linux / macOS:
```bash
git clone https://github.com/GuDong2003/xianyu-auto-reply-fix.git
cd xianyu-auto-reply-fix
chmod +x docker-deploy.sh
./docker-deploy.sh
```

Windows:
```bash
git clone https://github.com/GuDong2003/xianyu-auto-reply-fix.git
cd xianyu-auto-reply-fix
docker-deploy.bat
```

默认访问地址：
- `docker-compose.yml`: http://localhost:9000
- `docker-compose-cn.yml`: http://localhost:8000

**方式二：手动 Docker Compose**
```bash
git clone https://github.com/GuDong2003/xianyu-auto-reply-fix.git
cd xianyu-auto-reply-fix
docker compose up -d --build
```

**方式三：本地运行**
```bash
git clone https://github.com/GuDong2003/xianyu-auto-reply-fix.git
cd xianyu-auto-reply-fix
python -m venv venv
source venv/bin/activate  # Linux/macOS
pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
python Start.py
```
访问地址：http://localhost:8090

#### 环境要求
- **Python**: 3.11+
- **Node.js**: 16+（用于 PyExecJS）
- **系统**: Windows / Linux / macOS
- **架构**: x86_64 (amd64) / ARM64 (aarch64)
- **Docker**: 20.10+（如使用 Docker 部署）
- **资源建议**: 2GB+ 内存，10GB+ 存储空间

#### 默认账号
- 用户名：`admin`
- 密码：`admin123`

⚠️ **安全提示**：首次登录后请立即修改默认密码！

#### 系统架构

```
┌─────────────────────────────────────────┐
│       Web 界面 (FastAPI + Static)        │
│          用户管理 + 功能界面               │
└───────────────────┬─────────────────────┘
                    │
┌───────────────────▼─────────────────────┐
│             CookieManager               │
│           多账号任务与状态管理             │
└───────────────────┬─────────────────────┘
                    │
┌───────────────────▼─────────────────────┐
│          XianyuLive (多实例)             │
│        WebSocket 连接 + 消息处理          │
└──────────────┬──────────────┬───────────┘
               │              │
┌──────────────▼───────┐ ┌────▼──────────────┐
│    AIReplyEngine     │ │ FileLogCollector  │
│     AI 回复与上下文    │ │   实时日志与统计    │
└──────────────┬───────┘ └────┬──────────────┘
               │              │
┌──────────────▼──────────────▼───────────┐
│              SQLite 数据库               │
│      用户数据 + 商品信息 + 配置数据         │
└─────────────────────────────────────────┘
```

---

### 3. XianyuAutoAgent - 闲鱼 AI 智能客服机器人

**来源**：[@WY_mask](https://x.com/WY_mask) / GitHub: [shaxiu/XianyuAutoAgent](https://github.com/shaxiu/XianyuAutoAgent)

**类型**：客服机器人 / AI Agent

#### 核心功能
专为闲鱼平台打造的 AI 值守解决方案，实现闲鱼平台 7×24 小时自动化值守，支持多专家协同决策、智能议价和上下文感知对话。

#### 核心特性

**智能对话引擎**

| 功能模块 | 技术实现 | 关键特性 |
|----------|----------|----------|
| 上下文感知 | 会话历史存储 | 轻量级对话记忆管理，完整对话历史作为 LLM 上下文输入 |
| 专家路由 | LLM prompt + 规则路由 | 基于提示工程的意图识别 → 专家 Agent 动态分发 |

**业务功能矩阵**

| 模块 | 已实现 | 规划中 |
|------|--------|--------|
| 核心引擎 | ✅ LLM 自动回复 ✅ 上下文管理 | 🔄 情感分析增强 |
| 议价系统 | ✅ 阶梯降价策略 | 🔄 市场比价功能 |
| 技术支持 | ✅ 网络搜索整合 | 🔄 RAG 知识库增强 |
| 运维监控 | ✅ 基础日志 | 🔄 钉钉集成 🔄 Web 管理界面 |

#### 快速开始

**保姆级教学文档**：[飞书文档](https://my.feishu.cn/wiki/JtkBwkI9GiokZikVdyNceEfZncE)

**环境要求：**
- Python 3.8+

**安装步骤：**

1. 克隆仓库
```bash
git clone https://github.com/shaxiu/XianyuAutoAgent.git
cd XianyuAutoAgent
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
创建 `.env` 文件（或重命名 `.env.example`）：
```bash
# 必配配置
API_KEY=***
COOKIES_STR=填写网页端获取的cookie
MODEL_BASE_URL=模型地址
MODEL_NAME=模型名称

# 可选配置
TOGGLE_KEYWORDS=接管模式切换关键词，默认为句号
SIMULATE_HUMAN_TYPING=True/False  # 模拟人工回复延迟
```

注意：
- 默认使用通义千问模型
- COOKIES_STR 需在闲鱼网页端获取（F12 → Network → Fetch/XHR → 查看 cookies）

4. 创建提示词文件
将 `prompts/` 目录下模板文件中的 `_example` 去掉，或自定义：
- `classify_prompt.txt` - 意图分类提示词
- `price_prompt.txt` - 价格专家提示词
- `tech_prompt.txt` - 技术专家提示词
- `default_prompt.txt` - 默认回复提示词

**使用方法：**
```bash
python main.py
```

#### 自定义提示词
可以通过编辑 `prompts` 目录下的文件来自定义各个专家的提示词，实现不同场景的个性化回复策略。

#### 联系方式
- **项目交流**：见 GitHub 仓库 README
- **作者邮箱**：[coderxiu@qq.com](mailto:coderxiu@qq.com)
- **作者微信**：coderxiu

⚠️ **注意**：本项目仅供学习与交流，如有侵权联系作者删除。

---

### 4. ai-money-maker-handbook - AI 副业赚钱宝典

**来源**：[@WY_mask](https://x.com/WY_mask) / GitHub: [XiaomingX/ai-money-maker-handbook](https://github.com/XiaomingX/ai-money-maker-handbook)

**类型**：知识库 / 副业指南

#### 核心内容
AI 副业赚钱大集合，教你如何利用 AI 做副业项目，赚取额外收益。这是一个面向程序员和早期创业者的中文内容仓库，专注于 AI 驱动的副业和创业指导。

#### 内容结构

**1. 程序员的副业赚钱宝典** (425 章，ch0001.md - ch0425.md)
- 程序员技术变现的实用指南
- 聚焦可执行的商业策略、财务计算和中国市场特点
- 涵盖：定价、成本、利润率、回本周期、CAC、LTV、ROI 等

**2. 创业者早期的烦恼树洞** (39 章，ch0001.md - ch0039.md)
- 创业基础知识问答
- 主题包括：PMF、融资轮次、股权、合规、指标（MAU、ARR、LTV/CAC）
- Q&A 形式，用户问题 + 详细回答

#### 内容特色

**写作哲学：**
- **财务具体化** - 包含具体数字：定价（¥）、成本、利润率、回本周期
- **中国市场聚焦** - 参考平台：微信、抖音、快手、小红书、闲鱼、淘宝、1688、知识星球
- **可执行的 SOP 格式** - 步骤化指令，避免模糊建议
- **商业指标** - 定价、投入成本、回本周期、利润率、北极星指标、KPI、OKR
- **合规导向** - 仅合法副业，标注灰色地带活动

**Agent 配置：**
- `.prompt/agent.md` - "Side Hustle Architect" 角色定义
- `.prompt/skill.md` - 五个内容生成技能：
  1. `generate_business_ledger` - 财务计算
  2. `define_mvp_strategy` - 最小可行产品指导
  3. `china_local_traffic_hacking` - 中国平台营销
  4. `risk_assessment` - 风险评估
  5. `case_study_simulation` - 程序员成功案例

#### 相关资源
- [跨境出海技术栈](https://github.com/XiaomingX/cross-border-tech-stack)
- [AI 搞钱原则手册](https://github.com/XiaomingX/ai-money-principles)
- [构建你自己的 X](https://github.com/XiaomingX/build-your-own-x-cn)
- [1000 个中国独立开发者项目](https://github.com/XiaomingX/1000-chinese-indie-projects)

#### 内容更新
- GitHub Actions 每天 23:30 UTC 自动更新
- 通过 GitHub issues 提交 AI 赚钱案例
- 分享文章、网站、博客、推文关于 AI 变现

---

## 资源汇总

### 所有 GitHub 仓库

| 项目 | 链接 | 简介 |
|------|------|------|
| ai-goofish-monitor | https://github.com/Usagi-org/ai-goofish-monitor | 闲鱼智能监控，11.1k stars |
| xianyu-auto-reply-fix | https://github.com/GuDong2003/xianyu-auto-reply-fix | 多账号管理系统 |
| XianyuAutoAgent | https://github.com/shaxiu/XianyuAutoAgent | AI 智能客服机器人 |
| ai-money-maker-handbook | https://github.com/XiaomingX/ai-money-maker-handbook | 副业赚钱指南 (425 章) |

### 值得关注的人/账号

- [@WY_mask](https://x.com/WY_mask) - 工具聚合分享者
- [@GuDong2003](https://github.com/GuDong2003) - 闲鱼管理系统开发者
- [@shaxiu](https://github.com/shaxiu) - XianyuAutoAgent 开发者，寻求 AI 产品经理机会
- [@cv-cat](https://github.com/cv-cat) - 提供技术支持，寻求研发工程师机会
- [@XiaomingX](https://github.com/XiaomingX) - AI 副业指南作者

### 衍生相关项目

| 项目 | 说明 |
|------|------|
| [XianYuApis](https://github.com/cv-cat/XianYuApis) | 闲鱼 API 接口技术参考 |
| [myfish](https://github.com/Kaguya233qwq/myfish) | 扫码登录实现参考 |
| [xianyu-auto-reply](https://github.com/zhinianboke-new/xianyu-auto-reply) | 原始项目基础 |

---

## 适用场景与建议

### 适用人群
1. **闲鱼卖家** - 希望自动化运营、提升效率的个体卖家或小型团队
2. **二手交易者** - 需要实时监控特定商品、捡漏好价的买家
3. **技术学习者** - 想学习 Playwright、FastAPI、浏览器自动化的开发者
4. **副业探索者** - 寻找 AI 驱动的副业机会

### 建议学习/使用路径

**路径一：买家捡漏**
```
ai-goofish-monitor → 配置监控任务 → 设置 AI 分析规则 → 接收通知推送
```

**路径二：卖家自动化**
```
xianyu-auto-reply-fix → 部署系统 → 添加账号 → 配置自动回复/发货规则
```

**路径三：客服智能化**
```
XianyuAutoAgent → 配置环境 → 自定义提示词 → 7×24 值守
```

**路径四：副业学习**
```
ai-money-maker-handbook → 阅读相关章节 → 学习中国平台运营策略 → 实践验证
```

---

## 技术栈总结

| 项目 | 后端 | 前端 | 自动化 | 数据库 | 部署 |
|------|------|------|--------|--------|------|
| ai-goofish-monitor | FastAPI + Python | Vue 3 + Vite | Playwright | JSONL/文件 | Docker |
| xianyu-auto-reply-fix | FastAPI + Python 3.11 | Bootstrap 5 | Playwright + DrissionPage | SQLite | Docker |
| XianyuAutoAgent | Python 3.8+ | - | 浏览器自动化 | 会话存储 | 本地运行 |
| ai-money-maker-handbook | - | - | - | - | GitHub Pages |

---

## 免责声明

⚠️ **重要提示：**

1. 以上工具仅供学习研究使用，请勿用于违法违规场景
2. 使用这些工具进行闲鱼自动化操作时，请遵守闲鱼平台规则
3. 部分项目明确声明禁止商业用途
4. 自动化工具可能存在账号风险，请谨慎使用
5. 因使用这些工具产生的任何风险和损失，由使用者自行承担

---

## 附录：快速参考

### 常用命令速查

**Docker 操作：**
```bash
# 启动服务
docker compose up -d --build

# 查看日志
docker compose logs -f

# 停止服务
docker compose down
```

**Git 克隆所有项目：**
```bash
mkdir xianyu-tools && cd xianyu-tools

git clone https://github.com/Usagi-org/ai-goofish-monitor.git
git clone https://github.com/GuDong2003/xianyu-auto-reply-fix.git
git clone https://github.com/shaxiu/XianyuAutoAgent.git
git clone https://github.com/XiaomingX/ai-money-maker-handbook.git
```

**Python 虚拟环境：**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

---

*来自翡冷翠*
