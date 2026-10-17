---
title: Tetrate
type: vendor
name: Tetrate
slug: tetrate
aka: [Tetrate Agent Router, Tetrate Agent Router Enterprise, Tetrate Agent Router Service, TARS, Envoy AI Gateway, Agent Router (AAIF), Tetrate Service Bridge]
primary_category: ai-gateway
also_listed_in: [mcp-gateway]
website: https://tetrate.io/
founded: 2018
hq: Milpitas, California, USA (self-described "Silicon Valley", remote-first)
ownership_state: independent
owner: null
ownership_note: Private, VC-backed. Series A ~$12.4M (2019); $40M Series B led by Sapphire Ventures (announced 2021-03-10). No later round or M&A found as of 2026-10-16. Co-creator and a maintainer of the open-source Agent Router project (formerly Envoy AI Gateway, Apache-2.0), which moved to the Agentic AI Foundation in September 2026 with a multi-company maintainer group.
acquisition: {announced: null, closed: null, price: null}
funding_total: "~$52.5M (third-party aggregate; unverified)"
last_funding: "$40M Series B, 2021-03-10 (Sapphire Ventures lead; Scale Venture Partners, NTTVC, Dell Technologies Capital, Intel Capital, 8VC, Samsung NEXT)"
market_position: {ai-gateway: challenger, mcp-gateway: challenger}
deployment_model: [saas, self-hosted, hybrid, on-prem]
form_factor: [inline-proxy, api, platform]
data_leaves_tenancy: partial
integrations: [envoy, kubernetes, openai, anthropic, google-gemini, azure-openai, aws-bedrock, opentelemetry, openinference, aws, azure, gcp, openshift, carahsoft, finos]
mcp_support: gateway
certifications: [soc2-type2]
pricing_model: "Agent Router Service: usage (model cost + routing fee, free signup credit). Agent Router Enterprise: flat licence by capability and deployment footprint, quote-based. OSS Agent Router: free (Apache-2.0)."
fs_traction: claimed
target_customer: large enterprise, regulated industries and government running Envoy/Kubernetes
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [envoy, envoy-ai-gateway, agent-router, aaif, mcp-gateway, ai-guardrails, oss-gateway, service-mesh, finos, aie-nyc-2026]
sources:
  - {claim: "Envoy AI Gateway becomes Agent Router and joins the Agentic AI Foundation; Apache-2.0; no migration needed", url: "https://tetrate.io/blog/agent-router-joins-aaif", date: 2026-09-10, confidence: high}
  - {claim: "AAIF: started by Bloomberg and Tetrate engineers; 9 maintainer seats across Bloomberg, Nutanix, AMD, Tetrate, Netflix; v1.0 June 2026, v1.1 Aug 2026", url: "https://aaif.io/blog/agent-router-joins-aaif", date: 2026-09-09, confidence: high}
  - {claim: "Envoy AI Gateway 1.0 released 2026-06-24 with stable v1 API, MCP routing/authz, token budgets, OTel tracing", url: "https://itbrief.news/story/tetrate-releases-envoy-ai-gateway-1-0-for-ai-traffic", date: 2026-06-24, confidence: medium}
  - {claim: "MCP support (MCPRoute, OAuth) added in v0.4.0, 2025-11-07", url: "https://aigateway.envoyproxy.io/release-notes/v0.4", date: 2025-11-07, confidence: high}
  - {claim: "Tetrate Agent Router Enterprise GA 2026-01-08: LLM gateway, MCP gateway, guardrails, agent certification", url: "https://itbrief.co.uk/story/tetrate-launches-tool-to-certify-enterprise-ai-agents", date: 2026-01-08, confidence: medium}
  - {claim: "Enterprise data planes in customer VPC/on-prem; Tetrate-run management plane not in data path, SOC 2 Type II audited; flat licence; comparison claims vs LiteLLM/Portkey/Kong", url: "https://tetrate.io/learn/ai/best-enterprise-ai-gateway", date: 2026-10-16, confidence: low}
  - {claim: "$40M Series B led by Sapphire Ventures", url: "https://www.venturecapitaljournal.com/tetrate-inks-40m-series-b/", date: 2021-03-10, confidence: high}
  - {claim: "Joined FINOS June 2025; mapping FINOS AI Governance Framework to EU AI Act, ISO 42001, FFIEC, NIST 800-53", url: "https://tetrate.io/press/tetrate-joins-finos-to-break-the-ai-governance-stalemate-for-highly-regulated-environments", date: 2026-10-16, confidence: medium}
  - {claim: "AIE NYC 2026 Silver sponsor", url: "https://www.ai.engineer/nyc", date: 2026-10-16, confidence: high}
---

# Tetrate

> Primary category: [ai-gateway](../categories/ai-gateway.md). Also listed in [mcp-gateway](../categories/mcp-gateway.md).

**One-liner** — The Envoy/Istio service-mesh company that co-created **Envoy AI Gateway**, an open-source LLM and MCP gateway now renamed **Agent Router** and governed by the Agentic AI Foundation. Tetrate sells a managed, enterprise-governed edition (**Agent Router Enterprise**) with data planes in your own VPC.

**What it does** — There are three layers, and it matters which one you buy:
1. **Agent Router (open source; Envoy AI Gateway until September 2026).** An AI gateway built on **Envoy Gateway**. It started as an Envoy sub-project, created by engineers at **Bloomberg** and Tetrate. Version **1.0** (2026-06-24) offers:
   - a stable v1 API;
   - one OpenAI-compatible interface over OpenAI, Anthropic, Gemini, Azure OpenAI, Bedrock, Groq, Mistral, Cohere and DeepSeek;
   - **token-aware rate limits, budgets and quotas** with per-token-type cost attribution;
   - centralised upstream credentials;
   - OpenInference and OpenTelemetry GenAI tracing;
   - **native MCP**: routing, multiplexing several MCP servers behind one endpoint, tool filtering, OAuth 2.0 with JWT claim forwarding and CEL-based authorization (MCP first shipped in v0.4.0, 2025-11-07).
   
   v1.1 followed in August 2026. On **2026-09-09/10** the project was renamed **Agent Router** and became a standalone project of the **Agentic AI Foundation (AAIF)**. Licence (Apache-2.0), code, CRDs and CLI are unchanged; existing deployments need no migration, and the 1.x compatibility commitment holds. The AAIF says the nine maintainer seats are spread across Bloomberg, Nutanix, AMD, Tetrate and Netflix, with no single company holding a majority. Public adopters include Bloomberg, Tencent Cloud, Nutanix and LY Corporation.
2. **Tetrate Agent Router Service.** A hosted, self-serve router at `router.tetrate.ai`, with a free signup credit and usage billed at model cost plus a routing fee (per a third-party directory).
3. **Tetrate Agent Router Enterprise** (GA announced 2026-01-08). Its components:
   - **LLM gateway**: approved model catalog, central keys, fallback, cost controls.
   - **MCP gateway**: shared tool catalog, authenticated access, tool filtering.
   - **AI guardrails**.
   - **Agent certification**: a formal "this agent is production-ready" workflow, with evaluation, reliability and impact dashboards.
   
   It is sold as a managed "dedicated instance". Data planes run in your AWS, Azure or GCP VPC or on-prem, managed from a Tetrate-run control plane that Tetrate says is out of the data path (vendor). The homepage also claims air-gapped deployment.

Tetrate's older business, **Tetrate Service Bridge** (an enterprise Istio/Envoy service mesh), no longer appears on its About page. Whether it is still sold was not confirmed.

**Naming / provenance** — Founded **2018** by contributors to Istio and Envoy. Current CEO is Jeyappragash JJ and co-founder/CTO is Varun Talwar. HQ is given as Milpitas, CA (CB Insights), "Silicon Valley" (company) or San Francisco (trade press). **Disambiguation:** "Agent Router" now means both the AAIF open-source project and Tetrate's commercial products (Agent Router Service and Agent Router Enterprise). Do not confuse it with [agentgateway](agentgateway.md), a separate agent/MCP gateway project created by Solo.io and also hosted under the AAIF.

**Ownership & viability** — `independent`, private. Its last disclosed round is a **$40M Series B led by Sapphire Ventures (2021-03-10)**, following a ~$12.4M Series A in 2019. No funding since 2021 was found, which is a long gap for a venture-backed company. A third-party estimate puts 2024 revenue at about $11M and headcount around 121, slightly down year on year; treat both as estimates. **Steward risk is lower than for most gateway vendors**: the OSS core is governed by a foundation with a multi-company maintainer group, and Bloomberg runs it in production, so the project would likely survive Tetrate. **Acquisition risk:** plausible buyers include API-management, networking or security platforms. If Tetrate were acquired, the commercial Enterprise control plane is the piece most at risk, while the OSS data plane would carry on.

**Positioning & differentiators** — `challenger` in ai-gateway. It has strong open-source credibility and a marquee FS production user (Bloomberg), but less commercial share or mindshare than [litellm](litellm.md), [portkey](portkey.md) or [kong](kong.md). It is also `challenger` in mcp-gateway, where MCP routing and authz are built into the same gateway rather than sold as a separate product.
- **Envoy-native vs Python proxy.** [litellm](litellm.md) is a Python proxy and [bifrost](bifrost.md) a Go proxy. Agent Router is an **Envoy data plane configured through Kubernetes Gateway API CRDs**. For a platform team already running Envoy or Istio, it slots into existing ingress, mTLS and observability. For everyone else, it is more infrastructure than a single `pip install`.
- **Foundation-governed OSS vs vendor-controlled OSS.** Against [bifrost](bifrost.md) (Maxim AI) or LiteLLM (BerriAI), the multi-company maintainer group is a genuine continuity advantage, and it is unusual in this category.
- **Kong comparison.** [kong](kong.md) is an API gateway with AI plugins and per-service pricing. Tetrate argues a purpose-built AI and MCP control plane is better, but that is Tetrate's marketing. Both are Envoy/NGINX-class infrastructure plays aimed at platform teams.
- **Agent "certification" workflow** in Enterprise goes beyond routing into agent lifecycle governance, which most gateways (for example [openrouter](openrouter.md) or [truefoundry](truefoundry.md)) do not attempt. It is unproven publicly.

Tetrate's own comparison page also criticises LiteLLM (single-Postgres multi-region design, 2026 security issues) and Portkey (now inside Palo Alto Networks' Prisma AIRS, so it questions neutrality). These are competitor claims and are not adopted here.

**Who should choose them / anti-fit** — Fits a **platform-engineering-heavy firm already on Envoy, Istio or Kubernetes Gateway API** that wants its LLM and MCP egress in the same data plane as the rest of its traffic, kept in its own VPC, with a foundation-governed open-source core. Bloomberg's production use is a relevant reference for an FS buyer. **Anti-fit:** a small fund without a Kubernetes platform team. [litellm](litellm.md), [portkey](portkey.md) or a SASE vendor's AI gateway will be faster to stand up. Also a poor fit if you want deep prompt-level DLP or injection detection; its guardrails are a component, not a dedicated [ai-runtime-security](../categories/ai-runtime-security.md) product.

**Known weaknesses / gotchas** —
- **Naming churn.** Envoy AI Gateway became Agent Router in 2026, and Tetrate uses "Agent Router" for both its hosted Service and its Enterprise product. Pin down exactly which you are evaluating.
- **Hosted Service means prompts transit Tetrate.** The self-serve Agent Router Service is a hosted router, so prompts and responses pass through Tetrate's infrastructure. That is not the same data posture as Enterprise or the OSS data plane.
- **Old funding and no named commercial customers.** No round since 2021 and no named commercial customers for the AI products. Ask for references.
- **Guardrail depth unknown.** What the Enterprise guardrails actually detect, and with which models, is not documented in sources found.

**Deployment & data handling** — It is an **inline proxy** on the model and tool call path, and how much latency that adds is not published. Data handling depends on which layer you use:
- **OSS Agent Router:** fully self-hosted (Kubernetes or the local `aigw` binary). No data goes to Tetrate.
- **Agent Router Enterprise:** data planes run in your VPC or on-prem. Tetrate says its management plane is **not in the data path**, that traffic continues if it is unreachable, and that you control what is sent to it (vendor).
- **Agent Router Service:** SaaS. Prompts transit Tetrate, and retention and training terms were not researched.

Overall `partial`.

**Integrations & partnerships** — Model providers: OpenAI, Anthropic, Gemini, Azure OpenAI, Bedrock and others via an OpenAI-compatible API. Observability: OpenTelemetry GenAI conventions and OpenInference (so traces land in [arize-phoenix](arize-phoenix.md), [langfuse](langfuse.md) or any OTel backend). MCP gateway is built in. Clouds and marketplaces: AWS, Azure, GCP and OpenShift. Public sector: Carahsoft. Standards: joined **FINOS** in June 2025 and is mapping the FINOS AI Governance Framework to the EU AI Act, ISO 42001, the FFIEC IT Handbook and NIST 800-53 (vendor), which is directly relevant to FS buyers. Nutanix is building the OSS project into Nutanix Agent Gateway and Enterprise AI. **AI Engineer New York 2026 (Oct 12–14):** listed as a **Silver sponsor**; no Tetrate talk appears on the published schedule.

**Compliance & FS traction** — Tetrate's comparison page states that its Enterprise management plane is **SOC 2 Type II** audited. That is vendor-stated only, with no trust-center report reviewed. FS evidence is `claimed`: the company says it works with "finance, government and global tech" organisations but names no commercial customers. The strongest FS signal is **Bloomberg**, which co-founded and runs the *open-source* project in production; that does not make Bloomberg a Tetrate customer. The FINOS work suggests a deliberate regulated-FS go-to-market.

**Commercial** — The OSS Agent Router is free (Apache-2.0). Agent Router Service is usage-based (model cost plus a routing fee; free signup credit). Agent Router Enterprise is a flat licence priced by capability and deployment footprint, quote-only. No price bands are public as of 2026-10-16.

## Open questions

- Any funding since the 2021 Series B, and current revenue and headcount (only third-party estimates found).
- Named commercial customers for Agent Router Enterprise, especially in FS.
- Whether Tetrate Service Bridge is still sold or supported.
- What the Enterprise "AI Guardrails" detect (PII, injection, toxicity), and whether they use in-house or third-party models.
- Data retention and training-use terms for the hosted Agent Router Service.
- Independent latency and throughput benchmarks against [litellm](litellm.md), [bifrost](bifrost.md) and [kong](kong.md).
- Whether the SOC 2 Type II claim covers the hosted Service or only the Enterprise management plane.

## Sources

- [Agent Router joins AAIF (Tetrate blog)](https://tetrate.io/blog/agent-router-joins-aaif) — fetched 2026-10-16 — supports: rename, licence, adopters, commercial product deployment; confidence: high
- [Agent Router joins AAIF (AAIF blog)](https://aaif.io/blog/agent-router-joins-aaif) — fetched 2026-10-16 — supports: maintainers, origins, release history; confidence: high
- [Tetrate releases Envoy AI Gateway 1.0 (IT Brief)](https://itbrief.news/story/tetrate-releases-envoy-ai-gateway-1-0-for-ai-traffic) — fetched 2026-10-16 — supports: 1.0 features and contributors; confidence: medium
- [Envoy AI Gateway v0.4 release notes](https://aigateway.envoyproxy.io/release-notes/v0.4) — fetched 2026-10-16 — supports: MCP support date; confidence: high
- [Tetrate launches tool to certify enterprise AI agents (IT Brief)](https://itbrief.co.uk/story/tetrate-launches-tool-to-certify-enterprise-ai-agents) — fetched 2026-10-16 — supports: Agent Router Enterprise GA and features; confidence: medium
- [Best Enterprise AI Gateway in 2026 (Tetrate)](https://tetrate.io/learn/ai/best-enterprise-ai-gateway) — fetched 2026-10-16 — supports: Enterprise deployment model, SOC 2 claim, pricing model, competitor claims; confidence: low (vendor marketing)
- [Tetrate homepage](https://tetrate.io/) and [About](https://tetrate.io/about) — fetched 2026-10-16 — supports: product line, leadership, deployment claims; confidence: medium
- [Tetrate inks $40M Series B (Venture Capital Journal)](https://www.venturecapitaljournal.com/tetrate-inks-40m-series-b/) — fetched 2026-10-16 — supports: Series B; confidence: high
- [Tetrate joins FINOS (press)](https://tetrate.io/press/tetrate-joins-finos-to-break-the-ai-governance-stalemate-for-highly-regulated-environments) — fetched 2026-10-16 — supports: FINOS membership and control mapping; confidence: medium
- [AI Engineer New York sponsors](https://www.ai.engineer/nyc) — fetched 2026-10-16 — supports: Silver sponsorship; confidence: high
- Cached: `raw/sources/2026-10-16--tetrate--agent-router-envoy-ai-gateway.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
