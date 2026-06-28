---
title: Sentra
type: vendor
name: Sentra
slug: sentra
categories: [dspm, data-access-governance]
layer: data
aliases: []
website: "https://www.sentra.io"
founded: 2021
hq: Tel Aviv, Israel (offices in New York, NY)
ownership: independent
ownership_detail: Privately held, VC-backed. >$100M raised total; $50M Series B (2025-04, led by Key1 Capital).
ownership_confidence: high
funding_total: ">$100M"
last_funding: $50M Series B (2025-04, led by Key1 Capital)
deployment: [saas, api]
target_customer: cloud-heavy enterprise adopting AI
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [dspm, data-access-governance, cloud-security, ai-data-security]
---

# Sentra

> **One-liner** — Agentless, cloud-native DSPM that discovers and classifies sensitive data across the cloud and adds controls to keep PII out of AI training sets and gen-AI prompts.

**What it does** — Sentra scans cloud environments (agentless) to find and classify sensitive data, score posture/risk, and detect risky movement (data detection & response). Its current emphasis is **data security for AI** — keeping training datasets and gen-AI prompts free of PII/restricted data — alongside data access governance (who/what can reach sensitive data). You buy it to get a fast, low-friction map of cloud data risk without deploying agents.

**Where it sits in the stack** — Primary: [dspm](../categories/dspm.md); also [data-access-governance](../categories/data-access-governance.md). Data layer. Lethal-trifecta role: the **sensitive-data** leg (discover/classify/constrain) and helping the **egress** leg by keeping sensitive data out of prompts/training. Trust zones: green/yellow cloud data plane feeding AI.

**Deployment & architecture** — SaaS, **agentless/cloud-connector** (scans cloud accounts and datastores without installing agents) — a fast, low-touch deployment story. Cloud-first (AWS/Azure/GCP, SaaS). Integrates with DLP, IAM, and SIEM/workflow tooling. Direct architectural analog to [cyera](cyera.md).

**Positioning & differentiators** — Sentra and [cyera](cyera.md) are the two prominent Israeli, ex-Unit 8200, agentless cloud-native DSPM challengers; Sentra is the smaller/earlier-stage of the pair and leans hard into the "secure data for AI adoption" framing. Versus [bigid](bigid.md) (broad governance/privacy, on-prem heavy) Sentra is leaner and cloud-only. Versus [microsoft-purview](microsoft-purview.md) it spans beyond the Microsoft estate and stands up faster. Differentiators it claims: classification accuracy and agentless DSPM + DDR (data detection & response) for movement, not just static posture.

**Ownership, funding & M&A** — **Independent**, privately held. Founded **2021**; HQ Tel Aviv with a New York office. Founders: Yoav Regev (CEO, ex-Head of Cyber Dept, Unit 8200), Asaf Kochan (President, former Unit 8200 commander), Ron Reiter (CTO), Yair Cohen (VP Product). Funding: **$50M Series B (Apr 2025)** led by Key1 Capital (Bessemer, Zeev Ventures, Standard Investments, Munich Re Ventures participating), bringing total to **>$100M** (prior $30M Series A). No acquisition; no seed M&A flag. Ownership confidence: high.

**CTO / hedge-fund lens** — **Day-1** for a cloud-heavy fund that wants fast, agentless data discovery specifically to de-risk AI adoption (clean training data / prompt hygiene). Lighter and earlier-stage than [cyera](cyera.md); a reasonable shortlist entry if you want a focused cloud DSPM without the enterprise heft (or price tag) of the leaders. SR 11-7: supports AI-governance/data-lineage evidence indirectly. Caveat: smaller vendor (concentration/longevity risk), SaaS-only, cloud-first — less relevant for on-prem-heavy estates.

**Competitors / alternatives** — [cyera](cyera.md), [bigid](bigid.md), [securiti](securiti.md), [concentric-ai](concentric-ai.md), [microsoft-purview](microsoft-purview.md), Varonis.

**Open questions / to verify**
- Current customer count / scale vs the agentless-DSPM leaders.
- Depth of the data-access-governance and DDR features vs core discovery.

## Sources
- [Sentra Closes $50M Series B (Sentra / BusinessWire, 2025-04-22)](https://sentra.io/news/sentra-closes-50-million-series-b-amid-surging-demand-for-securing-data-for-ai-adoption) + [SiliconANGLE coverage](https://siliconangle.com/2025/04/22/sentra-lands-50m-scale-cloud-native-data-security-ai-safeguards/) — fetched 2026-06-28 — supports: founding 2021, Tel Aviv/NY, founders, $50M Series B / >$100M total, agentless cloud DSPM + AI data security; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent (>$100M raised; $50M Series B Apr 2025, Key1 Capital), founded 2021, Tel Aviv/NY, agentless cloud-native DSPM focused on securing data for AI. Raised ownership_confidence to high. No M&A.
