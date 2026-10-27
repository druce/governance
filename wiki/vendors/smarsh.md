---
title: Smarsh
type: vendor
name: Smarsh
slug: smarsh
aka: [Smarsh Capture, Smarsh Enterprise Archive, Smarsh Professional Archive, Smarsh Surveillance, Smarsh Intelligent Agent, Digital Reasoning, Actiance, TeleMessage, CallCabinet]
primary_category: comms-surveillance
also_listed_in: []
website: https://www.smarsh.com
founded: 2001
hq: Portland, Oregon, USA
ownership_state: pe-owned
owner: K1 Investment Management
ownership_note: "PE-owned. K1 Investment Management is the controlling sponsor. K1 announced it would combine Actiance and Smarsh on 2017-11-15; a secondary commentary dates K1's original Smarsh buyout to January 2016. A reported 2025 secondary sale of K1's stake (Evercore-run, HarbourVest named) has no primary confirmation. Ares provides debt. The Silver Lake investment in the brief could not be found (searched 2026-10-26)."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {comms-surveillance: leader}
deployment_model: [saas]
form_factor: [platform, api]
data_leaves_tenancy: "true"
integrations: [microsoft-365-copilot, microsoft-teams, chatgpt-enterprise-compliance-api, claude-compliance-api, zoom, slack, whatsapp, signal, bloomberg, aws-bedrock, aws-marketplace]
mcp_support: server
certifications: []
pricing_model: "Quote-based subscription, per user / per channel. No public list price."
fs_traction: claimed
target_customer: regulated enterprises (broker-dealers, RIAs, banks, insurers, asset managers, government), from small advisers to Tier-1 banks
last_verified: 2026-10-26
verify_after: null
tags: [comms-archiving, dcga, sec-17a-4, finra-4511, ai-capture, copilot-capture, claude-compliance-api, chatgpt-compliance-api, conduct-surveillance, pe-owned, telemessage]
sources:
  - {claim: "Digital Reasoning acquisition announced 2020-11-10; terms undisclosed; close expected within 60 days", url: "https://www.smarsh.com/press-release/smarsh-acquires-digital-reasoning", date: 2020-11-10, confidence: high}
  - {claim: "K1 combines Actiance and Smarsh", url: "https://k1.com/k1-combines-actiance-and-smarsh-to-create-global-compliance-and-enterprise-information-archiving-leader/", date: 2017-11-15, confidence: medium}
  - {claim: "Founding 2001, Portland HQ, K1 parent, acquisition list", url: "https://en.wikipedia.org/wiki/Smarsh", date: 2026-10-26, confidence: medium}
  - {claim: "TeleMessage acquired Feb 2024; CallCabinet Feb 2025", url: "https://www.cfodive.com/news/smarsh-cfo-strategic-growth-opportunities-fintech-mergersacquisitions/742596/", date: 2025-03-14, confidence: high}
  - {claim: "Smarsh Capture for Microsoft 365 Copilot; Intelligent Agent surveillance; 6,500+ customers", url: "https://www.smarsh.com/press-release/smarsh-unveils-major-platform-innovations-next-gen-ai-robust-apis-for-smarter-financial-oversight", date: 2025-06-04, confidence: medium}
  - {claim: "Claude Compliance API integration into Smarsh Capture; supervision", url: "https://www.smarsh.com/press-release/smarsh-introduces-new-anthropic-integration-to-capture-and-govern-claude-enterprise-data-within-its-platform", date: 2026-05-21, confidence: high}
  - {claim: "AWS collaboration; 77% review-workload reduction claim; K1 as customer", url: "https://fintech.global/2026/06/29/how-smarsh-is-making-enterprise-ai-compliance-ready/", date: 2026-06-29, confidence: low}
  - {claim: "OpenAI + Anthropic compliance API launch partner; MCP server; agents", url: "https://siliconangle.com/2026/10/22/smarsh-edge-2026-governance-anchors-communications-intelligence-smarshedge/", date: 2026-10-22, confidence: medium}
  - {claim: "TeleMessage breach, service suspension, CISA KEV entries", url: "https://www.theregister.com/2025/07/02/cisa_telemessage_patch/", date: 2025-07-02, confidence: high}
---

# Smarsh

> Primary category: [comms-surveillance](../categories/comms-surveillance.md).

**One-liner**: The largest US communications archiving vendor. Smarsh captures and archives email, chat, voice, mobile messaging and now **AI-assistant conversations** (Microsoft 365 Copilot, ChatGPT Enterprise, Claude Enterprise) as SEC 17a-4 / FINRA books-and-records, and sells an AI-driven **surveillance** layer on top. For many funds it is already the system of record that any surveillance tool reads from.

**What it does**: Three layers, sold separately or together:
- **Capture.** Connectors for 100+ channels (vendor figure): email, Teams, Zoom, Slack, Bloomberg, mobile SMS, WhatsApp and Signal (through TeleMessage), and recorded voice (through CallCabinet, acquired February 2025).
- **Archive.** WORM-style retention for books-and-records, with search, legal hold and eDiscovery. Two tiers: **Professional Archive** for small and mid-sized advisers and broker-dealers, and **Enterprise Archive** (the former Actiance and Micro Focus Digital Safe estates) for large banks.
- **Surveillance.** Lexicon-plus-ML supervision, upgraded with the NLP from **Digital Reasoning** (whose models powered conduct surveillance at several Tier-1 banks at the time of the 2020 deal). The newest layer is the **Smarsh Intelligent Agent**, available from late 2025 and built on AWS Bedrock. Smarsh claims it cut review volume by about 77% at "a leading global investment bank" with under 2% loss in risk detection; this is a vendor claim with an unnamed customer. A **Noise Reduction Agent** for smaller firms claims up to 60% fewer alerts.

**AI-assistant capture** is where Smarsh matters for this wiki. All of the following are vendor claims:
- **Microsoft 365 Copilot** capture was announced 2025-06-04. It covers prompts, files and responses across web, Teams, Microsoft 365 apps and Copilot chat agents. A trade write-up says it uses Microsoft's Interaction Export APIs.
- **ChatGPT** is captured through OpenAI's Compliance API, listed on Smarsh's channel pages.
- **Claude Enterprise** capture through Anthropic's Claude Compliance API was announced 2026-05-21. It covers text, files, Claude-generated artifacts, deleted messages and archived conversations, fed into "capture, supervision, and analytics." Smarsh says it is one of the first certified partners. Anthropic's own partner list (see [anthropic-claude-enterprise](anthropic-claude-enterprise.md)) also names Smarsh.
- At its EDGE 2026 conference (October 2026), Smarsh described itself as a launch partner for both the OpenAI and Anthropic compliance APIs. It said it treats agent-to-agent traffic as a channel to capture, and that it had shipped an **MCP server** and several agents in six months.

**Naming / provenance**: Founded in **2001** in Brooklyn by Stephen Marsh ("S. Marsh"). HQ moved to Portland, Oregon in 2004. CEO Kim Crawford Goodman since 2020 (per Wikipedia; not checked against Smarsh's leadership page). Most of its product lines came from acquisitions, which explains the many product names:

| Year | Acquired | What it brought |
|---|---|---|
| 2017–18 | Actiance (combined by K1) | enterprise archive and collaboration capture |
| 2020 | Digital Reasoning | AI/NLP conduct surveillance |
| 2020–21 | Entreda, Privva | cyber and vendor-risk compliance |
| 2021–22 | Digital Safe (from Micro Focus) | large-bank archive |
| 2024-02 | TeleMessage | mobile, WhatsApp and Signal capture |
| 2025-02 | CallCabinet | cloud compliance call recording |

Digital Reasoning was **announced 2020-11-10**, terms undisclosed, with close "expected in the next 60 days". **No close announcement was found**, though Smarsh has sold the technology as its own since then.

**Ownership & viability**: `pe-owned`. **K1 Investment Management** is the controlling sponsor.
- K1 announced it would combine Actiance (which K1 had acquired) with Smarsh on **2017-11-15**. A secondary commentary and Dealroom date K1's original Smarsh buyout to **January 2016** ($215M); that date is not confirmed from a primary source.
- Kirkland & Ellis's 2020 release calls Smarsh a K1 portfolio company. Ares Management provides debt.
- A 2025 commentary describes a **secondary sale of K1's stake**, run by Evercore with HarbourVest among the buyers. No primary confirmation was found; treat it as unverified.
- **Silver Lake:** the brief mentioned a Silver Lake investment. Standard and extended searches on 2026-10-26 found **no evidence** of one, so the page does not assert it.
- Viability is strong: decades of revenue, 6,500+ customers (vendor), a growing AI product line, and a multi-year AWS strategic collaboration (from October 2025). The usual PE caveats apply: expect pricing pressure at renewal, more acquisitions, and an eventual sponsor-to-sponsor sale or IPO. Odd detail: K1 is also a named Smarsh *customer* in its own case study.

**Positioning & differentiators**: `leader` in comms-surveillance. It is the largest capture/archive incumbent, and its Digital Reasoning-derived surveillance runs at Tier-1 banks (Smarsh claims "18 of the top 20" North American, European and Asian banks as clients).
- **Vs. [global-relay](global-relay.md):** the closest peer. Both are archive-first and both now capture Copilot, ChatGPT and Claude. Smarsh has the deeper surveillance pedigree (Digital Reasoning, since 2020) and broader voice and mobile capture through acquisitions. Global Relay is founder-owned, runs its own data centre and has a single, home-grown codebase.
- **Vs. analytics-first surveillance** ([behavox](behavox.md), [shield](shield.md), [steeleye](steeleye.md), [nice-actimize](nice-actimize.md)): those tools often *read from* a Smarsh archive. Smarsh now competes with them for the analytics layer too. Large banks still frequently pair a Smarsh archive with another vendor's surveillance.
- **Vs. [theta-lake](theta-lake.md):** Theta Lake is stronger on rich capture from video and collaboration tools. Smarsh is broader across email, mobile, voice and legacy channels.
- **Vs. down-market platforms** ([hadrius](hadrius.md), [greenboard](greenboard.md), [aca-group](aca-group.md)): for a small RIA, Smarsh Professional Archive is the incumbent these newer platforms are trying to displace.

**Who should choose them / anti-fit**: Fits a fund that needs a **defensible 17a-4 / FINRA 4511 archive across many channels**, wants AI-assistant conversations in the *same* archive and review queue as email and chat, and prefers one vendor for capture and first-line surveillance. Also fits a fund already on Smarsh that wants to add Copilot or Claude capture without a new vendor. **Anti-fit:** firms wanting best-of-breed market-abuse analytics joined to trade data, where a trade-plus-comms platform fits better. Also small advisers who want archiving bundled with marketing review and attestations, where the newer AI-native platforms are lighter. And anyone who needs the archive inside their own cloud tenancy.

**Known weaknesses / gotchas**:
- **TeleMessage breach (May 2025).** TeleMessage, Smarsh's mobile-archiving unit, was breached after its modified Signal client (TM SGNL) was seen in use by US officials. Smarsh suspended all TeleMessage services. Chat data from 60+ government users was published, and CISA added three TeleMessage CVEs to its Known Exploited Vulnerabilities list (May–July 2025). Other Smarsh products stayed online. **Ask any Smarsh mobile-capture prospect** what replaced it and how the TeleMessage code base was remediated.
- **Product sprawl from acquisitions.** Professional vs. Enterprise archives, legacy Actiance and Digital Safe estates, and separate surveillance and capture SKUs. Expect migrations and inconsistent features across tiers.
- **Surveillance claims are vendor case studies.** The 77% and 60% reductions come from unnamed or affiliated customers.
- **Capture ≠ supervision.** Capturing Copilot, ChatGPT or Claude conversations does not by itself mean your lexicons and models are tuned for prompt-style text. Test with real AI transcripts.
- **Ownership chatter.** Sponsor-to-sponsor activity and an unverified Silver Lake rumour; recheck ownership at renewal.

**Deployment & data handling**: SaaS. Captured communications, including AI prompts and responses pulled through the vendors' compliance APIs, are **copied into Smarsh's cloud archive** (`data_leaves_tenancy: "true"`). That is the point of a third-party 17a-4 archive. The newer AI surveillance runs on AWS (Bedrock / AgentCore); data-residency and model-hosting detail by region was not verified. Capture is **out-of-band**, pulled through APIs after the fact, so it adds no latency and cannot block anything.

**Integrations & partnerships**: Microsoft (Copilot, Teams), OpenAI and Anthropic compliance APIs, Zoom, Slack, Bloomberg, mobile carriers and WhatsApp/Signal, AWS (strategic collaboration agreement; sold through AWS Marketplace). An **MCP server** was announced at EDGE 2026 (vendor; scope not documented); recorded as `mcp_support: server`, low confidence.

**Compliance & FS traction**: The core market is FS. Smarsh claims 6,500+ customers and 18 of the top 20 global banks (vendor figures; no named hedge-fund customers found). Certifications were not verified for this page; check the trust portal. Hedge-fund fit: **high for archive and capture**, where it is likely already present at many funds. Fit is **medium for surveillance**, depending on whether you also need trade surveillance.

**Commercial**: Quote-based. Typically priced per user per channel for capture and archive, with surveillance as an add-on. No public pricing.

## Open questions

- Digital Reasoning **close date**: announced 2020-11-10 and expected within 60 days; no close announcement found.
- K1 entry date (2016 buyout vs. 2017 Actiance combination) and whether the reported 2025 secondary closed and who holds what now.
- **Silver Lake**: no evidence found of any Silver Lake investment in Smarsh. Ask the brief's author for the source.
- Current certifications (SOC 2 Type II, ISO 27001) and data-residency options for AI surveillance on AWS.
- Whether Smarsh's ChatGPT capture covers ChatGPT Enterprise, Edu and Team, and whether Copilot Studio agents are in scope.
- TeleMessage remediation status and current product name for mobile capture.
- CEO as of 2026-10 (Wikipedia says Kim Crawford Goodman; not checked against a primary source).

## Sources

- [Smarsh acquires Digital Reasoning (Smarsh)](https://www.smarsh.com/press-release/smarsh-acquires-digital-reasoning), fetched 2026-10-26. Supports: 2020-11-10 announcement, undisclosed terms, close expected in 60 days, Tier-1 bank surveillance. Confidence: high.
- [K1 Combines Actiance and Smarsh (K1)](https://k1.com/k1-combines-actiance-and-smarsh-to-create-global-compliance-and-enterprise-information-archiving-leader/) and [TechCrunch 2017-11-15](https://techcrunch.com/2017/11/15/two-compliance-companies-are-merging-to-build-a-firm-that-could-generate-100m-in-revenue/), search snapshots 2026-10-26. Supports: K1 combination of Actiance and Smarsh. Confidence: medium.
- [Smarsh, Wikipedia](https://en.wikipedia.org/wiki/Smarsh), fetched 2026-10-26. Supports: founding, HQ, K1 parent, acquisition list. Confidence: medium.
- [Smarsh CFO (CFO Dive, 2025-03-14)](https://www.cfodive.com/news/smarsh-cfo-strategic-growth-opportunities-fintech-mergersacquisitions/742596/), fetched 2026-10-26. Supports: TeleMessage (2024-02) and CallCabinet (2025-02) acquisitions. Confidence: high.
- [Smarsh platform innovations (Smarsh, 2025-06-04)](https://www.smarsh.com/press-release/smarsh-unveils-major-platform-innovations-next-gen-ai-robust-apis-for-smarter-financial-oversight), fetched 2026-10-26. Supports: Copilot capture, Intelligent Agent, product menu, 6,500+ customers. Confidence: medium (vendor).
- [Smarsh Anthropic integration (Smarsh, 2026-05-21)](https://www.smarsh.com/press-release/smarsh-introduces-new-anthropic-integration-to-capture-and-govern-claude-enterprise-data-within-its-platform), fetched 2026-10-26. Supports: Claude Compliance API capture and supervision. Confidence: high (vendor primary).
- [How Smarsh is making enterprise AI compliance-ready (FinTech Global, 2026-06-29)](https://fintech.global/2026/06/29/how-smarsh-is-making-enterprise-ai-compliance-ready/), fetched 2026-10-26. Supports: AWS collaboration, agent claims, K1 as customer. Confidence: low (vendor-sourced).
- [Smarsh EDGE 2026 (SiliconANGLE, 2026-10-22)](https://siliconangle.com/2026/10/22/smarsh-edge-2026-governance-anchors-communications-intelligence-smarshedge/), fetched 2026-10-26. Supports: OpenAI and Anthropic launch partner, MCP server, agents. Confidence: medium (paid media partner).
- [CISA TeleMessage KEV (The Register, 2025-07-02)](https://www.theregister.com/2025/07/02/cisa_telemessage_patch/), search snapshot 2026-10-26. Supports: TeleMessage breach, suspension, KEV entries. Confidence: high.
- Cached: `raw/sources/2026-10-26--smarsh--ownership-ma-ai-capture.md`

## History

- [2026-10-26] Page created and researched in one pass. Primary comms-surveillance, chosen over a "capture/archive is upstream" framing: Smarsh sells surveillance (Digital Reasoning lineage, Intelligent Agent) and is the main capture point for Copilot, ChatGPT and Claude conversations. Established K1 PE ownership (Actiance combination 2017-11-15), the Digital Reasoning announcement (2020-11-10, close unconfirmed), the TeleMessage 2025 breach, and AI-assistant capture claims. A Silver Lake investment could not be verified and is not asserted.
