---
type: vendor
name: UpGuard
slug: upguard
categories: [vendor-risk]
layer: governance
aliases: [ScriptRock]
website: https://www.upguard.com/
founded: 2012
hq: Mountain View, California, USA
ownership: independent
ownership_detail: "Private, VC-backed (~$121M raised). Series C $75M (2026) led by Springcoast Partners."
ownership_confidence: high
funding_total: ~$121M
last_funding: "Series C, $75M, 2026 (Springcoast Partners)"
deployment: [saas]
target_customer: mid-market
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [security-ratings, vendor-risk, tprm, attack-surface, data-leak]
---

# UpGuard

> Primary category: [[vendor-risk]].

**One-liner** — A cyber-risk-ratings and third-party-risk platform that pairs external security scoring with attack-surface management and data-leak detection.

**What it does** — UpGuard scores an organization and its vendors on external security posture (like the other ratings vendors) but bundles attack-surface monitoring and a well-known data-leak-detection capability (it built a reputation publicizing exposed-cloud-storage breaches). Buyers use it for vendor screening/monitoring, security questionnaires, and watching their own external exposure.

**Where it sits in the stack** — [[vendor-risk]], governance layer. External risk-signal + exposure detection feeding TPRM, not a runtime data control (`trifecta_relevance: none`). Peer of [[bitsight]], [[securityscorecard]], [[black-kite]]; complements assessment workflows like [[processunity]] / [[onetrust]].

**Deployment & architecture** — SaaS. Outside-in ratings + attack-surface/data-leak scanning + questionnaire workflow; integrations with GRC/security tooling.

**Positioning & differentiators** — More mid-market-accessible and product-led than the enterprise-heavy [[bitsight]] / [[securityscorecard]]; the data-leak-detection heritage and combined attack-surface + ratings + questionnaire bundle are its differentiators.

**Ownership, funding & M&A** — `independent`, private, VC-backed. Founded 2012 (Mike Baukes, Alan Sharp-Paul; originally "ScriptRock"); HQ Mountain View, CA (Australian origins). ~$121M raised; Series C $75M (2026) led by Springcoast Partners, with August Capital, Square Peg, Pelion. No acquisition found. (high confidence)

**CTO / hedge-fund lens** — Day-1-ish and arguably the most approachable of the ratings vendors for a mid-size fund: vendor screening/monitoring plus self-exposure detection in one subscription. Good fit for a leaner team; triage signal alongside real assessments, not a sole control.

**Competitors / alternatives** — [[bitsight]], [[securityscorecard]], [[black-kite]], [[processunity]], [[onetrust]].

**Open questions / to verify** — Post-Series-C scale/valuation; depth of vendor-assessment workflow vs. dedicated TPRM platforms.

## Sources
- [UpGuard raises $75M Series C](https://www.upguard.com/press/upguard-raises-75m-in-series-c-funding-to-accelerate-market-leadership-in-cyber-risk-posture-management) — fetched 2026-06-28 — supports: Series C $75M Springcoast, ~$121M total, positioning; confidence: high
- [UpGuard Crunchbase profile](https://www.crunchbase.com/organization/upguard) — fetched 2026-06-28 — supports: founded 2012 (ScriptRock), HQ, founders, investors; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent VC-backed (~$121M, Springcoast-led Series C 2026); founded 2012 (ex-ScriptRock); ownership unchanged (independent).
