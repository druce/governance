---
type: category
name: Enterprise Logging / SIEM / SOC
slug: siem-soc
layer: foundation
priority: day-1
trifecta_role: none-detection (detection, audit trail, and forensics — not a preventive leg of the trifecta)
maps_to_seed_doc: Enterprise logging / SIEM / SOC
maps_to_seed_csv: SIEM/SOAR/SecOps
vendor_count: 9
status: drafted
last_updated: 2026-06-28
---

## Business objective

The security camera control room. A SIEM (security information and event management) platform collects logs and telemetry from across the estate — endpoints, network, cloud, SaaS, and now AI gateways and assistants — correlates them, raises alerts when something looks off, and keeps the audit trail. SOAR (security orchestration, automation, and response) adds playbooks that automate the response. Together they are the system of record for "what happened" and the detection layer that flags when it shouldn't have.

For AI specifically, the SIEM is where prompt/response logs, gateway traffic, and agent actions should land so there is a single, queryable audit trail across the whole AI platform.

## When you need it

Day-1, required — and usually already deployed. No regulated firm operates without centralized logging and some detection capability; for a hedge fund it is both a security and a compliance/audit necessity. The AI-era work is not buying a SIEM but *piping AI telemetry into it* — making sure gateway logs, assistant transcripts, and agent activity are ingested, retained, and alertable alongside everything else.

## Lethal-trifecta role

Detection and forensics, not prevention. The SIEM does not break untrusted-input, sensitive-data, or egress directly — it is how you *notice* when a control failed and reconstruct the chain afterward. It is the green-zone audit backbone and the evidence layer behind every other control.

## Vendors

Enterprise SIEM / SecOps platforms:

- [[microsoft-sentinel]] — cloud-native SIEM, default for Azure/M365 shops; tight Defender integration.
- [[splunk]] — the data-platform incumbent; powerful, broad, expensive (per seed, acquired by Cisco).
- [[sumo-logic]] — cloud-native SIEM/log analytics (per seed, taken private by Francisco Partners).
- [[elastic]] — ELK/Elastic Security; open-source-rooted, popular where teams want to self-host and control cost.
- [[google-secops]] — Google SecOps (formerly Chronicle); hyperscale log retention and detection.
- [[crowdstrike-logscale]] — CrowdStrike Falcon LogScale; high-speed log management tied to the CrowdStrike estate.
- [[palo-alto-networks]] — Cortex XSIAM; AI-driven SIEM/SOC platform consolidating SIEM + SOAR + analytics.

SOAR / automation cross-listed (modern, AI-leaning automation that overlaps the SOC):

- [[torq]] — hyperautomation/SOAR platform (also relevant to AI-SPM and AI SOC).

## Consolidation / M&A dynamics

- Splunk — per seed, acquired by Cisco (per seed; unverified — to confirm in research).
- Sumo Logic — per seed, taken private by Francisco Partners (per seed; unverified — to confirm in research).

The SIEM market is consolidating into platform owners (Cisco/Splunk, Palo Alto Cortex, Microsoft, Google, CrowdStrike), with the standalone independents being absorbed. The strategic trend is SIEM folding into broader "SecOps platforms" that bundle SIEM + SOAR + XDR + AI analysts (see [[ai-soc-analysts]]).

## Adjacent categories

- [[ai-soc-analysts]] — the AI/agentic layer that triages the alerts this SIEM generates; tightly coupled (XSIAM, Charlotte, LogScale all pair with their SOC).
- [[edr-xdr]] — feeds endpoint telemetry into the SIEM; CrowdStrike and Defender span both.
- [[ai-gateway]] / [[llm-observability]] — sources of AI telemetry that should be ingested for audit.
- [[comms-surveillance]] — separate compliance-driven archive/surveillance; different system of record but conceptually adjacent.

## Survey

**Question.** Which SIEM / SOAR / SecOps platform(s) is your firm currently using or evaluating?

**Answer options.** Microsoft Sentinel; Splunk; Sumo Logic; Elastic (ELK); Google SecOps (Chronicle); CrowdStrike Falcon LogScale; Palo Alto Cortex XSIAM; Torq; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** Sentinel and Splunk are table-stakes and will dominate "in production"; most firms already own one, so emphasize the *primary* SIEM and whether AI telemetry is ingested. Torq is SOAR/automation rather than full SIEM — it overlaps [[ai-soc-analysts]] and may confuse respondents; consider moving them to that question or labeling them clearly. Splunk→Cisco and Sumo→Francisco Partners (per seed) date those options.

## Open taxonomy questions

- SOAR/automation (Torq) straddles this and [[ai-soc-analysts]]. (Jazz Security reclassified to [[dlp]] post-research.)
- As SIEM folds into "SecOps platforms," confirm whether this stays a distinct category or merges with [[ai-soc-analysts]] and [[edr-xdr]].
