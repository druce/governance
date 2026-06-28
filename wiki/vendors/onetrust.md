---
type: vendor
name: OneTrust
slug: onetrust
categories: [enterprise-grc, ai-governance-platform, dspm]
layer: governance
aliases: []
website: "https://www.onetrust.com"
founded: 2016
hq: Atlanta, Georgia, USA
ownership: independent
ownership_detail: "Private, growth-equity backed (Insight Partners, TCV, Coatue, SoftBank Vision Fund, Generation Investment Management). ~$1.1B raised total; last priced round $150M in 2023 at $4.5B (a down round from a prior ~$5.3B peak). No IPO as of 2026-06."
ownership_confidence: medium
funding_total: "~$1.1B (as of 2025)"
last_funding: "$150M, 2023, led by Generation Investment Management (down round, $4.5B valuation)"
deployment: [saas]
target_customer: enterprise (and large mid-market); regulated industries
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [grc, privacy, ai-governance, dspm]
---

# OneTrust

> Primary category: [enterprise-grc](../categories/enterprise-grc.md). Also tagged [ai-governance-platform](../categories/ai-governance-platform.md) and [dspm](../categories/dspm.md).

**One-liner** — The large incumbent privacy/GRC platform that bolted on an AI Governance module, so the team that already owns your privacy and third-party-risk program can also run an EU AI Act / NIST AI RMF model inventory from the same tool.

## What it does
OneTrust started as a privacy-management platform (data mapping, consent/cookie management, DSAR/privacy-rights automation) and expanded into a broad trust/GRC suite: third-party risk management, governance-risk-compliance workflows, ethics & whistleblowing (via the Convercent acquisition), regulatory intelligence (DataGuidance), and data discovery & classification. Its **AI Governance** solution (launched May 2023) lets organizations inventory AI projects, models, and datasets — both internally built and third-party/embedded — assess them against frameworks, and monitor them over time. Out-of-the-box content maps to the **EU AI Act, NIST AI RMF, and ISO/IEC 42001**, and it can auto-generate documentation such as conformity assessments. It integrates with model registries and MLOps tooling to detect AI use and changes, and pairs with OneTrust Data Discovery & Governance to find sensitive/personal data that drives bias or privacy risk.

## Where it sits in the stack
This is a **governance-layer** play. Primary fit is [enterprise-grc](../categories/enterprise-grc.md) (the system of record for policies, risk register, assessments, and audit evidence). The AI module makes it an [ai-governance-platform](../categories/ai-governance-platform.md) (use-case/model inventory, risk assessment, regulatory mapping), and its data discovery/classification capability gives it a foot in [dspm](../categories/dspm.md) (finding and classifying sensitive data at rest).

On the lethal trifecta it is mostly an **inventory/oversight** tool rather than an inline control — it does not sit in the prompt or egress path. Its trifecta relevance is **sensitive-data**: knowing where regulated data lives and which AI systems touch it. It lives in the governance/oversight zone, not in the runtime data path; it documents and assesses risk rather than blocking it.

## Deployment & architecture
SaaS (multi-tenant cloud), configured by privacy/GRC/compliance teams rather than embedded in application runtime. AI Governance integrates with existing model registries and MLOps tooling and connects to structured and unstructured data sources for discovery/classification. It is a workflow, assessment, and documentation engine — questionnaires, risk registers, control libraries, regulatory mappings — not a network/inference-path enforcement point.

## Positioning & differentiators
OneTrust's edge is **breadth and incumbency**: 14,000+ customers and an existing footprint in privacy and GRC at most large enterprises. For a buyer who already runs OneTrust for privacy or third-party risk, the AI Governance module is an incremental add-on staffed by the same team, with shared inventory, assessment, and regulatory-intelligence plumbing. It was recognized in Gartner's 2025 AI Governance Platforms market report.

The tradeoff versus focused AI-governance pureplays — [credo-ai](credo-ai.md), [holistic-ai](holistic-ai.md) — is depth: the pureplays go further on model-specific evaluation, bias/fairness testing, and AI-native policy intelligence, while OneTrust optimizes for fitting AI into an existing enterprise GRC operating model. Against compliance-automation tools like [vanta](vanta.md), OneTrust is heavier, broader, and aimed at large regulated enterprises rather than fast SOC 2 / security-attestation automation for smaller shops.

## Ownership, funding & M&A
- **Private and independent** as of 2026-06; venture/growth-equity backed, no IPO. (confidence: medium)
- Founded **2016** by Kabir Barday; HQ **Atlanta, Georgia**.
- ~**$1.1B raised** across roughly seven rounds (as of 2025). Notable rounds: $200M Series A (Insight Partners, 2019), $210M Series B (Coatue, 2020), $300M Series C (TCV, 2021) plus a $210M Series C extension (SoftBank Vision Fund).
- Most recent priced round: **$150M in 2023 led by Generation Investment Management at a $4.5B valuation** — a **down round** from a prior peak around $5.3B. (confidence: medium; valuation figures from aggregators, not a primary filing.)
- A frequent acquirer itself: DataGuidance (2019), Integris Software (2020), Convercent, Planetly, Tugboat Logic, Docuvision (2021). No evidence OneTrust itself has been acquired.

> No M&A flag in the seed; none found. OneTrust remains an independent private company. No contradiction.

## CTO / hedge-fund lens
**Day-1 if you already own it; Day-2 as a net-new AI purchase.** Many funds and asset managers already run OneTrust (or a peer) for privacy/GDPR/CCPA and vendor risk. If so, switching on AI Governance is the cheapest path to a defensible **AI use-case and model inventory** mapped to EU AI Act / NIST AI RMF — useful for board reporting and regulator-facing documentation.

On **SR 11-7 / model risk**: be clear about scope. OneTrust covers the *governance wrapper* — inventory, ownership, risk tiering, policy attestation, documentation, and regulatory mapping — which overlaps the documentation and oversight expectations of SR 11-7 and EU AI Act conformity. It does **not** perform quantitative model validation, backtesting, or independent performance/bias testing of trading or pricing models; that remains with model-risk/quant functions or specialist tools. Treat it as the compliance system of record, not a model validator.

For a small fund (sub-50 people) with no existing OneTrust footprint, the platform is likely **oversized and over-priced** for AI governance alone — a lighter pureplay or a spreadsheet-plus-policy approach may suffice. The value rises with regulatory exposure (EU nexus, regulated entities) and with the size of the existing privacy/GRC program it can ride on.

## Competitors / alternatives
- AI-governance pureplays: [credo-ai](credo-ai.md), [holistic-ai](holistic-ai.md)
- Compliance automation / attestation: [vanta](vanta.md)
- Broad GRC / privacy peers (overlap on [enterprise-grc](../categories/enterprise-grc.md) and [dspm](../categories/dspm.md))

## Open questions / to verify
- Confirm latest valuation/funding against a primary source (filing or company statement) — current figures are from aggregators (PitchBook/Crunchbase/getLatka); confidence medium.
- Any 2024-2026 funding events or renewed IPO talk.
- Depth of AI Governance bias/fairness evaluation vs pureplays — likely shallower; verify against current product docs.
- Exact pricing/packaging of AI Governance as a standalone vs bundled add-on.

## Sources
- [OneTrust Introduces AI Governance Solution (press release)](https://www.onetrust.com/news/onetrust-introduces-ai-governance-solution/) — fetched 2026-06-28 — supports: AI Governance capabilities, EU AI Act/NIST AI RMF/ISO 42001 mapping, May 2023 launch; confidence: high (vendor primary, mark capabilities as vendor claims).
- [OneTrust — Wikipedia](https://en.wikipedia.org/wiki/OneTrust) — fetched 2026-06-28 — supports: founding 2016, founder Kabir Barday, Atlanta HQ, private ownership, product modules, acquisitions, customer count; confidence: medium.
- [Search aggregators (PitchBook, Crunchbase/getLatka, Contrary Research) via WebSearch](https://pitchbook.com/profiles/company/166325-05) — fetched 2026-06-28 — supports: ~$1.1B total funding, investor list, $150M 2023 down round at $4.5B, ~$500M ARR; confidence: medium (aggregator, not primary filing).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founding 2016 (Kabir Barday), Atlanta HQ, private/independent (growth-equity backed: Insight, TCV, Coatue, SoftBank, Generation IM), ~$1.1B raised, last round $150M/2023 at $4.5B down round, no IPO, no M&A of OneTrust. Documented AI Governance module (May 2023 launch) with EU AI Act / NIST AI RMF / ISO 42001 mappings and model/use-case inventory; positioned as GRC incumbent vs pureplays. Set status researched, confidence medium, hedge_fund_fit medium.
