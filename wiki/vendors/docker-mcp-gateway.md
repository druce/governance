---
title: Docker MCP Gateway
type: vendor
name: Docker MCP Gateway
slug: docker-mcp-gateway
aka: [Docker MCP Toolkit, Docker MCP Catalog, docker mcp gateway]
primary_category: mcp-gateway
also_listed_in: []
website: https://github.com/docker/mcp-gateway
founded: 2025-07-09
hq: Palo Alto, California, US
ownership_state: independent
owner: null
ownership_note: Open-source project (MIT) from Docker, Inc., a private/independent company (HQ Palo Alto). Ships as part of Docker Desktop's MCP Toolkit and is also usable standalone with any Docker Engine. Parent company not acquired; was last priced at ~$2.1B (2022).
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: 2022 — $105M Series ? at ~$2.1B valuation (Docker, Inc.; aggregator-sourced)
market_position: null
deployment_model: [self-hosted]
form_factor: [platform, sdk]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: developers and enterprise platform/security teams already using Docker
last_verified: 2026-10-20
verify_after: null
tags: [mcp, gateway, container-isolation, open-source, docker]
sources:
  - {claim: "repo docker/mcp-gateway still MIT, not archived, last push 2026-09-23, latest tag v0.44.1", url: "https://github.com/docker/mcp-gateway", date: 2026-10-20, confidence: high}
  - {claim: "Docker AI Governance (launched 2026-05-12) is a control plane over Docker Sandboxes and the MCP Gateway", url: "https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/", date: 2026-05-12, confidence: high}
  - {claim: "Docker Sandboxes' built-in MCP gateway is separate from the Docker Desktop MCP Toolkit; Cedar MCP policy via AI Governance", url: "https://docs.docker.com/ai/sandboxes/mcp-gateway/", date: 2026-10-20, confidence: high}
  - {claim: "AI Governance audit logs cover Sandboxes decisions; MCP Gateway enforcement decisions planned, no date", url: "https://www.docker.com/blog/docker-ai-governance-audit-logs-now-where-your-security-team-already-works/", date: 2026-08-03, confidence: high}
---

# Docker MCP Gateway

**One-liner** — An open-source (MIT) Docker CLI plugin that runs MCP servers as isolated containers from a signed catalog and puts them behind one central gateway, adding secrets handling, image-signature verification, call logging, and request interceptors — security mainly through containment.

## What it does

Docker MCP Gateway sits between MCP clients (the AI app / agent) and the MCP
servers (the tools). Instead of an agent launching tool servers directly on the
host via `npx`/`uvx`, the gateway pulls each MCP server as a Docker image and
runs it in its own container "with restricted privileges, network access, and
resource usage." It then aggregates many such servers behind a single endpoint,
so one gateway connection exposes a curated, filtered set of tools.

Around that it layers a handful of governance features:

- **Verified catalog** — servers come from the Docker MCP Catalog (300+ servers
  distributed via Docker Hub), where Docker "builds and signs all local servers"
  and ships them with full provenance and SBOM metadata.
- **Signature verification** — `--verify-signatures` checks image provenance
  before a server is allowed to run.
- **Secrets management** — credentials/API keys are injected from Docker
  Desktop's secret store rather than pasted into config; a `--block-secrets`
  interceptor scans inbound/outbound payloads for content that looks like API
  keys, passwords, or tokens and blocks it.
- **Interceptors** — pre-call (argument/type checks, safety classifiers) and
  post-call (redaction, PII scrub) hooks on tool traffic.
- **Logging / call tracing** — `--log-calls` audits gateway activity for
  visibility and governance.
- **OAuth** — built-in OAuth flows for services that need token auth.
- **Tool filtering** — restrict which servers and which individual tools are
  exposed (`--servers=...`, `--tools=...`).

## Where it sits in the stack

Primary category: [mcp-gateway](../categories/mcp-gateway.md) (layer: model-prompt). It is the control point
between an agent and its tools, the same slot as other MCP gateways/proxies.

Lethal-trifecta role: its main contribution is **containment** — each tool server
runs sandboxed in a container with limited host/network/resource access, which
shrinks the blast radius if a tool is malicious or compromised, and the gateway
is a chokepoint where untrusted tool input and outbound egress can be inspected
(`--block-secrets`, interceptors, signature checks). It touches the
**untrusted-input** leg (it is the boundary where tool responses re-enter the
agent) and the **egress** leg (secret-blocking and call logging on outbound
traffic). It does not by itself solve the sensitive-data leg — that depends on
which servers you run and how interceptors are configured.

## Deployment & architecture

- **Form factor:** a `docker mcp` CLI plugin; the gateway is a process that spawns
  MCP servers as Docker containers on demand and routes client traffic to them.
- **Two ways to run it:**
  1. Bundled in **Docker Desktop's MCP Toolkit** — runs automatically in the
     background when the Toolkit is enabled; zero-config for desktop developers.
  2. **Standalone** with any Docker Engine — download the binary into
     `~/.docker/cli-plugins/` and run `docker mcp gateway run`. Integrates with
     **Docker Compose** for production/agentic workloads.
- **Transports:** stdio and SSE (e.g. `--transport=sse`).
- **Clients:** any MCP client — Docker documents VS Code, Cursor, and Claude
  Desktop connecting to the same gateway config.
- **Catalog:** Docker MCP Catalog on Docker Hub (`hub.docker.com/mcp`); custom
  org-specific catalogs can be imported.
- **Kubernetes:** not clearly documented as a first-class deployment in the
  sources reviewed (to verify).

## Positioning & differentiators

Docker's angle is **isolation-first** governance: it leans on the thing Docker is
already good at — running things in containers — and adds catalog signing, secrets
hygiene, and interceptors on top. That makes it distinctive among MCP gateways,
most of which focus on identity/policy/proxying rather than per-tool sandboxing.

Nearest neighbors (all in [mcp-gateway](../categories/mcp-gateway.md)):

- [ibm-contextforge](ibm-contextforge.md) — open-source MCP gateway/registry; federation and
  virtualization of servers, less about container sandboxing.
- [agentgateway](agentgateway.md) — data-plane/proxy oriented gateway for agent/MCP traffic.
- [obot](obot.md) — MCP gateway with an access-control/management focus.
- [mintmcp](mintmcp.md) — managed MCP gateway aimed at enterprise governance.
- [arcade](arcade.md) — tool-calling/auth platform (strong on per-user OAuth/identity).
- [pomerium](pomerium.md) — identity-aware access proxy applied to MCP.

Versus those, Docker's relative strengths are containment + a signed image supply
chain + native Docker/Compose workflow; its relative gaps are enterprise identity,
multi-tenant policy, and centralized RBAC, where the identity-proxy products
(Pomerium, Arcade, MintMCP) are stronger. Many of these are complementary rather
than mutually exclusive.

## Docker AI Governance and Docker Sandboxes (added 2026-10-20)

In 2026 Docker built a second, proprietary MCP-governance path next to this
open-source gateway. It is covered on [docker-sandboxes](docker-sandboxes.md):

- **Docker Sandboxes (`sbx`)**, launched around March–April 2026, runs coding
  agents in per-session microVMs. Since **v0.38.0 (2026-08-06)** it has its own
  built-in MCP gateway (`sbx mcp`). Docker's docs say this gateway "is separate
  from the Docker Desktop MCP Toolkit" and does not share server settings with
  it. Whether it shares code with this repo is not stated (open question).
- **Docker AI Governance** (launched **2026-05-12**, paid, contact-sales) is
  described as "the control plane that sits on top of" the sandbox and the MCP
  Gateway. It adds admin-console policy, SAML/SCIM team scoping, and MCP rules
  written in **Cedar** covering registration, tool calls, resources, prompts and
  approval gates. As of 2026-08-03, its audit logs/SIEM streaming cover Sandboxes
  decisions only. MCP Gateway enforcement decisions are "planned" with no date.

What this means for a buyer: the earlier gap noted below (thin centralized
policy/RBAC) is partly addressed, but **only through the paid Sandboxes +
AI Governance product, for agents running inside Docker Sandboxes**. The
open-source gateway on its own still has the gaps described on this page. As of
2026-10-20 the repo is still MIT, not archived, last pushed 2026-09-23, latest
tag v0.44.1.

## Ownership, funding & M&A

- **Owner:** Docker, Inc., an independent private company headquartered in Palo
  Alto, California. MCP Gateway is its open-source project, licensed **MIT** (per
  the GitHub repo), launched/open-sourced **2025-07-09**.
- **Parent funding:** Docker, Inc. raised $105M at a ~$2.1B valuation in 2022 led
  by Bain Capital Ventures; aggregators cite a cumulative ~$443M–$541M (figures
  vary by source, not from audited filings — low confidence).
- **M&A:** none relevant to the gateway. Docker, Inc. has not been acquired; it
  sold its enterprise business to Mirantis in 2019 and refocused on developer
  tooling. No seed M&A flag for this entry.
- **Refresh 2026-10-20:** still private and independent. No 2026 funding round
  or acquisition found. CEO Don Johnson (ex-Oracle Cloud Infrastructure founder)
  since 2025-02-12. Mat Velloso (CPO) and Vinh Le (CFO) appointed 2026-08-18
  (Docker press releases). Secondary-market estimates (~$0.8–0.9B, May–Jul 2026,
  TrueUp) are below the 2022 mark; aggregator figures, low confidence.

## CTO / hedge-fund lens

This is a **Day-2** building block, not a turnkey enterprise governance platform.
It is most attractive to a fund that (a) already standardizes on Docker / Docker
Desktop and (b) wants to let developers or agents use MCP tools without each one
running unsandboxed on a laptop or server. The container-isolation and
signed-catalog story is the part a security team will like: it gives a defensible
default (sandbox + verified images + secret-blocking + audit log) at low adoption
cost.

Limits to weigh: it is developer/workstation-centric in its bundled form;
enterprise-grade centralized identity, RBAC, and multi-tenant policy are thinner
than in the identity-proxy gateways, so a regulated shop would likely pair it with
(or front it by) an identity-aware proxy. No SR 11-7 / model-risk angle — this is
infrastructure plumbing. Good as the *sandboxing and supply-chain* layer of an MCP
stack; not sufficient on its own as the *access-governance* layer.

## Competitors / alternatives

[ibm-contextforge](ibm-contextforge.md) · [agentgateway](agentgateway.md) · [obot](obot.md) · [mintmcp](mintmcp.md) · [arcade](arcade.md) ·
[pomerium](pomerium.md)

## Open questions / to verify

- First-class Kubernetes deployment story (vs Docker Desktop / Compose)?
- Exact interceptor extensibility (custom interceptors / plugin API) and whether
  `--block-secrets`/redaction are configurable beyond on/off.
- Centralized multi-user RBAC / multi-tenant policy — present or roadmap?
- Parent Docker, Inc. total funding — no primary/audited figure; aggregator range
  only.
- Relationship/overlap with Docker's `cagent` multi-agent tooling.
- Does the `sbx` built-in MCP gateway share code with this repo? Is Docker
  Desktop MCP Toolkit being superseded by Sandboxes + AI Governance? (added 2026-10-20)

## Sources

- [Docker MCP Gateway: Open Source, Secure Infrastructure for Agentic AI](https://www.docker.com/blog/docker-mcp-gateway-secure-infrastructure-for-agentic-ai/) — fetched 2026-06-28 — supports: what it does, interceptors (`--verify-signatures`/`--block-secrets`/`--log-calls`), OAuth, Compose, launch date 2025-07-09; confidence: high (vendor blog)
- [docker/mcp-gateway (GitHub)](https://github.com/docker/mcp-gateway) — fetched 2026-06-28 — supports: MIT license, container isolation, secrets via Docker Desktop, OAuth, catalog, dynamic discovery, monitoring; confidence: high (primary repo)
- [MCP Gateway / MCP Catalog (Docker Docs)](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) — fetched 2026-06-28 — supports: proxy/isolation architecture, restricted privileges/network/resources, Docker Desktop vs standalone install, signed catalog (300+ servers, provenance + SBOM); confidence: high (vendor docs)
- [docker/mcp-gateway GitHub API](https://api.github.com/repos/docker/mcp-gateway) — fetched 2026-10-20 — supports: MIT, not archived, last push 2026-09-23, tag v0.44.1; confidence: high
- [Docker AI Governance launch blog (2026-05-12)](https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/), [AI Governance audit logs blog (2026-08-03)](https://www.docker.com/blog/docker-ai-governance-audit-logs-now-where-your-security-team-already-works/), [Sandboxes MCP gateway docs](https://docs.docker.com/ai/sandboxes/mcp-gateway/) — fetched 2026-10-20 — supports: AI Governance scope, separation from MCP Toolkit, audit coverage; confidence: high (vendor). Cached: `raw/sources/2026-10-20--docker-ai-governance--launch-audit-docs.md`, `raw/sources/2026-10-20--docker-sandboxes--docs-architecture-security.md`, `raw/sources/2026-10-20--docker--leadership-ownership-2026.md`
- [Docker Raises $105M at $2.1B Valuation (Crunchbase News)](https://news.crunchbase.com/enterprise/docker-bain-capital-vc-funding/) — fetched 2026-06-28 — supports: Docker, Inc. private, Palo Alto HQ, 2022 raise/valuation; confidence: medium (secondary); total-funding figures low confidence (aggregators disagree)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Docker MCP Gateway as an MIT-licensed open-source Docker CLI plugin/gateway (launched 2025-07-09) that runs MCP servers as isolated containers from a signed Docker MCP Catalog, with secrets handling, `--verify-signatures`/`--block-secrets`/`--log-calls` interceptors, and OAuth; ships in Docker Desktop's MCP Toolkit and runs standalone on Docker Engine. Owner = Docker, Inc., independent private company (Palo Alto); not acquired. Corrected license assumption: repo states MIT, not Apache-2.0. Kept primary category [mcp-gateway](../categories/mcp-gateway.md). Set ownership_confidence high (origin) but funding low (aggregator-only). hedge_fund_fit = medium. No M&A flag; no contradictions.
- [2026-10-20] Refreshed (user question on Docker AI Governance / sbx). Added a section on Docker AI Governance (launched 2026-05-12) and the separate MCP gateway built into Docker Sandboxes `sbx` (v0.38.0, 2026-08-06), cross-linked to the new [docker-sandboxes](docker-sandboxes.md) page. Re-checked the repo (MIT, active, v0.44.1). Ownership refresh: still independent; 2026-08-18 CPO/CFO hires. No prior claims changed; added `sources:` frontmatter.
