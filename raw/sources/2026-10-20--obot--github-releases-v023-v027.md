# Obot — GitHub repo metadata, README, and release notes v0.23.0 → v0.27.0

- URL: https://github.com/obot-platform/obot (via GitHub API: repos/obot-platform/obot, /releases, /readme)
- URL: https://github.com/obot-platform/obot/releases/tag/v0.27.0
- URL: https://github.com/obot-platform/obot/releases/tag/v0.26.2
- URL: https://github.com/obot-platform/obot/releases/tag/v0.25.0
- URL: https://github.com/obot-platform/obot/releases/tag/v0.24.0
- URL: https://github.com/obot-platform/obot/releases/tag/v0.23.0
- URL: https://api.github.com/orgs/obot-platform/repos
- Fetched: 2026-10-20
- Good for: repo health (stars, licence, cadence), product scope as of Oct 2026 (MCP gateway, LLM gateway,
  device enforcement via Obot Sentry, vMCPs, Claude Environments), edition/licensing change. Primary, vendor-authored.

## Repo metadata (GitHub API, 2026-10-20)
- Description: "Complete AI Governance Platform from Obot AI" (was positioned as an MCP platform/gateway in June 2026).
- Stars 1,111; forks 237; open issues 325; licence MIT; not archived; last push 2026-10-20; created 2024-09-05.
- Topics: ai, chat, mcp, modelcontextprotocol.
- Org repos of note: obot-sentry (device agent, MIT), enterprise-providers (MIT, "Enterprise model and auth providers"),
  providers (Apache-2.0), terraform-provider-obot (MPL-2.0), mcp-catalog, pii-filter (MIT), credential-filter (MIT),
  mmmcp ("An MCP multiplexer"). Archived: nanobot (MCP agent framework, 1,361 stars, archived by 2026-09-24),
  hosted-agents-images (archived; superseded by Claude Environments), obot-mcp-server, several single-SaaS MCP servers.

## Release cadence
Stable releases since last check: v0.23.0 (2026-06-17), v0.23.1 (06-18), v0.23.2 (06-22), v0.23.4 (07-14),
v0.24.0 (07-24), v0.24.1 (07-24), v0.25.0 (07-31), v0.25.1–v0.25.6 (08-03 → 09-18), v0.26.0 (09-17),
v0.26.1 (09-25), v0.26.2 (10-02), v0.26.3 (10-08), v0.27.0 (2026-10-20). Still pre-1.0.

## Release highlights (quoted/paraphrased from release notes)
- v0.23.0 (2026-06-17): UI split into administration vs consumption; "introduces enterprise licensing";
  LLM Gateway usable by external coding agents (Claude Code, Codex) as their model endpoint; multi-user MCP
  server templates in Git-backed catalog; MCP discovery from CLI; Enterprise License Key.
- v0.24.0 (2026-07-24): Device Management via companion agent **Obot Sentry** — MDM enrollment (Microsoft Intune
  first; Jamf planned), device scans, managed hooks for Claude Code, Codex, VS Code, Cursor; "Every tool call those
  tools make is submitted back to Obot and recorded in the MCP Audit Logs". Device Management "remains in Beta".
  **LLM Audit Logs** — every LLM Gateway request logged with model, provider, user-agent, token usage, outcome;
  Auditor role can view full request/response bodies. LLM Gateway providers added: AWS Bedrock, Azure (OpenAI +
  Microsoft Foundry, Entra service principal), generic Responses-compatible. MCP proxy moved in-process (smaller footprint).
  Built-in local auth (dev/test only).
- v0.25.0 (2026-07-31): **Tool Call Enforcement for Local AI Clients** — allowlist enforced by Obot Sentry before
  Claude Code/Codex/Cursor run a tool; "Enforcement fails closed"; marked "experimental and is not yet recommended
  for production use"; not supported for VS Code. **MCP Tunnels** (outbound WebSocket from private network, for Obot
  Cloud users). **Agent Auth Scopes** (replace API keys; scoped to MCP servers, API, LLM proxy, skills, device scans;
  expiry). **Editions**: "The code remains 100 percent MIT licensed, and parts that were previously closed source,
  including the enterprise auth providers and model providers, are now open source." Default edition up to 100 users
  and 100 devices with GitHub/Google/Local auth; Community adds Entra, Okta, JumpCloud, Auth0 at same limits;
  Enterprise removes limits and adds support.
- v0.26.0 (2026-09-17) / v0.26.2 (2026-10-02): **Virtual MCP servers (vMCPs)** replace composite servers;
  components pinned to catalog snapshots (catalog edit/failed sync no longer changes running servers); additive
  user/group profiles grant tools — a user "can narrow their grant but never widen it". MCP tester; detached catalog
  entries; opt-in anonymous product analytics (off until admin consents). v0.26.0 "Existing installations should
  not upgrade"; upgrade path delivered in v0.26.2 with a startup data migration (scale to 1 replica, Recreate
  strategy); legacy MCP server REST APIs removed; static config values now stored as credentials.
- v0.27.0 (2026-10-20): **Claude Environments** (experimental, disabled by default) — run Claude cloud sessions on
  your own Kubernetes; Obot decides who can start a session, which vMCPs it can use, egress allowlist, CPU/memory;
  "destination-specific secrets are injected at the egress gateway, so the session never sees them"; every egress
  request in Audit Logs; uses Agent Substrate; requires Claude Team/Enterprise with self-hosted environments;
  "replaces the former Hosted Agents feature". OpenAPI-backed MCP servers (no upstream OAuth flows). Okta SCIM
  provisioning (deprovision in Okta deactivates Obot user and credentials). Japanese/Korean/Simplified Chinese UI.
  Tool search for vMCPs (search_tools/call_tool; each call still authorized and audited as the underlying tool).
  Built-in credential filter configurable from UI.
- Earlier 2026 context: v0.20.0 (2026-04-28) MCP Filters + filter mutation, JumpCloud; v0.21.0 (2026-05-05) MCP
  server egress control with Aviatrix integration; v0.22.0 (2026-05-27) centrally managed skills + `obot scan`.

## README (2026-10-20)
"Obot is an open-source platform for organizations to manage, secure, and govern their AI ecosystems." Core
capabilities: MCP Gateway (proxy, composite, per-user/group tool access, MCP OAuth + credential management,
"Inspect, reject, or modify MCP requests and responses with MCP or webhook filters"); LLM Gateway (OpenAI, Anthropic,
Bedrock, Azure; model access policies; records requests/responses, token usage, estimated cost); sandboxed hosted MCP
servers and agents with domain-based egress rules; MCP and Skills registries (standard MCP Registry API, Git-backed);
Obot CLI and skill; Obot Sentry (device inventory + hooks; beta); identity and access control; correlated audit logs
with one-time or scheduled export. Docker quickstart mounts the Docker socket — "Use it only for development,
evaluation, or trusted single-tenant environments. Use the Kubernetes deployment for production". Licence: MIT.
