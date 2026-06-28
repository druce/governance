---
type: vendor
name: Astrix Security
slug: astrix-security
categories: [non-human-identity, ai-spm]
layer: foundation
aliases: [Astrix]
website: https://astrix.security
founded: 2021
hq: Boston, Massachusetts, USA (R&D in Tel Aviv, Israel)
ownership: acquired
ownership_detail: "Cisco announced INTENT to acquire Astrix 2026-05-04; deal PENDING (not closed) as of 2026-06-28. Terms undisclosed (press cites ~$400M, unconfirmed). Prior to deal: independent, $85M+ raised."
ownership_confidence: medium
funding_total: $85M+ (pre-acquisition)
last_funding: Series B $45M led by Menlo Ventures
deployment: [saas, api]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [non-human-identity, nhi, agentic-identity, cisco]
---

# Astrix Security

> Primary category: [[non-human-identity]]. Pending acquisition by [[cisco]].

**One-liner** — Non-human identity (NHI) security: discover, govern and protect the API keys, service accounts, OAuth tokens and AI-agent credentials that machines and agents use to access enterprise systems.

**What it does** — Inventories every non-human identity and its connections across SaaS, cloud and internal systems, then scores risk (over-privileged, stale, leaked, or anomalous credentials), enforces least-privilege and lifecycle policy, and detects/responds to NHI-based threats. As agentic AI proliferates, Astrix extends this to **AI agents** — an "AI Agent Control Plane" governing what credentials agents hold and how they're used. The job it does: stop the sprawl of machine credentials from becoming an unmonitored attack surface.

**Where it sits in the stack** — [[non-human-identity]] at the foundation layer, with an [[ai-spm]] angle (governing agent identities is part of AI security posture). Trifecta role: guards **sensitive-data** access (least-privilege on machine credentials) and constrains **egress**/lateral movement by reining in over-scoped tokens. Adjacent to [[identity-access]] (human IdP) and [[tool-identity-integration]] (agent→SaaS auth).

**Deployment & architecture** — SaaS, integrating via API/OAuth connectors into SaaS apps, cloud providers, IdPs and secrets stores to map NHIs without agents on every box. Post-acquisition, Cisco plans to fold capabilities into **Cisco Identity Intelligence, Secure Access and Duo**, with telemetry feeding **[[splunk]]** for SOC detection/response.

**Positioning & differentiators** — One of the early, well-funded NHI pure-plays, now leaning hard into the agentic-identity narrative. Differentiates on breadth of integrations and the agent-control-plane framing. Nearest neighbors: [[token-security]], [[aembit]], [[oasis-security]], [[entro-security]], [[clutch-security]], [[natoma]], and the NHI capabilities inside [[cyberark]].

## Ownership, funding & M&A

> Contradiction (soft): seed frontmatter said `ownership: acquired` by Cisco. Reality as of 2026-06-28 is **intent announced, deal pending** — not yet closed. Status: noted, non-blocking — flagged 2026-06-28.

Astrix was founded **2021** (Israeli-founded; HQ now listed as Boston, MA with Tel Aviv R&D) by **Alon Jackson** (CEO) and **Idan Gour** (CTO). It raised **$85M+**, including a **$45M Series B led by Menlo Ventures**. **Cisco announced intent to acquire Astrix on 2026-05-04**; the transaction is **pending** (no Cisco completion announcement found by 2026-06-28). Financial terms were not disclosed; press reports cite ~$400M (unconfirmed). Verified against Cisco's blog and Astrix's own announcement — the **intent** is high confidence; **completion** is not yet confirmed, so `ownership_confidence` is medium pending close.

## CTO / hedge-fund lens

NHI governance is generally **Day-2** for a fund — you stand up human IdP/SSO and secrets management first — but it climbs the list fast once you deploy AI agents that hold their own credentials. Astrix's value is visibility into machine/agent identities you didn't know existed. For a Cisco/Duo/Splunk shop, the pending acquisition makes it a natural extension; for others, weigh it against NHI pure-plays and CyberArk. Watch the deal: until it closes, roadmap and standalone availability carry integration risk.

## Competitors / alternatives

[[token-security]], [[aembit]], [[oasis-security]], [[entro-security]], [[clutch-security]], [[natoma]], [[cyberark]].

## Open questions / to verify

- **Deal close**: confirm if/when the Cisco acquisition completes and final terms.
- Exact founding date and current standalone product availability/pricing.

## Sources
- [Cisco Blogs — Cisco Announces Intent to Acquire Astrix Security](https://blogs.cisco.com/news/cisco-announces-intent-to-acquire-astrix-security) — fetched 2026-06-28 — supports: intent 2026-05-04, NHI/agentic identity, integration into Identity Intelligence/Secure Access/Duo/Splunk; confidence: high
- [Astrix Security — A New Chapter: Astrix Is Joining Cisco](https://astrix.security/learn/blog/a-new-chapter-astrix-security-is-joining-cisco/) — fetched 2026-06-28 — supports: founders Alon Jackson & Idan Gour, $85M+ raised / $45M Series B (Menlo Ventures), HQ Boston; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified Cisco announced INTENT to acquire Astrix 2026-05-04 — deal PENDING, not closed. Corrected the seed's flat "acquired" to intent/pending (soft contradiction flagged). Founded 2021, founders Jackson & Gour, $85M+ raised. ownership_confidence medium pending close.
