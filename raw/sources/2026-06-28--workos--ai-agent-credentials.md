# WorkOS — Give your AI agents their own credentials (vendor blog)

URL: https://workos.com/blog/ai-agent-credentials
Fetched: 2026-06-28
Good for: the agent-identity model (agents as first-class principals), scoped tokens, M2M.

## Key extracted text

- WorkOS treats agents as first-class principals needing distinct identities separate from users: "scoped, revocable credentials and tool-level authorization" rather than inheriting a user session wholesale.
- User-authorized agents: AuthKit uses authorization code flow with PKCE; "the agent receives a separate, scoped token that represents what the user has authorized the agent to do. Not what the user can do."
- Machine-to-machine / background agents: OAuth 2.1 Client Credentials; "if this agent is compromised, you revoke its client credentials. No user sessions are affected."
- Authorization: RBAC layered with fine-grained access controls (FGA); tool-level enforcement validates permissions at each invocation; agents "can only call tools that have been explicitly mapped to permissions it holds." Tokens short-lived (minutes to hours).
- Deployment: delivered via WorkOS identity platform with native MCP server authentication support; developers add credential scoping without building auth infra.
- Framed against ASI03 (identity & privilege abuse) risk.
