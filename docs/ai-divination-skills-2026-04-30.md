# GitHub 热度最高的玄学 AI Skill 整理

> 来源：[@eastweb3eth](https://x.com/eastweb3eth/status/2049665268293783914)  
> 整理时间：2026-04-30  
> 来自翡冷翠

---

## 简介

本文档整理了 GitHub 上热度最高的两个玄学 AI Skill，涵盖八字排盘、奇门遁甲、紫微斗数等传统命理分析工具。这些 Skill 基于 Claude Code 构建，通过结构化 Prompt 和外部计算脚本，将传统术数知识工程化、可复用、可审计。

**⚠️ 免责声明**：本文档内容仅供传统文化学习与娱乐参考，不构成任何现实决策依据。命理学属于传统文化范畴，请理性看待，切勿迷信。

---

## 内容清单总览

| 序号 | Skill 名称 | Stars | 核心体系 | 技术方案 | 主要用途 |
|------|-----------|-------|----------|----------|----------|
| 1 | [赛博算命 Skill](#一赛博算命-skill) | 1.2K | 四柱八字 | Claude Code Skill | 八字排盘、命理分析 |
| 2 | [Numerologist Skills](#二numerologist-skills) | 621 | 奇门遁甲、紫微斗数、四柱八字 | Python CLI + Skill | 单事判断、择时、方位、本命盘解读 |

---

## 一、赛博算命 Skill

**GitHub**: [jinchenma94/bazi-skill](https://github.com/jinchenma94/bazi-skill)  
**Stars**: ⭐ 1.2K  
**License**: MIT

### 1.1 这是什么

基于 Claude Code 的八字排盘与命理分析工具。通过交互式对话收集出生信息，排出四柱八字，参照九本经典命理典籍进行专业分析。

**核心洞察**：
> 这不是让 AI"学会"算命，而是通过结构化 Prompt 约束提问顺序和输出边界，用 References 固定术语、口径和判断顺序，让整个过程更透明、可审计。

### 1.2 功能特性

| 功能模块 | 说明 |
|----------|------|
| **信息收集** | 逐步收集姓名、阳历/农历生日、出生时辰、性别、出生地等信息 |
| **排盘计算** | 自动排出年柱、月柱、日柱、时柱，计算大运与流年 |
| **综合分析** | 日主强弱、十神关系、五行平衡、格局判定、大运流年解读 |
| **生活建议** | 事业、感情、健康等方面的参考建议 |

### 1.3 安装使用

```bash
# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/jinchenma94/bazi-skill .claude/skills/bazi

# 或安装到全局（所有项目都能用）
git clone https://github.com/jinchenma94/bazi-skill ~/.claude/skills/bazi
```

**触发关键词**：
`算八字` `看八字` `批八字` `排八字` `四柱` `命盘` `算命` `排盘` `bazi`

触发后，Skill 会逐步引导你提供出生信息，然后进行排盘和综合分析。

### 1.4 参考典籍

| 典籍 | 简称 | 主要内容 |
|------|------|----------|
| 《穷通宝典》 | 论日主调候 | 五行调候用神 |
| 《三命通会》 | 论格局神煞 | 格局判定与神煞 |
| 《滴天髓》 | 论五行旺衰 | 五行旺衰分析 |
| 《渊海子平》 | 论十神六亲 | 十神关系与六亲 |
| 《千里命稿》 | 论命例实证 | 命例实证分析 |
| 《协纪辨方书》 | 论择日神煞 | 择日神煞规则 |
| 《果老星宗》 | 论星命合参 | 星命合参方法 |
| 《子平真诠》 | 论用神格局 | 用神与格局详解 |
| 《神峰通考》 | 论命理辨误 | 命理辨析与勘误 |

### 1.5 项目结构

```
bazi-skill/
├── SKILL.md                        # Skill 入口
├── references/                     # 参考文件
│   ├── wuxing-tables.md            # 五行、天干地支、十神参考表
│   ├── shichen-table.md            # 时辰对照表、日上起时法
│   ├── dayun-rules.md              # 大运顺逆排规则、起运年龄计算
│   └── classical-texts.md          # 九本经典典籍核心规则摘要
├── LICENSE
└── README.md
```

---

## 二、Numerologist Skills

**GitHub**: [FANzR-arch/Numerologist_skills](https://github.com/FANzR-arch/Numerologist_skills)  
**Stars**: ⭐ 621

### 2.1 这是什么

AI 术数工程化项目，将传统术数相关的 AI skill 拆成可审计、可复用、可逐步扩展的工程模块。目标不是把模型包装成"更会玄学"，而是尽量减少它在排盘、流派口径、步骤顺序和解释链路上的幻觉。

**核心洞察**：
> "与其让 LLM 在'似懂非懂'的状态里硬着头皮往下说，不如把关键步骤拆开：用 Prompt 约束控制提问顺序和输出边界，用 References 固定术语、口径和判断顺序，用外部脚本承接刚性计算。"

### 2.2 当前包含的 Skills

| 目录 | 体系 | 主要用途 | 固定计算方式 |
|------|------|----------|--------------|
| `qimen-dunjia/` | 奇门遁甲 | 单事判断、择时、方位、趋吉避凶 | Python CLI：`scripts/qimen_cli.py` |
| `ziwei-doushu/` | 紫微斗数 | 本命盘结构解读、宫位分析、大限流年 | 规则与 references 驱动 |
| `bazi/` | 四柱八字 | 日主强弱、格局、十神、大运流年 | 规则与 references 驱动 |

### 2.3 设计原则

1. **先追问，再输出** — 信息不全时，优先补参数，不硬排盘
2. **确定性计算外包** — 历法换算、固定排盘、结构化计算，优先交给脚本或可信排盘结果
3. **先声明口径，再做结论** — 流派、换日规则、闰月归属、默认规则都要说清楚
4. **只给结构化参考** — 健康、法律、财务等高风险场景不替代现实专业建议

### 2.4 快速上手

**奇门遁甲计算脚本**：

```bash
pip install -r qimen-dunjia/scripts/requirements.txt
python qimen-dunjia/scripts/qimen_cli.py --input tmp/qimen_input.json --output tmp/qimen_output.json
```

### 2.5 仓库结构

```
Numerologist_skills/
├── SKILL.md              # 主技能说明、触发条件、工作流、输出约束
├── references/           # 规则集、术语表、示例、口径说明
│   ├── qimen-dunjia/     # 奇门遁甲参考资料
│   ├── ziwei-doushu/     # 紫微斗数参考资料
│   └── bazi/             # 四柱八字参考资料
└── scripts/              # 刚性计算脚本
    └── qimen_cli.py      # 奇门遁甲 CLI 计算工具
```

---

## 三、两个项目的对比分析

| 维度 | 赛博算命 Skill | Numerologist Skills |
|------|---------------|---------------------|
| **Stars** | 1.2K (更高热度) | 621 |
| **技术栈** | Claude Code Skill | Python CLI + Skill |
| **术数体系** | 四柱八字 | 奇门遁甲 + 紫微斗数 + 四柱八字 |
| **设计哲学** | 交互式对话 + 典籍参考 | 工程化拆分 + 刚性计算 |
| **适用场景** | 个人命理咨询 | 单事判断、择时、方位选择 |
| **计算方式** | 规则驱动 | Python 脚本 + 规则驱动 |
| **透明度** | 引用九本典籍 | 可审计、可复用、版本边界清晰 |

---

## 四、适用场景

### 适合谁使用

- **传统文化爱好者** — 想系统学习八字、奇门遁甲、紫微斗数等传统术数知识
- **AI 开发者** — 研究如何用结构化 Prompt 约束 LLM 输出，减少幻觉
- **产品经理** — 了解 AI 在垂直领域的应用方式，学习可审计 AI 系统的设计思路
- **Claude Code 用户** — 想在自己的工作流中加入有趣的 Skill

### 使用建议

1. **学习目的** — 把这两个 Skill 当作传统术数的"结构化教材"，通过交互式对话了解命理体系的基本概念
2. **研究目的** — 学习其设计原则：Prompt 约束、References 固定、外部脚本承接刚性计算
3. **娱乐目的** — 仅供娱乐参考，切勿用于重大决策

---

## 五、资源汇总

### GitHub 仓库

| 项目 | 链接 | 说明 |
|------|------|------|
| 赛博算命 Skill | [jinchenma94/bazi-skill](https://github.com/jinchenma94/bazi-skill) | 八字排盘与命理分析 |
| Numerologist Skills | [FANzR-arch/Numerologist_skills](https://github.com/FANzR-arch/Numerologist_skills) | 奇门遁甲、紫微斗数、四柱八字 |

### 相关技术

- **Claude Code** — Anthropic 的 CLI 编程助手，支持自定义 Skill
- **AgentSkills** — Claude Code 的 Skill 规范标准

### 值得关注

- **[@eastweb3eth](https://x.com/eastweb3eth)** — Web3 | 美股 | AI，持续分享有用有趣的工具和项目

---

## 六、快速参考

### 赛博算命 Skill 安装命令
```bash
mkdir -p .claude/skills
git clone https://github.com/jinchenma94/bazi-skill .claude/skills/bazi
```

### 触发关键词
```
算八字、看八字、批八字、排八字、四柱、命盘、算命、排盘、bazi
```

### Numerologist Skills 奇门遁甲计算
```bash
pip install -r qimen-dunjia/scripts/requirements.txt
python qimen-dunjia/scripts/qimen_cli.py   --input tmp/qimen_input.json   --output tmp/qimen_output.json
```

---

*来自翡冷翠*
