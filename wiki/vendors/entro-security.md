---
title: Entro Security
type: vendor
name: Entro Security
slug: entro-security
aka: []
primary_category: non-human-identity
also_listed_in: [secrets-management]
website: https://entro.security
founded: 2022
hq: Boston, Massachusetts, USA (R&D Tel Aviv)
ownership_state: acquired-closed
owner: SailPoint
ownership_note: Acquired by SailPoint (announced 2026-06-15, closed 2026-06-29); reported ~$200M (Calcalist; terms not officially disclosed). Entro brand and entro.security domain persist as a SailPoint sub-brand; sold standalone while integrating into SailPoint Agentic Fabric.
acquisition: {announced: 2026-06-15, closed: 2026-06-29, price: reported ~$200M (not officially disclosed)}
funding_total: $24M
last_funding: Series A, June 2024 ($18M, led by Dell Technologies Capital)
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise / regulated
last_verified: 2026-07-27
verify_after: 2026-10-01
tags: [non-human-identity, secrets-management, nhi, agentic, sailpoint]
---

# Entro Security

> **Now a SailPoint company** — acquired by [sailpoint](sailpoint.md) (announced 2026-06-15, closed 2026-06-29; reported ~$200M). The **Entro brand and entro.security domain are still live** (verified 2026-07-27) — this is a surviving sub-brand, not a retired one.

> **One-liner** — An agentless SaaS platform that discovers, governs, and manages the full lifecycle of non-human identities and secrets (API keys, tokens, service accounts) across cloud, SaaS, and on-prem — now the NHI/credentials layer of SailPoint's Agentic Fabric.

**Categories** — [non-human-identity](../categories/non-human-identity.md) (primary), [secrets-management](../categories/secrets-management.md)

## What it does
Entro inventories the machine identities and secrets scattered across an enterprise — API keys, OAuth tokens, certificates, service accounts — and manages them end to end: discovery, vaulting, automatic rotation, anomaly/threat detection, and decommissioning of idle or over-privileged identities. The pitch is that most organizations have thousands of unmanaged secrets with excessive permissions and no single owner; Entro maps them, scores risk, and provides real-time detection and response. It has since extended into securing AI/agent ("agentic") identities.

## Where it sits in the stack
Foundation layer. Primary home is [non-human-identity](../categories/non-human-identity.md) (the system of record and lifecycle for machine identities) with strong overlap into [secrets-management](../categories/secrets-management.md). Unlike a vault (which stores secrets), Entro focuses on *discovery, posture, and lifecycle governance* across the secrets that already exist in many vaults and platforms. It limits what credentials can reach, and prevents sensitive-data exposure by finding and rotating exposed or over-scoped secrets.

## Deployment & architecture
Agentless SaaS — connects via API/read access to cloud providers, SaaS apps, vaults, and source/CI systems rather than installing agents. Detection-and-response across on-prem, cloud, and SaaS. SOC2 and GDPR compliant per vendor.

## Positioning & differentiators
Entro is an NHI-and-secrets *governance* layer rather than a vault — it sits over existing secret stores (cloud secret managers, [hashicorp-vault](hashicorp-vault.md), [cyberark](cyberark.md)/Conjur) to give one inventory, risk posture, and automated rotation. Its nearest neighbors are [clutch-security](clutch-security.md), [token-security](token-security.md), [oasis-security](oasis-security.md), [aembit](aembit.md), and [astrix-security](astrix-security.md); vs. those it emphasizes the secrets-lifecycle (vaulting + rotation + decommissioning) angle. Differentiated from MCP-native agent brokers like [natoma](natoma.md) and [mintmcp](mintmcp.md), which govern the runtime tool call rather than the credential lifecycle.

## Ownership, funding & M&A
- **Acquired by [sailpoint](sailpoint.md).** Intent announced **2026-06-15**; deal **closed 2026-06-29** (both SailPoint press releases, high confidence). Price not officially disclosed; **~$200M reported** by Calcalist (medium confidence, single press source). Co-founders Alvas and Cheriki joined SailPoint's technology organization.
  - *Date correction (2026-07-27):* this page previously recorded the announce date as 2026-06-18. That was the **publication date of the SecurityWeek write-up**, not the announcement — SailPoint's own intent-to-acquire release is datelined **Austin, June 15, 2026**. Corrected against the acquirer's newswire release.
  - SailPoint guided the deal to close in **Q3 FY2027**; it actually closed 2026-06-29, i.e. in **Q2 FY2027** (SailPoint's fiscal year ends Jan 31) — ahead of the guided window.
- **No SEC confirmation yet.** SailPoint (CIK 0002030781) has **no filing mentioning Entro** as of 2026-07-27: the last 10-Q was filed 2026-06-10 for the quarter ended 2026-04-30 (before the announcement), and no 8-K was filed for the deal — consistent with undisclosed, immaterial terms. The **Q2 FY2027 10-Q (period ending 2026-07-31, due ~Sept 2026)** should carry the business-combination footnote and is the place to look for an official purchase price.
- **Brand survives.** entro.security still resolves 200 with no redirect and the title "Agentic AI & Non-Human Identity Security Platform | Entro Security"; the footer reads "© 2026 SailPoint Technologies, Inc." and the site carries a co-branded **SailPoint | Entro** lockup, with the privacy policy pointing at sailpoint.com. Corporate plumbing moved; the product-facing brand did not. Notably different from the absorb-and-retire pattern seen elsewhere in this space — e.g. Normalyze, where normalyze.ai now 301-redirects and the product is sold only as [proofpoint-dspm](proofpoint-dspm.md) — buyers here still shop "Entro," so it stays a distinct survey option rather than folding into the SailPoint row.
- **Integration:** Entro's NHI and credentials products are sold standalone to SailPoint customers for now, with native integration into **SailPoint Agentic Fabric** (agent/AI identity control plane) underway. Watch for roadmap/packaging changes as it's absorbed.
- **History:** Founded 2022 by Itzik Alvas (CEO) and Adam Cheriki (CTO), both Israeli IDF cyber-unit alumni. HQ Boston, MA, with R&D in Tel Aviv.
- **Funding:** $6M seed (May 2023) + $18M Series A (June 2024, led by Dell Technologies Capital) = **$24M total** pre-acquisition.
- Prior note (2026-06-28) recorded no M&A found — superseded by the June 2026 SailPoint deal.

## CTO / hedge-fund lens
Day-2. Most relevant once a fund has meaningful cloud/SaaS sprawl and is worried about ungoverned API keys and service-account credentials — a real audit and breach concern (NHI/secrets breaches rank high in IBM/Verizon data per vendor). For a small fund largely on managed cloud secret managers, this is optional until secrets sprawl becomes unmanageable. No direct SR 11-7 role, but supports access-control and operational-risk evidence. Post-acquisition, the buying question changes: if you're a SailPoint shop, Entro is now the natural NHI add-on inside a suite you already govern identities with; if you're not, weigh whether a standalone purchase survives the Agentic Fabric integration (packaging and roadmap are likely to shift toward SailPoint's platform).

## Competitors / alternatives
[clutch-security](clutch-security.md), [token-security](token-security.md), [oasis-security](oasis-security.md), [aembit](aembit.md), [astrix-security](astrix-security.md), [silverfort](silverfort.md); vaults: [hashicorp-vault](hashicorp-vault.md), [cyberark](cyberark.md), [azure-key-vault](azure-key-vault.md), [aws-secrets-manager](aws-secrets-manager.md).

## Open questions / to verify
- Current customer count / scale (only vendor-stated headcount growth found).
- Depth of agentic-AI identity capabilities vs. core NHI/secrets product.
- How long Entro remains sellable standalone vs. Agentic Fabric-only packaging; pricing changes under SailPoint.
- Official deal value (only the Calcalist ~$200M figure is public). **Next check: SailPoint's Q2 FY2027 10-Q** (period ending 2026-07-31, due ~Sept 2026) — first filing expected to carry a business-combination footnote; `verify_after: 2026-10-01` is set for this.
- Whether the Entro brand survives long-term or eventually folds into Agentic Fabric naming (as of 2026-07-27 it survives).

## Sources
- [Non-Human Identity Lifecycle Firm Entro Security Raises $18 Million](https://www.securityweek.com/non-human-identity-lifecycle-firm-entro-security-raises-18-million/) — fetched 2026-06-28 — supports: $18M Series A (Dell Tech Capital), $24M total, founders, founded, Boston HQ, product scope; confidence: high
- Web search (Crunchbase, Business Wire, Calcalist) — fetched 2026-06-28 — supports: $6M seed May 2023, founding details; confidence: med
- [SailPoint completes acquisition of Entro Security (SailPoint PR via GlobeNewswire)](https://www.globenewswire.com/news-release/2026/06/29/3318987/0/en/sailpoint-completes-acquisition-of-entro-security-to-secure-agentic-identities.html) — fetched 2026-07-09 — supports: close date 2026-06-29, Agentic Fabric integration, standalone availability, founders joining SailPoint; confidence: high (acquirer primary source); cached `raw/sources/2026-07-09--entro-security--sailpoint-close-pr.md`
- [SailPoint to Acquire Entro in Reported $200 Million Deal (SecurityWeek)](https://www.securityweek.com/sailpoint-to-acquire-entro-in-reported-200-million-deal/) — fetched 2026-07-09 — supports: ~$200M reported price (via Calcalist, not officially disclosed); confidence: med on price. **Do not use for the announce date** — the article is dated 2026-06-18 but never states when SailPoint announced; cached `raw/sources/2026-07-09--entro-security--securityweek-announce.md`
- [SailPoint Announces Intent to Acquire Entro (SailPoint PR via GlobeNewswire)](https://www.globenewswire.com/news-release/2026/06/15/3311837/0/en/sailpoint-announces-intent-to-acquire-entro-to-accelerate-and-enhance-agentic-fabric-and-secure-the-future-of-ai-driven-enterprises.html) — fetched 2026-07-27 — supports: **announce date 2026-06-15** (dateline "AUSTIN, Texas, June 15, 2026"), guided close Q3 FY2027, terms undisclosed; confidence: high (acquirer primary source); cached `raw/sources/2026-07-27--entro-security--sailpoint-announce-date-correction.md`
- SEC EDGAR — SailPoint, Inc. CIK 0002030781 (submissions JSON + full-text search) — checked 2026-07-27 — supports: **no SailPoint filing mentions Entro yet**; last 10-Q filed 2026-06-10 for period ended 2026-04-30, no deal 8-K; confidence: high; cached in the same 2026-07-27 source file
- Live-site check of https://entro.security/ — 2026-07-27 — supports: HTTP 200 no redirect, Entro-branded title, "© 2026 SailPoint Technologies, Inc." footer, SailPoint|Entro co-branded lockup; confidence: high (direct observation)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2022, Boston HQ (R&D Tel Aviv), founders Alvas/Cheriki, $24M total funding ($6M seed 2023 + $18M Series A 2024, Dell Tech Capital). No M&A — confirmed independent (high confidence). Agentless SaaS NHI + secrets-lifecycle positioning; hedge_fund_fit medium.
- [2026-07-09] Verified SailPoint acquisition (user flag): announced 2026-06-18, **closed 2026-06-29** per SailPoint PR; ~$200M reported (Calcalist). Ownership independent → acquired-closed, owner SailPoint. Founders joined SailPoint; product standalone for now, integrating into Agentic Fabric. Cached 2 sources.
- [2026-07-27] URL-audit re-verification. Confirmed `ownership_state: acquired-closed` / `owner: SailPoint` is accurate and correctly attributed (not stale from a prior status). **Corrected announce date 2026-06-18 → 2026-06-15**: the old date was SecurityWeek's publication date, whereas SailPoint's own intent PR is datelined Austin, June 15, 2026. Close date 2026-06-29 re-confirmed against the acquirer PR; price still not officially disclosed (~$200M remains Calcalist-only). Checked SEC EDGAR (CIK 0002030781) per the prefer-filings rule — **no SailPoint filing mentions Entro yet**, no deal 8-K, and the last 10-Q predates the announcement; flagged the Q2 FY2027 10-Q (~Sept 2026) as the next check and set `verify_after: 2026-10-01`. Confirmed **the Entro brand and entro.security domain persist** (HTTP 200, no redirect, Entro title, SailPoint copyright footer, SailPoint|Entro lockup) — a surviving sub-brand, unlike the absorb-and-retire pattern; `website` kept as entro.security and the survey row keeps the Entro name. Cached 1 source.
