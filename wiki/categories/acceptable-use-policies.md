---
title: Acceptable Use Policies
type: category
name: Acceptable Use Policies
slug: acceptable-use-policies
layer: policy
priority: process
trifecta_role: none-detection
maps_to_seed_doc: Acceptable Use Policies
maps_to_seed_csv: "—"
vendor_count: 0
status: drafted
last_updated: 2026-06-28
---

> A **practice**, not a product — an internal policy framework. There's nothing to
> buy; it's a document, the training around it, and the attestation that people read
> it.

## Business objective

The **"here's what you can and can't do with AI here" rulebook everyone signs.** An
acceptable-use policy (AUP) sets the organization's baseline standards for AI: which
tools are sanctioned, what data may and may not go into them, what's flat-out
prohibited (e.g. pasting MNPI or client PII into a public chatbot), who to ask when
unsure, and the consequences for ignoring it.

A useful AI AUP for a fund typically covers:

- **Sanctioned vs. prohibited tools** — what's approved, and that everything else
  routes through the [ai-gateway](ai-gateway.md) or gets reviewed first.
- **Data handling** — what classes of data are forbidden in AI tools, tied to your
  [data classification](dspm.md) labels (MNPI, client-confidential, legal-privileged,
  PII).
- **Disclosure & review** — when AI output must be checked by a human before it's
  used or sent, and when AI involvement must be disclosed.
- **Acknowledgement** — everyone reads and attests, so it's enforceable and auditable.

The seed calls it **"the cheapest control there is,"** and that's exactly right: it
costs a document and an attestation, and it's the precondition that makes every
technical control defensible (you can't enforce a rule nobody was told).

## When you need it

**Day 1 — the cheapest control there is.** This is the first thing you write, before
any tooling. Employees are already using AI (sanctioned or not), so the policy is what
turns "we never said you could" into an enforceable standard. For a small fund it's a
one-to-two-page document plus a sign-off; it grows teeth as you add the technical
controls ([ai-access-governance](ai-access-governance.md), [dlp](dlp.md)) that detect and enforce what the policy
declares.

## Lethal-trifecta role

None directly — a policy doesn't break a trifecta leg. It's the **human-layer
baseline** that sets expectations and reduces the easy, accidental leaks (someone
pasting positions into a consumer chatbot) that no firewall should have to catch in
the first place. Think of it as the floor; the technical controls are the net under
the people who ignore the floor.

## How it gets backed by tooling (not a shortlist)

A policy is only as good as the controls that observe and enforce it:

- [ai-access-governance](ai-access-governance.md) — discovers shadow AI and enforces inline policy on what
  data flows to which model; turns the AUP from words into enforcement.
- [dlp](dlp.md) — stops sanctioned-data classes from leaving via prompts, backing the
  data-handling clauses.
- [dspm](dspm.md) — the data classification the AUP's "don't put X in AI" rules reference.
- [enterprise-grc](enterprise-grc.md) — where the policy, its versions, and attestations are recorded
  and audited.

## Adjacent categories

- [risk-tiers](risk-tiers.md) — the AUP is the floor everyone agrees to; tiers add graduated
  scrutiny above it.
- [ai-access-governance](ai-access-governance.md) / [dlp](dlp.md) — the detective/preventive controls that enforce
  the policy.
- [enterprise-grc](enterprise-grc.md) — system of record for the policy and sign-offs.
- [ai-governance-platform](ai-governance-platform.md) — maps the policy to external frameworks (NIST AI RMF,
  EU AI Act, SR 11-7) for regulators.

## Open taxonomy questions

- The AUP overlaps every other process page (it references tiers, gates, and zones).
  It's the umbrella document; the others are specific mechanisms. Keep separate so the
  "what you write" vs. "what you do" distinction stays clear.
