---
type: vendor
name: agentgateway (Solo.io / AAIF)
slug: agentgateway
categories: [mcp-gateway]
layer: model-prompt
aliases: [agent gateway]
website: https://agentgateway.dev
founded: 2025
hq: # n/a — OSS project; sponsor Solo.io is HQ'd in Cambridge, MA
ownership: independent
ownership_detail: "Open-source project created by Solo.io; donated to the Linux Foundation 2025-08-25, now hosted under the Agentic AI Foundation (AAIF). Apache 2.0."
ownership_confidence: high
funding_total: # n/a — OSS project, no funding round
last_funding: # n/a
deployment: [self-hosted, inline-proxy, on-prem]
target_customer: enterprise / platform & cloud-native teams
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [egress, untrusted-input]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [open-source, mcp, a2a, llm-gateway, rust, linux-foundation, aaif]
---

# agentgateway (Solo.io / AAIF)

**One-liner** — An open-source, Rust-built proxy ("data plane") that sits in front of LLMs, MCP tool servers, and agent-to-agent (A2A) traffic, adding auth, RBAC, rate limiting, and observability in one binary.

## What it does

agentgateway is a single proxy that mediates three kinds of AI traffic that a normal API gateway was never designed for:

- **MCP gateway** — fronts Model Context Protocol tool servers: tool discovery/federation (aggregate many MCP servers behind one endpoint), RBAC over which tools/clients can do what, support for stdio/HTTP/SSE/Streamable-HTTP transports, OpenAPI-to-MCP conversion, OAuth, versioning, and audit trails.
- **LLM gateway** — a unified OpenAI-compatible endpoint to route to OpenAI, Anthropic/Claude, Gemini, Bedrock, and self-hosted models, with per-team token budgets/spend controls, failover, and load balancing.
- **A2A gateway** — brokers agent-to-agent calls with identity, capability discovery, tracing, and replay across frameworks (LangChain, CrewAI, ADK).

The pitch is to give platform teams one consistent control point — auth, policy, rate limits, audit, telemetry — across all agentic traffic instead of stitching together separate proxies. It is infrastructure software, not a managed product.

## Where it sits in the stack

Primary category: [[mcp-gateway]] (model/prompt layer). It also overlaps the [[authorization-engine]] register because it enforces fine-grained RBAC via a policy engine (CEL policies on the homepage feature list; OPA-evaluated policies also referenced) over tool/agent calls.

**Lethal-trifecta role.** As a tool-call broker it primarily controls the **egress** leg (what tools/data an agent is allowed to reach, with rate limits and audit) and touches the **untrusted-input** leg by sitting between the model and external MCP tool servers. It does not, on its own, do content inspection / prompt-injection scanning the way a dedicated runtime firewall ([[prisma-airs]]) does — it is connectivity + access control, not a semantic firewall.

**Trust zones.** Designed to sit at the boundary between an agent/LLM (untrusted-ish) and the tools, data sources, and other agents it wants to reach — i.e. a chokepoint between trust zones.

## Deployment & architecture

- **Form factor:** standalone single binary, Docker container, or Kubernetes (Helm charts). It is an inline **data plane** proxy; you self-host it. No SaaS offering from the project itself.
- **Built in Rust** (with Go and TypeScript components), derived from lessons building Istio's ztunnel zero-trust tunnel.
- **Control plane / k8s:** agentgateway is positioned as the AI-native data plane; Solo.io's kgateway-style Kubernetes Gateway-API control plane can manage it (and Solo.io ships a commercial "Solo Enterprise for agentgateway" with its own docs/versioning).
- **Integrations:** MCP, A2A, OpenAI-compatible LLM APIs, OpenAPI, OIDC/JWT/API-keys/OAuth for auth, mTLS/TLS, OpenTelemetry for metrics/logs/tracing (so it can feed a SIEM/observability stack).

## Positioning & differentiators

- **Open-source + neutral governance.** Unlike most MCP-gateway entrants, agentgateway is Apache-2.0 and lives under the Linux Foundation's Agentic AI Foundation (AAIF), with contributors from AWS, Microsoft, Red Hat, IBM, Cisco, Huawei, Shell, and Zayo. That neutrality is its main differentiator versus single-vendor tools.
- **Three-in-one data plane (LLM + MCP + A2A)** in one Rust binary, rather than just an MCP proxy.
- **Versus single-vendor / product gateways:** [[kong]] and [[truefoundry]] approach AI/MCP gateways from existing API-gateway products; [[docker-mcp-gateway]] focuses on running MCP servers in containers locally; [[ibm-contextforge]] (MCP Context Forge) is another OSS MCP gateway/registry; [[obot]], [[mintmcp]], [[arcade]], and [[natoma]] are more managed/SaaS MCP-access plays; [[pomerium]] comes from identity-aware access proxying. agentgateway's claim to fame is being the broad, foundation-governed, performance-focused OSS data plane.
- Note Solo.io ships sibling OSS projects (kagent, agentregistry, agentevals) around it.

> Marketing claims (flagged): "first complete connectivity solution for Agentic AI," "zero-config TLS." Treat as vendor framing.

## Ownership, funding & M&A

- **Created by Solo.io** (private company; vendor behind Gloo/Istio Ambient/kgateway; CEO Idit Levine). Project created ~2025 (community meetings began July 2025).
- **Donated to the Linux Foundation on 2025-08-25**, then hosted under the **Agentic AI Foundation (AAIF)**, a Linux Foundation project, for vendor-neutral governance. Apache 2.0. (confidence: high — primary Solo.io blog + AAIF project page, dated.)
- **No funding/valuation** applies — it is an OSS project, not a company. Solo.io monetizes via a commercial "Solo Enterprise for agentgateway" distribution.
- No acquisition. The seed's "kgateway OSS" flag is a category/lineage hint, not an M&A event: kgateway is a separate CNCF Envoy-based project; agentgateway is a distinct Rust project from the same vendor.

## CTO / hedge-fund lens

**Day-2, and only if you're building.** This is platform infrastructure for teams that are self-hosting agents and MCP tool servers at some scale and want one governed chokepoint. For a typical 50-person hedge fund that mostly *consumes* SaaS AI tools, standing up and operating a Rust proxy + Kubernetes control plane is overkill — you'd get more governance value from a managed MCP-access product or your existing IdP/gateway. Relevant if you have a real platform-engineering team, run agents in your own environment, and value open-source + no vendor lock-in. Useful as an architecture reference even if you don't deploy it. SR 11-7 / model-risk: not a model-risk tool; its audit logs and access controls could feed an evidence trail but it isn't a governance product.

## Competitors / alternatives

[[docker-mcp-gateway]], [[ibm-contextforge]], [[mintmcp]], [[obot]], [[arcade]], [[pomerium]], [[kong]], [[truefoundry]], [[natoma]], [[prisma-airs]]

## Open questions / to verify

- Exact project creation date (March 2025 cited by some secondary sources vs. July 2025 first community meetings).
- Real-world maturity/production adoption beyond GitHub metrics (~3.6k stars, v1.x at time of fetch); how many shops run it in prod.
- CEL vs OPA: homepage lists a CEL policy engine; project site references OPA-evaluated policies — confirm the actual policy engine(s) supported.
- Division of labor between OSS agentgateway and the commercial "Solo Enterprise for agentgateway" (what's gated).
- Whether [[authorization-engine]] should be added as a secondary category (it enforces RBAC but isn't a standalone policy engine).

## Sources

- [agentgateway GitHub repo](https://github.com/agentgateway/agentgateway) — fetched 2026-06-28 — supports: features (MCP/A2A/LLM), Apache 2.0, "Linux Foundation project," Rust, ~3.6k stars/maturity; confidence: high.
- [agentgateway.dev (official site)](https://agentgateway.dev/) — fetched 2026-06-28 — supports: one-liner, feature/deployment list, AAIF governance, license; confidence: high.
- [Solo.io blog: Solo Contributes agentgateway to Linux Foundation](https://www.solo.io/blog/solo-contributes-agentgateway-linux-foundation) — fetched 2026-06-28 — supports: donation date 2025-08-25, Solo.io authorship, ztunnel lineage, kgateway distinction, contributor list; confidence: high.
- [AAIF agentgateway project page](https://aaif.io/projects/agentgateway/) — fetched 2026-06-28 — supports: AAIF/Linux Foundation hosting, Solo.io sibling projects; confidence: medium.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established it is an Apache-2.0 OSS Rust proxy created by Solo.io and donated to the Linux Foundation (2025-08-25), now hosted under the Agentic AI Foundation (AAIF) — ownership set to independent/high. Confirmed it is distinct from (not the same as) kgateway. Filled MCP/A2A/LLM gateway functionality, self-hosted/inline-proxy deployment, egress+untrusted-input trifecta role; hedge_fund_fit set low (platform-team infra, Day-2). No M&A. Cached 4 sources.
