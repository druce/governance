---
type: vendor
name: Varonis
slug: varonis
categories: [data-access-governance, dspm, dlp]
layer: data
aliases: [Varonis Systems, VRNS]
website: https://www.varonis.com
founded: 2005
hq: Miami, Florida, US (relocated from New York, Q1 2025)
ownership: public
ownership_detail: "Publicly traded, NASDAQ: VRNS (IPO 2014-02-28). Acquired Cyral (database activity monitoring) 2025-03-17."
ownership_confidence: high
funding_total: n/a (public company)
last_funding: IPO 2014-02-28 (NASDAQ: VRNS)
deployment: [saas, self-hosted, on-prem, api]
target_customer: enterprise / regulated
hedge_fund_fit: high
priority: day-2
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [data-security-platform, dag, dspm, dlp, data-classification]
---

# Varonis

> Researched 2026-06-28. Primary category: [[data-access-governance]]; also [[dspm]] and [[dlp]].

**One-liner** — The original data-access-governance vendor: a Data Security Platform that maps who can access which sensitive files/data, flags over-permissioned and stale access, classifies the data, and watches for abnormal access across on-prem and SaaS stores.

## What it does

Varonis answers the questions that underpin data access governance: *where is our sensitive data, who can access it, who actually does, and is any of that access wrong or risky?* It crawls file shares (Windows/NAS), SharePoint/OneDrive, Microsoft 365, cloud object storage, databases, and SaaS apps; classifies content (PII, financial, regulated); maps effective permissions and group memberships; surfaces "blast radius" and over-exposed data; and runs user-behavior analytics to detect anomalous or malicious access. More recently it has pushed into DSPM (posture across cloud data stores) and added database activity monitoring via the Cyral acquisition. The platform is now sold primarily as a managed SaaS service (Varonis MDDR / SaaS), reflecting the company's pivot to a cloud-delivered, ARR model.

## Where it sits in the stack

Data layer. Primary fit is [[data-access-governance]] — the control plane for who/what can reach sensitive data — with strong overlap into [[dspm]] (data posture) and [[dlp]] (classification + egress monitoring). Lethal-trifecta role: **sensitive-data** leg. Varonis is the kind of tooling you lean on before pointing RAG/Copilot at file shares and SharePoint, because it tells you what an over-permissioned AI agent or user could actually reach. It lives in the data trust zone, governing access rather than inspecting prompts or model egress.

## Deployment & architecture

- Delivered as SaaS (cloud-hosted analysis with collectors) and historically self-hosted/on-prem for air-gapped or on-prem data stores; API-based connectors for SaaS and cloud data.
- Cyral (acquired 2025) adds agentless, "stateless interception" database activity monitoring (DAM) for cloud databases.
- Integrations: IdP/Active Directory and Entra ID (for permission and identity mapping), SIEM/SOC and SOAR, Microsoft 365 / SharePoint / OneDrive, cloud providers (AWS/Azure/GCP), and various SaaS apps. Identity-and-permission graph is the core asset.

## Positioning & differentiators

Varonis is best known for deep, accurate **permissions and access mapping over unstructured data** (file shares, SharePoint, M365) — historically its strongest moat versus posture-only DSPM startups. It bundles classification, access governance, behavior analytics, and (now) DAM into one platform, and has shifted to selling outcomes via a managed service. Versus pure-play DSPM newcomers like [[cyera]] and [[sentra]], Varonis carries deeper on-prem/unstructured-data heritage but a heavier footprint; versus identity-governance players like [[sailpoint]] and access-graph vendors like [[veza]], Varonis is data-centric (it governs access *to data*) rather than identity-lifecycle-centric. Marketing positions it as "the data security leader" — treat the leadership framing as marketing.

## Ownership, funding & M&A

- **Public.** Varonis Systems trades on NASDAQ under **VRNS**; IPO 2014-02-28. (Corrects the prior stub, which wrongly listed `ownership: independent` / confidence low.)
- Founded 2005 in New York City by Yaki Faitelson and Ohad Korkus; HQ relocated to Miami, Florida in Q1 2025 per its 2024 10-K (Wikipedia-reported; verify against filing if material).
- **M&A (verified):** acquired **Cyral**, a cloud-native database activity monitoring vendor, announced **2025-03-17** (GlobeNewswire primary release). Terms undisclosed; described as not material to current-year revenue.
- Mid-pivot from perpetual licensing to a SaaS/ARR model, targeted for completion around 2026 (reported ~$737-745M ARR target, Feb 2025 reporting — secondary, treat as indicative).

## CTO / hedge-fund lens

For a hedge fund this is **Day-1 if you are about to run RAG, Copilot, or any LLM over internal file shares / SharePoint** — you need to know what those agents can reach before you turn them loose, and Varonis is purpose-built for that "effective access to sensitive data" question. Otherwise it is a Day-2 data-governance and insider-threat investment. Not directly an SR 11-7 / model-risk tool, but its access auditing and classification are useful for data-handling compliance (SEC recordkeeping, privacy, breach-blast-radius reporting). It fits regulated, data-heavy shops; the full platform can be heavy/expensive for a very small fund, where a lighter SaaS-only DSPM may suffice.

## Competitors / alternatives

[[cyera]], [[sentra]], [[veza]], [[sailpoint]], [[netwrix]]; adjacent [[dspm]] and [[dlp]] vendors.

## Open questions / to verify

- Confirm Miami HQ relocation and exact ARR figures against the most recent 10-K / investor filings (currently secondary-sourced).
- Cyral integration status and whether DAM is GA within the platform as of 2026.
- Current pricing/packaging of the managed SaaS (MDDR) offering.

## Sources

- [Varonis Acquires Cyral to Reinvent Database Activity Monitoring (GlobeNewswire)](https://www.globenewswire.com/news-release/2025/03/17/3044111/0/en/Varonis-Acquires-Cyral-to-Reinvent-Database-Activity-Monitoring.html) — fetched 2026-06-28 — supports: public status (Nasdaq: VRNS), Cyral acquisition 2025-03-17, DAM scope; confidence: high.
- [Varonis Systems — Wikipedia](https://en.wikipedia.org/wiki/Varonis_Systems) — fetched 2026-06-28 — supports: founded 2005 (Faitelson/Korkus), IPO 2014, Miami HQ relocation, SaaS/ARR pivot; confidence: med (secondary).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected ownership from independent/low to public/high (NASDAQ: VRNS, IPO 2014). Confirmed Cyral acquisition (2025-03-17) via primary press release. Established founding (2005), founders, HQ (Miami, relocated Q1 2025), data-security-platform scope, SaaS/ARR pivot. Added dspm + dlp categories; set sensitive-data trifecta leg, hedge_fund_fit high. Cached 2 sources.
