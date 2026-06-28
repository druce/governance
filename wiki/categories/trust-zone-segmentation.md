---
title: Trust Zone Segmentation
type: category
name: Trust Zone Segmentation
slug: trust-zone-segmentation
layer: policy
priority: process
trifecta_role: all
maps_to_seed_doc: Trust Zone Segmentation
maps_to_seed_csv: "—"
vendor_count: 0
status: drafted
last_updated: 2026-06-28
---

> This is a **practice**, not a product. It is the organizing idea behind the whole
> stack — the architecture you design so that no single component failure becomes a
> breach. There is no shortlist to buy; you implement it with tooling you already
> have (network controls, identity, [ephemeral-environments](ephemeral-environments.md), gateways).

## Business objective

The job is to **break the exfiltration chain** before it can form. Simon Willison's
[lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) says
an AI system becomes dangerous only when three things line up at once:

1. **Untrusted input** — the model reads attacker-controlled text (a web page, an
   email, a document, a tool result) that can carry hidden instructions.
2. **Sensitive data** — the model has access to data you care about (MNPI, PII,
   positions, client files, source code).
3. **Egress** — the model can send data somewhere it shouldn't (the open internet,
   an arbitrary API, an attacker's endpoint).

Any two of these are survivable. **All three together** means a prompt-injection
attack can read your secrets and mail them out, and no amount of prompt-level
guardrail fully closes the gap. Trust-zone segmentation is the architectural answer:
carve your AI workloads into zones where the three legs **can never co-occur**.

The seed doc's three-zone model:

- **Red zone** — agents "YOLO" on the open internet. Untrusted input + egress are
  both present, so **sensitive data must be absent**. This is where you let an agent
  browse, scrape, or call public APIs freely — because there is nothing valuable in
  the blast radius. Disposable, isolated, no path to internal systems.
- **Yellow zone** — agents reach the data warehouse and internal data, but **cannot
  reach the internet**. Sensitive data + untrusted input may be present, but egress
  is cut, so nothing can leave. This is where analysis over real data happens, behind
  a sealed perimeter with no outbound path.
- **Green zone** — agents touch internal **production** systems and can take
  consequential action. Sensitive data + egress exist, so **untrusted input must be
  excluded**: no raw web content, no unvetted documents, no arbitrary user prompts.
  Everything entering is vetted, and the agents themselves go through heavy review
  ([promotion-gates](promotion-gates.md), [hitl-approvals](hitl-approvals.md)).

The discipline is simply: **for every workload, name its zone, then prove the missing
trifecta leg is actually missing.** If you can't say which leg is removed, the
workload is ungoverned.

## When you need it

**Day 1 — you design it in.** This is not something you bolt on later; it is the
shape of the platform. The day you let any agent read untrusted content *and* touch
real data *and* call out to the network, you have already lost, and retrofitting
zones onto a sprawling deployment is painful. For a hedge-fund CTO, the cheapest
version is a whiteboard exercise before the first agent ships: decide where research
agents (red), analytics agents (yellow), and execution/OMS-adjacent agents (green)
live, and what enforces the boundary between them.

The practice scales down. A 50-person fund doesn't need three Kubernetes clusters; it
needs a clear rule that the agent allowed to browse the web is **not** the agent
allowed to read the trade blotter, and that neither can do both.

## Lethal-trifecta role

This is the **only** category that addresses all three legs at once — not by
inspecting traffic but by **architecturally guaranteeing** the three never align.
Every other control (runtime firewalls, DLP, gateways) is a mitigation *within* a
zone; segmentation is the containment that makes those mitigations survivable when
they fail. It is the meta-control the rest of the stack hangs off.

| Zone | Untrusted input | Sensitive data | Egress | Missing leg |
|---|---|---|---|---|
| Red | yes | **no** | yes | sensitive data |
| Yellow | yes | yes | **no** | egress |
| Green | **no** | yes | yes | untrusted input |

## How it gets enforced (tooling, not a shortlist)

Segmentation is a design realized through controls you already run:

- **Isolation / disposability** — [ephemeral-environments](ephemeral-environments.md) give you zone-scoped,
  short-lived compute that vanishes after use, so red-zone work leaves nothing sticky
  to compromise.
- **Egress control** — [network-security-sase](network-security-sase.md) and the [ai-gateway](ai-gateway.md) (the single
  exit door for model traffic) are how you actually cut or allowlist outbound paths
  for the yellow zone.
- **Input/output inspection within a zone** — [ai-runtime-security](ai-runtime-security.md) (the AI
  firewall) and [dlp](dlp.md) catch what slips through at the prompt/response boundary.
- **Identity & authorization** — [identity-access](identity-access.md), [authorization-engine](authorization-engine.md), and
  [mcp-gateway](mcp-gateway.md) decide which agent may enter which zone and reach which tools.
- **Retrieval scoping** — [entitlement-aware-rag](entitlement-aware-rag.md) ensures even an in-zone agent
  only retrieves what its caller was already allowed to see.

## Adjacent categories

- [overview](../overview.md) — the thesis page; trust zones and the lethal trifecta are its spine.
- [ephemeral-environments](ephemeral-environments.md) — the disposable compute that makes red/yellow isolation
  cheap and real.
- [ai-gateway](ai-gateway.md) / [network-security-sase](network-security-sase.md) — the egress chokepoints that enforce the
  yellow-zone "no internet" rule.
- [ai-runtime-security](ai-runtime-security.md) — in-zone prompt/response inspection; the mitigation layer
  segmentation backstops.
- [risk-tiers](risk-tiers.md) — sorts use cases by stakes; high-tier use cases get the strictest
  zone.
- [promotion-gates](promotion-gates.md) / [hitl-approvals](hitl-approvals.md) — the human checkpoints that gate entry to
  the green zone.

## Open taxonomy questions

- Overlaps heavily with [ephemeral-environments](ephemeral-environments.md): that page is the *product*
  category (Codespaces, Dev Boxes, Workers); this is the *design discipline* that uses
  it. Keep separate — one is "what you buy," one is "how you arrange it."
- Zone boundaries map cleanly onto [risk-tiers](risk-tiers.md); some shops may collapse the two
  into a single "tier dictates zone" policy. Worth noting in survey design even though
  this page carries no survey.
