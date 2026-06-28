---
type: vendor
name: Arize Phoenix
slug: arize-phoenix
categories: [llm-observability]
layer: model-prompt
aliases: [Arize AI, Phoenix, Arize AX]
website: https://arize.com
founded: 2020
hq: Berkeley, CA
ownership: independent
ownership_detail: "Arize AI, independent VC-backed; Series C $70M Feb 2025. Phoenix is its open-source library; Arize AX is the commercial SaaS"
ownership_confidence: high
funding_total: "~$135M across 5 rounds"
last_funding: "Series C $70M, 2025-02 (led by Adams Street Partners)"
deployment: [saas, self-hosted, sdk, api]
target_customer: "ML/AI engineering teams; enterprise (Booking.com, Uber, Duolingo, PepsiCo cited)"
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [open-source, observability, evals, ml-monitoring]
---

# Arize Phoenix

> **Researched 2026-06-28.** Primary category: [[llm-observability]].

**One-liner** — Open-source AI observability and evaluation library (Phoenix) from Arize AI, with a commercial enterprise platform (Arize AX) alongside.

**What it does** — Phoenix traces LLM and agent applications, runs evaluations, surfaces failures (hallucinations, retrieval problems, regressions), and helps teams debug and improve output quality. Arize's heritage is classic ML observability (drift, performance monitoring), and Phoenix extended that into the LLM/agent world. Phoenix is OSS and self-hostable; Arize AX is the managed, enterprise-scale commercial product.

**Where it sits in the stack** — The [[llm-observability]] layer of the model/prompt tier. Dev/ops-time tracing and eval, not an inline guardrail, so it does not directly break a leg of the lethal trifecta — but its eval/monitoring helps detect data-leak or injection symptoms. Complements [[ai-runtime-security]] and [[ai-red-teaming]].

**Deployment & architecture** — OpenTelemetry/OpenInference-based SDK instrumentation; Phoenix runs locally or self-hosted, Arize AX is SaaS. Integrations include Azure AI Foundry / AI Studio and most major model and framework providers. Reported >2M monthly downloads for Phoenix (company claim).

**Positioning & differentiators** — Among the strongest OSS-plus-commercial combos in the category, with deeper roots in production ML monitoring than LLM-native startups. Versus [[langfuse]] both are OSS-first and overlap on tracing/evals; Arize brings more mature ML-monitoring lineage. Versus [[braintrust]] it is observability-and-monitoring-led rather than eval-first; versus [[datadog]] it is AI-specialized rather than a general observability suite. Notably, [[datadog]] is itself an investor in Arize's Series C.

**Ownership, funding & M&A** — Independent, VC-backed. **Series C $70M announced 2025-02-20**, led by Adams Street Partners (with M12/Microsoft, Datadog, PagerDuty, OMERS, Sinewave, Industry Ventures, and returning Foundation Capital, Battery, TCV, Swift). ~$135M total across 5 rounds. Founded 2020; HQ Berkeley, CA. No M&A. Confidence: high.

**CTO / hedge-fund lens** — Day-1 for a shop doing RAG or agents that wants both LLM observability and an upgrade path to production ML monitoring. Phoenix OSS lets you keep traces (potential MNPI) self-hosted; Arize AX is the route when you need scale/support. Strong funding and strategic investors lower continuity risk. Not a governance/SR 11-7 system itself — pair with [[ai-governance-platform]].

**Competitors / alternatives** — [[langfuse]], [[langsmith]], [[braintrust]], [[helicone]], [[datadog]], [[comet]], [[fiddler-ai]], [[whylabs]].

**Open questions / to verify**
- Phoenix OSS vs Arize AX feature boundary (what's gated to commercial).
- Independent verification of the >2M downloads figure (vendor claim).

## Sources
- [Arize AI Secures $70M Series C (PR Newswire)](https://www.prnewswire.com/news-releases/arize-ai-secures-70m-series-c-to-fix-ais-biggest-problem-making-llms-and-ai-agents-work-in-the-real-world-302381601.html) — fetched 2026-06-28 — supports: Series C amount/date/investors, Phoenix OSS, customers, founding/HQ; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed independent (Arize AI, Series C Feb 2025 $70M), clarified Phoenix (OSS) vs Arize AX (commercial), filled founding/HQ/funding/deployment. No M&A. `ownership_confidence` low→high.
