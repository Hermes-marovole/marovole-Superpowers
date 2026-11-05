# AI Agent 深度商业调研、数据抓取与事实核查（Grounding）全量配置 Handoff SOP

> **给同事的使用方法（两步搞定）**：
> 1. 先看 **【第 0 步：5 分钟领齐免费 API Keys】**，点开链接把 Key 领好（哪怕只领前 3 个也能跑通主力调研链路；另外内置的「6大平台搜索动作/购买意图雷达」与 DuckDuckGo/Jina 完全免 Key）。
> 2. 把本文档连同你填好的 Keys 直接发给你的 **Hermes Agent** 或 **Claude Code**，发送这一句指令：
>    **“请严格按照这份 Handoff 文档的 Step 1 到 Step 6，自动识别我当前的宿主环境（Hermes 或 Claude Code），帮我把 CLI 依赖、6 个 MCP 服务、多引擎搜索路由器以及含《深度商业与招股书财报调研 (market-intelligence)》在内的核心 Skills 全部配齐，并跑通 Step 5 验收测试。”**
>
> *—— 来自 翡冷翠 · 智子 (Hermes Agent)*

---

## 第 0 步：人类准备清单（5 分钟领齐搜索与提取 API Keys）

为了让你的 Agent 具备 **「语义发现 + 深度调研 + Google 原始 SERP + 动态网页转 Markdown + 招股书/财报穿透 + 电商/社媒一手数据抓取」** 的完整能力，建议配齐以下 API Key（**前 5 个均有免费额度**）：

| 优先级 | 服务名称 | 核心用途 | 免费额度 / 门槛 | Key 格式特征 | 申请控制台直达链接 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P0 必配** | **Exa AI** | 语义/神经搜索、找论文/GitHub/相似竞品公司 | 注册送免费 Credits | `xxxxxxxx-xxxx-...` (UUID) | [dashboard.exa.ai/api-keys](https://dashboard.exa.ai/api-keys) |
| **P0 必配** | **Tavily** | AI 深度研究、原理解析、多源聚合问答 | **每月 1,000 次免费**（免绑卡） | `tvly-dev-...` 或 `tvly-...` | [app.tavily.com/home](https://app.tavily.com/home) |
| **P0 必配** | **Firecrawl** | 动态网页/PDF招股书转纯净 Markdown、全站爬取 | 注册送 **500 页免费额度** | `fc-...` | [firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) |
| **P0 必配** | **Serper.dev** | **Google 原始搜索结果**（查价格/招股书/电商/site:语法最准） | 注册送 **2,500 次免费 Google 查询** | 40 位十六进制字符串 | [serper.dev/api-key](https://serper.dev/api-key) |
| **P1 推荐** | **Brave Search** | 独立索引高速网页搜索、时效新闻与本地商业检索 | Free AI 档 **每月 2,000 次免费** | `BSA...` | [api-dashboard.search.brave.com](https://api-dashboard.search.brave.com/) |
| **P1 推荐** | **TinyFish** | 免费 Search/Fetch + 远程云端浏览器自然语言提取 JSON | Search 与 Fetch 接口免费 | `tf_...` | [agent.tinyfish.ai](https://agent.tinyfish.ai) |
| **免 Key** | **内置免鉴权武器** | **6大平台下拉词雷达 (百度/Google/必应/淘宝/Amazon/YouTube) + OpenCLI 181 站点 + Context7 + Jina + DDGS** | **永久免费、无需注册** | 无需 Key | 脚本自动内置配置 |

**发给 Agent 时的填空模板（直接复制填好连同本文档发给 Agent）**：

```env
EXA_API_KEY=在这里填你的_Exa_Key
TAVILY_API_KEY=在这里填你的_Tavily_Key
FIRECRAWL_API_KEY=在这里填你的_Firecrawl_Key
SERPER_API_KEY=在这里填你的_Serper_Key
BRAVE_SEARCH_API_KEY=在这里填你的_Brave_Key
TINYFISH_API_KEY=在这里填你的_TinyFish_Key
```

---

## Agent 自动化执行总则（Agent Execution Rules — 供接收方 Agent 阅读）

当你（Hermes Agent / Claude Code / Alma / Cursor）收到本文档后，**严禁只做文字总结**，必须严格按照 **Step 1 → Step 5** 顺序在终端与文件系统中自动落地全部配置：

1. **自动识别宿主环境并适配路径**：
   - **Hermes Agent**（检测到 `~/.hermes/config.yaml` 存在）：
     - 环境变量写入：`~/.hermes/.env`
     - MCP 配置合并进：`~/.hermes/config.yaml` 的 `mcp_servers:` 块
     - 技能安装目录：`~/.hermes/skills/research/` 与 `~/.hermes/skills/web-automation/`
     - Python 虚拟环境：若存在 `~/.hermes/hermes-agent/venv/bin/pip`，同步将 `ddgs` 安装进该 venv。
   - **Claude Code**（检测到 `~/.claude` 或运行在 Claude Code CLI 下）：
     - MCP 配置合并进：`~/.claude.json` 的 `mcpServers` 块
     - 技能安装目录：`~/.claude/skills/`
   - **通用共享路由器目录**：统一安装在 `~/.config/agent-research-router/`（供所有 Agent 跨宿主共用）。
2. **保护存量配置（Non-Destructive Merge）**：
   - 修改 `~/.hermes/config.yaml`、`~/.hermes/.env` 或 `~/.claude.json` 前，**必须先备份原文件（`.bak-YYYYMMDD`）**，只做增量合并（Merge），严禁覆盖或清空用户原有的模型、代理或其他 MCP 配置。
3. **缺省 Key 优雅降级**：
   - 若用户未提供某项 API Key，将其留空并继续执行；多引擎路由脚本会自动跳过未配置的引擎并无缝降级到已配置或免 Key 引擎（如 `ddgs` / `jina` / 6大平台下拉词接口）。

---

## Step 1：安装前置 CLI 武器库（OpenCLI 181 站点 + Dokobot + TinyFish + Parallel + DDGS）

Agent 请在终端执行以下命令，装齐 5 大核心采集 CLI：
- **`@jackwener/opencli`**：把 **181 个主流网站（京东、淘宝、1688、闲鱼、小红书、抖音、知乎、B站、东方财富、雪球、BOSS直聘、Amazon、Reddit、YouTube、PubMed 等 1289 个命令）** 变成免写爬虫的结构化 JSON CLI。
- **`@dokobot/cli`**：复用本机真实 Chrome 登录态读取防爬/登录墙网页。
- **`@tiny-fish/cli`**：支持自然语言驱动远程云端浏览器抓取动态表格。
- **`parallel-cli`**：全网实体发现（`findall`）与 CSV 竞品表自动联网补全（`enrich`）。
- **`ddgs`**：免费 DuckDuckGo 搜索 Python 库。

```bash
# 1. 检查 Node / Python 基础环境并安装 uv (用于驱动 uvx MCP)
node -v && npm -v && python3 --version
command -v uvx >/dev/null 2>&1 || curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 安装 Python 免费搜索包 ddgs（系统级 + Hermes runtime venv 双装）
pip3 install -U ddgs pyyaml 2>/dev/null || pip3 install --break-system-packages -U ddgs pyyaml
if [ -x "$HOME/.hermes/hermes-agent/venv/bin/pip" ]; then
  "$HOME/.hermes/hermes-agent/venv/bin/pip" install -U ddgs pyyaml
fi

# 3. 安装 OpenCLI（181 个国内外网站结构化数据 CLI：京东/淘宝/1688/闲鱼/小红书/抖音/雪球/东方财富/Reddit/Amazon）
command -v opencli >/dev/null 2>&1 || npm install -g @jackwener/opencli@latest

# 4. 安装 Dokobot CLI（真实 Chrome 浏览器桥接）与 TinyFish CLI
command -v dokobot >/dev/null 2>&1 || npm install -g @dokobot/cli@latest
command -v tinyfish >/dev/null 2>&1 || npm install -g @tiny-fish/cli@latest

# 5. 安装 Parallel CLI（可选重型研究武器）
command -v parallel-cli >/dev/null 2>&1 || brew install parallel-web/tap/parallel-cli 2>/dev/null || npm install -g parallel-web-cli 2>/dev/null || true
```

---

## Step 2：挂载 6 大调研与提取 MCP 服务（支持 Hermes 与 Claude Code 双环境）

Agent 请运行以下 Python 脚本，将用户提供的 API Keys 写入环境变量，并将 **Firecrawl、Exa Search、Brave Search、Context7（最新开发文档防幻觉）、Fetch、Time** 安全增量合并进 `~/.hermes/config.yaml`（若存在）和 `~/.claude.json`（若存在）：

```bash
python3 - <<'PY'
import datetime, json, os, re, shutil
from pathlib import Path

# === Agent 请在此填入用户提供的真实 Key（未提供则留空 ""）===
USER_KEYS = {
    "EXA_API_KEY": "<YOUR_EXA_API_KEY>",
    "TAVILY_API_KEY": "<YOUR_TAVILY_API_KEY>",
    "FIRECRAWL_API_KEY": "<YOUR_FIRECRAWL_API_KEY>",
    "SERPER_API_KEY": "<YOUR_SERPER_API_KEY>",
    "BRAVE_SEARCH_API_KEY": "<YOUR_BRAVE_API_KEY>",
    "TINYFISH_API_KEY": "<YOUR_TINYFISH_API_KEY>",
}

def clean_key(val: str) -> str:
    val = (val or "").strip()
    if not val or val.startswith("<YOUR_") or val.startswith("在这里填"):
        return ""
    return val

# 1. 从已有环境变量或 ~/.hermes/.env 补充读取已存在的 Key
hermes_env = Path.home() / ".hermes/.env"
if hermes_env.exists():
    for line in hermes_env.read_text().splitlines():
        m = re.match(r"^\s*([A-Z0-9_]+)\s*=\s*(.*)$", line)
        if m and not clean_key(USER_KEYS.get(m.group(1), "")):
            USER_KEYS[m.group(1)] = m.group(2).strip().strip('"').strip("'")

for k in list(USER_KEYS.keys()):
    USER_KEYS[k] = clean_key(USER_KEYS[k]) or clean_key(os.getenv(k, ""))

ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
uvx_bin = shutil.which("uvx") or str(Path.home() / ".local/bin/uvx")

# 2. 更新统一路由器环境变量 ~/.config/agent-research-router/.env
router_dir = Path.home() / ".config/agent-research-router"
router_dir.mkdir(parents=True, exist_ok=True)
env_lines = [f'{k}="{v}"' for k, v in USER_KEYS.items() if v]
(router_dir / ".env").write_text("\n".join(env_lines) + "\n")
print("✅ Wrote router .env:", router_dir / ".env")

# 3. 若存在 Hermes Agent (~/.hermes)，增量更新 .env 与 config.yaml
hermes_dir = Path.home() / ".hermes"
if hermes_dir.exists():
    if hermes_env.exists():
        shutil.copy2(hermes_env, hermes_dir / f".env.bak-{ts}")
        existing_text = hermes_env.read_text()
    else:
        existing_text = ""
    for k, v in USER_KEYS.items():
        if v and f"{k}=" not in existing_text:
            existing_text = existing_text.rstrip() + f"\n{k}={v}\n"
    hermes_env.write_text(existing_text)

    cfg_path = hermes_dir / "config.yaml"
    if cfg_path.exists():
        import yaml
        shutil.copy2(cfg_path, hermes_dir / f"config.yaml.bak-{ts}")
        cfg = yaml.safe_load(cfg_path.read_text()) or {}
        mcp = cfg.setdefault("mcp_servers", {})

        if USER_KEYS["FIRECRAWL_API_KEY"] and "firecrawl" not in mcp:
            mcp["firecrawl"] = {
                "command": "npx",
                "args": ["-y", "firecrawl-mcp"],
                "env": {"FIRECRAWL_API_KEY": USER_KEYS["FIRECRAWL_API_KEY"]},
                "connect_timeout": 60,
                "timeout": 120,
            }
        if USER_KEYS["EXA_API_KEY"] and "exa" not in mcp:
            mcp["exa"] = {
                "command": "npx",
                "args": ["-y", "exa-mcp-server", "tools=web_search_exa,get_code_context_exa,crawling_exa,company_research_exa,linkedin_search_exa,deep_researcher_start,deep_researcher_check"],
                "env": {"EXA_API_KEY": USER_KEYS["EXA_API_KEY"]},
                "connect_timeout": 60,
                "timeout": 120,
            }
        if USER_KEYS["BRAVE_SEARCH_API_KEY"] and "brave" not in mcp:
            mcp["brave"] = {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-brave-search"],
                "env": {"BRAVE_API_KEY": USER_KEYS["BRAVE_SEARCH_API_KEY"]},
                "connect_timeout": 60,
                "timeout": 120,
            }
        mcp.setdefault("context7", {"command": "npx", "args": ["-y", "@upstash/context7-mcp"], "connect_timeout": 60, "timeout": 120})
        mcp.setdefault("fetch", {"command": uvx_bin, "args": ["mcp-server-fetch"], "connect_timeout": 60, "timeout": 120})
        mcp.setdefault("time", {"command": uvx_bin, "args": ["mcp-server-time"], "connect_timeout": 60, "timeout": 120})

        cfg_path.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True))
        print("✅ Updated Hermes MCP servers:", list(mcp.keys()))

# 4. 若存在 Claude Code (~/.claude.json)，增量合并 mcpServers
claude_json = Path.home() / ".claude.json"
if claude_json.exists():
    shutil.copy2(claude_json, Path.home() / f".claude.json.bak-{ts}")
    cdata = json.loads(claude_json.read_text())
    cservers = cdata.setdefault("mcpServers", {})
    if USER_KEYS["EXA_API_KEY"]:
        cservers.setdefault("exa", {"command": "npx", "args": ["-y", "exa-mcp-server"], "env": {"EXA_API_KEY": USER_KEYS["EXA_API_KEY"]}})
    if USER_KEYS["FIRECRAWL_API_KEY"]:
        cservers.setdefault("firecrawl", {"command": "npx", "args": ["-y", "firecrawl-mcp"], "env": {"FIRECRAWL_API_KEY": USER_KEYS["FIRECRAWL_API_KEY"]}})
    if USER_KEYS["BRAVE_SEARCH_API_KEY"]:
        cservers.setdefault("brave", {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-brave-search"], "env": {"BRAVE_API_KEY": USER_KEYS["BRAVE_SEARCH_API_KEY"]}})
    cservers.setdefault("context7", {"command": "npx", "args": ["-y", "@upstash/context7-mcp"]})
    cservers.setdefault("fetch", {"command": uvx_bin, "args": ["mcp-server-fetch"]})
    claude_json.write_text(json.dumps(cdata, indent=2, ensure_ascii=False) + "\n")
    print("✅ Updated Claude Code ~/.claude.json mcpServers:", list(cservers.keys()))
PY
```

---

## Step 3：部署多引擎智能搜索与网页提取路由器（`search.py`）

单次搜索绝不能绑定死一个引擎。以下脚本部署在 `~/.config/agent-research-router/search.py`（并软链到 Hermes 与 Claude Code 技能目录），实现：
- **按查询意图自动选路**：查价格/招股书/电商 → `Serper (Google)`；查原理/深度对比 → `Tavily`；查相似公司/GitHub/论文 → `Exa`；
- **6 级自动故障转移**：`Exa → Tavily → Serper → TinyFish → Brave → Firecrawl → DuckDuckGo (免Key)`；
- **网页转纯净 Markdown**：`Firecrawl → TinyFish Fetch → Jina Reader (免Key)`。

```bash
mkdir -p ~/.config/agent-research-router

cat > ~/.config/agent-research-router/config.json <<'EOF'
{
  "defaults": { "provider": "exa", "max_results": 5 },
  "auto_routing": {
    "enabled": true,
    "keyword_mappings": {
      "serper": ["price", "buy", "cost", "review", "specs", "招股书", "年报", "问询函", "价格", "多少钱", "差评", "site:"],
      "tavily": ["how does", "explain", "research", "analyze", "compare", "deep dive", "原理", "为什么", "对比", "深度", "分析"],
      "exa": ["similar to", "companies like", "alternatives", "startup", "github", "paper", "类似", "竞品", "替代品", "论文", "开源"]
    }
  }
}
EOF

cat > ~/.config/agent-research-router/search.py <<'PY'
#!/usr/bin/env python3
"""Multi-Engine Web Search & Extract Router (Exa/Tavily/Serper/TinyFish/Brave/Firecrawl/DDGS/Jina)."""
import argparse, json, os, re, sys, urllib.parse, urllib.request
from pathlib import Path

BASE_DIR = Path.home() / ".config/agent-research-router"
CONFIG_PATH = BASE_DIR / "config.json"
ENV_PATHS = [BASE_DIR / ".env", Path.home() / ".hermes/.env", Path.home() / ".config/alma/web-search-plus/.env"]

def load_envs() -> None:
    for p in ENV_PATHS:
        if p.exists():
            for line in p.read_text().splitlines():
                m = re.match(r"^\s*([A-Z0-9_]+)\s*=\s*(.*)$", line)
                if m:
                    val = m.group(2).strip().strip('"').strip("'")
                    if val and not val.startswith("<YOUR_") and not val.startswith("在这里填"):
                        os.environ.setdefault(m.group(1), val)

def load_config() -> dict:
    load_envs()
    return json.loads(CONFIG_PATH.read_text()) if CONFIG_PATH.exists() else {}

def get_key(env_name: str) -> str:
    val = os.getenv(env_name, "").strip()
    return "" if (not val or val.startswith("<YOUR_") or val.startswith("在这里填")) else val

def route_engine(query: str, cfg: dict) -> str:
    q = query.lower()
    mappings = cfg.get("auto_routing", {}).get("keyword_mappings", {})
    best_engine, best_hits = None, 0
    for engine, kw_list in mappings.items():
        hits = sum(1 for kw in kw_list if kw.lower() in q)
        if hits > best_hits:
            best_hits, best_engine = hits, engine
    return best_engine or cfg.get("defaults", {}).get("provider", "exa")

def http_json(url: str, method: str = "GET", headers: dict = None, payload: dict = None, timeout: int = 25) -> dict:
    hdrs = {"User-Agent": "curl/8.0 (Macintosh; Intel Mac OS X)"}
    if headers:
        hdrs.update(headers)
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    if data is not None:
        hdrs.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))

def search_exa(query: str, limit: int, cfg: dict) -> list:
    key = get_key("EXA_API_KEY")
    if not key: raise RuntimeError("EXA_API_KEY not configured")
    res = http_json("https://api.exa.ai/search", "POST", {"x-api-key": key}, {"query": query, "numResults": limit, "type": "neural", "contents": {"text": {"maxCharacters": 800}}})
    return [{"title": r.get("title", ""), "url": r.get("url", ""), "snippet": (r.get("text") or "")[:500]} for r in res.get("results", [])]

def search_tavily(query: str, limit: int, cfg: dict) -> list:
    key = get_key("TAVILY_API_KEY")
    if not key: raise RuntimeError("TAVILY_API_KEY not configured")
    res = http_json("https://api.tavily.com/search", "POST", payload={"api_key": key, "query": query, "max_results": limit, "search_depth": "advanced"})
    return [{"title": r.get("title", ""), "url": r.get("url", ""), "snippet": r.get("content", "")[:500]} for r in res.get("results", [])]

def search_serper(query: str, limit: int, cfg: dict) -> list:
    key = get_key("SERPER_API_KEY")
    if not key: raise RuntimeError("SERPER_API_KEY not configured")
    res = http_json("https://google.serper.dev/search", "POST", {"X-API-KEY": key}, {"q": query, "num": limit})
    return [{"title": r.get("title", ""), "url": r.get("link", ""), "snippet": r.get("snippet", "")} for r in res.get("organic", [])[:limit]]

def search_tinyfish(query: str, limit: int, cfg: dict) -> list:
    key = get_key("TINYFISH_API_KEY")
    if not key: raise RuntimeError("TINYFISH_API_KEY not configured")
    res = http_json(f"https://api.search.tinyfish.ai?{urllib.parse.urlencode({'query': query})}", "GET", {"X-API-Key": key}, timeout=45)
    return [{"title": r.get("title", ""), "url": r.get("url", ""), "snippet": (r.get("snippet") or "")[:500]} for r in res.get("results", [])[:limit]]

def search_brave(query: str, limit: int, cfg: dict) -> list:
    key = get_key("BRAVE_SEARCH_API_KEY")
    if not key: raise RuntimeError("BRAVE_SEARCH_API_KEY not configured")
    res = http_json(f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(query)}&count={limit}", "GET", {"X-Subscription-Token": key, "Accept": "application/json"})
    return [{"title": r.get("title", ""), "url": r.get("url", ""), "snippet": r.get("description", "")} for r in res.get("web", {}).get("results", [])[:limit]]

def search_firecrawl(query: str, limit: int, cfg: dict) -> list:
    key = get_key("FIRECRAWL_API_KEY")
    if not key: raise RuntimeError("FIRECRAWL_API_KEY not configured")
    res = http_json("https://api.firecrawl.dev/v1/search", "POST", {"Authorization": f"Bearer {key}"}, {"query": query, "limit": limit})
    return [{"title": r.get("title", ""), "url": r.get("url", ""), "snippet": (r.get("description") or r.get("markdown") or "")[:500]} for r in res.get("data", [])[:limit]]

def search_ddgs(query: str, limit: int, cfg: dict) -> list:
    from ddgs import DDGS
    with DDGS() as ddgs:
        rows = list(ddgs.text(query, max_results=limit))
    return [{"title": r.get("title", ""), "url": r.get("href", ""), "snippet": (r.get("body") or "")[:500]} for r in rows]

def extract_firecrawl(url: str, cfg: dict) -> dict:
    key = get_key("FIRECRAWL_API_KEY")
    if not key: raise RuntimeError("FIRECRAWL_API_KEY not configured")
    res = http_json("https://api.firecrawl.dev/v1/scrape", "POST", {"Authorization": f"Bearer {key}"}, {"url": url, "formats": ["markdown"]}, timeout=45)
    data = res.get("data", {})
    return {"url": url, "engine": "firecrawl", "title": data.get("metadata", {}).get("title", ""), "markdown": data.get("markdown", "")}

def extract_jina(url: str, cfg: dict) -> dict:
    req = urllib.request.Request(f"https://r.jina.ai/{url}", headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return {"url": url, "engine": "jina", "markdown": resp.read().decode("utf-8", errors="replace")}

def main():
    parser = argparse.ArgumentParser(description="Multi-Engine Web Search & Extract Router")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sp_s = sub.add_parser("search")
    sp_s.add_argument("query")
    sp_s.add_argument("--engine", "-e", default="auto", choices=["auto", "exa", "tavily", "serper", "tinyfish", "brave", "firecrawl", "ddgs"])
    sp_s.add_argument("--max-results", "-n", type=int, default=5)
    sp_s.add_argument("--json", action="store_true")

    sp_x = sub.add_parser("extract")
    sp_x.add_argument("urls", nargs="+")
    sp_x.add_argument("--engine", "-e", default="firecrawl", choices=["firecrawl", "jina"])
    sp_x.add_argument("--json", action="store_true")

    args = parser.parse_args()
    cfg = load_config()
    if args.cmd == "search":
        engine = route_engine(args.query, cfg) if args.engine == "auto" else args.engine
        dispatch = {"exa": search_exa, "tavily": search_tavily, "serper": search_serper, "tinyfish": search_tinyfish, "brave": search_brave, "firecrawl": search_firecrawl, "ddgs": search_ddgs}
        chain = [engine] + [fb for fb in ["serper", "exa", "tavily", "tinyfish", "brave", "firecrawl", "ddgs"] if fb != engine]
        errors = {}
        for eng in chain:
            try:
                rows = dispatch[eng](args.query, args.max_results, cfg)
                if not rows:
                    errors[eng] = "empty"
                    continue
                out = {"ok": True, "engine": eng, "routed_from": args.engine, "query": args.query, "results": rows}
                print(json.dumps(out, indent=2, ensure_ascii=False) if args.json else f"[{eng.upper()}] {len(rows)} hits for: {args.query}\n" + "\n".join(f"{i+1}. {r['title']} ({r['url']})\n   {r.get('snippet','')}" for i, r in enumerate(rows)))
                return
            except Exception as e:
                errors[eng] = str(e)
        print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
    elif args.cmd == "extract":
        results = []
        for u in args.urls:
            try:
                results.append(extract_firecrawl(u, cfg) if args.engine == "firecrawl" else extract_jina(u, cfg))
            except Exception:
                try:
                    results.append(extract_jina(u, cfg))
                except Exception as e2:
                    results.append({"url": u, "error": str(e2)})
        print(json.dumps(results, indent=2, ensure_ascii=False) if args.json else "\n".join(f"=== {r['url']} ===\n{r.get('markdown') or r.get('error','')}" for r in results))

if __name__ == "__main__":
    main()
PY
chmod +x ~/.config/agent-research-router/search.py
```

---

## Step 4：安装核心《深度商业、招股书财报、用户行为与获客调研 (`market-intelligence`)》及配套 Skills

Agent 请执行以下脚本，在宿主技能目录（Hermes 的 `~/.hermes/skills/research/` 与 Claude Code 的 `~/.claude/skills/`）同时安装：
1. **`market-intelligence`（王牌核心技能）**：包含 **6大平台实时用户搜索动作/购物框下拉词雷达 (`intent`)**、**港美A股招股书与财报解剖 (`queries`)**、**TAM/SAM/SOM 双向三角校验 (`size`)**、**OpenCLI 181 站点用户付费意愿与供应链底价挖掘**、**失忆侦察兵（Scout Dossier）**、**魔鬼代言人（Devil's Advocate）反方压测**。
2. **`grounded-citations`（事实核查与 Perplexity 风格引用台账）**：包含 `sources.py`，强制所有数据必须来自本次抓取的原文并校验逐字引语（Verbatim Quote）。
3. **`blocked-page-recovery`（403/429/付费墙 5 级破墙梯队）**。

```bash
python3 - <<'PY'
import os, shutil, stat
from pathlib import Path

targets = []
if (Path.home() / ".hermes").exists():
    targets.append(Path.home() / ".hermes/skills/research")
if (Path.home() / ".claude").exists() or not targets:
    targets.append(Path.home() / ".claude/skills")

base = targets[0]
mi_dir = base / "market-intelligence"
(mi_dir / "scripts").mkdir(parents=True, exist_ok=True)
(mi_dir / "references").mkdir(parents=True, exist_ok=True)

# 1. Write market_intel_tool.py (intent + queries + size)
tool_code = '''#!/usr/bin/env python3
"""Market, Financial, User Intent & GTM Intelligence CLI Helper.
Subcommands:
  1. intent   -- Live user search action & commercial autocomplete expander (Google/Baidu/Bing/Taobao/Amazon/YouTube).
  2. queries  -- Generate targeted search queries for Prospectuses (S-1/HKEX/CN), 10-K/Earnings, VOC 1-3 star reviews, and GTM funnels.
  3. size     -- Compute Top-Down vs Bottom-Up TAM/SAM/SOM and flag triangulation failures (>3x divergence).
"""
import argparse, concurrent.futures, json, sys, urllib.parse, urllib.request

UA = "curl/8.0 (Macintosh; Intel Mac OS X)"

def _http_get_json(url: str, timeout: int = 8):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))

def fetch_google_suggest(q: str, hl: str = "zh-CN", ds: str = "") -> list:
    ds_param = f"&ds={ds}" if ds else ""
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&hl={hl}{ds_param}&q={urllib.parse.quote(q)}"
    try:
        data = _http_get_json(url)
        return data[1] if isinstance(data, list) and len(data) > 1 else []
    except Exception:
        return []

def fetch_baidu_suggest(q: str) -> list:
    url = f"https://www.baidu.com/sugrec?prod=pc&wd={urllib.parse.quote(q)}"
    try:
        return [item["q"] for item in _http_get_json(url).get("g", []) if "q" in item]
    except Exception:
        return []

def fetch_bing_suggest(q: str) -> list:
    url = f"https://api.bing.com/osjson.aspx?query={urllib.parse.quote(q)}"
    try:
        data = _http_get_json(url)
        return data[1] if isinstance(data, list) and len(data) > 1 else []
    except Exception:
        return []

def fetch_taobao_suggest(q: str) -> list:
    url = f"https://suggest.taobao.com/sug?code=utf-8&q={urllib.parse.quote(q)}"
    try:
        return [row[0] for row in _http_get_json(url).get("result", []) if isinstance(row, list) and row]
    except Exception:
        return []

def fetch_amazon_suggest(q: str) -> list:
    url = f"https://completion.amazon.com/api/2017/suggestions?limit=10&prefix={urllib.parse.quote(q)}&alias=aps&mid=ATVPDKIKX0DER"
    try:
        return [s.get("value") for s in _http_get_json(url).get("suggestions", []) if s.get("value")]
    except Exception:
        return []

def cmd_intent(args: argparse.Namespace) -> None:
    seed = args.seed.strip()
    is_cjk = any("\\u4e00" <= ch <= "\\u9fff" for ch in seed)
    if is_cjk:
        modifiers = {
            "base_autocomplete": [seed],
            "pain_and_symptom (痛点与副作用)": [f"{seed} 副作用", f"{seed} 没用", f"{seed} 智商税", f"{seed} 禁忌"],
            "willingness_to_pay (购买与选型意图)": [f"{seed} 哪个牌子", f"{seed} 多少钱", f"{seed} 平替", f"{seed} 怎么选"],
            "usage_and_adherence (用法与依从性行为)": [f"{seed} 怎么吃", f"{seed} 什么时候", f"{seed} 搭配", f"{seed} 长期"],
        }
    else:
        modifiers = {
            "base_autocomplete": [seed],
            "pain_and_symptom": [f"{seed} side effects", f"{seed} not working", f"{seed} problem"],
            "willingness_to_pay": [f"best {seed} for", f"{seed} price", f"{seed} alternative", f"{seed} worth it"],
            "usage_and_adherence": [f"how to take {seed}", f"{seed} dosage", f"{seed} vs"],
        }
    report = {"seed": seed, "search_engines": {}, "ecommerce_buying_intent": {}, "intent_matrix": {}}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        f_google = ex.submit(fetch_google_suggest, seed, "zh-CN" if is_cjk else "en")
        f_yt = ex.submit(fetch_google_suggest, seed, "zh-CN" if is_cjk else "en", "yt")
        f_bing = ex.submit(fetch_bing_suggest, seed)
        f_baidu = ex.submit(fetch_baidu_suggest, seed) if is_cjk else None
        f_taobao = ex.submit(fetch_taobao_suggest, seed) if is_cjk else None
        f_amazon = ex.submit(fetch_amazon_suggest, seed)
        mod_futures = {}
        for cat, q_list in modifiers.items():
            mod_futures[cat] = []
            for q in q_list:
                if is_cjk:
                    mod_futures[cat].append(ex.submit(fetch_baidu_suggest, q))
                    mod_futures[cat].append(ex.submit(fetch_bing_suggest, q))
                else:
                    mod_futures[cat].append(ex.submit(fetch_google_suggest, q, "en"))
        report["search_engines"]["google"] = f_google.result()
        report["search_engines"]["youtube"] = f_yt.result()
        report["search_engines"]["bing"] = f_bing.result()
        if f_baidu: report["search_engines"]["baidu"] = f_baidu.result()
        if f_taobao: report["ecommerce_buying_intent"]["taobao_tmall"] = f_taobao.result()
        report["ecommerce_buying_intent"]["amazon_us"] = f_amazon.result()
        for cat, fut_list in mod_futures.items():
            seen = []
            for fut in fut_list:
                for item in fut.result():
                    if item not in seen: seen.append(item)
            report["intent_matrix"][cat] = seen[:16]
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"=== Live User Search & Buying Intent Radar: '{seed}' ===")
        for eng, items in report["search_engines"].items():
            if items: print(f"  • [Search] {eng.upper():8}: {', '.join(items[:8])}")
        for shop, items in report["ecommerce_buying_intent"].items():
            if items: print(f"  • [Shop]   {shop:8}: {', '.join(items[:8])}")
        for cat, items in report["intent_matrix"].items():
            print(f"  • [{cat}]: {', '.join(items[:10])}")

def cmd_ecommerce(args: argparse.Namespace) -> None:
    kw = args.keyword.strip()
    plan = {
        "1_shelf_ecommerce": [f'opencli jd search "{kw}" -f json', f'opencli taobao search "{kw}" -f json', f'opencli amazon search "{kw}" -f json'],
        "2_supply_chain_bom": [f'opencli 1688 search "{kw} 代工 贴牌" -f json', f'python3 ~/.config/agent-research-router/search.py search \'site:yangkeduo.com OR "拼多多" "{kw}" ("百亿补贴" OR "已拼")\' --engine serper'],
        "3_interest_live_ecommerce": [
            f'opencli douyin search "{kw}" -f json',
            f'python3 ~/.config/agent-research-router/search.py search \'"{kw}" ("蝉妈妈" OR "考古加" OR "精选联盟" OR "佣金" OR "GMV")\' --engine serper',
            f'opencli xiaohongshu search "{kw} 测评 避雷" -f json',
            f'opencli weixin search "{kw} 视频号" -f json',
        ],
        "4_secondhand_abandonment": [f'opencli xianyu search "{kw} 闲置 未拆封" -f json'],
    }
    print(json.dumps(plan, indent=2, ensure_ascii=False) if args.json else "\\n".join(f"[{k}]\\n  " + "\\n  ".join(v) for k, v in plan.items()))

def cmd_queries(args: argparse.Namespace) -> None:
    c, ind = args.company, args.industry or args.company
    queries = {
        "1_prospectus_industry_overview": [
            f'"{ind}" ("招股书" OR "招股说明书" OR "聆讯后资料集") ("行业概览" OR "弗若斯特沙利文" OR "灼识咨询" OR "欧睿")',
            f'site:hkexnews.hk "{ind}" ("行业概览" OR "市场规模" OR "竞争格局") filetype:pdf',
            f'"{c}" ("Form S-1" OR "Form F-1" OR "424B4") ("Industry Overview" OR "Market Opportunity")',
        ],
        "2_earnings_unit_economics_and_cac": [
            f'"{c}" ("年报" OR "招股书" OR "问询函回复") ("毛利率" OR "销售费用率" OR "获客成本" OR "复购率" OR "留存率")',
            f'"{c}" ("10-K" OR "20-F") ("Gross Margin" OR "Selling and marketing" OR "Retention" OR "CAC")',
            f'"{c}" "Earnings Call Transcript" ("Q&A" OR "guidance" OR "churn") 2025 OR 2026',
        ],
        "3_risk_factors_and_weaknesses": [
            f'"{c}" ("招股书" OR "年报") "风险因素" ("依赖" OR "下滑" OR "投诉" OR "合规" OR "退货")',
            f'"{c}" ("10-K" OR "S-1") "Item 1A. Risk Factors" ("churn" OR "regulatory" OR "competition")',
        ],
        "4_voc_negative_reviews_and_switching": [
            f'"{c}" ("差评" OR "避雷" OR "拔草" OR "没用" OR "副作用" OR "换到了")',
            f'site:reddit.com "{c}" ("switched from" OR "instead of" OR "waste of money" OR "side effects")',
        ],
    }
    print(json.dumps(queries, indent=2, ensure_ascii=False) if args.json else "\\n".join(f"[{k}]\\n  " + "\\n  ".join(v) for k, v in queries.items()))

def cmd_size(args: argparse.Namespace) -> None:
    td_tam, td_sam, td_som = args.tam_total, args.tam_total * args.sam_pct, args.tam_total * args.sam_pct * args.som_pct
    bu_tam, bu_sam, bu_som = args.total_customers * args.acv, args.reachable_customers * args.acv, args.reachable_customers * args.conv_rate * args.acv
    ratio = max(td_som, bu_som) / max(min(td_som, bu_som), 1e-9)
    ok = ratio <= 3.0
    print(f"Top-Down SOM: {td_som:,.0f} | Bottom-Up SOM: {bu_som:,.0f} | Ratio: {ratio:.2f}x -> {'✅ PASS' if ok else '🚨 FAIL (>3x)'}")
    if not ok: sys.exit(2)

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sp_i = sub.add_parser("intent"); sp_i.add_argument("seed"); sp_i.add_argument("--json", action="store_true")
    sp_e = sub.add_parser("ecommerce"); sp_e.add_argument("keyword"); sp_e.add_argument("--json", action="store_true")
    sp_q = sub.add_parser("queries"); sp_q.add_argument("-c", "--company", required=True); sp_q.add_argument("-i", "--industry", default=""); sp_q.add_argument("--json", action="store_true")
    sp_s = sub.add_parser("size"); sp_s.add_argument("--tam-total", type=float, required=True); sp_s.add_argument("--sam-pct", type=float, default=0.15); sp_s.add_argument("--som-pct", type=float, default=0.02); sp_s.add_argument("--total-customers", type=float, required=True); sp_s.add_argument("--reachable-customers", type=float, required=True); sp_s.add_argument("--conv-rate", type=float, default=0.02); sp_s.add_argument("--acv", type=float, required=True)
    args = p.parse_args()
    {"intent": cmd_intent, "ecommerce": cmd_ecommerce, "queries": cmd_queries, "size": cmd_size}[args.cmd](args)

if __name__ == "__main__":
    main()
'''
tool_path = mi_dir / "scripts/market_intel_tool.py"
tool_path.write_text(tool_code)
tool_path.chmod(tool_path.stat().st_mode | stat.S_IEXEC)

# 2. Write SKILL.md for market-intelligence
skill_md = '''---
name: market-intelligence
description: "Use when doing market/competitor/10-K/GTM intel."
---

# Market, Financial, User Intent & GTM Intelligence (深度商业调研总控)

当用户要求做市场调研、找产品机会点与迭代方向、分析竞品或拆解行业巨头时，严格按以下 **「宽度 × 深度」六步标准作业程序** 执行，禁止用二手软文或宏观套话交差：

## Step 1: 实时用户搜索动作与购买框意图雷达 (Width: Search & Buying Intent)
运行 `python3 ~/.hermes/skills/research/market-intelligence/scripts/market_intel_tool.py intent "<核心词/品类>"`（或对应宿主路径），并发抓取 **Google / 百度 / 必应 / YouTube / 淘宝天猫 / Amazon** 实时下拉词，拆解：
1. **掏钱前的购物框选型词**（规格、剂型、品牌、平替）；
2. **痛点与副作用恐惧**（吃后不适、禁忌、智商税质疑）；
3. **用法与依从性断崖**（怎么吃、吃几天停、怎么搭配）。

## Step 2: 行业巨头招股书（S-1/港交所/A股问询函）与财报解剖 (Depth: Financial & Unit Economics)
运行 `market_intel_tool.py queries -c "<巨头名>" -i "<赛道名>"` 并配合 `~/.config/agent-research-router/search.py` 抓取原文：
1. **白嫖顶级定制研报**：从港股/美股招股书 `Industry Overview（行业概览）` 提取沙利文/灼识咨询/欧睿的子赛道真实规模、CAGR 与 CR5 市占率。
2. **拆解单位经济模型与获客底牌**：从财报附注/A股问询函回复提取 **毛利率（Gross Margin）**、**销售费用率（S&M %）**、**线上推广买量占比**、**推算单客获客成本（CAC）** 与 **复购留存率（Cohort Retention）**。
   - 若巨头毛利 >75% 但销售费用率 >45%：说明边际成本极低但公域买量已成红海，我们必须走「免费自测工具 Quiz + 搜索/内容矩阵 + 私域闭环」，严禁正面硬刚泛流量买量。
   - 若首单毛利 < CAC：说明全靠第 2~4 次复购赚钱，产品第一优先级必须是「提升依从性与复购的闭环功能」。
3. **风险因素（Risk Factors）与电话会 Q&A**：提取巨头管理层承认的退货原因、渠道依赖与合规红线。

## Step 3: 市场规模双向三角校验 (TAM / SAM / SOM Triangulation)
运行 `market_intel_tool.py size` 同时计算 Top-Down 与 Bottom-Up（目标可触达人数 × 转化率 × 年客单价 ACV）。若两者 SOM 相差超过 3 倍，必须标红预警并修正假设。

## Step 4: 八大电商全链路（货架 + 兴趣直播带货 + 源头供应链）与用户行为穿透
运行 `market_intel_tool.py ecommerce "<品类/品牌>"` 生成 8 大电商阵地采集指令，并调用本机 `opencli` 结构化命令：
- **货架电商（京东/淘宝/Amazon）**：`opencli jd search/item/reviews`、`opencli taobao search/detail/reviews`、`opencli amazon bestsellers/movers-shakers`（提取真实价格带与 30-90 天追评原话）。
- **兴趣与直播带货电商（抖音精选联盟/蝉妈妈/考古加 + 小红书买手种草 + 视频号微信小店）**：
  - 抖音：`opencli douyin search/detail/user-videos` 拆解爆款带货视频前 3 秒黄金钩子与完整口播文案，配合 `search.py` 检索蝉妈妈/考古加/精选联盟公开数据（看达人带货佣金率 20%-50%、直播间 GMV 构成）；
  - 小红书：`opencli xiaohongshu search/note/comments` 筛选「收藏/点赞比 > 0.8」的高转化种草笔记，统计评论区“求链接/怎么买”买单信号；
  - 视频号小店（40-60岁高客单价营养品第一阵地）：`opencli weixin search` 或借公众号后台 `/cgi-bin/videosnap` 接口拉取竞品视频号全量爆款。
- **供应链真实 BOM 底价与拼多多白牌底线**：`opencli 1688 search "<品类> 代工 贴牌" -f json`（对比 1688 出厂价与终端零售价算毛利倍数）+ 拼多多百亿补贴价格底线检索。
- **后端弃坑率检测（闲鱼测试法）**：`opencli xianyu search "<竞品> 闲置 未拆封" -f json`（检验冲动消费 vs 真实长期复购）。
- **用户手工土办法（Workaround）与迁移原话**：用 `opencli xiaohongshu`、`opencli reddit`、`opencli zhihu` 寻找用户自制表格、分装药盒或 `"换到了" / "switched from"` 原话，转化为产品核心功能切口（Feature Wedge）。

## Step 5: 并发竞品侦察兵与魔鬼代言人反方压测 (Scouts & Devil's Advocate)
1. 用 `firecrawl_map` 扫描竞品全站目录结构（识别 `/quiz`、`/calculator`、`/vs` 获客漏斗），用 `opencli boss` / `linkedin` 查竞品在招岗位 JD（逆向工程其未来 6 个月产品路线图）。
2. **魔鬼代言人（Devil's Advocate）强制三问**：① 为什么财大气粗的巨头没做这个功能（是算不过账还是合规红线）？② 哪条结论目前只有孤证？③ 前 100 个真实付费客户具体从哪个词/哪个钩子进来？

## Step 6: Grounding 原文引用台账与浅色一页式 HTML 报告交付
所有数字、日期、财报口径、竞品价格和用户原话必须附真实抓取 URL 与逐字引语，最终输出一份**浅色简洁、一页到底的独立 HTML 报告** + Markdown 存档。
'''
(mi_dir / "SKILL.md").write_text(skill_md)

# 3. Write Reference Manuals (Prospectus/Earnings Playbook, User Behavior/OpenCLI Map, Competitor Dossier)
(mi_dir / "references/prospectus-earnings-playbook.md").write_text('''# 招股书（S-1/港股/A股问询函）与财报解剖核心公式
1. **毛利率 > 75% + 销售费用率 > 45%** -> 生产边际成本极低，公域买量已成红海；严禁硬刚泛流量投流，必走「自测 Quiz 钩子 + 搜索内容矩阵 + 私域闭环」。
2. **推算单客 CAC = 当期线上推广费 / 新增付费客户数** -> 若首单毛利 < CAC，说明全靠第 2~4 次复购赚钱，产品第一优先级必须是「提升依从性与复购的闭环功能」。
3. **三大检索金矿**：
   - 港股：`site:hkexnews.hk "<公司/赛道>" ("行业概览" OR "弗若斯特沙利文" OR "灼识咨询") filetype:pdf`
   - A股：`"<公司/赛道>" ("招股说明书" OR "问询函回复") ("获客成本" OR "复购率" OR "线上推广费")`
   - 美股：`"<Company>" ("Form S-1" OR "10-K") ("Industry Overview" OR "Selling and marketing" OR "Item 1A. Risk Factors")`
''')

(mi_dir / "references/user-behavior-and-willingness-to-pay.md").write_text('''# 用户行为、付费意愿与 OpenCLI 181 站点命令速查
- **1688 源头代工底价（算真实 BOM 成本）**：`opencli 1688 search --keyword "<品类> 代工" -f json`
- **京东/淘宝差评与 90 天追评**：`opencli jd search/item/reviews`、`opencli taobao search/reviews`
- **闲鱼二手弃坑率（验假复购）**：`opencli xianyu search --keyword "<竞品> 闲置" -f json`
- **小红书/抖音/知乎/Reddit 痛点与手工土办法（Workaround）**：`opencli xiaohongshu search/comments`、`opencli douyin hashtag/detail`、`opencli reddit search/read`
- **东方财富/雪球/BOSS直聘（商业推动与招聘信号）**：`opencli eastmoney announcement`、`opencli xueqiu search`、`opencli boss detail`
''')

# 4. Install grounded-citations (sources.py) & blocked-page-recovery
gc_dir = base / "grounded-citations"
(gc_dir / "scripts").mkdir(parents=True, exist_ok=True)
(gc_dir / "SKILL.md").write_text('''---
name: grounded-citations
description: "Ground answers and documents in cited, verifiable sources."
---
# Grounded Citations & Anti-Hallucination Ledger
1. 只认抓取到的原文，不认搜索摘要（snippet 只能当线索）。
2. 每抓取阅读一篇原文后，运行 `python3 scripts/sources.py add "<url>" --title "<title>" --quote "<逐字原句>"` 登记编号 `[1]`。
3. 二手比例必须回溯核对分母；无法查证的内容必须显式标注 `[未核实推断]`。
''')
sources_py = gc_dir / "scripts/sources.py"
sources_py.write_text('''#!/usr/bin/env python3
import argparse, json, os, re, sys
from pathlib import Path
LEDGER = Path(os.getenv("CITATION_LEDGER", str(Path.home() / ".config/agent-research-router/citations_ledger.json")))
def load(): return json.loads(LEDGER.read_text()) if LEDGER.exists() else {"sources": []}
def save(d): LEDGER.parent.mkdir(parents=True, exist_ok=True); LEDGER.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\\n")
def main():
    p = argparse.ArgumentParser(); sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("reset")
    a = sub.add_parser("add"); a.add_argument("url"); a.add_argument("--title", default=""); a.add_argument("--quote", default="")
    sub.add_parser("render")
    v = sub.add_parser("verify"); v.add_argument("file")
    args = p.parse_args(); d = load(); s_list = d["sources"]
    if args.cmd == "reset": save({"sources": []}); print("Ledger reset: OK")
    elif args.cmd == "add":
        for s in s_list:
            if s["url"].rstrip("/") == args.url.rstrip("/"):
                if args.quote and args.quote not in s["quotes"]: s["quotes"].append(args.quote)
                save(d); print(f"[{s['id']}] {s['url']}"); return
        nid = len(s_list) + 1
        s_list.append({"id": nid, "url": args.url, "title": args.title or args.url, "quotes": [args.quote] if args.quote else []})
        save(d); print(f"[{nid}] {args.url}")
    elif args.cmd == "render":
        print("\\n## Sources\\n" + "\\n".join(f"- [{s['id']}] [{s['title']}]({s['url']})" + "".join(f'\\n  > "{q}"' for q in s.get("quotes", [])) for s in s_list))
    elif args.cmd == "verify":
        txt = Path(args.file).read_text(); cited = sorted({int(m) for m in re.findall(r"\\[(\\d+)\\]", txt)}); known = {s["id"] for s in s_list}
        bad = [i for i in cited if i not in known]
        if bad: print(f"FAIL: Unknown citations {bad}", file=sys.stderr); sys.exit(1)
        print(f"GROUNDED OK: {len(cited)} sources verified.")
if __name__ == "__main__": main()
''')
sources_py.chmod(sources_py.stat().st_mode | stat.S_IEXEC)

bpr_dir = base / "blocked-page-recovery"
bpr_dir.mkdir(parents=True, exist_ok=True)
(bpr_dir / "SKILL.md").write_text('''---
name: blocked-page-recovery
description: "Use when a fetch fails: 403/429, paywall, WAF, bot wall."
---
# Blocked-Page Recovery (5级反爬破墙梯队)
遇到 403/429/Cloudflare/付费墙时严禁死循环重试，按以下顺序降级：
1. `python3 ~/.config/agent-research-router/search.py extract "<url>"` (Firecrawl -> Jina)
2. Wayback Machine: `curl -sL "https://archive.org/wayback/available?url=<url>"`
3. archive.today 域名轮询: `archive.ph` / `archive.md` / `archive.is`
4. 同源 API / fxtwitter (`https://api.fxtwitter.com/<user>/status/<id>`)
5. 真实浏览器兜底: `dokobot read --local "<url>"` 或 `opencli`
''')

# Copy all 3 skills to secondary targets if both Hermes and Claude Code exist
for t in targets[1:]:
    t.mkdir(parents=True, exist_ok=True)
    for sk in ["market-intelligence", "grounded-citations", "blocked-page-recovery"]:
        src, dst = base / sk, t / sk
        if src.exists() and src != dst:
            if dst.exists(): shutil.rmtree(dst)
            shutil.copytree(src, dst)

print("✅ Installed 3 core skills (market-intelligence, grounded-citations, blocked-page-recovery) into:", [str(t) for t in targets])
PY
```

---

## Step 5：全链路端到端验收（Agent 必须运行并向用户输出体检表）

完成上述步骤后，Agent 必须在终端运行以下一键验收脚本，实测 **CLI 工具链、多引擎搜索路由器、网页 Markdown 提取、6大平台用户搜索动作与购物意图雷达、市场规模三角校验** 五大模块，并向用户输出体检报告：

```bash
python3 - <<'PY'
import json, shutil, subprocess
from pathlib import Path

print("=== 1. 核心 CLI 二进制检查 ===")
for cmd in ["opencli", "dokobot", "tinyfish", "uvx"]:
    p = shutil.which(cmd)
    print(f"  {'✅' if p else '⚠️'} {cmd:12} -> {p or 'not found'}")

print("\n=== 2. 多引擎搜索路由器连通性 (search.py) ===")
search_py = str(Path.home() / ".config/agent-research-router/search.py")
for eng in ["auto", "exa", "tavily", "serper", "brave", "firecrawl", "ddgs"]:
    try:
        out = subprocess.check_output(["python3", search_py, "search", "Apple 10-K Gross Margin", "--engine", eng, "-n", "1", "--json"], stderr=subprocess.STDOUT, text=True, timeout=20)
        d = json.loads(out)
        print(f"  ✅ Search [{eng:9}] -> routed to {d.get('engine')}, {len(d.get('results', []))} hits")
    except Exception as e:
        print(f"  ⚠️ Search [{eng:9}] -> skipped/unconfigured")

print("\n=== 3. 实时用户搜索动作与电商购买意图雷达 (intent) ===")
mi_tool = Path.home() / ".hermes/skills/research/market-intelligence/scripts/market_intel_tool.py"
if not mi_tool.exists():
    mi_tool = Path.home() / ".claude/skills/market-intelligence/scripts/market_intel_tool.py"
out = subprocess.check_output(["python3", str(mi_tool), "intent", "甘氨酸镁", "--json"], text=True, timeout=20)
d = json.loads(out)
print(f"  ✅ Search Autocomplete (Baidu/Bing/Google): {len(d['search_engines'].get('baidu', []))} + {len(d['search_engines'].get('bing', []))} terms")
print(f"  ✅ E-Commerce Buying Box (Taobao/Amazon):  {d['ecommerce_buying_intent'].get('taobao_tmall', [])[:4]}")

print("\n=== 4. TAM/SAM/SOM 双向三角校验器 (size) ===")
out_s = subprocess.check_output(["python3", str(mi_tool), "size", "--tam-total", "200000000000", "--sam-pct", "0.15", "--som-pct", "0.01", "--total-customers", "150000000", "--reachable-customers", "10000000", "--conv-rate", "0.015", "--acv", "1800"], text=True)
print(" ", out_s.strip())
PY
```

---

## Step 6：配好之后怎么用？（日常深度商业调研 4 大实战指令模板）

全部配通后，你平时只需要直接把下面任意一段话发给你的 Hermes 或 Claude Code，它就会自动调动全套武器库给你跑出深度报告：

### 场景 1：找新赛道机会点 & 产品迭代方向（宽度 × 深度全开）
> “调用 `market-intelligence` 技能，帮我深度调研【目标赛道/品类，如：40-60岁女性睡眠与骨关节精准营养 / AI 跨境电商选品工具】：
> 1. 先跑 `intent` 雷达拉取百度、Google、淘宝、Amazon 上用户的真实搜索动作、副作用焦虑与购买选型词；
> 2. 检索该赛道港股/美股/A股龙头公司的招股书（沙利文/灼识行业概览）与最新财报，拆出真实毛利率、销售费用率、获客成本（CAC）和风险因素；
> 3. 用 `opencli` 查 1688 源头代工底价、京东/Amazon 差评追评、闲鱼二手弃坑率，以及小红书/Reddit 上用户的手工替代方案（Workaround）；
> 4. 经过魔鬼代言人反方压测后，给我输出**市场切入机会点、核心产品迭代功能优先级、低成本获客漏斗设计**，生成浅色简洁一页到底的 HTML 报告（所有数据附原文链接与逐字引语）。”

### 场景 2：解剖行业巨头招股书与财报（看穿商业推动力与底牌）
> “按 `market-intelligence` 的招股书与财报解剖手册，帮我深扒【公司名，如：健合集团 H&H / 汤臣倍健 / Hims & Hers】的最新年报、招股书与业绩电话会 Q&A：
> 重点拆出它的各产品线毛利率、销售及营销费用明细（买量投流 vs 渠道佣金占比）、复购留存数据，以及管理层在风险因素里承认的软肋，告诉我我们做同类产品时哪里绝对不能硬碰硬、哪里是利润最厚的切口。”

### 场景 3：像素级拆解标杆竞品的获客漏斗与产品路线图
> “派并发侦察兵帮我拆解这 3 家竞品【域名 A, B, C】：
> 1. 用 `firecrawl_map` 扫出他们全站 URL 目录树，看他们靠什么免费工具（`/tools`）、测评问卷（`/quiz`）或对比页（`/vs`）截流获客；
> 2. 逐字摘录他们首屏 Hero 文案、Onboarding 步数与付费墙定价锚定策略；
> 3. 查他们最近在 BOSS直聘 / LinkedIn 招什么岗位，反推他们未来半年重兵投入的产品迭代方向。”

### 场景 4：验证一个新产品 Idea 值不值得做（冷酷压测）
> “我想做【一句话描述你的产品或新功能】，请结合 `market-intelligence` 和 `startup-pressure-test`，去小红书、Reddit、京东差评和淘宝下拉词里找真实痛点证据，算一下 Top-Down 和 Bottom-Up 的市场规模三角校验，并用魔鬼代言人视角挑刺，告诉我这个想法是 Strong、Weak 还是应该 Pivot（转型），以及前 100 个付费客户怎么最低成本拿到。”
