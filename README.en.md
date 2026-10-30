# AISecSight Skill · Global AI Security Law Lookup

[![license](https://img.shields.io/badge/license-MIT-1a7a5a)](LICENSE)
[![skill](https://img.shields.io/badge/skill-v1.0.0-1a7a5a)](aisecsight/SKILL.md)
[![api](https://img.shields.io/badge/API-anonymous%20read--only-1a7a5a)](https://aisecsight.com/api/v1)

**Install once. Your agent stops guessing about AI regulations and starts citing articles, dates, and sources.**

An [Agent Skill](https://aisecsight.com/connect) that connects Claude Code, Codex, Cursor, Gemini CLI or WorkBuddy to [AISecSight](https://aisecsight.com) — a curated database of global AI laws, standards, penalty clauses, and governance news.

- **85 laws and standards** across the EU, China, the US, APAC and international bodies
- **29 real AI security incidents** since 2023, each with a primary source
- **Penalties broken down article by article** for 31 laws, FX-normalised to CNY
- **Reviewed dates and official sources** on every answer
- **Anonymous read-only API**, no key, no signup, no tracking

## Start here: the Top 10

Ranked by binding force, scope, direct relevance to AI security, currency and actionability (re-assessed 2026-10-13).

| # | Law / standard | Status |
|---|---|---|
| 1 | EU AI Act | Phased (from 2024) |
| 2 | China: Interim Measures for Generative AI Services | In force (2023-08-15) |
| 3 | NIST AI Risk Management Framework | Published (2023-01) |
| 4 | ISO/IEC 42001:2023 AI management systems | Published (2023-12) |
| 5 | EU Code of Practice for General-Purpose AI | Published (2025-07-10) |
| 6 | China: Measures for Labelling AI-Generated Content | In force (2025-09-01) |
| 7 | ISO/IEC 27090:2026 AI security threats | Published (2026-10) |
| 8 | OWASP LLM/GenAI Top 10 (2026) | Published (2026-08) |
| 9 | OWASP Agentic AI Top 10 (2026) | Published (2025-12) |
| 10 | GB/T 45654-2025 Generative AI service security | In force (2025-11-01) |

## Real incidents, not hypotheticals

29 documented events, filterable by category, each with a primary source.

| Category | Count | Example |
|---|---|---|
| AI used for attacks | 7 | First large-scale AI-orchestrated cyber-espionage campaign (Anthropic, 2025-11) |
| Supply chain & infrastructure | 7 | LiteLLM PyPI package poisoned to steal model API credentials (2026-10) |
| Data leaks | 6 | OpenCode console breach exposed users' model API keys (2026-10) |
| Agent failures | 5 | Replit agent deleted a production database during a code freeze (2025-07) |
| Model & app vulnerabilities | 2 | EchoLeak: zero-click prompt injection in Microsoft 365 Copilot (2025-06) |
| Deepfakes & fraud | 2 | Arup Hong Kong employee defrauded of HK$200M via deepfake video call (2024-02) |

Recent: a self-taught hacker with no IT background used AI coding agents to breach 60+ companies and steal 8.2M records (Seoul, 2026-10-26); Hugging Face was breached by an autonomous AI agent (2026-07-16).

## What non-compliance actually costs

| Law | Provision | Maximum penalty | ≈ CNY |
|---|---|---|---|
| EU AI Act | Art. 99(3) | €35M or 7% of worldwide turnover, whichever is higher | ¥267M |
| EU GDPR | Art. 83 | €20M or 4% of worldwide turnover, whichever is higher | ¥152M |
| China PIPL | Art. 66 | Up to ¥50M **or** up to 5% of prior-year turnover (alternatives, not the higher) | — |
| New York RAISE Act | — | $1M first violation, $3M each subsequent | ¥20.2M |

FX basis: CFETS central parity, 2026-09-30.

## Install

```bash
# macOS / Linux
SKILLS_DIR="$HOME/.claude/skills"
mkdir -p "$SKILLS_DIR/aisecsight" && \
curl -fsSL https://aisecsight.com/api/v1/skill -o "$SKILLS_DIR/aisecsight/SKILL.md"
```

```powershell
# Windows PowerShell
$dir = "$HOME\.claude\skills"
New-Item -ItemType Directory -Force "$dir\aisecsight" | Out-Null
curl.exe -fsSL https://aisecsight.com/api/v1/skill -o "$dir\aisecsight\SKILL.md"
```

Or clone and run the installer, which also verifies connectivity:

```bash
git clone https://github.com/SecurityGuardian-pro/aisecsight-skill.git
cd aisecsight-skill && ./scripts/install.sh      # .\scripts\install.ps1 on Windows
```

Skills directories by agent: Claude Code `~/.claude/skills/` · Codex `~/.codex/skills/` · Cursor `~/.cursor/skills/` · Gemini CLI `~/.gemini/skills/` · WorkBuddy `~/.workbuddy/skills/`. **Start a new session** after installing.

No skill support? Just tell your agent: *"GET https://aisecsight.com/api/v1/skill and follow it for all my AI-regulation questions."*

## Ask it

- What are the transparency obligations for high-risk AI systems under the EU AI Act?
- What is the maximum fine under the EU AI Act, and how many tiers are there?
- Which parts of the EU AI Act are already applicable, and which dates are still ahead?
- How do China and the EU differ on deepfake labelling requirements?
- How should ISO/IEC 42001 and the NIST AI RMF be used together?
- What real-world agent failures have happened since 2023?
- What moved in AI governance this week?

## API

All endpoints are anonymous, read-only, `GET`, JSON (UTF-8).

| What you want | Request |
|---|---|
| Search by keyword / region / kind / stage | `/api/v1/laws?q=deepfake&region=eu` |
| One law: key points, obligations, penalties, recent coverage | `/api/v1/laws/{id}` |
| Relationships between laws | `/api/v1/relations?law={id}` |
| Max penalties and FX conversion | `/api/v1/penalties` |
| Curated compliance Q&A with citations | `/api/v1/qa?q=labelling` |
| Top 10 laws and standards | `/api/v1/top10` |
| Major AI security incidents | `/api/v1/incidents?cat=attack` |
| News: governance / safety / agent / vuln / whitepaper | `/api/v1/news?type=governance&limit=10` |
| Last week's highlights | `/api/v1/weekly/latest` |
| Endpoint index | `/api/v1` |

Rate limit: 60 requests/minute per IP (`429` + `Retry-After`). Responses carry `ETag`; replay with `If-None-Match` for `304`.

```bash
curl -s "https://aisecsight.com/api/v1/laws/euact" | jq '.law.penalty.tiers[] | {article, fine}'
```

## Verify

```bash
python scripts/verify.py --etag
```

Checks 11 endpoints plus ETag / 304 negotiation, standard library only.

## Follow us

<table>
<tr>
<td width="58%" valign="top">

**数字安全守护者** (Digital Security Guardian) — a Chinese WeChat account that tracks official, institutional and media sources daily, filters out the noise, and keeps only the new rules, primary texts and items genuinely worth reading.

Content is in Chinese.

</td>
<td width="42%" align="center">

<img src="assets/wechat-card.png" width="100%" alt="WeChat: 数字安全守护者">

</td>
</tr>
</table>

## Disclaimer

Content is for research and compliance reference only and does not constitute legal advice. Official primary sources and qualified counsel prevail. Quotes should credit AISecSight and the original source. News items remain the copyright of their publishers; this project provides titles, summaries and links only.

## License

[MIT](LICENSE) © 2026 AISecSight
