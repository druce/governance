URL: https://aembit.io/blog/aembit-iam-for-agentic-ai-is-now-generally-available/
fetched: 2026-06-28
Note: Vendor blog — primary source for the agentic-AI / MCP product, deployment architecture, and Blended Identity model.

Key extracted text (trimmed):
- "AI agents are not coming. They are already here: calling APIs, querying databases, and triggering workflows, autonomously, at machine speed."
- Capabilities: cryptographic workload attestation, ephemeral credential issuance, least-privilege policy enforcement.
- Blended Identity: evaluates the AI agent's identity AND the human operating it together in a single policy decision at request time — "Is this specific user, using this specific agent, authorized to access this specific resource right now?" Per-user credential isolation per session.
- Architecture, two components:
  1. MCP Authorization Server — fully managed SaaS; OAuth 2.1 authorization-code flow; integrates with Okta, Azure AD, Google.
  2. MCP Identity Gateway — edge deployment, a Linux VM that validates tokens and enforces policy on every MCP request, performing real-time credential exchange so "the agent never holds direct credentials."
- Supports Claude and Microsoft Copilot Studio agents.
- GA announced April 2026 after alpha/beta with customers/design partners.
- Pricing: Starter (free dev tier); AI Teams $20/agent/month (10-500 agents); Enterprise (unlimited agents, 24/7 support).
- Stat cited: 60%+ of orgs plan AI agents in production within two years, <20% feel they have adequate security controls.
