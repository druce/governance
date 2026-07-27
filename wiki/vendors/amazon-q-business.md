---
title: Amazon Q Business
type: vendor
name: Amazon Q Business
slug: amazon-q-business
aka: [Amazon Q, AWS Q Business, Q Business]
primary_category: enterprise-ai-assistant
also_listed_in: [entitlement-aware-rag]
website: https://aws.amazon.com/q/business/
founded: 2023
hq: Seattle, WA, USA
ownership_state: public
owner: Amazon Web Services
ownership_note: 'Product of Amazon Web Services (Amazon.com, Inc., NASDAQ: AMZN). Closed to new customers as of 2026-07-30; maintenance mode (bug fixes and security updates only, no new features) for existing customers, with no announced end-of-service date. AWS directs new and migrating customers to Amazon Quick.'
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
last_verified: 2026-07-27
verify_after: 2027-01-31
tags: [aws, enterprise-assistant, rag, generative-ai, maintenance-mode, closed-to-new-customers]
---

# Amazon Q Business

**One-liner** — AWS's managed enterprise AI assistant: a generative-AI chat/RAG layer over your enterprise content, with retrieval that honors each user's existing source-system permissions and a contractual no-training commitment, delivered as a SaaS service inside your AWS account boundary.

**Categories** — [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) (primary), [entitlement-aware-rag](../categories/entitlement-aware-rag.md)

## Product status — closed to new customers (2026-07-30)

**You can no longer buy this.** AWS's product page carries an End of Support Notice: *"Amazon Q Business will no longer be open to new customers starting on July 30, 2026. If you would like to use the service, please sign up prior to July 30, 2026."* The AWS docs banner gives the same instruction with the date stated as July 31 — a one-day discrepancy in AWS's own copy; both agree that sign-up must happen **before 2026-07-30**.

For existing customers, per AWS: *"Amazon Q Business remains fully supported and AWS will continue to provide bug fixes and security updates for existing customers, however new feature requests will no longer be considered."* That is maintenance mode. **No end-of-service or shutdown date has been announced** — treat retirement timing as unknown, not as indefinite.

AWS's recommended path is **Amazon Quick**, which it calls *"the next evolution of Amazon Q Business."* Read that phrase as positioning, not as a rename — see [Amazon Quick: what it actually is](#amazon-quick-what-it-actually-is) below. The rest of this page describes a product that remains in production at existing customers and still needs to be governed; it is no longer a shortlist candidate.

## What it does

Amazon Q Business is a fully managed generative-AI assistant for the workforce. Employees ask questions in natural language and get synthesized answers, summaries, and actions grounded in the company's own documents and applications — wikis, file shares, ticketing, CRM, email, and 40+ connectors. It is AWS's answer to Microsoft 365 Copilot, [gemini-enterprise](gemini-enterprise.md), [glean](glean.md), and [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md). The draw for an AWS-centric shop is that the index, the retrieval, and the model inference all run as an AWS service governed by IAM, CloudTrail, and AWS's compliance envelope, rather than a third-party SaaS you have to onboard through vendor risk from scratch.

## Where it sits in the stack

UX layer — the chatbot people actually use ([enterprise-ai-assistant](../categories/enterprise-ai-assistant.md)) — but its defining governance feature is entitlement-aware retrieval ([entitlement-aware-rag](../categories/entitlement-aware-rag.md)), so it spans both. Its main risk exposure is **sensitive data** — it ingests and surfaces internal documents, so the controls that matter are (a) not leaking content to a user who shouldn't see it, and (b) not leaking content to a model trainer. Q Business's permission-aware retrieval and no-training stance are aimed squarely at both. It is not a network/egress control and not an untrusted-input firewall; pair it with [ai-access-governance](../categories/ai-access-governance.md) / [dlp](../categories/dlp.md) for shadow-AI and exfiltration concerns.

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

As of 2026-07-30 all of the above is **retrospective**. `market_position` stays `null`: none of the SCHEMA.md §3.3 labels (leader / challenger / legacy-incumbent / platform-module / oss-default / niche-specialist / ai-native-disruptor) honestly describes a product withdrawn from sale, and the rule requires justifying the label in a sentence — which cannot be done here without misleading. Stated here rather than left as a silent null.

## Amazon Quick: what it actually is

**A capability merge, not a rename** — the same call this wiki made for Dev Box → Windows 365. AWS's migration guide says *"Amazon Quick represents the next evolution of Amazon Q Business,"* but that sentence is positioning aimed at the Q Business reader. Quick is the **QuickSight service lineage** with Q Business's use cases folded into it:

- AWS announced on **2025-10-09** that Amazon QuickSight (its BI product, GA since 2016) "evolves to **Amazon Quick Suite**" — the existing BI engine plus new generative features (Quick Research, Quick Flows, Quick Automate, Quick Index, Quick Chat). By the **2026-04-28** "What's Next with AWS" event AWS uses the plain name **Amazon Quick**; the "Suite" suffix has been dropped from its 2026 copy.
- The plumbing confirms the lineage. Quick setup asks you to pick a Region for *"initial data storage capacity, called **SPICE**"* — QuickSight's engine. AWS's own migration script calls `boto3.client('quicksight')` and `quicksight.update_folder_permissions` against `arn:aws:quicksight:…` principals: the Quick control plane **is** the QuickSight API. Quick appears in the console under **Analytics**. Q Business's non-IDC auth mode is even named `AWS_QUICKSIGHT_IDP`.

So Quick's scope is materially wider than Q Business's — BI dashboards, workflow automation, and agentic research alongside enterprise-content Q&A — and its slug is not this vendor's slug. **"Amazon Quick" was deliberately not added to `aka`**: adding it would wrongly assert that the two names denote the same buying unit. (A separate `amazon-quick` page is a reasonable future addition; not created here to keep this change one vendor wide.)

Capabilities AWS lists for Quick: Quick Sight (visualization), Flows (workflow automation), Automate (multi-step process automation), Research (cited research over enterprise and public data), Spaces (unified files/dashboards/knowledge bases), Apps, Quick Index, plus mobile and desktop apps. Named connectors include Slack, Teams, Outlook, Google Workspace, Zoom, Airtable and Dropbox. Note the licensing gate: **creating knowledge bases and action connectors requires the Enterprise subscription**; Professional users can only consume what has been shared with them.

> Do not conflate with **Amazon Q Developer**, the IDE coding assistant, which AWS is separately sunsetting in **2027** in favour of **Kiro**. Different product, different successor, different timeline.

### Migration path (BYOI) and its governance regressions

AWS's recommended on-ramp is **BYOI (Bring Your Own Index)** — attach the existing Q Business index to Quick as a knowledge base, non-destructively, while Q Business keeps running in parallel. Index and Quick instance must be in the **same AWS account and Region**. Limits: **max two Q Business indexes per Region (quota not increasable)**, and once selected an index **cannot be unselected**. Customers using anonymous access or API integration into custom apps are told to contact AWS Support — there is no documented self-serve path for them.

The regressions below are AWS's own documented gaps, and they land squarely on the properties that earned this page its [entitlement-aware-rag](../categories/entitlement-aware-rag.md) tag. A firm migrating should treat them as a security review, not a lift-and-shift:

- **Guardrails do not transfer.** Q Business global and topic-level controls, and Actions, are *"explicitly excluded from the BYOI capability."* Content filtering and blocked topics must be rebuilt in Quick, and AWS warns that guardrails configured in Q Business will not apply through BYOI.
- **The User Store has no equivalent.** *"In Quick, user management operates at the knowledge base level rather than through a centralized user store."*
- **Non-IDC mode loses per-user entitlement outright.** *"In a non-IDC implementation, all Amazon Quick users automatically receive access to connected Q Business indexes… you lose the per-user and per-group access distinctions that Q Business enforced at the index level."* The documented workaround is to shard content into role-scoped knowledge bases and script permissions per knowledge base in Spaces. **Under IAM Identity Center (IDC) entitlement is preserved** — access is granted only to users who had access to the index. For a firm relying on this product to hold information barriers, the IdP choice is therefore a **security decision, not a convenience one**.
- **Document-level ACLs cover fewer connectors.** Quick supports document-level ACLs for **S3, Confluence Cloud, SharePoint and Google Drive** only, versus Q Business's broader connector-side ACL crawling; elsewhere AWS again recommends per-role knowledge bases. As in Q Business, ACLs must be enabled at creation and the setting is permanent.
- **One improvement:** Quick's ingest default is stricter — it *"does not ingest documents that lack an associated ACL entry,"* whereas Q Business granted all users access to S3 prefixes absent from the ACL file. Migrators must give every document an explicit ACL entry first or silently lose content.
- **Q Apps must be hand-rebuilt as Quick Flows** (excluded from BYOI); form-based Q Apps have no equivalent yet.
- **Connectors without a native Quick equivalent are bridged via MCP**, with Quick as MCP client. Caveats: fixed 60-second timeout (HTTP 424 on exceed), no custom HTTP headers, static tool lists, no step-up authorization, and **MCP integrations cannot back a knowledge base** — actions only.

## Ownership, funding & M&A

Amazon Q Business is a product of **Amazon Web Services**, a segment of **Amazon.com, Inc.** (NASDAQ: **AMZN**), a public company. Launched at AWS re:Invent (announced Nov 2023, general availability 2024). No standalone funding or M&A — corrected from the stub, which incorrectly listed `independent`. Ownership confidence: **high**.

## CTO / hedge-fund lens

**If you are evaluating now — you can't buy this.** Sign-up closes 2026-07-30. An AWS-centric firm that wanted this shape of product should evaluate **Amazon Quick**, budgeting for the Enterprise subscription (Professional cannot create knowledge bases or connectors) and treating the entitlement model as the thing to test first, not the answer quality. If the firm is not committed to AWS, the closure removes the main reason to prefer this lineage at all, and [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md), [anthropic-claude-enterprise](anthropic-claude-enterprise.md), [glean](glean.md) or [microsoft-365-copilot](microsoft-365-copilot.md) are cleaner paths.

**If you already run Q Business.** Nothing breaks and there is no announced end date, so this is Day-2 work, not a fire drill — but it is now a **frozen** dependency receiving only bug fixes and security updates, so plan the migration on your own schedule rather than AWS's. Three things to get right:

- **Do the BYOI attach early** — it is non-destructive and runs in parallel, so it is a cheap way to size the gap before committing.
- **Insist on IAM Identity Center.** This is the single highest-stakes item in the migration. On the non-IDC path Quick grants *every* Quick user access to connected indexes, which would collapse exactly the per-user entitlement that justified deploying an assistant over sensitive research and deal material. A firm with Chinese-wall obligations should treat a non-IDC migration as a control failure, not a configuration preference.
- **Re-derive your guardrails and ACL coverage.** Topic controls do not carry over, the User Store has no equivalent, and document-level ACLs cover only four connectors. Re-run the information-barrier review against the Quick deployment rather than assuming the Q Business posture is inherited.

**Still true, and unchanged by the closure.** The no-training commitment, in-account processing, and permission-aware retrieval remain the reason this product was worth listing, and the underlying thesis — an assistant that honors source-system ACLs so it doesn't become a leak engine — is unchanged; only the SKU moved. Firms should confirm the equivalent no-training commitment for Quick directly (see open questions) rather than assuming it transfers.

- **SR 11-7 / model risk:** Q Business is a productivity assistant, not a model that prices or trades, so it's largely outside core model-risk scope — but its outputs informing analysts may fall under your AI governance policy; log usage via CloudTrail and govern it through [ai-governance-platform](../categories/ai-governance-platform.md) / [enterprise-grc](../categories/enterprise-grc.md). A migration to Quick is a change of system-of-record for that policy and should be logged as one.
- **Comms surveillance / eDiscovery gap (verify).** Conversations are accessible via API, but Q Business is **not** a purpose-built comms-surveillance archive. A regulated fund treating the assistant as a monitored communications channel (MAR/MNPI, SEC/FINRA books-and-records) would need to build export into an archive and feed a [comms-surveillance](../categories/comms-surveillance.md) tool ([behavox](behavox.md), [steeleye](steeleye.md), [theta-lake](theta-lake.md)); native retention/legal-hold controls for chat are limited. Treat this as an open item, not a solved one — and note that any export pipeline built against the Q Business API will need rebuilding against Quick.
- **Fit:** **medium** for an existing AWS-centric estate that must now manage a migration; effectively **not applicable** for a new evaluation, since the product cannot be purchased.

## Competitors / alternatives

[microsoft-365-copilot](microsoft-365-copilot.md), [gemini-enterprise](gemini-enterprise.md), [glean](glean.md), [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md), [anthropic-claude-enterprise](anthropic-claude-enterprise.md), [perplexity-enterprise](perplexity-enterprise.md). For the permission-aware-RAG dimension specifically: [glean](glean.md), [microsoft-graph](microsoft-graph.md), [knostic](knostic.md).

## Open questions / to verify

- Exact list of AWS Regions where Amazon Q Business is GA (check the AWS Regional Services List); commercial vs GovCloud (US) scope for FedRAMP.
- Native conversation **retention / legal-hold / eDiscovery** controls and whether a supported export path to comms-surveillance archives exists — current read is "API access yes, purpose-built retention no."
- Whether GDPR DPA terms and data-residency guarantees pin processing to the selected Region with no cross-region inference fan-out by default (cross-region inference is a documented feature — confirm default and opt-out).
- Degree of model choice / Bedrock model selection exposed to admins.
- **Does the no-training commitment carry over to Amazon Quick?** The primary-sourced *"does not use customer data for service improvement or for improving underlying LLMs"* language is a Q Business doc. The equivalent Quick commitment has **not** been verified here — it is the first thing to confirm before a migration, not an assumption.
- **Whether an end-of-service date for existing Q Business customers gets announced.** None exists as of 2026-07-27; `verify_after` set to 2027-01-31 to re-check.
- Whether Quick inherits Q Business's compliance attestations (HIPAA eligibility, ISO 42001, SOC/PCI) or carries QuickSight's — the two lineages had different attestation sets and the merged product's scope is unconfirmed.
- Whether Quick document-level ACL support expands beyond S3 / Confluence Cloud / SharePoint / Google Drive, which would materially reduce migration effort for firms on other connectors.

## Sources

- [Amazon Q Business Service improvement](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/service-improvement.html) — fetched 2026-06-28 — supports: no-training commitment ("does not use customer data for service improvement or for improving underlying LLMs"); confidence: high
- [Data protection in Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-protection.html) — fetched 2026-06-28 — supports: shared-responsibility model, TLS 1.2+, CloudTrail user/API logging, KMS encryption, GDPR center, IAM Identity Center; confidence: high
- [Compliance validation for Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/compliance-validation.html) — fetched 2026-06-28 — supports: HIPAA, SOC 1/2/3, PCI, ISO 42001 attestation; confidence: high
- [Enable or disable ACL crawling safely in Amazon Q Business (AWS ML Blog) + connector concepts docs](https://aws.amazon.com/blogs/machine-learning/enable-or-disable-acl-crawling-safely-in-amazon-q-business/) — fetched 2026-06-28 — supports: entitlement-aware retrieval, ACL/identity crawling into User Store, query-time filtering by user permissions, irreversible-once-enabled; confidence: high
- [Amazon Q Business is now HIPAA eligible (AWS What's New, 2024-10)](https://aws.amazon.com/about-aws/whats-new/2024/10/amazon-q-business-hipaa-eligible/) — fetched 2026-06-28 (via search) — supports: HIPAA eligibility date; confidence: med
- [Amazon Q Business availability change + migration guide (AWS docs)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html) — fetched 2026-07-27 — supports: closure to new customers, maintenance-mode language for existing customers, absence of an end-of-service date, BYOI migration path and its quotas, guardrail/User Store/non-IDC entitlement/document-ACL regressions, MCP bridging limits, Q Apps → Quick Flows; confidence: high
- [Amazon Q Business product page — End of Support Notice](https://aws.amazon.com/q/business/) — fetched 2026-07-27 — supports: verbatim closure notice and the 2026-07-30 date; confidence: high
- [Reimagine business intelligence: Amazon QuickSight evolves to Amazon Quick Suite (AWS BI Blog, 2025-10-09)](https://aws.amazon.com/blogs/business-intelligence/reimagine-business-intelligence-amazon-quicksight-evolves-to-amazon-quick-suite/) — fetched 2026-07-27 — supports: Quick's QuickSight lineage and 2025-10-09 rebrand, component names, that this is an evolution of QuickSight rather than of Q Business; confidence: high
- [AWS Weekly Roundup: What's Next with AWS 2026, Amazon Quick… (2026-05-04)](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-whats-next-with-aws-2026-amazon-quick-openai-partnership-and-more-may-4-2026/) — fetched 2026-07-27 — supports: 2026-04-28 launch event, "Amazon Quick" as the current name without the "Suite" suffix, connector list, separate Amazon Q Developer → Kiro sunset in 2027; confidence: high
- Cached: `raw/sources/2026-07-27--amazon-q-business--amazon-quick-transition.md`

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected ownership independent->public (AWS / Amazon.com, NASDAQ: AMZN, high confidence). Established no-training commitment (primary doc), entitlement-aware ACL-crawling retrieval via connectors + IAM Identity Center/SCIM/trusted identity propagation, CloudTrail audit logging, TLS/KMS encryption, and compliance attestations (HIPAA-eligible, SOC 1/2/3, PCI, ISO 42001). Added entitlement-aware-rag as secondary category. Flagged comms-surveillance/eDiscovery retention as an open gap for regulated funds. Set hedge_fund_fit medium, confidence medium.
- [2025-10-09] Amazon **QuickSight** rebranded to **Amazon Quick Suite** — the BI engine plus new generative capabilities (Quick Research, Flows, Automate, Index, Chat). This is the lineage Q Business is later folded into. (Date of the event, recorded here 2026-07-27.)
- [2026-04-28] **Amazon Quick** featured at "What's Next with AWS"; the "Suite" suffix drops from AWS's copy and the product picks up desktop/mobile apps, autonomous agents and expanded connectors. (Recorded here 2026-07-27.)
- [2026-07-30] **Closed to new customers.** AWS stopped accepting new Q Business sign-ups; existing customers continue on maintenance-only support (bug fixes and security updates, no new features) with **no announced end-of-service date**. AWS directs prospects and migrators to Amazon Quick. (AWS's docs banner states the date as July 31 while the product page states July 30; both instruct sign-up before July 30. Recorded here 2026-07-27, three days ahead of the date.)
- [2026-07-27] Researched; confirmed the closure from two AWS primary sources (product page notice + docs availability-change/migration guide). `last_verified` → 2026-07-27; `verify_after` 2027-01-31 to re-check for an announced end-of-service date. `ownership_state` unchanged (`public`) — this is an internal product sunset, not M&A; detail added to `ownership_note`, and `maintenance-mode` / `closed-to-new-customers` tags added (following the `helicone` and `azure-dev-boxes` precedent of tagging frozen status rather than overloading `ownership_state`). **"Amazon Quick" deliberately NOT added to `aka`** — Quick is the QuickSight service lineage (SPICE, the `quicksight` API namespace, console under Analytics, `AWS_QUICKSIGHT_IDP`) with Q Business's use cases merged in, so it is a capability merge across a wider scope, not a rename; same call as Dev Box → Windows 365. `market_position` stays `null` with the reason stated on the page — no schema label honestly describes a product withdrawn from sale. Body re-cut around buying-relevance: page now leads with the closure, adds an "Amazon Quick: what it actually is" section documenting the BYOI migration path and, most importantly for this wiki's [entitlement-aware-rag](../categories/entitlement-aware-rag.md) framing, AWS's own documented entitlement regressions in the successor (non-IDC mode grants all Quick users access to connected indexes; guardrails and User Store do not transfer; document-level ACLs cover only four connectors). CTO lens split into new-evaluation / existing-estate.
