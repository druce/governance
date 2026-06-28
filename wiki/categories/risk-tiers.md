---
type: category
name: Risk Tiers
slug: risk-tiers
layer: policy
priority: process
trifecta_role: none-detection
maps_to_seed_doc: Risk Tiers
maps_to_seed_csv: "—"
vendor_count: 0
status: drafted
last_updated: 2026-06-28
---

> A **practice**, not a product. There's nothing to buy; the tiers live as a field in
> the systems you already own — your [enterprise-grc](enterprise-grc.md) register and your
> [ai-governance-platform](ai-governance-platform.md).

## Business objective

Rate every AI system and use case **from "meh" to "oh no,"** so that scrutiny matches
the stakes. Not all AI is equal: a marketing-copy assistant and an agent that can move
money or surface MNPI should not get the same review. Risk tiers are the internal
classification that decides **how much governance each use case earns** — what review,
what monitoring, what approvals, which [trust zone](trust-zone-segmentation.md).

A workable tiering for a hedge fund usually keys on a few axes:

- **Data sensitivity** — does it touch MNPI, client PII, positions, source code?
- **Autonomy / consequence** — does it advise a human, or act on its own? Can it
  trade, send, delete, or commit?
- **Audience / exposure** — internal-only, client-facing, or regulator-facing?
- **Reversibility** — can a bad output be caught and undone, or is it irreversible?

A simple three- or four-band scheme (e.g. *minimal / limited / high / unacceptable*,
echoing the EU AI Act's risk bands) is enough. The point is that the tier is assigned
**before** build, written down, and drives everything downstream.

## When you need it

**Day 1 — it's a process, and a cheap one.** You need the tiering rubric before you
approve the first use case, because the tier is what tells you which other controls
apply. Without it, every request gets either too much friction (and shadow AI routes
around you) or too little (and the risky one ships unwatched). For a small fund, this
is a one-page rubric and a column in a spreadsheet, not a program.

It pairs with [acceptable-use-policies](acceptable-use-policies.md) (which sets the floor everyone agrees to)
and feeds [promotion-gates](promotion-gates.md) and [hitl-approvals](hitl-approvals.md) (which enforce more rigor as the
tier rises).

## Lethal-trifecta role

None directly — risk tiers don't break any leg of the trifecta. They are the
**triage layer** that decides how hard the trifecta-breaking controls get applied:
a high tier mandates the strictest [zone](trust-zone-segmentation.md), the tightest
[runtime](ai-runtime-security.md) policy, and mandatory [human
sign-off](hitl-approvals.md); a low tier rides on lightweight defaults. It governs *how much* control,
not *which* control.

## How it gets recorded (tooling, not a shortlist)

- [enterprise-grc](enterprise-grc.md) — the system of record where the tier, its rationale, and its
  owner actually live (ServiceNow GRC, Archer, AuditBoard, OneTrust, etc.). Usually
  already owned.
- [ai-governance-platform](ai-governance-platform.md) — purpose-built AI inventories that attach a risk tier to
  each model/use case and map it to NIST AI RMF / EU AI Act / SR 11-7 obligations.

## Adjacent categories

- [acceptable-use-policies](acceptable-use-policies.md) — the baseline rules; tiers add graduated scrutiny on
  top.
- [promotion-gates](promotion-gates.md) / [hitl-approvals](hitl-approvals.md) — consume the tier to decide how much
  sign-off a use case needs.
- [trust-zone-segmentation](trust-zone-segmentation.md) — the tier often dictates which zone a workload runs in.
- [ai-governance-platform](ai-governance-platform.md) / [enterprise-grc](enterprise-grc.md) — where tiers are stored and audited.

## Open taxonomy questions

- Strong overlap with [ai-governance-platform](ai-governance-platform.md): tiering is a *practice*, that page is
  the *tooling* that operationalizes it. Keep distinct.
- Tier definitions may eventually want to align 1:1 with EU AI Act bands for regulated
  shops — a naming decision to revisit after research, not now.
