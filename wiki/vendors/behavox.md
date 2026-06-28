---
type: vendor
name: Behavox
slug: behavox
categories: [comms-surveillance]
layer: governance
aliases: [Behavox Quantum, Behavox LLM]
website: https://www.behavox.com/
founded: 2014
hq: London, UK (major hubs in Montreal, New York, Belfast)
ownership: independent
ownership_detail: "VC/PE-backed independent. SoftBank Vision Fund 2 invested $100M (2020-02-24); HPS Investment Partners (part of BlackRock) made a $175M preferred-equity investment (2026-06-22). Other investors: Citigroup, Index Ventures, Hoxton Ventures. No acquisition."
ownership_confidence: high
funding_total: ~$296M equity (per aggregators); $100M SoftBank (2020) + $175M HPS/BlackRock (2026) confirmed via primary/press
last_funding: "$175M preferred equity from HPS Investment Partners (BlackRock), 2026-06-22"
deployment: [saas, on-prem]
target_customer: enterprise / regulated — global banks, asset managers, hedge funds, commodity trading firms
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [comms-surveillance, market-abuse, mar, mnpi, conduct-risk, voice-surveillance, regtech]
---

# Behavox

> AI-native communications-surveillance and conduct-risk platform for regulated financial firms — ingests e-comms and voice, and uses a finance-specific LLM to flag market abuse, MNPI leakage, and misconduct.

**One-liner** — Behavox is a compliance-surveillance vendor that scans a firm's e-comms and voice traffic with its own purpose-built financial-services LLM to surface market abuse, conduct risk, and insider/MNPI signals.

**Categories** — [comms-surveillance](../categories/comms-surveillance.md)

## What it does

Behavox sits on top of a firm's captured communications (email, chat, messaging, and transcribed voice) and runs surveillance models to generate alerts on potential **market abuse** (insider dealing, spoofing/manipulation), **MNPI / information-barrier breaches**, financial crime, conflicts of interest, anti-competitive conduct, and general misconduct. Its flagship is the **Behavox Quantum** surveillance platform, powered by a proprietary, finance-tuned **Behavox LLM** (marketed as "LLM 2.0"). The pitch is that a domain-specific model produces fewer false positives and better multilingual coverage than lexicon/keyword surveillance or generalist models, at low compute cost. **Behavox Voice** adds transcription across 15+ languages so voice/turret traffic can be surveilled alongside text. Behavox has also extended into regulatory archiving and, in 2025, trade surveillance (product "Polaris," covering the major asset classes) — moving it from a pure comms-surveillance point tool toward a broader "controls platform."

The job for a buyer: meet regulatory obligations to monitor employee communications for abuse and conduct, with materially less analyst time spent triaging noise.

## Where it sits in the stack

Primary category: [comms-surveillance](../categories/comms-surveillance.md), in the **governance** layer. This is a **detective control** — it observes and alerts on activity after the fact; it does not block prompts, redact data, or gate egress. In lethal-trifecta terms it breaks **no leg directly** (`trifecta_relevance: none`); it is a **green-zone detective backstop** that helps you *discover* that something bad (MNPI in a chat, collusion on a call) already happened. It complements, rather than replaces, preventive controls like DLP, information barriers, and AI runtime guardrails.

## Deployment & architecture

- **Deployment:** SaaS (cloud) with on-premises options; SOC 2 Type 2 certified (vendor claim). SSO/SAML/Active Directory for auth.
- **Data ingestion / integrations:** pulls communications and content from sources such as SharePoint, Google Drive, Box, and OneDrive (per vendor). In practice comms-surveillance tools sit downstream of capture/archival systems (e.g. Smarsh, Global Relay, Microsoft Purview) — Behavox positions its own archiving as part of the ecosystem, but interoperates with existing capture estates.
- **Models:** proprietary Behavox LLM run in-house; vendor markets "zero third-party LLM dependencies" and "no training on user data."

## Positioning & differentiators

Behavox's distinguishing bet is a **vendor-owned, finance-specific LLM** rather than rules/lexicons or wrapping a third-party foundation model — claiming better precision, multilingual voice+text alerting, and low per-day compute cost. It is known for an AI-first, "controls platform" ambition spanning surveillance, archiving, and (newer) trade surveillance.

Versus nearest neighbors:
- [steeleye](steeleye.md) — combines comms surveillance with trade surveillance and record-keeping in one data layer; strong on holistic/trade-comms correlation.
- [nice-actimize](nice-actimize.md) — incumbent, broad financial-crime and surveillance suite; deep in large banks.
- [theta-lake](theta-lake.md) — specialist in modern collaboration channels (Zoom, Teams, voice/video) capture + compliance.
- [shield](shield.md) — AI-centric comms surveillance, a direct philosophical competitor on ML-driven detection.
- [relativity-trace](relativity-trace.md) — surveillance built on the Relativity e-discovery/data platform.

Behavox overlaps most with [shield](shield.md) and [steeleye](steeleye.md) on the "AI-driven surveillance" message; its differentiator claim is the proprietary in-house LLM and voice multilingual coverage. (All capability claims here are vendor marketing and not independently benchmarked.)

## Ownership, funding & M&A

- **Independent**, VC/PE-backed. Founded **2014**; HQ **London**, with a large hub in **Montreal** and offices in New York, Belfast, Seattle, Tokyo, Singapore.
- **SoftBank Vision Fund 2** invested **$100M** on **2020-02-24** (confirmed, vendor press release).
- **HPS Investment Partners** (part of **BlackRock**) made a **$175M preferred-equity** investment on **2026-06-22**; Behavox concurrently repaid/retired a $70M Hercules Capital venture-debt facility (press announcement).
- Other named investors: **Citigroup, Index Ventures, Hoxton Ventures**. Aggregators (Crunchbase) cite ~$296M total raised — treat the aggregate as medium confidence; the two rounds above are well-sourced.
- Company states it has been **profitable since 2023** and grown ~7x since 2020 (vendor claim).
- **No acquisition** — Behavox is the buyer's counterparty directly; HPS/BlackRock holds a minority preferred stake, not control. `ownership_confidence: high` for "independent."

## CTO / hedge-fund lens

Comms surveillance is broadly **Day-2** infrastructure, but for a **regulated** trading shop it can be effectively mandatory: firms subject to **MAR** (EU/UK Market Abuse Regulation), **SEC/FINRA** supervision, or **CFTC** rules are expected to monitor employee communications for market abuse and MNPI handling. A hedge fund's actual need depends on registration and footprint:
- **Large or multi-jurisdiction managers** (especially UK/EU MAR-scoped, or those that have had off-channel-comms ("WhatsApp") enforcement exposure) are the natural fit — Behavox markets relationships with several of the largest hedge-fund managers.
- **Small US-only funds** often satisfy obligations more cheaply via their archival vendor's built-in surveillance (e.g. Smarsh/Global Relay) rather than a heavyweight standalone platform; Behavox is likely overkill until headcount, channels, and regulatory scope grow.

**AI-prompt surveillance angle:** as employees adopt genAI chat, those interactions become another communications channel a surveillance program may need to capture and review (e.g. MNPI pasted into a chatbot). Behavox's value proposition — an LLM that reads natural-language conversations for risk — is conceptually adjacent, but I did **not** find an explicit, documented Behavox product feature that surveils employee genAI *prompts/responses* (e.g. ChatGPT/Copilot) as of 2026-06-28. Treat "AI-prompt surveillance" as a plausible roadmap adjacency, not a confirmed capability (see Open questions). For preventive controls on AI prompts/egress, that is the runtime-security/DLP layer, not Behavox.

No specific **SR 11-7 / model-risk** tie-in for the *buyer* beyond the general point that Behavox's own surveillance LLM is itself a model a firm would need to validate/govern if relied upon for regulatory monitoring.

## Competitors / alternatives

[steeleye](steeleye.md) · [nice-actimize](nice-actimize.md) · [theta-lake](theta-lake.md) · [shield](shield.md) · [relativity-trace](relativity-trace.md)

## Open questions / to verify

- Total funding figure (~$296M) is from aggregators, not a primary filing — confirm if precision matters.
- Whether Behavox has a **named, shipping feature** that surveils employee generative-AI prompts/responses (vs. surveilling conventional e-comms channels) — not confirmed as of 2026-06-28.
- Exact interop with third-party capture/archival estates (Smarsh, Global Relay, Purview) — vendor lists cloud content sources but capture-vendor integrations weren't enumerated in sources reviewed.
- Founders/CEO and the precise London-vs-Montreal HQ designation (company page labels London "HQ"; Montreal is the largest operational hub) — minor.

## Sources
- [Behavox Announces $100 Million Investment From SoftBank Vision Fund 2](https://www.behavox.com/news/behavox-announces-100-million-investment-from-softbank-vision-fund-2/) — fetched 2026-06-28 — supports: SoftBank Vision Fund 2 $100M on 2020-02-24; comms-data platform positioning; confidence: high (primary, vendor release)
- [Behavox Raises $175 Million from HPS Investment Partners, Part of BlackRock](https://financialit.net/news/fundraising-news/behavox-raises-175-million-hps-investment-partners-part-blackrock-accelerate) — fetched 2026-06-28 — supports: $175M preferred equity 2026-06-22, still independent, prior investors, profitable since 2023, $70M Hercules debt retired, Polaris trade surveillance; confidence: high (press announcement)
- [Behavox AI / Behavox LLM product page](https://www.behavox.com/behavox-ai/) — fetched 2026-06-28 — supports: Quantum + Behavox LLM 2.0, market-abuse/financial-crime alerting, voice+text 15 languages, SaaS/on-prem, integrations, SOC 2; confidence: medium (vendor marketing)
- [Behavox — Our Company](https://www.behavox.com/our-company/) — fetched 2026-06-28 — supports: London HQ + office footprint incl. Montreal, product ecosystem, traction claims; confidence: medium (vendor marketing). Founding year 2014 / founders corroborated via Crunchbase/PitchBook search results (aggregator, medium confidence).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Behavox = independent, VC/PE-backed comms-surveillance vendor (Quantum + proprietary Behavox LLM) for MAR/SEC/FINRA market-abuse + MNPI/conduct detection across e-comms and voice. Confirmed SoftBank $100M (2020) and HPS/BlackRock $175M preferred equity (2026-06-22) — no acquisition, ownership_confidence raised to high. Set founded 2014, London HQ, SaaS/on-prem, hedge_fund_fit medium, status researched. AI-prompt/response surveillance noted as unconfirmed adjacency, not a documented feature.
