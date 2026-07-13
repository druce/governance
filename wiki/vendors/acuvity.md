---
title: Acuvity
type: vendor
name: Acuvity
slug: acuvity
aka: [RYNO]
primary_category: ai-access-governance
also_listed_in: [agent-runtime-security]
website: https://acuvity.ai
founded: null
hq: Sunnyvale, California, USA
ownership_state: acquired-closed
owner: Proofpoint
ownership_note: Acquired by Proofpoint — announced as completed 2026-02-12; terms undisclosed. (Proofpoint is itself Thoma Bravo-owned; this is its second data/AI-security buy after Normalyze.)
acquisition: {announced: 2026-02-12, closed: 2026-02-12, price: null}
funding_total: $9M seed (pre-acquisition)
last_funding: $9M seed led by Foundation Capital, announced at stealth exit 2024-09
market_position: null
deployment_model: [saas]
form_factor: [platform]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-13
verify_after: null
tags: [acquired, shadow-ai, mcp-security, agentic-workspace, proofpoint]
---

# Acuvity

> **Researched 2026-07-13.** Primary category: [ai-access-governance](../categories/ai-access-governance.md). **Acquired by Proofpoint** — announced as completed 2026-02-12.

**One-liner** — An AI security and governance startup (RYNO platform) covering the full span of enterprise AI usage — shadow-AI visibility from endpoints and browsers through to runtime enforcement on agents and MCP servers — now the AI-security layer of Proofpoint's "agentic workspace" platform.

## What it does
Acuvity's RYNO platform gives security teams visibility and enforcement across "the full range of AI usage in the enterprise": employee GenAI use discovered at endpoints and browsers (including locally installed tools like Ollama), plus runtime inspection and governance of autonomous agents and **MCP servers**. That dual scope — workforce shadow-AI governance *and* agent/MCP runtime security in one product — is what distinguished it from single-lane peers and what Proofpoint bought it for.

## Where it sits in the stack
Primary [ai-access-governance](../categories/ai-access-governance.md) (the workforce AI-usage governance job — the natural fit with Proofpoint's human-centric security portfolio), cross-listed in [agent-runtime-security](../categories/agent-runtime-security.md) for the agent/MCP runtime side. Layer: model-prompt. Post-acquisition, Proofpoint positions the combination as "the first unified platform to comprehensively secure every dimension of the agentic workspace" — collaboration security, data security/governance, and AI security together.

## Deployment & architecture
Platform with endpoint/browser-level visibility and runtime enforcement points for agents and MCP traffic; SaaS delivery assumed but not confirmed (open question). Emerged from stealth 2024-09; ran as a lean ~24-person team pre-acquisition.

## Positioning & differentiators
- **Breadth across the AI usage surface** — one platform from employee chat use to local AI tools to agent/MCP infrastructure, where most shadow-AI peers stop at the browser/network.
- **MCP-era coverage** — early mover on securing MCP servers and agent tool calls, the same forward-looking angle F5 cites for [surepath-ai](surepath-ai.md).
- **Now a platform module** — like [normalyze](normalyze.md) before it, the standalone brand is being absorbed into Proofpoint; evaluate it as Proofpoint's AI-security capability, not an independent tool.

Nearest neighbors: [surepath-ai](surepath-ai.md) (the closest analogue — both discovery-led, both acquired by platform vendors in 2026), [witnessai](witnessai.md), [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [lanai](lanai.md); on the agent/MCP side [zenity](zenity.md), [lasso-security](lasso-security.md), [operant-ai](operant-ai.md).

## Ownership, funding & M&A
HQ **Sunnyvale, CA**; founded by cybersecurity/engineering veterans (founding year and founder names not verified — open question). Emerged from stealth **2024-09** with a **$9M seed led by Foundation Capital**. **Acquired by Proofpoint, announced as completed 2026-02-12** (PR past tense; no separate close date given); **terms undisclosed**. Ownership chain: Proofpoint is Thoma Bravo-owned, so Acuvity is now a Thoma Bravo-portfolio asset — Proofpoint's second data/AI-security acquisition after [normalyze](normalyze.md) (DSPM, 2024). Verified against Proofpoint's press release. Confidence: high.

## CTO / hedge-fund lens
Relevant mainly as **Proofpoint's AI-security answer**: if you already run Proofpoint for email/collaboration security and DLP, the Acuvity capability arrives as consolidation — shadow-AI visibility plus agent/MCP governance under an existing vendor relationship. If you're not a Proofpoint shop, the standalone comparators are the independent shadow-AI specialists. Too early to judge integration depth or packaging; no FS traction verified.

## Competitors / alternatives
[surepath-ai](surepath-ai.md), [witnessai](witnessai.md), [harmonic-security](harmonic-security.md), [aurascape](aurascape.md), [nudge-security](nudge-security.md), [lanai](lanai.md), [cyberhaven](cyberhaven.md), [zenity](zenity.md), [lasso-security](lasso-security.md).

## Open questions / to verify
- Founding year and founder names/backgrounds.
- Deployment model (SaaS assumed, unconfirmed) and enforcement mechanism (agent, extension, network).
- Whether RYNO survives as a product/brand or is fully absorbed into Proofpoint packaging; pricing.
- MCP support depth (monitoring vs gateway-style enforcement).
- Data handling: where AI-usage telemetry/prompt content is processed and retained.

## Sources
- [Proofpoint acquires Acuvity (Proofpoint press release)](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-acquires-acuvity-deliver-ai-security-and-governance-across) — fetched 2026-07-13 — supports: acquisition announced as completed 2026-02-12, terms undisclosed, product scope (shadow AI + agents/MCP), agentic-workspace positioning; confidence: high. Cached: `raw/sources/2026-07-13--acuvity--proofpoint-acquisition-pr.md`
- Press/search corroboration (BankInfoSecurity, Futurum, Crunchbase — not separately cached): $9M seed led by Foundation Capital at 2024-09 stealth exit, Sunnyvale HQ, ~24 employees, RYNO platform name; confidence: med.

## History
- [2026-07-13] Page created via wiki-create + researched: surfaced while triaging Google-suggested SurePath competitors (user request). Acquired-closed by Proofpoint (announced as completed 2026-02-12); categorized ai-access-governance + agent-runtime-security cross-list.
