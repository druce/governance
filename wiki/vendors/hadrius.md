---
title: Hadrius
type: vendor
name: Hadrius
slug: hadrius
aka: []
primary_category: comms-surveillance
also_listed_in: [enterprise-grc]
website: https://www.hadrius.com
founded: 2023
hq: New York, NY, USA
ownership_state: independent
owner: null
ownership_note: VC-backed, independent. $27M raised across seed + Series A ($22M Series A led by CRV, announced 2026-07-14). YC Winter 2023. No acquisition found as of 2026-08-18.
acquisition: {announced: null, closed: null, price: null}
funding_total: $27M (seed + Series A)
last_funding: Series A, $22M, announced 2026-07-14 (led by CRV; YC, Pathlight Ventures participating)
market_position: {comms-surveillance: ai-native-disruptor}
deployment_model: [saas]
form_factor: [platform, api]
data_leaves_tenancy: 'true'
integrations: [Claude Enterprise (Claude Compliance API), ChatGPT, email, chat, SMS, social media]
mcp_support: unverified
certifications: [ISO 27001 (vendor-stated), AICPA SOC (vendor-stated), GDPR (vendor-stated)]
pricing_model: null
fs_traction: claimed
target_customer: SEC/FINRA-regulated US firms — RIAs, broker-dealers, private funds, and compliance consultants; one-person RIAs up to 100,000+ employee institutions
last_verified: 2026-08-18
verify_after: 2027-02-18
tags: [comms-surveillance, regtech, sec, finra, 17a-4, recordkeeping, ai-chat-archiving, marketing-review, personal-trading, yc]
---

# Hadrius

**One-liner** — An AI-native compliance platform for SEC/FINRA-regulated US firms that
bundles comms supervision, marketing review, personal-trading oversight and testing into
one system of record — and is one of the few vendors that archives employees'
**ChatGPT and Claude conversations** as a supervised books-and-records channel.

## What it does

Hadrius sells "agentic compliance infrastructure" to registered advisers and
broker-dealers, pitched as a replacement for the stack of legacy point tools a
compliance team otherwise runs. Six modules (vendor's framing, 2026-08-18):

- **Communications** — supervision of email, chat, social media and **AI-assistant
  conversations**, with 17(a)-4 / WORM retention and what the vendor calls
  "zero-data-retention AI" review.
- **Marketing** — AI-assisted review and approval workflow for advertising and
  marketing material (SEC Marketing Rule territory).
- **People Oversight** — personal trading, attestations, certifications.
- **Account Surveillance** — employee and firm trades checked against restricted lists
  and blackout windows.
- **Testing Program** — automated compliance testing with audit-ready reporting.
- **Compliance-manual implementation** and branch-location oversight.

Multi-tenant workspaces let **compliance consultants** run many client firms from one
console — a real channel in the RIA market, where much of the compliance function is
outsourced.

### The part that matters for an AI stack

On **2026-07-28** Hadrius added **Claude** to its communications archive, built on
**Anthropic's Claude Compliance API**; **ChatGPT** capture was already supported. Firms
on **Claude Enterprise** can archive employees' AI conversations alongside email and
chat, with the same surveillance applied. Capture is **agentless** — nothing installed
on employee devices, no change to how employees use the assistant — and runs on Hadrius
infrastructure. Hadrius is named on Anthropic's own Compliance API partner list, so this
is corroborated, not just vendor copy.

This closes the gap flagged elsewhere in this wiki: most comms-surveillance incumbents
apply AI *to* the archive (LLM alert triage) but do not treat the AI assistant itself as
a **channel**. The regulatory logic is simple and hard to argue with — SEC recordkeeping
attaches to any channel where employees conduct business, and an adviser working through
a client question with Claude is conducting business.

## Where it sits in the stack

- Primary category: [comms-surveillance](../categories/comms-surveillance.md) (governance layer);
  also relevant to [enterprise-grc](../categories/enterprise-grc.md).
- **Detective control**, not preventive. It records and reviews after the fact; it does
  not block a prompt or an egress. If you want an employee stopped from pasting the
  position book into a chatbot, that is [dlp](../categories/dlp.md) /
  [ai-access-governance](../categories/ai-access-governance.md), not this.
- **Scope-boundary note:** the category page draws a line between capture/archival
  (Smarsh, Global Relay, Purview) and surveillance/analysis. Hadrius deliberately does
  **both** — it is the archive *and* the supervision layer. That is the pitch for small
  firms and a limitation for firms with an entrenched archive they will not move.

## Positioning & differentiators

- vs [behavox](behavox.md), [shield](shield.md), [nice-actimize](nice-actimize.md) —
  those are enterprise conduct/market-abuse surveillance engines aimed at banks and
  large asset managers, usually layered on a separate archive. Hadrius is aimed **down
  market** at the US registered-adviser/BD compliance program as a whole, and covers
  non-surveillance chores (attestations, marketing review, testing) those tools do not.
- vs [steeleye](steeleye.md) — SteelEye couples comms with **trade surveillance** under
  MAR for EU/UK-facing firms. Hadrius is US-rule-shaped (SEC/FINRA, 17a-4, Marketing
  Rule) and its trading angle is **personal/employee** account surveillance, not market-
  abuse modeling on the firm's order flow.
- vs [greenboard](greenboard.md) — the closest comparable: same YC lineage, same buyer,
  overlapping module map. The clearest split today is **AI-assistant capture**, which
  Hadrius ships and Greenboard does not list. Hadrius is also roughly 3x the headcount
  (80 vs 26 per YC, 2026-08-18) and better capitalized ($27M vs $20M).
- vs [theta-lake](theta-lake.md) — Theta Lake specializes in modern collaboration
  (video, voice, UC) capture and risk detection; deeper on those channels, far narrower
  as a compliance program.

## Who should choose them / anti-fit

**Good fit:** a US RIA, broker-dealer or private fund — anywhere from a few people to a
few thousand — that wants one platform for the whole compliance program instead of an
archive plus a surveillance tool plus a marketing-review inbox plus a spreadsheet of
attestations. Sharpest fit if you have **deployed an enterprise AI assistant and need a
recordkeeping answer for it**, which is a live and under-served problem.

**Anti-fit:** EU/UK firms whose obligation is MAR-shaped; firms needing genuine
**trade/market-abuse surveillance** on firm order flow; tier-1 institutions with an
incumbent Smarsh/Global Relay archive and a NICE Actimize-class surveillance stack they
are not replacing; anyone requiring self-hosted or in-tenant deployment.

## Known weaknesses / gotchas

- **Young and unproven at scale.** Founded 2023. Impressive customer count, but the
  reference base for hedge-fund-scale complexity is thin; ask for references at your
  size and strategy.
- **Efficacy numbers are marketing.** "99% reduction in false positives," "70% less
  manual review," "20 hours a week saved" are all vendor/customer-reported with no
  defined denominator. The $3T AUM figure is a sum across the client base, not a measure
  of depth.
- **Consolidation cuts both ways.** One platform for archive + supervision + testing
  means one vendor's outage, one vendor's retention posture, and a painful exit if you
  later need to migrate a 17a-4 archive out.
- **AI-assistant capture requires Claude Enterprise.** The Compliance API is not
  available on lower Claude tiers, so the marquee capability has a licence prerequisite
  on the model-vendor side.
- **Certifications are vendor-stated** (ISO 27001, SOC) and were not independently
  verified here — ask for the reports.

## Deployment & data handling

Multi-tenant **SaaS**; data leaves your tenancy by design — that is what an archive is.
Capture for AI assistants is **agentless** and API-based (Claude Compliance API), running
on Hadrius infrastructure. The vendor markets **"zero-data-retention AI"** for the review
layer, which should mean model providers do not retain content passed for analysis —
**get this in writing**, distinguishing (a) retention by the LLM provider, (b) retention
by Hadrius, and (c) any use of customer content for model training. None of the three is
spelled out in public sources.

## Integrations & partnerships

Email, chat, SMS, social media; **ChatGPT** and **Claude Enterprise** conversation
capture via Anthropic's Compliance API. Named customers include **BBVA, Altruist,
Allworth Financial, World Investment Advisors, M1 Finance** (vendor). MCP support:
unverified.

## Compliance & FS traction

Purpose-built for **SEC/FINRA** obligations: 17(a)-4/WORM recordkeeping, supervision,
Marketing Rule review, personal-trading and code-of-ethics oversight, exam-ready
evidence. Vendor claims **500+ financial institutions** and compliance managed across
**"$3T+ AUM"**; `fs_traction: claimed` — named logos are real, the aggregate stats are
self-reported.

## Commercial

Not disclosed. No public pricing; expect per-seat or per-firm annual subscription with
module-based tiering, as is standard in this segment.

## Competitors / alternatives

[greenboard](greenboard.md) · [behavox](behavox.md) · [steeleye](steeleye.md) ·
[shield](shield.md) · [theta-lake](theta-lake.md) · [nice-actimize](nice-actimize.md) ·
[relativity-trace](relativity-trace.md)

## Open questions / to verify

- **Data handling specifics** — retention periods, sub-processor list, whether customer
  content (including archived AI conversations) is ever used for model training, and
  what "zero-data-retention AI" contractually means.
- **Which ChatGPT tier** the existing OpenAI capture requires, and by what mechanism
  (compliance API vs admin export) — the Claude path is documented, the ChatGPT one is
  a bare vendor claim.
- Whether Copilot / Gemini / other assistants are on the roadmap as capture channels.
- Independent confirmation of ISO 27001 and SOC 2 reports.
- Pricing bands, and whether the consultant multi-tenant edition is priced differently.
- Post-Series A cap table and board composition.

## Sources

- [Hadrius — Announcing our $22 Million Series A](https://www.hadrius.com/insights/series-a) — fetched 2026-08-18 — supports: $27M seed+A / $22M Series A, CRV lead, YC + Pathlight, 2026-07-14, founders, NYC HQ, 500+ firms, named customers; confidence: high for funding, low for efficacy stats (vendor).
- [Hadrius — homepage / product modules](https://www.hadrius.com/) — fetched 2026-08-18 — supports: six-module map, 17(a)-4/WORM, zero-data-retention AI claim, consultant workspaces, vendor-stated ISO 27001 / SOC / GDPR; confidence: med (vendor marketing).
- [Hadrius Adds Claude to Its Communications Archive — PRNewswire](https://www.prnewswire.com/news-releases/hadrius-adds-claude-to-its-communications-archive-bringing-enterprise-ai-under-compliance-oversight-302835563.html) — fetched 2026-08-18 — supports: 2026-07-28 Claude integration, agentless capture, Claude Enterprise requirement, prior ChatGPT support, Stewart quote; confidence: high (vendor PR, corroborated below).
- [Anthropic — Claude Compliance API integrations](https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations) — fetched 2026-08-18 — supports: Hadrius named as a Compliance API partner; Enterprise vs Platform access tiers; independent corroboration of the integration; confidence: high (primary, the API's own vendor).
- [Hadrius — Y Combinator company profile](https://www.ycombinator.com/companies/hadrius) — fetched 2026-08-18 — supports: YC W23, founded 2023, NYC, team size 80, founder backgrounds, $3T AUM claim; confidence: high for identity facts, low for the AUM claim.
- Cached: `raw/sources/2026-08-18--hadrius--funding-and-yc-profile.md`, `raw/sources/2026-08-18--hadrius--claude-compliance-api-archive.md`.

## History

- [2026-08-18] Page created and researched in one pass (survey-v2.csv row → wiki-create + wiki-research). Established: founded 2023, NYC, YC W23, independent, $27M raised ($22M Series A led by CRV, 2026-07-14), six-module SEC/FINRA compliance platform. Key finding: archives ChatGPT and Claude Enterprise conversations as a supervised recordkeeping channel via Anthropic's Compliance API (2026-07-28), corroborated by Anthropic's partner list — the AI-channel-capture gap flagged on [steeleye](steeleye.md). Efficacy and AUM stats recorded as vendor claims, not facts.
