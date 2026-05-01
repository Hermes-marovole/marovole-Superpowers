# Pi-hole 网络级广告拦截完全指南

> 来源：[套利豪仔🗽 @pritipatelfgoo](https://x.com/pritipatelfgoo/status/2049842509212434795)  
> 整理时间：2026-05-01  
> 来自翡冷翠

---

## 简介

Pi-hole 是一个开源的网络级广告拦截工具，通过部署在本地网络的 DNS 服务器，在域名解析层面拦截广告和追踪器。相比浏览器插件，它能保护整个网络中的所有设备——从智能电视到手机 App，无需逐台安装软件。

**核心价值**：
- 一次性投入 < $50（旧电脑或树莓派）
- 保护全屋所有联网设备
- 屏蔽电视广告、App 弹窗、网页广告、后台追踪器
- 100% 开源，无需订阅会员

---

## 内容清单总览

| 章节 | 内容 | 核心要点 |
|------|------|----------|
| 1 | 硬件准备 | 旧电脑/树莓派要求 |
| 2 | 安装部署 | 一行命令完成安装 |
| 3 | 网络配置 | 修改路由器 DNS |
| 4 | 效果验证 | 各平台广告拦截效果 |
| 5 | 进阶配置 | 自定义规则与维护 |

---

## 详细内容

### 一、硬件准备

**最低配置要求**：
- **树莓派**：Raspberry Pi Zero 2 W / Pi 3 / Pi 4（推荐）
- **旧电脑**：任何能运行 Linux 的 x86 设备
- **内存**：512MB 即可，1GB 更流畅
- **存储**：8GB SD 卡或硬盘
- **网络**：有线连接优先，WiFi 亦可

**成本估算**：
| 方案 | 设备 | 价格 |
|------|------|------|
| 极简方案 | 树莓派 Zero 2 W | $15-20 |
| 推荐方案 | 树莓派 4 (2GB) | $35-45 |
| 废物利用 | 旧笔记本/迷你主机 | $0 |

---

### 二、安装部署

#### 方案 A：官方一键安装（推荐）

```bash
# 在树莓派或 Linux 设备上执行
curl -sSL https://install.pi-hole.net | bash
```

安装过程会引导配置：
1. 选择上游 DNS（推荐 Cloudflare 1.1.1.1 或 Quad9）
2. 选择屏蔽列表（默认即可）
3. 设置管理员密码
4. 确认网络接口

#### 方案 B：Docker 部署

```bash
# docker-compose.yml
version: "3"
services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "80:80/tcp"
    environment:
      TZ: 'Asia/Shanghai'
      WEBPASSWORD: '你的管理密码'
    volumes:
      - './etc-pihole:/etc/pihole'
      - './etc-dnsmasq.d:/etc/dnsmasq.d'
    restart: unless-stopped
```

---

### 三、网络配置

**核心步骤：将路由器 DNS 指向 Pi-hole**

#### 路由器设置方法

1. **登录路由器管理界面**（通常是 192.168.1.1 或 192.168.0.1）
2. **找到 DNS 设置**（在 WAN 或 DHCP 设置中）
3. **将主 DNS 改为 Pi-hole 的 IP 地址**
4. **保存并重启路由器**

#### Pi-hole IP 获取

```bash
# 在 Pi-hole 设备上查看 IP
hostname -I
# 或
ip addr show
```

#### 客户端配置（可选）

如果无法修改路由器，可单独配置每个设备：
- **iOS/Android**：WiFi 设置 → 高级 → 自定义 DNS
- **Windows**：网络适配器设置 → IPv4 DNS
- **macOS**：系统设置 → 网络 → DNS

---

### 四、效果验证

#### 拦截效果覆盖范围

| 平台 | 拦截内容 |
|------|----------|
| **智能电视** | 开机广告、系统广告、视频前贴片广告 |
| **手机 App** | 启动广告、弹窗广告、内嵌广告 |
| **网页浏览** | 横幅广告、悬浮广告、追踪脚本 |
| **后台追踪** | Google Analytics、Facebook Pixel 等 |
| **IoT 设备** | 智能音箱、摄像头的 telemetry 上报 |

#### 验证方法

1. **访问 Pi-hole 管理面板**
   - 浏览器打开 `http://<Pi-hole-IP>/admin`
   - 登录查看仪表盘

2. **检查拦截统计**
   - 仪表盘显示今日拦截查询数
   - 查看 "Query Log" 确认特定域名被拦截

3. **测试广告网站**
   - 访问 `https://ads-blocker.com/testing/`
   - 或访问常见新闻网站查看广告是否消失

---

### 五、进阶配置

#### 添加自定义屏蔽列表

```
Pi-hole 管理面板 → Group Management → Adlists
```

推荐列表：
- `https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts`（综合列表）
- `https://someonewhocares.org/hosts/zero/hosts`（轻量列表）
- `https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts`（挖矿脚本）

#### 白名单设置

某些网站功能可能被误拦截：
```
管理面板 → Whitelist → 添加域名
```

常见需要白名单的域名：
- `login.live.com`（微软服务登录）
- `app.link`（某些 App 深度链接）

#### 本地 DNS 记录

可为内网设备添加自定义域名：
```
管理面板 → Local DNS → DNS Records
```

#### 自动更新

Pi-hole 自动更新屏蔽列表（默认每周），也可手动更新：
```bash
pihole -g
```

---

## 资源汇总

### 官方资源
| 名称 | 链接 | 说明 |
|------|------|------|
| Pi-hole 官网 | https://pi-hole.net | 官方网站与文档 |
| GitHub 仓库 | https://github.com/pi-hole/pi-hole | 开源代码 |
| 安装脚本 | https://install.pi-hole.net | 一键安装 |
| 社区论坛 | https://discourse.pi-hole.net | 技术支持 |

### 涉及工具/技术
- **Pi-hole** - 开源 DNS 级广告拦截器
- **dnsmasq** - 轻量级 DNS 转发器
- **gravity** - Pi-hole 的屏蔽列表管理系统
- **AdminLTE** - Web 管理界面框架

### 值得关注
- **@pritipatelfgoo** - 套利豪仔，价值投资者，分享实用工具与链上套利技巧

---

## 快速参考

### 常用命令

```bash
# 查看状态
pihole status

# 更新屏蔽列表
pihole -g

# 查看日志
tail -f /var/log/pihole.log

# 重启服务
pihole restartdns

# 禁用/启用
pihole disable
pihole enable

# 查看版本
pihole -v
```

### 管理面板快捷键

| 功能 | 路径 |
|------|------|
| 仪表盘 | `/admin` |
| 查询日志 | `/admin/queries.php` |
| 白名单 | `/admin/groups-domains.php?type=white` |
| 黑名单 | `/admin/groups-domains.php?type=black` |
| 屏蔽列表 | `/admin/groups-adlists.php` |

---

## 故障排查

### 安装后无法访问网络

**症状**：设备无法上网  
**解决**：
1. 检查 Pi-hole 是否正常运行：`pihole status`
2. 确认上游 DNS 配置正确（管理面板 → Settings → DNS）
3. 临时切换回原始 DNS，排查 Pi-hole 设备网络问题

### 某些网站无法打开

**症状**：特定网站显示错误或无法加载  
**解决**：
1. 检查 Pi-hole 查询日志，找出被拦截的域名
2. 将相关域名加入白名单
3. 或使用 "Tail pihole.log" 实时查看拦截记录

### 广告仍然存在

**症状**：部分广告未被拦截  
**解决**：
1. 添加更多屏蔽列表（Group Management → Adlists）
2. 检查是否为 HTTPS/DNS-over-HTTPS 广告（Pi-hole 无法拦截）
3. 确认设备确实在使用 Pi-hole 作为 DNS

---

## 扩展阅读

### 进阶方案：AdGuard Home

如果 Pi-hole 功能不满足需求，可考虑 **AdGuard Home**：
- 更现代的 Web 界面
- 内置 HTTPS/DNS-over-HTTPS 过滤
- 更精细的家长控制
- 同样开源免费

### 企业级方案

- **pfSense + pfBlockerNG**：防火墙级别的拦截
- **AdGuard DNS**：云托管方案，无需本地设备

---

*来自翡冷翠*
