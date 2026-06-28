---
type: vendor
name: Rubrik
slug: rubrik
categories: [dspm]
layer: data
aliases: []
website: https://www.rubrik.com
founded: 2014
hq: Palo Alto, California, USA
ownership: public
ownership_detail: Public on NYSE (ticker RBRK) since IPO 2024-04-25 ($752M raised). Stub's "independent" corrected to "public".
ownership_confidence: high
funding_total: N/A (public; raised $752M at IPO)
last_funding: IPO 2024-04-25 (NYSE: RBRK)
deployment: [saas, on-prem]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [dspm, cyber-resilience, backup, ransomware-recovery, public-company]
---

# Rubrik

> Cyber-resilience / data-protection vendor (backup + ransomware recovery) that added DSPM via the Laminar acquisition. Category here: [[dspm]].

**One-liner** — A public data-security company best known for backup and ransomware/cyber recovery, now offering DSPM (built on acquired Laminar) to find and govern exposed sensitive data — including for AI/Copilot.

## What it does
Rubrik's core is **cyber resilience**: immutable backup, recovery, and ransomware/anomaly detection across enterprise, cloud, and SaaS (the "Data Security Cloud"). On top of that it sells **DSPM** — discovering and classifying sensitive data, scoring exposure, and flagging over-shared/over-exposed data — including a DSPM-for-Microsoft-365-Copilot offering aimed at the AI-adoption risk of copilots surfacing sensitive content. So Rubrik spans *recover-from-incidents* and *reduce-data-exposure*.

## Where it sits in the stack
Listed under [[dspm]] in the data layer, though Rubrik's center of gravity is backup/cyber-recovery, not posture management. Lethal-trifecta role: the **sensitive-data** leg (find/reduce exposed sensitive data; recover it after an incident). Adjacent to [[dlp]], [[data-access-governance]], and pure-play DSPM ([[cyera]], [[sentra]], [[bedrock-security]], [[symmetry-systems]]).

## Deployment & architecture
Hybrid: appliance/software for on-prem backup plus a SaaS control plane (Rubrik Security Cloud); DSPM (Laminar-based) is agentless cloud data scanning. Integrates with SIEM/SOC and Microsoft 365 / Copilot for the AI-exposure use case.

## Positioning & differentiators
Rubrik's edge is owning **both** the backup/recovery franchise and a data-security/DSPM story — "cyber resilience + cyber posture" in one platform — which pure DSPM vendors can't match, while pure DSPM vendors ([[cyera]], [[sentra]]) go deeper on classification/posture. Primary backup/recovery rivals are Cohesity/Veritas and Commvault (no pages). DSPM is an *adjacency* acquired via Laminar, not Rubrik's origin — weigh DSPM depth accordingly.

## Ownership, funding & M&A
**Public company — NYSE: RBRK.** IPO on 2024-04-25, a $752M upsized offering (23.5M Class A shares at $32). Founded January 2014 in Palo Alto by Bipul Sinha (CEO), Arvind Jain, Soham Mazumdar, and Arvind Nithrakashyap; subscription ARR surpassed $1B (Q3 FY2025). DSPM capability came from acquiring **Laminar** (DSPM/cloud data security), announced 2023-08-08, terms undisclosed; Rubrik DSPM GA early 2025. **The stub listed `ownership: independent` — corrected to `public`** (verified against IPO coverage and SEC filings). Ownership confidence high.

## CTO / hedge-fund lens
If a fund already runs Rubrik for backup/ransomware recovery, its DSPM is a low-friction add-on to get basic data-exposure visibility (including for Copilot) without buying a separate tool — a reasonable **Day-1 "good enough"** path. If you need best-of-breed classification/posture for a complex regulated estate, a focused DSPM ([[cyera]], [[sentra]], [[symmetry-systems]]) likely goes deeper. Backup/cyber-recovery itself is table-stakes resilience for any fund. Being a public company is a procurement/vendor-stability plus.

## Competitors / alternatives
DSPM: [[cyera]], [[sentra]], [[bigid]], [[bedrock-security]], [[symmetry-systems]], [[normalyze]], [[wiz]], [[microsoft-purview]]. Backup/resilience: Cohesity, Commvault, Veritas (no pages).

## Open questions / to verify
- Real-world depth/adoption of Rubrik DSPM (Laminar) vs. dedicated DSPM vendors.
- Latest ARR / market cap (volatile — public).
- Whether DSPM is bought standalone or only by existing backup customers.

## Sources
- [Rubrik Announces $752M Upsized IPO (Cooley)](https://www.cooley.com/news/coverage/2024/2024-04-29-rubrik-announces-$752-million-upsized-ipo) — fetched 2026-06-28 — supports: public, NYSE RBRK, IPO date/size; confidence: high.
- [Rubrik Acquires DSPM Leader Laminar (Rubrik newsroom)](https://www.rubrik.com/company/newsroom/press-releases/23/rubrik-acquires-dspm-leader-laminar-to-accelerate-cloud-data-security) — fetched 2026-06-28 — supports: DSPM via Laminar, 2023-08-08, terms undisclosed; confidence: high.
- [Rubrik DSPM for M365 Copilot (Rubrik newsroom)](https://www.rubrik.com/company/newsroom/press-releases/24/rubrik-data-security-posture-management-unblocks-ai-adoption-with-single-platform) — fetched 2026-06-28 — supports: DSPM GA early 2025, Copilot/AI use case; confidence: high.
- [Rubrik — Wikipedia](https://en.wikipedia.org/wiki/Rubrik) — fetched 2026-06-28 — supports: founded 2014, Palo Alto, founders, ARR scale; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CORRECTED ownership independent → public (NYSE: RBRK, IPO 2024-04-25, $752M). Established founded 2014 Palo Alto, core = backup/cyber-resilience, DSPM via Laminar acquisition (2023). Set ownership_confidence high, confidence high.
