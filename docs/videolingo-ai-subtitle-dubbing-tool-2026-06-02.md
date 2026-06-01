# VideoLingo — 一键 AI 视频字幕、翻译、配音工具（17K Stars）

> 来源：[@yhslgg (老杨啊) on X](https://x.com/yhslgg/status/2061385981870354619)
> 整理时间：2026-06-02
> 来自翡冷翠

---

## 简介

VideoLingo 是一个开源全自动视频翻译本地化工具，GitHub 17,000+ Stars。核心能力：丢一个视频进去，自动完成**语音识别 → 字幕切分 → 翻译 → 本地化 → 配音**全流程，输出质量对标 Netflix 字幕标准。支持 YouTube 直接下载，Windows/macOS/Linux 跨平台，有 Google Colab 云版本。

适合做跨语言视频搬运、海外内容加中文字幕、中文视频出海、知识类内容本地化的内容创作者。

---

## 作者是谁

- **GitHub**: [Huanshere](https://github.com/Huanshere/VideoLingo)
- **X/Twitter**: [@Huanshere](https://twitter.com/Huanshere)
- **官网**: https://videolingo.io
- **邮箱**: team@videolingo.io

---

## 核心功能

### 1. 字幕识别 — WhisperX 词级精准识别
- 使用 WhisperX（large-v3 模型）做词级别对齐识别
- 幻觉率极低，不会出现"乱飘的粗糙字幕"
- 支持 8+ 输入语言：英语、俄语、法语、德语、意大利语、西班牙语、日语、中文
- 对背景音乐复杂的视频可开启人声分离增强

### 2. 高质量翻译 — 三步走管线
Translator 不走"直接扔给 GPT 翻译"这种粗暴路线——而是三步流程：
1. **先翻译**（Translate）— 初版翻译
2. **再反思**（Reflect）— 对翻译进行自我检查
3. **本地化适配**（Adaptation）— 根据目标语言文化习惯进行本地化润色

支持 Claude、GPT、Gemini、DeepSeek、Grok 等多种 LLM 后端，按质量排序推荐。

### 3. Netflix 标准字幕
- **单行字幕原则** — 不会出现一行字塞半篇文章的情况
- NLP + AI 智能切分，严格按 Netflix 字幕规范
- 时间轴精确对齐

### 4. AI 配音 — 多引擎 + 声音克隆
- 支持引擎：GPT-SoVITS、Azure TTS、OpenAI TTS、Fish TTS、Edge TTS、SiliconFlow FishTTS
- 可自定义 TTS（修改 custom_tts.py）
- 支持声音克隆（Cosy2 Voice Clone、GPT-SoVITS 用自己的声音）
- 做了大量语速工程处理，保证配音与原视频节奏对齐

### 5. 完整的工作流控制
- YouTube 视频直接下载（yt-dlp）
- Streamlit Web UI，一键启动
- 详细日志 + 进度断点续传
- 任务控制：暂停/继续/停止任意步骤
- 模型搜索框：API 自动拉取完整模型列表，搜索和过滤

---

## 安装方式

### 方式 A：uv 安装（推荐，无需 Anaconda）

```bash
git clone https://github.com/Huanshere/VideoLingo.git
cd VideoLingo
python setup_env.py          # 自动安装 uv + Python 3.10 + 所有依赖

# 启动
.venv/bin/streamlit run st.py    # macOS / Linux
# 或 Windows: .venv\Scripts\streamlit run st.py
```

### 方式 B：Docker
```bash
docker build -t videolingo .
docker run -d -p 8501:8501 --gpus all videolingo
```

### 方式 C：Google Colab（零安装）
无需本地环境，浏览器直接跑。

---

## 支持的 API

| 服务类型 | 支持选项 |
|---------|---------|
| LLM | Claude, GPT, Gemini, DeepSeek, Grok 等（OpenAI 兼容格式） |
| WhisperX | 本地运行 or 302.ai API |
| TTS | Azure TTS, OpenAI TTS, Fish TTS, GPT-SoVITS, Edge TTS, 自定义 TTS |
| 免费方案 | Ollama（本地 LLM）+ Edge-TTS，完全免费，无需 API Key |

> **提示**: VideoLingo 与 302.ai 合作，一个 API Key 覆盖所有服务（LLM + WhisperX + TTS）。

---

## 当前限制

1. **背景噪音影响** — WhisperX 使用 wav2vec 对齐，背景音乐过大时可能影响识别精度
2. **弱模型易出错** — 弱 LLM 可能因 JSON 格式要求严格而出错（建议使用推荐模型）
3. **配音不完美** — 跨语言语速和语调差异导致配音效果可能不完全 100%
4. **多语言视频只保留主语言** — WhisperX 强制对齐时会删除其他语言
5. **不支持多角色分开配音** — 说话人区分能力还不够可靠

---

## 谁适合用

| 角色 | 场景 |
|------|------|
| 跨语言内容搬运 | 把海外视频搬到国内平台加精翻字幕 |
| 给海外内容加中文字幕 | YouTube/TikTok 内容中文化 |
| 中文视频出海 | 把自己的中文内容翻译成英文/其他语言 |
| 知识类内容本地化 | 教程、课程、技术分享的多语言版本 |
| 编程教学创作者 | 精确翻译技术术语和代码讲解 |

---

## 同类对比

| 特性 | VideoLingo | 直接 GPT 翻译 | 传统字幕工具 |
|------|-----------|-------------|------------|
| 字幕识别 | WhisperX 词级对齐 | — | 粗粒度 |
| 翻译质量 | 三步法（翻译→反思→本地化） | 一次性直译 | 无 AI |
| 字幕格式 | Netflix 标准单行 | 不处理 | 需手动切分 |
| 配音 | 多引擎 + 声音克隆 | — | 无 |
| 安装复杂度 | 一键（uv） | — | 需手动组合工具链 |
| 断点续传 | 支持 | — | 不支持 |
| 免费方案 | Ollama + Edge-TTS | 需付费 API | 免费但手工 |

---

## 快速开始建议

如果是内容创作者，推荐工作流：
1. **macOS 用户**: `brew install ffmpeg` → clone → `python setup_env.py` → 启动
2. **配置 LLM**: 推荐 Claude 或 Gemini 获得最佳翻译质量
3. **配置 TTS**: 先试 Edge-TTS（免费），追求效果上 GPT-SoVITS
4. **处理视频**: Streamlit UI 拖拽即可

---

## 资源链接

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/Huanshere/VideoLingo |
| 官网 | https://videolingo.io |
| 在线体验 | https://videolingo.io/en/login（15 分钟免费试用） |
| 定价 | https://videolingo.io/en/pricing |
| 文档 (中文) | https://github.com/Huanshere/VideoLingo/blob/main/docs/pages/docs/start.zh-CN.md |
| 文档 (English) | https://github.com/Huanshere/VideoLingo/blob/main/docs/pages/docs/start.en-US.md |
| 作者 Twitter | https://twitter.com/Huanshere |

---

## ⚡ 发布者洞察

> @yhslgg 的评价：
> "丢一个视频进去，自动识别语音、切字幕、翻译、配音，全程一键，出来的质量对标 Netflix 字幕标准。"
> "三步走：先翻译、再反思、再本地化适配，比直接扔给 GPT 翻一遍强得多"
> "这个工具能把你的效率直接干到另一个维度。"

VideoLingo 的核心价值在于把原本需要**字幕组团队**（听写 + 翻译 + 校对 + 时间轴 + 配音）才能完成的工作链压缩成了一键流程。对于个人创作者来说，这是以前需要 5 个人才能做到的事情。

---

*来自翡冷翠*
