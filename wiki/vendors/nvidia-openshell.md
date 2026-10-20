---
title: NVIDIA OpenShell
type: vendor
name: NVIDIA OpenShell
slug: nvidia-openshell
aka: [OpenShell, NVIDIA/OpenShell]
primary_category: agent-runtime-security
also_listed_in: [ephemeral-environments, trust-zone-segmentation]
website: https://github.com/NVIDIA/OpenShell
founded: 2026
hq: Santa Clara, CA (NVIDIA)
ownership_state: oss-vendor-backed
owner: NVIDIA
ownership_note: 'Open-source project (Apache-2.0) built and maintained by NVIDIA (NASDAQ: NVDA), part of the NVIDIA Agent Toolkit. Not a standalone company. Repo created 2026-02-24, announced at GTC 2026-03-16, repositioned on 2026-09-28 as the software half of the NVIDIA Open Agent Safety Platform. The related Open Secure AI Alliance is governed by the Linux Foundation, but OpenShell itself remains an NVIDIA-controlled repo.'
acquisition: {announced: null, closed: null, price: null}
funding_total: n/a (NVIDIA-funded OSS project)
last_funding: n/a
market_position: {agent-runtime-security: oss-default}
deployment_model: [self-hosted]
form_factor: [inline-proxy, platform]
data_leaves_tenancy: "false"
integrations: [docker-oci, podman, kubernetes, claude-code, codex, cursor, opencode, openclaw, crowdstrike, cisco-defenseclaw, slack, sap-joule]
mcp_support: unverified
certifications: []
pricing_model: oss (Apache-2.0, free; no paid support tier found)
fs_traction: claimed
target_customer: Platform and security teams running autonomous or long-running agents (coding agents, always-on assistants) on their own infrastructure; NVIDIA hardware users (DGX Spark/Station, Vera, BlueField) get extra features
last_verified: 2026-10-20
verify_after: 2027-01-20
tags: [agent-sandbox, open-source, nvidia, landlock, seccomp, opa, egress-control, credential-brokering, policy-prover, nemoclaw, openclaw]
sources:
  - {claim: "Announced 2026-03-16 at GTC; Apache 2.0; part of NVIDIA Agent Toolkit; sandbox + policy engine + privacy router; out-of-process enforcement; supports OpenClaw, Claude Code, Codex, Cursor, OpenCode", url: "https://developer.nvidia.com/blog/run-autonomous-self-evolving-agents-more-safely-with-nvidia-openshell", date: 2026-03-16, confidence: high}
  - {claim: "Repo created 2026-02-24; Apache-2.0; Rust; ~16.8k stars; v0.1.0 2026-09-25, latest v0.1.4 2026-10-13; libkrun VM runtime; telemetry on by default and can be disabled", url: "https://github.com/NVIDIA/OpenShell", date: 2026-10-20, confidence: high}
  - {claim: "Gateway/supervisor/sandbox split; Landlock filesystem, seccomp user-notification for network ops; Docker/Podman/Kubernetes/MicroVM drivers; JWTs bound to sandbox", url: "https://docs.nvidia.com/openshell/v0.1.3/about/architecture.md", date: 2026-10-20, confidence: high}
  - {claim: "Deny-by-default egress via CONNECT proxy + OPA; per-sandbox network namespace; opaque credential placeholders; L7 enforcement defaults to audit; approvals permanently widen running sandbox policy", url: "https://docs.nvidia.com/openshell/security/best-practices.md", date: 2026-10-20, confidence: high}
  - {claim: "Open Agent Safety Platform 2026-09-28: OpenShell + Sentry (BlueField-4); partners incl. Anthropic, SAP, Salesforce, CrowdStrike, Cisco, Microsoft, JPMorganChase, Citi; Open Secure AI Alliance under Linux Foundation", url: "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Open-Agent-Safety-Platform-to-Secure-Agents-From-Testing-to-Deployment/default.aspx", date: 2026-09-28, confidence: high}
  - {claim: "Security bulletin 2026-08-25: six OpenShell CVEs incl. CVE-2026-65093 sandbox escape (CVSS 9.9) and CVE-2026-65092 L7 policy bypass; affected 0–0.0.33, fixed v0.0.34; found externally", url: "https://github.com/NVIDIA/product-security/tree/main/2026/5872", date: 2026-08-25, confidence: high}
  - {claim: "Analyst view: out-of-band design sound; prover only proves the policy you wrote; no overhead data; governance sits with NVIDIA; credential swap and MCP coverage need scrutiny", url: "https://futurumgroup.com/?p=96053", date: 2026-09-29, confidence: medium}
  - {claim: "CSA draft assessment: isolation strong; no behavioural monitoring; does not address inter-agent trust, identity, prompt-injection detection", url: "https://labs.cloudsecurityalliance.org/agentic/csa-research-note-nemoclaw-security-assessment-20260327/", date: 2026-03-27, confidence: medium}
  - {claim: "Single-agent, single-machine scope; no shared agent identity across sandboxes (vendor analysis by Tigera)", url: "https://www.tigera.io/?p=69229", date: 2026-07-15, confidence: medium}
  - {claim: "Cisco DefenseClaw sits on top of OpenShell and enforces MCP blocks through the sandbox allow-list", url: "https://blogs.cisco.com/ai/cisco-announces-defenseclaw", date: 2026-03-23, confidence: high}
---

# NVIDIA OpenShell

> Primary category: [agent-runtime-security](../categories/agent-runtime-security.md). Also listed in [ephemeral-environments](../categories/ephemeral-environments.md) and [trust-zone-segmentation](../categories/trust-zone-segmentation.md).

**One-liner**: Free, open-source software from NVIDIA that runs an AI agent inside a locked-down sandbox and checks everything the agent tries to do (files, processes, network calls, model calls, credential use) against a policy the operator writes. The checks run in a separate process the agent cannot reach.

**What it does**: OpenShell is a runtime that sits between an agent and the machine it runs on. You start an unmodified agent inside it (for example `openshell sandbox create -- claude`). From then on the agent can read files, install packages and call APIs only as far as a declarative YAML policy allows. NVIDIA names Claude Code, Codex, Cursor, OpenCode and OpenClaw as supported agents. The design has three parts:

- **Gateway**: the control plane. It creates and tracks sandboxes, holds policy and stored credentials ("providers"), and issues short-lived tokens bound to one sandbox.
- **Supervisor**: the trusted enforcement point, one per sandbox and outside it. It decides every outbound connection, resolves DNS, and adds real credentials to approved requests.
- **Sandbox**: where the untrusted agent runs. It reports what the agent is trying to do but, per the docs, "never makes policy decisions."

The policy covers four layers. The **filesystem** layer (readable and writable paths) uses Linux Landlock. The **process** layer runs the agent non-root with no capabilities and seccomp filters blocking `mount`, `ptrace`, `bpf` and similar calls. The **network** layer denies all egress by default. Each sandbox gets its own network namespace, and all traffic is forced through a CONNECT proxy that consults an **OPA** policy engine. Each allowed endpoint is tied to the specific binaries allowed to use it, with optional HTTP method/path inspection. The **inference** layer controls which model provider a call may reach, and originally included a "privacy router" meant to keep sensitive prompts on local models. Filesystem and process rules are fixed when the sandbox is created. Network and credential rules can change live. When the agent hits a block, it can propose a policy change, and a human approves or rejects it. Since 0.1.0 a **policy prover** checks each proposed change and holds risky ones for review, such as new credentialed reach, new HTTP methods, or cloud-metadata access.

**Naming / provenance**: The repo was created 2026-02-24, and NVIDIA announced OpenShell at **GTC on 2026-03-16** as part of the NVIDIA Agent Toolkit (successor to the NeMo Agent Toolkit). The launch blog's authors came to NVIDIA with its Gretel acquisition. **NemoClaw**, announced the same day, is a separate NVIDIA reference stack (also Apache-2.0) that installs and configures agents such as OpenClaw *inside* OpenShell and adds managed inference and onboarding. It is labelled alpha in its own README. **OpenClaw** is the third-party open-source always-on assistant that NemoClaw packages. OpenShell does not require NemoClaw. On **2026-09-28** NVIDIA rebranded the pairing of OpenShell with a new hardware watchdog, **Sentry** (runs on BlueField-4 DPUs, reference design, no ship date), as the **NVIDIA Open Agent Safety Platform**. Not to be confused with [nemo-guardrails](nemo-guardrails.md), NVIDIA's older guardrails library. That library filters prompts and responses *inside* the application. OpenShell confines the agent's *environment* and does not inspect content for injection.

**Ownership & viability**: `oss-vendor-backed`. NVIDIA employs the maintainers and controls the repo. The surrounding Open Secure AI Alliance (started by NVIDIA in July 2026, 120+ members) is governed by the Linux Foundation, but **OpenShell itself has not moved to a foundation**. Futurum's analysts flag this directly: until it does, "governance sits with NVIDIA." Viability signals are strong: about 16.8k GitHub stars and 1.8k forks (2026-10-20), very active commits, and a security bulletin process. NVIDIA says more than 100 organisations are building on the platform. The main risk is not abandonment but **steward risk**. NVIDIA has a hardware interest: the press release stresses tuning for its Vera CPUs, and Sentry needs BlueField-4. Feature priorities may follow NVIDIA's hardware roadmap.

**Positioning & differentiators**: Labelled `oss-default` in agent-runtime-security. It is the only open-source runtime in this category's shortlist, it is free, and most security vendors in the space announced integrations with it rather than competing with it (Cisco, CrowdStrike, Microsoft, Palo Alto Networks and others are named partners). Unlike the commercial vendors here, it is an enforcement substrate, not a detection product.
- **vs. [zenity](zenity.md), [operant-ai](operant-ai.md), [straiker](straiker.md) and similar runtime agent-security products:** those mostly *watch* agent behaviour, detect injection or risky actions, and alert or block in SaaS or in-cluster. OpenShell *confines* the agent at the OS and network layer and does no content or behavioural analysis. The CSA assessment rated its Evaluation & Monitoring coverage "Minimal". The two approaches are complementary, and partners are building exactly that pairing (see Integrations).
- **vs. agent sandboxes [daytona](daytona.md) / [modal](modal.md):** those sell hosted, disposable compute for agent code, billed per second, with egress allowlists as a feature. OpenShell is self-hosted software for running long-lived agents on your own laptops, servers or Kubernetes, with much finer policy: per-binary, per-HTTP-method rules, credential placeholders, and proved policy changes. It provides no compute.
- **vs. [docker-sandboxes](docker-sandboxes.md):** this is the closest peer. Docker's `sbx` also confines a coding agent on the developer's machine and controls egress, mounts and credentials from outside. Docker isolates with a microVM by default and sells a paid central-admin layer (Docker AI Governance). OpenShell defaults to kernel controls on a shared host kernel, with its microVM driver less mature. It has no commercial admin tier, but it offers finer per-binary and L7 policy and a policy prover.
- **vs. [docker-mcp-gateway](docker-mcp-gateway.md) and other [mcp-gateway](../categories/mcp-gateway.md) products:** an MCP gateway governs one protocol path. OpenShell governs every outbound connection from the sandbox. MCP traffic is subject to its network policy, but whether it parses MCP semantics is unclear (see Open questions).
- **Credential brokering is the distinctive control.** The agent only ever holds an opaque placeholder. The supervisor substitutes the real key only for requests to the host, port and path the policy authorises. So even a fully compromised agent cannot read or carry away the firm's API keys.

**Agent-security role: the lethal trifecta.** OpenShell attacks the trifecta (untrusted input, sensitive data, and external egress in one agent context) mainly on the **egress** and **sensitive-data** legs. Default-deny networking with per-binary allowlists closes most exfiltration paths. Credential placeholders keep secrets out of the agent's reach. Landlock limits which firm files the agent can read. It does **nothing about the untrusted-input leg**: per CSA, it "cannot prevent initial code execution" and has no prompt-injection detection. It also does not stop an agent from misusing access it was legitimately granted. If policy allows the agent to post to an internal API, an injected agent can post harmful content there. In zone terms ([trust-zone-segmentation](../categories/trust-zone-segmentation.md)), it is a practical way to build a red or yellow zone on a developer laptop or server. The policy file *is* the zone definition. That makes policy authoring the real work.

**Who should choose them / anti-fit**: Fits a firm that **runs its own autonomous or long-running agents on its own infrastructure**. Examples: quant-dev teams letting Claude Code or Codex work unattended on research repos; a platform team hosting always-on internal assistants; anyone who wants a self-hosted, auditable, no-licence-cost enforcement layer and has Linux engineers to write and review policies. It is also a natural base layer if you already use CrowdStrike, Cisco or Microsoft security tooling that plugs into it. **Anti-fit:** firms whose AI use is SaaS chatbots or vendor-hosted agents (nothing runs on your hosts to confine). Teams wanting a turnkey product with a vendor SLA, a support contract and a SOC 2 report (none exists). Buyers who need detection of prompt injection or misbehaviour rather than containment. And fleet-scale multi-agent deployments needing shared agent identity and cross-agent policy, which OpenShell does not provide (see gotchas).

**Known weaknesses / gotchas**:
- **Young code with a serious CVE history.** NVIDIA's 2026-08-25 bulletin fixed six OpenShell CVEs in v0.0.34, all reported by outside researchers. They include **CVE-2026-65093, a Linux sandbox escape (CVSS 9.9)**, a 9.9 provisioning-API input-filtering flaw, and **CVE-2026-65092, a path-traversal bypass of L7 REST network policy (8.5)**. NemoClaw had twelve more in the same bulletin. Patching cadence matters. Pin and track versions.
- **Shared-kernel isolation by default.** The Docker/Podman/Kubernetes drivers rely on Landlock, seccomp and namespaces on the host kernel. A microVM driver (libkrun) exists. Its runtime artifacts were still published as a "development build" prerelease (2026-05-06). If you need a hypervisor boundary, confirm the VM driver's support status.
- **Defaults are less strict than "deny-by-default" suggests.** Endpoints not on the list are denied. But L7 request rules default to **`audit`** (violations are logged and the traffic still goes through), and the extra filesystem policy defaults to **`best_effort`**. Each **approved endpoint permanently widens the running sandbox's policy** until the sandbox is recreated. Escape hatches (`tls: skip`, `allow_uninspected_credentials`, broad binary globs like `/**`) quietly disable key protections. Review policies for these.
- **The prover proves the policy, not your intent.** NVIDIA's own docs say a passing check "does not establish least privilege or semantic safety". Futurum: "the fence is where you drew it, not whether you drew it in the right place." Policies also tend to drift wider over time (CSA).
- **Single-sandbox scope.** Each sandbox enforces its own policy, with no shared agent identity and no view of other sandboxes (Tigera's point, a vendor with a competing fleet product). Agent-to-agent trust, behavioural drift and identity revocation are out of scope (CSA).
- **No overhead benchmarks published** (Futurum, 2026-09-29). Linux requirements: Landlock ABI 3 (kernel 6.2+). Kubernetes needs 1.33+, and user namespaces are off by default. GPU plus user-namespace compatibility is "unverified" per the docs. Windows support is via WSL 2 and labelled experimental.
- **Telemetry on by default.** Anonymous operational counts go to NVIDIA unless `OPENSHELL_TELEMETRY_ENABLED=false` is set on the gateway.

**Deployment & data handling**: **Self-hosted only.** It runs on Linux, macOS (Apple Silicon) or Windows/WSL 2, using Docker, Podman, a microVM, or Kubernetes via Helm charts. No NVIDIA-hosted service is involved. Agent code, files and credentials stay on the firm's hosts, hence `data_leaves_tenancy: "false"`. Two caveats: the default anonymous telemetry above, and inference traffic goes wherever your policy lets it (OpenShell routes model calls; it does not host models). It is **inline** for network traffic: every connection passes through the supervisor's proxy. That is what makes it enforce rather than observe, and it is also why the performance overhead question matters. Audit: the supervisor logs allow/deny decisions to the gateway, and the codebase includes OCSF-format logging. Export to SIEM is via partners (CrowdStrike, Cisco/Splunk). The docs warn that the sandbox "does not scrub application-level output", so logs may contain sensitive data.

**Integrations & partnerships**: Runtimes Docker, Podman, Kubernetes (Helm) and microVM. Agents Claude Code, Codex, Cursor, OpenCode, OpenClaw, plus Pi and Hermes per later coverage. Security partners, in order of how concrete the integration is:
- **Cisco DefenseClaw** (open source, announced 2026-03-23) sits on top of OpenShell. It scans skills and MCP servers before install and enforces blocks by editing the sandbox allow-list, with Splunk telemetry. See [cisco-ai-defense](cisco-ai-defense.md).
- **CrowdStrike** "Secure-by-Design AI Blueprint" (2026-03-16) connects Falcon to OpenShell for prompt/response/action monitoring and endpoint coverage of local agents. Coverage at the time framed it as an integration plan, not a GA product. See [crowdstrike](crowdstrike.md).
- **Salesforce:** Slack-based approval of agent permission requests.
- **SAP:** embedding OpenShell in the Joule Studio runtime.
- **Anthropic:** Claude Managed Agents integrate with OpenShell and BlueField.
- **Red Hat:** OpenShell on Red Hat AI Factory.
- Microsoft, Palo Alto Networks ([palo-alto-networks](palo-alto-networks.md)), Palantir and Trend Micro ([trend-micro](trend-micro.md)) are named as participants without described integrations.
- **Tigera** pitches its Lynx product as the fleet-identity layer around OpenShell.

**Compliance & FS traction**: No certifications. It is open-source software, so the buyer's own controls apply. **FS evidence is `claimed`:** NVIDIA's 2026-09-28 press release names **JPMorganChase** as "a financial services leader collaborating with NVIDIA on shared open-source agent safety technologies" and lists **Citi** among participants. No JPMorgan statement, deployment detail or case study is given, and Futurum notes that "reference deployments or third-party audits from regulated partners would carry more weight than the logos." Audit-relevant features include a deny/allow decision trail and human-approved, prover-checked policy changes. Both are useful evidence for model-risk or change-management reviews, but neither is packaged as compliance reporting. Hedge-fund-scale fit is good: it runs on a single laptop and needs no seat minimums.

**Commercial**: Free, Apache-2.0. No paid edition or NVIDIA support offering specific to OpenShell was found (2026-10-20). Whether it is covered by NVIDIA AI Enterprise support is unverified. The real costs are engineering time for policy authoring and review, plus patch management. Sentry requires BlueField-4 hardware.

## Open questions

- Is OpenShell covered by an NVIDIA AI Enterprise support subscription or any paid SLA?
- Production status of the microVM (libkrun) driver. Is it GA in 0.1.x, or still a development build?
- Does the network layer parse MCP (tool names, arguments), or treat MCP as generic HTTP? Coverage summaries claim MCP-aware inspection, while Futurum says MCP coverage is unclear. Not confirmed in primary docs.
- Performance overhead of the inline proxy and seccomp user-notification path. NVIDIA has published none.
- What JPMorganChase and Citi actually do with it (contributors, pilots, production?).
- Whether OpenShell will move to the Linux Foundation alongside the Open Secure AI Alliance.
- Exact content of default telemetry, and whether any prompt or path data is included.
- Status of the CrowdStrike Falcon integration: GA or still planned?
- Trend Micro's analysis piece ("What OpenShell gets right, what NemoClaw still can't fix") surfaced in search but returned 404 on 2026-10-20. Content not reviewed.

## Sources

- [Run Autonomous, Self-Evolving Agents More Safely with NVIDIA OpenShell (NVIDIA Technical Blog, 2026-03-16)](https://developer.nvidia.com/blog/run-autonomous-self-evolving-agents-more-safely-with-nvidia-openshell): fetched 2026-10-20. Supports: announce date, licence, launch architecture, supported agents. Confidence: high (vendor).
- [NVIDIA/OpenShell on GitHub](https://github.com/NVIDIA/OpenShell) and [releases](https://github.com/NVIDIA/OpenShell/releases): fetched 2026-10-20. Supports: repo creation date, stars, versions and dates, VM runtime, telemetry, platform support. Confidence: high.
- [OpenShell docs: architecture (v0.1.3)](https://docs.nvidia.com/openshell/v0.1.3/about/architecture.md) and [security best practices](https://docs.nvidia.com/openshell/security/best-practices.md): fetched 2026-10-20. Supports: isolation mechanism, OPA proxy, credential placeholders, defaults and footguns. Confidence: high (vendor docs).
- [NVIDIA Launches Open Agent Safety Platform (press release, 2026-09-28)](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Open-Agent-Safety-Platform-to-Secure-Agents-From-Testing-to-Deployment/default.aspx): fetched 2026-10-20. Supports: Sentry, partner roster and roles, JPMorganChase/Citi mentions, alliance governance. Confidence: high (vendor marketing for partner claims).
- [NVIDIA Security Bulletin: NemoClaw and OpenShell, August 2026 (bulletin 5872)](https://github.com/NVIDIA/product-security/tree/main/2026/5872): fetched 2026-10-20. Supports: CVEs, scores, affected/fixed versions. Confidence: high (primary).
- [NVIDIA Wants Agent Safety Enforced in Silicon (Futurum Group, 2026-09-29)](https://futurumgroup.com/?p=96053): fetched 2026-10-20. Supports: independent assessment and limitations. Confidence: medium (analyst opinion).
- [CSA research note: NemoClaw security assessment (draft, 2026-03-27)](https://labs.cloudsecurityalliance.org/agentic/csa-research-note-nemoclaw-security-assessment-20260327/): fetched 2026-10-20. Supports: isolation rating, scope gaps. Confidence: medium (draft).
- [NVIDIA OpenShell Secures the Agent. Who Governs the Fleet? (Tigera, 2026-07-15)](https://www.tigera.io/?p=69229): fetched 2026-10-20. Supports: single-sandbox scope critique. Confidence: medium (vendor with competing product).
- [Cisco announces DefenseClaw (Cisco blog, 2026-03-23)](https://blogs.cisco.com/ai/cisco-announces-defenseclaw): fetched 2026-10-20. Supports: DefenseClaw ↔ OpenShell relationship. Confidence: high.
- CrowdStrike Secure-by-Design AI Blueprint release (Business Wire, 2026-03-16), via search summary only. Supports: CrowdStrike integration scope. Confidence: medium.
- Cached: `raw/sources/2026-10-20--nvidia-openshell--github-repo-releases.md`, `raw/sources/2026-10-20--nvidia-openshell--docs-architecture-security.md`, `raw/sources/2026-10-20--nvidia-openshell--gtc-launch-and-partners.md`, `raw/sources/2026-10-20--nvidia-openshell--agent-safety-platform-pr.md`, `raw/sources/2026-10-20--nvidia-openshell--security-bulletin-aug-2026.md`, `raw/sources/2026-10-20--nvidia-openshell--independent-analysis.md`

## History

- [2026-10-20] Page created via wiki-create + wiki-research (user query on "NVIDIA OpenShell analysis"). Product slug chosen because OpenShell, not NVIDIA, is the shopping unit; cross-links [nemo-guardrails](nemo-guardrails.md).
