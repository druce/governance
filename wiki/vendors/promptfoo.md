---
title: Promptfoo
type: vendor
name: Promptfoo
slug: promptfoo
aka: [promptfoo]
primary_category: ai-red-teaming
also_listed_in: [llm-observability]
website: https://www.promptfoo.dev
founded: 2024
hq: San Francisco, CA (US)
ownership_state: acquired-pending
owner: OpenAI
ownership_note: 'OpenAI announced an agreement to acquire Promptfoo 2026-03-09; terms undisclosed. Both parties used pending language ("to acquire" / "has agreed to be acquired") and both posts state "The closing of the acquisition is subject to customary closing conditions." No completion announcement from either side as of 2026-07-27, and neither is an SEC filer — treated as pending, not closed. Intended to remain open source and fold into OpenAI Frontier.'
acquisition: {announced: 2026-03-09, closed: null, price: null}
funding_total: ~$23M (pre-acquisition)
last_funding: Series A $18.4M, Jul 2025 (Insight Partners lead, a16z participation, ~$86M post-money)
market_position: null
deployment_model: [self-hosted, saas]
form_factor: [sdk, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: developers / AI engineering teams; enterprise (25%+ of Fortune 500 used it)
last_verified: 2026-07-27
verify_after: 2026-10-01
tags: [open-source, eval, red-teaming, m-and-a]
---

# Promptfoo

> **One-liner** — Popular open-source tool for testing, evaluating, and red-teaming LLM apps; OpenAI agreed to acquire it in March 2026, to be folded into OpenAI Frontier (stays open source). The deal has not been publicly confirmed as closed.

**Categories** — [ai-red-teaming](../categories/ai-red-teaming.md), [llm-observability](../categories/llm-observability.md)

## What it does
Promptfoo is a developer-first, open-source framework for **systematically testing AI applications**: prompt/model evals (compare prompts, models, and RAG configs against test cases and graded assertions), automated **red teaming** (generates adversarial probes for prompt injection, jailbreaks, PII leakage, etc., mapped to frameworks like OWASP LLM Top 10), and **static scanning** of models/configs. You wire it into CI so a model or prompt change can't ship without passing your eval and security suite. It runs locally from a config file (no data leaves your environment by default), which is a big part of why it spread bottom-up among engineers.

## Where it sits in the stack
Primary fit is [ai-red-teaming](../categories/ai-red-teaming.md) (build-time adversarial testing / guardrail validation) with heavy overlap into [llm-observability](../categories/llm-observability.md) (the eval half). Its focus is **untrusted input** — it helps you find where prompt injection and jailbreaks get through *before* production. It's a testing/assurance tool, not an inline runtime control, so it complements rather than replaces an [ai-runtime-security](../categories/ai-runtime-security.md) firewall.

## Deployment & architecture
Open-source CLI/SDK (npm), run locally or in CI/CD; config-as-code (YAML). Self-hosted by default; a hosted/enterprise offering adds collaboration, sharing, and continuous monitoring. Integrates with most model providers and gateways via API. No inline proxy.

## Positioning & differentiators
Known as the de-facto open-source eval + red-team tool — huge bottom-up adoption (350k+ developers used it, ~130k monthly active, teams at 25%+ of the Fortune 500, per OpenAI's acquisition post; vendor/acquirer figures). Differs from commercial red-teaming peers like [mindgard](mindgard.md), [splxai](splxai.md), and managed services in that it's free, code-native, and self-hosted; differs from pure eval/observability tools like [langfuse](langfuse.md), [braintrust](braintrust.md), and [patronus-ai](patronus-ai.md) by bundling security red-teaming into the same harness. Now OpenAI-owned, which colors neutrality for buyers standardizing on non-OpenAI models — though it remains multi-model and open source.

## Ownership, funding & M&A
**Seed flag CONFIRMED as announced — but the deal is pending, not closed.** OpenAI announced an agreement to **acquire Promptfoo on 2026-03-09** (primary: OpenAI's "OpenAI to acquire Promptfoo" post and Promptfoo's own "joining OpenAI" blog; corroborated by CNBC's "OpenAI to buy Promptfoo"). Both parties used unambiguously *pending* language — OpenAI's post says "**Once the acquisition is finalized** we will integrate Promptfoo's technology directly into OpenAI Frontier", Promptfoo's says it "**has agreed to be acquired**", and both carry the rider "The closing of the acquisition is subject to customary closing conditions." Watch for headline noise: TechCrunch and Forbes ran "OpenAI *acquires* Promptfoo" headlines whose body copy still said "once the deal closes."

**No completion has ever been publicly announced.** Neither party is an SEC filer, so no filing is owed and this may remain permanently unconfirmed. Corporate artifacts as of 2026-07-27 are all still standalone-Promptfoo — GitHub org untransferred with a co-founder still a public member, LICENSE still "Copyright (c) Promptfoo 2025", active commits under the promptfoo org, and a "© 2026 Promptfoo, Inc." site footer with no OpenAI branding. That is circumstantial rather than dispositive (an acquirer may leave all of it untouched post-close), but combined with the absence of any completion notice it does not support an `acquired-closed` state. Terms undisclosed. Promptfoo's tech integrates into **OpenAI Frontier** (OpenAI's enterprise agent platform) to strengthen agentic security testing; the open-source suite stays open source under its current license and existing customers continue to be supported. Founded 2024 by **Ian Webster (CEO)** and **Michael D'Angelo (CTO)**. Pre-acquisition funding ~$23M, including an $18.4M Series A (Jul 2025, Insight Partners lead, a16z participation, ~$86M post-money). `ownership_confidence: high`.

## CTO / hedge-fund lens
**Day-2, but a cheap and high-value Day-2.** If you build or heavily customize any LLM/agent app, an eval+red-team gate in CI is one of the best-leverage controls you can add, and the OSS version costs nothing to trial. SR 11-7 / model-risk angle: the eval harness produces repeatable, versioned evidence that a model was tested before promotion — useful for [promotion-gates](../categories/promotion-gates.md) and model-validation documentation. Caveats for a hedge fund: (1) it's a build-time assurance tool, not a runtime guardrail, so it doesn't substitute for [ai-runtime-security](../categories/ai-runtime-security.md) or [ai-access-governance](../categories/ai-access-governance.md); (2) OpenAI ownership is a procurement/neutrality consideration if you're standardizing on competing models. Fit is **medium** — valuable if you develop AI in-house, largely irrelevant if you only consume SaaS assistants.

## Competitors / alternatives
[mindgard](mindgard.md), [splxai](splxai.md), [patronus-ai](patronus-ai.md), [giskard](giskard.md), [braintrust](braintrust.md), [langfuse](langfuse.md), [guardrails-ai](guardrails-ai.md), [lakera](lakera.md).

## Open questions / to verify
- **Whether the OpenAI deal has closed at all.** As of 2026-07-27 no completion announcement exists from either party and neither files with the SEC, so there may never be a public close date. Re-check by `verify_after: 2026-10-01`; if nothing surfaces, consider whether `acquired-pending` should persist indefinitely or the page should say the close is unknowable.
- Any post-close rebrand/integration specifics into OpenAI Frontier.
- Long-term governance of the open-source license now that it's OpenAI-owned.
- Exact HQ (San Francisco inferred from team/press; confirm).

## Sources
- [Promptfoo is joining OpenAI](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) — fetched 2026-06-28 — supports: acquisition 2026-03-09, founders, OSS commitment, OpenAI Frontier integration; confidence: high
- [OpenAI to acquire Promptfoo](https://openai.com/index/openai-to-acquire-promptfoo/) — fetched 2026-06-28 (403 to bot; content via search + Promptfoo blog) — supports: acquisition, adoption stats; confidence: high
- [CNBC: OpenAI to buy Promptfoo](https://www.cnbc.com/2026/03/09/open-ai-cybersecurity-promptfoo-ai-agents.html) — fetched 2026-06-28 — supports: deal, date; confidence: high
- (cached: `raw/sources/2026-06-28--promptfoo--openai-acquisition.md`)
- **Close-status check, 2026-07-27** — re-read OpenAI's announcement post, Promptfoo's blog, promptfoo.dev, the promptfoo GitHub org/LICENSE, and post-announcement trade press across five query framings; found the "subject to customary closing conditions" rider on both primary posts and **no** completion announcement anywhere. Supports: deal is pending, `closed` should be null; confidence: high on the pending framing, and this is a searched-and-not-found on the close, not proof the deal failed. Cached: `raw/sources/2026-07-27--promptfoo--openai-deal-close-status.md`

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED OpenAI acquisition (announced 2026-03-09, terms undisclosed, stays open source → OpenAI Frontier); set ownership_confidence high. Founded 2024 (Webster/D'Angelo), ~$23M raised. Added llm-observability as secondary category (eval half). hedge_fund_fit = medium (build-time assurance tool).
- [2026-07-27] Date-sanity sweep — **corrected `acquired-closed` → `acquired-pending` and removed a fabricated close date**. `closed` was 2026-03-09, an exact copy of the announcement date, while the page's own Open Questions admitted "only the announcement was public" and the body said OpenAI "announced it *would* acquire" — the frontmatter asserted a close the rest of the page denied. Re-checked both primary posts: OpenAI's is titled "OpenAI **to** acquire Promptfoo" and says "once the acquisition is finalized"; Promptfoo's says it "has **agreed** to be acquired"; both state "The closing of the acquisition is subject to customary closing conditions." No completion announcement exists from either side, and neither is an SEC filer, so no close date may ever be public. Set `closed: null`, added `verify_after: 2026-10-01` (required for `acquired-pending`), and rewrote the ownership note, body and open questions to say the close is *not publicly confirmed* rather than merely undocumented. `price` left null — the ~$86M figure in circulation is the Jul 2025 post-money valuation, not a deal price. Cached 1 new source.
