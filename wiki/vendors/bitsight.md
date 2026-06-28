---
title: Bitsight
type: vendor
name: Bitsight
slug: bitsight
categories: [vendor-risk]
layer: governance
aliases: [BitSight Technologies]
website: "https://www.bitsight.com/"
founded: 2011
hq: Boston, Massachusetts, USA
ownership: independent
ownership_detail: "Private; Moody's Corporation is largest shareholder after a $250M investment in 2021 (~$2.4B valuation). Not a Moody's subsidiary. Acquired Cybersixgill (2024, ~$115M)."
ownership_confidence: high
funding_total: ">$465M (incl. Moody's $250M, 2021)"
last_funding: "Moody's strategic investment, $250M, 2021"
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [security-ratings, vendor-risk, tprm, cyber-ratings]
---

# Bitsight

> Primary category: [vendor-risk](../categories/vendor-risk.md).

**One-liner** — The other major outside-in security-ratings provider, scoring organizations and their third parties on externally observable cyber posture; Moody's is its largest shareholder.

**What it does** — Bitsight continuously gathers external security telemetry (compromised systems, patching, configuration hygiene, exposed assets) and produces a numeric security rating per organization, used to assess and monitor supplier/third-party risk, benchmark posture, and (via the Moody's tie) inform cyber-risk quantification and insurance. The 2024 Cybersixgill acquisition added real-time/dark-web threat intelligence.

**Where it sits in the stack** — [vendor-risk](../categories/vendor-risk.md), governance layer. An external risk-signal source for TPRM, not a runtime data control (`trifecta_relevance: none`). Peer of [securityscorecard](securityscorecard.md), [black-kite](black-kite.md), [upguard](upguard.md); feeds assessment-workflow tools like [processunity](processunity.md) / [onetrust](onetrust.md).

**Deployment & architecture** — SaaS. Outside-in ratings portal/API + threat intelligence (Cybersixgill); integrations with GRC/TPRM, SIEM, and cyber-insurance workflows.

**Positioning & differentiators** — One of the two best-known ratings brands with [securityscorecard](securityscorecard.md). Differentiators: the Moody's relationship (financial-grade risk framing, cyber-risk quantification) and now integrated threat intel. Same external-signal-accuracy caveats as all ratings.

**Ownership, funding & M&A** — `independent` but strategically tied: **Moody's Corporation** invested $250M in 2021 (~$2.4B valuation) and became Bitsight's **largest shareholder** — a large minority/strategic stake, not a full acquisition, so Bitsight remains a private, independently operated company (not a Moody's subsidiary). Founded 2011, HQ Boston; surpassed $200M ARR (2025). Itself an acquirer: bought **Cybersixgill** for ~$115M (signed 2024-11-14, closed 2024-12-11). (high confidence)

**CTO / hedge-fund lens** — Day-1-ish for third-party risk: low-effort external screening/monitoring of vendors (incl. AI/SaaS). The Moody's link makes it attractive where the fund wants cyber risk expressed in financial terms. Use as a triage signal alongside real assessments, not as sole control.

**Competitors / alternatives** — [securityscorecard](securityscorecard.md), [black-kite](black-kite.md), [upguard](upguard.md), [processunity](processunity.md), [onetrust](onetrust.md).

**Open questions / to verify** — Whether Moody's stake has changed since 2021; Cybersixgill integration depth.

## Sources
- [Bitsight completes acquisition of Cybersixgill](https://www.bitsight.com/press-releases/bitsight-completes-acquisition-cyber-threat-intelligence-leader-cybersixgill) — fetched 2026-06-28 — supports: Cybersixgill close 2024-12-11, Bitsight positioning; confidence: high
- [Bitsight buys Cybersixgill for $115M (TechCrunch)](https://techcrunch.com/2024/11/14/bitsight-buys-dark-web-security-specialist-cybersixgill-for-115m/) — fetched 2026-06-28 — supports: deal value, Moody's largest shareholder, $2.4B valuation; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (Moody's largest shareholder via $250M 2021 minority stake, NOT a subsidiary); founded 2011 Boston; acquired Cybersixgill (~$115M, 2024); ownership stays independent, confidence high.
