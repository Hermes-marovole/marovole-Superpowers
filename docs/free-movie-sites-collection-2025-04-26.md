# 6个免费开源影视网站完整整理 —— 4K画质，零广告，一键部署

> **来源**：火山哥 (@huoshan007) X 帖子  
> **原始链接**：https://x.com/huoshan007/status/2047882942337454133  
> **整理时间**：2025-04-26  
> 来自翡冷翠

---

## 📺 简介

还在被会员费、广告弹窗、手机卡顿画质糊成渣折磨吗？剧荒、片源下架、1080P都像PPT？

这6大纯开源免费神站，零广告、零会员、资源拉满、画质封神！手机原生4K丝滑，躺床上刷大片直接变私人影院！🔥📽️

全部 GitHub 开源，一键部署到 Vercel/Docker/Cloudflare Pages，打造你的专属4K影院！全网最新电影、剧集、动漫、综艺一搜即有，更新飞快，HDR+杜比音效随便切，手机电脑平板电视全通吃！🚀

---

## 📋 项目总览

| 序号 | 项目名称 | 技术栈 | 核心特性 | 官方实例 |
|------|----------|--------|----------|----------|
| 1 | **LibreTV** | 纯前端 | 轻量聚合、多源4K、搜索秒开 | [libretv.is-an.org](https://libretv.is-an.org) |
| 2 | **LunaTV** | Next.js | 海量资源、收藏同步、播放记录 | - |
| 3 | **OrangeTV** | Next.js 14 + Tailwind | 多资源搜索、云同步、无弹窗 | - |
| 4 | **MoonCakeTV** | Next.js 15 + TypeScript | 苹果CMS聚合、深色模式、HLS播放 | - |
| 5 | **GoFilm** | Golang + Vue + Gin | 自动采集、蓝光画质、Redis缓存 | [m.mubai.link](https://m.mubai.link/) |
| 6 | **movie-web** | React + TypeScript | 海量资源、无缝观看、4K体验 | - |

---

## 🔍 详细内容

### 1. LibreTV —— 轻量纯前端聚合神器

**项目地址**：https://github.com/LibreSpark/LibreTV  
**官方实例**：[libretv.is-an.org](https://libretv.is-an.org)

#### 简介
LibreTV 是一个轻量级、免费的在线视频搜索与观看平台，提供来自多个视频源的内容搜索与播放服务。无需注册，即开即用，支持多种设备访问。项目结合了前端技术和后端代理功能，可部署在支持服务端功能的各类网站托管服务上。

本项目基于 [bestK/tv](https://github.com/bestK/tv) 进行重构与增强。

#### 核心特性
- 🎬 多源视频搜索与聚合播放
- 🔍 快速搜索，结果秒开
- 📱 响应式设计，支持手机/平板/电脑
- 🚀 支持 Vercel 一键部署
- 🆓 无需注册，即开即用
- 🌐 支持多视频源切换

#### 快速部署

**Vercel 一键部署**：
```bash
# 点击按钮即可部署
# https://vercel.com/new/clone?repository-url=https://github.com/LibreSpark/LibreTV
```

**Docker 部署**：
```bash
docker run -d --name libretv -p 8899:80 docker.io/bestk/libretv:latest
```

---

### 2. LunaTV —— Next.js跨平台播放器（MoonTV新版）

**项目地址**：https://github.com/MoonTechLab/LunaTV  
**旧版地址**：https://github.com/senshinya/MoonTV （已迁移到新仓库）

#### 简介
MoonTV 已迁移到 LunaTV，是一个基于 Next.js 构建的跨平台影视播放器，支持海量资源、收藏同步和播放记录功能。

#### 核心特性
- 📺 海量影视资源聚合
- 💾 收藏同步，跨设备观看
- 📜 播放记录自动保存
- 📱 界面丝滑，手机4K完美支持
- 🎨 现代化 UI 设计

#### 技术栈
- Next.js 框架
- 响应式设计
- 云端数据同步

---

### 3. OrangeTV —— Next.js影视聚合站

**项目地址**：https://github.com/djteang/OrangeTV

#### 简介
OrangeTV 是一个开箱即用的、跨平台的影视聚合播放器。它基于 **Next.js 14** + **Tailwind CSS** + **TypeScript** 构建，支持多资源搜索、在线播放、收藏同步、播放记录、云端存储。

#### 核心特性
- 🔍 **多源聚合搜索**：一次搜索立刻返回全源结果
- 📄 **丰富详情页**：支持剧集列表、演员信息、简介展示
- ▶️ **在线播放**：内置播放器，支持多清晰度切换
- ❤️ **收藏与历史**：云端同步收藏和播放记录
- 🌙 **深色模式**：支持自动/手动切换深色主题
- 📱 **PWA 支持**：可安装为桌面/移动应用
- 🐳 **Docker 支持**：一键 Docker 部署

#### 快速开始

**Docker 部署**：
```bash
docker pull djteang/orangetv:latest
docker run -d -p 3000:3000 --name orangetv djteang/orangetv:latest
```

**源码部署**：
```bash
git clone https://github.com/djteang/OrangeTV.git
cd OrangeTV
npm install
npm run build
npm start
```

---

### 4. MoonCakeTV —— 月饼TV，苹果CMS多源聚合

**项目地址**：https://github.com/MoonCakeTV/MoonCakeTV

#### 简介
MoonCakeTV（月饼TV）是一个超级简单的影视聚合搜索服务，基于 Next.js 15 + TypeScript 构建，支持苹果CMS数据源聚合和HLS在线播放。

#### 核心特性
- 🥮 **超级简单**：极简部署，开箱即用
- 🔗 **多源聚合**：支持自定义视频源
- 🌙 **深色模式**：支持深色主题切换
- 📱 **响应式**：适配手机、平板、电脑
- 🔒 **HTTPS 自动配置**：支持 Caddy + Let's Encrypt 自动 SSL
- 🐳 **Docker 一键部署**：提供自动化部署脚本

#### 快速部署

**一键脚本部署**（支持 Debian, Ubuntu, Rocky Linux, AlmaLinux, Arch Linux）：
```bash
bash <(curl -fsSL https://raw.githubusercontent.com/MoonCakeTV/MoonCakeTV/main/deploy.sh)
```

脚本会自动：
- 安装 Docker（如果没有）
- 生成配置文件
- 配置 SSL 证书（Caddy + Let's Encrypt）
- 启动服务

**Docker Compose 部署**：
```yaml
version: '3'
services:
  mooncaketv:
    image: mooncaketv/mooncaketv:latest
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
```

---

### 5. GoFilm —— Golang+Vue自动采集多源

**项目地址**：https://github.com/ProudMuBai/GoFilm  
**演示站点**：[m.mubai.link](https://m.mubai.link/)  
**备用站点**：[m2.mubai.link](https://m2.mubai.link/)

#### 简介
GoFilm 是一个基于 Vue 和 Gin 实现的在线观影网站，采用 Vite + Vue 作为前端技术栈，使用 ElementPlus 作为 UI 框架。后端使用 Gin + GORM + go-redis 提供接口服务，使用 GoColly 和 robfig/cron 进行公共影视资源采集和定时更新。

#### 核心特性
- 🎬 自动采集公共影视资源
- ⏰ 定时更新功能（cron 任务）
- 🚀 Golang 后端，性能稳定
- 💾 Redis 缓存支持
- 📱 移动端优化适配
- 🔍 多源搜索聚合
- 🖼️ 蓝光级画质支持

#### 技术栈
- **前端**：Vite + Vue 3 + ElementPlus
- **后端**：Gin + GORM + go-redis
- **采集**：GoColly (爬虫)
- **定时**：robfig/cron

#### 部署方式

**Docker 部署**（推荐）：
```bash
# 查看详细部署文档
curl -fsSL https://blog.mubai.link/procedure/application/github/GoFilm/
```

**1Panel 面板部署**：
支持可视化面板操作，适合新手用户。

---

### 6. movie-web —— 现代Web技术免费聚合平台

**项目地址**：https://github.com/movie-web/movie-web

#### 简介
movie-web 是一个使用现代 Web 技术打造的免费影视聚合平台，提供海量资源的无缝观看体验，4K 体验直接起飞！

#### 核心特性
- 🎬 海量影视资源聚合
- 🖥️ 现代化 Web 技术栈
- 📱 全平台支持（手机/平板/电脑/电视）
- ⚡ 4K 画质支持
- 🔍 智能搜索
- 📜 播放历史

#### 技术栈
- React + TypeScript
- 现代化前端架构
- PWA 支持

---

## 🛠️ 技术栈对比

| 项目 | 前端 | 后端 | 数据库 | 特色技术 |
|------|------|------|--------|----------|
| LibreTV | 原生/Vue | - | - | 纯前端，无后端 |
| LunaTV | Next.js | Node.js | - | 云端同步 |
| OrangeTV | Next.js 14 | Node.js | - | PWA, TypeScript |
| MoonCakeTV | Next.js 15 | Node.js | - | Caddy SSL |
| GoFilm | Vue 3 + Vite | Gin (Go) | Redis | GoColly 爬虫 |
| movie-web | React | Node.js | - | 现代 Web 技术 |

---

## 🚀 快速部署指南

### Vercel 部署（适合前端项目）

适用于：LibreTV, LunaTV, OrangeTV, MoonCakeTV, movie-web

1. 登录 [Vercel](https://vercel.com)
2. 点击项目页面的 "Deploy with Vercel" 按钮
3. 或使用 Vercel CLI：
```bash
npm i -g vercel
vercel --prod
```

### Docker 部署（适合有后端的项目）

适用于：所有项目

```bash
# 通用 Docker 部署步骤
1. 克隆项目：git clone https://github.com/xxx/xxx.git
2. 进入目录：cd xxx
3. 构建镜像：docker build -t xxx .
4. 运行容器：docker run -d -p 3000:3000 xxx

# 或使用 docker-compose
docker-compose up -d
```

### Cloudflare Pages 部署

适用于：纯前端静态项目

1. 连接 GitHub 仓库到 Cloudflare Pages
2. 设置构建命令（通常为 `npm run build` 或 `yarn build`）
3. 设置输出目录（通常为 `dist` 或 `.next`）
4. 部署！

---

## 📱 实测体验

根据火山哥实测：
- ✅ 《Oppenheimer》《繁花》《黑神话》相关资源全在
- ✅ 手机4K秒开、零缓冲
- ✅ 倍速、弹幕、投屏全都有
- ✅ 操作像原生 App 一样爽
- ✅ 一次部署，终身免费4K

---

## 🔗 资源汇总

### GitHub 仓库链接

| 项目 | GitHub 链接 | Stars |
|------|-------------|-------|
| LibreTV | https://github.com/LibreSpark/LibreTV | ⭐ 热门 |
| LunaTV | https://github.com/MoonTechLab/LunaTV | ⭐ 新兴 |
| OrangeTV | https://github.com/djteang/OrangeTV | ⭐ 热门 |
| MoonCakeTV | https://github.com/MoonCakeTV/MoonCakeTV | ⭐ 新兴 |
| GoFilm | https://github.com/ProudMuBai/GoFilm | ⭐ 热门 |
| movie-web | https://github.com/movie-web/movie-web | ⭐ 热门 |

### 官方演示站点

- **LibreTV**: https://libretv.is-an.org
- **GoFilm**: https://m.mubai.link / https://www.mubai.cn.mt / https://m2.mubai.link

---

## 🎯 适用场景推荐

| 场景 | 推荐项目 | 理由 |
|------|----------|------|
| 快速搭建个人影院 | LibreTV | 纯前端，Vercel 一键部署 |
| 需要播放记录同步 | LunaTV / OrangeTV | 云端同步功能 |
| 自建采集站 | GoFilm | 自动采集，后端强大 |
| NAS/内网部署 | MoonCakeTV | 一键脚本，支持无 HTTPS |
| 追求极致画质 | 任意项目 + 好源 | 都支持4K |

---

## ⚠️ 免责声明

1. 本项目所有内容均来自公开网络，仅供学习和研究使用
2. 请勿用于商业用途或侵犯版权的内容传播
3. 部署后请遵守当地法律法规
4. 项目作者不对内容版权负责，请自行判断使用合法性

---

*来自翡冷翠*
