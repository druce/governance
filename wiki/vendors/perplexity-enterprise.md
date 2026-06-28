---
type: vendor
name: Perplexity Enterprise
slug: perplexity-enterprise
categories: [enterprise-ai-assistant]
layer: ux
aliases: [Perplexity Enterprise Pro, Perplexity for Enterprise, Enterprise Max]
website: https://www.perplexity.ai/enterprise
founded: 2022
hq: San Francisco, California, USA
ownership: independent
ownership_detail: "Private, venture-backed (Perplexity AI, Inc.); no single controlling owner. Valued ~$20B (Sept 2025, ~$200M round); reported ~$21B after a Series E-6 round early 2026. Investors incl. Nvidia, Jeff Bezos, SoftBank Vision Fund 2, IVP, Accel, NEA, Databricks."
ownership_confidence: high
funding_total: "~$1B+ (uncertain; Wikipedia-disclosed rounds ~$665M, aggregators report higher)"
last_funding: "~$200M round Sept 2025 at ~$20B valuation; further raise reported early 2026"
deployment: [saas]
target_customer: enterprise / mid-market (knowledge workers; research-heavy teams)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [untrusted-input, sensitive-data, egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [answer-engine, web-search, rag, assistant]
---

# Perplexity Enterprise

> Researched 2026-06-28. Primary category: [[enterprise-ai-assistant]].

**One-liner** — An enterprise "answer engine": a web-search-grounded AI assistant with citations, plus enterprise add-ons (Spaces, internal file/app connectors, SSO/SCIM, admin controls, no-training guarantee).

## What it does
Perplexity is primarily a **web-search assistant / answer engine** — you ask a question, it searches the live web, synthesizes an answer, and shows **inline citations**. Enterprise Pro and Enterprise Max wrap that consumer product in a governance shell: it stops training on your data, adds **Spaces** (shared workspaces / collections), and lets the assistant search across **internal files and connected work apps** (Google Drive, OneDrive, SharePoint, Box, Dropbox) alongside the web. The pitch to a knowledge-work org is "Google + ChatGPT for research," with sources attached so analysts can verify claims.

Note the center of gravity differs from [[openai-chatgpt-enterprise]] / [[anthropic-claude-enterprise]]: Perplexity leads with **external web research and citations**, not general-purpose chat or coding. Internal-knowledge RAG is a newer add-on, not the core.

## Where it sits in the stack
- Category: [[enterprise-ai-assistant]] (UX layer) — the chatbot end-users actually touch.
- Lethal-trifecta exposure: as a research assistant it pulls **untrusted web content** into the model (prompt-injection surface), can be pointed at **sensitive internal data** via connectors, and has an inherent **egress** path (it sends queries to the web and to third-party model providers). All three legs are in play, which is exactly why the enterprise controls below matter.
- It is a consumer of, not a substitute for, perimeter controls like an [[ai-gateway]], [[ai-access-governance]] (shadow-AI / CASB-for-AI), and [[dlp]]. A fund would typically still want shadow-AI discovery to see who's using the *consumer* Perplexity vs. the sanctioned enterprise tenant.

## Deployment & architecture
- **SaaS only.** No self-hosted / on-prem option; runs in Perplexity's cloud. Models are a mix of Perplexity's own and third-party frontier models (OpenAI, Anthropic, Google) accessed under contract.
- **Identity:** SAML 2.0 SSO (Okta and other IdPs), **SCIM** provisioning (Okta, Entra ID, Google Workspace), MFA, short-lived session credentials.
- **Connectors:** Google Drive, OneDrive, SharePoint, Box, Dropbox. Connectors are **permission-aware at view time** — e.g. a file deleted or de-permissioned in SharePoint is immediately removed from Perplexity; files surfaced from connected apps in a Space are searchable by anyone with Space access, but a user needs rights on the underlying app to see file *contents*. Admins enable/disable each connector org-wide.
- **Admin & audit:** central admin panel governs file upload/download, sharing of Threads/Pages/Spaces, and connectors. **Audit Logs** capture end-to-end queries (input, agent steps, answers) plus admin setting changes (event type, timestamp, user email, IP) and are pushed in **real time to a customer-configured webhook (HTTP POST)** — that is the main hook into a SIEM/SOC. Audit Logs are gated to orgs with 50+ seats or ≥1 Enterprise Max user. Data export in JSON/CSV/PDF.

## Positioning & differentiators
- **Differentiator:** citation-first web research. For an investment shop the appeal is fast, sourced answers on markets, companies, filings, and news — with links to chase down.
- **Governance posture (the CTO-relevant part):**
  - **No training on enterprise data** — Enterprise content is not used to train Perplexity's or third-party providers' models; Perplexity says it holds contractual no-train terms with model providers, reviewed annually.
  - **Retention controls** — uploaded files default to short retention (~7 days; some materials cite 1-day auto-delete); the containing Thread persists until deleted. Orgs with 50+ Pro seats or ≥1 Max seat can set **custom retention** and force-delete on demand.
  - **Certifications** — SOC 2 Type II (2026 attestation), HIPAA-aligned safeguards (HIPAA gap assessment 2025), GDPR, plus a Trust Center (trust.perplexity.ai) and CAIQlite. DPA available. PCI DSS appears in marketing summaries — verify before relying on it.
  - **Data residency** — no evidence of configurable regional residency (e.g. EU-only) for the enterprise assistant; treat as **not available** until confirmed. This is a gap vs. some Microsoft/Google offerings.
- vs. neighbors: [[glean]] is the closer comparison for *internal* entitlement-aware enterprise search/RAG ([[entitlement-aware-rag]]); Perplexity's connectors are newer and web-research-led. [[openai-chatgpt-enterprise]] and [[anthropic-claude-enterprise]] are stronger general assistants; [[microsoft-365-copilot]] / [[gemini-enterprise]] win on native data-estate integration and residency.

## Ownership, funding & M&A
- **Independent, private, venture-backed.** No seed M&A flag and none found — Perplexity is an acquirer-of-talent/none-of-note, not acquired. Ownership confidence **high** (well-documented private company).
- Valued **~$20B (Sept 2025)** after a ~$200M round; reports of a **Series E-6 ~$21B** valuation early 2026 (figures vary $18–21B across outlets). Investors: Nvidia, Jeff Bezos (personal), SoftBank Vision Fund 2, IVP, Accel, NEA, Databricks, Bessemer, Nat Friedman, Tobias Lütke. Microsoft committed ~$750M GPU capacity (Jan 2026).
- **Funding total is uncertain:** Wikipedia-disclosed rounds sum ~$665M; aggregators (Tracxn/TexAu) report ~$1B–$1.7B. Left as a range, not a point estimate.

## CTO / hedge-fund lens
- **Day-1 question, conditional fit.** As an *answer engine* it's a genuinely useful research tool for analysts and is cheap to pilot. The governance shell (no-train, SSO/SCIM, audit logs, retention controls) clears the basic enterprise bar.
- **Where a fund should be careful:**
  - **Comms surveillance / eDiscovery:** there is **no native archival or eDiscovery/WORM hook** for MAR/MNPI-style supervision. The audit-log webhook can stream activity to a SIEM, but that is monitoring telemetry, not a compliant comms archive. If analyst interactions need to be captured for surveillance ([[comms-surveillance]]) or legal hold, you'd have to build it off the webhook/export — flag this explicitly with Compliance.
  - **Data residency** appears unavailable — a problem for EU/region-locked mandates.
  - **SaaS-only + third-party model providers** means data leaves your tenant to multiple providers under contract; acceptable for many, but diligence the subprocessor list.
- **SR 11-7 / model risk:** low direct relevance — it's an assistant, not a model you deploy in a decision pipeline. Treat outputs as un-validated research, not model output.
- **Fit:** medium. Good sanctioned research tool; not a system of record, not a surveillance-grade comms channel. Most useful where citations and live web matter more than deep internal-data RAG.

## Competitors / alternatives
- [[glean]] — internal entitlement-aware enterprise search/assistant (closest on connectors).
- [[openai-chatgpt-enterprise]], [[anthropic-claude-enterprise]] — stronger general assistants.
- [[microsoft-365-copilot]], [[gemini-enterprise]], [[amazon-q-business]] — data-estate-native assistants with stronger residency/compliance stories.

## Open questions / to verify
- Exact default retention (7-day vs 1-day) and whether custom retention covers Threads/Pages, not just uploaded files.
- Whether data residency (e.g. EU) is offered at all for the enterprise assistant.
- Current subprocessor / model-provider list and PCI DSS scope (marketing claim).
- Precise cumulative funding figure and confirmation of the early-2026 Series E-6 valuation from a primary source.

## Sources
- [Perplexity Enterprise Security / "How Perplexity Enterprise Pro Keeps Your Data Secure"](https://www.perplexity.ai/enterprise/security) — fetched 2026-06-28 (via search summary; site 403s WebFetch) — supports: no-training, SSO/SAML, SCIM, MFA, SOC 2 Type II, HIPAA/GDPR; confidence: med.
- [Data Retention & Privacy for Enterprise / Audit Logs / SharePoint connector (Help Center)](https://www.perplexity.ai/help-center/en/articles/11187708-data-retention-and-privacy-for-enterprise-organizations-and-users) — fetched 2026-06-28 (via search summary) — supports: retention defaults + custom retention, admin controls, permission-aware connectors, audit-log webhook, export formats; confidence: med.
- [Perplexity AI — Wikipedia](https://en.wikipedia.org/wiki/Perplexity_AI) — fetched 2026-06-28 — supports: founding 2022, SF HQ, private/independent, investors, ~$20B valuation; confidence: high (corporate facts) / med (funding total).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Perplexity Enterprise as SaaS web-search answer engine with enterprise governance shell (no-train on enterprise data, SAML SSO + SCIM, MFA, admin/audit controls with real-time audit-log webhook, ~7-day default file retention + custom retention for larger orgs, permission-aware connectors), SOC 2 Type II / HIPAA / GDPR certs; ownership independent/private venture-backed (~$20B Sept 2025, high confidence) with no M&A; flagged absence of native eDiscovery/comms-archival and apparent lack of data residency as hedge-fund gaps. fit = medium.
