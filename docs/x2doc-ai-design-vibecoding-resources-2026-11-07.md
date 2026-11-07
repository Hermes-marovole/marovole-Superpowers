# AI 辅助设计与 Vibe Coding 19 个灵感与组件资源拆解 - X2Doc 整理

> 来源：https://x.com/BardhylBytyqi/status/2118838961602748834
> 作者：@BardhylBytyqi (Bardhyl Bytyqi, Building @modulify)
> 发布时间：2026-11-06 22:52:29 UTC
> 整理时间：2026-11-07
> 来自翡冷翠

---

## TL;DR

- **原帖本质拆解**：表面是「AI 设计必存 20 个网站」的高收藏清单帖（625 赞 / 944 收藏 / 2.5 万浏览），实则是 Modulify 创始人 `@BardhylBytyqi` 的**「特洛伊木马清单（Trojan Horse Listicle）」增长范式**——将自家产品放在 #1（`modulify.ai`）与 #3（`modulify.ai/templates`），并配一段右下角带 `Edit with Modulify` 水印的 21.8 秒 3D 点云建站演示视频（NORRVIK 模板），借成熟设计站点的长尾声量实现冷启动转化。
- **实测核验脱水（19 链 → 17 个独立站点）**：原帖序号跳过了 `#19`（从 18 直接到 20，共 19 条链接）；经逐一 HTTP 实测解析，其中 `#1` 与 `#3` 同属作者自家产品 `modulify.ai`，`#8 godly.website` 已重定向至 `#11 recent.design/?ref=godly`（即 Godly 改名 Recent 后被重复计入两次），而 `#17 sent.dm` 实为 SMS/WhatsApp/RCS 消息路由 API（非设计工具，属 Indie Hacker 互推夹带）。
- **真正高价值的 5 个可落地资产**：
  1. **beUI (`beui.dev`)**：MIT 开源动效组件库（GitHub `starc007/ui-components` 含 156 个 React 组件 + `starc007/beui-native` 含 73 个 React Native 组件），基于 Motion + Tailwind CSS 4，直接通过 `shadcn` CLI 一键安装源码。
  2. **Motion (`motionin.design`)**：物理与光标响应型高阶 Web 交互区块库（rAF + GSAP），每个动效区块交付物即为**完整的 Prompt + 技术规格书（Spec）**，可直接粘贴进 Claude Code / Codex 复刻。
  3. **60fps (`60fps.design`) & Mobbin (`mobbin.com`)**：分别收录 2,140+ 顶级应用动效镜头与 600,000+ 真实 App 界面，且**均已上线 MCP 接口（`60fps.design/mcp` 与 Mobbin MCP）**，可直接作为 AI 编码 Agent 的设计参考源。
  4. **posts.design (`posts.design`)**：收录 1,080+ 科技与 AI 品牌（OpenAI、Vercel、Notion、Perplexity、Mistral、Nous Research 等）的 5,556+ 真实社媒发布海报、Launch 视频首帧与 OG 图，是极佳的宣发视觉对标库。
  5. **Paper Animation (`paperanimation.ai`)**：浏览器端一键生成折纸展开、报纸高亮、杂志剪报字母与推文卡片动画（导出 720×1280 MP4/GIF 或绿幕素材），可与本地 `papermorph-book-film` 技能形成互补对标。

---

## 原帖核心内容与结构还原

原帖正文（已将 19 个 `t.co` 短链还原为实际落地 URL）：

> If you design with AI, save this
>
> 1. https://modulify.ai — best vibecoding tool
> 2. https://landdding.com — top notch landings
> 3. https://modulify.ai/templates — free templates
> 4. https://motionin.design — 1 prompt 1 website
> 5. https://iconly.design — world best icons
> 6. https://fontinlogo.com — fonts behind brands
> 7. https://on.design — design community
> 8. https://godly.website — award websites *(实测重定向至 `https://recent.design/?ref=godly`)*
> 9. https://60fps.design — mobile UI animations
> 10. https://footer.design — footer inspiration
> 11. https://recent.design — next level design
> 12. https://backgrounds.supply — backgrounds
> 13. https://posts.design — big brands posts
> 14. https://beui.dev — animated components
> 15. https://wonderlist.design — figma designs
> 16. https://mobbin.com — real app screens
> 17. https://sent.dm — almost free sms
> 18. https://logotouse.com — premium logos
> *(注：原帖漏掉序号 19)*
> 20. https://paperanimation.ai — cool anim
>
> bookmark this

**附带视频内容**：
- 时长 21.86 秒（1464×1080），展示一个名为 **NORRVIK**（*"The ground truth for every building"*）的暗黑工业风建筑 LiDAR 点云交互网站模板，画面右下角固定悬浮白底胶囊按钮 **`Edit with Modulify`**，进一步印证该帖是以清单收藏驱动自家建站工具转化的典型案例。

---

## 关键信息与资源（19 条链接逐一实测核验表）

以下按实际用途重分类，并标注真实页面标题、核心机制、定价/开源状态及核验备注：

### 一、可直接接入 AI 编码工作流（Prompt / 组件源码 / MCP）

| 原帖序号 | 名称 | 实测链接 | 核心定位与技术机制 | 适用场景与价值判断 |
|---|---|---|---|---|
| #14 | **beUI / beUI Native** | https://beui.dev <br>([GitHub Web](https://github.com/starc007/ui-components) / [Native](https://github.com/starc007/beui-native)) | **MIT 开源动效组件库**。含 156 个 React/Next.js 组件（基于 Framer Motion + Tailwind CSS 4）与 73 个 React Native 组件（Reanimated + Gesture Handler + Uniwind）。支持 `bunx --bun shadcn add @beui/<name>` 直接把源码拉进仓库。另有付费 Pro 版（350+ 区块）。 | **全清单含金量最高的技术资产**。含 Dynamic Island、Morphing Modal、Animated Toast Stack、Command Palette、Swipeable List 等高定交互，源码直接落盘无黑盒依赖。 |
| #4 | **Motion (motionin.design)** | https://motionin.design | **「复制 Prompt 即交付」的高阶交互区块库**。聚焦基于物理（弹簧、重力空洞、滚动曲率透镜、复古 CRT 抖动像素）的 `requestAnimationFrame` + GSAP 网页区块。提供部分免费区块（如 Liquid Type），付费版 $9/月（解锁 3 个/月）或 $99 买断。 | 它验证了**「用超长高精度物理与视觉 Spec Prompt 替代传统组件库」**的路线（见其首页每张卡片长达 200 词的逐帧物理描述），其公开的文字描述本身就是极佳的动画 Prompt 范本。 |
| #9 | **60fps** | https://60fps.design | **移动端与 Web 顶级微交互/动效拆解库**。收录 499 个知名 App（Apple Health、Revolut、Duolingo、Runmo 等）的 2,140+ 动效录屏、83 种动效模式、32 个代码片段、67 个分镜（Storyboards），并提供 **`60fps.design/mcp`**。 | 做 iOS/Web 产品微交互（Splash、Bottom Sheet、计数器滚动、液态玻璃）的首选对标库；其动作分类词表（Spring Physics、Shimmer、Liquid Glass 等）可与本地 `animation-vocabulary` 技能配合使用。 |
| #16 | **Mobbin** | https://mobbin.com | **全球最大真实 App 界面与用户流搜索引擎**。收录超 600,000 张可按页面类型、组件、流程检索的 iOS/Android/Web 截图，现已推出 **Mobbin MCP** 供 AI Agent 直接调取设计参考。 | 产品经理做 Onboarding、Paywall、结账流、设置页信息架构时的行业基础设施。 |
| #1 & #3 | **Modulify** *(作者自家产品)* | https://modulify.ai <br>https://modulify.ai/templates | **AI 提示词建站与模板克隆工具**。输入 Prompt 生成含布局、文案、CMS、数据库与托管的网站，提供可一键克隆的免费模板库。 | 属作者 `@BardhylBytyqi` 自建 SaaS（植入在榜单 #1 和 #3）。我们已有 Claude Code / Codex + Next.js/Cloudflare 完整研发流，无需切换至此闭源建站平台，但其模板区的工业风/点云视觉可作参考。 |

### 二、网页与社媒视觉灵感库（Landing Page / 品牌宣发 / 局部组件）

| 原帖序号 | 名称 | 实测链接 | 核心定位与体量 | 适用场景与价值判断 |
|---|---|---|---|---|
| #13 | **posts.design** | https://posts.design | **科技与 AI 品牌真实社媒宣发视觉库**。收录 1,080+ 品牌（OpenAI、Vercel、Notion、Perplexity、Mistral、E2B、Nous Research 等）的 5,556+ 条 X 发布卡片、产品更新视频首帧、里程碑海报、X Header 与 OG 图，每日更新。 | **对自媒体与出海产品宣发极有价值**。发新开源 Skill、产品功能上线或里程碑推文前，可直接按 `Launch` / `Product Update` / `Announcement Card` 检索硅谷一线团队的构图与排版。 |
| #8 & #11 | **Recent** *(原 Godly)* | https://recent.design <br>*(#8 `godly.website` 301 跳转至此)* | **获奖级前卫网页设计画廊**。原名 `godly.website`，现已重命名并跳转至 `recent.design`。原帖作者把新旧两个域名分别列为 #8 和 #11 凑数。 | 寻找重动效、WebGL、极具实验性的独立工作室与新锐 AI 产品官网视觉风格时的头部灵感站。 |
| #2 | **Landdding** | https://landdding.com | **社区投票驱动的每日新 Landing Page 展示站**。支持设计师提交作品并由社区 Upvote 排序。 | 适合快速扫览独立开发者与中早期 SaaS 的落地页首屏（Hero Section）结构。 |
| #10 | **Footer.design** | https://www.footer.design | **全球唯一的网站页脚（Footer）专项画廊**。支持按布局类型与视觉风格筛选各大网站的 Footer 设计。 | 解决落地页收尾粗糙的痛点——AI 生成网页最容易做出千篇一律的四列平庸页脚，可直接从此处挑样式喂给 AI 复刻。 |
| #15 | **Wonderlist** | https://wonderlist.design | **127 套精品 Figma 网站设计模板合集**。覆盖 SaaS、Agency、Portfolio、Consulting 等分类。 | 适合需要 Figma 源文件而非纯代码模板的场景。 |
| #7 | **on.design** | https://on.design | **邀请制独立设计师与工作室作品社区**（访问首页直接跳 `/login` 登录墙）。 | 封闭式设计师社交网络，非公开免登录检索库，实用度低于 Recent 和 Landdding。 |

### 三、视觉资产与短视频动效工具（图标 / 字体 / Logo / 背景 / 剪报动画）

| 原帖序号 | 名称 | 实测链接 | 核心定位与体量 | 适用场景与价值判断 |
|---|---|---|---|---|
| #20 | **Paper Animation** | https://paperanimation.ai | **浏览器端折纸与报纸剪报动画生成器**。支持 4 种风格：折纸展开（Paper Fold，自带 AI 抠图）、报纸关键词高亮（Newspaper Highlight，15 种报纸字体 + 8 种纸张纹理）、杂志剪贴字母（Magazine Letters）、推文卡片（Tweet Posts）。支持导出 720×1280 竖屏 MP4/GIF 及绿幕（Green Screen）模式。免费版带水印，付费版 $9/月或 $39 创始终身版。 | 宣称已有 12 万创作者使用。其产品形态与我们本地沉淀的 `papermorph-book-film` 技能高度同源，非常适合作为**出海微工具（Micro-SaaS）定价与转化页设计**的直接拆解样本（单点视觉钩子 + 浏览器零安装 + $9/月 vs $39 限量编号终身买断）。 |
| #5 | **Iconly** | https://iconly.design | **2,400+ 应用、游戏与 Web 图标灵感库**。支持按分类、视觉风格（3D、拟物、极简等）和色系检索 App Icon。 | 适合在给新项目、桌面插件或移动端 App 设计启动图标（配合 `avatar-icon-asset-processing` 技能）前寻找构图与质感参考。 |
| #6 | **Font In Logo** | https://www.fontinlogo.com | **知名品牌 Logo 背后的字体反查库**。收录 Nike、Tesla、Chanel、YouTube、Nvidia、NYT 等品牌的 Logo 使用字体解析。 | 品牌设计或海报排版时快速查找大厂同款字体的轻量工具站（同样是典型的程序化 SEO 流量站样本）。 |
| #12 | **Backgrounds Supply** | https://backgrounds.supply | **手绘与 AI 生成的高清背景、壁纸与渐变素材库**。 | 提供可直接垫在 Hero Section 或社媒宣发卡片底部的纹理与渐变图。 |
| #18 | **Logo To Use** | https://logotouse.com | **可用于样机（Mockup）与模板占位的免费高质 Logo 库**。提供彩色/纯色、带字/纯图形且支持 Figma 编辑的虚拟公司 Logo。 | 做产品演示 Demo、组件库预览或模板展示时，避免使用真实客户商标侵权的实用占位资产。 |

### 四、非设计类夹带项

| 原帖序号 | 名称 | 实测链接 | 核心定位 | 核验备注 |
|---|---|---|---|---|
| #17 | **Sent** | https://www.sent.dm | **SMS、WhatsApp 与 RCS 统一消息发送 API**（处理通道路由、合规与格式转换）。 | 与「AI 设计」毫无关系，原帖标注为 `almost free sms`，属清单帖常见的商业互推或私货夹带。 |

---

## 我的吸收判断

### 1. 可复用能力与直接落点
- **组件级复用（`beui.dev`）**：`starc007/ui-components` 是真开源（MIT）且基于 `shadcn` 分发体系。遇到需要高质感弹簧动效（如灵知 AI 或出海工具站的动态胶囊提示、丝滑抽屉、数字滚动）时，可直接参考或按需提取其组件源码（注意其默认基于 Tailwind v4，若在锁死 Tailwind 3.4 的项目中使用需转换样式写法）。
- **Prompt 级复用（`motionin.design`）**：该站最大的启发不是买它的会员，而是它**「如何用自然语言把一个复杂物理交互描述得让 LLM 一次写对」**。哪怕不付费解锁，它首页公开的每个区块长文案（明确指定哪里用单 `requestAnimationFrame` 循环、哪里用 GSAP、如何处理滚轮速度阻尼、如何做 `prefers-reduced-motion` 降级）就是一套现成的高阶动效 Prompt 模板。
- **宣发视觉对标（`posts.design`）**：个人号与开源项目（如 `marovole-skills` 后续重磅 Skill 发布）做 X 宣发图/视频首帧时，先看 `posts.design` 上 Vercel、Raycast、OpenAI、Nous Research 的最新卡片版式。

### 2. 值得沉淀到 skill / workflow 吗？
- **无需新建独立 Skill**（遵循现有 Skill 能出活即直接复用的原则）。
- 可在后续前端开发或动效优化任务中，将 `beui.dev`、`60fps.design`、`posts.design` 作为 `pick-ui-library`、`animate`、`niaoshu-packaging` 的外部参考源。

### 3. 对 AI × Product × Super Individual（超级个体 / 出海工具站）的价值
- **增长范式拆解（Trojan Horse Listicle）**：`@BardhylBytyqi` 这条推文展示了极高 ROI 的 X 冷启动打法——不发枯燥的「我的产品上线了」，而是攒一个「20 个 AI 设计神器」清单，把自家产品塞在 #1 和 #3，视频放自家产品的惊艳模板演示。**收藏数（944）甚至高于点赞数（625）**，算法权重极高。我们后续推开源 Skill 或出海小工具时，完全可以复用这套「高密度行业资源盘点 + #1 自家核心资产」的叙事结构。
- **出海 Micro-SaaS 样本（`paperanimation.ai` & `fontinlogo.com`）**：
  - `fontinlogo.com` 是典型的「品牌名 + What font」程序化 SEO 字典站；
  - `paperanimation.ai` 则是将短视频高频刚需（报纸高亮/折纸转场）封装成浏览器零门槛工具，采用「免费带水印裂变 + $9/月订阅 + $39 限量 1,000 名编号终身买断（阶梯涨价制造紧迫感）」的定价模型，非常值得出海工具站定价页参考。

### 4. 风险或待验证点
- **清单帖的水分过滤**：原帖未披露利益相关性（#1、#3 为本人项目），且存在新旧域名重复凑数（#8 `godly.website` 与 #11 `recent.design`）、序号跳号（缺 #19）及跨界夹带（#17 `sent.dm`）。引述或二次传播时务必使用本报告脱水后的 17 个独立站点数据。
- **技术栈版本注意**：`beui.dev` 官方文档标注依赖 React 19 + Tailwind CSS 4；在要求锁定 Tailwind CSS 3.4 的工程（如 InsForge 模板项目）中不可盲目直接跑 CLI 覆盖配置，应采用读取源码单文件移植的方式。

---

## 可执行下一步

- [ ] 在后续需要制作开源项目 Release 宣发卡片或 X 置顶图时，使用 `posts.design` 检索同类 AI 基础设施品牌（如 Vercel / E2B / Nous Research）的 Announcement Card 构图。
- [ ] 在需要编写复杂 Canvas / DOM 物理交互动效时，参考 `motionin.design` 的「rAF 物理循环 + GSAP 入场 + 阻尼参数描述」三段式 Spec 结构编写编码提示词。
- [ ] 出海工具站设计 Pricing 页面时，参考 `paperanimation.ai` 的「免费带水印 + $9 月付 + 阶梯涨价编号 Founder Lifetime」转化漏斗设计。

---

*来自翡冷翠*
