---
type: vendor
name: Microsoft Sentinel
slug: microsoft-sentinel
categories: [siem-soc]
layer: foundation
aliases: [Azure Sentinel]
website: https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel
founded: 2019
hq: Redmond, WA, USA
ownership: public
ownership_detail: Product line of Microsoft Corporation (NASDAQ: MSFT)
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [microsoft, siem, soc, incumbent]
---

# Microsoft Sentinel

> Cloud-native SIEM from Microsoft — collects security telemetry across an org, detects threats, and (as of 2025-26) runs as an agentic AI security platform via Security Copilot.

**One-liner** — Microsoft's cloud-native SIEM/SOAR that ingests security logs across cloud and on-prem, runs detections, and increasingly drives AI-assisted investigation through Security Copilot.

**What it does** — Sentinel is a security information and event management (SIEM) platform: it centralizes logs and alerts from endpoints, identity, network, cloud, and SaaS, correlates them into incidents, and supports hunting and automated response (SOAR playbooks). It is the data/analytics backbone of a SOC. For shops already in Azure/Microsoft 365, it is the default SIEM because telemetry from Entra, Defender, and Microsoft 365 flows in natively.

**Where it sits in the stack** — [siem-soc](../categories/siem-soc.md), foundation layer. This is detection-and-response plumbing, not an AI-specific control, so its lethal-trifecta role is **none** directly — but it is increasingly where AI-related security signals land (Copilot/agent activity connectors, agent identity tables) and where an [ai-soc-analysts](../categories/ai-soc-analysts.md) layer would draw context. Lives across all trust zones as an observer.

**Deployment & architecture** — SaaS, runs on Azure; billed on data ingestion/retention. A 2025 redesign added the **Sentinel data lake** (GA Sep 2025) for cheaper long-term retention, a graph layer, and an **MCP server** (public preview) so AI agents (Security Copilot, or VS Code + GitHub Copilot) can query and act on security data over an open standard. Integrates with Microsoft Defender XDR ([microsoft-defender](microsoft-defender.md)), Entra, and third-party sources.

**Positioning & differentiators** — Tightly coupled to the Microsoft security ecosystem; strongest when Defender/Entra/M365 are the telemetry sources. The 2025-26 pivot is "agentic SOC": natural-language playbook generation (Python), no-code agent building in the Security Copilot portal, and agentic triage. Competes with [google-secops](google-secops.md), [splunk](splunk.md), [elastic](elastic.md), [crowdstrike-logscale](crowdstrike-logscale.md), [sumo-logic](sumo-logic.md).

**Ownership, funding & M&A** — Product line of **Microsoft Corporation (NASDAQ: MSFT)**; public, ownership_confidence high. No M&A flag. Stub previously listed `ownership: independent` — corrected to `public` (Microsoft parent).

**CTO / hedge-fund lens** — **Day-1** for any Microsoft-centric fund: if you run Microsoft 365 / Azure / Entra, Sentinel is the path-of-least-resistance SIEM and consolidates licensing. Watch ingestion cost — log volume drives the bill; the data lake tier helps. Not a model-risk (SR 11-7) tool itself, but it is where you would centralize AI/agent audit logs for oversight.

**Competitors / alternatives** — [google-secops](google-secops.md), [splunk](splunk.md), [elastic](elastic.md), [crowdstrike-logscale](crowdstrike-logscale.md), [sumo-logic](sumo-logic.md).

**Open questions / to verify** — Exact pricing impact of data-lake tier vs analytics tier for a small SOC; maturity/GA status of the agentic features beyond preview.

## Sources
- [Microsoft Sentinel: the security platform for the agentic era](https://www.microsoft.com/en-us/security/blog/2025/09/30/empowering-defenders-in-the-era-of-agentic-ai-with-microsoft-sentinel/) — fetched 2026-06-28 — supports: Microsoft ownership, SIEM, data lake/MCP/Copilot agentic features; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); confirmed Microsoft ownership (public, MSFT), set ownership=public/high, filled SIEM one-liner + agentic-AI angle (Security Copilot, data lake, MCP). 1 source cached.
