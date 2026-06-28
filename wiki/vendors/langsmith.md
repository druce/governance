---
type: vendor
name: LangSmith (LangChain)
slug: langsmith
categories: [llm-observability]
layer: model-prompt
aliases: [LangChain]
website: https://www.langchain.com/langsmith
founded: 2023
hq: San Francisco, CA
ownership: independent
ownership_detail: "Product of LangChain (independent, VC-backed); Series B Oct 2025 at $1.25B valuation"
ownership_confidence: high
funding_total: "~$160M across 3 rounds"
last_funding: "Series B $125M, 2025-10 (led by IVP), $1.25B valuation"
deployment: [saas, self-hosted, sdk, api]
target_customer: "AI-native startups to global enterprise (35% of Fortune 500 cited)"
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [observability, evals, agent-engineering, langchain]
---

# LangSmith (LangChain)

> **Researched 2026-06-28.** Primary category: [[llm-observability]].

**One-liner** — LangChain's commercial observability-and-evaluation platform for building, tracing, and improving LLM agents.

**What it does** — LangSmith captures detailed traces of every LLM call, tool call, cost, and latency in an agent, then layers evaluation (LLM-as-a-judge and custom evaluators), a prompt playground, dataset management, and human-in-the-loop annotation on top. It is LangChain's primary revenue product and the natural observability choice if you build on LangChain/LangGraph — though it works independently of those frameworks too.

**Where it sits in the stack** — The [[llm-observability]] layer of the model/prompt tier. Development- and operations-time visibility plus eval; not an inline runtime control, so it does not directly break a leg of the lethal trifecta. Complements [[ai-runtime-security]] and [[ai-gateway]] controls rather than replacing them.

**Deployment & architecture** — SDK-based instrumentation (Python, JS/TS), tightest with LangChain/LangGraph but framework-agnostic. SaaS (LangSmith Cloud) plus self-hosted/enterprise deployment for teams that need traces inside their own boundary. Adjacent "Deployment" product (formerly LangGraph Platform) ships long-running agents on managed infra.

**Positioning & differentiators** — The incumbent tied to the most widely used agent framework; strong for teams already on LangChain. Closed-source SaaS, unlike OSS-first [[langfuse]] and [[arize-phoenix]]. Versus [[braintrust]] it is observability-and-framework-led rather than eval-first; versus [[helicone]] it is SDK-based rather than proxy-based. Framework lock-in is the main critique — LangSmith is most compelling inside the LangChain ecosystem.

**Ownership, funding & M&A** — Independent, VC-backed. LangChain raised a **$125M Series B in Oct 2025 at a $1.25B valuation** (led by IVP; Sequoia, Benchmark, Amplify, plus new CapitalG and Sapphire Ventures), ~$160M total. HQ San Francisco. No M&A; the company is a unicorn-stage independent. Confidence: high.

**CTO / hedge-fund lens** — Day-1 if you are building agents, especially on LangChain/LangGraph. Self-host option matters for a fund that does not want prompts/outputs (potential MNPI) in a third-party cloud. Healthy funding and Fortune 500 traction reduce continuity risk. Not a model-risk/SR 11-7 governance system — pair with an [[ai-governance-platform]]. Watch framework lock-in if you are not committed to LangChain.

**Competitors / alternatives** — [[langfuse]], [[arize-phoenix]], [[braintrust]], [[helicone]], [[datadog]], [[comet]].

**Open questions / to verify**
- Self-hosted/enterprise pricing and exact data-residency guarantees.
- Degree of real framework-neutrality in practice vs LangChain-optimized.

## Sources
- [LangChain raises $125M to build the platform for agent engineering](https://www.langchain.com/blog/series-b) — fetched 2026-06-28 — supports: Series B $125M / $1.25B valuation / Oct 2025, LangSmith positioning, customers, deployment; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (LangChain, Series B Oct 2025, $1.25B), filled HQ/founding/funding/deployment. No M&A. `ownership_confidence` low→high.
