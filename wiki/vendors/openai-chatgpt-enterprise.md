---
title: ChatGPT Enterprise (OpenAI)
type: vendor
name: ChatGPT Enterprise (OpenAI)
slug: openai-chatgpt-enterprise
categories: [enterprise-ai-assistant]
layer: ux
aliases: [ChatGPT Enterprise, ChatGPT Business, ChatGPT Team, OpenAI Enterprise]
website: "https://openai.com/enterprise/"
founded: 2015
hq: San Francisco, California, USA
ownership: independent
ownership_detail: "Independent. OpenAI Group PBC, controlled by the non-profit OpenAI Foundation. Microsoft holds a large minority stake (~27% reported, post Oct-2025 restructuring) plus a commercial/Azure partnership, but does not control OpenAI."
ownership_confidence: medium
funding_total: "$60B+ raised across rounds (incl. 2025 SoftBank-led round); exact cumulative figure varies by source"
last_funding: "2025 SoftBank-led round (~$40B announced); as-of 2026-06-28"
deployment: [saas, api]
target_customer: enterprise / regulated / mid-market
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [llm, assistant, frontier-model, openai]
---

# ChatGPT Enterprise (OpenAI)

**One-liner** — The enterprise tier of ChatGPT: the frontier-model chat assistant most employees already want, wrapped with admin controls, a no-training-on-your-data default, audit/compliance logging, and data-residency options.

**Categories** — [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md)

## What it does

ChatGPT Enterprise (and its smaller sibling ChatGPT Business/Team) is OpenAI's managed SaaS chat assistant for organizations: access to the latest GPT models, larger context, file/data analysis, custom GPTs, connectors to enterprise content, and an admin layer for identity, retention, and compliance. The job it does is the "front-door chatbot people actually use" — the UX-layer surface where employees draft, summarize, code, and reason over documents. For a CTO, the value of the *Enterprise* tier over consumer/Plus is governance: contractual data protection, admin visibility, and the export hooks compliance needs.

## Where it sits in the stack

UX layer, [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md). This is the human-facing endpoint of the AI stack, the direct competitor to [anthropic-claude-enterprise](anthropic-claude-enterprise.md), [microsoft-365-copilot](microsoft-365-copilot.md), [gemini-enterprise](gemini-enterprise.md), [amazon-q-business](amazon-q-business.md), [perplexity-enterprise](perplexity-enterprise.md) and [glean](glean.md).

Lethal-trifecta role: an assistant by itself does not *break* a leg of the trifecta — it is the surface where the legs converge. Employees paste **sensitive data** in and the model can act as an **egress** path. ChatGPT Enterprise's governance features (no-training default, retention controls, audit/compliance export, DLP-partner integrations) are the mitigations on the sensitive-data and egress legs. The untrusted-input leg (prompt injection via tools/RAG/web browsing) is only partly addressed at this layer; that is why shops still layer [ai-runtime-security](../categories/ai-runtime-security.md) / [ai-access-governance](../categories/ai-access-governance.md) / [dlp](../categories/dlp.md) in front of it. It lives across trust zones — a sanctioned green-zone tool whose whole point is to keep employees off shadow-AI in the red zone.

## Deployment & architecture

- **SaaS** ChatGPT web/desktop/mobile app, administered through a workspace admin console. Also delivered as the **API** platform (separate commercial agreement, same privacy posture).
- **Identity** SAML **SSO** and **SCIM** provisioning/deprovisioning against the customer's IdP (Entra, Okta, etc.); domain verification; role-based admin.
- **Compliance / audit** an **Audit Logs API** and the **Enterprise Compliance API** (now part of OpenAI's unified "Compliance Logs Platform" exporting immutable, time-windowed JSONL log files). Records time-stamped interactions: conversations, uploaded files, workspace GPT configs + metadata, memories, and workspace users. This is the integration point for **comms-surveillance and archiving**: launch partners and connectors include **Global Relay**, **Smarsh**, **Theta Lake** and other eDiscovery/DLP vendors (see [comms-surveillance](../categories/comms-surveillance.md)). Global Relay's connector captures prompts, conversations and file attachments into Global Relay Archive for FINRA 3310 / SEC 17a-4 recordkeeping.
- **Connectors / retrieval** connectors to SharePoint, Google Drive, etc., bringing it into [content-sources](../categories/content-sources.md) / RAG territory (entitlement enforcement depends on the connector).
- **Data residency** at-rest storage in-region for Europe, UK, US, Canada, Japan, South Korea, Singapore, India, Australia, and UAE; included at no extra cost for Enterprise/Edu. Optional **inference residency** (in-region GPU) in the US or Europe.

## Positioning & differentiators

What it's known for: the strongest consumer/employee pull of any assistant (people already know ChatGPT), frontier model quality, and the broadest third-party tooling ecosystem.

Enterprise governance posture a hedge-fund CTO cares about:
- **No training on your data by default** — across ChatGPT Enterprise, Business/Team, and the API, OpenAI does not train on customer content unless the customer explicitly opts in. Customer owns inputs and outputs.
- **Retention controls** — admins set retention; deleted conversations purged (≈30 days) unless legally required.
- **Encryption** — AES-256 at rest, TLS 1.2+ in transit.
- **Certifications** — SOC 2 Type 2 (ChatGPT Enterprise and API platform), ISO/IEC 27001 (and 27017/27018/27701), CSA STAR; DPA available; supports GDPR and CCPA. Documentation and subprocessor list on the OpenAI Trust Portal (trust.openai.com).

vs nearest neighbors: [microsoft-365-copilot](microsoft-365-copilot.md) wins on being *inside* the M365 tenant with existing Purview/Entra governance and per-user entitlement-aware Graph grounding; [anthropic-claude-enterprise](anthropic-claude-enterprise.md) competes on similar enterprise posture and safety positioning; [glean](glean.md) differentiates on entitlement-aware enterprise search/RAG. ChatGPT Enterprise's edge is model strength + adoption; its relative gap is that governance is bolted on via its own console/API rather than inheriting an existing enterprise control plane.

## Ownership, funding & M&A

- **Ownership: independent.** OpenAI operates as OpenAI Group PBC, controlled by the non-profit OpenAI Foundation (post October-2025 restructuring). **Microsoft holds a large minority equity stake (reported ~27%)** and a deep commercial/Azure partnership, but **does not own or control OpenAI**. No acquirer; the seed carried no M&A flag. `ownership_confidence: medium` — the Microsoft stake percentage and restructuring details are widely reported but volatile; verify the exact figure before relying on it. (as-of 2026-06-28)
- **Funding:** OpenAI has raised on the order of $60B+ cumulatively, including a 2025 SoftBank-led round (~$40B announced). Figures vary by source and date.
- **OpenAI as acquirer:** OpenAI has itself made acquisitions (e.g. [promptfoo](promptfoo.md) per the registry); not material to the Enterprise governance posture.

## CTO / hedge-fund lens

- **Day-1.** A sanctioned enterprise assistant is one of the first things a fund stands up — both to give staff a capable tool and to kill shadow-AI. ChatGPT Enterprise is a default-shortlist option.
- **Why the Enterprise tier specifically:** the no-training default + DPA + SOC 2/ISO + audit/Compliance API are the contractual and technical facts your risk and compliance teams will ask for. The consumer/Plus tier does **not** carry the same data-ownership and logging guarantees.
- **Comms surveillance (MAR/MNPI/recordkeeping):** the Compliance API + archiving connectors (Global Relay, Smarsh, Theta Lake) let you pull ChatGPT interactions into the same surveillance/archive pipeline as email and chat — important for SEC 17a-4 / FINRA 3310 books-and-records and for catching MNPI leakage. This is a meaningful differentiator for a regulated fund and a reason to prefer Enterprise over ad-hoc usage.
- **Data residency:** EU/UK/US/etc. in-region storage (and optional in-region inference) helps with GDPR and client/LP data-handling commitments.
- **SR 11-7 / model risk:** as a third-party frontier model it falls under vendor/model risk — route it through [vendor-risk](../categories/vendor-risk.md) TPRM and, if used for anything decision-relevant, [ai-governance-platform](../categories/ai-governance-platform.md) controls. The assistant layer itself does not give you model-risk documentation.
- **Residual gaps to cover elsewhere:** prompt-injection/untrusted-input and egress DLP at the assistant boundary are only partly handled here; pair with [ai-access-governance](../categories/ai-access-governance.md) / [dlp](../categories/dlp.md) / [ai-runtime-security](../categories/ai-runtime-security.md) if those risks matter. Entitlement-aware grounding depends on how connectors are configured — don't assume per-user permission trimming for RAG.
- **Fit:** **high** for most funds as the sanctioned assistant; the main reasons to pick a neighbor are a Microsoft-first estate (Copilot) or an entitlement-aware-search-first need (Glean).

## Competitors / alternatives

[anthropic-claude-enterprise](anthropic-claude-enterprise.md) · [microsoft-365-copilot](microsoft-365-copilot.md) · [gemini-enterprise](gemini-enterprise.md) · [amazon-q-business](amazon-q-business.md) · [perplexity-enterprise](perplexity-enterprise.md) · [glean](glean.md)

## Open questions / to verify

- Exact current Microsoft equity stake and the precise post-restructuring governance terms (volatile; ~27% reported).
- Cumulative funding figure and latest round size (sources disagree).
- Whether entitlement-aware permission trimming on enterprise connectors matches Copilot/Glean for RAG use cases.
- Current full list of archiving/eDiscovery/DLP Compliance-API partners and whether Theta Lake's integration is GA.

## Sources

- [Enterprise privacy at OpenAI](https://openai.com/enterprise-privacy/) — fetched 2026-06-28 (via search extraction; openai.com 403s direct fetch) — supports: no-training default, encryption, certifications, retention, audit log; confidence: high
- [Business data privacy, security & compliance / Security and privacy at OpenAI / Trust Portal](https://openai.com/business-data/) — fetched 2026-06-28 — supports: SOC 2 Type 2, ISO 27001/27017/27018/27701, CSA STAR, DPA, GDPR/CCPA; confidence: high
- [Expanding data residency access to business customers worldwide + Data residency help article](https://openai.com/index/expanding-data-residency-access-to-business-customers-worldwide/) — fetched 2026-06-28 — supports: residency country list, covered content, inference residency, no extra cost; confidence: high
- [OpenAI rolls out Compliance API and integrations for ChatGPT Enterprise — SecurityWeek](https://www.securityweek.com/openai-rolls-out-compliance-api-and-integrations-for-chatgpt-enterprise/) — fetched 2026-06-28 — supports: what the Compliance API records, eDiscovery/DLP integrations, regulated-industry framing; confidence: high
- [Global Relay announces integration with OpenAI's ChatGPT Enterprise Compliance API](https://www.globalrelay.com/resources/our-news/global-relay-announces-integration-with-openais-chatgpt-enterprise-compliance-api/) — fetched 2026-06-28 — supports: comms archiving/surveillance hook, FINRA 3310 / SEC 17a-4; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent ownership (OpenAI Foundation-controlled PBC; Microsoft ~27% minority, no control, confidence medium); documented enterprise governance posture — no-training default across Enterprise/Business/API, AES-256/TLS encryption, SOC 2 Type 2 + ISO 27001 family + CSA STAR + DPA/GDPR, SAML SSO + SCIM, Enterprise Compliance API / Audit Logs + archiving connectors (Global Relay/Smarsh/Theta Lake) for SEC 17a-4/FINRA recordkeeping, and data residency across 10 regions incl. optional in-region inference. Set hedge_fund_fit high, status researched, 4 sources cached. No M&A flag; no contradictions.
