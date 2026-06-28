# Stytch Agent Ready — Enterprise security for AI agents (vendor product page)

URL: https://stytch.com/ai-agent-ready  (also https://stytch.com/docs/get-started/guides/ai-agents-and-apps)
fetched: 2026-06-28
Good for: the agent-auth / non-human-identity angle — Connected Apps, MCP auth, agent fraud detection. Vendor marketing/docs.

## Key extracted text

Connected Apps / OAuth for agents:
- "OAuth 2.0 and OIDC for agents" — turns the customer's app into an OAuth 2.0 / OIDC authorization server so AI agents and MCP servers get scoped, auditable, revocable access to user data.
- Token lifecycle: issue / validate / refresh / revoke access, refresh, and ID tokens; revoke at user OR organization level.
- "apps inherit only the permissions the user already has" (delegated, scoped consent).

MCP (Model Context Protocol):
- "Native support for the Model Context Protocol"; integrates with Claude, ChatGPT and agent ecosystems. Remote MCP with dynamic client registration. Deployment guides for Cloudflare Workers and Vercel edge.
- Enterprise controls: IT-admin consent, org-level policies, allowlists, audit logs, one-click revocation.

Fraud & abuse detection for agents:
- "Prevent automated attacks" — data scraping, prompt injection, compute abuse; intelligent rate limiting to block unknown automated traffic and misbehaving agents. Powered by Stytch Device Fingerprinting.

Deployment model:
- Pre-built UI components AND headless SDKs; "no migration required." Supports first-party apps, third-party integrations, and CLI tools via Authorization Code Flow with PKCE.
