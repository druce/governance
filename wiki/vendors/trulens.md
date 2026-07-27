---
title: TruLens
type: vendor
name: TruLens
slug: trulens
aka: [TruEra]
primary_category: llm-observability
also_listed_in: []
website: https://www.trulens.org
founded: 2019
hq: Redwood City, California, USA (TruEra, pre-acquisition); TruLens now maintained by Snowflake
ownership_state: acquired-closed
owner: Snowflake
ownership_note: 'Snowflake (NYSE: SNOW) acquired the TruEra AI Observability platform — announced 2024-05-22 as an intent to "acquire certain technology assets and hire key employees from TruEra" (Snowflake Q1 FY2025 earnings release, 8-K EX-99.1). Assets + acqui-hire, not a stock purchase of the company. Closed in the quarter ended 2024-07-31 and on/before 2024-06-24 (Snowflake blog that date: "in the weeks since the acquisition"); exact close date never disclosed. TruEra brand retired; truera.com is a frozen 2024 transition page. TruLens continues as MIT-licensed OSS under Snowflake stewardship and is the engine behind Snowflake Cortex AI Observability (GA 2025-07-31).'
acquisition: {announced: 2024-05-22, closed: 2024-06, price: undisclosed (~$10.8M cash — inferred from an unnamed asset acquisition in Snowflake's FY2025 Q2 10-Q; Snowflake never named TruEra in a filing)}
funding_total: n/a (TruLens is an OSS project; TruEra was VC-backed pre-acquisition — total not verified here)
last_funding: n/a (TruEra assets acquired by Snowflake 2024)
market_position: null
deployment_model: [self-hosted]
form_factor: [sdk, api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: developers / ML & GenAI engineering teams (esp. Snowflake users)
last_verified: 2026-07-27
verify_after: null
tags: [observability, evaluation, open-source, rag, snowflake, acquired]
sources:
  - {claim: acquisition-announced, url: "https://www.sec.gov/Archives/edgar/data/1640147/000164014724000122/fy2025q1earnings.htm", date: 2026-07-27, confidence: high}
  - {claim: acquisition-structure, url: "https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/", date: 2026-07-27, confidence: high}
  - {claim: acquisition-close, url: "https://www.snowflake.com/en/blog/trulens-open-source-ai/", date: 2026-07-27, confidence: medium}
  - {claim: acquisition-price, url: "https://www.sec.gov/Archives/edgar/data/1640147/000164014724000207/snow-20240731.htm", date: 2026-07-27, confidence: medium}
  - {claim: oss-stewardship, url: "https://www.trulens.org", date: 2026-07-27, confidence: high}
  - {claim: cortex-ai-observability-ga, url: "https://docs.snowflake.com/en/release-notes/2025/other/2025-07-31-ai-observability-ga", date: 2026-07-27, confidence: high}
---

# TruLens

> **Researched 2026-06-28; re-verified 2026-07-27 against Snowflake's SEC filings and trulens.org.** Primary category: [llm-observability](../categories/llm-observability.md). **Ownership status corrected 2026-07-27: `acquired-pending` → `acquired-closed`.** The Snowflake/TruEra deal closed in mid-2024 and has been settled fact for two years; the page had been carrying a stale "pending" flag.

**One-liner** — An open-source Python library for evaluating and tracing LLM, RAG, and agent applications, now stewarded by Snowflake.

**TruEra vs TruLens — read this first.** They are not the same thing. **TruEra** was the *commercial* ML/LLM-observability company (Redwood City, founded 2019). **TruLens** was TruEra's *open-source* evaluation library. In 2024 Snowflake bought the TruEra platform and hired the team; the TruEra brand and commercial product were retired, while TruLens survived as an independently released MIT-licensed OSS project that Snowflake now maintains. This page is about the surviving artifact — the OSS library — which is why the slug is `trulens` and not `truera`. If someone hands you a "TruEra" shortlist entry, it is either historical or it means Snowflake Cortex AI Observability.

**What it does** — TruLens instruments an LLM/RAG/agent app and scores it with "feedback functions" — programmatic evaluators for things like context relevance, groundedness, and answer relevance (the "RAG triad"), plus toxicity, bias, and custom criteria. It records traces of each call and surfaces a local dashboard to compare app versions experiment-over-experiment. The job: measure whether your LLM app is actually correct/grounded before and after you ship, without hand-built eval harnesses.

**Where it sits in the stack** — [llm-observability](../categories/llm-observability.md) (model/prompt layer), specifically the **evaluation** sub-segment. Its groundedness/relevance checks touch the **untrusted-input** leg (catching hallucination/injection-driven bad outputs) but TruLens is a measurement/eval library, not an inline guardrail or firewall — it observes, it doesn't block.

**Deployment & architecture** — A pip-installable OSS SDK (**MIT-licensed**, GitHub `truera/trulens` — the repo still sits under the legacy TruEra org, not a Snowflake org) that runs in your own environment; feedback functions can call any model provider as the judge. Ships a Streamlit dashboard for local/self-hosted review. Integrates tightly with the Snowflake ecosystem (Cortex, Arctic, Streamlit) but works standalone with LangChain/LlamaIndex and arbitrary stacks. Verified 2026-07-27: repo active (last push same day, ~3.5k stars, not archived), PyPI `trulens` **2.9.0 released 2026-07-23** on a steady ~6-week cadence through 2026 — Snowflake has *not* folded it into a Cortex-only distribution. (The `trulens` PyPI package dates back to 2020-12-15; the eval-focused `trulens-eval` line began 2023-05-23. `founded: 2019` in frontmatter is TruEra the company, not the library.)

**Positioning & differentiators** — Known as a developer-first, **open-source evaluation** library — lighter and more eval-focused than full hosted observability platforms. The productized, commercial version of this technology now lives inside Snowflake (Cortex AI Observability) rather than being sold as a separate "TruLens" product, so TruLens itself is best understood as the free OSS layer. Nearest neighbors: [arize-phoenix](arize-phoenix.md) (also OSS eval/tracing), [langfuse](langfuse.md) (OSS tracing + evals), [giskard](giskard.md) (OSS testing/red-teaming), [braintrust](braintrust.md) and [comet](comet.md) (Opik).

**Ownership, funding & M&A** — **M&A CONFIRMED AND CLOSED.**

- **Structure — assets + acqui-hire, not a stock purchase.** Snowflake's own Q1 FY2025 earnings release (SEC Form 8-K EX-99.1, filed **2024-05-22**) says it "announced its **intent to acquire certain technology assets and hire key employees from TruEra**." The same-day Snowflake blog calls it a definitive agreement to acquire "the TruEra AI Observability platform" — the platform, not the corporate entity. Co-founders Will Uppington (CEO), Anupam Datta (Chief Scientist) and Shayak Sen (CTO) joined Snowflake, with ~37 employees per contemporaneous press coverage.
- **Closed: 2024-06 (on or before 2024-06-24); exact date never disclosed.** Two independent anchors. (1) Snowflake's 10-Q for the quarter ended **2024-07-31** books a completed business combination in Note 7. (2) Snowflake's **2024-06-24** blog post writes in the past tense — "in the weeks since the acquisition" — while listing shipped TruLens improvements. So the close lands between 2024-05-22 and 2024-06-24. Because the deal was immaterial, Snowflake filed no completion 8-K and none was required.
- **Price: undisclosed; ~$10.8M cash is a high-confidence inference.** The Note 7 entry reads: "the Company acquired certain technology assets and hired key employees from a privately-held company for **$10.8 million in cash**" ($2.5M developed technology, $8.3M goodwill). Snowflake **does not name the counterparty** — but the wording is a verbatim match for its own TruEra press-release language, it falls in the quarter immediately after the announcement, and EDGAR full-text search for "TruEra" across all Snowflake 8-K/10-Q/10-K returns exactly one hit (the 2024-05-22 EX-99.1). Treat as inference, not disclosure. (confidence: medium-high on price; high on the close itself)
- **What happened to each asset.** The TruEra brand is retired and there is no TruEra-branded product for sale; `truera.com` is a frozen 2024 transition page that still reads "TruEra **has agreed to** join Snowflake!" and auto-redirects. The commercial successor is **AI Observability in Snowflake Cortex**, GA **2025-07-31**. TruLens stayed open source: `trulens.org` (checked 2026-07-27) states "Originally created by TruEra" and "**Since TruEra's acquisition by Snowflake, Snowflake now actively oversees and supports the development of TruLens in open source**."

> Seed flag "(Snowflake/TruEra)" verified: correct. TruLens is the surviving OSS project; TruEra was the commercial company whose platform and team Snowflake absorbed in 2024.

> **Why this page said "pending" until 2026-07-27:** the only page still describing the deal in forward-looking language is the abandoned `truera.com` landing page ("has agreed to join"), frozen since 2024. Every live source — Snowflake's filings, Snowflake's blog, trulens.org, and Snowflake's own product docs — treats it as long since done. Do not confuse this with Snowflake's **separate and genuinely pending** 2026 acquisition of [natoma](natoma.md).

**CTO / hedge-fund lens** — Day-1 for any team building RAG/agent apps that wants a cheap, code-first way to prove output quality and groundedness — the OSS library has no license cost. Especially natural if your data already lives in **Snowflake**. It is an engineering tool, not a governance/audit platform: it gives you eval evidence but not the SR 11-7 reporting wrapper that [fiddler-ai](fiddler-ai.md) or [arthur-ai](arthur-ai.md) aim at. Good complement to, not replacement for, a governance layer.

**Competitors / alternatives** — [arize-phoenix](arize-phoenix.md), [langfuse](langfuse.md), [langsmith](langsmith.md), [giskard](giskard.md), [braintrust](braintrust.md), [comet](comet.md), [patronus-ai](patronus-ai.md).

**Open questions / to verify**
- ~~Current degree of separation between the standalone OSS TruLens and Snowflake's commercial Cortex AI Observability offering.~~ **Answered 2026-07-27:** not a fork. Snowflake's docs state "TruLens is the platform that Snowflake uses to track your applications" and require `trulens-core`, `trulens-connectors-snowflake` and `trulens-providers-cortex` ≥ 2.1.2. Cortex AI Observability is a managed deployment of the same OSS library with Snowflake-table-backed storage.
- ~~Whether Snowflake continues independent TruLens releases vs folding it into Cortex.~~ **Answered 2026-07-27:** independent releases continue — PyPI 2.9.0 on 2026-07-23.
- Exact close date of the TruEra transaction (never disclosed; bounded to 2024-05-22 → 2024-06-24). Low priority — unlikely ever to be published.

## Sources
- [Snowflake Q1 FY2025 earnings release (SEC 8-K EX-99.1, 2024-05-22)](https://www.sec.gov/Archives/edgar/data/1640147/000164014724000122/fy2025q1earnings.htm) — fetched 2026-07-27 — supports: announce date, **deal structure ("certain technology assets and … key employees")**; confidence: high (primary, SEC).
- [Snowflake Form 10-Q, quarter ended 2024-07-31 (Note 7, Business Combinations)](https://www.sec.gov/Archives/edgar/data/1640147/000164014724000207/snow-20240731.htm) — fetched 2026-07-27 — supports: close within the quarter, ~$10.8M cash (counterparty unnamed — inference); confidence: medium (primary but not name-matched).
- [Snowflake to Acquire TruEra AI Observability Platform](https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/) — fetched 2026-06-28, re-checked 2026-07-27 — supports: acquirer, date (2024-05-22), founders; confidence: high (primary, acquirer).
- [TruLens ❤️ Snowflake OSS (2024-06-24)](https://www.snowflake.com/en/blog/trulens-open-source-ai/) — fetched 2026-06-28, re-checked 2026-07-27 — supports: **close on/before 2024-06-24** ("in the weeks since the acquisition"), OSS commitment; confidence: high (primary).
- [trulens.org](https://www.trulens.org) — fetched 2026-07-27 — supports: "Originally created by TruEra"; Snowflake "now actively oversees and supports the development of TruLens in open source"; confidence: high (project site).
- [AI Observability in Snowflake Cortex — GA 2025-07-31](https://docs.snowflake.com/en/release-notes/2025/other/2025-07-31-ai-observability-ga) and [AI Observability docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability) — fetched 2026-07-27 — supports: commercial successor product, TruLens as its engine; confidence: high (primary).
- [truera/trulens (GitHub)](https://github.com/truera/trulens) — fetched 2026-06-28, re-checked 2026-07-27 — supports: OSS library, eval/tracing scope, **MIT license**, active development; confidence: high.
- Cached: `raw/sources/2026-07-27--trulens--snowflake-truera-closed.md`.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; CONFIRMED Snowflake acquired TruEra (creators of TruLens), announced 2024-05-22; TruLens remains open source under Snowflake. Set ownership=acquired, confidence high. Seed flag verified correct.
- [2026-07-27] Re-verified against SEC filings and live sites. **Corrected stale `ownership_state: acquired-pending` → `acquired-closed`**: the deal closed in **2024-06 (on/before 2024-06-24)**, per Snowflake's 10-Q for the quarter ended 2024-07-31 and its 2024-06-24 blog ("in the weeks since the acquisition"). Established the deal **structure**: an asset purchase + acqui-hire ("certain technology assets and … key employees from TruEra", Snowflake 8-K EX-99.1 2024-05-22), not a stock purchase — which is why the TruEra entity/brand simply disappeared. Added inferred price **~$10.8M cash** from the unnamed Note 7 business combination (flagged as inference; Snowflake never names TruEra in any filing — EDGAR full-text search returns exactly one "TruEra" hit). **Corrected license: MIT, not Apache.** Confirmed TruLens is still independently released OSS (PyPI 2.9.0, 2026-07-23) and is the engine under Snowflake Cortex AI Observability (GA 2025-07-31). Clarified the TruEra-vs-TruLens relationship up front, kept the slug as `trulens`, and cross-noted the unrelated, still-pending Snowflake/[natoma](natoma.md) deal. `last_verified` → 2026-07-27; `verify_after` → null; added frontmatter `sources:`. 1 new source cached.
