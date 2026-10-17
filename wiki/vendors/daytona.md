---
title: Daytona
type: vendor
name: Daytona
slug: daytona
aka: [Daytona Platforms, daytona.io]
primary_category: ephemeral-environments
also_listed_in: []
website: https://www.daytona.io/
founded: null
hq: New York, NY, USA
ownership_state: independent
owner: null
ownership_note: Venture-backed, Series A. $24M Series A announced 2026-02-05, led by FirstMark Capital with Pace Capital, Upfront Ventures, E2VC, Darkmode, and strategic investments from Datadog and Figma Ventures. Founded as a human dev-environment company (lineage from CEO Ivan Burazin's Codeanywhere); hard pivot to AI-agent sandboxes in January 2025.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: Series A, $24M, 2026-02-05 (led by FirstMark Capital)
market_position: {ephemeral-environments: ai-native-disruptor}
deployment_model: [saas, hybrid]
form_factor: [api, sdk, platform]
data_leaves_tenancy: partial
integrations: [langchain, docker-oci, mcp-server]
mcp_support: server
certifications: [soc2-type2]
pricing_model: usage
fs_traction: unverified
target_customer: AI-agent builders, coding-agent and RL/eval teams; startups to large enterprises and AI labs
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [agent-sandbox, code-execution, sysbox, bare-metal, byoc, pivot, aie-nyc-2026]
sources:
  - {claim: "$24M Series A 2026-02-05 led by FirstMark; Pace, Upfront, E2VC, Darkmode; Datadog and Figma Ventures strategic; NY HQ; 20 people; customers LangChain, Turing, Writer, SambaNova", url: "https://pulse2.com/daytona-24-million-series-a/", date: 2026-02-05, confidence: high}
  - {claim: "Pivot from human dev environments to agent sandboxes in January 2025; Sysbox-hardened containers on bare metal with own scheduler; ~60 ms start; AGPL-3.0 sandbox licence; ~25 employees; largest customer ~850k sandboxes/day", url: "https://latent.space/p/daytona", date: 2026-05-21, confidence: medium}
  - {claim: "SOC 2 Type II report issued 2026-07-28 (Insight Assurance, period 2025-12-16 to 2026-03-15); sub-processors Leaseweb, Latitude.sh, OVHcloud, Stripe, AWS; Sysbox boundary named in CVE-2026-31431 advisory", url: "https://trust.daytona.io/", date: 2026-10-16, confidence: high}
  - {claim: "Per-tier egress controls: CIDR/domain allowlists, block-all, outbound proxy", url: "https://www.daytona.io/docs/en/network-limits/", date: 2026-10-16, confidence: high}
  - {claim: "Usage pricing per second; $200 free credit; Enterprise tier adds SSO, audit logs, BYOC", url: "https://www.daytona.io/pricing", date: 2026-10-16, confidence: high}
  - {claim: "Public GitHub repo no longer maintained; development moved private June 2026; repo archived (GitHub API archived=true, banner 2026-10-03)", url: "https://github.com/daytonaio/daytona", date: 2026-10-16, confidence: high}
---

# Daytona

> Primary category: [ephemeral-environments](../categories/ephemeral-environments.md).

**One-liner** — An API that gives an AI agent its own disposable, isolated computer: spin up a sandbox in well under a second, let the agent run code or drive a desktop inside it, snapshot or fork it, then throw it away.

**What it does** — Daytona sells programmatic "composable computers for AI agents". A developer's code (or an agent framework) calls the API or one of the SDKs (Python, TypeScript, Ruby, Go, Java) to create a **sandbox**: an OCI/Docker-compatible environment with its own filesystem, network stack, and allotted vCPU, RAM, disk and optionally GPU. Sandboxes are **stateful**: they can be paused, resumed, snapshotted, and forked into parallel branches, which suits agents exploring several solution paths and reinforcement-learning or evaluation harnesses that need thousands of identical environments at once. The company targets three workloads: agent code execution, computer use (including feature-flagged Windows sandboxes), and RL/evals. By the founder's account, RL/eval workloads went from near zero to about half of usage within months in 2026.

**How agent code sandboxes differ from the dev environments in this category.** The category page currently lists [github-codespaces](github-codespaces.md) and [azure-dev-boxes](azure-dev-boxes.md). Those are workstations for a *human*: provisioned in minutes, long-lived for days or weeks, sized for an IDE session, and governed through seats and developer identity. An agent sandbox is built for a *program*:

- **Lifecycle.** It is created per task or per tool call, often lives for seconds or minutes, and is created by the thousand. Daytona's founder cites about 60 ms to start one sandbox and about 75 seconds for 50,000 concurrent ones. Codespaces and Dev Boxes are not built for that scale.
- **Interface.** Control is by API or SDK from inside an agent loop, not through a portal or IDE.
- **Threat model.** The code inside is assumed untrusted: model-generated and possibly steered by malicious input. The isolation boundary and the egress policy are the product, not a side feature.
- **Billing.** Pay per second of compute, not per developer seat.

The goal in this category is the same: disposable compute with nothing persistent to compromise. The buyer is different, though. The agent-platform or quant-engineering team owns these sandboxes, not developer-experience.

**Naming / provenance** — The company began about three years before mid-2026 by automating human dev environments, building on the stack behind Burazin's earlier browser IDE, Codeanywhere. That product was open-core under Apache 2.0. In **January 2025** Daytona made what the founder calls a hard pivot to AI-agent sandboxes, after watching early coding agents (Devin, OpenDevin/OpenHands) struggle on existing infrastructure. Older articles and GitHub issues that describe Daytona as a "dev environment manager" refer to the pre-pivot product. Founding year and legal entity name were not confirmed from a primary source.

**Ownership & viability** — `independent`, Series A. **$24M Series A announced 2026-02-05**, led by FirstMark Capital (Matt Turck joined the board), with Pace Capital, Upfront Ventures, E2VC and Darkmode. Datadog and Figma Ventures invested strategically. A secondary profile puts total funding near $31M including a ~$7M seed. That figure is **unverified**. The company stated that it hit a $1M forward revenue run rate in under three months, then doubled it about six weeks later, and that growth is limited by hardware supply. Headcount was about 20 at the Series A and about 25 by May 2026. On viability: usage growth is strong (74% month over month per the founder), and named users include Cognition, Lovable, Harvey, LangChain and Writer. But this is a small company running its own bare-metal fleet against far better-funded rivals ([modal](modal.md) raised $750M in October 2026). It is a plausible acquisition target for a cloud, observability or AI-lab buyer. Datadog's strategic stake is worth watching.

**Positioning & differentiators** — Labelled `ai-native-disruptor`: it is purpose-built for agents, unlike the human-workstation incumbents this category lists, and it was founded and funded on that pivot.
- **vs. [github-codespaces](github-codespaces.md) / [azure-dev-boxes](azure-dev-boxes.md):** different job. Those provide human dev workstations. Daytona provides sub-second, API-driven, per-task sandboxes. A firm can need both.
- **vs. [modal](modal.md):** Modal is a general serverless-compute platform whose Sandboxes product runs on **gVisor** or a VM runtime. Daytona does only sandboxes and isolates with **Sysbox-hardened containers** on its own bare metal. Daytona puts more emphasis on long-lived stateful sandboxes (pause, fork, Windows desktops). Modal brings far greater scale, funding and a broader compute platform.
- **vs. [cloudflare-workers](cloudflare-workers.md):** Workers are V8 isolates for short request handlers, not a full Linux machine where an agent can `pip install` and run arbitrary binaries.
- **Isolation strength is a design choice to probe.** Sysbox gives containers stronger isolation (user namespaces, no privileged host access), but it is still a container sharing the host kernel. Firecracker microVMs and gVisor put an extra boundary between guest code and the host kernel. The docs' phrase "dedicated kernel" does not match the founder's description of Sysbox containers, so ask the vendor to explain this in a POC.

**Who should choose them / anti-fit** — Fits a firm building **its own agents that execute generated code**: a research-platform team giving an internal coding or data-analysis agent a scratch machine, or a team running large eval or RL sweeps where cold-start time and fork/snapshot matter. Also fits teams wanting Windows desktops for computer-use agents. **Anti-fit:** a firm whose only AI use is a vendor chatbot or a commercial coding assistant. It has no code-execution workload to sandbox. Also anti-fit: a firm that requires fully self-hosted software it can audit, now that the open-source repo is archived (see below), and any buyer whose vendor-risk process will not accept a ~25-person Series A company running on bare-metal hosting providers.

**Known weaknesses / gotchas** —
- **The open-source story changed in 2026.** The public `daytonaio/daytona` repo (~71k stars, AGPL-3.0 per the founder) says it is **no longer maintained**. Core development moved to a private codebase in June 2026, and GitHub shows the repo archived (banner dated 2026-10-03). Self-hosting the archived AGPL code is possible but unsupported. Do not take "open source, self-hostable" claims in older comparisons at face value.
- **Shared-kernel isolation.** See differentiators. Hostile code in a container is a different risk from hostile code in a microVM.
- **Egress is open by default on higher tiers.** Tier 3–4 organisations get full internet access unless a sandbox sets an allowlist or block-all. A sandbox that can reach the internet and holds credentials or firm data can leak them. Set egress policy explicitly.
- **Hosting footprint.** Sub-processors include Leaseweb, Latitude.sh and OVHcloud (bare-metal providers) as well as AWS. Some FS vendor-risk teams will want to review that.

**Deployment & data handling** — Default is **SaaS**: sandboxes run in Daytona-operated US or EU regions on bare metal, so any code, data or credentials placed in a sandbox leave the firm's tenancy. **BYOC** ("custom regions": customer runner nodes managed by Daytona's control plane) is an Enterprise feature. It was invite-only/experimental as of January 2026. It keeps sandbox compute in the customer's infrastructure, while orchestration metadata still goes to Daytona's control plane. Hence `data_leaves_tenancy: partial`. Egress controls per sandbox: up to 10 IPv4 CIDRs, up to 100 domains (wildcards allowed), block-all, or forcing traffic through an upstream proxy. Retention terms for snapshots and logs are **unverified**. The trust center lists encryption at rest but gives no detail.

**Integrations & partnerships** — SDKs in five languages plus REST API and CLI. Docs list an **MCP server**, so agents can drive Daytona as a tool. Named framework and agent users include LangChain, Cognition, Lovable and Harvey, and Harbor/Terminal-Bench uses it for evals. Strategic investors: Datadog ([datadog](datadog.md)) and Figma Ventures. Cloud-marketplace listings were not verified.

**Compliance & FS traction** — **SOC 2 Type II** report issued 2026-07-28 by Insight Assurance (unqualified opinion, period 2025-12-16 to 2026-03-15; Security, Availability, Confidentiality), available on request. The trust center also lists ISO/IEC 27001, HIPAA and GDPR, without scope detail, so those are recorded here as unverified. **No named financial-services customers found.** Customer examples are AI startups, AI labs and Harvey (legal).

**Commercial** — Usage-based, billed per second: vCPU $0.0504/h, memory $0.0162/GiB-h, storage $0.000108/GiB-h (first 5 GiB free), Windows $0.0858/vCPU-h, preemptible GPUs $0.57–$4.08/h (pricing page, 2026-10-16). $200 free trial credit, and up to $50k for startups. Enterprise (SSO, audit logs, BYOC, higher limits) is contact-sales.

## Open questions

- Exact isolation stack in production: Sysbox containers only, or microVM options for higher tiers? How does that square with the docs' "dedicated kernel" language?
- Scope of ISO 27001 and HIPAA claims on the trust center; whether the SOC 2 covers BYOC.
- BYOC general availability status, and what metadata the control plane sees.
- Licence and support status of the archived AGPL code; whether any self-hosted option remains.
- Total funding to date (seed amount unconfirmed); founding year.
- Data retention for snapshots, volumes and logs.
- Any FS customers.

## Sources

- [Daytona: $24 Million Series A (Pulse 2.0, republishing the press release)](https://pulse2.com/daytona-24-million-series-a/) — fetched 2026-10-16 — supports: round, investors, HQ, headcount, customers; confidence: high
- [Giving Agents Computers — Ivan Burazin (Latent Space, 2026-05-21)](https://latent.space/p/daytona) — fetched 2026-10-16 — supports: pivot date and story, Sysbox isolation, bare metal, AGPL licence, usage figures; confidence: medium (founder self-description)
- [Daytona Trust Center](https://trust.daytona.io/) — fetched 2026-10-16 — supports: SOC 2 Type II details, sub-processors, Sysbox boundary; confidence: high
- [Daytona docs: network limits](https://www.daytona.io/docs/en/network-limits/) and [docs home](https://www.daytona.io/docs/en/) — fetched 2026-10-16 — supports: egress controls, SDKs, product features; confidence: high (vendor docs)
- [Daytona pricing](https://www.daytona.io/pricing) — fetched 2026-10-16 — supports: rates, Enterprise BYOC; confidence: high
- [daytonaio/daytona on GitHub](https://github.com/daytonaio/daytona) — fetched 2026-10-16 — supports: no-longer-maintained notice, archived status; confidence: high
- Cached: `raw/sources/2026-10-16--daytona--series-a-and-pivot.md`, `raw/sources/2026-10-16--daytona--docs-trust-pricing.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
