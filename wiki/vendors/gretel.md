---
title: Gretel (NVIDIA)
type: vendor
name: Gretel
slug: gretel
aka: [Gretel.ai, Gretel Labs, Gretel Navigator, NVIDIA NeMo Safe Synthesizer, NVIDIA NeMo Data Designer]
primary_category: synthetic-masked-data
also_listed_in: []
website: "https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/"
founded: 2019
hq: San Diego, California, USA (pre-acquisition); now part of NVIDIA, Santa Clara, California
ownership_state: acquired-closed
owner: "NVIDIA (NASDAQ: NVDA)"
ownership_note: "Acquisition reported by Wired and TechCrunch on 2025-03-19 as completed; NVIDIA declined to comment and issued no press release. Price reported as nine figures, above Gretel's last $320M valuation (unconfirmed). Gretel's founders and roughly 80 staff joined NVIDIA. gretel.ai now 301-redirects to an NVIDIA page; the gretelai GitHub repos are archived. The technology lives on as open-source NVIDIA NeMo Data Designer and NeMo Safe Synthesizer (Apache-2.0)."
acquisition: {announced: 2025-03-19, closed: 2025-03-19, price: "undisclosed; reported nine figures (Wired via TechCrunch), unconfirmed"}
funding_total: ">$67M pre-acquisition (Crunchbase via TechCrunch)"
last_funding: null
market_position: {synthetic-masked-data: platform-module}
deployment_model: [self-hosted]
form_factor: [sdk, platform]
data_leaves_tenancy: "false"
integrations: [nvidia-nemo, nvidia-ai-enterprise]
mcp_support: unverified
certifications: []
pricing_model: "OSS (Apache-2.0) for NeMo Data Designer and Safe Synthesizer; enterprise support via NVIDIA (terms unverified). Standalone Gretel SaaS no longer sold as far as can be verified."
fs_traction: unverified
target_customer: ML and data-science teams that need privacy-safe synthetic tabular data or synthetic training/eval datasets for in-house models, and can run GPU workloads
last_verified: 2026-10-26
verify_after: null
tags: [synthetic-data, differential-privacy, training-data, nvidia-nemo, absorbed-product]
sources:
  - {claim: "NVIDIA reportedly acquired Gretel; nine-figure price above $320M valuation; ~80 staff; founders; San Diego; >$67M raised; NVIDIA no comment", url: "https://techcrunch.com/2025/03/19/nvidia-reportedly-acquires-synthetic-data-startup-gretel", date: 2025-03-19, confidence: medium}
  - {claim: "gretel.ai 301-redirects to NVIDIA synthetic-data use-case page; page describes NeMo Data Designer and NeMo Safe Synthesizer", url: "https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/", date: 2026-10-26, confidence: high}
  - {claim: "gretelai/gretel-synthetics archived (last push 2025-06-24)", url: "https://github.com/gretelai/gretel-synthetics", date: 2026-10-26, confidence: high}
  - {claim: "NeMo Data Designer open source Apache-2.0, repo created 2025-10-16", url: "https://github.com/NVIDIA-NeMo/DataDesigner", date: 2026-10-26, confidence: high}
  - {claim: "NeMo Safe Synthesizer open source Apache-2.0, repo created 2026-01-20; private synthetic versions of sensitive tabular data; GPU/Linux requirements", url: "https://github.com/NVIDIA-NeMo/Safe-Synthesizer", date: 2026-10-26, confidence: high}
  - {claim: "Gretel co-founder Ali Golshan joined NVIDIA in 2025; senior director of AI software", url: "https://developer.nvidia.com/blog/author/aligolshan/", date: 2026-10-26, confidence: medium}
  - {claim: "NeMo Microservices retired 2026-10-01 in favour of NeMo Platform; Safe Synthesizer workflow (PII replacement, DP training, evaluation)", url: "https://docs.nvidia.com/nemo/microservices/latest/safe-synthesizer/about/index.html", date: 2026-10-26, confidence: medium}
---

# Gretel (NVIDIA)

> Primary category: [synthetic-masked-data](../categories/synthetic-masked-data.md).

**One-liner** — Formerly the best-known standalone synthetic-data startup. Since its March 2025 acquisition by NVIDIA, Gretel is **no longer a product you buy**: its technology survives as two open-source NVIDIA NeMo components, **NeMo Data Designer** (generate synthetic datasets for AI training and evaluation) and **NeMo Safe Synthesizer** (make a privacy-safe synthetic copy of a sensitive table).

**What it does** — Two successor components, which is what a buyer evaluates today:
- **NeMo Safe Synthesizer**: takes a sensitive tabular dataset and produces an entirely synthetic one "with no one-to-one mapping to your original records". The workflow is PII replacement, then model training (optionally with differential privacy), then a quality and privacy evaluation report. This is the direct descendant of Gretel's core privacy-synthetics business. It needs an NVIDIA GPU (A100 or larger) on Linux for training and generation.
- **NeMo Data Designer**: builds synthetic datasets from scratch or from a small seed, mixing LLM-generated fields, samplers and validators. It is used for fine-tuning, evaluation and agent test sets rather than for masking production data. It began as an early preview inside **Gretel Navigator** before the acquisition. NVIDIA open-sourced it (repo created 2025-10-16).

Pre-acquisition, Gretel sold a SaaS console and APIs (Gretel Navigator, synthetics, transforms/PII redaction, evaluation) plus open-source libraries such as `gretel-synthetics`.

**Naming / provenance** — Founded 2019 in San Diego by Alex Watson, Laszlo Bock, John Myers and Ali Golshan (CEO). **Slug decision:** the page keeps the slug `gretel` and title "Gretel (NVIDIA)", not an NVIDIA product slug. Survey respondents and buyers still say "Gretel". The NeMo component names have changed with NVIDIA's packaging: NeMo Microservices was retired on 2026-10-01 in favour of "NeMo Platform" per NVIDIA docs banners. NeMo is a large framework, and synthetic data is a small part of it. If NVIDIA's synthetic-data products later become a shopping unit in their own right, revisit with an `nvidia-nemo` page and make this an alias. Related NVIDIA page: [nvidia-openshell](nvidia-openshell.md), whose product lead is Gretel's co-founder Ali Golshan per his NVIDIA bio.

**Ownership & viability** — `acquired-closed`, owner **NVIDIA**. Wired and TechCrunch reported on **2025-03-19** that NVIDIA *had* acquired Gretel, for a price "said to be nine figures", above Gretel's most recent $320M valuation. NVIDIA declined to comment and never issued a release, so price and exact close date rest on press reporting (announced and closed are both set to the report date). Corroboration that the deal closed: Gretel's co-founder lists NVIDIA as his employer since 2025, gretel.ai 301-redirects to an NVIDIA page, the gretelai GitHub repos are archived (gretel-synthetics last pushed 2025-06-24), and NVIDIA ships the successor components. Pre-acquisition Gretel had raised more than $67M (Anthos Capital, Greylock, Moonshots Capital and others).

Judgement: **acquired and absorbed, not shelved.** The technology is actively developed (both NeMo repos had commits on 2026-10-26), but as NVIDIA infrastructure for AI developers, not as a privacy product for enterprise data teams. Former Gretel SaaS customers had to migrate. Whether NVIDIA offers a hosted equivalent outside NVIDIA AI Enterprise is unverified.

**Positioning & differentiators** — `platform-module` in [synthetic-masked-data](../categories/synthetic-masked-data.md): it is now a component of NVIDIA's NeMo AI stack, not a standalone vendor.
- **Versus [tonic-ai](tonic-ai.md) and [k2view](k2view.md):** they mask and subset *production databases for software testing*, keeping real-looking rows with real referential structure. Safe Synthesizer *learns a model of a table and samples new rows*, which suits analytics and ML training more than application QA across many joined tables.
- **Versus MOSTLY AI (now Syntho) and SAS Data Maker (ex-Hazy):** the same model-based synthetic-tabular niche. NVIDIA's version is free and open source but GPU-bound and self-operated. The others are commercial products with UIs and support.
- **Data Designer** competes more with DIY LLM-based dataset generation than with any masking vendor.

**Who should choose them / anti-fit** — Fits a fund with a **quant or data-science team already on NVIDIA GPUs** that wants synthetic versions of sensitive tabular data (client, transaction or HR data) to share with researchers, vendors or a fine-tuning job, or that needs synthetic eval sets for in-house models. Free OSS keeps the cost to compute and engineering time. **Anti-fit:** anyone who wants a supported, UI-driven product with a vendor contract (the standalone Gretel product is gone); dev/QA teams that need masked copies of application databases (use Tonic, K2view, or a TDM suite); and shops without GPU capacity.

**Known weaknesses / gotchas** —
- **The product you may remember no longer exists as sold.** Survey answers of "Gretel" after 2025 likely mean NeMo components, legacy self-hosted libraries, or memory of the brand. Treat them with care.
- **Packaging churn.** Gretel to NeMo Microservices to NeMo Platform within about 18 months. Pin versions and expect API changes.
- **GPU and Linux only** for Safe Synthesizer training and generation.
- **Synthetic is not automatically safe.** Model-based synthesis can memorise rare records. Rely on the privacy evaluation report and differential-privacy settings, and do your own review before releasing data outside the firm.

**Deployment & data handling** — `self-hosted`: both components run in the customer's own environment (pip/uv install, containers, or NVIDIA's platform). `data_leaves_tenancy: "false"` for self-run OSS. If Data Designer is pointed at a hosted LLM endpoint (NVIDIA-hosted or a third-party model provider), seed data and prompts go to that endpoint. Batch, out-of-band.

**Integrations & partnerships** — Part of NVIDIA NeMo, with enterprise support through NVIDIA AI Enterprise (terms not verified). Data Designer has a plugin catalogue and works with OpenAI-compatible model endpoints. MCP support unverified.

**Compliance & FS traction** — No certifications apply to self-run OSS. No financial-services customers verified, before or after the acquisition. NVIDIA says Safe Synthesizer defaults are intended to help meet HIPAA and GDPR. That is a design goal, not a certification.

**Commercial** — Open source, Apache-2.0 (both repos). Cost is GPU compute plus engineering time, and optionally NVIDIA AI Enterprise licensing for support (pricing not reviewed).

## Open questions

- Exact close date and price (NVIDIA never confirmed). Is there an NVIDIA 10-K/10-Q reference?
- Is any hosted, Gretel-equivalent service sold by NVIDIA today, and what support terms apply to Safe Synthesizer under NVIDIA AI Enterprise?
- What happened to Gretel's SaaS customers and contracts at shutdown (dates of console sunset)?
- MCP support in Data Designer or the NeMo Platform.
- Any FS users of Safe Synthesizer.

## Sources

- [Nvidia reportedly acquires synthetic data startup Gretel (TechCrunch)](https://techcrunch.com/2025/03/19/nvidia-reportedly-acquires-synthetic-data-startup-gretel) — fetched 2026-10-26 — supports: acquisition report 2025-03-19, price, staff, founders, funding; confidence: medium (press report citing Wired; NVIDIA no comment)
- [NVIDIA synthetic data generation for agentic AI](https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/) — fetched 2026-10-26 (redirect target of gretel.ai) — supports: domain absorption, successor products; confidence: high
- [gretelai/gretel-synthetics (GitHub)](https://github.com/gretelai/gretel-synthetics) — API checked 2026-10-26 — supports: archived repo; confidence: high
- [NVIDIA-NeMo/DataDesigner (GitHub)](https://github.com/NVIDIA-NeMo/DataDesigner) — API checked 2026-10-26 — supports: Apache-2.0, active; confidence: high
- [NVIDIA-NeMo/Safe-Synthesizer (GitHub)](https://github.com/NVIDIA-NeMo/Safe-Synthesizer) — README fetched 2026-10-26 — supports: function, license, GPU requirements; confidence: high
- [Ali Golshan author page (NVIDIA Developer)](https://developer.nvidia.com/blog/author/aligolshan/) — via search 2026-10-26 — supports: co-founder joined NVIDIA 2025; confidence: medium
- [About Generating Safe Synthetic Data (NVIDIA docs)](https://docs.nvidia.com/nemo/microservices/latest/safe-synthesizer/about/index.html) — via search 2026-10-26 — supports: workflow, NeMo Microservices retirement banner; confidence: medium
- Cached: `raw/sources/2026-10-26--gretel--nvidia-acquisition-and-nemo.md`

## History

- [2026-10-26] Page created via wiki-create and researched the same day, as a seed vendor of the new [synthetic-masked-data](../categories/synthetic-masked-data.md) category. Slug kept as `gretel` (company name buyers recognise) with owner NVIDIA, title "Gretel (NVIDIA)". Acquisition dated to the 2025-03-19 press reports; NVIDIA never announced it.
