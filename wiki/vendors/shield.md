---
type: vendor
name: Shield
slug: shield
categories: [comms-surveillance]
layer: governance
aliases: ["Shield FC", "Shield Financial Compliance"]
website: "https://www.shieldfc.com"
founded: 2018
hq: Tel Aviv, Israel (offices in New York and London)
ownership: independent
ownership_detail: "VC-backed independent; $20M Series B (2022-12) led by Macquarie Capital, with UBS Next, Mindset Ventures, OurCrowd. No acquisition found as of 2026-06-28."
ownership_confidence: medium
funding_total: "~$35M (as of 2022-12)"
last_funding: "Series B, $20M, 2022-12"
deployment: [saas, api]
target_customer: regulated (banks, broker-dealers, asset managers, PE); enterprise / tier-1
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [comms-surveillance, regtech, mar, mnpi, ecomms, conduct, ai-nlp]
---

# Shield

> Communications-compliance / e-comms surveillance SaaS for regulated financial
> firms, with AI/NLP analytics layered over the usual lexicon rules. Primary
> category: [comms-surveillance](../categories/comms-surveillance.md).

**One-liner** — An end-to-end communications-surveillance platform that captures,
correlates, and analyzes employees' electronic comms (and voice) to detect market
abuse, MNPI leakage, and misconduct for regulated financial institutions.

**Categories** — [comms-surveillance](../categories/comms-surveillance.md)

## What it does

Shield automates the full e-comms data lifecycle — capture, correlation,
enrichment, analytics, retention, and archiving — across the messaging and voice
channels regulated employees use (email, chat, collaboration tools, voice via an
NLP partnership). On top of the captured record it runs surveillance models to
flag market abuse (MAR-type scenarios), insider-dealing / MNPI risk, and conduct
issues, and supports supervision, record-keeping, and e-discovery workflows. The
pitch is to replace fragmented, single-channel point tools with one consolidated
data layer plus analytics so compliance teams can "read between the lines."

It is a **detective / supervisory** control: it does not block communications or
sit in any production AI data path. It reconstructs and reviews what was said
after the fact.

## Where it sits in the stack

This is a [comms-surveillance](../categories/comms-surveillance.md) tool in the **governance** layer. In trust-zone
terms it lives in the **green zone** — a back-office oversight system reading
copies of communications, not an inline control on untrusted input, sensitive
data, or egress. Its lethal-trifecta role is **none** (detective oversight, not a
trifecta-leg control). Its job is regulatory: MAR / market-abuse and MNPI
detection, plus SEC/FINRA/CFTC-style books-and-records and supervision
obligations.

## Deployment & architecture

- **SaaS / cloud**, multi-channel capture. Ingests and normalizes e-comms (and
  voice through an NLP/transcription partnership, e.g. Intelligent Voice) into a
  single data model, then applies analytics and review tooling on top.
- Functions as a capture + archive + surveillance + e-discovery stack rather than
  a bolt-on to someone else's archive.
- API/connector integrations to communication sources; exact channel list and
  SIEM/case-management integrations not fully verified here (see open questions).

## Positioning & differentiators

Shield positions itself as **AI/NLP-native** conduct and communications
surveillance — lexicon/rules *plus* machine-learning models and (per vendor
marketing) an "AmplifAI" suite pitched for "agentic compliance." The claimed edge
is reducing the false-positive noise that plagues legacy lexicon-only surveillance
and unifying capture+analytics in one platform.

How it differs from nearest neighbors:
- [behavox](behavox.md) — also AI-first conduct surveillance; Behavox leans hard on
  behavioral/voice AI and risk scoring. Closest direct competitor.
- [steeleye](steeleye.md) — combines comms surveillance with trade surveillance and
  consolidated record-keeping; broader "RegTech data" framing.
- [nice-actimize](nice-actimize.md) — incumbent enterprise surveillance suite (trade + comms),
  large-bank installed base; heavier, less AI-native-branded.
- [theta-lake](theta-lake.md) — specializes in modern collaboration/UC channels (Zoom, Teams,
  Webex) capture and risk; more channel-coverage focused.
- [relativity-trace](relativity-trace.md) — proactive comms surveillance built on the Relativity
  e-discovery platform; strong e-discovery DNA.

Differentiation claims here are vendor-stated and not independently benchmarked.

## Ownership, funding & M&A

- **Independent, VC-backed.** No acquisition found as of 2026-06-28.
- **Series B: $20M, December 2022**, led by **Macquarie Capital**, with **UBS
  Next**, **Mindset Ventures**, and **OurCrowd** (OurCrowd also backed Series A).
  Confidence: medium (reputable press: TechCrunch, Crowdfund Insider).
- **Series A: $15M, early 2022.** Total **~$35M** raised as of end-2022.
- No funding or ownership change confirmed after 2022-12 in this pass; treat
  funding_total as as-of 2022-12.
- Founders: **Shiran Weitzman** (CEO), **Ofir Shabtai** (CTO), **Eran Noam** (CBO).

## CTO / hedge-fund lens

- **Day-2, but mandatory once you have regulated comms.** A fund with
  registered/regulated staff communicating over monitored channels needs comms
  surveillance to meet MAR (EU/UK), SEC/FINRA books-and-records and supervision,
  and CFTC obligations — including the off-channel / messaging-app enforcement wave
  that has driven recent fines. It's not a launch-day stack item, but it becomes
  non-negotiable as headcount and regulatory footprint grow.
- **Posture/fit: medium.** Shield targets banks and larger regulated enterprises;
  a 50-person fund may find it (and peers like Behavox) heavier/pricier than
  needed and might start with archiving + lighter surveillance. Mid-to-larger
  funds and those under FCA/SEC scrutiny are the better fit.
- **AI-prompt-surveillance angle:** as employees increasingly converse with LLMs
  and AI assistants, comms-surveillance vendors are a candidate home for
  surveilling those interactions. Shield's "agentic compliance" / AmplifAI
  messaging gestures at this, but coverage of AI-chat channels was not verified
  here.
- Not a model-risk (SR 11-7) tool; relevance is conduct/market-abuse compliance,
  not model governance.

## Competitors / alternatives

[behavox](behavox.md) · [steeleye](steeleye.md) · [nice-actimize](nice-actimize.md) · [theta-lake](theta-lake.md) ·
[relativity-trace](relativity-trace.md)

## Open questions / to verify
- Exact channel coverage (which chat/collaboration/AI-assistant channels) and
  whether AI-prompt/LLM-interaction surveillance is a real shipped capability vs
  marketing.
- Any funding or ownership change after 2022-12 (later rounds, acquisition,
  insolvency) — none found, but not exhaustively confirmed.
- Single legal HQ vs distributed Tel Aviv / New York / London footprint; a
  third-party source (Tracxn) lists founding as 2017 vs ~2018 implied by press —
  minor discrepancy, treated as soft.
- Trade-surveillance scope (does it cover trade as well as comms, like SteelEye?).

## Sources
- [About Shield](https://www.shieldfc.com/about-us/) — fetched 2026-06-28 — supports: founders (Weitzman/Shabtai/Noam), positioning, AmplifAI/agentic-compliance; confidence: med (vendor marketing).
- [Shield raises $20M (TechCrunch)](https://techcrunch.com/2022/12/01/shield-a-communication-compliance-platform-for-financial-institutions-raises-20m/) — fetched 2026-06-28 — supports: Series B $20M Dec 2022, investors, ~2018 founding, Tel Aviv + NY HQ, AI/NLP (Intelligent Voice), SEC/financial-crime focus; confidence: high.
- [Regtech Shield Raises $20M Series B (Crowdfund Insider)](https://www.crowdfundinsider.com/2022/12/199370-regtech-shield-raises-20-million-series-b-ourcrowd-joins-round/) — fetched 2026-06-28 — supports: $20M Series B, Macquarie/UBS Next/Mindset/OurCrowd, Israel-based, ~$35M total, AI risk-mitigation; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Shield FC = Israeli/London regtech founded ~2018 by Shiran Weitzman (CEO) / Ofir Shabtai (CTO) / Eran Noam (CBO), HQ Tel Aviv with NY+London offices, SaaS e-comms+voice surveillance with AI/NLP analytics; independent VC-backed, $20M Series B (2022-12, Macquarie Capital lead; UBS Next/Mindset/OurCrowd), ~$35M total. No M&A found. Set ownership_confidence medium, hedge_fund_fit medium, status researched.
