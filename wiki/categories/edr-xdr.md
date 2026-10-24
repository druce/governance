---
title: EDR / XDR
type: category
name: EDR / XDR
slug: edr-xdr
category: edr-xdr
layer: foundation
survey_question: EDR / XDR
adoption_tier: day-1
trigger: table stakes — usually already deployed
maturity_stage_required: null
category_maturity: mature
adjacent: [siem-soc, network-security-sase]
incumbent_coverage: []
vendor_count: 6
maps_to_seed_doc: EDR / XDR
maps_to_seed_csv: EDR
last_verified: 2026-06-28
---

# EDR / XDR

## Business objective

Endpoint Detection and Response (EDR), and its broader cousin Extended Detection
and Response (XDR), detect and stop malware and intrusions at the endpoint —
laptops, servers, and increasingly cloud workloads. The seed doc calls it the
**immune system for laptops and servers**: it spots and kills bad stuff before it
causes damage, and gives the SOC the telemetry to investigate when it doesn't.
XDR extends the same detect-and-respond loop across endpoint, identity, email,
and network signals so analysts chase one correlated incident instead of a dozen
disconnected alerts.

## When you need it

**Day 1 — but almost always already deployed.** This is baseline enterprise
security hygiene, not an AI-specific control, so a hedge fund of any size will
typically already own one of these before the AI conversation starts. For the AI
program specifically, EDR/XDR matters because agentic and developer workloads run
*on* endpoints and in ephemeral compute — the place a compromised agent, a poisoned
dependency, or an exfiltration tool actually executes. Treat it as a prerequisite
you confirm, not a new purchase you scope.

## Security role

Detective and responsive rather than inline — it doesn't sit on the prompt or data
path the way an AI firewall or DLP does. Its job is **detection and response** on
the machines where AI workloads run: if a green-zone host running an agent is
compromised, EDR/XDR is what notices the malicious process and contains it — the
backstop when preventive controls fail. Relevant across all trust zones, but most
load-bearing in the **green zone** (internal production systems) where the
consequences of a compromised endpoint are highest.

## Vendors

- [crowdstrike](../vendors/crowdstrike.md) — Falcon platform; market-leading cloud-native EDR/XDR, also a hub for the SOC stack (and owns [crowdstrike-logscale](../vendors/crowdstrike-logscale.md) for SIEM).
- [microsoft-defender](../vendors/microsoft-defender.md) — Defender XDR; bundled with M365 E5, the default for Microsoft-centric shops.
- [sentinelone](../vendors/sentinelone.md) — Singularity platform; autonomous EDR/XDR, also pushing into AI/runtime security.
- [palo-alto-networks](../vendors/palo-alto-networks.md) — Cortex XDR; part of the broader Palo Alto platform (NGFW, Prisma, Cortex SIEM).
- [trend-micro](../vendors/trend-micro.md) — Trend Vision One; XDR fused with attack-surface risk management, strong hybrid/legacy-server coverage, and the only mainstream non-US-listed option (TSE 4704). PE take-private reported Feb 2025 and still unresolved. (added 2026-08-26)
- [sophos](../vendors/sophos.md) — Thoma Bravo-owned, channel-led endpoint + firewall + the largest pure-play MDR (40k+ orgs); acquired Secureworks (closed 2025-02-03); Taegis now the analytics core of Sophos Fusion. (added 2026-10-23)

## Consolidation / M&A dynamics

The endpoint market is mature and consolidating into platform plays — each vendor
above is bundling EDR/XDR with SIEM, identity, and now AI-security modules.
[sentinelone](../vendors/sentinelone.md) is reported to have acquired Prompt Security to move into AI
runtime security (per seed; unverified — to confirm in research). [crowdstrike](../vendors/crowdstrike.md)
and [palo-alto-networks](../vendors/palo-alto-networks.md) are both serial acquirers building out adjacent
SOC/AI-security capabilities. The strategic question for a buyer is less "which
EDR" and more "which platform do I want to standardize the rest of my SOC on."

## Adjacent categories

- [siem-soc](siem-soc.md) — EDR/XDR telemetry feeds the SIEM; the lines blur as vendors sell both.
- [ai-soc-analysts](ai-soc-analysts.md) — AI/agentic triage layered on top of EDR/XDR alerts.
- [network-security-sase](network-security-sase.md) — the network-side counterpart; XDR increasingly correlates network signals too.

## Survey

**Question:** Which EDR / XDR platform does your firm use or evaluate for endpoint
detection and response?

**Answer options (multi-select):**
- CrowdStrike (Falcon)
- Microsoft Defender XDR
- SentinelOne
- Palo Alto Cortex XDR
- Trend Micro (Trend Vision One)
- Sophos (incl. Secureworks Taegis)
- Other (Please Specify)

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:** This is a table-stakes category — most respondents
will already have one in production, so the useful signal is *which* one and
whether they'd recommend it, not whether they have one. Expect heavy
Microsoft Defender penetration in M365 E5 shops. Likely correlates with the
respondent's broader platform choice (CrowdStrike/Palo Alto shops cluster).
Not an AI-specific control; included for stack completeness.

## Open taxonomy questions

- Overlap with [siem-soc](siem-soc.md) is increasing as XDR absorbs SIEM telemetry; worth
  watching whether respondents conflate the two.
- Cortex XDR vs Cortex XSIAM (Palo Alto's SIEM) can confuse respondents who own
  the broader Palo Alto platform.
