---
type: vendor
name: Relativity Trace
slug: relativity-trace
categories: [comms-surveillance]
layer: governance
aliases: ["Trace", "kCura", "Relativity"]
website: "https://www.relativity.com/data-breach-response/communication-surveillance/"
founded: 2018                        # Trace product launched 2018-11-06; parent kCura/Relativity founded 2001 (Chicago)
hq: Chicago, IL
ownership: subsidiary               # product of Relativity (privately held; Silver Lake-backed)
ownership_detail: "Product of Relativity (formerly kCura), a private company. Silver Lake made a strategic growth investment (2021-03-18) at a reported ~$3.6B valuation, becoming largest shareholder with a significant minority stake; ICONIQ Growth remains an investor; founder Andrew Sieja remains a shareholder."
ownership_confidence: high
funding_total:                       # Relativity not separately broken out; ICONIQ $125M (2015), Silver Lake strategic growth investment (2021)
last_funding: "Silver Lake strategic growth investment, 2021-03 (amount undisclosed; ~$3.6B valuation per WSJ)"
deployment: [saas]
target_customer: regulated (banking, investment management, financial services, pharma); enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [comms-surveillance, ecomms, market-abuse, mnpi, ediscovery, ai-detection]
---

# Relativity Trace

> Proactive communications-surveillance application built on the Relativity e-discovery platform: ingests e-comms, applies machine learning plus policy/lexicon rules, and flags market abuse, MNPI leakage, collusion and other misconduct for compliance review.

**One-liner** — A proactive e-comms surveillance product from the e-discovery vendor Relativity, leaning on the same review/search/ML stack lawyers use for litigation to catch market abuse and MNPI risk before it becomes an enforcement problem.

**Categories** — [comms-surveillance](../categories/comms-surveillance.md)

## What it does

Relativity Trace monitors employee electronic communications in (near) real time and surfaces the highest-risk messages to compliance officers for review. It ingests communication data across channels — email, chat/Slack, text and short-message data, voice/audio, and other configured sources — and applies a combination of customizable policies, lexicons and machine-learning models to flag content suggesting insider trading, collusion, improper investment-management practices, bribery, market manipulation and similar regulatory misconduct. The emphasis is **proactive** surveillance (catch-it-before-it-escalates) rather than the reactive, post-incident document review that Relativity's core e-discovery product is built for. Trace also adds AI-powered data-cleansing/normalization to make noisy short-message data reviewable.

## Where it sits in the stack

Trace lives in the [comms-surveillance](../categories/comms-surveillance.md) category at the **governance** layer. It is a **detective** control — it does not sit inline in any AI request path, so its lethal-trifecta relevance is **none** (it neither breaks untrusted-input, sensitive-data, nor egress legs; it observes after the fact). In trust-zone terms it operates in the **green zone**, reviewing communications data that has already been captured and archived.

Its distinguishing trait is **e-discovery heritage**: Trace is an application on the Relativity platform, so the same indexing, search, analytics, ML and document-review workflows that power litigation discovery are repurposed for ongoing surveillance. For a firm that already runs Relativity/RelativityOne for legal hold and e-discovery, surveillance and investigation share one data substrate and one review UI — an alert in Trace can flow into the same review/escalation tooling used for litigation.

## Deployment & architecture

- **Delivery:** SaaS, primarily on **RelativityOne**, Relativity's cloud platform (Azure-hosted). Trace is an app layered on the Relativity data-management engine.
- **Data ingestion:** connectors/feeds for e-comms channels (email, chat/collaboration, short messages/SMS, voice/audio transcription, and other configured sources); supports out-of-the-box surveillance policies plus custom rules and lexicons.
- **Detection:** policy/lexicon rules combined with machine learning and search; AI-based data cleansing to reduce noise in short-message data before review.
- **Workflow:** alerting to compliance officers, review queues, escalation — leveraging Relativity's review tooling.
- **Delivered via partners:** managed-service and implementation offerings exist through Deloitte, FTI Consulting, and Complete Discovery Source (CDS), in addition to direct.

## Positioning & differentiators

Trace's pitch is "surveillance from the people who do discovery." Versus the **markets-first** surveillance incumbents — [behavox](behavox.md), [steeleye](steeleye.md), [nice-actimize](nice-actimize.md), [shield](shield.md) — which were built specifically around trade/e-comms surveillance and market-abuse models, Trace comes at the problem from the litigation/review side and emphasizes platform consolidation with e-discovery and investigations. Versus **collaboration-first** entrants like [theta-lake](theta-lake.md) (deep on Zoom/Teams/Slack capture and modern collaboration risk), Trace is more channel-broad and review-workflow-centric. The strongest case for Trace is shared infrastructure: one platform for e-discovery, legal hold, investigations and surveillance, rather than a standalone surveillance silo.

Worth noting the inverse: a buyer who does *not* already use Relativity gets less of the consolidation benefit and is comparing Trace head-to-head with purpose-built surveillance vendors on detection quality, market-abuse model depth and channel coverage.

## Ownership, funding & M&A

Trace is a **product of Relativity** (the e-discovery company formerly known as **kCura**, founded by **Andrew Sieja** and headquartered in **Chicago**; kCura founding year commonly cited as 2001 — not re-verified against a primary filing here). Relativity is **privately held**. On **2021-03-18** Relativity announced a **strategic growth investment from Silver Lake**; per WSJ reporting (corroborated by LawSites and Built In Chicago) the deal valued Relativity at **~$3.6 billion** and made **Silver Lake the largest shareholder with a significant minority stake**, with Silver Lake representatives joining the board and management unchanged. Prior investor **ICONIQ Growth** (which put in $125M in 2015) remained an investor, and founder Andrew Sieja remained a shareholder. The investment explicitly earmarked funds to grow RelativityOne and the Trace surveillance platform. No separate funding total is broken out for Trace itself.

> Note: Silver Lake's stake is characterized in reporting as a *significant minority* (largest shareholder), not a confirmed majority. The ownership label here is "subsidiary" to reflect that Trace is a Relativity product, not an independent company; the parent's cap table is PE-anchored but not a confirmed buyout.

## CTO / hedge-fund lens

Comms surveillance is a **Day-2** capability for most funds but becomes **critical** for any regulated shop subject to **market-abuse / recordkeeping regimes** — EU/UK MAR, SEC/FINRA, and CFTC — where firms are expected to monitor employee e-comms for MNPI handling, insider trading and manipulation. Trace is most attractive when **the firm already uses Relativity/RelativityOne** for e-discovery or legal hold: surveillance then rides existing infrastructure, contracts and review skills, and investigations share a platform. The AI/ML detection angle helps with the volume and noise of modern multi-channel comms. For a smaller fund with no Relativity footprint, evaluate it against purpose-built surveillance vendors on detection efficacy, market-abuse model coverage, collaboration-channel depth and total cost — the consolidation argument is weaker without the e-discovery anchor. As a detective control it carries no inline-availability risk, but it depends entirely on complete upstream **capture/archiving** of all in-scope channels.

## Competitors / alternatives

- [behavox](behavox.md) — markets-first behavioral/e-comms surveillance with ML risk models.
- [steeleye](steeleye.md) — surveillance + recordkeeping/trade reconstruction, MAR-focused.
- [nice-actimize](nice-actimize.md) — incumbent financial-crime/surveillance suite.
- [shield](shield.md) — e-comms compliance/surveillance platform.
- [theta-lake](theta-lake.md) — collaboration-first capture & compliance (Zoom/Teams/Slack).

## Open questions / to verify

- kCura/Relativity founding year (2001 is widely cited; not verified here against a primary filing).
- Exact Silver Lake stake size and whether the position has changed since 2021; whether any subsequent control transaction has occurred.
- Channel coverage and market-abuse model depth relative to [behavox](behavox.md)/[steeleye](steeleye.md) (independent benchmarks, not vendor claims).
- Pricing model and whether Trace is sold standalone vs. bundled with RelativityOne.
- Voice/audio surveillance maturity (native vs. partner transcription).

## Sources

- [Relativity Announces the Release of Relativity Trace — proactive risk management & compliance](https://www.relativity.com/news-events/relativity-announces-the-release-of-relativity-trace-a-new-app-for-proactive-risk-management-and-compliance/) — fetched 2026-06-28 — supports: Trace launched 2018-11-06, app built on Relativity platform, proactive monitoring; confidence: high (primary/vendor).
- [Relativity Announces Strategic Investment from Silver Lake (PRNewswire / Relativity newsroom)](https://www.prnewswire.com/news-releases/relativity-announces-strategic-investment-from-silver-lake-301250508.html) — fetched 2026-06-28 — supports: 2021-03-18 Silver Lake strategic growth investment, funds earmarked for RelativityOne + Trace, Andrew Sieja founder, ICONIQ prior investor; confidence: high (primary/vendor).
- [Investment In Relativity Puts the E-Discovery Company's Valuation At Reported $3.6 Billion (LawSites)](https://www.lawnext.com/2021/03/investment-in-relativity-puts-the-e-discovery-companys-valuation-at-reported-3-6-billion.html) — fetched 2026-06-28 — supports: ~$3.6B valuation, Silver Lake largest shareholder / significant minority stake, board seats, Chicago, kCura→Relativity, ICONIQ $125M 2015; confidence: med (reputable trade press citing WSJ).
- [Relativity Reaches $3.6B Valuation After Recent Investment From Silver Lake (Built In Chicago)](https://www.builtinchicago.org/articles/relativity-silver-lake-funding-3b-valuation) — fetched 2026-06-28 — supports: $3.6B valuation, Chicago HQ corroboration, use of funds toward Trace; confidence: med (trade press).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; refined ownership (Relativity, Silver Lake-backed strategic growth investment 2021-03, ~$3.6B valuation, significant minority, largest shareholder; ownership_confidence low→high). Added full body: Trace = proactive e-comms surveillance on RelativityOne (SaaS), launched 2018; e-discovery heritage as key differentiator; detective control, trifecta=none; positioned vs [behavox](behavox.md)/[steeleye](steeleye.md)/[nice-actimize](nice-actimize.md)/[shield](shield.md)/[theta-lake](theta-lake.md); hedge_fund_fit unclear→medium. Cached 2 source files (4 cited sources). status stub→researched, confidence low→medium.
