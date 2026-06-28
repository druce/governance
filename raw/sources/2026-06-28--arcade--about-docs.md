URL: https://docs.arcade.dev/en/get-started/about-arcade
Fetched: 2026-06-28
Good for: Arcade architecture, how OAuth/scopes auth works, supported frameworks and integrations, MCP support.

# Key extracted text

- Arcade is an authorization system for agentic applications—AI systems that need to perform tasks requiring user-specific data and access to external services.
- Problem: "Applications that use models to perform tasks (agentic applications) commonly require access to sensitive data and services."
- Handles three auth mechanisms: OAuth 2.0, API keys, and user tokens.
- Uses scopes (OAuth 2.0 permissions): "A scope is what the user has authorized someone else (in this case, the AI agent) to do on their behalf."
- Workflow: "When an agent calls a tool, if the user has not granted the required permissions, Arcade Engine will automatically prompt the user to authorize the tool and coordinate the OAuth 2.0 flow with the service provider."
- OAuth tokens / API keys are securely injected by Arcade into tool calls at runtime; the client and LLM never see the secret values. Arcade remembers user's authorization tokens (re-auth not needed until token revoked).
- Architecture: "Arcade Engine" coordinates authorization flows and tool execution.
- Frameworks: LangChain, OpenAI Agents, Google ADK, CrewAI, AG2, Vercel AI SDK, Spring AI SDK.
- Service integrations: Gmail, Google Calendar/Contacts/Drive/Docs/Sheets/Slides, Microsoft 365, Slack, Discord, GitHub, Salesforce, HubSpot, Stripe, Zoom, + 100s more toolkits.
- MCP support: provides MCP servers usable across IDE clients (Cursor, Claude Desktop, VS Code) and agent frameworks.
- Some tools require no auth (e.g., GoogleSearch.Search).
- Per vendor (search result): can be deployed in your own cloud, VPC, on-premises, or fully air-gapped.
