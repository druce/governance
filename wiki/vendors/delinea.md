---
title: Delinea
type: vendor
name: Delinea
slug: delinea
aka: [Thycotic, Centrify, ThycoticCentrify, Secret Server]
primary_category: secrets-management
also_listed_in: [identity-access, non-human-identity]
website: https://delinea.com/
founded: 2021
hq: Redwood City, CA, USA
ownership_state: pe-owned
owner: TPG Capital
ownership_note: Formed April 2021 by TPG-backed merger of Thycotic (bought from Insight Partners) and Centrify (bought from Thoma Bravo in March 2021); renamed Delinea February 2022. Thoma Bravo and PSP Investments hold minority stakes.
acquisition: {announced: 2021-03, closed: 2021-04, price: null}
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
target_customer: mid-market to enterprise
last_verified: 2026-08-26
verify_after: null
tags: [pam, secrets-management, privileged-access, merger, pe-owned]
sources:
  - {claim: "Delinea formed April 2021 through the TPG-backed merger of Thycotic and Centrify; Thycotic acquired from Insight Partners, Centrify from Thoma Bravo in March 2021; Thoma Bravo and PSP Investments took minority stakes", url: "https://delinea.com/news/tpg-led-investor-group-announces-combination-thycotic-and", date: 2026-08-26, confidence: high}
  - {claim: "TPG renamed ThycoticCentrify to Delinea in February 2022", url: "https://siliconangle.com/2022/02/01/tpg-changes-thycoticcentrifys-name-delinea/", date: 2026-08-26, confidence: high}
---

# Delinea

> Primary category: [secrets-management](../categories/secrets-management.md). Also listed in [identity-access](../categories/identity-access.md) and [non-human-identity](../categories/non-human-identity.md).

**One-liner** — A privileged access management incumbent assembled from Thycotic and Centrify by TPG — the mid-market alternative to CyberArk, with credential vaulting (Secret Server) as its centre of gravity.

**What it does** — PAM in the classic sense. **Secret Server** (the Thycotic heritage) is the privileged-credential vault: discovery of privileged accounts, storage, rotation, and checkout with approval. Around it sit privileged session management and recording, endpoint privilege management (removing local admin rights while allowing specific elevated actions), and the identity-consolidation work inherited from Centrify. Increasingly marketed around **machine and non-human identities** — service accounts, workloads and now AI agents — which is why it also appears under [non-human-identity](../categories/non-human-identity.md).

**Naming / provenance — read this before searching.** Four names for one thing. **Thycotic** (Secret Server) and **Centrify** were separate PAM companies. TPG bought Thycotic from Insight Partners and Centrify from Thoma Bravo, merged them in **April 2021** as **ThycoticCentrify**, and renamed the combination **Delinea** in **February 2022**. Any comparison content, analyst note or customer reference older than 2022 will use one of the legacy names for what is now the same vendor.

**Ownership & viability** — `pe-owned` by **TPG Capital**, with **Thoma Bravo** and **PSP Investments** holding minority stakes. Five-plus years into the hold on a merged asset — late in a normal PE cycle, so a sale, recapitalisation or IPO is a reasonable expectation. Financially sound; the risks are commercial. **The specific thing to price in: merged-product estates under PE ownership reliably produce end-of-life decisions on the losing product line and renewal-price increases.** Ask directly which components are strategic and which are in maintenance before committing.

**Positioning & differentiators** —
- **Secret Server is genuinely good and genuinely established.** It is the product most mid-market firms actually deploy, and it deploys faster than [cyberark](cyberark.md).
- **On-prem is first-class**, not a legacy concession — relevant for firms that will not put a privileged-credential vault in a vendor cloud.
- **Positioned below [cyberark](cyberark.md), above [keeper](keeper.md).** More capable and more expensive than Keeper; less deep and less expensive than CyberArk. That middle slot is the whole proposition.
- **Merger integration is the standing question.** Thycotic and Centrify overlapped substantially, and a buyer should establish which code base underlies what they are being sold.

**Who should choose them / anti-fit** — Fits a **mid-size regulated firm** that needs real privileged-credential control, session recording for audit, and endpoint privilege removal, without a CyberArk-scale programme. Privileged access is a standard SEC-examination and cyber-insurance topic, so this is a defensible baseline purchase for an alternative manager. **Anti-fit:** a firm with the largest and most complex privileged estates ([cyberark](cyberark.md)); a cloud-native platform team wanting dynamic short-lived secrets ([hashicorp-vault](hashicorp-vault.md)); a small shop that only needs a vault ([keeper](keeper.md), [1password](1password.md)).

**Known weaknesses / gotchas** — Product-line overlap from the merger, and the associated end-of-life risk. PE renewal pricing. The Centrify-heritage identity components have had a less clear roadmap than the Thycotic-heritage vault. **Delinea also disclosed a security incident affecting its cloud Secret Server tenants in April 2024**, which took portals offline — old and remediated, but directly relevant history for a vendor holding privileged credentials, and worth raising in diligence.

**Deployment & data handling** — SaaS, on-prem and hybrid. For the SaaS path, key management, tenancy isolation and recovery are **unverified** and are the critical questions given what the product holds.

**Integrations & partnerships** — IdP/directory, ITSM, SIEM, DevOps and CI/CD secrets injection. MCP support unverified.

**Compliance & FS traction** — **Unverified in specifics.** Large regulated-industry base is presumed; no named FS references confirmed. Certifications not confirmed.

**Commercial** — Not public. Per-user / per-secret enterprise licensing; typically well below CyberArk.

## Open questions

- Which merged product lines are strategic and which are in maintenance mode.
- Cloud key-management and tenancy-isolation model for Secret Server Cloud; post-2024-incident changes.
- TPG hold period and exit expectations.
- Certifications held (FedRAMP status).
- Substance of the AI-agent / non-human-identity positioning versus renamed service-account management.

## Sources

- [TPG Announces merger of Thycotic and Centrify (Delinea)](https://delinea.com/news/tpg-led-investor-group-announces-combination-thycotic-and) — fetched 2026-08-26 — supports: merger, ownership, minority stakes; confidence: high (primary)
- [TPG changes ThycoticCentrify's name to Delinea (SiliconANGLE)](https://siliconangle.com/2022/02/01/tpg-changes-thycoticcentrifys-name-delinea/) — fetched 2026-08-26 — supports: rename and date; confidence: high
- Cached: `raw/sources/2026-08-26--delinea--merger-provenance-and-ownership.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Found by diffing the live SurveyMonkey instrument against the wiki.
