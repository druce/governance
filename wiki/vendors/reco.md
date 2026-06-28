---
type: vendor
name: Reco
slug: reco
categories: [ai-spm, ai-access-governance, sspm]
layer: model-prompt
aliases: [Reco AI, Reco Labs, recolabs]
website: "https://www.reco.ai"
founded: 2020
hq: New York, NY, US (also Tel Aviv, Israel)
ownership: independent
ownership_detail: Venture-backed; $85M total raised. $30M Series B led by Zeev Ventures (2026-02). No acquisition.
ownership_confidence: high
funding_total: $85M
last_funding: Series B, $30M, 2026-02
deployment: [saas, api]
target_customer: enterprise (regulated, large SaaS estates)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [sspm, ai-spm, shadow-ai, identity, saas-security]
---

# Reco

> Primary category: [ai-spm](../categories/ai-spm.md). Also [sspm](../categories/sspm.md) and [ai-access-governance](../categories/ai-access-governance.md).

**One-liner** — An agentless, AI-native SaaS security posture management (SSPM) platform that connects to your SaaS apps and IdP via API/OAuth, builds an identity graph, and discovers shadow SaaS and shadow-AI usage along with the access and misconfigurations around it.

## What it does

Reco continuously monitors an organization's SaaS estate to find misconfigurations, over-permissioned identities, risky third-party app integrations, and unsanctioned ("shadow") apps — including the growing class of embedded and standalone **AI tools and agents**. It connects to sanctioned SaaS apps (Microsoft 365, Google Workspace, Salesforce, Slack, GitHub, etc.) and the identity provider through API/OAuth, then maps the relationships between users, data, permissions, and apps into an **identity graph**. From that graph it flags posture problems (e.g. public file shares, dormant admin accounts, dangerous OAuth grants), detects anomalous behavior, and can drive remediation (revoke access, alert, enforce policy). The 2025-2026 product framing leans heavily on **shadow-AI discovery** and "agentic ecosystem security" — securing the apps, identities, and permissions that AI agents touch, rather than the model prompt itself.

## Where it sits in the stack

- Primary: [ai-spm](../categories/ai-spm.md) — AI security posture management, here delivered as a discovery/posture lens over the SaaS layer (which AI tools are connected, what they can reach).
- [sspm](../categories/sspm.md) — its origin and core: classic SaaS security posture management.
- [ai-access-governance](../categories/ai-access-governance.md) — the identity-graph view of who/what can access which data through SaaS and AI integrations.
- Layer: model-prompt (per taxonomy), though Reco's actual control point is the **SaaS/identity/data layer around** the model, not inline on prompts.
- Lethal-trifecta role: mainly **sensitive-data** exposure and **egress/connectivity** (risky third-party and AI OAuth grants that can exfiltrate data). It does **not** sit inline on untrusted input — it is a posture/visibility and access-governance tool, not a runtime prompt firewall.
- Trust zones: spans the green/yellow zones (sanctioned SaaS + IdP) and surfaces yellow/red shadow-AI connections.

## Deployment & architecture

- **Agentless, API-driven** via OAuth integrations to SaaS apps and the IdP; no inline proxy, no endpoint agent. Vendor claims deployment in ~24 hours and new-app onboarding in 3-5 days ("SaaS AppFactory" model). (Vendor marketing.)
- Builds and maintains an **identity graph** across users, apps, data, and permissions; layered detections (vendor claims 235+ app integrations, 1,000+ detection controls — marketing).
- Integrates with SIEM/SOC and IdP for alerting and response; positions itself as the SaaS/AI-discovery feed for the security team.

## Positioning & differentiators

Reco's pitch is SSPM rebuilt for a dynamic, AI-heavy SaaS world: broad/fast app coverage plus an identity-graph correlation engine, now extended to shadow-AI and agent discovery.

- vs [appomni](appomni.md) and [obsidian-security](obsidian-security.md) — fellow SSPM/identity-threat platforms; the three are direct SSPM competitors, with Reco emphasizing speed of integration and the AI/agent narrative.
- vs [nudge-security](nudge-security.md) — Nudge leans SaaS/identity governance with user-nudging workflows; overlapping shadow-SaaS discovery, lighter on deep posture detections.
- vs [grip-security](grip-security.md) — Grip centers on SaaS identity risk and shadow-SaaS sprawl; similar discovery goal, different emphasis (identity sprawl/offboarding).
- vs [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [witnessai](witnessai.md) — these are **runtime / inline** AI-usage governance (DLP on prompts, AI gateways/proxies). Reco is **out-of-band posture/discovery**, not an inline guardrail — complementary rather than directly competing on the same control point.

## Ownership, funding & M&A

- **Independent, venture-backed.** No acquisition — confirmed; the only "SentinelOne" link is **S Ventures**, SentinelOne's corporate venture fund, as a minority **investor** (not acquirer) in the Series B.
- **$85M total raised** (vendor, 2026-02). Trajectory: an earlier ~$30M (to ~$55M? — see note), then **$25M in April 2025** bringing total to ~$55M, then a **$30M Series B led by Zeev Ventures on 2026-02-10** to reach $85M. Series B also added Insight Partners (existing), boldstart ventures, Angular Ventures, and new investors Workday Ventures, TIAA Ventures, S Ventures, and Quadrille Capital.
- Founded **2020** (legal entity Reco Labs). Founders: **Ofer Klein** (CEO; ex-Israeli pilot/serial entrepreneur), **Gal Nakash** (CPO; ex-Lt. Col., Israeli PM's Office), **Dr. Tal Shapira** (CTO; PhD Tel Aviv U., ex-cyber R&D head, Israeli PM's Office). This matches the brief's target ("ex-Israeli intelligence" founders) — correct Reco.
- HQ listed as **New York, NY** in recent press; About page also lists offices in Altamonte Springs FL, Tel Aviv, and Moldova.

## CTO / hedge-fund lens

**Day-2.** This is a posture/governance tool you adopt once you have a meaningful SaaS estate and want to (a) inventory and control shadow SaaS/AI and (b) tighten access and third-party OAuth grants. For a small fund it's likely overkill; for a mid-size-to-large asset manager running Microsoft 365 / Google Workspace plus dozens of SaaS apps and worried about employees wiring data into unsanctioned AI tools, the **shadow-AI discovery** angle is the most relevant hook. It is not a substitute for an inline AI firewall/DLP — pair it with a runtime control if prompt-level egress is the concern. SR 11-7 model-risk relevance is indirect (it governs the SaaS/identity surface, not models). `hedge_fund_fit: medium`.

## Competitors / alternatives

[appomni](appomni.md), [obsidian-security](obsidian-security.md), [nudge-security](nudge-security.md), [grip-security](grip-security.md) (SSPM/SaaS-identity); complementary to inline AI-usage governance [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [witnessai](witnessai.md).

## Open questions / to verify

- Exact round history and labels (the "$30M earlier / $25M Series A April 2025 / $30M Series B Feb 2026" sequence is partly press-derived; one aggregator cites $98M total vs vendor's $85M — used vendor figure).
- Single canonical HQ (NY vs FL) — press and About page differ.
- Depth of true AI-SPM (model/agent posture) vs SSPM-with-AI-discovery marketing — verify against product docs.
- Real-world remediation/enforcement maturity vs alert-only.

## Sources

- [Reco Raises $30M B Round for a Total of $85M](https://www.reco.ai/blog/reco-raises-30m-b-round-for-a-total-of-85m-to-meet-rapidly-growing-demand-for-saas-ai-security-among-enterprises) — fetched 2026-06-28 — supports: $85M total, $30M Series B (2026-02-10) led by Zeev Ventures, investor list, NY HQ, Ofer Klein CEO; confidence: high (vendor/marketing for metrics).
- [S Ventures' Investment in Reco — SentinelOne](https://www.sentinelone.com/s-ventures/blog/s-ventures-investment-in-reco/) — fetched 2026-06-28 — supports: agentless API/OAuth deployment, identity graph, shadow-AI discovery, SSPM positioning, S Ventures = investor not acquirer; confidence: med (investor marketing).
- [About Us — Reco AI](https://www.reco.ai/about-us) — fetched 2026-06-28 — supports: founders + backgrounds, founded 2020, offices, agentic-ecosystem positioning; confidence: med (vendor).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed correct Reco (Reco Labs, founded 2020, ex-Israeli-PM's-Office founders Klein/Nakash/Shapira). Independent, venture-backed, $85M total, $30M Series B led by Zeev Ventures (2026-02). No M&A — SentinelOne link is S Ventures investor only, not acquirer (no hard contradiction). Set ownership_confidence high, status researched, confidence medium. Kept categories [ai-spm, ai-access-governance, sspm]; noted control point is SaaS/identity layer, not inline prompt. 3 sources cached.
