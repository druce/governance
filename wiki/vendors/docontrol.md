---
type: vendor
name: DoControl
slug: docontrol
categories: [sspm]
layer: foundation
aliases: []
website: https://www.docontrol.io
founded: 2020
hq: New York, NY
ownership: independent
ownership_detail: VC-backed independent; no acquisition found as of 2026-06-28.
ownership_confidence: medium
funding_total: ~$45M
last_funding: Series B $30M (Apr 2022), led by Insight Partners
deployment: [saas, api]
target_customer: enterprise / mid-market
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [sspm, saas-dlp, data-security, data-access-governance]
---

# DoControl

> SaaS data-access security: maps who can reach what across your SaaS apps and uses no-code workflows to auto-detect and remediate risky sharing and exposure.

**One-liner** — An automated SaaS data-security / data-access-controls platform that finds over-shared and exposed data across SaaS apps and remediates it with no-code workflows.

## What it does

DoControl focuses on the **data** inside SaaS apps rather than only app configuration. It ingests user interactions and API/data-access events across SaaS tools (file stores, collaboration suites, etc.), builds a picture of who can access and share what, and runs no-code workflows that automatically identify, alert on, and remediate data-exposure threats — for example public links, external sharing, over-broad collaboration, and risky access by departing employees or third-party vendors. In effect it is **SaaS data security / SaaS DLP** with an SSPM-adjacent footprint.

The job for a buyer: stop sensitive data leaking out of SaaS via over-sharing, and automate the cleanup instead of doing it by hand.

## Where it sits in the stack

Filed under [sspm](../categories/sspm.md) in this wiki, but its center of gravity is **SaaS data security / data-access governance** (closer to DSPM-for-SaaS than to config-posture SSPM). Layer: foundation.

Lethal-trifecta role: **sensitive-data** and **egress** — it limits exposure and exfiltration of corporate data shared through SaaS apps. Not a model/prompt firewall.

## Deployment & architecture

SaaS, **API-first / agentless**: connects to SaaS apps via API to read sharing and access events, with no-code workflow automation for response and remediation. Integrates with IdP and SaaS collaboration platforms. No inline proxy or browser agent.

## Positioning & differentiators

Known for **data-centric, no-code remediation** of SaaS over-sharing — a different emphasis from config-posture-first SSPMs like [appomni](appomni.md), [obsidian-security](obsidian-security.md), and [wing-security](wing-security.md). Closest neighbors are tools that govern SaaS data access and OAuth/identity risk: [valence-security](valence-security.md), [grip-security](grip-security.md), [reco](reco.md). Backed early by CrowdStrike's Falcon Fund, which positions it near the endpoint-security ecosystem (vendor/investor framing).

## Ownership, funding & M&A

Independent, VC-backed. Founded 2020; HQ New York, NY. Total funding ~$45M raised in roughly 22 months; most recent disclosed round a **$30M Series B (April 2022) led by Insight Partners**, with StageOne Ventures, Cardumen Capital, RTP Global, and CrowdStrike Falcon Fund (Series A was ~$10M led by RTP Global). No acquisition found as of 2026-06-28. Figures from the company's Series B press release (primary) plus aggregators.

## CTO / hedge-fund lens

**Day-2.** This is for funds that already run heavy SaaS collaboration (Google Workspace / Microsoft 365 / Slack / Box) and worry about sensitive data — deal docs, positions, LP data — leaking via public links and external sharing. It complements DLP/CASB and is increasingly relevant as AI tools get OAuth access to those same data stores. No direct SR 11-7 / model-risk role. Fit is **medium** — most valuable where SaaS file-sharing sprawl is real; a smaller fund may rely on native admin controls plus its IdP first.

## Competitors / alternatives

[valence-security](valence-security.md), [grip-security](grip-security.md), [reco](reco.md), [appomni](appomni.md), [obsidian-security](obsidian-security.md), [wing-security](wing-security.md), [nudge-security](nudge-security.md).

## Open questions / to verify

- Any funding/round after the 2022 Series B; current employee count and traction.
- Current product scope (has it added AI/OAuth-governance features since 2022?).
- Whether to recategorize toward a SaaS-DLP / DSPM-for-SaaS slot vs. SSPM in this wiki's taxonomy.

## Sources

- [DoControl Secures $30M Series B to Redefine SaaS Data Security (PR Newswire)](https://www.prnewswire.com/news-releases/docontrol-secures-30-million-series-b-to-redefine-saas-data-security-301525545.html) — fetched 2026-06-28 — supports: founded 2020, NYC HQ, $30M Series B (Insight Partners), ~$45M total, SaaS data-access/no-code-remediation positioning; confidence: high (company PR) for funding, med for product framing (marketing).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed (NYC, founded 2020, ~$45M total, $30M Series B led by Insight Partners, CrowdStrike Falcon Fund backer), SaaS data-security/DLP with no-code remediation; no acquisition found. Set ownership independent (medium), hedge_fund_fit medium, status researched. Noted possible recategorization toward SaaS-DLP/DSPM.
