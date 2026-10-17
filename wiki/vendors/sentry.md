---
title: Sentry
type: vendor
name: Sentry
slug: sentry
aka: [Functional Software, Sentry Agent Monitoring, Sentry AI Agent Monitoring, Sentry Agent Tracing]
primary_category: llm-observability
also_listed_in: []
website: https://sentry.io/
founded: 2012
hq: San Francisco, California, USA
ownership_state: independent
owner: null
ownership_note: "Functional Software, Inc. (d/b/a Sentry), privately held, VC-backed. Last disclosed round: $90M Series E (BOND, Accel co-lead) at >$3B valuation, 2022-05-04; ~$217M total raised. No later round found."
acquisition: {announced: null, closed: null, price: null}
funding_total: "~$217M (as of 2022-05)"
last_funding: "Series E $90M, 2022-05-04"
market_position: {llm-observability: platform-module}
deployment_model: [saas, self-hosted]
form_factor: [sdk, platform]
data_leaves_tenancy: partial
integrations: [openai, anthropic, google-genai, langchain, langgraph, openai-agents-sdk, pydantic-ai, litellm, vercel-ai-sdk, huggingface, mcp]
mcp_support: server
certifications: [soc2-type2]
pricing_model: platform
fs_traction: unverified
target_customer: software teams already using Sentry for errors/performance, startup to enterprise
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [apm, error-monitoring, agent-tracing, incumbent, fair-source, aie-nyc-2026]
sources:
  - {claim: "AI Agent Monitoring open beta / major upgrade 2025-06-26: tracing, tool visibility, model performance, error grouping, available to all users", url: "https://sentry.io/changelog/ai-agent-monitoring--open-beta/", date: 2025-06-26, confidence: high}
  - {claim: "Current agent monitoring: agent runs, tool calls, handoffs; Conversations/Traces/LLM Calls views; model cost dashboards; MCP server monitoring", url: "https://docs.sentry.io/ai/monitoring", date: 2026-10-16, confidence: high}
  - {claim: "Python AI integrations auto-enabled: Anthropic, Google GenAI, HF Hub, OpenAI, OpenAI Agents, LangChain, LangGraph, Pydantic AI, MCP; manual: LiteLLM, Mistral", url: "https://docs.sentry.io/platforms/python/integrations/", date: 2026-10-16, confidence: high}
  - {claim: "sendDefaultPii controls prompt/output capture; gen_ai message and tool attributes not scrubbed server-side by default", url: "https://docs.sentry.io/product/insights/ai/agents/privacy/", date: 2026-10-16, confidence: high}
  - {claim: "Plans Developer free / Team $29 / Business $89 / Enterprise custom; 5M spans included; agent tracing on all plans; Seer add-on", url: "https://sentry.io/pricing/", date: 2026-10-16, confidence: high}
  - {claim: "SOC 2 Type II", url: "https://sentry.io/security/", date: 2026-10-16, confidence: high}
  - {claim: "Self-hosted Sentry under Functional Source License; no intended feature difference between SaaS and self-hosted", url: "https://open.sentry.io/licensing", date: 2026-10-16, confidence: medium}
  - {claim: "$90M Series E at >$3B valuation; $217M total; founded 2012; San Francisco", url: "https://news.crunchbase.com/enterprise/sentry-unicorn-funding-bond-accel", date: 2022-05-04, confidence: high}
---

# Sentry

> Primary category: [llm-observability](../categories/llm-observability.md). This page covers Sentry's AI/agent monitoring; Sentry's core error and performance monitoring is context, not the subject.

**One-liner** — The developer-incumbent route into LLM observability. If your engineers already use Sentry for errors and performance, its **Agent Monitoring** adds agent, tool-call and model-call traces (tokens, cost, latency, errors) to the same traces, with no new vendor.

**What it does** — Sentry's SDKs auto-instrument common AI libraries and record agent runs, model calls, tool calls and handoffs as spans inside the application's normal distributed trace. The **Explore → Agents** area has three views. **Conversations** replays multi-turn sessions grouped by conversation ID. **Traces** shows an agent run alongside the surrounding app work. **LLM Calls** compares individual requests by model, prompt, tokens, cost and latency. Dashboards cover agent executions, model cost, token usage, tool calls and recent errors. A separate **MCP Servers** view monitors MCP servers you operate. Its strength is correlation: an AI failure links to the frontend session replay, the backend API span and the release that shipped it, and similar failures are grouped the way Sentry groups exceptions. **No evals or LLM-as-judge scoring** appear in the sources reviewed. Sentry measures whether the agent broke or slowed down, not whether its answer was good. Sentry's separate **Seer** product is an AI debugging agent for root cause and fixes. It is a different thing from monitoring your own AI.

**Naming / provenance** — Sentry began as an open-source error tracker. The company, **Functional Software, Inc.**, was founded in **2012** in San Francisco. The AI product has been named "LLM Monitoring" (earlier beta), then "AI Agent Monitoring" (open beta announced **2025-06-26**), and appears in current navigation as "Agent Tracing". Not to be confused with Microsoft **Sentinel** ([microsoft-sentinel](microsoft-sentinel.md)), a SIEM.

**Ownership & viability** — `independent`, privately held. The last disclosed round was a **$90M Series E** co-led by BOND and Accel (with NEA and K5 Global) at a **valuation above $3B**, announced **2022-05-04**, for about **$217M total raised**. No later round was found. The company is a mature, large developer-tools business, and AI monitoring is a feature line inside it rather than a bet-the-company product. Viability risk is low. Product risk is that AI monitoring gets less investment than the core if it doesn't win share against Datadog and the AI-native tools.

**Positioning & differentiators** — `platform-module`: AI monitoring is a module of an incumbent developer-monitoring platform, bought because you already have Sentry.
- **Versus [datadog](datadog.md):** the same "AI traces inside the APM you already run" approach. Datadog adds built-in quality and safety evaluations and sensitive-data scanning, and is SaaS-only. Sentry is cheaper to start, developer-centric, has **self-hosting under the Functional Source License**, and offers no evals.
- **Versus [langfuse](langfuse.md), [langsmith](langsmith.md), [arize-phoenix](arize-phoenix.md), [braintrust](braintrust.md), [judgment-labs](judgment-labs.md):** those offer evals, datasets, prompt management and annotation, which Sentry doesn't. Sentry wins on error grouping, release correlation and full-stack context.
- **Versus [pydantic-logfire](pydantic-logfire.md):** both connect AI traces to app telemetry. Logfire has evals and SQL. Sentry has a much larger installed base and session replay.

**Who should choose them / anti-fit** — Fits a firm whose **engineering teams already run Sentry** and want production visibility into agents (what broke, how slow, how much it cost) at near-zero procurement friction. **Anti-fit:** teams that need evaluation, regression testing of prompts, or answer-quality monitoring (Sentry doesn't do these; pair it with an eval tool). Firms standardised on Datadog. Compliance-driven buyers who need evidence-grade retention of AI interactions: Sentry is a debugging tool, not an archive.

**Known weaknesses / gotchas** —
- **Prompt capture is opt-in and then unscrubbed.** With `sendDefaultPii` off, only metadata is recorded (model, tokens, tool names, timings). Turning it on captures **full prompts, responses and tool inputs and outputs**. Sentry's server-side scrubbing **does not cover** `gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.tool.call.arguments` or `gen_ai.tool.call.result` by default; you must add Advanced Data Scrubbing rules. For a fund, this is the single most important configuration item. Python integrations also accept `include_prompts=False`.
- No evals or LLM-as-judge capability.
- Whether every agent-monitoring view works identically on self-hosted Sentry was not confirmed. Sentry states an intent of feature parity.

**Deployment & data handling** — SaaS (sentry.io) or **self-hosted** (Docker Compose, single node, "no guarantees or dedicated support", FSL licence converting to Apache 2.0 after two years). `data_leaves_tenancy: partial`: on SaaS, spans go to Sentry, and prompts and outputs go only if you enable PII capture. Self-hosted keeps everything in-house. Data-region options (US/EU) and retention periods were not confirmed on the security page reviewed. It works out-of-band through the SDK, with sampling configurable; Sentry recommends keeping complete agent runs rather than sampling all traffic.

**Integrations & partnerships** — Python SDK (3.x), auto-enabled: **OpenAI, OpenAI Agents SDK, Anthropic, Google Gen AI, LangChain, LangGraph, Pydantic AI, Hugging Face Hub, MCP**. Manual: LiteLLM, Mistral. JavaScript: Vercel AI SDK, OpenAI, Anthropic, Google GenAI, LangChain, LangGraph. **MCP:** Sentry monitors MCP servers you run and also offers its own hosted Sentry MCP server (mcp.sentry.dev) so coding agents can query Sentry data. Sentry was a Silver sponsor at AI Engineer New York 2026 (no session on the agenda).

**Compliance & FS traction** — **SOC 2 Type II** confirmed on Sentry's security page. A DPA and BAA are offered (scope not reviewed). ISO 27001 was not confirmed in the sources reviewed. No FS-specific AI-monitoring references were found. Sentry's core product is very widely used across software teams, so it may already be in a fund's estate.

**Commercial** — Platform tiers: **Developer free, Team $29/month ($26 annual), Business $89/month ($80 annual), Enterprise custom**. Each self-serve tier includes **5M spans**. "Agent tracing" is listed on all plans with no separate SKU, so AI monitoring costs whatever spans it consumes. Agents generate many spans, so watch the quota. Seer is a separate paid add-on.

## Open questions

- Formal GA status of Agent Monitoring (docs no longer label it beta, but no GA announcement was found).
- Span overage pricing, and the typical span volume per agent run.
- Data-region options and retention defaults for AI spans on SaaS.
- Parity of agent and MCP monitoring on self-hosted Sentry.
- Any roadmap toward evals or quality scoring.
- Funding or valuation events since 2022.

## Sources

- [Sentry changelog: AI Agent Monitoring open beta (2025-06-26)](https://sentry.io/changelog/ai-agent-monitoring--open-beta/) — fetched 2026-10-16 — supports: launch date, feature set, availability; confidence: high
- [Sentry blog: updated Agent Monitoring (2025-06-26)](https://blog.sentry.io/sentrys-updated-agent-monitoring) — fetched 2026-10-16 — supports: features, SDK minimums; confidence: medium (vendor blog)
- [Sentry docs: AI monitoring](https://docs.sentry.io/ai/monitoring) — fetched 2026-10-16 — supports: current views, cost dashboards, MCP server monitoring; confidence: high
- [Sentry docs: Python integrations](https://docs.sentry.io/platforms/python/integrations/) — fetched 2026-10-16 — supports: AI integration list; confidence: high
- [Sentry docs: AI agent data privacy](https://docs.sentry.io/product/insights/ai/agents/privacy/) — fetched 2026-10-16 — supports: PII/prompt capture defaults and scrubbing gaps; confidence: high
- [Sentry pricing](https://sentry.io/pricing/) — fetched 2026-10-16 — supports: plan prices, span quotas, agent tracing on all plans; confidence: high
- [Sentry security](https://sentry.io/security/) — fetched 2026-10-16 — supports: SOC 2 Type II; confidence: high
- [Sentry licensing (open.sentry.io)](https://open.sentry.io/licensing) — via search 2026-10-16 — supports: FSL, SaaS/self-hosted parity intent; confidence: medium
- [Crunchbase News, 2022-05-04](https://news.crunchbase.com/enterprise/sentry-unicorn-funding-bond-accel) — fetched 2026-10-16 — supports: Series E, valuation, total raised, founding year, HQ; confidence: high
- Cached: `raw/sources/2026-10-16--sentry--agent-monitoring.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
