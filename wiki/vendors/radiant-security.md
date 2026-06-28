---
title: Radiant Security
type: vendor
name: Radiant Security
slug: radiant-security
categories: [ai-soc-analysts]
layer: foundation
aliases: []
website: "https://radiantsecurity.ai"
founded: 2021
hq: San Francisco Bay Area, CA, USA
ownership: independent
ownership_detail: VC-backed; $15M Series A led by Next47 (2023-11). Total ~$22.5M.
ownership_confidence: high
funding_total: ~$22.5M
last_funding: Series A $15M (2023-11, Next47)
deployment: [saas, api]
target_customer: enterprise SOC teams (also mid-market)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [agentic-soc, ai-soc, alert-triage]
---

# Radiant Security

**One-liner** — An AI SOC platform/"co-pilot" that automatically triages and investigates every alert across all data sources — no playbooks or preset rules — and drives containment and remediation.

**What it does** — Radiant ingests alerts from your existing tooling and uses generative AI / LLMs to triage, investigate, and decide on each one, then automates containment, remediation, and escalation approvals. It markets itself as handling **every alert type across all sources with no playbooks required**, deployed via API in minutes, claiming up to ~95% reduction in analyst workload. The job is the same as its peers: collapse the Tier-1 triage burden and speed response.

**Where it sits in the stack** — [ai-soc-analysts](../categories/ai-soc-analysts.md), Foundation layer; automation/decision layer over [siem-soc](../categories/siem-soc.md) and [edr-xdr](../categories/edr-xdr.md). SOC-ops tooling — trifecta_relevance: none. Trusted security-ops zone.

**Deployment & architecture** — SaaS, API-deployed; reads from SIEM/EDR/cloud/identity sources and writes investigations/actions back. Emerged from stealth at Black Hat 2023.

**Positioning & differentiators** — Leadership drawn from former Imperva and Exabeam executives (SIEM/SOC pedigree). Differentiates on the "no-playbook, every-alert-type" claim and tight investigation→response automation. Nearest neighbors: [prophet-security](prophet-security.md), [dropzone-ai](dropzone-ai.md), [7ai](7ai.md), [simbian](simbian.md), [torq](torq.md).

**Ownership, funding & M&A** — Independent, VC-backed. $15M Series A (Nov 2023) led by Next47 (Siemens' venture arm), with Lightspeed Venture Partners, Acrew Capital, Uncorrelated Ventures, Jibe Ventures; total ~$22.5M. No M&A; no seed acquisition flag.

> Note (resolved, not a contradiction): early web results conflated "Radiant Security" with an unrelated company, **Radiant** (nuclear microreactors), which raised ~$300M Series D in 2025 with DCVC participating. That is a different company; Radiant Security's last confirmed round is the 2023 Series A.

HQ: SecurityWeek lists San Francisco; CB Insights lists Milpitas, CA — both SF Bay Area (soft discrepancy, recorded as "SF Bay Area").

**CTO / hedge-fund lens** — **Day-2.** Standard for this category: needs an existing SIEM/EDR and real alert volume. Smaller raise / older vintage than [7ai](7ai.md) or [torq](torq.md) — evaluate runway and roadmap. Fits a mid-to-large shop with an in-house SOC; a 50-person fund would more likely get this via an MDR. No direct SR 11-7 angle; diligence autonomous-action scope and data handling.

**Competitors / alternatives** — [prophet-security](prophet-security.md), [dropzone-ai](dropzone-ai.md), [7ai](7ai.md), [simbian](simbian.md), [torq](torq.md).

**Open questions / to verify** — Exact HQ city; precise total funding (profiles vary $15M–$22.5M); any 2024-2025 raise; founder names; how autonomous the remediation actions are by default.

## Sources
- [Radiant Snags $15 Million for AI-Powered SOC Technology (SecurityWeek)](https://www.securityweek.com/radiant-snags-15-million-for-ai-powered-soc-technology/) — fetched 2026-06-28 — supports: $15M Series A, investors, product, exec pedigree; confidence: med.
- [Radiant Security — Crunchbase profile](https://www.crunchbase.com/organization/radiantsecurity) — fetched 2026-06-28 — supports: total funding ~$22.5M, independence; confidence: low-med (aggregator).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established $15M Series A (Next47, 2023-11), ~$22.5M total, SF-Bay-Area HQ, ex-Imperva/Exabeam leadership, independent. Disambiguated from unrelated "Radiant" nuclear company (DCVC) that some searches surfaced. Set ownership_confidence high. trifecta=none. hedge_fund_fit=medium (Day-2).
