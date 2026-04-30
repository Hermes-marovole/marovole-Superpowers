# GPT Image 2 逼真身份证照片生成提示词

> 来源：https://x.com/iqrasaifiii/status/2049564376638657011
> 作者：Iqra Saifi (@IqraSaifiii)
> 发布时间：2026-04-30
> 来自翡冷翠

---

## 简介

本提示词由 AI Filmmaker & Creator Iqra Saifi 分享，展示了如何使用 GPT Image 2 生成高度逼真的虚构身份证照片。这个案例完美体现了 GPT Image 2 在细节刻画、材质表现和光影处理上的强大能力。

---

## 原始帖子

**Iqra Saifi** (@IqraSaifiii)

> GPT hat richtig gekocht 🔥
> GPT Image 2 von @PixPrettyAI

（德语："GPT 真的做对了" / "GPT 做得太棒了"）

---

## 完整提示词

```json
{
  "type": "Nahaufnahme-Fotografie",
  "subject": "Eine fiktive Ausweiskarte, die von einer Hand gehalten wird",
  "card_content": {
    "header_text": "MUSTERREPUBLIK / AUSWEISKARTE / SAMPLE ID CARD",
    "logo": "Ein blaues Symbolfeld oben links mit dem Länderkürzel 'MR'",
    "portrait": {
      "appearance": "Junge Frau mit langen, glatten blonden Haaren und Mittelscheitel",
      "facial_features": "Helle Haut mit deutlich sichtbaren natürlichen Sommersprossen auf Nase und Wangen, neutraler Gesichtsausdruck, haselgrüne Augen mit geradem Blick nach vorn",
      "clothing": "Schwarzes Oberteil mit sichtbarem Ausschnitt",
      "accessories": "Kleine silberne Ohrstecker an den Ohrläppchen"
    },
    "text_data": {
      "surname": "MUSTERNAME",
      "given_name": "ERIKA",
      "birth_date": "07.11.1998",
      "birth_place": "BERLIN",
      "expiry_date": "01.12.2030"
    },
    "surface_texture": "Glänzende laminierte Oberfläche mit sichtbaren holografischen Sicherheitsmustern und Guilloche-Linien über Porträt und Text"
  },
  "foreground_hand": {
    "position": "Hält die untere rechte Ecke der Karte",
    "skin_tone": "Hell",
    "fingernail": "Sichtbarer Daumen mit langem, mandelförmigem Fingernagel, lackiert in glänzendem Bordeauxrot oder Dunkelrot"
  },
  "background": "Schlichte, einfarbig weiße Oberfläche",
  "lighting": "Weiches, gleichmäßiges Innenlicht mit leichten Reflexionen auf der Kartenoberfläche und dem glänzenden Nagellack",
  "framing": "Vertikale Nahaufnahme aus der Vogelperspektive, vollständig auf die Karte und den Daumen fokussiert"
}
```

---

## 提示词结构解析

### 1. 拍摄类型 (type)
- **Nahaufnahme-Fotografie** (特写摄影)

### 2. 主体 (subject)
- 虚构身份证，由手拿着

### 3. 卡片内容 (card_content)

#### 3.1 头部信息
- 机构名称：MUSTERREPUBLIK (样本共和国)
- 文档类型：AUSWEISKARTE / SAMPLE ID CARD
- 标志：蓝色标志框，左上角，国家代码 "MR"

#### 3.2 人像细节 (portrait)
| 属性 | 描述 |
|------|------|
| 外貌 | 年轻女性，长直金发，中分 |
| 面部特征 | 白皙皮肤，明显的自然雀斑（鼻子和脸颊），中性表情，榛绿色眼睛直视前方 |
| 服装 | 黑色上衣，可见领口 |
| 配饰 | 耳垂上小巧的银色耳钉 |

#### 3.3 文本信息 (text_data)
| 字段 | 内容 |
|------|------|
| 姓氏 | MUSTERNAME |
| 名字 | ERIKA |
| 出生日期 | 07.11.1998 |
| 出生地 | BERLIN |
| 有效期至 | 01.12.2030 |

#### 3.4 表面材质 (surface_texture)
- 光泽的层压表面
- 可见的全息安全图案
- Guilloche 线条（防伪花纹）覆盖人像和文本区域

### 4. 前景手部 (foreground_hand)
| 属性 | 描述 |
|------|------|
| 位置 | 握着卡片右下角 |
| 肤色 | 浅色 |
| 指甲 | 可见的拇指，长杏仁形指甲，涂有闪亮的波尔多红/深红色指甲油 |

### 5. 背景 (background)
- 简洁的纯白表面

### 6. 光线 (lighting)
- 柔和均匀的室内光线
- 卡片表面和闪亮指甲油上有轻微反光

### 7. 构图 (framing)
- 垂直特写
- 俯视角度
- 完全聚焦于卡片和拇指

---

## 提示词设计要点

### 1. 细节层次丰富
从人像特征（雀斑、眼睛颜色）到材质（层压表面、全息图案），每个元素都有精确描述。

### 2. 写实性增强
- **自然缺陷**：加入"自然雀斑"增加真实感
- **材质表现**：明确描述"光泽层压"、"反光"等物理特性
- **手部细节**：指甲形状、指甲油颜色、肤色——这些细节让照片更具真实感

### 3. 技术规范
- **德国身份证格式**：使用德语术语（"Musterrepublik"、"Ausweiskarte"）
- **防伪元素**：Guilloche 线条、全息图案
- **标准信息字段**：姓名、出生日期、有效期等

### 4. 光影控制
- 明确指定"柔和均匀的室内光线"
- 强调反光效果（层压表面、指甲油）

---

## 使用建议

### 1. 生成类似证件照
可以基于这个结构修改：
- 更换国家/地区（使用对应语言）
- 调整人像描述（性别、发型、肤色等）
- 修改背景颜色（证件类型不同，底色不同）

### 2. 学习提示词技巧
- **分层描述**：整体 → 细节 → 材质
- **多感官描写**：视觉（颜色、形状）+ 触觉（光泽、质感）
- **环境要素**：光线、背景、角度

### 3. 其他应用场景
- 护照照片生成
- 驾照照片生成
- 员工工牌照片生成
- 会员卡照片生成

---

## 输出示例

基于该提示词，GPT Image 2 可生成：
- 高度逼真的证件照片
- 正确的透视关系（手持角度）
- 真实的光影效果（层压膜反光）
- 自然的肤色和材质表现

---

## 社交媒体反响

- **浏览量**：558.5K
- **点赞**：3.8K
- **转发**：509
- **收藏**：5.9K
- **评论**：73

---

## 相关资源

### 作者信息
- **Twitter/X**: [@IqraSaifiii](https://x.com/IqraSaifiii)
- **简介**: AI Filmmaker & Creator | Turning Ideas into Prompt CPP
- **合作联系**: iqrasaifihere@gmail.com
- **关联账号**: @Kling_ai | @Hailuo_AI | @haimeta_ai & 20+

### GPT Image 2 相关信息
- **推荐服务**: @PixPrettyAI
- **模型版本**: GPT Image 2

---

## 快速参考模板

```json
{
  "type": "[拍摄类型：特写/证件照]",
  "subject": "[主体描述]",
  "card_content": {
    "header_text": "[文档标题]",
    "logo": "[标志描述]",
    "portrait": {
      "appearance": "[外貌]",
      "facial_features": "[面部特征细节]",
      "clothing": "[服装]",
      "accessories": "[配饰]"
    },
    "text_data": {
      "field1": "[信息1]",
      "field2": "[信息2]"
    },
    "surface_texture": "[材质描述]"
  },
  "foreground_hand": {
    "position": "[手持位置]",
    "skin_tone": "[肤色]",
    "fingernail": "[指甲细节]"
  },
  "background": "[背景]",
  "lighting": "[光线]",
  "framing": "[构图]"
}
```

---

*来自翡冷翠*
