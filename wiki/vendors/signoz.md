---
title: SigNoz
type: vendor
name: SigNoz
slug: signoz
aka: [SigNoz Inc., SigNoz/signoz]
primary_category: siem-soc
also_listed_in: [llm-observability]
website: https://signoz.io
founded: 2020
hq: San Francisco, CA (US) & Bengaluru, India
ownership_state: oss-vendor-backed
owner: null
ownership_note: Independent, VC-backed open-core company (SigNoz Inc.); Y Combinator alum. ~$6.5M raised total — $1.1M post-YC (2021) plus a $5.4M round announced 2023-09-28 led by SignalFire. No later round and no M&A found as of 2026-08-16.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$6.5M
last_funding: $5.4M, announced 2023-09-28 (SignalFire lead; Uncorrelated Ventures, Alumni Ventures, angels incl. Tom Preston-Werner)
market_position: {siem-soc: niche-specialist, llm-observability: challenger}
deployment_model: [saas, self-hosted, hybrid, on-prem]
form_factor: [platform, api]
data_leaves_tenancy: partial
integrations: [opentelemetry, clickhouse, prometheus, kubernetes, opamp, mcp]
mcp_support: server
certifications: [soc2-type2, hipaa]
pricing_model: usage-based ($0.30/GB logs and traces, $0.10/M metric samples; Teams from $49/mo, Enterprise from $4,000/mo); Community Edition free
fs_traction: unverified
target_customer: Engineering / platform teams wanting a self-hostable, OpenTelemetry-native alternative to Datadog
last_verified: 2026-08-16
verify_after: null
tags: [observability, opentelemetry, logging, open-source, clickhouse, apm, llm-observability, mcp-server]
sources:
  - {claim: license-repo-traction, url: "https://github.com/SigNoz/signoz", date: 2026-08-16, confidence: high}
  - {claim: pricing-tiers-retention, url: "https://signoz.io/pricing/", date: 2026-08-16, confidence: high}
  - {claim: product-scope-and-ai-features, url: "https://signoz.io/", date: 2026-08-16, confidence: medium}
  - {claim: funding-history, url: "https://signoz.io/blog/signoz-funding/", date: 2026-08-16, confidence: high}
---

# SigNoz

> **Scope caveat, stated up front:** SigNoz is an **observability** platform, not a
> SIEM. It is filed under
> [siem-soc](../categories/siem-soc.md) because that category is
> "Enterprise Logging / SIEM / SOC" and SigNoz is a serious answer to the
> *enterprise logging* half — the same slot [elastic](elastic.md) occupies when
> teams self-host ELK for log retention. It ships **no detection content**: no
> rule packs, no ATT&CK mappings, no case management, no SOAR. Do not put it in a
> SIEM bake-off against [microsoft-sentinel](microsoft-sentinel.md) or
> [splunk](splunk.md) without that caveat. See open taxonomy questions below.

**One-liner** — Open-source, OpenTelemetry-native observability on ClickHouse:
logs, metrics, traces, APM and dashboards in one self-hostable tool, sold as the
Datadog alternative whose bill does not scale with hosts or users.

**Categories** — [siem-soc](../categories/siem-soc.md),
[llm-observability](../categories/llm-observability.md)

## What it does

SigNoz collects application and infrastructure telemetry over **OpenTelemetry** —
its only ingestion story, deliberately — and stores it in **ClickHouse**, a
columnar database, giving you one queryable backend for the three signals instead
of a log tool plus a metrics tool plus a tracing tool. On top of that sit APM
(latency/error/throughput per service), distributed tracing with flamegraphs, log
management, infrastructure monitoring, exceptions, dashboards and alerting.

Querying is deliberately multi-level: a point-and-click builder, **PromQL** for
metrics, and raw **ClickHouse SQL** when you need it. Telemetry pipelines are
configurable in-product via **OpAmp**, so you can drop or transform data at the
collector without redeploying agents. The site claims 50+ data-source
integrations.

Two 2026-era additions matter for this wiki:

- **LLM/AI observability** — tracing for AI applications built on OpenTelemetry's
  GenAI semantic conventions, which is why the page is cross-listed to
  [llm-observability](../categories/llm-observability.md). It is the generalist's
  version of that category: traces, spans and cost/latency for model calls, not
  prompt management, evals or scoring the way [langfuse](langfuse.md) or
  [braintrust](braintrust.md) do it.
- **"Agent Native Observability"** — a **SigNoz MCP server** that lets coding
  agents (Claude Code, Cursor) query your observability data directly, plus an AI
  assistant called **Noz** in SigNoz Cloud. Useful and also worth a threat-model
  note: an MCP server that exposes production telemetry to an agent is a
  sensitive-data source, and should be gated like one — see
  [mcp-gateway](../categories/mcp-gateway.md).

## Where it sits in the stack

Foundation layer, [siem-soc](../categories/siem-soc.md), on the **logging** side of
that category rather than the detection side. Its role is **detective and
out-of-band**: it is where telemetry lands so you can ask what happened. For AI
specifically it is a plausible sink for [ai-gateway](../categories/ai-gateway.md)
traces — [bifrost](bifrost.md), [litellm](litellm.md) and
[portkey](portkey.md) all emit OpenTelemetry, which SigNoz ingests natively with
no adapter.

What it is **not**: it does not correlate security events, score user behaviour,
run playbooks, or hold the case record. If SigNoz is your log store, your detection
and response still live in a real SIEM or with an MDR provider. The realistic
pattern for a fund is SigNoz for engineering telemetry alongside
[microsoft-sentinel](microsoft-sentinel.md) or equivalent for security — two
systems, not one.

## Deployment & architecture

- **Community Edition** — free, self-hosted, MIT-licensed core (see the licence
  gotcha below). Runs on your own infrastructure; nothing leaves your tenancy.
- **SigNoz Cloud (Teams)** — managed, with a choice of **US, EU or India** data
  region. Data does leave your tenancy here.
- **Enterprise** — dedicated cloud environment, **bring-your-own-cloud managed by
  SigNoz**, or self-hosted with a support contract. The BYOC and supported
  self-hosted options are the ones that matter to a regulated firm.
- `data_leaves_tenancy: partial` because it is entirely a function of which of
  those you pick.
- **Retention is a purchased parameter**, not a fixed policy: logs and traces at
  15 / 30 / 90 / 180 days or 1 year; metrics at 1 / 3 / 6 or 13 months. For
  anything with a records-retention obligation, note that a year is the published
  ceiling on the log/trace side.

## Positioning & differentiators

- **OpenTelemetry-native by conviction, not by adapter.** SigNoz's core argument
  against [datadog](datadog.md), New Relic and Dynatrace is that those absorbed
  OTel into proprietary agents and pricing, while SigNoz stores OTel semantics
  end-to-end — so your instrumentation is portable out of SigNoz too. That is a
  real lock-in argument and the most credible thing it says.
- **Pricing shape, not just level.** No per-host and no per-user charge, and no
  custom-metric surcharge — the two line items that make Datadog bills
  unpredictable. You pay per GB ingested and per million metric samples.
- **Self-hostable at full function**, which is the differentiator versus every
  SaaS observability vendor and the reason it shows up in regulated shops.
- **vs [elastic](elastic.md)** — the closest comparison in this category. Both are
  open-source-rooted and self-hostable. Elastic brings a real security product
  (Elastic Security, detection rules, SIEM positioning) and a much larger
  ecosystem; SigNoz brings a far simpler operational story (ClickHouse, one
  backend, no cluster-tuning folklore) and OTel-first design. If you want SIEM,
  Elastic. If you want engineering telemetry without operating Elasticsearch,
  SigNoz.
- **Very large OSS footprint for its funding** — 31.8k stars, 2.4k forks, weekly
  releases. Community traction substantially outruns the ~$6.5M raised.

## Ownership, funding & M&A

**Independent, VC-backed, open-core.** Founded by **Pranay Prateek** and **Ankit
Nayan**; **Y Combinator** alum; US and Bengaluru presence. Repo dates to
2021-01-03, company activity from 2020.

Funding is **~$6.5M total**: ~$1.1M post-YC in 2021 (SignalFire plus angels), then
**$5.4M announced 2023-09-28** led by **SignalFire**, with Uncorrelated Ventures,
Alumni Ventures, and angels including GitHub co-founder **Tom Preston-Werner**. As
of 2026-08-16, searches found **no Series B and no acquisition**.

The honest read: the last raise was nearly three years ago against a project with
31k stars and a weekly release cadence. Either cloud revenue is carrying the
company or another round is due; there is no public evidence either way. That is
the main viability question, and the mitigant is the same one as always for
open-core — the MIT-licensed core self-hosts, so a bad outcome for SigNoz Inc.
does not immediately strand your telemetry.

## Who should choose them / anti-fit

- **Good fit:** an engineering-led firm that wants unified logs/metrics/traces,
  refuses to send telemetry to a US SaaS or needs a specific data region, is
  already instrumenting with OpenTelemetry, and is tired of per-host observability
  bills. Also a reasonable sink for AI-gateway traces without buying a dedicated
  LLM-observability tool.
- **Anti-fit:** anyone shopping for a **SIEM**. If the requirement is security
  detection, correlation, case management, compliance reporting or a SOC workflow,
  this is the wrong category of product entirely — see
  [microsoft-sentinel](microsoft-sentinel.md), [splunk](splunk.md),
  [google-secops](google-secops.md). Also an anti-fit for a small team with no
  appetite to run ClickHouse, and — critically — for anyone who needs **audit
  logs, custom RBAC roles or multi-tenancy**, since all three are marked
  *COMING SOON* on the Enterprise tier and therefore ship at no price today
  (checked 2026-08-22).

## Known weaknesses / gotchas

- **"Open source" is open *core*, and the split lands exactly where an enterprise
  cares.** The root LICENSE puts everything outside `ee/` and `cmd/enterprise/`
  under **MIT**, and everything inside `ee/` under a separate SigNoz enterprise
  licence. The `ee/` tree includes **`authn`, `authz`, `auditor`, `anomaly`,
  `gateway`, `licensing` and `querier`** — i.e. authentication, authorization,
  audit logging and anomaly detection are the paid side. GitHub reports the repo
  licence as "NOASSERTION" for this reason. **But note what `ee/auditor` is not:**
  code in the repository is not evidence a feature ships — SigNoz's own pricing
  table marks Audit Logs *COMING SOON* even on Enterprise (see below). Follow the
  price list, not the directory tree.
- **Not a SIEM** — restated because it is the most likely way to misuse this page.
  No detection rules, no correlation content, no case management, no SOAR, no UEBA.
- **Still pre-1.0** at v0.137.1 (2026-08-14), with ~1,500 open issues. Release
  cadence is weekly, which is a strength and a churn risk.
- **Audit logs do not exist yet, at any price.** The pricing table marks
  **Audit Logs**, **Finer RBAC with custom roles** and **Multi-tenancy** as
  *COMING SOON* on the **Enterprise** tier (checked 2026-08-22) — so the
  $4,000/mo minimum does not currently buy an audit trail. For a regulated firm
  this is the single most important line on the page: if you need to evidence who
  looked at which telemetry, SigNoz cannot do it today, and there is no published
  date. Ask for a commitment in writing before it becomes a control assumption.
- **Access control tiers better than you might expect, though.** Plain **SSO is on
  all three tiers including the free Community edition**, and **SAML starts at the
  $49/mo Teams tier** — not at Enterprise. The $4,000/mo minimum buys dedicated
  environments, BYOC, support and volume terms; it is not the price of admission
  for basic single sign-on.
- **Certifications are claimed on the website, not evidenced.** SOC 2 Type II and
  HIPAA are asserted; no report period, auditor or trust-centre artefact was
  retrieved. Verify before relying on them.
- **You own the ClickHouse.** Self-hosting means operating and scaling a columnar
  database under high-cardinality telemetry — simpler than Elasticsearch, not free.

## Compliance & FS traction

Website claims **SOC 2 Type II** and **HIPAA**, with SSO/SAML, query API keys and
US/EU/India data residency. No FedRAMP, no ISO 27001 found. Note the gap between
that compliance posture and the feature table: SigNoz markets a SOC 2 Type II
while its own **Audit Logs** row reads *COMING SOON* on every tier — its
certification covers SigNoz's operation of the service, not your ability to
produce an access audit trail out of it. **No named financial-services
customers** and no FS case studies located —
`fs_traction: unverified`. Nothing about the product assumes enterprise scale in
the negative sense: a mid-size firm can run it.

## Commercial

Community Edition free (MIT core). **Teams Cloud from $49/mo** (site notes a cut
from $199), usage-based: **$0.30/GB ingested for logs**, **$0.30/GB for traces**,
**$0.10 per million metric samples**; the $49 includes roughly 163 GB of
logs/traces or ~490M metric samples. Teams also carries **SAML**; plain **SSO is
available on every tier, Community included**. **Enterprise from $4,000/mo
minimum**, adding dedicated environments, bring-your-own-cloud or self-host-with-
support, dedicated support, volume discounts, BAAs, migration assistance and an
SLA — but *not* audit logs, custom RBAC roles or multi-tenancy, all three of
which are marked *COMING SOON* (checked 2026-08-22). Startups under three years
old with <30 staff and <$6M raised get 50% off.

## Competitors / alternatives

[elastic](elastic.md) (closest, and the one with an actual security product),
[splunk](splunk.md), [sumo-logic](sumo-logic.md),
[crowdstrike-logscale](crowdstrike-logscale.md),
[microsoft-sentinel](microsoft-sentinel.md), [google-secops](google-secops.md) in
[siem-soc](../categories/siem-soc.md); [datadog](datadog.md),
[langfuse](langfuse.md), [helicone](helicone.md),
[arize-phoenix](arize-phoenix.md) in
[llm-observability](../categories/llm-observability.md). Grafana/Loki/Tempo is the
other obvious OSS alternative and has no page here.

## Open questions / to verify

- **Category fit.** SigNoz stretches `siem-soc` toward pure observability. Either
  the category is genuinely "enterprise logging *or* SIEM" (in which case
  [datadog](datadog.md) and Grafana arguably belong too), or SigNoz should move.
  Raised in `taxonomy-gaps.md`; flagged for the human.
- SOC 2 Type II report period and auditor; HIPAA attestation basis. Claimed on the
  site, not evidenced.
- **Ship date for Audit Logs, Finer RBAC and Multi-tenancy.** All three are
  *COMING SOON* on Enterprise with no published timeline. For a regulated buyer
  this is the gating question, not a nice-to-have.
- Whether any funding has closed since 2023-09 — nothing public, and the gap is
  large enough to matter for vendor-risk assessment.
- Headcount and cloud-revenue signal; no reliable figure found.
- Which specific capabilities moved into `ee/` over time — the split is documented
  by directory, not by a feature-comparison table.
- Real-world ingest ceilings for self-hosted ClickHouse at, say, 1 TB/day; no
  independent scaling write-up found.
- Whether the SigNoz MCP server supports scoped/read-only credentials, given it
  exposes production telemetry to an agent.
- Any financial-services references at all.

## Sources

- [SigNoz/signoz (GitHub repo, LICENSE, `ee/` tree via API)](https://github.com/SigNoz/signoz) — fetched 2026-08-16 — supports: created 2021-01-03, 31,847 stars / 2,426 forks / 1,509 open issues, v0.137.1 (2026-08-14), MIT-core-plus-`ee/` licence split and the contents of `ee/`; confidence: high (primary, machine-read).
- [SigNoz pricing](https://signoz.io/pricing/) — fetched 2026-08-16, **re-read row by row 2026-08-22** — supports: $0.30/GB logs and traces, $0.10/M metric samples, $49/mo Teams, $4,000/mo Enterprise minimum, retention options, BYOC/self-hosted-with-support, startup discount; and the corrected feature tiering — SSO on all three tiers, SAML on Teams and Enterprise, Audit Logs / Finer RBAC with custom roles / Multi-tenancy all *COMING SOON* on Enterprise; confidence: high (vendor's own price list). Cached: `raw/sources/2026-08-22--signoz--pricing-table-feature-tiers.md`.
- [SigNoz homepage](https://signoz.io/) — fetched 2026-08-16 — supports: OpenTelemetry-native positioning, ClickHouse backend, APM/logs/traces/infra scope, PromQL/ClickHouse querying, OpAmp pipelines, LLM observability, MCP server and "Noz", SOC 2 / HIPAA claims, US/EU/India regions, competitive framing vs Datadog/New Relic/Grafana/Dynatrace; confidence: medium (vendor marketing).
- [We've raised $6.5M to build the future of open source observability (SigNoz blog)](https://signoz.io/blog/signoz-funding/) — fetched 2026-08-16 — supports: $6.5M total, $5.4M round, SignalFire lead, YC lineage, founders; confidence: high (primary).
- [SigNoz raises $5.4 Mn in a new round (Entrackr, 2023-09)](https://entrackr.com/2023/09/signoz-raises-5-4-mn-in-a-new-round/) — fetched 2026-08-16 — supports: independent corroboration of the 2023-09-28 round, investor list including Tom Preston-Werner; confidence: medium (press).

## History

- [2026-08-16] Page created and researched in one pass (user-requested addition, not a seed/CSV row). Filed `siem-soc` as requested with an explicit scope caveat — SigNoz is observability/enterprise logging, not a SIEM (no detection content, no case management, no SOAR); cross-listed to `llm-observability` on the strength of its OTel GenAI tracing. Established: independent open-core, ~$6.5M raised, last round 2023-09-28 (SignalFire), no M&A; MIT core with `ee/` (authn/authz/auditor/anomaly) under a separate enterprise licence; SSO/SAML behind a $4,000/mo minimum. Category-fit question raised in `taxonomy-gaps.md`. 1 source cached.
- [2026-08-22] **Correction (pricing tiers).** Two claims from the 2026-08-16 build were wrong; both came from a summarized read of the pricing page rather than the feature table, and both drove buying advice. (1) The page said SSO/SAML was "gated behind the $4,000/mo Enterprise minimum, a steep step from the $49/mo Teams tier" — in fact **SSO is on all three tiers including free Community, and SAML starts at Teams ($49/mo)**. (2) The page advised budgeting for Enterprise "if you need SSO/SAML and audit trails" — in fact **Audit Logs, Finer RBAC with custom roles and Multi-tenancy are all marked *COMING SOON* on Enterprise**, so no tier buys an audit trail today. Re-read https://signoz.io/pricing/ row by row on 2026-08-22 and corrected the anti-fit line, the open-core bullet, the weaknesses bullets, Compliance and Commercial. Also recorded that the `ee/auditor` package existing in the repo is not evidence the feature ships. The `siem-soc` filing and the observability-not-a-SIEM scope caveat are unchanged and remain correct. Source cached.
