---
type: vendor
name: Netwrix
slug: netwrix
categories: [data-access-governance, identity-governance, dlp]
layer: data
aliases: [Netwrix Corporation]
website: "https://www.netwrix.com"
founded: 2006
hq: Frisco, Texas, US
ownership: acquired
ownership_detail: "Private, PE-owned. TA Associates majority shareholder (since 2020); Centerbridge Partners strategic investor (announced 2023-09-05); Updata Partners + management minority."
ownership_confidence: high
funding_total: n/a (PE-backed, terms undisclosed)
last_funding: Centerbridge strategic investment, announced 2023-09-05 (terms undisclosed)
deployment: [self-hosted, on-prem, saas]
target_customer: mid-market / enterprise / regulated
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [data-access-governance, dag, iam, pam, identity-governance, active-directory]
---

# Netwrix

> Researched 2026-06-28. Primary category: [data-access-governance](../categories/data-access-governance.md); also [identity-governance](../categories/identity-governance.md).

**One-liner** — A data-and-identity security vendor (rooted in Active Directory auditing) that does data access governance, change/access auditing, and identity/privileged-access management for mid-market and enterprise shops, assembled largely through acquisition.

## What it does

Netwrix started as Active Directory change-auditing software and grew — by acquisition — into a broad "data and identity" security portfolio. The data-access-governance piece (largely from the Stealthbits acquisition) discovers where sensitive data lives across file shares, SharePoint, and databases; maps who can access it; flags over-exposed, stale, and risky permissions; and audits access activity for compliance and insider-threat detection. Around that it sells identity and access management (IAM/IGA), privileged access management (PAM), Active Directory security and recovery, and ransomware protection — pitched as unified visibility across data and identity.

## Where it sits in the stack

Data layer. Primary fit is [data-access-governance](../categories/data-access-governance.md) (who can reach sensitive data), with a strong second foot in [identity-governance](../categories/identity-governance.md) (IGA/PAM from the Usercube and Stealthbits lines). Lethal-trifecta role: **sensitive-data** leg — it governs and audits access to the data an AI agent or user could reach. It lives in the data/identity trust zone, not in prompt or egress inspection.

## Deployment & architecture

- Traditionally **self-hosted / on-prem** software (a fit for AD-centric, on-prem-heavy estates), with a growing SaaS/subscription delivery as part of its ARR transition.
- Connectors/collectors for Active Directory, Entra ID, file servers/NAS, SharePoint, Microsoft 365, and databases.
- Integrations: SIEM/SOC, IdP/Active Directory and Entra ID; portfolio spans DAG, IAM/IGA, PAM, and AD security/recovery (multiple acquired product lines under one partner portal).

## Positioning & differentiators

Netwrix's heritage and strongest pull is **Active Directory / Windows-estate auditing and security** for mid-market and lean-IT enterprises — strong in regulated, on-prem-heavy shops that want one vendor across data access *and* identity. It is a multi-product roll-up rather than a single unified platform, so breadth comes with some product-line seams. Versus [varonis](varonis.md), Netwrix is broader across identity/PAM but generally lighter/cheaper and less deep on large-scale unstructured-data permission analytics; versus identity-first players like [sailpoint](sailpoint.md) and [veza](veza.md), Netwrix is more AD-/audit-centric; versus DSPM pure-plays like [cyera](cyera.md) and [sentra](sentra.md), it is more on-prem and compliance-audit oriented than cloud-data-posture oriented.

## Ownership, funding & M&A

- **Private, private-equity owned.** **TA Associates** has been majority shareholder since its initial investment in **2020**. **Centerbridge Partners** made a strategic investment **announced 2023-09-05** (terms undisclosed); **Updata Partners** and management retain minority stakes. (Corrects the prior stub, which listed `ownership: independent`.) Ownership confidence high (primary Netwrix/TA press release).
- Founded 2006 by Mike Walters and Alex Vovk; HQ Frisco, Texas.
- **M&A (verified, secondary):** grew via acquisitions including **Stealthbits** (merged 2021-01-04, data security / DAG / PAM), **PolicyPak** (Oct 2021, Windows desktop management), and **Usercube** (Aug 2022, France-based IGA); plus others noted (Strongpoint, ANIXIS, New Net Technologies/NNT). Acquisition dates are Wikipedia-sourced — treat as medium confidence pending primary releases.

## CTO / hedge-fund lens

**Day-2** for most funds, and most compelling if you are an **AD-/Windows-centric, on-prem-heavy shop** that wants data access governance *and* identity/PAM auditing from one mid-market-friendly vendor. Like Varonis, it becomes more Day-1-relevant if you're about to run RAG/Copilot over file shares and SharePoint and need to know what's over-exposed first — though Varonis is the deeper tool for large unstructured-data permission analytics. Not an SR 11-7 / model-risk tool, but its access auditing supports data-handling and recordkeeping compliance. Good fit for lean IT teams; very cloud-native, SaaS-only funds may find a pure DSPM lighter.

## Competitors / alternatives

[varonis](varonis.md), [sailpoint](sailpoint.md), [veza](veza.md), [cyera](cyera.md), [sentra](sentra.md); adjacent [identity-governance](../categories/identity-governance.md) and [dlp](../categories/dlp.md) vendors.

## Open questions / to verify

- Confirm individual acquisition dates (Stealthbits, PolicyPak, Usercube, NNT) against primary press releases (currently secondary-sourced).
- Whether Centerbridge's 2023 investment changed the majority position (release states TA *remains* majority — verify no later change).
- Current SaaS vs on-prem delivery mix and packaging.

## Sources

- [Netwrix Announces Strategic Investment from Centerbridge Partners (Netwrix)](https://netwrix.com/en/resources/news/netwrix-announces-strategic-investment-from-centerbridge-partners/) — fetched 2026-06-28 — supports: TA majority (since 2020), Centerbridge investor (2023-09-05), Updata/management minority, Frisco HQ, DAG/IAM/PAM scope; confidence: high.
- [Netwrix — Wikipedia](https://en.wikipedia.org/wiki/Netwrix) — fetched 2026-06-28 — supports: founded 2006 (Walters/Vovk), acquisitions (Stealthbits 2021, PolicyPak 2021, Usercube 2022, NNT); confidence: med (secondary).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected ownership from independent/low to acquired/PE-owned/high — TA Associates majority (since 2020), Centerbridge strategic investor (2023-09-05), Updata + management minority, per primary Netwrix release. Established founding (2006, Walters/Vovk), Frisco TX HQ, DAG+IGA+PAM scope, roll-up acquisition history (Stealthbits/PolicyPak/Usercube/NNT). Added identity-governance + dlp categories; set sensitive-data trifecta leg, hedge_fund_fit medium. Cached 2 sources.
