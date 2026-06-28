---
type: category
name: Authorization Engine (Agent / Tool)
slug: authorization-engine
layer: model-prompt
priority: day-2
trifecta_role: sensitive-data, egress (constrains what an agent action is allowed to do; not inline content inspection)
maps_to_seed_doc: Authorization Engine (Agent / Tool)
maps_to_seed_csv: MCP / Agent Gateway & Tool Access (split)
vendor_count: 6
status: drafted
last_updated: 2026-06-28
---

# Authorization Engine (Agent / Tool)

## Business objective

An authorization engine is the **externalized rules engine that answers one question** —
"is this principal allowed to do *this* action on *this* resource, right now?" — and
returns allow/deny in milliseconds. Instead of scattering `if user.role == ...` checks
through application code, you ship policy to a dedicated decision point (PDP) that every
app and agent calls. For agentic AI the principal is increasingly an *agent*, and the
question becomes "is this agent permitted to call this tool / read this record / take
this action on behalf of this user?"

This is plumbing, not an AI product per se — the same engines that do fine-grained authz
for microservices now get pointed at agent and tool calls. The value is **consistency
and auditability**: one place where access decisions are made, logged, and changed.

## When you need it

Day-2 — relevant **when agents start to *act*** rather than just chat, and especially when
agents act *on behalf of different users* with different entitlements. A fund with a
single read-only assistant can lean on the underlying app's permissions. The trigger to
adopt an externalized engine is **fine-grained, per-action, identity-aware decisions** at
scale — e.g. an agent that can touch many systems and must respect each user's existing
access. Teams already doing [[policy-as-code]] often already own one of these (OPA), so
it may be a re-use rather than a new buy.

## Lethal-trifecta role

An authorization engine constrains the **sensitive-data** and **egress** legs: it can
deny the read of sensitive data or the action that would move it, per request. It does
*not* inspect prompt content for injection (that's [[ai-runtime-security]] /
[[agent-runtime-security]]) — it enforces *whether the action is permitted at all*. It is
a building block of [[trust-zone-segmentation]] and entitlement-aware designs: the
mechanism that makes "this agent may not reach the Internet / this record" actually
enforceable. Lives wherever decisions are made — typically yellow/green zones.

## Vendors

**Open-source policy engines**
- [[open-policy-agent]] — CNCF policy engine (Rego); the de-facto OSS standard PDP, general-purpose and widely embedded.
- [[cerbos]] — open-source, stateless authorization with human-readable policies; positions for app and agent/tool authz. Cross-listed to [[mcp-gateway]].

**Commercial / managed policy platforms**
- [[styra]] — commercial company behind OPA; enterprise management, distribution, and tooling for Rego policy at scale. Cross-listed to [[policy-as-code]].
- [[permit-io]] — developer-first authorization-as-a-service (wraps OPA/Cedar); SDKs and a hosted PDP, pitching agent/MCP authz. Cross-listed to [[mcp-gateway]].
- [[oso]] — authorization-as-a-service / library (Polar language) for application and agent permissions.

**Relationship-based (ReBAC / Zanzibar-style)**
- [[authzed]] — AuthZed / SpiceDB, a Google-Zanzibar-style relationship-based permissions database for fine-grained, relationship-driven access.

## Consolidation / M&A dynamics

No seed M&A flags, but research surfaced one **major event**: in **Aug 2025 Apple acqui-hired
the core OPA maintainers and several engineers from [[styra]]** (the commercial OPA company).
It was a **team acqui-hire, not a clean corporate acquisition** — [[open-policy-agent]] itself
stays under CNCF (governance/license/cadence unchanged), but Styra's commercial products (DAS,
Enterprise OPA) face an uncertain roadmap. Net effect: buyers standing up authz today should
default to OPA directly or a managed alternative ([[permit-io]], [[cerbos]] Cloud, [[oso]]);
existing Styra DAS customers have a vendor-risk/migration question. Otherwise the category is
independent OSS projects and venture-backed startups (Cerbos, Permit.io, AuthZed, Oso all
independent; AuthZed Series A $12M/2024, Permit.io Series A $8M/2024). The dynamic to watch is
**adjacency capture**: MCP-gateway and tool-identity vendors bundle authz as a feature, and
these engines are repositioning from "microservice authz" to **"agent authz"** to ride the
agentic wave — [[oso]] went furthest, launching "Oso for Agents" (2025) that extends into
[[agent-runtime-security]].

## Adjacent categories

- [[mcp-gateway]] — the enforcement *chokepoint* for tool calls; an MCP gateway often *calls* an authorization engine for the allow/deny decision. Cerbos and Permit.io straddle both.
- [[policy-as-code]] — same engines (OPA, Styra) applied to infra/CI policy rather than per-request agent actions; large overlap.
- [[agent-runtime-security]] — watches agent *behaviour*; authz decides *permission*. Complementary.
- [[tool-identity-integration]] — establishes *who the agent is* to a tool; authz decides *what that identity may do*.
- [[non-human-identity]] — issues agent/workload identities that authz policies are written against.

## Survey

**Question.** Which authorization / policy engines is your organization using or
evaluating to make fine-grained access decisions for agents and tools? *(Select all that
apply and indicate stage.)*

**Answer options.** Open Policy Agent (OPA) · Cerbos · Styra · Permit.io · Oso ·
AuthZed (SpiceDB) · Other (Please Specify)

**Response scale.** multi-select; Interested; Considering/evaluating; Pilot/implementing;
In production; Would recommend; Would not recommend.

**Notes for survey design.**
- **Table-stakes / most-deployed:** OPA (likely already in production for non-AI authz — responses may reflect existing infra, not new agent use). **Niche:** AuthZed, Oso.
- **OPA vs Styra confusion:** Styra is the commercial OPA company; some respondents will pick one meaning the other. Consider pairing them ("OPA / Styra") as the CSV did, or a clarifying note. **M&A dates this option:** Apple acqui-hired Styra's OPA team (Aug 2025) and its commercial products are in limbo — a "Styra" response in 2026 likely means legacy DAS usage, not net-new adoption.
- This question overlaps [[policy-as-code]] and [[mcp-gateway]] survey items (same vendors appear). If you ask all three, scope each clearly ("agent/tool *authorization decisions*" here) to avoid respondents answering the same thing three times.

## Open taxonomy questions

- **This is one of three rows the CSV bundled into a single survey question** — "MCP / Agent Gateway & Tool Access" — which we split into [[authorization-engine]] (decide if an action is allowed), [[mcp-gateway]] (the doorway that brokers tool calls), and [[tool-identity-integration]] (give agents managed identity/connectors to tools). See Q1 in taxonomy-gaps.md: we **keep all three granular** because they are genuinely different jobs, but products routinely cover two of them, so vendor overlap is expected and noted on each page.
- **Overlap to watch:** Cerbos and Permit.io appear here *and* under [[mcp-gateway]]; Pomerium (primary in mcp-gateway) is an identity-aware proxy that also does authz. The clean line is **engine (makes the decision) vs gateway (enforces it at the network/tool boundary)** — but bundles blur it.
- Heavy overlap with [[policy-as-code]] (OPA, Styra live in both). Whether agent authorization deserves its own category separate from general policy-as-code is a candidate to revisit after research; kept separate because the *agent/tool* framing is what the survey is probing.
