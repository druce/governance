---
type: vendor
name: 7AI
slug: 7ai
categories: [ai-soc-analysts]
layer: foundation
aliases: [7 AI, Seven AI]
website: "https://7ai.com"
founded: 2024
hq: Boston, MA, USA
ownership: independent
ownership_detail: VC-backed; $130M Series A led by Index Ventures (2025-12) at ~$700M valuation. ~$166M total raised.
ownership_confidence: high
funding_total: ~$166M
last_funding: Series A $130M (2025-12, Index Ventures)
deployment: [saas]
target_customer: Fortune 500 / large enterprise (finance, retail, tech, healthcare)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [agentic-soc, ai-soc, alert-triage, cybereason-founders]
---

# 7AI

**One-liner** — A "dynamic agentic security" platform from the Cybereason founders that runs swarms of autonomous AI agents to investigate security alerts at enterprise scale.

**What it does** — 7AI deploys autonomous AI security agents that pick up alerts, investigate them, and close out the triage/investigation work that normally consumes a SOC. The company reports its agents have processed 2.5M+ alerts and completed 650,000+ investigations, cutting investigation time from hours to minutes and removing 95–99% of false positives (vendor metrics — marketing). It's pitched as end-to-end autonomous SOC operations rather than a single co-pilot.

**Where it sits in the stack** — [ai-soc-analysts](../categories/ai-soc-analysts.md), Foundation layer; an autonomous automation layer over [siem-soc](../categories/siem-soc.md) and [edr-xdr](../categories/edr-xdr.md). SOC-ops tooling, not an AI-application guardrail — trifecta_relevance: none. Trusted security-ops zone.

**Deployment & architecture** — SaaS. Two offerings: the **7AI Platform** (self-serve/independent deployment) and **7AI Platform + PLAID** ("People-Led, AI-Driven"), a white-glove model with expert customization — i.e., closer to a managed-service wrap. Named customer DXC Technology reportedly deployed in ~8 weeks.

**Positioning & differentiators** — Founded 2024 by Lior Div (CEO, ex-Cybereason CEO) and Yonatan Striem-Amit (ex-Cybereason CTO); launched from stealth Feb 2025. The pedigree and the record-setting raise are the headline differentiators; it leans hard on "agentic"/swarm framing and raw investigation throughput. Nearest neighbors: [prophet-security](prophet-security.md), [dropzone-ai](dropzone-ai.md), [radiant-security](radiant-security.md), [simbian](simbian.md), [torq](torq.md).

**Ownership, funding & M&A** — Independent, VC-backed. **$130M Series A led by Index Ventures (announced 2025-12-04)**, with new investor Blackstone Innovations Investments plus Greylock, CRV, and Spark; ~$700M valuation (per Calcalist/Globes); ~$166M total raised. Billed as the largest cybersecurity Series A on record (marketing). No M&A; no seed acquisition flag. Confidence high on independence and the round; valuation from secondary press (medium).

**CTO / hedge-fund lens** — **Day-2**, and skewed to the larger end. The throughput story and Fortune-500 customer base suggest it fits big SOCs, not a 50-person fund. For most asset managers this is interesting mainly via the PLAID managed wrap or via an MSSP. Very new (post-stealth 2025) — weigh maturity/stability against the funding hype. No direct SR 11-7 angle; diligence the autonomy boundaries (what actions agents take unsupervised) and data handling.

**Competitors / alternatives** — [prophet-security](prophet-security.md), [dropzone-ai](dropzone-ai.md), [radiant-security](radiant-security.md), [simbian](simbian.md), [torq](torq.md).

**Open questions / to verify** — Product maturity vs. marketing; what autonomous response actions agents are allowed to take; data-residency/training-use terms; whether the $700M valuation is confirmed by a primary source.

## Sources
- [Citing the 'Agentic Security Inflection Point,' 7AI Raises Largest Cybersecurity A Round in History (7AI blog)](https://blog.7ai.com/citing-the-agentic-security-inflection-point-7ai-raises-largest-cybersecurity-a-round-in-history-to-bring-ai-security-agents-to-enterprises) — fetched 2026-06-28 — supports: $130M Series A, founders, metrics, deployment; confidence: med (vendor blog).
- [Cybereason founders' 7AI raises record $130M Series A (Calcalist)](https://www.calcalistech.com/ctechnews/article/sj2b4zkzzx) — fetched 2026-06-28 — supports: 2024 founding, Boston HQ, ~$700M valuation, Index Ventures lead; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established 2024 founding, Boston HQ, founders ex-Cybereason (Lior Div / Yonatan Striem-Amit), $130M Series A (Index, 2025-12), ~$166M total, ~$700M valuation, independent. Set ownership_confidence high. trifecta=none. hedge_fund_fit=medium (Day-2, large-enterprise skew).
