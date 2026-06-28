---
type: vendor
name: Helicone
slug: helicone
categories: [llm-observability]
layer: model-prompt
aliases: []
website: "https://www.helicone.ai"
founded: 2023
hq: San Francisco, CA
ownership: acquired
ownership_detail: "Acquired by Mintlify (announced 2026-03-03); Helicone product now in maintenance mode, founders joined Mintlify"
ownership_confidence: high
funding_total: "pre-seed/seed stage (small; YC W23)"
last_funding: "Pre-seed/seed (pre-acquisition); acquired by Mintlify 2026-03"
deployment: [saas, self-hosted, inline-proxy, api]
target_customer: "developers / engineering teams (~16,000 organizations cited)"
hedge_fund_fit: low
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [open-source, observability, proxy, ai-gateway, yc-w23, maintenance-mode]
---

# Helicone

> **Researched 2026-06-28.** Primary category: [llm-observability](../categories/llm-observability.md).

**One-liner** — Open-source, proxy-based LLM observability and AI gateway — one line of code to monitor LLM usage; acquired by Mintlify and now in maintenance mode.

**What it does** — Helicone sits as a proxy between your app and LLM providers: change one line (point your base URL at Helicone) and it logs every request/response, cost, latency, and usage, with caching, rate-limiting, and a unified gateway to 100+ models via an OpenAI-compatible endpoint. The low-friction proxy model was its signature. It processed ~14.2 trillion tokens across ~16,000 organizations.

**Where it sits in the stack** — The [llm-observability](../categories/llm-observability.md) layer; its gateway features also overlap [ai-gateway](../categories/ai-gateway.md). As a proxy it sits on the model-traffic path, but it is an observability/routing layer, not a security firewall — it does not by itself break a leg of the lethal trifecta. Adjacent to [litellm](litellm.md), [portkey](portkey.md), [openrouter](openrouter.md) on the gateway side.

**Deployment & architecture** — Inline proxy (the default, one-line integration), plus async logging SDK option; self-hostable OSS or Helicone Cloud SaaS. Integrates with OpenAI, Anthropic, Azure, and other providers at the API layer.

**Positioning & differentiators** — Best known for the proxy-based, one-line-change integration — the lowest-friction onboarding in the category and a combined observability + gateway pitch. Contrast with SDK/OTel-based [langfuse](langfuse.md), [arize-phoenix](arize-phoenix.md), [langsmith](langsmith.md) (more eval depth, deeper instrumentation) and eval-first [braintrust](braintrust.md). The proxy model adds a network hop on the critical path, a tradeoff for the convenience.

**Ownership, funding & M&A** — **Acquired by Mintlify, announced 2026-03-03** (confirmed via both companies' blogs). Founders Justin Torre and Cole Gottdank joined Mintlify in San Francisco; the Helicone product remains live but in **maintenance mode** (security patches, new-model support, bug fixes only — active feature development ended). Founded 2023 (YC W23), HQ San Francisco; funding was early-stage/small. Confidence: high.

**CTO / hedge-fund lens** — The maintenance-mode status makes Helicone a **weak choice for a new Day-1 deployment** — you would be adopting a frozen product. Of interest mainly to teams already on it (self-hosted OSS can keep running) or studying the proxy pattern. For new builds prefer an actively developed alternative. The inline-proxy model also means LLM traffic (potentially MNPI) flows through Helicone unless self-hosted — self-host if you adopt it at all.

**Competitors / alternatives** — [langfuse](langfuse.md), [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [datadog](datadog.md), [comet](comet.md), [litellm](litellm.md), [portkey](portkey.md).

**Open questions / to verify**
- Long-term fate of Helicone Cloud SaaS under Mintlify (how long it stays live).
- Whether the OSS repo continues to receive community contributions.

## Sources
- [Helicone is joining Mintlify (Helicone blog)](https://www.helicone.ai/blog/joining-mintlify) — fetched 2026-06-28 — supports: acquisition by Mintlify 2026-03-03, maintenance mode, proxy model, scale, founders; confidence: high.
- [Mintlify acquires Helicone (Mintlify blog)](https://www.mintlify.com/blog/mintlify-acquires-helicone) — fetched 2026-06-28 — supports: acquisition confirmation/rationale; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Helicone acquired by Mintlify (2026-03-03, confirmed), product now maintenance-mode — changed `ownership` independent→acquired (confidence low→high), set hedge_fund_fit low for new deployments; filled founding/HQ/proxy deployment. No seed M&A flag existed but acquisition found and recorded.
