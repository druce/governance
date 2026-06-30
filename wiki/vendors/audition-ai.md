---
title: Audition AI
type: vendor
name: Audition AI
slug: audition-ai
categories: [enterprise-ai-assistant, ai-governance-platform, dlp]
layer: ux
aliases: [Saberin Data Platform]
website: "https://audition-ai.com"
founded: 2025
hq: Hauppauge, NY (Long Island)
ownership: independent
ownership_detail: Private, bootstrapped product of Saberin Data Platform, Inc. (Saberin Group, founded 2007). No external/VC funding found. No M&A.
ownership_confidence: high
funding_total: none found (likely bootstrapped)
last_funding:
deployment: [saas, self-hosted, on-prem]
target_customer: regulated finance (hedge funds, RIAs, asset managers); SMB-to-enterprise within that niche
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 2
last_updated: 2026-06-30
tags: [enterprise-ai-assistant, agent-platform, in-tenant, azure, hedge-fund, ai-governance, dlp, regulated-finance]
---

# Audition AI

> Primary category: [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md). Also [ai-governance-platform](../categories/ai-governance-platform.md), [dlp](../categories/dlp.md).

**One-liner** — A compliance-first enterprise AI platform purpose-built for hedge funds and
regulated financial firms: it deploys secure AI assistants, agents, and automations **inside
the customer's own Microsoft Azure tenant** (or on-prem), with identity-bound access, DLP,
and immutable audit trails baked in.

**Categories** — [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md), [ai-governance-platform](../categories/ai-governance-platform.md), [dlp](../categories/dlp.md)

## What it does

Audition AI lets a regulated fund use frontier LLMs against its internal documents and
workflows **without** sending data to public AI services, while producing the audit and
compliance evidence (SEC, Reg S-P) examiners expect. It targets real fund workflows —
analyst research assistants, DDQ/RFP drafting, compliance policy Q&A, investor-letter and
reporting automation, meeting/email summarization, due-diligence extraction.

The product is a build-and-deploy AI platform, not a single chatbot. Components (vendor
marketing):

- **Local Agents** — agentic workloads on Windows, Linux, cloud, or on-prem.
- **Sidekick** — personal desktop agents with browser, shell, and file access.
- **Agentic Swarms** — coordinated parallel agent teams for high-volume work.
- **Enterprise Intelligence Engine** — "sub-second" search across SharePoint, Egnyte, email,
  Teams, CRM, databases, and local files, with citations back to source documents.
- **Persona Marketplace** — pre-built managed skills/assistants.
- **Integration Forge** — MCP servers + arbitrary APIs and connectors (S3, Azure, Office
  365, Slack, SQLite, Azure Managed SQL).

The differentiating idea is a **secure enterprise AI workspace where governance is part of
the platform**, vertically tuned for capital-markets compliance — rather than a horizontal
assistant you bolt a guardrail onto.

## Where it sits in the stack

Primary home is [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) (the `ux` layer) — it is the sanctioned,
in-tenant assistant/agent platform a fund's people actually use, an alternative to the
horizontal players ([openai-chatgpt-enterprise](openai-chatgpt-enterprise.md), [anthropic-claude-enterprise](anthropic-claude-enterprise.md),
[microsoft-365-copilot](microsoft-365-copilot.md), [glean](glean.md)). It carries two strong secondary feet:
[ai-governance-platform](../categories/ai-governance-platform.md) via its GRC console (policy enforcement, violation tracking,
compliance dashboards) and [dlp](../categories/dlp.md) via built-in PII/SSN/PCI pattern matching plus
behavioral "Generative Rules." Its permission-aware retrieval also overlaps
[entitlement-aware-rag](../categories/entitlement-aware-rag.md), and its org-wide chat visibility / violation alerts edge toward
[comms-surveillance](../categories/comms-surveillance.md).

Lethal-trifecta role:

- **Sensitive-data — strong.** In-tenant deployment, permission-aware retrieval ("if a user
  doesn't have access to a document, the AI doesn't either"), and DLP keep fund data inside
  the customer's cloud. This is the product's center of gravity.
- **Egress — partial.** Keeping inference inside the customer's Azure tenant and brokering
  model access (instead of users pasting into public ChatGPT), plus DLP and audit on
  outputs, constrains where data flows; but there is no outbound network-egress firewall or
  shadow-AI CASB.
- **Untrusted-input — weak/partial.** "Generative Rules" provide some prompt-content policy
  enforcement, but no published prompt-injection defense for the Sidekick agents that have
  shell + browser + file access — an open risk the vendor's own blog gestures at.

It lives in the yellow zone: a trusted UX/agent surface through which untrusted content and
privileged tools meet.

## Deployment & architecture

Three deployment models: fully-hosted **SaaS** (Pro tiers, from ~$200/mo single-user);
deployed **inside the customer's Azure Resource Group / tenant** ("your compute, storage, AI
resources" — the Business tier); or **on-prem**. Listed on the Azure Marketplace (publisher:
Saberin Data Platform Inc).

- **Identity/access:** Azure Entra ID ([microsoft-entra](microsoft-entra.md)), described as zero-trust with
  admin-granular control of M365 permissions and permission-aware responses.
- **Models:** multi-model via **Azure AI Foundry** — Claude, GPT, Gemini, Llama, Mistral;
  claims 11,000+ models and new frontier models "within hours of release" (marketing).
- **Integrations:** MCP + APIs ("Integration Forge"); SharePoint, Egnyte, Office 365, Teams,
  Slack, CRM, S3, Azure SQL/SQLite; policy enforcement extends to AI IDEs (Cursor, Copilot).
- **Governance plumbing:** immutable audit trails, real-time email violation alerts,
  org-wide chat visibility, AI-generated compliance reports/dashboards. No published SIEM,
  DSPM, or non-Entra IdP integrations — a gap (absence of evidence).

## Positioning & differentiators

The core differentiator is **vertical focus on regulated finance** — built by a team with
~17+ years serving capital-markets compliance, with a "runs in your cloud / your tenant"
data-residency pitch and a "compliance-first," SEC / Reg S-P framing. Secondary
differentiators: dual-layer guardrails (Generative Rules + traditional DLP) and
citation-grounded answers.

Against nearest neighbors:

- vs the horizontal assistants ([openai-chatgpt-enterprise](openai-chatgpt-enterprise.md), [anthropic-claude-enterprise](anthropic-claude-enterprise.md),
  [microsoft-365-copilot](microsoft-365-copilot.md), [glean](glean.md)) — those are broad, deep, well-resourced
  general-purpose platforms; Audition AI trades breadth/scale for a finance-specific,
  in-tenant, governance-baked-in package and white-glove fit.
- vs [ai-governance-platform](../categories/ai-governance-platform.md) vendors ([credo-ai](credo-ai.md), [holistic-ai](holistic-ai.md), [modelop](modelop.md)) — those
  are model-risk / attestation platforms (SR 11-7); Audition AI's GRC is *usage* governance
  over its own AI workspace, not a model-risk register.
- vs [witnessai](witnessai.md) / [harmonic-security](harmonic-security.md) (CASB-for-AI) — those govern employees reaching
  *outward* to third-party AI; Audition AI is the sanctioned inward platform itself.

A notable credibility signal: **Eldon Sprickerhoff** (founder of eSentire, MDR pioneer) is
listed as Cybersecurity Advisor — independently corroborated.

## Ownership, funding & M&A

Independent and **private**. Audition AI is a product of **Saberin Data Platform, Inc.**, a
Saberin Group company. Saberin Group was **founded 2007** as a data-first
automation/reporting firm for capital markets; Audition AI itself appears to be a recent
(2025-era) product offshoot. **HQ: Hauppauge, NY** (Long Island).

Leadership: **Sharon Saberin** (Founder/CEO), **Benjamin Saberin** (Founder /
Developer-Architect), **Eldon Sprickerhoff** (Cybersecurity Advisor, eSentire founder), and
**Michael "Mags" Maguire** (Director of Customer Success).

**No external/VC funding was found** in any search (no seed/Series rounds, no
TechCrunch/Crunchbase funding entries; Crunchbase org pages returned 403). The structure
strongly implies it is **bootstrapped/self-funded** under the privately held Saberin Group —
an operating software/services company, not a VC-backed startup. No funding figure is
recorded here. **No M&A.** Ownership confidence: high (clear private parent); funding:
"none found," confidence medium (absence of evidence).

## CTO / hedge-fund lens

For the wiki's core reader — a hedge-fund / asset-manager CTO — this is one of the few
vendors **purpose-built for exactly that buyer**, which makes it Day-1-relevant as a
candidate for the sanctioned enterprise assistant slot. Its strengths line up with fund
requirements: in-tenant data residency, permission-aware retrieval, DLP, immutable audit,
and explicit SEC / Reg S-P framing — the things that otherwise make a fund nervous about
ChatGPT/Copilot. It can also double as the *agent* platform (research, DDQ/RFP, reporting
automations) and a usage-governance console.

The caveats are vendor maturity and verification: it is a **small, bootstrapped shop**, its
"30+ hedge fund customers" claim is unverified, and key architecture details (runtime
isolation, prompt-injection defenses for tool-using agents) are not publicly documented —
the latter a real concern given Sidekick agents wield shell, browser, and file access. No
formal model-risk attestation (SR 11-7) capability — its GRC is usage governance, not a
model-risk register. Fit: high *as a finance-vertical assistant/agent option to evaluate*,
weighed against the scale and roadmap of the horizontal incumbents and standard vendor-risk
diligence on a small provider.

## Competitors / alternatives

[openai-chatgpt-enterprise](openai-chatgpt-enterprise.md), [anthropic-claude-enterprise](anthropic-claude-enterprise.md), [microsoft-365-copilot](microsoft-365-copilot.md),
[glean](glean.md), [credo-ai](credo-ai.md), [holistic-ai](holistic-ai.md), [witnessai](witnessai.md), [harmonic-security](harmonic-security.md)

## Open questions / to verify

- Exact Audition AI product launch date and whether it's a standalone entity vs. a Saberin
  Data Platform product line (appears 2025-era).
- The "30+ hedge fund customers" claim — no independent corroboration.
- Whether there is any outside funding (none found; presumed bootstrapped).
- Real architecture details: runtime isolation and prompt-injection defenses for the
  tool-using (shell/browser/file) Sidekick agents.
- Pricing above the published $200/mo Pro tier (Business/Enterprise are custom).

## Sources
- [Audition AI homepage + GRC/Agents/Leadership/Team pages](https://audition-ai.com/) — fetched 2026-06-30 — supports: in-tenant Azure deployment, product components, dual-layer DLP + Generative Rules, Entra zero-trust, permission-aware retrieval, leadership, Hauppauge NY HQ, Saberin parent, hedge-fund target, "30+ funds" claim (vendor/marketing); confidence: high (that they claim it) / med (accuracy)
- [Saberin Group / Saberin Data Platform](https://www.saberin.com/) — fetched 2026-06-30 — supports: parent operating company founded 2007, private/bootstrapped structure, capital-markets data heritage; confidence: high

## History
- [2026-06-30] Created and researched from vendor request. Established primary fit as a finance-vertical, in-tenant secure [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) + agent platform, with [ai-governance-platform](../categories/ai-governance-platform.md) (usage GRC) and [dlp](../categories/dlp.md) as secondary tags. Ownership: private/bootstrapped product of Saberin Data Platform Inc (Saberin Group, founded 2007), Hauppauge NY; no external funding found; no M&A. Trifecta: strong sensitive-data, partial egress, weak untrusted-input (flagged Sidekick shell/browser/file agents as an open risk). Cached 1 source file.
