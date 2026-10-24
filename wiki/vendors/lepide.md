---
title: Lepide
type: vendor
name: Lepide
slug: lepide
aka: [Lepide Software, Lepide Data Security Platform, Lepide Auditor]
primary_category: data-access-governance
also_listed_in: [dspm]
website: "https://www.lepide.com"
founded: 2005
hq: "Unverified: UK (Kent) per press coverage; US office Austin, Texas; Indian engineering entity (Lepide Software Pvt Ltd)"
ownership_state: independent
owner: null
ownership_note: "Private. Growth investment from Foresight Group (LSE-listed private equity manager) announced June 2024; amount and stake undisclosed, so whether Foresight holds control is unknown. Company said it was already profitable at the time."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: "Foresight Group growth investment, 2024-06 (undisclosed)"
market_position: {data-access-governance: challenger, dspm: niche-specialist}
deployment_model: [on-prem, self-hosted]
form_factor: [platform]
data_leaves_tenancy: "false"
integrations: [active-directory, entra-id, windows-file-server, microsoft-365, sharepoint, exchange, sql-server, nutanix, nasuni, microsoft-365-copilot]
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: mid-market, AD/Windows-centric estates, lean IT teams
last_verified: 2026-10-23
verify_after: null
tags: [dag, data-security-platform, active-directory-auditing, permissions-analysis, data-classification, copilot-readiness, on-prem]
sources:
  - {claim: "Foresight Group growth investment, June 2024; Kent-based; clients incl. Home Office and Deloitte; terms undisclosed", url: "https://foresight.group/news/foresight-supports-data-security-innovator-lepide-on-next-stage-of-growth", date: 2026-10-23, confidence: high}
  - {claim: "Modules (Auditor, Trust, Detect, Identify, Protect, AI); coverage of AD, Entra ID, file servers, M365, Copilot, Exchange, SharePoint, SQL, Nutanix, Nasuni", url: "https://www.lepide.com/", date: 2026-10-23, confidence: medium}
  - {claim: "Deployment on-premises, virtual and hybrid; positioning as lower-cost, faster-to-deploy Varonis alternative; 1,000+ customers", url: "https://www.lepide.com/data-security-platform/lepide-vs-varonis/", date: 2026-10-23, confidence: low}
  - {claim: "Founded 2005; Austin TX address", url: "https://www.cbinsights.com/company/lepide", date: 2026-10-23, confidence: low}
---

# Lepide

> Primary category: [data-access-governance](../categories/data-access-governance.md). Also listed in [dspm](../categories/dspm.md).

**One-liner** — A mid-market, mostly on-prem data security platform that audits Active Directory and file activity, analyses who has access to sensitive unstructured data, classifies it, and alerts on suspicious access. It competes with [varonis](varonis.md) and [netwrix](netwrix.md) on price and simplicity.

**What it does** — Lepide's Data Security Platform is a set of modules over the Microsoft-centric estate:

- **Lepide Auditor**: change and activity auditing for Active Directory, Entra ID, Exchange, file servers, SharePoint and SQL Server. This is the product's origin.
- **Lepide Trust**: permissions analysis, showing who has effective access to what, plus over-exposed and stale access.
- **Lepide Identify**: data classification of sensitive content in file stores.
- **Lepide Detect**: real-time alerting and automated response on anomalous access, such as ransomware-like mass changes.
- **Lepide Protect**: permissions remediation and management.
- **Lepide AI**: AI-assisted analytics, plus a **Microsoft 365 Copilot security** angle and a free "AI Security Readiness Assessment". This is the usual "find what Copilot could expose before you turn it on" pitch.

Coverage named on its site: AD, Entra ID, Windows file servers, Microsoft 365, M365 Copilot, Exchange, SharePoint, SQL, and the NAS/hybrid-file platforms Nutanix and Nasuni.

**Naming / provenance** — Founded 2005 per directories (CB Insights, Datanyze); not confirmed by a primary source. Started as Lepide Auditor (AD/Windows auditing) and widened into a "Data Security Platform". The respondent wrote "Lepide (lepide.com) started using early 2026 - on prem solution that can monitor on-prem...", which matches the vendor's own deployment description.

**Ownership & viability** — `independent` (private). **Foresight Group**, an LSE-listed private equity and infrastructure manager, made a **growth investment announced June 2024**. Amount and stake are undisclosed, so this page does not classify Lepide as `pe-owned`. The CEO said at the time that Lepide was "already profitable". Scale is modest: press in 2024 cited 80+ staff across the UK, US and India. Aggregator figures (~$20M revenue, ~190 staff, $4.8M–$10.5M total funding) conflict and are low confidence. **Acquisition-risk note:** a profitable, PE-backed mid-market data-security vendor is a natural tuck-in for a larger identity or data-security roll-up. Netwrix itself was assembled that way. If that happens, on-prem continuity and licence terms are the things to protect contractually.

**Positioning & differentiators** —
- **Versus [varonis](varonis.md):** Lepide markets itself explicitly as a cheaper, faster-to-deploy Varonis alternative ("straightforward licensing", "auditing began on day one"). That is vendor marketing. The structural point holds, though: Varonis has moved to a cloud-delivered SaaS model, while Lepide remains an **on-prem / self-hosted** product. For a firm that wants the software inside its own estate, that is a real difference. Varonis remains deeper on large-scale permission analytics and behavioural detection.
- **Versus [netwrix](netwrix.md):** the closest like-for-like peer. Both started in AD auditing and target the same mid-market Windows shop. Netwrix is larger and broader (IGA, PAM, via acquisitions); Lepide is smaller and narrower, focused on data plus AD.
- **Versus cloud-first DSPM ([cyera](cyera.md), [sentra](sentra.md)) and [microsoft-purview](microsoft-purview.md):** Lepide's centre of gravity is on-prem file servers and AD. It is a weak fit for cloud data warehouses and SaaS-native data. Purview's classification is stronger inside M365, but Purview does little for on-prem NAS permission auditing.
- **Survey signal:** two respondents in production (DSPM and DAG), one of whom started in early 2026. Small numbers, but Lepide was not previously in the wiki at all.

**Who should choose them / anti-fit** — Fits a **small or mid-sized fund with significant on-prem Windows file servers / NAS and Active Directory**, a lean IT team, and a preference for running security tooling inside its own environment. It is particularly relevant as a pre-Copilot clean-up of over-permissioned shares. **Anti-fit:** a cloud-native, SaaS-first firm with little on-prem data (a cloud DSPM or Purview covers it better). The same goes for a large enterprise that needs Varonis-scale analytics with a managed detection service behind it, or anyone who wants a vendor-hosted SaaS with no servers to run.

**Known weaknesses / gotchas** — Small vendor with limited independent analyst coverage found on this pass. Comparative claims against Varonis come from Lepide's own comparison page. Customer logos (Deloitte, KPMG, Pfizer, NHS, Clifford Chance) are logos, not case studies. Cloud and SaaS coverage beyond Microsoft (Google Workspace, Box, Dropbox, AWS data stores) is unverified. Being on-prem, you own the servers, upgrades and collector health.

**Deployment & data handling** — **On-prem / self-hosted**: deployed into the customer's environment directly or as one of Lepide's pre-built virtual machines; the vendor also describes "hybrid" coverage of on-prem and cloud repositories. No vendor-hosted SaaS was confirmed. Because the software runs in-house, audit data and classification results **stay in the customer's environment** by design (`data_leaves_tenancy: false`). Whether Lepide AI features call an external model service, and what telemetry returns to the vendor, are unverified. Out-of-band (log/event collection and scanning), not inline.

**Integrations & partnerships** — Microsoft Gold partner badge (vendor-displayed). Native coverage as listed above. SIEM export and ticketing integrations are likely for this product class but were not verified. MCP support unverified (none found).

**Compliance & FS traction** — **Unverified.** No named financial-services customer found; no certifications confirmed. For an on-prem product, vendor SOC 2 matters less than for SaaS, but software supply-chain assurances and secure update practices still do. The survey evidence (two hedge-fund/PE respondents in production) is the strongest FS signal available.

**Commercial** — Not public. Vendor describes licensing as "straightforward". Likely per-user or per-object, but unverified.

## Open questions

- Foresight's stake: minority or control? If control, change `ownership_state` to `pe-owned`.
- Primary-source founding year and legal HQ (UK vs US vs India entity structure).
- Whether a vendor-hosted SaaS edition exists, and what Lepide AI sends off-box.
- Supported repositories beyond the Microsoft/NAS estate.
- Certifications; named FS customers; SIEM integrations.
- Pricing model and band.

## Sources

- [Foresight supports data security innovator Lepide on next stage of growth (Foresight Group)](https://foresight.group/news/foresight-supports-data-security-innovator-lepide-on-next-stage-of-growth) — fetched 2026-10-23 — supports: June 2024 growth investment, Kent base, client examples; confidence: high (primary, investor)
- [Lepide homepage (Lepide)](https://www.lepide.com/) — fetched 2026-10-23 — supports: module list, coverage, Copilot readiness positioning; confidence: medium (vendor marketing)
- [Lepide vs Varonis (Lepide)](https://www.lepide.com/data-security-platform/lepide-vs-varonis/) — fetched 2026-10-23 — supports: on-prem/virtual/hybrid deployment, comparative positioning, 1,000+ customers claim; confidence: low (vendor comparison marketing)
- [Lepide company profile (CB Insights)](https://www.cbinsights.com/company/lepide) — fetched via search 2026-10-23 — supports: founded 2005, Austin address; confidence: low (aggregator)
- Cached: `raw/sources/2026-10-23--lepide--foresight-investment.md`, `raw/sources/2026-10-23--lepide--platform-and-vs-varonis.md`

## History

- [2026-10-23] Page created via wiki-create and researched the same day. Triggered by two in-production write-ins (DSPM, DAG) in the October 2026 CTO survey. Primary set to data-access-governance (AD/file auditing and permission analysis is the core, the Netwrix/Varonis shape); DSPM cross-listed for Lepide Identify classification. Ownership recorded as independent because Foresight's stake is undisclosed.
