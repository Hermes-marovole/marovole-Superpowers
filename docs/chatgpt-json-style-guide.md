# ChatGPT JSON 风格协议：用一张参考图生成整套风格一致的作品

> 来源：https://x.com/VigoCreativeAI/status/2046961307048427630
> 整理时间：2026-04-23
> 来自翡冷翠

---

## 简介

**核心突破**：用 **1 张参考图 + 1 个 JSON 文件**，生成整套画风一致的作品。

@VigoCreativeAI（Vigo Zhao）分享的方法，让 AI 图像生成从"每次重新写 Prompt"进化到"建立可复用的风格系统"。

**关键成果**：
- ✅ 同一套视觉 DNA
- ✅ 同一套配色体系
- ✅ 同一种"气味"和质感
- ✅ 4 张（甚至 20 张）完全不同的海报，风格却完全一致
- ✅ **无需训练 LoRA，无需微调模型**

---

## 核心理念：从"收藏图"到"风格协议"

### 传统做法的问题

很多人收藏参考图只是"存了个寂寞"——存了就忘了，用的时候找不出来，更无法稳定复现风格。

### 新方法：JSON 风格协议

**把一张喜欢的插画，拆解成一套可变量化的 JSON 风格协议**。

```
参考图 → 拆解风格要素 → JSON 结构化 → 可变参数 → 稳定复现
```

**优势**：
- 换主体、换配色、换场景，都能稳定出同款风格
- JSON 格式便于编辑、复用、分享
- AI 能精确理解并执行

---

## JSON 风格协议结构

### 基础模板框架

```json
{
  "style_name": "风格名称",
  "visual_dna": {
    "art_direction": "艺术指导方向",
    "color_palette": {
      "primary": "主色调",
      "secondary": "辅助色",
      "accent": "强调色",
      "mood": "色彩情绪"
    },
    "lighting": {
      "type": "光线类型",
      "quality": "光线质感",
      "direction": "光源方向"
    },
    "texture": {
      "surface": "表面质感",
      "material": "材质特征",
      "finish": "处理方式"
    },
    "composition": {
      "framing": "构图方式",
      "perspective": "视角",
      "depth": "景深处理"
    }
  },
  "subject_variables": {
    "main_subject": "主体内容（可变）",
    "setting": "场景环境（可变）",
    "action": "动作/状态（可变）"
  },
  "output_spec": {
    "aspect_ratio": "1:1",
    "quality": "high",
    "rendering": "渲染方式"
  }
}
```

---

## 实战案例：真实照片 + 街头涂鸦叠加

### Vigo 的创作示例

**风格描述**：
- 真实照片作为基底
- 街头涂鸦艺术叠加
- 粉色系主色调（从上海屋顶那只粉色大猫提炼）
- 虚实结合的视觉冲击力

### JSON 协议示例

```json
{
  "style_name": "Street Photo Graffiti Fusion",
  "visual_dna": {
    "art_direction": "真实摄影与街头涂鸦的碰撞融合",
    "color_palette": {
      "primary": "柔和粉色系 (pastel pink, coral)",
      "secondary": "城市灰调 (concrete gray)",
      "accent": "亮黄与荧光色涂鸦高光",
      "mood": "俏皮、年轻、略带叛逆"
    },
    "lighting": {
      "type": "自然日光 + 人工补光",
      "quality": "柔和但有方向性",
      "direction": "侧逆光，增强质感"
    },
    "texture": {
      "surface": "真实照片基底 + 涂鸦笔触叠加",
      "material": "墙面粗糙质感 + 光滑涂鸦颜料",
      "finish": "保留了涂鸦的手绘不完美感"
    },
    "composition": {
      "framing": "主体居中，涂鸦元素环绕",
      "perspective": "略带仰角，增强气势",
      "depth": "虚实层次分明"
    }
  },
  "subject_variables": {
    "main_subject": "[可替换：猫/人物/动物/物体]",
    "setting": "[可替换：屋顶/街道/室内/任何场景]",
    "action": "[可替换：静态/动态/互动]"
  },
  "output_spec": {
    "aspect_ratio": "1:1",
    "quality": "photorealistic with artistic overlay",
    "rendering": "digital art with photo base"
  }
}
```

---

## 使用方式

### 方式一：基础风格重绘（Basic Retexturing）

**Prompt 结构**：
```
[参考图像] + [JSON 风格代码] + 
"retexture this image into the following JSON style aesthetic"
```

**效果**：AI 会根据风格模板，把图片表面质感、颜色等进行"换肤"。

---

### 方式二：严格风格换肤（Strict Retexturing）

**Prompt 结构**：
```
[参考图像] + [JSON 风格代码] + 
"retexture this image exactly as it is. 
 do not change the shape, proportion, or layout of the image. 
 apply only the surface texture, material, lighting, and color effects 
 based on the following JSON style aesthetic. 
 keep the images geometry completely intact 
 and output in a 1:1 square aspect ratio image"
```

**效果**：只改表面风格（材质、色彩、光影），**不改变原图的结构和构图**。

**适用场景**：保持原始内容完整的美学升级。

---

### 方式三：风格环境嵌入（Environment Placement）

**Prompt 结构**：
```
[参考图像] + [JSON 风格代码] + 
"place this image in this json styled environment. 
 do not change the shape, proportion, or layout of the input image. 
 keep the image's geometry completely intact 
 and output in a 1:1 square aspect ratio image"
```

**效果**：把主体放入 JSON 描述的环境中，主体不变，环境风格化。

---

### 方式四：风格融合（Style Fusion）

**Prompt 结构**：
```
[参考图像] + [JSON 风格 A] + [JSON 风格 B] + ... + 
"combine these styles and retexture the image"
```

**效果**：融合多种风格，获得更复杂多样的视觉效果。

**进阶玩法**：
- 递归使用：上一次输出的图片作为新的输入
- 再套用另一个 JSON 风格模板
- 逐步叠加变化

---

## 从参考图提炼 JSON 协议的方法

### 步骤 1：视觉分析

观察参考图，记录以下要素：

| 维度 | 观察要点 | 记录示例 |
|------|----------|----------|
| **色彩** | 主色、辅助色、强调色 | 粉色主导，灰色背景，亮黄高光 |
| **光影** | 光源方向、质感、氛围 | 侧逆光，柔和但有层次 |
| **质感** | 表面处理方式 | 真实照片 + 手绘涂鸦叠加 |
| **构图** | 视角、框架、重心 | 居中构图，略带仰角 |
| **情绪** | 整体感觉 | 俏皮、年轻、叛逆 |
| **技术** | 媒介、工具、手法 | 摄影 + 数字涂鸦 |

### 步骤 2：结构化为 JSON

将观察结果填入 JSON 模板，使用精确的形容词。

### 步骤 3：测试迭代

1. 用 JSON 生成第一张图
2. 对比参考图，找出差异
3. 调整 JSON 中的描述词
4. 重复直到满意

### 步骤 4：变量定义

确定哪些元素是可变的：
- 主体（subject）→ 可替换
- 场景（setting）→ 可替换
- 动作（action）→ 可替换
- 风格核心（style core）→ 保持不变

---

## 对比：为什么 JSON 比传统 Prompt 更好

| 维度 | 传统 Prompt | JSON 风格协议 |
|------|-------------|---------------|
| **复用性** | 每次重写，难以一致 | 一次建立，多次复用 |
| **可编辑性** | 长文本难修改 | 结构化，精确调整 |
| **协作性** | 难以分享 | JSON 文件轻松分享 |
| **版本管理** | 混乱 | 可版本化，可追溯 |
| **AI 理解** | 可能遗漏细节 | 结构化，AI 理解更精确 |
| **批量生成** | 困难 | 替换变量即可批量生成 |

---

## 工具与资源

### 相关工具

| 工具 | 用途 | 链接 |
|------|------|------|
| **JSON Visuals** | ChatGPT 风格模板可视化 | https://json.visuals.zip/ |
| **ChatGPT** | 图像生成（gpt-4o） | chat.openai.com |
| **Cursor/Claude** | JSON 编辑辅助 | cursor.com / claude.ai |

### 参考资源

- **作者 X**：@VigoCreativeAI（Vigo Zhao）
- **核心作品**：上海屋顶粉色大猫系列
- **社区工具**：50+ 预定义 JSON 风格代码库

---

## 进阶技巧

### 技巧 1：分层风格定义

把复杂风格拆成多个 JSON 层：
```json
{
  "base_layer": { /* 基础摄影风格 */ },
  "overlay_layer": { /* 涂鸦叠加风格 */ },
  "post_process": { /* 后期处理风格 */ }
}
```

### 技巧 2：随机化参数

在 JSON 中加入随机变量：
```json
{
  "color_palette": {
    "primary": "random(warm_colors)",
    "accent": "random(complementary)"
  }
}
```

用于探索风格变体。

### 技巧 3：风格版本控制

用 Git 管理 JSON 文件：
```bash
git init style-library
git add style-v1.json
git commit -m "Add base graffiti style"
git checkout -b warm-variant
# 修改配色
git commit -m "Warm color variant"
```

---

## 应用场景

| 场景 | 价值 |
|------|------|
| **品牌视觉系统** | 建立一致的视觉 DNA |
| **IP 角色设计** | 同一角色多场景统一风格 |
| **社交媒体运营** | 批量生成风格一致的封面 |
| **游戏美术** | NPC、场景、道具风格统一 |
| **电商产品图** | 不同产品同风格展示 |
| **艺术创作** | 探索风格变体，快速迭代 |

---

## 核心要点总结

> **"很多人收藏图只是存了个寂寞。我的做法是把它拆成一套可变量化的 JSON 风格协议，换主体、换配色都能稳定出同款。"**

**关键转变**：
1. 从"存图"到"拆风格"
2. 从"每次重写 Prompt"到"复用 JSON 协议"
3. 从"不稳定生成"到"风格一致性保障"
4. 从"单张创作"到"批量生产"

**核心价值**：
- 无需 LoRA 训练
- 无需模型微调
- 仅需 1 张参考图 + 1 个 JSON 文件

---

*来自翡冷翠*
