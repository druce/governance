URL: https://www.mintmcp.com/docs/intro
Fetched: 2026-06-28
Good for: MintMCP's own product definition — architecture, gateway, virtual MCP, SSO/RBAC, audit, deployment.

---

Core: "enterprise gateway for Model Context Protocol (MCP)" that "sits between your AI clients and MCP servers, handling authentication, logging every tool call, and enforcing access policies."

Architecture / components:
- MCP Gateway: centralizes MCP server management vs distributed local configs; "MCP store" of pre-approved servers; "role-based tool sets" so teams see relevant integrations; hosts MCP servers in MintMCP infrastructure (no local install).
- Agent Monitor: captures/analyzes AI agent behavior (file operations, command execution, tool invocations); can create rules blocking risky activities.

Capabilities:
- Auth/SSO: OAuth 2.0, SAML, SSO; pre-configured credentials; servers activate immediately post-SSO.
- RBAC: role-based access determines which tools teams can access.
- Audit logging: centralized governance with audit logs, access policies, credential management.
- DLP/guardrails: detection and blocking of risky behavior patterns.

Integrations: MCP servers for data warehouses (Snowflake, BigQuery, Databricks), comms (Slack, Teams), docs (Google Drive, SharePoint, Confluence), custom APIs. Clients: Claude, Claude Code, Cursor, custom agents.

Deployment: managed cloud service; self-hosted options available through enterprise consultation.
