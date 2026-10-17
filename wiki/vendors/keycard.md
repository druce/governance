---
title: Keycard
type: vendor
name: Keycard
slug: keycard
aka: [Keycard Labs, Keycard Labs Inc., keycard.ai]
primary_category: non-human-identity
also_listed_in: [tool-identity-integration, authorization-engine]
website: https://www.keycard.ai/
founded: 2025
hq: San Francisco, CA, USA
ownership_state: independent
owner: null
ownership_note: Venture-backed; emerged from stealth 2025-10-22 with $38M combined seed (>$8M, co-led by a16z and Boldstart Ventures) and Series A ($30M, led by Acrew Capital). Acquired Anchor.dev (certificate automation) in Feb 2026, terms undisclosed. Legal entity Keycard Labs, Inc. (Delaware).
acquisition: {announced: null, closed: null, price: null}
funding_total: $38M (as of 2025-10-22)
last_funding: Series A, $30M, 2025-10-22 (led by Acrew Capital)
market_position: {non-human-identity: ai-native-disruptor}
deployment_model: [saas, self-hosted, on-prem]
form_factor: [sdk, inline-proxy, api]
data_leaves_tenancy: partial
integrations: [okta, entra, auth0, google, aws, gcp, github-actions, vercel, splunk, panther, s3, langchain, mcp, a2a, cedar, terraform]
mcp_support: gateway
certifications: [soc2-type2]
pricing_model: usage
fs_traction: claimed
target_customer: developer teams shipping agents, startup to enterprise
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [agent-identity, oauth, token-exchange, rfc-8693, delegation, cedar, task-scoped-credentials, coding-agents, multi-agent, aie-nyc-2026]
sources:
  - {claim: "Emerged from stealth 2025-10-22 with $38M: >$8M seed co-led by a16z and Boldstart, $30M Series A led by Acrew Capital; founded 2025 by ex-Snyk/Okta leaders; HQ San Francisco; task-scoped identity-bound tokens replace static secrets", url: "https://www.securityweek.com/keycard-emerges-from-stealth-mode-with-38-million-in-funding/", date: 2025-10-22, confidence: high}
  - {claim: "Founders Ian Livingstone (CEO), Jared Hanson (creator of Passport.js), Matthew Creager; $38M raised; investor list; legal entity Keycard Labs, Inc.", url: "https://keycard.ai/about", date: 2026-10-16, confidence: medium}
  - {claim: "Runtime authorization: short-lived credentials per request, Cedar policy-as-code via Terraform, SDK / optional gateway / sidecar enforcement points, IdP list, OCSF/Splunk/Panther/S3 audit export, SOC 2 Type II claim, Chime named customer", url: "https://www.keycard.ai/", date: 2026-10-16, confidence: medium}
  - {claim: "Usage pricing on transactions: free 5k/mo, Team $500/mo for 100k, Enterprise custom with dedicated/BYOC/on-prem deployment and customer-managed KMS", url: "https://www.keycard.ai/pricing", date: 2026-10-16, confidence: medium}
  - {claim: "Keycard for Multi-Agent Apps (2026-05-13, early access): per-hop scoped credentials via OAuth 2.0 Token Exchange (RFC 8693), permissions narrow at each hop, workload attestation, Cedar evaluated at every hop", url: "https://keycard.ai/blog/announcing-keycard-for-multi-agent-apps/", date: 2026-05-13, confidence: medium}
  - {claim: "Acquired Anchor.dev (Feb 2026, undisclosed) alongside Keycard for Coding Agents", url: "https://pulse2.com/keycard-acquires-anchor-dev-to-unlock-autonomous-coding-agents/", date: 2026-02-15, confidence: medium}
  - {claim: "Gold sponsor of AI Engineer NYC 2026 (Oct 12–14); CEO Ian Livingstone and Allie Howe on 'Intent Based Auth' main-stage panel with JPMC's Global Chief Security Architect; Kim Maida online talk", url: "https://ai.engineer/nyc", date: 2026-10-16, confidence: high}
---

# Keycard

> Primary category: [non-human-identity](../categories/non-human-identity.md). Also listed in [tool-identity-integration](../categories/tool-identity-integration.md) and [authorization-engine](../categories/authorization-engine.md).

**One-liner** — Runtime authorization for AI agents: instead of handing an agent a long-lived API key, Keycard verifies which agent is asking, on whose behalf, and for what task, then issues a short-lived, narrowly scoped credential — and narrows it further each time the agent delegates work to another agent or tool.

**What it does** — Keycard sits between agents and the resources they call (APIs, SaaS apps, MCP servers, databases) and makes a policy decision every time an agent needs a credential. The pieces, per the vendor's own materials:

- **Agent identity.** The agent proves who it is from its runtime environment (workload attestation), plus the human, if any, it is acting for. The point is that no static secret is stored on disk.
- **Task-scoped, short-lived credentials.** When policy approves a request, the agent gets a token limited to that task and expiring quickly. The vendor's example is a one-hour token restricted to `knowledge:read`. For SaaS such as GitHub or Slack this is a delegated OAuth token. For services without OAuth it brokers stored API tokens.
- **Delegation chains that narrow.** In the multi-agent product (announced 2026-05-13, **early access**), each originating request opens a session. As work passes from agent to agent, Keycard issues a new credential at each hop through **OAuth 2.0 Token Exchange (RFC 8693)**, and permissions can only narrow along the chain. Policy can say things like "this Snowflake grant may not be delegated to a different server" or "no deletes anywhere in this chain."
- **Policy as code in Cedar** (the AWS-originated policy language), managed through Terraform, with every allow and deny logged with attribution and exportable to a SIEM.
- **Three enforcement points:** an SDK in the application (Python, TypeScript, Go, Ruby), an optional gateway that needs no code change, and a **sidecar proxy that swaps placeholder secrets for real user-scoped tokens**, so the agent process never holds a usable credential. A gateway also brokers legacy protocols (Postgres, Kafka, HTTP).

There are two product lines on one platform. **Keycard for Coding Agents** (Feb 2026) covers Cursor, Claude Code, Codex and Windsurf across laptops, sandboxes and CI, and can require explicit approval for sensitive operations. **Keycard for Multi-Agent Apps** (May 2026, early access) is the SDK for teams building their own agent systems.

**Naming / provenance** — Founded **2025** (SecurityWeek). Legal entity **Keycard Labs, Inc.** Founders: **Ian Livingstone** (CEO; SecurityWeek describes the founders as ex-Snyk and ex-Okta senior leadership), **Jared Hanson** (creator of Passport.js, the widely used Node.js auth library) and **Matthew Creager**. The name is generic, so don't confuse it with the unrelated hardware-wallet "Keycard" (Status) or with physical access-card vendors.

**Ownership & viability** — `independent`. It emerged from stealth on **2025-10-22** with **$38M**: a seed of more than $8M co-led by **Andreessen Horowitz** and **Boldstart Ventures**, and a **$30M Series A led by Acrew Capital**. Essence, Exceptional Capital, Mantis, Modern Technical Fund, Tapestry and Vermilion Cliffs participated, and the angels include identity veterans from Auth0 and Okta. In **February 2026** it bought **Anchor.dev**, a stealth certificate-automation startup, for undisclosed terms. No round since 2025 was found. Headcount is unverified (one aggregator says ~15 in 2026). That is a small team carrying a broad protocol surface (OAuth 2.1, Token Exchange, SPIFFE, WIMSE, MCP, A2A).

*Acquisition-risk note:* agent identity is exactly where the identity incumbents are buying. [sailpoint](sailpoint.md) bought [entro-security](entro-security.md), and the category page tracks others. Keycard's founder lineage (Okta, Auth0, Snyk) and investor set make it a plausible target for an IdP or a security platform. If it is acquired, the open-standards design (OAuth token exchange, Cedar) should make the policy model easier to move than a proprietary one. That is an inference, not a vendor commitment.

**Positioning & differentiators** —
- **Against NHI posture vendors** ([astrix-security](astrix-security.md), [token-security](token-security.md), [oasis-security](oasis-security.md), [entro-security](entro-security.md)): those discover and govern the machine credentials that already exist. Keycard tries to stop the credential from existing at all: it issues credentials just in time, per task. You would plausibly run one of each.
- **Against [aembit](aembit.md)**, the closest analogue: both replace static secrets with short-lived, policy-issued credentials. Aembit started from workload-to-workload IAM. Keycard is agent-first: user-delegated sessions, narrowing across multi-hop delegation, and coding-agent coverage. Whether Aembit's agent features now match this is a comparison worth a direct pilot.
- **Against agent-auth / connector platforms** ([arcade](arcade.md), [composio](composio.md), [stytch](stytch.md), [descope](descope.md), [workos](workos.md)): those mostly solve "let my agent call Gmail as this user" plus a connector catalog. Keycard has a smaller connector list (GitHub, Slack, PagerDuty, Sentry, Neon, Linear, custom) but a deeper policy story: Cedar rules, per-hop narrowing, and deny logging.
- **Against authorization engines** ([cerbos](cerbos.md), [permit-io](permit-io.md), [oso](oso.md), [authzed](authzed.md)): those answer "may principal X do Y?" for your own application. Keycard combines that decision with credential issuance and brokering to third-party resources. It is cross-listed in authorization-engine for that reason, not as a general-purpose policy engine.

**Who should choose them / anti-fit** — Fits a firm where **engineers or quants are running coding agents, or building multi-agent systems, against production data and SaaS**, and where security wants to get rid of long-lived tokens in agent configs and get an attributable record of which agent touched what, for whom. It also fits teams that want policy as code (Cedar plus Terraform) that security can review. **Anti-fit:** a firm whose only AI is vendor copilots (Microsoft 365 Copilot, ChatGPT Enterprise), which has no agents of its own to issue credentials to. It also doesn't fit a firm that wants a catalog of hundreds of prebuilt SaaS connectors, or one that needs an NHI *inventory* of existing service accounts and keys. Buy a posture tool for that.

**Known weaknesses / gotchas** —
- **Young and partly early-access.** Founded 2025, and the multi-agent product was still early access as of 2026-05. Expect the API surface to change.
- **One named customer** (Chime, a fintech) is quoted on the vendor site. No independent case study was found.
- **Placement in your stack is not obvious.** Keycard can live in your app (SDK), on the network (gateway) or beside the workload (sidecar), so a pilot should decide which enforcement point you will standardise on. Each has different coverage and failure modes.
- **Overlap with your MCP gateway.** If you already run an [mcp-gateway](../categories/mcp-gateway.md) that brokers OAuth, decide which component owns credential issuance so you don't get two policy planes.

**Deployment & data handling** — The default is multi-tenant SaaS. The **Enterprise** tier offers **dedicated, BYOC or on-prem** deployment, private networking and **customer-managed KMS**. Keycard is in the credential path, not the content path: it issues and brokers tokens and records authorization events (agent, principal, permissions used, outcome). The vendor states that credentials stay in memory, never touch disk, and expire at session close. When the gateway or sidecar is used, requests do traverse Keycard infrastructure. Whether request or response *payloads* are logged or retained is **unverified**. Telemetry retention is 7 days (free), 90 days (Team) and 180 days, extendable (Enterprise). `data_leaves_tenancy: partial` reflects authorization metadata leaving the tenancy on SaaS tiers, with an in-tenant option on Enterprise. Latency added per credential exchange is unpublished.

**Integrations & partnerships** — IdPs: Okta, Microsoft Entra ID, Google, Auth0, OIDC, plus workload identity from AWS, Google Cloud, Vercel and GitHub Actions. Audit export goes to OCSF-compatible SIEMs, Splunk, Panther and S3, with continuous OCSF export on Enterprise. Agent frameworks and protocols: LangChain, MCP, A2A and OAuth 2.1 (trade press adds Mastra). Coding agents: Cursor, Claude Code, Codex, Windsurf. Deploy targets include Vercel, Cloudflare, Fly.io, Modal, AWS, GCP and Azure. `mcp_support: gateway` is set because Keycard brokers auth for MCP servers and offers a gateway enforcement point. It is **not** a full MCP gateway with a tool catalog and content inspection. It published an "Agent Baseline" white paper with Docker and Snyk. Keycard was a **Gold sponsor at AI Engineer NYC 2026** (Oct 12–14). There, CEO Ian Livingstone and Allie Howe were on the main-stage **"Intent Based Auth"** panel with JPMorgan Chase's Global Chief Security Architect and AAuth founder Dick Hardt, and Kim Maida gave an online-track talk on adding identity, token exchange and task-scoped policy to an on-call agent.

**Compliance & FS traction** — **SOC 2 Type II** is claimed on the vendor site. The report itself was not seen. No ISO 27001 or ISO 42001 was found. **FS traction: claimed.** Chime, a consumer fintech, is a named production user per the vendor. The JPMC security architect sharing a panel with Keycard is **not** evidence of a customer relationship. No hedge-fund or asset-manager references were found. For a small fund, the free and Team tiers ($500/mo) mean it does not assume enterprise seat counts.

**Commercial** — **Usage-based**, metered on "transactions" (each request Keycard is involved in). Starter is free (5,000/mo, hard cap). Team is **$500/mo** for 100,000, with $1 per extra 1,000. Enterprise is custom, on an annual commitment, and adds SCIM/AD/LDAP, device- and org-level policy, dedicated/BYOC/on-prem deployment and a 99.95% SLA. These are list prices as of 2026-10-16.

## Open questions

- Is any request or response **payload** content logged in gateway or sidecar mode, and where are the authorization logs stored (region)?
- Is the SOC 2 Type II report current? Any ISO 27001 plans?
- When does the multi-agent product reach GA, and does Coding Agents coverage extend beyond the four named IDE agents?
- Named FS customers beyond Chime. Any buy-side (hedge fund / asset manager) deployments?
- Headcount and any funding since 2025-10.
- How it compares head-to-head with [aembit](aembit.md)'s agent-identity features and with the OAuth brokering inside MCP gateways such as [runlayer](runlayer.md) and [speakeasy](speakeasy.md).
- Whether the primary category should be [tool-identity-integration](../categories/tool-identity-integration.md) rather than NHI. Keycard spans both, and NHI was chosen because its core object is the agent's own identity and credential lifecycle.

## Sources

- [Keycard emerges from stealth with $38M (SecurityWeek)](https://www.securityweek.com/keycard-emerges-from-stealth-mode-with-38-million-in-funding/) — fetched 2026-10-16 — supports: funding amounts and leads, founding year, HQ, product summary; confidence: high
- [Keycard secures $38m (FinTech Global)](https://fintech.global/2025/10/23/keycard-secures-38m-to-advance-ai-agent-security/) — fetched 2026-10-16 — supports: funding corroboration; confidence: medium
- [About Keycard (vendor)](https://keycard.ai/about) — fetched 2026-10-16 — supports: founders, investors, legal entity; confidence: medium
- [Keycard homepage (vendor marketing)](https://www.keycard.ai/) — fetched 2026-10-16 — supports: product mechanics, enforcement points, integrations, SOC 2 claim, Chime; confidence: medium
- [Keycard pricing (vendor)](https://www.keycard.ai/pricing) — fetched 2026-10-16 — supports: tiers, prices, deployment options, retention; confidence: medium
- [Announcing Keycard for Multi-Agent Apps (vendor blog, 2026-05-13)](https://keycard.ai/blog/announcing-keycard-for-multi-agent-apps/) — fetched 2026-10-16 — supports: RFC 8693 token exchange, per-hop narrowing, early-access status; confidence: medium
- [Keycard for Multi-Agent Apps (Help Net Security, 2026-05-15)](https://www.helpnetsecurity.com/2026/05/15/keycard-for-multi-agent-apps/) — fetched 2026-10-16 — supports: launch corroboration, framework list; confidence: medium
- [Keycard acquires Anchor.dev (Pulse2, 2026-02-15)](https://pulse2.com/keycard-acquires-anchor-dev-to-unlock-autonomous-coding-agents/) — fetched 2026-10-16 — supports: acquisition, Coding Agents product; confidence: medium
- [CRN startups to watch (GlobeNewswire, 2026-01-29)](https://www.globenewswire.com/news-release/2026/01/29/3228894/0/en/Keycard-Named-a-Top-Cloud-Computing-Startup-to-Watch-for-Solving-the-AI-Agent-Identity-and-Access-Problem.html) — fetched 2026-10-16 — supports: CRN recognition; confidence: medium
- [AI Engineer NYC 2026](https://ai.engineer/nyc) — fetched 2026-10-16 — supports: Gold sponsorship, panel and talk details; confidence: high
- Cached: `raw/sources/2026-10-16--keycard--funding-and-founding.md`, `raw/sources/2026-10-16--keycard--product-pricing-and-launches.md`, `raw/sources/2026-10-16--aie-nyc-2026--sponsors-and-sessions.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
