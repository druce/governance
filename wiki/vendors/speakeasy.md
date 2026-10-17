---
title: Speakeasy
type: vendor
name: Speakeasy
slug: speakeasy
aka: [Gram, Gram by Speakeasy, Speakeasy AI Control Plane, Speakeasy MCP Gateway, speakeasy-api]
primary_category: mcp-gateway
also_listed_in: [tool-identity-integration]
website: https://www.speakeasy.com/
founded: null
hq: San Francisco, CA, USA (also London)
ownership_state: independent
owner: null
ownership_note: Venture-backed. Best-known as an API SDK-generation company; pivoted/expanded into an MCP gateway and "AI control plane" in 2025–26. Last confirmed round $15M Series A (2024-10-30) led by FPV Ventures with GV and Quiet Capital. No 2025–26 round found.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: Series A, $15M, 2024-10-30 (led by FPV Ventures)
market_position: {mcp-gateway: challenger}
deployment_model: [saas, self-hosted, on-prem]
form_factor: [inline-proxy, platform, agent]
data_leaves_tenancy: partial
integrations: [okta, entra, auth0, workos, google-workspace, ping, tailscale, jamf, intune, datadog, grafana, langfuse, opentelemetry, drata, vanta, openrouter, litellm, claude, chatgpt, codex, cursor, gemini, copilot]
mcp_support: gateway
certifications: [soc2-type2, iso27001]
pricing_model: null
fs_traction: claimed
target_customer: mid-market to enterprise
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [mcp, mcp-gateway, ai-control-plane, agpl, oauth-2.1, shadow-ai, agent-hooks, guardrails, pivot-from-devtools, aie-nyc-2026]
sources:
  - {claim: "Gram repo (speakeasy-api/gram) is AGPL-3.0, created 2025-08-06, and now describes itself as 'the AI control plane... built around an enterprise-grade MCP gateway', role-provisioned from the IdP, policy enforced on every action", url: "https://github.com/speakeasy-api/gram", date: 2026-10-16, confidence: high}
  - {claim: "MCP Gateway launched 2026-03-10, grew out of Gram; OAuth 2.1 layer with DCR and PKCE, OAuth proxy to SSO, RBAC at server/toolset/tool level, client hooks for shadow-server discovery, telemetry", url: "https://www.speakeasy.com/blog/release-speakeasy-mcp-gateway", date: 2026-03-10, confidence: medium}
  - {claim: "Four products (Agent Identity, Agent Security, MCP gateway, Agent observability); SOC 2 Type II, ISO 27001, GDPR claims; self-hosted or cloud; named customers incl. Fifth Third, Google, Cisco, MoonPay, Polar; IdP/observability/compliance integrations", url: "https://www.speakeasy.com/", date: 2026-10-16, confidence: medium}
  - {claim: "Gateway is OAuth authorization server; strips client creds and injects upstream credential; SCIM sync from Okta/Entra; detectors for secrets/PII/financial/gov-ID/health, CEL rules, LLM-judged policies; fail-open/closed; self-hosted incl. air-gapped, customer KMS", url: "https://www.speakeasy.com/blog/speakeasy-vs-mintmcp", date: 2026-09-22, confidence: low}
  - {claim: "Tailscale partnership 2026-10-13: gateway as node on customer tailnet, public route closable, per-request user/device identity; Enterprise only", url: "https://speakeasy.com/blog/partnering-with-tailscale", date: 2026-10-13, confidence: medium}
  - {claim: "MoonPay rollout: 30-day POC, 200+ MCP servers governed, 60,000+ agent sessions, SSO/RBAC/audit/SIEM", url: "https://aaif.io/blog/ai-governance-in-a-regulated-industry-how-moonpay-brought-mcp-sprawl-under-control", date: 2026-09-24, confidence: medium}
  - {claim: "$15M Series A 2024-10-30 led by FPV Ventures with GV and Quiet Capital; offices SF and London; product then was REST API tooling and SDK generation", url: "https://www.speakeasy.com/blog/fundraising-series-a", date: 2024-10-30, confidence: high}
  - {claim: "Gold sponsor of AI Engineer NYC 2026; CEO on preview speaker list (Dev Tools & Evals)", url: "https://ai.engineer/nyc", date: 2026-10-16, confidence: high}
---

# Speakeasy

> Primary category: [mcp-gateway](../categories/mcp-gateway.md). Also listed in [tool-identity-integration](../categories/tool-identity-integration.md). This is a developer-tools company that has repositioned around MCP governance. The product formerly marketed as **Gram** is now the "AI Control Plane".

**One-liner** — An MCP gateway and "AI control plane" that gives each team one governed path to its MCP servers. Access is provisioned by role from the corporate IdP, credentials are brokered so agents never hold the underlying API keys, and policy checks run on prompts, responses and tool calls. It grew out of Speakeasy's open-source (AGPL) MCP server platform, Gram.

**Why it is in this wiki (fit decision, 2026-10-16).** This page was raised as a candidate in the belief that Gram was purely tooling for building and hosting MCP servers. That was true at Gram's 2025 launch and is no longer true. The March 2026 gateway launch says Speakeasy concluded that "building servers was not the hardest problem — auth, observability, and distribution were." The Gram repository now describes itself as an enterprise control plane with IdP-provisioned access and per-action policy. That squarely meets the [mcp-gateway](../categories/mcp-gateway.md) definition: allowlist, broker, authenticate, apply policy and audit tool calls. The OAuth brokering layer also qualifies it for [tool-identity-integration](../categories/tool-identity-integration.md). Speakeasy's **SDK-generation** business remains, but it is out of scope here.

**What it does** — Per vendor materials, four products share one identity, policy and audit trail:
- **MCP gateway**: a registry of approved servers, role-based provisioning, and shadow-MCP discovery. Servers can be generated from OpenAPI specs, imported (TypeScript) or picked from prebuilt integrations (Stripe, GitHub, Slack). Progressive tool disclosure (`search_tools` / `execute_tool`) keeps agent context small. Servers can be rolled out org-wide, including as Claude plugins.
- **Agent Identity**: Speakeasy acts as the **OAuth 2.1 authorization server** for gateway sessions (PKCE; Dynamic Client Registration or Client ID Metadata Documents). An **OAuth proxy** bridges to upstream APIs that don't support MCP's DCR requirement, which per Speakeasy's docs includes Google, GitHub and Azure AD. The gateway strips the client's credentials and applies the upstream one, so **the agent never holds the vendor key**. Directory sync from Okta or Entra runs over SCIM. Agent identities are in early access.
- **Agent Security**: inline detectors for secrets, PII, financial data, government IDs and health data, plus custom rules in CEL and plain-language policies that an LLM judges and that can be replayed against past sessions. Actions are log, warn/confirm, deny or quarantine the session, and admins choose fail-open or fail-closed. **Agent hooks** (Anthropic hooks, LiteLLM, Cursor hooks and a device agent for macOS, Windows and Linux) extend enforcement to prompts, shell commands and file edits inside the agent session, which a gateway alone cannot see.
- **Agent observability**: adoption, cost, per-tool latency and errors, and distributed tracing.

**Agent-security role.** In lethal-trifecta terms, Speakeasy acts on the **egress** leg (only sanctioned MCP servers, and unsanctioned ones blocked at the point of use) and on the **sensitive-data** leg (detectors on tool traffic, and least-privilege per-tool grants mapped from the IdP). The agent hooks give it some reach into the **untrusted-input** leg on developer endpoints. The OAuth credential-brokering design matters here: an injected agent that never holds a vendor API key cannot exfiltrate that key. All detection claims are vendor-described, and no independent benchmark was found.

**Naming / provenance** — Speakeasy (GitHub org `speakeasy-api`) is best known for generating SDKs, Terraform providers and API tests from OpenAPI. **Gram** was launched around **August–September 2025** as an open-source platform for building and hosting MCP servers; the repo was created 2025-08-06. The **MCP Gateway** was announced **2026-03-10**. By October 2026 the marketing says "AI Control Plane", the `/product/gram` page returns 404, and the Gram repo carries the control-plane description. No formal rename notice was found, so treat "Gram" as the codebase and legacy brand name. CEO and co-founder: **Sagar Batchu**. Founding year: **unverified**.

**Ownership & viability** — `independent`. The last confirmed round is a **$15M Series A (2024-10-30) led by FPV Ventures**, with **GV** and **Quiet Capital**; it was raised for the *API tooling* business. A third-party profile puts total funding at ~$26M, which is **unverified**. No 2025–26 round was found. The viability question is less about cash than **focus**. The company is running a pivot from devtools into a crowded, fast-moving security category against specialists that raised specifically for it ([runlayer](runlayer.md) $42M, [natoma](natoma.md) bought by Snowflake). The existing SDK customer base and revenue are a cushion the pure-play startups don't have.

*Acquisition-risk note:* plausible acquirers include API-management and gateway vendors ([kong](kong.md)), IdPs, or security platforms. The **AGPL-3.0** licence on the core means a community fork could survive an exit, but AGPL obligations matter if you plan to modify and expose it.

**Positioning & differentiators** —
- **vs [mintmcp](mintmcp.md) and [runlayer](runlayer.md)** (closed-source managed gateways): Speakeasy's core is **source-available under AGPL** and it publishes **SOC 2 Type II and ISO 27001** claims. Runlayer publishes none, and MintMCP lists SOC 2 but not ISO per Speakeasy's comparison. Its unusual strength is the **OpenAPI → MCP server** path inherited from the SDK business: if your firm has internal REST APIs, it can turn them into governed MCP tools.
- **vs [obot](obot.md)** (MIT open-source gateway): both have open code you can inspect. Obot is MIT and permissive. Speakeasy's AGPL is copyleft, so check with counsel before modifying it in-house. Speakeasy adds endpoint agent hooks and a richer guardrail layer.
- **vs [arcade](arcade.md) and [composio](composio.md)** (agent auth plus connectors): there is overlap on OAuth brokering. Speakeasy's centre of gravity is **governance of all MCP traffic** rather than a connector catalog.
- **vs [keycard](keycard.md)**: Keycard is a dedicated credential-issuance and authorization layer (Cedar, per-hop token exchange). Speakeasy's identity piece serves its gateway. Firms wanting a stand-alone agent-identity plane would look at Keycard. Firms wanting one MCP control point with identity included would look at Speakeasy.

**Who should choose them / anti-fit** — Fits a firm that (a) wants **one sanctioned path** for employees' and agents' MCP use across Claude, Cursor, Codex, ChatGPT and others, with IdP-based roles and audit, (b) values **self-hosting, including air-gapped**, plus customer-managed keys, and (c) has internal APIs it wants exposed as governed tools. **Anti-fit:** firms that won't accept AGPL code in their environment. It also doesn't fit buyers who want a vendor whose *only* business is security; Speakeasy is mid-pivot. A fund with no MCP usage doesn't need it.

**Known weaknesses / gotchas** —
- **Mid-pivot vendor.** The governance product is about a year old (gateway GA 2026-03). The customer logos on the homepage (Google, Cisco, Vercel, etc.) may come from the SDK-generation business, not the control plane. Ask which logos are control-plane customers.
- **Most capability detail comes from Speakeasy-authored comparison posts** (e.g. vs MintMCP) and should be verified in a pilot.
- **AGPL-3.0**: free to self-host, but modifications offered over a network trigger source-disclosure obligations.
- Agent identities are **early access**. Roadmap items (MCP catalog, MCP 2026-07-28 spec support) are planned for Q3–Q4 2026, not shipped.

**Deployment & data handling** — **Managed cloud**, or **self-hosted** in your VPC, on-prem or **air-gapped**. Data residency and customer-managed **AWS or GCP KMS** keys are supported. Outbound-only **MCP tunnels** connect private servers without opening inbound ports. Since **2026-10-13** Enterprise customers can run the gateway as a node on their own **Tailscale** tailnet and close the public route entirely, with each request carrying Tailscale user and device identity. The control plane runs on Kubernetes, with per-org isolation of credentials and workloads. It is **inline**: the gateway sees tool-call traffic and audit logs record tool calls, users, prompts and results (MoonPay story). On managed cloud that content transits and is stored by Speakeasy. Self-hosted keeps it in-tenant (`partial`). Retention periods and training-use terms are **unverified**.

**Integrations & partnerships** — IdP: Okta, Entra ID, Auth0, WorkOS, Google Workspace, Ping, any SAML/OIDC. Device and network: Tailscale (partner), Jamf, Intune. Observability: Datadog, Grafana Cloud, Langfuse, OpenTelemetry, with SIEM alert routing. Compliance: Drata, Vanta. AI gateways: OpenRouter, LiteLLM. Agents: Claude, ChatGPT, Codex, Cursor, Gemini, Copilot, Devin, Mistral. Speakeasy is a member of the **Agentic AI Foundation** (AAIF) per the AAIF blog, and was a **Gold sponsor at AI Engineer NYC 2026**, with its CEO on the speaker preview list.

**Compliance & FS traction** — It claims **SOC 2 Type II, ISO 27001 and GDPR** compliance and markets mappings to the EU AI Act, ISO 42001 and NIST AI RMF. The reports were not seen. **FS traction: claimed.** **Fifth Third** (a US regional bank) appears among homepage customer logos, but it is unclear whether that relationship is for SDKs or the control plane. **MoonPay** (crypto payments) co-published a production rollout story covering 200+ MCP servers, 60,000+ agent sessions, SSO, RBAC, audit logs and SIEM export, plus detection for cardholder data. It is the most concrete regulated-industry evidence, though it is co-branded marketing. No hedge-fund or asset-manager reference was found.

**Commercial** — There is a free self-serve start ("Deploy for free"), and the AGPL code can be self-hosted. Enterprise features such as the Tailscale integration are Enterprise-tier. No price list was found.

## Open questions

- Which homepage customers (notably Fifth Third, Google, Cisco) use the **control plane** rather than SDK generation?
- Total funding and any 2025–26 round. Founding year.
- The licensing boundary: which features are AGPL in the repo and which are enterprise-only/closed?
- Audit-log retention and storage region on managed cloud. Training-use terms for scanned content.
- An independent evaluation of the detectors' accuracy and the latency overhead.
- GA date for Agent Identities.
- Whether also_listed_in should add [agent-runtime-security](../categories/agent-runtime-security.md), given the endpoint agent hooks.

## Sources

- [speakeasy-api/gram (GitHub, via API)](https://github.com/speakeasy-api/gram) — fetched 2026-10-16 — supports: AGPL-3.0, repo creation date, control-plane self-description; confidence: high
- [Speakeasy MCP Gateway release (vendor blog, 2026-03-10)](https://www.speakeasy.com/blog/release-speakeasy-mcp-gateway) — fetched 2026-10-16 — supports: gateway launch, Gram lineage, OAuth/RBAC/hooks; confidence: medium
- [Speakeasy homepage (vendor marketing)](https://www.speakeasy.com/) — fetched 2026-10-16 — supports: product lines, certifications claims, deployment, customers, integrations; confidence: medium
- [Speakeasy vs MintMCP (vendor-authored comparison, 2026-09-22)](https://www.speakeasy.com/blog/speakeasy-vs-mintmcp) — fetched 2026-10-16 — supports: OAuth server design, SCIM, detectors, fail-open/closed, air-gapped/KMS; confidence: low (competitor-authored marketing)
- [Speakeasy partners with Tailscale (vendor blog, 2026-10-13)](https://speakeasy.com/blog/partnering-with-tailscale) — fetched 2026-10-16 — supports: tailnet deployment, Polar; confidence: medium
- [How MoonPay brought MCP sprawl under control (AAIF blog, 2026-09-24)](https://aaif.io/blog/ai-governance-in-a-regulated-industry-how-moonpay-brought-mcp-sprawl-under-control) — fetched 2026-10-16 — supports: MoonPay rollout metrics and features; confidence: medium (co-branded customer marketing)
- [Speakeasy's $15M Series A (vendor blog, 2024-10-30)](https://www.speakeasy.com/blog/fundraising-series-a) — fetched 2026-10-16 — supports: round, investors, offices, CEO; confidence: high
- [API Platform Speakeasy Raises $15M (Finovate)](https://finovate.com/api-platform-speakeasy-raises-15-million-in-series-a-funding) — search result 2026-10-16 — supports: round corroboration; confidence: medium
- [AI Engineer NYC 2026](https://ai.engineer/nyc) — fetched 2026-10-16 — supports: Gold sponsorship; confidence: high
- Cached: `raw/sources/2026-10-16--speakeasy--control-plane-and-gram.md`, `raw/sources/2026-10-16--aie-nyc-2026--sponsors-and-sessions.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan). Fit decision: Gram evolved from MCP-server dev tooling into an MCP governance gateway, so the page was written (primary mcp-gateway) rather than rejected.
