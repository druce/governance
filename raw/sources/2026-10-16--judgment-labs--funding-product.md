# Judgment Labs — $32M seed + Series A, product, Judgeval OSS SDK

- URL: https://www.vcaonline.com/news/2026051203/judgment-labs-closes-32m-in-seed-and-series-a-funding-to-build-the-continuous-improvement-layer-for-ai-agents/ (press release, 2026-05-12)
- URL: https://www.judgmentlabs.ai/
- URL: https://github.com/JudgmentLabs/judgeval
- URL: https://docs.judgmentlabs.ai/llms.txt (docs index)
- URL: https://ai.engineer/nyc (sponsor list)
- Fetched: 2026-10-16
- Good for: funding, founders, product scope, OSS licence, integrations.

## Funding (press release, 2026-05-12, San Francisco)
- **$32M combined seed + Series A**, both led by **Lightspeed Venture Partners** (Series A
  less than six months after its initial investment). Participants: Nova Global, SV Angel,
  Valor Equity Partners, Dynamic. No per-round split disclosed.
- Founders: Alex Shan (CEO; ex-Stanford NLP group), Andrew Li (Chief Scientist; ex-Together AI),
  Joseph Camyre (CTO; ex-Datadog). HQ San Francisco.
- Product: evaluates long reasoning traces, tool use and memory of "deep agents"; full
  trajectory view; surfaces recurring failure patterns. Named customer: E3 Group (testimonial).
- Use of funds: hiring researchers/engineers in SF; forward-deployed engineering team.
- Founding year: aggregators disagree (2025 vs other); not stated in release.

## Website (vendor marketing)
- "The continuous-improvement stack for agents." Features: Slack-based investigation agent;
  agent-swarm triage of similar failures; pre-ship testing of fixes against production cases;
  behavior tracking that flags drift and regressions (e.g. "Missed Escalation" monitor);
  Agent Search (behavioral query over trajectories); Agent Judge (trajectory-level
  evaluators); Behavior Discovery (failure modes from unlabeled production trajectories);
  AutoRubrics.
- MCP access from Claude, Codex, Cursor or any MCP client.
- Testimonials: Monaco, Human Behavior, Contrario, E3 Group, Vigil Labs.
- Pricing, deployment options and certifications not stated on current site.

## Judgeval (GitHub)
- Apache-2.0; ~1.1k stars. Python SDK; OpenTelemetry-based tracing (`@Tracer.observe()`);
  agent judges run on live traffic (server-side online scoring, Slack alerts) or replayed
  on historical traces; read-only SQL over project data; CLI + MCP server.
- Quickstart requires JUDGMENT_API_KEY / ORG_ID → hosted Judgment backend needed for
  online scoring, SQL, UI.
- Integrations (docs index): LangGraph, OpenAI Agents SDK, Claude Agent SDK, Claude Managed
  Agents, Google ADK, Vercel AI SDK, LiveKit, Pipecat; model providers incl. Anthropic, OpenAI,
  Bedrock, Vertex, LiteLLM, OpenRouter, Ollama; OTLP direct export, dual export, OpenLLMetry,
  OpenInference, OpenLit.
- Docs also cover datasets, offline tests, and turning production failures into regression tests.

## Unverified (search snippets of pages now returning 404)
- Pricing page snippet: Pro $49/user/month; $8 per 100K trace spans (14-day retention);
  $20 per 1,000 evals; Enterprise custom with self-hosting / private VPC.
- Compliance page snippet: SOC 2 Type 1 completed; Type 2 in progress (Delve portal).
- Self-hosting docs snippets conflict ("coming soon" vs request-access, AWS + Supabase).
  These pages 404 on 2026-10-16; treat all as low confidence.

## AIE NYC 2026
- Listed as a Silver sponsor; no session found on the agenda.
