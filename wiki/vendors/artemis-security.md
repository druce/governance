---
title: Artemis Security
type: vendor
name: Artemis Security
slug: artemis-security
categories: [ai-soc-analysts]
layer: foundation
aliases: [Artemis]
website: "https://artemissecurity.com"
founded: 2025
hq: New York, NY (Israeli-founded team)
ownership: independent
ownership_detail: Independent, VC-backed; emerged from stealth 2026-04-15 with $70M ($15M seed + $55M Series A led by Felicis). No M&A.
ownership_confidence: high
funding_total: ~$70M
last_funding: Series A, $55M (part of $70M total), 2026-04-15
deployment: [saas]
target_customer: enterprise (technology, banking, financial services)
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [none]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-30
tags: [ai-soc, agentic-secops, siem-replacement, threat-detection, new-york]
---

# Artemis Security

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md).

**One-liner** — An AI-native security-operations platform: AI agents that autonomously
hunt threats, investigate every signal, and assemble "attack stories" across an enterprise's
identity, cloud, endpoint, network, and SaaS telemetry — a next-generation SIEM / SOC
replacement.

**Categories** — [ai-soc-analysts](../categories/ai-soc-analysts.md)

> Scope note (soft): Artemis is **"AI for security," not "security for AI."** It defends
> conventional enterprise infrastructure with AI agents; it does **not** govern LLM usage,
> discover shadow AI, or guard model prompts/egress. It sits in the wiki's adjacent
> [ai-soc-analysts](../categories/ai-soc-analysts.md) category (agentic SecOps), not the core LLM-app governance stack.
> Included because it's a notable, well-funded AI-security entrant a CTO will encounter.

## What it does

Artemis is an AI-native threat detection, investigation, and response (TDIR) platform
positioned to replace or augment the traditional SIEM. The job-to-be-done is to cut
mean-time-to-detect/respond by having AI agents do the work a SOC team does at scale:
generate detections tuned to each customer, autonomously investigate every alert (rather
than sampling), and correlate signals across **identity, cloud, endpoint, network, and
SaaS** to surface multi-stage attacks that single-source detections miss — then present
them as coherent incidents instead of a flood of disconnected alerts.

Its pitch is framed around an era where "AI battles AI" and attacks unfold in seconds, so
human-speed triage no longer keeps up. (Vendor metrics — e.g. a claimed "96% reduction in
MTTR" to under five minutes, "2B+ events/hour" — are marketing and unverified.)

## Where it sits in the stack

Home is [ai-soc-analysts](../categories/ai-soc-analysts.md) — the agentic-SOC / AI-SecOps layer that sits on top of
the [siem-soc](../categories/siem-soc.md) backbone. Unlike the independent AI-SOC startups that ride *on top of*
an existing SIEM, Artemis pitches itself as the SIEM-replacement data layer *and* the AI
analyst in one.

Lethal-trifecta role: **none** for the LLM-app trifecta. Artemis is green-zone defensive
operational tooling — it monitors enterprise telemetry rather than sitting in the path of
an LLM application's prompts, retrieval, or model egress. Its only tangential relevance is
detecting *post-compromise* behavior (anomalous exfiltration, identity misuse) at the
infrastructure level — not LLM-specific egress control.

## Deployment & architecture

SaaS platform that overlays the existing stack — no rip-and-replace. The core is a
proprietary **per-customer "dynamic data model"** built from that customer's own behavioral
telemetry (users, machines, cloud workloads, apps, plus business context). Architecturally
its differentiator is **federated query**: it retrieves data on-demand from the customer's
existing cloud storage, data lakes, and SIEMs rather than ingesting and storing everything,
which it claims decouples cost from coverage (pitched at roughly a fifth of the cost of
ingest-priced architectures — marketing).

Integrations (vendor site): Okta, [ping-identity](ping-identity.md), Entra ([microsoft-entra](microsoft-entra.md)) for
identity; AWS, Google Cloud, Azure for cloud; Snowflake, Databricks, S3, Cribl for data;
[splunk](splunk.md) and [elastic](elastic.md) for SIEM; ServiceNow, Jira for case management. Automated
response includes actions like identity isolation.

## Positioning & differentiators

Differentiators it stresses: a per-customer behavioral data model; detections tuned per
customer "within minutes"; autonomous investigation of *every* signal (not sampling); and
the federated/on-demand data architecture that decouples spend from telemetry volume.

Against nearest neighbors:

- vs the independent AI-SOC startups [prophet-security](prophet-security.md), [dropzone-ai](dropzone-ai.md), [radiant-security](radiant-security.md),
  [simbian](simbian.md), [7ai](7ai.md) — those layer an AI analyst on top of your existing SIEM; Artemis
  bundles the data layer (SIEM-replacement) with the AI analyst, competing on owning both.
- vs next-gen SIEM players (Anvilogic, Hunters, Panther — not yet in this wiki) — similar
  "modern SIEM" ambition, with Artemis leaning harder on autonomous agentic investigation.
- vs platform-embedded analysts ([crowdstrike](crowdstrike.md) Charlotte AI, [palo-alto-networks](palo-alto-networks.md)
  Cortex AgentiX) — incumbents building agentic SOC into their stacks; Artemis competes as a
  platform-neutral, AI-native challenger.

Notable credibility signal: a founding team with deep SecOps pedigree — see below.

## Ownership, funding & M&A

Independent, VC-backed. Emerged from **stealth on 2026-04-15** with **$70M total**, raised
as a **$15M seed + $55M Series A**, the Series A led by **Felicis**. Other backers named in
coverage: First Round Capital and Brightmind Partners; Calcalist additionally lists Theory
VC, Two Sigma, and Lockstep, plus angels from Demisto, Abnormal, Splunk, CrowdStrike, Palo
Alto, Microsoft, and Okta. Valuation not disclosed.

Founded ~late 2025 (described as "six-month-old" at the April 2026 launch). **HQ: New York
City**; Israeli-founded team. Founders: **Shachar Hirshberg** (CEO) — ex–Demisto (acquired
by Palo Alto, ~$600M) and former lead of AWS GuardDuty, Harvard MBA; **Dan Shiebler** (CTO)
— previously led AI/ML at Abnormal AI, ML PhD, Oxford. Headcount ~30, reportedly scaling
toward ~65 by end of 2026. **No M&A** — far too early. Ownership confidence: high (multiple
independent outlets corroborate the raise); granular funding split and the extended investor
list lean on a single source (Calcalist).

## CTO / hedge-fund lens

This is a **Day-2** control, and for most hedge funds an indirect one. A SOC platform / SIEM
replacement only matters once you have meaningful security telemetry and an alert pipeline to
tame — which a large fund with an in-house SOC has, but a typical ~50-person fund usually
**outsources to an MDR/MSSP** rather than buying a SIEM-replacement directly. Where it's
relevant, the appeal is the same as the AI-SOC category generally: force-multiply a thin
security team. Two cautions specific to Artemis: it is **brand-new (stealth-exit 2026)** with
unproven production references, and its headline metrics are vendor marketing. No SR 11-7 /
model-risk relevance — this is infrastructure defense, not AI model governance. Fit: medium,
and mostly via your MDR/MSSP rather than a direct buy.

## Competitors / alternatives

[prophet-security](prophet-security.md), [dropzone-ai](dropzone-ai.md), [radiant-security](radiant-security.md), [simbian](simbian.md), [7ai](7ai.md),
[torq](torq.md), [crowdstrike](crowdstrike.md) (Charlotte AI), [palo-alto-networks](palo-alto-networks.md) (Cortex AgentiX)

## Open questions / to verify

- Exact incorporation date and whether there's an Israel R&D center (couldn't confirm).
- Valuation (not disclosed).
- Whether named "customers" (Mercury, Wix, Lemonade, Upwork, Amazon Security, Sony) are
  paying customers or design partners — logos are unverified vendor claims.
- Independent validation of the 96% MTTR and events/hour metrics.
- Pricing / packaging — not public.

## Sources
- [Artemis Emerges from Stealth with $70M to Rebuild Security Operations (Newswire press release)](https://www.newswire.com/news/artemis-emerges-from-stealth-with-70m-to-rebuild-security-operations-for-ai) — fetched 2026-06-30 — supports: $70M raise, Felicis lead, founders/backgrounds, NYC HQ, target sectors, 2026-04-15 stealth exit, AI-SOC positioning; confidence: high
- [Cyber startup Artemis raises $70M six months after launch (Calcalist/CTech)](https://www.calcalistech.com/ctechnews/article/h1eagbt311x) — fetched 2026-06-30 — supports: $15M seed + $55M Series A split, full investor list, ~30→65 headcount, founder bios, Israeli-founded/NYC; confidence: med (single source for the granular figures)
- [Artemis Security homepage](https://artemissecurity.com/) — fetched 2026-06-30 — supports: product description, federated-query architecture, integrations, customer logos, claimed metrics (vendor marketing); confidence: med

## History
- [2026-06-30] Created and researched from vendor request. Established AI-native SecOps / agentic-SOC category fit ([ai-soc-analysts](../categories/ai-soc-analysts.md)); $70M stealth exit 2026-04-15 (Felicis-led Series A), NYC HQ, founders Hirshberg (ex-Demisto/AWS GuardDuty) & Shiebler (ex-Abnormal); federated-query SIEM-replacement architecture; trifecta = none (AI-for-security, not security-for-AI), flagged as soft scope note. Cached 1 source file.
