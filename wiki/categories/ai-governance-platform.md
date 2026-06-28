---
title: AI Governance / Model Risk & Compliance
type: category
name: AI Governance / Model Risk & Compliance
slug: ai-governance-platform
layer: governance
priority: day-2
trifecta_role: none-detection
maps_to_seed_doc: AI Governance Platform
maps_to_seed_csv: AI Governance, Model Risk & Compliance
vendor_count: 13
status: drafted
last_updated: 2026-06-28
---

## Business objective

The control tower for AI risk. An AI governance platform inventories every model,
prompt, agent, and AI use case in the firm, then maps each to a control framework
(NIST AI RMF, EU AI Act, ISO 42001, and — for a regulated financial firm — internal
model-risk policy). The job it does is **prove and manage AI risk to regulators and
the board**: a single register of "what AI do we run, who owns it, what could go
wrong, and what controls sit on it." It is the governance system of record that the
runtime tools ([ai-runtime-security](ai-runtime-security.md), [llm-observability](llm-observability.md), [ai-access-governance](ai-access-governance.md))
feed evidence into.

## When you need it

Nominally **Day-2** for a generic enterprise — you can run a pilot before you have a
governance platform. But for a hedge fund or asset manager this is effectively
**Day-1 under SR 11-7**. The Fed/OCC model-risk guidance (SR 11-7) treats any model
that drives investment, valuation, or risk decisions as something requiring
documented development, independent validation, ongoing monitoring, and an inventory.
An LLM that touches the investment process, research, or trade rationale is a model
under that lens. A CTO at a regulated shop should expect their model-risk and
compliance functions to demand exactly the inventory, lineage, validation evidence,
and attestations these platforms produce. If you already maintain an SR 11-7 model
inventory in a spreadsheet or [enterprise-grc](enterprise-grc.md) tool, the question is whether AI use
cases get folded into that or into a dedicated AI-governance platform — most firms
start with the GRC tool they already own and add an AI module or a specialist
platform once the AI footprint grows.

## Lethal-trifecta role

**None-detection / oversight.** This layer does not sit inline and does not break a
leg of the lethal trifecta itself. It is the documentation, attestation, and
audit-trail layer that records *which* controls break the trifecta and proves they
exist. It lives in the **green (governed) zone** as a system of record, consuming
evidence from the inline controls rather than enforcing at runtime.

## Vendors

Specialist AI-governance / model-risk platforms:

- [credo-ai](../vendors/credo-ai.md) — AI governance and registry; policy packs mapped to NIST AI RMF / EU AI Act.
- [holistic-ai](../vendors/holistic-ai.md) — AI governance, risk, and auditing; bias/robustness assessment lean.
- [modelop](../vendors/modelop.md) — model lifecycle governance with deep roots in traditional MRM/SR 11-7 model inventory.
- [monitaur](../vendors/monitaur.md) — model governance and assurance aimed at regulated (esp. insurance/financial) use.
- [fairly-ai](../vendors/fairly-ai.md) — AI governance and compliance automation; policy-as-checklist framing.
- [ibm-watsonx-governance](../vendors/ibm-watsonx-governance.md) — governance module of the watsonx stack; lifecycle + risk dashboards.
- [governgpt](../vendors/governgpt.md) — AI governance / due-diligence automation (positioning TBD on depth).
- [cranium](../vendors/cranium.md) — AI security + governance posture; inventory of AI assets and supply chain.

Adjacent platforms that also carry an AI-governance module (cross-listed):

- [onetrust](../vendors/onetrust.md) — privacy/GRC suite with an AI governance module; strong if you already own OneTrust.
- [vanta](../vendors/vanta.md) — compliance automation (SOC 2, ISO) extending into AI governance / ISO 42001.
- [securiti](../vendors/securiti.md) — data + AI governance, anchored in DSPM and data lineage.
- [collibra](../vendors/collibra.md) — data governance/catalog extending to AI/model registry.
- [calypsoai](../vendors/calypsoai.md) — runtime AI security vendor with governance/reporting framing (per seed; acq. by F5 — unverified).

Observability vendors with governance reporting also overlap here: [fiddler-ai](../vendors/fiddler-ai.md),
[arthur-ai](../vendors/arthur-ai.md).

## Consolidation / M&A dynamics

The space is fragmented — specialist startups (Credo, Holistic, Monitaur, Fairly)
versus governance modules bolted onto incumbents (OneTrust, IBM, ServiceNow,
Collibra, Vanta). [calypsoai](../vendors/calypsoai.md) is flagged as acquired by F5 (per seed; unverified —
to confirm in research), which would pull a runtime-security vendor into the
governance reporting conversation. Expect continued absorption of point AI-governance
tools into broader GRC and data-governance suites.

## Adjacent categories

- [enterprise-grc](enterprise-grc.md) — the general system of record for risk/controls; AI governance is often a module inside it rather than a separate tool.
- [llm-observability](llm-observability.md) — supplies the runtime evaluation/monitoring evidence that proves controls work.
- [ai-spm](ai-spm.md) — discovers and inventories AI assets/agents; feeds the governance inventory.
- [ai-runtime-security](ai-runtime-security.md) — the enforcement layer whose policies governance attests to.
- [comms-surveillance](comms-surveillance.md) — a parallel governance/detective discipline specific to MAR/MNPI.

## Survey

**Question.** Which AI governance / model-risk & compliance platforms is your firm
using or evaluating to inventory AI use cases and map them to frameworks (NIST AI
RMF, EU AI Act, SR 11-7 model risk)?

**Answer options.** Credo AI; Holistic AI; ModelOp; Monitaur; Fairly AI; IBM
watsonx.governance; GovernGPT; Cranium; OneTrust (AI Governance); Vanta; Securiti;
Collibra; CalypsoAI; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** Heavy overlap with [enterprise-grc](enterprise-grc.md): many respondents
will "govern AI" inside ServiceNow/Archer/OneTrust rather than a dedicated tool — ask
both and reconcile. ModelOp and Monitaur skew to firms with a mature SR 11-7 MRM
function; Credo/Holistic/Fairly skew to newer AI-RMF/EU-AI-Act framing. OneTrust,
Vanta, Securiti, Collibra are table-stakes-adjacent because firms may already own
them for other reasons. CalypsoAI's M&A status (F5, per seed) may date that option.
For a hedge-fund audience, consider asking whether AI use cases live in the existing
model-risk inventory vs a new platform.

## Open taxonomy questions

- Where is the line between this and [enterprise-grc](enterprise-grc.md)? For many firms AI governance
  is a GRC module, not a separate product — the survey must let respondents say so.
- [ai-spm](ai-spm.md) (discovery/inventory of AI assets) vs governance platform (risk mapping
  + attestation) overlap on "AI inventory." Worth a comparison page.
- Observability vendors (Fiddler, Arthur) straddle [llm-observability](llm-observability.md) and
  governance; primary listing kept under observability.
