---
type: vendor
name: Patronus AI
slug: patronus-ai
categories: [ai-red-teaming, llm-observability]
layer: model-prompt
aliases: [Patronus, Lynx, Glider]
website: https://www.patronus.ai
founded: 2023
hq: San Francisco, CA
ownership: independent
ownership_detail: VC-backed; $50M Series B (2026-06-25, Greenfield Partners), ~$70M total (no acquisition)
ownership_confidence: high
funding_total: ~$70M
last_funding: Series B $50M (2026-06-25)
deployment: [saas, api]
target_customer: enterprise (Fortune 500) & AI companies
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [untrusted-input, sensitive-data]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [ai-red-teaming, evaluation, hallucination, llm-observability]
---

# Patronus AI

> Automated evaluation and security platform for generative AI — detects LLM
> mistakes (hallucinations, PII leakage, copyright, brand) at scale, "one line of
> code."

**One-liner** — A model-agnostic evaluation/judge platform that scores and flags LLM
outputs for hallucination, accuracy, safety, and compliance failures.

**Categories** — [ai-red-teaming](../categories/ai-red-teaming.md), [llm-observability](../categories/llm-observability.md)

## What it does
Patronus runs automated evaluations against LLM outputs using purpose-built evaluator
models and benchmarks. It detects hallucinations, factual/accuracy errors, PII
leakage, copyright violations, and brand-misalignment, and lets teams add evaluators
"with one line of code." Notable assets include **Lynx** (open hallucination-detection
model), **Glider** (an evaluator/judge model), and research benchmarks **FinanceBench**,
**CopyrightCatcher**, **EnterprisePII**, and the Enterprise Scenarios Leaderboard. As
of its 2026 Series B it is expanding into "Digital World Models" — large-scale
simulation/reliability tooling for autonomous AI systems.

## Where it sits in the stack
Straddles [ai-red-teaming](../categories/ai-red-teaming.md) (adversarial/failure testing) and [llm-observability](../categories/llm-observability.md)
(production evaluation/monitoring) in the model/prompt layer. Lethal-trifecta role:
**untrusted-input** (adversarial eval, jailbreak/safety testing) and **sensitive-data**
(PII-leakage and copyright detection on outputs). It is an offline/async evaluation
and monitoring layer, not an inline blocking firewall.

## Deployment & architecture
SaaS with an API; evaluator models callable as judges in CI/CD and in production
monitoring. Serves Fortune 500s and AI companies processing large eval volumes.
Model- and domain-agnostic.

## Positioning & differentiators
Best known for **hallucination detection and rigorous benchmarks** (FinanceBench is
notable for finance use cases), backed by ex-Meta AI research founders. Competes with
eval/observability platforms [maxim-ai](maxim-ai.md), [braintrust](braintrust.md), [galileo](galileo.md), [arize-phoenix](arize-phoenix.md),
[langsmith](langsmith.md) and red-team testers [haize-labs](haize-labs.md), [mindgard](mindgard.md), [splxai](splxai.md). Its
FinanceBench benchmark is the most directly finance-relevant artifact among these
vendors. The 2026 pivot toward simulation/"world models" pushes it beyond pure text eval.

## Ownership, funding & M&A
Independent, VC-backed. Founded 2023 by ex-Meta researchers Anand Kannappan (CEO) and
Rebecca Qian (CTO); stealth launch Sept 2023. Series A $17M (June 2024, led by Notable
Capital f.k.a. GGV, with Lightspeed, Datadog). **Series B $50M on 2026-06-25 led by
Greenfield Partners** (Notable, Lightspeed, Datadog, Samsung), bringing total to ~$70M.
No seed M&A flag and no acquisition — **ownership confirmed independent** (confidence
high).

## CTO / hedge-fund lens
Day-2. Relevant if you **build LLM/RAG applications** and need quantified evaluation
(hallucination/accuracy/PII) for release gates and SR 11-7 model-risk evidence —
FinanceBench and finance-scenario benchmarks make it more relevant here than most
peers. A fund that only consumes vendor AI assistants does not operate this. Strong
fit for an internal AI/quant team productionizing LLM workflows that need defensible
evaluation documentation.

## Competitors / alternatives
[maxim-ai](maxim-ai.md), [braintrust](braintrust.md), [galileo](galileo.md), [arize-phoenix](arize-phoenix.md), [langsmith](langsmith.md),
[haize-labs](haize-labs.md), [mindgard](mindgard.md), [splxai](splxai.md).

## Open questions / to verify
- How material the "Digital World Models" / simulation pivot is vs. the core eval product.
- Pricing and whether finance benchmarks translate into a packaged finance offering.

## Sources
- [Announcing our $17M Series A (Patronus)](https://www.patronus.ai/blog/announcing-our-17-million-series-a) — fetched 2026-06-28 — supports: what it does, Series A, investors, products/benchmarks; confidence: high (primary).
- [Patronus AI raises $50M Series B (The SaaS News)](https://www.thesaasnews.com/news/patronus-ai-raises-50m-series-b/) — fetched 2026-06-28 — supports: Series B $50M, 2026-06-25, Greenfield, ~$70M total, founders, HQ; confidence: med (press aggregator).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent VC-backed (2023, SF, ex-Meta founders; $17M A 2024, $50M B 2026-06, ~$70M total); no acquisition. Set ownership_confidence high, confidence high, hedge_fund_fit low.
