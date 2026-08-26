---
title: BeyondTrust
type: vendor
name: BeyondTrust
slug: beyondtrust
aka: [Beyond Trust, Bomgar, Password Safe, Remote Support]
primary_category: secrets-management
also_listed_in: [identity-access]
website: https://www.beyondtrust.com/
founded: 1985
hq: Johns Creek, GA, USA
ownership_state: pe-owned
owner: Francisco Partners (majority), Clearlake Capital (minority)
ownership_note: Francisco Partners acquired BeyondTrust in 2018; Clearlake Capital's minority investment closed August 2021. Francisco Partners has been reported exploring a multi-billion-dollar sale; ~$500M ARR cited. No transaction announced as of 2026-08-26.
acquisition: {announced: 2021-06, closed: 2021-08, price: null}
funding_total: null
last_funding: null
market_position: {secrets-management: legacy-incumbent}
deployment_model: [saas, on-prem, hybrid]
form_factor: [platform, agent]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-08-26
verify_after: 2027-02-26
tags: [pam, privileged-access, remote-support, password-safe, pe-owned, sale-rumored]
sources:
  - {claim: "Francisco Partners acquired BeyondTrust in 2018 and holds the majority; Clearlake Capital's investment closed August 2021 as a minority position", url: "https://www.beyondtrust.com/press/beyondtrust-completes-transaction-with-clearlake-capital-and-francisco-partners", date: 2026-08-26, confidence: high}
  - {claim: "Francisco Partners exploring a multi-billion-dollar sale of BeyondTrust; ~$500M annual recurring revenue", url: "https://www.privateequitywire.co.uk/francisco-partners-weighs-multi-billion-dollar-sale-of-cybersecurity-firm-beyondtrust/", date: 2026-08-26, confidence: medium}
  - {claim: "Leader in the 2025 Gartner Magic Quadrant for Privileged Access Management; Overall Leader in the 2026 KuppingerCole Leadership Compass for PAM, its sixth consecutive year", url: "https://checkthat.ai/brands/beyondtrust", date: 2026-08-26, confidence: low}
---

# BeyondTrust

> Primary category: [secrets-management](../categories/secrets-management.md). Also listed in [identity-access](../categories/identity-access.md).

**One-liner** — A top-tier privileged access management vendor — credential vaulting, privileged remote access and endpoint privilege management — consistently ranked alongside CyberArk and Delinea, and reportedly up for sale.

**What it does** — Three product lines. **Password Safe** is the privileged-credential vault with discovery, rotation, session management and recording. **Privileged Remote Access** (the Bomgar heritage) brokers vendor and administrator access to internal systems without VPN or shared credentials — genuinely strong, and the piece most directly relevant to a firm managing third-party administrator access to its trading and back-office systems. **Endpoint Privilege Management** removes standing local admin rights while permitting specific elevated actions. Newer work sits under identity-security posture: finding the privileged paths and standing entitlements that exist across an estate.

**Naming / provenance** — Long and tangled: the current company is the result of Bomgar (backed by Francisco Partners) acquiring BeyondTrust in 2018 and adopting the BeyondTrust name; earlier lineage runs through Symark and eEye Digital Security. Founding dates cited for it range from 1985 onward depending on which predecessor is counted — treat the founding year on this page as approximate.

**Ownership & viability** — `pe-owned`. **Francisco Partners** has held the majority since **2018**; **Clearlake Capital** took a minority position closing **August 2021**. **The live issue: Francisco Partners has been reported to be exploring a multi-billion-dollar sale**, with roughly **$500M ARR** cited. No transaction has been announced as of 2026-08-26. Eight years is a long PE hold, so a sale is more likely than not — and for a product line that holds a firm's privileged credentials, an ownership change is a genuine planning input, not gossip. `verify_after: 2027-02-26`.

**Positioning & differentiators** —
- **Privileged Remote Access is the standout.** Brokering third-party and vendor administrator access with full session recording is a specific, well-executed capability, and vendor access is a recurring finding in financial-services examinations and a repeated root cause in real breaches.
- **Analyst standing is genuinely top-tier** — Leader in the 2025 Gartner MQ for PAM, and Overall Leader in the 2026 KuppingerCole Leadership Compass for a sixth consecutive year. Among the strongest independent validation of any vendor in this category. (Sourced here via a secondary aggregator, not the reports themselves — see confidence note.)
- **Versus [cyberark](cyberark.md):** the closest peer. CyberArk is broader in identity security overall; BeyondTrust is at least its equal on remote/vendor privileged access.
- **Versus [delinea](delinea.md):** similar tier, similar PE dynamics. Delinea leans mid-market via Secret Server; BeyondTrust leans enterprise.

**Who should choose them / anti-fit** — Fits an **enterprise-scale firm with substantial third-party administrator access** — outsourced IT, managed service providers, fund-administration and market-data vendors touching internal systems. That describes a great many alternative managers, and it is the clearest reason for this page. **Anti-fit:** a small firm that needs a vault and nothing more ([keeper](keeper.md), [1password](1password.md)); a cloud-native platform team ([hashicorp-vault](hashicorp-vault.md)).

**Known weaknesses / gotchas** — Sale overhang per above. Deployment weight and cost are enterprise-grade. **Most important history: in December 2024 BeyondTrust disclosed a compromise of its Remote Support SaaS instances via a stolen API key, an incident that was subsequently linked publicly to intrusions at the US Treasury Department.** For a vendor whose product is privileged remote access, this is material and must be raised explicitly in diligence — what changed, and what the current key-management and tenancy-isolation model is.

**Deployment & data handling** — SaaS, on-prem and hybrid; on-prem remains fully supported and is the conservative choice for the vault given the incident above. SaaS key-management and isolation specifics are **unverified**.

**Integrations & partnerships** — IdP/directory, ITSM, SIEM, vulnerability management. MCP support unverified.

**Compliance & FS traction** — **Unverified in specifics.** Large regulated-industry install base including financial services is presumed; no named references confirmed. Certifications not confirmed here.

**Commercial** — Not public. Enterprise licensing by user/asset; among the more expensive options in the category.

## Open questions

- **Sale status** — recheck by 2027-02-26.
- Post-December-2024 changes to SaaS key management, tenancy isolation and monitoring for Remote Support.
- Verify the Gartner and KuppingerCole placements against the reports directly rather than the aggregator cited here.
- Certifications held (FedRAMP status).
- Named FS customers.

## Sources

- [BeyondTrust Completes Transaction with Clearlake Capital and Francisco Partners (BeyondTrust)](https://www.beyondtrust.com/press/beyondtrust-completes-transaction-with-clearlake-capital-and-francisco-partners) — fetched 2026-08-26 — supports: ownership structure and dates; confidence: high (primary)
- [Francisco Partners weighs multi-billion dollar sale of BeyondTrust (Private Equity Wire)](https://www.privateequitywire.co.uk/francisco-partners-weighs-multi-billion-dollar-sale-of-cybersecurity-firm-beyondtrust/) — fetched 2026-08-26 — supports: reported sale process, ARR scale; confidence: medium
- [BeyondTrust profile (checkthat.ai)](https://checkthat.ai/brands/beyondtrust) — fetched 2026-08-26 — supports: analyst placements; confidence: low (aggregator restating analyst reports; verify against the primary reports)
- Cached: `raw/sources/2026-08-26--beyondtrust--ownership-and-sale-process.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
