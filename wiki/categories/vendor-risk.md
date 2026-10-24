---
title: Third-Party / Vendor Risk + Cyber Ratings
type: category
name: Third-Party / Vendor Risk + Cyber Ratings
slug: vendor-risk
category: vendor-risk
layer: governance
survey_question: Vendor Risk Rating & Monitoring
adoption_tier: day-1
trigger: extend existing TPRM to AI vendors and AI features of existing vendors
maturity_stage_required: null
category_maturity: mature
adjacent: [enterprise-grc, third-party-ai-apps]
incumbent_coverage: []
vendor_count: 11
maps_to_seed_doc: Third-Party / Vendor Risk + Cyber Ratings
maps_to_seed_csv: Vendor Risk
last_verified: 2026-07-27
---

## Business objective

The background check on every AI vendor before they touch your data — and the
continuous monitoring after. Third-party/vendor risk management (TPRM) assesses and
monitors the security, privacy, and operational risk a supplier brings, via two
complementary mechanisms: **questionnaire-driven assessments** (you ask the vendor
to document controls, SOC 2, data handling, subprocessors) and **outside-in cyber
ratings** (a continuous, externally observed security score of the vendor's attack
surface). For AI, the new wrinkle is which models the vendor uses, where prompts and
data go, what is retained, and which fourth parties (model providers,
subprocessors) sit behind them.

## When you need it

**Day-1 — extend existing TPRM to AI vendors.** Like [enterprise-grc](enterprise-grc.md), a regulated
firm already runs a TPRM program; the AI task is to extend it, not to buy a new tool.
The moment a hedge fund signs up for an enterprise AI assistant, an AI gateway, a
data vendor with AI features, or any SaaS that quietly added an LLM, that supplier
needs to pass third-party diligence: data residency, training-data use, retention,
subprocessor disclosure, and breach history. A CTO's Day-1 move is to add AI-specific
questions to the standard vendor questionnaire and to flag AI/model subprocessors in
the vendor inventory. This is where "is our data being used to train someone's model?"
gets answered contractually.

## Security role

**Oversight, not enforcement.** Vendor risk does not sit inline and blocks nothing
at runtime. It is a **green-zone governance control** that gates *which* external
parties (and their outbound data paths) you allow into the stack in the first
place — an upstream, preventive filter on the supply chain rather than a runtime
enforcement point. Closely related but distinct from [software-supply-chain](software-supply-chain.md) (code/dependency
provenance) and [non-human-identity](non-human-identity.md) (machine credentials for those vendors' agents).

## Vendors

Often deployed in pairs — one assessment/workflow platform plus one or more ratings
feeds:

- [processunity](../vendors/processunity.md) — TPRM assessment + workflow platform (vendor onboarding, questionnaires, lifecycle).
- [securityscorecard](../vendors/securityscorecard.md) — outside-in cyber ratings; continuous external security scoring.
- [bitsight](../vendors/bitsight.md) — outside-in cyber ratings; large ratings dataset, common benchmark.
- [black-kite](../vendors/black-kite.md) — cyber ratings with financial-impact and ransomware-susceptibility framing.
- [upguard](../vendors/upguard.md) — cyber ratings + attack-surface / vendor monitoring, lighter-weight.
- [venminder](../vendors/venminder.md) — TPRM assessment platform + analyst-performed vendor reviews; FI-heavy; part of Ncontracts since 2024.
- [whistic](../vendors/whistic.md) — security-questionnaire automation and vendor-profile exchange network; AI-assisted assessments.
- [panorays](../vendors/panorays.md) — combines both halves in one tool: outside-in ratings plus questionnaire workflow, with DORA/NIS2 regulatory mapping and LLM-assisted questionnaire autofill. Forrester Wave Leader, Q2 2026. (added 2026-08-26)
- [vendict](../vendors/vendict.md) — GenAI questionnaire automation that works in **both directions**: it drafts the answers to inbound allocator/counterparty questionnaires from the firm's own compliance corpus, not just the ones you issue. The half of this category most alternative managers actually feel. (added 2026-08-26)
- [drawbridge](../vendors/drawbridge.md) — Cyber-programme software + advisory services built only for hedge funds/PE; vendor due diligence is one advisor-led service line, benchmarked against 1,000+ peer managers. Cross-listed to [enterprise-grc](enterprise-grc.md). (added 2026-10-23)
- [viso-trust](../vendors/viso-trust.md) — AI-native TPRM that assesses vendors from their existing SOC 2/audit artifacts instead of questionnaires, with 4th/nth-party monitoring; now a Protecht brand (acquired 2026-04). Cross-listed to [enterprise-grc](enterprise-grc.md). (added 2026-10-23)

### Also named in survey write-ins (no page)

- BlueVoyant Supply Chain Defense — fully managed third-party cyber-risk monitoring with BlueVoyant analysts working remediation with the vendors.
- Mitratech (Prevalent) — Mitratech acquired Prevalent (completed 2024-10-02); Prevalent TPRM is now a Mitratech product.
- Safe Security (SAFE TPRM) — "autonomous" agentic-AI TPRM with FAIR-based scores, launched 2025-05-28 (vendor marketing).

## Consolidation / M&A dynamics

A market split between assessment/workflow platforms (ProcessUnity, Venminder,
Whistic) and ratings providers (BitSight, SecurityScorecard, Black Kite, UpGuard) —
and consolidating: **Ncontracts acquired Venminder** (announced 2024-09-04, via an Hg
buyout), ProcessUnity had earlier merged with CyberGRX, and SecurityScorecard bought
HyperComply (2025) to add questionnaire automation. The live trend is ratings vendors
and TPRM platforms each adding AI-vendor-specific risk modules and "is this vendor
using AI / training on your data" signals.

## Adjacent categories

- [enterprise-grc](enterprise-grc.md) — TPRM is frequently a module of the same GRC suite; the vendor register lives there.
- [software-supply-chain](software-supply-chain.md) — code/dependency provenance, the engineering-side cousin of vendor risk.
- [ai-governance-platform](ai-governance-platform.md) — vendor/model risk feeds the broader AI risk register.
- [non-human-identity](non-human-identity.md) — once a vendor's agents are in your environment, they need governed machine identities.

## Survey

**Question.** Which third-party/vendor-risk and cyber-ratings tools does your firm
use to assess and monitor suppliers (including AI vendors)?

**Answer options.** ProcessUnity; SecurityScorecard; BitSight; Black Kite; UpGuard;
Venminder (Ncontracts); Whistic; Panorays; Vendict; Drawbridge; VISO TRUST (Protecht); Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** Respondents commonly use an assessment platform *and* a
ratings feed, so multi-select is essential and overlap is expected, not noise.
BitSight and SecurityScorecard are the table-stakes ratings names; Black Kite and
UpGuard are credible alternatives/additions. Venminder skews to banks/credit unions —
useful to see whether buy-side firms use it too; Whistic is the questionnaire-exchange
niche. Many firms run TPRM inside their
[enterprise-grc](enterprise-grc.md) tool (ServiceNow, Archer, OneTrust) rather than a dedicated
product — add an "our GRC platform handles this" option or follow-up. Consider asking
separately whether AI-specific vendor questions have been added to the standard
questionnaire. Drawbridge answers measure "outsourced vendor DD to a specialist", not "which TPRM platform you run".

## Open taxonomy questions

- Overlap with [enterprise-grc](enterprise-grc.md): TPRM as a module vs a standalone tool. Survey
  should capture both.
- Ratings (outside-in) vs assessments (inside-out) are arguably two sub-segments;
  kept together here as one buyer's map but could split if responses warrant.
