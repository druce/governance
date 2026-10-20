# TrueFoundry — TrueForge open-source agent harness (GitHub, press release, InfoWorld)

- URL: https://github.com/truefoundry/trueforge (via GitHub API)
- URL: https://www.01net.it/truefoundry-launches-trueforge-an-open-source-vendor-neutral-alternative-to-claude-managed-agents-at-50-lower-cost/ (Business Wire syndication, dateline 2026-08-19)
- URL: https://www.infoworld.com/article/4211969/truefoundry-debuts-open-source-ai-agent-harness-claiming-up-to-75-lower-costs.html (2026-08-20)
- URL: https://www.hpcwire.com/aiwire/2026/08/19/truefoundry-debuts-trueforge-for-building-and-managing-ai-agents/ (not fetched; corroborates date)
- Fetched: 2026-10-20
- Good for: TrueForge licence, launch date, scope, traction; independent caveats on cost claims.

## GitHub (2026-10-20)
- truefoundry/trueforge: MIT; created 2026-07-23; 6,313 stars; 531 forks; TypeScript; last push 2026-10-20;
  homepage trueforge.dev; npm releases at very high cadence (@truefoundry/trueforge 0.179.2 on 2026-10-16).
- README: runs "the agent execution loop for you - model calls, MCP tools, skills, sandboxing, approvals, context
  management, and session state"; any model provider incl. OpenAI-compatible endpoints; remote MCP with header auth
  or OAuth; git-backed SKILL.md skills; "Sandbox as a tool - isolated code/file execution (Daytona today; more
  providers planned)... Secrets stay in the harness."; human checkpoints; subagents, deferred tool loading, Code Mode,
  compaction; local mode (SQLite, no login — "keep it on localhost") or hosted mode (Postgres + Redis; Docker
  Compose, Helm, Railway).

## Press release (Business Wire, 2026-08-19) — vendor marketing
- Open-source harness positioned as "an alternative to Claude Managed Agents"; OpenAI, Anthropic + 20+ models; 40+
  built-in tools; sandboxed execution; human-approval workflows; generative UI; Tavily web search.
- Routes every model call and MCP interaction through TrueFoundry's AI Gateway; budget enforcement, rate limits,
  guardrails on model and tool calls; every call logged. Hosted version with self-serve pay-per-usage pricing (no rates).
- Claim: cuts total agent operating cost 50%. Named customers on TrueForge: Automatiq, NetApp (quote from NetApp's
  Robert Rubin). AI Gateway + MCP Gateway process >1 trillion tokens/day (vendor claim).
- Describes TrueFoundry's AI Gateway as comprising LLM Gateway, MCP Gateway and Agent Gateway.

## InfoWorld (2026-08-20) — independent trade press
- Benchmark is TrueFoundry's own: 14 tasks from DevRev Enterprise-Bench. With Opus 4.8 both TrueForge and Claude
  Managed Agents completed ~11 tasks; $8.50 vs $11.80 per run (~30% less). With GLM-5.2 ~$2.90/run (~75% less).
  "not independently validated" for larger production workloads.
- Pareekh Jain: "more control and less vendor lock-in"; self-hosting pays off for high-volume continuous agents.
  Lian Jye Su (Omdia): regulated firms can apply their own budget/access/observability controls but must run more of the stack.
