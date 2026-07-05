---
title: Dropzone AI
type: vendor
name: Dropzone AI
slug: dropzone-ai
aka: []
primary_category: ai-soc-analysts
also_listed_in: []
website: https://www.dropzone.ai
founded: 2023
hq: Seattle, WA, USA
ownership_state: independent
owner: null
ownership_note: VC-backed; $37M Series B led by Theory Ventures (2025-07). ~$57.4M total across 3 rounds.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$57.4M
last_funding: Series B $37M (2025-07, Theory Ventures)
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise SOC teams, MSSPs/MDR providers
last_verified: 2026-06-28
verify_after: null
tags: [agentic-soc, ai-soc, alert-triage, mssp]
---

# Dropzone AI

**One-liner** — An autonomous AI SOC analyst that investigates every security alert end-to-end, 24/7, with human-level reasoning and no playbooks to write.

**What it does** — Dropzone connects to your SIEM/EDR/cloud/identity tooling and, for each alert, runs a full investigation the way an experienced analyst would: pulls context, chases artifacts, decides whether it's a real threat, and writes a verdict with the evidence. It covers phishing, endpoint, network, cloud, identity, and insider-threat alerts. The goal is to clear the Tier-1 triage backlog and cut MTTR without expanding headcount — explicitly marketed (marketing) as "the world's first AI SOC analyst."

**Where it sits in the stack** — [ai-soc-analysts](../categories/ai-soc-analysts.md), Foundation layer; an automation layer over [siem-soc](../categories/siem-soc.md) and [edr-xdr](../categories/edr-xdr.md). SOC-ops tooling, not an AI-application control — trifecta_relevance: none. Operates in the trusted security-ops zone.

**Deployment & architecture** — SaaS with API integrations into SIEM, EDR, and cloud systems; no inline/proxy data-path role. Notably sold to **MSSPs/MDR providers** as well as end-enterprises, so it shows up as the engine behind some managed offerings. Named customers include UiPath, Zapier, Pipe, Mysten Labs.

**Positioning & differentiators** — Founder/CEO Edward Wu (early ExtraHop engineer). Differentiates on no-playbook autonomy (claims it doesn't need pre-built runbooks) and breadth of alert types, plus an MSSP channel. Nearest neighbors: [prophet-security](prophet-security.md), [radiant-security](radiant-security.md), [7ai](7ai.md), [simbian](simbian.md); vs. [torq](torq.md) (which comes from hyperautomation/SOAR rather than analyst-replacement).

**Ownership, funding & M&A** — Independent, VC-backed. $37M Series B led by Theory Ventures (2025-07-17), with Madrona, Decibel Ventures, Pioneer Square Labs, and IQT; prior $16.85M Series A (2024-04, also Theory Ventures). ~$57.4M total across three rounds; reported ~$207M valuation. No M&A; no seed acquisition flag. Confidence high on independence.

**CTO / hedge-fund lens** — **Day-2.** Same logic as the rest of this category: you need an existing SIEM/EDR and meaningful alert volume first. The MSSP angle matters for a hedge fund — if you outsource detection-and-response, your provider may already run Dropzone (or a peer) under the hood, so the buying decision may be "which MDR" rather than "which AI SOC tool." No direct model-risk/SR 11-7 tie; standard vendor diligence on data retention and LLM use applies.

**Competitors / alternatives** — [prophet-security](prophet-security.md), [radiant-security](radiant-security.md), [7ai](7ai.md), [simbian](simbian.md), [torq](torq.md).

**Open questions / to verify** — Exact total/valuation; data-residency and self-hosted options for regulated customers; how its agents are evaluated for false-negatives (autonomous verdicts carry tail risk).

## Sources
- [Dropzone AI Raises $37M to Scale AI SOC Analyst Platform](https://www.dropzone.ai/press-release/dropzone-ai-37m-series-b-funding-ai-soc-agents) — fetched 2026-06-28 — supports: Series B, Seattle HQ, CEO, deployment, customers; confidence: med (vendor PR).
- [Seattle startup Dropzone AI raises $37M (GeekWire)](https://www.geekwire.com/2025/seattle-startup-dropzone-raises-37m-to-supercharge-its-ai-soc-analyst-security-software/) — fetched 2026-06-28 — supports: founding 2023, total ~$57.4M, valuation; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established 2023 founding, Seattle HQ, CEO Edward Wu, $37M Series B (Theory Ventures), ~$57.4M total, MSSP channel, independent. Set ownership_confidence high. trifecta=none. hedge_fund_fit=medium (Day-2).
