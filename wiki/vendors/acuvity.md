---
title: Acuvity
type: vendor
name: Acuvity
slug: acuvity
aka: [RYNO, Proofpoint AI Security]
primary_category: ai-access-governance
also_listed_in: [agent-runtime-security]
website: https://www.proofpoint.com/us/platform/ai-security
founded: null
hq: Sunnyvale, California, USA
ownership_state: acquired-closed
owner: Proofpoint
ownership_note: Acquired by Proofpoint — announced as completed 2026-02-12; terms undisclosed. (Proofpoint is itself Thoma Bravo-owned; this is its second data/AI-security buy after Normalyze.) Brand retired — acuvity.ai 301-redirects to Proofpoint's AI Security platform page; capability sold as AI Access Security / Agentic AI Security / AI MCP Security.
acquisition: {announced: 2026-02-12, closed: 2026-02-12, price: null}
funding_total: $9M seed (pre-acquisition)
last_funding: $9M seed led by Foundation Capital, announced at stealth exit 2024-09
market_position: null
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: unverified
integrations: []
mcp_support: gateway
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [acquired, shadow-ai, mcp-security, agentic-workspace, proofpoint, thoma-bravo]
sources:
  - {claim: "Acuvity brand retired; acuvity.ai 301-redirects to proofpoint.com/us/platform/ai-security; page is entirely Proofpoint-branded with no Acuvity/RYNO mention", url: "https://www.proofpoint.com/us/platform/ai-security", date: 2026-07-27, confidence: high}
  - {claim: "Acuvity capability now sold as three SKUs — AI Access Security, Agentic AI Security, AI MCP Security; MCP support is gateway-style inline enforcement plus discovery and transaction forensics", url: "https://www.proofpoint.com/us/products/ai-mcp-security", date: 2026-07-27, confidence: high}
  - {claim: "Acquisition announced as completed 2026-02-12; terms undisclosed", url: "https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-acquires-acuvity-deliver-ai-security-and-governance-across", date: 2026-07-13, confidence: high}
---

# Acuvity

> **Researched 2026-07-13; brand-status re-verified 2026-07-27.** Primary category: [ai-access-governance](../categories/ai-access-governance.md). **Acquired by Proofpoint** — announced as completed 2026-02-12. **Brand retired**: acuvity.ai now 301-redirects to Proofpoint's AI Security platform page. Shop for this as **Proofpoint AI Security**, not Acuvity.

**One-liner** — An AI security and governance startup (RYNO platform) covering the full span of enterprise AI usage — shadow-AI visibility from endpoints and browsers through to runtime enforcement on agents and MCP servers — now shipped as Proofpoint's **AI Security** product line.

## What it does
Acuvity's RYNO platform gave security teams visibility and enforcement across "the full range of AI usage in the enterprise": employee GenAI use discovered at endpoints and browsers (including locally installed tools like Ollama), plus runtime inspection and governance of autonomous agents and **MCP servers**. That dual scope — workforce shadow-AI governance *and* agent/MCP runtime security in one product — is what distinguished it from single-lane peers and what Proofpoint bought it for.

As of 2026-07-27 that capability is sold as three Proofpoint SKUs under the AI Security platform:

- **AI Access Security** — discovery/inventory of AI apps (first-party, third-party, embedded) and AI agents; runtime observability; runtime inspection and enforcement with 18 built-in detectors; forensic audit trails; SIEM/SOAR routing.
- **Agentic AI Security** — governance of autonomous agent behavior.
- **AI MCP Security** — MCP server discovery and risk classification (missing auth/encryption, unsanctioned remote hosts, local servers on employee machines), **gateway-style inline enforcement** (identity, permissions, content inspection before a request reaches the server), transaction forensics across user → app → LLM → server, and a "trusted MCP server registry" of 800-plus pre-vetted open-source servers.

## Naming / provenance
Page kept at slug `acuvity` (the acquired company) rather than folded into the [proofpoint](proofpoint.md) page the way Normalyze was: the Acuvity technology did not land as one shopping unit but was split across three Proofpoint SKUs, so no single product slug fits. Unlike Normalyze, Proofpoint published **no "Acuvity is now Proofpoint" transition page** (that URL 404s) — the redirect goes straight to the platform page and the Acuvity/RYNO names appear nowhere in Proofpoint's product content.

## Where it sits in the stack
Primary [ai-access-governance](../categories/ai-access-governance.md) (the workforce AI-usage governance job — the natural fit with Proofpoint's human-centric security portfolio), cross-listed in [agent-runtime-security](../categories/agent-runtime-security.md) for the agent/MCP runtime side. Layer: model-prompt. Post-acquisition, Proofpoint positions the combination as "the first unified platform to comprehensively secure every dimension of the agentic workspace" — collaboration security, data security/governance, and AI security together.

## Deployment & architecture
Platform with endpoint/browser-level visibility and runtime enforcement points for agents and MCP traffic; SaaS delivery assumed but not confirmed (open question). The MCP piece is an inline **gateway** (requests are brokered and inspected before reaching the server), not passive monitoring — confirmed on Proofpoint's AI MCP Security page 2026-07-27. Emerged from stealth 2024-09; ran as a lean ~24-person team pre-acquisition.

## Positioning & differentiators
- **Breadth across the AI usage surface** — one platform from employee chat use to local AI tools to agent/MCP infrastructure, where most shadow-AI peers stop at the browser/network.
- **MCP-era coverage** — early mover on securing MCP servers and agent tool calls, the same forward-looking angle F5 cites for [surepath-ai](surepath-ai.md). Under Proofpoint this has hardened into a named SKU with a gateway and a vetted-server registry.
- **Data-context pitch** — Proofpoint's differentiation claim is now "intent-aware" AI security: AI runtime controls joined to its data security estate ([proofpoint](proofpoint.md) + Proofpoint DLP). That is a platform argument, not an Acuvity one — treat it as vendor marketing until you see the integration.
- **No longer a standalone tool** — like [proofpoint](proofpoint.md) before it, the brand is gone (site redirects, name absent from product pages). Evaluate it as Proofpoint's AI-security line, priced and packaged by Proofpoint.

Nearest neighbors: [surepath-ai](surepath-ai.md) (the closest analogue — both discovery-led, both acquired by platform vendors in 2026), [witnessai](witnessai.md), [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [lanai](lanai.md); on the agent/MCP side [zenity](zenity.md), [lasso-security](lasso-security.md), [operant-ai](operant-ai.md).

## Ownership, funding & M&A
HQ **Sunnyvale, CA**; founded by cybersecurity/engineering veterans (founding year and founder names not verified — open question). Emerged from stealth **2024-09** with a **$9M seed led by Foundation Capital**. **Acquired by Proofpoint, announced as completed 2026-02-12** (PR past tense; no separate close date given); **terms undisclosed**. Ownership chain: Proofpoint is Thoma Bravo-owned, so Acuvity is now a Thoma Bravo-portfolio asset — Proofpoint's second data/AI-security acquisition after [proofpoint](proofpoint.md) (DSPM, 2024). Verified against Proofpoint's press release. Confidence: high.

## CTO / hedge-fund lens
Relevant mainly as **Proofpoint's AI-security answer**: if you already run Proofpoint for email/collaboration security and DLP, this arrives as consolidation — shadow-AI visibility plus agent/MCP governance under an existing vendor relationship, now on Proofpoint's paper and roadmap. If you're not a Proofpoint shop, the comparators are the independent shadow-AI specialists; there is no longer an Acuvity to buy on its own. Practical note for procurement: ask for the SKU names (AI Access Security / Agentic AI Security / AI MCP Security), not "Acuvity" — the name has been retired for ~5 months and is absent from Proofpoint's product content. Integration depth and pricing still unverified; no FS traction verified.

## Competitors / alternatives
[surepath-ai](surepath-ai.md), [witnessai](witnessai.md), [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [nudge-security](nudge-security.md), [lanai](lanai.md), [cyberhaven](cyberhaven.md), [zenity](zenity.md), [lasso-security](lasso-security.md).

## Open questions / to verify
- Founding year and founder names/backgrounds.
- Deployment model (SaaS assumed, unconfirmed) and workforce-side enforcement mechanism (agent, browser extension, network) — the MCP side is confirmed gateway.
- Packaging and pricing of the three AI Security SKUs (sold separately, bundled, or platform-only?).
- Deal price (undisclosed) and whether a separate close date was ever stated — the PR is past-tense at announcement.
- Data handling: where AI-usage telemetry/prompt content is processed and retained.
- ~~Whether RYNO survives as a product/brand~~ — **resolved 2026-07-27: brand retired.**
- ~~MCP support depth (monitoring vs gateway)~~ — **resolved 2026-07-27: `gateway` (inline enforcement).**

## Sources
- [Proofpoint AI Security platform (redirect target of acuvity.ai)](https://www.proofpoint.com/us/platform/ai-security) — fetched 2026-07-27 — supports: acuvity.ai 301-redirects here, page fully Proofpoint-branded with no Acuvity/RYNO mention, brand retired, "intent-aware" AI-security-plus-data-security positioning; confidence: high
- [Proofpoint AI MCP Security](https://www.proofpoint.com/us/products/ai-mcp-security) — fetched 2026-07-27 — supports: MCP discovery + risk classification, gateway-style inline enforcement, transaction forensics, trusted-MCP-server registry; confidence: high
- [Proofpoint AI Access Security](https://www.proofpoint.com/us/products/ai-access-security) — fetched 2026-07-27 — supports: AI app/agent discovery and inventory, runtime observability, 18 built-in detectors, forensic audit trails, SIEM/SOAR routing; confidence: high
- [Proofpoint acquires Acuvity (Proofpoint press release)](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-acquires-acuvity-deliver-ai-security-and-governance-across) — fetched 2026-07-13 — supports: acquisition announced as completed 2026-02-12, terms undisclosed, product scope (shadow AI + agents/MCP), agentic-workspace positioning; confidence: high
- Press/search corroboration (BankInfoSecurity, Futurum, Crunchbase, No Jitter, Thoma Bravo newsroom — not separately cached): $9M seed led by Foundation Capital at 2024-09 stealth exit, Sunnyvale HQ, ~24 employees, RYNO platform name; confidence: med.
- Cached: `raw/sources/2026-07-13--acuvity--proofpoint-acquisition-pr.md`, `raw/sources/2026-07-27--acuvity--brand-retired-proofpoint-ai-security.md`

## History
- [2026-07-13] Page created via wiki-create + researched: surfaced while triaging Google-suggested SurePath competitors (user request). Acquired-closed by Proofpoint (announced as completed 2026-02-12); categorized ai-access-governance + agent-runtime-security cross-list.
- [2026-07-27] URL audit flagged the site. Verified `acuvity.ai` **301-redirects to https://www.proofpoint.com/us/platform/ai-security**, a wholly Proofpoint-branded page with zero Acuvity content; no "Acuvity is now Proofpoint" transition page exists (404). **Brand retired**; capability now ships as AI Access Security / Agentic AI Security / AI MCP Security. Updated `website`, `aka`, `mcp_support` unverified→gateway, `last_verified`→2026-07-27; added frontmatter `sources:`. Resolved two open questions (brand survival, MCP depth). Slug kept as `acuvity` — the tech split across three SKUs, so no single product slug applies (contrast [proofpoint](proofpoint.md)). No new acquisition facts: announced-as-completed 2026-02-12 stands, price still undisclosed.
