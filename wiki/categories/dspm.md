---
title: Data Classification & DSPM
type: category
name: Data Classification & DSPM
slug: dspm
layer: data
priority: day-1
trifecta_role: sensitive-data (detection — finds and labels the sensitive data leg)
maps_to_seed_doc: Data Classification & DSPM
maps_to_seed_csv: DSPM / Data Governance / DLP (split — see Survey notes)
vendor_count: 15
status: drafted
last_updated: 2026-06-28
---

# Data Classification & DSPM

## Business objective

Data Security Posture Management (DSPM) discovers, classifies, and assesses the
posture of **data at rest** across cloud stores, SaaS, databases, and file shares.
It is the labeler that knows *where* sensitive data lives — Client confidential,
Employee confidential, Legal privileged, IP, MNPI, PII — and *how exposed* it is
(who can reach it, whether it is encrypted, whether it sits in the wrong place).

You cannot protect, or decide what an AI model is allowed to retrieve, data you
have not found and classified. DSPM is the map that every downstream data control
([dlp](dlp.md), [data-access-governance](data-access-governance.md), [entitlement-aware-rag](entitlement-aware-rag.md)) reads from.

## When you need it

**Day-1.** For a hedge fund the sensitive-data inventory is foundational: you have
MNPI, PII, and privileged/IP material scattered across SharePoint, OneDrive, email,
data warehouses, and SaaS. Before you point any AI assistant or RAG pipeline at
internal content, you need to know what is sensitive and where it is. DSPM is also
the precondition for credible model-risk and regulatory conversations (you can show
where regulated data lives and who can touch it).

## Lethal-trifecta role

DSPM addresses the **sensitive-data** leg, in **detection** mode — it does not block
anything at runtime, it *finds and labels* the sensitive data so other controls can
act. It mostly inventories data sitting in the **green zone** (internal stores) and
flags where that data is over-exposed to yellow/red paths. It is the discovery layer
underneath the enforcement controls; on its own it breaks no leg, but nothing else
in the data layer works well without it.

## Vendors

Broad-platform / data-governance-led:

- [microsoft-purview](../vendors/microsoft-purview.md) — native classification + labeling across the Microsoft
  estate; default for M365/Azure-heavy shops (also does [dlp](dlp.md)).
- [bigid](../vendors/bigid.md) — discovery and classification breadth across structured/unstructured;
  privacy and data-governance heritage.
- [securiti](../vendors/securiti.md) — data command-center spanning DSPM, privacy, and AI governance.
- [collibra](../vendors/collibra.md) — data-catalog/governance lineage; more cataloging than security posture.
- [immuta](../vendors/immuta.md) — data-access policy and governance for analytic data platforms.

Cloud-native DSPM:

- [cyera](../vendors/cyera.md) — AI-driven data classification; spans DSPM, [dlp](dlp.md), and
  [data-access-governance](data-access-governance.md).
- [sentra](../vendors/sentra.md) — cloud DSPM with data-access context.
- [normalyze](../vendors/normalyze.md) — cloud-data security posture (seed flags acquisition — see below).
- [wiz](../vendors/wiz.md) — DSPM as part of a broader cloud-security platform (also [ai-spm](ai-spm.md)).
- [bedrock-security](../vendors/bedrock-security.md) — data-store discovery and posture.
- [symmetry-systems](../vendors/symmetry-systems.md) — data-store-centric posture and access analysis.
- [concentric-ai](../vendors/concentric-ai.md) — AI-based classification of unstructured data (also
  [data-access-governance](data-access-governance.md)).
- [rubrik](../vendors/rubrik.md) — DSPM bolted onto data-resilience/backup footprint.

Cross-listed:

- [onetrust](../vendors/onetrust.md) — data discovery/classification within a broader GRC/privacy suite.
- [netskope](../vendors/netskope.md) — DSPM as part of its SSE/data-protection platform.

## Consolidation / M&A dynamics

- [normalyze](../vendors/normalyze.md) — acquired by Proofpoint (per seed; unverified — to confirm in research).
- [wiz](../vendors/wiz.md) — acquired by Google (per seed; unverified — to confirm in research).

Beyond the specific flags, DSPM is consolidating in two directions: cloud-security
platforms (Wiz, Netskope) absorbing it as a feature, and data-governance/privacy
suites (OneTrust, Securiti, Collibra) folding it in alongside cataloging.

## Adjacent categories

- [dlp](dlp.md) — DSPM finds and labels data at rest; DLP enforces at the egress moment.
  The CSV merges them; we keep them split (see Survey notes).
- [data-access-governance](data-access-governance.md) — consumes DSPM classification to right-size *who can
  reach* the sensitive data; several vendors do both.
- [entitlement-aware-rag](entitlement-aware-rag.md) — relies on classification/labels so an AI assistant
  never retrieves data the user could not see.
- [ai-spm](ai-spm.md) — posture management for AI assets, conceptually parallel to DSPM for data.

## Survey

**Question.** Which data classification / DSPM tools is your firm using or
evaluating to discover and classify sensitive data at rest?

**Answer options.** Microsoft Purview, BigID, Securiti, Cyera, Sentra, Normalyze,
Wiz, Bedrock Security, Symmetry Systems, Concentric AI, Rubrik, Immuta, Collibra,
OneTrust, Netskope, Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.**
- The seed CSV asks one merged question (`DSPM / Data Governance / DLP`). Per
  taxonomy gap **D2** we split it into DSPM (this page) and [dlp](dlp.md). Several
  vendors — Cyera, Sentra, Concentric AI, Microsoft Purview, Netskope — legitimately
  answer *both* questions; expect respondents to tick the same vendor on both pages,
  and note that on the DLP page too.
- Table-stakes for most respondents: Microsoft Purview (often already owned via M365).
- Watch overlap confusion between "DSPM" and "data catalog/governance" — Collibra and
  Immuta lean governance/cataloging, not security posture; some respondents will not
  think of them as DSPM.
- M&A may date options: confirm Normalyze (Proofpoint) and Wiz (Google) status before
  fielding.

## Open taxonomy questions

- Where does data *cataloging/governance* (Collibra, Immuta) end and security *posture*
  begin? They sit on this page for now but lean toward a governance cut.
- Overlap with [data-access-governance](data-access-governance.md) is heavy (Cyera, Sentra, Concentric, Immuta
  appear on both) — candidate for a future merge or explicit primary/secondary split.
- The CSV merge (DSPM+DLP+governance) vs the doc's split is the core open tension;
  resolved here in favor of the doc spine but flagged for survey design.
