---
title: Vendict
type: vendor
name: Vendict
slug: vendict
aka: []
primary_category: vendor-risk
also_listed_in: [enterprise-grc]
website: https://vendict.com/
founded: 2022
hq: Tel Aviv, Israel
ownership_state: independent
owner: null
ownership_note: VC-backed; ~$20M total. Emerged from stealth with $9.5M, then a $10M Series A announced August 2025 led by Moneta VC and JAL Ventures with NFX, Cardumen Capital, Disruptive AI and Cyber Club London.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$20M
last_funding: Series A $10M led by Moneta VC and JAL Ventures, 2025-08
market_position: {vendor-risk: ai-native-disruptor}
deployment_model: [saas]
form_factor: [platform, api]
data_leaves_tenancy: "true"
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: mid-market to enterprise
last_verified: 2026-08-26
verify_after: null
tags: [questionnaire-automation, tprm, genai, trust-center, grc-automation]
sources:
  - {claim: "$10M Series A led by Moneta VC and JAL Ventures with NFX, Cardumen Capital, Disruptive AI and Cyber Club London, announced August 2025; brings total funding to $20M", url: "https://vendict.com/blog/series-a-announcement", date: 2026-08-26, confidence: high}
  - {claim: "Emerged from stealth with $9.5M to automate security compliance with generative AI; extracts data from existing compliance material and generates questionnaire responses, shortening assessments from weeks to hours", url: "https://venturebeat.com/security/vendict-emerges-with-9-5m-in-funding-to-automate-security-compliance-with-generative-ai", date: 2026-08-26, confidence: medium}
---

# Vendict

> Primary category: [vendor-risk](../categories/vendor-risk.md). Also listed in [enterprise-grc](../categories/enterprise-grc.md).

**One-liner** — Generative-AI automation of the security-questionnaire treadmill: it reads the firm's existing compliance material and drafts questionnaire answers, cutting assessments from weeks to hours — and it runs in both directions, answering and issuing.

**What it does** — Attacks the single most labour-intensive part of third-party risk: the questionnaire. Vendict ingests an organisation's existing compliance corpus — policies, SOC 2 reports, ISO certificates, prior questionnaire responses — and uses an LLM stack to generate accurate, appropriately-worded answers to each item of an incoming questionnaire, in whatever format the counterparty demanded. It also covers the reverse direction (assessing your own vendors), trust centres, and audit workflow, positioning itself as AI-native GRC automation rather than a questionnaire tool alone.

**Why this matters for an alternative manager specifically.** The questionnaire burden runs both ways and is unusually heavy in this industry. A manager **answers** exhaustive operational due-diligence questionnaires from institutional allocators, consultants and fund administrators — a workload that lands on a small operations or compliance team and recurs constantly. It also **issues** questionnaires to its own vendors. Vendict is one of the few tools that addresses the answering side, which most of [vendor-risk](../categories/vendor-risk.md) ignores in favour of the issuing side. [whistic](whistic.md) is the closest comparison.

**Naming / provenance** — Founded 2022, Tel Aviv. Single brand.

**Ownership & viability** — `independent`, VC-backed, **~$20M total**: **$9.5M** at stealth exit, then a **$10M Series A announced August 2025** led by **Moneta VC** and **JAL Ventures**, with NFX, Cardumen Capital, Disruptive AI and Cyber Club London. Small and early. Note that Moneta VC also backs [panorays](panorays.md), a broader TPRM platform in the same category — the two are adjacent rather than directly competing, but it is worth knowing.

**Positioning & differentiators** —
- **Answers questionnaires, not just issues them.** The genuinely differentiated half, and the half a manager on the receiving end of allocator ODD actually feels.
- **Corpus-grounded generation.** Answers are drawn from the firm's own attested compliance material rather than freely generated — which is the only defensible design, since a fabricated questionnaire answer is a misrepresentation to a counterparty.
- **Versus [panorays](panorays.md)'s Smart Match:** the incumbents are adding questionnaire autofill as a feature. Vendict's bet is that doing only this, better, wins. That is a narrow moat against well-funded platforms.
- **Versus [whistic](whistic.md):** Whistic built a vendor-profile exchange network; Vendict is AI-first on generation. Different mechanisms for the same pain.

**Who should choose them / anti-fit** — Fits a **firm drowning in inbound security and due-diligence questionnaires** with a small team answering them — a very recognisable alternative-manager problem. **Anti-fit:** a firm whose need is outside-in vendor monitoring and ratings ([bitsight](bitsight.md), [securityscorecard](securityscorecard.md)), or one wanting a full TPRM platform of record ([processunity](processunity.md), [panorays](panorays.md)).

**Known weaknesses / gotchas** — **The governance question is the important one and it is unresolved on this page: an LLM drafting answers that go to allocators and regulators must not fabricate.** Everything depends on how tightly generation is grounded in the source corpus, how confidently it flags gaps rather than filling them, and what the human review step looks like. That is the thing to test in a pilot, with deliberately unanswerable questions. Beyond that: small vendor, no independent evaluation, competing against platform incumbents adding the same feature.

**Deployment & data handling** — SaaS, also listed on AWS Marketplace. **The firm's complete compliance corpus is uploaded** — policies, audit reports, prior answers — which is a concentrated and sensitive dataset. Where it is stored, retention, and **whether it trains shared models** are unverified and are blocking diligence questions.

**Integrations & partnerships** — AWS Marketplace listing; GRC and ticketing integrations claimed. Specific list unverified. MCP support unverified.

**Compliance & FS traction** — **Unverified.** No named financial-services customers confirmed; certifications not confirmed — notable for a vendor selling compliance automation.

**Commercial** — Not public.

## Open questions

- **Hallucination controls**: how generation is grounded, how gaps are flagged, what the mandatory human-review step is.
- Whether the uploaded compliance corpus trains shared models; retention and residency.
- Certifications held — a compliance vendor without its own SOC 2 would be a notable finding either way.
- Named customers, particularly any asset managers answering allocator ODD.
- How it holds up against [panorays](panorays.md)'s and [whistic](whistic.md)'s equivalent features on the same questionnaire set.

## Sources

- [Announcing Vendict's $10M Series A (Vendict)](https://vendict.com/blog/series-a-announcement) — fetched 2026-08-26 — supports: Series A, investors, total funding; confidence: high (primary)
- [Vendict emerges with $9.5M to automate security compliance with generative AI (VentureBeat)](https://venturebeat.com/security/vendict-emerges-with-9-5m-in-funding-to-automate-security-compliance-with-generative-ai) — fetched 2026-08-26 — supports: stealth-exit funding, product mechanism; confidence: medium
- Cached: `raw/sources/2026-08-26--vendict--funding-and-questionnaire-automation.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki — a human had added it to the vendor-risk question alongside [panorays](panorays.md).
