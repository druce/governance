---
type: vendor
name: Braintrust
slug: braintrust
categories: [llm-observability, ai-red-teaming]
layer: model-prompt
aliases: [Braintrust Data]
website: "https://www.braintrust.dev"
founded: 2023
hq: San Francisco, CA
ownership: independent
ownership_detail: "Independent, VC-backed; Series B $80M Feb 2026 (led by ICONIQ), reported ~$800M valuation"
ownership_confidence: high
funding_total: "~$116M (Series A $36M Oct 2024 + Series B $80M Feb 2026)"
last_funding: "Series B $80M, 2026-02 (led by ICONIQ)"
deployment: [saas, self-hosted, sdk, api]
target_customer: "AI-forward engineering/product teams; enterprise (Notion, Stripe, Vercel, Cloudflare cited)"
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [evals, observability, ci-cd, prompt-management]
---

# Braintrust

> **Researched 2026-06-28.** Primary category: [llm-observability](../categories/llm-observability.md); also [ai-red-teaming](../categories/ai-red-teaming.md) (eval/scoring of model outputs).

**One-liner** — Eval-first observability platform for production AI: log traces, score outputs, turn failures into test cases, and gate releases on evals.

**What it does** — Braintrust unifies trace logging, automated evaluations (LLM-as-a-judge and custom code scorers), prompt management, and dataset curation into one workflow. The signature loop: capture every prompt/tool call in production, score outputs, one-click-convert failures into test cases, and gate CI/CD releases on eval results. Built around a custom database for AI observability data and tuned for long-running, multi-step agents.

**Where it sits in the stack** — Primary home is the [llm-observability](../categories/llm-observability.md) layer; its scoring/red-teaming-style evals also touch [ai-red-teaming](../categories/ai-red-teaming.md). Dev/CI- and ops-time tooling, not an inline runtime firewall — it does not directly break a leg of the lethal trifecta, though eval gates can catch unsafe behavior pre-release. Complements [ai-runtime-security](../categories/ai-runtime-security.md).

**Deployment & architecture** — SDK-based instrumentation, SaaS by default with self-hosting for enterprise. Deep CI/CD integration for eval gating is a core design point. Framework-agnostic.

**Positioning & differentiators** — Known as the eval-first / "make evals a first-class CI gate" platform, contrasted with observability-first tools. Versus [langfuse](langfuse.md) and [arize-phoenix](arize-phoenix.md) it is closed-source and leads with evals rather than OSS tracing; versus [langsmith](langsmith.md) it is framework-neutral and eval-centric; versus [helicone](helicone.md) it is SDK/eval-based not proxy-based. Strong logos (Notion, Stripe, Vercel, Replit, Ramp, Cloudflare) signal traction with AI-native engineering teams.

**Ownership, funding & M&A** — Independent, VC-backed. **Series B $80M announced 2026-02-17, led by ICONIQ** (a16z, Greylock, Elad Gil, basecase participating); press reports ~$800M valuation. Prior $36M Series A (Oct 2024, led by a16z, ~$150M post). Founded 2023 by Ankur Goyal (ex-SingleStore/MemSQL, ex-Figma); HQ San Francisco. No M&A. Confidence: high on round facts; valuation is press-reported (med).

**CTO / hedge-fund lens** — Day-1 if your bar is "no AI ships without passing evals." The CI-gating model fits a fund that wants a promotion gate between experiment and production (ties to [promotion-gates](../categories/promotion-gates.md)). Self-hosting addresses keeping eval data (potential MNPI) in-boundary. Well-funded, so continuity risk is low. Not a governance/SR 11-7 platform by itself — pair with [ai-governance-platform](../categories/ai-governance-platform.md).

**Competitors / alternatives** — [langfuse](langfuse.md), [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [helicone](helicone.md), [datadog](datadog.md), [comet](comet.md), [patronus-ai](patronus-ai.md), [maxim-ai](maxim-ai.md).

**Open questions / to verify**
- Confirm the ~$800M Series B valuation against a primary disclosure (press-reported).
- Self-hosted feature parity vs SaaS.

## Sources
- [Braintrust's Series B (company blog)](https://www.braintrust.dev/blog/announcing-series-b) — fetched 2026-06-28 — supports: $80M Series B, ICONIQ lead, 2026-02-17, positioning, customers; confidence: high (valuation med — press).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (Series B $80M Feb 2026, ICONIQ), filled founding/HQ/funding/deployment; kept dual category (llm-observability + ai-red-teaming). No M&A. `ownership_confidence` low→high.
