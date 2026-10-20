---
title: TrueFoundry
type: vendor
name: TrueFoundry
slug: truefoundry
aka: [TrueFoundry AI Gateway, TrueFoundry MCP Gateway, TrueFoundry Agent Gateway, TrueFoundry Agent Harness, TrueForge]
primary_category: ai-gateway
also_listed_in: [mcp-gateway]
website: https://www.truefoundry.com
founded: 2021
hq: San Francisco, US + Bengaluru, India (dual HQ)
ownership_state: independent
owner: null
ownership_note: VC-backed; $19M Series A led by Intel Capital (Feb 2025); no newer round found as of 2026-10-20. Not acquired. TrueFoundry is itself an acquirer, buying Seldon AI's business and customers (announced 2026-06-24, price undisclosed).
acquisition: {announced: null, closed: null, price: null}
funding_total: $21.3M
last_funding: Series A, $19M, 2025-02 (lead Intel Capital)
market_position: {ai-gateway: challenger, mcp-gateway: platform-module}
deployment_model: [saas, self-hosted, on-prem]
form_factor: [inline-proxy, api, sdk, platform]
data_leaves_tenancy: partial
integrations: [openai, anthropic, aws-bedrock, gemini, okta, azure-ad, opentelemetry, datadog, grafana, prometheus, langchain, crewai, daytona, kubernetes, mlflow, hugging-face]
mcp_support: gateway
certifications: []
pricing_model: "Platform / gateway: quote-based, no public list. Hosted TrueForge: self-serve, usage-based (rates not published). TrueForge OSS: free (MIT)."
fs_traction: unverified
target_customer: enterprise (regulated — banking, healthcare, insurance, government); Kubernetes-operating platform/ML teams
last_verified: 2026-10-20
verify_after: 2027-04-20
tags: [ai-gateway, mcp-gateway, agent-gateway, agent-harness, llmops, kubernetes, open-source, acquirer]
sources:
  - {claim: "Agent Gateway launched 2026-06-02 as part of AI Gateway platform alongside LLM Gateway and MCP Gateway; agent registry, RBAC, policies, governed MCP tool access; named customers NVIDIA, Innovaccer, Siemens Healthineers", url: "https://www.01net.it/truefoundry-launches-agent-gateway-to-close-the-enterprise-ai-governance-gap/", date: 2026-06-02, confidence: medium}
  - {claim: "Agent Gateway features: per-agent quotas/budgets, agent identity/service accounts at gateway, tool allowlists, PII filtering, VPC/on-prem/air-gapped; SOC 2/HIPAA/GDPR badges", url: "https://www.truefoundry.com/agent-gateway", date: 2026-10-20, confidence: medium}
  - {claim: "Agent Harness: managed harness built on AI Gateway + MCP Gateway; HITL approvals, sandbox, credentials held by gateway; SaaS/self-hosted/on-prem; launch blog 2026-06-09", url: "https://www.truefoundry.com/blog/agent-harness-managed-ai-agents", date: 2026-06-09, confidence: medium}
  - {claim: "Agent Harness is TrueForge embedded as-is, hosted multi-user sharing platform auth/RBAC/control plane; old agent APIs sunset 2026-10-15", url: "https://www.truefoundry.com/docs/agent-platform/agent-harness/overview", date: 2026-10-20, confidence: high}
  - {claim: "TrueForge open-sourced: MIT, repo created 2026-07-23, 6,313 stars at 2026-10-20, sandbox via Daytona", url: "https://github.com/truefoundry/trueforge", date: 2026-10-20, confidence: high}
  - {claim: "TrueForge launch 2026-08-19 as alternative to Claude Managed Agents; hosted usage-based version; 50% cost claim; customers Automatiq, NetApp", url: "https://www.01net.it/truefoundry-launches-trueforge-an-open-source-vendor-neutral-alternative-to-claude-managed-agents-at-50-lower-cost/", date: 2026-08-19, confidence: medium}
  - {claim: "Cost benchmark is TrueFoundry's own (14 DevRev Enterprise-Bench tasks); ~30% cheaper on Opus 4.8, ~75% on GLM-5.2; not independently validated", url: "https://www.infoworld.com/article/4211969/truefoundry-debuts-open-source-ai-agent-harness-claiming-up-to-75-lower-costs.html", date: 2026-08-20, confidence: high}
  - {claim: "TrueFoundry acquired Seldon AI (UK, founded 2014, Seldon Core); announced 2026-06-24; price undisclosed", url: "https://www.sdxcentral.com/news/truefoundry-snaps-up-seldon-ai/", date: 2026-06-24, confidence: high}
  - {claim: "'TrueFoundry has acquired Seldon's business and customers'; Seldon ML continues on AI Deploy; nothing changes for existing TrueFoundry customers", url: "https://www.truefoundry.com/blog/truefoundry-seldon-unified-control-plane-for-enterprise-ai", date: 2026-07-23, confidence: high}
  - {claim: "$19M Series A Feb 2025 led by Intel Capital; no newer round found in 2026-10-20 searches", url: "https://www.intelcapital.com/truefoundry-secures-19-million-series-a-funding-to-transform-ai-deployment-at-scale-powered-by-their-agent-on-autopilot/", date: 2025-02-06, confidence: high}
---

# TrueFoundry

> Researched 2026-06-28; refreshed 2026-10-20. Primary category: [ai-gateway](../categories/ai-gateway.md). Also: [mcp-gateway](../categories/mcp-gateway.md).

**One-liner**: A Kubernetes-native enterprise AI platform built around an AI gateway. The gateway family covers LLM, MCP and agent traffic, and TrueFoundry adds a managed agent runtime (the "Agent Harness", built on its open-source TrueForge) and model deployment/LLMOps. The pitch is one governed control plane for models, tools and agents.

## What it does

TrueFoundry started as an LLMOps / model-deployment platform: deploy and serve any LLM, embedding or custom model on your own Kubernetes (vLLM, TGI and Triton backends, fractional GPUs). It has since put its **AI Gateway** at the front of the product. As of 2026-10-20 the gateway is marketed as a family of three:

- **LLM Gateway**: a unified API in front of OpenAI, Anthropic, Gemini, Groq, Mistral and (vendor claim) 250+ models. It adds centralized key management, latency-based routing and fallback, per-user/team/endpoint rate limits and token or cost budgets, RBAC, SSO, immutable audit logging and observability. Input/output **guardrails** are built in: PII filtering, toxicity, prompt-injection checks, and OpenAI Moderation and Bedrock Guardrails integration.
- **MCP Gateway**: a central registry of approved MCP servers, OAuth/RBAC on every tool call, credential brokering (one token exchanged for per-server tokens) and tracing of agent→tool actions. Tools can be flagged "destructive" once at the gateway, and every agent that uses them then needs human approval (per the 2026-06-09 blog).
- **Agent Gateway** (launched **2026-06-02**): an agent registry plus a control layer for agents built in any framework (LangChain, CrewAI, custom). It provides step-level traces, token/cost quotas per agent, workflow or environment, RBAC over who can deploy, run or change an agent, dev/staging/prod separation, per-agent tool allowlists, PII filtering, and agent identity and service-account management at the gateway. These features come from the vendor's product page and are not independently tested.

**Agent Harness / TrueForge** (the item flagged for this refresh):

- **What it is.** TrueFoundry defines an agent harness as "the runtime layer around an LLM that turns it into a reliable, long-running agent". The harness runs the plan-act-observe loop, tool routing, context management, sandboxing, approvals, session state and tracing. Agents are defined declaratively (model + MCP servers + skills + instructions) in a no-code builder, or in code through an experimental SDK.
- **Timeline.** The managed **Agent Harness** was introduced in a vendor blog on **2026-06-09** as "a managed harness built on top of the AI Gateway and MCP Gateway". TrueFoundry then released the harness itself as **TrueForge**, an MIT-licensed open-source project. The GitHub repo was created 2026-07-23, the public launch was **2026-08-19**, and the repo had 6.3k stars by 2026-10-20. Current docs say the platform's Agent Harness *is* TrueForge, "embedded in the platform as-is, not forked or re-implemented". The older TrueFoundry agent APIs were scheduled to stop working on **2026-10-15**, and existing agents were migrated automatically.
- **How it relates to the gateways.** The harness does not have its own credential or tool configuration. Models, MCP servers and skills registered in the AI Gateway appear in the agent builder, and all agent model and tool traffic goes through the gateways. Budgets, rate limits, guardrails, RBAC and logging therefore apply to agent runs with no extra instrumentation, and "no API keys or credentials are ever pasted into agent definitions". The harness is the runtime, and the gateways are where policy is enforced.
- **Governance features.** Human-approval checkpoints on tool calls, a sandbox for code, file and shell execution (on by default; the OSS README says it uses [daytona](daytona.md) "today", with more providers planned), centralized secrets, per-run traces with cost and tokens per step, and OpenTelemetry export. Guardrail configuration specific to the harness is not documented on the harness pages; it is inherited from the gateway.
- **Positioning.** Marketed as an open, model-neutral alternative to Anthropic's Claude Managed Agents and LangChain's LangSmith managed agents. The headline claim is 50% lower cost (later "up to 75%"). That benchmark is TrueFoundry's own: 14 tasks from DevRev Enterprise-Bench, about 30% cheaper on the same frontier model and about 75% only when swapping to a cheaper open model. InfoWorld notes it has not been independently validated.

## Where it sits in the stack

Primarily the [ai-gateway](../categories/ai-gateway.md): the single exit door for model traffic. It is also an [mcp-gateway](../categories/mcp-gateway.md) for agent tool access. Its main security role is controlling outbound traffic: the gateway is where model, tool and now agent calls are routed, logged, budgeted and checked against policy, so it is the natural place to enforce where data can and cannot go. The built-in guardrails add some screening of prompts, responses and tool calls, but it is not a dedicated [ai-runtime-security](../categories/ai-runtime-security.md) firewall. With the Agent Harness, TrueFoundry also *runs* agents, not just governs their traffic. That makes it an agent platform as well as a gateway, which is worth noting when deciding who owns it internally (platform/ML team vs security).

**Cross-listing decision (2026-10-20): `also_listed_in` unchanged at `[mcp-gateway]`.** [agent-runtime-security](../categories/agent-runtime-security.md) was considered and rejected. That category is about *protecting* running agents (detecting hijacked behavior, runtime threat detection and response; Zenity, Lasso, Operant). TrueFoundry provides the runtime plus preventive controls (approvals, sandbox, tool allowlists, budgets, agent identity), but no evidence was found of behavioral detection or of security-team-oriented response features. Its Agent Gateway competes more with agent platforms and gateways than with agent-security tools. Cross-listing it there would also need a new survey-v2.csv row. The taxonomy has no "agent platform / harness" category; that is noted under Open questions as a possible taxonomy gap.

## Deployment & architecture

An API gateway (inline proxy for model, tool and agent calls), not a network appliance or browser agent. Unusually among gateways, it is **Kubernetes-native and designed to run inside your own environment**: VPC, on-prem, air-gapped, hybrid or multi-cloud. The vendor stresses data sovereignty and says the agent page means "No data leaves your domain". It is also offered as SaaS. The Agent Harness docs and blog list SaaS, self-hosted and on-prem. A 2026-10-20 search snippet described the harness as "SaaS only", but the live docs fetched the same day do not say that; the docs are adopted.

**Data handling (`data_leaves_tenancy: partial`)**: self-hosted or on-prem deployments keep prompts, responses and logs in your environment (vendor claim). SaaS and hosted TrueForge send them to TrueFoundry. Whether a self-hosted deployment still depends on a TrueFoundry-hosted control plane was not verified (see Open questions). The OSS TrueForge "local mode" has no login and is for localhost only. Production use needs hosted mode with Postgres and Redis.

Performance claims (marketing): sub-3ms internal latency, more than 1 trillion tokens per day through the gateway (2026 claim; it was "10B+ requests/month" in earlier marketing), more than 1,000 clusters managed. Integrations: Kubernetes, Hugging Face, MLflow, AWS/Azure/GCP; OpenTelemetry tracing to Grafana, Datadog and Prometheus; SSO via Okta/Azure AD; MCP servers (Slack, GitHub, internal tools); LangChain and CrewAI agents; Daytona sandboxes (TrueForge). Compliance: SOC 2, HIPAA and GDPR badges on the vendor site. The SOC 2 report type and auditor were not verified.

## Positioning & differentiators

**Market position**: **challenger** in [ai-gateway](../categories/ai-gateway.md). It was named in the 2025 Gartner Market Guide for AI Gateways (vendor-reported), and it claims large-enterprise customers (NVIDIA, Siemens Healthineers, NetApp) and very high volume. Category incumbents with larger distribution are Kong, Cloudflare and Palo Alto via Portkey. In [mcp-gateway](../categories/mcp-gateway.md) it is a **platform-module**: the MCP Gateway is bought as part of the AI Gateway platform, not on its own.

Differentiators vs named peers:

- **[portkey](portkey.md)**: the closest gateway analog. Portkey (now part of Palo Alto Networks) is gateway-focused. TrueFoundry bundles the gateway with model serving, an agent runtime (TrueForge) and, since the Seldon deal, classic ML serving customers.
- **[litellm](litellm.md)**: an open-source library and lightweight proxy. TrueFoundry is a heavier commercial platform with UI, RBAC, deployment and agent hosting.
- **[kong](kong.md)**: an API-gateway incumbent extending into AI and MCP. TrueFoundry is AI/ML-native and ships model serving and an agent harness.
- **[cloudflare](cloudflare.md)**: an edge/SaaS AI Gateway. TrueFoundry runs inside your own Kubernetes.
- **[openrouter](openrouter.md)**: a hosted model marketplace. TrueFoundry is infrastructure you run, not a model reseller.
- **[obot](obot.md)**: an open-source MCP and LLM gateway focused on governing employee AI clients. TrueFoundry is focused on platform teams building and running production agents.

**Who should choose it**: a fund that already runs Kubernetes and ML infrastructure and wants gateway, model serving and agent runtime governed from one vendor, with everything self-hosted.

**Who should not**: a small fund that just wants a managed exit door for model traffic ([portkey](portkey.md) or a thin [litellm](litellm.md) proxy is lighter), or a shop wary of putting its agent runtime, gateway and model serving on one Series-A vendor.

**Gotchas**: TrueForge moves very fast (npm package at v0.179 within about three months of the repo being created). The harness SDK is experimental. Retiring the old agent APIs on 2026-10-15 shows the agent surface is still unstable. The cost-saving claims come from the vendor's own benchmark.

## Ownership, funding & M&A

Independent and VC-backed. Founded June 2021 by Nikunj Bajaj (CEO), Abhishek Choudhary and Anuraag Gutgutia. Dual HQ in San Francisco and Bengaluru. (2026 press releases say "headquartered in San Francisco" and operating across North America, Europe and APAC. That is a soft difference in description, not a factual conflict, so the dual-HQ line is kept.) Raised a $2.3M seed (Sep 2022, Peak XV's Surge) and a **$19M Series A in Feb 2025 led by Intel Capital** (Eniac Ventures, Peak XV's Surge, new investor Jump Capital, plus angels), for about $21.3M in total. **No newer round found** in searches on 2026-10-20. TrueFoundry has not been acquired. Ownership confidence: high.

**TrueFoundry as acquirer: Seldon AI.** Announced **2026-06-24** (Business Wire; SDxCentral exclusive the same day) and reported as completed ("has acquired"). No separate closing date and no price were disclosed. Seldon is a UK company founded in 2014 (backers AlbionVC, Bright Pixel, Cambridge Innovation Capital) known for **Seldon Core**, open-source Kubernetes model serving. TrueFoundry describes the deal as acquiring "Seldon's business and customers". Seldon customers' ML workloads move to TrueFoundry's AI Deploy platform, with the AI Gateway offered as their route into agentic AI. Existing TrueFoundry customers are told "nothing changes". Neither source addresses what happens to the Seldon Core licence or roadmap. For a fund that runs Seldon Core, that is the open question.

**Viability / acquisition risk**: making an acquisition on about $21M of disclosed funding implies either a small, distressed-asset price or undisclosed capital. Neither was confirmed. TrueFoundry's scope keeps widening (gateway family, agent harness, ML serving, Seldon migration), so execution risk is real for a Series-A company. Plausible acquirers include API-gateway, observability or cloud vendors. Exit would be partly cushioned for customers by the self-hosted deployment and the MIT-licensed TrueForge, but not for the commercial gateway.

## CTO / hedge-fund lens

An AI gateway is a **Day-1** control: before desks and agents call models, you want one governed exit door for keys, budgets, rate limits, audit logs and a kill switch. TrueFoundry's self-hosted, air-gapped, Kubernetes-native design suits a fund that wants prompts and outputs never to leave its own infrastructure (MNPI and data-residency concerns).

What changed in 2026: TrueFoundry now also offers a **governed place to run agents**. For a fund building internal research or ops agents, the Agent Harness gives approvals, sandboxing, central secrets and per-run cost tracing for free once the gateway is in place. TrueForge being MIT-licensed reduces lock-in. That bundling is the appeal and the risk: gateway, MCP governance, agent runtime and model serving from one Series-A vendor concentrates dependency. A fund already standardizing on Claude Managed Agents or a hyperscaler agent service gets little from the harness, and the gateway remains the reason to buy. Not a model-risk/SR 11-7 governance tool in itself, though its audit logs and policy enforcement feed that process. **Fit: medium**, higher for Kubernetes-operating shops building their own agents.

## Competitors / alternatives

[portkey](portkey.md), [litellm](litellm.md), [kong](kong.md), [cloudflare](cloudflare.md), [openrouter](openrouter.md); MCP-gateway peers [obot](obot.md), [agentgateway](agentgateway.md). Adjacent: [ai-runtime-security](../categories/ai-runtime-security.md) (dedicated AI firewalls), [agent-runtime-security](../categories/agent-runtime-security.md) (agent threat detection, which TrueFoundry does not do), [llm-observability](../categories/llm-observability.md), [authorization-engine](../categories/authorization-engine.md) (fine-grained agent/tool authorization).

## Open questions / to verify

- Independent benchmarks of the sub-3ms latency, 1T-tokens/day and TrueForge cost claims (all vendor-stated).
- Maturity and standalone adoption of the MCP and Agent Gateways vs the core LLM gateway.
- Whether self-hosted deployments depend on a TrueFoundry-hosted control plane (affects `data_leaves_tenancy`).
- SOC 2 report type and auditor; ISO 27001/42001 status.
- Platform pricing bands; hosted TrueForge usage rates.
- Seldon deal: price, formal close date, Seldon Core licence and roadmap after the acquisition.
- Whether a Series B or other capital has been raised since Feb 2025 (none found as of 2026-10-20).
- Whether A2A protocol support is shipped in the Agent Gateway (mentioned in a TF blog per search summary, not on the product page).
- Taxonomy gap (for the human): no category for agent platforms/harnesses (TrueForge, Claude Managed Agents, LangSmith), which neither [agent-runtime-security](../categories/agent-runtime-security.md) nor [ai-gateway](../categories/ai-gateway.md) covers cleanly.

## Sources

- [TrueFoundry Secures $19M Series A (Intel Capital)](https://www.intelcapital.com/truefoundry-secures-19-million-series-a-funding-to-transform-ai-deployment-at-scale-powered-by-their-agent-on-autopilot/): fetched 2026-06-28. Supports Series A $19M Feb 2025, lead Intel Capital, founders. Confidence: high.
- [Peak XV-backed TrueFoundry secures $19M Series A (Entrackr)](https://entrackr.com/news/peak-xv-backed-truefoundry-secures-19-mn-in-series-a-funding-8697254): fetched 2026-06-28. Supports founded 2021, dual HQ, $21.3M total, $2.3M seed Sep 2022. Confidence: medium.
- [TrueFoundry AI Gateway product page](https://www.truefoundry.com/ai-gateway): fetched 2026-06-28. Supports gateway features, deployment, guardrails, performance claims. Confidence: medium (marketing).
- [TrueFoundry MCP Gateway product/docs](https://www.truefoundry.com/mcp-gateway): fetched 2026-06-28. Supports MCP registry, tool RBAC/OAuth, credential brokering. Confidence: medium (marketing).
- [Agent Harness docs](https://www.truefoundry.com/docs/agent-platform/agent-harness/overview) and [launch blog](https://www.truefoundry.com/blog/agent-harness-managed-ai-agents) (2026-06-09): fetched 2026-10-20. Support harness = TrueForge, gateway integration, governance features, deployment options, API sunset. Confidence: high (docs) / medium (blog). Cached: `raw/sources/2026-10-20--truefoundry--agent-harness-docs-blog.md`.
- [GitHub: truefoundry/trueforge](https://github.com/truefoundry/trueforge), [TrueForge launch release](https://www.01net.it/truefoundry-launches-trueforge-an-open-source-vendor-neutral-alternative-to-claude-managed-agents-at-50-lower-cost/) (2026-08-19), [InfoWorld](https://www.infoworld.com/article/4211969/truefoundry-debuts-open-source-ai-agent-harness-claiming-up-to-75-lower-costs.html) (2026-08-20): fetched 2026-10-20. Support MIT licence, dates, traction, cost-claim caveats. Confidence: high (GitHub, InfoWorld) / medium (PR). Cached: `raw/sources/2026-10-20--truefoundry--trueforge-oss-launch.md`.
- [Agent Gateway launch release](https://www.01net.it/truefoundry-launches-agent-gateway-to-close-the-enterprise-ai-governance-gap/) (2026-06-02) and [product page](https://www.truefoundry.com/agent-gateway): fetched 2026-10-20. Support Agent Gateway features, named customers, certification badges. Confidence: medium (marketing). Cached: `raw/sources/2026-10-20--truefoundry--agent-gateway-launch.md`.
- [SDxCentral: TrueFoundry snaps up Seldon AI](https://www.sdxcentral.com/news/truefoundry-snaps-up-seldon-ai/) (2026-06-24), [Open Source For You](https://www.opensourceforu.com/2026/06/truefoundry-acquires-open-source-ai-pioneer-seldon/) (2026-06-25), [Pulse 2.0](https://pulse2.com/why-truefoundry-acquired-seldon-ai/) (2026-06-27), [TrueFoundry blog](https://www.truefoundry.com/blog/truefoundry-seldon-unified-control-plane-for-enterprise-ai): fetched 2026-10-20. Support Seldon acquisition, date, terms, customer commitments. Confidence: high. Cached: `raw/sources/2026-10-20--truefoundry--seldon-acquisition.md`.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2021, dual HQ (SF + Bengaluru), founders, $21.3M total funding ($19M Series A led by Intel Capital Feb 2025), independent VC-backed (no M&A, confidence high). Documented AI Gateway + MCP Gateway, Kubernetes-native self-hosted deployment, egress-control role, medium hedge-fund fit; compared to portkey/litellm/kong/cloudflare/openrouter. Cached 3 sources.
- [2026-10-20] Refreshed. Added Agent Gateway (launched 2026-06-02), the managed Agent Harness (blog 2026-06-09) and its open-source core TrueForge (MIT, repo 2026-07-23, launched 2026-08-19, 6.3k stars; old agent APIs sunset 2026-10-15), and the Seldon AI acquisition (TrueFoundry as acquirer, announced 2026-06-24, price undisclosed). These all predate or follow the 2026-06-28 pass, which missed the June items; no prior claim conflicts. Ownership unchanged (independent; no new round found). Soft note: 2026 press says "headquartered in San Francisco" vs page's dual HQ, kept both. Set market_position (ai-gateway challenger, mcp-gateway platform-module), mcp_support gateway, form_factor, data_leaves_tenancy partial, integrations, pricing_model, sources. Considered and rejected adding agent-runtime-security to also_listed_in (runtime + preventive controls, not agent threat detection; would need a CSV row). Flagged a possible taxonomy gap for agent platforms/harnesses. 4 sources cached.
