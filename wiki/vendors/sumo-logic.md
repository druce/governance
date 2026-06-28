---
type: vendor
name: Sumo Logic
slug: sumo-logic
categories: [siem-soc]
layer: foundation
aliases: []
website: "https://www.sumologic.com"
founded: 2010
hq: Redwood City, USA
ownership: acquired
ownership_detail: "Taken private by Francisco Partners (PE) for ~$1.7B ($12.05/share); announced 2023-02-09, closed 2023-05-12. Delisted from Nasdaq."
ownership_confidence: high
funding_total: "n/a (was public, Nasdaq: SUMO, before take-private)"
last_funding: IPO Sep 2020
deployment: [saas]
target_customer: enterprise / cloud-native ops & security teams
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [siem, log-analytics, observability, francisco-partners]
---

# Sumo Logic

> **One-liner** — A cloud-native SaaS log analytics and SIEM platform for security + ops telemetry; taken private by Francisco Partners in 2023.

**Categories** — [siem-soc](../categories/siem-soc.md)

## What it does
Sumo Logic ingests logs, metrics and events from cloud and on-prem systems and provides log analytics, observability and a **cloud SIEM / Cloud SOC** for threat detection and investigation. The job: centralize machine data so security and ops teams can search, alert and investigate — the SIEM tier that AI-system audit logs, gateway logs and agent activity should ultimately feed into.

## Where it sits in the stack
Foundation layer, [siem-soc](../categories/siem-soc.md). Lethal-trifecta leg: **none directly** — it is the detection/audit substrate, not an inline control. It is where you'd land logs from [ai-gateway](../categories/ai-gateway.md), [ai-runtime-security](../categories/ai-runtime-security.md) and [ai-access-governance](../categories/ai-access-governance.md) tools for monitoring and forensics. Adjacent to [ai-soc-analysts](../categories/ai-soc-analysts.md), which increasingly sit on top of SIEM data.

## Deployment & architecture
SaaS, multi-tenant; agent/collector and API-based ingestion. Integrates with cloud providers, security tooling and observability sources. Not an inline proxy.

## Positioning & differentiators
A cloud-native SIEM/log-analytics alternative to the heavyweight incumbents. Nearest neighbors: [splunk](splunk.md) (now Cisco), [microsoft-sentinel](microsoft-sentinel.md), [elastic](elastic.md), [google-secops](google-secops.md), [crowdstrike-logscale](crowdstrike-logscale.md). Sumo's pitch is SaaS-native economics and combined ops+security telemetry; it is generally positioned below Splunk/Sentinel in enterprise mindshare.

## Ownership, funding & M&A
**Verified.** **Taken private by Francisco Partners** (PE) — announced **2023-02-09**, **closed 2023-05-12** at **$12.05/share, ~$1.7B** equity value (~57% premium). Delisted from Nasdaq (was SUMO). Founded 2010; HQ Redwood City, CA; previously public (IPO Sep 2020). Now a private Francisco Partners portfolio company. Ownership confidence **high**.

## CTO / hedge-fund lens
**Day-1 (SIEM is table-stakes)** — but most funds already own a SIEM, so the question is whether Sumo is your incumbent rather than whether to buy net-new. As a private PE-owned asset, watch for roadmap/pricing changes and the typical PE focus on margin. For AI governance, what matters is that your AI control points log to whatever SIEM you run; Sumo is a fine landing zone but not differentiated for AI specifically.

## Competitors / alternatives
[splunk](splunk.md), [microsoft-sentinel](microsoft-sentinel.md), [elastic](elastic.md), [google-secops](google-secops.md), [crowdstrike-logscale](crowdstrike-logscale.md).

## Open questions / to verify
- Current AI/LLM-monitoring features under Francisco Partners ownership.
- Any post-take-private M&A or product rebranding.

## Sources
- [Francisco Partners Completes Acquisition of Sumo Logic](https://www.sumologic.com/newsroom/francisco-partners-completes-acquisition-of-sumo-logic) — fetched 2026-06-28 — supports: acquirer, close date 2023-05-12, $12.05/share, ~$1.7B, delisting; confidence: high
- [Sumo Logic to be Acquired by Francisco Partners for $1.7 Billion](https://www.franciscopartners.com/media/sumo-logic-to-be-acquired-by-francisco-partners-for-17-billion) — fetched 2026-06-28 — supports: deal value, announce 2023-02-09, premium; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified Francisco Partners take-private (~$1.7B, closed 2023-05-12), raised ownership_confidence low→high; filled founding/HQ, SIEM positioning.
