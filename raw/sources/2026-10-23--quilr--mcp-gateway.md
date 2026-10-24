# Quilr — MCP Gateway ("Give your agents tools")

- URL: https://quilr.ai/solutions/mcp-tooling
- Fetched: 2026-10-23
- Good for: confirming Quilr markets an MCP gateway (proxy in front of MCP servers, tool scoping, identity, audit). Vendor marketing only.

## Extracted

- Product: "MCP Gateway," claims coverage of 500+ MCP servers; "works with every major MCP server in the ecosystem, out of the box" (GitHub, Slack, Jira, PostgreSQL, Salesforce...).
- "Drop the gateway in front of your MCP servers." Dynamic Tool Calling: "your agent describes what it needs and the gateway selects the right tool automatically."
- Tool scoping via "Guardian" (e.g., GitHub MCP limited to approved repos; filesystem MCP limited to project dir); permissions set in Guardian's CLARIFY phase, enforced at runtime.
- "Every agent-to-MCP call goes through the QuilrAI gateway with identity verification." "Tools know who's calling and can refuse requests outside policy." Auth mechanisms/IdPs not specified.
- Each tool call logged with agent identity, tool name, redacted parameters, response; logs searchable, exportable, retention-configurable.
- Separate MCP Security scanner checks community packages at install and on update.
- Endpoint Agent + MCP Gateway together discover self-hosted MCP servers. Deployment model (SaaS vs self-hosted) not stated. No latency/SLA figures for MCP path.
