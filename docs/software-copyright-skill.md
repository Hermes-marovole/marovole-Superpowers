# Software Copyright Skill - 软件著作权申请材料生成工具

> 来源：[https://github.com/Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill)
> 整理时间：2026-05-01
> 来自翡冷翠

---

## 简介

**Software Copyright Skill** 是一个开源的 Codex Skill，专门用于生成中文软件著作权（软著）申请所需的全套材料。这个项目解决了开发者在申请软著时面临的核心痛点：繁琐的材料整理工作。

软件著作权申请本身不神秘，真正复杂的是整理材料——申请表字段要写对，操作手册要像样，代码材料要按规则截取，且软件名称、版本号、页数需要保持一致。很多开发者最终会把这件事交给付费代办服务，花钱买的往往只是文档整理工作。

这个 Skill 的目标很明确：**让开发者不用再为整理软著材料额外付费**，也不用把项目代码和产品细节交给外部商家来回沟通。

---

## 核心功能

| 功能模块 | 说明 |
|---------|------|
| **自动生成全套资料** | 从项目分析、业务理解、申请表信息、操作手册到代码材料，一套流程跑完 |
| **从真实源码抽取** | 代码材料只来自开发者已有项目，禁止 AI 编造源码 |
| **自动处理代码分页** | 按「前 30 页 / 后 30 页」规则生成；不足 60 页时生成全部代码 |
| **智能操作手册** | 先理解项目业务、页面和功能，再写面向审核员的操作说明 |
| **申请表字段整理** | 统一生成到 `申请表信息.txt`，官网填报时可对照复制 |
| **多节点人工确认** | 业务口径、申请表字段、代码选择、截图方式、最终草稿都需确认 |
| **Word/TXT 一键输出** | 生成操作手册 DOCX、代码材料 DOCX 和申请表 TXT |
| **本地生成，资料可控** | 所有材料留在本地，方便审阅、修改和归档 |

---

## 项目信息

| 属性 | 内容 |
|------|------|
| **项目名称** | Software Copyright Materials Skill |
| **作者** | Fokkyp |
| **开源协议** | MIT License |
| **适用平台** | Codex |
| **主要语言** | Python 3 |
| **仓库地址** | https://github.com/Fokkyp/SoftwareCopyright-Skill |

---

## 目录结构

```
SoftwareCopyright-Skill/
├── docs/
│   └── screenshots/          # 演示截图
│       ├── demo-1.png ~ demo-6.png
│       └── 著作权申请表.png
├── software-copyright-materials/   # 真正的 Skill 目录
│   ├── SKILL.md              # Skill 入口文件
│   ├── agents/               # Agent 配置
│   ├── references/           # 参考资料
│   ├── scripts/              # Python 脚本
│   └── vendor/               # 第三方工具（DOCX 生成）
└── 生成demo/
    └── 软件著作权申请资料/    # 示例输出
        ├── 草稿/
        └── 正式资料/
            ├── 申请表信息.txt
            ├── 软件名称_操作手册.docx
            ├── 软件名称-代码(前30页).docx
            └── 软件名称-代码(后30页).docx
```

---

## 安装方法

### 第一步：下载代码

**使用 Git：**
```bash
git clone https://github.com/Fokkyp/SoftwareCopyright-Skill.git
cd SoftwareCopyright-Skill
```

**不使用 Git：**
打开 GitHub 仓库页面 → 点击 `Code` → 点击 `Download ZIP` → 解压后进入目录

### 第二步：安装到 Codex

将 `software-copyright-materials/` 目录复制到 Codex 的 skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R software-copyright-materials ~/.codex/skills/
```

安装完成后应看到：
```
~/.codex/skills/software-copyright-materials/SKILL.md
```

### 第三步：重启 Codex

重新打开 Codex 会话或刷新技能列表，然后在项目中提出「生成软著申请资料」即可使用。

### 安装到特定项目

如果只想让某个项目使用该 Skill：

```bash
PROJECT_DIR="<你的项目目录>" && \
git clone https://github.com/Fokkyp/SoftwareCopyright-Skill.git && \
mkdir -p "$PROJECT_DIR/.codex/skills" && \
cp -R SoftwareCopyright-Skill/software-copyright-materials "$PROJECT_DIR/.codex/skills/"
```

---

## 使用方法

安装完成后，在 Codex 中打开需要生成软著资料的项目，然后说：

```
使用 software-copyright-materials 生成当前项目的软件著作权申请资料
```

Codex 会按流程引导填写信息、确认草稿，并在当前项目目录下生成 `软件著作权申请资料/`。

---

## 完整工作流程

```
1. 环境检查 → 2. 项目定位 → 3. 项目分析 → 4. 业务理解 → 5. 字段确认
    ↓
6. 代码文件选择 → 7. 生成 Markdown 草稿 → 8. 截图获取 → 9. 用户确认 → 10. 生成 Word/TXT
```

### 各阶段详情

#### 1. 环境检查
- 检查 Markdown 草稿、TXT、基础 DOCX 是否可用
- 检查完整 DOCX OpenXML 环境（需要 .NET SDK）
- 如缺失 .NET SDK，用户可选择安装或使用基础兜底方案

#### 2. 项目定位
- 扫描当前目录，避开本 skill、node_modules、构建产物
- 找到最可能的项目根目录
- 多个候选时询问用户选择

#### 3. 项目分析
分析内容包括：
- `package.json`、README、脚本命令、依赖
- 前端框架和主要编程语言
- 入口文件、路由、页面、组件、接口、状态管理
- 源码文件数量和源程序行数
- 软件名称候选、主要功能候选

#### 4. 业务理解
模型阅读项目文档和源码后，生成：
- 产品定位
- 面向行业/领域
- 目标用户
- 核心价值
- 主要业务功能
- 典型操作流程
- 申请表建议口径
- 操作手册结构建议

**必须用户确认后才能继续。**

#### 5. 字段确认
需要确认的字段：
- 软件全称
- 版本号（如项目版本 < V1.0，需确认是否写 V1.0）
- 著作权人
- 开发完成日期
- 首次发表日期或未发表
- 开发/运行硬件环境
- 开发/运行操作系统
- 开发工具（IDE/编辑器）
- 运行支撑环境（Node.js、Python、Docker 等）

#### 6. 代码文件选择
- 生成候选文件清单
- 模型根据业务理解选择最能体现软件功能的源码
- 优先抽取：前端入口、路由、页面、核心组件、接口封装、状态管理
- 用户确认选择后抽取

#### 7. 生成 Markdown 草稿
生成：
- `草稿/业务理解.md`
- `草稿/申请表信息.md`
- `草稿/代码-前30页.md` / `草稿/代码-后30页.md`（或全部）
- `草稿/操作手册.md`（含自检记录）

#### 8. 截图获取
三种方式可选：
1. **Chrome DevTools MCP** - 适合 Web 项目
2. **Codex Computer Use** - 适合桌面应用
3. **用户自行截图** - 手动放入指定目录

如跳过截图，操作手册保留截图预留位置。

#### 9. 用户确认 Markdown
检查要点：
- 软件名称和版本号一致性
- 业务理解准确性
- 代码材料来源真实性
- 操作手册可读性
- 截图完整性

#### 10. 生成正式 Word/TXT
输出：
- `正式资料/申请表信息.txt`
- `正式资料/<软件全称>-代码(前30页).docx`
- `正式资料/<软件全称>-代码(后30页).docx`（或全部）
- `正式资料/<软件全称>_操作手册.docx`
- `正式资料/生成报告.md`

---

## 官网填报指南

### 官方入口

| 平台 | 地址 |
|------|------|
| 中国版权保护中心 | https://www.ccopyright.com.cn/ |
| 著作权登记系统 | https://register.ccopyright.com.cn/login.html |
| 法规依据 | https://www.gov.cn/zhengce/2002-02/20/content_5724627.htm |

### 申请流程

1. 打开中国版权保护中心官网，进入著作权登记系统
2. 注册/登录并完成实名认证
3. 选择「计算机软件著作权登记申请」
4. 在线填写申请表（对照本工具生成的 `申请表信息.txt` 复制）
5. 上传申请材料（DOCX 需转换为 PDF）
6. 提交申请并查看受理结果

### 文件使用说明

| 文件 | 用途 | 提交方式 |
|------|------|---------|
| `申请表信息.txt` | 填报辅助 | 对照复制到官网 |
| `操作手册.docx` | 软件说明文档 | 转换为 PDF 后上传 |
| `代码(前30页).docx` | 代码鉴别材料 | 转换为 PDF 后上传 |
| `代码(后30页).docx` | 代码鉴别材料 | 转换为 PDF 后上传 |

---

## 技术特点

### 代码材料真实性保障

依据软件著作权申请材料要求，代码鉴别材料应来自申请软件本身。本 Skill：
- ❌ 不通过 AI 生成项目代码
- ❌ 不编造不存在的源码内容
- ✅ 从已有项目中选择代码文件
- ✅ 提取真实的源代码内容
- ✅ 生成代码提取清单用于追溯

### 智能内容生成

- 业务理解基于模型对项目的深度分析
- 操作手册避免「AI 味」和空泛套话
- 每段内容都能回答「这个功能具体做什么、用户看见什么、操作后有什么结果」
- 自检记录确保质量

---

## 运行要求

### 必需环境
- **Codex**：本仓库提供的是 Codex Skill
- **Python 3**：用于分析项目、生成草稿、抽取代码
- **可读取的项目源码**：代码材料必须从真实项目中抽取

### 可选环境
- **.NET SDK**：启用更完整的 DOCX OpenXML 生成
- **Chrome DevTools MCP**：自动截取网页截图
- **Codex Computer Use**：通过桌面界面操作并截图

---

## 免责声明

> **本项目完全免费。请不要相信任何使用本项目包装出来的付费服务。**

使用者需自行核对生成材料是否符合实际项目和官网当前要求。本 Skill 仅辅助整理文档格式，不保证申请一定通过。

---

## 相关链接

- **项目主页**：https://github.com/Fokkyp/SoftwareCopyright-Skill
- **Linux Do 社区**：https://linux.do/
- **V2EX**：https://www.v2ex.com/

---

*来自翡冷翠*
