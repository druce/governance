---
title: Presidio (ex-Microsoft)
type: vendor
name: Presidio (ex-Microsoft)
slug: presidio
aka: [Microsoft Presidio, Presidio Analyzer, Presidio Anonymizer, Data Privacy Stack]
primary_category: ai-red-teaming
also_listed_in: [dlp]
website: https://presidio.dataprivacystack.org
founded: 2018
hq: null
ownership_state: oss-foundation
owner: null
ownership_note: 'MIT-licensed OSS created at Microsoft (repo dates from 2018-05-04). In 2026 it moved to Data Privacy Stack, a community org (blog post last updated 2026-06-29; GitHub org created 2026-04-13). Governance follows GitHub''s Minimum Viable Governance template: a 4-person TSC of existing Presidio maintainers. Not a legal foundation, no company, no trademark. Whether Microsoft still pays the maintainers is unverified.'
acquisition: {announced: null, closed: null, price: null}
funding_total: n/a (OSS project)
last_funding: n/a
market_position: {ai-red-teaming: oss-default, dlp: niche-specialist}
deployment_model: [self-hosted]
form_factor: [sdk, api]
data_leaves_tenancy: "false"
integrations: [litellm, spacy, huggingface-transformers, azure-ai-language, spark, fabric, azure-data-factory]
mcp_support: none
certifications: []
pricing_model: OSS (free); no commercial support offering
fs_traction: unverified
target_customer: engineering and data teams that need to find and redact PII in text, images or tables, often before data reaches an LLM or a log
last_verified: 2026-10-26
verify_after: null
tags: [open-source, pii, redaction, anonymization, guardrails, data-privacy-stack]
sources:
  - {claim: move-to-data-privacy-stack, url: "https://dataprivacystack.org/blog/presidio-project-joins-data-privacy-stack/", date: 2026-06-29, confidence: high}
  - {claim: governance-tsc-charter, url: "https://github.com/data-privacy-stack/MVG", date: 2026-10-26, confidence: high}
  - {claim: repo-license-components-releases, url: "https://github.com/data-privacy-stack/presidio", date: 2026-10-26, confidence: high}
  - {claim: docs-llm-samples-disclaimer, url: "https://presidio.dataprivacystack.org/", date: 2026-10-26, confidence: high}
  - {claim: thoughtworks-radar-trial, url: "https://www.thoughtworks.com/radar/languages-and-frameworks/presidio", date: 2025-11-01, confidence: high}
---

# Presidio (ex-Microsoft)

> **One-liner** — The standard open-source library for **finding and redacting PII**
> (names, card numbers, SSNs, emails and so on) in text, images and tables. Engineers drop it in
> front of an LLM call or a log pipeline to mask sensitive fields. Built by Microsoft;
> since mid-2026 governed by an independent community org, **Data Privacy Stack**.

**Categories** — [ai-red-teaming](../categories/ai-red-teaming.md) (primary, the
"guardrails" half), [dlp](../categories/dlp.md)

## What it does

Presidio is a Python SDK, also packaged as Docker REST services, with four parts:

- **Analyzer** — detects PII entities in text. It combines regex and checksum
  recognizers with NER models (spaCy or Hugging Face transformers by default; Flair,
  GLiNER and Span Marker pluggable) and context words. It can also call Azure AI
  Language or Azure Health Data Services as remote recognizers.
- **Anonymizer** — replaces what was found: redact, mask, hash, encrypt (reversible) or
  substitute fake values.
- **Image Redactor** — OCR-based redaction of PII in images and DICOM files.
- **Structured** — PII detection in tables and semi-structured data, with PySpark
  support for batch jobs.

You extend it with custom recognizers, such as internal account IDs, fund codes or
counterparty names. In the AI stack it is most often used as an **input/output
filter**: mask PII in a prompt before it leaves for a model provider, and scan
responses and traces before they are logged. The project ships samples for doing this
through the [litellm](litellm.md) proxy and the AISIX AI gateway, and LiteLLM lists
Presidio as a built-in guardrail provider.

## Where it sits in the stack

Filed under [ai-red-teaming](../categories/ai-red-teaming.md) ("AI Red Teaming /
Guardrails"), alongside the other OSS guardrail toolkits
([guardrails-ai](guardrails-ai.md), [nemo-guardrails](nemo-guardrails.md)). In AI
deployments it is a PII guardrail, not a red-team tool. Cross-listed in
[dlp](../categories/dlp.md) because the detection engine is DLP-style content
inspection. It is a building block, not a DLP product: it has no endpoints, policy
console, incident workflow or network or SaaS coverage. Commercial DLP and AI-firewall
products ([microsoft-purview](microsoft-purview.md), [nightfall-ai](nightfall-ai.md),
[lakera](lakera.md), [prisma-airs](prisma-airs.md)) bundle detection, enforcement point
and management. Presidio gives you only the detection and redaction, which you wire into
your own gateway or pipeline.

## Deployment & data handling

- Self-hosted only: pip packages, or Docker images for analyzer and anonymizer REST
  services on Kubernetes or App Service, or Spark jobs. No SaaS. Container images moved
  from Microsoft's registry to `ghcr.io/data-privacy-stack/presidio-*` (secondary
  source).
- **Data stays in your environment** by default. Models run locally. Data leaves only
  if you configure a remote recognizer (such as Azure AI Language) or an LLM-based
  recognizer.
- Inline if you put it in the request path, through a gateway hook or your own code.
  Latency depends on the NER model: regex-only is fast, transformer models add tens to
  hundreds of milliseconds and need sizing (unverified; benchmark yourself).

## Positioning & differentiators

- **The default free PII engine.** Many AI gateways and guardrail frameworks wrap it
  rather than build their own, which is why it shows up in [litellm](litellm.md)'s
  guardrail list. The other OSS guardrail frameworks ([guardrails-ai](guardrails-ai.md),
  [nemo-guardrails](nemo-guardrails.md)) orchestrate checks; Presidio is a detector you
  plug into them.
- **vs commercial PII detection** ([nightfall-ai](nightfall-ai.md), Purview sensitive
  information types, cloud DLP APIs): Presidio is free, runs entirely in your tenancy and
  can be customized to your own entity types. It is less accurate out of the box, and
  you own tuning, false-positive handling and operations.
- **Independent assessment:** Thoughtworks Technology Radar moved it from Assess (Apr
  2025) to **Trial** (Nov 2025), noting enterprise use where strict data-sharing controls
  apply to LLM integrations. Radar caveat: it "isn't foolproof and may miss or misidentify
  entities."

**Position labels:** *oss-default* in ai-red-teaming/guardrails: it is the PII
detector other tools embed. *niche-specialist* in dlp: a detection library, not a DLP
programme.

## Who should choose them / anti-fit

- **Choose** if you are building an internal LLM app or gateway and want a free,
  in-tenancy way to mask client names, account numbers and personal data before prompts
  go to a model API or land in observability logs. It also suits anonymizing datasets
  for evals and test environments.
- **Anti-fit:**
  - Firms that want a DLP product with policies, alerts, coverage of endpoints, email
    and SaaS, and an audit trail. Buy [dlp](../categories/dlp.md) or
    [ai-access-governance](../categories/ai-access-governance.md).
  - Teams with no engineers to tune recognizers.
  - Anyone who needs vendor support or an SLA. There is none.
  - Defending against prompt injection. Presidio detects PII, not attacks.

## Known weaknesses / gotchas

- **Recall is not guaranteed.** The project's own disclaimer says there is "no guarantee
  that Presidio will find all sensitive information." Out-of-the-box recognizers are
  US/English-centric. Finance-specific identifiers (ISINs, internal account formats,
  deal code names) need custom recognizers.
- **Governance change in 2026.** The move from Microsoft to Data Privacy Stack is
  recent. The new org has no legal entity, trademark or funding disclosed. Microsoft's
  continued involvement is unstated. Old `microsoft/presidio` links and MCR image paths
  redirect or are being replaced, so pin versions and update image sources.
- No MCP- or agent-specific features. It is a text, image and table scanner.

## Ownership & viability

Created at Microsoft (repo created 2018-05-04, MIT). In 2026 the project moved to
**Data Privacy Stack**, described as "an independent, community-driven organization".
The announcement post was last updated **2026-06-29**, the GitHub org was created
2026-04-13, and `github.com/microsoft/presidio` now redirects to
`data-privacy-stack/presidio`. The post thanks Microsoft for "supporting Presidio and
helping nurture both the project and its community". It does not say whether Microsoft
continues to fund or employ maintainers.

Governance uses GitHub's **Minimum Viable Governance** template. A Technical Steering
Committee of four existing maintainers (Omri Mendels, Nava Vaisman Levy, Sharon Hart,
Coby Peled) serves "not as representatives of any employer". Decisions are by
consensus. The charter states the org holds no trademark.

Activity is healthy: releases 2.2.363 (2026-06-28), 2.2.364 (2026-07-22) and 2.2.365
(2026-10-25), and about 11.5k GitHub stars. `ownership_state: oss-foundation` is the
closest vocabulary fit. It is community-governed and vendor-neutral by charter, but not
a formal foundation such as the Linux Foundation or CNCF. No acquisition risk applies;
the risk is maintainer sustainability.

## Integrations & partnerships

- Official samples: [litellm](litellm.md) proxy PII masking, AISIX AI Gateway, Azure App
  Service, Kubernetes, Spark, Microsoft Fabric, Azure Data Factory, telemetry/log
  redaction, OpenAI-based synthetic data.
- NER backends: spaCy, Hugging Face transformers, Flair, GLiNER, Span Marker. Remote
  recognizers for Azure AI Language PII and Azure Health Data Services de-identification.
- Commonly wrapped by AI gateways and guardrail frameworks. LiteLLM is confirmed in this
  wiki; other wrappers are not verified here.
- MCP: none.

## Compliance & FS traction

No certifications (it is a library). No named FS adopters found. As a self-hosted
library it inherits your own controls. Being able to run it fully inside your tenancy is
the main compliance selling point.

## Commercial

Free (MIT). No paid tier or commercial support from the project. Support is through
GitHub issues and discussions, or presidio@dataprivacystack.org.

## CTO / hedge-fund lens

**Cheap Day-2 building block for firms that build their own LLM apps.** If prompts to
external models may contain client or counterparty names, account numbers or employee
data, a Presidio pass in your gateway is the lowest-cost mitigation. It is not a
complete one: pair it with allow-listed model providers and contractual no-training
terms. Budget engineering time to add fund-specific recognizers and measure recall on
your own data. Do not present it to compliance as "DLP".

## Open questions / to verify

- Exact announcement date of the move to Data Privacy Stack (post shows only "last
  updated 2026-06-29").
- Whether Microsoft still employs or sponsors the core maintainers; any corporate
  members.
- Whether the PyPI package names and Docker registry change are complete. PyPI homepage
  already points to the data-privacy-stack repo.
- Production FS adopters.
- Measured latency and recall benchmarks for common configurations.

## Sources

- [The Presidio Project Joins Data Privacy Stack](https://dataprivacystack.org/blog/presidio-project-joins-data-privacy-stack/) — fetched 2026-10-26 (last updated 2026-06-29) — supports: move from Microsoft, MIT retained, community governance; confidence: high
- [data-privacy-stack/MVG: STEERING-COMMITTEE.md, CHARTER.md](https://github.com/data-privacy-stack/MVG) — fetched 2026-10-26 — supports: TSC members, consensus governance, no trademark; confidence: high
- [data-privacy-stack/presidio (GitHub + API)](https://github.com/data-privacy-stack/presidio) — fetched 2026-10-26 — supports: MIT, created 2018-05-04, redirect from microsoft/presidio, releases, components; confidence: high
- [Presidio docs](https://presidio.dataprivacystack.org/) — fetched 2026-10-26 — supports: components, deployment, LiteLLM/AISIX samples, Azure recognizers, disclaimer; confidence: high
- [Thoughtworks Radar: Presidio](https://www.thoughtworks.com/radar/languages-and-frameworks/presidio) — fetched 2026-10-26 — supports: Assess (2025-04) to Trial (2025-11), caveat on accuracy; confidence: high
- [Pasquale Pillitteri: Presidio (ex-Microsoft)](https://pasqualepillitteri.it/en/news/5538/microsoft-presidio-pii-data-protection-ai) — search snippet 2026-10-26 (update 2026-07-15) — supports: Docker images moved to ghcr.io/data-privacy-stack; confidence: low-medium
- Cached: `raw/sources/2026-10-26--presidio--data-privacy-stack-transition.md`, `raw/sources/2026-10-26--presidio--repo-site-thoughtworks.md`

## History

- [2026-10-26] Page created. Slug `presidio` rather than `microsoft-presidio` because
  the project left Microsoft governance in 2026 (Data Privacy Stack). "Microsoft
  Presidio" kept in `aka`. Primary ai-red-teaming (guardrails half, consistent with
  guardrails-ai and nemo-guardrails), cross-listed dlp. Cached 2 sources.
