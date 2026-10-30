# AISecSight Skill · 全球 AI 安全洞察

**简体中文** · [English](README.en.md)

[![license](https://img.shields.io/badge/license-MIT-1a7a5a)](LICENSE)
[![skill](https://img.shields.io/badge/skill-v1.0.0-1a7a5a)](aisecsight/SKILL.md)
[![api](https://img.shields.io/badge/API-anonymous%20read--only-1a7a5a)](https://aisecsight.com/api/v1)
[![stars](https://img.shields.io/github/stars/SecurityGuardian-pro/aisecsight-skill?color=1a7a5a)](https://github.com/SecurityGuardian-pro/aisecsight-skill/stargazers)

**装一次 Skill，之后问 AI 法规就自动查、自动给条款和出处，不用每次贴提示词。**

> **全球 AI 安全洞察**：85 部法规与标准 · 29 起真实安全事件 · 31 部法规的逐档罚则 · 62 个信源近乎实时更新

<table>
<tr>
<td width="62%" valign="top">

把 [AISecSight](https://aisecsight.com) 整理的全球 AI 安全数据库接进你的 Agent——不只是法规条文，还有**该先读哪几部**、**真实出过什么事**、**违规到底罚多少**。

装好之后，你在 Claude Code、Codex、Cursor 里随口问一句「欧盟 AI 法对通用模型提供者的罚款上限是多少」，Agent 会自己调接口取回条款原文再回答，带上核对日期和官方链接。

- 85 部法规与标准（含 2 部已失效备查），覆盖欧盟、中国、美国、亚太与国际组织
- 29 起真实 AI 安全事件，每条附一手信源
- 31 部法规的罚则逐条拆开，外币统一折算人民币
- 匿名只读接口，不需要 API Key，不收集任何数据

</td>
<td width="38%" valign="top" align="center">

<img src="assets/wechat-qrcode.png" width="180" alt="微信公众号：数字安全守护者">

**微信公众号：数字安全守护者**

扫码关注，法规更新与 AI 安全动态不错过

</td>
</tr>
</table>

---

## 为什么需要它

大模型对 AI 法规的记忆有几个固定毛病，而且都是硬伤：

| 问题 | 典型表现 | 装了 Skill 之后 |
|---|---|---|
| **日期会漂** | 把「2026-08-02 起适用」的条款说成已经全面生效 | 按接口返回的 `stage` / `effective` / `reviewed` 回答 |
| **罚款金额记错** | 欧盟 AI 法只记得「3500 万欧元」，漏掉「或全球营业额 7%，取高者」 | 金额与条款（`tiers[].article`）、原文引文一起给 |
| **修订跟不上** | 不知道欧盟已通过 Digital Omnibus（Reg (EU) 2026/1744）修正 | 法规 `summary` 里逐条写明修正与新的适用日期 |
| **只给结论不给出处** | 无法核对，会议上不敢引用 | 每条都带官方源链接与信源名称 |
| **讲不出案例** | 说「智能体有风险」但举不出真实事件 | 直接调大事记，给日期、经过、一手报道 |

---

## 重点一：Top 10 —— 先读哪几部

合规不是把所有法规读一遍，而是先抓真正有约束力、影响面最大的那几部。这个榜单按**约束力、影响范围、与 AI 安全的直接程度、时效、可操作性**综合排序，2026-10-13 重新评估。

| # | 法规 / 标准 | 状态 | 为什么排在前面 |
|---|---|---|---|
| 1 | 欧盟《人工智能法》 | 分阶段生效（2024 起） | 范式源头：全球首部综合性 AI 立法，风险分级 + GPAI 义务，被多国借鉴 |
| 2 | 《生成式人工智能服务管理暂行办法》 | 已生效（2023-08-15） | 在中国提供生成式 AI 服务最直接的约束性依据：训练数据、标注、内容安全、备案 |
| 3 | NIST 人工智能风险管理框架（AI RMF） | 已发布（2023-01） | 美国无联邦 AI 法，这是联邦层面最主要的安全依据 |
| 4 | ISO/IEC 42001:2023《人工智能 管理体系》 | 已发布（2023-12） | 首个可第三方认证的 AI 管理体系标准，我国等同采用为 GB/T 45081-2024 |
| 5 | 《通用目的人工智能行为准则》 | 已发布（2025-07-10） | 证明 GPAI 义务合规的自愿准则，Anthropic、Google、Microsoft、OpenAI 已签署 |
| 6 | 《人工智能生成合成内容标识办法》 | 已生效（2025-09-01） | 与强制性国标 GB 45438-2025 同日施行，全球最早全面落地的 AI 生成内容标识制度 |
| 7 | ISO/IEC 27090:2026《网络安全 人工智能》 | 已发布（2026-10） | 首部专门针对 AI 系统特有威胁（数据投毒、模型窃取）的国际标准 |
| 8 | OWASP LLM/GenAI 十大安全风险（2026） | 已发布（2026-08） | 威胁建模与验收的业界基线；2026 版首次引入真实事件数据，过度代理升至第 3 |
| 9 | OWASP 智能体应用十大风险（2026） | 已发布（2025-12） | ASI01–ASI10：目标劫持、工具滥用、权限滥用、记忆投毒、失控智能体 |
| 10 | GB/T 45654-2025《生成式人工智能服务安全基本要求》 | 已生效（2025-11-01） | 服务安全评估与备案的技术依据：训练数据全量过滤、生成内容合格率不低于 90% |

> 怎么问：**「AI 合规最该先看哪几部法？给我排个序，说清理由。」** → Agent 调 `/api/v1/top10`，并给每部法规的详情链接。
> 网页版：[aisecsight.com/top10](https://aisecsight.com/top10)

---

## 重点二：大事记 —— 2023 年以来真实发生的 29 起

讲风险最怕空对空。这个库只收真实发生、有据可查的事件，每条附一手来源，可按类别筛。

| 类别 | 起数 | 代表事件 |
|---|---|---|
| AI 用于攻击 | 7 | AI 主导的网络间谍活动、用 Claude Code 勒索 17 家机构 |
| 供应链与基础设施 | 7 | LiteLLM PyPI 投毒、首个在野恶意 MCP 服务器、Nx 供应链攻击 |
| 数据泄露 | 6 | OpenCode 控制台失陷、三星员工把源码贴进 ChatGPT、DeepSeek 数据库裸奔 |
| 智能体失控 | 5 | Replit 智能体删除生产库、OpenClaw 无视停止指令删邮件、Hugging Face 遭自主智能体入侵 |
| 模型与应用漏洞 | 2 | EchoLeak 零点击提示注入、Slack AI 间接提示注入 |
| 深度伪造与诈骗 | 2 | Arup 香港员工被深度伪造视频会议骗走 2 亿港元 |

最近 8 起：

| 日期 | 地区 | 类别 | 事件 |
|---|---|---|---|
| 2026-10-26 | 韩国 | AI 用于攻击 | 首尔警方逮捕用生成式 AI 入侵 90 多家企业的黑客（无 IT 背景，40 多天窃取 820 万条个人信息） |
| 2026-10-21 | 国际 | 供应链 | AI 网关 LiteLLM 的 PyPI 包被投毒，恶意版 v1.107.0 窃取云平台与模型 API 凭据 |
| 2026-10-20 | 国际 | AI 用于攻击 | PHP2Shell：AI 参与发现 PHP 核心预认证 RCE，影响 PHP 5.4 起几乎所有版本 |
| 2026-10-19 | 国际 | 数据泄露 | AI 编程工具 OpenCode 控制台遭入侵，约 1.4% 用户保存的模型 API 密钥可能外泄 |
| 2026-07-16 | 美国 | 智能体失控 | Hugging Face 遭自主 AI 智能体入侵 |
| 2026-07 | 英国 | 智能体失控 | Claude Mythos 5 在英国 AISI 测试中向真实 GitHub 项目植入后门 |
| 2025-11-13 | 国际 | AI 用于攻击 | Anthropic 披露首个大规模 AI 主导的网络间谍活动 |
| 2024-02 | 中国香港 | 深度伪造 | Arup 香港员工遭深度伪造视频会议诈骗 2 亿港元 |

> 怎么问：**「有没有智能体失控的真实案例？挑最严重的三个讲。」** → Agent 调 `/api/v1/incidents?cat=agent`，给日期、经过和一手链接。
> 网页版：[aisecsight.com/incidents](https://aisecsight.com/incidents)

---

## 重点三：处罚量化 —— 到底罚多少

老板只想知道「这事罚多少」。所有最高罚款都按中国外汇交易中心 2026-09-30 中间价折算成人民币，放在一张表里比：

| 法规 | 条款 | 最高处罚 | 折人民币 |
|---|---|---|---|
| 欧盟《人工智能法》 | Art. 99(3) | 3500 万欧元，或全球年营业额 7%，取高者 | ≈ 2.67 亿元 |
| 欧盟 GDPR | Art. 83 | 2000 万欧元，或全球年营业额 4%，取高者 | ≈ 1.52 亿元 |
| 中国《个人信息保护法》 | 第六十六条 | 5000 万元以下，或上一年度营业额 5% 以下 | — |
| 纽约 RAISE 法 | — | 首次 100 万美元，此后每次 300 万美元 | ≈ 2020 万元 |
| 伊利诺伊《人工智能安全措施法》 | SB315 | 首次 100 万美元，此后每次 300 万美元 | ≈ 2020 万元 |
| 纽约《AI 陪伴不安全功能禁令》 | GBL §1802 | 每项违规 2.5 万美元 | ≈ 17 万元 |

共 31 部法规、逐档罚则，每档带条款号、官方原文引文（`quote`）与生效日期。中国《个人信息保护法》的「5000 万元」与「营业额 5%」是并列选项、不是取高者——这类差别只看摘要就会写错。

> 怎么问：**「欧盟和美国州法，AI 违规的最高罚款各是多少？折人民币多少？」** → Agent 调 `/api/v1/penalties`，注明汇率日期。
> 网页版：[aisecsight.com/penalty](https://aisecsight.com/penalty)

---

## 数据从哪来

| 维度 | 情况 |
|---|---|
| 信源 | **62 个**：官方（网信办、全国网安标委、美国联邦公报、欧盟委员会等）+ 机构 + 媒体 |
| 官方优先 | 每条标来源级别，同一件事多家报道只留一条，避免重复 |
| 中文 | 海外内容配中文标题与摘要；机器翻译条目带 `machineTranslated` 标记，涉及措辞以原文为准 |
| 透明 | [`/api/v1/health`](https://aisecsight.com/api/v1/health) 公开每个信源的抓取状态：最近一次检查 2026-10-30，56 正常 / 4 陈旧 / 2 休眠 / 0 失败 |
| 人工核对 | 法规状态定期对照官方原文复核，页面写明核对日期 |
| 更新节奏 | 动态约每小时；法规库人工核对后更新；每周要点每周一生成 |

---

## 快速安装

### 方式一：装成 Skill（推荐，一次装好长期生效）

Skill 就是一个带 YAML 头的 `SKILL.md` 文件夹。装到你的 Agent 读取的 skills 目录里，它就会在遇到相关问题时自动调用。

**① 一键命令（macOS / Linux）**

```bash
SKILLS_DIR="$HOME/.claude/skills"   # 换成你的 Agent 的目录
mkdir -p "$SKILLS_DIR/aisecsight" && \
curl -fsSL https://aisecsight.com/api/v1/skill -o "$SKILLS_DIR/aisecsight/SKILL.md"
```

**② 一键命令（Windows PowerShell）**

```powershell
$dir = "$HOME\.claude\skills"
New-Item -ItemType Directory -Force "$dir\aisecsight" | Out-Null
curl.exe -fsSL https://aisecsight.com/api/v1/skill -o "$dir\aisecsight\SKILL.md"
```

**③ 用本仓库的安装脚本**（会顺手做一次接口连通性自检）

```bash
git clone https://github.com/SecurityGuardian-pro/aisecsight-skill.git
cd aisecsight-skill
./scripts/install.sh          # macOS / Linux
# .\scripts\install.ps1       # Windows PowerShell
```

**④ 手动**：下载 [`aisecsight/SKILL.md`](aisecsight/SKILL.md)，放进 skills 目录下的 `aisecsight/` 文件夹即可。

各 Agent 的 skills 目录：

| Agent | 目录 |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex CLI | `~/.codex/skills/` |
| Cursor | `~/.cursor/skills/` |
| Gemini CLI | `~/.gemini/skills/` |
| WorkBuddy | `~/.workbuddy/skills/` |
| 其他 | 见该 Agent 文档中「skill」目录配置项 |

装完**新开一个会话**再问，Agent 才会加载到新 Skill。

> 官网也提供图形化安装入口（可选安装方式、`SKILL.md` 内容预览、一键复制命令）：
>
> <img src="assets/install-zh.png" width="100%" alt="官网安装入口">

### 方式二：不装 Skill，直接调接口

Skill 本质上只是给 Agent 的一份说明书，接口本身谁都能直接请求：

```bash
# 先读哪几部
curl -s "https://aisecsight.com/api/v1/top10" | jq '.items[] | "\(.rank). \(.name) [\(.status)]"'

# 智能体失控的真实案例
curl -s "https://aisecsight.com/api/v1/incidents?cat=agent" | jq '.items[] | {date, title}'

# 某部法规的罚则
curl -s "https://aisecsight.com/api/v1/laws/euact" | jq '.law.penalty.tiers[] | {article, fine}'
```

### 方式三：什么都不装

把下面这句直接发给任意 Agent，它就能自己接上：

> 请 GET `https://aisecsight.com/api/v1/skill` 读取这份说明书，之后我所有关于 AI 法规的问题都按它来查、来答。

---

## 使用示例

**问：欧盟《人工智能法》里，违反禁止性 AI 实践最高罚多少？**

> 答（依据接口返回，2026-10-21 核对）：违反第 5 条禁止性实践的行政处罚**最高 3500 万欧元，或企业上一财年全球年营业额的 7%，取较高者**（中小企业取较低者）——Art. 99(3)。
>
> - 适用时间：第 5 条禁令自 **2025-02-02** 起适用；第 XII 章罚则自 **2025-08-02** 起适用（Art. 113(a)(b)）。经 Reg (EU) 2026/1744 新增的第 5(1)(ba)(bb) 项（未经同意的私密深度伪造、儿童性虐待材料）自 **2026-12-02** 起适用，同样落入本档。
> - 第二档：违反提供者/部署者义务或第 50 条透明度义务，最高 1500 万欧元或全球营业额 3%，取高者。
> - 折算参考：按中国外汇交易中心 2026-09-30 中间价 1 EUR = 7.6215 CNY，3500 万欧元约合 2.67 亿元人民币。
> - 原文：`eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689`
> - 出处：[aisecsight.com/law/euact](https://aisecsight.com/law/euact)
>
> 仅供研究与合规参考，不构成法律意见；具体以官方原文和专业法律意见为准。

**问：我们接入一个能自动执行操作的智能体，出了事有先例吗？**

> 答：会去大事记里找 `agent` 类事件，按时间返回 Replit 智能体删除生产数据库（2025-07-18）、OpenClaw 无视停止指令删除 200 多封邮件（2026-02-23）、Hugging Face 遭自主智能体入侵（2026-07-16）等，每条附一手报道链接与相关标准（OWASP 智能体十大风险）。

**问：中国对生成式 AI 服务的标识有哪些强制要求？**

> 答：会同时命中《生成式人工智能服务管理暂行办法》《人工智能生成合成内容标识办法》与强制性国标 GB 45438-2025，并逐条给出显式标识、隐式标识（元数据水印）的适用范围与施行日期，附条款出处。
> 出处：[aisecsight.com/api/v1/qa?q=标识](https://aisecsight.com/api/v1/qa?q=标识)

更多示例见 [`examples/prompts.md`](examples/prompts.md)。

---

## 数据覆盖

| 维度 | 情况 |
|---|---|
| 法规库 | **85 部**（欧盟 10 · 中国 25 · 美国 26 · 国际 15 · 亚太 6 · 其他 3），其中 2 部已失效或搁置、保留备查 |
| 类型 | 法律 · 法规与规章 · 政策与行政令 · 标准（12 部）· 框架与指南 · 国际文件 |
| 状态 | 已生效 `inforce` · 已签署 `signed` · 立法中 `pending` · 已失效 `lapsed` |
| 核对日期 | 法规状态整体核对至 **2026-10-13**；单部以该条 `reviewed` 为准（更晚者优先） |
| 安全事件 | 2023 年以来 **29 起**（2026 年 12 起），每条附一手信源 |
| 处罚量化 | **31 部**法规的逐档罚则，汇率基准 2026-09-30 |
| 限制 | 单个 IP 每分钟 60 次，超出返回 `429`，按 `Retry-After` 等待，请勿并发重试 |

---

## 接口一览

全部匿名只读、GET 请求、返回 JSON（UTF-8），无需 API Key。

| 想知道 | 请求 |
|---|---|
| 先读哪几部（含入选理由） | `/api/v1/top10` |
| 真实发生过的 AI 安全事件 | `/api/v1/incidents?cat=agent` |
| 各法规最高处罚与外币折算 | `/api/v1/penalties` |
| 关键词 / 法域 / 类型 / 状态检索 | `/api/v1/laws?q=…&region=eu&kind=标准&stage=inforce` |
| 单部法规详情（要点、义务、罚则、近 90 天报道） | `/api/v1/laws/{id}` |
| 法规之间的关系（上下位 / 冲突 / 影响 / 同源） | `/api/v1/relations?law={id}` |
| 已整理的合规问答（带条款出处） | `/api/v1/qa?q=标识` |
| 治理 / 安全 / 智能体 / 漏洞 / 白皮书动态 | `/api/v1/news?type=governance&limit=10` |
| 上一周要点 | `/api/v1/weekly/latest` |
| 每个信源的抓取状态 | `/api/v1/health` |
| 接口索引 | `/api/v1` |

参数说明：`q` 关键词（多个用空格分隔，需全部命中，中英文皆可）；`region` 取 `intl` / `eu` / `cn` / `us` / `apac` / `other`；`kind` 取 `法律` / `法规与规章` / `政策与行政令` / `标准` / `框架与指南` / `国际文件`；`stage` 取 `inforce` / `signed` / `pending` / `lapsed`；`cat` 取 `attack` / `vuln` / `leak` / `fake` / `agent` / `supply`；`limit` ≤ 100。

响应带 `ETag`，重复请求带 `If-None-Match` 可拿 `304`，省流量也省时间。

---

## 它是怎么保证不瞎编的

SKILL.md 里对 Agent 有几条硬约束，这也是这个 Skill 和「随手问模型」的区别：

1. **先查再答** —— 状态、生效日期、罚款金额一律以接口返回为准，不允许凭记忆补。
2. **必注时间** —— 给 `reviewed` 核对日期或动态的 `date` 发布日期。
3. **必给出处** —— 法规给 `links.page`，动态给 `source` 与 `url`。
4. **金额看条款** —— 以 `tiers` 里的条款、`quote` 原文引文为准；外币按 `penalty.fx` 折算并注明汇率日期。
5. **id 不许猜** —— 只从接口返回里取；查不到就如实说没收录。
6. **结尾免责** —— 仅供研究与合规参考，不构成法律意见。

---

## 项目结构

```
aisecsight-skill/
├── aisecsight/
│   └── SKILL.md            # Skill 本体（装进 skills 目录的就是它）
├── examples/
│   └── prompts.md          # 提问示例，含期望回答要点
├── scripts/
│   ├── install.sh          # macOS / Linux 安装
│   ├── install.ps1         # Windows 安装
│   └── verify.py           # 接口连通性与字段自检
├── assets/
│   ├── wechat-qrcode.png   # 公众号二维码
│   ├── wechat-card.png     # 公众号关注卡
│   ├── social-preview.png  # 仓库社交预览图
│   └── logo.png
├── CHANGELOG.md
├── NOTICE.md               # 许可范围、第三方内容与数据时点
└── LICENSE
```

## 自检

装完想确认能不能用：

```bash
python scripts/verify.py --etag
```

会依次检查接口索引、法规检索、法规详情罚则、合规问答、动态、每周要点，打印每项的 HTTP 状态与关键字段是否齐全。

---

## 常见问题

**Q：需要 API Key 吗？要付费吗？**
不需要 Key，也不需要注册。接口匿名只读，公开数据。

**Q：会被限流吗？**
单 IP 每分钟 60 次。Agent 正常问答远用不到这个量；触发 `429` 就按 `Retry-After` 等，不要并发重试。

**Q：装了没反应？**
确认三点：目录名是 `aisecsight/`、文件是 `SKILL.md`（大写）、YAML 头完整；然后**新开会话**。部分 Agent 需要重启。

**Q：模型安全榜、智能体攻防榜能查吗？**
不能。排行榜在网站上直接看，接口目前只提供法规、罚则、问答、事件与动态，不提供榜单数据——SKILL.md 里也写明了这一点，Agent 不会硬编。

**Q：数据准不准，能不能直接拿去合规？**
法规状态经人工核对并标注日期，每条都链到官方原文。但它是研究工具，**不构成法律意见**，正式结论请以官方原文和专业法律意见为准。

**Q：我提需求 / 发现错漏怎么办？**
开 [Issue](https://github.com/SecurityGuardian-pro/aisecsight-skill/issues)，或到公众号后台留言。

---

## 关注公众号

<table>
<tr>
<td width="58%" valign="top">

**数字安全守护者** —— 每天追踪官方、机构与媒体信源，筛掉重复和噪音，把新规、官方原文和真正值得看的几条留下来；法规状态定期对照原文人工复核。

希望这个小站，能帮做 AI 合规、法务和安全的同行，少花点时间找信息。

内容有误或想补充法规、信源，欢迎在公众号后台留言。

📖 推荐阅读：[《安利给安全同行：一个查 AI 法规、看 AI 安全动态、评 AI 模型安全的平台》](https://mp.weixin.qq.com/s/xO4QxcR7paP5rrAIZ3Zq_w)

</td>
<td width="42%" align="center">

<img src="assets/wechat-card.png" width="100%" alt="微信公众号：数字安全守护者">

</td>
</tr>
</table>

---

## 免责声明

本项目与 [AISecSight](https://aisecsight.com) 提供的内容仅供研究与合规参考，不构成法律意见；具体以官方原文和专业法律意见为准。引用请注明 AISecSight 及原始来源。动态类内容版权归各原始来源所有，本项目只提供标题、摘要与原文链接。

## License

[MIT](LICENSE) © 2026 AISecSight
