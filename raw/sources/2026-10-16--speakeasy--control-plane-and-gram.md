# Speakeasy — AI control plane / MCP gateway (Gram), funding, customers

- URL: https://www.speakeasy.com/
- URL: https://www.speakeasy.com/blog/release-speakeasy-mcp-gateway
- URL: https://www.speakeasy.com/blog/speakeasy-vs-mintmcp
- URL: https://speakeasy.com/blog/partnering-with-tailscale
- URL: https://aaif.io/blog/ai-governance-in-a-regulated-industry-how-moonpay-brought-mcp-sprawl-under-control
- URL: https://www.speakeasy.com/blog/fundraising-series-a
- URL: https://github.com/speakeasy-api/gram (via GitHub API)
- Fetched: 2026-10-16
- Good for: category fit decision (Gram is now a governance gateway, not just dev tooling),
  capabilities, deployment, certifications, funding, customers. Speakeasy pages are vendor marketing.

## Category-fit evidence
- GitHub `speakeasy-api/gram`: created 2025-08-06, **AGPL-3.0**, ~274 stars, pushed 2026-10-16.
  Repo description: "The AI control plane for every agent in your enterprise, built around an
  enterprise-grade MCP gateway... provisioned by role from the IdP you already run, with
  security policy enforced on every action." → Gram is the codebase of the control plane.
- MCP Gateway launch blog (2026-03-10): gateway "grew out of" Gram, the OSS MCP-server
  build platform; Speakeasy found auth, observability and distribution were the real blockers.
  Capabilities: generate servers from OpenAPI, import TS servers, prebuilt integrations;
  unified **OAuth 2.1 layer (DCR, PKCE)**, OAuth proxy to SSO; RBAC at server/toolset/tool;
  client hooks for shadow-server discovery; telemetry/tracing.
- /product/gram returned 404 on 2026-10-16 — Gram branding appears retired in favour of
  "AI Control Plane" (no formal rename notice found).

## Homepage (vendor marketing)
- "The AI control plane for every agent in your enterprise, built around an enterprise-grade
  MCP gateway." Four products on one identity/policy/audit trail: Agent Identity, Agent Security
  (shadow AI, block risky actions, stop data leaks), MCP gateway (registry of approved servers,
  role-based provisioning, shadow MCP discovery), Agent observability.
- Policy checks on every prompt, response and tool call incl. prompt injection / exfiltration.
- Claims **SOC 2 Type II, ISO 27001, GDPR**; markets alignment to EU AI Act, ISO 42001, NIST AI RMF.
- Self-hosted ("your own cloud or on-premises") and cloud. "Deploy for free" CTA; no prices.
- Customers named: Google, **Fifth Third**, Mistral, Cisco, PlanetScale, Vercel, Polar, MoonPay (+Fermat).
  (Logos may reflect legacy SDK-generation customers, not necessarily control-plane customers.)
- Integrations: Okta, Entra ID, Auth0, WorkOS, Google Workspace, Ping, SAML/OIDC; Tailscale, Jamf,
  Intune; Datadog, Grafana, Langfuse, OTel, SIEM alerts; Drata, Vanta; OpenRouter, LiteLLM;
  agents Claude, ChatGPT, Codex, Cursor, Gemini, Copilot, Devin, Mistral.

## Speakeasy vs MintMCP (Speakeasy-authored, 2026-09-22)
- Speakeasy is OAuth authorization server for gateway sessions (OAuth 2.1 + PKCE; DCR or CIMD);
  gateway strips client creds and applies upstream credential — agent never holds vendor key.
- SCIM directory sync from Okta/Entra (~30s). Detectors: secrets, PII, financial, gov ID,
  health; CEL custom rules; LLM-judged plain-language policies replayable on past sessions;
  log/warn/deny/quarantine; fail-open or fail-closed configurable.
- Agent hooks (Anthropic hooks, LiteLLM, device agent macOS/Windows/Linux, Cursor hooks).
- Deployment: managed or self-hosted (VPC, data residency, air-gapped); outbound tunnel; IP
  allowlisting; customer-managed AWS/GCP KMS.

## Tailscale partnership (2026-10-13)
- Gateway runs as a node on the customer's tailnet; public route can be closed; per-org
  attestor attaches Tailscale user/device identity to each request. Enterprise only. Polar
  has run MCP servers on Speakeasy since 2025.

## MoonPay story (AAIF blog, 2026-09-24, joint byline Speakeasy/MoonPay — customer marketing)
- 30-day POC → company-wide rollout; 200+ MCP servers governed; 60,000+ agent sessions;
  5,000+ brokered connections; SSO, per-server/tool/team RBAC, audit logs, SIEM export;
  detection for PII, cardholder data, PHI, secrets, prompt injection, destructive commands.

## Funding
- Series A **$15M**, 2024-10-30, led by **FPV Ventures**, with GV and Quiet Capital (Speakeasy blog).
  Offices San Francisco and London. Co-founders Sagar Batchu (CEO) and Simon (surname not given).
- Third-party profile puts total ≈ $26M (unverified; implies ~$11M prior seed). No 2025–26 round found.

## Search-result extracts (not fetched in full; lower confidence)
- https://www.speakeasy.com/docs/mcp/secure/adding-oauth-servers — docs note MCP spec calls for
  OAuth 2.1 + Dynamic Client Registration, which Google, GitHub and Azure AD don't support; Gram
  offers an OAuth proxy bridging to standard OAuth.
- https://speakeasy.com/roadmap — Q3/Q4 2026 in-progress items incl. MCP catalog, custom
  domains for the control plane, MCP 2026-07-28 spec support (planned, not commitments).
- Product Hunt (~Sep 2025): Gram by Speakeasy open-sourced, self-serve access.
