---
title: Sophos
type: vendor
name: Sophos
slug: sophos
aka: [Secureworks, Secureworks Taegis, Taegis XDR, Sophos MDR, Sophos Intercept X, Sophos Central, Sophos Fusion, Sophos Firewall, Sophos AI Defense]
primary_category: edr-xdr
also_listed_in: [siem-soc, network-security-sase, ai-access-governance, ai-soc-analysts]
website: https://www.sophos.com/
founded: null
hq: Oxfordshire, UK (described as "Oxford-based" by UKTN, 2025-02-04; exact HQ town not verified)
ownership_state: pe-owned
owner: Thoma Bravo
ownership_note: Taken private by Thoma Bravo for ~$3.9B. Announced 2019-10-14, completed 2020-03-02, delisted from the LSE. Sophos then bought SecureWorks Corp. (NASDAQ:SCWX, ~83% owned by Dell). Merger agreement signed and announced 2024-10-21, closed 2025-02-03, at $8.50/share cash (~$859M). Secureworks is now a wholly owned Sophos subsidiary, and Taegis is the analytics engine under the Sophos Fusion platform launched 2026-07-15.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {edr-xdr: challenger, siem-soc: niche-specialist, network-security-sase: challenger, ai-access-governance: platform-module, ai-soc-analysts: challenger}
deployment_model: [saas, hybrid]
form_factor: [agent, platform, inline-proxy]
data_leaves_tenancy: "true"
integrations: [crowdstrike, microsoft-defender, sentinelone]
mcp_support: unverified
certifications: []
pricing_model: subscription per user/endpoint/server; Next-Gen SIEM priced by users and servers rather than data volume
fs_traction: unverified
target_customer: SMB to mid-market, heavily through MSP/channel partners
last_verified: 2026-10-23
verify_after: null
tags: [edr, xdr, mdr, firewall, siem, pe-owned, thoma-bravo, secureworks, taegis, shadow-ai]
sources:
  - {claim: "Merger agreement with Sophos Inc. (Thoma Bravo affiliates) entered 2024-10-21", url: "https://www.sec.gov/Archives/edgar/data/1468666/000095014224002611/eh240547106_8k.htm", date: 2026-10-23, confidence: high}
  - {claim: "Merger consummated 2025-02-03; each share converted to $8.50 cash; Secureworks became a wholly owned subsidiary of Sophos Inc.", url: "https://www.sec.gov/Archives/edgar/data/1468666/000095014225000239/eh250585750_8k.htm", date: 2026-10-23, confidence: high}
  - {claim: "Deal valued at ~$859M; 28% premium; Sophos 'leading pure-play' MDR provider; Secureworks CTU joins Sophos X-Ops", url: "https://www.sophos.com/en-us/press/press-releases/2025/02/sophos-completes-secureworks-acquisition", date: 2026-10-23, confidence: high}
  - {claim: "Thoma Bravo completed ~$3.9B take-private of Sophos 2020-03-02 (announced 2019-10-14)", url: "https://techcrunch.com/2020/03/02/thoma-bravo-completes-3-9b-sophos-acquisition", date: 2026-10-23, confidence: high}
  - {claim: "Sophos Endpoint bundled into all Taegis MDR/XDR subscriptions at no extra cost; Taegis ingests CrowdStrike, Defender, SentinelOne, Carbon Black (2025-09-03)", url: "https://www.channelinsider.com/security/sophos-taegis-response-capabiities/", date: 2026-10-23, confidence: medium}
  - {claim: "Sophos Fusion launched 2026-07-15 on Taegis analytics; Next-Gen SIEM priced by users/servers; AI resolves 52% of cases (vendor claim)", url: "https://siliconangle.com/?p=789962", date: 2026-10-23, confidence: medium}
  - {claim: "Sophos AI Defense GA October 2026: shadow-AI discovery and real-time prompt/upload inspection across device, network, sign-in, browser", url: "https://www.sophos.com/en-us/press/press-releases/2026/10/sophos-launches-ai-defense-to-expose-shadow-ai-and-secure-ai-use-in-real-time", date: 2026-10-23, confidence: medium}
  - {claim: "625K+ customers; Sophos MDR >40,000 organizations; portfolio spans endpoint, XDR, Next-Gen SIEM, ITDR, NGFW, NDR, ZTNA, email, MDR", url: "https://www.sophos.com/en-us/company", date: 2026-10-23, confidence: medium}
---

# Sophos

> Primary category: [edr-xdr](../categories/edr-xdr.md). Also listed in [siem-soc](../categories/siem-soc.md), [network-security-sase](../categories/network-security-sase.md) and [ai-access-governance](../categories/ai-access-governance.md). **Owner of Secureworks (Taegis)** since 2025-02-03.

**One-liner** — A Thoma Bravo-owned, channel-led security platform for small and mid-size organisations: endpoint protection, firewalls and the largest pure-play MDR business. Since buying Secureworks in 2025 it also owns the Taegis XDR/SIEM analytics engine that respondents wrote in as "Secureworks Taegis".

**What it does** — Four businesses, now sold as one platform (**Sophos Fusion**, launched 2026-07-15, which rebuilds Sophos Central):
- **Endpoint (EDR/XDR).** The historical core: next-gen AV, EDR, server and mobile protection (the Intercept X lineage).
- **Security operations.** XDR, ITDR, and a **Next-Gen SIEM** (GA from 2026-08-15) that is priced by users and servers rather than by data volume. Fusion's XDR "runs on the Taegis analytics" that came with Secureworks.
- **Managed services.** **Sophos MDR**, which Sophos says covers more than 40,000 organisations, plus incident response. With the Secureworks Counter Threat Unit added to Sophos X-Ops, Sophos calls itself the "leading pure-play" MDR provider.
- **Network.** Sophos Firewall (NGFW), NDR, ZTNA, switches and wireless.

The newest piece is **Sophos AI Defense** (GA October 2026). It discovers sanctioned and shadow AI tools and inspects "prompts, uploads, and other AI interactions as they happen", enforcing through the existing device, network, sign-in and browser controls and feeding AI events to XDR/MDR analysts.

**Naming / provenance** — Survey respondents wrote "Secureworks Taegis (Sophos)". **Secureworks** was Dell's majority-owned public MDR/XDR company (NASDAQ: SCWX), and **Taegis** was its cloud XDR platform. Both now belong to Sophos, so the wiki has no separate Secureworks page. As of 2026-10, Sophos still uses the Taegis name for its MDR/XDR subscriptions, and the Secureworks name survives in legal and product-terms pages. Expect the Taegis brand to fade into "Sophos XDR / Fusion" (inferred from the Fusion launch, not announced).

**Ownership & viability** — `pe-owned` by **Thoma Bravo**: a ~$3.9B take-private announced 2019-10-14 and completed 2020-03-02. **Secureworks deal**, verified against SEC filings:
- **Signed and announced** 2024-10-21 (Secureworks 8-K, Item 1.01).
- **Closed** 2025-02-03 (8-K Item 2.01: each share converted to **$8.50 cash**; Form 25 delisting filed the same day).
- **Value:** ~**$859M** (Sophos), a 28% premium to the unaffected 90-day VWAP. Dell held ~83% of Secureworks at signing (trade press).

Viability is not in question at Sophos's scale. The PE-ownership risks are the usual ones: a later sale or IPO by Thoma Bravo, and consolidating products to cut costs. Taegis customers who did not choose Sophos have already seen the platform folded into Fusion.

**Positioning & differentiators** —
- **MDR first, for the mid-market.** Against [crowdstrike](crowdstrike.md) (Falcon Complete) and [sentinelone](sentinelone.md), Sophos's pitch is a large managed service sold through MSPs at mid-market prices. Many small firms buy Sophos *as* their SOC.
- **Accepts other vendors' endpoints.** Taegis/Fusion ingests CrowdStrike, Microsoft Defender, SentinelOne and Carbon Black telemetry, so you can buy Sophos MDR or SIEM without replacing EDR. Since 2025-09-03, Sophos Endpoint is bundled free into Taegis MDR/XDR subscriptions to encourage switching.
- **SIEM priced by user and server, not by ingest.** This is a deliberate contrast with [splunk](splunk.md) and [microsoft-sentinel](microsoft-sentinel.md) ingest economics. It suits firms whose SIEM need is compliance logging plus MDR-driven detection.
- **One vendor across endpoint, firewall and MDR.** [fortinet](fortinet.md) and [palo-alto-networks](palo-alto-networks.md) also bundle firewall and endpoint. Sophos's difference is that it leads with the managed service.
- **AI-access controls are brand new.** AI Defense went GA in October 2026 and has no independent evaluation. Against dedicated [ai-access-governance](../categories/ai-access-governance.md) tools or [zscaler](zscaler.md)/[netskope](netskope.md), it is a platform module and should be judged as one.

**Who should choose them / anti-fit** — Fits a **small or mid-size fund without a 24/7 security team** that wants endpoint plus MDR (and maybe the firewall) from one channel-friendly vendor. Also fits an existing Secureworks/Taegis customer weighing whether to stay. **Anti-fit:** a large firm with its own SOC and detection engineers. The SIEM is not built for heavy custom detection engineering at Splunk/Sentinel scale. Also a firm committed to Microsoft E5 (Defender plus Sentinel overlap heavily), and anyone who wants best-of-breed AI-usage governance today.

**Known weaknesses / gotchas** — Secureworks integration is ongoing. Ask legacy Taegis customers what changed in support, pricing and roadmap after 2025-02-03. Brand confusion: Taegis, Secureworks, Sophos XDR and Sophos Fusion all appear in contracts and documentation. Vendor statistics (52% of cases resolved by AI without humans, 89-second average alert-to-automated-response) are self-reported. Sophos's firewall line, like every edge appliance, has had serious CVEs. Treat it as patch-critical infrastructure. Specific KEV entries not verified here.

**Deployment & data handling** — SaaS management and analytics (Sophos Central / Fusion) plus endpoint agents, with on-prem firewalls and collectors, so `hybrid`. Telemetry leaves the tenancy to Sophos's cloud by design (`data_leaves_tenancy: "true"`), and Taegis has an on-prem collector forwarding syslog to its data lake. Data residency regions are **unverified**. For AI Defense, whether inspected prompt content is stored or sent to an AI model is **unverified**.

**Integrations & partnerships** — 500+ third-party integrations into the Fusion data layer (vendor). Ingests third-party EDR (CrowdStrike, Microsoft Defender, SentinelOne, Carbon Black). Strong MSP/MSSP distribution channel. MCP support unverified.

**Compliance & FS traction** — **Unverified.** No named hedge-fund or asset-manager references found. The Oct-2026 CTO survey had 2 respondents in production on "Secureworks Taegis (Sophos)" under SIEM/Logging.

**Commercial** — Subscription per user, endpoint or server, mostly sold through partners. The Next-Gen SIEM is priced by users and servers. Endpoint is bundled free into Taegis MDR/XDR (2025-09-03 onward). No public price bands found.

## Open questions

- Long-term status of the **Taegis** brand and contracts inside Sophos Fusion. Is there a migration deadline for legacy Taegis customers?
- Data residency regions for Fusion / Taegis telemetry.
- AI Defense data handling (are prompts retained, and where are they analysed?) and any independent evaluation.
- Certifications (SOC 2 Type II, ISO 27001, FedRAMP for Taegis), not checked.
- Gartner/Forrester placements for EPP, MDR and SIEM, not checked.
- Sophos founding year (the company dates to the 1980s, but this was not verified from a primary source this pass).

## Sources

- [SecureWorks Corp. Form 8-K, 2024-10-21 (Item 1.01, merger agreement)](https://www.sec.gov/Archives/edgar/data/1468666/000095014224002611/eh240547106_8k.htm) — fetched 2026-10-23 — supports: signing date, buyer = Sophos Inc. / Thoma Bravo affiliates; confidence: high
- [SecureWorks Corp. Form 8-K, 2025-02-03 (Item 2.01, completion)](https://www.sec.gov/Archives/edgar/data/1468666/000095014225000239/eh250585750_8k.htm) — fetched 2026-10-23 — supports: closing date 2025-02-03, $8.50/share cash, wholly owned subsidiary; confidence: high
- [Sophos completes Secureworks acquisition (Sophos press)](https://www.sophos.com/en-us/press/press-releases/2025/02/sophos-completes-secureworks-acquisition) — fetched 2026-10-23 — supports: ~$859M value, 28% premium, MDR leadership claim, CTU into X-Ops; confidence: high
- [Thoma Bravo completes $3.9B Sophos acquisition (TechCrunch, 2020-03-02)](https://techcrunch.com/2020/03/02/thoma-bravo-completes-3-9b-sophos-acquisition) — fetched 2026-10-23 — supports: PE ownership, dates, price; confidence: high
- [Sophos bundles endpoint protection into Taegis MDR and XDR (ChannelInsider, 2025-09-03)](https://www.channelinsider.com/security/sophos-taegis-response-capabiities/) — fetched 2026-10-23 — supports: endpoint bundling, third-party EDR ingestion; confidence: medium
- [Sophos Fusion launch (SiliconANGLE, 2026-07-15)](https://siliconangle.com/?p=789962) — fetched 2026-10-23 — supports: Fusion on Taegis analytics, Next-Gen SIEM pricing, AI SOC stats (vendor); confidence: medium
- [Sophos launches AI Defense (Sophos press, Oct 2026)](https://www.sophos.com/en-us/press/press-releases/2026/10/sophos-launches-ai-defense-to-expose-shadow-ai-and-secure-ai-use-in-real-time) — fetched 2026-10-23 — supports: AI Defense GA and capabilities; confidence: medium (vendor)
- [Sophos company page](https://www.sophos.com/en-us/company) — fetched 2026-10-23 — supports: customer counts, portfolio; confidence: medium
- Cached: `raw/sources/2026-10-23--sophos--secureworks-sec-8k-merger.md`, `raw/sources/2026-10-23--sophos--ownership-platform-fusion-ai-defense.md`

## History

- [2026-10-23] Page created and researched. Added because of Oct-2026 CTO survey write-ins ("Secureworks Taegis (Sophos)", 2 in production under SIEM/Logging). Secureworks is folded into this page (acquired-closed subsidiary, no separate page). Primary set to edr-xdr (core endpoint/XDR business, and Taegis is an XDR), with cross-lists siem-soc (Taegis/Next-Gen SIEM), network-security-sase (Sophos Firewall/ZTNA), and ai-access-governance (AI Defense, GA Oct 2026).
- [2026-10-24] Cross-listed in ai-soc-analysts as an MDR provider (Sophos MDR / Taegis MDR) after the decision to place MDR providers in that category.
