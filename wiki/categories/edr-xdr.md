---
type: category
name: EDR / XDR
slug: edr-xdr
layer: foundation
priority: day-1
trifecta_role: none-detection
maps_to_seed_doc: EDR / XDR
maps_to_seed_csv: EDR
vendor_count: 4
status: drafted
last_updated: 2026-06-28
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

## Lethal-trifecta role

Not a direct trifecta control — it doesn't sit on the prompt/data/egress path the
way an AI firewall or DLP does. Its job is **detection and response** on the
machines where AI workloads run. It backstops the trifecta: if a green-zone host
running an agent is compromised, EDR/XDR is what notices the malicious process and
contains it. Relevant across all trust zones, but most load-bearing in the
**green zone** (internal production systems) where the consequences of a
compromised endpoint are highest.

## Vendors

- [[crowdstrike]] — Falcon platform; market-leading cloud-native EDR/XDR, also a hub for the SOC stack (and owns [[crowdstrike-logscale]] for SIEM).
- [[microsoft-defender]] — Defender XDR; bundled with M365 E5, the default for Microsoft-centric shops.
- [[sentinelone]] — Singularity platform; autonomous EDR/XDR, also pushing into AI/runtime security.
- [[palo-alto-networks]] — Cortex XDR; part of the broader Palo Alto platform (NGFW, Prisma, Cortex SIEM).

## Consolidation / M&A dynamics

The endpoint market is mature and consolidating into platform plays — each vendor
above is bundling EDR/XDR with SIEM, identity, and now AI-security modules.
[[sentinelone]] is reported to have acquired Prompt Security to move into AI
runtime security (per seed; unverified — to confirm in research). [[crowdstrike]]
and [[palo-alto-networks]] are both serial acquirers building out adjacent
SOC/AI-security capabilities. The strategic question for a buyer is less "which
EDR" and more "which platform do I want to standardize the rest of my SOC on."

## Adjacent categories

- [[siem-soc]] — EDR/XDR telemetry feeds the SIEM; the lines blur as vendors sell both.
- [[ai-soc-analysts]] — AI/agentic triage layered on top of EDR/XDR alerts.
- [[network-security-sase]] — the network-side counterpart; XDR increasingly correlates network signals too.

## Survey

**Question:** Which EDR / XDR platform does your firm use or evaluate for endpoint
detection and response?

**Answer options (multi-select):**
- CrowdStrike (Falcon)
- Microsoft Defender XDR
- SentinelOne
- Palo Alto Cortex XDR
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

- Overlap with [[siem-soc]] is increasing as XDR absorbs SIEM telemetry; worth
  watching whether respondents conflate the two.
- Cortex XDR vs Cortex XSIAM (Palo Alto's SIEM) can confuse respondents who own
  the broader Palo Alto platform.
