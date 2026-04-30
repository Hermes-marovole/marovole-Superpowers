# Awesome GPT Image 2 提示词库 - 完整整理

> 来源：https://github.com/YouMind-OpenLab/awesome-gpt-image-2
> 整理时间：2026-04-24
> 来自翡冷翠

---

## 简介

**Awesome GPT Image 2** 是由 YouMind OpenLab 维护的 GPT Image 2 创意提示词精选集合。该项目收录了 **1526+** 个经过社区验证的高质量提示词，支持 **16 种语言**，涵盖从产品设计到动漫创作等多个领域。

GPT Image 2（代号 "duct-tape"）是 OpenAI 下一代图像生成模型，在文字渲染、跨图一致性、商用级插画质量等方面实现了质的飞跃。

---

## 仓库概览

| 指标 | 数据 |
|------|------|
| ⭐ GitHub Stars | 1.1k+ |
| 📝 提示词总数 | 1526 |
| 🌟 精选提示词 | 6 |
| 🌍 支持语言 | 16 种 |
| 🔄 最后更新 | 2026年4月23日 |
| 📜 许可证 | CC BY 4.0 |

---

## 核心特性

### GPT Image 2 优势

- 🎯 **像素级文字渲染** — 中文、英文、日文均达到 native 水准，无错字、无字形扭曲
- 🎨 **跨图像素级一致性** — 同一角色、风格、IP 在多张图间保持像素级一致
- ⚡ **商用级插画质量** — 插画风格输出无需人工精修，即可直接用于商业场景
- 🌈 **真实艺术风格注入** — 真正理解并再现艺术风格的灵魂
- 🔧 **故事板与产品系列** — 适合故事板、IP 形象、产品系列图等需要多图一致性的场景
- 📐 **多语言平面设计** — 社交卡片、Banner、海报一次生图即可完成多语言文字排版

---

## 精选提示词（Featured Prompts）

### No. 1: VR 头显爆炸视图海报

**描述**：生成一张高科技 VR 头显爆炸视图，包含详细的组件标注和宣传文案。

**核心提示词结构**：
```json
{
  "type": "产品爆炸视图海报",
  "subject": "VR 头显",
  "style": "简洁的高科技 3D 渲染，摄影棚灯光，发光装饰",
  "layout": {
    "centerpiece": "VR 头显的垂直堆叠爆炸视图，展示 9 层内部组件",
    "callout_labels": {
      "count": 8,
      "left_side": ["Snapdragon XR2 Gen 2", "可调节 IPD 机构", "精密设计的头带"],
      "right_side": ["前面板", "追踪摄像头", "Pancake 透镜", "高性能电池", "柔软的面部接口"]
    }
  }
}
```

**标签**：`产品营销` `3D渲染` `技术示意图` `英文`

**来源**：[@wory37303852](https://x.com/wory37303852) · 2026年4月19日

---

### No. 2: 手绘城市美食地图

**描述**：生成一张手绘水彩风格的旅游地图，包含编号的当地特色美食、地标建筑及图例。

**核心提示词结构**：
```json
{
  "type": "手绘地图信息图",
  "style": "复古羊皮纸上的水彩墨水手绘插画",
  "title_section": {
    "text": "{城市名} 吃货暴走地图",
    "mascot": "戴着墨镜并竖起大拇指的卡通红辣椒"
  },
  "layout": {
    "landmarks": 6,
    "food_locations": 12,
    "legend": 5
  }
}
```

**标签**：`信息图` `旅游` `美食` `手绘风格` `中文`

**来源**：[@mm_zzm44854](https://x.com/mm_zzm44854) · 2026年4月19日

---

### No. 3: 混合风格的桃太郎讲解 Slides

**描述**：融合 Irasutoya 插图简约温馨的美学风格与日本政府 Slides 高信息密度特征的提示词。

**核心提示词**：
```
创建一个讲解型 Slides（{format}），主题为 {theme}，
将"Irasutoya"的柔和氛围与"霞关风格 Slides"极高的信息密度完美融合。
```

**标签**：`演示文稿` `教育` `混合风格` `日文`

**来源**：[@yammamon](https://x.com/yammamon) · 2026年4月19日

---

### No. 4: 电商直播 UI 样机

**描述**：生成逼真的社交媒体直播界面，叠加在人物肖像之上，包含可自定义的聊天消息、礼物弹窗和商品购买卡片。

**核心提示词结构**：
```json
{
  "type": "直播 UI 样机",
  "subject": {
    "description": "主播肖像，面带微笑",
    "background": "品牌 Logo 和产品展示"
  },
  "ui_overlay": {
    "top_header": "主播信息、排名徽章、观众统计",
    "mid_left_gifts": "礼物动画展示",
    "bottom_left_chat": "实时聊天消息",
    "bottom_right_product_card": "商品购买卡片"
  }
}
```

**标签**：`UI/UX` `社交媒体` `电商` `样机` `中文`

**来源**：[@sjbbxhz](https://x.com/sjbbxhz) · 2026年4月19日

---

### No. 5: 动漫武术对决

**描述**：生成一个动态的动漫风格动作场景，展示两个角色在传统道场中伴随元素光环进行战斗。

**核心提示词**：
```
一幅极具动态感的动漫插画，描绘了两名少女在传统木质道场内进行激烈武术对决的场景。
前景：黑色高丸子头配红色丝带的少女，红色能量斩击环绕
右侧：浅紫色双丸子头的少女跃起，蓝色水流状能量轨迹
背景：质朴的木质寺庙内部，悬挂"武術会"招牌
```

**标签**：`动漫` `动作场景` `角色设计` `英文`

**来源**：[@Tanemomi_Ver2](https://x.com/Tanemomi_Ver2) · 2026年4月20日

---

### No. 6: 3D 石阶演化信息图

**描述**：将平面的演化时间轴转化为逼真的 3D 石阶信息图，包含精细的生物渲染图和结构化的侧边栏。

**核心提示词结构**：
```json
{
  "type": "演化时间轴信息图",
  "instruction": "将平面矢量设计转化为高度逼真的 3D 信息图",
  "style": {
    "background": "复古纹理羊皮纸",
    "staircase": "逼真的纹理石块",
    "subjects": "高度精细的照片级真实 3D 渲染"
  },
  "levels": ["L0: 单细胞生命", "L1: 多细胞生物", "L2: 动物界", ...]
}
```

**标签**：`信息图` `教育` `3D渲染` `演化` `英文`

**来源**：社区贡献

---

## 使用场景分类

### 个人与社交
- [个人资料 / 头像](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=profile-avatar)
- [社交媒体帖子](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=social-media-post)
- [YouTube 缩略图](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=youtube-thumbnail)
- [漫画 / 故事板](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=comic-storyboard)

### 商业与营销
- [产品营销](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=product-marketing)
- [电商主图](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=ecommerce-main-image)
- [海报 / 传单](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=poster-flyer)
- [App / 网页设计](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=app-web-design)

### 教育与信息
- [信息图 / 教育视觉图](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=infographic-edu-visual)
- [游戏素材](https://youmind.com/zh-CN/gpt-image-2-prompts?categories=game-asset)

---

## 艺术风格分类

| 风格类别 | 说明 |
|----------|------|
| **摄影** | 真实感照片、产品摄影、人像摄影 |
| **电影 / 电影剧照** | 电影级光影、叙事场景 |
| **动漫 / 漫画** | 日式动漫风格、美式漫画 |
| **插画** | 商业插画、编辑插画 |
| **草图 / 线稿** | 手绘风格、概念草图 |
| **3D 渲染** | 产品渲染、建筑可视化 |
| **像素艺术** | 复古游戏风格 |
| **油画 / 水彩** | 传统美术风格 |
| **水墨 / 中国风** | 东方美学风格 |
| **赛博朋克 / 科幻** | 未来主义风格 |

---

## 多语言支持

仓库原生支持 16 种语言：

- 🇺🇸 English
- 🇨🇳 简体中文
- 🇹🇼 繁體中文
- 🇯🇵 日本語
- 🇰🇷 한국어
- 🇹🇭 ไทย
- 🇻🇳 Tiếng Việt
- 🇮🇳 हिन्दी
- 🇪🇸 Español
- 🇪🇸 Español (Latinoamérica)
- 🇩🇪 Deutsch
- 🇫🇷 Français
- 🇮🇹 Italiano
- 🇧🇷 Português (Brasil)
- 🇵🇹 Português
- 🇹🇷 Türkçe

---

## YouMind 网页图库

除了 GitHub README，项目还提供精美的网页图库：

**👉 [youmind.com/zh-CN/gpt-image-2-prompts](https://youmind.com/zh-CN/gpt-image-2-prompts)**

### 图库优势

| 功能 | GitHub README | YouMind 图库 |
|------|--------------|--------------|
| 🎨 可视化布局 | 线性列表 | 瀑布流网格 |
| 🔍 搜索 | Ctrl+F | 全文搜索和筛选 |
| 🤖 AI 一键生图 | - | ✅ 支持 |
| 📱 移动端 | 基础 | 完全响应式 |
| 🏷️ 分类 | - | 多维度分类浏览 |

---

## Raycast 集成

部分提示词支持使用 **Raycast Snippets** 语法的动态参数，方便快速迭代：

**示例格式**：
```
A quote card with "{argument name="quote" default="Stay hungry, stay foolish"}"
by {argument name="author" default="Steve Jobs"}
```

寻找 🚀 Raycast Friendly 徽章即可使用此功能。

---

## 相关资源

### 相关项目
- **[Nano Banana Pro 提示词库](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts)** — Google 旗舰生图模型，10000+ 精选提示词

### 官方链接
- **GitHub 仓库**: https://github.com/YouMind-OpenLab/awesome-gpt-image-2
- **YouMind 图库**: https://youmind.com/zh-CN/gpt-image-2-prompts
- **贡献指南**: [CONTRIBUTING.md](https://github.com/YouMind-OpenLab/awesome-gpt-image-2/blob/main/docs/CONTRIBUTING.md)
- **FAQ**: [FAQ.md](https://github.com/YouMind-OpenLab/awesome-gpt-image-2/blob/main/docs/FAQ.md)

### 社区资源
- **组织**: [YouMind OpenLab](https://github.com/YouMind-OpenLab)

---

## 使用建议

### 提示词使用流程
1. **浏览图库**：在 [YouMind 图库](https://youmind.com/zh-CN/gpt-image-2-prompts) 中按分类筛选
2. **选择提示词**：根据使用场景和艺术风格找到合适的提示词
3. **自定义参数**：使用 Raycast 或手动替换动态参数
4. **生成图像**：在 GPT Image 2 中运行提示词
5. **迭代优化**：根据结果调整参数和描述

### 最佳实践
- 使用结构化的 JSON 格式提示词可获得更精确的控制
- 利用动态参数（arguments）实现快速迭代
- 参考示例图片了解预期输出效果
- 关注 Featured 提示词获取高质量模板

---

## 如何贡献

项目欢迎社区贡献：

1. **提交新提示词**：通过 GitHub Issue 提交
2. **翻译**：帮助完善多语言版本
3. **改进现有提示词**：提交 PR 优化现有内容
4. **分享使用案例**：展示你的创作成果

详见 [贡献指南](https://github.com/YouMind-OpenLab/awesome-gpt-image-2/blob/main/docs/CONTRIBUTING.md)

---

## 许可证

本项目采用 **CC BY 4.0** 许可证，允许自由使用、修改和分享，需注明原作者。

**版权声明**：所有提示词均收集自社区，仅供教育目的使用。

---

*来自翡冷翠*
