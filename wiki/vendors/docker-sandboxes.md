---
title: Docker Sandboxes
type: vendor
name: Docker Sandboxes
slug: docker-sandboxes
aka: [sbx, docker sbx, Docker AI Governance, Docker Sandboxes CLI, sandboxd]
primary_category: ephemeral-environments
also_listed_in: [mcp-gateway, agent-runtime-security]
website: https://docs.docker.com/ai/sandboxes/
founded: 2026
hq: Palo Alto, California, US
ownership_state: independent
owner: null
ownership_note: Proprietary product of Docker, Inc., a private, venture-backed company (HQ Palo Alto). No 2026 funding round or acquisition found as of 2026-10-20. Last primary round $105M at ~$2.1B (2022). CEO Don Johnson since 2025-02-12; new CPO and CFO appointed 2026-08-18. Sister product to the open-source docker-mcp-gateway page.
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: 2022 — $105M at ~$2.1B valuation (Docker, Inc.; led by Bain Capital Ventures)
market_position: {ephemeral-environments: challenger, mcp-gateway: platform-module, agent-runtime-security: platform-module}
deployment_model: [self-hosted, saas]
form_factor: [platform, api, sdk]
data_leaves_tenancy: partial
integrations: [claude-code, codex, gemini-cli, github-copilot, opencode, kiro, cursor, cedar, saml, scim, splunk, dynatrace]
mcp_support: gateway
certifications: []
pricing_model: "Local sbx CLI and local sandboxes free (including commercial use); cloud sandboxes pay-as-you-go (rates not published on docs); AI Governance (central policy, audit logs) a separate paid subscription, contact sales"
fs_traction: unverified
target_customer: Developers running autonomous coding agents on laptops or Linux hosts; platform and security teams that want central control over those agents
last_verified: 2026-10-20
verify_after: 2027-01-20
tags: [agent-sandbox, coding-agents, microvm, egress-policy, credential-injection, cedar, ai-governance, proprietary, docker, fast-release-cadence]
sources:
  - {claim: "sbx v0.38.0 published 2026-08-06; contents (kit spec v2, sbx mcp built-in gateway with Cedar org policy, CVE-2026-17106 sbx cp fix, Claude Desktop token exposure fix); latest stable v0.49.1 on 2026-10-20; proprietary licence", url: "https://github.com/docker/sbx-releases/releases/tag/v0.38.0", date: 2026-08-06, confidence: high}
  - {claim: "microVM per session with own kernel and private Docker daemon; custom VMM on Hypervisor.framework / Windows Hypervisor Platform / KVM; launched week before 2026-04-16; supported agents; no Docker Desktop licence needed", url: "https://www.docker.com/blog/why-microvms-the-architecture-behind-docker-sandboxes/", date: 2026-04-16, confidence: high}
  - {claim: "host-side proxy for all outbound TCP; sentinel-swap credential injection; deny-by-default egress; stated limitations; free local use; telemetry", url: "https://docs.docker.com/ai/sandboxes/security/", date: 2026-10-20, confidence: high}
  - {claim: "Docker AI Governance launched 2026-05-12: central network, filesystem, credential and MCP policy over Sandboxes and MCP Gateway; SAML/SCIM; contact sales", url: "https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/", date: 2026-05-12, confidence: high}
  - {claim: "AI Governance audit logs 2026-08-03: 90-day retention in Docker Cloud, CSV export, SIEM streaming over HTTPS; metadata only; Sandboxes decisions only, MCP Gateway decisions later", url: "https://www.docker.com/blog/docker-ai-governance-audit-logs-now-where-your-security-team-already-works/", date: 2026-08-03, confidence: high}
  - {claim: "Governance requires separate paid subscription; Docker Home AI Platform console and Governance API; ~5 min propagation; cloud sandboxes not covered", url: "https://docs.docker.com/ai/sandboxes/security/governance/", date: 2026-10-20, confidence: high}
  - {claim: "Docker, Inc. leadership: CEO Don Johnson (2025-02-12); CPO Mat Velloso and CFO Vinh Le (2026-08-18)", url: "https://www.docker.com/press-release/docker-announces-don-johnson-as-new-ceo-succeeding-scott-johnston/", date: 2026-08-18, confidence: high}
---

# Docker Sandboxes

> Primary category: [ephemeral-environments](../categories/ephemeral-environments.md). Also listed in [mcp-gateway](../categories/mcp-gateway.md) and [agent-runtime-security](../categories/agent-runtime-security.md).

**One-liner** — Docker's `sbx` CLI runs a coding agent such as Claude Code or Codex inside a disposable microVM on the developer's own machine, or in Docker's cloud. Network egress, mounted folders, credentials and MCP tools are all controlled from outside the VM. **Docker AI Governance** is the paid admin layer: it pushes those controls centrally to every developer and logs every decision.

**What it does** — A developer installs `sbx`, signs in with a Docker account and runs, for example, `sbx run claude` in a project directory. `sbx` starts a microVM with its own Linux kernel and its own private Docker daemon. The project folder is mounted in, or cloned in read-only. The agent then runs with no permission prompts ("YOLO mode by default", per the README), because the VM boundary takes the place of the agent's own approval prompts. Everything the agent sends out goes through a proxy on the host. That proxy applies the network policy and adds real credentials to approved requests. The agent itself only ever holds a placeholder. Agents named by Docker (2026-04-16): Claude Code, Codex, OpenCode, GitHub Copilot, Gemini CLI, Kiro, Docker Agent, OpenClaw and NanoClaw. Later release notes also mention Cursor. Other features as of October 2026: "kits", which are signed, reusable sandbox definitions; a built-in MCP gateway (`sbx mcp`); experimental GPU passthrough on Linux; local-model mode; and **cloud sandboxes**, which run on Docker-managed compute and are driven from the CLI or a Sandboxes API/SDK.

**How it differs from the others in this category.** [daytona](daytona.md) and [modal](modal.md) sell sandboxes as a cloud API for agents that *a firm builds*. [github-codespaces](github-codespaces.md) and [azure-dev-boxes](azure-dev-boxes.md) are workstations for *humans*. Docker Sandboxes is aimed mainly at the third case: a firm's developers running *off-the-shelf coding agents* on their own machines. The question it answers is "how do I let Claude Code run unattended on a quant's laptop without it reaching everything on that laptop and the network?" Its cloud mode overlaps with Daytona and Modal, but that mode is newer and less documented (see gotchas).

**Naming / provenance** — "Docker Sandboxes" is the product. `sbx` is its CLI, and `sandboxd` is the background daemon it runs on the host. The release repo `docker/sbx-releases` was created 2026-03-03. A Docker engineering post dated **2026-04-16** says the product launched "last week". One third-party source says March 2026. Take the launch as roughly March–April 2026; the exact date is not confirmed. **Docker AI Governance** launched **2026-05-12** as "the control plane that sits on top of" Sandboxes and the MCP Gateway. It is not a separate engine. It is the centrally managed policy and audit layer for these same sandboxes, so it is covered on this page rather than given a page of its own. Two things to keep apart: (a) the open-source [docker-mcp-gateway](docker-mcp-gateway.md) and Docker Desktop MCP Toolkit, and (b) the MCP gateway built into `sbx`. Docker's docs say (b) "is separate from the Docker Desktop MCP Toolkit" and the two don't share server settings. Whether they share code was not confirmed.

**The v0.38.0 release (asked about specifically).** Published **2026-08-06**. It is **no longer current**: stable releases ship roughly weekly, and the latest is **v0.49.1 (2026-10-20)**. What v0.38.0 brought:
- **MCP management**: `sbx mcp` registers remote or local MCP servers once and reuses them across agents and sandboxes through a built-in gateway. OAuth tokens stay on the host, and organizations can govern server registration and tool calls with **Cedar** policies.
- **Kit spec v2**, a new schema for sandbox definitions covering setup, permissions, networking and credentials.
- **Security fixes**: a destination-escape flaw in `sbx cp` copy-out (**CVE-2026-17106**, GHSA-hfg8-hc9c-6c3h). Claude Desktop SSH sessions no longer expose Desktop OAuth tokens inside sandboxes. The local egress proxy no longer serves other users on a shared host.
- **Policy usability**: per-sandbox `--deny-network` rules; organization policy refreshes as soon as the user signs in; clearer messages when organization policy overrides a local allow.
- **Experimental**: enterprise upstream-proxy settings (including Windows NTLM/Kerberos), NVIDIA GPU passthrough on Linux, and running Claude Code against a local GGUF or Ollama model.

The cadence and the security fixes have a practical consequence. A firm should track current releases (the stable channel on WinGet/APT/Homebrew), not standardize on v0.38.0.

**Ownership & viability** — Docker, Inc. is private and `independent`. No 2026 funding round, sale or acquisition was found (searched 2026-10-20). The last primary round was **$105M at ~$2.1B in 2022**. Secondary-market estimates are lower: TrueUp put it at ~$0.8–0.9B in May–July 2026. Those are aggregator figures and low confidence. Leadership: CEO **Don Johnson**, formerly founder of Oracle Cloud Infrastructure, since **2025-02-12**. On **2026-08-18** Docker appointed **Mat Velloso** as CPO (ex-Microsoft, Google AI Studio) and **Vinh Le** as CFO. The release framed this as helping organizations "secure, govern, and manage agentic workflows". Viability: Docker has a large developer installed base and is plainly putting its AI strategy behind Sandboxes and AI Governance. The risk is in the product's age, not the company's survival. The product is about seven months old, ships weekly and changes often (kit v1 to v2, deprecated secret flags). Commentators speculate that Docker could be acquired by a cloud or enterprise-software vendor. That is speculation only; no deal is reported.

**Positioning & differentiators** — `challenger` in ephemeral-environments: it is a new product from an established developer-tools company and is growing fast in a slot where Daytona and Modal are the purpose-built agent players. In mcp-gateway and agent-runtime-security it is `platform-module`, because those capabilities come bundled with the sandbox and governance product rather than sold on their own.
- **vs. [daytona](daytona.md) / [modal](modal.md):** both are cloud sandbox APIs for agents a firm builds itself. Docker's centre of gravity is *local* microVMs for existing coding agents, with free local compute. Isolation also differs. Docker gives each sandbox its own kernel through a hypervisor. Daytona uses Sysbox containers that share the host kernel, and Modal uses gVisor or a VM runtime.
- **vs. running agents in a plain container or devcontainer:** Docker's own argument (blog, 2026-04-16) is that agents which build containers need Docker-in-Docker, and that requires elevated privileges. Giving each sandbox its own daemon inside a VM avoids that.
- **vs. agent-runtime-security vendors** such as [zenity](zenity.md) and [lasso-security](lasso-security.md): Docker enforces at the execution boundary, through the egress proxy, mount rules and credential substitution. It does not inspect prompts or agent intent. The two approaches complement each other.
- **vs. other [mcp-gateway](../categories/mcp-gateway.md) products:** the `sbx` gateway governs MCP only for agents running inside Docker Sandboxes, using Cedar policy. It is not a general MCP gateway for every agent in the firm.

**Who should choose them / anti-fit** — Fits a firm that wants developers or quants to use autonomous coding agents on their machines, and wants a hard boundary around what those agents can touch: which repos, which hosts, which secrets. Fits especially well where Docker is already the standard tooling and the security team wants central policy plus SIEM logs. **Anti-fit:** a firm that needs sandboxes for agents it is *building and running in production at scale*. Cloud mode exists, but Daytona or Modal are the more established choice there. Also anti-fit: a firm that requires source-available or self-hosted software for every control, since `sbx` is proprietary and the governance console is Docker-hosted. Also anti-fit: anyone expecting AI Governance to cover non-Docker agents, or Docker's cloud sandboxes, which it does not as of 2026-10-20.

**Known weaknesses / gotchas** —
- **The workspace is a live path to the host.** In direct-mount mode the agent can edit files that run later outside the sandbox: Git hooks in `.git/` (which `git diff` does not show), CI configs, `Makefile`, `package.json` scripts. Docker's docs list this limitation themselves. Clone mode (read-only source) reduces the exposure.
- **Not everything runs inside the VM.** Local stdio MCP servers run *on the host* with host permissions, and remote MCP servers run outside Sandboxes altogether. Shared skills with read-write access put several sandboxes inside one trust boundary.
- **The default allowlist is broad.** Egress is deny-by-default, but the default allowed domains include wildcards such as `*.googleapis.com`. Review the defaults with `sbx policy ls`; do not assume the starting state is minimal.
- **Agents run with no approval prompts by default.** Containment then depends entirely on the VM, the egress policy and what is mounted. This is by design, but approval gates have to be configured deliberately (network "require approval", MCP Cedar approval rules).
- **Governance coverage is partial.** AI Governance policy does not apply to cloud sandboxes. Filesystem rules are checked only when a sandbox is created. As of 2026-08-03, audit logs cover Sandboxes decisions only; MCP Gateway enforcement decisions are "planned", with no date.
- **Fast-moving and proprietary.** Weekly releases with real security fixes (CVE-2026-17106 in v0.38.0) mean patch management matters. The licence is proprietary ("All rights reserved"), and the GitHub repo holds release builds, not source.
- **Sign-in required.** Each sandbox is tied to a Docker account. Local use needs network access to Docker services for authentication, image pulls and diagnostics.

**Deployment & data handling** — **Local sandboxes** run on the developer's macOS, Windows or Linux machine. Docker built its own VMM on Apple Hypervisor.framework, Windows Hypervisor Platform or KVM, and chose not to use Firecracker because it lacks macOS and Windows support. Per a third-party Arm guide, `sbx` is not available on Arm Linux. Code and agent work stay on the machine, though prompts still go to whichever model provider the agent uses. Data that does reach Docker: CLI telemetry (command, success, duration, Docker username; not prompts or code; opt-out `SBX_NO_TELEMETRY=1`), diagnostic uploads, and AI Governance audit records (metadata only: never prompt content, agent output or parameter values; 90-day retention in Docker Cloud). **Cloud sandboxes** run on Docker-managed infrastructure (provider and region not stated) and keep their own store of secrets and network policy. Anything placed in them leaves the firm. Hence `data_leaves_tenancy: partial`. **Inline:** the host proxy sits in line on every outbound TCP connection from the sandbox. For HTTP(S) the proxy swaps a placeholder for the real credential after the request leaves the VM, so raw secrets never enter the VM. The docs do not say whether HTTPS is terminated (intercepted) for inspection. Latency figures: none published.

**Integrations & partnerships** — Agents: Claude Code, Codex, OpenCode, GitHub Copilot, Gemini CLI, Kiro, Docker Agent, OpenClaw, NanoClaw, Cursor. MCP: built-in gateway with OAuth on the host and Cedar policy. Identity: Docker accounts, with SAML SSO and SCIM for AI Governance and teams synced from IdP groups. SIEM: HTTPS streaming. Splunk and Dynatrace are named, and some copies of the post also name Datadog and Grafana (unconfirmed). Management: Docker Home "AI Platform" console plus a Governance API (network and filesystem rules only). Enterprise networking: upstream proxy chaining, PAC support, Windows integrated proxy authentication (experimental as of v0.38.0). Related Docker pages: [docker-mcp-gateway](docker-mcp-gateway.md).

**Compliance & FS traction** — No certifications specific to Sandboxes or AI Governance were found. Docker, Inc.'s corporate attestations (SOC 2, ISO 27001) were **not checked** for this page. **No named financial-services customers**, and no customers at all are named in the launch posts. Useful for exams: the audit log has a decision record per policy evaluation (allowed / denied / held for a human), carrying identity, timestamp, session context and the matching rule, with CSV export and SIEM streaming. Retention in Docker Cloud is 90 days, so longer retention needs the SIEM.

**Commercial** — The local `sbx` CLI and local sandbox compute are **free, including commercial use**, and need no Docker Desktop licence (Docker, 2026-04-16). Cloud sandboxes are **pay-as-you-go**; no rates are published in the docs. **AI Governance** requires "a separate paid subscription" through Docker Sales, with no list price. Docker does not say whether it is an add-on to Docker Business. Model-provider costs are separate.

## Open questions

- Is AI Governance an add-on to Docker Business or a standalone SKU, and what does it cost?
- Is it formally GA? Docker says "available now" but gives no GA or beta label. Same question for cloud sandboxes.
- Does the `sbx` built-in MCP gateway share code with open-source [docker-mcp-gateway](docker-mcp-gateway.md)? What is the long-term plan for Docker Desktop MCP Toolkit alongside it?
- Does the host proxy terminate TLS? How do credential substitution and HTTP method/path rules work for HTTPS?
- Which provider and region host cloud sandboxes, what isolation do they use, and what do they cost?
- Do Docker, Inc.'s SOC 2 / ISO 27001 reports cover Sandboxes, cloud sandboxes and AI Governance?
- Exact launch date of Docker Sandboxes (sometime from March to mid-April 2026).
- Any FS customers; any independent security review of the microVM boundary.
- When MCP Gateway decisions will appear in AI Governance audit logs.

## Sources

- [docker/sbx-releases — v0.38.0 release notes](https://github.com/docker/sbx-releases/releases/tag/v0.38.0) plus GitHub API metadata for the repo, releases, README and LICENSE — fetched 2026-10-20 — supports: v0.38.0 date and contents, CVE, release cadence, latest v0.49.1, proprietary licence, install channels; confidence: high
- [Why MicroVMs: The Architecture Behind Docker Sandboxes (Docker blog, 2026-04-16)](https://www.docker.com/blog/why-microvms-the-architecture-behind-docker-sandboxes/) — fetched 2026-10-20 — supports: microVM design, per-OS hypervisors, launch timing, agents, no Docker Desktop licence; confidence: high (vendor engineering blog)
- [Docker Sandboxes docs: overview](https://docs.docker.com/ai/sandboxes/), [architecture](https://docs.docker.com/ai/sandboxes/architecture/), [security](https://docs.docker.com/ai/sandboxes/security/), [FAQ](https://docs.docker.com/ai/sandboxes/faq/), [local vs cloud](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud/), [MCP gateway](https://docs.docker.com/ai/sandboxes/mcp-gateway/) — fetched 2026-10-20 — supports: proxy and credential mechanics, defaults, limitations, pricing, telemetry, cloud differences, separation from MCP Toolkit; confidence: high (vendor docs)
- [Docker AI Governance: Unlock Agent Autonomy, Safely (Docker blog, 2026-05-12)](https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/) — fetched 2026-10-20 — supports: launch, scope, policy delivery, SAML/SCIM; confidence: high (vendor marketing)
- [Docker AI Governance: Audit Logs (Docker blog, 2026-08-03)](https://www.docker.com/blog/docker-ai-governance-audit-logs-now-where-your-security-team-already-works/) — fetched 2026-10-20 — supports: audit retention, export, SIEM, scope; confidence: high (vendor marketing)
- [AI Governance docs](https://docs.docker.com/ai/sandboxes/security/governance/) — fetched 2026-10-20 — supports: paid subscription, console/API, enforcement timing, limitations; confidence: high (vendor docs)
- [Docker press release: Don Johnson CEO (2025-02-12)](https://www.docker.com/press-release/docker-announces-don-johnson-as-new-ceo-succeeding-scott-johnston/) and [Docker press release: CPO and CFO appointments (2026-08-18)](https://www.docker.com/?p=92869) — fetched 2026-10-20 — supports: leadership, independence; confidence: high. Secondary valuation estimates (TrueUp, Stockanalysis/Hiive) via search summary; confidence: low
- Cached: `raw/sources/2026-10-20--docker-sandboxes--sbx-releases-v0-38-0.md`, `raw/sources/2026-10-20--docker-sandboxes--docs-architecture-security.md`, `raw/sources/2026-10-20--docker-sandboxes--why-microvms-blog.md`, `raw/sources/2026-10-20--docker-ai-governance--launch-audit-docs.md`, `raw/sources/2026-10-20--docker--leadership-ownership-2026.md`

## History

- [2026-10-20] Page created via wiki-create + wiki-research, prompted by a user question about "Docker AI Governance" and "Docker sbx v0.38.0". Product slug chosen (Docker Sandboxes is the unit people shop for), matching the existing product-slug choice for [docker-mcp-gateway](docker-mcp-gateway.md). Docker AI Governance is covered here as the paid control plane over Sandboxes, not given its own page.
