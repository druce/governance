# TrueFoundry — Agent Harness (docs + launch blog)

- URL: https://www.truefoundry.com/docs/agent-platform/agent-harness/overview
- URL: https://www.truefoundry.com/docs/agent-platform/agent-harness/getting-started
- URL: https://www.truefoundry.com/docs/agent-platform/agent-harness/sdk/overview (via search summary)
- URL: https://www.truefoundry.com/blog/agent-harness-managed-ai-agents (published 2026-06-09, author Boyu Wang)
- Fetched: 2026-10-20
- Good for: what "Agent Harness" is, how it relates to TrueForge, AI Gateway and MCP Gateway; governance features;
  deployment options. Vendor docs and vendor blog (marketing).

## Docs (2026-10-20)
- Agent Harness = "the runtime layer around an LLM that turns it into a reliable, long-running agent" — planning,
  tool calls, context, approvals, state, observability.
- TrueFoundry's harness is TrueForge, "embedded in the platform as-is, not forked or re-implemented". TrueFoundry adds
  hosting as "a managed, multi-user service inside the platform, sharing its authentication, RBAC, and control plane.
  There is nothing to install or operate, and it is available as SaaS, self-hosted, or on-prem."
- Models, MCP servers and skills registered in the AI Gateway appear in the agent builder: "No provider credentials,
  MCP endpoints, or skill sources have to be configured separately in TrueForge." Agent traffic flows through the
  gateway, so "cost, tokens, and tool calls for every session are captured without extra instrumentation."
- Human checkpoints (tool approval, structured ask-user questions); sandbox for code/file/shell execution, a Runtime
  Config toggle on by default, provisioned only when needed. Guardrails mentioned only in diagram alt text.
- "The previous TrueFoundry agent APIs keep working until 15th October, 2026; migrate to the TrueForge API before
  then." Agents created before the TrueForge portal were migrated automatically. SDK marked experimental.
- Note: a 2026-10-20 search-engine snippet summarised the getting-started page as "SaaS only"; the live page fetched
  the same day says "SaaS, self-hosted, or on-prem". Treated as a stale snippet; live page adopted.

## Launch blog (2026-06-09)
- "a managed harness built on top of the AI Gateway and MCP Gateway." Agents defined declaratively (model + MCP
  servers + skills + instructions).
- HITL gates on sensitive tool calls; destructive tools flagged once at the MCP Gateway so the requirement applies to
  every agent using them. Provider credentials held in AI Gateway where RBAC, budgets and guardrails are enforced;
  "no API keys or credentials are ever pasted into agent definitions". Skills Registry versioned under RBAC. Per-run
  traces with cost/tokens/latency per step; OpenTelemetry export inherited from the gateway.
- "it deploys as SaaS, self-hosted, or on-prem." Compares itself with Anthropic Claude Managed Agents and LangChain
  LangSmith Managed Deep Agents; positions itself as no-code-first with centralized credentials. Notes some
  capabilities "may be in active development".
