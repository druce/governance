---
title: CATEGORY_NAME
type: category
name: CATEGORY_NAME
slug: category-slug
category: category-slug
layer: null                     # must match taxonomy.yaml
survey_question: null           # must match taxonomy.yaml
adoption_tier: null             # must match taxonomy.yaml
trigger: null                   # must match taxonomy.yaml
maturity_stage_required: null   # crawl | walk | run | fly
category_maturity: null
adjacent: []
incumbent_coverage: []
vendor_count: 0
maps_to_seed_doc: null
maps_to_seed_csv: null
last_verified: null
---

# CATEGORY_NAME

## Job to be done

TBD — one sentence, buyer language.

## Business objective

TBD — what this layer is for, the threat/risk it mitigates.
<!-- Lethal-trifecta discussion ONLY if agent_security_context: true in taxonomy.yaml (SCHEMA.md §0) -->

## In scope / out of scope

TBD — name the adjacent thing this is NOT.

## Framework mapping

- OWASP LLM Top 10: TBD
- MITRE ATLAS: TBD
- NIST AI RMF: TBD

## When you need it

TBD — defend the adoption tier with the trigger condition; Crawl/Walk/Run/Fly
stage; firm-type applicability.

## Sourcing posture

TBD — buy / build / free / already-covered; feature-vs-company risk;
incumbent coverage check ("if you own X, you may already have this").

## Market structure

TBD — maturity, consolidation ledger (dated, announced vs closed), overlap map.

## Vendors

<!-- - [slug](../vendors/slug.md) — one-line positioning; group into sub-segments if the category splits -->

## Selection guidance

TBD — 5–10 POC evaluation questions; "if you are X firm with Y stack, start
with Z"; procurement notes; what happens if you skip it.

## Adjacent categories

<!-- - [slug](slug.md) — how they overlap -->

## Survey

<!-- omit this whole section if adoption_tier is `practice` -->
- **Question** — TBD (use/evaluate framing).
- **Answer options** — vendor list + `Other (Please Specify)`.
- **Response scale** — multi-select: Interested; Considering/evaluating; Pilot/implementing; In production; Would recommend; Would not recommend.
- **Notes for survey design** — table-stakes vs niche, confusing overlaps, M&A that dates an option.

## Open questions

- TBD

## History

- [YYYY-MM-DD] Page scaffolded via wiki-create.
