---
title: Ephemeral Environments
type: category
name: Ephemeral Environments
slug: ephemeral-environments
category: ephemeral-environments
layer: governance
survey_question: null
adoption_tier: practice
trigger: underpins trust-zone design — disposable compute for risky AI work
maturity_stage_required: null
category_maturity: null
adjacent: [trust-zone-segmentation, promotion-gates]
incumbent_coverage: []
vendor_count: 8
maps_to_seed_doc: Ephemeral Environments
maps_to_seed_csv: —
last_verified: 2026-06-28
---

## Business objective

Disposable, build-to-order workspaces that vanish when you are done — nothing sticky to
compromise. Ephemeral environments provide **zone-scoped, reproducible, short-lived
compute**: a dev box, sandbox, or runtime that is spun up from declarative config,
scoped to exactly one trust zone, used for a task, and then destroyed. The security
value is that there is no long-lived, drifted, credential-laden machine sitting around
for an attacker (or a runaway agent) to find and pivot from. For agentic AI workloads,
this is the practical substrate of [trust-zone-segmentation](trust-zone-segmentation.md): an agent runs in a
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

## Security role

**Preventive isolation: constrains outbound data flows and data reach per zone.**
Ephemeral environments are how trust zones are physically realized: a red-zone agent
gets internet but no internal data; a yellow-zone agent gets data-warehouse access
but no internet to exfiltrate to. Because the environment is short-lived and rebuilt
from config, there is no accumulated sensitive state to leak. It underpins
[trust-zone-segmentation](trust-zone-segmentation.md) directly and spans the
red and yellow zones by design.

## Vendors

These are general-purpose compute/dev-environment platforms used *for* zone-scoped
ephemeral workloads, not AI-security products per se:

- [github-codespaces](../vendors/github-codespaces.md) — on-demand, container-based cloud dev environments defined in-repo.
- [azure-dev-boxes](../vendors/azure-dev-boxes.md) — managed, policy-governed cloud developer workstations on Azure.
- [terraform-cloud](../vendors/terraform-cloud.md) — declarative infrastructure provisioning/teardown; cross-listed with [policy-as-code](policy-as-code.md) (Sentinel) for governing what gets built.
- [cloudflare-workers](../vendors/cloudflare-workers.md) — edge serverless compute; short-lived, isolated execution for sandboxed/red-zone tasks.

**Agent code sandboxes** (added 2026-10-16). A different product from the four above: those give a *human* a disposable workstation; these give an *agent* a disposable, API-created box per task in which to run code nobody has reviewed. The buying questions are isolation strength (container vs gVisor vs microVM), default egress, and whether the sandbox can run in your own cloud.

- [modal](../vendors/modal.md) — serverless AI compute whose Sandboxes run untrusted agent-generated code on gVisor or a per-sandbox VM runtime; hosted only; outbound network open by default. $750M Series D at $15.75B (2026-10-14).
- [daytona](../vendors/daytona.md) — API-driven, sub-second, stateful agent sandboxes (Sysbox-hardened containers, not microVMs); pivoted from human dev environments in 2025; open-source repo archived, BYOC is Enterprise-only.
- [docker-sandboxes](../vendors/docker-sandboxes.md) — Docker Sandboxes (`sbx`) runs off-the-shelf coding agents (Claude Code, Codex, Copilot, Gemini CLI…) in local per-session microVMs with their own kernel, a host-side egress proxy (deny by default) and placeholder-credential injection; the paid Docker AI Governance add-on gives central policy and audit. Proprietary CLI, free locally. (added 2026-10-20)
- [nvidia-openshell](../vendors/nvidia-openshell.md) — NVIDIA's open-source, self-hosted sandbox runtime for long-running agents (Docker/Podman/Kubernetes; microVM driver in prerelease); provides policy and containment, not compute. Primary is [agent-runtime-security](agent-runtime-security.md). (added 2026-10-20)
- **Also in this space, no pages:** E2B (Firecracker microVM sandboxes), and the browser-agent sandboxes Browserbase and Anchor Browser — hosted headless browsers in which an agent can be confined.

## Consolidation / M&A dynamics

Not an AI-security M&A market — these are platform offerings from major cloud/dev
incumbents (Microsoft/GitHub, Azure, HashiCorp/IBM, Cloudflare). The HashiCorp →
IBM acquisition (per seed flags elsewhere; unverified — to confirm in research) is the
only relevant ownership note, affecting Terraform Cloud's stewardship. The trend to
watch is platforms adding agent-sandbox primitives (isolated, ephemeral runtimes
purpose-built for AI agents executing code).

## Adjacent categories

- [trust-zone-segmentation](trust-zone-segmentation.md) — the design pattern ephemeral environments physically enforce.
- [policy-as-code](policy-as-code.md) — governs *what* may be provisioned and how zones are configured (Terraform Cloud / Sentinel).
- [agent-runtime-security](agent-runtime-security.md) — runtime protection for the agents that run inside these environments.
- [mcp-gateway](mcp-gateway.md) — controls the tools/egress an agent in a zone is allowed to reach.

## Survey

**Question.** Which platforms does your firm use to provide ephemeral, zone-scoped
compute for developers or AI/agentic workloads?

**Answer options.** GitHub Codespaces; Azure Dev Boxes; Terraform Cloud; Cloudflare
Workers; Modal Sandboxes; Daytona; Other (Please Specify).

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
  [trust-zone-segmentation](trust-zone-segmentation.md) than as a vendor shortlist. Keep as-is for now.
- Overlap with [policy-as-code](policy-as-code.md) via Terraform Cloud / Sentinel; cross-listed.
