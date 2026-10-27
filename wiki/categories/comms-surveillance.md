---
title: Comms Surveillance
type: category
name: Comms Surveillance
slug: comms-surveillance
category: comms-surveillance
layer: governance
survey_question: Comms Surveillance
adoption_tier: firm-type-specific
trigger: registered advisers / regulated comms (MAR/MNPI) — hedge-fund-critical
maturity_stage_required: null
category_maturity: mature
adjacent: [dlp, anti-deepfake]
incumbent_coverage: []
vendor_count: 11
maps_to_seed_doc: Comms Surveillance
maps_to_seed_csv: (in AI Governance, Model Risk)
last_verified: 2026-08-18
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

Note the division of labor, and where it blurs: **capture/archival** preserves
communications as 17a-4/FINRA books-and-records, and **surveillance** analyzes that
archive for market abuse and conduct risk. The two archive incumbents,
[smarsh](../vendors/smarsh.md) and [global-relay](../vendors/global-relay.md), now sell
their own AI surveillance on top and are the main capture points for Copilot, ChatGPT and
Claude conversations, so they are listed here (since 2026-10-26). Analytics-first tools
(Behavox, Shield, SteelEye, NICE Actimize) often read from their archives rather than
replacing them. Microsoft Purview remains capture/retention infrastructure, not
surveillance.

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

## Security role

**Detective, out-of-band.** Surveillance is after-the-fact: it does not sit inline and
does not prevent a leak in real time. It is the **green-zone** detective backstop that
catches MNPI / sensitive-data leakage *after* it has hit a comms channel —
complementary to the preventive controls in [dlp](dlp.md) and [ai-access-governance](ai-access-governance.md) that
try to stop the leak before it happens.

## Vendors

- [behavox](../vendors/behavox.md) — AI-led conduct and market-abuse surveillance; behavioral/voice analytics, lexicon-plus-ML.
- [steeleye](../vendors/steeleye.md) — combined trade + comms surveillance with integrated recordkeeping; strong MAR framing.
- [nice-actimize](../vendors/nice-actimize.md) — incumbent financial-crime/markets surveillance suite (also AML/fraud); enterprise-heavy.
- [theta-lake](../vendors/theta-lake.md) — surveillance and compliance for modern collaboration channels (Zoom, Teams, Webex) and AI features.
- [shield](../vendors/shield.md) — communications compliance/surveillance platform with an AI/LLM analytics emphasis.
- [relativity-trace](../vendors/relativity-trace.md) — proactive comms surveillance built on the Relativity (e-discovery) platform.
- [hadrius](../vendors/hadrius.md) — AI-native SEC/FINRA compliance platform (archive + supervision + marketing review); archives **ChatGPT and Claude Enterprise conversations** as a recordkeeping channel.
- [greenboard](../vendors/greenboard.md) — AI-native SEC/FINRA compliance platform unifying 17a-4 archiving/supervision with marketing review and attestations; Instant Bloomberg among its channels.
- [aca-group](../vendors/aca-group.md) — Compliance consultancy to much of the alternatives industry that also sells ComplianceAlpha — e-comms capture, 17a-4 archive and surveillance bundled with personal-trading and trade surveillance; the default surveillance vendor for funds already using ACA advisory. No documented capture of AI-assistant conversations (2026-10). Cross-listed to [enterprise-grc](enterprise-grc.md). (added 2026-10-23)
- [smarsh](../vendors/smarsh.md) — largest US comms archive (17a-4/FINRA) with AI surveillance from its Digital Reasoning acquisition (announced 2020-11-10); captures M365 Copilot, ChatGPT and Claude Enterprise conversations. PE-owned (K1). Its TeleMessage mobile-archiving unit was breached in May 2025. (added 2026-10-26)
- [global-relay](../vendors/global-relay.md) — founder-owned archive common at hedge funds (17a-4/FINRA), with an LLM-based surveillance module since 2024-11; connectors capture ChatGPT Enterprise, Microsoft Copilot and Claude conversations. (added 2026-10-26)

## Consolidation / M&A dynamics

A specialized RegTech market serving regulated financial firms, split between
markets-surveillance incumbents (NICE Actimize), AI-native challengers (Behavox,
Shield, SteelEye), collaboration-channel specialists (Theta Lake), e-discovery
crossovers (Relativity Trace), and — new as of 2026 — **YC-lineage full-program
platforms aimed down-market at US registered advisers and broker-dealers**
(Hadrius, Greenboard), which bundle the archive itself with supervision, marketing
review and attestations rather than selling surveillance alone. No specific seed M&A flags for these vendors. The live
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
Trace; Hadrius; Greenboard; ACA Group (ComplianceAlpha); Smarsh; Global Relay; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** This question only applies to firms under market-conduct
supervision (MAR / SEC / FINRA / CFTC) — consider a gating question first. Smarsh and
Global Relay are options since 2026-10-26 because both now sell surveillance, but many
respondents will tick them for the **archive** alone — consider a separate capture
question, or ask whether their surveillance module is licensed. Purview is still
capture, not surveillance. NICE Actimize skews to large enterprises and doubles as
AML/financial-crime, which may inflate its selection for reasons unrelated to comms.
The high-signal AI-era follow-up: "are AI assistant prompts/outputs in scope for
capture and surveillance?" As of 2026-10-26 **Hadrius**, **Smarsh** and **Global Relay**
document capture of employee ChatGPT/Claude conversations (Smarsh and Global Relay also
Microsoft Copilot), so that follow-up discriminates between vendors rather than merely
measuring intent. Hadrius and Greenboard are also **program platforms, not pure
surveillance tools** — small-RIA respondents may name them for archiving or attestations
rather than market-abuse monitoring; interpret their selections with that in mind.

## Open taxonomy questions

- Capture/archival vs surveillance/analytics (this page) — should capture be its own
  thin category? Since 2026-10-26 Smarsh and Global Relay are listed here because they
  sell surveillance too; Purview stays out as capture-only infrastructure.
- The CSV folds this under "AI Governance, Model Risk & Compliance"; kept separate here
  because the buyer (compliance/surveillance) and vendors are distinct from
  [ai-governance-platform](ai-governance-platform.md).
