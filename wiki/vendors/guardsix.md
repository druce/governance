---
title: guardsix (formerly LogPoint)
type: vendor
name: guardsix
slug: guardsix
aka: [LogPoint, Logpoint, Logpoint SIEM, Guardsix Command Centre, Logpoint Director, Muninn]
primary_category: siem-soc
also_listed_in: []
website: "https://guardsix.com/"
founded: null
hq: Copenhagen, Denmark
ownership_state: pe-owned
owner: "Summa Equity (majority, Fund III); Yttrium (formerly Digital+ Partners) significant minority"
ownership_note: "Summa Equity majority stake announced 2023-03-02, subject to regulatory approval expected Q2 2023; a later company release says Summa acquired the stake in April 2023 (exact close date not found). Size undisclosed. Rebranded from Logpoint to guardsix 2026-03-12: a rename, not a merger or change of control. Acquired Muninn (NDR) 2024-10-01 and Logmanager (CZ log management) announced 2026-08-10."
acquisition: {announced: 2023-03-02, closed: null, price: null}
funding_total: "~US$42M venture funding before the Summa buyout (incl. US$30M Series B 2020 led by Digital+ Partners)"
last_funding: "Summa Equity majority investment, announced 2023-03-02"
market_position: {siem-soc: niche-specialist}
deployment_model: [on-prem, saas]
form_factor: [platform]
data_leaves_tenancy: partial
integrations: []
mcp_support: unverified
certifications: [soc2-type2, common-criteria-eal3plus]
pricing_model: "licence/subscription; historically priced by number of nodes (log sources), not data volume"
fs_traction: unverified
target_customer: European MSSPs and regulated or critical-infrastructure organisations that want an EU-owned, self-hostable SIEM with predictable pricing
last_verified: 2026-10-24
verify_after: null
tags: [siem, ndr, soar, ueba, sap-security, mssp, multi-tenant, sovereign, european, on-prem, pe-owned, rebrand]
sources:
  - {claim: "Logpoint rebrands to guardsix (2026-03-12); HQ Copenhagen; SIEM, NDR, SOAR and fleet management; sovereign SecOps platform for MSSPs and regulated organisations; SOC 2 Type II; CEO Mikkel Drucker", url: "https://www.mynewsdesk.com/guardsix/pressreleases/logpoint-becomes-guardsix-as-europe-reassesses-sovereign-security-operations-3436974", date: 2026-03-12, confidence: high}
  - {claim: "Summa Equity acquiring majority stake (2023-03-02), regulatory approval expected Q2 2023; Yttrium (ex-Digital+ Partners) remains significant minority; SaaS and on-premise", url: "https://www.mynewsdesk.com/guardsix/pressreleases/summa-equity-invests-in-logpoint-to-create-european-cybersecurity-powerhouse-3236284", date: 2023-03-02, confidence: high}
  - {claim: "guardsix acquires Logmanager (announced 2026-08-10), terms undisclosed; ~400 customers in CEE/Japan", url: "https://www.mynewsdesk.com/guardsix/pressreleases/guardsix-acquires-logmanager-to-strengthen-log-management-capabilities-across-central-eastern-europe-3460382", date: 2026-08-10, confidence: high}
  - {claim: "Logpoint acquires Muninn (AI-driven NDR), 2024-10-01; first deal under Summa ownership", url: "https://www.govinfosecurity.com/logpoint-strengthens-siem-by-acquiring-muninn-ai-powered-ndr-a-26417", date: 2024-10-01, confidence: medium}
  - {claim: "Command Centre (SIEM, NDR, SOAR, Fleet, Governance); on-prem; positioned against ingestion pricing; MSSP programme", url: "https://guardsix.com/", date: 2026-10-24, confidence: medium}
  - {claim: "Common Criteria EAL3+ certification (vendor release)", url: "https://www.mynewsdesk.com/guardsix/pressreleases/logpoint-only-siem-provider-awarded-eal-3-plus-certification-3085187", date: 2026-10-24, confidence: medium}
---

# guardsix (formerly LogPoint)

> Primary category: [siem-soc](../categories/siem-soc.md).

**One-liner** — guardsix is the Copenhagen-based SIEM vendor known until March 2026 as **LogPoint**. It sells a SIEM + NDR + SOAR platform that can run on-prem, mainly to European MSSPs and regulated organisations. Its pitch is data sovereignty and predictable (non-ingest) pricing.

**What it does** — The platform, now branded **Guardsix Command Centre**, includes:
- **SIEM:** log collection, correlation, search and UEBA, which is LogPoint's historical core. It also has an **SAP security monitoring** module, from LogPoint's 2020 agreement to buy agileSI. Whether UEBA and SAP monitoring are still separately packaged under guardsix is unverified.
- **NDR:** network detection and response from **Muninn**, a Danish AI-driven NDR company acquired **2024-10-01**.
- **SOAR:** playbook automation and case management.
- **Fleet and Governance:** multi-instance management. Its main users are MSSPs running many customer tenants (the "Director" product in LogPoint days; current naming per guardsix.com).

guardsix positions itself against ingestion-based SIEM pricing. Customers choose where it runs ("Your data. Your deployment. Your jurisdiction."), as SaaS or on-premise. In **August 2026** it announced the acquisition of **Logmanager**, a Czech log-management vendor for smaller organisations with about 400 customers in Central Eastern Europe and Japan. Logmanager keeps its brand during integration.

**Naming / provenance — the "guardsix" question resolved.** On **2026-03-12** LogPoint announced "its rebrand to guardsix". This is a **rename only, not a merger, sale or change of ownership**. The release says the rebrand "does not change the company's products, contractual commitments, or support services". logpoint.com now 301-redirects to guardsix.com (checked 2026-10-24). The brand is lower-case "guardsix" in company copy and "Guardsix" at the start of sentences. The page is slugged `guardsix` (current company name), with LogPoint in `aka:`. Older history: per its own history page, the company took the LogPoint name around 2012 after Danish VC seed funding. The original founding year was not confirmed.

**Ownership & viability** — `pe-owned`.
- **Summa Equity.** Summa, a Swedish growth investor, announced on **2023-03-02** that it was "acquiring a majority stake in ... Logpoint" from its Fund III, subject to regulatory approval expected in Q2 2023. A later company release says the stake was acquired in **April 2023**; the exact close date was not found. Deal size undisclosed.
- **Minority holder.** **Yttrium** (formerly Digital+ Partners, which led LogPoint's US$30M Series B in 2020) remains a significant minority shareholder.
- **Management.** CEO **Mikkel Drucker** (ex-Netigate) since May 2024 per secondary reporting.
- **Strategy.** Under Summa the company is consolidating: Muninn (2024), then Logmanager (2026). Three years into the hold, a further sale or merger in the next few years would not be surprising.
- **Customer risk.** The main risk is a buyer folding the SIEM into a larger platform. Contracts should carry continuity terms for on-prem licences.

**Positioning & differentiators** — `niche-specialist`: a European SIEM with real installed base among MSSPs and public and critical-infrastructure organisations, but not a peer of the US platforms in scale or in breadth of detection content.
- **Sovereignty and self-hosting:** EU-owned and HQ'd, deployable on-prem, SOC 2 Type II, and (per the vendor) the only European SIEM with a Common Criteria **EAL3+** certification. [splunk](splunk.md) (Cisco), [microsoft-sentinel](microsoft-sentinel.md) and [google-secops](google-secops.md) are US-owned, and the last two are cloud-only.
- **Pricing model:** historically licensed by **number of nodes (log sources), not data volume**, which avoids the ingest-cost surprises of Splunk and Sentinel. The closest analogue is [manageengine](manageengine.md)'s licence pricing.
- **MSSP-native:** multi-tenant fleet management and an MSSP partner programme. Many end customers consume guardsix through a European MSSP, not directly. [sekoia](sekoia.md) is the other European, MSSP-heavy option (SaaS, AI SOC-leaning).
- **Versus [elastic](elastic.md):** both are self-hostable. Elastic has the larger ecosystem and open-source base. guardsix ships a more packaged SIEM + SOAR + NDR with vendor support.

**Who should choose them / anti-fit** — Fits a **European or EU-regulated firm** (DORA, NIS2, data-residency constraints) or one served by a European MSSP that runs guardsix. It also fits firms that need SIEM on-prem with predictable licence cost. The one survey respondent (in production) shows it does reach this audience. **Anti-fit:**
- A US hedge fund on Microsoft E5. [microsoft-sentinel](microsoft-sentinel.md) with Defender is the default and integrates more tightly.
- Firms that want a cloud-native, AI-SOC-first platform with a large US detection-content ecosystem.
- Firms that want a managed detection service. guardsix sells software; MDR comes from its MSSP partners.

**Known weaknesses / gotchas** —
- **The name changed in 2026.** Survey answers, RFPs and analyst reports will say "LogPoint", "Logpoint" or "guardsix". Treat them as one vendor.
- **Smaller detection ecosystem** than Splunk or Sentinel. Check rule coverage for your SaaS estate (M365, Okta, cloud) and the community content available.
- **Post-acquisition integration** (Muninn, Logmanager) is ongoing. Ask which components share one console and data model today.
- **AI/agent features not evidenced.** The homepage fetched on 2026-10-24 shows no AI-analyst or MCP features. If an agentic SOC layer matters, pair guardsix with a product from [ai-soc-analysts](../categories/ai-soc-analysts.md).
- **Analyst placement dated.** The Gartner MQ SIEM "Visionary" placement LogPoint promoted is from 2020. Current placement was not checked.

**Deployment & data handling** — On-prem/self-hosted or SaaS (the 2023 Summa release says "available as a SaaS solution and On-Premise"). With on-prem, logs stay in your environment. With SaaS, hosting location (EU regions are claimed as part of the sovereignty pitch) and retention are **unverified** in detail. Out-of-band (log collection), so there is no inline latency concern.

**Integrations & partnerships** — Integrations catalogue on guardsix.com (contents not enumerated on this pass). SAP monitoring is a historical differentiator. Channel is MSSP- and partner-led ("Guardsix Collaborate"). MCP support unverified (none advertised).

**Compliance & FS traction** — SOC 2 Type II attestation (company release). Common Criteria EAL3+ (vendor release; achieved ~2015, renewed 2021 for v6.8; current version status unverified). The homepage lists healthcare, energy and utilities, municipalities and defence. Financial services is not a featured vertical; there is one Gartner Peer Insights review from a banking analyst. FS traction unverified.

**Commercial** — Licence or subscription. Historically per-node pricing (vendor statements 2019–2020). The current guardsix model is described only as "predictable" and positioned against ingestion pricing. A SIEM sizing calculator is on the site. No public price bands.

**Survey note** — 2026-10 CTO survey write-in: **1 respondent, in production**, under Q46 *SIEM / Logging*, written as "LogPoint".

## Open questions

- Exact close date of the Summa Equity majority investment (April 2023 per a company release).
- Current pricing metric under guardsix (nodes, EPS, assets?) and price bands.
- SaaS hosting regions and retention; current EAL3+ status for the latest version.
- Whether the Logmanager deal has closed; Muninn integration status.
- Any AI-analyst / agentic SOC roadmap or MCP support.
- Named financial-services customers.

## Sources

- [Logpoint becomes guardsix (guardsix newsroom, 2026-03-12)](https://www.mynewsdesk.com/guardsix/pressreleases/logpoint-becomes-guardsix-as-europe-reassesses-sovereign-security-operations-3436974) — fetched 2026-10-24 — supports: rebrand, HQ, product scope, SOC 2, CEO; confidence: high
- [Summa Equity invests in Logpoint (company release, 2023-03-02)](https://www.mynewsdesk.com/guardsix/pressreleases/summa-equity-invests-in-logpoint-to-create-european-cybersecurity-powerhouse-3236284) — fetched 2026-10-24 — supports: majority stake, approval timing, Yttrium minority, SaaS/on-prem; confidence: high
- [guardsix acquires Logmanager (company release, 2026-08-10/11)](https://www.mynewsdesk.com/guardsix/pressreleases/guardsix-acquires-logmanager-to-strengthen-log-management-capabilities-across-central-eastern-europe-3460382) — fetched 2026-10-24 — supports: Logmanager deal; confidence: high
- [Logpoint strengthens SIEM by acquiring Muninn (GovInfoSecurity, 2024-10-01)](https://www.govinfosecurity.com/logpoint-strengthens-siem-by-acquiring-muninn-ai-powered-ndr-a-26417) — search snippet 2026-10-24 (403 on fetch) — supports: Muninn NDR acquisition, Summa context, Drucker; confidence: medium
- [guardsix homepage](https://guardsix.com/) — fetched 2026-10-24 — supports: Command Centre modules, deployment choice, pricing positioning, MSSP programme, verticals; confidence: medium (vendor marketing)
- [Logpoint only SIEM provider awarded EAL 3+ certification (company release)](https://www.mynewsdesk.com/guardsix/pressreleases/logpoint-only-siem-provider-awarded-eal-3-plus-certification-3085187) — search snippet 2026-10-24 — supports: EAL3+; confidence: medium
- Cached: `raw/sources/2026-10-24--logpoint--guardsix-summa-ownership.md`; earlier one-liner evidence in `raw/sources/2026-10-23--mdr-soc-writeins--one-liner-sources.md`

## History

- [2026-10-24] Page created via wiki-create and researched the same day. Triggered by a single in-production write-in ("LogPoint") under Q46 SIEM / Logging in the 2026-10 CTO survey. Verified the "guardsix" note: a 2026-03-12 rename of LogPoint, not a merger or sale. Slugged by current company name (guardsix), with LogPoint in aka.
