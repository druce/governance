---
type: comparison
name: AI Gateways — head to head
slug: ai-gateways-head-to-head
status: drafted
last_updated: 2026-06-28
confidence: medium
sources_count: 18
---

# AI gateways, head to head

The [[ai-gateway]] is the **single exit door for all model traffic** — one endpoint in front of
many model providers, with routing/failover, rate + cost limits, caching, prompt/response logging,
and guardrail hooks. For a hedge-fund CTO it's a **Day-1** control: it's the chokepoint where you
get one audit log of every model call and one place to enforce policy, archive for surveillance,
and cap spend. This page compares the realistic shortlist. See each vendor page for sourced detail.

## At a glance

| Vendor | What it really is | Deploy | OSS? | Ownership (2026-06-28) | Best fit |
|---|---|---|---|---|---|
| [[portkey]] | Fast gateway + built-in governance/observability | SaaS or self-hosted | Partial | **Acquired → [[palo-alto-networks]]** (closed 2026-05-29) | Shops standardizing on Prisma AIRS / PANW |
| [[litellm]] | OSS unified API + lightweight proxy (100+ providers) | Self-hosted (or SaaS) | **Yes (core)** | Independent | Teams wanting OSS control, no lock-in |
| [[kong]] | API-gateway lineage extended to AI + MCP | Self-hosted / hybrid | Partial (Kong GW OSS) | Independent (~$2B val, 2024) | Shops already running Kong for APIs |
| [[truefoundry]] | LLMOps platform with a gateway + MCP gateway | Self-hosted / SaaS | Partial | Independent | Teams wanting gateway + deployment/LLMOps in one |
| [[f5]] | App-delivery/security giant; AI gateway + guardrails | Self-hosted / appliance | No | Public (NYSE: FFIV); **acquired [[calypsoai]]** 2025-10 | F5 estates wanting gateway+guardrails together |
| [[cloudflare]] | AI Gateway as part of the edge/CDN platform | SaaS (edge) | No | Public (NYSE: NET) | Cloudflare-native shops, edge inference |
| [[openrouter]] | Hosted **third-party** inference aggregator | SaaS only | No | Independent (~$1.3B val, 2026-05) | Dev/experimentation; **not** for regulated data |

## How to tell them apart

**Pure OSS / control plane you run yourself.** [[litellm]] is the reference open-source gateway —
a unified OpenAI-compatible API over 100+ providers plus a self-hostable proxy with keys, budgets,
and logging. Pick it when you want no vendor lock-in and are comfortable operating it. [[truefoundry]]
and [[kong]] also self-host but bring more platform around the gateway (LLMOps; full API management).

**Gateway bundled into a security platform.** [[portkey]] (now Palo Alto's [[prisma-airs]] gateway
layer) and [[f5]] (with [[calypsoai]] guardrails) are the "gateway + AI firewall in one" plays. If
you're already buying the platform, the gateway comes wired into [[ai-runtime-security]],
observability, and agent identity — fewer integrations, more lock-in. This is the single biggest
2025–26 shift in the category: **two of the strongest independents are now inside platforms.**

**Edge/CDN-native.** [[cloudflare]] AI Gateway is the natural choice if you already run Cloudflare —
caching, rate-limiting, and logging at the edge, close to where inference and Workers run.

**The odd one out.** [[openrouter]] is not a gateway you deploy — it's a **hosted aggregator** that
routes your calls through *its* infrastructure to many models. Great for experimentation and breadth;
**a poor fit for MNPI/PII** because your prompts traverse a third party (data-residency/egress concern).
Rated low hedge-fund fit for that reason.

## The governance angle (what a CTO actually buys this for)

A gateway is where three Day-1 needs converge:
1. **One audit log** of every model call → feeds [[siem-soc]] and [[comms-surveillance]] archival.
2. **Egress control** — it's the lethal-trifecta **egress** chokepoint; bolt [[ai-runtime-security]]
   inspection (prompt-injection, DLP) onto it.
3. **Cost + rate governance** — budgets, quotas, caching to control spend.

If you only deploy one AI-specific control on Day 1, this plus an [[ai-access-governance]]/DLP layer
is the highest-leverage pair. Note the overlap with [[mcp-gateway]]: Kong, TrueFoundry, and Prisma
AIRS also broker **tool/MCP** traffic, not just model calls.

## Survey-design notes
- **Portkey now = Palo Alto.** As an answer option it should read "Portkey (Palo Alto Prisma AIRS)".
- **OpenRouter** answers a different question (hosted aggregator) — respondents may tick it meaning
  "we let devs use it," which is a shadow-AI signal, not an enterprise-gateway deployment.
- LiteLLM is the OSS default to anchor the question; expect high "evaluating" from technical shops.

## Sources
Per-vendor sourcing is on each linked vendor page (funding, ownership, deployment). M&A confirmations
(Portkey→PANW, CalypsoAI→F5) are in [[ai-security-m-and-a-map]].

## History
- [2026-06-28] Created from Phase 3 Wave 2 researched gateway pages.
