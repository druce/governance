---
type: vendor
name: Elastic (ELK)
slug: elastic
categories: [siem-soc]
layer: foundation
aliases: [Elasticsearch, ELK Stack, Elastic Security]
website: https://www.elastic.co/security
founded: 2012
hq: Mountain View, CA, USA (incorporated in the Netherlands as Elastic N.V.)
ownership: public
ownership_detail: Elastic N.V., public (NYSE: ESTC)
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
sources_count: 2
last_updated: 2026-06-28
tags: [elastic, elk, siem, soc, open-source, incumbent]
---

# Elastic (ELK)

> The ELK-stack company — Elasticsearch-based search/analytics that powers a self-hostable or SaaS SIEM (Elastic Security) with a built-in generative-AI assistant.

**One-liner** — Elastic Security is a SIEM/XDR built on the Elasticsearch (ELK) stack, popular because teams can self-host the data plane and avoid per-GB SaaS SIEM pricing, now with an LLM-backed AI Assistant.

**What it does** — Elasticsearch is the search/analytics engine; Logstash ingests, Kibana visualizes (together "ELK"). Elastic Security layers SIEM, endpoint/XDR, and SOAR-style automation on top. The draw for cost-sensitive shops is deployment flexibility: run it yourself on your own infra, or buy it as a managed cloud service. Detection rules are developed in public repos on a ~two-week cadence.

**Where it sits in the stack** — [siem-soc](../categories/siem-soc.md), foundation layer. Detection/response plumbing; lethal-trifecta role **none** directly. Also widely used as a general log/observability store, so it often already holds the data an AI-oversight program needs.

**Deployment & architecture** — SaaS (Elastic Cloud) or self-hosted/on-prem — a key differentiator vs cloud-only SIEMs. The **Elastic AI Assistant** is built on the Elasticsearch Relevance Engine (ESRE) and gives context-aware alert-triage/IR guidance; it exposes a reasoning trace (prompts, tool calls, responses) and lets customers connect multiple LLMs and pick per workflow. The **Elastic AI SOC Engine (EASE)** targets alert fatigue and can work alongside [splunk](splunk.md) / [microsoft-sentinel](microsoft-sentinel.md).

**Positioning & differentiators** — Open-source heritage and self-host option keep data-plane costs controllable; bring-your-own-LLM and a transparent reasoning trace are differentiators on the AI side. Named a Leader in IDC MarketScape Worldwide SIEM 2026. Competes with [splunk](splunk.md), [microsoft-sentinel](microsoft-sentinel.md), [google-secops](google-secops.md), [crowdstrike-logscale](crowdstrike-logscale.md), [sumo-logic](sumo-logic.md). Note: AWS's [opensearch](opensearch.md) is a fork of Elasticsearch (relicensing dispute, 2021).

**Ownership, funding & M&A** — **Elastic N.V., public (NYSE: ESTC)**; IPO 2018. Founded 2012 (Elasticsearch created 2010 by Shay Banon); HQ Mountain View, incorporated in the Netherlands. No M&A flag. Stub previously `ownership: independent` — corrected to `public`.

**CTO / hedge-fund lens** — **Day-1**-capable, and attractive to funds that want to control SIEM data costs by self-hosting or that already run Elasticsearch for other workloads. More engineering ownership than a fully managed Sentinel/SecOps. Not an SR 11-7 tool; serves as the searchable log store underpinning AI/security audit.

**Competitors / alternatives** — [splunk](splunk.md), [microsoft-sentinel](microsoft-sentinel.md), [google-secops](google-secops.md), [crowdstrike-logscale](crowdstrike-logscale.md), [sumo-logic](sumo-logic.md), [opensearch](opensearch.md).

**Open questions / to verify** — Licensing nuances (Elastic License / SSPL vs AGPL re-add 2024) for self-hosters; managed-vs-self-host TCO for a small SOC.

## Sources
- [Elastic AI Assistant](https://www.elastic.co/elasticsearch/ai-assistant) — fetched 2026-06-28 — supports: ELK-based security, ESRE AI assistant, multi-LLM; confidence: high
- [Elastic Named a Leader in IDC MarketScape: Worldwide SIEM 2026](https://www.businesswire.com/news/home/20260617537664/en/Elastic-Named-a-Leader-in-the-IDC-MarketScape-Worldwide-SIEM-2026) — fetched 2026-06-28 — supports: public (NYSE: ESTC), SIEM leadership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); confirmed Elastic N.V. public (NYSE: ESTC), set ownership=public/high, filled ELK/SIEM one-liner + AI Assistant (ESRE) angle. 2 sources cached.
