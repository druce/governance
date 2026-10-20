---
title: agentregistry (Solo.io)
type: vendor
name: agentregistry (Solo.io)
slug: agentregistry
aka: [agent registry, Solo Enterprise for agentregistry, arctl]
primary_category: mcp-gateway
also_listed_in: [ai-spm]
website: https://github.com/agentregistry-dev/agentregistry
founded: 2025
hq: Cambridge, MA, USA (Solo.io)
ownership_state: oss-vendor-backed
owner: Solo.io
ownership_note: Apache-2.0 open-source project created by Solo.io (announced 2025-11-12). CNCF Sandbox application (cncf/sandbox#477) filed 2026-03-25; TOC vote passed 2026-09-29, but the contribution agreement was still unsigned and CNCF onboarding not started as of 2026-10-20. Solo.io sells a commercial distribution, Solo Enterprise for agentregistry. Solo.io is private and VC-backed (last disclosed round $135M Series C, October 2021, $1B valuation).
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$171.5M (at parent Solo.io, through 2021)
last_funding: Series C, $135M, 2021-10 (Solo.io; led by Altimeter)
market_position: {mcp-gateway: niche-specialist, ai-spm: niche-specialist}
deployment_model: [self-hosted, on-prem]
form_factor: [platform, api]
data_leaves_tenancy: "false"
integrations: [kagent, agentgateway, aws-bedrock-agentcore, azure-ai-foundry, microsoft-copilot-studio, oidc, keycloak, okta, auth0, opentelemetry, kubernetes]
mcp_support: unverified
certifications: []
pricing_model: oss+support
fs_traction: unverified
target_customer: Platform-engineering teams on Kubernetes that want one approved catalog of agents, MCP servers and skills
last_verified: 2026-10-20
verify_after: 2027-01-20
tags: [open-source, cncf, mcp-registry, agent-registry, skills, kubernetes, solo-io]
sources:
  - {claim: "Apache-2.0; repo created 2025-10-27; ~526 stars; v0.4.0 released 2026-08-03; README: curate and approve agents, servers and skills before company-wide deployment", url: "https://github.com/agentregistry-dev/agentregistry", date: 2026-10-20, confidence: high}
  - {claim: "CNCF Sandbox application filed 2026-03-25; TOC vote passed 2026-09-29 (9 for, 0 against); contribution agreement unsigned, onboarding pending as of 2026-10-20", url: "https://github.com/cncf/sandbox/issues/477", date: 2026-10-20, confidence: high}
  - {claim: "Launched 2025-11-12 at KubeCon NA as a curated open-source registry for AI artifacts, with Agent Skills support", url: "https://www.solo.io/press-releases/agent-skills-kubernetes-ecosystem", date: 2025-11-12, confidence: high}
  - {claim: "Enterprise edition: OIDC-only access, role-based AccessPolicy, default-deny for non-admins, admin approval queue for staged changes, runtime authorization via agentgateway, read-only discovery of agents in Bedrock AgentCore / Azure AI Foundry / Copilot Studio; air-gapped install; latest 2026.9.0", url: "https://docs.solo.io/agentregistry/latest/security/overview/", date: 2026-10-20, confidence: high}
  - {claim: "Catalogs agents, MCP servers, skills, prompts, plugins, models; sits on top of npm/PyPI/OCI registries", url: "https://www.solo.io/blog/understanding-the-agentregistry-project-and-the-problems-it-solves", date: 2026-08-20, confidence: high}
  - {claim: "Solo.io $135M Series C led by Altimeter at $1B valuation (October 2021); total $171.5M", url: "https://www.gunder.com/news/altimeter-capital-leads-135m-series-c-financing-of-solo-io", date: 2026-10-20, confidence: high}
---

# agentregistry (Solo.io)

> Primary category: [mcp-gateway](../categories/mcp-gateway.md). Also listed in [ai-spm](../categories/ai-spm.md).

**One-liner** — An open-source, self-hosted catalog where a platform team lists the agents, MCP servers and skills it has approved, so developers pull from one curated list instead of installing whatever they find. Solo.io's commercial edition adds sign-in through the firm's IdP, role-based permissions, an admin approval queue and a read-only inventory of agents already running in AWS, Azure and Copilot Studio.

**What it does** — agentregistry is a registry of *metadata*, not a store of binaries. The project describes it as sitting "on top of" npm, PyPI and OCI container registries: an entry points at the package or image and records the version, description and trust metadata the platform team wants recorded. Entries cover six artifact types: agents, MCP servers (built locally and published, or registered remotely by URL), skills, prompts, plugins and models. A CLI, `arctl`, packages, publishes and deploys artifacts to a target runtime. Solo.io's own pitch is the problem statement "nobody knows which ones are approved or how to run them consistently" (Solo blog, 2026-08-20).

The open-source and commercial editions differ in ways that matter for governance:

- **Open source (Apache-2.0).** The catalog, versioning, search, the CLI and deployment to Kubernetes via [kagent](#related-solo-io-projects). The README promises curation and approval "before company-wide deployment", but it delegates enforcement on MCP traffic (identity checks, JWT validation) to [agentgateway](agentgateway.md). Solo's "OSS vs. Enterprise" comparison page returned 404 on 2026-10-20, so exactly which controls are open source is **unverified**.
- **Solo Enterprise for agentregistry** (docs version 2026.9.0 as of 2026-10-20). Every request needs a JWT from an external OIDC provider; Keycloak, Okta and Auth0 are the documented examples. Users are **denied by default**: a role gets nothing until an `AccessPolicy` grants it actions such as read, publish, deploy or invoke. The `admin` role bypasses all policy. When **approval mode** is on, any create, update or delete by a non-admin is staged and invisible to others until an admin approves it. **Runtime authorization** limits which MCP tools and agents a deployed agent may call. It is enforced at an agentgateway waypoint for kagent (and needs Solo Enterprise for Istio) or at a managed gateway for AWS Bedrock AgentCore. **Discovery** connects read-only to AWS Bedrock AgentCore, Azure AI Foundry, Microsoft Copilot Studio and kagent and lists agents nobody registered. OpenTelemetry traces and MCP-aware gateway logs (session, tool name, resource) feed observability. The docs also have pages on audit logs and on SBOM/CVE scans, which were not read for this page.

**Naming / provenance** — Solo.io announced it on **2025-11-12** at KubeCon NA (Atlanta) as its third open-source agentic-infrastructure project, after kagent (March 2025) and agentgateway. The repo was created 2025-10-27. Do not confuse it with the community-run **official MCP Registry** (registry.modelcontextprotocol.io), a public index of MCP servers. Solo positions agentregistry as the private, governed layer an enterprise needs beyond that index. Also do not confuse it with **Apicurio Registry**, a separate CNCF Sandbox project that added AI-agent registry features in 2026.

## Ownership & viability

`oss-vendor-backed`, owner Solo.io. The foundation status is easy to get wrong:

- Solo.io said on **2026-03-25** (KubeCon EU, Amsterdam) that it "is contributing" agentregistry to the CNCF. Trade coverage then described it as already a CNCF Sandbox project (SD Times, 2026-04-17). **The primary record disagrees.** The CNCF sandbox application ([cncf/sandbox#477](https://github.com/cncf/sandbox/issues/477)) was opened that day, and the TOC vote **passed only on 2026-09-29** (9 in favour, 0 against). As of 2026-10-20 the issue is still open and labelled `contribution-agreement/unsigned`. CNCF says onboarding cannot begin until that agreement is signed, and the project has no page on cncf.io yet. Reclassify to `oss-foundation` once onboarding completes (`verify_after` 2027-01-20).
- **Maturity is early.** About 526 GitHub stars. The latest OSS release is v0.4.0 (2026-08-03), still pre-1.0. By comparison, sibling kagent has ~4,060 stars and agentgateway ~3.6k (at 2026-06).
- **Solo.io** was founded in 2017 by CEO Idit Levine and is based in Cambridge, MA. Its last disclosed round was a **$135M Series C in October 2021**, led by Altimeter at a $1B valuation, bringing total funding to about $171.5M. Searches on 2026-10-20 found no 2025–2026 funding round, acquisition or layoffs. Solo's revenue base is service mesh and API gateway (Gloo, Istio Ambient, kgateway). The agentic line is newer, and how much revenue it brings is not disclosed.
- **Steward risk.** Contributors outside Solo were not counted for this project. CNCF governance would reduce dependence on one company, but it has not started. If Solo.io were acquired or changed priorities, a pre-1.0 project with ~500 stars could stall. The Apache-2.0 licence lets anyone fork it.

## Positioning & differentiators

Labelled `niche-specialist` in both categories. It is a catalog-and-approval component, built for Kubernetes shops, with policy enforcement handed off to a separate gateway. Most peers here sell a full gateway or a full AI-inventory product.

- **vs. [agentgateway](agentgateway.md):** they work as a pair. agentgateway is the inline proxy that enforces policy on each MCP, A2A or LLM call. agentregistry is the list of what is approved and where it runs. In Solo's enterprise stack, runtime authorization rules written in the registry are enforced by agentgateway.
- **vs. [runlayer](runlayer.md):** both keep an "approved catalog of MCP servers and skills". Runlayer is a commercial SaaS-or-self-hosted product aimed at AI *clients* (Claude, Cursor, ChatGPT), with tool-call scanning and shadow-AI discovery. agentregistry is open source and Kubernetes-first, and it is aimed at agents the firm *deploys* to runtimes.
- **vs. [ibm-contextforge](ibm-contextforge.md), [obot](obot.md), [docker-mcp-gateway](docker-mcp-gateway.md):** each combines an MCP catalog with its own gateway. agentregistry keeps the registry separate and is the only one of these that also covers skills, prompts and agents as first-class entries.
- **vs. AI-SPM products ([noma-security](noma-security.md), [zenity](zenity.md), [wiz](wiz.md)):** the enterprise edition's read-only discovery of agents in Bedrock AgentCore, Azure AI Foundry and Copilot Studio overlaps their inventory feature. It does not assess posture or misconfiguration. It only lists what exists.

**Who should choose it / anti-fit** — It fits a firm with a real platform-engineering team that already runs Kubernetes, builds its own agents, and wants a self-hosted, open-source source of truth for which MCP servers and skills are allowed. It fits best alongside agentgateway and kagent, or as a way to inventory agents spread across AWS and Azure. **Anti-fit:** a fund whose AI use is vendor assistants and coding tools. It has nothing to deploy and no Kubernetes estate, and would get more from a managed MCP gateway or the IdP it already has. Also anti-fit: anyone who needs the governance controls in the free edition, because the approval queue, RBAC and discovery are documented only for the commercial product.

**Known weaknesses / gotchas** —
- **Governance is mostly in the paid edition.** Treat "curated, trusted registry" in OSS marketing as a design goal. Confirm which controls run without a Solo licence.
- **The approval model is basic.** An admin approves or does not, and admins bypass every policy. No multi-step approval chain, separation of duties or automated trust scoring was found.
- **Runtime enforcement depends on the rest of Solo's stack.** Policies for kagent agents require Solo Enterprise for Istio (ambient mesh) and agentgateway. Buying the registry alone does not enforce them.
- **CNCF status is often overstated** in 2026 press (see Ownership).

## Deployment & data handling

Self-hosted only: Helm on Kubernetes (EKS documented), with air-gapped installation documented and a bring-your-own PostgreSQL option. No Solo-hosted SaaS edition was found. Registry metadata, audit data and traces therefore stay in the firm's own infrastructure (`data_leaves_tenancy: "false"`). This assumes the OTel export target is in-house too. The discovery connectors make outbound read calls to AWS, Azure and Microsoft 365 APIs. The registry is **out-of-band**: it is not in the request path, so it adds no latency to agent calls. Inline enforcement is agentgateway's job.

## Integrations & partnerships

Runtimes: [kagent](#related-solo-io-projects), AWS Bedrock AgentCore, Azure AI Foundry, Microsoft Copilot Studio, and agentgateway as a remote MCP gateway. IdPs: any OIDC provider (Keycloak, Okta and Auth0 documented; Entra ID presumably works through OIDC but was not seen in docs). Telemetry: OpenTelemetry. Whether agentregistry exposes its own MCP server (so agents can query the catalog) was not confirmed, so `mcp_support` stays `unverified`. The 2026-08-07 Broadcom/VMware Cloud Foundation validation covered agentgateway and kagent, not agentregistry. Microsoft, Amazon and Oracle are named as contributors to Solo's agentic projects, not as partners for this product.

## Compliance & FS traction

No certifications apply to self-hosted OSS. Solo.io's own SOC 2 or ISO status was not checked. Solo says kagent is "trusted by leading retail, financial services, and telecommunications enterprises" (press release, 2026-05-07), but it names no customers, and no agentregistry customers at all were found. `fs_traction: unverified`.

## Commercial

The OSS core is free (Apache-2.0). Solo Enterprise for agentregistry is a contact-sales subscription with enterprise support. **No pricing published** as of 2026-10-20. Expect it to be sold bundled with Solo Enterprise for kagent, agentgateway and Istio.

## Related Solo.io projects

These were researched 2026-10-20 and have no pages of their own:

- **kagent** — Kubernetes-native framework and runtime for running AI agents as CRDs. CNCF Sandbox (accepted 2025-05-22), Apache-2.0, ~4,060 stars, latest stable v0.10.3 (2026-10-02) with v1.0 alphas shipping. It supports MCP tools, A2A, per-tool human-approval (`requireApproval`) and OpenTelemetry tracing. Solo Enterprise for kagent (announced 2025-09-15) adds on-behalf-of identity and policy, an AgentOps tracing UI, multicluster federation and FIPS 140-2 builds. NVIDIA NemoClaw/OpenClaw assistants have been supported since 2026-05-07. No page, because no current category fits an agent *runtime* (see the open questions below).
- **agentevals** — Apache-2.0 agent evaluation harness launched 2026-03-25 (~166 stars). It scores OpenTelemetry traces against golden eval sets (trajectory match, LLM-as-judge) and has a CLI, UI and MCP server. It fits [llm-observability](../categories/llm-observability.md) but is too young and small for a page today.
- **[agentgateway](agentgateway.md)** — the inline LLM/MCP/A2A proxy, under the Linux Foundation's AAIF.

## Open questions

- Exact OSS-vs-Enterprise feature split (the comparison page 404'd on 2026-10-20). Is the approval queue or any RBAC in OSS?
- When the CNCF contribution agreement is signed and onboarding completes. Does the project then move to a neutral GitHub org?
- Contents of the "SBOMs and CVE scans" and "Audit logs" doc pages. Does the registry scan artifacts it lists, or only publish Solo's own SBOMs?
- Does agentregistry expose an MCP server or an official-MCP-Registry-compatible API for clients?
- Contributor diversity outside Solo.io.
- Enterprise pricing, and whether it is sold standalone or only bundled.
- Any named customers, FS or otherwise; Solo.io's own SOC 2/ISO status.
- Solo.io funding since 2021, and current headcount.

## Sources

- [agentregistry on GitHub](https://github.com/agentregistry-dev/agentregistry) (plus GitHub API) — fetched 2026-10-20 — supports: licence, stars, releases, OSS feature claims; confidence: high
- [cncf/sandbox#477 — [Sandbox] agentregistry](https://github.com/cncf/sandbox/issues/477) — fetched 2026-10-20 — supports: application date, TOC vote result 2026-09-29, unsigned contribution agreement; confidence: high (primary record)
- [Solo.io press release: Agent Skills / agentregistry launch](https://www.solo.io/press-releases/agent-skills-kubernetes-ecosystem) — 2025-11-12, fetched 2026-10-20 — supports: launch date, positioning; confidence: high (vendor)
- [Solo.io blog: Understanding the agentregistry project](https://www.solo.io/blog/understanding-the-agentregistry-project-and-the-problems-it-solves) — 2026-08-20 — supports: artifact types, "sits on top of" package registries, enterprise runtimes; confidence: high (vendor)
- [Solo Enterprise for agentregistry docs](https://docs.solo.io/agentregistry/latest/), [concepts](https://docs.solo.io/agentregistry/latest/about/concepts/), [security overview](https://docs.solo.io/agentregistry/latest/security/overview/) — fetched 2026-10-20 — supports: OIDC/RBAC, approval mode, runtime authorization, discovery, air-gap install; confidence: high (vendor docs)
- [Solo.io press release: agentevals and agentregistry CNCF contribution](https://solo.io/press-releases/introducing-new-agentic-open-source-project-agentevals) — 2026-03-25 — supports: contribution announcement, agentevals; confidence: high (vendor)
- [SD Times: Solo open-source projects address challenges of agentic AI](https://sdtimes.com/ai/solo-open-source-projects-address-challenges-of-agentic-ai/) — 2026-04-17 — supports: (premature) sandbox claim, shown here as superseded; confidence: low on that point
- [Gunderson: Altimeter leads $135M Series C of Solo.io](https://www.gunder.com/news/altimeter-capital-leads-135m-series-c-financing-of-solo-io) — 2021-10 — supports: parent funding; confidence: high
- [CNCF kagent project page](https://www.cncf.io/projects/kagent/) — fetched 2026-10-20 — supports: kagent Sandbox acceptance 2025-05-22; confidence: high
- Cached: `raw/sources/2026-10-20--agentregistry--repo-cncf-docs.md`, `raw/sources/2026-10-20--kagent--cncf-repo-enterprise.md`, `raw/sources/2026-10-20--solo-io--company-agentevals.md`

## History

- [2026-10-20] Page created via wiki-create + wiki-research. User asked whether Solo.io kagent/agentregistry were covered. agentregistry was given its own page under mcp-gateway (cross-listed ai-spm). kagent and agentevals were summarised here rather than paged. The CNCF status was corrected against the primary sandbox record: the vote passed 2026-09-29 and onboarding is pending.
