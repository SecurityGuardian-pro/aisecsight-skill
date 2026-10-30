# Changelog

本项目的版本号跟随 Skill 文件（`aisecsight/SKILL.md`）的接口约定。

## v1.0.0 — 2026-10-30

首个正式发布。

**Skill**
- 以开放格式发布 `SKILL.md`（YAML 头 + 使用说明），可直接放进 Claude Code、Codex、Cursor、Gemini CLI、WorkBuddy 等 Agent 的 skills 目录。
- 覆盖 12 个匿名只读接口：法规检索、法规详情、法规关系、处罚量化、合规问答、Top 10、安全事件、五类动态、每周要点、接口索引。
- 写入 6 条回答约束：先查再答、必注时间、必给出处、金额看条款、id 不许猜、结尾免责。

**仓库**
- 新增 `scripts/install.sh` / `install.ps1`：自动探测 skills 目录，下载并校验 YAML 头，装完自动跑自检。
- 新增 `scripts/verify.py`：11 项接口检查（含 `ETag` / `304` 协商缓存），只依赖 Python 标准库。
- 新增 `examples/prompts.md`：七类提问示例与期望回答形态。
- 新增公众号二维码、关注卡与仓库社交预览图。
- 新增 GitHub Actions：每次推送校验 SKILL.md 前置字段并跑接口冒烟测试。

**数据基线**
- 法规库 85 部（欧盟 10 · 中国 25 · 美国 26 · 亚太 / 国际 / 其他），状态整体核对至 2026-10-13。
- 安全事件 29 起（2023 年以来），每条附一手信源。
- 外币折算基准：中国外汇交易中心 2026-09-30 中间价。
