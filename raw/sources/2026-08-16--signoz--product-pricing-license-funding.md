# SigNoz — product, pricing, license, funding

- URL: https://signoz.io/ + https://signoz.io/pricing/ + https://github.com/SigNoz/signoz
  (repo, LICENSE, `ee/` tree via GitHub API) + https://signoz.io/blog/signoz-funding/
  and press coverage (entrackr, BW Disrupt) for the funding history
- Fetched: 2026-08-16
- Good for: what SigNoz is (and is *not*), OSS licensing split, deployment options,
  list pricing, certifications, ownership/funding.

## Facts

**Identity.** SigNoz is an **open-source, OpenTelemetry-native observability
platform** — logs, metrics, traces, APM, distributed tracing, infra monitoring,
dashboards, alerts and exceptions in one tool, backed by **ClickHouse**. Positions
explicitly as an open-source alternative to **Datadog, New Relic, Grafana and
Dynatrace**. Founded by **Pranay Prateek** and **Ankit Nayan**; **Y Combinator**
alum (2021 batch), US + India (Bengaluru) team.

**Repo metadata (GitHub API, 2026-08-16).**
- `SigNoz/signoz`, created **2021-01-03**, last push 2026-08-15 (very active).
- **31,847 stars, 2,426 forks, 1,509 open issues.** Not archived.
- Primary language TypeScript (frontend) over a Go query service.
- Releases roughly weekly: **v0.137.1 (2026-08-14)**, v0.137.0 (2026-08-12),
  v0.136.1 (2026-08-05). Still pre-1.0 versioning.

**License — open core, not uniformly MIT.** The root `LICENSE` states: everything
under **`ee/` and `cmd/enterprise/` is under the separate `ee/LICENSE`** (SigNoz
enterprise license); everything else is **MIT ("MIT Expat")**. The `ee/` tree
contains `authn`, `authz`, `auditor`, `anomaly`, `gateway`, `licensing`,
`querier`, `query-service`, `metercollector`, `zeus` and more — i.e. **SSO/SAML,
authorization, audit and anomaly detection are on the enterprise side.** GitHub's
license detector reports "NOASSERTION" for this reason.

**Deployment options.** SigNoz Cloud (US, EU, India regions); self-hosted
community edition (OSS); and, on Enterprise, a dedicated cloud environment,
**bring-your-own-cloud managed by SigNoz**, or self-hosted with a support contract.

**Pricing (signoz.io/pricing, 2026-08-16).**
- Community Edition: free, self-managed.
- **Teams Cloud from $49/mo** (site notes this was reduced from $199), usage-based:
  **$0.30/GB ingested for logs**, **$0.30/GB for traces**, **$0.10 per million
  metric samples**. The $49 includes ~163 GB of logs/traces or ~490M metric
  samples. No per-user or per-host charge; no custom-metric surcharge.
- Retention is selectable: logs/traces 15 / 30 / 90 / 180 days or 1 year; metrics
  1 / 3 / 6 / 13 months.
- **Enterprise: minimum $4,000/mo**, adds **SSO/SAML**, dedicated support, volume
  discounts, BAAs, migration help, SLA with developer pairing.
- Startup discount (≤3 yrs old, <30 employees, <$6M raised): 50% off, $19/mo.

**Compliance.** Site claims **SOC 2 Type II** and **HIPAA**, SSO/SAML, query API
keys, and data-residency choice (US/EU/India). Reports not public; not fetched.

**AI-adjacent features (2026).** "LLM/AI observability" for tracing AI application
performance; **"Agent Native Observability"** — a **SigNoz MCP server** so coding
agents (Claude Code, Cursor) can query observability data, plus an AI teammate
called **"Noz"** in SigNoz Cloud. Claims 50+ data-source integrations and native
OpenTelemetry semantic-convention support, signal correlation, span events and
deployment markers.

**Scope caveat — this is observability, not a SIEM.** Nothing on the product or
pricing pages offers security detection content: no bundled detection rules, no
correlation/alerting content packs mapped to ATT&CK, no case management, no SOAR
playbooks, no UEBA. It is a **logging/telemetry backend** (the ELK-shaped half of
the "Enterprise Logging / SIEM / SOC" category), not a detection platform.

**Ownership & funding.**
- **Independent, VC-backed. Total raised ~$6.5M**, all of it pre-Series-B.
- **$1.1M** previously-undisclosed round after Y Combinator (2021), SignalFire +
  angels.
- **$5.4M** round announced **2023-09-28**, led by **SignalFire**, with
  Uncorrelated Ventures, Alumni Ventures, and angels including GitHub co-founder
  Tom Preston-Werner. SigNoz's own blog frames the combined total as **$6.5M**.
- Searches on 2026-08-16 found **no Series B and no M&A** — last round remains
  2023-09. That is a ~3-year-old last raise against a large OSS footprint; treat
  runway/commercial traction as an open question.
