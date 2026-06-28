---
type: vendor
name: Promptfoo
slug: promptfoo
categories: [ai-red-teaming, llm-observability]
layer: model-prompt
aliases: [promptfoo]
website: https://www.promptfoo.dev
founded: 2024
hq: San Francisco, CA (US)
ownership: acquired
ownership_detail: "acq. by OpenAI — announced 2026-03-09; terms undisclosed; remains open source, folded into OpenAI Frontier (primary: OpenAI + promptfoo blog)"
ownership_confidence: high
funding_total: ~$23M (pre-acquisition)
last_funding: "Series A $18.4M, Jul 2025 (Insight Partners lead, a16z participation, ~$86M post-money)"
deployment: [self-hosted, sdk, saas, api]
target_customer: developers / AI engineering teams; enterprise (25%+ of Fortune 500 used it)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [open-source, eval, red-teaming, m-and-a]
---

# Promptfoo

> **One-liner** — Popular open-source tool for testing, evaluating, and red-teaming LLM apps; acquired by OpenAI in March 2026 and folded into OpenAI Frontier (stays open source).

**Categories** — [[ai-red-teaming]], [[llm-observability]]

## What it does
Promptfoo is a developer-first, open-source framework for **systematically testing AI applications**: prompt/model evals (compare prompts, models, and RAG configs against test cases and graded assertions), automated **red teaming** (generates adversarial probes for prompt injection, jailbreaks, PII leakage, etc., mapped to frameworks like OWASP LLM Top 10), and **static scanning** of models/configs. You wire it into CI so a model or prompt change can't ship without passing your eval and security suite. It runs locally from a config file (no data leaves your environment by default), which is a big part of why it spread bottom-up among engineers.

## Where it sits in the stack
Primary fit is [[ai-red-teaming]] (build-time adversarial testing / guardrail validation) with heavy overlap into [[llm-observability]] (the eval half). In lethal-trifecta terms it mainly attacks the **untrusted-input** leg — it helps you find where prompt injection and jailbreaks get through *before* production. It's a testing/assurance tool, not an inline runtime control, so it complements rather than replaces an [[ai-runtime-security]] firewall.

## Deployment & architecture
Open-source CLI/SDK (npm), run locally or in CI/CD; config-as-code (YAML). Self-hosted by default; a hosted/enterprise offering adds collaboration, sharing, and continuous monitoring. Integrates with most model providers and gateways via API. No inline proxy.

## Positioning & differentiators
Known as the de-facto open-source eval + red-team tool — huge bottom-up adoption (350k+ developers used it, ~130k monthly active, teams at 25%+ of the Fortune 500, per OpenAI's acquisition post; vendor/acquirer figures). Differs from commercial red-teaming peers like [[mindgard]], [[splxai]], and managed services in that it's free, code-native, and self-hosted; differs from pure eval/observability tools like [[langfuse]], [[braintrust]], and [[patronus-ai]] by bundling security red-teaming into the same harness. Now OpenAI-owned, which colors neutrality for buyers standardizing on non-OpenAI models — though it remains multi-model and open source.

## Ownership, funding & M&A
**Seed flag CONFIRMED.** OpenAI announced it would **acquire Promptfoo on 2026-03-09** (primary: OpenAI's "OpenAI to acquire Promptfoo" post and Promptfoo's own "joining OpenAI" blog; corroborated by CNBC/Bloomberg). Terms undisclosed. Promptfoo's tech integrates into **OpenAI Frontier** (OpenAI's enterprise agent platform) to strengthen agentic security testing; the open-source suite stays open source under its current license and existing customers continue to be supported. Founded 2024 by **Ian Webster (CEO)** and **Michael D'Angelo (CTO)**. Pre-acquisition funding ~$23M, including an $18.4M Series A (Jul 2025, Insight Partners lead, a16z participation, ~$86M post-money). `ownership_confidence: high`.

## CTO / hedge-fund lens
**Day-2, but a cheap and high-value Day-2.** If you build or heavily customize any LLM/agent app, an eval+red-team gate in CI is one of the best-leverage controls you can add, and the OSS version costs nothing to trial. SR 11-7 / model-risk angle: the eval harness produces repeatable, versioned evidence that a model was tested before promotion — useful for [[promotion-gates]] and model-validation documentation. Caveats for a hedge fund: (1) it's a build-time assurance tool, not a runtime guardrail, so it doesn't substitute for [[ai-runtime-security]] or [[ai-access-governance]]; (2) OpenAI ownership is a procurement/neutrality consideration if you're standardizing on competing models. Fit is **medium** — valuable if you develop AI in-house, largely irrelevant if you only consume SaaS assistants.

## Competitors / alternatives
[[mindgard]], [[splxai]], [[patronus-ai]], [[giskard]], [[braintrust]], [[langfuse]], [[guardrails-ai]], [[lakera]].

## Open questions / to verify
- Acquisition close date and any post-close rebrand/integration specifics (only the announcement was public as of 2026-06-28).
- Long-term governance of the open-source license now that it's OpenAI-owned.
- Exact HQ (San Francisco inferred from team/press; confirm).

## Sources
- [Promptfoo is joining OpenAI](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) — fetched 2026-06-28 — supports: acquisition 2026-03-09, founders, OSS commitment, OpenAI Frontier integration; confidence: high
- [OpenAI to acquire Promptfoo](https://openai.com/index/openai-to-acquire-promptfoo/) — fetched 2026-06-28 (403 to bot; content via search + Promptfoo blog) — supports: acquisition, adoption stats; confidence: high
- [CNBC: OpenAI to buy Promptfoo](https://www.cnbc.com/2026/03/09/open-ai-cybersecurity-promptfoo-ai-agents.html) — fetched 2026-06-28 — supports: deal, date; confidence: high
- (cached: `raw/sources/2026-06-28--promptfoo--openai-acquisition.md`)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED OpenAI acquisition (announced 2026-03-09, terms undisclosed, stays open source → OpenAI Frontier); set ownership_confidence high. Founded 2024 (Webster/D'Angelo), ~$23M raised. Added llm-observability as secondary category (eval half). hedge_fund_fit = medium (build-time assurance tool).
