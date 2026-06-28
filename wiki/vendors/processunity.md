---
type: vendor
name: ProcessUnity
slug: processunity
categories: [vendor-risk]
layer: governance
aliases: [ProcessUnity + CyberGRX]
website: "https://www.processunity.com/"
founded: 2003
hq: Concord, Massachusetts, USA
ownership: acquired
ownership_detail: "PE-owned: Marlin Equity Partners acquired ProcessUnity 2021-09-28. ProcessUnity acquired/merged CyberGRX 2023-07."
ownership_confidence: high
funding_total:
last_funding: "Acquired by Marlin Equity Partners (2021)"
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [tprm, vendor-risk, grc, third-party-risk]
---

# ProcessUnity

> Primary category: [vendor-risk](../categories/vendor-risk.md).

**One-liner** — A third-party-risk-management (TPRM) and GRC platform that, after merging with CyberGRX, pairs assessment workflow with a large pre-completed vendor-risk data exchange.

**What it does** — ProcessUnity runs the TPRM lifecycle: vendor onboarding, risk-tiering, assessments/questionnaires, continuous monitoring, and remediation, plus broader GRC (policy, controls). The 2023 CyberGRX combination added an "exchange" of pre-completed third-party risk assessments and predictive risk data, reducing the questionnaire burden on both buyers and vendors.

**Where it sits in the stack** — [vendor-risk](../categories/vendor-risk.md), governance layer. Process/workflow + data for assessing suppliers — including AI vendors — not a runtime data control (`trifecta_relevance: none`). Complements security-ratings vendors ([bitsight](bitsight.md), [securityscorecard](securityscorecard.md), [black-kite](black-kite.md), [upguard](upguard.md)) by owning the assessment workflow they feed into.

**Deployment & architecture** — SaaS. Questionnaire/assessment engine + CyberGRX exchange data; integrations with GRC and security tooling.

**Positioning & differentiators** — Workflow-and-exchange TPRM, differentiated from the pure outside-in cyber-ratings vendors. The CyberGRX merger is its main moat (assessment data network). Competes with [onetrust](onetrust.md) vendor risk and the ratings players.

**Ownership, funding & M&A** — `acquired` / PE-owned. **Marlin Equity Partners** acquired ProcessUnity on 2021-09-28. As a Marlin portfolio company, ProcessUnity then acquired/merged with **CyberGRX** (announced 2023-07-12; CyberGRX holders retained a minority stake; terms undisclosed). Stub "independent" corrected to `acquired`. (high confidence)

**CTO / hedge-fund lens** — Day-1 for a fund formalizing third-party/vendor risk (extends naturally to AI-vendor due diligence). Good fit where the fund wants a real assessment workflow plus reusable vendor data rather than just an external score. Heavier than a ratings-only subscription.

**Competitors / alternatives** — [onetrust](onetrust.md), [securityscorecard](securityscorecard.md), [bitsight](bitsight.md), [black-kite](black-kite.md), [upguard](upguard.md), [archer](archer.md).

**Open questions / to verify** — Current scale of the CyberGRX exchange; AI-vendor-specific assessment content.

## Sources
- [Marlin: ProcessUnity acquires CyberGRX](https://www.marlinequity.com/news/marlin-portfolio-company-processunity-acquires-cybergrx/) — fetched 2026-06-28 — supports: Marlin ownership, CyberGRX merger 2023; confidence: high
- [ProcessUnity + CyberGRX press release](https://www.processunity.com/resources/press-releases/processunity-cybergrx-form-most-complete-third-party-risk-management-platform/) — fetched 2026-06-28 — supports: combined TPRM platform scope; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected ownership independent→acquired (Marlin Equity PE, 2021); documented CyberGRX merger (2023); confidence high.
