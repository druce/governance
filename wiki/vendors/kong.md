---
type: vendor
name: Kong
slug: kong
categories: [ai-gateway, mcp-gateway]
layer: model-prompt
aliases: [Kong Inc., Mashape, Kong AI Gateway, Kong Konnect]
website: https://konghq.com
founded: 2009
hq: San Francisco, CA, USA
ownership: independent
ownership_detail: "Private, VC-backed (unicorn). $175M Series E at $2B valuation closed 2024-11-19; total raised ~$345M. Not acquired, not public."
ownership_confidence: high
funding_total: ~$345M
last_funding: "Series E, $175M, 2024-11-19 (Tiger Global lead; $2B valuation)"
deployment: [saas, self-hosted, inline-proxy, api, on-prem]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [egress, untrusted-input]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [ai-gateway, mcp-gateway, api-management, llm-proxy, guardrails]
---

# Kong

> This page is scoped to **Kong's AI angle** — the **Kong AI Gateway** (AI plugins on Kong Gateway) and its **MCP / agent gateway** capabilities. Kong Inc. is primarily an API-management company (Kong Gateway, Kong Konnect, Insomnia); general API-management history is kept brief here. Primary category: [[ai-gateway]].

**One-liner** — Kong is a mature, open-source-rooted API-management vendor whose **AI Gateway** turns its battle-tested Kong Gateway proxy into a single governed exit door for LLM and agent traffic, adding multi-LLM routing, guardrails, PII redaction, semantic caching, and an MCP/agent gateway.

## What it does

Kong's core product is **Kong Gateway**, a widely deployed API gateway/proxy. **Kong AI Gateway** is not a separate product but a set of **plugins layered on Kong Gateway** that make it understand AI traffic:

- **AI Proxy / AI Proxy Advanced** — a provider-agnostic "Universal API": configure once, call any model. Supports OpenAI, Anthropic, Azure AI, AWS Bedrock, GCP Vertex/Gemini, Cohere, Mistral, Llama, and more, so client apps stay decoupled from provider-specific APIs.
- **Multi-LLM load balancing** — consistent-hashing, lowest-latency, usage-based, round-robin, and **semantic** routing, with retries and fallback across models/providers.
- **Guardrails & prompt security** — **AI Prompt Guard** (regex allow/deny), **AI Semantic Prompt Guard** (block by intent/meaning, not just keywords), plus integrations to Azure Content Safety, AWS Bedrock Guardrails, and **Lakera Guard**.
- **PII sanitization** — built-in AI PII Sanitizer detects/redacts sensitive data across ~20 categories and 9 languages on the way out.
- **AI Semantic Cache** — caches responses by embedding-similarity threshold to cut cost and latency.
- **Prompt templates/decorators/compression**, automated RAG injection, and observability (token/cost metrics) into Konnect dashboards and OpenTelemetry.
- **MCP & agent gateway** — an enterprise MCP gateway inside AI Gateway: autogenerate secure MCP servers from Kong-managed APIs, centralized MCP OAuth 2.1 auth, MCP observability/governance, MCP-enabled Konnect Developer Portal, the Volcano SDK for agents, and (AI Gateway 3.14) **Kong Agent Gateway** for agent-to-agent (A2A) traffic.

You'd want it when you already run, or are willing to run, an API gateway and want LLM/agent traffic governed by the **same** control plane as the rest of your APIs.

## Where it sits in the stack

- Primary: [[ai-gateway]] (model-prompt layer) — the single governed egress point for model traffic.
- Secondary: [[mcp-gateway]] — tool/agent access control for MCP and A2A.

**Lethal-trifecta role:** primarily controls the **egress** leg — it is the chokepoint where outbound model calls (and now MCP/agent calls) are routed, logged, rate-limited, and cost-controlled. Its guardrail and prompt-guard plugins also touch the **untrusted-input** leg (blocking/inspecting malicious prompts and moderating content). PII sanitization touches the sensitive-data leg but is redaction, not full DLP. Lives at the boundary between the application/agent zone and external model/tool providers.

## Deployment & architecture

- **Inline proxy / data plane.** AI traffic flows through Kong Gateway's proxy; AI features are plugins on that data plane — no separate runtime to learn if you already run Kong.
- **Deployment modes:** Konnect (Kong's SaaS control plane), self-hosted/traditional, hybrid (Kong-hosted control plane + self-hosted data planes), DB-less, and Kubernetes (Kong Ingress Controller). On-prem and air-gapped-friendly.
- **Integrations:** AI providers above; SIEM/observability via OpenTelemetry; IdP/OAuth/OIDC for auth (incl. MCP OAuth 2.1); guardrail partners (Lakera, Azure Content Safety, AWS Guardrails); Redis for semantic cache; Kong + **Noma** partnership for agentic-AI runtime security.

## Positioning & differentiators

- **API-management incumbent extending into AI.** Unlike AI-native gateways, Kong's pitch is "you already need an API gateway — let it govern AI too," consolidating LLM, MCP, and A2A traffic on one mature, self-hostable proxy. This is its key differentiator vs lighter LLM-only routers.
- **vs [[litellm]]** — LiteLLM is an open-source, developer-first LLM proxy/SDK; Kong is a heavier enterprise gateway with broader policy/auth/observability and a commercial control plane (Konnect), but more operational weight.
- **vs [[portkey]]** and **[[truefoundry]]** — those are AI-native gateways/LLMOps platforms; Kong leads on general API-gateway maturity, self-hosting depth, and treating AI as one traffic class among many, rather than an AI-first product.
- **vs [[cloudflare]]** (AI Gateway) — Cloudflare is edge/SaaS-network-native and easy to switch on; Kong is the self-hostable, data-plane-owned alternative favored by teams wanting on-prem control.
- **vs MCP-gateway neighbors** — Kong competes with MCP/agent-gateway entrants on the agentic side; advantage is auto-generating MCP servers from existing Kong-managed APIs and unifying LLM+MCP+A2A in one gateway.

## Ownership, funding & M&A

- **Independent, private, VC-backed (unicorn).** Founded **2009** as **Mashape** (an API marketplace), pivoted to API infrastructure and rebranded to **Kong**. HQ **San Francisco**.
- **Series E: $175M at a $2B valuation, closed 2024-11-19** (mix of primary and secondary), led by **Tiger Global**, co-led by **Balderton**, with Teachers' Venture Growth (Ontario Teachers'), 137 Ventures, and continuing investors Andreessen Horowitz, Index Ventures, CRV, Sapphire Ventures, Notable Capital. **Total raised ~$345M.** (confidence: high — primary source)
- **No M&A:** Kong has not been acquired and is not public (no seed M&A flag). Kong is the acquirer/partner side of deals, not a target, as of 2026-06-28.

## CTO / hedge-fund lens

- **Day-1** if you treat a governed AI exit door as foundational and you want to self-host the control point. Kong is most compelling for a fund that **already runs Kong Gateway** for its APIs — adding AI Gateway is incremental and keeps one policy/audit plane.
- **Fit: medium.** Strong if you want on-prem/self-hosted control, unified API+AI governance, and don't mind running gateway infrastructure. For a small fund with no existing gateway, a lighter SaaS option ([[portkey]], [[cloudflare]]) or open-source [[litellm]] may be faster to stand up. Kong shines at enterprise scale and multi-team governance.
- **Model-risk / SR 11-7:** the gateway gives you the centralized logging, cost attribution, and access control that support model-usage oversight, but it is governance plumbing, not a model-validation tool.
- Egress control + PII redaction + prompt guards address the most common Day-1 worries (uncontrolled model calls, data leaving, prompt injection) at one chokepoint.

## Competitors / alternatives

[[litellm]], [[portkey]], [[truefoundry]], [[cloudflare]] — and on the agentic side, MCP-gateway peers in [[mcp-gateway]].

## Open questions / to verify

- Exact licensing split between open-source Kong Gateway AI plugins vs Enterprise/Konnect-gated AI features (which guardrails/caching require a paid tier).
- Depth of PII detection vs dedicated DSPM/DLP tools (redaction breadth, false-positive behavior).
- Maturity/GA status of Kong Agent Gateway (A2A) and Volcano SDK as of mid-2026 (some announced at API Summit 2025).
- Verify exact 2009 Mashape founding date and rebrand year against a primary source.

## Sources

- [Kong Secures $175 Million New Financing at $2B Valuation (Kong press room)](https://konghq.com/company/press-room/press-release/kong-secures-175-million-new-financing) — fetched 2026-06-28 — supports: funding $175M, $2B valuation, 2024-11-19, ~$345M total, SF HQ, independent/private; confidence: high
- [Kong AI Gateway (Kong Docs)](https://developer.konghq.com/ai-gateway/) — fetched 2026-06-28 — supports: AI Proxy, guardrails, PII sanitizer, semantic cache, load balancing, deployment modes, MCP/A2A; confidence: high
- [Kong Announces Konnect MCP Support (Kong press room, API Summit 2025)](https://konghq.com/company/press-room/press-release/kong-announces-konnect-mcp-support-to-make-ai-and-agentic-development-easier-more-secure-and-cost-effective) — fetched 2026-06-28 — supports: MCP gateway capabilities, MCP OAuth 2.1, Agent/A2A gateway, Volcano SDK; confidence: high (vendor marketing)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; scoped page to Kong AI Gateway + MCP/agent gateway. Established founding 2009 (as Mashape), SF HQ, independent private VC-backed unicorn, Series E $175M at $2B valuation (2024-11-19), ~$345M total raised, no M&A (ownership_confidence high). Set deployment, trifecta_relevance [egress, untrusted-input], hedge_fund_fit medium; status researched, 3 sources cached.
