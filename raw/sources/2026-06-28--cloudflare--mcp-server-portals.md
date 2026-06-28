URL: https://blog.cloudflare.com/zero-trust-mcp-server-portals/
Fetched: 2026-06-28
Note: Cloudflare blog (vendor) — MCP Server Portals + AI Gateway as chokepoint for agent/MCP traffic. Marketing/announcement source.

Key extracted text:
- MCP Server Portals: "a single, centralized gateway for all your MCP servers" — Open Beta announced 2025-08-26, part of Cloudflare One SASE/Zero Trust platform.
- Users authenticate once via corporate IdP; single Portal URL gives dynamic access to authorized MCP servers/tools; eliminates manual per-server endpoint config.
- Enforce granular access policies (MFA, device posture, geo restrictions); curate/approve servers before user access (zero-trust).
- Aggregates MCP request logs for audit trails + anomaly detection; can detect unauthorized remote MCP servers accessed via the enterprise network.
- DLP: when a tool call matches a Block DLP policy, Gateway blocks it; applies in both directions (requests + responses); portal surfaces the block to the MCP client as an error.
- Roadmap: host MCP servers through AI Gateway for "deeper prompt filtering and controls."
- Related: Cloudflare Agents docs — deploy your own remote MCP server on Workers using Streamable HTTP transport; Cloudflare runs a catalog of managed remote MCP servers (OAuth from Claude, Windsurf, AI Playground). Durable Objects + OAuth for agent authn/authz.
- Enterprise MCP reference architecture (blog.cloudflare.com/enterprise-mcp/): separation of MCP clients and servers keeps a boundary between the AI and corporate credentials/APIs.
