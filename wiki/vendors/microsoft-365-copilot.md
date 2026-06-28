---
type: vendor
name: Microsoft 365 Copilot
slug: microsoft-365-copilot
categories: [enterprise-ai-assistant]
layer: ux
aliases: [M365 Copilot, Office Copilot, Copilot for Microsoft 365]
website: https://www.microsoft.com/microsoft-365/copilot
founded: 1975
hq: Redmond, Washington, USA
ownership: public
ownership_detail: "Product of Microsoft Corporation (NASDAQ: MSFT)"
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [microsoft, m365, copilot, enterprise-assistant, rag]
---

# Microsoft 365 Copilot

**One-liner** — The generative-AI assistant embedded across Word, Excel, PowerPoint, Outlook, Teams and the M365 apps, grounded in your tenant's own content via Microsoft Graph and governed by the Purview/Entra controls you already own.

**Categories** — [[enterprise-ai-assistant]] (primary). Tightly coupled to [[microsoft-graph]], [[microsoft-purview]], [[sharepoint]], and the [[entitlement-aware-rag]] pattern.

## What it does

M365 Copilot is an orchestration engine that connects large language models to three things: the LLM, content in [[microsoft-graph]] (emails, chats, documents, calendar, meetings the user can access), and the Office apps the user works in. It answers questions, drafts documents, summarizes meetings/threads, and builds slides/spreadsheets grounded in the organization's own data. For a hedge fund, the appeal is that the assistant most staff will actually use is the one already inside Outlook, Teams, Excel and SharePoint — no new data plane, no new vendor for the core stack.

The governance story is the reason it belongs on a CTO's Day-1 list rather than a shadow-IT worry: it inherits the M365 tenant's identity, permissions, encryption, audit, retention and DLP rather than introducing a parallel one.

## Where it sits in the stack

UX layer — the [[enterprise-ai-assistant]] slot, alongside [[openai-chatgpt-enterprise]], [[anthropic-claude-enterprise]], [[gemini-enterprise]], [[amazon-q-business]] and [[glean]]. Because it grounds answers in tenant content through [[microsoft-graph]] honoring existing permissions, it is also a concrete instance of the [[entitlement-aware-rag]] pattern.

Lethal-trifecta role: its primary exposure is the **sensitive-data** leg — it reads broadly across the user's accessible corpus, so the risk is not the model leaking to the open internet (data stays in the M365 service boundary) but **oversharing**: Copilot surfaces anything a user technically can open, including content that was over-permissioned in SharePoint/OneDrive long before AI made it easy to find. It addresses the **untrusted-input** leg partially via built-in jailbreak/cross-prompt-injection (XPIA) classifiers, but it is a productivity assistant, not a security control — pair it with [[microsoft-purview]] DSPM-for-AI and data-access remediation.

## Deployment & architecture

- **SaaS only**, delivered as a per-user add-on license on top of Microsoft 365 (E3/E5/Business). No self-hosting.
- **Grounding** runs through [[microsoft-graph]] and the Semantic Index, which "honors the user identity-based access boundary so that the grounding process only accesses content that the current user is authorized to access." Permissions come from [[sharepoint]]/OneDrive/Exchange/Teams — Copilot does not relax them.
- **Processing** uses Azure OpenAI service (not OpenAI's public service); prompts, retrieved data and responses "remain within the Microsoft 365 service boundary." Azure OpenAI does not cache content for Copilot, and Copilot has opted out of Azure OpenAI abuse-monitoring/human review.
- **Model note (as-of 2026-06):** Anthropic models are now offered within some Copilot experiences as a subprocessor under the Microsoft Product Terms/DPA — but Microsoft states Anthropic models are **out of scope for the EU Data Boundary** and in-country LLM-processing commitments. Worth flagging for EU-resident funds.
- **Extensibility** via Graph connectors and agents; agents are admin-gated in the M365 admin center (admins see each agent's permissions, data access, terms and privacy statement).
- **Integrations:** [[microsoft-entra]] for identity/SSO; [[microsoft-purview]] for audit, DLP, eDiscovery, retention, Communication Compliance, Insider Risk, DSPM-for-AI; [[microsoft-defender]] XDR receives Insider-Risk AI signals.

## Enterprise governance posture (what a hedge-fund CTO actually checks)

- **No-training commitment (high confidence):** "Prompts, responses, and data accessed through Microsoft Graph aren't used to train foundation LLMs, including those used by Microsoft 365 Copilot." Stored interaction history is encrypted and likewise not used for training. Optional customer feedback is also excluded from foundation-model training.
- **Data residency / EU Data Boundary:** Copilot was added as a covered workload in the Product Terms data-residency commitments on 2024-03-01; covered by **Advanced Data Residency (ADR)** and **Multi-Geo**. For EU customers it is an EU Data Boundary service (EU traffic stays in the EUDB); non-EU customers may have queries processed in US/EU/other regions. Caveat above re Anthropic models being out of EUDB scope.
- **Entitlement-aware retrieval:** Copilot "only surfaces organizational data to which individual users have at least view permissions," using the same underlying access controls as the rest of M365. The flip side is Microsoft's own warning to fix the permission model first — the well-known **oversharing risk**. [[microsoft-purview]] DSPM-for-AI ships a weekly **data risk assessment** ("Protect your data from potential oversharing risks") plus one-click remediation precisely for this.
- **Sensitivity labels / encryption:** Copilot honors [[microsoft-purview]] Information Protection labels and IRM; for encrypted items the user must hold both VIEW and EXTRACT usage rights before content is returned. Copilot in Word/PowerPoint/Outlook inherits the source file's label onto generated content; Copilot Chat surfaces the highest-priority (most restrictive) label among cited items. (Best results require enabling sensitivity labels for SharePoint/OneDrive.)
- **Purview audit & comms surveillance (hedge-fund-critical):** Copilot prompts and responses are captured in the unified audit log (including which M365 service and which files were referenced) and stored in the user's mailbox. They are discoverable via **eDiscovery** (query for `Copilot activity` / ItemClass `IPM.SkypeTeams.Message.Copilot.*`), subject to **retention/Data Lifecycle** policies ("Microsoft Copilot Experiences"), and monitorable by **Communication Compliance** — i.e., Copilot interactions fall under the same MAR/MNPI comms-surveillance regime a fund already runs (see [[comms-surveillance]]). **DLP** has a dedicated "Microsoft 365 Copilot and Copilot Chat" policy location to block processing of prompts/files by sensitive-info type or label; Endpoint DLP can block pastes into third-party gen-AI sites. **Insider Risk Management** has a "Risky AI usage" template (prompt injection, protected-material access).
- **Identity & access:** tenant isolation via [[microsoft-entra]] authorization + RBAC; Copilot rides existing Entra SSO and (as a connected experience within M365 Apps) is governed by the same Conditional Access and admin controls — verify CA policy coverage for your specific Copilot surfaces.
- **Certifications / contractual:** Copilot inherits M365's commitments — GDPR, ISO/IEC 27001, ISO/IEC 27018, **ISO/IEC 42001** (AI management systems), HIPAA, plus the Microsoft Product Terms / Data Protection Addendum (DPA). Broader M365 service certifications (SOC 1/2, FedRAMP) apply at the platform level (verify scope per surface). Microsoft extends its Copilot Copyright Commitment (IP indemnity) to Copilot output when built-in guardrails are used.

## Positioning & differentiators

Versus [[openai-chatgpt-enterprise]] and [[anthropic-claude-enterprise]]: those are strong standalone assistants but sit *outside* the productivity suite and require their own connectors to reach enterprise content. M365 Copilot's edge is native grounding in the data and permissions you already manage, and reuse of the Purview/Entra control plane — there is essentially nothing new to govern. Versus [[glean]] (a cross-app entitlement-aware assistant that indexes many SaaS sources): Glean is more source-agnostic and often better where the corpus is non-Microsoft; Copilot is deepest where the shop is Microsoft-centric. Its weakness is the inverse: Copilot's value collapses if your knowledge lives outside M365, and its oversharing exposure is only as good as your SharePoint hygiene.

## Ownership, funding & M&A

Microsoft 365 Copilot is a product of **Microsoft Corporation** (NASDAQ: MSFT), a public company headquartered in Redmond, WA (founded 1975). Not an independent or acquired entity — the stub's `independent` value was incorrect and is corrected here to `public` (high confidence). No funding/M&A applies. GA for enterprise was 2023-11-01.

## CTO / hedge-fund lens

Day-1 for any Microsoft-shop fund: if you run M365, this is the assistant your staff will reach for, so governing it is not optional. The good news is it folds into existing controls — Entra SSO/Conditional Access, Purview audit/eDiscovery/retention/DLP/Communication Compliance, sensitivity labels. The real project is **not** the AI; it is **permission hygiene** in SharePoint/OneDrive before turn-on, because Copilot weaponizes oversharing. Run Purview DSPM-for-AI oversharing assessments first. SR 11-7/model-risk angle is light (it is a productivity tool, not a pricing/risk model), but comms-surveillance and records-retention obligations attach directly to Copilot interactions, which is squarely a hedge-fund concern. Note for EU-resident or strict-residency funds: validate which underlying models are in play given the Anthropic-out-of-EUDB caveat.

## Competitors / alternatives

[[openai-chatgpt-enterprise]], [[anthropic-claude-enterprise]], [[gemini-enterprise]], [[amazon-q-business]], [[perplexity-enterprise]], [[glean]].

## Open questions / to verify
- Exact Conditional Access / SCIM coverage for each Copilot surface (Chat web vs in-app) — Entra governs M365 broadly; confirm per-surface granularity.
- FedRAMP authorization level/boundary specifically covering Copilot (vs M365 platform).
- Current default underlying model mix (OpenAI vs Anthropic vs Microsoft) per experience, and the residency implications, as this is changing.

## Sources
- [Data, Privacy, and Security for Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy) — fetched 2026-06-28 — supports: no-training commitment, EU Data Boundary, Advanced Data Residency, service boundary, entitlement honoring, Entra isolation, certifications (GDPR/ISO 27001/27018/42001/HIPAA), Anthropic-out-of-EUDB caveat; confidence: high.
- [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot) — fetched 2026-06-28 — supports: Purview audit/eDiscovery/retention/DLP/Communication Compliance/Insider Risk/sensitivity labels/DSPM-for-AI, oversharing risk assessment, Copilot interactions in unified audit log + mailbox; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected ownership independent->public (Microsoft Corporation, NASDAQ: MSFT, high confidence); documented governance posture from two learn.microsoft.com primary sources — no-training commitment, EU Data Boundary/Advanced Data Residency, Graph entitlement-aware retrieval + oversharing risk, full Purview integration (audit/eDiscovery/retention/DLP/Communication Compliance/Insider Risk/DSPM-for-AI), Entra isolation, ISO 42001/27001/27018/GDPR/HIPAA certs; flagged Anthropic-models-out-of-EUDB caveat; set status researched, hedge_fund_fit high, trifecta_relevance sensitive-data. No HARD contradictions.
