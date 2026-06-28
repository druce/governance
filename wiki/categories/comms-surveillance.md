---
type: category
name: Comms Surveillance
slug: comms-surveillance
layer: governance
priority: day-2
trifecta_role: none-detection
maps_to_seed_doc: Comms Surveillance
maps_to_seed_csv: (in AI Governance, Model Risk)
vendor_count: 6
status: drafted
last_updated: 2026-06-28
---

## Business objective

The compliance detective. Communications surveillance replays the firm's archived
communications — now increasingly including **AI prompts and responses** alongside
email, chat, voice, and trading-room messaging — hunting for market abuse, MNPI
(material non-public information) leakage, collusion, and improper chatter. It exists
to satisfy market-conduct rules (the EU/UK **Market Abuse Regulation (MAR)**, SEC/FINRA
and CFTC supervision obligations in the US) that require regulated firms to surveil
employee communications for insider dealing and market manipulation. The tooling
applies lexicons, behavioral models, and increasingly LLM-based analysis to a captured
archive and surfaces alerts for compliance review.

Note the division of labor: **capture/archival** (Smarsh, Global Relay, Microsoft
Purview) preserves the communications; **surveillance** (this category) analyzes that
archive. The seed lists surveillance vendors; the capture vendors are upstream
infrastructure.

## When you need it

Labeled **Day-2** in the generic stack — but for a **hedge fund or asset manager this
is hedge-fund-critical and effectively non-negotiable** wherever the firm is subject
to MAR or US market-conduct supervision. If you trade, you almost certainly already run
e-comms capture and a surveillance tool; the AI-era task is to ensure **AI assistant
prompts and outputs are captured into the same archive and swept by the same
surveillance**. A research analyst pasting MNPI into a chatbot, or an LLM summarizing a
deal that surfaces inside information, is exactly the leakage these systems exist to
catch — and a new, under-monitored channel. For a CTO, the Day-1-in-spirit action is to
confirm AI channels are in scope for capture and surveillance even if the broader
governance buildout is Day-2.

## Lethal-trifecta role

**None-detection / detective control.** Surveillance is after-the-fact: it does not sit
inline and does not prevent a leak in real time, so it breaks no leg of the lethal
trifecta directly. It is the **green-zone** detective backstop that catches MNPI /
sensitive-data leakage *after* it has hit a comms channel — complementary to the
preventive controls in [dlp](dlp.md) and [ai-access-governance](ai-access-governance.md) that try to stop the leak
before it happens.

## Vendors

- [behavox](../vendors/behavox.md) — AI-led conduct and market-abuse surveillance; behavioral/voice analytics, lexicon-plus-ML.
- [steeleye](../vendors/steeleye.md) — combined trade + comms surveillance with integrated recordkeeping; strong MAR framing.
- [nice-actimize](../vendors/nice-actimize.md) — incumbent financial-crime/markets surveillance suite (also AML/fraud); enterprise-heavy.
- [theta-lake](../vendors/theta-lake.md) — surveillance and compliance for modern collaboration channels (Zoom, Teams, Webex) and AI features.
- [shield](../vendors/shield.md) — communications compliance/surveillance platform with an AI/LLM analytics emphasis.
- [relativity-trace](../vendors/relativity-trace.md) — proactive comms surveillance built on the Relativity (e-discovery) platform.

## Consolidation / M&A dynamics

A specialized RegTech market serving regulated financial firms, split between
markets-surveillance incumbents (NICE Actimize), AI-native challengers (Behavox,
Shield, SteelEye), collaboration-channel specialists (Theta Lake), and e-discovery
crossovers (Relativity Trace). No specific seed M&A flags for these vendors. The live
dynamic is every vendor racing to (a) ingest AI assistant prompts/outputs and modern
collaboration channels, and (b) replace brittle lexicons with LLM-based intent
detection.

## Adjacent categories

- [dlp](dlp.md) — preventive control that tries to stop MNPI/sensitive data leaving before surveillance would catch it.
- [ai-access-governance](ai-access-governance.md) — governs/records what employees send to AI tools; a capture point for the surveillance archive.
- [ai-governance-platform](ai-governance-platform.md) — the broader model-risk/governance register; the CSV folds surveillance under it.
- [enterprise-grc](enterprise-grc.md) — where surveillance alerts and conduct findings are tracked as risk/audit items.

## Survey

**Question.** Which communications surveillance platform does your firm use for
market-abuse / conduct monitoring (and is it sweeping AI assistant prompts and
responses)?

**Answer options.** Behavox; SteelEye; NICE Actimize; Theta Lake; Shield; Relativity
Trace; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** This question only applies to firms under market-conduct
supervision (MAR / SEC / FINRA / CFTC) — consider a gating question first. Do **not**
confuse surveillance with capture/archival (Smarsh, Global Relay, Purview); if
respondents name those, they answered the wrong question — add a note or a separate
capture question. NICE Actimize skews to large enterprises and doubles as
AML/financial-crime, which may inflate its selection for reasons unrelated to comms.
The high-signal AI-era follow-up: "are AI assistant prompts/outputs in scope for
capture and surveillance?"

## Open taxonomy questions

- Capture/archival (Smarsh, Global Relay, Purview) vs surveillance/analytics (this
  page) — should capture be its own thin category? Currently treated as upstream infra.
- The CSV folds this under "AI Governance, Model Risk & Compliance"; kept separate here
  because the buyer (compliance/surveillance) and vendors are distinct from
  [ai-governance-platform](ai-governance-platform.md).
