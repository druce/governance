---
title: Egnyte
type: vendor
name: Egnyte
slug: egnyte
aka: [Egnyte Secure & Govern, Egnyte Protect, Egnyte Connect, Egnyte Collaborate]
primary_category: data-access-governance
also_listed_in: [dspm, content-sources]
website: "https://www.egnyte.com"
founded: 2007
hq: Mountain View, California, USA
ownership_state: pe-owned
owner: GI Partners and TA Associates (majority)
ownership_note: "Majority investment by GI Partners and TA Associates announced 2025-02-25, terms undisclosed; founders, management and prior VCs (Springcoast, GV, Polaris, Kleiner Perkins) retain significant stakes. Close date not found. Previously VC-backed ($137.5M raised through a 2018 $75M Series E led by Goldman Sachs)."
acquisition: {announced: 2025-02-25, closed: null, price: null}
funding_total: "$137.5M VC (pre-2025); 2025 PE majority deal terms undisclosed"
last_funding: "PE majority investment (GI Partners + TA Associates), announced 2025-02-25, terms undisclosed"
market_position: {data-access-governance: platform-module, dspm: platform-module, content-sources: challenger}
deployment_model: [saas]
form_factor: [platform, api]
data_leaves_tenancy: "true"
integrations: [microsoft-365, sharepoint-online, onedrive, google-drive, amazon-s3, splunk, chatgpt, claude, microsoft-copilot-studio]
mcp_support: server
certifications: []
pricing_model: seat
fs_traction: claimed
target_customer: mid-market and lower-enterprise firms with heavy file workloads; strong in alternative investments, AEC, life sciences
last_verified: 2026-10-23
verify_after: null
tags: [content-platform, file-sharing, content-governance, data-classification, ransomware-detection, virtual-data-room, sec-17a-4, mcp-server]
sources:
  - {claim: "GI Partners and TA Associates majority investment; founders/management/VCs retain significant ownership; terms undisclosed; 22,000 customers; founded 2007", url: "https://blocksandfiles.com/2025/02/26/private-equity-egnyte", date: 2026-10-23, confidence: high}
  - {claim: "Secure & Govern = Content Classification, Access Control, Content Lifecycles; ransomware detection via signatures + behavioural analytics; classification of PII/financial data; AI Safeguards", url: "https://www.egnyte.com/products/governance", date: 2026-10-23, confidence: medium}
  - {claim: "Buy-side positioning; SEC 17a-4 claim; named PE customers Rockbridge and The Riverside Company", url: "https://www.egnyte.com/industries/financial-services/buy-side", date: 2026-10-23, confidence: medium}
  - {claim: "Egnyte MCP Server honours existing Egnyte permissions; requires AI add-on and admin opt-in; OAuth 2.0", url: "https://learn.microsoft.com/en-us/connectors/egnytemcpserver/", date: 2026-10-23, confidence: high}
  - {claim: "HQ Mountain View; funding history to $137.5M; Protect + Connect merged 2020", url: "https://en.wikipedia.org/wiki/Egnyte", date: 2026-10-23, confidence: medium}
---

# Egnyte

> Primary category: [data-access-governance](../categories/data-access-governance.md). Also listed in [dspm](../categories/dspm.md) and [content-sources](../categories/content-sources.md).

**One-liner** — A cloud file-sharing and content platform, popular with alternative investment firms, that ships its own governance layer (Secure & Govern): it classifies sensitive files, reviews permissions and external sharing, detects ransomware, and enforces retention, mainly over content stored in Egnyte and in connected Microsoft 365 repositories.

**What it does** — Egnyte is a **content platform first**. Firms use it as the file system of record: shared drives, desktop-Excel-against-cloud-files, external sharing, and virtual data rooms for LPs, GPs and advisors. The governance product, sold as **Secure & Govern** (formerly *Egnyte Protect*; folded into one platform with *Egnyte Connect* in 2020), has three services by Egnyte's description:

- **Content Classification**: AI-based detection of PII, financial and regulated content, with one-click policy packs (PCI-DSS, GDPR, and others).
- **Access Control**: reviews permissions and sharing, finds public links without passwords and over-shared content, and flags unusual access through user-behaviour analytics.
- **Content Lifecycles**: retention, archiving and disposal rules. Egnyte claims these support SEC 17a-3/17a-4 recordkeeping (vendor claim; see open questions).

On top of that it runs **ransomware detection** (signature scanning plus behavioural analytics, optional automatic suspension of the affected user, and snapshot recovery). It also has an AI layer (AI Assistant, Knowledge Bases, AI Agents, "AI Safeguards" to control which content AI tools can reach) and, since February 2026, a generally available **MCP server**.

**Naming / provenance** — Founded 2007 (incorporated 2008) by Vineet Jain (CEO), Amrit Jassal, Kris Lahiri and Rajesh Ram; HQ Mountain View, California. Product names drift: Egnyte Connect / Collaborate (the file platform), Egnyte Protect, then Secure & Govern (the governance module). Survey respondents wrote "Egnyte", "Egnyte for files" and "Egnyte Secure and Govern". All of these mean this page.

**Ownership & viability** — `pe-owned`. **GI Partners and TA Associates** announced a **majority investment on 2025-02-25**, terms undisclosed. Founders, management and earlier VCs (Springcoast, GV, Polaris, Kleiner Perkins) kept significant stakes. Before that Egnyte raised **$137.5M** of venture capital, the last round a **$75M Series E led by Goldman Sachs in 2018**. Blocks & Files reported **22,000 customers** at the time of the deal. An aggregator (multiples.vc) puts the price at ~$2.9B on ~$250M revenue. No primary source corroborates that, so treat it as unverified. Viability is not a near-term concern: at ~22,000 customers and with two large sponsors behind it, Egnyte is an established vendor. The usual PE pattern of price increases and bundling at renewal is the more realistic risk. TA Associates also controls [netwrix](netwrix.md), a data-access-governance peer. That is worth knowing but not a conflict in practice.

**Positioning & differentiators** —
- **Governance where the files already live.** [varonis](varonis.md), [netwrix](netwrix.md) and [lepide](lepide.md) govern data that sits on file servers, SharePoint and M365. Egnyte governs content *inside its own repository* (plus connected OneDrive/SharePoint Online sources). For a firm that already runs on Egnyte, classification and permission review come with no separate collector estate. The cost is that coverage outside Egnyte is narrower and less proven than Varonis's.
- **A platform module, not a standalone governance tool.** The `platform-module` label fits: you buy Egnyte for file sharing and data rooms, and governance is an add-on tier. Compare [microsoft-purview](microsoft-purview.md), which plays the same role for M365 content, and [sharepoint](sharepoint.md) and [google-drive](google-drive.md) as the competing content sources.
- **Alt-investment fit is real.** Buy-side marketing (PE deal workflows, CIM summarisation, LP data rooms) and named PE customers (Rockbridge, The Riverside Company) line up with the survey. Five write-ins and four respondents in production make Egnyte one of the most-cited write-ins in the October 2026 survey.
- **Permission-aware AI access via MCP.** The MCP server performs every request as the signed-in user under existing Egnyte permissions. Agents and copilots therefore inherit Egnyte's access model instead of a copied index. This matters if you plan to point ChatGPT, Claude or Copilot Studio at deal files.

**Who should choose them / anti-fit** — Fits a **hedge fund or PE firm already standardised on Egnyte** as its file system, especially one with external data-room needs and a small IT team that wants classification, sharing hygiene and ransomware detection without a separate DAG deployment. **Anti-fit:** a firm whose unstructured data lives mainly in SharePoint/OneDrive or on-prem file servers. There [microsoft-purview](microsoft-purview.md), [varonis](varonis.md) or [netwrix](netwrix.md) govern the data in place, and adopting Egnyte for governance alone would mean migrating content. Also anti-fit: a firm that needs posture management across databases, warehouses and cloud object stores ([cyera](cyera.md), [sentra](sentra.md)), because Egnyte is file-centric.

**Known weaknesses / gotchas** —
- **Coverage boundary.** Connected sources confirmed in documentation are Egnyte itself, OneDrive for Business and SharePoint Online. A 2020 datasheet also listed on-prem SharePoint and Windows file servers, and the governance page names Google Drive and Amazon S3. Box, Dropbox and current on-prem file-server support are unverified. Check the current supported-sources list before treating Egnyte as a firm-wide DAG tool.
- **Tier gating.** Third-party pricing summaries suggest that "basic" ransomware protection is in lower tiers and fuller detection and governance sit in higher tiers or the governance add-on. The MCP server requires the **AI add-on**. Expect the useful governance features to cost more than the base seat.
- **Survey placement.** Respondents put Egnyte under DSPM (2), Data Access Governance (1), GRC / AI Governance (1) and Data Engineering / Ingestion (1). The DSPM and DAG placements are legitimate: classification is DSPM-shaped, permission review is DAG-shaped. **The GRC placement is a respondent misplacement**: Egnyte has compliance features (retention, audit trails, a governance risk dashboard) but no risk register, control library or audit-management workflow, so it is not an [enterprise-grc](../categories/enterprise-grc.md) platform. The respondent may have meant the "AI Governance" half of the combined question (Egnyte's AI Safeguards / AI Control Center), which governs AI access to content and is closer to DAG. **The Data Engineering placement is plausible**: as a document source for ingestion/RAG it is a [content-sources](../categories/content-sources.md) entry.

**Deployment & data handling** — SaaS. Egnyte has historically offered on-prem caching/sync appliances for hybrid file access, but that was not verified on this pass, so `deployment_model` lists SaaS only. **Data leaves the tenancy** in the sense that matters: Egnyte *is* the hosted repository, so file content resides with Egnyte. Its built-in AI features process that content inside Egnyte's service. Which model providers sit behind Egnyte AI, where inference runs, retention, and training-use terms are unverified. Through MCP, external LLM clients (ChatGPT, Claude, Copilot) can pull content out to the client's model under the user's permissions. That is governed by admin allow-lists (ChatGPT, Claude, Microsoft Copilot and local CLI tools are on by default once MCP is enabled, per Egnyte's March 2026 release notes), but content leaving to those clients is then subject to *their* data terms. Out-of-band scanning, not inline.

**Integrations & partnerships** — Microsoft 365 co-editing, OneDrive/SharePoint Online as governed sources, Google Drive, Amazon S3, Splunk (security event export). **MCP server** (generally available February 2026 for AI-add-on plans) listed as a connector in Microsoft Copilot Studio / Power Platform, as an app in ChatGPT and as a connector in Claude. Per-app admin controls added March 2026.

**Compliance & FS traction** — Egnyte's governance page lists SOC 2 Type 2, ISO 27001, GDPR, PCI-DSS, CMMC, GxP and SEC 17a-3/17a-4 alongside "FedRAMP Moderate Equivalent". It is ambiguous which of these Egnyte holds as attestations and which it helps customers meet, so `certifications` is left empty pending the trust-centre check. **FS traction claimed**: named PE customers Rockbridge and The Riverside Company (vendor case studies), FS logo strip (Creative Planning, EP Wealth, IK Partners, GP Bullhound, Wintrust, Nasdaq). Its new majority owner GI Partners is reportedly a customer. Independently, the October 2026 CTO survey (mostly hedge funds and PE) had four respondents reporting it in production. No named hedge-fund customer found.

**Commercial** — Per-user subscription in tiers, with governance and AI as higher tiers or add-ons. One third-party summary cites a $20/user/month Business tier. That figure is unverified and likely stale.

## Open questions

- Which certifications Egnyte itself holds (SOC 2 Type II, ISO 27001/27701/42001), not just the frameworks it supports.
- Whether SEC 17a-4 support is WORM-compliant storage with a designated-third-party undertaking, or just retention policy. This matters for a registered adviser.
- Current list of governed third-party repositories (on-prem file servers, Box, Dropbox, Google Drive) for Secure & Govern.
- Egnyte AI: which LLM providers, inference location, retention, and whether customer content is used for training.
- Close date of the GI Partners / TA Associates majority deal; whether the reported ~$2.9B valuation is accurate.
- Current packaging and pricing of Secure & Govern and the AI add-on.

## Sources

- [Private equity pair make Egnyte majority buy (Blocks & Files)](https://blocksandfiles.com/2025/02/26/private-equity-egnyte) — fetched 2026-10-23 — supports: GI Partners/TA majority investment, retained holders, 22,000 customers, founders, prior funding; confidence: high
- [Egnyte governance product page (Egnyte)](https://www.egnyte.com/products/governance) — fetched 2026-10-23 — supports: classification, UBA, ransomware detection, compliance claims, AI Safeguards; confidence: medium (vendor marketing)
- [Egnyte for buy-side financial services (Egnyte)](https://www.egnyte.com/industries/financial-services/buy-side) — fetched 2026-10-23 — supports: PE/data-room positioning, SEC 17a-4 claim, Rockbridge and Riverside case studies; confidence: medium (vendor marketing)
- [Egnyte MCP Server (Microsoft Learn)](https://learn.microsoft.com/en-us/connectors/egnytemcpserver/) — fetched 2026-10-23 — supports: MCP server tools, permission inheritance, AI add-on prerequisite; confidence: high
- [Egnyte (Wikipedia)](https://en.wikipedia.org/wiki/Egnyte) — fetched 2026-10-23 — supports: HQ, founding, funding history, 2020 product merge; confidence: medium (secondary)
- Cached: `raw/sources/2026-10-23--egnyte--gi-ta-majority-investment.md`, `raw/sources/2026-10-23--egnyte--governance-product-page.md`, `raw/sources/2026-10-23--egnyte--buy-side-financial-services.md`, `raw/sources/2026-10-23--egnyte--mcp-server.md`, `raw/sources/2026-10-23--egnyte--wikipedia.md`

## History

- [2026-10-23] Page created via wiki-create and researched the same day. Triggered by five write-ins (four in production) in the October 2026 CTO survey, spread across DSPM, DAG, GRC / AI Governance and Data Engineering. Primary set to data-access-governance (governance module is permission/sharing review plus classification over unstructured files, the Varonis/Netwrix shape); DSPM and content-sources cross-listed; GRC placement judged a respondent misplacement.
