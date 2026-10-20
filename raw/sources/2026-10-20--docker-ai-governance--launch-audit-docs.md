# Docker AI Governance — launch blog (2026-05-12), audit logs blog (2026-08-03), governance docs

- URL: https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/
- URL: https://www.docker.com/blog/docker-ai-governance-audit-logs-now-where-your-security-team-already-works/
- URL: https://docs.docker.com/ai/sandboxes/security/governance/
- Fetched: 2026-10-20
- Good for: what Docker AI Governance is and governs, policy delivery, licensing posture, audit/SIEM. Vendor marketing (blogs) and vendor docs.

## Launch blog — 2026-05-12, Srini Sekaran
- "Centralized control over how agents execute, what they can reach on the network, which credentials they can use, and which MCP tools they can call".
- "The control plane that sits on top of that runtime. It turns the sandbox and the MCP Gateway into centralized policy, defined once in the admin console, enforced at every node the agent touches, and auditable from end to end."
- Four control surfaces: network and filesystem (allow/deny for domains, IPs, CIDRs; mount rules RO/RW); credentials (scope to session, "blocks exfiltration to unapproved destinations"); MCP tools (org-wide managed policies, "unapproved servers blocked by default"); role-based policy assignment (policy groups, users via IdP, team rules layered on org guardrails that "can't be overridden").
- Delivery: developer authenticates, machine pulls latest policy; SAML and SCIM.
- Enforcement "at the proxy and mount level rather than as an advisory layer".
- "Available now"; "Contact sales"; no price, no tier named, no customers named. Model Runner not part of it.
- Docker site nav (2026-08) describes AI Governance as "Govern agents and Claws across every team".

## Audit logs blog — 2026-08-03, Srini Sekaran and Julie Gray
- Audit logs in Docker Cloud: org-wide searchable view, 90-day retention, CSV export. Local disk delivery still supported.
- SIEM streaming via generic HTTPS endpoint; Splunk and Dynatrace named (other copies of the post also name Datadog and Grafana — unconfirmed).
- Events: Docker Sandboxes policy decisions (allowed / denied / held for a human) and sandbox session events. MCP Gateway enforcement decisions to use the same schema "as they become available" (no date).
- Metadata only: never prompt content, agent output, or parameter values.
- Included with Docker AI Governance; covers users with an AI Governance license under an enforced org policy.

## Governance docs
- Org policies control what local sandboxes can access; apply org-wide or to teams (teams synced from IdP group mapping). Cloud sandboxes not covered (separate network policy).
- Requires "a separate paid subscription" — contact Docker Sales; tier not named.
- Managed in Docker Home under "AI Platform", or via Governance API (network and filesystem only).
- Policy types: network (host, or HTTP method + path; "all traffic" rules for TCP/UDP to hosts/IPs/CIDRs); filesystem (which host paths may be mounted); MCP (Cedar statements: registration, tool calls, resources, prompts, approval gates). Credential policy not covered on this page.
- When org governance active, only org allow rules grant access; local allows not evaluated; local denies still apply.
- Propagation within ~5 minutes; `sbx policy reset` forces sync (and deletes local rules).
- Enforcement timing: network per request; filesystem only at sandbox creation; MCP registration at `sbx mcp add`, use-time rules at the gateway.
- "Require approval before access" option on network policies (developer confirms each destination).
- Default: only org owners view/manage policies; custom roles otherwise. Admin support message up to 500 chars.
- Limitations: cloud sandboxes not covered; filesystem changes don't affect running sandboxes; editing replaces whole policy; one destination per HTTP rule; composer lacks CONNECT/TRACE.

## Secondary (not relied on for facts)
- byteiota.com/docker-ai-governance-agent-security-2026/ — third-party summary.
