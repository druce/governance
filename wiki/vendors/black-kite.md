---
type: vendor
name: Black Kite
slug: black-kite
categories: [vendor-risk]
layer: governance
aliases: []
website: https://blackkite.com/
founded: 2016
hq: Boston, Massachusetts, USA
ownership: independent
ownership_detail: "Private, VC-backed (~$33M+ raised). Series B $22M (2023) led by Volition Capital."
ownership_confidence: high
funding_total: ~$33M+
last_funding: "Series B, $22M, 2023 (Volition Capital)"
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [security-ratings, vendor-risk, tprm, cyber-ratings, fair]
---

# Black Kite

> Primary category: [[vendor-risk]].

**One-liner** — A third-party cyber-risk-intelligence / ratings vendor that scores suppliers across technical, financial (dollar-risk), and compliance dimensions.

**What it does** — Black Kite does outside-in assessment and continuous monitoring of third parties, but differentiates by translating cyber posture into three lenses: a technical rating, a **FAIR-based financial** estimate of probable breach impact (dollars), and a compliance/standards mapping. The dollar-risk framing is its signature pitch to TPRM teams who need to prioritize vendors by business impact.

**Where it sits in the stack** — [[vendor-risk]], governance layer. External risk-signal source for TPRM, not a runtime data control (`trifecta_relevance: none`). Peer of [[bitsight]], [[securityscorecard]], [[upguard]]; feeds assessment workflows like [[processunity]] / [[onetrust]].

**Deployment & architecture** — SaaS. Outside-in scanning + ratings/portal + FAIR quantification + compliance mapping; integrations with GRC/TPRM tooling.

**Positioning & differentiators** — Smaller and more focused than [[bitsight]] / [[securityscorecard]]; the FAIR financial-quantification angle is the main differentiator versus letter/number-grade ratings. Standards-based compliance mapping is a secondary hook.

**Ownership, funding & M&A** — `independent`, private, VC-backed. Founded 2016 (Candan Bolukbas, ex-NATO ethical hacker; co-founder Mohamoud Jibrell); HQ Boston; CEO Paul Paget. ~$33M+ raised: Series A $7.5M (2020, Moore Strategic Ventures + Glasswing + Data Point), Series B $22M (2023, led by Volition Capital). No acquisition found. (high confidence)

**CTO / hedge-fund lens** — Day-1-ish for a fund that wants third-party risk expressed in dollars to prioritize remediation across vendors (including AI/SaaS). Smaller brand than the leaders but the financial framing resonates with risk committees. Triage signal, not sole control.

**Competitors / alternatives** — [[bitsight]], [[securityscorecard]], [[upguard]], [[processunity]], [[onetrust]].

**Open questions / to verify** — Latest funding/scale post-2023; coverage breadth vs. larger ratings vendors.

## Sources
- [Black Kite raises $22M Series B (SecurityWeek)](https://www.securityweek.com/vendor-risk-management-firm-black-kite-raises-22-million/) — fetched 2026-06-28 — supports: Series B $22M Volition, total funding; confidence: high
- [Black Kite Series A announcement](https://blackkite.com/blog/black-kite-secures-7-5-million-in-series-a-funding) — fetched 2026-06-28 — supports: founded 2016, founders, Series A, FAIR/technical/compliance model; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent VC-backed (~$33M+, Volition-led Series B 2023); founded 2016 Boston; FAIR dollar-risk differentiator noted; ownership unchanged (independent).
