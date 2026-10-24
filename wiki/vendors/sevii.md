---
title: Sevii
type: vendor
name: Sevii
slug: sevii
aka: [Sevii ADR, Sevii Warriors, Sevii Cyber Warriors, Cyber Swarm Defense]
primary_category: ai-soc-analysts
also_listed_in: []
website: "https://www.sevii.com/"
founded: null
hq: null
ownership_state: independent
owner: null
ownership_note: "Early-stage, venture-backed. Pre-seed (announced ~2025-04-24) led by Overline with 10VC and SaaS Ventures, amount undisclosed. BMW i Ventures invested (post dated 2026-02; round type and amount undisclosed; an aggregator labels it a seed round dated 2026-02-01). Co-founded by CEO Curt Aubley (ex-Deloitte, CrowdStrike, Intel, Lockheed Martin)."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: "BMW i Ventures-led or joined round, 2026-02 (amount undisclosed)"
market_position: {ai-soc-analysts: ai-native-disruptor}
deployment_model: [saas, on-prem]
form_factor: [platform, api]
data_leaves_tenancy: partial
integrations: [crowdstrike, splunk, microsoft, google-secops, servicenow, jira, tenable, fortinet]
mcp_support: unverified
certifications: [soc2-type2]
pricing_model: "per protected asset; vendor states no AI token or usage charges"
fs_traction: unverified
target_customer: security teams with an established EDR/XDR + SIEM stack (CrowdStrike-heavy especially) that want autonomous triage-to-remediation; public sector and regulated environments via an on-prem appliance
last_verified: 2026-10-24
verify_after: null
tags: [ai-soc, agentic, autonomous-remediation, adr, crowdstrike-ecosystem, aws-marketplace, on-prem-appliance, early-stage]
sources:
  - {claim: "Sevii ADR platform: Cyber Warriors agents for triage, investigation, hunting, remediation within customer AI-governance policies; 365+ API integrations; SOC 2 Type II; per-asset pricing with no token costs; BMW i Ventures investor", url: "https://www.sevii.com/", date: 2026-10-24, confidence: medium}
  - {claim: "Out of stealth 2025-09-05; agentless; commercial deployments on AWS; on-prem NVIDIA appliance for classified/regulated; CrowdStrike NG-SIEM and ServiceNow case mirroring; AWS and CrowdStrike Marketplace", url: "https://securityboulevard.com/2025/09/sevii-agentic-ai-warriors-march-out-of-stealth-to-augment-socs-with-machine-speed-remediation/", date: 2025-09-05, confidence: medium}
  - {claim: "Pre-seed led by Overline with 10VC and SaaS Ventures; amount undisclosed", url: "https://pulse2.com/sevii-pre-seed-funding-raised-for-autonomous-agentic-ai-defense-platform", date: 2025-05-04, confidence: medium}
  - {claim: "BMW i Ventures investment; co-founders Aubley, Collins, Cross, Shimo; Aubley background", url: "https://bmwiventures.com/news/why-we-backed-sevii-and-the-case-for-autonomous-cyber-remediation", date: 2026-02-01, confidence: high}
  - {claim: "Cyber Swarm Defense Mode, fixed price per asset", url: "https://www.helpnetsecurity.com/?p=368311", date: 2026-04-28, confidence: medium}
---

# Sevii

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md).

**One-liner** — Sevii is an early-stage US startup whose AI agents ("Cyber Warriors") take detections from your existing EDR/XDR and SIEM, investigate and hunt, and then **carry out the remediation**, such as isolating hosts and disabling identities. It sells this as "autonomous defense and remediation" (ADR): an action layer on top of the SOC rather than a triage assistant.

**What it does** — Sevii connects by API (agentless, nothing installed on endpoints) to 365+ security tools. Named integrations include CrowdStrike Falcon, Splunk, Microsoft, Google SecOps, Tenable, Fortinet, ServiceNow and Jira. Agents then:
- triage and investigate incoming detections;
- run escalated, hypothesis and 7-day retrospective threat hunts;
- **remediate within policies the customer defines** ("AI governance policies"), with human-in-the-loop optional and every action documented for audit.

Its headline metric is "mean time to act". It claims remediation in under 15 minutes, "often under six" (vendor claim). Modules split by domain: enterprise and SIEM/data lake ("Spike"), identity ("Oz"), cloud ("Ace"), AI security ("Aegis") and "preemptive" hunting. **Cyber Swarm Defense** (April 2026) spins up more agents when alert volume spikes. Case notes can be mirrored back into CrowdStrike NG-SIEM and ServiceNow. Sevii's own site calls AI SOC "the starting point", so it is squarely in the category the respondent placed it in.

**Naming / provenance** — Came out of stealth **2025-09-05**. The co-founders are **Curt Aubley** (CEO; previously led US cyber detection and response at Deloitte, ran technology alliances and solution architecture at CrowdStrike, was VP/CTO in Intel's Data Center Group, and spent about 12 years as a cybersecurity CTO at Lockheed Martin), Stephen Collins (CTO), Caleb Cross (CDO) and Arnie Shimo (CSO). The founding year is unconfirmed: the company was funded and pre-launch in April 2025. **HQ is unconfirmed.** Aggregators disagree (Charlotte, NC vs Mooresville, NC) and the company site does not state it. Not to be confused with unrelated companies with similar names (e.g. Sev1Tech, Sevatec).

**Ownership & viability** — `independent`, early-stage venture.
- **Pre-seed** led by **Overline** with 10VC and SaaS Ventures, announced around **2025-04-24**. Amount undisclosed.
- **BMW i Ventures** invested in a round described in a post dated **February 2026**, joining Overline, TenVC and Tandem Launch. Amount and stage undisclosed; an aggregator calls it a seed.
- **Programmes.** Selected for the **2026 CrowdStrike / AWS / NVIDIA Cybersecurity Startup Accelerator**, per a Carahsoft (public-sector reseller) listing and the company site.
- **Viability.** Seed-stage. Runway and headcount are unknown, and there are no named customers.
- **Acquisition-risk note.** Its tight CrowdStrike alignment (marketplace listing, accelerator, CEO's CrowdStrike background) makes CrowdStrike or another XDR/SIEM owner a plausible acquirer. That pattern, platforms absorbing AI-SOC startups, is described on the [ai-soc-analysts](../categories/ai-soc-analysts.md) page. For customers, the risk is that an acquisition ends support for non-acquirer integrations.

**Positioning & differentiators** — `ai-native-disruptor`: a 2025-vintage startup selling autonomous agents in place of tier-1/tier-2 analyst work.
- **Remediation-first, not investigation-first.** [dropzone-ai](dropzone-ai.md), [prophet-security](prophet-security.md) and [radiant-security](radiant-security.md) lead with autonomous *investigation* and a verdict for a human. Sevii leads with *taking the action*. That gains speed, and it raises the cost of an agent error.
- **On-prem, air-gapped option.** Sevii offers a self-contained appliance with NVIDIA GPUs that needs no cloud connection, for classified and regulated environments. Most AI-SOC peers are SaaS-only. [d3-security](d3-security.md) is the other self-hostable option on this list.
- **Per-asset pricing, no token charges** (vendor-stated). This contrasts with usage- or alert-volume-priced peers, which makes cost predictable during an alert storm.
- **Versus platform-native agents ([crowdstrike](crowdstrike.md) Charlotte AI, [palo-alto-networks](palo-alto-networks.md) Cortex AgentiX):** Sevii claims cross-vendor reach (EDR + identity + cloud + SIEM). If your estate is mostly Falcon, Charlotte AI may already cover much of the same ground.

**Who should choose them / anti-fit** — Fits a **security team with a mature, well-tuned EDR/XDR and SIEM stack**, CrowdStrike especially, and **written response playbooks**. It suits teams willing to let software contain threats automatically within tight policy guardrails, and that want 24/7 machine-speed containment without a night shift. The one survey respondent (in production) shows a hedge-fund-type buyer has adopted it. **Anti-fit:**
- A firm whose change-control or operational-risk culture will not allow automated containment of production identities or trading endpoints. Use an investigation-only AI SOC analyst instead.
- A firm that wants a vendor with a long track record and named FS references.
- A firm without a reliable detection layer. Sevii acts on detections; it does not replace EDR or SIEM.

**Known weaknesses / gotchas** —
- **Autonomous remediation needs careful policy.** A wrongly isolated trading workstation or a disabled service account during market hours is an operational incident. Insist on a scoped allow-list of actions, approval gates for high-impact assets, a dry-run mode, and full action logs. Test rollback.
- **Vendor metrics only.** "$107M+ saved", "2M+ remediations" and the "Level 6" autonomy label are self-reported. No named customers or independent evaluations were found.
- **Thin company disclosure.** Funding amounts, HQ and headcount are not public.
- **Integration depth varies by tool.** "365+ integrations" will not all support write actions. Ask which tools Sevii can *remediate* in, not just read from.

**Deployment & data handling** — Commercial deployments run as SaaS on **AWS**, and Sevii pulls detection and context data from your tools by API into its environment. The **on-prem appliance** keeps processing local, without internet or cloud connectivity. The CEO describes the system as "entirely under the customer's operational control." Sevii holds API credentials with *write* permissions into EDR, identity and cloud consoles. Those are high-value credentials: ask how they are stored, scoped and rotated. Model provider, data retention, and whether customer data trains models are **unverified**.

**Integrations & partnerships** — Named: CrowdStrike Falcon / NG-SIEM, Splunk, Microsoft, Google SecOps (Chronicle), Tenable, Fortinet, ServiceNow, Jira. Distribution through **AWS Marketplace** and **CrowdStrike Marketplace** (announced as slated in 2025-09; current listing not checked), plus Carahsoft for the public sector. MCP support unverified.

**Compliance & FS traction** — SOC 2 Type II (vendor site). No FS customers named, so FS traction is unverified beyond the survey respondent. Every agent action is documented, which supports incident-response evidence for SEC cyber-disclosure and exam purposes. Ask for an export format.

**Commercial** — Fixed price **per protected asset**, with no AI token or usage charges (vendor). Price bands not public.

**Survey note** — 2026-10 CTO survey write-in: **1 respondent, in production**, under Q47 *AI SOC*.

## Open questions

- HQ location and founding date (aggregators conflict: Charlotte vs Mooresville, NC).
- Funding amounts for the pre-seed and the 2026 BMW i Ventures round.
- Which integrations support write/remediation actions vs read-only.
- Model providers used, data retention, training-use terms; credential storage for connected tools.
- Named customers, especially in financial services; independent evaluations.
- Current AWS / CrowdStrike Marketplace listing status.

## Sources

- [Sevii homepage](https://www.sevii.com/) — fetched 2026-10-24 — supports: ADR platform modules, integrations, SOC 2, per-asset pricing, aggregate claims, BMW i Ventures; confidence: medium (vendor marketing)
- [Sevii agentic AI warriors march out of stealth (Security Boulevard, 2025-09-05)](https://securityboulevard.com/2025/09/sevii-agentic-ai-warriors-march-out-of-stealth-to-augment-socs-with-machine-speed-remediation/) — fetched 2026-10-24 — supports: launch, deployment (AWS, on-prem appliance), integrations, marketplaces; confidence: medium
- [Sevii pre-seed funding (Pulse 2.0, 2025-05-04)](https://pulse2.com/sevii-pre-seed-funding-raised-for-autonomous-agentic-ai-defense-platform) — fetched 2026-10-24 — supports: pre-seed investors; confidence: medium
- [Why we backed Sevii (BMW i Ventures, 2026-02)](https://bmwiventures.com/news/why-we-backed-sevii-and-the-case-for-autonomous-cyber-remediation) — fetched 2026-10-24 — supports: investment, co-founders, CEO background; confidence: high
- [Sevii unveils Cyber Swarm Defense Mode (Help Net Security, 2026-04-28)](https://www.helpnetsecurity.com/?p=368311) — fetched 2026-10-24 — supports: Cyber Swarm Defense, per-asset pricing; confidence: medium
- Cached: `raw/sources/2026-10-24--sevii--adr-platform-funding.md`; earlier one-liner evidence in `raw/sources/2026-10-23--mdr-soc-writeins--one-liner-sources.md`

## History

- [2026-10-24] Page created via wiki-create and researched the same day. Triggered by a single in-production write-in under Q47 AI SOC in the 2026-10 CTO survey. Primary ai-soc-analysts. Differentiated as remediation-first (autonomous action) vs investigation-first peers.
