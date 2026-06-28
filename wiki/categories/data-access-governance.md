---
type: category
name: Data Access Governance
slug: data-access-governance
layer: data
priority: day-2
trifecta_role: sensitive-data (right-sizes who can reach the sensitive data leg)
maps_to_seed_doc: Data Access Governance
maps_to_seed_csv: — (doc-only; overlaps IGA survey question)
vendor_count: 10
status: drafted
last_updated: 2026-06-28
---

# Data Access Governance

## Business objective

Data Access Governance (DAG) audits and right-sizes *who can open which data*, and
monitors how data is actually accessed. The seed's metaphor: the **audit of who can
open which file** — the control that finds the folder where "Everyone" accidentally
has access. Where [[dspm]] tells you *what* sensitive data exists and *where*, DAG
tells you *who can reach it* and whether that access is justified, then helps you
remediate over-permissioned access.

This is the data-layer cousin of identity governance ([[identity-governance]]): IGA
governs access to *applications/systems*, DAG governs access to *data* (files,
shares, warehouse tables, SaaS objects).

## When you need it

**Day-2 in general — but Day-1 if you are doing RAG.** The reason: the instant an AI
assistant retrieves on a user's behalf, every over-permissioned folder becomes a
data-leak surface. RAG inherits the permissions mess; if "Everyone" can see a
sensitive folder, the chatbot will happily surface it to anyone who asks. So for a
hedge fund standing up an enterprise assistant or RAG pipeline, DAG (alongside
[[entitlement-aware-rag]]) moves to Day-1. Absent RAG, it is a Day-2 hygiene project.

## Lethal-trifecta role

DAG works the **sensitive-data** leg: by shrinking who can reach sensitive data, it
limits how easily that data can be lined up with untrusted input and egress. It is a
**green-zone** control — it governs access inside your trusted internal stores — and
it is the precondition that makes entitlement-aware retrieval trustworthy. It does
not block at runtime; it reduces standing exposure.

## Vendors

Data-access-specialist:

- [[varonis]] — the category archetype; permissions analysis, sensitive-data
  monitoring, and remediation across file shares, SaaS, and cloud.
- [[netwrix]] — permissions auditing and data-access governance for files/AD.

DSPM vendors extending into access context:

- [[cyera]] — classification plus who-can-access analysis (also [[dspm]], [[dlp]]).
- [[sentra]] — cloud DSPM with data-access governance.
- [[concentric-ai]] — unstructured-data classification with access right-sizing.
- [[immuta]] — policy-based access control for analytic data platforms.

Identity-governance vendors extending into data:

- [[sailpoint]] — SailPoint Data Access Security extends IGA to unstructured data.
- [[veza]] — access-graph across systems and data; "who can do what" visibility.
- [[conductorone]] — AI-native IGA extending into data-access right-sizing.
- [[silverfort]] — identity-security platform with data-access controls.

## Consolidation / M&A dynamics

No specific acquisition flags in the seed for the primary vendors here. The structural
dynamic is convergence from two sides: DSPM vendors (Cyera, Sentra, Concentric) adding
access context, and IGA vendors (SailPoint, Veza, ConductorOne, Silverfort) extending
governance from applications down to data. DAG is as much an overlap zone as a
standalone market.

## Adjacent categories

- [[dspm]] — supplies the classification DAG right-sizes access against; heavy vendor
  overlap (Cyera, Sentra, Concentric, Immuta on both).
- [[identity-governance]] — IGA governs app/system access; DAG governs data access.
  The CSV's IGA/ISPM question is where survey respondents may place these vendors.
- [[entitlement-aware-rag]] — the RAG-time enforcement that depends on access being
  correctly governed first; DAG is the cleanup, entitlement-aware RAG is the guardrail.
- [[dlp]] — DAG limits standing access; DLP catches data on the way out.

## Survey

**Question.** Which data access governance tools is your firm using or evaluating to
audit and right-size who can access sensitive data?

**Answer options.** Varonis, Netwrix, Cyera, Sentra, Concentric AI, Immuta, SailPoint
(Data Access Security), Veza, ConductorOne, Silverfort, Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.**
- This is **doc-only** — the seed CSV has no dedicated DAG question; these vendors
  appear under the CSV's `Identity Governance & Visibility (IGA / ISPM)` and
  `DSPM / Data Governance / DLP` questions. Expect overlap: SailPoint, Veza,
  ConductorOne, Silverfort will also be ticked on the [[identity-governance]] survey;
  Cyera, Sentra, Concentric, Immuta on the [[dspm]] survey.
- Table-stakes anchor: Varonis (the recognized incumbent). Most others are extensions
  of an adjacent platform a respondent may already own.
- Consider framing the question around the RAG trigger ("if you are deploying AI
  assistants/RAG over internal content, how are you governing data access?") since
  that is when this becomes Day-1.

## Open taxonomy questions

- Strong overlap with both [[dspm]] and [[identity-governance]]; DAG may be better
  modeled as a *capability* spanning those two than as a standalone category — flag
  for the final taxonomy pass.
- Several vendors (Cyera, Sentra, Concentric, Immuta, SailPoint, Veza, ConductorOne,
  Silverfort) are cross-listed; confirm each one's primary home to avoid double-counting.
- Whether to surface "DAG for RAG readiness" as its own comparison page given the
  Day-1/Day-2 split hinges entirely on the RAG decision.
