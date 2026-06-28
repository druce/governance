# WorkOS — Secure auth for MCP servers (vendor product page)

URL: https://workos.com/mcp
Fetched: 2026-06-28
Good for: the MCP/agent-auth angle, OAuth 2.1 authorization-server model, deployment.

## Key extracted text

- WorkOS provides OAuth 2.1-based authorization for MCP servers through AuthKit; acts as a spec-compatible OAuth Authorization Server. "handles all the complexity of the OAuth Authorization Server. You just build the MCP tools and resource endpoints."
- Features: metadata discovery, Dynamic Client Registration, PKCE, JWT validation, scopes, tool-level permissions, RBAC enforcement.
- Two integration paths: full AuthKit OAuth authorization server; or "Connect" standalone middleware in front of an existing identity system handling only the MCP OAuth flows (discovery, DCR, PKCE, token issuance, consent) — no migration.
- FGA enables tool-level permission scoping: grant an agent access to specific tools within a service, not the whole service.
- Developer-centric: code samples, open-source templates, mcp.shop example, MCP Night events, Discord. Claims integrate "in a matter of days."
