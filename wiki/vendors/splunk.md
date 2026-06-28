---
type: vendor
name: Splunk
slug: splunk
categories: [siem-soc]
layer: foundation
aliases: [Splunk Enterprise Security, Splunk ES]
website: https://www.splunk.com
founded: 2003
hq: San Francisco, California, USA
ownership: subsidiary
ownership_detail: "Acquired by Cisco — completed 2024-03-18 for ~$28B (announced 2023-09-21). Now a Cisco business unit; was NASDAQ: SPLK."
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, self-hosted, on-prem]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [siem, soar, observability, cisco]
---

# Splunk

> Primary category: [siem-soc](../categories/siem-soc.md). The incumbent SIEM/observability platform, now owned by [cisco](cisco.md).

**One-liner** — The market-leading machine-data platform for searching, monitoring and analyzing logs — the SIEM/SOAR and observability backbone many SOCs run on, now Cisco's security/observability flagship.

**What it does** — Ingests and indexes log and telemetry data at scale, then powers search, dashboards, alerting and correlation. **Splunk Enterprise Security** is the SIEM; **Splunk SOAR** automates response; **Splunk Observability Cloud** covers APM/infra/AI-agent monitoring. For an AI stack, Splunk is where security and AI-app telemetry lands for detection, investigation and audit. Cisco is routing telemetry from its acquired AI-security products ([cisco-ai-defense](cisco-ai-defense.md), [galileo](galileo.md), pending [astrix-security](astrix-security.md)) into Splunk as the unifying SOC/observability layer.

**Where it sits in the stack** — [siem-soc](../categories/siem-soc.md) at the foundation layer: the system of record for security events and the place AI-pipeline logs get correlated. Trifecta role is indirect — it doesn't block any leg in line, but it gives you the **detection and audit** visibility over sensitive-data access and anomalous behavior that the other controls feed.

**Deployment & architecture** — Self-hosted (Splunk Enterprise), cloud (Splunk Cloud Platform), or hybrid. Ingests via forwarders, HEC, and APIs; huge app/integration ecosystem. Observability Cloud is SaaS. Cisco is layering Talos threat intel into Splunk and connecting Splunk to Cisco XDR.

**Positioning & differentiators** — The reference SIEM by mindshare and ecosystem depth; cost (volume-based licensing) is the classic complaint and the reason shops weigh alternatives. Nearest neighbors: [microsoft-sentinel](microsoft-sentinel.md), [google-secops](google-secops.md), [elastic](elastic.md), [sumo-logic](sumo-logic.md), [crowdstrike-logscale](crowdstrike-logscale.md), plus Cisco/Palo Alto Cortex XSIAM at the high end.

## Ownership, funding & M&A

**Acquired by [cisco](cisco.md)** — announced **2023-09-21**, completed **2024-03-18** for ~**$28 billion** ($157/share cash), the largest acquisition in Cisco's history. Splunk (founded 2003, San Francisco; formerly NASDAQ: SPLK) is now a Cisco business unit. Verified against Network World and Channel Futures completion coverage and the original SEC 8-K (high confidence).

## CTO / hedge-fund lens

**Day-1.** SIEM/SOC logging is table-stakes and Splunk is the most common shortlist entry; many funds already run it. For AI specifically, it's where you centralize and retain AI-app and security telemetry for detection and for audit/regulatory evidence. The Cisco ownership matters for roadmap (tighter Cisco XDR/AI-Defense integration) and for procurement leverage if you're a Cisco shop. Main decision axis vs [microsoft-sentinel](microsoft-sentinel.md)/[google-secops](google-secops.md) is cost and existing platform gravity, not capability.

## Competitors / alternatives

[microsoft-sentinel](microsoft-sentinel.md), [google-secops](google-secops.md), [elastic](elastic.md), [sumo-logic](sumo-logic.md), [crowdstrike-logscale](crowdstrike-logscale.md), [palo-alto-networks](palo-alto-networks.md) (Cortex XSIAM).

## Open questions / to verify

- Post-acquisition packaging changes (Splunk + Cisco XDR bundling) and current licensing model.

## Sources
- [Network World — Cisco completes $28 billion Splunk acquisition](https://www.networkworld.com/article/2066444/cisco-completes-28-billion-splunk-acquisition.html) — fetched 2026-06-28 — supports: close 2024-03-18, $28B, SIEM/SOAR/observability; confidence: high
- [Splunk Inc Form 8-K (SEC) — merger announcement](https://www.sec.gov/Archives/edgar/data/0001353283/000110465923102594/tm2326347d1_ex99-1.htm) — fetched 2026-06-28 — supports: 2023-09-21 announcement, $157/share / ~$28B; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed Splunk acquired by Cisco, completed 2024-03-18 for ~$28B (announced 2023-09-21). Set ownership=subsidiary (Cisco), confidence high; hedge_fund_fit high (Day-1 SIEM).
