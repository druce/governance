---
title: Confident AI (DeepEval)
type: vendor
name: Confident AI (DeepEval)
slug: confident-ai
aka: [DeepEval, DeepTeam, Confident AI platform]
primary_category: llm-observability
also_listed_in: [ai-red-teaming]
website: https://www.confident-ai.com
founded: 2024
hq: San Francisco, CA (US)
ownership_state: independent
owner: null
ownership_note: 'Venture-backed startup (Y Combinator W25). $2.2M seed dated 2025-03-20 by aggregators; YC, Flex Capital, January Capital, Liquid 2, Rebel Fund, Vermilion Cliffs participated (lead unconfirmed). Ships the Apache-2.0 OSS frameworks DeepEval and DeepTeam; monetizes the hosted Confident AI platform. No acquisition or later round found as of 2026-10-26.'
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$2.2M (seed; secondary sources)
last_funding: Seed $2.2M, 2025-03 (YC W25 round)
market_position: {llm-observability: challenger, ai-red-teaming: niche-specialist}
deployment_model: [self-hosted, saas, on-prem]
form_factor: [sdk, platform]
data_leaves_tenancy: partial
integrations: [langchain, langgraph, llamaindex, crewai, pydantic-ai, openai-agents-sdk, google-adk, aws-agentcore, mastra, strands]
mcp_support: server
certifications: [soc2-type2, hipaa]
pricing_model: OSS core + tiered SaaS (free / $200 / $2,000 per month / enterprise)
fs_traction: unverified
target_customer: AI engineering teams that build LLM apps and agents and want test-style evals in CI plus production monitoring
last_verified: 2026-10-26
verify_after: null
tags: [open-source, eval, llm-as-judge, red-teaming, yc]
sources:
  - {claim: yc-batch-founders-founded, url: "https://www.ycombinator.com/companies/confident-ai", date: 2026-10-26, confidence: high}
  - {claim: seed-funding, url: "https://seedtable.com/companies/confident-ai/funding-rounds/seed-2025-03", date: 2025-03-20, confidence: medium}
  - {claim: deepeval-oss-license-features, url: "https://github.com/confident-ai/deepeval", date: 2026-10-26, confidence: high}
  - {claim: deepteam-oss-red-teaming, url: "https://github.com/confident-ai/deepteam", date: 2026-10-26, confidence: high}
  - {claim: pricing-deployment-certs, url: "https://www.confident-ai.com/pricing", date: 2026-10-26, confidence: medium}
  - {claim: telemetry-data-handling, url: "https://deepeval.com/docs/data-privacy", date: 2026-10-26, confidence: high}
---

# Confident AI (DeepEval)

> **One-liner** — The company behind **DeepEval**, a widely used open-source,
> pytest-style LLM evaluation framework, and **DeepTeam**, its open-source red-teaming
> sibling. It sells **Confident AI**, a hosted platform for running those evals, tracing
> production traffic and gating releases.

**Categories** — [llm-observability](../categories/llm-observability.md) (primary),
[ai-red-teaming](../categories/ai-red-teaming.md)

## What it does

Three pieces, one company:

- **DeepEval (OSS, Apache 2.0)** is a Python framework for writing LLM tests the way you
  write unit tests. You write test cases, attach metrics, and run them in CI. It ships
  50+ metrics: LLM-as-judge with custom criteria (G-Eval), RAG metrics (faithfulness,
  answer relevancy, contextual precision/recall), agent metrics (task completion, tool
  correctness, plan quality), multi-turn conversation metrics, hallucination, bias and
  toxicity, and MCP-specific metrics. It runs entirely on your machine. LLM-judge
  metrics call whatever model you configure. About 19.1k GitHub stars (2026-10-26), one
  of the most-starred eval frameworks.
- **DeepTeam (OSS, Apache 2.0)** is built on DeepEval and does automated red teaming of
  LLM apps and agents. It covers 50+ vulnerability types (PII and prompt leakage,
  injection, BOLA/BFLA, SSRF, tool-metadata poisoning, excessive agency) and 20+ attack
  methods, including multi-turn jailbreaks. Results map to OWASP LLM Top 10 2025, OWASP
  Agentic Top 10, NIST AI RMF and MITRE ATLAS. It also has seven simple runtime "guards"
  (prompt injection, privacy, toxicity, topical and others). About 3.1k stars.
- **Confident AI (commercial)** is where `deepeval login` sends results. It provides
  shared test reports, dataset management and production tracing with evals on every
  trace/span/thread. It also does drift alerts, clustering of failing traces into
  failure modes, annotation queues, red-team risk assessments and an org-wide
  **release gate** that blocks releases failing evals or red-team checks. An MCP server
  lets engineers query failing traces from Claude Code or Cursor.

## Where it sits in the stack

Primary fit is [llm-observability](../categories/llm-observability.md). The core product is
evaluation (does the app give correct, grounded, on-policy answers?), with tracing added
on top. The DeepTeam half earns the [ai-red-teaming](../categories/ai-red-teaming.md)
cross-list, since it is pre-production adversarial testing. Its runtime guards are
lightweight and not the main product. It is not an inline firewall or gateway: nothing
here sits in the request path unless you call the guards from your own code.

## Deployment & data handling

- **DeepEval/DeepTeam:** pip packages, run locally or in CI. Your test data stays on your
  machines unless you log in to Confident AI. Two caveats:
  1. LLM-judge metrics send test inputs and outputs to the judge model you configure,
     such as OpenAI or a self-hosted model.
  2. DeepEval sends anonymous usage telemetry (event and metric names, an anonymous ID
     and your public IP) to PostHog by default. Turn it off with
     `DEEPEVAL_TELEMETRY_OPT_OUT=1`.
- **Confident AI platform:** SaaS by default. Data sits in Confident AI's private cloud on
  AWS. The docs name no region or retention period. Enterprise tier offers a "Dedicated
  On-Prem Deployment" (vendor says it can run in your AWS/Azure/GCP) and custom data
  residency (Canada, Australia, Japan named). So `data_leaves_tenancy: partial`: the
  OSS can run fully in-house, while the hosted platform takes prompts, outputs and
  traces off-tenant.
- Out-of-band: evals run in CI or async on traces. No inline latency cost, except for
  DeepTeam guards you choose to call.

## Positioning & differentiators

- **Code-first, test-style evals.** Compared with [langfuse](langfuse.md) and
  [arize-phoenix](arize-phoenix.md), which start from tracing and add evals,
  DeepEval starts from evals (pytest-style assertions in CI) and adds tracing. Closest
  OSS peers in feel: [promptfoo](promptfoo.md) (YAML/CLI-driven, also red teams),
  [comet](comet.md)'s Opik, [trulens](trulens.md) and [giskard](giskard.md).
- **Eval + red team from one vendor, both OSS.** Like [promptfoo](promptfoo.md) and
  [giskard](giskard.md), it pairs quality evals with adversarial testing. Unlike Promptfoo
  (OpenAI acquisition announced 2026-03-09), it is still independent and
  model-neutral.
- **Small company, large OSS footprint.** Commercial peers [braintrust](braintrust.md),
  [galileo](galileo.md) and [patronus-ai](patronus-ai.md) have far larger funding and
  sales teams. Confident AI had about 7 staff on its YC profile and has raised about
  $2.2M. The OSS adoption is real; the enterprise platform is much less proven.

**Position labels:** *challenger* in llm-observability: DeepEval is a default choice
for OSS evals, but the paid platform competes against better-funded Braintrust,
Langfuse and Arize. *niche-specialist* in ai-red-teaming: DeepTeam is a credible free
red-team harness, but it is a side product next to dedicated red-team vendors
([mindgard](mindgard.md), [splxai](splxai.md)).

## Who should choose them / anti-fit

- **Choose** if you have engineers building RAG apps or agents in Python who want
  regression tests for model/prompt changes in CI. You can adopt DeepEval and DeepTeam
  for free and stay self-hosted. Useful for model-risk evidence: versioned, repeatable
  eval runs and red-team reports tied to OWASP/NIST.
- **Anti-fit:**
  - Firms that only consume SaaS assistants (ChatGPT Enterprise, Copilot). There is
    nothing to evaluate.
  - Buyers who want an inline guardrail or firewall. Look at
    [ai-runtime-security](../categories/ai-runtime-security.md) instead.
  - Shops whose procurement needs a vendor with a long track record, large support
    organization or FS references. Confident AI is a tiny seed-stage company, so treat
    the paid platform as vendor-concentration risk and keep the OSS as the fallback.

## Known weaknesses / gotchas

- **Telemetry on by default** in DeepEval (anonymous, but it phones home). Set the
  opt-out variable in regulated environments.
- **Logging in uploads test cases automatically.** Once `deepeval login` is set,
  results go to the Confident AI cloud. Make sure developers don't do this with MNPI or
  client data on the multi-tenant SaaS tier.
- **LLM-as-judge cost and variance.** Most metrics are model-graded, so scores depend on
  the judge model and add API spend.
- **Viability:** seed-stage, small team, no disclosed raise since 2025-03. It is a plausible
  acquisition target (Promptfoo, a comparable OSS eval and red-team tool, agreed to
  be acquired by OpenAI). The Apache-2.0 licence protects the OSS, not the platform.

## Ownership, funding & M&A

Independent. Y Combinator **Winter 2025** batch; founded **2024** per YC (some
profiles say 2023, the year DeepEval first shipped). Founders **Jeffrey Ip (CEO)** and
**Kritin Vongthongsri (CTO)**, San Francisco. **$2.2M seed**, dated 2025-03-20 by CB
Insights/Seedtable, described as oversubscribed and closed in about five days around
W25 Demo Day. Participants: Y Combinator, Flex Capital, January Capital, Liquid 2
Ventures, Rebel Fund, Vermilion Cliffs Ventures and angel Oliver Jung. One profile says
YC led; the lead is unconfirmed. Searches on 2026-10-26 found no Series A, acquisition
or shutdown. Confidence: high on YC/founders (primary), medium on round details
(aggregators only).

## Integrations & partnerships

- Agent and LLM frameworks: LangChain, LangGraph, LlamaIndex, CrewAI, Pydantic AI,
  OpenAI Agents SDK, Google ADK, AWS AgentCore, AI SDK, Mastra, Strands. Model
  providers: OpenAI, Anthropic and others as judges.
- **MCP:** Confident AI exposes an MCP server for IDE agents to query traces and
  datasets, and DeepEval has metrics for evaluating MCP tool use.
- Cloud marketplace: a third-party DeepEval AMI exists on AWS Marketplace. An official
  Confident AI listing was **not** confirmed.

## Compliance & FS traction

- Pricing page shows SOC 2 Type II, HIPAA (Enterprise) and GDPR badges (vendor claims;
  report not reviewed). SSO from the Team tier. No ISO 27001/42001 claim found.
- Named customers or testimonials: Finom (EU SME fintech/banking), Amdocs, RLDatix,
  Humach, Supernormal, plus an unnamed Fortune 500 medical-device firm. No hedge-fund or
  asset-manager reference found. `fs_traction: unverified`.

## Commercial

OSS core is free. Platform (vendor pricing page, 2026-10-26):

| Tier | Price | Includes |
|---|---|---|
| Free | $0 | 2 seats, 1 project, 5 test runs/week |
| Starter | $200/month | 5 projects |
| Team | $2,000/month | Unlimited projects, SSO, 75 GB-months of trace spans |
| Enterprise | Custom | On-prem and data residency |

Trace overage on paid tiers is $1 per GB-month.

## CTO / hedge-fund lens

**Day-2, low cost to try.** If your team builds research copilots or agents, DeepEval in
CI is one of the cheapest ways to catch regressions when you swap models or prompts. Its
eval runs make good SR 11-7-style validation evidence. Start with the OSS, self-hosted,
telemetry off and a judge model inside your tenancy. Treat the hosted platform as an
optional convenience you evaluate against Langfuse or Braintrust, and only after
checking data residency and the vendor's size.

## Open questions / to verify

- Seed round lead investor and any subsequent raise (only aggregators seen; primary
  announcement page returned 403).
- Founding year: 2024 (YC) vs 2023 (DeepEval first release).
- SOC 2 Type II report scope and date; HIPAA claim basis.
- Whether an official AWS Marketplace listing exists (one unconfirmed claim of Aug 2026).
- Hosted-platform AWS region(s) and retention; what "VIP plan" storage means.
- Any FS customers.

## Sources

- [Confident AI — Y Combinator profile](https://www.ycombinator.com/companies/confident-ai) — fetched 2026-10-26 — supports: W25 batch, founded 2024, founders, SF, team size; confidence: high
- [Seedtable: Confident AI seed 2025-03](https://seedtable.com/companies/confident-ai/funding-rounds/seed-2025-03) and [CB Insights profile](https://www.cbinsights.com/company/confident-ai) — search snippets 2026-10-26 — supports: $2.2M seed, 2025-03-20, investors; confidence: medium
- [confident-ai/deepeval (GitHub)](https://github.com/confident-ai/deepeval) — fetched 2026-10-26 — supports: Apache 2.0, metrics, integrations, MCP, stars; confidence: high
- [confident-ai/deepteam (GitHub)](https://github.com/confident-ai/deepteam) — fetched 2026-10-26 — supports: red-teaming scope, framework mappings, guards, built on DeepEval; confidence: high
- [Confident AI pricing](https://www.confident-ai.com/pricing) and [homepage](https://www.confident-ai.com) — fetched 2026-10-26 — supports: tiers/prices, on-prem, residency, certification badges, customer names, release gate (vendor marketing); confidence: medium
- [DeepEval data privacy](https://deepeval.com/docs/data-privacy) — fetched 2026-10-26 — supports: PostHog telemetry and opt-out, AWS storage; confidence: high
- Cached: `raw/sources/2026-10-26--confident-ai--deepeval-deepteam-github.md`, `raw/sources/2026-10-26--confident-ai--funding-yc-pricing.md`

## History

- [2026-10-26] Page created (company slug `confident-ai`; DeepEval and DeepTeam in `aka`). Primary llm-observability, cross-listed ai-red-teaming (DeepTeam confirmed real, Apache 2.0). Verified YC W25 and $2.2M seed (2025-03). Cached 2 sources.
