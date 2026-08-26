---
title: Black Duck
type: vendor
name: Black Duck Software
slug: black-duck
aka: [Synopsys Software Integrity Group, Black Duck Software Inc., Coverity, Black Duck SCA]
primary_category: software-supply-chain
also_listed_in: []
website: https://www.blackduck.com/
founded: 2002
hq: Burlington, MA, USA
ownership_state: pe-owned
owner: Clearlake Capital Group and Francisco Partners (joint)
ownership_note: Carve-out of Synopsys' Software Integrity Group. Announced 2024-05-06, closed 2024-10-01, valued at up to $2.1B (including up to $475M contingent on a specified sponsor return). The independent company took the Black Duck name at close.
acquisition: {announced: 2024-05-06, closed: 2024-10-01, price: up to $2.1B (incl. up to $475M contingent)}
funding_total: null
last_funding: null
market_position: {software-supply-chain: legacy-incumbent}
deployment_model: [saas, self-hosted, on-prem]
form_factor: [platform, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-08-26
verify_after: null
tags: [appsec, sca, sbom, open-source-license, carve-out, pe-owned]
sources:
  - {claim: "Clearlake and Francisco Partners completed the acquisition of Synopsys' Software Integrity Group on 2024-10-01, establishing it as Black Duck Software, Inc.; valued at up to $2.1B including up to $475M contingent", url: "https://www.franciscopartners.com/media/clearlake-and-francisco-partners-complete-acquisition-of-black-duck-software-formerly-known-as-synopsys-software-integrity-group", date: 2026-08-26, confidence: high}
  - {claim: "Transaction first announced 2024-05-06; Black Duck brand taken from the flagship SCA product", url: "https://www.businesswire.com/news/home/20241001535294/en/Clearlake-and-Francisco-Partners-Complete-Acquisition-of-Black-Duck-Software-Formerly-Known-as-Synopsys-Software-Integrity-Group", date: 2026-08-26, confidence: high}
---

# Black Duck

> Primary category: [software-supply-chain](../categories/software-supply-chain.md). **Ownership changed 2024-10-01** — this is no longer Synopsys.

**One-liner** — The open-source composition-analysis incumbent: Black Duck SCA plus the Coverity static analyser, carved out of Synopsys in 2024 and now a standalone PE-owned AppSec company.

**What it does** — Two flagship engines. **Black Duck SCA** inventories open-source components in a codebase and reports both security vulnerabilities and **licence obligations** — the licence-compliance half is the historical moat and the reason the product exists in legal and M&A workflows, not just security ones. **Coverity** is the static analyser (SAST). Around them sit Polaris (SaaS platform), Seeker (IAST), Defensics (protocol fuzzing) and the Black Duck Audit services business used in software due diligence during M&A.

**Naming / provenance** — Confusing lineage, worth getting right. Black Duck Software was an independent SCA company founded in 2002; **Synopsys acquired it in 2017** and folded it into its Software Integrity Group alongside Coverity (acquired 2014) and Codenomicon. In 2024 Synopsys sold that whole group, and the newly independent company **took the Black Duck name back** for the entire business. So "Black Duck" today means the former Synopsys SIG, which is much larger than the original Black Duck product.

**Ownership & viability** — `pe-owned`, jointly by **Clearlake Capital Group** and **Francisco Partners**. Announced **2024-05-06**, closed **2024-10-01**, valued at **up to $2.1B**, of which up to $475M is contingent on the sponsors hitting a specified rate of return. This is a classic sponsor carve-out: a profitable, slow-growing asset separated from a parent that wanted to focus elsewhere (Synopsys was buying Ansys). The viability question is not survival — it is investment level. Carve-outs of this shape are typically run for margin, and the AI-native competitors are moving faster.

**Positioning & differentiators** —
- **Licence compliance, not just CVEs.** Black Duck's open-source **licence** knowledge base is deeper than anyone else's and is the reason it appears in legal diligence. [snyk](snyk.md), [socket](socket.md) and [endor-labs](endor-labs.md) are security-first; Black Duck is the one lawyers ask for. This matters if the firm ships or distributes software, or is acquiring a company that does.
- **M&A software audits.** A services line no pure-play competitor has, directly relevant to a PE or credit fund diligencing a software target.
- **Deep on-prem support.** A real differentiator for firms that will not send code out.
- **Slow relative to the field.** Reachability analysis and AI-generated-code risk — the axes [endor-labs](endor-labs.md) and [socket](socket.md) compete on — are catch-up areas here.

**Who should choose them / anti-fit** — Fits a firm with **open-source licence exposure** (distributing software, or an investment firm diligencing software targets), or one requiring on-prem AppSec. **Anti-fit:** an internal-only engineering team with no distribution obligations and no diligence use case — the licence half of the value proposition is dead weight, and the security half is available cheaper and faster elsewhere.

**Known weaknesses / gotchas** — Heavy, expensive, and slower-moving than the AI-native field; false-positive volume on SCA without reachability filtering is a standing complaint. **Name collision is a real research hazard** — much published comparison content still says "Synopsys" and is describing the same product under old ownership. Carve-out integration risk: back-office separation from Synopsys was still in progress through 2025.

**Deployment & data handling** — SaaS (Polaris), self-hosted, and on-prem all supported. Whether code leaves the tenancy depends entirely on which deployment is chosen; specifics **unverified**.

**Integrations & partnerships** — CI/CD, SCM, IDE, SBOM export (SPDX/CycloneDX). Detail unverified.

**Compliance & FS traction** — Financial-services install base inherited from Synopsys is presumed large but **unverified**; no named references confirmed here.

**Commercial** — Not public. Enterprise licence, historically among the more expensive options in the category.

## Open questions

- Post-carve-out product investment: is Coverity being maintained or modernised?
- Certifications held; FedRAMP status.
- Named FS customers.
- Reachability-analysis maturity versus [endor-labs](endor-labs.md).
- Clearlake/Francisco hold thesis — margin extraction or roll-up platform?

## Sources

- [Clearlake and Francisco Partners Complete Acquisition of Black Duck Software (Francisco Partners)](https://www.franciscopartners.com/media/clearlake-and-francisco-partners-complete-acquisition-of-black-duck-software-formerly-known-as-synopsys-software-integrity-group) — fetched 2026-08-26 — supports: close date, ownership, valuation structure; confidence: high (primary)
- [Completion announcement (BusinessWire)](https://www.businesswire.com/news/home/20241001535294/en/Clearlake-and-Francisco-Partners-Complete-Acquisition-of-Black-Duck-Software-Formerly-Known-as-Synopsys-Software-Integrity-Group) — fetched 2026-08-26 — supports: announce date, brand rationale; confidence: high
- Cached: `raw/sources/2026-08-26--black-duck--synopsys-carve-out.md`

## History

- [2026-08-26] Page created via wiki-create + researched same day. Sourced from the 2026-08-25 competitor scan (Tier A, score 9); the scan's "verify current ownership" flag is resolved above.
