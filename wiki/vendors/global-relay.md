---
title: Global Relay
type: vendor
name: Global Relay
slug: global-relay
aka: [Global Relay Archive, Global Relay Message, Global Relay Surveillance, Global Relay AI Surveillance, Global Relay Communications Inc.]
primary_category: comms-surveillance
also_listed_in: []
website: https://www.globalrelay.com
founded: 1999
hq: Vancouver, British Columbia, Canada
ownership_state: independent
owner: null
ownership_note: "Private, founder- and employee-controlled. Founded 1999 by Warren Roy (CEO), Duff Reid and Eric Parusel. Wikipedia says it has taken no outside or venture funding. No investment in or acquisition of Global Relay found as of 2026-10-26."
acquisition: {announced: null, closed: null, price: null}
funding_total: "none disclosed (no outside/venture funding per Wikipedia)"
last_funding: null
market_position: {comms-surveillance: platform-module}
deployment_model: [saas]
form_factor: [platform, api]
data_leaves_tenancy: "true"
integrations: [microsoft-365-copilot, chatgpt-enterprise-compliance-api, claude-compliance-api, microsoft-teams, exchange-online, bloomberg, whatsapp]
mcp_support: unverified
certifications: [soc2-type2, iso27001]
pricing_model: "Quote-based subscription, per user / per connector. No public list price."
fs_traction: claimed
target_customer: regulated financial firms, from small hedge funds and RIAs to global banks
last_verified: 2026-10-26
verify_after: null
tags: [comms-archiving, dcga, sec-17a-4, finra-4511, mifid-ii, ai-capture, copilot-capture, claude-compliance-api, chatgpt-compliance-api, ai-surveillance, founder-owned, hedge-funds]
sources:
  - {claim: "Founded 1999 by Roy/Reid/Parusel; Vancouver; private, employee-controlled, no outside funding; 22 of 25 largest banks, 61% of US hedge funds (press-cited)", url: "https://en.wikipedia.org/wiki/Global_Relay", date: 2026-10-26, confidence: medium}
  - {claim: "ChatGPT Enterprise connector via OpenAI Compliance API; supervision; 17a-4/4511/MiFID II", url: "https://www.globalrelay.com/connector/global-relay-connector-for-chatgpt-enterprise/", date: 2026-10-26, confidence: high}
  - {claim: "Microsoft Copilot connector: prompts, responses, metadata via official Copilot APIs", url: "https://www.globalrelay.com/connector/microsoft-copilot/", date: 2026-10-26, confidence: high}
  - {claim: "Claude connector via Claude Compliance API; AI-enabled supervision/surveillance; WORM", url: "https://www.globalrelay.com/connector/claude/", date: 2026-10-26, confidence: high}
  - {claim: "AI-enabled surveillance launched 2024-11 (five-layer design)", url: "https://www.businesswire.com/news/home/20241112420017/en/Global-Relay-Announces-Next-Gen-AI-Enabled-Communications-Surveillance", date: 2024-11-12, confidence: medium}
  - {claim: "Enhanced AI Surveillance at FINRA 2026; LLM classification with chain-of-thought pre-alert", url: "https://www.globalrelay.com/?p=54606", date: 2026-05-11, confidence: medium}
  - {claim: "Gartner DCGA Magic Quadrant Leader (vendor claim)", url: "https://www.businesswire.com/news/home/20251027851036/en", date: 2025-10-27, confidence: low}
---

# Global Relay

> Primary category: [comms-surveillance](../categories/comms-surveillance.md).

**One-liner**: A founder-owned Canadian archiving vendor that is one of the default **17a-4 / FINRA books-and-records archives at hedge funds**. It captures email, chat, voice, mobile and now **Microsoft Copilot, ChatGPT Enterprise and Claude** conversations, and since late 2024 sells an **LLM-based surveillance** layer over the same archive.

**What it does**:
- **Capture.** Connectors for email, Teams, Bloomberg, mobile and WhatsApp, voice, websites and more, plus an Open Connector API for custom sources.
- **Archive.** Hosted in Global Relay's own data centres, with optional WORM storage, search, legal hold and eDiscovery.
- **Message.** Its own compliant instant-messaging and collaboration app, used by some funds as a recorded alternative to consumer chat.
- **Surveillance.**
  - Launched in **November 2024** as "AI-enabled communications surveillance": five layers covering data standardisation, transcription and translation, noise reduction, risk identification and alert management.
  - Upgraded at FINRA 2025 to review whole conversations in context.
  - Repositioned at FINRA 2026 (release dated 2026-05-11). Global Relay says an LLM classifies messages, reasoning step by step **before** an alert is raised. It contrasts this with competitors that add an explanation after the alert; that comparison is a vendor claim with no data.
  - A separate **Voice Surveillance** product and an internal **AI Assistant** sit alongside. Global Relay claims 50+ languages for audio and text.

**AI-assistant capture** (all vendor claims, checked against connector pages on 2026-10-26):
- **ChatGPT Enterprise**, through OpenAI's Compliance API. Announced **July 2024**, among the earliest such integrations. Captures conversations, attachments, uploaded and generated media, and history subject to workspace retention.
- **Microsoft Copilot.** Captures all Copilot prompts and responses (text, files, audio) with user and timestamp metadata across Teams, Outlook, Word, Excel, SharePoint, BizChat and web chat, using "official Copilot APIs". Undated page. Copilot Studio and agents are not mentioned.
- **Claude**, through Anthropic's **Claude Compliance API**. Covers chats, files, prompts including images, **incognito chats**, projects, and Claude-generated artifacts, edits and deletions. Records feed Global Relay's "AI-enabled supervision, surveillance, and analytics" with optional WORM storage. The page is undated. This resolves an open question on [anthropic-claude-enterprise](anthropic-claude-enterprise.md), which had flagged Global Relay's Claude support as unconfirmed.
- No Gemini connector was seen.

**Naming / provenance**: Founded **1999** in Vancouver by **Warren Roy** (CEO), **Duff Reid** and **Eric Parusel**. Wikipedia's infobox gives 2000-06-02, a minor inconsistency. Offices in New York, Chicago, London, Singapore, Raleigh and Halifax. Products have been home-built rather than acquired, apart from a 2008 mobile-software purchase. "Global Relay" is also the legal name (Global Relay Communications Inc.).

**Ownership & viability**: `independent`. Private and **founder- and employee-controlled**. Wikipedia says it has taken **no outside or venture funding**. No investment, sale process or acquisition was found as of 2026-10-26.
- **Viability:** a 25-year-old profitable-by-necessity business (no venture funding) with a large regulated client base and its own infrastructure. Low near-term risk.
- **Acquisition-risk note:** as a founder-controlled company, a sale would be a founder decision. Plausible buyers are PE roll-ups in DCGA or a market-data or exchange group. A change of control would most likely bring re-pricing rather than a shutdown, since the archive is the asset.

**Positioning & differentiators**: `platform-module` in comms-surveillance. It is a leading archive (Global Relay claims Leader in Gartner's 2025 Digital Communications Governance and Archiving Magic Quadrant, a vendor claim), but its surveillance is a 2024-vintage module sold to existing archive customers rather than a standalone category leader.
- **Vs. [smarsh](smarsh.md):** the closest peer. Both archive-first, both now capture Copilot, ChatGPT and Claude.
  - Global Relay: **founder-owned with no sponsor**, so less renewal-pricing churn; runs its own data centres; home-grown, single platform.
  - Smarsh: PE-owned and built by acquisition, with a deeper and older surveillance stack (Digital Reasoning) and Tier-1 bank references.
- **Vs. analytics-first surveillance** ([behavox](behavox.md), [shield](shield.md), [steeleye](steeleye.md), [nice-actimize](nice-actimize.md)): Global Relay is frequently the archive these tools ingest from. Its own surveillance is the "good enough, same vendor" option.
- **Vs. [theta-lake](theta-lake.md):** Theta Lake is richer on video and collaboration capture; Global Relay is broader on legacy and FS channels, plus its own messaging app.

**Who should choose them / anti-fit**: Fits a **hedge fund or RIA that wants one stable vendor for the books-and-records archive across email, chat, mobile and AI assistants**, with workable surveillance in the same console and no PE-driven renewal surprises. This is especially true if the fund already uses Global Relay, which Wikipedia (citing press) says ~61% of US hedge funds do; that figure is dated and vendor-originated. **Anti-fit:** firms that need sophisticated market-abuse analytics correlated with trade data, or a proven Tier-1-scale behavioural surveillance engine. They should pair the archive with a specialist. Also anti-fit: anyone needing the archive inside their own cloud tenancy.

**Known weaknesses / gotchas**:
- **Surveillance is young.** It launched November 2024. Proof points beyond conference demos and vendor releases were not found, so pilot it on your own data.
- **Where the LLM runs is undocumented** in the pages reviewed. The FINRA 2026 release mentions a "best-in-class LLM" without naming the model, host or whether customer data reaches a third-party model provider. Ask before letting it score MNPI-laden content.
- **AI connector pages are undated.** The Claude and Copilot connectors' launch dates and general-availability status were not found; confirm availability and which plans (Enterprise vs. Team) are covered.
- **Capture ≠ supervision.** Archiving AI chats does not mean your lexicons and models handle prompt-style text well.

**Deployment & data handling**: SaaS, hosted in Global Relay's **own data centres** ("private cloud archive"). Captured communications and AI prompts and responses are copied into Global Relay's archive (`data_leaves_tenancy: "true"`), which is inherent to a third-party 17a-4 archive. Capture is out-of-band through vendor APIs: no latency, no blocking.

**Integrations & partnerships**: OpenAI and Anthropic compliance APIs, Microsoft Copilot, Teams and Exchange Online, Bloomberg, mobile and WhatsApp, Open Connector API. Historical exclusive archiving partnership with Thomson Reuters (2007). No MCP server found (`mcp_support: unverified`).

**Compliance & FS traction**: ISO 27001 and SOC 2 Type 2 logos appear on its site (logos only, not checked against reports). Wikipedia notes annual KPMG controls verification. Client claims (press-cited, dated): 18,000+ clients, 22 of the 25 largest banks, ~61% of US hedge funds. **Hedge-fund fit: high.** It is among the most likely incumbents at a fund, so the practical question is usually "turn on the AI connectors and surveillance module?" rather than "buy Global Relay?"

**Commercial**: Quote-based, typically per user and per connector. Surveillance and AI connectors are add-ons. No public pricing.

## Open questions

- Launch and general-availability dates of the **Claude** and **Microsoft Copilot** connectors; whether Copilot Studio agents are covered.
- Which LLM powers AI Surveillance, where it is hosted, and whether any customer data reaches a third-party model provider or is used for training.
- Gartner 2025 DCGA Leader placement: verify against Gartner, not the vendor release.
- Current customer counts (the 61% of US hedge funds figure is old and press-cited).
- Current CEO and ownership: Warren Roy is listed as CEO on older sources; no 2026 confirmation.

## Sources

- [Global Relay, Wikipedia](https://en.wikipedia.org/wiki/Global_Relay), fetched 2026-10-26. Supports: founding, founders, HQ, offices, private/employee-controlled with no outside funding, client claims, KPMG verification. Confidence: medium.
- [Global Relay Connector for ChatGPT Enterprise](https://www.globalrelay.com/connector/global-relay-connector-for-chatgpt-enterprise/), fetched 2026-10-26. Supports: ChatGPT capture scope, supervision, 17a-4/4511/MiFID II framing. Confidence: high (vendor primary).
- [Global Relay Connector for Microsoft Copilot](https://www.globalrelay.com/connector/microsoft-copilot/), fetched 2026-10-26. Supports: Copilot prompt and response capture via official APIs. Confidence: high (vendor primary).
- [Global Relay Connector for Claude](https://www.globalrelay.com/connector/claude/), fetched 2026-10-26. Supports: Claude Compliance API capture scope, AI-enabled supervision and surveillance, WORM. Confidence: high (vendor primary).
- [Global Relay Announces Next Gen AI-Enabled Communications Surveillance (BusinessWire, 2024-11-12)](https://www.businesswire.com/news/home/20241112420017/en/Global-Relay-Announces-Next-Gen-AI-Enabled-Communications-Surveillance), search snapshot 2026-10-26. Supports: surveillance launch, five-layer design. Confidence: medium.
- [Global Relay AI Surveillance at FINRA 2026](https://www.globalrelay.com/?p=54606), fetched 2026-10-26. Supports: LLM classification, chain-of-thought before alerting. Confidence: medium (vendor).
- [Global Relay Gartner DCGA release (BusinessWire, 2025-10)](https://www.businesswire.com/news/home/20251027851036/en), search snapshot (direct fetch 403). Supports: Leader claim. Confidence: low (vendor claim, unverified against Gartner).
- Cached: `raw/sources/2026-10-26--global-relay--ownership-ai-connectors-surveillance.md`

## History

- [2026-10-26] Page created and researched in one pass. Primary comms-surveillance, because it now sells AI surveillance (since 2024-11) and is a main capture point for Copilot, ChatGPT and Claude records. Labelled platform-module rather than leader in this category, since the surveillance is a newer add-on to a leading archive. Confirmed founder- and employee-controlled independent ownership with no outside funding found. Confirmed a Claude Compliance API connector exists (previously an open question on anthropic-claude-enterprise).
