---
title: CrowdStrike Falcon LogScale
type: vendor
name: CrowdStrike Falcon LogScale
slug: crowdstrike-logscale
categories: [siem-soc, edr-xdr]
layer: foundation
aliases: [Humio, Falcon LogScale, Falcon Next-Gen SIEM]
website: "https://www.crowdstrike.com/en-us/platform/next-gen-siem/falcon-logscale/"
founded: 2016
hq: Austin, TX, USA
ownership: public
ownership_detail: "Product of CrowdStrike Holdings, Inc. (NASDAQ: CRWD); formerly Humio, acq. 2021 (~$400M)"
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, self-hosted]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [none]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [crowdstrike, humio, siem, soc, next-gen-siem, incumbent]
---

# CrowdStrike Falcon LogScale

> CrowdStrike's index-free log management engine (formerly Humio) — the data plane behind Falcon Next-Gen SIEM, paired with the Charlotte AI assistant.

**One-liner** — The high-speed, index-free log store (formerly Humio) that powers CrowdStrike's Next-Gen SIEM, letting Falcon customers consolidate EDR/XDR telemetry and broad log data without per-index surcharges.

**What it does** — LogScale is a streaming, index-free log management technology: fast ingest and search at low storage cost. Inside CrowdStrike it is the foundation of **Falcon Next-Gen SIEM**, extending the Falcon platform from endpoint EDR/XDR into full SIEM by ingesting third-party logs alongside native CrowdStrike telemetry. Charlotte AI (CrowdStrike's genAI assistant) sits on top for triage.

**Where it sits in the stack** — [siem-soc](../categories/siem-soc.md) (and [edr-xdr](../categories/edr-xdr.md) via the broader Falcon platform), foundation layer. Detection/response plumbing; lethal-trifecta role **none** directly. The central log/data plane that an [ai-soc-analysts](../categories/ai-soc-analysts.md)-style layer (here, Charlotte AI) draws on.

**Deployment & architecture** — Primarily SaaS as part of Falcon; LogScale/Humio also available self-hosted for log management. Priced per-GB ingested without indexing surcharges (positioned against [splunk](splunk.md)). Charlotte AI Agentic Detection Triage is benchmarked against Falcon Complete MDR analyst decisions. Strongest when CrowdStrike Falcon is already the EDR ([crowdstrike](crowdstrike.md)).

**Positioning & differentiators** — Cost/performance of index-free ingest plus tight coupling to Falcon EDR/XDR — the consolidation pitch is "your endpoint vendor is now your SIEM." Competes with [microsoft-sentinel](microsoft-sentinel.md), [google-secops](google-secops.md), [splunk](splunk.md), [elastic](elastic.md), [sumo-logic](sumo-logic.md).

**Ownership, funding & M&A** — Product of **CrowdStrike Holdings, Inc. (NASDAQ: CRWD)**, public, high confidence. **Humio acquisition confirmed**: announced Feb 2021, ~$400M, closed March 2021; rebranded to Falcon LogScale in 2022. Seed flag "(CrowdStrike)" verified. Stub previously `ownership: independent` with unverified detail — corrected to `public`.

**CTO / hedge-fund lens** — **Day-1** for funds already standardized on CrowdStrike Falcon for endpoint: Next-Gen SIEM avoids running a separate SIEM vendor and the index-free model controls cost as log volume grows. Less compelling if you are not a Falcon shop. Not an SR 11-7 tool; central store for security/AI audit logs.

**Competitors / alternatives** — [microsoft-sentinel](microsoft-sentinel.md), [google-secops](google-secops.md), [splunk](splunk.md), [elastic](elastic.md), [sumo-logic](sumo-logic.md).

**Open questions / to verify** — Standalone (non-Falcon) LogScale availability/pricing today; current Charlotte AI agentic feature GA status.

## Sources
- [Falcon LogScale (Next-Gen SIEM)](https://www.crowdstrike.com/en-us/platform/next-gen-siem/falcon-logscale/) — fetched 2026-06-28 — supports: CrowdStrike ownership, index-free SIEM data plane, Charlotte AI; confidence: high
- [CrowdStrike Redefines True XDR With Humio Acquisition](https://www.crowdstrike.com/en-us/blog/taking-our-falcon-xdr-platform-further/) — fetched 2026-06-28 — supports: Humio acquired by CrowdStrike (~$400M); confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); confirmed CrowdStrike ownership (public, CRWD), verified Humio acquisition (2021, ~$400M), set ownership=public/high, filled Next-Gen SIEM one-liner + Charlotte AI angle. 2 sources cached.
