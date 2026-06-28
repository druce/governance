---
type: vendor
name: Vanta
slug: vanta
categories: [ai-governance-platform, enterprise-grc]
layer: governance
aliases: []
website: "https://www.vanta.com"
founded: 2018
hq: San Francisco, CA, USA
ownership: independent
ownership_detail: Private, venture-backed. Series D $150M (2025-07, led by Wellington Management) at $4.15B valuation; ~$504M raised total. No acquisition of Vanta; Vanta is itself an acquirer (TrustPage 2023, Riskey 2025).
ownership_confidence: high
funding_total: ~$504M (as of 2025-07)
last_funding: Series D $150M, 2025-07 (Wellington Management lead), $4.15B valuation
deployment: [saas, api]
target_customer: SMB / startup / mid-market (moving upmarket to enterprise)
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [grc, compliance-automation, iso-42001, soc2, ai-governance]
---

# Vanta

> Primary category: [ai-governance-platform](../categories/ai-governance-platform.md). Also: [enterprise-grc](../categories/enterprise-grc.md).

**One-liner** — Automated security-and-compliance certification (SOC 2, ISO 27001, etc.) that has added an AI-governance module (ISO 42001, EU AI Act, NIST AI RMF mapping); strong on continuous control evidence, light on true model-risk testing.

## What it does

Vanta is a GRC (governance, risk, compliance) automation platform. Its core job is to get a company *certified* and keep it certified: it connects to your cloud, identity, code, and SaaS tools (400+ integrations), continuously runs automated tests against controls (hourly), collects evidence, fills policy templates, and hands a clean package to third-party auditors. It made its name automating SOC 2 and ISO 27001 for startups.

On AI specifically, Vanta added an **ISO 42001 (AI Management System / AIMS)** product plus a dedicated **EU AI Act** compliance-automation product. These let an org scope its AI systems, stand up an AIMS, monitor controls, and cross-map evidence to neighbouring regimes. Vanta states ISO 42001 evidence overlaps roughly 50% with the EU AI Act and ~15% with the NIST AI RMF, and also maps to CPS 234 and ISO 27001. A "Vanta AI Agent" automates gap analysis, policy drafting, and security-questionnaire responses.

Important framing for a model-risk reader: this is **compliance automation, not model-risk management**. Vanta documents and proves that you *have* an AI governance program (policies, controls, an AIMS, audit evidence). It does not red-team models, test for jailbreaks/bias/hallucination, or quantify model risk. That deeper work belongs to dedicated AI-governance/testing vendors.

## Where it sits in the stack

- Layer: **governance** — the [ai-governance-platform](../categories/ai-governance-platform.md) and [enterprise-grc](../categories/enterprise-grc.md) categories.
- **Lethal-trifecta role: none.** Vanta is a documentation/attestation layer, not a runtime control. It does not sit in the path of untrusted input, sensitive data, or egress; it does not break any leg of the trifecta. It evidences that controls elsewhere exist.
- Trust zone: governance/oversight plane, not the data/model path.

## Deployment & architecture

SaaS, agentless-leaning, integration-driven. It pulls evidence via API from cloud providers (AWS, GCP, Azure), identity (IdP/SSO), version control (GitHub), and AI tooling (e.g., OpenAI). Outputs are dashboards, risk registers, nonconformity tracking, and a **Trust Center** for sharing compliance artifacts with prospects/auditors during diligence. Works alongside accredited ISO 42001 auditors who do the actual certification.

## Positioning & differentiators

- **Compliance automation first.** Vanta's strength is breadth of framework coverage and speed-to-audit (claims ~50% faster audits), not depth of AI risk analysis. Its AI governance is an extension of the same continuous-monitoring engine that does SOC 2.
- **vs [onetrust](onetrust.md)** — OneTrust is a broader enterprise GRC/privacy/AI-governance suite aimed at large regulated enterprises with deeper policy/privacy/inventory tooling; Vanta is leaner, faster to deploy, and historically SMB/mid-market.
- **vs [credo-ai](credo-ai.md) and [holistic-ai](holistic-ai.md)** — these are purpose-built AI-governance vendors that go deeper on model inventory, risk assessment, policy-to-control mapping for AI, and (Holistic AI) technical model testing/auditing. Vanta covers the *certification/attestation* slice (ISO 42001, EU AI Act evidence) but not technical model evaluation.
- Net: Vanta is the "get certified and prove it" tool, not the "interrogate the model" tool.

## Ownership, funding & M&A

- **Independent, private, venture-backed.** Confirmed; stub's "independent" stands. Confidence: high.
- Founded **2018** by Christina Cacioppo and Erik Goldman (both ex-Dropbox); HQ **San Francisco**, primarily remote with offices in US/UK/Ireland/Australia.
- Funding: Seed $3.5M (2018) → Series A $50M (2021, Sequoia) → Series B $110M (2022, Craft) + $40M ext. → Series C $150M (2024, Sequoia, $2.45B val.) → **Series D $150M (2025-07, Wellington Management lead), $4.15B valuation; ~$504M total raised.**
- **Vanta is an acquirer, not a target:** TrustPage (2023), Riskey (2025). No acquisition *of* Vanta found.

## CTO / hedge-fund lens

- **Day-2, and low fit for a fund's *model-risk* needs.** For an asset manager, Vanta's natural pull is the security-certification side (SOC 2/ISO 27001), often as something you *demand of your vendors* rather than run yourself.
- **SR 11-7 coverage: minimal.** SR 11-7 is about model validation, effective challenge, ongoing monitoring of model performance — Vanta does essentially none of that. ISO 42001/EU AI Act modules give you an *AI governance management system and audit evidence*, which is useful for showing regulators/clients you have a program, but it is not model validation. A fund treating AI as a model-risk problem needs a validation framework (internal or a [credo-ai](credo-ai.md)/[holistic-ai](holistic-ai.md)-type tool), not Vanta.
- **Size fit:** Vanta skews **startup/SMB/mid-market**. A large fund with an established GRC/model-risk function will likely find it thin; a small fund might use it to stand up SOC 2 / basic AI-governance attestation quickly.
- When you actually need it: if you must *get certified* (ISO 42001, SOC 2, EU AI Act readiness) fast and cheaply with continuous evidence, not when you need to *evaluate model risk*.

## Competitors / alternatives

[onetrust](onetrust.md), [credo-ai](credo-ai.md), [holistic-ai](holistic-ai.md); in the security-certification niche, Drata, Secureframe, Sprinto (not yet pages).

## Open questions / to verify

- Exact split of Vanta's revenue between core security compliance vs AI-governance modules (likely small AI share).
- Depth of EU AI Act product beyond evidence mapping — does it handle high-risk system classification workflow?
- Any technical model-testing partnerships (vs purely documentation)?

## Sources

- [Vanta announces Series D](https://www.vanta.com/resources/vanta-announces-series-d) — fetched 2026-06-28 — supports: $150M Series D, $4.15B valuation (2025-07), AI Agent positioning; confidence: high (vendor primary).
- [Vanta ISO 42001 product](https://www.vanta.com/products/iso-42001) — fetched 2026-06-28 — supports: AIMS/ISO 42001 compliance automation, EU AI Act ~50% / NIST AI RMF ~15% mapping, SaaS architecture, compliance-not-model-testing posture; confidence: high (vendor primary, marketing claims labeled).
- [Vanta (company) — Wikipedia](https://en.wikipedia.org/wiki/Vanta_(company)) — fetched 2026-06-28 — supports: 2018 founding, founders, HQ, private ownership, full funding/valuation history, ~$504M total, TrustPage/Riskey acquisitions; confidence: medium (secondary).

## History
- [2026-06-28] Researched; established independent/private (Series D $150M 2025-07 at $4.15B, ~$504M total, Wellington lead), founded 2018 SF by Cacioppo & Goldman, SaaS GRC automation skewing SMB/mid-market. ISO 42001 + EU AI Act modules are compliance-automation/attestation (maps to NIST AI RMF ~15%, EU AI Act ~50%), not model-risk testing — so weak SR 11-7 coverage; hedge_fund_fit set low. Ownership confirmed independent; no M&A of Vanta (it is an acquirer). Confidence raised to medium.
- [2026-06-28] Stub created from seed registry.
