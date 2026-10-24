# LiteLLM — MCP Gateway (official docs)

- URL: https://docs.litellm.ai/docs/mcp
- Fetched: 2026-10-23
- Good for: confirming LiteLLM proxy ships an MCP gateway function (central endpoint, access control, auth, transports).

## Extracted

- The proxy offers "a fixed endpoint for all MCP tools" — clients connect to one LiteLLM URL instead of each MCP server.
- Access control "By Key," "By Team," "By Organization"; customer-level controls via the `x-litellm-end-user-id` header (which MCP servers a customer can reach; budgets). Page describes server-level access control; per-tool allowlisting not explicitly described on this page.
- Upstream auth types: `api_key`, `bearer_token`, `basic`, OAuth 2.0 (PKCE and `client_credentials`), AWS SigV4 (Bedrock AgentCore), static headers, per-server headers `x-mcp-{server_alias}-{header_name}`.
- Transports: Streamable HTTP, SSE, stdio. "stdio MCP servers are disabled unless the proxy is started with `LITELLM_ENABLE_MCP_STDIO=true`."
- Tool calls attributed per customer ("All tool calls are tracked under `customer_123`"); links to general logging/observability docs.
- Licensing of MCP features vs Enterprise tier not stated on the page (footer MIT; enterprise callout lists SSO/SAML, audit logs, spend tracking, multi-team management, guardrails).
