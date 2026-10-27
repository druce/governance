---
title: Tonic.ai
type: vendor
name: Tonic.ai
slug: tonic-ai
aka: [Tonic, Tonic Structural, Tonic Textual, Tonic Ephemeral, Tonic Fabricate, Mockaroo Fabricate]
primary_category: synthetic-masked-data
also_listed_in: []
website: "https://www.tonic.ai"
founded: 2018
hq: San Francisco, California, USA
ownership_state: independent
owner: null
ownership_note: "Venture-backed private company. Last confirmed priced round: $35M Series B led by Insight Partners, announced 2021-09-29. Aggregators disagree on total raised ($35M to $46.9M) and one lists an unconfirmed April 2025 raise. Acquired Fabricate (from Mockaroo) 2025-04-22, price undisclosed."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: "Series B, $35M, led by Insight Partners, announced 2021-09-29 (later rounds unconfirmed)"
market_position: {synthetic-masked-data: leader}
deployment_model: [saas, self-hosted]
form_factor: [platform, api, sdk]
data_leaves_tenancy: partial
integrations: [aws-marketplace, snowflake, microsoft-fabric, sql-server, oracle]
mcp_support: server
certifications: [SOC 2 (vendor-stated; type unverified), HIPAA (vendor-stated)]
pricing_model: "annual contract by plan and source-data size (Structural); per-1,000-words usage (Textual); free tier + credits (Fabricate)"
fs_traction: claimed
target_customer: engineering and data teams that need production-shaped test data or de-identified text for development, QA and AI training without copying real customer data into lower environments
last_verified: 2026-10-26
verify_after: null
tags: [test-data-management, data-masking, subsetting, synthetic-data, pii-redaction, unstructured-data, ephemeral-databases, rag-data-prep]
sources:
  - {claim: "Product line (Structural, Textual, Fabricate); Tonic Cloud and self-hosted deployment; SOC/HIPAA/GDPR badges; FS logos", url: "https://www.tonic.ai/", date: 2026-10-26, confidence: medium}
  - {claim: "Pricing model per product; self-hosted on Enterprise tiers; AWS Marketplace AMI and Snowflake Native App for Textual", url: "https://www.tonic.ai/pricing", date: 2026-10-26, confidence: high}
  - {claim: "Fabricate acquisition from Mockaroo, 2025-04-22; founded 2018; HQ San Francisco; named customers", url: "https://www.tonic.ai/press-releases/tonic-ai-acquires-fabricate-expanding-its-leadership-in-synthetic-data", date: 2025-04-22, confidence: high}
  - {claim: "Series B $35M led by Insight Partners, 2021-09-29", url: "https://www.hpcwire.com/bigdatawire/this-just-in/tonic-ai-lands-35m-series-b-funding-puts-fake-data-at-forefront-of-growth/", date: 2021-09-29, confidence: high}
  - {claim: "Tonic Ephemeral databases-on-demand with expiry timers, API/CI-driven", url: "https://tonic.ai/blog/ephemeral-databases-on-demand-have-arrived-meet-tonic-ephemeral", date: 2026-10-26, confidence: medium}
  - {claim: "Open-source Textual MCP server, March 2026", url: "https://docs.tonic.ai/textual/textual-integrations/textual-mcp-server", date: 2026-10-26, confidence: high}
  - {claim: "Textual GA for Microsoft Fabric, 2026-03-18", url: "https://www.tonic.ai/press-releases/tonic-textual-general-availablity-for-fabric", date: 2026-03-18, confidence: medium}
---

# Tonic.ai

> Primary category: [synthetic-masked-data](../categories/synthetic-masked-data.md).

**One-liner** — The best-known developer-oriented vendor for **realistic fake data**. It masks and subsets production databases into safe test copies, redacts or synthesises PII in free text and documents (including for AI training and RAG), and generates data from scratch when there is no production data to start from.

**What it does** — Four products, sold separately:
- **Tonic Structural**: the original product. Connects to a production database and produces a de-identified, optionally subsetted copy for dev and test. Masking is consistent across tables so foreign keys and joins still work, and schema changes are tracked so the masked copy does not break when production changes.
- **Tonic Textual**: finds and redacts or replaces PII and other sensitive entities in unstructured text, JSON, HTML and files. It is pitched at preparing data for LLM fine-tuning and RAG ingestion. Since November 2025 customers can train their own entity types; since March 2026 it is GA inside Microsoft Fabric and ships an **open-source MCP server** so agents can call its redaction tools.
- **Tonic Ephemeral**: short-lived databases on demand. It spins up a database from a snapshot (typically Structural's masked output), gives it an expiry timer, and tears it down. It is meant for CI pipelines, per-branch test databases and demos.
- **Tonic Fabricate**: from-scratch generation of relational data, free text and mock APIs from a schema, SQL or a natural-language prompt. It came with the **Fabricate acquisition from Mockaroo (2025-04-22)**. It is the option when no production data exists yet or none may be used.

**Naming / provenance** — Founded 2018, San Francisco, with offices in Atlanta, New York and London (company boilerplate, 2025). Fabricate was built by Mockaroo, the long-running mock-data site. Its founder Mark Brocato joined Tonic to run it. Not to be confused with unrelated "Tonic" apps and audio products. Check the domain, tonic.ai.

**Ownership & viability** — `independent`, venture-backed. The confirmed financing is a **$35M Series B led by Insight Partners (announced 2021-09-29)**, with GGV Capital (Series A lead), Bloomberg Beta, Octave, Heavybit and Silicon Valley CISO Investments. Aggregators put total funding between $35M and $46.9M, and one lists an April 2025 raise that no primary source confirms. The company is active: an acquisition in 2025, an AWS strategic collaboration agreement (2025-04-08), and product releases through March 2026. Acquisition risk: Tonic is a natural target for a data-platform or DevOps vendor, following the pattern of Perforce/Delphix and SAS/Hazy. Self-hosted customers would keep running software they hold, but the roadmap would be at the buyer's discretion.

**Positioning & differentiators** — `leader` in [synthetic-masked-data](../categories/synthetic-masked-data.md): among the vendors covered here it has the broadest product coverage (structured masking, unstructured redaction, ephemeral databases, from-scratch generation) and the most visible developer-facing presence.
- **Versus [k2view](k2view.md):** Tonic is database-centric and developer-led. You point it at a database and get a masked copy. K2view is entity-centric and enterprise-integration-led. It assembles "a customer" across many source systems and masks in flight, which suits large estates with dozens of systems of record. Tonic is usually lighter to stand up; K2view is better suited to complex, cross-system referential integrity.
- **Versus [gretel](gretel.md) (now NVIDIA NeMo Safe Synthesizer):** Gretel's lineage is model-based synthesis for ML training data. Tonic's is masking production data for software testing. Tonic Textual and Fabricate narrow the gap. For "make a safe copy of my database for QA", Tonic is the more direct fit.
- **Versus legacy TDM (Delphix/Perforce, Informatica, Broadcom TDM):** those are older, ops-led suites often bought with mainframe or ERP estates in mind. Tonic is SaaS-first with self-serve tiers and per-product pricing.
- **Unstructured redaction overlaps open source.** Textual competes with self-built pipelines on [presidio](presidio.md). Tonic sells accuracy, custom entity training, synthesis (realistic replacements rather than `<REDACTED>`) and operations.

**Who should choose them / anti-fit** — Fits a fund with **in-house developers** who keep copying production databases (OMS/PMS extracts, CRM, investor-relations or fund-admin data) into dev and test, or a data/AI team that needs to scrub research notes, emails or documents before fine-tuning or indexing them. **Anti-fit:** a firm with almost no in-house software development (the problem is small there); a large bank-style estate with mainframe and dozens of systems of record that needs cross-system entity assembly (look at K2view or legacy TDM suites); and anyone who needs statistically faithful synthetic tabular data for model training with formal privacy guarantees, where differential-privacy-focused tools (NVIDIA Safe Synthesizer, MOSTLY AI) are the closer fit.

**Known weaknesses / gotchas** —
- **Masking is only as good as detection.** A missed column or free-text field (a "notes" column holding client names) leaks straight into the test copy. Budget time to review generator rules per table. This is not a set-and-forget product.
- **Four products, four price meters.** Structural is priced by source-data size, Textual per word, Fabricate by credits/tokens, and Ephemeral is not on the public pricing page. Ask for an all-in quote.
- **Tonic Cloud means production data goes to Tonic.** Hosted Structural and Textual process real production data and real documents. Regulated shops will usually want self-hosted (Enterprise tier).
- Most capability and customer claims are vendor marketing. No independent benchmark of detection accuracy was found.

**Deployment & data handling** — `saas` (Tonic Cloud) or `self-hosted` (container deployment; Enterprise tiers of Structural, Textual and Fabricate). `data_leaves_tenancy: partial`: in Tonic Cloud, production data and documents are processed by Tonic. Self-hosted, they stay in the customer's environment. Textual is also available as an AWS Marketplace AMI and a Snowflake Native App, which keep processing inside those platforms. Out-of-band batch processing, not inline. Retention and sub-processor terms for Tonic Cloud were not reviewed.

**Integrations & partnerships** — Source connectors span relational databases, data lakes, NoSQL, flat files and SaaS apps (Fabricate Enterprise lists SQL Server and Oracle exports; full connector list not reviewed). AWS strategic collaboration agreement (2025-04-08) and AWS Marketplace listing. Snowflake Native App. Microsoft Fabric GA for Textual (2026-03-18). **MCP:** an open-source Textual MCP server (`@tonicai/textual-mcp`, March 2026) exposes redaction tools to MCP clients such as Claude Code and Cursor. That makes it usable as a redaction step inside agent workflows.

**Compliance & FS traction** — Site shows SOC 2, HIPAA and GDPR badges. SOC 2 type and report date unverified. A case study references CSA STAR. **FS traction claimed:** homepage logos include Texas Capital Bank, Greenlight, iCapital and Vestmark, and the 2025 release names American Express. No FS case study was read, and no hedge-fund customer was found.

**Commercial** — Structural: annual contracts by plan and connected source-data size (Professional up to 10TB, 10 users, cloud only; Enterprise unlimited, cloud or self-hosted). Textual: pay-as-you-go per 1,000 words or an annual word bank. Fabricate: free ($5 credits), Plus at $29/month, Enterprise custom. No dollar figures are published for Structural or Textual.

## Open questions

- Total funding and any round after the 2021 Series B (the April 2025 aggregator listing is unconfirmed).
- SOC 2 Type II report date; ISO 27001; Tonic Cloud hosting regions, retention and sub-processors.
- Ephemeral pricing and whether it is sold standalone or only with Structural.
- Named financial-services references, especially buy-side.
- Detection accuracy of Textual versus Presidio-based pipelines (no independent benchmark found).

## Sources

- [Tonic.ai homepage](https://www.tonic.ai/) — fetched 2026-10-26 — supports: product line, deployment, compliance badges, FS logos; confidence: medium (vendor marketing)
- [Tonic.ai pricing](https://www.tonic.ai/pricing) — fetched 2026-10-26 — supports: pricing model and tiers, self-hosted availability; confidence: high
- [Tonic.ai acquires Fabricate (press release)](https://www.tonic.ai/press-releases/tonic-ai-acquires-fabricate-expanding-its-leadership-in-synthetic-data) — fetched 2026-10-26 — supports: 2025-04-22 acquisition, founding 2018, HQ, named customers; confidence: high
- [Tonic.ai lands $35M Series B (BigDATAwire)](https://www.hpcwire.com/bigdatawire/this-just-in/tonic-ai-lands-35m-series-b-funding-puts-fake-data-at-forefront-of-growth/) — via search 2026-10-26 — supports: Series B 2021-09-29, investors; confidence: high
- [Meet Tonic Ephemeral (Tonic blog)](https://tonic.ai/blog/ephemeral-databases-on-demand-have-arrived-meet-tonic-ephemeral) — via search 2026-10-26 — supports: Ephemeral capabilities; confidence: medium (vendor)
- [Textual MCP server (Tonic docs)](https://docs.tonic.ai/textual/textual-integrations/textual-mcp-server) — via search 2026-10-26 — supports: MCP server; confidence: high
- [Tonic Textual GA for Microsoft Fabric](https://www.tonic.ai/press-releases/tonic-textual-general-availablity-for-fabric) — via search 2026-10-26 — supports: 2026-03-18 Fabric GA; confidence: medium
- Cached: `raw/sources/2026-10-26--tonic-ai--products-pricing-fabricate.md`

## History

- [2026-10-26] Page created via wiki-create and researched the same day, as one of the three seed vendors of the new [synthetic-masked-data](../categories/synthetic-masked-data.md) category. No cross-listing: Textual's redaction overlaps DLP-style use cases but Tonic does not market it as DLP.
