---
type: category
name: HITL Approvals
slug: hitl-approvals
layer: policy
priority: process
trifecta_role: none-detection
maps_to_seed_doc: HITL Approvals
maps_to_seed_csv: "—"
vendor_count: 0
status: drafted
last_updated: 2026-06-28
---

> A **practice**, not a product. Human-in-the-loop approvals are a workflow you wire
> into your agents using approval tooling you already run (ServiceNow, custom workflow
> engines, the agent framework's own interrupt/approval hooks).

## Business objective

**A human has to press "yes" before the AI does something consequential.** HITL
(human-in-the-loop) approvals insert a person into the agent's action path at the
moments that matter — moving money, sending an external message, deleting data,
committing code to production, placing or amending an order. The agent proposes; a
human disposes.

The design question is **which actions earn a human gate**, and the answer comes from
[[risk-tiers]]: low-stakes, reversible actions run autonomously; high-stakes or
irreversible ones pause for sign-off. Over-gating trains people to rubber-stamp (and
defeats the point); under-gating lets an agent take an irreversible wrong action at
machine speed. The craft is putting the checkpoint only where consequence is real.

Good HITL also captures **what** is being approved and **why**, so the approval is an
auditable record, not a reflexive click.

## When you need it

**Day 2 — when agents take consequential actions.** A read-only research or
analytics assistant doesn't need it. The moment an agent can *act* on the world —
especially anything touching the OMS, payments, client comms, or production — you need
a human gate on the high-stakes subset. For a hedge fund, the trigger is the shift
from "AI that drafts" to "AI that does," and that line should be drawn explicitly
before the agent is allowed to act.

It complements [[promotion-gates]]: promotion gates approve **shipping the system**
once; HITL approvals approve **specific actions** the live system proposes, again and
again, at runtime.

## Lethal-trifecta role

None directly — HITL doesn't remove a trifecta leg. It is the **last-resort
containment** for the green zone, where sensitive data and egress both exist: when an
agent that *can* act proposes something harmful (whether from a prompt injection that
slipped through or its own error), a human is the circuit-breaker between proposal and
irreversible effect. It backstops the automated controls rather than replacing them.

## How it gets enforced (tooling, not a shortlist)

- **Workflow / approval engines** — ServiceNow approvals, custom workflow engines, or
  the interrupt/approval primitives built into agent frameworks (the agent pauses and
  requests sign-off before a designated tool call).
- [[authorization-engine]] — externalized authz ("is this agent allowed to do this,
  right now?") that can require a human approval as a condition of allowing an action.
- [[mcp-gateway]] — brokers the tools an agent can call and is a natural place to
  interpose an approval before a sensitive tool runs.
- [[enterprise-grc]] — records the approval and its rationale for audit.

## Adjacent categories

- [[promotion-gates]] — release-time sign-off on the system vs. runtime sign-off on an
  action. The two are easy to conflate; keep distinct.
- [[risk-tiers]] — decides which actions are consequential enough to gate.
- [[authorization-engine]] / [[mcp-gateway]] — the runtime chokepoints where an
  approval requirement is actually enforced.
- [[trust-zone-segmentation]] — HITL is the human checkpoint guarding entry to
  green-zone (production-acting) workloads.

## Open taxonomy questions

- Primary confusion is with [[promotion-gates]] (system vs. action). Flag the
  distinction wherever both appear.
- Some agent platforms ship native HITL hooks; as that matures this practice may grow a
  thin tooling shortlist. For now it stays pure-process.
