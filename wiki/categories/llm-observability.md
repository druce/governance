---
title: LLM Observability & Evaluation
type: category
name: LLM Observability & Evaluation
slug: llm-observability
layer: model-prompt
priority: day-1
trifecta_role: none-detection
maps_to_seed_doc: LLM Observability & Evaluation
maps_to_seed_csv: LLM Observability & Eval
vendor_count: 13
status: drafted
last_updated: 2026-06-28
---

# LLM Observability & Evaluation

## Business objective

The flight recorder for your AI. LLM observability traces what a model actually did
in production — the prompt, the retrieved context, the tool calls, the response,
the latency, the token spend — so you can debug failures, watch quality drift, and
control cost. The "evaluation" half is the offline complement: scored test suites
and regression checks that tell you whether a prompt or model change made things
better or worse before you ship it. Most platforms also serve as a central **prompt
repository / version store**.

In plain terms: observability answers "what is my AI doing and what is it costing
me," and evaluation answers "is this version actually good." Together they are how
you keep an LLM app reliable and explainable rather than a black box.

## When you need it

Day-1, and deliberately lightweight — you want it from launch because it's far
cheaper to instrument early than to retrofit. Even a single RAG app or copilot
benefits immediately from traces (to debug) and evals (to avoid regressions). For a
hedge-fund CTO the trace log doubles as an audit and cost-control artifact, and the
eval harness is the evidence trail that supports model-risk review under
[ai-governance-platform](ai-governance-platform.md) / SR 11-7. This is monitoring, not enforcement — pair it
with [ai-runtime-security](ai-runtime-security.md) for blocking.

## Lethal-trifecta role

Detection and visibility, not enforcement — it does not break a leg of the
trifecta. Its role is to *see* everything (the green-zone instrumentation that makes
the other controls auditable and tunable): it surfaces the evidence that a prompt
injection happened or that sensitive data appeared in output, which feeds the
guardrails and red-teaming that actually block. Treat it as the eyes, not the
bouncer.

## Vendors

**Tracing / observability-first (often OSS or OSS-core)**
- [langfuse](../vendors/langfuse.md) — open-source LLM observability + prompt management; a common default.
- [langsmith](../vendors/langsmith.md) — LangChain's tracing/eval platform, tightly coupled to that ecosystem.
- [arize-phoenix](../vendors/arize-phoenix.md) — Arize's open-source tracing/eval (OpenTelemetry-based); pairs with its enterprise monitoring.
- [helicone](../vendors/helicone.md) — lightweight proxy-based observability and cost tracking.
- [comet](../vendors/comet.md) — Opik, Comet's open-source LLM eval/observability alongside its ML-experiment heritage.
- [trulens](../vendors/trulens.md) — open-source RAG/agent evaluation framework (TruEra/Snowflake lineage).

**Evaluation / testing-first**
- [braintrust](../vendors/braintrust.md) — eval-and-experimentation platform for LLM apps (cross-listed in [ai-red-teaming](ai-red-teaming.md)).
- [giskard](../vendors/giskard.md) — open-source testing/eval for ML and LLMs (cross-listed in [ai-red-teaming](ai-red-teaming.md)).

**Enterprise monitoring / explainability / model-risk-leaning**
- [datadog](../vendors/datadog.md) — LLM observability inside the broader Datadog APM/monitoring suite.
- [weights-and-biases](../vendors/weights-and-biases.md) — Weave, W&B's LLM tracing/eval alongside its experiment-tracking platform.
- [fiddler-ai](../vendors/fiddler-ai.md) — model monitoring and explainability (cross-listed in [ai-governance-platform](ai-governance-platform.md)).
- [arthur-ai](../vendors/arthur-ai.md) — model/LLM monitoring and guardrails (cross-listed in [ai-governance-platform](ai-governance-platform.md)).
- [whylabs](../vendors/whylabs.md) — data/ML and LLM monitoring (drift, quality).

## Consolidation / M&A dynamics

Per seed flags (unverified — to confirm in research): Weights & Biases flagged as
acquired by CoreWeave. Broader dynamics: observability is bifurcating — OSS-core
startups (Langfuse, Phoenix, Helicone, Opik) competing on developer adoption, while
incumbents fold LLM observability into existing suites (Datadog into APM, W&B into
its ML platform). Evaluation increasingly bleeds into [ai-red-teaming](ai-red-teaming.md) (Braintrust,
Giskard, Galileo, Patronus, Maxim all do "evals") and monitoring bleeds into
[ai-governance-platform](ai-governance-platform.md) (Fiddler, Arthur).

## Adjacent categories

- [ai-red-teaming](ai-red-teaming.md) — shares the "evaluation" surface; offline evals and red-team tests overlap heavily, and several vendors (Braintrust, Giskard, Galileo, Patronus, Maxim) sit in both.
- [ai-gateway](ai-gateway.md) — emits the traces/logs observability consumes; some gateways ship their own observability.
- [ai-governance-platform](ai-governance-platform.md) — consumes eval/monitoring evidence for model-risk and regulator reporting; explainability vendors (Fiddler, Arthur) straddle both.
- [ai-runtime-security](ai-runtime-security.md) — the enforcement layer that acts on what observability reveals.

## Survey

**Question:** Which LLM observability and evaluation tools are you using or evaluating
to trace, debug, evaluate, and monitor your AI applications?

**Answer options:** Langfuse, LangSmith, Arize Phoenix, Braintrust, Helicone,
Datadog LLM Observability, Weights & Biases (Weave), Comet (Opik), Fiddler AI,
TruLens, WhyLabs, Arthur AI, Giskard, Other (Please Specify).

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:**
- Table-stakes / highest adoption: Langfuse, LangSmith, Arize Phoenix; Datadog for shops already on Datadog.
- Strong split between observability-first (Langfuse, Helicone, Datadog) and eval-first (Braintrust, Giskard) tools — respondents using both may answer twice; the question stem should make clear it's multi-select.
- Overlap with [ai-red-teaming](ai-red-teaming.md) (Braintrust, Giskard) and [ai-governance-platform](ai-governance-platform.md) (Fiddler, Arthur) will confuse some respondents about where to place a tool.
- Promptfoo (an OSS eval/red-team tool, flagged → OpenAI) is filed under [ai-red-teaming](ai-red-teaming.md) but some respondents will expect it here.

## Open taxonomy questions

- Observability vs evaluation vs red-teaming: the seed CSV split observability/eval from red-teaming/guardrails, but the vendor lists overlap heavily. Are these one category or three? Currently kept as observability+eval here and guardrails+red-team in [ai-red-teaming](ai-red-teaming.md).
- Do explainability/monitoring vendors (Fiddler, Arthur) belong primarily here or in [ai-governance-platform](ai-governance-platform.md)?
