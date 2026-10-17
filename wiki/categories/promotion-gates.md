---
title: Promotion Gates
type: category
name: Promotion Gates
slug: promotion-gates
category: promotion-gates
layer: policy
survey_question: null
adoption_tier: practice
trigger: CI/CD sign-off between experiment and production
maturity_stage_required: null
category_maturity: null
adjacent: [risk-tiers, policy-as-code, software-supply-chain]
incumbent_coverage: []
vendor_count: 1
maps_to_seed_doc: Promotion Gates
maps_to_seed_csv: —
last_verified: 2026-06-28
---

> A **practice**, not a product. You implement it with the CI/CD, change-management,
> and ticketing tooling you already run — there's no shortlist to buy.

## Business objective

Put **checkpoints between "fun experiment" and "live in production,"** so somebody has
to sign off before an AI app or agent crosses the line. A promotion gate is the
controlled path that a use case walks from sandbox → staging → production, with a
defined approval (and the evidence to support it) at each step.

In practice a gate bundles a few things to check before promotion:

- the use case has a [risk tier](risk-tiers.md) assigned and its tier-appropriate
  controls are in place;
- evals / red-team results meet a bar ([llm-observability](llm-observability.md), [ai-red-teaming](ai-red-teaming.md));
- the workload is in the right [trust zone](trust-zone-segmentation.md) with egress and
  data access scoped;
- logging, archival, and rollback exist before it goes live;
- a named owner accepts the residual risk.

The deliberate design goal is **lightweight**: a gate that's too heavy gets bypassed,
and shadow AI is the result. The seed framing is "keep it lightweight" — a gate is a
tripwire and a sign-off, not a six-week committee.

## When you need it

**Day 1 — process, kept light.** You want the gate the day anything moves toward
production, because uncontrolled promotion is how a weekend prototype ends up making
client-facing decisions on Monday. For a small fund, this can be as simple as: nothing
reaches production without a PR review plus a one-line sign-off from a designated owner
against a short checklist. Heavier, tier-driven gates come as the estate grows.

Gates are the *automated/procedural* counterpart to [hitl-approvals](hitl-approvals.md): promotion
gates govern **releasing the system**; HITL approvals govern **individual high-stakes
actions** the system then takes at runtime.

## Security role

None directly at runtime — a gate screens no input and blocks no exfiltration
itself. Instead it **verifies that the controls which do are present and
configured** before a workload goes live: the enforcement moment where risk-tier
requirements and zone placement get checked, and the quality gate that stops a
misconfigured workload — one exposed to untrusted input with sensitive-data access
and an open outbound path — from shipping.

## How it gets enforced (tooling, not a shortlist)

- **CI/CD + change management** — branch protection, required reviewers, deployment
  approvals in GitHub/GitLab and your release pipeline. This is where the gate
  actually lives.
- [policy-as-code](policy-as-code.md) — encode promotion rules as software (OPA, Sentinel, Kyverno) so
  the gate enforces itself instead of relying on a human remembering the checklist.
- [enterprise-grc](enterprise-grc.md) — the change/approval record and audit trail (ServiceNow and
  peers, usually already owned).
- [llm-observability](llm-observability.md) / [ai-red-teaming](ai-red-teaming.md) — supply the eval and red-team evidence a
  gate checks against.
- **Code-quality gates on AI-written code** — [sonar](../vendors/sonar.md) (SonarQube quality gates, with an
  "AI Code Assurance" label that applies a stricter gate to AI-generated code) is the
  established example; AI code reviewers such as Greptile and Qodo (no pages) sit at
  the same pull-request checkpoint. (added 2026-10-16)
- **Feature flags and kill switches** — e.g. LaunchDarkly AI Configs (no page): ship the
  model/prompt change dark, ramp it, and turn it off without a redeploy. The runtime half
  of a gate. (added 2026-10-16)

## Adjacent categories

- [hitl-approvals](hitl-approvals.md) — runtime human sign-off on actions, vs. release-time sign-off on
  the system. Easy to conflate; keep distinct.
- [risk-tiers](risk-tiers.md) — sets how strict the gate is for a given use case.
- [policy-as-code](policy-as-code.md) — automates the gate.
- [ai-governance-platform](ai-governance-platform.md) / [enterprise-grc](enterprise-grc.md) — where approvals and evidence are
  recorded for audit.

## Open taxonomy questions

- Boundary with [hitl-approvals](hitl-approvals.md) is the main source of confusion: "gate" (promote the
  system) vs. "approval" (authorize an action). Worth an explicit note wherever both
  appear so survey respondents don't blur them.
