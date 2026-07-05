---
title: SecurityScorecard
type: vendor
name: SecurityScorecard
slug: securityscorecard
aka: []
primary_category: vendor-risk
also_listed_in: []
website: https://securityscorecard.com/
founded: 2013
hq: New York, New York, USA
ownership_state: independent
owner: null
ownership_note: Private, VC/growth-backed (~$290M+ raised; Series E $180M 2021, ~$1B valuation). Acquired HyperComply (2025).
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$290M+
last_funding: Series E, $180M, 2021
market_position: null
deployment_model: [saas]
form_factor: []
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-06-28
verify_after: null
tags: [security-ratings, vendor-risk, tprm, cyber-ratings]
---

# SecurityScorecard

> Primary category: [vendor-risk](../categories/vendor-risk.md).

**One-liner** — An outside-in security-ratings service that scores companies (and their vendors) A–F on externally observable cyber posture, used to triage third-party risk.

**What it does** — SecurityScorecard continuously scans the internet for signals (patching cadence, exposed services, DNS/email hygiene, leaked credentials, malware chatter) and rolls them into a letter-grade rating per organization. Buyers use it to screen and monitor suppliers without sending questionnaires, and to benchmark their own posture. Increasingly bundles supply-chain detection and, via the 2025 HyperComply buy, AI-driven security-questionnaire automation.

**Where it sits in the stack** — [vendor-risk](../categories/vendor-risk.md), governance layer. An external risk-signal source feeding TPRM decisions — not a runtime data control or inline prompt/egress control. Complements assessment-workflow platforms like [processunity](processunity.md) and [onetrust](onetrust.md); a direct peer of [bitsight](bitsight.md), [black-kite](black-kite.md), [upguard](upguard.md).

**Deployment & architecture** — SaaS. Outside-in scanning + ratings API/portal; integrations with GRC/TPRM and security tooling; questionnaire automation (post-HyperComply).

**Positioning & differentiators** — One of the two best-known ratings brands alongside [bitsight](bitsight.md). Differentiators are breadth of scanned signals and a marketplace/ecosystem play; like all ratings, accuracy/attribution of external signals is the perennial critique. The HyperComply acquisition pushes it toward "ratings + automated assessments."

**Ownership, funding & M&A** — `independent`, private, VC/growth-backed. Founded 2013 (Aleksandr Yampolskiy, Sam Kassoumeh); HQ New York. ~$290M+ raised; Series E $180M (2021) at ~$1B valuation; investors include Silver Lake, Sequoia, GV, Evolution Equity. Itself an acquirer: bought **HyperComply** (2025-09-15) for AI questionnaire automation. No acquisition of SecurityScorecard found. (high confidence)

**CTO / hedge-fund lens** — Day-1-ish for a fund standing up third-party risk: a low-effort way to screen and monitor vendors (including AI/SaaS suppliers) by external posture. Best used alongside an assessment workflow rather than as the sole control; external ratings are a triage signal, not ground truth.

**Competitors / alternatives** — [bitsight](bitsight.md), [black-kite](black-kite.md), [upguard](upguard.md), [processunity](processunity.md), [onetrust](onetrust.md).

**Open questions / to verify** — Latest valuation/funding post-2021; HyperComply integration timeline; rating methodology changes.

## Sources
- [SecurityScorecard acquires HyperComply](https://securityscorecard.com/company/press/securityscorecard-acquires-hypercomply-to-bring-ai-powered-automation-to-supply-chain-risk-management/) — fetched 2026-06-28 — supports: 2025 acquisition, AI questionnaire automation; confidence: high
- [SecurityScorecard PitchBook/Crunchbase profiles](https://www.crunchbase.com/organization/security-scorecard) — fetched 2026-06-28 — supports: founded 2013, NY HQ, funding ~$290M+, Series E, investors; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent VC-backed (~$290M+, Series E 2021, ~$1B); founded 2013 NY; itself acquired HyperComply (2025); ownership unchanged (independent).
