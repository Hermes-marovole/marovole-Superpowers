# Proxifly 免费代理服务 - 完整整理

> 来源：https://x.com/wsl8297/status/2047587170404426090  
> 整理时间：2026-04-24  
> 来自翡冷翠

---

## 简介

本文档整理了由 Joruno (@wsl8297) 分享的 **Proxifly** 开源项目 —— 一个每 5 分钟自动抓取、更新并验证免费代理的服务，彻底解决爬虫和数据采集中代理 IP 被封的问题。

---

## 核心信息

| 指标 | 详情 |
|------|------|
| **GitHub 仓库** | [proxifly/free-proxy-list](https://github.com/proxifly/free-proxy-list) |
| **官网** | [proxifly.dev](https://proxifly.dev) |
| **Stars** | 4.7k+ |
| **Forks** | 530+ |
| **更新频率** | 每 5 分钟 |
| **覆盖国家** | 76+ 个 |
| **可用代理** | 2800+ 个 |
| **支持协议** | HTTP / HTTPS / SOCKS4 / SOCKS5 |
| **许可证** | GPL-3.0 |

---

## 为什么需要它？

开发爬虫和做数据采集时，代理服务器几乎是刚需：

- **IP 容易被封** — 频繁请求同一网站会触发反爬机制
- **免费代理失效快** — 网上多数"免费代理"早已不可用
- **验证成本高** — 手动测试代理可用性耗时耗力

**Proxifly 的解决方案**：
- ✅ 每 5 分钟自动抓取、更新并验证
- ✅ 去重处理，避免重复代理
- ✅ 按协议类型与国家/地区分类
- ✅ 提供 JSON / TXT / CSV 三种格式
- ✅ 支持 npm 安装，代码直接调用

---

## 实时代理统计

> 数据更新时间：2026-04-24 UTC

| 类型 | 可用代理数 | JSON | TXT | CSV |
|------|-----------|------|-----|-----|
| **全部代理** | 2876 | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.json) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.txt) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.csv) |
| **HTTP** | 1031 | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/http/data.json) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/http/data.txt) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/http/data.csv) |
| **HTTPS** | 779 | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/https/data.json) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/https/data.txt) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/https/data.csv) |
| **SOCKS4** | 732 | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks4/data.json) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks4/data.txt) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks4/data.csv) |
| **SOCKS5** | 334 | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks5/data.json) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks5/data.txt) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks5/data.csv) |
| **美国** | 449 | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/countries/US/data.json) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/countries/US/data.txt) | [下载](https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/countries/US/data.csv) |

**更多国家**：[查看完整国家列表](https://github.com/proxifly/free-proxy-list/tree/main/proxies/countries)

---

## 使用方式

### 方式一：网页直接下载（最简单）

访问官网工具页面，按需筛选下载：

👉 [proxifly.dev/tools/proxy-list](https://proxifly.dev/tools/proxy-list)

支持按协议、国家、匿名度筛选，一键下载所需格式。

---

### 方式二：桌面客户端

Proxifly 提供跨平台的代理抓取软件：

| 平台 | 下载 |
|------|------|
| Windows | [下载](https://proxifly.dev/download?download=windows) |
| macOS | [下载](https://proxifly.dev/download?download=macos) |
| Linux | [下载](https://proxifly.dev/download?download=linux) |

---

### 方式三：cURL 命令行下载

```bash
# 下载全部代理
curl -sL https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.txt -o all.txt

# 下载 HTTP 代理
curl -sL https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/http/data.txt -o http.txt

# 下载 SOCKS5 代理
curl -sL https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks5/data.txt -o socks5.txt

# 下载美国代理
curl -sL https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/countries/US/data.txt -o us.txt
```

---

### 方式四：Node.js 集成（推荐开发者）

#### 安装

```bash
npm install proxifly
```

#### ESM 用法

```js
import Proxifly from 'proxifly';

const proxifly = new Proxifly({
  // 可选，但有 API Key 可移除请求限制
  // 获取地址：https://proxifly.dev/account#apiKeys
  apiKey: 'your-api-key'
});

// 获取代理
proxifly.getProxy({
  protocol: 'http',     // http | socks4 | socks5
  anonymity: 'elite',   // transparent | anonymous | elite
  country: 'US',        // ISO 国家代码
  https: true,          // 是否支持 HTTPS
  quantity: 1,          // 返回数量 (1-20)
  format: 'json',       // json | text
})
.then(proxy => {
  console.log('代理:', proxy);
})
.catch(e => {
  console.error(e);
});
```

#### CommonJS 用法

```js
const Proxifly = require('proxifly');

const proxifly = new Proxifly({
  apiKey: 'your-api-key'
});

// 获取公开 IP
proxifly.getPublicIp()
  .then(response => {
    console.log('IP:', response.ip);
    console.log('国家:', response.country);
    console.log('城市:', response.city);
  })
  .catch(e => console.error(e));
```

#### 浏览器 Script Tag 用法

```html
<script src="https://cdn.jsdelivr.net/npm/proxifly@latest/dist/proxifly.min.js"></script>
<script>
  var proxifly = new Proxifly({
    apiKey: 'your-api-key',
  });
  
  proxifly.getProxy({ protocol: 'http', quantity: 5 })
    .then(result => console.log(result));
</script>
```

---

### 方式五：REST API 直接调用

#### 获取代理

```bash
# JSON 格式
curl -X POST https://api.proxifly.dev/get-proxy \
  -H "Content-Type: application/json" \
  -d '{
    "apiKey": "your-api-key",
    "country": ["US", "RU"],
    "protocol": ["http", "socks4"],
    "https": true,
    "quantity": 20
  }'

# 简化版（无需 API Key，有频率限制）
curl "https://api.proxifly.dev/proxy?protocol=http&quantity=3&format=text"
```

#### 获取公开 IP

```bash
curl https://api.proxifly.dev/ip
```

---

## API 参数详解

### getProxy(options)

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `protocol` | string | - | 协议类型：`http` / `socks4` / `socks5` |
| `anonymity` | string | - | 匿名度：`transparent` / `anonymous` / `elite` |
| `country` | string | - | ISO 国家代码（如 `US`, `CN`, `GB`） |
| `https` | boolean | - | 是否支持 HTTPS |
| `quantity` | number | 1 | 返回代理数量（1-20） |
| `format` | string | `json` | 返回格式：`json` / `text` |
| `timeout` | number | 60000 | 请求超时（毫秒） |

### 返回示例

```json
{
  "proxy": "socks4://103.99.110.222:5678",
  "protocol": "socks4",
  "ip": "103.99.110.222",
  "port": 5678,
  "https": false,
  "anonymity": "transparent",
  "score": 1,
  "geolocation": {
    "country": "IN",
    "city": "Unknown"
  }
}
```

---

## 代理匿名度说明

| 匿名度 | 说明 | 适用场景 |
|--------|------|----------|
| **Transparent** | 透明代理，会透露真实 IP | 缓存加速、内容过滤 |
| **Anonymous** | 匿名代理，隐藏真实 IP 但标识自己是代理 | 一般爬虫、数据采集 |
| **Elite** | 高匿代理，完全隐藏代理痕迹 | 敏感操作、高安全需求 |

---

## 项目特点

| 特性 | 说明 |
|------|------|
| ⚡ 极速更新 | 每 5 分钟自动抓取验证 |
| 📝 多格式 | JSON / TXT / CSV 三种格式 |
| 🌎 全球覆盖 | 76+ 国家/地区 |
| 🔐 协议齐全 | HTTP / HTTPS / SOCKS4 / SOCKS5 |
| 😊 无重复 | 智能去重算法 |
| 🔧 多平台 | 支持 Node.js / 浏览器 / cURL |
| 📦 NPM 包 | `npm install proxifly` 即用 |
| 🆓 免费开源 | GPL-3.0 许可证 |

---

## 使用建议

### 爬虫场景最佳实践

1. **轮询策略**：从代理池随机选取，避免单一代理过度使用
2. **失败重试**：代理失效时自动切换，设置 3 次重试机制
3. **匿名度选择**：
   - 普通数据采集 → Anonymous
   - 敏感/高频操作 → Elite
4. **地理位置**：根据目标网站选择相近地区代理，降低延迟

### 代码示例：Python 配合 Proxifly

```python
import requests
import random

# 从 Proxifly 获取的代理列表
proxies_list = [
    "http://103.99.110.222:8080",
    "http://47.88.18.204:3128",
    "socks5://104.173.192.180:1080"
]

def get_with_proxy(url):
    proxy = random.choice(proxies_list)
    proxies = {
        "http": proxy,
        "https": proxy
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        return response
    except:
        # 代理失效，重试
        return get_with_proxy(url)

# 使用
response = get_with_proxy("https://example.com")
print(response.status_code)
```

### 代码示例：Node.js 配合 Proxifly

```js
const Proxifly = require('proxifly');
const axios = require('axios');

const proxifly = new Proxifly();

async function fetchWithProxy(url) {
  try {
    // 获取一个 HTTP 代理
    const { proxy } = await proxifly.getProxy({
      protocol: 'http',
      anonymity: 'elite',
      quantity: 1
    });
    
    // 使用代理请求
    const response = await axios.get(url, {
      proxy: {
        protocol: 'http',
        host: proxy.ip,
        port: proxy.port
      },
      timeout: 10000
    });
    
    return response.data;
  } catch (error) {
    console.error('请求失败:', error.message);
    // 可在此实现重试逻辑
  }
}

// 使用
fetchWithProxy('https://example.com').then(data => console.log(data));
```

---

## 资源汇总

### 官方链接
| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/proxifly/free-proxy-list |
| NPM 包 | https://www.npmjs.com/package/proxifly |
| 官网 | https://proxifly.dev |
| 代理列表工具 | https://proxifly.dev/tools/proxy-list |
| 公开 IP 查询 | https://proxifly.dev/tools/public-ip |
| 文档 | https://proxifly.dev/docs |

### 相关仓库
| 项目 | 链接 |
|------|------|
| proxifly SDK | https://github.com/proxifly/proxifly |

### 值得关注的人
- **Joruno** [@wsl8297](https://x.com/wsl8297) - AI 程序员，分享高质量教程与 AI 工具

---

## 许可证

- **free-proxy-list**: GPL-3.0 License
- **proxifly npm**: MIT License

---

## 免责声明

使用免费代理时请注意：
1. 免费代理稳定性不如付费代理，生产环境建议做好容错
2. 部分代理可能有流量限制或使用时长限制
3. 遵守目标网站的 robots.txt 和使用条款
4. 不要用于非法用途或恶意攻击

---

*来自翡冷翠*
