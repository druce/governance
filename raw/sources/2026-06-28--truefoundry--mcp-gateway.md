URL: https://www.truefoundry.com/mcp-gateway (and /blog/introducing-truefoundry-mcp-gateway, /docs/ai-gateway/mcp/mcp-overview)
Fetched: 2026-06-28
Note: MCP Gateway / agent registry features — tool access control, auth, observability.

Key extracted text:
- MCP gateway is part of the same AI Gateway control plane (not a separate product).
- Tool access control: Federated IdPs (Okta, Azure AD) + OAuth 2.0; per-server RBAC;
  metadata-based policies on every tool invocation; audit/log of all agent-initiated tool
  actions.
- Auto-discovery of all tools/servers registered with MCP, gated by RBAC.
- MCP registry: centralized catalog / single source of truth for every approved tool in the
  org; searchable directory for agents to discover tools/resources dynamically.
- Credential handling: single Personal-Access-Token (PAT) or machine-scoped Virtual-Account-
  Token (VAT) auto-exchanged for per-server OAuth/header tokens behind the scenes.
- Routing: agents auth once to the MCP Gateway, which routes MCP requests to registered MCP
  servers (Slack, GitHub, internal tools); Control Plane manages tokens, OAuth flows, policies.
- Observability/compliance: tracing of every MCP server call, agent decision, LLM request;
  structured telemetry (latency, errors, usage).
