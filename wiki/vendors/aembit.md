---
type: vendor
name: Aembit
slug: aembit
categories: [non-human-identity]
layer: foundation
aliases: [Aembit Workload IAM]
website: "https://aembit.io"
founded: 2021
hq: Silver Spring, Maryland, USA
ownership: independent
ownership_detail: Venture-backed and independent as of 2026-06; no acquisition found. Last round Series A (2024-09).
ownership_confidence: high
funding_total: ~$45M (cumulative, per vendor + SecurityWeek, as of 2024-09)
last_funding: Series A, $25M, 2024-09-12 (led by Acrew Capital)
deployment: [saas, self-hosted, sdk]
target_customer: enterprise; distributed/cloud-native engineering orgs
hedge_fund_fit: low
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [non-human-identity, workload-iam, secretless, agent-identity, mcp, nhi]
---

# Aembit

> "Workload IAM" — secretless, policy-based, just-in-time access for workloads (and now AI
> agents) to the APIs, SaaS, and data they call, so credentials are never hardcoded or stored.

**One-liner** — A non-human identity platform that issues short-lived, policy-scoped credentials
to workloads and AI agents at request time, so apps stop hardcoding secrets to reach the services
they depend on.

**Categories** — [non-human-identity](../categories/non-human-identity.md)

## What it does

Aembit sells an access-management approach to non-human identity (NHI). Where most NHI vendors
start with discovery and posture — find every service account, token, and API key and tell you
which are risky — Aembit starts at the access decision itself. Its policy engine sits between a
workload (a service, a container, a CI job, an AI agent) and the resource it wants to reach (a
database, a SaaS API, another internal service), and it brokers that access: it cryptographically
attests the calling workload's identity, checks policy and posture, and then delivers a short-lived
credential *just-in-time, per task*. The workload never stores or shares a long-lived secret.

The pitch is that this removes the root cause of most NHI incidents — hardcoded keys, sprawling
service-account secrets, over-permissioned tokens that never rotate — rather than just inventorying
them after the fact. Capabilities include workload attestation, ephemeral/secretless credential
issuance, least-privilege policy, and centralized auditing of every machine-to-machine access.

## Where it sits in the stack

Primary category: [non-human-identity](../categories/non-human-identity.md) (Foundation layer). Aembit is the "access management"
pole of NHI, as distinct from the "posture/discovery/governance" pole occupied by [oasis-security](oasis-security.md),
[token-security](token-security.md), [astrix-security](astrix-security.md), and [clutch-security](clutch-security.md). In lethal-trifecta terms it works
the **sensitive-data** and **egress** legs: by gating which workload/agent can reach which resource,
with short-lived scoped credentials, it constrains an agent's ability to reach sensitive data and to
exfiltrate via over-broad service-to-service access. It does not inspect prompts or untrusted input.
It lives at the boundary between trust zones — it is the broker that decides whether a workload in
one zone may call a resource in another.

## Deployment & architecture

- **SaaS control plane** — Aembit's policy/credential service is delivered as a managed cloud
  service; for agentic AI this includes an **MCP Authorization Server** implementing the OAuth 2.1
  authorization-code flow and integrating with existing IdPs (Okta, Microsoft Entra/Azure AD,
  Google).
- **Edge enforcement component** — a customer-deployed gateway/agent (for the agentic product, an
  **MCP Identity Gateway** that runs as a Linux VM) validates tokens and enforces policy on every
  request, performing real-time credential exchange so the workload/agent "never holds direct
  credentials." For classic workloads, Aembit deploys an edge agent (e.g., sidecar/host) that
  intercepts the workload's outbound calls and injects the just-in-time credential.
- **Integrations** — IdPs for the human side of identity, secrets managers, and the target SaaS/API
  surfaces; for agents, it secures **Claude** and **Microsoft Copilot Studio** agents over MCP.
- **Blended Identity** — its access model evaluates the AI agent's identity *and* the human
  operating it together in a single policy decision at request time ("is this user, via this agent,
  allowed to reach this resource right now?"), with per-user credential isolation per session.

## Positioning & differentiators

Aembit's differentiator is that it is *enforcement-first*, not inventory-first. [oasis-security](oasis-security.md),
[token-security](token-security.md), [astrix-security](astrix-security.md), and [clutch-security](clutch-security.md) largely lead with discovering NHIs,
mapping their entitlements and ownership, scoring risk, and helping rotate/clean up — a posture and
governance motion that overlays existing identity providers and secrets stores. Aembit instead
inserts itself in the access path and *brokers* the credential, aiming to make long-lived secrets
unnecessary in the first place. That makes its closest conceptual neighbor the workload-identity
/ machine-auth lineage (SPIFFE/SPIRE, and the secretless side of [cyberark](cyberark.md)'s machine-identity /
Conjur portfolio) rather than the NHI posture startups. It also moved early and visibly on **agent
identity / MCP**, shipping GA "IAM for Agentic AI" in April 2026 and MCP governance for Copilot
Studio agents at Identiverse in June 2026.

Tradeoff: enforcement-first means deploying Aembit in the access path (edge gateway/agent) and
modeling policies, which is more invasive than read-only posture tools — higher value if you adopt
it, more integration work to stand up.

## Ownership, funding & M&A

Independent and venture-backed. Founded **2021**, HQ **Silver Spring, Maryland**. Co-founders
**David Goldschlag** (CEO) and **Kevin Sapp**, who previously built New Edge Labs (acquired by
Netskope), an early user-side zero-trust product; their backgrounds span the identity/zero-trust
space (the brief's specific Zscaler/Mandiant tenure was not corroborated in the primary sources
reviewed — treat those specifics as unverified). Funding: **$25M Series A on 2024-09-12 led by
Acrew Capital**, with Ballistic Ventures, Ten Eleven Ventures, Okta Ventures, and CrowdStrike Falcon
Fund participating, bringing cumulative funding to **~$45M** (vendor + SecurityWeek). The earlier
seed (~$16.5M) rolls into that ~$45M cumulative figure. **No acquisition found** — the seed registry
carried no M&A flag and research found none; ownership `independent`, confidence `high` (corroborated
by independent press). Note the investor base (Okta Ventures, CrowdStrike Falcon Fund) ties it to
two identity/security incumbents — worth watching as NHI consolidates.

## CTO / hedge-fund lens

This is **Day-2** for most shops and, for a typical hedge fund, **low fit** today. Aembit solves a
problem that bites cloud-native engineering organizations with lots of workload-to-workload and
workload-to-SaaS traffic and a sprawl of service-account secrets — i.e., teams that build and run
substantial software. A 50-person fund running mostly SaaS and a couple of internal apps gets more
NHI risk reduction sooner from secrets hygiene in its existing vault and IdP than from standing up a
workload-IAM broker. It has **no direct SR 11-7 / model-risk** role; it is an access-control
control, not a governance or model-risk tool. Where it becomes interesting for a fund is the
**agentic-AI** angle: if you start running AI agents that autonomously call internal APIs and SaaS
(via MCP), Aembit's Blended Identity and per-session short-lived credentials are a credible way to
keep agents from holding standing secrets or acting beyond the operating human's entitlements — a
control you will want *before* agents touch anything sensitive. Until you are at that stage, this is
a watch-list item, not a Day-1 buy.

## Competitors / alternatives

[oasis-security](oasis-security.md), [token-security](token-security.md), [astrix-security](astrix-security.md), [clutch-security](clutch-security.md), [cyberark](cyberark.md)
(machine identity / Conjur), [entro-security](entro-security.md), [natoma](natoma.md); conceptually also SPIFFE/SPIRE for
open-source workload identity.

## Open questions / to verify

- Founders' exact prior employers (brief cites ex-Zscaler/Mandiant; only New Edge Labs→Netskope was
  corroborated here).
- Seed round size/date and lead (brief notes ~$16.5M; not separately confirmed in cached sources).
- Any funding round after the 2024-09 Series A (none found as of 2026-06).
- Production traction/customer count beyond named references (Snowflake, Fortune 250 retailer).
- How heavy the edge-agent deployment is in practice for classic (non-agent) workloads.

## Sources

- [Aembit Raises $25 Million in Series A Funding (Aembit press release)](https://aembit.io/press-release/aembit-raises-25-million-in-series-a-funding-for-non-human-identity-and-access-management/) — fetched 2026-06-28 — supports: HQ, founders, $25M Series A / ~$45M total, Acrew + investors, secretless/JIT product framing, agentic/MCP; confidence: high (vendor primary on funding).
- [Non-Human IAM Provider Aembit Raises $25 Million (SecurityWeek)](https://www.securityweek.com/non-human-iam-provider-aembit-raises-25-million/) — fetched 2026-06-28 — supports: founded 2021, HQ Silver Spring MD, ~$45M total, policy-based access-mgmt description, customers; confidence: high (independent press).
- [Aembit IAM for Agentic AI Is Now Generally Available (Aembit blog)](https://aembit.io/blog/aembit-iam-for-agentic-ai-is-now-generally-available/) — fetched 2026-06-28 — supports: agentic-AI product, Blended Identity, MCP Authorization Server + MCP Identity Gateway architecture, Claude/Copilot Studio, April-2026 GA; confidence: med (vendor).
- [Aembit agent-identity / MCP coverage aggregate (Identiverse 2026-06; Security Boulevard 2026-04)](https://aembit.io/) — fetched 2026-06-28 — supports: MCP governance for Copilot Studio at Identiverse 2026-06-16, agent-identity push timeline; confidence: med (vendor + trade).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2021, HQ Silver Spring MD, founders David Goldschlag (CEO) & Kevin Sapp (ex-New Edge Labs/Netskope), $25M Series A 2024-09 led by Acrew (~$45M cumulative), independent (no M&A). Documented secretless/JIT workload-IAM access-management model (vs posture/discovery NHI peers), SaaS control plane + edge gateway/agent architecture, and the agentic-AI/MCP push (Blended Identity, MCP Authorization Server + Identity Gateway, Claude/Copilot Studio, April-2026 GA). Set ownership_confidence high, hedge_fund_fit low, status researched, confidence medium. 4 sources cached.
