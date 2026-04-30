# 用 CREAO × GPT-Image-2 做一本全自动生成的女儿绘本

> 来源：[AI奶爸 @zstmfhy](https://x.com/zstmfhy/status/2047263960005845109)  
> 整理时间：2026-04-24  
> 来自翡冷翠

---

## 简介

本教程由 AI 创作者 **AI奶爸**（@zstmfhy）分享，详细讲解如何使用 **CREAO** 平台结合 **GPT-Image-2** 图像模型，搭建一条全自动的儿童绘本生成流水线。

核心解决的问题：**从"做一次作品是魔法"升级为"做一条生产线是工程"**。实现输入一个书名，8 分钟后自动获得一本画风统一、角色一致的完整 PDF 绘本。

---

## 内容清单总览

| 章节 | 内容 | 核心要点 |
|------|------|----------|
| 1 | 问题定义 | AI 绘本的真问题是"能不能源源不断做下去" |
| 2 | 角色卡制作 | 用 GPT-Image-2 制作 5 张角色参考图 |
| 3 | 四节点流水线 | 剧情大纲 → 角色拼图 → 逐页插图 → PDF 合成 |
| 4 | CREAO Agent 搭建 | 把一次性操作沉淀为可复用的自动化工作流 |
| 5 | 应用场景扩展 | 情报简报、周报自动化、短视频工厂等 |

---

## 详细内容

### 一、问题定义：从作品到生产线

**触发场景：**
> 「爸爸，能给我讲一个**我是主角**的故事吗？」

市面上所有绘本都不是为孩子本人写的。用 AI 做一本不难，但三天后孩子要新故事时，又得重来一遍。

**核心洞察：**
- 做一次作品是**魔法**
- 做一条**永久在线的生产线**是**工程**

**目标：** 输入书名，自动产出一本新绘本。

---

### 二、角色卡制作：一劳永逸的"原材料"

用 GPT-Image-2 制作 5 张角色卡：爸爸、妈妈、女儿、爷爷、奶奶。

**三条关键 Tip：**

1. **背景完全一致**
   - 所有角色卡用浅米色纯背景
   - 背景变化会导致模型参考语境漂移

2. **特征描述具象化**
   - ❌ 不要说"可爱小女孩"
   - ✅ 要说"圆脸颊、粉腮红、两撮红头绳、黄色小花 T 恤"
   - 越具体，一致性越高

3. **人物占幅比例固定**
   - 每张角色卡人物占画幅 60% 左右
   - 确保拼参考图时视觉权重均衡

**角色卡效果：**
![角色卡示例](https://pbs.twimg.com/media/HGlOLESb0AAeKAb?format=jpg&name=small)

---

### 三、四节点流水线架构

整体流程图：

```
┌─────────────────────────────┐
│ 👤 用户输入                 │
│ 书名 / 主题 / 页数          │
└──────────────┬──────────────┘
               ▼
┌────────────────────────────────────────┐
│ 🧠 CREAO Agent · 儿童绘本一键生成器     │
│                                        │
│ ① 剧情大纲生成 ─ Claude Sonnet 4.6     │
│               ▼                        │
│ ② 角色模板拼图 ─ Python（拼 5 张卡）   │◀── 📎 角色卡
│               ▼                        │
│ ③ 逐页插图生成 ─ GPT-Image-2           │
│               ▼                        │
│ ④ PDF 合成 ─ Python HTML→PDF           │
└─────────────────┼──────────────────────┘
                  ▼
            📘 成品 PDF · 14 页 · 13.1MB
```

---

### 四、节点详解

#### 节点 ① · 剧情大纲生成（LLM 节点）

**使用模型：** CREAO 内置 Claude Sonnet 4.6

**Prompt 模板：**
```
你是一位儿童绘本编剧。
根据书名《{book_title}》和主题「{theme}」，
创作一个 {page_count} 页的故事大纲。

要求：
- 每页剧情不超过 30 字
- 主角是 3-4 岁的小女孩「汤圆」
- 必须体现主题，结尾温馨治愈
- 每页只能出现 2-4 个角色，不要出现路人
- 场景尽量多样化（家里/户外/白天/夜晚）

输出 JSON 数组，每项包含：page / scene / characters / mood
```

---

#### 节点 ② · 角色模板拼图（Python 代码节点）

**核心代码：**
```python
from PIL import Image
import os

names = ["爸爸", "妈妈", "女儿", "爷爷", "奶奶"]
imgs = [Image.open(f"/path/to/{name}照片.png") for name in names]

total_w = sum(i.width for i in imgs) + 10 * (len(imgs) - 1)
max_h = max(i.height for i in imgs)

canvas = Image.new("RGB", (total_w, max_h), "white")
x = 0
for img in imgs:
    canvas.paste(img, (x, 0))
    x += img.width + 10

canvas.save("/tmp/all_chars_ref.png")
```

**价值：**
- 拼好一次，12 页插图都复用它
- 成本降低 **92%**
- 角色一致性拉满

---

#### 节点 ③ · 逐页插图生成（图像模型节点）

**每页 Prompt 骨架：**
```
flat 2D cartoon illustration, clean bold outlines, chibi style, 
bright soft pastel colors, simple clean background, 
round chubby faces with rosy cheeks, Chinese children picture book style, 
smooth flat coloring.

EXACTLY {n} characters only: {characters_from_outline}
Scene: {page_scene}
NO other people. NO text in image.
```

**关键技巧：**
- 在"参考图"栏挂上节点 ② 拼好的 `all_chars_ref.png`
- 模型每次生成时都会参考这张拼图
- 确保 12 页画出"同一个汤圆"

---

#### 节点 ④ · PDF 合成（Python 代码节点）

**核心代码：**
```python
html = f"<html><body>{''.join(pages_html)}</body></html>"
filename = f"《{book_title}》_绘本_{int(time.time())}.pdf"
HTML(string=html).write_pdf(f"/tmp/{filename}")
```

---

### 五、CREAO 的核心优势

#### 1. 自动保存，终生复用

Agent 搭建完成后自动进入工作空间。下一次做新绘本：
- 第二本《汤圆去探索大自然》→ 输入 3 个字，等 8 分钟
- 第三本《汤圆和小豆的一天》→ 输入 3 个字，等 8 分钟
- 第一百本 → 还是 3 个字，8 分钟

**魔法的成本是一次性的，快乐是永续的。**

#### 2. 一键克隆，分享传播

CREAO Agent 支持**分享链接**：
- 扫码/点链接即可一键拷贝到自己的工作空间
- 换上家人的角色卡，5 分钟后拥有专属"绘本机"

**可扩展方向：**
- 🎨 换角色卡：用自己的家人照片
- ✏️ 改剧情 Prompt：睡前故事 / 科普 / 成长主题
- 🖌️ 换插图风格：水彩 / 剪纸 / 宫崎骏风格
- 📚 扩展系列合集：一个角色库 + N 个主题批量产出

---

### 六、应用场景扩展

同样的"固化成按钮"思路，可应用于：

| 场景 | 输入 | 输出 |
|------|------|------|
| 📰 每日情报简报 | 关注的领域关键词 | 新论文/博客/X 热帖摘要 → 微信推送 |
| 📊 周报自动化 | 日历 + 邮件 + Git 提交 | 周报草稿 |
| 🎬 短视频工厂 | 一段文字 | 分镜 → TTS 配音 → 60 秒成片 |
| 📚 英语学习流水线 | 英文 PDF | 章节摘要 + 生词卡 → 导入 Anki |
| 🍱 家庭小助手 | 冰箱照片 | 今晚食谱 + 购物清单 |

**核心思考：** 你生活里，有哪件每周都要重做一遍的事，值得被做成一个按钮？

---

## 资源汇总

### 相关链接

| 名称 | 链接 | 说明 |
|------|------|------|
| CREAO 官网 | https://agent.creao.ai | AI Agent 搭建平台 |
| 免费注册 | https://agent.creao.ai/signup | 新用户注册入口 |
| 示例绘本 PDF | https://github.com/zstmfhy/pdf | 汤圆学会了分享（GitHub） |
| 原始 X 帖子 | https://x.com/zstmfhy/status/2047263960005845109 | 完整教程原文 |

### 涉及工具/模型

- **CREAO** - AI Agent 编排平台
- **GPT-Image-2** - OpenAI 图像生成模型
- **Claude Sonnet 4.6** - Anthropic 大语言模型
- **Python PIL** - 图像处理库
- **HTML to PDF** - 文档转换工具

### 值得关注

- **@zstmfhy** (AI奶爸) - 万象AI实验室共创者，专注 AIGC 创作
- **@CreaoAI** - CREAO 官方账号

---

## 快速参考

### 角色卡 Prompt 示例

```
A cute 4-year-old Chinese girl named Tangyuan,
round chubby face with rosy cheeks,
two red hair ties, yellow flower T-shirt,
light beige solid background,
character reference sheet, front view,
children's book illustration style
```

### 插图生成 Prompt 模板

```
flat 2D cartoon illustration, clean bold outlines,
chibi style, bright soft pastel colors,
simple clean background, round chubby faces,
Chinese children picture book style,
{character_description},
Scene: {scene_description},
NO text in image
```

---

*来自翡冷翠*
