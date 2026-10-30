# AISecSight Skill · Global AI Security Law Lookup

[![license](https://img.shields.io/badge/license-MIT-1a7a5a)](LICENSE)
[![skill](https://img.shields.io/badge/skill-v1.0.0-1a7a5a)](aisecsight/SKILL.md)
[![api](https://img.shields.io/badge/API-anonymous%20read--only-1a7a5a)](https://aisecsight.com/api/v1)

**Install once. Your agent stops guessing about AI regulations and starts citing articles, dates, and sources.**

An [Agent Skill](https://aisecsight.com/connect) that connects Claude Code, Codex, Cursor, Gemini CLI or WorkBuddy to [AISecSight](https://aisecsight.com) — a curated database of global AI laws, standards, penalty clauses, and governance news.

- **85 laws and standards** across the EU, China, the US, APAC and international bodies
- **Penalties down to the article** (e.g. EU AI Act Art. 99(3): up to €35M or 7% of worldwide turnover, whichever is higher)
- **Reviewed dates and official sources** on every answer
- **Anonymous read-only API**, no key, no signup, no tracking

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
