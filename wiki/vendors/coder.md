---
title: Coder
type: vendor
name: Coder
slug: coder
aka: [Coder Technologies, coder.com, Coder AI Gateway, AI Bridge, Coder Agent Firewall, Agent Boundaries, Coder Tasks]
primary_category: ephemeral-environments
also_listed_in: [ai-gateway, agent-runtime-security]
website: https://coder.com/
founded: 2017
hq: Austin, Texas, USA
ownership_state: independent
owner: null
ownership_note: 'Venture-backed, Series C. $90M Series C announced 2026-04-01, led by funds managed by KKR, with Qube Research & Technologies (QRT), Uncork Capital and existing investors. KKR and QRT are also large customers. Core product is open source (AGPL-3.0); governance features are in the paid Premium licence.'
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: Series C, $90M, 2026-04-01 (led by KKR)
market_position: {ephemeral-environments: leader, ai-gateway: platform-module, agent-runtime-security: platform-module}
deployment_model: [self-hosted, on-prem]
form_factor: [platform, inline-proxy]
data_leaves_tenancy: "false"
integrations: [terraform, kubernetes, docker, aws, azure, gcp, anthropic, openai, aws-bedrock, siem-export]
mcp_support: gateway
certifications: [soc2-type2]
pricing_model: null
fs_traction: verified
target_customer: Enterprises and regulated or government organisations that want developer and coding-agent workspaces on their own infrastructure
last_verified: 2026-10-26
verify_after: 2027-04-26
tags: [cloud-development-environments, self-hosted, air-gapped, open-core, agpl, coding-agents, egress-control, llm-gateway, kkr, qrt]
sources:
  - {claim: "$90M Series C 2026-04-01 led by KKR; QRT and Uncork participated; founded 2017 in Austin; KKR 500+ engineers; QRT half of 2,000+ employees", url: "https://coder.com/blog/90m-series-c-led-by-kkr-to-advance-secure-enterprise-ai-development", date: 2026-04-01, confidence: high}
  - {claim: "Coder 2.30 (2026-02-03): AI Bridge and Agent Boundaries GA in AI Governance add-on for Premium; July 2026 renamed AI Gateway / Agent Firewall; AI Governance now included in new Premium licences", url: "https://coder.com/blog/secure-agentic-ai-now-production-ready", date: 2026-02-03, confidence: high}
  - {claim: "Agent Firewall: nsjail/landjail process-level jail, domain/method/path allowlist, per-request audit to control plane, DNS exfiltration caveat", url: "https://coder.com/docs/ai-coder/agent-firewall", date: 2026-10-26, confidence: high}
  - {claim: "AI Gateway: proxies OpenAI/Anthropic, central keys, logs prompts/token usage/tool calls per user, admin-approved MCP servers", url: "https://coder.com/docs/ai-coder/ai-gateway", date: 2026-10-26, confidence: high}
  - {claim: "Self-hosted on any cloud, on-prem or air-gapped; SOC 2 Type II audited annually; audit events to SIEM; telemetry on by default, can be disabled", url: "https://coder.com/use-cases/secure-development-environments", date: 2026-10-26, confidence: medium}
  - {claim: "Autostop, dormancy and auto-deletion of workspaces; dormancy/auto-delete are Premium", url: "https://coder.com/docs/admin/templates/managing-templates/schedule", date: 2026-10-26, confidence: high}
  - {claim: "AGPL-3.0, active repo, releases 2026-10-23", url: "https://github.com/coder/coder", date: 2026-10-26, confidence: high}
---

# Coder

> Primary category: [ephemeral-environments](../categories/ephemeral-environments.md). Also listed in [ai-gateway](../categories/ai-gateway.md) and [agent-runtime-security](../categories/agent-runtime-security.md).

**One-liner** — Self-hosted cloud development environments: developers and coding agents work in disposable workspaces that run on the firm's own cloud, on-prem or air-gapped infrastructure, with source code kept off laptops. Recent versions add an LLM gateway and a per-agent egress firewall.

**What it does** — An admin writes **templates**, usually Terraform, that define a workspace: a container, VM or Kubernetes pod, plus its image, network, and the credentials it gets. Developers, or agents launched through **Coder Tasks**, create workspaces from those templates on infrastructure the firm runs. A control plane (`coderd`) manages them. Users connect from VS Code, JetBrains, Cursor, a browser IDE or SSH. Workspaces can stop automatically when idle, go dormant, and be deleted after a set period, so environments do not pile up.

Since 2026, a paid **AI Governance** layer adds two controls for coding agents:

- **AI Gateway** (called *AI Bridge* until July 2026) sits between agents or IDEs and model providers: OpenAI, Anthropic, and AWS Bedrock, including through a corporate gateway. Users sign in with their Coder identity and `coderd` calls the provider for them, so developers never hold provider API keys. It can log prompts, token usage and tool calls, each attributed to a named user. Admins set which MCP servers and tools are allowed. It works for clients outside Coder workspaces as well as inside.
- **Agent Firewall** (called *Agent Boundaries* until July 2026) is a process-level network jail around an agent running in a workspace. It allows only listed domains, HTTP methods and paths, and blocks everything else. Every HTTP request is logged centrally with the allow or deny decision, workspace, owner, template, method, URL and the rule that matched. It works with any terminal-based agent (Claude Code, Codex CLI, custom agents).

**Why a CTO would use it for isolation** — Coder is the self-hosted way to turn the [trust-zone-segmentation](../categories/trust-zone-segmentation.md) design into real infrastructure for developers and coding agents:

- **Zone-scoped by template.** Each template fixes the network, data access and credentials a workspace gets. You can have a research-data template with warehouse access and no internet, and an open-source template with internet and no internal data. Developers choose a template; they cannot widen what it allows.
- **Short-lived.** Autostop, dormancy and auto-delete stop workspaces from accumulating months of credentials and drift.
- **Agent-specific egress.** Agent Firewall applies a tighter allowlist to the agent process than to the human in the same workspace. This is the main difference from [github-codespaces](github-codespaces.md) and [google-cloud-workstations](google-cloud-workstations.md), which control the network only at workspace or VPC level.
- **One audit trail** for model calls (AI Gateway) and agent network requests (Agent Firewall), streamed to the SIEM.

**Naming / provenance** — Founded in 2017 in Austin, Texas, as Coder Technologies, and sold as "Coder" at coder.com. The earlier `code-server` project, which runs VS Code in a browser, is also Coder's. The governance features were renamed in July 2026 with no change in function: AI Bridge became **AI Gateway** and Agent Boundaries became **Agent Firewall**. Some configuration options still use the old "boundary" name. Older documents and comparisons use the old names.

**Ownership & viability** — `independent`, Series C. **$90M Series C announced 2026-04-01**, led by funds managed by KKR (mainly its Next Generation Technology Growth Fund III), with Qube Research & Technologies (QRT), Uncork Capital and existing investors. Third-party trackers put the earlier Series B at $65M in total, including a $35M extension in June 2024, and total funding near $175M. Those figures are **unverified** and `funding_total` stays null. The company says bookings grew 300% year on year over four quarters and net dollar retention was 184%. These are vendor figures. Releases ship frequently: v2.36 to v2.38 patch releases all came out on 2026-10-23, and the AGPL repo is active. Viability risk looks low for a Series C company. As a likely acquisition target, the plausible buyers are a cloud, a developer-platform vendor or an AI lab. Ona went to OpenAI in 2026 ([ona](ona.md)), which shows the pattern. Because the core is AGPL and self-hosted, an acquisition would not cut off running deployments, though roadmap and Premium support could change.

**Positioning & differentiators** — `leader` in ephemeral-environments, in the self-hosted segment. After [ona](ona.md)'s acquisition by OpenAI and the shutdown of its hosted service, and with DevPod unmaintained, Coder is the main independent self-hosted cloud-development-environment vendor. It also has named hedge-fund and asset-manager deployments. `platform-module` in ai-gateway and agent-runtime-security: those features are part of Coder Premium and are not sold on their own.

- **vs. [github-codespaces](github-codespaces.md):** Codespaces runs on GitHub's Azure infrastructure. Coder runs on yours, including air-gapped networks, and works with any Git host and any cloud. Codespaces needs no infrastructure team. Coder needs one.
- **vs. [google-cloud-workstations](google-cloud-workstations.md):** both put workspaces in your own network. Cloud Workstations is a managed service on Google Cloud only. Coder runs on any cloud or on-prem, and adds an LLM gateway and agent-level egress control.
- **vs. agent sandboxes ([daytona](daytona.md), [modal](modal.md), [docker-sandboxes](docker-sandboxes.md)):** those are API-created sandboxes for code an agent generates, often lasting seconds. Coder workspaces are full development environments that last hours or days, shared between a human and the agents that person runs. Docker Sandboxes' microVM isolation per session on a laptop is a stronger boundary than a namespace jail. Coder's advantage is running centrally, on server infrastructure, under one policy.
- **vs. a standalone [ai-gateway](../categories/ai-gateway.md):** Coder's AI Gateway knows which workspace, template and user a request came from. A standalone gateway has broader provider routing, guardrails and cost features. Firms that already run a gateway can chain Coder's gateway to it.

**Who should choose them / anti-fit** — Fits a firm that wants developers, quants and coding agents to work **inside its own perimeter**: code and data stay in its VPC or data centre, egress is controlled per template and per agent, and every model call can be audited. That describes most hedge funds with proprietary strategy code. KKR and QRT are reference customers and investors. **Anti-fit:** a small team without platform engineers to run Kubernetes or Terraform and operate a control plane; a firm content with SaaS-hosted dev environments (use Codespaces); and teams whose only need is thousands of short API-created sandboxes for agent-generated code (use an agent-sandbox product).

**Known weaknesses / gotchas** —
- **The governance features are paid.** AI Gateway, Agent Firewall, dormancy and auto-delete, and autostop requirements are Premium features. The free AGPL edition gives you workspaces, not the agent controls.
- **Agent Firewall bypass limits are documented.** The default `nsjail` mode needs `CAP_NET_ADMIN` and may need seccomp changes. Its PID namespace and UDP controls are listed as in progress. The `landjail` mode is rated by Coder itself as "medium bypass resistance": a process can connect directly to the proxy port, there is no UDP control, and tools that ignore `HTTP_PROXY` are blocked rather than filtered. The `use_real_dns` option allows DNS-based data exfiltration. Treat it as a strong guardrail, not a hard security boundary on the level of a microVM.
- **The firewall covers HTTP and HTTPS.** Coder describes workspace network policy plus HTTP allowlists for agents. Lock down non-HTTP egress at the template or VPC level.
- **Telemetry is on by default.** It can be turned off. Do so before treating the deployment as fully in-tenant.
- **The SOC 2 claim is vendor-stated.** The report's scope was not seen.

**Deployment & data handling** — **Self-hosted only** in its standard form, on any cloud, on-prem, or fully air-gapped. Workspaces run on the firm's own compute: Kubernetes, VMs or Docker. An AWS Marketplace listing labelled SaaS delivery appears to be a billing route, not a Coder-hosted service. That is **unverified**. Source code, credentials and model traffic stay inside the firm's infrastructure, and Coder says it has no access to workspaces or source code. Hence `data_leaves_tenancy: "false"`, provided default product telemetry is disabled. AI Gateway is inline between agents and model providers, so prompts still go to whichever provider you configure, under your own contract with that provider. Where AI Gateway stores prompt logs and how long it keeps them is configurable but was not reviewed. That is an open question.

**Integrations & partnerships** — Terraform-based templates on Kubernetes, Docker, AWS, Azure and GCP. IDEs: VS Code, JetBrains, Cursor and browser-based IDEs. Model providers through AI Gateway: OpenAI, Anthropic, AWS Bedrock, and corporate gateways in front of them. MCP: admin-approved MCP server and tool lists (`mcp_support: gateway`). Audit events stream to a SIEM. Coder's Series C release names Claude Code, Cursor and OpenClaw as tools its customers use. Available on AWS Marketplace.

**Compliance & FS traction** — SOC 2 Type II, stated by the vendor as "independently audited annually". Report not seen. **Financial-services evidence is strong and on the record.** In Coder's 2026-04-01 announcement, KKR said Coder runs for more than 500 of its engineers, and more than half of its commits come from Coder-managed environments with AI assistance. QRT (Qube Research & Technologies, a quantitative hedge fund) said it has rolled Coder out to half of its 2,000-plus employees, including engineers, data scientists and analysts. QRT's Zohar Melamed is quoted saying Coder lets it "audit every LLM request". Both firms also invested in the round. That is customer evidence, but both are also shareholders. Other named users include a US defence-intelligence organisation (2,500+ developers), Square and Palantir.

**Commercial** — Open core. The Community edition is free under AGPL-3.0. **Premium** is contact-sales, and per the July 2026 update all newly purchased Premium licences include AI Governance. Earlier Premium licences bought it as an add-on. No public price. Third-party sites quote figures from about $35 per user per month, which is unverified, so `pricing_model` stays null.

## Open questions

- Premium pricing band, and whether it is per seat or per workspace.
- Scope and date of the SOC 2 Type II report, and whether it covers anything beyond Coder's corporate controls, since the product is self-hosted.
- Whether there is a genuinely Coder-hosted SaaS option, given the "SaaS" label on an AWS Marketplace listing.
- Where AI Gateway stores prompts and tool-call logs, and the default retention.
- Agent Firewall's roadmap for PID namespace and UDP controls in `nsjail`, and for egress control beyond HTTP.
- Total funding to date.

## Sources

- [Coder secures $90M Series C led by KKR (Coder blog, 2026-04-01)](https://coder.com/blog/90m-series-c-led-by-kkr-to-advance-secure-enterprise-ai-development), also issued as a press release via [Nasdaq/GlobeNewswire](https://www.nasdaq.com/press-release/coder-secures-90m-series-c-led-kkr-advance-secure-enterprise-ai-development-2026-04). Fetched 2026-10-26. Supports: round, investors, founding, KKR and QRT usage, growth claims. Confidence: high for the round; vendor-reported for the metrics.
- [Secure agentic AI now production-ready (Coder blog, 2026-02-03, with July 2026 update)](https://coder.com/blog/secure-agentic-ai-now-production-ready). Fetched 2026-10-26. Supports: v2.30 GA, AI Governance add-on, renames. Confidence: high.
- [Agent Firewall docs](https://coder.com/docs/ai-coder/agent-firewall) and [AI Gateway docs](https://coder.com/docs/ai-coder/ai-gateway). Fetched 2026-10-26. Supports: mechanisms, audit fields, limitations, licensing. Confidence: high (vendor docs).
- [Secure development environments use case (Coder)](https://coder.com/use-cases/secure-development-environments). Fetched 2026-10-26. Supports: deployment options, SOC 2 claim, SIEM streaming, telemetry, named users. Confidence: medium (marketing).
- [Template scheduling docs](https://coder.com/docs/admin/templates/managing-templates/schedule). Fetched 2026-10-26. Supports: autostop, dormancy, auto-delete, Premium gating. Confidence: high.
- [coder/coder on GitHub](https://github.com/coder/coder). Fetched 2026-10-26. Supports: AGPL licence, release cadence. Confidence: high.
- Cached: `raw/sources/2026-10-26--coder--series-c-and-ai-governance.md`

## History

- [2026-10-26] Page created via wiki-create + wiki-research (dev-environment products batch for ephemeral-environments).
