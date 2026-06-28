URL: https://www.pomerium.com/blog/secure-access-for-mcp
Fetched: 2026-06-28
Note: Pomerium's own technical explainer for how its proxy secures MCP servers (per-request authz, tool-level policy, OIDC).

Key extracted text:

- Pomerium functions as an identity-aware proxy that intercepts all MCP traffic. Rather than agents directly accessing MCP servers, requests flow through Pomerium's authorization engine first.
- Per-request policy enforcement: "Evaluate every file access, API call, or update." Each request assessed against policies considering user role, time of day, IP origin, device posture, request path — beyond static OAuth scopes.
- Tool-level authorization example:
    - mcp_tool:
        in: ["search","fetch"]
  Restricts which tools an agent can invoke even with valid credentials.
- IdP integration: integrates with existing SSO (Okta, Azure AD, Google Workspace). Agents inherit user-level identity; "every action tied to a user." Pomerium validates external OAuth tokens and translates them to short-lived, scoped JWTs injected into headers — prevents token sprawl.
- Deployment: sits between agents and MCP servers as a reverse proxy. Terminates TLS, performs authN/authZ at session establishment, proxies approved traffic at wire speed, supports WebSockets and HTTP/2 streaming.
- Policy language: YAML-based route config combining identity conditions with MCP-specific controls; centralized enforcement.
- Does not require modifying MCP clients/servers; configure them to talk through Pomerium; remains MCP-spec compliant.
