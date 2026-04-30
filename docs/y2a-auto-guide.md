# Y2A-Auto：YouTube 到 AcFun/B站 全自动搬运工具

> 来源：https://x.com/wsl8297/status/2046936828394303689
> 整理时间：2026-04-23
> 来自翡冷翠

---

## 简介

**Y2A-Auto** 是一款开源免费的搬运利器，一键将 YouTube 优质内容同步到 **AcFun** 和 **bilibili**。

它把整套搬运流程做成**全自动化**：
- ✅ 下载视频
- ✅ ASR 语音识别
- ✅ 字幕翻译
- ✅ 字幕质检
- ✅ 内容审核
- ✅ 自动投稿上传

配套 **Web 管理界面** 和 **浏览器插件**，管理、浏览都更顺手。

---

## 核心功能一览

| 功能阶段 | 具体能力 |
|----------|----------|
| **视频下载** | YouTube 视频自动下载，支持多种分辨率 |
| **语音识别** | ASR 自动生成字幕 |
| **字幕翻译** | AI 翻译字幕（支持多语言） |
| **字幕质检** | 自动检查翻译质量 |
| **内容审核** | 自动审核内容合规性 |
| **自动上传** | 一键投稿到 AcFun / bilibili |
| **YouTube 监控** | 自动盯盘热门趋势和指定频道 |
| **Web 管理** | 内置管理后台，可视化操作 |
| **浏览器插件** | 配套插件，浏览更顺手 |

---

## 全自动流程图

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  YouTube    │ →  │   视频      │ →  │   ASR       │ →  │   AI        │
│  视频链接   │    │   下载      │    │   字幕生成   │    │   翻译      │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                              ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  AcFun/     │ ←  │   自动      │ ←  │   内容      │ ←  │   字幕      │
│  B站发布    │    │   上传      │    │   审核      │    │   质检      │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

---

## 部署方式

### Docker 一键部署（推荐）

```bash
# 1. 克隆项目
git clone https://github.com/fqscfqj/Y2A-Auto.git
cd Y2A-Auto

# 2. 启动 Docker 容器
docker-compose up -d

# 3. 浏览器打开管理界面
open http://localhost:5000
```

**启动后**，在 Web 界面填好 LLM API Key 就能直接使用。

---

### 手动部署

```bash
# 1. 克隆项目
git clone https://github.com/fqscfqj/Y2A-Auto.git
cd Y2A-Auto

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入 YouTube API Key、LLM API Key 等

# 4. 启动服务
python app.py

# 5. 浏览器打开
open http://localhost:5000
```

---

## 配置说明

### 必需配置项

| 配置项 | 说明 | 获取方式 |
|--------|------|----------|
| `YOUTUBE_API_KEY` | YouTube Data API 密钥 | Google Cloud Console |
| `OPENAI_API_KEY` | OpenAI API 密钥（用于翻译） | OpenAI 官网 |
| `ACFUN_SESS` | AcFun 登录凭证 | 浏览器 Cookie |
| `BILIBILI_SESS` | B站登录凭证 | 浏览器 Cookie |

### 可选配置项

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `TARGET_PLATFORM` | 目标平台（acfun/bilibili/both） | both |
| `TRANSLATE_LANG` | 翻译目标语言 | zh-CN |
| `VIDEO_QUALITY` | 下载视频质量 | 1080p |
| `AUTO_UPLOAD` | 是否自动上传 | true |
| `CONTENT_REVIEW` | 是否启用内容审核 | true |

---

## YouTube 监控功能

Y2A-Auto 支持 **自动盯盘** YouTube 内容：

### 监控类型

| 类型 | 说明 |
|------|------|
| **热门趋势** | 自动监控 YouTube 热门视频 |
| **指定频道** | 监控特定 UP 主的新发布 |
| **关键词订阅** | 按关键词自动发现新内容 |

### 监控设置

在 Web 管理界面中：
1. 进入「监控管理」页面
2. 添加监控任务（频道/关键词/趋势）
3. 设置检查频率（每小时/每天）
4. 触发条件后自动执行搬运流程

---

## Web 管理界面

### 功能模块

| 模块 | 功能 |
|------|------|
| **仪表盘** | 查看搬运统计、成功率、队列状态 |
| **任务管理** | 查看/暂停/重试搬运任务 |
| **监控管理** | 配置 YouTube 监控规则 |
| **视频库** | 管理已下载的视频和字幕 |
| **设置中心** | 配置 API Key、平台账号等 |
| **日志查看** | 查看详细运行日志 |

### 界面预览

内置现代化 Dashboard，支持：
- 实时任务进度
- 成功/失败统计图表
- 队列状态可视化
- 拖拽式任务管理

---

## Telegram Bot（可选）

除了 Web 界面，还提供 **Telegram 转发机器人**：

- **试用版**：[@Y2AAuto_bot](https://t.me/Y2AAuto_bot)
- **自部署版**：[Y2A-Auto-tgbot](https://github.com/fqscfqj/Y2A-Auto-tgbot)

**功能**：
- 在 Telegram 中直接发送 YouTube 链接
- 机器人自动触发搬运流程
- 完成后推送通知

---

## 浏览器插件

配套浏览器插件，提供更便捷的操作体验：

- 在 YouTube 页面直接点击「搬运到 AcFun/B站」
- 实时显示搬运进度
- 一键查看历史记录

---

## 技术架构

### 技术栈

| 层级 | 技术 |
|------|------|
| **后端** | Python Flask |
| **前端** | HTML + JavaScript + Bootstrap |
| **数据库** | SQLite（默认）/ PostgreSQL |
| **任务队列** | Redis + Celery |
| **容器化** | Docker + Docker Compose |

### 核心模块

```
Y2A-Auto/
├── modules/          # 核心功能模块
│   ├── downloader/   # 视频下载
│   ├── asr/          # 语音识别
│   ├── translator/   # AI 翻译
│   ├── reviewer/     # 内容审核
│   └── uploader/     # 上传模块
├── static/           # 前端静态资源
├── templates/        # HTML 模板
├── tests/            # 单元测试
└── docker-compose.yml # Docker 配置
```

---

## 资源汇总

### 项目链接

| 资源 | 链接 | 说明 |
|------|------|------|
| **主项目** | https://github.com/fqscfqj/Y2A-Auto | GitHub 仓库 |
| **Telegram Bot** | https://t.me/Y2AAuto_bot | 试用版机器人 |
| **Bot 源码** | https://github.com/fqscfqj/Y2A-Auto-tgbot | 自部署版本 |

### 社区资源

- **作者**：fqscfqj
- **推荐人 X**：@wsl8297（Joruno）
- **GitHub Stars**：251+
- **Forks**：35+

---

## 快速启动清单

```bash
# 1. 克隆项目
git clone https://github.com/fqscfqj/Y2A-Auto.git
cd Y2A-Auto

# 2. 配置环境
cp .env.example .env
vim .env  # 填入 API Keys

# 3. Docker 一键启动
docker-compose up -d

# 4. 访问 Web 界面
open http://localhost:5000

# 5. 配置监控任务（可选）
# 在 Web 界面「监控管理」中添加 YouTube 频道
```

---

## 常见问题

### Q: 需要什么 API Key？
**A**: 至少需要：
- YouTube Data API Key（Google Cloud）
- OpenAI API Key 或其他 LLM API Key

### Q: 支持哪些目标平台？
**A**: 目前支持 AcFun 和 bilibili，可配置同时发布到两个平台。

### Q: 翻译质量如何？
**A**: 使用 AI 大模型翻译，支持 GPT-4/Claude 等，质量接近人工水平。支持翻译后人工校对。

### Q: 会被封号吗？
**A**: 工具内置了频率控制和随机延迟，但请遵守平台规则，合理控制搬运频率。

---

## 适用场景

| 场景 | 价值 |
|------|------|
| **优质内容引进** | 将海外优质科普/教育内容引入国内平台 |
| **多平台分发** | 海外创作者将内容同步到国内平台 |
| **内容运营** | 自动搬运特定领域的热门内容 |
| **翻译组工作** | 大幅提升字幕翻译和上传效率 |

---

## 免责声明

本工具仅供学习和个人使用，请遵守以下原则：
1. 尊重原创内容版权
2. 搬运内容需符合目标平台社区规范
3. 不搬运受版权保护的商业内容
4. 合理使用，避免对源平台和目标平台造成负担

---

*来自翡冷翠*
