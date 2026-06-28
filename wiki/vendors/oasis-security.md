---
type: vendor
name: Oasis Security
slug: oasis-security
categories: [non-human-identity]
layer: foundation
aliases: [Oasis, Oasis NHI, Oasis Agentic Access Management, AAM]
website: "https://www.oasis.security"
founded: 2022
hq: New York, NY, USA (R&D roots in Tel Aviv, Israel)
ownership: independent
ownership_detail: Independent, venture-backed as of 2026-06; no acquisition found. $120M Series B (2026-03-19) led by Craft Ventures.
ownership_confidence: high
funding_total: ~$195M (per press; one source says $190M — minor discrepancy)
last_funding: Series B, $120M, 2026-03-19 (led by Craft Ventures)
deployment: [saas, api]
target_customer: large enterprise / Fortune 500; regulated (finance, healthcare, insurance, energy, retail)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
tags: [non-human-identity, nhi, machine-identity, agentic-identity, secrets, least-privilege]
sources_count: 4
last_updated: 2026-06-28
---

# Oasis Security

> A Non-Human Identity Management (NHIM) platform: discover, posture-check, govern, and
> remediate the service accounts, tokens, secrets, workloads — and now AI agents — that
> outnumber human identities in the enterprise.

**One-liner** — A platform that finds, governs, and cleans up all your non-human identities
(service accounts, API keys, tokens, bots, workloads), and has extended that into purpose-built
identity governance for autonomous AI agents.

**Categories** — [non-human-identity](../categories/non-human-identity.md)

## What it does

Modern enterprises run far more non-human identities (NHIs) than human ones — service accounts,
API keys, OAuth tokens, certificates, secrets, and increasingly AI agents — and most are
ungoverned, over-privileged, and unrotated. Oasis builds an inventory of every NHI across cloud,
SaaS, and on-prem, classifies them, scores their posture (stale/unused identities, standing
secrets, excessive privilege, anomalous behavior), and drives remediation including safe secret
rotation. Its own framing is "discover, resolve, automate."

In late 2025 Oasis launched **Agentic Access Management (AAM)** (announced 2025-11-19), which it
markets as the first identity solution purpose-built to govern AI agents across their full
lifecycle. AAM adds three things on top of the NHI base: **intent inference** (LLM-driven reading
of what an agent is trying to do, so policy can judge purpose, not just the raw action),
**deterministic policy enforcement** (a policy engine that approves/denies and escalates to a
human when an agent crosses a privilege boundary), and **just-in-time session identities**
(ephemeral, least-privilege credentials minted per session to eliminate standing secrets, with a
full audit trail).

## Where it sits in the stack

Primary category: [non-human-identity](../categories/non-human-identity.md) (Foundation layer). Oasis governs the identities that
machines and agents use, which is upstream plumbing rather than an AI-specific control. In
lethal-trifecta terms it mainly hardens the **sensitive-data** and **egress** legs indirectly: by
enforcing least privilege and just-in-time, short-lived credentials it limits what a compromised
workload or a misbehaving agent can reach and exfiltrate. It does not inspect prompts or model
output, so it does not address the untrusted-input leg. Its AAM line reaches into agent-governance
territory adjacent to [ai-spm](../categories/ai-spm.md) and authorization layers ([authorization-engine](../categories/authorization-engine.md)), but its
spine remains identity governance, not runtime prompt security.

## Deployment & architecture

- **SaaS, agentless.** No endpoint agents; Oasis connects via API/read integrations to discover
  and govern NHIs. This lowers deployment friction versus agent-based approaches.
- **Integrations** (per vendor site, marketing): IdPs and clouds — Azure, AWS, GCP, Okta, Ping,
  Active Directory; secret vaults — HashiCorp Vault, Azure Key Vault, AWS KMS, GCP; PaaS/SaaS —
  Snowflake, Databricks, GitHub, Salesforce; AI services — OpenAI, AWS Bedrock, Glean.
- **Capabilities map**: discovery/inventory, posture management (incl. an AI-SPM-style agent risk
  view and anomaly detection), lifecycle (provisioning to deprovisioning, secret rotation across
  vaults), and remediation with time-bound, intent-aware access.
- **AAM** issues ephemeral just-in-time session identities and runs an LLM-driven intent-inference
  plus deterministic policy engine for AI agents.

## Positioning & differentiators

Oasis is one of the category-defining NHI startups and is known for an agentless, fast-to-stand-up
discovery+remediation platform and an early, aggressive pivot to **agent identity** (AAM). It
competes with a crowded NHI field:

- [token-security](token-security.md) and [entro-security](entro-security.md) — NHI discovery/posture and secrets-security peers;
  Entro leans secrets-centric, Token leans machine-identity-centric.
- [clutch-security](clutch-security.md) — NHI lifecycle/security peer.
- [astrix-security](astrix-security.md) — closest direct rival on NHI + agent identity (note Astrix carries a seed
  flag of acquisition by Cisco — verify on its own page).
- [aembit](aembit.md) — adjacent but architecturally different: a workload IAM / access "broker" that brokers
  credentials at access time, vs Oasis's discover/govern/posture model.
- [cyberark](cyberark.md) — the incumbent identity-security platform (secrets via Conjur, plus NHI and machine
  identity); the big-vendor consolidation threat to point NHI startups.

Oasis's differentiator pitch is intent-aware, lifecycle-wide governance ("access control that
understands intent, not just static roles") and being first to market with a dedicated agentic
access product. These are vendor claims; independent corroboration of "first" is weak.

## Ownership, funding & M&A

Independent, venture-backed. Founded 2022 by **Danny Brickman** (CEO) and **Amit Zimerman** (Chief
Product Officer), both veterans of Israeli military cyber (reported as Unit 81 / IDF cyber R&D).
Funding timeline:

- Stealth exit 2024-01-31 with **$40M** total ($5M seed + $35M Series A), Series A led by **Sequoia
  Capital**, with Accel, Cyberstarts, Maple Capital, and angels Guy Podjarny (Snyk) and Michael Fey
  (Island).
- **$35M Series A extension**, May 2024 (led by Accel, Cyberstarts, Sequoia per press).
- **$120M Series B**, 2026-03-19, led by **Craft Ventures**, with Cyberstarts, Sequoia, and Accel.
  Reported total to date **~$195M** (one source says $190M — minor unreconciled discrepancy).
  Company reports new ARR up 5x YoY and a majority-Fortune-500 customer base.

**No acquisition found** — the seed registry carried no M&A flag, and nothing in research indicates
one. Ownership: `independent` / confidence `high` (multiple dated primary/press sources on funding;
no cap-table doc reviewed).

> Soft discrepancy: founding year given as 2022 by Oasis's own 2025–2026 materials and the Series B
> coverage; the Jan-2024 TechCrunch piece implied ~2023 ("less than a year after founded"). HQ is
> now New York, NY per current vendor/PR materials, with Tel Aviv R&D roots (early coverage called
> it Tel Aviv). Using 2022 / New York. Non-blocking.

## CTO / hedge-fund lens

NHI governance is generally **Day-2** for a hedge fund: you stand up human IdP/SSO, secrets
management, and logging first (Day-1), then tackle the sprawl of service accounts, tokens, and
secrets. It becomes more pressing — arguably Day-1.5 — the moment you start deploying **AI agents**
with real access to data and systems, which is exactly the gap Oasis's AAM targets: ungoverned,
over-privileged agent credentials are a direct path to data egress. There is no specific SR 11-7 /
model-risk mapping here; this is a security/identity control, not a model-governance tool.

Fit caveats: Oasis sells primarily to **Fortune 500 / large enterprise**, so a 50-person fund may
find it heavier and pricier than needed, and may get partial NHI coverage from an existing
[cyberark](cyberark.md) footprint or cloud-native IAM. The agentless SaaS model is the friendliest part of the
deployment story. A mid/large asset manager already running many service accounts across
Snowflake/Databricks/GitHub and piloting agents is the natural buyer.

## Competitors / alternatives

[astrix-security](astrix-security.md), [token-security](token-security.md), [entro-security](entro-security.md), [clutch-security](clutch-security.md), [aembit](aembit.md),
[cyberark](cyberark.md), [silverfort](silverfort.md), [natoma](natoma.md)

## Open questions / to verify

- Exact cumulative funding ($190M vs ~$195M) and precise structure of the May-2024 $35M extension.
- Founding year 2022 vs 2023 (use 2022 per vendor; TechCrunch implied later).
- Real-world maturity/adoption of AAM (launched 2025-11) vs marketing; whether "first" agentic
  identity product holds up against [astrix-security](astrix-security.md) and others.
- Whether any on-prem/self-hosted option exists or it is SaaS-only.
- Pricing model and minimum viable deployment for a mid-market shop.

## Sources

- [Oasis Security leaves stealth with $40M (TechCrunch)](https://techcrunch.com/2024/01/31/oasis-security-leaves-stealth-with-40m-to-lock-down-the-wild-west-of-non-human-identity-management/) — fetched 2026-06-28 — supports: founders/backgrounds, $40M ($5M seed + $35M Series A) led by Sequoia, agentless SaaS NHI product, early customers; confidence: high (press).
- [Oasis raises $120M to secure NHIs across AI and cloud (SiliconANGLE)](https://siliconangle.com/2026/03/19/oasis-security-raises-120m-secure-non-human-identities-across-ai-cloud-environments/) — fetched 2026-06-28 — supports: $120M Series B 2026-03-19, Craft Ventures lead, ~$190M total, founded 2022, agentic AI focus, Fortune 500 / 5x ARR; confidence: high (press).
- [Oasis launches Agentic Access Management (PR Newswire)](https://www.prnewswire.com/news-releases/oasis-security-launches-agentic-access-management-the-first-identity-solution-built-for-ai-agents-302619375.html) — fetched 2026-06-28 — supports: AAM launch 2025-11-19, intent inference / deterministic policy / JIT session identities, HQ New York, founded 2022; confidence: med (vendor PR).
- [Oasis Security homepage](https://www.oasis.security/) — fetched 2026-06-28 — supports: NHIM capabilities, agentless SaaS + integration list, HQ NY address, target customers; confidence: med (vendor marketing).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2022, HQ New York NY (Tel Aviv R&D roots), founders Danny Brickman (CEO) & Amit Zimerman (CPO), independent/venture-backed with ~$195M total to a $120M Series B (2026-03-19, Craft Ventures); no M&A. Documented agentless SaaS NHI platform (discover/posture/lifecycle/remediate) and the 2025-11 Agentic Access Management launch (intent inference, deterministic policy, JIT session identities). Positioned vs Astrix/Token/Entro/Clutch/Aembit/CyberArk. Set status: researched, confidence medium, ownership_confidence high. 4 sources cached. Noted soft discrepancies on founding year (2022 vs 2023) and total funding ($190M vs ~$195M).
