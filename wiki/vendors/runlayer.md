---
title: Runlayer
type: vendor
name: Runlayer
slug: runlayer
aka: [RunLayer, runlayer.com]
primary_category: mcp-gateway
also_listed_in: []
website: https://www.runlayer.com/
founded: 2025
hq: null
ownership_state: independent
owner: null
ownership_note: Venture-backed. $11M seed (2025-11-17; Khosla Ventures' Keith Rabois and Felicis) and $30M Series A (2026-06-24; Felicis preempted/led, Khosla participated) — $42M total. In active litigation with Rippling (Runlayer suit filed 2026-07-28, S.D.N.Y.; Rippling patent countersuit reported 2026-08).
acquisition: {announced: null, closed: null, price: null}
funding_total: $42M (as of 2026-06-24)
last_funding: Series A, $30M, 2026-06-24 (led by Felicis, with Khosla Ventures)
market_position: {mcp-gateway: ai-native-disruptor}
deployment_model: [saas, self-hosted]
form_factor: [inline-proxy, platform, sdk]
data_leaves_tenancy: partial
integrations: [okta, entra, claude, cursor, chatgpt, codex, salesforce-agentforce, aws, eks, gke, terraform]
mcp_support: gateway
certifications: []
pricing_model: null
fs_traction: claimed
target_customer: mid-market to enterprise (unicorn-stage tech companies; Fortune 500 claimed)
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [mcp, mcp-gateway, shadow-ai, ai-control-plane, agent-governance, litigation, aie-nyc-2026]
sources:
  - {claim: "Out of stealth 2025-11-17 with $11M seed from Khosla's Keith Rabois and Felicis; founders Andrew Berman (ex-Nanit, Vowel→Zapier), Tal Peretz, Vitor Balocco; gateway + threat detection + Okta/Entra-integrated permissions + vetted MCP catalog; customers Gusto, dbt Labs, Instacart, Opendoor; MCP co-creator David Soria Parra as advisor", url: "https://techcrunch.com/2025/11/17/mcp-ai-agent-security-startup-runlayer-launches-with-8-unicorns-11m-from-khoslas-keith-rabois-and-felicis", date: 2025-11-17, confidence: high}
  - {claim: "$30M Series A, Felicis and Khosla, $42M total; platform for AI enablement, security and control across 5–20 AI clients; identity, permissions, policy, audit logs, shadow-AI discovery, runtime risk security", url: "https://www.runlayer.com/blog/series-A-30m-fundraise-felicis-khosla", date: 2026-06-24, confidence: high}
  - {claim: "Felicis preempted and led the Series A (GP Jake Storm led both rounds); founded ~Aug 2025; >12 unicorn customers; unnamed Fortune 500 bank monitors 100k+ employees across 200k devices; revenue undisclosed", url: "https://fortune.com/2026/06/24/exclusive-vinod-khosla-felicis-runlayer-nanit-30-million-enterprise-ai/", date: 2026-06-24, confidence: medium}
  - {claim: "Hosted or self-hosted in customer AWS (ECS+Terraform) or via operator on EKS/GKE; roles, PBAC on MCP tool invocation; audit logs; Shadow AI, Runtime Monitoring, Policies; Hooks SDK", url: "https://docs.runlayer.com", date: 2026-10-16, confidence: medium}
  - {claim: "Runlayer sued Rippling (trade secrets, unfair competition, breach of contract); Rippling confirmed building its own MCP gateway and denies misuse", url: "https://techcrunch.com/2026/07/28/mcp-startup-runlayer-accuses-rippling-of-stealing-its-product-idea/", date: 2026-07-28, confidence: high}
  - {claim: "Rippling countersued alleging infringement of three patents (filing listed 2026-08-10)", url: "https://runtimewire.com/article/rippling-sues-runlayer-three-patents-trade-secret-fight", date: 2026-10-16, confidence: low}
  - {claim: "Gold sponsor of AI Engineer NYC 2026", url: "https://ai.engineer/nyc", date: 2026-10-16, confidence: high}
---

# Runlayer

> Primary category: [mcp-gateway](../categories/mcp-gateway.md). Young, fast-funded, well-connected to the MCP core team, and currently in litigation with Rippling.

**One-liner** — An enterprise MCP gateway that has grown into an "AI control plane". It gives employees an approved catalog of MCP servers, skills and plugins across every AI client they use (Claude, Cursor, ChatGPT, Codex, Agentforce). It ties access to the corporate identity provider, scans tool calls in real time, and surfaces shadow AI.

**What it does** — Runlayer launched in November 2025 as an **all-in-one MCP security platform**. TechCrunch described it as a gateway, threat detection that analyses every MCP request, observability across permitted servers, and fine-grained permissions that **map each agent's rights to the user's own permissions in Okta or Entra**. It came with an "Okta-style" catalog of pre-vetted MCP servers. By the June 2026 Series A it had broadened into two products:

- **AI Control Plane**: a governed MCP gateway across major AI clients. Access is set "under which identity, budget, OAuth grant, and runtime conditions". "Real-time security models" scan tool calls, outputs and intent. Shadow-AI discovery covers unmanaged agents, MCP servers, skills, plugins and client configs. It also does usage, cost and adoption monitoring and keeps sessions and **audit logs**.
- **AI Enablement**: a curated starting catalog ("18,000+ MCPs" that admins narrow to an approved set), plus reusable skills, plugins and an agent builder. Fortune describes the result as a corporate app store plus control room.

The docs also expose a **Hooks SDK** that adds enforcement and telemetry to custom agents, a custom MCP server path, and a platform API. Tool invocation is governed by policy-based access control and platform features by fine-grained authorization.

**Agent-security role.** In lethal-trifecta terms, an MCP gateway is where the **egress** and **sensitive-data** legs meet a choke point. Every tool an agent can reach is either data it can read or a channel it can write out through. Runlayer's controls bear on all three legs. The approved catalog and shadow-MCP discovery shrink the set of untrusted tool servers. Identity-mapped permissions cap what data an agent can reach, at no more than the user's own rights. Inline scanning of tool calls and outputs is meant to catch injection and leakage in flight. The vendor's detection quality is not independently benchmarked. Treat the scanning as one layer of defence, not a guarantee.

**Naming / provenance** — Founded around **August 2025** (Fortune: "10-and-a-half months" before 2026-06-24). It came out of stealth on **2025-11-17**. The founders are **Andrew (Andy) Berman**, CEO and a third-time founder (Nanit; Vowel, acquired by Zapier in 2024; then Zapier's director of AI, where he helped build one of the first MCP servers), and **Tal Peretz** and **Vitor Balocco**, both ex-Zapier. Advisors and angels include **David Soria Parra** (MCP co-creator, Anthropic), **Travis McPeak** (head of security, Cursor) and Nikita Shamgunov (Neon). Styled both "Runlayer" and "RunLayer" (the AIE sponsor list uses the latter). HQ was not stated in any source found.

**Ownership & viability** — `independent`. Funding:
- **$11M seed** (2025-11-17) from Khosla Ventures' Keith Rabois and Felicis.
- **$30M Series A** (2026-06-24), which Felicis preempted and led, with Khosla participating.
- **$42M total.**

Revenue and valuation are undisclosed. Raising a Series A seven months after the seed signals strong demand, and capital is not the near-term risk. **Litigation is.** On **2026-07-28** Runlayer sued **Rippling** in the Southern District of New York for trade-secret misappropriation, unfair competition and breach of contract. It alleges that Rippling ran a near-year-long trial under NDA, with access to roadmap and source, and then built a clone. Rippling confirmed it is launching its own MCP gateway but denies misusing Runlayer IP, and it reportedly countersued in August 2026 alleging infringement of **three Rippling patents**. The countersuit is reported in secondary coverage only; the docket was not checked. A patent claim against a seed-to-Series-A company is a real distraction risk. A buyer should ask for the status of the case and whether any injunction is sought against the product.

*Acquisition-risk note:* MCP-gateway startups are being bought. See [natoma](natoma.md) (Snowflake, acquisition announced 2026-05) and the category page. Fortune names Wiz, Palo Alto Networks and Okta as building agent governance. Any of them, or an IdP, is a plausible acquirer. Self-hosted deployment would help continuity in an exit; contract terms should cover it.

**Positioning & differentiators** —
- **vs [mintmcp](mintmcp.md):** closest in shape. Both are managed gateways with role-based server bundles and an agent-activity monitor. Runlayer leans harder into **enablement** (app-store catalog, skills, agent builder) and **cross-client coverage**, including Agentforce. It also documents **self-hosting in your own AWS/EKS/GKE**. MintMCP's own materials are inconsistent on self-hosting (see its page).
- **vs [natoma](natoma.md):** Natoma is identity-first, with NHI governance and MCP access as one surface, and is now heading into Snowflake. Runlayer is gateway-first and remains independent. That matters if you don't want your tool-governance vendor owned by a data-platform company.
- **vs [obot](obot.md):** Obot offers an **MIT-licensed open-source** gateway you can run and inspect yourself. Runlayer is closed-source commercial with a hosted default. Choose Obot for transparency and zero licence cost. Choose Runlayer for managed operations, shadow-AI discovery and the runtime scanning layer.
- **vs [speakeasy](speakeasy.md):** a very similar control-plane pitch: gateway, IdP-mapped RBAC, shadow MCP, inline guardrails. Speakeasy publishes SOC 2 Type II and ISO 27001 claims and an AGPL codebase. Runlayer publishes neither certifications nor source.
- **vs platform modules** ([prisma-airs](prisma-airs.md), [kong](kong.md), [truefoundry](truefoundry.md)): those bolt MCP control onto an existing security or gateway product. Runlayer is a dedicated specialist with deeper MCP-ecosystem ties (the MCP co-creator is an advisor) but no adjacent platform to bundle.

**Who should choose them / anti-fit** — Fits a firm where **many employees, not just engineers, are adopting several AI clients at once** and IT wants one sanctioned catalog with identity-based access, cost visibility and shadow-AI discovery, without slowing adoption. That is the "golden path" pitch. **Anti-fit:** a firm that needs published certifications before procurement (none found). It also doesn't fit a firm that requires open source, or one unwilling to take on a vendor in unresolved IP litigation. A shop with one or two internal agents and no employee-wide MCP sprawl does not need this much platform.

**Known weaknesses / gotchas** —
- **No public certifications.** No SOC 2 or ISO found on the site, the /security page or the docs as of 2026-10-16. That does not mean none exist; ask.
- **PII masking is not documented publicly.** The site says it scans for "sensitive data" before risky actions. Whether that means *redaction or masking* versus *block or alert* is unverified.
- **Litigation with Rippling**, both directions, unresolved.
- **Vendor statistics are marketing.** The "18,000+ MCPs" catalog figure and the oft-quoted "~10% of MCP servers are malicious" claim (seen in secondary coverage, not on the pages fetched) are Runlayer's own numbers.
- **Breadth creep.** It now spans gateway, security, enablement, agent builder and spend. Evaluate whether the security layer is as deep as a specialist's.

**Deployment & data handling** — **Hosted SaaS** by default. **Self-hosted** in the customer's own AWS account (ECS + Terraform), or via the Runlayer Operator on EKS or GKE in a customer-managed cluster. **Inline**: the gateway sits in the tool-call path and scans tool calls and outputs in real time, so it sees tool-call content. On the hosted option that content transits Runlayer. Self-hosted keeps it in-tenant. Hence `data_leaves_tenancy: partial`. Retention, region and training-use terms are **unverified**, and latency overhead is unpublished.

**Integrations & partnerships** — IdPs: **Okta and Entra** (TechCrunch, launch coverage). SCIM, SSO and OAuth are claimed in a funding tracker but were not confirmed in primary docs. AI clients: Claude, Cursor, ChatGPT, Codex, Salesforce Agentforce and IDEs generally; the company claims coverage of 5–20 clients per enterprise. Custom agents connect through the Hooks SDK. SIEM export is **unverified**. Cloud: AWS (ECS), EKS, GKE. Runlayer was a **Gold sponsor at AI Engineer NYC 2026**. No specific Runlayer session appeared on the agenda fetched.

**Compliance & FS traction** — No certifications found. **FS traction: claimed.** Fortune reports an **unnamed Fortune 500 bank** monitoring AI activity for 100,000+ employees across 200,000 devices. Named customers are tech companies: Instacart, Gusto, Opendoor, dbt Labs, AngelList, Decagon, Lemonade, PagerDuty, Baseten, Homebase. Lemonade (insurance) and AngelList (venture platform) are the nearest to financial services. No hedge-fund or asset-manager reference was found. Whether evidence export and retention meet exam requirements is **unverified**.

**Commercial** — Pricing is not public ("Book a demo"). Model and band are unknown.

## Open questions

- SOC 2 Type II / ISO 27001 status. Ask for the report.
- Does the "sensitive data" scanning **mask or redact**, or only block and alert? Which detectors are built in (PII, secrets, cardholder data)?
- SIEM export targets and audit-log retention. Hosted data region and retention terms.
- Status of *Runlayer v. Rippling* and the Rippling patent countersuit. Has any injunction been sought?
- HQ, headcount, pricing model.
- Identity of the Fortune 500 bank and any buy-side FS customers.
- Seed lead: Runlayer's blog frames the seed as "led by Keith Rabois at Khosla Ventures with Felicis", while Fortune says Felicis GP Jake Storm "led both rounds". This is a soft discrepancy, recorded rather than resolved; it is plausibly a co-lead.

## Sources

- [Runlayer launches with 8 unicorns, $11M from Khosla's Keith Rabois and Felicis (TechCrunch, 2025-11-17)](https://techcrunch.com/2025/11/17/mcp-ai-agent-security-startup-runlayer-launches-with-8-unicorns-11m-from-khoslas-keith-rabois-and-felicis) — fetched 2026-10-16 — supports: seed, founders, launch capabilities, Okta/Entra, customers, advisors; confidence: high
- [Runlayer raises $11M (vendor blog)](https://www.runlayer.com/blog/runlayer-raises-11m-to-scale-enterprise-mcp-infrastructure) — fetched 2026-10-16 — supports: seed lead framing; confidence: medium
- [Runlayer raises $30M Series A (vendor blog, 2026-06-24)](https://www.runlayer.com/blog/series-A-30m-fundraise-felicis-khosla) — fetched 2026-10-16 — supports: Series A, $42M total, product scope, customers; confidence: high
- [Exclusive: Vinod Khosla wanted every dollar of Runlayer's round (Fortune, 2026-06-24)](https://fortune.com/2026/06/24/exclusive-vinod-khosla-felicis-runlayer-nanit-30-million-enterprise-ai/) — fetched 2026-10-16 — supports: Felicis preempt/lead, founding timing, Fortune 500 bank, competitors; confidence: medium
- [Runlayer homepage (vendor marketing)](https://www.runlayer.com/) and [/security](https://www.runlayer.com/security) — fetched 2026-10-16 — supports: product lines, catalog, shadow AI, clients, customers; absence of published certifications; confidence: medium
- [Runlayer docs](https://docs.runlayer.com) — fetched 2026-10-16 — supports: self-hosted options, PBAC/FGA, audit logs, Hooks SDK; confidence: medium
- [MCP startup Runlayer accuses Rippling of stealing its product idea (TechCrunch, 2026-07-28)](https://techcrunch.com/2026/07/28/mcp-startup-runlayer-accuses-rippling-of-stealing-its-product-idea/) — fetched 2026-10-16 — supports: claims, Rippling response, counsel; confidence: high
- [The first MCP lawsuit (Forkast)](https://forkast.news/the-first-mcp-lawsuit-runlayer-v-rippling-signals-a-maturing-agent-economy/) — fetched 2026-10-16 — supports: S.D.N.Y. venue, filing date; confidence: medium
- [Rippling sues Runlayer over three patents (Runtimewire)](https://runtimewire.com/article/rippling-sues-runlayer-three-patents-trade-secret-fight) — search result 2026-10-16 — supports: countersuit; confidence: low (secondary, not fetched in full)
- [AI Engineer NYC 2026](https://ai.engineer/nyc) — fetched 2026-10-16 — supports: Gold sponsorship; confidence: high
- Cached: `raw/sources/2026-10-16--runlayer--funding-and-founding.md`, `raw/sources/2026-10-16--runlayer--product-and-rippling-litigation.md`, `raw/sources/2026-10-16--aie-nyc-2026--sponsors-and-sessions.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
