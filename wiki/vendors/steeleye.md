---
type: vendor
name: SteelEye
slug: steeleye
categories: [comms-surveillance]
layer: governance
aliases: []
website: https://www.steel-eye.com
founded: 2017
hq: London, UK
ownership: independent
ownership_detail: "VC-backed, independent. Series B ($21M, 2022-09) led by Ten Coves Capital; total raised ~$43M. No acquisition found as of 2026-06-28."
ownership_confidence: medium
funding_total: ~$43M
last_funding: "Series B, $21M, 2022-09 (led by Ten Coves Capital)"
deployment: [saas, api]
target_customer: regulated financial firms (banks, brokers, asset managers, hedge funds); positioned for mid-size firms
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [comms-surveillance, trade-surveillance, market-abuse, mar, recordkeeping, regtech]
---

# SteelEye

**One-liner** — A London-based regtech that bundles trade surveillance, communications surveillance, recordkeeping/archiving and regulatory reporting onto a single cloud platform, pitched as one place to catch market abuse and meet records rules.

## What it does

SteelEye is an integrated compliance platform for regulated financial firms. Its core jobs:

- **Communications surveillance** — captures and monitors email, chat, voice, meetings and attachments, scanning for market abuse, MNPI/insider risk and conduct breaches.
- **Trade surveillance** — monitors orders and executions for market-manipulation patterns (spoofing, layering, wash trades, front-running) against the EU/UK **Market Abuse Regulation (MAR)** and equivalent regimes.
- **Recordkeeping & archiving** — WORM-style retention of communications and trade data, with eDiscovery and **trade reconstruction** (rebuilding the full comms + trade timeline around an event).
- **Best execution / transaction cost analysis** and **regulatory reporting** (e.g. MiFIR).

The pitch is that holding comms, trade and reference data in one place lets surveillance correlate *what was said* with *what was traded* — the combination that actually surfaces market abuse and MNPI misuse, rather than two siloed tools.

Its AI layer, **Compliance CoPilot** (launched 2023-11), uses LLMs to triage and explain surveillance alerts across both trade and comms — ranking alerts, assigning a risk score, suggesting a resolution category and writing a rationale, with a vendor-claimed reduction in review time (marketing). It analyzes communications in 12 languages and returns insights in English. Note this is **AI-assisted review of alerts**, not (per available primary sources) capture of employees' own generative-AI prompt/response traffic as a surveilled channel — see Open questions.

## Where it sits in the stack

- Category: [[comms-surveillance]], in the **governance** layer.
- This is a **detective control**, not a preventive one — it does "none-detection" (catching abuse/MNPI/conduct after the fact in logged comms and trades). It is a **green-zone backstop**: it watches the trusted internal environment for misconduct rather than blocking untrusted input or egress.
- It does **not** break a leg of the lethal trifecta (`trifecta_relevance: none`); its value is regulatory and conduct oversight, not data-exfiltration prevention.

## Deployment & architecture

- **Cloud / SaaS** data platform; data-ingestion- and API-led. Consolidates fragmented sources (comms channels, order/execution feeds, reference data) into a single store for surveillance, reporting and reconstruction.
- Integrates with **communications-capture vendors** (email, Teams/Slack/Zoom, mobile/voice, chat) and ingests **trade/order data** to align comms with trades.
- SOC 2 and ISO certified (vendor-stated). UK entity registered in England and Wales (#10581067); offices in London, New York, Singapore, Bangalore and Braga.

## Positioning & differentiators

SteelEye's distinguishing claim is the **single integrated platform** spanning trade surveillance + comms surveillance + recordkeeping + reporting, versus point tools you have to stitch together. How it differs from neighbors:

- vs [[behavox]] and [[shield]] — both are comms-surveillance / conduct specialists leaning heavily on AI/NLP; SteelEye spans the wider compliance stack (trade surveillance, reporting, recordkeeping) rather than being comms-first.
- vs [[nice-actimize]] — NICE Actimize is the incumbent enterprise surveillance/financial-crime suite (tier-1 banks); SteelEye positions as a more consolidated, lower-friction option aimed at mid-size firms.
- vs [[theta-lake]] — Theta Lake focuses on capture/compliance for modern collaboration tools (video, voice, UC); SteelEye covers comms surveillance but as part of a broader trade+records platform.
- vs [[relativity-trace]] — Relativity Trace is comms-surveillance built on Relativity's eDiscovery lineage; SteelEye couples comms with native trade surveillance and reporting.

## Ownership, funding & M&A

- **Independent, VC-backed.** Founded **2017** (London); CEO and co-founder **Matt Smith** (ex-Bloomberg, ex-Noble Group CIO). Other co-founders reported: Matthew/Matt Storey (CPO), David Haines (CTO), Shankar Vasudevan, Chris Young.
- **Series B: $21M, announced 2022-09**, led by **Ten Coves Capital**, with Fidelity International Strategic Ventures, Illuminate Financial, Beacon Equity Partners and a large family office; **total raised ~$43M**. Eight Roads Ventures also cited as an investor (aggregator data).
- **No acquisition found** as of 2026-06-28 — ownership remains independent. Confidence: medium (corroborated press + vendor; exact cap table not public).

## CTO / hedge-fund lens

- **Day-2, but hedge-fund-critical.** Comms + trade surveillance and recordkeeping are regulatory obligations under **MAR** (EU/UK), and **SEC / FINRA / CFTC / NFA** records and supervision rules in the US — including the SEC/CFTC **off-channel communications** ("WhatsApp") enforcement wave that has hit asset managers and advisers. A fund of any size handling MNPI needs *some* surveillance + recordkeeping answer; this is the layer.
- SteelEye is frequently pitched to **mid-size firms** that want one consolidated platform rather than a tier-1 stack (NICE Actimize) plus separate capture/archiving tools. That consolidation can be attractive to a lean compliance team.
- The **AI angle** (Compliance CoPilot) is mainly an efficiency play — fewer analyst hours per alert — relevant if alert volume is the pain point. Treat the "90%" figure as vendor marketing.
- Diligence points for a CTO: which comms channels you actually capture upstream (SteelEye surveils what it ingests), data residency, and whether you need trade surveillance at all (a pure long-only fund's MAR exposure differs from a multi-strategy/active trader).

## Competitors / alternatives

[[behavox]] · [[shield]] · [[nice-actimize]] · [[theta-lake]] · [[relativity-trace]]

## Open questions / to verify

- Does SteelEye capture **employees' generative-AI tool usage (prompt/response)** as a monitored surveillance channel? Compliance CoPilot is AI *assisting* alert review; no primary source confirms AI-prompt capture as a channel. Flag — likely conflation in the brief.
- Exact post-Series B cap table / control; whether any funding has occurred since 2022.
- Precise list of native trade-surveillance model coverage and which capture vendors are pre-integrated.

## Sources

- [SteelEye — About us](https://www.steel-eye.com/about-us) — fetched 2026-06-28 — supports: HQ London + offices, platform capabilities (trade/comms surveillance, recordkeeping, MAR, best execution, reporting, trade reconstruction), cloud platform, leadership, SOC2/ISO; confidence: med (vendor/marketing).
- [SteelEye raises $21 million in Series B funding — bobsguide](https://www.bobsguide.com/steeleye-raises-21-million-in-series-b-funding/) — fetched 2026-06-28 — supports: Series B $21M (2022-09), lead Ten Coves Capital, investors, ~$43M total, "London-based SaaS regtech"; confidence: high.
- [SteelEye introduces AI-driven Compliance CoPilot](https://www.steel-eye.com/news/steeleye-introduces-ai-driven-compliance-copilot) — fetched 2026-06-28 — supports: Compliance CoPilot launch 2023-11, LLM alert triage across trade+comms, 12 languages, Matt Smith quote; confidence: med (vendor/marketing).
- Corroborating (WebSearch, not separately cached): Tracxn / Crunchbase — founded 2017, founders, Eight Roads Ventures as investor; confidence: med (aggregators).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2017 (London), CEO/co-founder Matt Smith, independent VC-backed (Series B $21M 2022-09 led by Ten Coves Capital, ~$43M total — no acquisition), SaaS integrated trade+comms surveillance + recordkeeping + reporting platform with MAR coverage and AI "Compliance CoPilot" alert triage. Set ownership_confidence medium, status researched, hedge_fund_fit medium. Flagged that AI-prompt/response capture (vs AI-assisted alert review) is unconfirmed.
