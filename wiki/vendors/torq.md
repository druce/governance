---
type: vendor
name: Torq
slug: torq
categories: [ai-soc-analysts, siem-soc, ai-spm]
layer: foundation
aliases: [Torq HyperSOC]
website: https://torq.io
founded: 2020
hq: Denver, CO, USA (also New York; R&D in Israel)
ownership: independent
ownership_detail: VC-backed; $140M Series D led by Merlin Ventures (2026-01) at $1.2B valuation. $332M total.
ownership_confidence: high
funding_total: ~$332M
last_funding: Series D $140M (2026-01, Merlin Ventures, $1.2B valuation)
deployment: [saas]
target_customer: Fortune 500 / large enterprise, US Federal/Public Sector
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [hyperautomation, soar, ai-soc, agentic-ai, alert-triage]
---

# Torq

**One-liner** — A security hyperautomation platform (modern SOAR) that has grown into an "AI SOC" with agentic alert triage and a self-service agent builder.

**What it does** — Torq started as no/low-code security **hyperautomation** — the SOAR job of stitching together security tools and automating response workflows — and has layered an AI SOC ("HyperSOC") on top. Three pillars today: **Hyperautomation** (claims teams can handle ~100x more alerts without added headcount), **Agentic AI** (a self-service builder to spin up SOC agents), and **AI alert triage/investigation** (up to ~90% reduction in investigation time on low-fidelity alerts). It is the workflow/automation backbone as much as an analyst-replacement.

**Where it sits in the stack** — Primary [ai-soc-analysts](../categories/ai-soc-analysts.md); also tagged [siem-soc](../categories/siem-soc.md) (it's the SOAR/automation layer many SOCs run alongside the SIEM) and [ai-spm](../categories/ai-spm.md). SOC-ops tooling — trifecta_relevance: none. Trusted security-ops zone.

**Deployment & architecture** — Cloud-based SaaS platform with self-service agent/workflow building; broad integrations across security and IT tooling (its SOAR heritage means it's integration-heavy by design). Named customers include Marriott, PepsiCo, P&G, Siemens, Uber, Virgin Atlantic, Valvoline.

**Positioning & differentiators** — CEO & co-founder Ofer Smadari; founded 2020. Differs from the pure agentic-SOC startups ([prophet-security](prophet-security.md), [dropzone-ai](dropzone-ai.md), [7ai](7ai.md), [radiant-security](radiant-security.md), [simbian](simbian.md)) by coming from **hyperautomation/SOAR**: it's the orchestration substrate that executes response, with AI triage added — versus startups that lead with the autonomous "AI analyst" verdict. Most mature/best-funded option in this cohort ($1.2B valuation).

**Ownership, funding & M&A** — Independent, VC-backed. **$140M Series D led by Merlin Ventures (announced 2026-01-12) at a $1.2B valuation; ~$332M total raised.** Prior $70M Series C (Sept 2024, Evolution Equity). Other backers: Bessemer, Insight Partners, Notable Capital, Greenfield Partners. No M&A; no seed acquisition flag. Confidence high.

**CTO / hedge-fund lens** — **Day-2.** As a SOAR/hyperautomation platform it's most valuable once you have multiple security tools to orchestrate and enough alert/response volume to automate — large enterprise territory. For a hedge fund the realistic entry point is via an MSSP/MDR or a sizable in-house security team; a 50-person fund won't stand up Torq directly. Maturity and $1.2B-valuation stability are a plus versus the seed/Series-A peers. No direct SR 11-7 angle; diligence what automated response actions run unsupervised.

**Competitors / alternatives** — [prophet-security](prophet-security.md), [dropzone-ai](dropzone-ai.md), [7ai](7ai.md), [radiant-security](radiant-security.md), [simbian](simbian.md); incumbent SOAR/automation from [splunk](splunk.md) (SOAR) and [palo-alto-networks](palo-alto-networks.md) (Cortex XSOAR/XSIAM).

**Open questions / to verify** — Primary HQ (Denver vs New York in different profiles); how the [ai-spm](../categories/ai-spm.md) tag is justified by current product; degree of autonomy in agentic response by default.

## Sources
- [Torq Secures $140M Series D at $1.2B Valuation (Torq)](https://torq.io/news/torq-seriesd/) — fetched 2026-06-28 — supports: Series D, valuation, $332M total, product pillars, customers, CEO; confidence: med (vendor PR).
- [Torq raises $140M at $1.2B valuation (SiliconANGLE)](https://siliconangle.com/2026/01/11/torq-raises-140m-1-2b-valuation-scale-ai-driven-security-hyperautomation/) — fetched 2026-06-28 — supports: round, valuation, hyperautomation positioning; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established 2020 founding, Denver HQ, CEO Ofer Smadari, hyperautomation/SOAR→AI SOC, $140M Series D (Merlin, 2026-01) at $1.2B, $332M total, independent. Set ownership_confidence high. trifecta=none. hedge_fund_fit=medium (Day-2, large-enterprise/SOAR). Kept categories ai-soc-analysts/siem-soc/ai-spm as-is.
