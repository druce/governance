---
type: vendor
name: Microsoft Defender XDR
slug: microsoft-defender
categories: [edr-xdr]
layer: foundation
aliases: [Microsoft 365 Defender, Defender for Endpoint, Microsoft Defender for Endpoint]
website: "https://www.microsoft.com/en-us/security/business/endpoint-security/microsoft-defender-endpoint"
founded: 2019
hq: Redmond, WA, USA
ownership: public
ownership_detail: "Product line of Microsoft Corporation (NASDAQ: MSFT)"
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api, sdk]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [microsoft, edr, xdr, endpoint, incumbent]
---

# Microsoft Defender XDR

> Microsoft's unified XDR — endpoint EDR plus identity, email, and cloud-app detection — now adding Security Copilot agents and AI-agent discovery on endpoints.

**One-liner** — Microsoft's extended detection and response (XDR) suite that unifies endpoint EDR (Defender for Endpoint) with identity, email, and SaaS signals, with Security Copilot agents layered on for SOC automation.

**What it does** — Defender XDR correlates signals across Defender for Endpoint (EDR), Defender for Office 365 (email), Defender for Identity, and Defender for Cloud Apps into a single incident view with automated investigation and response. Defender for Endpoint itself is cloud-native EDR with advanced hunting and mobile threat protection. For Microsoft 365 shops it is the default endpoint/XDR stack and feeds [microsoft-sentinel](microsoft-sentinel.md).

**Where it sits in the stack** — [edr-xdr](../categories/edr-xdr.md), foundation layer. Detection/response on endpoints and across the Microsoft estate; lethal-trifecta role **none** directly. Notably, the 2026 "agentic endpoint security" capability discovers and can govern/block AI agents running locally on endpoints — an emerging control point as agentic software proliferates (surfaced in an AI-agent inventory + exposure map).

**Deployment & architecture** — SaaS, agent-based on endpoints; integrates natively with Entra, Microsoft 365, and Sentinel. Security Copilot in Defender (Copilot Chat GA April 2026) adds a context-aware conversational SOC interface; agents include a Phishing Triage Agent (GA), a Dynamic Threat Detection Agent (continuous backend correlation across Defender + Sentinel), and a Security Alert Triage Agent (identity/cloud alerts, preview from April 2026).

**Positioning & differentiators** — Breadth across the Microsoft estate and bundling with M365 E5 licensing; named a Leader in the 2026 Gartner Magic Quadrant for Endpoint Protection. The agentic-SOC and on-endpoint AI-agent discovery features are its current differentiators. Competes with [crowdstrike](crowdstrike.md), [sentinelone](sentinelone.md).

**Ownership, funding & M&A** — Product line of **Microsoft Corporation (NASDAQ: MSFT)**; public, high confidence. No M&A flag. Stub previously `ownership: independent` — corrected to `public`.

**CTO / hedge-fund lens** — **Day-1** for Microsoft-centric funds: if you license M365 E3/E5, Defender is the natural EDR/XDR and avoids a separate endpoint vendor. The new on-endpoint AI-agent discovery is directly relevant to governing shadow agentic tools. Not an SR 11-7 model-risk tool. Main decision is Defender vs a dedicated EDR like [crowdstrike](crowdstrike.md) / [sentinelone](sentinelone.md).

**Competitors / alternatives** — [crowdstrike](crowdstrike.md), [sentinelone](sentinelone.md).

**Open questions / to verify** — Which features require E5 vs add-on Security Copilot SCUs; GA timeline for the agentic-triage and AI-agent-blocking capabilities.

## Sources
- [Microsoft Defender for Endpoint product page](https://www.microsoft.com/en-us/security/business/endpoint-security/microsoft-defender-endpoint) — fetched 2026-06-28 — supports: Microsoft ownership, EDR/XDR scope; confidence: high
- [Microsoft named a Leader in the 2026 Gartner MQ for Endpoint Protection](https://www.microsoft.com/en-us/security/blog/2026/05/29/microsoft-is-named-a-leader-in-the-2026-gartner-magic-quadrant-for-endpoint-protection/) — fetched 2026-06-28 — supports: market leadership, agentic SOC features; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); confirmed Microsoft ownership (public, MSFT), set ownership=public/high, filled XDR one-liner + Security Copilot agentic + on-endpoint AI-agent discovery angle. 2 sources cached.
