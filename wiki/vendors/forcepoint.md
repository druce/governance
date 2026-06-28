---
type: vendor
name: Forcepoint
slug: forcepoint
categories: [network-security-sase, dlp]
layer: foundation
aliases: [Websense, Raytheon Forcepoint, Forcepoint Commercial]
website: https://www.forcepoint.com
founded: 2016
hq: Austin, Texas, USA
ownership: acquired
ownership_detail: "Commercial Forcepoint (DLP / Data-first SASE) owned by Francisco Partners (PE) since 2021; ownership retained in 2023 when TPG bought the separate G2CI public-sector unit (closed 2023-10-02). Verified 2026-06-28"
ownership_confidence: high
funding_total: n/a (PE-owned)
last_funding: "Acquired by Francisco Partners from Raytheon (2021); G2CI split off to TPG (2023)"
deployment: [saas, inline-proxy, api, on-prem, self-hosted]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [dlp, sase, sse, data-first-sase, private-equity]
---

# Forcepoint

> Long-standing data-protection / DLP vendor, now positioned around "Data-first SASE";
> the commercial business is owned by private-equity firm Francisco Partners.

**One-liner** — Forcepoint is the veteran DLP / data-security vendor (ex-Websense,
ex-Raytheon) that wraps data classification and DLP into a cloud-delivered SASE platform;
its commercial arm is owned by Francisco Partners.

**Categories** — [[network-security-sase]] (primary), [[dlp]]

## What it does
Forcepoint's core is data security — enterprise DLP across endpoint, network, cloud, email
and web — extended into a "Data-first SASE" platform (SWG, CASB, ZTNA) so policy follows
the data wherever it goes. It also offers data classification/DSPM-style discovery and risk-
adaptive protection that adjusts enforcement to user behavior. For AI, the relevant angle is
its DLP heritage: classifying and blocking sensitive data before it leaves to cloud or AI apps.

## Where it sits in the stack
Foundation-layer [[network-security-sase]] with a strong [[dlp]] role. On the lethal
trifecta it addresses the **sensitive-data** leg (classification + DLP) and the **egress**
leg (controlling data flow to cloud/AI destinations). Data-control layer, not a model guardrail.

## Deployment & architecture
Mixed: cloud-delivered SASE/SSE plus mature on-prem and endpoint DLP agents (a longer
on-prem/self-hosted heritage than cloud-native peers). Inline proxy for web/CASB, API for
SaaS, endpoint agents for data-in-use. Integrations: IdP, SIEM, classification engines.
AI-specific access-governance features are less prominently marketed than [[zscaler]] /
[[netskope]]; its pitch is data protection that incidentally covers AI egress.

## Positioning & differentiators
Known for deep, enterprise-grade DLP and data classification — often chosen by data-
protection-led and regulated/government-adjacent buyers. Differs from [[zscaler]] /
[[netskope]] by leading with data security rather than network scale. Nearest neighbors:
[[zscaler]], [[netskope]], [[palo-alto-networks]], [[cisco]], [[cato-networks]]. As a PE-
owned business it is less in the public eye than its newly/long-public rivals.

## Ownership, funding & M&A
The seed flagged ownership as uncertain. **Verified (2026-06-28):** ownership lineage is
Websense → Raytheon (formed "Forcepoint" in 2016 from Websense + Raytheon Cyber Products +
Stonesoft) → **Francisco Partners acquired Forcepoint from Raytheon in 2021** → in 2023 the
business was split: **TPG (via TPG Capital) acquired the Global Governments & Critical
Infrastructure (G2CI) public-sector unit for ~$2.45B, closing 2023-10-02**, while the
**commercial Forcepoint business (DLP / Data-first SASE) continues to be owned by Francisco
Partners** and co-investors (FP also kept a minority stake in the spun-out G2CI). So the
commercial DLP/SASE Forcepoint that an enterprise buyer shops for is **Francisco Partners-
owned private equity** — confidence high. (No single public acquirer of the whole entity;
the G2CI/Commercial split is the nuance.)

## CTO / hedge-fund lens
Day-1 if data protection / DLP is your driving requirement (preventing sensitive or
regulated data from leaving, including into AI prompts and unsanctioned SaaS) and you want
it bundled with SASE. Its DLP depth and classification suit compliance-heavy shops. As a
PE-owned vendor, weigh roadmap/independence considerations vs the publicly-traded
[[zscaler]]/[[netskope]]. No SR 11-7 / model-risk role; this is data-egress control. For a
small fund, full Forcepoint DLP+SASE may be more than needed.

## Competitors / alternatives
[[zscaler]], [[netskope]], [[palo-alto-networks]], [[cisco]], [[cato-networks]].

## Open questions / to verify
- Current product depth of Forcepoint's AI-specific access governance vs DLP-by-proxy.
- Any change of ownership / sale of the commercial business since 2023 (none found as of 2026-06-28).
- Strength of its DSPM/data-classification vs [[dspm]] specialists.

## Sources
- [TPG Completes Acquisition of Forcepoint G2CI from Francisco Partners — Forcepoint newsroom](https://www.forcepoint.com/newsroom/2023/tpg-completes-acquisition-forcepoint-global-governments-and-critical-infrastructure) — fetched 2026-06-28 — supports: 2023-10-02 G2CI sale to TPG; Francisco Partners retains commercial business; confidence: high.
- [TPG to buy Forcepoint public-sector business for $2.45B — Cybersecurity Dive](https://www.cybersecuritydive.com/news/tpg-acquires-forcepoint/686007/) — fetched 2026-06-28 (search) — supports: ~$2.45B deal value; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; VERIFIED ownership — commercial Forcepoint (DLP/SASE) owned by Francisco Partners (PE) since 2021; TPG acquired only the G2CI public-sector unit (closed 2023-10-02, ~$2.45B). Set ownership: acquired / Francisco Partners (high). Founded 2016, Austin TX. Source cached.
