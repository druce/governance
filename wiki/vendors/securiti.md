---
title: Securiti
type: vendor
name: Securiti
slug: securiti
categories: [dspm, ai-governance-platform, data-access-governance]
layer: data
aliases: [Securiti AI, Securiti.ai]
website: "https://securiti.ai"
founded: 2019
hq: San Jose, CA, USA
ownership: subsidiary
ownership_detail: Acquired by Veeam Software for $1.725B; announced 2025-10-21, completed 2025-12-11. CEO Rehan Jalil became Veeam President of Security and AI.
ownership_confidence: high
funding_total: ~$156M (pre-acquisition)
last_funding: $75M Series C (2022); acquired by Veeam 2025-12-11
deployment: [saas, self-hosted]
target_customer: large enterprise, regulated (privacy/compliance heavy)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [dspm, privacy, ai-governance, data-access-governance, veeam, acquired]
---

# Securiti

> **One-liner** — A broad "Data Command Center" — DSPM, privacy, data governance, data access, and AI trust on one knowledge-graph platform — now owned by backup/data-resilience giant Veeam.

**What it does** — Securiti unifies data intelligence and controls across hybrid, multicloud, and SaaS via a knowledge-graph "Data Command Center": DSPM (discover/classify/secure sensitive data), PrivacyOps (DSARs, consent, regulatory compliance), data access governance, and **AI trust/AI governance** — including safe enterprise AI search and guardrails for building gen-AI on enterprise data. It's one of the broader platforms in the category, spanning data security *and* privacy/governance *and* AI governance rather than DSPM alone.

**Where it sits in the stack** — Primary: [dspm](../categories/dspm.md); also [ai-governance-platform](../categories/ai-governance-platform.md) and [data-access-governance](../categories/data-access-governance.md). Data layer (with a foot in governance). Lethal-trifecta role: the **sensitive-data** leg (classify/constrain) plus **egress** controls around AI use of data. Trust zones: governs the data plane and the AI-governance overlay on top of it.

**Deployment & architecture** — SaaS and self-hosted options; knowledge-graph engine connecting structured/unstructured stores across hybrid, multicloud, and SaaS. Modules for DSPM, privacy, governance, data access, and "Gencore AI" (safe gen-AI pipelines). Integrates with IAM, DLP, and cloud platforms. Expect deeper integration with Veeam's data-resilience/backup estate going forward.

**Positioning & differentiators** — Known for breadth (data security + privacy + AI governance in one) and its knowledge-graph approach; strong in privacy/regulatory-heavy buyers — closest in spirit to [bigid](bigid.md) (broad data-governance/privacy platform) rather than the lean agentless DSPMs [cyera](cyera.md)/[sentra](sentra.md). Differentiator now is the Veeam tie-up: pairing DSPM/governance with the market-leading backup/data-resilience footprint (82% of the Fortune 500). Microsoft Purview competes on the data-security side but Securiti reaches well beyond the Microsoft estate.

**Ownership, funding & M&A** — **Acquired — subsidiary of Veeam Software.** Founded **2019** by Rehan Jalil (CEO; prior: Elastica, sold to Symantec); HQ San Jose, CA. Raised ~**$156M** pre-acquisition (Series A $31M 2019, B $50M 2020, C $75M 2022; backers General Catalyst, Mayfield, Capital One Ventures). **Veeam agreed to acquire Securiti for $1.725B (announced 2025-10-21) and completed the deal 2025-12-11**; ~600 employees joined Veeam and Rehan Jalil became Veeam's President of Security and AI. Verified against Veeam's own press release + Bloomberg. **Note:** the seed registry carried *no* M&A flag for Securiti, but the acquisition is confirmed by primary source. Ownership confidence: high.

**CTO / hedge-fund lens** — **Day-1**-relevant if you want one platform spanning data security *and* privacy/regulatory *and* AI governance — useful for a regulated fund that values consolidation. The Veeam acquisition is double-edged: more durable backing and integration with data-resilience, but watch for roadmap/pricing/packaging shifts as it folds into Veeam's stack through 2026. SR 11-7: its AI-governance module is directly relevant to model-risk/compliance evidence. If you only need fast cloud DSPM, lighter tools ([cyera](cyera.md)/[sentra](sentra.md)) may fit better; if you want breadth, Securiti and [bigid](bigid.md) are the comparison.

**Competitors / alternatives** — [bigid](bigid.md), [cyera](cyera.md), [sentra](sentra.md), [concentric-ai](concentric-ai.md), [microsoft-purview](microsoft-purview.md), [collibra](collibra.md), [immuta](immuta.md), OneTrust.

**Open questions / to verify**
- How Securiti is packaged/priced and roadmapped under Veeam through 2026 (standalone vs bundled).
- Whether the AI-governance module is retained/expanded or refocused post-acquisition.

## Sources
- [Veeam Completes Acquisition of Securiti AI (Veeam press release, 2025-12-11)](https://www.veeam.com/company/press-release/veeam-acquires-securiti-ai.html) + [Veeam to Acquire Securiti AI (announcement, 2025-10-21)](https://www.veeam.com/company/press-release/veeam-to-acquire-securiti-ai.html) — fetched 2026-06-28 — supports: $1.725B acquisition, announce/close dates, what Securiti does, founding/HQ/funding; confidence: high (primary).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; founded 2019, San Jose, broad DSPM + privacy + AI-governance "Data Command Center." Confirmed acquisition by Veeam ($1.725B, announced 2025-10-21, completed 2025-12-11) via Veeam primary source — seed had NO M&A flag. Set ownership=subsidiary, confidence high. Added data-access-governance tag.
