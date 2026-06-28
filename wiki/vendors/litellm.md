---
type: vendor
name: LiteLLM
slug: litellm
categories: [ai-gateway]
layer: model-prompt
aliases: [BerriAI]
website: "https://www.litellm.ai/"
founded: 2023
hq: San Francisco, CA, USA
ownership: independent
ownership_detail: Independent, VC-backed (BerriAI); Y Combinator W23. No M&A found as of 2026-06-28.
ownership_confidence: high
funding_total: ~$1.6M (seed, confirmed); aggregators claim up to ~$5M total (unverified)
last_funding: Seed (2023) — YC, Gravity Fund, Pioneer Fund
deployment: [self-hosted, saas, api, sdk, inline-proxy, on-prem]
target_customer: Developers and platform/ML-platform teams; startups through enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [open-source, ai-gateway, llm-proxy, yc]
---

# LiteLLM

> Open-source LLM gateway/proxy (by BerriAI) that lets you call 100+ model providers behind one OpenAI-compatible API, with cost tracking, virtual keys, guardrails, and load balancing. Primary category: [ai-gateway](../categories/ai-gateway.md).

**One-liner** — The popular self-hostable, open-source AI gateway: one OpenAI-compatible endpoint in front of every model provider, so you control spend, keys, and routing from a single chokepoint.

**Categories** — [ai-gateway](../categories/ai-gateway.md)

## What it does

LiteLLM normalizes access to 100+ LLM providers (OpenAI, Anthropic, Google Gemini, AWS Bedrock, Azure OpenAI, Cohere, Vertex AI, Hugging Face, vLLM, NVIDIA NIM, and more) behind a single OpenAI-format API. It ships in two forms:

- a **Python SDK** that translates calls to/from each provider, and
- a **Proxy Server (the "AI Gateway")** — a FastAPI service you run centrally for a team or org.

The proxy gives platform teams the things you want at a single exit door for model traffic: per-key/per-team **virtual keys**, **budget controls and rate limiting** (RPM/TPM), **cost/spend tracking**, **load balancing, fallbacks and caching** across deployments, **logging/observability** (S3/GCS, SIEM and observability integrations), and an admin dashboard. It also supports **guardrails** — PII masking, content filtering and policy enforcement on prompts/responses — natively and via integrations (e.g. Presidio, Bedrock guardrails, Pangea AI Guard).

## Where it sits in the stack

LiteLLM is an [ai-gateway](../categories/ai-gateway.md) in the model/prompt layer. Its core job is to be the **single egress chokepoint** for outbound model traffic — the lethal-trifecta leg it most directly addresses is **egress** (centralizing, authenticating, budgeting and logging every call to external/internal models). It is not primarily an untrusted-input or sensitive-data control, but because the gateway sees every prompt and response it is the natural place to **bolt on guardrails** (PII redaction, content filters), giving it a secondary touch on the sensitive-data and untrusted-input legs. In a trust-zone model it typically lives at the boundary between application zones and external model providers.

## Deployment & architecture

- **SDK** — import as a Python library for direct, in-process provider abstraction.
- **Self-hosted proxy** — deploy the gateway via Docker on your own infra (on-prem or private cloud); this is the common enterprise pattern. Acts as an **inline proxy** for all model calls.
- **Managed/cloud** — a LiteLLM-hosted/cloud option exists for teams that don't want to run it.
- **Integrations** — IdP/SSO (Okta, Azure AD) and JWT auth, RBAC, audit logs; guardrail providers (Presidio, Bedrock, Pangea, etc.); observability/logging sinks (S3, GCS, and LLM-observability tools such as [langfuse](langfuse.md)-style backends). MCP support is part of the broader gateway feature set.

## Positioning & differentiators

LiteLLM is the **de-facto open-source default** in this category: MIT-licensed core, huge adoption (240M+ Docker pulls and 1B+ requests served per its own marketing; ~18k+ GitHub stars; 1,000+ contributors), and very broad provider coverage updated quickly as new models ship. Its differentiator vs commercial gateways is **self-hostability and zero license cost for the core** — you can run the full data path inside your own environment with no vendor in the loop.

Versus neighbors:
- **[portkey](portkey.md)** and **[truefoundry](truefoundry.md)** — commercial gateways with more polished enterprise UX, governance and support out of the box; LiteLLM trades polish for control and openness.
- **[kong](kong.md)** — API-gateway heritage extended to AI; heavier infra platform.
- **[openrouter](openrouter.md)** — a hosted multi-model *routing/billing service* (you send traffic to them), conceptually the opposite of self-hosting LiteLLM.
- **[cloudflare](cloudflare.md)** (AI Gateway) — edge-hosted gateway tied to Cloudflare's network.

Enterprise features (SSO/SAML, RBAC, audit logs, dedicated support, SLAs) sit behind a separate **LiteLLM Commercial License** / Enterprise tier; the gateway core stays free.

## Ownership, funding & M&A

- **Ownership:** Independent, VC-backed. The company is **BerriAI**, a **Y Combinator W23** company; product = LiteLLM. Founders Krrish Dholakia and Ishaan Jaffer. HQ San Francisco. (confidence: high)
- **Funding:** A **~$1.6M seed** round (Y Combinator, Gravity Fund, Pioneer Fund) is well documented. Some aggregators (StartupHub, Tracxn) cite up to ~$5M total and PitchBook ~$2.1M; these are **unverified** against a primary announcement — treat the higher totals as low confidence.
- **M&A:** **No acquisition found** as of 2026-06-28. The stub carried no seed M&A flag; nothing in primary or press sources indicates LiteLLM/BerriAI has been acquired or has acquired anyone. Ownership remains independent.

## CTO / hedge-fund lens

An AI gateway is a **Day-1** control: before any AI go-live you want one auditable exit door for model traffic with keys, budgets, rate limits and logging. LiteLLM is the strongest **open-source** way to get that, which matters to a fund that wants the full prompt/response data path inside its own boundary (no third-party seeing prompts) and dislikes per-token middleman pricing.

Fit is **medium**: excellent if you have a platform/ML-platform engineer comfortable running and patching a fast-moving open-source FastAPI service; less ideal for a lean shop that would rather buy a fully supported, hardened gateway with someone to call — there, the Enterprise tier or a commercial option ([portkey](portkey.md), [truefoundry](truefoundry.md)) may be a better posture. Not a model-risk/SR 11-7 governance tool itself, but its centralized logging and spend/usage records are useful evidence feeding model-risk and audit processes. Validate the Enterprise licensing terms and your patching cadence before standing it up as a production chokepoint.

## Competitors / alternatives

[portkey](portkey.md) · [truefoundry](truefoundry.md) · [kong](kong.md) · [openrouter](openrouter.md) · [cloudflare](cloudflare.md)

## Open questions / to verify

- Exact **total funding** and whether any post-seed round (Series A) has closed — primary announcement not found; aggregators disagree (~$1.6M seed confirmed vs ~$2.1M–$5M claimed).
- Scope and pricing of the managed/cloud offering vs self-hosted Enterprise.
- Precise split of which guardrail/governance features are open-source vs Commercial-License-gated.

## Sources
- [LiteLLM | Y Combinator](https://www.ycombinator.com/companies/litellm) — fetched 2026-06-28 — supports: founded 2023, founders, SF HQ, W23 batch, $1.6M seed (YC/Gravity/Pioneer), product; confidence: high
- [LiteLLM (litellm.ai)](https://www.litellm.ai/) — fetched 2026-06-28 — supports: deployment options (SDK/proxy/cloud/on-prem), enterprise features (SSO, audit logs), guardrails, pricing tiers; confidence: med (vendor/marketing)
- [BerriAI/litellm — GitHub](https://github.com/BerriAI/litellm) — fetched 2026-06-28 — supports: open-source proxy/gateway feature set, 100+ providers, MIT core + Commercial License, guardrails/virtual keys/rate limiting; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2023, SF HQ, founders Krrish Dholakia & Ishaan Jaffer, BerriAI/YC W23, ~$1.6M seed (independent, ownership_confidence high), no M&A. Filled deployment (self-hosted/saas/api/sdk/inline-proxy/on-prem), trifecta_relevance=egress, hedge_fund_fit=medium. Cached 3 sources.
