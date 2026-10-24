---
title: AI SecOps / Agentic SOC Analysts
type: category
name: AI SecOps / Agentic SOC Analysts
slug: ai-soc-analysts
category: ai-soc-analysts
layer: foundation
survey_question: AI SOC analysts
adoption_tier: day-2
trigger: SOC alert volume outgrows analyst headcount
maturity_stage_required: null
category_maturity: growth
adjacent: [siem-soc]
incumbent_coverage: []
vendor_count: 23
maps_to_seed_doc: AI SecOps, Security Automation
maps_to_seed_csv: AI SOC analysts
last_verified: 2026-06-30
---

## Business objective

The RoboCop watching the logs. AI SOC analysts (a.k.a. agentic SOC, AI SecOps) use LLM-driven agents to do the tier-1/tier-2 work a human security analyst does: triage alerts from the [siem-soc](siem-soc.md), investigate them, pull context, decide what is a false positive, and draft or execute a response. The objective is to clear the alert backlog and shrink mean-time-to-respond without hiring a larger SOC team.

This is distinct from classic SOAR (rule-based playbooks): these tools reason over alerts rather than just running fixed automations, though the line blurs as SOAR vendors add AI.

## When you need it

Day-2. You need a SIEM and an alert pipeline first; the AI analyst sits on top of it. The trigger is alert volume the team cannot keep up with — a common state once AI telemetry, cloud, and SaaS logs all flow in. For a small fund with a thin or outsourced SOC, this can be attractive earlier as a force-multiplier; for a larger in-house SOC it is a Day-2 efficiency play. Maturity and trust in autonomous response are still developing, so most adopt in an assist (human-reviewed) mode first.

## Security role

Detection/response automation, not prevention. Like the SIEM it sits behind, it blocks nothing inline — it makes the detection-and-response loop faster and cheaper after other controls have fired or failed. Green-zone operational tooling; itself a consideration, since an AI analyst with broad read access to security telemetry is a sensitive agent that needs its own governance.

## Vendors

Independent AI SOC analyst startups (the survey shortlist):

- [prophet-security](../vendors/prophet-security.md) — agentic SOC analyst for autonomous alert triage and investigation.
- [dropzone-ai](../vendors/dropzone-ai.md) — AI SOC analyst that auto-investigates alerts end to end.
- [7ai](../vendors/7ai.md) — agentic security platform for SOC automation.
- [radiant-security](../vendors/radiant-security.md) — AI SOC analyst for triage, investigation, and response.
- [simbian](../vendors/simbian.md) — AI SOC agents / agentic security automation.
- [artemis-security](../vendors/artemis-security.md) — AI-native SecOps that bundles a SIEM-replacement data layer (federated query) *with* the agentic analyst; NYC, emerged from stealth 2026 with $70M.
- [sevii](../vendors/sevii.md) — Remediation-first agentic SOC: agents take detections from existing EDR/SIEM (CrowdStrike-centric) and isolate or remediate within customer policy. Priced per asset with no token charges; on-prem air-gapped appliance option. Seed-stage, no named customers. (added 2026-10-24)

Platform-embedded AI analysts (cross-listed; tied to a larger security stack):

- [crowdstrike](../vendors/crowdstrike.md) — Charlotte AI; agentic SOC analyst embedded in the Falcon platform.
- [palo-alto-networks](../vendors/palo-alto-networks.md) — Cortex AgentiX; agentic SOC built into the Cortex XSIAM platform.
- [datadog](../vendors/datadog.md) — Bits AI Security Analyst (GA 2026-03-23), investigates Datadog Cloud SIEM signals only. Primary in [llm-observability](llm-observability.md). (added 2026-10-23)

Managed / outcome-delivered agentic SOC:

- [reliaquest](../vendors/reliaquest.md) — Agentic SOC platform delivered as a managed outcome over your existing SIEM/EDR; scale ($300M+ ARR) and maturity the AI-SOC startups lack, priced at a premium. Cross-listed to [siem-soc](siem-soc.md). (added 2026-10-23)

Managed detection & response (MDR) providers. Placed here 2026-10-24 (decision in `log.md`): survey respondents wrote MDR providers into the SIEM and AI SOC questions, because for a small fund the "AI SOC" is often a service, not a tool. Each page says what AI the provider actually claims; several claim little.

- [blackpoint-cyber](../vendors/blackpoint-cyber.md) — MSP-channel MDR with a 24/7 "human-led, AI-accelerated" SOC that acts on threats; AI claims are vendor marketing with no technical detail. CompassOne adds a compliance SIEM. Bain Capital Tech Opportunities-backed. Cross-listed to [siem-soc](siem-soc.md). (added 2026-10-24)
- [adlumin](../vendors/adlumin.md) — N-able-owned (closed 2024-11-20) cloud SIEM/XDR with an optional 24/7 MDR service for SMBs and MSPs; claims proprietary AI automates 90% of investigation and remediation (vendor marketing). Cross-listed to [siem-soc](siem-soc.md). (added 2026-10-24)
- [esentire](../vendors/esentire.md) — Warburg Pincus-owned MDR whose Atlas platform runs multi-agent investigations on Claude via Amazon Bedrock with senior-analyst review; Atlas AIDR (2026-09) monitors customers' own AI and MCP use. Metrics vendor-reported. (added 2026-10-24)
- [bluevoyant](../vendors/bluevoyant.md) — Microsoft-specialist MDR (Sentinel/Defender) with a "BlueVoyant AI" agentic SecOps platform (2026-06), sold managed or as self-service SaaS; also a managed third-party-risk service (cross-listed to [vendor-risk](vendor-risk.md)). (added 2026-10-24)
- [soteria](../vendors/soteria.md) — Charleston boutique MDR (ex-NSA founders) running 24x7 detection on the client's EDR plus a Panther-based managed SIEM, IR and vCISO; human-led, makes no AI claim of its own. Cross-listed to [siem-soc](siem-soc.md). (added 2026-10-24)
- [sophos](../vendors/sophos.md) — Sophos MDR (40,000+ organisations, vendor figure) plus Secureworks Taegis MDR since 2025-02; the largest pure-play MDR. Primary in [edr-xdr](edr-xdr.md). (added 2026-10-24)
- [zscaler](../vendors/zscaler.md) — Red Canary MDR (closed 2025-08-01) and an Agentic SOC product; Red Canary was written in under SIEM. Primary in [network-security-sase](network-security-sase.md). (added 2026-10-24)

See also [reliaquest](../vendors/reliaquest.md) above (managed agentic SOC) and [rapid7](../vendors/rapid7.md) (MDR bundled with its SIEM; primary in [siem-soc](siem-soc.md)).

SOAR / automation that overlaps agentic SOC (cross-listed):

- [torq](../vendors/torq.md) — hyperautomation/SOAR adding AI-driven SOC capabilities.
- [qevlar-ai](../vendors/qevlar-ai.md) — agentic investigation with the strongest named reference base of the European entrants (Mercedes-Benz, Sodexo; Orange Cyberdefense, ECI, Atos as MSSPs); extending the same agents into vulnerability operations. (added 2026-08-26)
- [d3-security](../vendors/d3-security.md) — the incumbent-turned-AI-native case: a 2002-vintage SOAR vendor whose Morpheus platform pairs agentic investigation with the execution engine and 800+ integrations it already had. Self-hostable. (added 2026-08-26)
- [sekoia](../vendors/sekoia.md) — European AI-native SOC platform with first-party threat intelligence; the sovereignty option in a category that is otherwise entirely US-owned. Bpifrance-backed, heavy MSSP channel. (added 2026-08-26)
- [crogl](../vendors/crogl.md) — "knowledge engine" framing: investigation logic learned from the environment rather than authored as playbooks. Founded by ex-Splunk/Databricks leadership. Early-stage. (added 2026-08-26)

## Consolidation / M&A dynamics

No seed-flagged acquisitions in this row. The notable dynamic is build-vs-buy by the platform incumbents: CrowdStrike (Charlotte AI) and Palo Alto (Cortex AgentiX) are building agentic SOC capabilities natively into their platforms, squeezing the independent startups (Prophet, Dropzone, 7AI, Radiant, Simbian) — which compete on being platform-neutral and faster-moving. Expect acquisitions of the independents by SIEM/XDR owners.

## Adjacent categories

- [siem-soc](siem-soc.md) — the alert source and audit backbone these analysts sit on top of; tightly coupled.
- [edr-xdr](edr-xdr.md) — endpoint detection that generates much of the alert volume; CrowdStrike spans both.
- [ai-spm](ai-spm.md) — governs the AI agents in the org, which would include the AI analyst itself.
- [ai-runtime-security](ai-runtime-security.md) — protects AI apps at runtime; the AI analyst is itself an AI app worth protecting.

## Survey

**Question.** Which AI SOC analyst / agentic SecOps tool(s) is your firm currently using or evaluating?

**Answer options.** Prophet Security; Dropzone AI; 7AI; Radiant Security; Simbian; Artemis Security; CrowdStrike Charlotte AI; Palo Alto Cortex AgentiX; Crogl; D3 Security (Morpheus); Sekoia.io; Qevlar AI; Torq; ReliaQuest GreyMatter; Sevii; Blackpoint Cyber (MDR); Adlumin (N-able); eSentire (MDR / Atlas); BlueVoyant (MDR); Soteria (MDR); Sophos MDR; Red Canary (Zscaler); Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** Early, fast-moving category — expect heavy "Interested/Considering/pilot" and little "in production." The platform-embedded options (Charlotte AI, Cortex AgentiX) will be "in use" mostly as a byproduct of owning CrowdStrike/Palo Alto, not as a deliberate AI-SOC purchase — worth disambiguating. Torq straddles [siem-soc](siem-soc.md) SOAR; respondents may report it under either question. (Jazz Security was reclassified to [dlp](dlp.md) after research — it is AI-native DLP, not a SOC analyst.) Ask about deployment mode (assist vs. autonomous) since trust levels vary widely. MDR providers were added as options 2026-10-24 after respondents wrote them in; consider a separate "who runs your 24/7 detection?" question so outsourced SOCs are not conflated with AI-analyst software.

## Open taxonomy questions

- Overlap with [siem-soc](siem-soc.md) SOAR (Torq) — confirm which survey question owns it.
- As incumbents embed AI analysts, this may collapse back into [siem-soc](siem-soc.md) / [edr-xdr](edr-xdr.md) rather than remaining standalone.
