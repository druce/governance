URL: https://docs.composio.dev/
fetched: 2026-06-28
Good for: product/deployment specifics — managed auth (OAuth/API key), tool-calling, SDKs, MCP, deployment models.

Key extracted text (trimmed):
- Composio provides managed authentication and tool integration for AI agents. Handles OAuth and API key management to integrate third-party services into agent workflows.
- "Tool calling for AI agents" through a unified interface.
- SDKs: Python and TypeScript.
- Integration modes: Native Tools (provider packages) and MCP (Model Context Protocol) for broader compatibility.
- Deployment: SaaS, API-based, SDK, and self-hosted options.
- Auth UX: pass `user_id` to `composio.create()`; system abstracts manual credential setup, handling OAuth flows and API key management transparently during agent execution. Pattern: create a session with a user ID, retrieve available tools, pass them to your LLM framework.
