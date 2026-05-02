# Scrapling - 自适应 Web 抓取框架

> 来源：https://github.com/D4Vinci/Scrapling  
> 作者：Karim Shaari (D4Vinci)  
> 整理时间：2025-05-02  
> GitHub Stars：41k+ | Forks：3.7k+

---

## 执行摘要

Scrapling 是一个自适应的 Web 抓取框架，从单一请求到全规模爬取都能处理。它的核心理念是：**像浏览器一样解析页面，像 requests 一样快速**。

- **41k+ Stars** 证明其在开源社区的广泛认可
- **92% 测试覆盖率**，经过数百个真实网站验证
- **极致性能**，在多项基准测试中表现优于 BeautifulSoup、lxml 等常见库
- **完整的 AI 集成**，内置 MCP 服务器支持

---

## 核心功能特性

### 1. 完整的爬虫框架 (Spiders)

类 Scrapy API 设计，提供完整的爬虫开发体验：
n- **使用模式**：`start_urls` 配置、async 解析回调、Request/Response 对象
- **并发控制**：统一 HTTP 请求接口、每个域名的节流、智能延迟
- **多 Session 支持**：在单个 spider 中通过 ID 区分不同 session 的请求
- **暂停与恢复**：支持 graceful shutdown，通过 checkpoint 重启
- **流式模式**：支持 `stream=True` 处理大文件，实时统计
- **请求阻塞检测**：自动检测并处理被阻止的请求
- **Robots.txt 合规**：自动遵循 robots.txt，支持自定义 User-Agent

### 2. 高级网站抓取与会话支持

提供多层级的抓取能力：

- **HTTP 请求**：快速稳定，支持 HTTP/2、HTTP/3、浏览器级 TLS 指纹
- **动态加载**：通过 `DynamicFetcher` 实现完整的浏览器自动化
- **反 Bot 绕过**：高级隐身功能，击败 Cloudflare、DataDome、PerimeterX 等反爬机制
- **会话管理**：持久化 cookie 和状态管理
- **代理轮换**：支持每个请求的代理轮换，细粒度控制
- **域名与广告拦截**：内置 35,000+ 广告拦截规则，Cloudflare DNS 支持
- **异步支持**：完整的 async/await 支持

### 3. 自适应抓取与 AI 集成

**Scrapling 最突出的特性之一**：

- **智能元素追踪**：页面变化后通过智能相似度算法重新定位元素
- **智能灵活选择**：CSS 选择器、XPath、基于文本的搜索、正则表达式
- **类似人类的元素查找**：模拟人类行为的元素定位方式
- **MCP 服务器**：支持 Model Context Protocol，用于 AI 辅助的 Web 抓取

### 4. 高性能与久经考验的架构

- **极速性能**：在多项基准测试中表现优于大多数 Python 抓取库
- **内存高效**：优化的数据结构，延迟加载
- **快速 JSON 序列化**：比标准库快 10 倍
- **测试覆盖**：92% 的测试覆盖率，数百个真实网站验证

### 5. 开发者友好的体验

- **交互式 Web 抓取 Shell**：内置 Python shell，支持 URL 直接抓取
- **终端直接使用**：无需编写脚本，命令行直接提取数据
- **增强的导航 API**：DOM 遍历、同级查找、子元素导航
- **优化的文本处理**：内置正则、清理方法、字符串操作
- **自动选择器生成**：为任何元素生成鲁棒的 CSS/XPath 选择器
- **熟悉的 API**：类似 Scrapy/BeautifulSoup 的伪元素用法
- **完整的类型覆盖**：全类型提示，IDE 自动补全支持
- **即用型 Docker 镜像**：预装所有浏览器的 Docker 镜像

---

## 性能基准测试

### 文本提取速度测试 (5000 个嵌套元素)

| 库 | 时间 (ms) | vs Scrapling |
|------|-----------|--------------|
| **Scrapling** | **2.02** | 1.0x (基准) |
| parsel | 2.04 | 1.01x |
| BeautifulSoup | 2.54 | 1.26x |
| lxml | 26.12 | 12.9x |
| pyQuery | 41.13 | ~20x |
| html5lib | 82.63 | ~41x |
| MechanicalSoup | 149.21 | ~74x |
| BeautifulSoup with lxml | 1584.31 | ~784x |
| RoboBrowser with html5lib | 3391.91 | ~1679x |

### 元素相似度与文本搜索性能

| 库 | 时间 (ms) | vs Scrapling |
|------|-----------|--------------|
| **Scrapling** | **2.39** | 1.0x |
| parsel | 12.45 | 5.20x |
| BeautifulSoup | 42.43 | 17.7x |

*这些测试代表 100+ 次运行的平均值*

---

## 技术架构详情

### 核心组件架构

**1. Fetcher 层级**：四层抓取能力次递增

| 类名 | 功能 | 适用场景 |
|------|------|---------|
| `Fetcher` | 基础 HTTP 请求 | 简单抓取 |
| `AsyncFetcher` | 异步 HTTP | 高并发场景 |
| `StealthyFetcher` | 隐身模式 | 反反爬场景 |
| `DynamicFetcher` | 浏览器自动化 | 动态页面 |

**2. Session 管理**

| 类名 | 功能 | 特点 |
|------|------|------|
| `FetcherSession` | 保持 cookie 和状态 | 基础会话 |
| `StealthySession` | 隐身会话 | 反检测能力 |
| `DynamicSession` | 浏览器会话 | 完整渲染 |
| `AsyncFetcherSession` | 异步会话 | 并发优化 |

**3. 解析引擎**

- 基于 **Parsel** (Scrapy 的选择器库)
- 支持 CSS 选择器、XPath、正则表达式
- 自适应重定位算法

**4. Spider 框架**

- 类 Scrapy 架构
- 支持异步解析
- 内置并发控制和延迟
- 支持暂停/恢复和断点续传

---

## 安装方法

### 系统要求

Python 3.10 或更高版本

### 基础安装

```bash
pip install scrapling
```

*注意：此安装仅包含解析引擎和其依赖，不含 fetchers 或命令行支持*

### 可选依赖

**1. 如果需要使用 fetchers 或其他扩展功能**：

```bash
# 安装 fetcher 依赖
pip install "scrapling[fetcher]"

# 或一次性安装所有浏览器依赖
scrapling install

# 强制重新安装
scrapling install --force
```

**2. 扩展功能包**：

```bash
# MCP 服务器功能
pip install "scrapling[mcp]"

# Shell 功能（Web 抓取 shell 和 extract 命令）
pip install "scrapling[shell]"

# 安装所有功能
pip install "scrapling[all]"
```

**提醒**：安装任何扩展后，如果尚未安装浏览器依赖，需要运行 `scrapling install`

---

## 使用示例

### 1. 带会话支持的 HTTP 请求

```python
from scrapling.fetchers import Fetcher, FetcherSession

# 使用会话保持 cookie 和状态
with FetcherSession() as session:
    page = session.get('https://example.com', stealth_headers=True)
    quotes = page.css('div.quote')
```

### 2. 高级隐身模式

```python
from scrapling.fetchers import StealthyFetcher, StealthySession

# 自动处理指纹和反爬
with StealthySession() as session:
    page = session.get('https://example.com')
```

### 3. 完整浏览器自动化

```python
from scrapling.fetchers import DynamicFetcher, DynamicSession

# 使用 Playwright 驱动的浏览器
with DynamicSession(headless=False) as session:
    page = session.get('https://example.com')
    page.click('button#load-more')
```

### 4. Spiders 爬虫示例

```python
from scrapling.spiders import Spider, Request, Response

class QuotesSpider(Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']
    concurrent_requests = 2
    
    async def parse(self, response: Response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }
        
        # 自动跟踪分页
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
```

### 5. 异步会话管理

```python
import asyncio
from scrapling.fetchers import AsyncFetcherSession

async def main():
    async with AsyncFetcherSession() as session:
        task1 = session.get('https://example.com/1')
        task2 = session.get('https://example.com/2')
        results = await asyncio.gather(task1, task2)
```

---

## MCP 服务器详情

Scrapling 内置 MCP (Model Context Protocol) 服务器，用于 AI 辅助的 Web 抓取和数据提取。

### 核心能力

- **目标内容提取**：在传递给 AI 之前，先利用 Scrapling 提取目标内容
- **加速操作**：减少 token 使用量，降低成本
- **工具集成**：提供截图等 MCP 工具

### 安装使用

```bash
pip install "scrapling[mcp]"
```

安装后可与 Claude、Cursor 等支持 MCP 的 AI 工具配合使用。

---

## Docker 使用

### 从 DockerHub 拉取

```bash
docker pull paveldedik/scrapling:latest
```

### 从 GitHub Registry 拉取

```bash
docker pull ghcr.io/d4vinci/scrapling:latest
```

### 镜像特点

- 预装所有扩展功能
- 已安装所有浏览器
- 通过 GitHub Actions 自动构建并推送

---

## 与其他库的对比

| 特性 | Scrapling | Scrapy | BeautifulSoup | Selenium |
|------|-----------|--------|---------------|----------|
| 自适应重定位 | ✅ 内置 | ❌ 需外部 | ❌ | ❌ |
| 反反爬 | ✅ 多层级 | ✅ 中间件 | ❌ | ❌ |
| 浏览器自动化 | ✅ Playwright | ✅ Splash | ❌ | ✅ 原生 |
| 异步支持 | ✅ 原生 | ✅ Twisted | ❌ | ❌ |
| AI 集成 | ✅ MCP | ❌ | ❌ | ❌ |
| 学习曲线 | 低 | 高 | 低 | 中 |
| 性能 | 极高 | 高 | 中 | 低 |

---

## 适用场景

### 适合使用 Scrapling 的场景

1. **反反爬需求**：需要绕过 Cloudflare、DataDome 等防护系统
2. **动态内容**：页面大量使用 JavaScript 渲染
3. **结构变化**：目标网站经常变更 DOM 结构
4. **AI 集成**：需要与 LLM 工作流集成
5. **性能要求**：高并发、大规模抓取任务
6. **现代代替**：寻找 Scrapy 或 BeautifulSoup 的现代替代品

### 可能不适合的场景

- 超简单的静态页面抓取（BeautifulSoup 可能更轻量）
- 无特殊反爬需求的内部工具
- 团队已深度使用 Scrapy 生态并有现成扩展

---

## 实践建议

### 1. 选择合适的 Fetcher

```python
# 普通静态页面
from scrapling.fetchers import Fetcher

# 反反爬场景
from scrapling.fetchers import StealthyFetcher

# 动态 JavaScript 渲染
from scrapling.fetchers import DynamicFetcher
```

### 2. 会话最佳实践

```python
# 使用上下文管理器确保资源释放
with FetcherSession() as session:
    # 自动处理 cookie 和状态
    page1 = session.get('https://example.com/login')
    page2 = session.get('https://example.com/data')
```

### 3. 自适应元素定位

```python
# 当页面结构变化时，智能重定位
price = page.find(
    selector='div.price',
    similarity_threshold=0.8  # 调整相似度阈值
)
```

---

## 免责声明

> ⚠️ **警告**：
> 
> 本库仅用于教育和研究目的。使用本库即表示您同意遵守当地和国际法律关于 Web 抓取和数据提取的规定。作者和维护者不对本软件的任何滥用负责。始终尊重网站的服务条款和 robots.txt 文件。

---

## 参考文献

```bibtex
@software{scrapling,
  author = {Karim Shaari},
  title = {Scrapling},
  year = {2024},
  url = {https://github.com/d4vinci/scrapling},
  note = {An adaptive Web Scraping framework}
}
```

---

*来自翡冷翠*
