---
title: Panorays
type: vendor
name: Panorays
slug: panorays
aka: []
primary_category: vendor-risk
also_listed_in: [third-party-ai-apps]
website: https://panorays.com/
founded: 2016
hq: New York, NY, USA (R&D in Tel Aviv, Israel)
ownership_state: independent
owner: null
ownership_note: VC-backed; roughly $62–67M raised (sources differ). $42M Series B led by Greenfield Partners, announced 2021-09. Investors include Aleph VC, Oak HC/FT, StepStone Group, BlueRed Partners, Moneta VC, plus angels Amichai Shulman (Imperva co-founder) and Lane Bess. No acquisition found as of 2026-08-26.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$62–67M (sources differ)
last_funding: Series B $42M led by Greenfield Partners, 2021-09
market_position: {vendor-risk: challenger}
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: mid-market to enterprise
last_verified: 2026-08-26
verify_after: null
tags: [tprm, vendor-risk, cyber-ratings, questionnaire-automation, nis2, dora]
sources:
  - {claim: "Named a Leader in The Forrester Wave: Cybersecurity Risk Rating Platforms, Q2 2026 (published 2026-04-09), with highest possible scores in nine criteria including AI Capabilities and Innovation & Roadmap", url: "https://panorays.com/blog/forrester-report-2026/", date: 2026-08-26, confidence: medium}
  - {claim: "$42M Series B led by Greenfield Partners; investors include Aleph VC, Oak HC/FT, StepStone, BlueRed Partners, Moneta VC, Amichai Shulman, Lane Bess", url: "https://panorays.com/blog/panorays-closes-42-million-series-b-funding-round-to-revolutionize-third-party-security/", date: 2026-08-26, confidence: high}
  - {claim: "2026 Panorays study: 85% of CISOs report they cannot see third-party threats; AI adoption in TPRM rose from 27% to 66% year over year", url: "https://www.cio.com/article/4116858/2026-study-from-panorays-85-of-cisos-cant-see-third-party-threats-amid-increasing-supply-chain-attacks.html", date: 2026-08-26, confidence: medium}
---

# Panorays

> Primary category: [vendor-risk](../categories/vendor-risk.md). Also listed in [third-party-ai-apps](../categories/third-party-ai-apps.md).

**One-liner** — Third-party cyber risk management that combines outside-in attack-surface ratings with inside-out security questionnaires in one workflow — and now uses an LLM to autofill both sides of the questionnaire exchange.

**What it does** — Two halves. **Outside-in:** automated external attack-surface assessment of a supplier's internet-facing footprint, producing a rating — the same basic technique as [bitsight](bitsight.md), [securityscorecard](securityscorecard.md) and [black-kite](black-kite.md). **Inside-out:** the security questionnaire workflow — issuing, chasing, scoring and reconciling supplier responses, which is [processunity](processunity.md) and [whistic](whistic.md) territory. Panorays' argument is that neither half is sufficient alone: a rating tells you nothing about a supplier's internal controls, and a questionnaire is self-reported. It contextualises both against how the supplier is actually used (what data they hold, what access they have), and layers regulatory mapping — **DORA, NIS2, GDPR** — over the assessment.

The 2026 product direction is AI-assisted throughput. **Smart Match** extracts answers from a supplier's uploaded certifications, attestations and prior documentation to autofill questionnaires — attacking the real bottleneck in TPRM, which is the human hours spent on questionnaire round-trips rather than the assessment logic.

**Naming / provenance** — Founded 2016; Israeli R&D with a New York commercial HQ. Single brand, no renames.

**Ownership & viability** — `independent`, VC-backed. Roughly **$62–67M** raised (sources disagree on the total; the **$42M Series B led by Greenfield Partners in September 2021** is firm). Investor list includes Oak HC/FT and StepStone plus notable security angels. No round found since 2021 and no acquisition as of 2026-08-26 — the same five-year funding gap that applies to several vendors in this category. Named a **Leader in the Forrester Wave for Cybersecurity Risk Rating Platforms, Q2 2026**, which is meaningful third-party validation of product, not of balance sheet.

**Positioning & differentiators** —
- **Both halves in one tool.** The ratings vendors ([bitsight](bitsight.md), [securityscorecard](securityscorecard.md)) and the questionnaire vendors ([processunity](processunity.md), [whistic](whistic.md), [venminder](venminder.md)) have been converging on each other for years; Panorays was built at the intersection.
- **Regulatory mapping for DORA and NIS2.** Directly relevant to any manager with EU-regulated entities or EU counterparties — DORA's ICT third-party register is exactly this workload.
- **AI-assisted questionnaire processing** is where Forrester scored it highest. For a small compliance team, throughput is the binding constraint, so this is the differentiator most likely to matter in practice.
- **Extends to AI vendors.** The natural path for assessing the AI features your existing SaaS suppliers have quietly switched on — see [third-party-ai-apps](../categories/third-party-ai-apps.md). Whether Panorays ships a *specific* AI-vendor assessment template is unverified below.

**Who should choose them / anti-fit** — Fits a firm running a **real TPRM programme over dozens-to-hundreds of suppliers**, especially with DORA/NIS2 exposure, and a small team that needs the questionnaire cycle automated. The typical alternative-investment profile — heavy vendor concentration in fund admin, prime brokerage, market data, and now AI SaaS — matches well. **Anti-fit:** a firm that only wants a cheap outside-in score to satisfy a checkbox (a ratings-only vendor is cheaper), or one whose GRC suite ([hyperproof](hyperproof.md), [onetrust](onetrust.md), [archer](archer.md)) already carries an adequate TPRM module.

**Known weaknesses / gotchas** — Funding age versus a consolidating category. The published research it markets (the CISO survey) is vendor-sponsored — useful directionally, not as evidence. Outside-in rating accuracy suffers the same well-known limitations as every vendor in this space: attribution of internet assets to the right corporate entity is error-prone, and disputes with rated suppliers are routine.

**Deployment & data handling** — SaaS. Where assessment data resides, EU residency options, and retention terms are **unverified** — a live question for a DORA-driven purchase.

**Integrations & partnerships** — GRC and ticketing integrations claimed; specific connector list unverified.

**Compliance & FS traction** — **Unverified.** DORA/NIS2 mapping implies financial-services intent, but no named FS customers were confirmed. Certifications held not confirmed.

**Commercial** — Not public. Subscription, typically scaled by number of suppliers monitored.

## Open questions

- Reconcile total funding (~$62M vs ~$67M) and confirm whether anything has been raised since 2021.
- EU data residency — necessary to answer before a DORA-driven purchase.
- Certifications held; named financial-services customers.
- Does Panorays ship a purpose-built **AI-vendor** assessment template, or is AI risk handled through generic questionnaire customisation?
- Practical accuracy of the outside-in ratings versus [bitsight](bitsight.md)/[black-kite](black-kite.md) on the same supplier set.

## Sources

- [Panorays Recognized as a Leader in The Forrester Wave, Q2 2026 (Panorays)](https://panorays.com/blog/forrester-report-2026/) — fetched 2026-08-26 — supports: Forrester Leader placement, scored criteria; confidence: medium (vendor summary of a paid analyst report)
- [Panorays Closes $42 Million Series B (Panorays)](https://panorays.com/blog/panorays-closes-42-million-series-b-funding-round-to-revolutionize-third-party-security/) — fetched 2026-08-26 — supports: Series B size, lead, investor list; confidence: high (primary)
- [2026 Study from Panorays: 85% of CISOs Can't See Third-Party Threats (CIO)](https://www.cio.com/article/4116858/2026-study-from-panorays-85-of-cisos-cant-see-third-party-threats-amid-increasing-supply-chain-attacks.html) — fetched 2026-08-26 — supports: AI-in-TPRM adoption trend; confidence: medium (vendor-sponsored research)
- Cached: `raw/sources/2026-08-26--panorays--funding-and-forrester-2026.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Sourced from the 2026-08-25 competitor scan (Tier A, score 8) — surfaced as a peer by OneTrust.
