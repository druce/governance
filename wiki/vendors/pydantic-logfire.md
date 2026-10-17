---
title: Pydantic Logfire
type: vendor
name: Pydantic Logfire
slug: pydantic-logfire
aka: [Logfire, Pydantic]
primary_category: llm-observability
also_listed_in: []
website: https://pydantic.dev/logfire
founded: 2022
hq: United Kingdom (distributed team across US and Europe)
ownership_state: independent
owner: null
ownership_note: "Product of Pydantic (Pydantic Services Inc.), the company behind the open-source Pydantic library (2017) and Pydantic AI. VC-backed: $4.7M seed (Sequoia) and $12.5M Series A led by Sequoia with Partech and Irregular Expression (2024-10-01). No later round found."
acquisition: {announced: null, closed: null, price: null}
funding_total: "~$17.2M disclosed"
last_funding: "Series A $12.5M, Sequoia lead, 2024-10-01"
market_position: {llm-observability: challenger}
deployment_model: [saas, self-hosted]
form_factor: [sdk, platform]
data_leaves_tenancy: partial
integrations: [opentelemetry, pydantic-ai, openai, anthropic, langchain, llamaindex, litellm, vercel-ai-sdk, okta, entra, keycloak]
mcp_support: server
certifications: [soc2-type2, hipaa-baa]
pricing_model: usage
fs_traction: claimed
target_customer: Python-heavy engineering teams, startup to enterprise, wanting one OTel backend for app and AI telemetry
last_verified: 2026-10-16
verify_after: 2027-04-16
tags: [opentelemetry, apm, agent-tracing, evals, python, sql, aie-nyc-2026]
sources:
  - {claim: "OTel-based AI + general observability; agent/LLM tracing with token cost; offline and online evals; SQL querying; MCP server; MIT SDKs, closed-source server; named customers incl. Pictet", url: "https://pydantic.dev/logfire", date: 2026-10-16, confidence: medium}
  - {claim: "Plans Personal free / Team $49 / Growth $249 / Enterprise custom; $2 per extra million records; Cloud (EU/US), Dedicated (single-tenant, CMEK), Self-hosted via Helm; SOC 2 Type II; HIPAA BAAs; SSO/SCIM on Enterprise", url: "https://pydantic.dev/pricing", date: 2026-10-16, confidence: high}
  - {claim: "$12.5M Series A led by Sequoia; $4.7M seed; company launched 2022, UK-based; Logfire GA 2024-10-01", url: "https://techcrunch.com/2024/10/01/sequoia-backs-pydantic-to-expand-beyond-its-open-source-data-validation-framework", date: 2024-10-01, confidence: high}
  - {claim: "Pydantic AI Gateway merged into Logfire; inherits Logfire SSO, roles, permissions", url: "https://pydantic.dev/articles/gateway-merging-into-logfire", date: 2026-03-23, confidence: high}
  - {claim: "Pydantic Silver sponsor at AI Engineer New York 2026", url: "https://ai.engineer/nyc", date: 2026-10-16, confidence: high}
---

# Pydantic Logfire

> Primary category: [llm-observability](../categories/llm-observability.md). Slugged by product because Logfire is what buyers shop for; the company is Pydantic.

**One-liner** — A full-stack observability platform built on OpenTelemetry, from the team behind the Pydantic library. It puts LLM and agent traces in the same trace as your API calls and database queries, and lets you query everything in SQL.

**What it does** — Logfire takes standard OpenTelemetry traces, logs and metrics and adds AI-specific views. Agent runs, model calls, tool calls and retrieval steps appear inside the same trace as the surrounding application work, with token usage and cost where the framework reports them. Evals come in three layers: programmatic checks, narrow LLM judges and human review. They run offline against datasets or online against production traffic, with scores stored as span attributes. Data is queried in **Postgres-flavoured SQL** (vendor-named "FusionFire" engine on Apache DataFusion), and a **Logfire MCP server** gives coding agents the same query interface. Since **2026-03-23** the former **Pydantic AI Gateway** is part of Logfire, so routing, playground and tracing share one account and one set of access controls. Full gateway access is a paid add-on.

**Naming / provenance** — Samuel Colvin started the Pydantic open-source data-validation library in **2017**. TechCrunch reported users including Meta, Nvidia, Netflix, Google and OpenAI. The **company launched in 2022**. Logfire went into open beta in 2024 and **GA on 2024-10-01**. Pydantic also builds **Pydantic AI**, an agent framework, which Logfire instruments natively. Don't confuse it with other "Logfire" log products.

**Ownership & viability** — `independent`, VC-backed. **$4.7M seed (Sequoia)** and **$12.5M Series A led by Sequoia** with Partech and Irregular Expression (2024-10-01), about $17.2M disclosed in total. No later round was found as of 2026-10-16. Headcount was 13 at the Series A. The current figure is unverified. Viability rests on the open-source franchise: the Pydantic library gives the company distribution few observability startups have. Acquisition risk is moderate, since observability is consolidating (Langfuse went to ClickHouse, see [langfuse](langfuse.md)). The SDKs are MIT and the data is standard OTel, so leaving would be relatively easy.

**Positioning & differentiators** — `challenger`: an established, well-distributed product competing for the "AI observability plus general APM" slot against incumbents and AI-native specialists. It is neither the default nor a niche tool.
- **Versus [datadog](datadog.md) / [sentry](sentry.md):** same idea of AI traces correlated with the rest of the stack. Logfire is OTel-native end to end, offers SQL over raw telemetry, and can be **self-hosted** (Enterprise), which Datadog cannot. TechCrunch described it as a simpler alternative to Datadog aimed initially at smaller teams.
- **Versus [langfuse](langfuse.md) / [langsmith](langsmith.md) / [arize-phoenix](arize-phoenix.md):** those are LLM-specific tools; Logfire is general observability with first-class LLM views. If you want one backend for app and AI telemetry, Logfire fits better. If you want deep prompt management and annotation workflows, the LLM-specific tools are more mature (prompt management in Logfire was not verified).
- **Versus [signoz](signoz.md):** both are OTel-native. SigNoz is open source end to end, while the Logfire server is closed source. Logfire has richer AI-specific views and evals.

**Who should choose them / anti-fit** — Fits a **Python-heavy quant or platform team**, especially one already using Pydantic AI, that wants a single OTel backend for services and agents. Also one that likes SQL as the query language and needs EU hosting, single-tenant or self-hosted options. **Anti-fit:** a firm standardised on Datadog or Splunk that won't run a second observability backend. A firm wanting a fully open-source server (use SigNoz or Langfuse). A firm whose main need is eval experiments and prompt versioning rather than tracing.

**Known weaknesses / gotchas** —
- Pricing counts every span, log and metric record. Verbose instrumentation of agents, which produce many spans per run, can add up beyond the included 10M records per month.
- The server is closed source. Self-hosting is Enterprise-only and comes with "your compliance, our help": you own the controls.
- Default retention is 30 days on Personal and Team, up to 90 days on Growth. That is not enough for records-retention purposes without Enterprise terms or export.
- Pydantic also notes a "Data Loss Prevention" add-on. Whether prompts and PII are scrubbed by default was not verified.

**Deployment & data handling** — Three options. **Cloud**: multi-tenant, EU or US region. **Dedicated**: single-tenant, managed by Pydantic, any GCP region, CMEK. **Self-hosted**: open-source Helm chart on your Kubernetes, needs Postgres and S3-compatible storage, and data stays on-prem. Self-hosted is Enterprise only. `data_leaves_tenancy: partial`: on Cloud and Dedicated, traces (which can contain prompts and outputs) go to Pydantic-operated infrastructure. Self-hosted keeps them in-house. Training-use terms were not found. It works out-of-band via SDK and OTLP export.

**Integrations & partnerships** — First-party SDKs for Python, JS/TS and Rust (MIT). Any OTel-emitting language works (Go, Java, .NET and others). AI integrations: Pydantic AI, OpenAI, Anthropic, LangChain, LlamaIndex, LiteLLM, Vercel AI SDK. Enterprise SSO: Okta, Microsoft Entra ID, Keycloak, SAML; plus SCIM, custom roles and an audit-log API. MCP server for querying telemetry. [datadog](datadog.md) lists Pydantic among its own auto-instrumentation targets, which reflects how common Pydantic is in AI stacks. Pydantic was a Silver sponsor at AI Engineer New York 2026 (no session on the agenda).

**Compliance & FS traction** — **SOC 2 Type II** (Cloud and Dedicated). **HIPAA BAAs** on Growth and Enterprise. GDPR DPA and an EU data region. FS traction is `claimed`: **Pictet** (Swiss private bank and asset manager) and **Boosted.ai** (investment-research AI) appear among named customers on the vendor page. There is no published case study detailing their use. Fit for a hedge fund is reasonable: pricing is seat-light, and the self-hosted and EU options address residency.

**Commercial** — Usage-based with platform tiers: **Personal free** (10M records/month, hard cap), **Team $49/month** (5 seats, 30-day retention), **Growth $249/month** (unlimited seats, up to 90-day retention), **Enterprise custom** (invoice, Dedicated or self-hosted, SSO/SCIM, longer retention). Overage is **$2 per additional million records**. No effective date is shown on the pricing page.

## Open questions

- Default handling of prompts/PII in traces, and what the DLP add-on does.
- Prompt management and annotation-queue depth compared with Langfuse and LangSmith.
- Current headcount and any funding after the 2024 Series A.
- Details of the Pictet deployment (logo only).
- Training-use and sub-processor terms for Cloud.

## Sources

- [Pydantic Logfire product page](https://pydantic.dev/logfire) — fetched 2026-10-16 — supports: features, SDKs/licensing, named customers, compliance summary; confidence: medium (vendor marketing)
- [Pydantic pricing](https://pydantic.dev/pricing) — fetched 2026-10-16 — supports: plan prices, overage, hosting tiers, compliance by tier, SSO; confidence: high
- [TechCrunch, 2024-10-01](https://techcrunch.com/2024/10/01/sequoia-backs-pydantic-to-expand-beyond-its-open-source-data-validation-framework) — fetched 2026-10-16 — supports: funding, founding, HQ, Logfire GA; confidence: high
- [Pydantic AI Gateway is moving to Logfire (2026-03-23)](https://pydantic.dev/articles/gateway-merging-into-logfire) — via search 2026-10-16 — supports: gateway merge; confidence: high
- [AI Engineer New York 2026](https://ai.engineer/nyc) — fetched 2026-10-16 — supports: Silver sponsor; confidence: high
- Cached: `raw/sources/2026-10-16--pydantic-logfire--product-pricing-funding.md`

## History

- [2026-10-16] Page created via wiki-create + wiki-research (AIE NYC 2026 attendee scan).
