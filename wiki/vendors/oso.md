---
type: vendor
name: Oso
slug: oso
categories: [authorization-engine, agent-runtime-security]
layer: model-prompt
aliases: [Oso Cloud, Polar, Oso for Agents, osohq]
website: https://www.osohq.com
founded: 2018
hq: New York, NY, USA (remote)
ownership: independent
ownership_detail: "VC-backed; ~$11M raised disclosed (Series A $8.2M, 2021-03, Sequoia); some sources cite up to ~$26M cumulatively"
ownership_confidence: medium
funding_total: ~$11M (Series A; some sources ~$26M cumulative)
last_funding: "Series A $8.2M (2021-03, Sequoia)"
deployment: [saas, sdk, self-hosted]
target_customer: mid-market / enterprise (developer-led)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [authorization, polar, agent-authz, ai-agents, rebac, abac]
---

# Oso

> **Researched 2026-06-28.** Primary category: [authorization-engine](../categories/authorization-engine.md). Independent, VC-backed (Sequoia Series A). 2025 pivot toward AI-agent security.

**One-liner** — Authorization-as-a-service built on **Polar**, a declarative policy language — now repositioning hard as an **AI-agent security & control platform** ("Oso for Agents").

## What it does
Oso lets developers model and enforce access control (RBAC, ReBAC, ABAC, or mixes) using **Polar**, its declarative policy language (implemented in Rust). **Oso Cloud** is the managed authorization service (the company claims 1M+ req/s, <10ms latency); the earlier embeddable **Oso Library** is now legacy/deprecated in favor of Cloud. In 2025 Oso layered on **Oso for Agents**: discover agents running across an org (laptop, browser, terminal), monitor every prompt / tool call / response, detect policy violations, PII exposure and credential leakage, and enforce policy ("block unknown MCP servers," "deny all delete operations") with audit/compliance export.

## Where it sits in the stack
Primary [authorization-engine](../categories/authorization-engine.md) (Polar-based PDP); cross-listed to [agent-runtime-security](../categories/agent-runtime-security.md) because "Oso for Agents" extends from *deciding permissions* into *watching agent behaviour* — discovery, monitoring, detection. Layer: model-prompt. Lethal-trifecta role: as an authz engine it constrains **sensitive-data** and **egress** (decide whether an action is allowed); the agents product also touches **untrusted-input** monitoring (flagging risky tool calls), blurring toward [agent-runtime-security](../categories/agent-runtime-security.md). Not a content-injection firewall in the [ai-runtime-security](../categories/ai-runtime-security.md) sense, though its agent monitoring overlaps.

## Deployment & architecture
Managed **Oso Cloud** (SaaS) is the primary path; SDKs in major languages call a central PDP. Self-managed options exist. "Oso for Agents" adds discovery/monitoring across endpoints and an MCP-aware policy layer. Pairs with your IdP; authorizes rather than authenticates.

## Positioning & differentiators
Known for **Polar** — an expressive, purpose-built authz DSL — and a strong developer-education brand (Authorization Academy). Versus [open-policy-agent](open-policy-agent.md) (Rego, infra-general), [cerbos](cerbos.md) (stateless YAML), [authzed](authzed.md) (Zanzibar/ReBAC database), [permit-io](permit-io.md) (managed OPA/Cedar wrapper), [styra](styra.md) (enterprise OPA). Oso's distinctive 2025 bet is leaning into **agent** authorization/security as a wedge — closest in that framing to [zenity](zenity.md), [operant-ai](operant-ai.md), [straiker](straiker.md) on the runtime side while remaining an authz engine at its core.

## Ownership, funding & M&A
Founded **~2018** by **Graham Neray** (CEO) and **Sam Scott** (CTO); remote, New York base. **Series A $8.2M** (**2021-03**, led by **Sequoia**, with SV Angel, Company Ventures, Highland Capital and notable angels). Disclosed total ~**$11M** (incl. 2019 Sequoia seed); some trackers cite up to ~$26M cumulatively — hence ownership_confidence medium on the exact figure. **No M&A** — independent (no seed flag). Confidence high on independence, medium on total funding.

## CTO / hedge-fund lens
Day-2. Attractive if you want a managed authz engine with an expressive policy language and minimal ops, and you're interested in the **agent-security angle** (discover/monitor/control agents) from one vendor. The agents product is **new** — diligence maturity and production references before relying on it as a primary agent-runtime control; for pure authz the core Oso Cloud is more proven. The Polar DSL is a (mild) lock-in consideration vs OPA/Cedar's broader ecosystems.

## Competitors / alternatives
[open-policy-agent](open-policy-agent.md), [cerbos](cerbos.md), [authzed](authzed.md), [permit-io](permit-io.md), [styra](styra.md); on the agent-runtime side [zenity](zenity.md), [operant-ai](operant-ai.md), [straiker](straiker.md).

## Open questions / to verify
- **Exact cumulative funding** (sources disagree: ~$11M disclosed vs ~$26M cited) and any round since 2021.
- Maturity and customer references for **Oso for Agents** specifically (launched 2025; positioning is largely vendor marketing as of fetch).
- Status/end-of-life of the legacy open-source Oso Library.

## Sources
- [Oso Series A announcement (osohq.com)](https://www.osohq.com/post/oso-series-a-announcement) — fetched 2026-06-28 — supports: $8.2M Series A 2021-03 Sequoia, founders, ~2018 founding, Polar, Oso Cloud; confidence: high
- [Oso homepage — "Oso for Agents" (osohq.com)](https://www.osohq.com/) — fetched 2026-06-28 — supports: 2025 AI-agent security pivot (discover/monitor/detect/control/report), Oso Cloud scale claims; confidence: med (marketing)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established ~2018 founding, NY/remote, founders (Neray/Scott), Sequoia Series A $8.2M (2021), Polar/Oso Cloud. Documented **2025 "Oso for Agents" pivot** and added [agent-runtime-security](../categories/agent-runtime-security.md) as secondary category. No M&A — independent. Confidence high (funding total medium).
