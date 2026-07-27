---
title: Astrix Security
type: vendor
name: Astrix Security
slug: astrix-security
aka: [Astrix]
primary_category: non-human-identity
also_listed_in: [ai-spm]
website: https://astrix.security
founded: 2021
hq: Boston, Massachusetts, USA (R&D in Tel Aviv, Israel)
ownership_state: acquired-closed
owner: Cisco
ownership_note: 'Cisco announced intent 2026-05-04; acquisition COMPLETED 2026-06-29 (Cisco blog update note). Astrix ended standalone sales of new licenses effective 2026-06-30. Brand and site still live as a transition page. Terms undisclosed (press cites ~$400M, unconfirmed). Prior to deal: independent, $85M+ raised.'
acquisition: {announced: 2026-05-04, closed: 2026-06-29, price: null}
funding_total: $85M+ (pre-acquisition)
last_funding: Series B $45M led by Menlo Ventures
market_position: null
deployment_model: [saas]
form_factor: [api]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [non-human-identity, nhi, agentic-identity, cisco]
sources:
  - {claim: acquisition-close, url: "https://blogs.cisco.com/news/cisco-announces-intent-to-acquire-astrix-security", date: 2026-06-29, confidence: high}
  - {claim: standalone-sales-ended, url: "https://astrix.security", date: 2026-07-27, confidence: high}
---

# Astrix Security

> Primary category: [non-human-identity](../categories/non-human-identity.md). Acquired by [cisco](cisco.md) — deal **closed 2026-06-29**; standalone new-license sales ended **2026-06-30**.

**One-liner** — Non-human identity (NHI) security: discover, govern and protect the API keys, service accounts, OAuth tokens and AI-agent credentials that machines and agents use to access enterprise systems.

**What it does** — Inventories every non-human identity and its connections across SaaS, cloud and internal systems, then scores risk (over-privileged, stale, leaked, or anomalous credentials), enforces least-privilege and lifecycle policy, and detects/responds to NHI-based threats. As agentic AI proliferates, Astrix extends this to **AI agents** — an "AI Agent Control Plane" governing what credentials agents hold and how they're used. The job it does: stop the sprawl of machine credentials from becoming an unmonitored attack surface.

**Where it sits in the stack** — [non-human-identity](../categories/non-human-identity.md) at the foundation layer, with an [ai-spm](../categories/ai-spm.md) angle (governing agent identities is part of AI security posture). Its risk role: controls access to sensitive data (least-privilege on machine credentials) and constrains outbound data flows/lateral movement by reining in over-scoped tokens. Adjacent to [identity-access](../categories/identity-access.md) (human IdP) and [tool-identity-integration](../categories/tool-identity-integration.md) (agent→SaaS auth).

**Deployment & architecture** — SaaS, integrating via API/OAuth connectors into SaaS apps, cloud providers, IdPs and secrets stores to map NHIs without agents on every box. Post-close, Cisco plans to fold capabilities into **Cisco Identity Intelligence**, extended across **Cisco Secure Access** and **Duo Identity and Access Management**, with agent telemetry feeding **[splunk](splunk.md)** for SOC detection/response. As of 2026-07-27 no named Cisco product page has absorbed Astrix yet — `astrix.security` remains the authoritative page, so the integration is announced but not yet shipped under a Cisco SKU.

**Positioning & differentiators** — One of the early, well-funded NHI pure-plays, which leaned hard into the agentic-identity narrative before being acquired. Differentiated on breadth of integrations and the agent-control-plane framing. **No longer a buying unit**: standalone new-license sales ended 2026-06-30, so for new buyers this is a Cisco roadmap item, not a shortlist entry. Nearest neighbors: [token-security](token-security.md), [aembit](aembit.md), [oasis-security](oasis-security.md), [entro-security](entro-security.md), [clutch-security](clutch-security.md), [natoma](natoma.md), and the NHI capabilities inside [cyberark](cyberark.md).

## Ownership, funding & M&A

> Contradiction (soft): seed frontmatter said `ownership: acquired` by Cisco, which was premature when first checked (2026-06-28: intent announced, deal pending). Status: **Resolved 2026-07-27** — the deal has since closed and the seed's "acquired" is now correct.

Astrix was founded **2021** (Israeli-founded; HQ now listed as Boston, MA with Tel Aviv R&D) by **Alon Jackson** (CEO) and **Idan Gour** (CTO). It raised **$85M+**, including a **$45M Series B led by Menlo Ventures**. **Cisco announced intent to acquire Astrix on 2026-05-04** and **completed the acquisition on 2026-06-29** — confirmed by a dated update note Cisco added to the top of its own announcement blog: *"June 29, 2026 Update: We have completed the acquisition of Astrix Security. Welcome to Cisco!"* Financial terms were never officially disclosed; press (Calcalist/Ctech) reports ~$400M, with earlier talks reported at up to $350M — treat the figure as unofficial.

**Standalone sales have ended.** The `astrix.security` site is still live under Astrix branding but carries a banner stating Astrix "is now part of Cisco" and that **Astrix ended standalone sales of new licenses effective 2026-06-30**. Existing customers keep service and support under their current agreements while capabilities are integrated into Cisco over time. The brand and domain are not retired — they now function as a transition landing page rather than a shopping destination.

## CTO / hedge-fund lens

NHI governance is generally **Day-2** for a fund — you stand up human IdP/SSO and secrets management first — but it climbs the list fast once you deploy AI agents that hold their own credentials. Astrix's value is visibility into machine/agent identities you didn't know existed.

As of 2026-07-27 that value is **no longer separately purchasable**: new-license sales stopped 2026-06-30. Practical implications:

- **New buyers** can't buy Astrix. If you want this capability from Cisco, the question is when it lands in Identity Intelligence / Secure Access / Duo — unannounced as of this date. In the meantime, evaluate the remaining NHI pure-plays ([token-security](token-security.md), [aembit](aembit.md), [oasis-security](oasis-security.md), [clutch-security](clutch-security.md), [natoma](natoma.md)) or [cyberark](cyberark.md)'s NHI module. Note the pure-play field is consolidating fast, so weight acquirer risk when shortlisting.
- **Existing Astrix customers** are contractually fine near-term (support continues per current agreements) but should ask Cisco for a written migration path and pricing before renewal — post-acquisition repackaging into a Cisco bundle is the usual outcome and rarely renews at the standalone price.
- **Cisco/Duo/Splunk shops** get the best of this: the capability arrives inside a stack you already own, at the cost of waiting for it.

## Competitors / alternatives

[token-security](token-security.md), [aembit](aembit.md), [oasis-security](oasis-security.md), [entro-security](entro-security.md), [clutch-security](clutch-security.md), [natoma](natoma.md), [cyberark](cyberark.md).

## Open questions / to verify

- ~~**Deal close**~~ — resolved 2026-07-27: closed 2026-06-29. Final terms remain undisclosed (press ~$400M, unofficial).
- **Cisco product landing**: which named Cisco SKU absorbs Astrix, and when. Cisco has stated Identity Intelligence / Secure Access / Duo / Splunk as targets but shipped nothing branded as of 2026-07-27. Re-check.
- **Brand/domain fate**: whether `astrix.security` eventually 301s to Cisco (the Aim/Cato and Normalyze/Proofpoint pattern) or persists.
- Exact founding date; renewal pricing for existing customers under Cisco.

## Sources
- [Cisco Blogs — Cisco Announces Intent to Acquire Astrix Security](https://blogs.cisco.com/news/cisco-announces-intent-to-acquire-astrix-security) — fetched 2026-06-28, **re-fetched 2026-07-27** — supports: intent announced 2026-05-04; **close confirmed 2026-06-29** via the post's dated update note; integration into Identity Intelligence/Secure Access/Duo/Splunk; terms not disclosed; confidence: high
- [Astrix Security homepage](https://astrix.security) — fetched 2026-07-27 — supports: site live under Astrix branding, "now part of Cisco" banner, **standalone new-license sales ended 2026-06-30**, existing customers supported per current agreements; confidence: high
- [Calcalist/Ctech — Cisco acquires AI security startup Astrix for $400 million](https://www.calcalistech.com/ctechnews/article/dy5obf581) — fetched 2026-07-27 — supports: ~$400M reported price; confidence: medium (press report, not officially confirmed)
- [Astrix Security — A New Chapter: Astrix Is Joining Cisco](https://astrix.security/learn/blog/a-new-chapter-astrix-security-is-joining-cisco/) — fetched 2026-06-28 — supports: founders Alon Jackson & Idan Gour, $85M+ raised / $45M Series B (Menlo Ventures), HQ Boston; confidence: high
- Cached: `raw/sources/2026-07-27--astrix-security--cisco-deal-closed.md`

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; verified Cisco announced INTENT to acquire Astrix 2026-05-04 — deal PENDING, not closed. Corrected the seed's flat "acquired" to intent/pending (soft contradiction flagged). Founded 2021, founders Jackson & Gour, $85M+ raised. ownership_confidence medium pending close.
- [2026-07-27] **Deal closed.** Cisco added a dated update to its 2026-05-04 announcement blog: "June 29, 2026 Update: We have completed the acquisition of Astrix Security." `ownership_state` acquired-pending → **acquired-closed**, `acquisition.closed` → 2026-06-29, `verify_after` cleared. Price still undisclosed (press ~$400M, unofficial) so `price` stays null.
- [2026-07-27] **Standalone sales ended 2026-06-30.** `astrix.security` still resolves live under Astrix branding but banners "Astrix Security is now part of Cisco" and states standalone new-license sales ended 2026-06-30; existing customers supported per current agreements. `website` kept as `https://astrix.security` — no Cisco product page has absorbed the capability yet, so this remains the authoritative page. Brand/domain **not** retired (contrast Aim/Cato, Normalyze/Proofpoint). Soft contradiction from 2026-06-28 marked resolved.
