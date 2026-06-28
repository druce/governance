---
type: vendor
name: MintMCP
slug: mintmcp
categories: [mcp-gateway]
layer: model-prompt
aliases: ["Dependable AI, Inc."]
website: https://www.mintmcp.com
founded:
hq: San Francisco, CA, USA
ownership: independent
ownership_detail: "Venture-backed startup; legal name Dependable AI, Inc. Public launch 2026-02-05. Backers reported as Coatue, Hustle Fund, Maven Ventures, WVV Capital (+ angels); raise amount not disclosed in a primary source."
ownership_confidence: medium
funding_total:
last_funding:
deployment: [saas, self-hosted, inline-proxy, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [egress, untrusted-input, sensitive-data]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [mcp, agent-governance, gateway, soc2]
---

# MintMCP

> Researched 2026-06-28. Primary category: [mcp-gateway](../categories/mcp-gateway.md). Young (publicly launched Feb 2026), venture-backed; product detail is good, financials are thin.

**One-liner** — A managed enterprise gateway that sits between AI clients (Claude, Cursor, custom agents) and MCP servers, hosting the servers, handling SSO/credentials, enforcing per-role tool access, and logging every tool call.

## What it does

MintMCP is an **MCP gateway plus agent monitor**. Instead of every developer installing and configuring MCP servers locally with their own credentials, MintMCP hosts the MCP servers centrally and puts a control plane in front of them. It offers an "MCP store" of pre-approved/hosted connectors (100+ integrations claimed — Snowflake, BigQuery, Databricks, Slack, Teams, Google Drive, SharePoint, Confluence, custom APIs), wires them to enterprise SSO, and grants access by role.

Two products:
- **MCP Gateway** — authentication, credential management, hosting, and access control for MCP servers. Uses **Virtual MCP Bundles**: curated sets of servers/tools mapped to org roles (e.g. Engineering → GitHub/Linear/Datadog; Sales → Salesforce/HubSpot), with SCIM group membership auto-granting the right bundle.
- **Agent Monitor** — real-time visibility into agent behavior (file operations, command execution, tool calls) with guardrails that detect PII exposure, credential leakage, risky bash commands, and prompt-injection attempts, and can block/flag/alert.

The pitch is closing the "shadow AI" gap — developers running unmonitored local agents with broad credentials — by giving each agent its own scoped, rotatable identity and routing all tool traffic through one auditable choke point.

## Where it sits in the stack

Primary category: [mcp-gateway](../categories/mcp-gateway.md) (layer: model-prompt / agent tool-access control). It's a **policy and identity layer for agent→tool calls**, not a model firewall.

Lethal-trifecta role — it touches all three legs, though as a control point rather than deep content inspection:
- **Egress / sensitive-data exfiltration** — granular authorization (read-only DB access, blocking CRM bulk exports), plus PII/credential-leak detection on tool outputs; can hand off to Bedrock Guardrails, GCP DLP, or Microsoft Purview.
- **Untrusted input** — prompt-injection detection in Agent Monitor; inline policy via JavaScript sandboxes.
- **Sensitive data access** — per-agent scoped credentials and role-based tool sets limit blast radius.

Trust zones: it's the broker between the agent (yellow) and internal systems / SaaS (green), and it brokers untrusted tool results back (red).

## Deployment & architecture

- **Managed SaaS** is the default: MintMCP hosts the MCP servers (including STDIO-based servers) and manages their lifecycle and credentials. **Self-hosted** is offered via enterprise engagement.
- Acts as an **inline proxy** between AI clients and MCP servers; every request is authenticated, routed, policy-checked, and logged.
- **Identity/SSO:** OAuth 2.0, SAML, SSO; integrations named for Okta and Azure AD; **SCIM** for group-driven RBAC.
- **Audit:** structured logs (timestamp, agent/user attribution, tool call, policy decision); retention 90 days–7 years; export to SIEM (Sentinel, Splunk, S3).
- **Guardrail integrations:** AWS Bedrock Guardrails, GCP DLP, Microsoft Purview.
- **Compliance:** SOC 2 Type II audited; HIPAA with BAA available; encryption in transit/at rest; data-residency options; uptime SLAs (per vendor; not independently verified here).

## Positioning & differentiators

MintMCP positions as **managed-and-compliant first**: you get governed MCP access without operating connector infrastructure yourself. That's the main axis separating it from neighbors:

- vs [ibm-contextforge](ibm-contextforge.md) — ContextForge is self-hosted, Apache-2.0 open source you run and customize; MintMCP is the hosted, SOC-2/SSO/SCIM-out-of-the-box alternative (vendor's own comparison; read as marketing).
- vs [docker-mcp-gateway](docker-mcp-gateway.md) — Docker's gateway is a developer/runtime packaging-and-isolation tool; MintMCP is an org-level governance/identity layer.
- vs [obot](obot.md) — the seed bundled "Obot / MintMCP"; both are MCP-gateway plays, but they are **separate companies** (Obot is its own project/vendor). MintMCP leans managed-SaaS + agent monitoring; confirm Obot's posture on its own page.
- vs [agentgateway](agentgateway.md) — agentgateway is open-source data-plane proxy tech; MintMCP is a managed product with a console, store, and monitoring.
- vs [natoma](natoma.md), [arcade](arcade.md), [pomerium](pomerium.md) — overlapping MCP access-control / agent-identity space; differentiators are managed hosting, Virtual MCP Bundles, and the bundled Agent Monitor.

Differentiator to highlight: **Virtual MCP Bundles + SCIM-driven role bundles**, and the **bundled agent-behavior monitor** (not just a gateway).

## Ownership, funding & M&A

- **Independent venture-backed startup.** Legal entity reported as **Dependable AI, Inc.**
- **Founders:** Jiquan Ngiam (co-founder & CEO; ex-Google Brain, ex-Coursera), Vijay Vasudevan (ex-Google), Bozhi "Bo" See (ex-Brilliant Home, Shopkick). Founders described as early Google Brain members; advised by Andrew Ng.
- **Backers reported:** Coatue, Hustle Fund, Maven Ventures, WVV Capital; angels incl. Andrej Karpathy, Jeff Dean, Scott Belsky. **Raise amount and round not disclosed** in a primary source seen — left blank.
- **Public launch:** 2026-02-05 (press release).
- **HQ:** San Francisco (press/LinkedIn). Founding year not confirmed — left blank.
- No M&A; no acquisition flagged in seed. (Seed only bundled the name with Obot.)

## CTO / hedge-fund lens

- **Day-2, conditional on Day-1.** You only need an MCP gateway once agents are actually calling internal tools/data. For a fund, MintMCP becomes relevant when desk/quant/ops teams start wiring Claude/Cursor agents to Snowflake, SharePoint, Slack, internal APIs — at which point ungoverned local MCP credentials are a real exfiltration and audit problem.
- **Fit: medium.** The managed model is attractive for a small IT/security team (no connector infra to run), and SOC 2 / SSO / SCIM / SIEM-export / 7-year retention map cleanly onto financial-sector audit and surveillance expectations. Caveats: (1) it's a **new company (launched 2026)** — diligence the SOC 2 report, data residency, and roadmap stability; (2) **managed SaaS means MintMCP hosts your connectors and brokers credentials** — that concentration may be a non-starter for the most sensitive data unless self-hosted; evaluate the self-hosted option. Guardrail/PII claims lean partly on third-party engines (Purview, GCP DLP, Bedrock) — verify what's native vs delegated.
- Not a model-risk / SR 11-7 tool; it's access governance and audit plumbing.

## Competitors / alternatives

[obot](obot.md), [ibm-contextforge](ibm-contextforge.md), [docker-mcp-gateway](docker-mcp-gateway.md), [agentgateway](agentgateway.md), [natoma](natoma.md), [arcade](arcade.md), [pomerium](pomerium.md)

## Open questions / to verify

- Funding round, amount, and date (not disclosed in a primary source as of 2026-06-28).
- Founding year and exact incorporation (Dependable AI, Inc.).
- Self-hosted deployment details — is it full feature parity, and where do credentials live?
- Native vs delegated guardrails: which detections are MintMCP's own vs Purview/GCP DLP/Bedrock.
- Relationship/overlap with [obot](obot.md) beyond the seed's bundling — confirm they are unrelated companies.
- SOC 2 Type II report scope and any independent corroboration of compliance claims.

## Sources
- [MintMCP — Docs: Intro](https://www.mintmcp.com/docs/intro) — fetched 2026-06-28 — supports: gateway definition, architecture, SSO/RBAC/audit, deployment, integrations; confidence: high (vendor primary)
- [MintMCP — Home / About](https://www.mintmcp.com/about) — fetched 2026-06-28 — supports: founders + backgrounds, investors, customers, two-product structure; confidence: med (vendor primary; investor list secondary)
- [MintMCP Blog — What is an Agent Gateway?](https://www.mintmcp.com/blog/agent-gateway) — fetched 2026-06-28 — supports: Virtual MCP bundles, per-agent identity, egress/authorization, guardrails, audit/SIEM; confidence: med (vendor marketing)
- [MintMCP Launches Enterprise Governance Platform (Yahoo Finance / press release)](https://finance.yahoo.com/news/mintmcp-launches-enterprise-governance-platform-175800023.html) — fetched 2026-06-28 — supports: 2026-02-05 launch, CEO, HQ, named customers, SOC 2; confidence: med (vendor PR via aggregator)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established MintMCP as an independent venture-backed enterprise MCP gateway + agent monitor (managed SaaS, self-host optional), legal name Dependable AI Inc., SF, founders Jiquan Ngiam/Vijay Vasudevan/Bozhi See, publicly launched 2026-02-05, backers Coatue/Hustle Fund/Maven/WVV (amount undisclosed). Set ownership_confidence medium, hedge_fund_fit medium, status researched. Kept category [mcp-gateway](../categories/mcp-gateway.md). Cached 4 sources.
