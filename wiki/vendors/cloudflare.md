---
type: vendor
name: Cloudflare
slug: cloudflare
categories: [ai-gateway, network-security-sase, ephemeral-environments]
layer: model-prompt
aliases: [NET, "Cloudflare One", "Workers AI", "AI Gateway"]
website: https://www.cloudflare.com/products/ai-gateway/
founded: 2009
hq: San Francisco, California, USA
ownership: public
ownership_detail: "Public — NYSE: NET; IPO September 2019. Founders retain voting control via dual-class structure."
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api, inline-proxy, edge]
target_customer: enterprise / mid-market / developers
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [egress, untrusted-input]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [ai-gateway, edge, sase, mcp, workers]
---

# Cloudflare

> **Scope note.** This page is scoped to Cloudflare's **AI use case** — the **AI Gateway**
> (part of the Workers AI / developer platform) and Cloudflare's **MCP / agents** support.
> Cloudflare's general CDN/SASE business is enormous but only summarized here; for the
> network-security angle see [[network-security-sase]], and for edge compute see
> [[ephemeral-environments]] / [[cloudflare-workers]]. For this wiki's gateway shortlist the
> relevant lens is [[ai-gateway]]; the company's primary category overall is
> [[network-security-sase]].

**One-liner** — Cloudflare runs an edge-hosted **AI Gateway** that you put in front of your
LLM calls to get caching, rate limiting, spend caps, logging, model fallback, and content
guardrails — a single control point for AI traffic on the same global network that already
fronts much of the internet.

## What it does

Cloudflare AI Gateway sits between your application and the model providers (OpenAI,
Anthropic, Google Gemini, Workers AI, Replicate, and 20+ others). You change your base URL
to route through Cloudflare and get, without re-plumbing your app:

- **Caching** of identical requests at the edge (Cloudflare claims up to ~90% latency
  reduction and lower provider bills);
- **Rate limiting** (sliding/fixed window) and **spend limits** by model/provider/metadata
  with automatic blocking;
- **Observability** — per-request logs (prompt, response, provider, tokens, cost, duration,
  status), real-time analytics via GraphQL, and Logpush export;
- **Reliability** — request retries, model **fallback**, and dynamic/A-B routing;
- **Guardrails** — real-time harmful-content moderation on prompts and completions, plus
  **DLP** scanning for PII / financial / healthcare data;
- **Auth & BYOK** — token-gated access to the gateway and encrypted storage of provider keys.

Separately, on the **agents** side, Cloudflare lets you host **remote MCP servers** on
Workers (Durable Objects + OAuth for authn/authz) and offers **MCP Server Portals**
(Cloudflare One, Open Beta announced 2025-08-26): a single zero-trust front door for all an
org's MCP servers, with IdP login, device-posture/geo policies, server curation, audit
logging, and bidirectional DLP blocking on tool calls. Cloudflare's roadmap is to route MCP
traffic through AI Gateway for deeper prompt filtering.

## Where it sits in the stack

Primary lens here is the [[ai-gateway]] layer (model/prompt) — the "single exit door" for
model traffic. Its lethal-trifecta role is mainly **egress control** (it is the chokepoint
where outbound model/tool calls can be logged, capped, and blocked); the **Guardrails + DLP**
features add an **untrusted-input** moderation leg. The MCP Portals piece lives in the
governance/trust-zone space and ties into [[network-security-sase]] (Cloudflare One) and
[[mcp-gateway]]. Edge hosting of agents/MCP servers on Workers connects to
[[ephemeral-environments]] / [[cloudflare-workers]].

## Deployment & architecture

- **SaaS / edge** — runs on Cloudflare's global anycast network; nothing to self-host.
- **Inline proxy / API** — you point your provider SDK's base URL at the AI Gateway endpoint
  (a "universal" endpoint or per-provider path). It is an HTTP proxy, not an SDK rewrite.
- **Integrations** — native with Workers AI; works with major model providers; Logpush to
  SIEM; Cloudflare One / Access for the SASE + MCP-portal controls; IdP for auth.
- Core features (analytics, caching, rate limiting) are **free** with a Cloudflare account;
  Guardrails/DLP and higher-tier logging are paid.

## Positioning & differentiators

- **Edge-native + free entry.** Unlike pure-software gateways, Cloudflare runs the proxy on
  its own network, so caching/latency/global PoPs come for free and the on-ramp is one line
  of code. This is its main wedge versus self-hosted options.
- **vs [[litellm]] / [[portkey]] / [[truefoundry]] / [[kong]] / [[openrouter]]:**
  - [[litellm]] is open-source/self-hosted, very broad provider normalization, you run it.
  - [[portkey]] and [[truefoundry]] are AI-gateway-first platforms with richer
    guardrails/governance and prompt management; Cloudflare's gateway is thinner on
    prompt-engineering/governance but stronger on edge performance and is bundled into a
    network the buyer may already own.
  - [[kong]] comes from API-gateway heritage (and an MCP gateway); Cloudflare overlaps on the
    "gateway" framing but is delivered as edge SaaS rather than a deployable gateway.
  - [[openrouter]] is a model-routing/marketplace aggregator; Cloudflare is
    infrastructure/control-plane, not a model reseller.
- **Agents/MCP angle is differentiated:** few gateway vendors also host remote MCP servers
  and offer a zero-trust MCP portal on the same platform.

## Ownership, funding & M&A

- **Public company.** NYSE: **NET**, IPO **September 2019** (~$565M net proceeds per SEC
  filings). Founded **2009** by Matthew Prince (CEO), Lee Holloway, and Michelle Zatlyn;
  HQ **San Francisco**. Founders hold a dual-class structure giving them outsized voting
  control. `ownership_confidence: high`.
- **No relevant M&A** to verify for the AI-gateway scope (the stub carried no seed M&A flag;
  none found). Cloudflare is an acquirer, not a target.
- _Correction vs stub:_ the prior stub said `ownership: independent` — that was wrong;
  Cloudflare has been publicly traded since 2019. Fixed to `public`.

## CTO / hedge-fund lens

- **Day-1 for the gateway layer** if you are building or proxying LLM apps and want one place
  to log, cap spend, cache, and apply basic guardrails — especially attractive if you already
  use Cloudflare for CDN/WAF/Zero Trust, since it's the same console and network.
- **Fit: medium.** Strong, cheap on-ramp for engineering teams and a clean egress chokepoint;
  but a regulated hedge fund will likely want deeper model-risk/governance and DLP than
  Cloudflare's gateway provides today, and may already standardize egress on its incumbent
  SASE ([[network-security-sase]]: Palo Alto, Zscaler, Netskope) rather than route AI
  separately. Little direct SR 11-7 / model-risk tooling — this is plumbing and guardrails,
  not a model-governance platform.
- Best where the shop is already a Cloudflare customer, ships its own AI features on Workers,
  or wants a low-friction free starting point before adopting a heavier gateway.

## Competitors / alternatives

[[litellm]], [[portkey]], [[truefoundry]], [[kong]], [[openrouter]], and the cloud providers'
own gateways. On the MCP side: [[mcp-gateway]] vendors. On egress/SASE: [[network-security-sase]].

## Open questions / to verify

- Depth of Guardrails/DLP vs dedicated [[ai-runtime-security]] firewalls — appears moderation-
  grade, not full prompt-injection defense. Verify current capability.
- Maturity/GA status of routing MCP traffic through AI Gateway (was roadmap as of 2025).
- Enterprise pricing for Guardrails/DLP and log retention tiers (not captured).

## Sources

- [Cloudflare AI Gateway — Features (docs)](https://developers.cloudflare.com/ai-gateway/features/) — fetched 2026-06-28 — supports: caching, rate/spend limits, guardrails, DLP, fallback, logging, BYOK, providers, free core tier; confidence: high (vendor docs/marketing).
- [Cloudflare blog — MCP Server Portals (Zero Trust)](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) — fetched 2026-06-28 — supports: MCP portals open beta 2025-08-26, AI Gateway as MCP chokepoint, DLP on tool calls, remote MCP hosting; confidence: med (vendor blog).
- [Cloudflare corporate facts — Wikipedia + SEC S-1/8-K](https://en.wikipedia.org/wiki/Cloudflare) — fetched 2026-06-28 — supports: founded 2009, HQ SF, NYSE:NET IPO Sept 2019; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; scoped page to AI-Gateway/MCP angle. Fixed ownership independent→public (NYSE: NET, IPO Sept 2019, conf high). Established founded 2009, HQ San Francisco; deployment saas/api/inline-proxy/edge; trifecta egress (+untrusted-input via Guardrails/DLP); hedge_fund_fit medium. Reordered categories so primary lens = ai-gateway for this wiki's listing. Cached 3 sources. No M&A. No contradictions.
