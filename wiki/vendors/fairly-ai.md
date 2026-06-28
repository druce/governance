---
type: vendor
name: Fairly AI
slug: fairly-ai
categories: [ai-governance-platform]
layer: governance
aliases: [Asenion, anch.AI]
website: https://www.asenion.ai/
founded: 2020
hq: Kitchener-Waterloo, Ontario, Canada
ownership: independent
ownership_detail: "Independent venture-backed startup. Acquirer (not target): bought Swedish startup anch.AI on 2025-06-20 and rebranded the combined company as Asenion."
ownership_confidence: medium
funding_total: "~US$3.36M (aggregator-reported; unverified)"
last_funding: "CAD $2.2M seed (April 2023; aggregator-reported)"
deployment: [saas, api]
target_customer: regulated enterprises and AI-native product companies (financial services, insurance, HR-tech, healthcare, legal)
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [ai-governance, grc, model-validation, eu-ai-act, nist-ai-rmf, iso-42001, canada]
---

# Fairly AI

> Now operating as **Asenion** (rebranded after acquiring anch.AI, 2025-06-20). Primary category: [[ai-governance-platform]].

**One-liner** — A small Canadian AI governance/compliance (GRC) platform that assesses, tests, and provides runtime "assurance" for AI models and agents against regulatory frameworks (EU AI Act, NIST AI RMF, ISO 42001), pitched as "AI compliance in a box."

## What it does

Fairly AI (now Asenion) is an AI governance, risk, and compliance platform organized around three verbs:

- **Assess** — evaluate AI agents, models, systems, and data against an organization's internal policies and external regulatory requirements.
- **Test** — adversarial and behavioral testing (red-teaming) to surface security, privacy, fairness/bias, and safety problems before deployment.
- **Assure** — runtime governance and guardrails for agentic/LLM systems running in production.

The product is framed as turning weeks-long model audits into minutes, with "policy-as-code" controls and a "living compliance" framework that tracks evolving regulation. It markets two tiers: a lightweight "AI compliance in a box" for startups and scalable testing tooling for larger enterprises. The company claims patent-pending technology for automated compliance controls and helped a customer reach ISO/IEC 42001 certification.

## Where it sits in the stack

This is a **[[ai-governance-platform]]** play at the **governance layer** — the documentation/policy/model-validation control plane that sits above the runtime stack, not in the data path. It is registry-, evidence-, and workflow-centric: inventory AI systems, run validation/red-team tests, map results to regulatory controls, and produce audit artifacts.

- **Lethal-trifecta role:** none directly. It does not break the untrusted-input / sensitive-data / egress chain inline; the "Assure" runtime-guardrail capability is adjacent to runtime security but the company's center of gravity is governance/assurance, not an inline AI firewall.
- **Trust zone:** governance/oversight plane spanning all zones via evidence, rather than enforcement inside any one zone.

## Deployment & architecture

SaaS platform with API/connector-based assessment and testing; "Assure" adds runtime monitoring/guardrails for LLM and agentic systems. Exact integration surface (which model hosts, gateways, SIEM, IdP it plugs into) is not well documented publicly. Treat deployment specifics as thinly evidenced.

## Positioning & differentiators

Fairly/Asenion positions on **breadth of regulatory mapping plus testing/red-teaming**, and leans on third-party validation (named in the IDC MarketScape for Worldwide AI Governance Platforms 2023–2026 and as a representative vendor across several Gartner AI TRiSM categories). The 2025 anch.AI acquisition added European ethical-AI/EU-AI-Act framing (anch.AI founder Anna Felländer is a known EU AI-ethics figure) and a Stockholm presence.

Versus neighbors:
- **[[credo-ai]]** and **[[holistic-ai]]** — larger, better-funded, more mature AI-GRC/governance platforms; Fairly is smaller and lower-profile.
- **[[monitaur]]** — overlaps on model validation / model-risk documentation, with a stronger insurance/model-risk heritage.
- **[[governgpt]]** — narrower; due-diligence/questionnaire automation rather than full lifecycle governance.

The honest read: Fairly AI is an early-stage, niche vendor whose differentiation (fast audits, agentic-AI assurance, EU coverage via anch.AI) is largely self-asserted and hard to corroborate independently.

## Ownership, funding & M&A

- **Ownership:** independent, venture-backed. Confidence **medium**.
- **M&A (verified):** Fairly AI was the **acquirer**, not a target — it acquired Swedish startup **anch.AI** and rebranded the combined company **Asenion**, announced **2025-06-20** (Communitech; corroborated by Startup Ecosystem Canada). No public deal terms.
- **Founders / founded:** David Van Bruwaene (CEO) and Fion Lee-Madan (COO); founded ~2020 (aggregator-reported).
- **Funding:** aggregators report ~US$3.36M total over five rounds, including a CAD $2.2M seed (dated April 2023 by aggregators; described as "recently secured" in June 2025 press — a discrepancy in framing, with the $2.2M figure consistent). Investors reportedly include Techstars Toronto, Loyal VC, NEXT Canada, Backstage Capital, XFactor Ventures. Funding totals/round counts are aggregator-sourced and **not primary-verified**.

## CTO / hedge-fund lens

- **Day-1 or Day-2?** Day-2. Governance/assurance tooling matters once a fund is deploying multiple internal AI systems/agents and needs an audit trail — not on day one.
- **SR 11-7 / OSFI relevance:** Conceptually adjacent — model validation, testing, and documentation are the SR 11-7 (US model-risk) and OSFI E-23 (Canadian) wheelhouse. However, the public material emphasizes **EU AI Act, NIST AI RMF, ISO 42001, Colorado AI Act, and fair-lending/HR-bias** mapping; explicit SR 11-7 / OSFI E-23 coverage is **not confirmed** from the sources reviewed. Verify before relying on it for bank/asset-manager model-risk workflows.
- **When you'd need it:** a regulated shop building AI-native products that wants outsourced "compliance-in-a-box" plus red-teaming. For most hedge funds this is overkill versus a heavier model-risk/governance incumbent.
- **Maturity/size caveat:** This is a **small, early-stage vendor** (single-digit-millions funded) mid-rebrand. Vendor-viability and support-depth risk is real for an institutional buyer; weigh against larger governance platforms. Hence **hedge_fund_fit: low**.

## Competitors / alternatives

[[credo-ai]] · [[holistic-ai]] · [[monitaur]] · [[governgpt]]

## Open questions / to verify

- Primary-source confirmation of founding year, funding total, and round history (aggregator-only today).
- Whether it explicitly supports SR 11-7 / OSFI E-23 model-risk workflows, or only EU AI Act / NIST / ISO 42001 / Colorado AI Act.
- Concrete deployment/integration details (model hosts, gateways, SIEM/IdP, MCP) for the "Assure" runtime layer.
- Post-acquisition org: where anch.AI's product/team folded in, and whether "Fairly AI" or "Asenion" is the going-forward legal entity and contracting party.
- Real customer references in financial services beyond marketing recognition (IDC/Gartner listings).

## Sources

- [Asenion (formerly Fairly AI) vendor site](https://www.asenion.ai/) — fetched 2026-06-28 — supports: product (Assess/Test/Assure), regulatory coverage (ISO 42001, NIST AI RMF, EU AI Act, Colorado AI Act), HQ Kitchener, target customers; confidence: med (vendor marketing).
- [Communitech — Fairly AI acquires anch.AI](https://www.communitech.ca/technews/kitchener-based-fairly-ai-acquires-swedish-startup-anch.ai-to-help-companies-build-regulation-ready-ai.html) — fetched 2026-06-28 — supports: acquisition date 2025-06-20, Asenion rebrand, founders, HQ, $2.2M seed; confidence: high.
- [Startup Ecosystem Canada — Fairly AI acquires Anch.AI](https://www.startupecosystem.ca/news/fairly-ai-acquires-anch-ai-to-advance-global-ai-governance/) — fetched 2026-06-28 — supports: acquisition + rebrand corroboration, target sectors, product tiers; confidence: med.
- [Crunchbase / PitchBook / Tracxn (aggregators, via search)](https://www.crunchbase.com/organization/fairly-ai) — fetched 2026-06-28 — supports: founded 2020, founders, ~US$3.36M total / CAD $2.2M seed, investors; confidence: low (aggregator, unverified).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Fairly AI = Canadian (Kitchener-Waterloo) early-stage AI-GRC startup, founded ~2020 by Van Bruwaene & Lee-Madan, ~US$3.36M funded (aggregator). Confirmed it ACQUIRED anch.AI (Sweden) on 2025-06-20 and rebranded to Asenion — Fairly is acquirer, ownership stays independent (no contradiction with stub). Covers EU AI Act / NIST AI RMF / ISO 42001 / Colorado AI Act; SR 11-7 / OSFI E-23 not confirmed. hedge_fund_fit set to low (small/early-stage). status -> researched, confidence -> medium.
