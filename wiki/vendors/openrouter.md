---
title: OpenRouter
type: vendor
name: OpenRouter
slug: openrouter
categories: [ai-gateway]
layer: model-prompt
aliases: []
website: "https://openrouter.ai"
founded: 2023
hq: New York, NY (US)
ownership: independent
ownership_detail: "VC-backed independent. Seed (~$12.5M, a16z, early 2025); Series A (~$28M, Menlo Ventures, Apr 2025, ~$500M valuation); Series B ($113M, CapitalG-led, 2026-05-26, ~$1.3B valuation)."
ownership_confidence: high
funding_total: ~$153M (cumulative, through Series B 2026-05)
last_funding: Series B — $113M, led by CapitalG — 2026-05-26
deployment: [saas, api]
target_customer: developers / startups / enterprise (multi-model inference buyers)
hedge_fund_fit: low
priority: day-1
trifecta_relevance: [egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [ai-gateway, inference-marketplace, model-routing, hosted-aggregator]
---

# OpenRouter

> Primary category: [ai-gateway](../categories/ai-gateway.md).

**One-liner** — A hosted "unified interface for LLMs": one API and one billing relationship that routes your requests across 400+ models from 70+ providers, with automatic fallback and price/latency routing.

## What it does

OpenRouter is a third-party **inference marketplace and routing layer**. You point your app at OpenRouter's OpenAI-compatible API instead of at each model provider directly. OpenRouter normalizes the differing APIs, exposes a single catalog of 400+ models (OpenAI, Anthropic, Google, Mistral, Groq, DeepSeek, and many open-weight hosts), and forwards each request to a downstream provider — picking by price, latency, or availability and failing over automatically when a provider degrades. You get one bill, one API key, and the ability to switch or A/B models without re-integrating. The pitch is escaping single-vendor lock-in and the operational churn of an LLM market where "models flicker on and off, pricing changes overnight, and providers have different APIs" (a16z).

It is consumer/developer-facing in origin (it also ships a web chat UI) and has grown into the self-described "largest AI gateway": 10M+ users, 1M+ developers, ~100T tokens/month (25T/week as of mid-2026).

## Where it sits in the stack

[ai-gateway](../categories/ai-gateway.md) (AI model & prompt layer). An AI gateway is the **single exit door for model traffic** — the choke point where an org centralizes keys, spend, routing and policy for outbound LLM calls. OpenRouter occupies that slot but as a **hosted aggregator** rather than infrastructure you run.

Lethal-trifecta role: **egress**. The gateway is exactly where outbound model traffic (potentially carrying sensitive data) leaves your control. The critical nuance for a regulated buyer: with OpenRouter the egress endpoint is *OpenRouter's own cloud*, and from there to whichever downstream provider it routes to — so it adds a hop and a counterparty rather than being a control you own. It does not address untrusted-input or sensitive-data legs.

## Deployment & architecture

- **Hosted SaaS / API only.** There is no self-hosted edition. Your traffic transits OpenRouter's infrastructure (`openrouter.ai`, or `eu.openrouter.ai` for EU in-region) and is then proxied to the chosen provider.
- **OpenAI-compatible REST API**, plus SDKs and a web chat. Integrates at the application layer.
- **Data handling:** By default OpenRouter does **not** log prompts/completions — it keeps request metadata (timestamps, model, token counts, latency) for billing/ops. Prompt logging is opt-in (1% usage discount). Customers can restrict routing to **Zero-Data-Retention** endpoints (globally, per model group, per request) and set `data_collection: deny` to exclude providers that train on inputs. Enterprise accounts can pin **EU in-region routing**.
- Retention/training behavior ultimately **depends on the downstream provider** you route to — OpenRouter is a pass-through, so its data guarantees are only as strong as the endpoint it selects (constrained by your policy settings).

## Positioning & differentiators

Known for **breadth of model catalog and zero-friction multi-model access** — the fastest way to try, compare, and fail over across many models without per-provider contracts. Neutral marketplace positioning: it claims not to prioritize its own models (it has none).

How it differs from neighbors:
- vs **[litellm](litellm.md)** — LiteLLM is an open-source, self-hostable gateway/proxy you run inside your own perimeter; OpenRouter is a hosted service you route *through*. Same "unified API" idea, opposite trust model.
- vs **[portkey](portkey.md)** — Portkey is a gateway + observability/guardrails control plane (self-host or SaaS) aimed at enterprises; OpenRouter is a marketplace optimized for model access and billing aggregation.
- vs **[kong](kong.md)** / **[truefoundry](truefoundry.md)** — infrastructure/platform gateways you deploy and own; OpenRouter is managed and opinionated toward the aggregator marketplace.
- vs **[cloudflare](cloudflare.md)** (AI Gateway) — Cloudflare provides a hosted gateway too, but as edge infra alongside your existing provider keys; OpenRouter additionally aggregates *billing and supply* across providers.

The defining difference for governance: OpenRouter is a **counterparty in the data path**, not just software.

## Ownership, funding & M&A

Independent, VC-backed. No M&A (it is an acquirer of capital, not acquired). Funding (verified):
- ~$12.5M seed led by **Andreessen Horowitz** (early 2025).
- ~$28M **Series A** led by **Menlo Ventures** (Apr 2025) at a **~$500M** valuation; some outlets reported the seed+A together as "~$40M, a16z + Menlo."
- **$113M Series B** led by **CapitalG** (Alphabet) announced **2026-05-26** at a **~$1.3B** valuation; additional investors include the VC arms of Nvidia, ServiceNow, MongoDB, Snowflake, Databricks, plus a16z and Menlo.
- Founders: **Alex Atallah** (CEO, ex-OpenSea co-founder) and **Louis Vichy**; Chris Clark (COO). HQ commonly listed as New York (some sources say San Francisco — minor, see open questions).

## CTO / hedge-fund lens

AI gateways are a **Day-1** control (single exit door for model traffic), but OpenRouter is **probably the wrong gateway for a regulated fund**, hence `hedge_fund_fit: low`:

- **Data residency / egress concern.** Routing prompts (which may contain MNPI, positions, or client data) through a *third-party aggregator* that then forwards to downstream providers adds a counterparty and a second hop in the data path. Even with ZDR and EU-region options, you are trusting OpenRouter's controls plus each selected provider's — a harder vendor-risk and data-flow story than calling Anthropic/OpenAI directly or running a self-hosted gateway.
- **Concentration & supply opacity.** Auto-routing to "best available" provider can land your traffic on hosts (including open-weight/overseas providers) you might not have approved; you must actively constrain allow/deny lists.
- **Where it does fit:** R&D/experimentation, model evaluation, cost optimization on non-sensitive workloads — exactly the "try everything cheaply" use case. For production traffic with sensitive data, most funds will prefer a gateway they own ([litellm](litellm.md), [kong](kong.md), [truefoundry](truefoundry.md), [portkey](portkey.md) self-hosted) or direct provider contracts.
- Not an SR 11-7 / model-risk tool; it's plumbing, though it touches model-inventory and vendor-risk questions.

## Competitors / alternatives

[litellm](litellm.md), [portkey](portkey.md), [kong](kong.md), [truefoundry](truefoundry.md), [cloudflare](cloudflare.md) — see the [ai-gateway](../categories/ai-gateway.md) page. Self-hostable options are the natural alternative for regulated shops.

## Open questions / to verify

- HQ: New York vs San Francisco — sources conflict (soft, non-blocking).
- Exact cumulative funding total (estimated ~$153M from disclosed rounds; some round amounts reported as ranges).
- Whether OpenRouter offers contractual enterprise data-residency / DPA terms sufficient for a regulated fund (EU in-region exists; US/SOC2/BAA specifics not confirmed here).

## Sources

- [Investing in OpenRouter — Andreessen Horowitz](https://a16z.com/announcement/investing-in-openrouter/) — fetched 2026-06-28 — supports: founders, product/control-plane framing, a16z lead, 1M+ developers; confidence: high (primary investor, marketing tone).
- [OpenRouter Raises $113M CapitalG-led Series B (trendingtopics, covering BusinessWire)](https://www.trendingtopics.eu/openrouter-investment-capitalg-others/) — fetched 2026-06-28 — supports: $113M Series B, CapitalG lead, ~$1.3B valuation, 25T tokens/week, investor list, leadership; confidence: high.
- [OpenRouter About + ZDR/Data-Collection/Residency docs](https://openrouter.ai/about) — fetched 2026-06-28 — supports: 400+ models/70+ providers/100T monthly tokens, hosted SaaS+API model, ZDR/opt-in logging, EU in-region routing; confidence: med-high (vendor docs/marketing).
- (corroborating, from search) Orrick legal release on seed+Series A; ChainCatcher; Crunchbase Series A — supports: ~$40M seed+A, Menlo Series A ~$500M valuation; confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2023 (Atallah/Vichy), NY HQ, independent VC-backed (a16z seed → Menlo Series A ~$500M → CapitalG Series B $113M ~$1.3B, 2026-05-26), hosted SaaS/API aggregator (no self-host), egress trifecta leg, hedge_fund_fit=low due to third-party data-path/residency risk. 3 sources cached. No M&A. No hard contradictions (HQ NY/SF is a soft mismatch).
