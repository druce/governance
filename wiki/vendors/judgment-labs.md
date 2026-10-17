---
title: Judgment Labs
type: vendor
name: Judgment Labs
slug: judgment-labs
aka: [Judgment, Judgeval]
primary_category: llm-observability
also_listed_in: []
website: https://www.judgmentlabs.ai/
founded: null
hq: San Francisco, California, USA
ownership_state: independent
owner: null
ownership_note: "VC-backed; $32M combined seed + Series A, both led by Lightspeed Venture Partners (announced 2026-05-12). Founded by three Stanford alumni; founding year not stated in primary sources (aggregators disagree)."
acquisition: {announced: null, closed: null, price: null}
funding_total: "$32M (seed + Series A combined)"
last_funding: "Series A (with seed, $32M combined), Lightspeed lead, announced 2026-05-12"
market_position: {llm-observability: ai-native-disruptor}
deployment_model: [saas]
form_factor: [sdk, platform]
data_leaves_tenancy: unverified
integrations: [opentelemetry, langgraph, openai-agents-sdk, claude-agent-sdk, google-adk, vercel-ai-sdk, litellm, bedrock, vertex-ai, openinference, openllmetry, slack]
mcp_support: server
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: AI-native companies running production agents (startup to growth-stage)
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [agent-evaluation, agent-monitoring, trajectory-analysis, llm-as-judge, open-source-sdk, aie-nyc-2026]
sources:
  - {claim: "$32M combined seed + Series A led by Lightspeed; participants Nova Global, SV Angel, Valor Equity Partners, Dynamic; founders Alex Shan, Andrew Li, Joseph Camyre; HQ San Francisco", url: "https://www.vcaonline.com/news/2026051203/judgment-labs-closes-32m-in-seed-and-series-a-funding-to-build-the-continuous-improvement-layer-for-ai-agents/", date: 2026-05-12, confidence: high}
  - {claim: "Product: behavior tracking flags drift/regressions; Agent Search, Agent Judge, Behavior Discovery, AutoRubrics; Slack investigation agent; MCP access", url: "https://www.judgmentlabs.ai/", date: 2026-10-16, confidence: low}
  - {claim: "Judgeval SDK is Apache-2.0, OpenTelemetry-based tracing, online scoring and replay on historical traces; requires Judgment API key", url: "https://github.com/JudgmentLabs/judgeval", date: 2026-10-16, confidence: high}
  - {claim: "Integrations list, datasets, offline tests, regression tests from production failures, MCP server", url: "https://docs.judgmentlabs.ai/llms.txt", date: 2026-10-16, confidence: high}
  - {claim: "Silver sponsor at AI Engineer New York 2026; no session on agenda", url: "https://ai.engineer/nyc", date: 2026-10-16, confidence: high}
---

# Judgment Labs

> Primary category: [llm-observability](../categories/llm-observability.md).

**One-liner** — Agent-behavior monitoring and evaluation. It traces production agents, runs LLM "judges" over whole trajectories, and finds recurring failure modes and drift. The pitch is that it explains *what the agent did wrong*, not just how long it took and whether it errored.

**What it does** — The open-source **Judgeval** SDK instruments an agent with OpenTelemetry-based tracing. The hosted Judgment platform scores those traces. **Agent Judges** are prompt-based evaluators that run on live traffic (online) or replay over historical traces and versioned datasets (offline tests). **Behavior Discovery** clusters unlabeled production trajectories into failure modes and usage patterns. **Behavior tracking** monitors named behaviors (e.g. "Missed Escalation") and flags drift and regressions. **Agent Search** queries trajectories by behavior rather than keyword. Production failures can be promoted into datasets and regression tests, so fixes can be compared against a baseline before shipping. There is also a Slack-resident investigation agent, a read-only SQL interface, and a CLI plus MCP server so coding agents can query the data. The feature names and the "continuous-improvement stack" framing are **vendor marketing**. The SDK functionality is visible in the Apache-2.0 repository.

**Naming / provenance** — The company is Judgment Labs, the platform is "Judgment", and the OSS SDK is **Judgeval** (`pip install judgeval`). The founders are **Alex Shan** (CEO, ex-Stanford NLP group), **Andrew Li** (Chief Scientist, ex-Together AI) and **Joseph Camyre** (CTO, ex-Datadog). The founding year is not stated in the press release, and aggregators disagree, so it is left null.

**Ownership & viability** — `independent`. On **2026-05-12** the company announced **$32M across seed and Series A, both led by Lightspeed Venture Partners**, with Nova Global, SV Angel, Valor Equity Partners and Dynamic participating. No per-round split was disclosed. The user's hint said "$32M Series A"; more precisely, $32M is the **combined seed and Series A**. The company is well funded for its stage, but early: a small team, and named customers are mostly startups. Acquisition risk is real in a consolidating category (Langfuse went to ClickHouse; see [langfuse](langfuse.md)). Plausible acquirers include APM or observability platforms and AI-platform vendors. The SDK being Apache-2.0 limits lock-in for the tracing layer, but not for the hosted judges and analytics.

**Positioning & differentiators** — `ai-native-disruptor`: a 2026-funded startup positioned on agent trajectory analysis, which the APM incumbents and the first-generation LLM tracers treat as secondary.
- **Versus [langfuse](langfuse.md), [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md):** those are tracing-first, with evals added on top. Judgment leads with evaluation and **behavior discovery across many trajectories**, i.e. surfacing failure classes you didn't know to write an eval for. Whether that discovery is materially better than Arize's or Braintrust's clustering features is unproven publicly.
- **Versus [braintrust](braintrust.md), [patronus-ai](patronus-ai.md), [galileo](galileo.md):** the closest peers in the eval-first space. Judgment's angle is trajectory-level (multi-step, tool-using) judging rather than scoring single outputs.
- **Versus [datadog](datadog.md) / [sentry](sentry.md):** the incumbents give you latency, errors, tokens and cost tied to the rest of the stack. Judgment gives you *quality* signals about agent behavior. They are complementary rather than either-or, and Judgment supports dual export from existing OTel pipelines.
- **No independent benchmark or analyst coverage found**. All differentiation claims trace to the vendor.

**Who should choose them / anti-fit** — Fits a team **running agents in production with real users**, where the pain is "the agent did something dumb and we don't know how often," and which already has basic tracing. **Anti-fit:** a firm that needs a self-hosted or in-tenant deployment today (unverified; see below). A firm that needs vendor-risk evidence (certifications, FS references) that a 2026 startup may not yet have. A firm still at single-prompt chatbot features, where a general tracer like Langfuse is enough.

**Known weaknesses / gotchas** —
- **Agent traces contain whatever the agent saw**: prompts, retrieved documents, tool outputs. For a fund that can include MNPI or client data, and the platform is SaaS-first.
- Self-hosting status is unclear. Older docs pages that described self-hosting and SOC 2 status now return 404 (2026-10-16), and search snippets of them contradict each other.
- LLM-as-judge quality depends on judge calibration, which is your workload, not something the tool removes. The docs provide human labeling and calibration datasets for this.

**Deployment & data handling** — The hosted Judgment platform is the confirmed model. The SDK needs a `JUDGMENT_API_KEY`, and online scoring and SQL run server-side, so trace data, including prompts and outputs, is sent to Judgment. Search snippets of now-removed pages mentioned Enterprise self-hosting or private VPC (one variant needed an AWS account plus Supabase) and, elsewhere, "coming soon". **Treat self-hosting as unverified.** Retention: a snippet cited 14-day span retention on the Pro tier (unverified). Training-use and sub-processor terms were not found. It works out-of-band as SDK and OTLP export, with no inline latency impact on the agent.

**Integrations & partnerships** — OTLP direct export, dual export from existing providers, and OpenInference, OpenLLMetry and OpenLit trace import. Agent frameworks: **LangGraph, OpenAI Agents SDK, Claude Agent SDK, Claude Managed Agents, Google ADK, Vercel AI SDK**, LiveKit, Pipecat. Model providers: Anthropic, OpenAI, Bedrock, Vertex AI, Google, Groq, Together, OpenRouter, Ollama, LiteLLM. An **MCP server** exposes project data and tools to coding agents (Claude, Codex, Cursor). Slack is used for alerts and investigation. It was a Silver sponsor at AI Engineer New York 2026 (no session on the agenda).

**Compliance & FS traction** — **No certification verified.** A search snippet of a now-removed compliance page said SOC 2 Type 1 was complete and Type 2 in progress; confirm directly. No FS customers found. Testimonials come from startups (Monaco, Human Behavior, Contrario, E3 Group, Vigil Labs).

**Commercial** — Not confirmed: the pricing page returned 404 on 2026-10-16. A search snippet of an earlier version listed **Pro at $49/user/month** with usage overages ($8 per 100K spans, $20 per 1,000 evals) and custom Enterprise (low confidence). The SDK itself is free (Apache-2.0).

## Open questions

- Is self-hosted or private-VPC deployment generally available, and on what infrastructure?
- Current SOC 2 status (Type 1 vs Type 2) and the trust portal location.
- Data retention, training-use and sub-processor terms for trace data.
- Current pricing (the published page was offline on 2026-10-16).
- Per-round split of the $32M, and founding year.
- Any FS or regulated-industry customers.

## Sources

- [Judgment Labs closes $32M in seed and Series A (press release via VCA Online, 2026-05-12)](https://www.vcaonline.com/news/2026051203/judgment-labs-closes-32m-in-seed-and-series-a-funding-to-build-the-continuous-improvement-layer-for-ai-agents/) — fetched 2026-10-16 — supports: funding, investors, founders, HQ; confidence: high
- [Judgment Labs homepage](https://www.judgmentlabs.ai/) — fetched 2026-10-16 — supports: product features, MCP access, testimonials; confidence: low (vendor marketing)
- [JudgmentLabs/judgeval (GitHub)](https://github.com/JudgmentLabs/judgeval) — fetched 2026-10-16 — supports: Apache-2.0, OTel tracing, online/offline judging, hosted backend required; confidence: high
- [Judgment docs index (llms.txt)](https://docs.judgmentlabs.ai/llms.txt) — fetched 2026-10-16 — supports: integrations, datasets/offline tests, MCP server; confidence: high
- [AI Engineer New York 2026](https://ai.engineer/nyc) — fetched 2026-10-16 — supports: Silver sponsor; confidence: high
- Cached: `raw/sources/2026-10-16--judgment-labs--funding-product.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
