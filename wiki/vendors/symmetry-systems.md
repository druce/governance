---
type: vendor
name: Symmetry Systems
slug: symmetry-systems
categories: [dspm, data-access-governance]
layer: data
aliases: []
website: https://www.symmetry-systems.com
founded: 2021
hq: San Jose, California, USA
ownership: acquired
ownership_detail: "Acquired by Zscaler — announced 2026-05-21, terms undisclosed, close expected days after announcement (Access Graph for AI-agent identity/data mapping). Prior: VC-backed, $17.7M inside round 2023 (ForgePoint + Prefix)."
ownership_confidence: high
funding_total: ~$33M (approx; disclosed rounds)
last_funding: $17.7M inside round (2023-08-09, ForgePoint Capital + Prefix Capital)
deployment: [saas, self-hosted, on-prem]
target_customer: enterprise / regulated
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [dspm, data-access-governance, identity-graph, darpa]
---

# Symmetry Systems

> Data+AI security posture platform that fuses the data estate with the full identity graph. Primary category: [dspm](../categories/dspm.md); also [data-access-governance](../categories/data-access-governance.md).

**One-liner** — A DSPM platform that maps sensitive data to *who can reach it* — humans, service accounts, AI agents, third parties — and can automatically remediate over-permissioned or misconfigured access.

## What it does
Symmetry discovers and classifies sensitive data across clouds, SaaS, on-prem, legacy, and air-gapped stores, then joins that data map to a complete **identity graph** so you see not just what is exposed but exactly which identity could reach it and what they could do. **DataGuard** delivers the DSPM/data-access-governance view; **DataEnforce** acts on it — auto-remediating misconfigurations, revoking excess permissions, and enforcing policy without requiring a separate DLP or PAM tool. Increasingly positioned around exposure at the intersection of data and *agentic* identities.

## Where it sits in the stack
Data layer — primary [dspm](../categories/dspm.md), secondary [data-access-governance](../categories/data-access-governance.md). Lethal-trifecta role: the **sensitive-data** leg — reduce blast radius by knowing and shrinking who/what can reach sensitive data, including AI agents. Adjacent to [dlp](../categories/dlp.md) and identity tooling ([veza](veza.md), [sailpoint](sailpoint.md)).

## Deployment & architecture
Flexible deployment — managed SaaS, customer-hosted, cloud, on-prem, legacy, and air-gapped — which is unusual in DSPM and matters for regulated/isolated environments. Builds an identity-to-data graph rather than only tagging data at rest. Included as a Representative Vendor in the 2025 Gartner Market Guide for DSPM.

## Positioning & differentiators
Differentiator is the **identity-graph fusion** (data + identities + actions) and the active-remediation angle (DataEnforce), plus broad deployment reach including air-gapped. Origin: DARPA-funded research at UT Austin. Competes with [cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [bedrock-security](bedrock-security.md), [normalyze](normalyze.md), [concentric-ai](concentric-ai.md), and [varonis](varonis.md) on the access-aware DSPM edge. Smaller/quieter than the best-funded DSPM players, so vendor-scale risk applies.

## Ownership, funding & M&A
**Acquired by [zscaler](zscaler.md)** — announced 2026-05-21 (terms undisclosed; Zscaler folds Symmetry's Data Access Graph into its Zero Trust platform to map/secure AI-agent identity↔data flows; close expected shortly after announcement). Prior funding: ~$15M Series A (2022) + $17.7M inside round (2023-08-09, ForgePoint + Prefix, W11, TSG) — ~$33M total (approximate). The seed had no M&A flag and an earlier research pass wrongly recorded it as independent; corrected via the Zscaler/Symmetry primary announcements. See [ai-security-m-and-a-map](../comparisons/ai-security-m-and-a-map.md).

## CTO / hedge-fund lens
DSPM is **Day-1** for AI on internal data; Symmetry's identity-aware cut is appealing where the real question is "which account or agent could exfiltrate this." The flexible/air-gapped deployment suits funds unwilling to send sensitive data to a cloud scanner. Indirect SR 11-7 relevance (governs data feeding models). Weigh its smaller scale against bigger DSPM vendors; good shortlist candidate where identity-to-data lineage and on-prem/air-gapped coverage are priorities.

## Competitors / alternatives
[cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [bedrock-security](bedrock-security.md), [normalyze](normalyze.md), [concentric-ai](concentric-ai.md), [varonis](varonis.md), [microsoft-purview](microsoft-purview.md), [wiz](wiz.md).

## Open questions / to verify
- Precise total funding and any round since the 2023 inside round.
- Current customer scale / traction relative to Cyera/Sentra.
- How much of DataEnforce auto-remediation customers actually run in enforce (vs. observe) mode.

## Sources
- [Symmetry Systems Closes $17.7M (Symmetry newsroom)](https://www.symmetry-systems.com/news/symmetry-systems-closes-17-7-million-to-scale-its-ai-powered-data-security-platform/) — fetched 2026-06-28 — supports: $17.7M round, investors, date, product (DataGuard/DataEnforce), deployment; confidence: high.
- [Symmetry Systems Raises $17.7M (SecurityWeek)](https://www.securityweek.com/symmetry-systems-raises-17-7m-for-data-security-posture-management-platform/) — fetched 2026-06-28 — supports: round + DSPM positioning, DARPA/UT Austin origin; confidence: med.
- [Symmetry Systems — About](https://www.symmetry-systems.com/about/) — fetched 2026-06-28 — supports: HQ San Jose, identity-graph positioning; confidence: med (vendor).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent (private), San Jose, DARPA/UT-Austin origin, ~$33M raised incl. $17.7M (2023). Product = DataGuard (DSPM) + DataEnforce (remediation), identity-graph differentiator. No M&A. Set ownership_confidence high.

- [2026-06-28] CORRECTION (lint cross-check): ownership independent→acquired. Zscaler acquisition confirmed (announced 2026-05-21); earlier research missed it. Source cached.
