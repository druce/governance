---
title: Portkey
type: vendor
name: Portkey
slug: portkey
categories: [ai-gateway]
layer: model-prompt
aliases: [Portkey AI]
website: "https://portkey.ai"
founded: 2023
hq: San Francisco, California, USA
ownership: acquired
ownership_detail: "Acquired by Palo Alto Networks — announced 2026-04-30, closed 2026-05-29; terms undisclosed. Becomes the AI Gateway component of Prisma AIRS."
ownership_confidence: high
funding_total: ~$18M (≈$3M seed 2023 + $15M Series A Feb 2026)
last_funding: Series A $15M led by Elevation Capital, announced 2026-02-19 (acquired by PANW ~3 months later)
deployment: [saas, self-hosted, api, inline-proxy]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [egress, untrusted-input]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [ai-gateway, llm-routing, observability, palo-alto, acquired]
---

# Portkey

> Primary category: [ai-gateway](../categories/ai-gateway.md). The AI gateway / control plane Palo Alto Networks bought to anchor Prisma AIRS.

**One-liner** — A high-performance AI gateway and control plane that sits between enterprise apps and model APIs — routing, rate-limiting, caching, governing, and observing LLM traffic — acquired by [palo-alto-networks](palo-alto-networks.md) in May 2026 to become the gateway layer of [prisma-airs](prisma-airs.md).

**What it does** — Portkey is the "single exit door" for model traffic: one API endpoint in front of many model providers, with routing/failover, load balancing, cost and rate controls, prompt/response logging, caching, and guardrail hooks. It markets itself as a unified control plane for production AI and claims to process trillions of tokens per month at the low latency needed for agent-to-agent communication.

**Where it sits in the stack** — Model/prompt-layer [ai-gateway](../categories/ai-gateway.md). As a chokepoint on model egress it primarily controls the **egress** leg of the lethal trifecta (what leaves to which model/provider) and is the natural enforcement point to bolt **untrusted-input** inspection onto. Under PANW it becomes the AI Gateway that feeds Prisma AIRS three capabilities: AI runtime security (traffic inspection), agent identity security, and AI observability.

**Deployment & architecture** — Inline gateway/proxy deployed as SaaS or self-hosted, fronting provider APIs via a unified API; SDKs and an OpenAI-compatible interface; integrates with observability and guardrail tooling. Designed for high-throughput agentic workloads.

**Positioning & differentiators** — Known for combining a fast gateway with built-in governance/observability rather than being a thin proxy. Nearest neighbors: [litellm](litellm.md) (OSS routing), [kong](kong.md) (API-gateway lineage, MCP), [truefoundry](truefoundry.md), [cloudflare](cloudflare.md) AI Gateway, [openrouter](openrouter.md), and [f5](f5.md) (which acquired CalypsoAI). Post-acquisition, Portkey's differentiator is being natively wired into a full AI-security platform.

**Ownership, funding & M&A** — Founded 2023 (Rohit Agarwal, Ayush Garg); HQ San Francisco. Raised ~$3M seed (Lightspeed, 2023) and a **$15M Series A led by Elevation Capital** announced 2026-02-19. **Acquired by [palo-alto-networks](palo-alto-networks.md) — VERIFIED:** intent announced 2026-04-30, acquisition **completed 2026-05-29**; financial terms undisclosed. The seed flag "acq by Palo Alto" is **confirmed against PANW's own completion press release.** Notably, the acquisition came only ~3 months after Portkey's Series A — a fast exit.

**CTO / hedge-fund lens** — An AI gateway is Day-1 if you run LLM apps and want one governed exit door for model traffic (logging, cost control, provider failover, policy). For a fund, Portkey's value is now tied to the Prisma AIRS / PANW roadmap; an independent buyer who wanted a neutral gateway may prefer OSS ([litellm](litellm.md)) or a non-acquired vendor to avoid platform lock-in. Watch for whether Portkey remains usable standalone or only within Prisma AIRS.

**Competitors / alternatives** — [litellm](litellm.md), [kong](kong.md), [truefoundry](truefoundry.md), [cloudflare](cloudflare.md), [openrouter](openrouter.md), [f5](f5.md).

**Open questions / to verify**
- Whether Portkey stays available as a standalone product or only inside Prisma AIRS.
- Continued support for the open-source / self-hosted gateway under PANW.
- Acquisition price (undisclosed).

**Sources**
- [PANW Completes Acquisition of Portkey](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents) — fetched 2026-06-28 — supports: acquired by PANW, closed 2026-05-29, AI gateway role in Prisma AIRS; confidence: high
- [Portkey Raises $15M Series A (Portkey blog)](https://portkey.ai/blog/series-a-funding/) — fetched 2026-06-28 — supports: founded 2023, SF HQ, $15M Series A 2026-02; confidence: high (vendor source for funding)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **CONFIRMED** seed M&A flag: acquired by Palo Alto Networks (announced 2026-04-30, closed 2026-05-29, terms undisclosed) against PANW completion press release. Becomes Prisma AIRS AI Gateway. Established founded 2023, SF HQ, ~$18M total funding incl. $15M Series A (Feb 2026) only ~3 months pre-acquisition. Raised ownership_confidence low->high.
