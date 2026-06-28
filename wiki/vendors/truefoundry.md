---
type: vendor
name: TrueFoundry
slug: truefoundry
categories: [ai-gateway, mcp-gateway]
layer: model-prompt
aliases: []
website: "https://www.truefoundry.com"
founded: 2021
hq: San Francisco, US + Bengaluru, India (dual HQ)
ownership: independent
ownership_detail: VC-backed; $19M Series A led by Intel Capital (Feb 2025). No M&A.
ownership_confidence: high
funding_total: $21.3M
last_funding: Series A, $19M, 2025-02 (lead Intel Capital)
deployment: [self-hosted, saas, api, on-prem]
target_customer: enterprise (regulated — banking, healthcare, insurance, government)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [ai-gateway, mcp-gateway, llmops, kubernetes]
---

# TrueFoundry

> Primary category: [ai-gateway](../categories/ai-gateway.md). Also: [mcp-gateway](../categories/mcp-gateway.md).

**One-liner** — A Kubernetes-native enterprise AI platform whose centerpiece is an
LLM/AI gateway (plus MCP gateway and model-deployment/LLMOps tooling) that gives a
company one governed control plane for all model and agent traffic.

## What it does

TrueFoundry started as an LLMOps / model-deployment platform — deploy and serve any
LLM, embedding, or custom model on your own Kubernetes (vLLM, TGI, Triton backends,
fractional-GPU support) — and has pushed its **AI Gateway** to the front of the
product. The gateway is a unified API in front of OpenAI, Anthropic, Gemini, Groq,
Mistral and (vendor claim) 250+ models, adding the things an enterprise needs before
it lets teams hit model APIs: centralized key management, latency-based routing and
automatic fallback, per-user/team/endpoint rate limits and token/cost budgets, RBAC,
SSO, immutable audit logging, and observability (token usage, latency, error rates,
full request/response logs). Input/output **guardrails** (PII filtering, toxicity,
prompt-injection checks, OpenAI Moderation and Bedrock Guardrails integration) are
built in. The newer **MCP Gateway** extends the same control plane to agent tool
calls — a central registry of approved MCP servers, OAuth/RBAC on every tool
invocation, credential brokering (one token auto-exchanged for per-server tokens),
and full tracing of agent→tool actions.

## Where it sits in the stack

Lives in the model/prompt layer as the [ai-gateway](../categories/ai-gateway.md) — the single exit door for
model traffic — and as an [mcp-gateway](../categories/mcp-gateway.md) for agent tool access. Its lethal-trifecta
role is primarily **egress**: it is the chokepoint where outbound model/tool calls
are routed, logged, budgeted and policy-checked, so it's the natural place to enforce
where data can and can't go. The built-in guardrails give it a secondary touch on the
untrusted-input and sensitive-data legs, but it is not a dedicated [ai-runtime-security](../categories/ai-runtime-security.md)
firewall. It sits between the apps/agents (yellow zone) and external model providers,
and is most valuable when self-hosted so traffic and logs stay inside the trust boundary.

## Deployment & architecture

API gateway, not an inline network proxy or browser agent. Distinctive trait among
gateways: it is **Kubernetes-native and designed to run inside your own
environment** — VPC, on-prem, air-gapped, hybrid/multi-cloud — with the vendor
stressing data sovereignty and no external egress of prompt/response data. Also
offered as SaaS. Performance claims (marketing): sub-3ms internal latency, 10B+
requests/month, ~30% cost optimization. Integrations: Kubernetes, Hugging Face,
MLflow, AWS/Azure/GCP; OpenTelemetry-based tracing exporting to Grafana, Datadog,
Prometheus; SSO via Okta/Azure AD; MCP servers (Slack, GitHub, internal tools).
Compliance posture: SOC 2, HIPAA, GDPR (vendor stated).

## Positioning & differentiators

TrueFoundry's pitch is "one control plane for models, gateway, and agents," with the
self-hosted, Kubernetes-native, full-LLMOps story as the differentiator. Versus
neighbors:

- **[portkey](portkey.md)** — closest analog (gateway + guardrails + observability); Portkey is
  more gateway-focused, TrueFoundry bundles the gateway into a broader deploy/serve
  platform.
- **[litellm](litellm.md)** — open-source/library and lightweight proxy; TrueFoundry is a
  heavier, commercial, enterprise-governed platform with UI, RBAC, deployment.
- **[kong](kong.md)** — API-gateway incumbent extending into AI/MCP gateways; Kong leads with
  general API-management heritage, TrueFoundry is AI/ML-native and ships model serving.
- **[cloudflare](cloudflare.md)** — edge/SaaS AI Gateway tied to Cloudflare's network; TrueFoundry
  is run-it-yourself inside your K8s rather than at a third party's edge.
- **[openrouter](openrouter.md)** — a hosted multi-model marketplace/router (buy access to models);
  TrueFoundry is governance/infrastructure you run, not a model reseller.

## Ownership, funding & M&A

Independent and VC-backed. Founded June 2021 by Nikunj Bajaj (CEO), Abhishek
Choudhary and Anuraag Gutgutia. Dual HQ: San Francisco and Bengaluru. Raised a $2.3M
seed (Sep 2022, Peak XV's Surge) and a **$19M Series A in Feb 2025 led by Intel
Capital** (Eniac Ventures, Peak XV's Surge, new investor Jump Capital, plus angels),
for ~$21.3M total. No acquisition — no seed M&A flag, and none found. Ownership
confidence: high.

## CTO / hedge-fund lens

An AI gateway is a **Day-1** control: before you let desks and agents call models,
you want one governed exit door for keys, budgets, rate limits, audit logs and a kill
switch. TrueFoundry's self-hosted/air-gapped, Kubernetes-native posture is attractive
to a fund that wants prompts and outputs to never leave its own infrastructure (MNPI,
data-residency concerns). The catch: it is a **heavier, infra-centric platform** that
assumes you run Kubernetes and want model serving/LLMOps too. A 50-person fund that
just wants a managed exit door may find [portkey](portkey.md) (or a thin [litellm](litellm.md) proxy)
lighter; TrueFoundry fits a shop that already operates its own ML/K8s infra and wants
gateway + serving + agent governance from one vendor. Not itself a model-risk/SR 11-7
governance tool, but its audit logs and policy enforcement feed that process. Note its
smaller scale (single Series A, India+US startup) when weighing vendor risk.

## Competitors / alternatives

[portkey](portkey.md), [litellm](litellm.md), [kong](kong.md), [cloudflare](cloudflare.md), [openrouter](openrouter.md). Adjacent:
[ai-runtime-security](../categories/ai-runtime-security.md) (dedicated AI firewalls), [llm-observability](../categories/llm-observability.md),
[authorization-engine](../categories/authorization-engine.md) (fine-grained agent/tool authz).

## Open questions / to verify

- Independent benchmark of the sub-3ms latency / 10B-requests claims (vendor-stated).
- Maturity and standalone adoption of the MCP Gateway vs the core AI Gateway.
- SaaS vs self-hosted split among customers; pricing model.
- Whether any Series B or follow-on funding has closed since Feb 2025.

## Sources

- [TrueFoundry Secures $19M Series A (Intel Capital)](https://www.intelcapital.com/truefoundry-secures-19-million-series-a-funding-to-transform-ai-deployment-at-scale-powered-by-their-agent-on-autopilot/) — fetched 2026-06-28 — supports: Series A $19M Feb 2025, lead Intel Capital, founders, independent; confidence: high
- [Peak XV-backed TrueFoundry secures $19M Series A (Entrackr)](https://entrackr.com/news/peak-xv-backed-truefoundry-secures-19-mn-in-series-a-funding-8697254) — fetched 2026-06-28 — supports: founded 2021, dual HQ Bengaluru+SF, $21.3M total, $2.3M seed Sep 2022, customers; confidence: med
- [TrueFoundry AI Gateway product page](https://www.truefoundry.com/ai-gateway) — fetched 2026-06-28 — supports: gateway features, deployment, guardrails, performance claims (marketing); confidence: med
- [TrueFoundry MCP Gateway product/docs](https://www.truefoundry.com/mcp-gateway) — fetched 2026-06-28 — supports: MCP registry, tool RBAC/OAuth, credential brokering (marketing); confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2021, dual HQ (SF + Bengaluru), founders, $21.3M total funding ($19M Series A led by Intel Capital Feb 2025), independent VC-backed (no M&A, confidence high). Documented AI Gateway + MCP Gateway, Kubernetes-native self-hosted deployment, egress trifecta role, medium hedge-fund fit; compared to portkey/litellm/kong/cloudflare/openrouter. Cached 3 sources.
