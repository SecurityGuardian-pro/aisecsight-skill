---
name: aisecsight
description: 查询 AISecSight（aisecsight.com）整理的全球 AI 安全法规与标准、处罚条款、合规问答、AI 治理与安全动态和 AI 安全大事记。用户问到 AI 相关法律法规（如欧盟《人工智能法》、中国生成式 AI 管理办法与标识办法、美国联邦与州 AI 法）、合规义务、生效日期、罚款金额、AI 标准（ISO/IEC 42001、NIST AI RMF、GB/T、OWASP LLM 十大风险）、大模型或智能体安全事件、最近的 AI 监管动态时使用。
---

# AISecSight · AI 安全法规与动态查询

## 什么时候用

- 问某部 AI 法规或标准的内容、状态、生效日期、义务、处罚。
- 比较不同国家或地区的 AI 监管要求，或问某类产品（生成式 AI、深度合成、前沿模型、智能体）要遵守哪些规定。
- 问最近的 AI 治理、监管、立法动态，或大模型与智能体安全事件。

不用安装别的东西：用你能用的网页抓取或 HTTP 请求工具（如 `curl`）对下面的地址发 GET 请求即可。

AISecSight（https://aisecsight.com）整理全球 AI 安全相关的法律法规、处罚条款、AI 治理动态、AI 安全动态（大模型与智能体安全事件）和每周要点。法规库目前 85 部，法规状态核对至 2026-10-13（单部法规的 reviewed 字段更晚的，以该字段为准）。

下面的接口全部匿名只读、不需要 API Key，用 GET 请求，返回 JSON（UTF-8）。

## 按问题选地址

| 想知道 | 请求 |
|---|---|
| 某个主题或关键词有哪些法规 | `https://aisecsight.com/api/v1/laws?q=深度伪造` |
| 某个国家或地区的法规 | `https://aisecsight.com/api/v1/laws?region=cn`（region 取 intl 国际、eu 欧盟、cn 中国、us 美国、apac 亚太、other 其他国家；标准与框架按发布方归入各法域） |
| 某类法规（如美国州法、中国国家标准） | `https://aisecsight.com/api/v1/laws?region=us&type=州法`（kind 取 法律 / 法规与规章 / 政策与行政令 / 标准 / 框架与指南 / 国际文件，如 /api/v1/laws?region=cn&kind=标准；stage 取 inforce 已生效 / signed 已签署待生效 / pending 立法进行中 / lapsed 已失效或搁置） |
| 某部法规的要点、处罚条款和近期报道 | `https://aisecsight.com/api/v1/laws/{id}`（id 先用 laws?q= 查到） |
| 某部法规和哪些法规有关、是什么关系（上下位、冲突、影响、同源） | `https://aisecsight.com/api/v1/relations?law={id}` |
| 各法规的最高处罚、按条款的罚则 | `https://aisecsight.com/api/v1/penalties` |
| 具体的合规问题（义务、处罚、跨境适用、标识等） | `https://aisecsight.com/api/v1/qa?q=标识`（已整理的问答带条款出处，可按 country、law、category 筛选） |
| 最重要的 AI 法规和标准有哪些 | `https://aisecsight.com/api/v1/top10` |
| 2023 年以来真实发生的重大 AI 安全事件 | `https://aisecsight.com/api/v1/incidents`（cat 取 attack 用于攻击 / vuln 漏洞 / leak 数据泄露 / fake 深度伪造 / agent 智能体失控 / supply 供应链，每条附一手来源） |
| 最近的 AI 政策、监管、立法动态 | `https://aisecsight.com/api/v1/news?type=governance&limit=10` |
| 最近的大模型安全事件与研究 | `https://aisecsight.com/api/v1/news?type=safety&limit=10` |
| 智能体（Agent）安全 | `https://aisecsight.com/api/v1/news?type=agent` |
| AI 相关漏洞与安全事件 | `https://aisecsight.com/api/v1/news?type=vuln` |
| AI 安全白皮书、报告与技术规范 | `https://aisecsight.com/api/v1/news?type=whitepaper` |
| 和某部法规有关的动态 | `https://aisecsight.com/api/v1/news?law={id}` |
| 上一周的重点 | `https://aisecsight.com/api/v1/weekly/latest` |

参数：q 是关键词，多个词用空格分隔、需全部命中，中英文都可以；limit 是条数上限。完整接口列表见 `https://aisecsight.com/api/v1`。

## 回答时请这样做

- 先查再答：法规状态、生效日期、罚款金额都以接口返回为准，不要凭记忆补充。
- 注明时间：说明法规核对日期（reviewed）或动态的发布日期（date）。
- 给出处：法规给出名称和 `links.page` 链接；动态给出来源名称（source）和原文链接（url）。
- 处罚金额以 `tiers` 里的条款和原文引文（quote）为准；外币按 `penalty.fx`（单部法规里已附上，与 `/api/v1/penalties` 的 fx 相同）的汇率折算，并注明汇率日期。
- 带 `titleOriginal` 或 `machineTranslated` 的动态是机器翻译，涉及具体措辞时以原文为准。
- id 只从接口返回里取，不要猜；查不到就如实说明没有收录。
- 结尾提醒：仅供研究与合规参考，不构成法律意见；具体以官方原文和专业法律意见为准。引用请注明 AISecSight 及原始来源。

## 用得省

- 响应带 ETag，下次带 If-None-Match，没有变化时返回 304。
- 动态大约每小时更新；法规库人工核对后更新；每周要点每周一生成。
- 单个 IP 每分钟最多 60 次，超出返回 429，请按 Retry-After 等待，不要并发重试。

## 目前不提供

- 模型与智能体榜单数据。
- 动态的原文全文：只有标题、摘要和原文链接，原文版权归各来源所有。
- 写入、推送和 MCP。
