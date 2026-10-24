---
title: Enterprise Logging / SIEM / SOC
type: category
name: Enterprise Logging / SIEM / SOC
slug: siem-soc
category: siem-soc
layer: foundation
survey_question: SIEM/SOAR/SecOps
adoption_tier: day-1
trigger: table stakes — you cannot investigate what you did not log
maturity_stage_required: null
category_maturity: mature
adjacent: [ai-soc-analysts, edr-xdr]
incumbent_coverage: []
vendor_count: 18
maps_to_seed_doc: Enterprise logging / SIEM / SOC
maps_to_seed_csv: SIEM/SOAR/SecOps
last_verified: 2026-06-28
---

## Business objective

The security camera control room. A SIEM (security information and event management) platform collects logs and telemetry from across the estate — endpoints, network, cloud, SaaS, and now AI gateways and assistants — correlates them, raises alerts when something looks off, and keeps the audit trail. SOAR (security orchestration, automation, and response) adds playbooks that automate the response. Together they are the system of record for "what happened" and the detection layer that flags when it shouldn't have.

For AI specifically, the SIEM is where prompt/response logs, gateway traffic, and agent actions should land so there is a single, queryable audit trail across the whole AI platform.

## When you need it

Day-1, required — and usually already deployed. No regulated firm operates without centralized logging and some detection capability; for a hedge fund it is both a security and a compliance/audit necessity. The AI-era work is not buying a SIEM but *piping AI telemetry into it* — making sure gateway logs, assistant transcripts, and agent activity are ingested, retained, and alertable alongside everything else.

## Security role

Detective and out-of-band, not preventive. The SIEM does not screen untrusted input, gate sensitive data, or block outbound flows itself — it is how you *notice* when a control failed and reconstruct the chain afterward. It is the green-zone audit backbone and the evidence layer behind every other control.

## Vendors

Enterprise SIEM / SecOps platforms:

- [microsoft-sentinel](../vendors/microsoft-sentinel.md) — cloud-native SIEM, default for Azure/M365 shops; tight Defender integration.
- [splunk](../vendors/splunk.md) — the data-platform incumbent; powerful, broad, expensive (per seed, acquired by Cisco).
- [sumo-logic](../vendors/sumo-logic.md) — cloud-native SIEM/log analytics (per seed, taken private by Francisco Partners).
- [elastic](../vendors/elastic.md) — ELK/Elastic Security; open-source-rooted, popular where teams want to self-host and control cost.
- [google-secops](../vendors/google-secops.md) — Google SecOps (formerly Chronicle); hyperscale log retention and detection.
- [crowdstrike-logscale](../vendors/crowdstrike-logscale.md) — CrowdStrike Falcon LogScale; high-speed log management tied to the CrowdStrike estate.
- [palo-alto-networks](../vendors/palo-alto-networks.md) — Cortex XSIAM; AI-driven SIEM/SOC platform consolidating SIEM + SOAR + analytics.

SOAR / automation cross-listed (modern, AI-leaning automation that overlaps the SOC):

- [torq](../vendors/torq.md) — hyperautomation/SOAR platform (also relevant to AI-SPM and AI SOC).
- [reliaquest](../vendors/reliaquest.md) — GreyMatter runs triage, investigation and containment as a managed outcome on top of the SIEM/EDR you already own; it is not a SIEM itself. Primary in [ai-soc-analysts](ai-soc-analysts.md). (added 2026-10-23)

Mid-market and platform-bundled SIEM:

- [manageengine](../vendors/manageengine.md) — Low-cost, licence-priced (not ingest-priced) SIEM + UEBA + SOAR from Zoho's IT-management division; strongest on Windows/AD, on-prem or cloud. (added 2026-10-23)
- [sophos](../vendors/sophos.md) — Secureworks Taegis XDR (acquired with Secureworks, closed 2025-02-03) and Sophos Next-Gen SIEM, now the analytics core of Sophos Fusion; mostly bought alongside Sophos MDR. Primary in [edr-xdr](edr-xdr.md). (added 2026-10-23)
- [datadog](../vendors/datadog.md) — Datadog Cloud SIEM: detection rules (800+ out of the box) over logs already in Datadog log management; the natural option where observability already runs on Datadog. Primary in [llm-observability](llm-observability.md). (added 2026-10-23)

Enterprise-logging side only (telemetry backend, **no detection content**):

- [rapid7](../vendors/rapid7.md) — InsightVM + InsightIDR + MDR bundled for the mid-market; the "one vendor, no SOC" option. Public (NASDAQ: RPD) but under activist pressure from Jana Partners to sell itself — price the ownership uncertainty into a multi-year contract. (added 2026-08-26)
- [signoz](../vendors/signoz.md) — open-core, OpenTelemetry-native logs/metrics/traces on ClickHouse; self-hostable Datadog alternative. Answers the *logging* half of this category, not the SIEM half — no rule packs, correlation, case management or SOAR. Cross-listed to [llm-observability](llm-observability.md).
- [guardsix](../vendors/guardsix.md) — Formerly LogPoint (renamed 2026-03-12). Copenhagen SIEM + NDR + SOAR, on-prem or SaaS, historically priced by node rather than ingest; EAL3+ and SOC 2. The sovereignty/MSSP option for EU-regulated firms. Summa Equity-owned. (added 2026-10-24)
- [adlumin](../vendors/adlumin.md) — Cloud-native SIEM with "unmetered data ingest", sold standalone or fully managed via Adlumin MDR (N-able). Primary in [ai-soc-analysts](ai-soc-analysts.md). (added 2026-10-24)
- [blackpoint-cyber](../vendors/blackpoint-cyber.md) — CompassOne's compliance-oriented SIEM (logging & compliance) module bundled with Blackpoint MDR; not a standalone enterprise SIEM. Primary in [ai-soc-analysts](ai-soc-analysts.md). (added 2026-10-24)
- [soteria](../vendors/soteria.md) — Managed SIEM built on Panther, sold with its MDR. Primary in [ai-soc-analysts](ai-soc-analysts.md). (added 2026-10-24)

Several respondents wrote MDR providers into this question (Blackpoint Cyber, Red Canary, Adlumin, Soteria, Sophos/Secureworks). As of 2026-10-24 MDR providers are filed under [ai-soc-analysts](ai-soc-analysts.md); those that also sell a SIEM are cross-listed above.

## Consolidation / M&A dynamics

- Splunk — per seed, acquired by Cisco (per seed; unverified — to confirm in research).
- Sumo Logic — per seed, taken private by Francisco Partners (per seed; unverified — to confirm in research).

The SIEM market is consolidating into platform owners (Cisco/Splunk, Palo Alto Cortex, Microsoft, Google, CrowdStrike), with the standalone independents being absorbed. The strategic trend is SIEM folding into broader "SecOps platforms" that bundle SIEM + SOAR + XDR + AI analysts (see [ai-soc-analysts](ai-soc-analysts.md)).

## Adjacent categories

- [ai-soc-analysts](ai-soc-analysts.md) — the AI/agentic layer that triages the alerts this SIEM generates; tightly coupled (XSIAM, Charlotte, LogScale all pair with their SOC).
- [edr-xdr](edr-xdr.md) — feeds endpoint telemetry into the SIEM; CrowdStrike and Defender span both.
- [ai-gateway](ai-gateway.md) / [llm-observability](llm-observability.md) — sources of AI telemetry that should be ingested for audit.
- [comms-surveillance](comms-surveillance.md) — separate compliance-driven archive/surveillance; different system of record but conceptually adjacent.

## Survey

**Question.** Which SIEM / SOAR / SecOps platform(s) is your firm currently using or evaluating?

**Answer options.** Microsoft Sentinel; Splunk; Sumo Logic; Elastic (ELK); Google SecOps (Chronicle); CrowdStrike Falcon LogScale; Palo Alto Cortex XSIAM; Rapid7; Torq; SigNoz; ManageEngine Log360; guardsix (formerly LogPoint); Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** Sentinel and Splunk are table-stakes and will dominate "in production"; most firms already own one, so emphasize the *primary* SIEM and whether AI telemetry is ingested. Torq is SOAR/automation rather than full SIEM — it overlaps [ai-soc-analysts](ai-soc-analysts.md) and may confuse respondents; consider moving them to that question or labeling them clearly. [signoz](../vendors/signoz.md) has the same problem in the other direction: it is a telemetry backend with no detection content, so a respondent selecting it is telling you about their logging stack, not their SOC — label it "(observability/log backend)" in the option text or the answer is unusable. Splunk→Cisco and Sumo→Francisco Partners (per seed) date those options.

## Open taxonomy questions

- SOAR/automation (Torq) straddles this and [ai-soc-analysts](ai-soc-analysts.md). (Jazz Security reclassified to [dlp](dlp.md) post-research.)
- As SIEM folds into "SecOps platforms," confirm whether this stays a distinct category or merges with [ai-soc-analysts](ai-soc-analysts.md) and [edr-xdr](edr-xdr.md).
- **Does "Enterprise Logging" belong in the same category as SIEM/SOC?** [signoz](../vendors/signoz.md) (added 2026-08-16) is a pure observability backend with no detection capability, filed here on the logging half of the category name. If that is right, [datadog](../vendors/datadog.md) and Grafana/Loki arguably belong here too; if not, SigNoz needs a home elsewhere. Flagged for the human in `taxonomy-gaps.md`.
