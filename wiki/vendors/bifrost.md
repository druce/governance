---
title: Bifrost
type: vendor
name: Bifrost
slug: bifrost
aka: [Maxim Bifrost, Bifrost AI Gateway, maximhq/bifrost, getbifrost]
primary_category: ai-gateway
also_listed_in: []
website: https://www.getmaxim.ai/bifrost
founded: 2025
hq: San Francisco, CA (US) & India
ownership_state: oss-vendor-backed
owner: Maxim AI
ownership_note: Apache-2.0 open-source gateway built and maintained by Maxim AI (maximhq); repo created 2025-03-19. Maxim AI is independent and VC-backed ($3M seed 2024-06-18, Elevation Capital); no later round and no M&A found as of 2026-08-16.
acquisition: {announced: null, closed: null, price: null}
funding_total: ~$3M (at parent Maxim AI)
last_funding: Seed $3M (2024-06-18, Elevation Capital) — raised by Maxim AI, not Bifrost
market_position: {ai-gateway: challenger}
deployment_model: [self-hosted, saas, hybrid]
form_factor: [inline-proxy, api, sdk]
data_leaves_tenancy: partial
integrations: [openai, anthropic, aws-bedrock, google-vertex, azure-openai, cohere, mistral, groq, ollama, cerebras, opentelemetry, prometheus, datadog, maxim]
mcp_support: gateway
certifications: []
pricing_model: open-core (Apache-2.0 self-hosted; paid enterprise/managed tiers, no list price)
fs_traction: unverified
target_customer: Platform / AI-engineering teams running LLM traffic at scale
last_verified: 2026-08-16
verify_after: null
tags: [ai-gateway, llm-proxy, open-source, golang, mcp, semantic-cache, maxim-ai]
sources:
  - {claim: license-repo-traction, url: "https://github.com/maximhq/bifrost", date: 2026-08-16, confidence: high}
  - {claim: features-benchmarks-tiers, url: "https://www.getmaxim.ai/bifrost", date: 2026-08-16, confidence: medium}
  - {claim: oss-vs-enterprise-split, url: "https://docs.getbifrost.ai/", date: 2026-08-16, confidence: medium}
---

# Bifrost

> This page covers **Bifrost**, the AI gateway, as its own shopping unit. The
> company behind it has a separate page — [maxim-ai](maxim-ai.md), whose centre of
> gravity is evaluation, simulation and LLM observability. Buyers shop for Bifrost
> against [litellm](litellm.md), not against Maxim's eval suite, so it gets a
> product slug (see `log.md`, 2026-08-16). Primary category:
> [ai-gateway](../categories/ai-gateway.md).

**One-liner** — An Apache-2.0, Go-based LLM gateway that fronts ~20+ model
providers behind one OpenAI-compatible API, pitched squarely at
[litellm](litellm.md) on performance — microsecond-scale added latency, on
vendor-run benchmarks against a mocked provider — plus virtual-key budgets,
semantic caching and OpenTelemetry, with clustering, guardrails and the MCP
gateway held back for the paid tier.

**Categories** — [ai-gateway](../categories/ai-gateway.md)

## What it does

Bifrost is a self-hostable proxy that presents a single **OpenAI-compatible
endpoint** in front of every model provider you use, so application code stops
holding per-provider keys and SDKs. It ships as a Go binary (start it with `npx`
or Docker) with an HTTP transport and web UI, or as a **Go SDK** embedded
in-process.

The open-source core covers the gateway basics:

- **Unified provider interface** — OpenAI, Anthropic, AWS Bedrock, Google Vertex,
  Azure, Cohere, Mistral, Groq, Cerebras, Ollama and others, with multimodal
  (text/image/audio) and streaming support. Provider counts are inconsistent
  across Maxim's own surfaces — "8+", "20+" and "23+" appear on the product page,
  docs and README respectively, all against a "1000+ models" headline.
- **Reliability** — automatic failover between providers and weighted
  load balancing across keys.
- **Governance** — **virtual keys** are the primary governance object, with
  hierarchical budgets and rate limits stacked across virtual key → team →
  customer, plus usage and cost tracking.
- **Semantic caching** — cache hits on semantically similar prompts, sold as the
  main cost lever.
- **Observability** — Prometheus metrics and **OpenTelemetry** export out of the
  box, a built-in dashboard, and a first-party hook into
  [maxim-ai](maxim-ai.md)'s observability product.
- **Plugins** — middleware in Go or **WebAssembly** for analytics, governance and
  custom logic; the semantic cache, telemetry and a request mocker are themselves
  plugins.

Held behind the **enterprise licence**: clustering/HA, adaptive load balancing with
predictive scaling, the **MCP Gateway** (agent tool execution), content-safety
**guardrails** backed by AWS/Azure/Google, Okta/Entra SSO, RBAC, VPC isolation,
the **Audit Logs** feature, the Datadog connector, and automated log export to a
data lake.

Two different logs, easily confused, and the distinction matters: the **request
log** — every prompt and response through the gateway — is in the **free
Apache-2.0 build**. The enterprise **Audit Logs** feature is something else
entirely: per Bifrost's docs it records *"administrative activity so operators can
review who changed what, when it happened, and which resource was affected"*
(create/update/delete/authenticate/authorize/export/import events). That is
**configuration-change history for the gateway itself, not model traffic**.

## Where it sits in the stack

Squarely [ai-gateway](../categories/ai-gateway.md), in the model-prompt layer: the
single outbound exit door for model traffic. Its risk contribution is **control of
outbound flows** — which providers and models are reachable, under whose key,
within what budget, with every prompt and response logged in one place. That
**request log** is the artefact a fund actually needs downstream, both for
[siem-soc](../categories/siem-soc.md) ingestion and for
[comms-surveillance](../categories/comms-surveillance.md)-style review of what
people asked models — and it is in the free build. Do not confuse it with the
enterprise **Audit Logs** feature, which is configuration-change history (who
changed a virtual key, a budget or a provider) and answers a governance question,
not a surveillance one. A fund needs both eventually; only the first one is free,
and only the first one tells you what staff asked a model.

It is a chokepoint, not an inspector. In the free tier there is **no content
inspection at all** — guardrails are an enterprise feature, so an OSS deployment
gives you routing, budgets and a **request log**, and you bolt
[ai-runtime-security](../categories/ai-runtime-security.md) on separately.

## Deployment & architecture

- **Self-hosted OSS** — a single Go binary, `npx`/Docker/binary, in your own VPC.
  In this mode prompts and responses never leave your tenancy; logs land wherever
  you point them.
- **Enterprise managed** and **edge** tiers exist (14-day trial), which do change
  the data path; Maxim publishes no retention or training-use policy for the
  managed tier. `data_leaves_tenancy` is therefore `partial` — entirely a function
  of which tier you buy.
- **In-process Go SDK** for teams that would rather not run another network hop.
- **Plugin surface** in Go or WebAssembly, which is a genuinely unusual extension
  story for this category and the main reason to prefer it over a Python proxy if
  your platform team writes Go.

## Positioning & differentiators

- **It is a direct, explicit attack on [litellm](litellm.md).** The repo
  description is literally "50x faster than LiteLLM." Bifrost's whole thesis is
  that the OSS default is a Python proxy that becomes the bottleneck, and a Go
  gateway is not. If LiteLLM's overhead has never shown up in your latency budget,
  the pitch does not land.
- **Go, not Python.** Lower memory and a single static binary matter for teams that
  run the gateway as shared infrastructure rather than as an app dependency.
- **Governance model is well-shaped** — the virtual-key → team → customer budget
  hierarchy is closer to what a platform team needs for chargeback than most OSS
  gateways offer, and it is in the free tier.
- **vs [portkey](portkey.md)** (now the Prisma AIRS AI Gateway inside Palo Alto)
  and [truefoundry](truefoundry.md) — those are commercial control planes with
  guardrails and prompt management included; Bifrost's equivalents are paid or
  absent.
- **vs [gravitee](gravitee.md), [kong](kong.md), [f5](f5.md),
  [cloudflare](cloudflare.md)** — those are gateway/networking incumbents extending
  into AI, sold to whoever already owns the API estate. Bifrost is the opposite
  buy: a focused component a platform team adopts on its own authority.
- **Traction is real but young** — 7.3k stars and 1.0k forks on a repo created
  2025-03-19, actively developed (releases in the past week). Against LiteLLM's
  installed base this is a challenger, not the default.

## Ownership, funding & M&A

Bifrost is **vendor-backed open source**: Apache-2.0, developed in the open at
`maximhq/bifrost`, owned by **Maxim AI** — the same company covered at
[maxim-ai](maxim-ai.md). Maxim is independent and VC-backed, founded 2023 by
Vaibhavi Gangwar and Akshay Deo, SF + India, with a **$3M seed announced
2024-06-18** led by Elevation Capital. As of 2026-08-16 there is **no later
funding round and no M&A**.

That is the material risk here: a seed-stage company on a ~$3M raise from mid-2024
is maintaining infrastructure you would put on the critical path of every model
call. The Apache-2.0 licence and self-hostable binary are the mitigant — if Maxim
disappears or is acquired, the data plane you are running keeps running and can be
forked; what you lose is the roadmap, the enterprise features, and support.

## Who should choose them / anti-fit

- **Good fit:** a platform team already routing real LLM volume, that self-hosts,
  cares about gateway overhead and memory, wants budget/chargeback controls per
  team, and is comfortable operating an early-stage OSS component. Go shops get a
  first-class extension path.
- **Anti-fit:** a fund whose entire AI footprint is a vendor-hosted
  [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) — you have no
  gateway problem yet. Also an anti-fit if you need guardrails, SSO, RBAC and
  configuration **Audit Logs** *without* a commercial negotiation, since all four
  are enterprise-tier here (the prompt/response **request log** is free);
  [litellm](litellm.md) puts more of that in the open-source build. And an
  anti-fit anywhere procurement requires a mature vendor with published
  certifications.

## Known weaknesses / gotchas

- **The marketing page and the docs disagree about what is free.** The product page
  advertises "built-in MCP gateway" and "real-time model protection that blocks
  unsafe outputs" with no tier marking; the docs list the MCP Gateway and content
  guardrails as **enterprise-only**. Assume the docs are right and price
  accordingly.

  > Contradiction (soft): Bifrost product page presents MCP gateway + guardrails as
  > product features; docs.getbifrost.ai scopes both to the enterprise licence.
  > Status: recorded 2026-08-16; treating docs as authoritative on tier scope.

- **Every benchmark is vendor-run, the numbers do not reconcile, and the
  methodology makes them unfalsifiable.** Added latency is quoted as 20 µs
  (product page), 11 µs (README/docs, on an AWS t3.xlarge), 59 µs (t3.medium),
  "less than 15 µs ... on average" (docs) and "<100 µs" (repo description); the
  LiteLLM multiple is "54x" in one place, "50x" in another and "40.4x" in the
  benchmark write-up. No independent replication was found.

  The methodology explains why. Bifrost's docs state that **"All benchmarks are on
  mocked OpenAI calls"**, and the `maximhq/bifrost-benchmarking` harness runs
  **"the mocker as a stand-in provider"** so as to **"isolate gateway overhead from
  provider latency"**. The comparative test uses a **60 ms mock OpenAI response**.
  There is no real provider, no real network path and no token streaming anywhere
  in the numbers. Worse, the headline figures measure three different things:

  | Figure | What it actually measures |
  |---|---|
  | 0.99 ms vs LiteLLM's 40 ms → "40.4x" | gateway overhead, comparative, against the 60 ms mock |
  | 1.68 s vs LiteLLM's 90.72 s → "54.0x" | **P99 latency** at 500 RPS — a different metric |
  | 11 µs (t3.xlarge) / 59 µs (t3.medium) | Bifrost's **internal** overhead at 5,000 RPS — **no LiteLLM comparison at all** |

  So the microsecond numbers everyone quotes are Bifrost-only internal queue
  overhead, while the actual head-to-head margin is ~1 ms versus 40 ms. Against a
  60 ms canned response that gap is ~1.6% of a call; against a real provider
  (300 ms–3 s, streaming) it is noise. That does not make Bifrost slower than
  LiteLLM — the Go-vs-Python argument is real, and 40 ms of proxy overhead is
  genuinely bad — but it does mean **the "50x faster" headline is not a claim about
  your production latency**. Benchmark on your own traffic against your own
  providers.
- **The enterprise Audit Logs are not immutable out of the box, whatever the docs
  index says.** The docs index advertises *"Immutable, timestamped audit trails for
  every configuration change. SOC 2, GDPR, HIPAA, ISO 27001 friendly."* The
  audit-logs page itself guarantees nothing of the sort: entries live in a database
  governed by `retention_days` (default 365), the object-storage copy is a
  *"durable archive"* whose retention is *"governed by your bucket's lifecycle
  rules"*, and the only immutability mention is a recommendation that **you** *"use
  S3 Object Lock / WORM"*. HMAC signing (32-byte key minimum) makes entries
  tamper-**evident**, not tamper-**proof**. The detail page also makes no SOC 2,
  GDPR, HIPAA or ISO 27001 claim at all.

  > Contradiction (soft): docs.getbifrost.ai/enterprise asserts "Immutable ... audit
  > trails" and names four compliance regimes; docs.getbifrost.ai/enterprise/audit-logs
  > describes a mutable DB record plus an optional customer-configured WORM archive
  > and names no regime. Status: recorded 2026-08-22 — classified **soft, not hard**,
  > because it is the same marketing-overstates-docs pattern already recorded above on
  > tier scope, and HMAC tamper-evidence plus optional Object Lock is a coherent design
  > that "immutable" merely oversells. Treating the detail page as authoritative. If
  > you read the index's "immutable" as an unqualified product claim, this becomes a
  > hard contradiction — say so and it gets re-flagged for the human.

  Practical consequence: if WORM audit retention is a control you intend to assert
  to an examiner, it is **your** S3 Object Lock configuration doing the work, not a
  Bifrost feature. Budget and document it as such.
- **No published certifications.** No SOC 2, ISO 27001 or similar found for Bifrost
  or Maxim AI. For a self-hosted OSS deployment this matters less; for the managed
  tier it is a procurement blocker.
- **870 open issues** against a repo ~17 months old, and pre-1.0 per-component
  version tags rather than a product-level release line — normal for a fast-moving
  OSS project, but it means you are pinning components, not a version.
- **Single-vendor project.** Contribution is dominated by Maxim; there is no
  foundation and no second commercial backer.
- **"1,000+ teams use Bifrost"** is an unverified vendor claim with no named
  references.

## Compliance & FS traction

None found. No certifications published, no named financial-services customers, no
case studies. `fs_traction: unverified`. The honest framing for a fund is that
Bifrost is adopted as self-hosted infrastructure on engineering judgement, not
procured on a compliance dossier.

## Commercial

Open-source core is **Apache-2.0** and free to self-host. Enterprise (managed) and
edge tiers are quoted, with a 14-day free trial and **no published list pricing** —
you will be in a sales conversation for clustering, guardrails, SSO/RBAC,
configuration Audit Logs and the MCP gateway. The prompt/response request log is
in the free build and is not part of that negotiation.

## Competitors / alternatives

[litellm](litellm.md) (the direct target), [portkey](portkey.md),
[truefoundry](truefoundry.md), [openrouter](openrouter.md),
[gravitee](gravitee.md), [kong](kong.md), [cloudflare](cloudflare.md),
[f5](f5.md) — all in [ai-gateway](../categories/ai-gateway.md).

## Open questions / to verify

- Whether Bifrost warrants cross-listing to
  [mcp-gateway](../categories/mcp-gateway.md). It ships an MCP Gateway, but only in
  the enterprise tier and with no public documentation of tool-level ACLs, so it is
  not filed there yet — unlike [gravitee](gravitee.md), whose MCP method-level
  policy is documented.
- Managed-tier data handling: retention period for prompts/responses and whether
  any content is used for vendor purposes. Not published; `data_leaves_tenancy`
  stays `partial` pending this.
- Enterprise pricing band, and whether the enterprise licence is per-node,
  per-request or flat.
- Independent (non-Maxim) benchmarking against LiteLLM **against a real provider
  rather than a 60 ms mock**, and reconciliation of the 11 µs / 15 µs / 20 µs /
  59 µs / <100 µs / 0.99 ms figures. Nothing found as of 2026-08-22 — searched,
  not merely assumed absent.
- Whether the enterprise Audit Logs can be made immutable *by Bifrost* rather than
  by customer-side S3 Object Lock, and what the docs index's "SOC 2, GDPR, HIPAA,
  ISO 27001 friendly" is actually asserting. Unresolved with the vendor.
- Real production references, especially any in financial services; the "1,000+
  teams" figure has no supporting detail.
- Whether the guardrails are Bifrost's own detection or pure passthrough to
  AWS/Azure/Google content-safety services — the docs read like the latter.
- Maxim AI runway: last raise was 2024-06 and the company now maintains both an
  eval platform and a gateway.

## Sources

- [maximhq/bifrost (GitHub repo + API metadata)](https://github.com/maximhq/bifrost) — fetched 2026-08-16 — supports: Apache-2.0 licence, Go, created 2025-03-19, 7,339 stars / 1,049 forks / 870 open issues, per-component release tags, provider list, plugin architecture, 11 µs / t3.xlarge benchmark; confidence: high (primary, machine-read).
- [Bifrost — the fastest enterprise AI gateway (Maxim product page)](https://www.getmaxim.ai/bifrost) — fetched 2026-08-16 — supports: positioning, 1000+ models, virtual keys/budgets, SSO/audit claims, 54x/9.5x/68% benchmark claims, three tiers + 14-day trial, "1,000+ teams"; confidence: medium (vendor marketing).
- [Bifrost documentation](https://docs.getbifrost.ai/) — fetched 2026-08-16 — supports: architecture, deployment paths, OSS vs enterprise feature split (clustering, adaptive LB, MCP gateway, guardrails, IdP/RBAC/VPC/audit, Datadog, log export); confidence: medium (vendor docs).
- [Bifrost vs LiteLLM benchmarks](https://www.getmaxim.ai/bifrost/resources/benchmarks) + [benchmarking docs](https://docs.getbifrost.ai/benchmarking/getting-started) + [maximhq/bifrost-benchmarking](https://github.com/maximhq/bifrost-benchmarking) — fetched 2026-08-22 — supports: "All benchmarks are on mocked OpenAI calls", the mocker-as-stand-in-provider harness, the 60 ms mock OpenAI response, 0.99 ms vs 40 ms → 40.4x, 1.68 s vs 90.72 s P99 → 54.0x, 11 µs/59 µs Bifrost-only internal overhead at 5,000 RPS, ~10 KB payloads; confidence: high (vendor primary, but vendor-run).
- [Bifrost enterprise docs index](https://docs.getbifrost.ai/enterprise/) + [Audit Logs](https://docs.getbifrost.ai/enterprise/audit-logs) — fetched 2026-08-22 — supports: Audit Logs record administrative/configuration activity not model traffic; HMAC signing; `retention_days` default 365; S3 Object Lock as a customer-side recommendation; the index-vs-detail immutability discrepancy; confidence: high (vendor docs, read directly).
- Cached: `raw/sources/2026-08-22--bifrost--benchmark-methodology-and-audit-logs.md`
- [Announcing Maxim AI GA and $3M seed (Maxim blog)](https://www.getmaxim.ai/blog/announcing-maxim-ais-general-availability-and-the-3m-funding-round-led-by-elevation-capital/) — fetched 2026-06-28 (via [maxim-ai](maxim-ai.md)) — supports: parent ownership, founders, seed amount/date/lead; confidence: high (primary).

## History

- [2026-08-16] Page created and researched in one pass (user-requested addition, not a seed/CSV row). Filed as a **product slug** under `ai-gateway` with the parent company kept at [maxim-ai](maxim-ai.md). Established: Apache-2.0 Go gateway, repo created 2025-03-19, 7.3k stars, vendor-backed OSS under Maxim AI (independent, $3M seed 2024-06-18, no later round or M&A as of 2026-08-16). Recorded the marketing-vs-docs tier discrepancy on MCP gateway/guardrails as a soft contradiction and the unreconciled latency benchmarks as a gotcha. Position `challenger` in ai-gateway. 1 source cached.
- [2026-08-22] **Correction + sharpening.** (1) The unreconciled-latency gotcha was correct but under-specified; added the methodology that makes the numbers unfalsifiable — all benchmarks run against a **mocked** OpenAI provider, with a **60 ms mock response** for the gateway-overhead test — and separated the three distinct metrics being presented as one story (0.99 ms vs 40 ms comparative overhead → "40.4x"; 1.68 s vs 90.72 s P99 → "54x"; 11 µs/59 µs Bifrost-only internal overhead with no LiteLLM comparison). (2) Fixed an internal contradiction: the OSS-vs-enterprise section listed "audit logging" as enterprise-gated while "Where it sits in the stack" told a fund an OSS deployment gives it "an audit trail". These are two different artefacts — the **request log** (prompts/responses, free, and the thing comms-surveillance review actually needs) versus the enterprise **Audit Logs** feature (configuration-change history). Every mention now says which. (3) Recorded a **soft** contradiction on audit-log immutability between the docs index and the audit-logs page, with the reasoning for soft-not-hard stated inline. Sources re-fetched and cached.
