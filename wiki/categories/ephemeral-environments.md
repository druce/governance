---
type: category
name: Ephemeral Environments
slug: ephemeral-environments
layer: governance
priority: day-2
trifecta_role: egress
maps_to_seed_doc: Ephemeral Environments
maps_to_seed_csv: —
vendor_count: 4
status: drafted
last_updated: 2026-06-28
---

## Business objective

Disposable, build-to-order workspaces that vanish when you are done — nothing sticky to
compromise. Ephemeral environments provide **zone-scoped, reproducible, short-lived
compute**: a dev box, sandbox, or runtime that is spun up from declarative config,
scoped to exactly one trust zone, used for a task, and then destroyed. The security
value is that there is no long-lived, drifted, credential-laden machine sitting around
for an attacker (or a runaway agent) to find and pivot from. For agentic AI workloads,
this is the practical substrate of [[trust-zone-segmentation]]: an agent runs in a
fresh, network-constrained sandbox with only the access its zone permits.

## When you need it

**Day-2 — for dev and agentic workloads.** A hedge fund does not need ephemeral compute
to run an enterprise chatbot. It becomes relevant when the firm starts (a) letting
developers or quants use AI coding agents at scale, or (b) running autonomous/agentic
workloads that execute code or call tools. At that point, giving each agent or dev task
a disposable, zone-scoped environment is how you stop a compromised or prompt-injected
agent from establishing persistence or reaching across zones. For a CTO, this is the
infrastructure that makes the red/yellow/green zone design enforceable rather than
aspirational — you adopt it alongside, not before, agentic AI.

## Lethal-trifecta role

**Egress / isolation (and sensitive-data containment).** Ephemeral environments are how
trust zones are physically realized, and the trifecta is broken by **constraining
network egress and data reach per zone**: a red-zone agent gets internet but no internal
data; a yellow-zone agent gets data-warehouse access but no internet to exfiltrate to.
Because the environment is short-lived and rebuilt from config, there is no accumulated
sensitive state to leak. It underpins [[trust-zone-segmentation]] directly and spans the
red and yellow zones by design.

## Vendors

These are general-purpose compute/dev-environment platforms used *for* zone-scoped
ephemeral workloads, not AI-security products per se:

- [[github-codespaces]] — on-demand, container-based cloud dev environments defined in-repo.
- [[azure-dev-boxes]] — managed, policy-governed cloud developer workstations on Azure.
- [[terraform-cloud]] — declarative infrastructure provisioning/teardown; cross-listed with [[policy-as-code]] (Sentinel) for governing what gets built.
- [[cloudflare-workers]] — edge serverless compute; short-lived, isolated execution for sandboxed/red-zone tasks.

## Consolidation / M&A dynamics

Not an AI-security M&A market — these are platform offerings from major cloud/dev
incumbents (Microsoft/GitHub, Azure, HashiCorp/IBM, Cloudflare). The HashiCorp →
IBM acquisition (per seed flags elsewhere; unverified — to confirm in research) is the
only relevant ownership note, affecting Terraform Cloud's stewardship. The trend to
watch is platforms adding agent-sandbox primitives (isolated, ephemeral runtimes
purpose-built for AI agents executing code).

## Adjacent categories

- [[trust-zone-segmentation]] — the design pattern ephemeral environments physically enforce.
- [[policy-as-code]] — governs *what* may be provisioned and how zones are configured (Terraform Cloud / Sentinel).
- [[agent-runtime-security]] — runtime protection for the agents that run inside these environments.
- [[mcp-gateway]] — controls the tools/egress an agent in a zone is allowed to reach.

## Survey

**Question.** Which platforms does your firm use to provide ephemeral, zone-scoped
compute for developers or AI/agentic workloads?

**Answer options.** GitHub Codespaces; Azure Dev Boxes; Terraform Cloud; Cloudflare
Workers; Other (Please Specify).

**Response scale.** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design.** This is a niche/Day-2 question and will only resonate with
firms running AI coding agents or agentic workloads — consider gating on that.
Respondents will likely pick whatever matches their existing cloud (GitHub/Azure shops
pick Codespaces/Dev Boxes by default), so selections reflect incumbency more than a
deliberate security choice. The more meaningful signal may be a follow-up: "do you scope
AI/agent workloads into short-lived, network-constrained environments?" rather than the
specific product.

## Open taxonomy questions

- This category is doc-only (no CSV question) and product selection is largely
  determined by incumbency — it may read better as a practice note under
  [[trust-zone-segmentation]] than as a vendor shortlist. Keep as-is for now.
- Overlap with [[policy-as-code]] via Terraform Cloud / Sentinel; cross-listed.
