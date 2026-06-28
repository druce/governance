---
title: IBM ContextForge MCP Gateway
type: vendor
name: IBM ContextForge MCP Gateway
slug: ibm-contextforge
categories: [mcp-gateway]
layer: model-prompt
aliases: [MCP Context Forge, IBM mcp-context-forge, ContextForge AI Gateway]
website: "https://github.com/IBM/mcp-context-forge"
founded: 2025
hq: Armonk, NY (IBM)
ownership: public
ownership_detail: "IBM open-source project (Apache-2.0); IBM is public (NYSE: IBM). Community/corporate-backed OSS, not a separately sold commercial product as of 2026-06."
ownership_confidence: high
funding_total: n/a
last_funding: n/a
deployment: [self-hosted, on-prem, api, sdk]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [egress, untrusted-input]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [mcp, gateway, open-source, ibm, agentic]
---

# IBM ContextForge MCP Gateway

> Primary category: [mcp-gateway](../categories/mcp-gateway.md). Layer: model-prompt.

**One-liner** — IBM's open-source (Apache-2.0) MCP gateway, registry, and proxy that sits in front of many MCP / A2A / REST / gRPC backends and exposes them as one governed, observable endpoint.

## What it does

ContextForge is a self-hosted control point for agent tool access. It lets you register many backends — MCP servers, agent-to-agent (A2A) endpoints, and ordinary REST/gRPC APIs — and federate them behind a single MCP-compliant endpoint. From that central plane you get:

- **Federation + virtual servers** — point an agent at one gateway URL instead of wiring it to dozens of MCP servers; compose "virtual" MCP servers that expose a curated subset of tools/prompts/resources.
- **REST-to-MCP wrapping** — turn an existing REST API into MCP tools automatically (it extracts JSON Schema for the tools), so legacy services become agent-callable without rewriting them.
- **Central registry** — one catalog of tools, prompts, and resources that MCP-compatible clients can discover.
- **Auth, rate limiting, guardrails** — Basic/JWT/custom auth, user-scoped OAuth tokens, rate limiting and retries, plus a plugin framework (40+ plugins) for guardrails and protocol/transport extensions.
- **Observability** — OpenTelemetry tracing out to Phoenix, Jaeger, Zipkin, or any OTLP backend, plus an admin UI for management and monitoring.

It is itself a fully compliant MCP server, so any MCP client can talk to it.

## Where it sits in the stack

Lives in the [mcp-gateway](../categories/mcp-gateway.md) category at the model/prompt-to-tool boundary: it brokers what tools and data an agent (or LLM app) can reach. In lethal-trifecta terms it is positioned to control two legs:

- **Egress / sensitive-action control** — it is the chokepoint between the model and the tools/APIs/data the agent can call, so it is where you would enforce which backends and actions are allowed.
- **Untrusted-input handling** — its plugin/guardrail hooks can inspect and filter tool inputs/outputs (e.g. prompt-injection or content guardrails) as they flow through.

Trust-zone role: a gateway/broker that you place between a (yellow/red) agent runtime and (green) internal tools and data, concentrating auth, policy, and audit in one place rather than per-server.

## Deployment & architecture

- **Stack** — Python / FastAPI. Distributed as a PyPI package (`mcp-contextforge-gateway`, `pip install`), Docker images, Docker Compose, and Kubernetes Helm charts.
- **Scale** — single-node Gunicorn for small setups up to multi-replica Kubernetes with Redis-backed federation and caching. Data store: SQLite for dev, PostgreSQL for production.
- **Transports** — HTTP, JSON-RPC, WebSocket, SSE, stdio, and streamable-HTTP; it also translates between protocols (e.g. stdio backend exposed over streamable-HTTP).
- **Auth** — Basic, JWT, or custom schemes; user-scoped OAuth tokens; rate limiting and retries built in.
- **Integrations** — MCP servers, A2A (OpenAI-compatible and Anthropic agent routing), gRPC-to-MCP, and IBM **watsonx Orchestrate**: IBM's own developer tutorials deploy ContextForge on IBM Code Engine to give watsonx Orchestrate agents centralized, secure tool access. OTel/IdP integration via standard backends.
- **Self-host only** — there is no vendor-hosted SaaS; you run it yourself (on-prem, your cloud, or IBM Cloud).

> Caveat: the sample MCP servers shipped in the repo are demo-grade ("lack session management, persistent state, multi-tenancy, authentication") and not meant for production as-is. The gateway itself is the production artifact.

## Positioning & differentiators

- **IBM provenance + permissive license.** Backed by IBM and lead-maintained by an IBM Distinguished Engineer, but Apache-2.0 and vendor-neutral — no lock-in, runs anywhere. For regulated buyers the IBM name plus an open license is the headline differentiator. **But verify the support model** (see below) before treating it as "enterprise-supported software."
- **Breadth of what it fronts.** Beyond MCP it also fronts A2A agents and REST/gRPC APIs, and auto-wraps REST as MCP tools — broader protocol coverage than some pure MCP proxies.
- **Self-hosted, infra-first.** Kubernetes/Helm + Redis federation + OTel make it look like infrastructure you operate, versus managed-SaaS control planes.

Nearest neighbors:
- [docker-mcp-gateway](docker-mcp-gateway.md) — Docker's MCP gateway, tightly tied to Docker tooling/containerized MCP catalog; ContextForge is framework-agnostic Python and adds REST/A2A federation and a registry.
- [agentgateway](agentgateway.md) — open-source agent/MCP data-plane proxy (CNCF/solo.io orbit); similar gateway role, different ecosystem.
- [obot](obot.md) — open-source MCP gateway with a stronger product/UI bent.
- [mintmcp](mintmcp.md), [arcade](arcade.md) — more managed/commercial MCP access-control and tool-platform offerings.
- [pomerium](pomerium.md) — identity-aware access proxy extending to MCP; access-control-first vs ContextForge's registry/federation-first framing.

## Ownership, funding & M&A

- **Owner:** IBM (NYSE: IBM), public company, HQ Armonk, NY. Project repo: github.com/IBM/mcp-context-forge.
- **License:** Apache-2.0 (confirmed in repo LICENSE and docs).
- **Funding:** n/a — an internal IBM open-source project, not a venture-funded startup.
- **Product status:** Presented as a corporate-backed open-source community project. As of 2026-06 the docs/README do **not** advertise a separately sold, SLA-backed commercial "ContextForge" product or stated IBM commercial support/warranty. It is, however, the gateway IBM uses in its watsonx Orchestrate agent tutorials. No M&A activity (it's IBM-originated, not acquired).
- **Maturity:** Latest release v1.0.4 (2026-06-23); an earlier "1.0.0 Beta" milestone was announced on IBM Developer. Active repo (~4k stars, 7,000+ tests at fetch).

## CTO / hedge-fund lens

- **Day-2.** You need an MCP gateway once you have real agent deployments calling multiple tools/data sources and need central auth, allow-listing, and audit — not on day one.
- **When it fits:** a fund that wants to self-host its agent tool-access control plane, keep everything on-prem/in-VPC, and avoid a SaaS dependency or per-seat cost. Apache-2.0 + Python/Kubernetes means your platform team owns it.
- **Regulated-shop appeal:** the IBM name and open license read well in vendor due diligence. The honest caveat is the support model — this looks like community/best-effort OSS, not contracted enterprise support. A fund that requires a vendor SLA and someone to call at 2am should confirm whether IBM (or a partner) offers paid support before standardizing on it; otherwise budget for in-house operability.
- **No SR 11-7 / model-risk function itself** — it's plumbing/control-plane, not a model-risk or governance system. It contributes audit/observability and access control that a governance program can lean on.

## Competitors / alternatives

[docker-mcp-gateway](docker-mcp-gateway.md), [agentgateway](agentgateway.md), [obot](obot.md), [mintmcp](mintmcp.md), [arcade](arcade.md), [pomerium](pomerium.md)

## Open questions / to verify

- Does IBM (or a partner) offer paid/commercial support or an SLA for ContextForge, or is it strictly community OSS? (Could not confirm a supported commercial offering as of 2026-06.)
- Is ContextForge bundled into or required by any shipping watsonx product, or only referenced in tutorials? (Tutorials use it; no evidence it's a packaged watsonx component.)
- Founding/first-release date — listed as 2025 from release history context; confirm the initial public release date from the repo's earliest tag.
- Depth/maturity of the built-in guardrail plugins (prompt-injection, DLP) vs. needing external guardrail tools.

## Sources

- [IBM/mcp-context-forge (GitHub repo)](https://github.com/IBM/mcp-context-forge) — fetched 2026-06-28 — supports: what it does, Apache-2.0, Python/FastAPI, PyPI/Docker/K8s, transports, auth, observability, IBM ownership, maintainers; confidence: high
- [ContextForge AI Gateway docs](https://ibm.github.io/mcp-context-forge/) — fetched 2026-06-28 — supports: license, feature pillars (tools/agent/API gateway), admin UI, deployment targets; confidence: high
- [Latest release v1.0.4 (GitHub API)](https://api.github.com/repos/IBM/mcp-context-forge/releases/latest) — fetched 2026-06-28 — supports: version 1.0.4, published 2026-06-23; confidence: high
- [Deploying MCP Tools on watsonx Orchestrate using ContextForge MCP Gateway (IBM Developer)](https://developer.ibm.com/tutorials/build-mcp-tools-mcp-gateway-watsonx-orchestrate-agents/) — fetched 2026-06-28 (direct fetch 403; via IBM search index snippet) — supports: watsonx Orchestrate + IBM Code Engine integration; confidence: medium

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established it's IBM's Apache-2.0 open-source MCP/A2A/REST gateway+registry (Python/FastAPI, self-host via PyPI/Docker/K8s), federation + virtual servers + REST-to-MCP, OTel observability, used in IBM watsonx Orchestrate tutorials. Ownership set public (IBM, high confidence); flagged that commercial support model is unconfirmed (appears community OSS). Kept category [mcp-gateway](../categories/mcp-gateway.md). Latest release v1.0.4 (2026-06-23).
