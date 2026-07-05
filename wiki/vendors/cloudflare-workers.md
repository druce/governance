---
title: Cloudflare Workers
type: vendor
name: Cloudflare Workers
slug: cloudflare-workers
aka: [Workers, Cloudflare Workers AI]
primary_category: ephemeral-environments
also_listed_in: []
website: https://workers.cloudflare.com/
founded: 2017
hq: San Francisco, CA, USA
ownership_state: public
owner: Cloudflare
ownership_note: 'Product of Cloudflare, Inc. (public, NYSE: NET); Workers launched 2017'
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: null
deployment_model: [saas]
form_factor: []
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-06-28
verify_after: null
tags: [first-party, serverless, edge-compute, cloudflare]
---

# Cloudflare Workers

**One-liner** — Cloudflare's serverless edge-compute platform that runs code in lightweight V8 isolates, used to execute small, sandboxed, ephemeral workloads (including AI/agent tool calls and proxies) close to users without managing servers.

**What it does** — Workers runs functions in V8 isolates (not full containers/VMs) at Cloudflare's edge, with sub-millisecond cold starts and per-request isolation. The broader platform adds Workers AI (inference), AI Gateway, Durable Objects, KV/R2 storage, and a sandboxed code-execution offering for agents. For this wiki it appears as an **ephemeral-environments** primitive: a place to run untrusted or agent-generated code in a strongly isolated, short-lived sandbox with controllable egress.

**Where it sits in the stack** — [ephemeral-environments](../categories/ephemeral-environments.md), governance layer; overlaps Cloudflare's network/SASE and AI-gateway lines (see [cloudflare](cloudflare.md)). Lethal-trifecta role: isolates **untrusted-input** execution and is a natural **egress** chokepoint (all outbound traffic flows through Cloudflare's network). Enabler of [trust-zone-segmentation](../categories/trust-zone-segmentation.md).

**Deployment & architecture** — SaaS / serverless; deploy via Wrangler CLI or API. V8-isolate sandboxing (lighter and more locked-down than containers, but with runtime constraints). Integrates with Cloudflare's WAF, Zero Trust/SASE, AI Gateway, and storage.

**Positioning & differentiators** — Isolate-based model gives very fast, very cheap, strongly-bounded sandboxes — contrast [github-codespaces](github-codespaces.md) / [azure-dev-boxes](azure-dev-boxes.md) which are full dev environments, not a production execution runtime. Different *purpose*: Workers is where agent/tool code runs in production; Codespaces/Dev Box are where developers work.

**Ownership, funding & M&A** — Product of Cloudflare, Inc. (public, NYSE: NET). Seed flag "(Cloudflare)" confirmed; no separate M&A. Confidence: high. See parent page [cloudflare](cloudflare.md).

**CTO / hedge-fund lens** — Day-2 infrastructure. Relevant if you want agent tool execution or lightweight AI proxies running in isolated, egress-controlled sandboxes rather than on broadly-permissioned servers. Strong fit if Cloudflare is already your edge/Zero Trust provider; otherwise a build-vs-buy call against your existing serverless stack.

**Competitors / alternatives** — [github-codespaces](github-codespaces.md), [azure-dev-boxes](azure-dev-boxes.md) (dev-side), AWS Lambda / Fargate, Vercel, Deno Deploy (not in registry). Parent: [cloudflare](cloudflare.md).

**Open questions / to verify** — Isolation guarantees of the agent code-sandbox offering for genuinely hostile code.

## Sources
- [Cloudflare Workers](https://workers.cloudflare.com/) — fetched 2026-06-28 — supports: product description, Cloudflare ownership; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); confirmed Cloudflare (NYSE: NET) ownership → public, high. Positioned as ephemeral/serverless sandbox + egress chokepoint; cross-linked parent [cloudflare](cloudflare.md).
