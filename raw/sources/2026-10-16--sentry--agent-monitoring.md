# Sentry — AI agent monitoring, privacy controls, pricing, company

- URL: https://blog.sentry.io/sentrys-updated-agent-monitoring (2025-06-26)
- URL: https://sentry.io/changelog/ai-agent-monitoring--open-beta/ (2025-06-26)
- URL: https://docs.sentry.io/ai/monitoring
- URL: https://docs.sentry.io/product/insights/ai/agents/privacy/
- URL: https://docs.sentry.io/platforms/python/integrations/
- URL: https://sentry.io/pricing/
- URL: https://sentry.io/security/
- URL: https://open.sentry.io/licensing
- URL: https://news.crunchbase.com/enterprise/sentry-unicorn-funding-bond-accel (2022-05-04)
- Fetched: 2026-10-16
- Good for: what Sentry's AI/agent monitoring covers, prompt-capture defaults, plan pricing, ownership.

## Agent monitoring
- Open beta / "major upgrade" announced 2025-06-26: tracing, tool visibility, model performance
  (tokens, latency, error rate by model/version), error grouping, AI-only trace view, linked to
  frontend replays, backend spans, release metadata. Available to all Sentry users.
- Current docs: agent runs, tool calls, model interactions, handoffs; Explore → Agents tabs for
  Conversations (multi-turn replay), Traces, LLM Calls (tokens, cost, latency); dashboards for
  model cost, token usage, tool calls, errors; separate MCP Servers monitoring page. GA status
  not labelled in docs.
- Python SDK 3.x AI integrations auto-enabled: Anthropic, Google Gen AI, Hugging Face Hub, OpenAI,
  OpenAI Agents SDK, LangChain, LangGraph, Pydantic AI, MCP. Manual: LiteLLM, Mistral.
  JS: Vercel AI SDK, OpenAI, Anthropic, Google GenAI, LangChain, LangGraph.
- No evals / LLM-as-judge described in sources found.

## Privacy (docs)
- With sendDefaultPii false: only metadata (model names, token counts, tool names, timings).
- With true: "Full inputs, outputs, prompts, and responses from AI models and tools are captured."
- Server-side scrubbing does NOT cover gen_ai.input.messages, gen_ai.tool.call.arguments,
  gen_ai.tool.call.result, gen_ai.output.messages by default — need Advanced Data Scrubbing rules.
- Python integrations: include_prompts=False keeps prompts out even with send_default_pii=True.

## Pricing (pricing page)
- Developer free; Team $29/mo ($26 annual); Business $89/mo ($80 annual); Enterprise custom.
- 5M spans included on Developer/Team/Business. "Agent tracing" listed on all plans.
  Seer (AI debugging agent) is a paid add-on.

## Security / licensing
- SOC 2 Type II (security page). DPA and BAA linked; ISO/regions not stated on that page.
- Self-hosted Sentry under Functional Source License (converts to Apache 2.0 after two years);
  Sentry says no intended feature difference between SaaS and self-hosted; single-node Docker
  Compose, no support guarantees. Whether agent monitoring UI is fully available self-hosted: not confirmed.

## Company (Crunchbase News, 2022-05-04)
- Functional Software, Inc. (d/b/a Sentry), San Francisco, founded 2012.
- Series E $90M (BOND, Accel co-lead; NEA; K5 Global) at >$3B valuation; $217M total raised.
- No later round found as of 2026-10-16.

## AIE NYC 2026
- Sentry listed as Silver sponsor; no session found.
