URL: https://www.docker.com/blog/docker-mcp-gateway-secure-infrastructure-for-agentic-ai/
Fetched: 2026-06-28
Note: Docker's launch/positioning blog for the open-source MCP Gateway — best primary source for what it does, security interceptors, and launch date.

---

Docker MCP Gateway is an open-source project that acts as a "secure enforcement point between agents and external tools." It aggregates multiple MCP servers behind a single, secure interface for production environments. Integrates with Docker Compose.

Problems solved:
- Moving beyond local development to production
- Security risks of connecting AI agents to MCP servers
- Complexity of managing multiple MCP server connections
- Scaling governance of agent-based workloads

Core features / commands:
- Discovery: `docker mcp catalog show` — view MCP servers from Docker MCP Catalog (1M+ pulls cited)
- Configuration: `docker mcp secret set 'brave.api_key=XXXXX'`; `docker mcp config write` for host-specific settings
- Runtime: `docker mcp server enable google-maps brave`; `docker mcp gateway run`
  - Custom: `docker mcp gateway run --transport=sse --servers=brave,wikipedia-mcp --tools=brave_web_search,...` (tool filtering)
- Security interceptors:
  `docker mcp gateway run --verify-signatures --log-calls --block-secrets`
  - verify-signatures — container image provenance verification
  - block-secrets — scan payloads for exposed secrets
  - log-calls — audit all gateway calls
  - OAuth support — OAuth-enabled MCP server configuration

Availability:
- Included in latest Docker Desktop
- Open source on GitHub (github.com/docker/mcp-gateway)
- Launch date: July 9, 2025
- Integrates with Docker Compose
