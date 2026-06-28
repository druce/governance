---
type: vendor
name: Google SecOps (Chronicle)
slug: google-secops
categories: [siem-soc]
layer: foundation
aliases: [Chronicle, Chronicle Security Operations, Google Security Operations]
website: https://cloud.google.com/security/products/security-operations
founded: 2018
hq: Mountain View, CA, USA
ownership: public
ownership_detail: Google Cloud product line of Alphabet Inc. (NASDAQ: GOOGL/GOOG); incl. Mandiant (acq. completed 2022-09-12, ~$5.4B)
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [google, alphabet, siem, soc, chronicle, mandiant, incumbent]
---

# Google SecOps (Chronicle)

> Google Cloud's cloud-native SIEM (formerly Chronicle), now fused with Mandiant threat intel and Gemini AI for agentic alert triage and investigation.

**One-liner** — Google's cloud-native SIEM/SOAR platform, built for petabyte-scale log retention, enriched with Mandiant threat intelligence and Gemini-powered investigation agents.

**What it does** — Ingests and retains security telemetry at very large scale, applies detections, and supports threat hunting and SOAR-style response. Differentiated historically by flat-rate, petabyte-scale storage (priced on employee count rather than ingest volume) and by built-in Mandiant frontline threat intelligence. The 2025-26 story is Gemini: AI-generated case summaries, response recommendations, context-aware chat, and NL detection/playbook creation.

**Where it sits in the stack** — [[siem-soc]], foundation layer. Detection/response plumbing; lethal-trifecta role **none** directly. It is where AI/security signals are centralized and where Gemini agents perform [[ai-soc-analysts]]-style triage natively.

**Deployment & architecture** — SaaS on Google Cloud, API-driven ingestion. Bundles Mandiant threat intel; Gemini agents (Alert Triage & Investigation agent, Threat Intel agent) entered public preview late 2025 and reached GA in 1Q26. Integrates with Google Cloud, Chrome Enterprise, and third-party sources.

**Positioning & differentiators** — Scale + threat-intel depth (Mandiant) + Gemini. Elevated to Leader in Gartner MQ for SIEM (2025) and IDC MarketScape SIEM 2026. Strongest for Google Cloud-centric or threat-intel-hungry shops; weaker native pull for Microsoft-centric estates ([[microsoft-sentinel]]). Competes with [[splunk]], [[elastic]], [[crowdstrike-logscale]], [[sumo-logic]].

**Ownership, funding & M&A** — Product line of **Alphabet Inc. (NASDAQ: GOOGL/GOOG)** via Google Cloud; public, high confidence. Chronicle began inside Alphabet's X moonshot lab (2018), became a Google Cloud product, rebranded Chronicle -> Google Security Operations (April 2024). **Mandiant acquisition confirmed**: announced March 2022 ($23.00/share, ~$5.4B all-cash), completed **2022-09-12**. Stub previously `ownership: independent` — corrected to `public`.

**CTO / hedge-fund lens** — **Day-1** if you are Google Cloud-centric or want bundled top-tier threat intel; otherwise a strong alternative to evaluate against [[microsoft-sentinel]]. Pricing model (often per-user) can favor data-heavy shops. Not an SR 11-7 tool; useful as the central audit/log store for AI activity.

**Competitors / alternatives** — [[microsoft-sentinel]], [[splunk]], [[elastic]], [[crowdstrike-logscale]], [[sumo-logic]].

**Open questions / to verify** — Current pricing structure (per-user vs ingest) for a small fund; degree of Chrome Enterprise / Gemini Enterprise integration.

## Sources
- [Google Security Operations product page](https://cloud.google.com/security/products/security-operations) — fetched 2026-06-28 — supports: Google/Alphabet ownership, SIEM, Gemini agents; confidence: high
- [Mandiant 8-K (acquisition)](https://www.sec.gov/Archives/edgar/data/0001370880/000110465922099178/tm2225581d1_ex99-1.htm) — fetched 2026-06-28 — supports: Mandiant acquired by Google, $5.4B, closed 2022-09-12; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); confirmed Alphabet/Google ownership (public), confirmed Mandiant acquisition closed 2022-09-12, set ownership=public/high, filled SIEM one-liner + Gemini agentic angle. 2 sources cached.
