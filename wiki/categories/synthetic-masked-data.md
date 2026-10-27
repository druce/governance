---
title: Synthetic & Masked Data
type: category
name: Synthetic & Masked Data
slug: synthetic-masked-data
category: synthetic-masked-data
layer: data
survey_question: Synthetic / Masked Data
adoption_tier: day-2
trigger: developers, testers or model-training jobs need realistic data without exposing production PII or client data
maturity_stage_required: null
category_maturity: consolidating
adjacent: [dspm, dlp, ephemeral-environments]
incumbent_coverage: []
vendor_count: 3
maps_to_seed_doc: null
maps_to_seed_csv: null
last_verified: 2026-10-26
---

# Synthetic & Masked Data

## Job to be done

Give developers, testers, data scientists and AI pipelines **realistic data that is not real client data**, so production PII, client positions and MNPI never have to be copied into dev, test, a vendor sandbox or a training set.

## Business objective

Every firm that builds software or models faces the same temptation: the quickest way to get realistic data into a test database, a vendor proof-of-concept or a fine-tuning job is to copy production. That copy then lives in a lower-security environment with broader access, weaker logging, and sometimes a third party's cloud. Non-production copies of production data are a long-standing, mundane source of breaches and regulatory findings.

This category replaces that copy with one of three things:

1. **Masked / de-identified production data (test data management, TDM).** Take a production database, replace names, account numbers, emails and other identifiers with realistic fakes, consistently across tables so joins still work, and usually **subset** it to a manageable slice. Tools: [tonic-ai](../vendors/tonic-ai.md) Structural, [k2view](../vendors/k2view.md) TDM, Delphix, Informatica TDM, Broadcom TDM.
2. **Synthetic data.** Generate new records that keep the statistical shape of the original, or invent data from a schema or prompt when no production data exists. Model-based tabular synthesis ([gretel](../vendors/gretel.md), now NVIDIA NeMo Safe Synthesizer; MOSTLY AI; SAS Data Maker) suits analytics and ML. Schema- or LLM-driven generation (Tonic Fabricate, NVIDIA NeMo Data Designer) suits greenfield development and AI evaluation sets.
3. **Unstructured redaction and synthesis.** Find and redact or replace PII in free text, documents, emails and transcripts before they are used to fine-tune a model or indexed for RAG. Tools: Tonic Textual, or self-built pipelines on open-source [presidio](../vendors/presidio.md).

The risk mitigated is **sensitive-data exposure through non-production paths**: dev and test environments, contractors and offshore QA, vendor PoCs, analytics sandboxes, and model training data (where a model can memorise and later regurgitate what it was trained on).

## In scope / out of scope

- **In scope:** test-data masking and subsetting, synthetic data generation (tabular, relational, text), batch PII redaction/de-identification of datasets and documents for dev, test, training and RAG ingestion, and on-demand provisioning of masked test databases.
- **Not [dspm](dspm.md).** DSPM *finds and labels* sensitive data at rest and reports its exposure. This category *produces safe substitutes* for it. TDM tools have their own discovery step (K2view, Tonic), but only to drive masking rules.
- **Not [dlp](dlp.md).** DLP and AI-prompt guardrails *inspect data in motion* (email, uploads, prompts) and block or redact inline. Masking/synthesis is an out-of-band, batch transformation of datasets. The same detection engines (e.g. Presidio) appear in both.
- **Not [ephemeral-environments](ephemeral-environments.md).** Disposable compute for risky work is a practice. Masked data is often what you load *into* an ephemeral environment (Tonic Ephemeral sits on the boundary).
- **Not dynamic data masking** in a database or BI tool (masking columns at query time for certain users). That is a database or [data-access-governance](data-access-governance.md) feature.

## Framework mapping

- OWASP LLM Top 10 (2025): LLM02 Sensitive Information Disclosure (keep PII out of training and RAG corpora so the model cannot leak it).
- MITRE ATLAS: training-data inference and extraction techniques (membership inference, training-data extraction). Synthetic or redacted training data reduces what can be recovered.
- NIST AI RMF: MAP and MEASURE privacy functions (MEASURE 2.10, privacy risk of the AI system examined and documented). NIST SP 800-188 (de-identifying government datasets) is the reference for de-identification method.

## When you need it

**Day-2.** It is not a precondition for using AI. Nothing breaks on day one without it. It becomes necessary when the trigger fires: **developers, testers or model-training jobs need realistic data and the alternative is copying production.** For a fund that usually shows up in one of these ways:

- **Client, investor and MNPI data in dev/test.** In-house teams building or changing OMS/PMS integrations, investor-relations portals, CRM, fund-admin reconciliation or risk systems test against copies of production. Those copies contain LP identities, positions and trading data, which is MNPI in some contexts. Masked copies let the work proceed without widening access to that data.
- **Training and evaluation data for in-house models.** Fine-tuning or evaluating a model on research notes, emails, call transcripts or client communications needs PII redaction first. A model trained on raw data can reproduce it, and once trained the data cannot easily be removed. Synthetic eval sets (Data Designer-style) let you test agents without real client records.
- **Vendor PoCs and third parties.** Every AI vendor evaluation wants "your real data". A masked or synthetic dataset with realistic shape lets you run a meaningful PoC without sending client data to a startup that has not cleared vendor due diligence.
- **Offshore or contractor development** and analytics sandboxes with broad access.

Crawl/Walk/Run/Fly: not needed at Crawl (chat assistants on vendor platforms). It becomes relevant at Walk/Run, once the firm builds its own AI applications, RAG pipelines or fine-tunes. It is table stakes for any firm with a sizeable in-house engineering team, AI or not. **Firm-type applicability:** high for multi-strategy and quant funds and large asset managers with in-house development. Low for small funds that buy SaaS and write little software, where the cheaper control is simply "no production data outside production" plus vendor contracts. Bank-affiliated managers often already run an enterprise TDM suite (Informatica, Broadcom, Delphix) under group policy.

## Security role

A **preventive, out-of-band** data-layer control. It does not inspect traffic or block anything at runtime. It **removes sensitive data from paths where it should never have been**, so a breach of a test environment, a vendor sandbox or a model's training set exposes fakes instead of client data. It depends on discovery (knowing which columns and fields are sensitive, ideally informed by [dspm](dspm.md) classifications) and fails silently when discovery misses a field. A free-text "notes" column full of client names that nobody flagged goes straight into the test copy. Synthetic data is not automatically anonymous either: model-based generators can memorise rare records, so privacy evaluation (and differential privacy where offered) matters.

## Sourcing posture

- **Buy (point tool):** [tonic-ai](../vendors/tonic-ai.md) for developer-led masking, redaction and generation; [k2view](../vendors/k2view.md) for cross-system entity-based TDM in large estates.
- **Buy (legacy suite / incumbent module):** Delphix (Perforce), Informatica TDM (Salesforce), Broadcom TDM. **If you already own Informatica or a Perforce/Delphix estate, you may already have masking and subsetting licensed.** Check before buying another tool.
- **Free / OSS:** NVIDIA NeMo Safe Synthesizer and Data Designer (ex-[gretel](../vendors/gretel.md), Apache-2.0), the MOSTLY AI Synthetic Data SDK (Apache-2.0), and [presidio](../vendors/presidio.md) for text redaction. Credible for a team with data engineers. You own the operations and the accuracy.
- **Build:** many funds run home-grown masking scripts (SQL updates, Faker). This works for a few databases and breaks on referential integrity, schema drift and free text.
- **Feature-vs-company risk: high for synthetic-data startups, lower for TDM.** Standalone synthetic-data vendors have been absorbed by larger platforms (Gretel to NVIDIA, Hazy to SAS, MOSTLY AI's brand to Syntho), and Delphix went to Perforce. TDM has survived as a product line for decades, usually inside a larger data or DevOps vendor.

## Market structure

**Maturity: consolidating.** TDM is a mature, decades-old market (Informatica, Broadcom/CA, IBM-era tools). Model-based synthetic data was a 2019–2023 venture wave that has now largely been absorbed. Generative AI has revived demand on two fronts: redaction of unstructured data for training and RAG, and synthetic eval and training sets.

**Consolidation ledger:**

| Target | Acquirer | Announced | Closed | Notes |
|---|---|---|---|---|
| Delphix | Perforce (Francisco Partners / Clearlake-backed) | 2024-02-14 | 2024-03-25 | Terms undisclosed; delphix.com now redirects to perforce.com |
| Hazy (principal software assets) | SAS | 2024-11 | not separately reported | Asset deal; technology in SAS Data Maker (GA, Microsoft Marketplace 2025-11) |
| Gretel | NVIDIA | 2025-03-19 (press reports; NVIDIA never confirmed) | reported as completed 2025-03-19 | Reported nine-figure price; product absorbed into NeMo, gretel.ai redirects to NVIDIA |
| Fabricate (from Mockaroo) | Tonic.ai | 2025-04-22 | 2025-04-22 | Product tuck-in; price undisclosed |
| Informatica | Salesforce | 2025-05-27 | 2025-11-18 | ~$8B; Informatica TDM now a Salesforce-owned product line |
| MOSTLY AI (trademark and related assets) | Syntho | 2026-06-09 | not reported | Brand continues as "MOSTLY AI, powered by Syntho"; original company status unclear |

Implication for shortlists: half the recognisable names now sit inside a larger vendor. Survey options must use current owner names, and buyers should ask about roadmap commitment.

**Overlap map:**

| Vendor | This category | Also overlaps |
|---|---|---|
| [tonic-ai](../vendors/tonic-ai.md) | Masking, subsetting, text redaction, synthesis, ephemeral DBs | [dlp](dlp.md)-adjacent (Textual redaction; Textual MCP server for agent workflows) |
| [k2view](../vendors/k2view.md) | Entity-based TDM, masking, synthetic data | Data integration; agent data access via MCP; discovery overlaps [dspm](dspm.md) in function, not in market |
| [gretel](../vendors/gretel.md) (NVIDIA NeMo) | Model-based synthetic tabular data; synthetic training/eval sets | AI development platform (NVIDIA NeMo) |
| [presidio](../vendors/presidio.md) (OSS) | Detection/redaction engine used in DIY pipelines | Primary in [ai-red-teaming](ai-red-teaming.md); also [dlp](dlp.md) |

## Vendors

- [tonic-ai](../vendors/tonic-ai.md) — `leader`. Developer-oriented suite: Structural (database masking/subsetting), Textual (unstructured PII redaction/synthesis for AI training and RAG), Ephemeral (throwaway test databases), Fabricate (from-scratch generation). SaaS or self-hosted.
- [k2view](../vendors/k2view.md) — `challenger`. Entity-based enterprise TDM: masks and subsets a "customer" consistently across many systems of record. Heavier platform, suited to large multi-system estates.
- [gretel](../vendors/gretel.md) — `platform-module`. Acquired by NVIDIA (reported 2025-03-19). No longer sold standalone. Lives on as open-source NeMo Safe Synthesizer (privacy-safe synthetic tables) and NeMo Data Designer (synthetic AI training/eval datasets).

**Also in this space (no wiki pages yet; status verified 2026-10-26):**
- **Delphix (Perforce)** — TDM with masking and virtualised data copies. Acquired by Perforce, announced 2024-02-14, closed 2024-03-25.
- **Informatica Test Data Management (Salesforce)** — long-standing subset/mask/generate suite plus cloud masking in IDMC. Informatica acquired by Salesforce, closed 2025-11-18. The English TDM product page now redirects to Informatica's data-governance page, so packaging is unclear.
- **Broadcom Test Data Manager** — ex-CA Technologies TDM (subsetting, masking, synthetic generation; mainframe to cloud). Product page live; 4.10 described as the latest release.
- **SAS Data Maker (formerly Hazy)** — SAS acquired Hazy's principal software assets in November 2024. Data Maker went GA and launched on Microsoft Marketplace in November 2025.
- **MOSTLY AI (now "powered by Syntho")** — Syntho announced acquiring the MOSTLY AI trademark and related assets on 2026-06-09. The Apache-2.0 Synthetic Data SDK is still releasing (v6.2.0, 2026-10-12). A CB Insights listing says the original company ceased operations in March 2026 (unverified).

Not checked on this pass (candidates for a later sweep): IBM InfoSphere Optim, Datprof, Syntho as a standalone vendor, GenRocket, Protegrity/Privacera-style tokenisation vendors, cloud-native options (e.g. AWS/Google de-identification services).

## Selection guidance

**POC questions:**
1. **Discovery coverage:** how does it find sensitive columns and free-text fields, and how do you review what it missed? Run it against a schema you know well and count the misses.
2. **Referential integrity across systems:** if the same client appears in the OMS, CRM and fund-admin extract, is the masked value consistent across all three?
3. **Schema drift:** what happens when production adds a column? Does the job fail safe (block) or pass the new column through unmasked?
4. **Where does production data go?** Self-hosted, in your cloud, or the vendor's SaaS? For SaaS: region, retention, sub-processors.
5. **Unstructured data:** accuracy on your own documents (research notes, emails, transcripts) for names, tickers and account numbers. Can you train custom entities? Can it replace with realistic values instead of `<REDACTED>`?
6. **Synthetic privacy evidence:** does it produce a privacy report (memorisation, nearest-neighbour distance, differential-privacy settings) you can show compliance?
7. **Provisioning:** API and CI integration, refresh cadence, per-developer or ephemeral copies.
8. **Sources supported:** your actual databases (SQL Server, Postgres, Snowflake, Oracle, mainframe?) and file formats.

**Archetypes:**
- *Small fund, little in-house development:* you probably do not need to buy anything. Enforce "no production data outside production" and use vendor-supplied demo data for PoCs. If you fine-tune or build RAG, run Presidio-based redaction in the pipeline.
- *Mid-sized fund with a real engineering team (OMS/PMS integrations, internal apps, RAG):* a point tool such as [tonic-ai](../vendors/tonic-ai.md), self-hosted, covering both database masking and document redaction.
- *Large or bank-affiliated manager with many systems of record:* first check existing Informatica/Delphix/Broadcom entitlements. Evaluate [k2view](../vendors/k2view.md) where cross-system entity consistency is the pain.
- *Quant/data-science team needing synthetic tables for research or ML:* NVIDIA NeMo Safe Synthesizer (ex-[gretel](../vendors/gretel.md)) if you have GPUs and engineers; otherwise a commercial synthetic-data product (SAS Data Maker, MOSTLY AI/Syntho).

**Procurement:** enterprise annual contracts, usually priced by connected source-data volume or number of databases (Tonic Structural), by words processed (Tonic Textual), or by platform scope (K2view, legacy TDM). OSS options cost only compute and engineering time. Public price points are rare.

**If you skip it:** production copies accumulate in dev, test and vendor environments with weaker controls. A breach of any of them is a breach of client data, and an examiner asking "where does client PII live?" gets a longer answer than it should. For AI specifically, a model fine-tuned on unredacted client communications can reproduce them, and the data cannot be pulled back out of the weights.

## Adjacent categories

- [dspm](dspm.md) — finds and classifies the sensitive data. A good DSPM inventory tells the masking job which fields to transform.
- [dlp](dlp.md) — inline inspection and redaction of data in motion and prompts. Shares detection engines but acts at runtime, not on datasets.
- [ephemeral-environments](ephemeral-environments.md) — disposable compute for risky work. Masked or synthetic data is what should be loaded into it.

## Survey

- **Question** — Which synthetic-data or test-data masking tools is your firm using or evaluating to give developers, testers or AI training/evaluation jobs realistic data without exposing production client or personal data?
- **Answer options** — Tonic.ai; K2view; NVIDIA NeMo Safe Synthesizer / Data Designer (formerly Gretel); Delphix (Perforce); Informatica Test Data Management (Salesforce); Broadcom Test Data Manager; SAS Data Maker (formerly Hazy); MOSTLY AI (Syntho); Presidio (ex-Microsoft, open source); Other (Please Specify).
- **Response scale** — multi-select: Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.
- **Notes for survey design** —
  - Niche for most hedge funds: expect low adoption outside multi-strategy, quant and large asset managers with in-house development. Consider a screener ("Do you copy production data into dev/test or training sets?") or a "Home-grown scripts" option so the common answer is captured.
  - Three jobs share one question: database masking/TDM, synthetic generation, and unstructured redaction for AI. Respondents may answer for only one. Consider sub-questions if the response count justifies it.
  - M&A dates several options: Gretel is now NVIDIA NeMo; Hazy is SAS Data Maker; Delphix is Perforce; Informatica is Salesforce; MOSTLY AI's brand belongs to Syntho. Use the current owner in labels and keep "formerly X" for recognition.
  - Presidio also appears under DLP/guardrail-style questions. Respondents using it for prompt redaction may tick it here too.

## Open questions

- Should unstructured redaction for AI training/RAG (Tonic Textual, Presidio pipelines) live here or under [dlp](dlp.md)? Placed here for now because it is a batch dataset transformation.
- Does Tonic Ephemeral warrant a cross-list to [ephemeral-environments](ephemeral-environments.md) (a practice-tier category with no survey question)?
- Pages for Delphix (Perforce) and Informatica TDM if survey write-ins show they are in use at funds.
- Tier: is this `situational` (trigger-driven, depends on in-house development) rather than `day-2`? Kept day-2 per the 2026-10-26 human decision.

## History

- [2026-10-26] Category page created after the human approved the new `synthetic-masked-data` category in taxonomy.yaml. Seeded with tonic-ai, gretel and k2view; other vendors listed without pages after status checks. Sources cached in `raw/sources/2026-10-26--synthetic-masked-data--market-ma.md` and the per-vendor 2026-10-26 files.
