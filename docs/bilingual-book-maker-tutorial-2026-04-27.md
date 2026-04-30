# bilingual_book_maker - 开源 AI 图书翻译利器

> 来源：[Joruno @wsl8297](https://x.com/wsl8297/status/2048734050064679387)
> GitHub：[yihong0618/bilingual_book_maker](https://github.com/yihong0618/bilingual_book_maker)
> 整理时间：2026-04-27
> 来自翡冷翠

---

## 简介

**bilingual_book_maker** 是一个开源的 AI 图书翻译工具，利用大语言模型（ChatGPT、Claude、Gemini 等）将 epub、txt、srt、pdf 等格式的文件和整本书快速翻译成多语言版本。

**核心亮点：**
- 🚀 支持多种主流 AI 翻译模型（GPT-4、Claude、Gemini、DeepL、Qwen 等）
- 📚 支持 epub、txt、srt、pdf 等常见格式
- 🔄 自动生成双语对照版本
- 📝 采用吴恩达老师的三步翻译法，翻译质量更稳
- 🔧 支持自定义翻译 Prompt 和 API Provider
- 🐳 提供 Docker 支持，一键部署

---

## 内容清单总览

| 章节 | 内容 | 核心要点 |
|------|------|----------|
| 1 | 环境准备 | Python 3.8+、API Key、待翻译文件 |
| 2 | 快速开始 | pip 安装、命令行翻译、测试模式 |
| 3 | 支持的翻译服务 | 15+ 种翻译模型对比 |
| 4 | 高级用法 | 自定义 Prompt、批量翻译、断点续传 |
| 5 | Docker 部署 | 容器化运行指南 |

---

## 详细内容

### 一、环境准备

**前置要求：**

1. **Python 3.8+** 环境
2. **API Key**（根据选择的翻译模型）：
   - OpenAI API Key（GPT-3.5/GPT-4/GPT-4o）
   - Claude API Key
   - Gemini API Key
   - DeepL API Key（付费版）
   - 或 Qwen、Caiyun 等其他服务
3. **待翻译文件**：epub / txt / srt / pdf 格式
4. **网络环境**：需要能访问互联网或代理

**安装方式：**

```bash
# 方式 1：从源码安装
pip install -r requirements.txt

# 方式 2：pip 直接安装（推荐）
pip install -U bbook_maker
```

---

### 二、快速开始

**1. 测试模式（免费预览）**

```bash
# 使用源码
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --test

# 使用 pip 安装的命令
bbook --book_name test_books/animal_farm.epub --openai_key ${openai_key} --test
```

**2. 完整翻译一本书**

```bash
# 基础用法 - 翻译成简体中文
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --language "Simplified Chinese"

# 使用 GPT-4 模型
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --model gpt4

# 使用 Gemini Flash
python3 make_book.py --book_name test_books/animal_farm.epub --gemini_key ${gemini_key} --model gemini
```

**3. 环境变量配置（避免命令行暴露密钥）**

```bash
export OPENAI_API_KEY=sk-xxx
export BBM_CLAUDE_API_KEY=sk-ant-xxx
export BBM_GOOGLE_GEMINI_KEY=xxx

# 然后命令中可以省略 --openai_key 参数
python3 make_book.py --book_name test_books/animal_farm.epub --language zh-hans
```

---

### 三、支持的翻译服务对比

| 模型 | 参数 | 特点 | 适用场景 |
|------|------|------|----------|
| **GPT-3.5-turbo** | `--model chatgptapi` | 速度快、成本低 | 日常翻译、测试 |
| **GPT-4** | `--model gpt4` | 质量高、支持长文本 | 专业书籍、文学作品 |
| **GPT-4o** | `--model gpt4o` | 性价比平衡 | 大多数场景 |
| **Claude** | `--model claude-sonnet-4-20250514` | 翻译质量优秀 | 文学、技术文档 |
| **Gemini Flash** | `--model gemini` | 免费额度高 | 大体积文件 |
| **Gemini Pro** | `--model geminipro` | 质量更高 | 专业翻译 |
| **DeepL** | `--model deepl` | 传统机器翻译标杆 | 欧洲语言 |
| **DeepL Free** | `--model deeplfree` | 免费使用 | 轻量需求 |
| **Qwen-MT** | `--model qwen-mt-turbo/plus` | 阿里翻译专用模型 | 中英日互译 |
| **Google Translate** | `--model google` | 完全免费 | 基础翻译 |
| **Caiyun** | `--model caiyun` | 中文优化 | 中英日互译 |
| **xAI (Grok)** | `--model xai` | 最新大模型 | 尝鲜体验 |
| **Ollama** | `--ollama_model xxx` | 本地部署 | 隐私敏感 |

**多模型对比示例：**

```bash
# Claude 翻译
python3 make_book.py --book_name test_books/animal_farm.epub --model claude --claude_key ${claude_key}

# DeepL 翻译日语
python3 make_book.py --book_name test_books/animal_farm.epub --model deepl --deepl_key ${deepl_key} --language ja

# 通义千问翻译（支持 92 种语言）
python3 make_book.py --book_name test_books/animal_farm.epub --qwen_key ${qwen_key} --model qwen-mt-plus --language "Japanese"

# Google 免费翻译
python3 make_book.py --book_name test_books/animal_farm.epub --model google
```

---

### 四、高级用法

**1. 自定义翻译 Prompt**

```bash
# 简单自定义
python3 make_book.py --book_name test_books/animal_farm.epub --prompt "Translate {text} to {language}."

# 从文件加载 Prompt
python3 make_book.py --book_name test_books/animal_farm.epub --prompt prompt_template_sample.txt

# JSON 格式（含 system 角色）
python3 make_book.py --book_name test_books/animal_farm.epub --prompt '{"user":"Translate {text} to {language}", "system": "You are a professional translator."}'

# PromptDown 格式（推荐）
python3 make_book.py --book_name test_books/animal_farm.epub --prompt prompt_md.prompt.md
```

**吴恩达三步翻译法 Prompt 示例：**

```markdown
# Translation Prompt

## Developer Message
You are a professional translator. Follow these three steps:
1. Translate the text literally
2. Reflect on the translation and identify issues
3. Refine the translation for natural fluency

## Conversation

| Role | Content |
|------|---------|
| User | Please translate the following text into {language}:

{text} |
```

**2. 批量处理与断点续传**

```bash
# 批量翻译（txt 文件每 20 行一批）
python3 make_book.py --book_name test_books/the_little_prince.txt --batch_size 20

# 断点续传（中断后继续）
python3 make_book.py --book_name test_books/animal_farm.epub --model google --resume

# 并行处理（加速 EPUB 翻译，推荐 2-4 线程）
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --parallel-workers 4
```

**3. 自定义 API Provider**

支持任意 OpenAI-compatible API（DeepSeek、SiliconFlow、本地代理等）：

```bash
# 创建配置文件 bbm_providers.json
{
  "providers": {
    "deepseek": {
      "api_style": "openai",
      "base_url": "https://api.deepseek.com/v1",
      "default_models": ["deepseek-chat", "deepseek-reasoner"],
      "env_key": "BBM_DEEPSEEK_API_KEY"
    }
  }
}

# 使用自定义 Provider
python3 make_book.py --provider deepseek --api_key sk-xxx --book_name test_books/animal_farm.epub
```

**4. 标签控制与样式定制**

```bash
# 指定需要翻译的标签（默认只翻译 <p>）
python3 make_book.py --book_name test_books/animal_farm.epub --translate-tags h1,h2,h3,p,div

# 排除特定标签（默认排除 sup,code）
python3 make_book.py --book_name test_books/animal_farm.epub --exclude-translate-tags code,pre

# 翻译所有内容（包括代码块）
python3 make_book.py --book_name test_books/animal_farm.epub --exclude-translate-tags ""

# 自定义双语对照样式
python3 make_book.py --book_name test_books/animal_farm.epub --translation_style "color: #808080; font-style: italic;"
```

**5. 仅输出单语版本**

```bash
# 只输出翻译后的内容，不生成了双语对照
python3 make_book.py --book_name test_books/animal_farm.epub --openai_key ${openai_key} --single_translate
```

---

### 五、Docker 部署

**构建镜像：**

```bash
docker build --tag bilingual_book_maker .
```

**运行容器（Linux）：**

```bash
export folder_path=/home/user/my_books
export book_name=animal_farm.epub
export openai_key=sk-xxx
export language=zh-hans

docker run --rm --name bilingual_book_maker \
  --mount type=bind,source=${folder_path},target='/app/test_books' \
  bilingual_book_maker \
  --book_name "/app/test_books/${book_name}" \
  --openai_key ${openai_key} \
  --language "${language}"
```

**运行容器（Windows PowerShell）：**

```powershell
$folder_path="C:\Users\user\mybook\"
$book_name="animal_farm.epub"
$openai_key="sk-xxx"
$language="zh-hans"

docker run --rm --name bilingual_book_maker 
  --mount type=bind,source=$folder_path,target='/app/test_books' 
  bilingual_book_maker 
  --book_name "/app/test_books/$book_name" 
  --openai_key $openai_key 
  --language $language
```

---

## 资源汇总

### 官方链接
| 名称 | 链接 | 说明 |
|------|------|------|
| GitHub 仓库 | https://github.com/yihong0618/bilingual_book_maker | 源码、文档、Issues |
| 中文 README | https://github.com/yihong0618/bilingual_book_maker/blob/main/README-CN.md | 详细中文文档 |
| Docker 镜像 | 内置 Dockerfile | 一键部署 |

### 相关工具推荐
- **[书译 BookTranslator](https://www.booktranslator.app/)** - 更友好的商业化替代方案

### 值得关注
- **@wsl8297 (Joruno)** - AI 程序员，专注分享高质量 AI 工具教程
- **@yihong0618** - 项目作者，开源贡献者

---

## 快速参考

### 常用命令速查表

```bash
# 快速测试（预览效果）
bbook --book_name book.epub --openai_key sk-xxx --test

# 完整翻译一本书
bbook --book_name book.epub --openai_key sk-xxx --language "Simplified Chinese"

# 使用 GPT-4
bbook --book_name book.epub --openai_key sk-xxx --model gpt4

# 使用 Claude
bbook --book_name book.epub --claude_key sk-ant-xxx --model claude

# 使用 Gemini（免费）
bbook --book_name book.epub --gemini_key xxx --model gemini

# Google 免费翻译
bbook --book_name book.epub --model google

# 并行加速（4线程）
bbook --book_name book.epub --openai_key sk-xxx --parallel-workers 4

# 断点续传
bbook --book_name book.epub --openai_key sk-xxx --resume

# 仅输出翻译（无双语对照）
bbook --book_name book.epub --openai_key sk-xxx --single_translate
```

### 输出文件命名规则

| 输入格式 | 输出文件名 | 说明 |
|----------|----------|------|
| `.epub` | `{原文件名}_bilingual.epub` | 双语 EPUB |
| `.txt` | `{原文件名}_bilingual.txt` | 双语 TXT |
| `.srt` | `{原文件名}_bilingual.srt` | 双语字幕 |
| `.pdf` | `{原文件名}_bilingual.txt` + `_bilingual.epub` | TXT 保底 + EPUB |

**临时文件（中断时生成）：** `{原文件名}_bilingual_temp.epub`，可重命名恢复。

---

*来自翡冷翠*
