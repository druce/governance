# Keycard — product, pricing, Anchor.dev acquisition, Multi-Agent Apps launch

- URL: https://www.keycard.ai/
- URL: https://www.keycard.ai/pricing
- URL: https://keycard.ai/blog/announcing-keycard-for-multi-agent-apps/
- URL: https://www.helpnetsecurity.com/2026/05/15/keycard-for-multi-agent-apps/
- URL: https://pulse2.com/keycard-acquires-anchor-dev-to-unlock-autonomous-coding-agents/
- URL: https://www.globenewswire.com/news-release/2026/01/29/3228894/0/en/Keycard-Named-a-Top-Cloud-Computing-Startup-to-Watch-for-Solving-the-AI-Agent-Identity-and-Access-Problem.html
- Fetched: 2026-10-16
- Good for: how the product works, enforcement points, integrations, SOC 2 claim, named
  customer, pricing tiers, 2026 product/M&A timeline. Homepage/pricing/blog are vendor marketing.

## Homepage (vendor marketing)
- Headline "Runtime auth for agents." Evaluates each credential request against policy when
  the agent acts; issues **short-lived credentials** only on approval (example: one-hour token
  limited to `knowledge:read`).
- Delegated OAuth tokens for services like GitHub/Slack; stored API tokens for others.
- **Policy as code in Cedar**, managed with Terraform. Logs every authorization event incl.
  denials; instant revocation. SDKs: Python, TypeScript, Go, Ruby.
- Enforcement points: in-app SDK; optional gateway (no code change); infrastructure
  **sidecar proxy that swaps placeholder secrets for user-scoped tokens** so the agent never
  holds a real credential.
- IdPs: Okta, Entra ID, Google, AWS, Vercel, GitHub Actions, Google Cloud, OIDC; FAQ mentions Auth0.
- Resource connectors: GitHub, Slack, PagerDuty, Sentry, Neon, Linear, custom MCP servers/APIs.
- Audit export: OCSF-compatible SIEMs, Amazon S3, Splunk, Panther.
- Certification claim: **SOC 2 Type II**. Named customer: **Chime** (Dennis Yang, Principal PM GenAI quote).
- "Agent Baseline" white paper with Docker and Snyk.

## Pricing page (vendor)
- Usage-based on "transactions" (each request Keycard is involved in).
- Starter free: 5,000 tx/mo hard cap; RBAC/ABAC/ReBAC; 7-day telemetry.
- Team $500/mo: 100k tx/mo, $1 per 1,000 overage; SSO; 90-day telemetry.
- Enterprise custom/annual: SCIM/AD/LDAP; **dedicated, BYOC or on-prem deployment**; private
  networking; customer-managed KMS; continuous OCSF export; 180-day telemetry; 99.95% SLA.
- All plans: OAuth 2.1, Token Exchange, SPIFFE, WIMSE, MCP, A2A.

## Keycard for Multi-Agent Apps (blog 2026-05-13; Help Net Security 2026-05-15)
- Session per originating user/agent request; scoped credentials issued at each hop and
  **permissions narrow at each hop**; via **OAuth 2.0 Token Exchange (RFC 8693)**.
- Credentials in memory only, expire at session close. Cedar policy evaluated at every hop
  (e.g. block delegating Snowflake access to another server; bar deletes across the chain).
- Agent identity via **workload attestation**; Client ID Metadata Documents for agent-to-agent auth.
- Gateway swaps opaque session-bound creds for real ones for legacy protocols (Postgres, Kafka, HTTP).
- TS/Python SDKs; LangChain, MCP, A2A support (trade press adds Mastra). **Early access.**
- Builds on same platform as Keycard for Coding Agents.

## Anchor.dev acquisition (Pulse2, 2026-02-15; trackers say Feb 10–15)
- Keycard acquired **Anchor.dev** (stealth; automatic certificate issuance/validation);
  terms undisclosed. Team background Cloudflare/GitHub/Heroku; Wesley Beary (ex-Anchor CEO) joins.
- Announced alongside **Keycard for Coding Agents**: governs Cursor, Claude Code, Codex,
  Windsurf; policy at app layer on every tool call; short-lived per-task credentials;
  sensitive ops can require explicit approval.

## CRN (2026-01-29 press release)
- Named one of CRN's 10 cloud computing startups to watch in 2026.
