---
type: category
name: Enterprise GRC
slug: enterprise-grc
layer: governance
priority: day-1
trifecta_role: none-detection
maps_to_seed_doc: Enterprise GRC
maps_to_seed_csv: Enterprize GRC
vendor_count: 7
status: drafted
last_updated: 2026-06-28
---

## Business objective

One governed register for risk, controls, policy, and audit. Enterprise GRC
(Governance, Risk, and Compliance) is the **system of record** where risks are
logged, controls are documented and tested, policies are version-controlled and
attested, and audit findings are tracked to closure. In the AI context it is where
your **AI risk tiers, approvals, and policy attestations actually live** — the
durable register that an [ai-governance-platform](ai-governance-platform.md) or runtime tool ultimately rolls
up into. It is the spreadsheet-of-record, industrialized.

## When you need it

**Day-1 — but usually already owned.** Any firm of meaningful size, and certainly any
regulated hedge fund or asset manager, already runs a GRC platform for SOX, cyber,
operational risk, and audit. The AI question is rarely "do we buy GRC?" and almost
always "do we extend the GRC tool we already have to cover AI risk?" For a CTO, the
practical Day-1 move is to add AI use cases as a risk class in the existing register —
risk tiers (see [risk-tiers](risk-tiers.md)), control mappings, and sign-off workflows (see
[promotion-gates](promotion-gates.md), [hitl-approvals](hitl-approvals.md)) — rather than standing up a parallel system.
Standing up a *new* GRC tool just for AI is almost never the right call.

## Lethal-trifecta role

**None-detection / oversight.** GRC does not sit inline on any data path and breaks no
leg of the lethal trifecta directly. It is the governance backbone in the **green
(governed) zone**: the place where the existence and testing of trifecta-breaking
controls is recorded, attested, and audited.

## Vendors

- [servicenow](../vendors/servicenow.md) — GRC built on the ServiceNow platform; strong where the firm already runs ServiceNow ITSM/workflow.
- [archer](../vendors/archer.md) — long-standing enterprise GRC suite (formerly RSA Archer); deep, configurable, heavyweight.
- [logicgate](../vendors/logicgate.md) — risk-cloud / workflow-driven GRC; lighter and more modern UX.
- [auditboard](../vendors/auditboard.md) — audit-led GRC popular with internal audit and SOX teams; expanding into risk and IT compliance.
- [onspring](../vendors/onspring.md) — flexible no-code GRC platform.
- [onetrust](../vendors/onetrust.md) — privacy/GRC suite; cross-listed because it also carries an AI-governance and DSPM module.
- [vanta](../vendors/vanta.md) — compliance automation (SOC 2 / ISO) functioning as lightweight GRC for smaller/mid shops; extends into AI governance.

## Consolidation / M&A dynamics

A mature, consolidated market dominated by platform incumbents (ServiceNow, Archer,
OneTrust) with newer challengers (LogicGate, AuditBoard, Vanta) winning on UX and
time-to-value. No specific seed M&A flags for the core GRC vendors here. The live
dynamic is feature-creep: GRC suites adding AI-governance modules, pulling them into
competition with specialist [ai-governance-platform](ai-governance-platform.md) tools.

## Adjacent categories

- [ai-governance-platform](ai-governance-platform.md) — specialist AI/model-risk register; frequently a module inside, or a feed into, the GRC system of record.
- [vendor-risk](vendor-risk.md) — third-party/vendor risk is often a module of the same GRC suite.
- [risk-tiers](risk-tiers.md) — the AI-use-case risk classification that lives inside GRC.
- [promotion-gates](promotion-gates.md), [hitl-approvals](hitl-approvals.md) — sign-off workflows that GRC tools operationalize.

## Survey

**Question.** Which enterprise GRC platform does your firm use as its system of
record for risk, controls, policy, and audit (and would you extend it to cover AI
risk)?

**Answer options.** ServiceNow GRC; Archer; LogicGate; AuditBoard; Onspring;
OneTrust; Vanta; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** This is a "what do you already own" question more than an
"are you evaluating" one — most respondents will have an incumbent. The useful signal
is whether AI risk gets folded into the existing GRC tool vs a dedicated
[ai-governance-platform](ai-governance-platform.md); consider a follow-up. AuditBoard and Vanta skew to
audit/compliance-automation framing and may pull different buyer personas. OneTrust
and Vanta also appear on the [ai-governance-platform](ai-governance-platform.md) survey — expect overlap.

## Open taxonomy questions

- Boundary with [ai-governance-platform](ai-governance-platform.md): for many firms AI governance is a GRC
  module. Keep both surveys but reconcile responses.
- [vendor-risk](vendor-risk.md) is frequently a sub-module of these same suites — worth noting the
  overlap when respondents pick the same vendor twice.
