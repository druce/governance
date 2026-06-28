---
type: vendor
name: Amazon Q Business
slug: amazon-q-business
categories: [enterprise-ai-assistant, entitlement-aware-rag]
layer: ux
aliases: [Amazon Q, AWS Q Business, Q Business]
website: https://aws.amazon.com/q/business/
founded: 2023
hq: Seattle, WA, USA
ownership: public
ownership_detail: "Product of Amazon Web Services (Amazon.com, Inc., NASDAQ: AMZN)"
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 4
last_updated: 2026-06-28
tags: [aws, enterprise-assistant, rag, generative-ai]
---

# Amazon Q Business

**One-liner** — AWS's managed enterprise AI assistant: a generative-AI chat/RAG layer over your enterprise content, with retrieval that honors each user's existing source-system permissions and a contractual no-training commitment, delivered as a SaaS service inside your AWS account boundary.

**Categories** — [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) (primary), [entitlement-aware-rag](../categories/entitlement-aware-rag.md)

## What it does

Amazon Q Business is a fully managed generative-AI assistant for the workforce. Employees ask questions in natural language and get synthesized answers, summaries, and actions grounded in the company's own documents and applications — wikis, file shares, ticketing, CRM, email, and 40+ connectors. It is AWS's answer to Microsoft 365 Copilot, [gemini-enterprise](gemini-enterprise.md), [glean](glean.md), and [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md). The draw for an AWS-centric shop is that the index, the retrieval, and the model inference all run as an AWS service governed by IAM, CloudTrail, and AWS's compliance envelope, rather than a third-party SaaS you have to onboard through vendor risk from scratch.

## Where it sits in the stack

UX layer — the chatbot people actually use ([enterprise-ai-assistant](../categories/enterprise-ai-assistant.md)) — but its defining governance feature is entitlement-aware retrieval ([entitlement-aware-rag](../categories/entitlement-aware-rag.md)), so it spans both. Lethal-trifecta role: its main exposure is the **sensitive-data** leg — it ingests and surfaces internal documents, so the controls that matter are (a) not leaking content to a user who shouldn't see it, and (b) not leaking content to a model trainer. Q Business's permission-aware retrieval and no-training stance are aimed squarely at both. It is not a network/egress control and not an untrusted-input firewall; pair it with [ai-access-governance](../categories/ai-access-governance.md) / [dlp](../categories/dlp.md) for shadow-AI and exfiltration concerns.

## Deployment & architecture

- **SaaS, in-account.** A managed AWS service (no servers to run); you create a Q Business *application*, attach data sources, and expose a web experience or embed via API.
- **Identity / SSO.** Authenticates workforce users through **AWS IAM Identity Center**, which federates to an external IdP (Okta, Microsoft Entra ID, Ping) via SAML/OIDC and supports **SCIM** user/group provisioning. Newer setups use **trusted identity propagation** so the end user's identity flows through to the data layer for authorization. An IAM-federation path also exists for apps not using Identity Center.
- **Entitlement-aware retrieval (ACL crawling).** Connectors crawl each source's access-control lists at the document level and store principal info (users, local and federated groups) in the Amazon Q Business **User Store**. At query time the assistant filters responses to documents the asking user is actually permitted to read. ACL/identity crawling is on by default for supported connectors; once enabled it **cannot be turned off** (a deliberate safety default). This is the feature that lets it be deployed over sensitive shares without becoming a leak engine — the same problem Copilot's "oversharing" controversy raised.
- **Admin controls / guardrails.** Admin console with global and topic-level **guardrails** (blocked words/topics, response controls), data-source scoping, and Amazon Q Apps governance.
- **Encryption.** TLS 1.2+ in transit (1.3 recommended); encryption at rest with AWS-owned or customer-managed KMS keys.
- **Audit / logging.** API and user-activity logging via **AWS CloudTrail**; integrates with the broader AWS security tooling (Macie, CloudWatch). Conversation data is retrievable via the Q Business API, which is the hook for any archival/export pipeline.

## Positioning & differentiators

- **No-training commitment (the headline for a CTO).** Per AWS docs: *"Amazon Q Business does not use customer data for service improvement or for improving underlying LLMs."* Unambiguous and primary-sourced.
- **Native permission-aware RAG.** Unlike a bare ChatGPT/Claude deployment where you bolt on retrieval, Q Business's connectors enforce source ACLs out of the box — its closest peers here are [glean](glean.md) and [microsoft-365-copilot](microsoft-365-copilot.md) (Graph), not the raw frontier-model assistants.
- **AWS compliance envelope.** Q Business itself is attested for HIPAA (HIPAA-eligible since Oct 2024), SOC 1/2/3, PCI, and **ISO 42001** (the AI-management-system standard — relatively rare and notable). It rides AWS's broader SOC/ISO 27001/FedRAMP posture.
- **Tradeoff vs. frontier assistants.** Buyers generally rate its raw answer quality and model choice below ChatGPT Enterprise / Claude Enterprise; the value is governance and AWS-native integration, not best-in-class reasoning. Model is AWS-selected (Bedrock-family), not user-pickable to the same degree.

## Ownership, funding & M&A

Amazon Q Business is a product of **Amazon Web Services**, a segment of **Amazon.com, Inc.** (NASDAQ: **AMZN**), a public company. Launched at AWS re:Invent (announced Nov 2023, general availability 2024). No standalone funding or M&A — corrected from the stub, which incorrectly listed `independent`. Ownership confidence: **high**.

## CTO / hedge-fund lens

- **Day-1** if the firm is already AWS-centric and wants an internal assistant grounded in its own content without standing up third-party SaaS or a self-built RAG stack. The IAM/CloudTrail/KMS familiarity shortens the security review.
- **No-training + in-account + permission-aware retrieval** is a clean story for an investment firm worried about MNPI/research leaking into a model or across Chinese walls. The ACL-honoring retrieval is the control that maps to information-barrier requirements.
- **SR 11-7 / model risk:** Q Business is a productivity assistant, not a model that prices or trades, so it's largely outside core model-risk scope — but its outputs informing analysts may fall under your AI governance policy; log usage via CloudTrail and govern it through [ai-governance-platform](../categories/ai-governance-platform.md) / [enterprise-grc](../categories/enterprise-grc.md).
- **Comms surveillance / eDiscovery gap (verify).** Conversations are accessible via API, but Q Business is **not** a purpose-built comms-surveillance archive. A regulated fund treating the assistant as a monitored communications channel (MAR/MNPI, SEC/FINRA books-and-records) would need to build export into an archive and feed a [comms-surveillance](../categories/comms-surveillance.md) tool ([behavox](behavox.md), [steeleye](steeleye.md), [theta-lake](theta-lake.md)); native retention/legal-hold controls for chat are limited. Treat this as an open item, not a solved one.
- **Fit:** strongest for mid/large AWS shops; a 50-person fund with no AWS footprint gets a simpler path from ChatGPT Enterprise, Claude Enterprise, or Glean. Hence **medium** fit overall.

## Competitors / alternatives

[microsoft-365-copilot](microsoft-365-copilot.md), [gemini-enterprise](gemini-enterprise.md), [glean](glean.md), [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md), [anthropic-claude-enterprise](anthropic-claude-enterprise.md), [perplexity-enterprise](perplexity-enterprise.md). For the permission-aware-RAG dimension specifically: [glean](glean.md), [microsoft-graph](microsoft-graph.md), [knostic](knostic.md).

## Open questions / to verify

- Exact list of AWS Regions where Amazon Q Business is GA (check the AWS Regional Services List); commercial vs GovCloud (US) scope for FedRAMP.
- Native conversation **retention / legal-hold / eDiscovery** controls and whether a supported export path to comms-surveillance archives exists — current read is "API access yes, purpose-built retention no."
- Whether GDPR DPA terms and data-residency guarantees pin processing to the selected Region with no cross-region inference fan-out by default (cross-region inference is a documented feature — confirm default and opt-out).
- Degree of model choice / Bedrock model selection exposed to admins.

## Sources

- [Amazon Q Business Service improvement](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/service-improvement.html) — fetched 2026-06-28 — supports: no-training commitment ("does not use customer data for service improvement or for improving underlying LLMs"); confidence: high
- [Data protection in Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-protection.html) — fetched 2026-06-28 — supports: shared-responsibility model, TLS 1.2+, CloudTrail user/API logging, KMS encryption, GDPR center, IAM Identity Center; confidence: high
- [Compliance validation for Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/compliance-validation.html) — fetched 2026-06-28 — supports: HIPAA, SOC 1/2/3, PCI, ISO 42001 attestation; confidence: high
- [Enable or disable ACL crawling safely in Amazon Q Business (AWS ML Blog) + connector concepts docs](https://aws.amazon.com/blogs/machine-learning/enable-or-disable-acl-crawling-safely-in-amazon-q-business/) — fetched 2026-06-28 — supports: entitlement-aware retrieval, ACL/identity crawling into User Store, query-time filtering by user permissions, irreversible-once-enabled; confidence: high
- [Amazon Q Business is now HIPAA eligible (AWS What's New, 2024-10)](https://aws.amazon.com/about-aws/whats-new/2024/10/amazon-q-business-hipaa-eligible/) — fetched 2026-06-28 (via search) — supports: HIPAA eligibility date; confidence: med

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected ownership independent->public (AWS / Amazon.com, NASDAQ: AMZN, high confidence). Established no-training commitment (primary doc), entitlement-aware ACL-crawling retrieval via connectors + IAM Identity Center/SCIM/trusted identity propagation, CloudTrail audit logging, TLS/KMS encryption, and compliance attestations (HIPAA-eligible, SOC 1/2/3, PCI, ISO 42001). Added entitlement-aware-rag as secondary category. Flagged comms-surveillance/eDiscovery retention as an open gap for regulated funds. Set hedge_fund_fit medium, confidence medium.
