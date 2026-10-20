---
title: Obot
type: vendor
name: Obot
slug: obot
aka: [Obot AI, Acorn Labs, GPTScript, Obot MCP Gateway, Obot Platform]
primary_category: mcp-gateway
also_listed_in: []
website: https://obot.ai
founded: 2022
hq: Cupertino, California, USA
ownership_state: independent
owner: null
ownership_note: Independent VC-backed startup; formerly Acorn Labs, rebranded to Obot AI 2025-09-23. No M&A found as of 2026-10-20.
acquisition: {announced: null, closed: null, price: null}
funding_total: $35M (seed)
last_funding: Seed, $35M, announced 2025-09-23 (co-led by Mayfield and Nexus Venture Partners)
market_position: {mcp-gateway: challenger}
deployment_model: [self-hosted, saas]
form_factor: [platform, inline-proxy, agent, api]
data_leaves_tenancy: partial
integrations: [okta, entra, jumpcloud, auth0, google, github, microsoft-intune, aws-bedrock, azure-openai, anthropic, openai, aviatrix, claude-code, codex, cursor, vscode, mcp-registry-api]
mcp_support: gateway
certifications: []
pricing_model: "Open-core by licence key, same MIT code: free Community edition (up to 100 users / 100 devices); free Registered Community adds Entra/Okta/JumpCloud/Auth0; Enterprise (self-hosted, quote-based, removes caps, adds support); Obot Cloud (hosted, free trial then paid). No public price list."
fs_traction: unverified
target_customer: enterprise IT / platform teams governing employee and agent use of MCP servers, models and local coding agents
last_verified: 2026-10-20
verify_after: 2027-04-20
tags: [mcp, open-source, oauth, audit, agent-platform, llm-gateway, device-management, coding-agents]
sources:
  - {claim: "Repo described as 'Complete AI Governance Platform'; MIT; 1,111 stars; release v0.27.0 2026-10-20; still pre-1.0; nanobot repo archived", url: "https://github.com/obot-platform/obot", date: 2026-10-20, confidence: high}
  - {claim: "v0.23.0 2026-06-17 enterprise licensing + LLM Gateway for external coding agents; v0.24.0 2026-07-24 Obot Sentry device management (beta), LLM audit logs, Bedrock/Azure providers", url: "https://github.com/obot-platform/obot/releases/tag/v0.24.0", date: 2026-07-24, confidence: high}
  - {claim: "v0.25.0 2026-07-31 tool-call enforcement for local AI clients (experimental, fail-closed), MCP tunnels, Agent Auth Scopes; editions introduced; enterprise auth/model providers open-sourced, code remains 100% MIT", url: "https://github.com/obot-platform/obot/releases/tag/v0.25.0", date: 2026-07-31, confidence: high}
  - {claim: "v0.26.0 2026-09-17 virtual MCP servers (vMCPs) replace composite servers; upgrade path only in v0.26.2 2026-10-02 with data migration; legacy MCP server REST APIs removed", url: "https://github.com/obot-platform/obot/releases/tag/v0.26.2", date: 2026-10-02, confidence: high}
  - {claim: "v0.27.0 2026-10-20 experimental Claude Environments (self-hosted Claude sessions on K8s, egress allowlist, secret injection at egress gateway; replaces Hosted Agents), OpenAPI-backed MCP servers, Okta SCIM, tool search for vMCPs", url: "https://github.com/obot-platform/obot/releases/tag/v0.27.0", date: 2026-10-20, confidence: high}
  - {claim: "Editions: same MIT image, differ only by licence key; Community 100 users/100 devices; Registered Community adds enterprise IdPs; Enterprise removes caps; Obot Cloud hosted; licence re-checked every 24h", url: "https://docs.obot.ai/enterprise/overview", date: 2026-10-20, confidence: high}
  - {claim: "No new funding, acquisition or rename found Jun-Oct 2026; aggregator valuation/ARR claims uncorroborated", url: "https://obot.ai/blog/", date: 2026-10-20, confidence: medium}
  - {claim: "$35M seed 2025-09-23 co-led by Mayfield and Nexus; rename from Acorn Labs; founders; Cupertino HQ", url: "https://obot.ai/acorn-labs-is-now-obot-ai/", date: 2025-09-23, confidence: high}
---

# Obot

> Researched 2026-06-28; refreshed 2026-10-20. Primary category: [mcp-gateway](../categories/mcp-gateway.md).

**One-liner**: An open-source (MIT) control plane between an organization's AI clients and the tools and models they use. It started as an MCP gateway and catalog. As of October 2026 it also includes an LLM gateway, a device agent that audits and can block tool calls made by local coding agents (Claude Code, Codex, Cursor), a skills registry, and an experimental way to run Claude sessions on your own Kubernetes.

## What it does

Obot sits between AI clients and Model Context Protocol (MCP) servers (local, remote or hosted) and brokers every connection. Instead of each developer wiring agents directly to MCP tools, with credentials scattered across client configs, the organization gets one entry point. In October 2026 the GitHub repo was retitled "Complete AI Governance Platform from Obot AI" (in June 2026 it was described as an MCP platform). The scope grew in four releases between June and October 2026:

- **MCP gateway with virtual MCP servers (vMCPs), v0.26, 2026-09-17.** A vMCP bundles one or more catalog entries behind one endpoint. Each component is pinned to a snapshot of its catalog entry, so an edit to the catalog or a failed Git sync does not silently change a running server. Changes only apply through an explicit upgrade. Access comes from additive user and group profiles: a user can narrow their own tool grant but never widen it. MCP and webhook **filters** (since v0.20, April 2026) can inspect, reject or modify MCP requests and responses. The org publishes `pii-filter` and `credential-filter` filters, and the credential filter can be configured from the UI as of v0.27. A tool-search mode (v0.27) shows clients only `search_tools`/`call_tool`, and every call is still authorized and audited as the underlying tool.
- **Catalog / registry.** Curated, Git-backed catalogs of approved MCP servers and agent skills, exposed through the standard MCP Registry API, with per-entry access policies. As of v0.27 any HTTP API with an OpenAPI schema can be published as an MCP server without writing one. These servers forward API keys or bearer tokens but do not run OAuth flows against the upstream API.
- **Credential and identity brokering.** Obot handles MCP OAuth server-side, so downstream credentials are not exposed to the AI client. Headless agents get **Agent Auth Scopes** (v0.25, 2026-07-31): scoped, expiring keys limited to named MCP servers, the LLM proxy, skills or device scans. **Okta SCIM provisioning** (v0.27) means removing a user in Okta deactivates them in Obot and revokes their keys.
- **LLM gateway** (external clients from v0.23, 2026-06-17). Provider-compatible endpoints for OpenAI, Anthropic, AWS Bedrock and Azure/Microsoft Foundry. Provider keys stay in Obot, model access policies control which models each user can call, and LLM audit logs (v0.24) record every request with token usage and estimated cost. Users with the Auditor role can view full prompt and response bodies.
- **Device management via Obot Sentry** (v0.24, 2026-07-24, **beta**). An endpoint agent, deployable through Microsoft Intune (Jamf planned), inventories local AI clients, MCP servers and skills. It installs hooks in Claude Code, Codex, VS Code and Cursor so their local tool calls land in the same audit log as gateway traffic. v0.25 added **tool-call enforcement**: an allowlist checked before the local client runs a tool, failing closed. The vendor labels this "experimental and ... not yet recommended for production use", and it does not work for VS Code.
- **Hosted workloads.** Obot can host `npx`/`uvx`/container MCP servers on Docker or Kubernetes with domain-based egress rules. v0.21 (2026-05) added Aviatrix integration for egress control. v0.27 (2026-10-20) adds **Claude Environments** (experimental, off by default). Users keep working in Claude while the session runs on the customer's Kubernetes. Obot decides who can start a session, which vMCPs it can reach and which hosts it can call, and it injects secrets at the egress gateway so the session never sees them. Every egress request is logged. This requires a Claude Team or Enterprise organization with self-hosted environments enabled, and it replaces the earlier "Hosted Agents" feature.
- **Audit.** Correlated logs across MCP calls, LLM calls, hosted workloads and device-side tool calls, filterable by user, server, tool, model, device or session, with one-time or scheduled export.

**Lineage cleanup.** The `nanobot` MCP agent framework repo was archived by 2026-09-24, and the hosted-agents images were archived in October 2026. The earlier agent-builder lineage (GPTScript → Obot agents → Nanobot) has been wound down in favor of governance.

## Where it sits in the stack

Primary category: [mcp-gateway](../categories/mcp-gateway.md), the **model/prompt → tool-access** layer. Since mid-2026 Obot also covers ground that belongs to [ai-gateway](../categories/ai-gateway.md) (its LLM gateway) and endpoint visibility into coding agents. Those are secondary features, and the MCP gateway is still what it is evaluated on.

Lethal-trifecta role: it constrains two legs. By gating which MCP servers and tools an agent can invoke, brokering credentials, and (for hosted servers and Claude Environments) enforcing egress allowlists, it limits **egress**. Its curated catalog, snapshot-pinned vMCPs and request/response filters reduce exposure to **untrusted input** from rogue or drifting MCP servers. On **sensitive data** it is still mostly an access-control product. The PII and credential filters are a first step toward content inspection, but they are not a DLP engine. Pair it with a runtime guardrail or DLP layer if content inspection matters.

Trust zones: it sits on the boundary between internal agents (yellow zone) and external tools and SaaS (red zone) and enforces policy there. With Sentry it also reaches onto developer laptops, where coding agents act outside any network choke point.

## Deployment & architecture

- **Self-hosted**: Kubernetes for production (Docker for evaluation only; the Docker quickstart mounts the host Docker socket). External Postgres, optional S3-compatible storage. Helm chart and Terraform provider are available.
- **Obot Cloud**: hosted by Obot. MCP tunnels (v0.25) let it reach MCP servers on a private network over an outbound WebSocket, with no inbound port.
- **Data handling (`data_leaves_tenancy: partial`)**: when self-hosted, MCP and LLM traffic and the audit logs stay in your environment. Two things still leave it. Licence keys are validated against Obot's licence service at startup and every 24 hours, and anonymous product analytics (v0.26) can be sent, but are off until an admin opts in or the operator forces a setting. With Obot Cloud, traffic and logs live with Obot.
- **Inline**: the MCP and LLM gateways are inline proxies, so every call adds a hop. No vendor latency figures were found. v0.24 moved the MCP proxy into the main server process, so remote servers no longer each need their own pod.
- **Operational gotchas**: the product is pre-1.0 and changes fast (13 stable releases from 2026-06-17 to 2026-10-20). The vMCP change in v0.26 broke upgrades: v0.26.0 told existing installs not to upgrade, and a data migration (scale to one replica, Recreate strategy, catalog YAML conversion) only arrived in v0.26.2. Legacy MCP-server REST APIs were removed. Budget platform-team time for upgrades.

## Positioning & differentiators

**Market position: challenger** in [mcp-gateway](../categories/mcp-gateway.md). It is one of the broadest open-source MCP control planes (gateway, registry, hosting, LLM gateway and device hooks in one MIT codebase, about 1.1k GitHub stars as of 2026-10-20) from a seed-stage company. No market-share data was found, and the category has no settled leader.

Differentiators vs named peers:
- vs **[mintmcp](mintmcp.md)** and **[natoma](natoma.md)**: Obot is fully open source and self-hostable. Those two are SaaS-first managed gateways.
- vs **[docker-mcp-gateway](docker-mcp-gateway.md)**: Docker is strong on container packaging and its catalog. Obot adds multi-user IdP governance, per-tool profiles and audit.
- vs **[ibm-contextforge](ibm-contextforge.md)** and **[agentgateway](agentgateway.md)**: similar open-source gateway and registry scope, but Obot also governs local coding agents on endpoints through Sentry, which those projects do not.
- vs **[arcade](arcade.md)** and **[pomerium](pomerium.md)**: Arcade is a developer SDK for tool auth, and Pomerium comes from zero-trust access proxies. Obot is an admin control plane.

**Who should choose it**: a fund with a platform team that already runs Kubernetes, wants agent-to-tool traffic and logs inside its own environment, and is starting to see Claude Code or Cursor used against internal systems.

**Who should not**: a shop that wants a managed product with a stable API and no upgrade work, or one that needs DLP-grade content inspection on tool traffic.

## Ownership, funding & M&A

- **Independent, VC-backed.** Founded **2022** as **Acorn Labs** in **Cupertino, CA**, and rebranded to **Obot AI** on **2025-09-23**. No acquisition, and none found in searches on 2026-10-20.
- **Funding:** a **$35M seed**, announced **2025-09-23**, co-led by **Mayfield** and **Nexus Venture Partners**. No new round found from June to October 2026. Aggregator claims of a $180M valuation with an a16z/Index lead (salestools.io), or "$0 funding, bootstrapped, ~$2.1M ARR" (getlatka), contradict the primary announcement and are not adopted.
- **Founders / leadership:** Sheng Liang (CEO), Darren Shepherd, Shannon Williams and Will Chan, the team behind **Rancher Labs** (acquired by SUSE) and **Cloud.com** (acquired by Citrix).
- **Viability / acquisition risk:** about 13 months after a large seed, with no Series A reported as of 2026-10-20, so watch runway. The founders have sold infrastructure companies twice. Plausible acquirers include identity, SASE or platform vendors buying an MCP or agent control plane. Because the code is MIT and the enterprise providers are now open source too, customers could keep running a fork if the company exits. Support and roadmap would not survive that, though.

Ownership confidence: **high**. Funding-history confidence: medium.

## CTO / hedge-fund lens

An MCP gateway is a **Day-2** capability: you need one once agents call tools against real systems. Two mid-2026 changes make Obot more relevant to small and mid-size funds than it was in June:

1. **Licensing.** As of v0.25 (2026-07-31) the enterprise IdP connectors (Entra, Okta) are open source and free under "Registered Community", capped at 100 users and 100 devices. A fund under that size can run SSO-integrated Obot without a contract. It just does not get vendor support.
2. **Coding-agent governance.** Sentry's audit hooks and allowlist for Claude Code, Codex and Cursor address a real gap: quant developers' local agents calling tools that no network gateway sees. Enforcement is experimental, so treat it as visibility for now, not control.

Caveats: young company, pre-1.0 software with breaking upgrades, device management still in beta, Claude Environments experimental. No certifications or financial-services references were found. The audit log, which records full request and response bodies and is restricted to the Auditor role, is useful for compliance and incident response. It also contains sensitive content, so its retention and access need to be governed. **Fit: medium**, rising for funds that already run Kubernetes.

## Competitors / alternatives

[mintmcp](mintmcp.md), [docker-mcp-gateway](docker-mcp-gateway.md), [ibm-contextforge](ibm-contextforge.md), [agentgateway](agentgateway.md), [arcade](arcade.md), [pomerium](pomerium.md), [natoma](natoma.md), [truefoundry](truefoundry.md) (MCP gateway as part of a broader AI gateway platform).

## Open questions / to verify

- Exact funding chronology: was the $35M a single 2025 seed, or cumulative with an earlier Acorn Labs round? Aggregator data is inconsistent.
- Certifications (SOC 2 etc.) for Obot Cloud: none found.
- Production references and scale: no named enterprise or financial-services deployments found.
- Whether to cross-list in [ai-gateway](../categories/ai-gateway.md), now that the LLM gateway ships. That would need a survey-v2.csv row (human decision).
- Enterprise pricing bands: quote-based, and no public price list was found (obot.ai/pricing/ returned 404 on 2026-10-20).
- Inline latency overhead of the MCP and LLM gateways: no figures found.

## Sources

- [GitHub: obot-platform/obot](https://github.com/obot-platform/obot): fetched 2026-06-28 and 2026-10-20. Supports MIT licence, repo description, stars, release cadence and archived repos. Confidence: high. Cached: `raw/sources/2026-10-20--obot--github-releases-v023-v027.md`.
- [Obot release notes v0.23.0–v0.27.0](https://github.com/obot-platform/obot/releases): fetched 2026-10-20. Supports LLM gateway, Sentry device management, tool-call enforcement, editions, vMCPs, Claude Environments, upgrade gotchas. Confidence: high (primary). Cached: same file.
- [Obot docs: editions](https://docs.obot.ai/enterprise/overview): fetched 2026-10-20. Supports edition limits, licence-key mechanics, Obot Cloud. Confidence: high. Cached: `raw/sources/2026-10-20--obot--docs-editions.md`.
- [Obot blog index](https://obot.ai/blog/) and funding searches: fetched 2026-10-20. Supports the finding that no new funding or M&A was found; the aggregator claims are rejected. Confidence: medium. Cached: `raw/sources/2026-10-20--obot--funding-ownership-check.md`.
- [Obot MCP Gateway Platform](https://obot.ai/mcp-gateway-platform/): fetched 2026-06-28. Supports the June 2026 feature set and IdP list. Confidence: medium (vendor marketing).
- [Obot MCP Gateway launch coverage](https://www.helpnetsecurity.com/2025/08/15/obot-mcp-gateway-adoption-mcp-servers/): fetched 2026-06-28. Supports open-source positioning and the creator. Confidence: high (independent trade press).
- [Acorn Labs is Now Obot AI](https://obot.ai/acorn-labs-is-now-obot-ai/): fetched 2026-06-28. Supports rename date 2025-09-23, $35M seed, founders, HQ. Confidence: high (primary).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Obot = open-source MIT-licensed MCP gateway/platform (catalog + OAuth + per-tool RBAC + audit) from Obot AI, formerly Acorn Labs (founded 2022, Cupertino), rebranded 2025-09-23 with a $35M seed co-led by Mayfield and Nexus; founders are the Rancher/Cloud.com team; lineage GPTScript → Obot. Kept primary category [mcp-gateway](../categories/mcp-gateway.md). Ownership high confidence (independent, no M&A); funding-history confidence medium. hedge_fund_fit set to medium (good self-host story, but young/OSS, IdP behind Enterprise tier). 4 sources cached.
- [2026-10-20] Refreshed from GitHub (v0.23.0–v0.27.0) and docs. Scope widened from MCP gateway to an AI governance platform: LLM gateway with audit logs, Obot Sentry device hooks and experimental tool-call enforcement for local coding agents, Agent Auth Scopes, MCP tunnels, vMCPs (breaking upgrade), and experimental Claude Environments (2026-10-20). Soft update to the 2026-06-28 claim that "Okta/Entra sit behind the paid Enterprise edition": true then, but superseded on 2026-07-31 (v0.25), when the enterprise providers were open-sourced and offered free under Registered Community, up to 100 users and 100 devices. Nanobot repo archived. No new funding or M&A found. Set market_position challenger, mcp_support gateway, form_factor, data_leaves_tenancy partial, integrations, pricing_model, sources. also_listed_in unchanged (possible ai-gateway cross-list flagged for the human). 3 sources cached.
