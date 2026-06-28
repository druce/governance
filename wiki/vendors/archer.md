---
title: Archer
type: vendor
name: Archer
slug: archer
categories: [enterprise-grc]
layer: governance
aliases: [RSA Archer, Archer IRM, Archer Technologies]
website: "https://www.archerirm.com/"
founded: 2000
hq: Overland Park, Kansas, USA
ownership: acquired
ownership_detail: "PE-owned: acquired by Cinven (carved out of RSA Security) — announced 2023-04-13, completed 2023-07-10. Prior chain: Dell→STG (2020)→STG+Clearlake."
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, self-hosted, on-prem]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [grc, irm, risk-management, compliance]
---

# Archer

> Primary category: [enterprise-grc](../categories/enterprise-grc.md).

**One-liner** — One of the original enterprise GRC platforms (the old "RSA Archer"), now a standalone integrated-risk-management vendor owned by PE firm Cinven.

**What it does** — Archer is a configurable GRC / integrated-risk-management suite: risk register, policy & compliance management, controls assurance, audit, third-party (vendor) risk, business resiliency, and regulatory change. It is a deep, customizable system of record favored by large regulated enterprises with mature risk programs. It serves more than half of the Fortune 500.

**Where it sits in the stack** — [enterprise-grc](../categories/enterprise-grc.md), governance layer. A risk/control system of record, not a runtime data-flow control (`trifecta_relevance: none`). For AI governance it is where AI use-case risk, model inventory, and policy attestations would be tracked, overlapping [ai-governance-platform](../categories/ai-governance-platform.md) tooling.

**Deployment & architecture** — Available SaaS and self-managed/on-prem (legacy Archer deployments are frequently on-prem), highly configurable via its app-builder. Integrates with enterprise risk data sources and security tooling.

**Positioning & differentiators** — The legacy heavyweight, often compared to [servicenow](servicenow.md) GRC. Known for depth and configurability but a reputation for heavy implementation and dated UX, which is what newer entrants ([logicgate](logicgate.md), [onspring](onspring.md), [auditboard](auditboard.md)) position against.

**Ownership, funding & M&A** — `acquired` / PE-owned. Archer was part of RSA Security, which Dell sold to Symphony Technology Group (STG) in 2020; STG + Clearlake ran RSA/Archer; the Archer GRC business was carved out and sold to **Cinven** — announced 2023-04-13, completed 2023-07-10 (terms undisclosed). The seed/stub "independent" is corrected: it is an independent *company* but PE-owned, so `ownership: acquired`. (high confidence)

**CTO / hedge-fund lens** — Day-1 governance plumbing for shops that already run Archer; rarely a fresh purchase for a mid-size fund given weight and cost. Strong fit for large, heavily regulated institutions; lighter tools usually win for a 50–500-person fund.

**Competitors / alternatives** — [servicenow](servicenow.md), [logicgate](logicgate.md), [auditboard](auditboard.md), [onspring](onspring.md), [onetrust](onetrust.md).

**Open questions / to verify** — Current AI-governance feature set under Cinven ownership; SaaS vs on-prem install base mix.

## Sources
- [Cinven agrees to acquire Archer](https://www.cinven.com/news-insights/cinven-agrees-to-acquire-archer/) — fetched 2026-06-28 — supports: Cinven ownership, RSA carve-out, founded 2000, Kansas HQ, Fortune 500 base; confidence: high
- [Clearlake & STG complete sale of Archer to Cinven](https://clearlake.com/news/clearlake-and-stg-complete-sale-of-archer-to-cinven/) — fetched 2026-06-28 — supports: close date 2023-07-10, ownership chain; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected ownership independent→acquired (Cinven PE, from RSA carve-out, 2023); documented full Dell→STG→Cinven chain; confidence high.
