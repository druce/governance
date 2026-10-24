---
title: ManageEngine
type: vendor
name: ManageEngine
slug: manageengine
aka: [ManageEngine Log360, Log360, EventLog Analyzer, ADAudit Plus, PAM360, Zoho Corp]
primary_category: siem-soc
also_listed_in: []
website: https://www.manageengine.com/
founded: null
hq: Chennai, India (parent Zoho Corp.)
ownership_state: independent
owner: Zoho Corporation (privately held)
ownership_note: ManageEngine is "the enterprise IT management division of Zoho Corp." Zoho is privately held and bootstrapped (no outside investors), with about 19,000 staff and HQ in Chennai, per Zoho's 2026-02-18 release. ManageEngine has been "in the IT management arena since 2002". No external funding, so there is no investor exit clock.
acquisition: {announced: null, closed: null, price: null}
funding_total: none (bootstrapped parent)
last_funding: null
market_position: {siem-soc: challenger}
deployment_model: [on-prem, saas]
form_factor: [platform, agent]
data_leaves_tenancy: partial
integrations: []
mcp_support: server
certifications: []
pricing_model: quote-based licence (on-prem) / subscription (cloud); 30-day free trial
fs_traction: unverified
target_customer: SMB to mid-market IT and security teams, especially Microsoft/Active Directory-heavy shops
last_verified: 2026-10-23
verify_after: null
tags: [siem, log-management, ueba, soar, active-directory, zoho, on-prem, value-tier]
sources:
  - {claim: "Log360 marketed as AI-powered SIEM with SOAR, UEBA, Vigil IQ TDIR, Ask Zia / Zia Agents and an MCP Server integration; downloadable and cloud editions", url: "https://www.manageengine.com/log-management/", date: 2026-10-23, confidence: medium}
  - {claim: "Log360 included in the Gartner Magic Quadrant for SIEM dated 2025-10-08 (quadrant not stated by vendor)", url: "https://www.manageengine.com/blog/it-security/manageengine-recognized-in-the-2025-gartner-magic-quadrant-for-security-information-and-event-management.html", date: 2026-10-23, confidence: medium}
  - {claim: "ManageEngine is the enterprise IT management division of Zoho Corp.; 60+ products; own data centres", url: "https://www.manageengine.com/about-us.html", date: 2026-10-23, confidence: high}
  - {claim: "Zoho is bootstrapped and private; ~19,000 staff; HQ Chennai (release dated 2026-02-18)", url: "https://www.manageengine.com/news/zoho-corporation-marks-30-years-now-supports-over-one-million-organisations.md", date: 2026-10-23, confidence: high}
---

# ManageEngine

> Primary category: [siem-soc](../categories/siem-soc.md).

**One-liner** — Zoho's enterprise IT-management division. In this category its product is **Log360**, a low-cost SIEM with log management, UEBA and SOAR that grew out of Windows/Active Directory auditing tools. It is usually bought by IT-led shops that want SIEM coverage without Splunk prices.

**What it does** — **Log360** packages log collection and analysis (the EventLog Analyzer heritage), Active Directory and cloud auditing, UEBA (behavioural baselines and peer grouping), threat detection (Vigil IQ), and SOAR (50+ default playbooks plus a visual builder with ITSM ticketing). ManageEngine claims 2,000+ prebuilt, cloud-delivered detection rules. AI features: **Ask Zia** answers natural-language questions over logs and alerts, **Zia Agents** are prebuilt or custom security agents, and an **MCP Server** integration connects Log360 to AI clients such as Claude or Copilot (all vendor-stated). It ships as a downloadable on-prem product and as a cloud edition.

ManageEngine sells 60+ IT-management products. The relevant neighbours are **PAM360** (privileged access), **ADAudit Plus** and **AD360** (directory auditing and identity), and **Endpoint Central** (endpoint management). This page lists only the SIEM. The other products are noted for context and are not cross-listed in the wiki.

**Naming / provenance** — The company is "ManageEngine" and the product is "Log360". Older names you will meet include EventLog Analyzer and ADAudit Plus, which Log360 bundles. The parent is **Zoho Corp.** (Chennai), the same company behind the Zoho business-apps suite. ManageEngine has been in IT management since 2002 (vendor). Its exact founding date as a separate brand is not verified.

**Ownership & viability** — Recorded as `independent`: a division of **privately held, bootstrapped Zoho Corp.** Zoho co-founder Sridhar Vembu: "Being bootstrapped, private, and built entirely in-house" (2026-02-18). Zoho has about 19,000 staff. There is no venture or PE money and no exit pressure, and the vendor is very stable. The trade-off is that ManageEngine publishes no product-level financials.

**Positioning & differentiators** —
- **Price.** The reason it gets bought. Against [splunk](splunk.md), [microsoft-sentinel](microsoft-sentinel.md) or [google-secops](google-secops.md), Log360 is licensed rather than priced on ingest volume, and runs on-prem on modest hardware. That makes cost predictable for a firm whose log volume would be expensive in Splunk.
- **Strongest on Windows and Active Directory.** Its roots are AD and Windows event auditing. That suits a Microsoft-on-prem estate and suits cloud-native or Linux-heavy estates less well.
- **In the Gartner SIEM MQ** (report dated 2025-10-08), per the vendor. The vendor does not say which quadrant. Treat it as "credible enough to be evaluated", not as a sign of leadership.
- **Has AI and MCP features.** Ask Zia and the MCP server are unusual at this price point. They are new and vendor-described, so test them in a POC.

**Who should choose them / anti-fit** — Fits a **small or mid-size fund or manager with an IT-led security function**, mostly Windows/AD, that needs compliance logging and basic detection and response (audit trails, SEC/FINRA-style retention evidence, AD change tracking) at low cost. It also fits shops that need SIEM data to stay on-prem. **Anti-fit:** a firm with a real SOC or detection-engineering team that needs scale, advanced correlation and a large detection-content ecosystem. Also a firm already paying for Microsoft E5 (Sentinel plus Defender is often cheaper incrementally), and one that wants a managed service. ManageEngine sells software, not MDR, so you supply the people or an MSSP.

**Known weaknesses / gotchas** — Many products with overlapping names and a bundled-licence structure make scoping confusing. Ask exactly which modules Log360 includes at your tier. Detection depth and scale are below the category leaders. ManageEngine on-prem products have been exploited in the wild. CVE-2022-47966, an RCE in a shared Apache xmlsec dependency affecting many ManageEngine on-prem products including AD360, was added to CISA's Known Exploited Vulnerabilities catalogue and was used by nation-state actors (CISA advisory AA23-250A, 2023-09-07). **Whether Log360 itself was in the affected list was not confirmed here.** Check the KEV catalogue and require a patch SLA. Any self-hosted SIEM is internet-adjacent infrastructure that you must patch quickly.

**Deployment & data handling** — On-prem (downloadable, Windows server) or ManageEngine's cloud edition. `data_leaves_tenancy: partial`: on-prem keeps logs in-house, the cloud edition sends them to Zoho-operated data centres (ManageEngine: "We do not use third-party data centers to run our cloud applications"). The page also says detections are "cloud-delivered", so on-prem installs presumably pull content updates. Whether **Ask Zia or Zia Agents send log data to a hosted model** is **unverified** and is the key question for an on-prem buyer.

**Integrations & partnerships** — Log ingestion from Windows, Linux, network devices, cloud (M365, AWS, Azure) and apps. Open API. ITSM integration (natively ManageEngine ServiceDesk Plus). MCP server per the vendor (`mcp_support: server`, vendor-stated, not tested).

**Compliance & FS traction** — Compliance report packs are a selling point (vendor). Named FS customers **unverified**. The Oct-2026 CTO survey (mostly hedge funds and PE) had 2 respondents in production on Log360.

**Commercial** — Quote-based, with a 30-day free trial. Licensed by devices or log sources rather than ingest volume (licence metric to confirm). Generally positioned well below Splunk and Sentinel on cost.

## Open questions

- Gartner MQ quadrant placement (vendor blog doesn't state it).
- Whether Zia AI features process data with a ManageEngine-hosted model or a third-party LLM; whether that applies to on-prem installs.
- Certifications for the cloud edition (SOC 2, ISO 27001).
- Whether Log360 (vs other ManageEngine products) was affected by CVE-2022-47966 or later KEV-listed bugs.
- Licence metric and price band.

## Sources

- [ManageEngine Log360 product page](https://www.manageengine.com/log-management/) — fetched 2026-10-23 — supports: feature set, AI/MCP features, on-prem + cloud editions, quote pricing; confidence: medium (marketing)
- [ManageEngine recognized in the 2025 Gartner MQ for SIEM (blog, 2025-11-05)](https://www.manageengine.com/blog/it-security/manageengine-recognized-in-the-2025-gartner-magic-quadrant-for-security-information-and-event-management.html) — fetched 2026-10-23 — supports: MQ inclusion (report dated 2025-10-08), 2,000+ rules; confidence: medium (vendor)
- [ManageEngine — About us](https://www.manageengine.com/about-us.html) — fetched 2026-10-23 — supports: division of Zoho Corp., 60+ products, own data centres; confidence: high
- [Zoho Corporation marks 30 years (2026-02-18)](https://www.manageengine.com/news/zoho-corporation-marks-30-years-now-supports-over-one-million-organisations.md) — fetched 2026-10-23 — supports: bootstrapped/private, ~19,000 staff, Chennai HQ, brand list; confidence: high
- [CISA AA23-250A: Multiple nation-state actors exploit CVE-2022-47966 and CVE-2022-42475 (2023-09-07)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-250a) — via search 2026-10-23 — supports: ManageEngine on-prem RCE exploited in the wild, KEV listing; confidence: high (government advisory; read via search summary)
- Cached: `raw/sources/2026-10-23--manageengine--log360-and-zoho.md`

## History

- [2026-10-23] Page created and researched. Added because of Oct-2026 CTO survey write-ins ("ManageEngine Log360", 2 in production under SIEM/Logging). Company-level slug; Log360 is the only product cross-referenced to a category.
