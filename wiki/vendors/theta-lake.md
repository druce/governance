---
type: vendor
name: Theta Lake
slug: theta-lake
categories: [comms-surveillance]
layer: governance
aliases: []
website: https://thetalake.com
founded: 2017
hq: Santa Barbara, California, USA
ownership: independent
ownership_detail: "Private, VC-backed. $50M Series B led by Battery Ventures (2022-03-23); strategic investors include Cisco, Salesforce Ventures, Zoom, RingCentral Ventures, Lightspeed, Neotribe, Wells Fargo. No Series C disclosed as of 2026-06-28."
ownership_confidence: high
funding_total: "~$71M (over $70M as of Series B, 2022)"
last_funding: "Series B, $50M, 2022-03-23 (Battery Ventures)"
deployment: [saas, api]
target_customer: enterprise / regulated (financial services, banks, asset managers)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-28
tags: [comms-surveillance, dcga, collaboration, archiving, ai-surveillance]
---

# Theta Lake

**One-liner** — A compliance-surveillance and archiving platform purpose-built for
modern collaboration tools (Zoom, Teams, Webex, Slack, RingCentral) that captures
and supervises video, voice, chat — and increasingly the output of AI meeting
assistants like Zoom AI Companion and Microsoft Copilot.

**Categories** — [[comms-surveillance]]

## What it does

Theta Lake addresses a gap that legacy email/IM archiving and surveillance vendors
were slow to fill: the explosion of regulated communication happening inside
unified-communications and collaboration (UCC) platforms. It does two jobs that
often come from separate vendors:

1. **Capture & archive** — it ingests and retains the full richness of modern
   channels: meeting video and screen-share, voice/audio, chat, reactions,
   whiteboards, files, and AI-generated artifacts (meeting summaries, transcripts).
   It can act as the system of record itself or feed an existing archive.
2. **Surveillance / supervision** — it runs ML/NLP risk detection over that
   captured content to flag potential regulatory, conduct, privacy, and security
   issues, with review/escalation workflows for compliance teams. The company
   self-describes the combined category as **Digital Communications Governance and
   Archiving (DCGA)** and holds an early patent for risk detection in *video*
   communications.

## Where it sits in the stack

This is a **governance-layer**, **detective** control on the [[comms-surveillance]]
slot. Like other surveillance tools it is **"none" on the lethal trifecta** — it
does not block untrusted input, sensitive data, or egress in real time; it captures
records after the fact and detects problems for human review. It lives in the
**green zone** (records of internal/employee communications), supporting MAR/MNPI
and conduct supervision.

Note its breadth: unlike pure-analytics surveillance peers that only score data fed
to them by a separate archive, Theta Lake **spans both capture/archival and
surveillance** of collaboration channels. That makes it as much an archiving choice
as a surveillance choice — relevant when comparing against capture/archive-first
incumbents (Smarsh, Global Relay) as well as analytics-first players.

## Deployment & architecture

- **SaaS**, cloud-/AI-native. Connects via certified API integrations rather than
  inline interception.
- **Channel coverage**: Zoom (incl. Zoom AI Companion), Microsoft Teams, Webex by
  Cisco, RingCentral, Slack, Microsoft Exchange/email, Salesforce, Symphony, plus
  collaboration/workflow tools (Asana, Box, Mural, Movius and others).
- **AI-assistant capture** is the current differentiator: partnerships to capture
  and supervise the output of **Zoom AI Companion** and **Microsoft 365 Copilot**
  (summaries, prompts/responses) so that AI-generated content is archived and
  surveilled like any other regulated communication.
- Can **feed existing archives/eDiscovery** or serve as the archive of record;
  integrates with downstream review and SIEM/security tooling.

## Positioning & differentiators

- **Modern-collaboration and AI-assistant specialist.** Built from 2017 for video/
  voice/chat collaboration, not retrofitted from email archiving. Deep, certified
  partnerships with the platform vendors themselves (Cisco, Zoom, RingCentral,
  Salesforce are both investors and integration partners).
- Differs from **markets-/trade-surveillance-first** vendors — [[behavox]],
  [[steeleye]], [[nice-actimize]], [[shield]] — which lead with trade + comms
  analytics aimed at market-abuse detection. Theta Lake leads with rich
  collaboration capture and conduct/AI surveillance, and is typically a complement
  to (not a replacement for) a markets-surveillance system.
- Differs from **eDiscovery/investigations** tooling like [[relativity-trace]],
  which focuses on review/legal hold over captured comms.

## Ownership, funding & M&A

- **Independent, private, VC-backed.** Founded **2017**, HQ **Santa Barbara, CA**
  (office in New York). Co-founders include **Devin Redmond** (CEO) and **Rich
  Sutton** (CTO); Crunchbase/Tracxn also list **Anthony J. Cresci** as co-founder.
- **$50M Series B** led by **Battery Ventures**, announced **2022-03-23**, with
  Lightspeed, Neotribe, Cisco Investments, RingCentral Ventures, Salesforce
  Ventures and Zoom participating; **total raised over $70M** to date.
- **No Series C** or acquisition disclosed as of **2026-06-28**. Named a Visionary
  in the **2025 Gartner Magic Quadrant for DCGA** (vendor-cited; confirm placement
  before relying on it). Ownership confidence: **high**.

## CTO / hedge-fund lens

- **Day-2.** This is supervision/archiving infrastructure, not a launch-blocking
  control. You reach for it once you have regulated communications flowing through
  collaboration tools that your existing email-era archiver doesn't cover well.
- **Most relevant if your firm runs Zoom and/or Teams for client and deal
  conversations and is adopting AI meeting assistants / Copilot.** Capturing and
  supervising those AI-generated summaries/transcripts is exactly Theta Lake's edge,
  and is an emerging MAR/MNPI and recordkeeping exposure most legacy tools miss.
- For a regulated US fund this maps to **SEC/FINRA recordkeeping and off-channel
  communications** concerns and to **MAR**-style conduct surveillance — but as a
  detective control, not model-risk (SR 11-7) tooling.
- **Complements rather than replaces** a markets/trade-surveillance tool. Expect to
  run it alongside, or to consolidate comms capture here while keeping trade
  surveillance elsewhere. Smaller funds may find full DCGA heavier than they need;
  fit is **medium** and scales with collaboration-tool and AI-assistant adoption.

## Competitors / alternatives

- Surveillance / analytics: [[behavox]], [[steeleye]], [[nice-actimize]],
  [[shield]]
- eDiscovery / comms review: [[relativity-trace]]
- Capture/archive incumbents (email-era, now extending to collaboration): Smarsh,
  Global Relay (no page yet)

## Open questions / to verify

- Confirm exact founding date and full co-founder list (Redmond / Sutton / Cresci)
  and any prior Actiance/Smarsh background — not verified from a primary source.
- Confirm whether any round closed after the 2022 Series B (Series C / extension).
- Verify the 2025 Gartner DCGA "Visionary" placement against Gartner, not vendor
  marketing.
- Clarify which functions are system-of-record archive vs. archive-feeding, for
  buyers who already have an archive.

## Sources
- [Theta Lake Attracts $50 Million in Series B Funding](https://thetalake.com/theta-lake-series-b-funding/) — fetched 2026-06-28 — supports: $50M Series B, 2022-03-23, Battery Ventures lead, investor roster, >$70M total, HQ Santa Barbara, video/voice/chat capture + patent; confidence: high (vendor primary)
- [Theta Lake — About](https://thetalake.com/about/) — fetched 2026-06-28 — supports: founding/leadership, DCGA positioning, channel coverage, Zoom AI Companion + Microsoft Copilot surveillance, venture ownership, 2025 Gartner DCGA Visionary; confidence: high (vendor primary)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founding 2017, HQ Santa Barbara CA, founders Devin Redmond (CEO) / Rich Sutton (CTO) (Cresci also listed), independent VC-backed with $50M Series B (Battery Ventures, 2022) and >$70M total / no disclosed Series C, SaaS DCGA platform spanning capture+archive+surveillance for Zoom/Teams/Webex/Slack/RingCentral with Zoom AI Companion + Microsoft Copilot AI-assistant surveillance as key differentiator. Cached 2 primary sources. No M&A; ownership confidence raised to high.
