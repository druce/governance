---
title: GitGuardian
type: vendor
name: GitGuardian
slug: gitguardian
aka: [ggshield, ggscout, GitGuardian Secrets Detection, GitGuardian NHI Governance, GitGuardian MCP server (ggmcp)]
primary_category: software-supply-chain
also_listed_in: [non-human-identity]
website: https://www.gitguardian.com
founded: 2017
hq: Paris, France / New York, USA
ownership_state: independent
owner: null
ownership_note: "Private, VC-backed. $50M Series C led by Insight Partners (2026-02-11), following a $44M Series B led by Eurazeo (2021-12-07). Other investors: Balderton, BPI, Fly Ventures, Sapphire, Quadrille. No acquisition found as of 2026-10-26."
acquisition: {announced: null, closed: null, price: null}
funding_total: "~$106M (derived: $56M through Series B + $50M Series C; not a company-stated total)"
last_funding: "Series C, $50M, 2026-02-11 (Insight Partners lead)"
market_position: {software-supply-chain: niche-specialist, non-human-identity: challenger}
deployment_model: [saas, self-hosted, on-prem]
form_factor: [platform, api, agent]
data_leaves_tenancy: partial
integrations: [github, gitlab, bitbucket, azure-devops, slack, jira, confluence, claude-code, cursor, github-copilot, codex, vscode, hashicorp-vault]
mcp_support: server
certifications: []
pricing_model: "Per-developer subscription. Free tier for small teams and the open-source ggshield CLI; enterprise and NHI Governance are quote-based."
fs_traction: claimed
target_customer: mid-market to large enterprise engineering and security teams; public sector (air-gapped option)
last_verified: 2026-10-26
verify_after: null
tags: [secrets-scanning, secrets-detection, honeytokens, nhi-governance, ai-coding-agents, mcp, ggshield, appsec]
sources:
  - {claim: "$50M Series C, Insight Partners lead, 2026-02-11; metrics; named customers incl. ING", url: "https://blog.gitguardian.com/series-c-pr/", date: 2026-02-11, confidence: high}
  - {claim: "$44M Series B led by Eurazeo, $56M total; founded 2017 by Thomas and Fourrier", url: "https://www.securityweek.com/gitguardian-raises-44-million-create-code-security-platform", date: 2021-12-07, confidence: high}
  - {claim: "NHI Governance scope: inventory, rotation, over-privilege, ggscout", url: "https://www.gitguardian.com/nhi-governance", date: 2026-10-26, confidence: medium}
  - {claim: "AI Hooks for Claude Code, Cursor, Copilot CLI, VS Code, Codex, Mistral Vibe; agent and MCP inventory", url: "https://docs.gitguardian.com/releases/saas/2026/09/07/changelog", date: 2026-09-07, confidence: medium}
  - {claim: "ggshield MIT, ggmcp MIT MCP server (created 2025-05-14)", url: "https://github.com/GitGuardian/ggmcp", date: 2026-10-26, confidence: high}
  - {claim: "Air-gapped on-prem deployment option", url: "https://gitguardian.com/industries/public-sector", date: 2026-10-26, confidence: medium}
---

# GitGuardian

> Primary category: [software-supply-chain](../categories/software-supply-chain.md). Also listed in [non-human-identity](../categories/non-human-identity.md).

**One-liner**: The best-known specialist in **secrets detection**. It finds API keys, tokens and passwords leaked into code, git history, CI logs and collaboration tools (Slack, Jira, Confluence). It has extended into **NHI governance** (an inventory of machine credentials and their owners and permissions) and into scanning what **AI coding agents** read and write.

**What it does**:
- **Secrets Detection.** Scans internal repositories, including full git history, CI pipelines, containers and collaboration sources for 550+ secret types (vendor figure), with validity checks and a remediation workflow. The **ggshield** CLI (MIT licence) runs as a pre-commit hook, CI step or GitHub Action.
- **Public Monitoring.** Watches public GitHub for your organisation's secrets leaked by employees or contractors.
- **Honeytokens.** Decoy credentials that alert when used.
- **NHI Governance** (launched around April 2025, per a third-party profile).
  - **Inventory:** a central list of the secrets machine identities use, *including ones outside your vault*, with consumers, last rotation date, permissions and owners. A collector (**ggscout**) hashes secret metadata inside your environment before sending it.
  - **Lifecycle:** flags stale, unused or over-privileged secrets, semi-automates rotation and supports revocation.
- **AI-agent coverage** (September 2026 changelog). "AI Hooks" scan **prompts and tool calls** in Claude Code, Cursor, Copilot CLI, VS Code, Codex and Mistral Vibe, configured with one ggshield command. There is also an **inventory of agents and MCP servers** on developer machines. GitGuardian claims developers using AI coding tools leak secrets at about twice the baseline rate (vendor research). The open-source **ggmcp** MCP server (MIT, May 2025) lets a coding agent call GitGuardian scanning directly.

**Naming / provenance**: Founded **2017** in Paris by **Jérémy Thomas** and **Eric Fourrier** (CEO). It started as a public-GitHub leak alerting service and became a commercial platform. GitGuardian calls itself the "most installed GitHub application" (vendor claim). Dual HQ in Paris and New York; over 80% of new ARR comes from North America (vendor).

**Ownership & viability**: `independent`, VC-backed.

| Date | Round | Lead | Amount |
|---|---|---|---|
| 2021-12-07 | Series B | Eurazeo (with Sapphire, Balderton, BPI, Fly Ventures) | $44M ($56M total) |
| 2026-02-11 | Series C | Insight Partners (with Quadrille; existing investors followed) | $50M |

Total is roughly **$106M** (derived, not company-stated). The Series C was explicitly earmarked for AI-agent security and enterprise NHI governance. Viability is solid, with fresh capital and vendor-claimed 5x year-on-year growth in remediated exposures.

**Acquisition-risk note:** secrets and NHI startups are being bought. SailPoint bought [entro-security](entro-security.md) (closed 2026-06-29), Palo Alto Networks bought [cyberark](cyberark.md) (closed 2026-02-11) and Cisco bought [astrix-security](astrix-security.md) (closed 2026-06-29), per those wiki pages. GitGuardian is a plausible target for an AppSec platform, a code host or an identity vendor. Customers would most likely see it folded into a broader suite; the open-source ggshield gives some continuity.

**Positioning & differentiators**: `niche-specialist` in software-supply-chain, as the leading specialist for secrets detection rather than a full AppSec suite. `challenger` in non-human-identity: it entered from the detection side against dedicated NHI platforms.
- **Vs. built-in secret scanning** ([github-advanced-security](github-advanced-security.md), [gitlab](gitlab.md)):
  - GitGuardian covers **multiple SCMs plus Slack, Jira and Confluence**, scans full history, and offers honeytokens, public-leak monitoring and a cross-source incident workflow.
  - GitHub's push protection is "free" if you already pay for GitHub Advanced Security and only use GitHub.
- **Vs. [truffle-security](truffle-security.md) (TruffleHog):** the most common head-to-head. TruffleHog's strengths are its open-source scanner and **live verification** of whether a key works, plus permission analysis of a leaked key. GitGuardian's are a more mature commercial workflow, NHI inventory and governance, and AI-agent hooks.
- **Vs. broad AppSec** ([semgrep](semgrep.md), [aikido-security](aikido-security.md), [snyk](snyk.md)): these include secrets scanning as one feature. GitGuardian is deeper on secrets but does not do SAST or SCA.
- **Vs. NHI platforms** ([astrix-security](astrix-security.md), [entro-security](entro-security.md), [oasis-security](oasis-security.md), [token-security](token-security.md)): GitGuardian builds its NHI inventory from **where secrets leak and are used**. Those platforms start from identity-provider and SaaS-integration discovery, so GitGuardian is less complete on OAuth grants and SaaS-to-SaaS connections.

**Who should choose them / anti-fit**: Fits a fund with **real in-house engineering** that has more than one code host or heavy Slack and Confluence use, wants leaked-credential detection plus remediation workflow, and is rolling out coding agents. The AI Hooks are one of the few products that scan what Claude Code or Cursor sends and runs, specifically for secrets. Also fits as an NHI starting point for a team without budget for a separate NHI platform. **Anti-fit:** a small team entirely on GitHub that already pays for Advanced Security, where native push protection may be enough. Also anyone wanting SAST and SCA too (buy an AppSec platform), or full SaaS and OAuth NHI governance (buy a dedicated NHI platform).

**Known weaknesses / gotchas**:
- **NHI governance is a newer extension** of a detection product. Its inventory depends on secrets GitGuardian can see; non-secret machine identities such as workload identity federation and OAuth apps are covered less directly.
- **Certifications not confirmed.** Only an older "SOC 2 Type I" announcement was found. Request a current SOC 2 Type II report and ISO 27001 status.
- **Detection volume.** Scanning full git history across many sources produces large initial backlogs; plan triage time.
- AI-agent hooks run on developer machines and depend on per-machine rollout of ggshield.

**Deployment & data handling**: SaaS by default. A **self-hosted, including air-gapped on-prem,** edition exists (public-sector page). In SaaS mode, scanned content is sent to GitGuardian for detection. NHI collection through ggscout **hashes** secret metadata in your environment before upload. Hence `data_leaves_tenancy: partial`: depends on edition and module. Detection is out-of-band, except for pre-commit and push-time hooks, which add seconds to developer workflows rather than runtime latency.

**Integrations & partnerships**: GitHub, GitLab, Bitbucket and Azure DevOps; CI systems; Slack, Jira and Confluence as scan sources; secrets managers for NHI context (HashiCorp Vault and others; the vendor links a list but this page did not enumerate it); AI coding tools (Claude Code, Cursor, Copilot CLI, VS Code, Codex, Mistral Vibe). **MCP:** ships an MCP server (ggmcp) and inventories MCP servers on developer machines.

**Compliance & FS traction**: Named customers include **ING** (the only FS name found), Snowflake, BASF, Bouygues Telecom and Deutsche Telekom. 115k+ developers covered at enterprise customers (vendor). No named hedge-fund customers. Hedge-fund fit: **medium**. Good for funds with sizeable dev teams; overkill for a SaaS-only shop.

**Commercial**: Per-developer pricing. Free tier for small teams; ggshield is open source (MIT). Enterprise, self-hosted and NHI Governance are quote-based.

## Open questions

- Current SOC 2 Type II / ISO 27001 status.
- Company-stated total funding and headcount after the Series C.
- NHI Governance: which secrets managers and cloud identity providers are integrated, and whether non-secret identities (OAuth apps, workload identity) are inventoried.
- Whether AI Hooks can block (preventive) or only alert on secrets in prompts and tool calls.
- Named FS / hedge-fund customers beyond ING.

## Sources

- [GitGuardian Raises $50M Series C (GitGuardian, 2026-02-11)](https://blog.gitguardian.com/series-c-pr/), fetched 2026-10-26. Supports: round, investors, metrics, named customers, NHI and AI-agent strategy. Confidence: high (vendor primary).
- [GitGuardian Raises $44 Million (SecurityWeek, 2021-12-07)](https://www.securityweek.com/gitguardian-raises-44-million-create-code-security-platform), search snapshot 2026-10-26. Supports: Series B, $56M total, founders, 2017 founding. Confidence: high.
- [GitGuardian NHI Governance](https://www.gitguardian.com/nhi-governance), fetched 2026-10-26. Supports: NHI inventory, rotation, ggscout hashing. Confidence: medium (vendor).
- [GitGuardian SaaS changelog 2026-09-07](https://docs.gitguardian.com/releases/saas/2026/09/07/changelog), search snapshot 2026-10-26. Supports: AI Hooks coverage, agent and MCP inventory, 2x leak-rate claim. Confidence: medium.
- [GitGuardian public sector](https://gitguardian.com/industries/public-sector), search snapshot 2026-10-26. Supports: air-gapped on-prem option. Confidence: medium.
- [GitGuardian/ggmcp](https://github.com/GitGuardian/ggmcp) and [GitGuardian/ggshield](https://github.com/GitGuardian/ggshield) (GitHub API), fetched 2026-10-26. Supports: MIT licences, MCP server, activity. Confidence: high.
- Cached: `raw/sources/2026-10-26--gitguardian--funding-nhi-ai-hooks.md`

## History

- [2026-10-26] Page created and researched in one pass. Primary software-supply-chain, because secrets scanning is described there. Cross-listed non-human-identity because GitGuardian sells a distinct NHI Governance product (inventory, rotation, ownership) and framed its 2026 Series C around it. Considered and rejected secrets-management: it detects and governs secrets but does not vault them.
