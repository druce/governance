URL: https://obot.ai/mcp-gateway-platform/
Fetched: 2026-06-28
Note: Vendor product page for the Obot MCP Gateway — best single source for gateway feature set, IdP support, and OSS vs Enterprise vs Managed Cloud tiers. (Vendor marketing.)

## Key extracted text

Core function: centralized management and security for MCP servers; acts as a control plane between AI clients and MCP servers. "Obot sits between AI clients (Claude, Cursor, ChatGPT, internal agents) and any MCP server, whether local, remote, or hosted. Obot enforces auth and authorization on every request, brokers tokens server-side, applies per-tool access policies, and logs everything for audit and incident response."

Access & identity:
- Centralized OAuth with support for Google, GitHub, Okta, Auth0, JumpCloud, and Entra.
- Per-user and per-group access controls.
- Token brokering handled server-side to prevent credential exposure.

Governance & compliance:
- Complete audit logging of every tool call with user, agent, server, arguments, and outcomes.
- Fine-grained access policies / per-tool permissions.
- Real-time usage dashboards; compliance-ready audit trails.
- Predefined RBAC roles: Owner, Admin, Power User+, Power User, Basic User, Auditor.

Server management:
- Local, remote, and hosted MCP servers; curated internal catalog of vetted servers; single console for deployment, versioning, retirement.

Deployment tiers:
- **Open Source Edition:** MIT-licensed, self-hostable on Kubernetes or Docker.
- **Enterprise Edition:** adds advanced IdP integrations (Okta, Entra), SLAs, support.
- **Managed Cloud:** dedicated, fully-hosted gateway option.

Positioning quote: "Without a gateway, security teams say 'no' and AI adoption stalls."
