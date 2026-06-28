---
type: vendor
name: Gemini Enterprise / Agentspace (Google)
slug: gemini-enterprise
categories: [enterprise-ai-assistant, entitlement-aware-rag]
layer: ux
aliases: [Google Agentspace, Gemini Enterprise app, Gemini for Google Cloud, Gemini Enterprise Standard, Gemini Enterprise Plus]
website: "https://cloud.google.com/gemini-enterprise"
founded:
hq: Mountain View, California, USA
ownership: public
ownership_detail: "Product of Google LLC / Alphabet Inc. (NASDAQ: GOOGL/GOOG)"
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [google, alphabet, gcp, workspace, enterprise-search, rag, agents]
---

# Gemini Enterprise / Agentspace (Google)

**One-liner** — Google's enterprise AI front door: a governed chat + enterprise-search + agent platform that grounds Gemini models on your company's data (Workspace, Drive, plus third-party connectors) while honoring source permissions, with the data-residency, no-training and audit controls a regulated buyer expects from Google Cloud.

**Categories** — [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) (primary), [entitlement-aware-rag](../categories/entitlement-aware-rag.md)

> **Naming / rebrand (2025-10-09):** Google folded **Google Agentspace** into **Gemini Enterprise** (announced around the "Gemini at Work"/Google Cloud event). The Agentspace URL now redirects to Gemini Enterprise; existing Agentspace customers continue uninterrupted, but **Agentspace is closed to new subscriptions from 2025-12-31**. "Agentspace" survives as the underlying agent-platform/orchestration tech ("Gemini Enterprise Agent Platform" in the docs). Sold as **Gemini Enterprise Standard** and **Gemini Enterprise Plus**, with **NotebookLM Enterprise** as a related SKU. Distinguish from **Gemini for Google Workspace** (the assistant embedded in Gmail/Docs/Meet) and the consumer **Gemini app** — governance behavior differs by surface (see Vault note below).

## What it does

Three jobs in one product:

1. **Enterprise assistant** — a Gemini-powered chat UI employees actually use, with ready-made agents (Deep Research, NotebookLM, coding agents).
2. **Entitlement-aware enterprise search / RAG** — connectors ingest content **and its ACLs** from sources (Google Drive/Workspace plus third-party systems like SharePoint, Jira, ServiceNow, Confluence), so answers are grounded only on documents the querying user is actually allowed to see.
3. **Agent platform** — build, deploy and run agents (the former Agentspace), with a no-code agent builder and support for custom/partner agents.

For a hedge fund the draw is that it sits natively on top of Google Workspace if that's your stack, and inherits Google Cloud's compliance and data-governance posture.

## Where it sits in the stack

UX layer — the [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) people interact with — riding on a [entitlement-aware-rag](../categories/entitlement-aware-rag.md) retrieval layer. It pulls from [google-drive](google-drive.md) / Workspace and other [content-sources](../categories/content-sources.md). Lethal-trifecta role: its main job is to control the **sensitive-data** leg — retrieval is permission-filtered so the model never grounds on data the user can't see. It does **not** by itself break the untrusted-input or egress legs; pair it with [ai-runtime-security](../categories/ai-runtime-security.md) / [ai-access-governance](../categories/ai-access-governance.md) for those. Trust zone: handles green/yellow-zone enterprise data under enterprise controls.

## Deployment & architecture

- **SaaS** on Google Cloud. No inline proxy/agent to deploy; consumed as a managed app + APIs.
- **Connectors & data stores** convert each source into a standardized Document (content + metadata + ACLs) held in data stores; retrieval is filtered by the user's identity at query time.
- **Identity:** Google Identity is required for Workspace connectors (Drive, Gmail, Chat, Calendar), which delegate ACL decisions to the native Workspace platform. For third-party sources you can use **Workforce Identity Federation** to authenticate via external IdPs (**Entra ID, Okta, Ping**) over OIDC/SAML 2.0 — syncless. ACL enforcement uses either **Pure ACLs** (email-based identities) or **Identity Mapping** (usernames/legacy/external IDs).
- **Admin & audit:** managed via Google Cloud / Workspace admin consoles. Cloud Audit Logs (immutable) for the Cloud product; Gemini audit logs in Workspace are exposed via the Reporting API (Admin SDK) and surface in the security/audit investigation tools.
- **Security controls:** VPC Service Controls, CMEK via Cloud KMS (US/EU multi-region APIs only), Access Transparency (not in the `global` region).

## Positioning & differentiators

- **Native to Google Workspace.** If your firm runs on Gmail/Drive, the entitlement-aware grounding is largely "free" because it reuses Workspace permissions — analogous to [microsoft-365-copilot](microsoft-365-copilot.md) on M365 + [microsoft-graph](microsoft-graph.md). The cross-cloud parallel is [glean](glean.md) (best-of-breed connectors/search) and [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md) / [anthropic-claude-enterprise](anthropic-claude-enterprise.md) (model-led assistants with thinner native connector graphs).
- **Agent platform inheritance.** Carries Agentspace's agent builder/orchestration, which positions it more as a build-and-run agent platform than a pure chatbot.
- **Cloud-grade governance.** Data residency zones, no-training commitments, broad certifications, Vault/eDiscovery integration — see below.

## Data governance posture (the part a hedge-fund CTO cares about)

- **No training on your data.** "Gemini doesn't use your prompts or its responses as data to train its models." On the Gemini Enterprise Agent Platform, "Google won't use your data to train or fine-tune any AI/ML models without your prior permission or instruction" (incl. GA and pre-GA models). Prompts handled under the Cloud Data Processing Addendum (CDPA), encrypted in transit.
- **Data residency (DRZ).** At-rest residency in multi-regions `us` and `eu`, plus in-country `ca` (Canada) and `in` (India) (GA with allowlist). ML processing (training/prediction/tuning) stays in the `us` or `eu` multi-region matching the regional API used. Caveat: "Grounding with Google Search" and "dynamic facets" run only in the `global` region, where DRZ/CMEK/Access Transparency don't apply — so residency holds only if you avoid those features.
- **Encryption:** CMEK via Cloud KMS (US/EU multi-region APIs only; not in in-country or `global` regions).
- **Certifications (Gemini Enterprise Standard/Plus + NotebookLM Enterprise):** SOC 1/2/3, ISO/IEC 27001, 27017, 27018, 27701, PCI DSS, BSI C5:2020, HIPAA, FedRAMP; **ISO/IEC 42001** (AI management system) awarded May 2025 to Gemini for Google Cloud / Vertex AI Agents / Code Assist. (Confirm exact FedRAMP level and per-SKU scope on Google Cloud's compliance pages before relying on it.) GDPR addressed via the CDPA/DPA.
- **Vault / eDiscovery / retention (comms surveillance angle).** Google Vault supports the **Gemini app** for search/export of prompts & responses (since 2025-02), and as of **2026-06** supports **retention rules and litigation holds** for the Gemini app (Vault holds take precedence over admin/user settings). Important caveat: this covers the standalone Gemini app; "Gemini in Workspace" features embedded in other apps (e.g., "Help me write" in Gmail/Docs) are **not** retained the same way — a gap to probe if you need full comms-surveillance capture ([comms-surveillance](../categories/comms-surveillance.md)).

## Ownership, funding & M&A

**Public.** Gemini Enterprise is a product of **Google LLC**, part of **Alphabet Inc.** (NASDAQ: GOOGL/GOOG). The prior stub incorrectly marked it `independent`; corrected to `public`, confidence **high**. No standalone funding/valuation (it's a line of business, not a separate entity). The only "M&A-like" event here is internal: the **Agentspace → Gemini Enterprise** product consolidation (2025-10-09), not an acquisition.

## CTO / hedge-fund lens

- **Day-1** for the assistant/RAG slot **if you're a Google Workspace shop** — the entitlement-aware grounding reuses permissions you already manage, which is the hard part of safe RAG. If you're on Microsoft, [microsoft-365-copilot](microsoft-365-copilot.md) is the natural default and this becomes a comparison candidate rather than the obvious pick.
- **Governance fit is strong:** no-training, residency zones, CMEK, broad certs incl. ISO 42001, and Vault-based eDiscovery/holds map well onto regulated/asset-manager requirements. ISO 42001 + model documentation can feed an SR 11-7 / model-risk file, though Gemini Enterprise is an *assistant*, not a model-risk governance tool ([ai-governance-platform](../categories/ai-governance-platform.md)).
- **Watch-outs:** (1) residency only holds if you avoid `global`-only features like Google Search grounding; (2) Vault capture gaps for embedded "Gemini in Workspace" actions vs the standalone app — material for MNPI/comms surveillance; (3) you still need [ai-runtime-security](../categories/ai-runtime-security.md) / [ai-access-governance](../categories/ai-access-governance.md) for prompt-injection and shadow-AI — this product governs *its own* data access, not all AI traffic.
- **Fit:** mid-to-large regulated shops already on Google Workspace/Cloud. A small Microsoft-centric fund gets less value.

## Competitors / alternatives

[microsoft-365-copilot](microsoft-365-copilot.md) · [openai-chatgpt-enterprise](openai-chatgpt-enterprise.md) · [anthropic-claude-enterprise](anthropic-claude-enterprise.md) · [glean](glean.md) · [amazon-q-business](amazon-q-business.md) · [perplexity-enterprise](perplexity-enterprise.md). On the retrieval/entitlement axis specifically: [glean](glean.md), [microsoft-graph](microsoft-graph.md), [knostic](knostic.md).

## Open questions / to verify
- Exact **FedRAMP level** (High vs Moderate) and which controls/certs attach to **Gemini Enterprise Standard vs Plus vs NotebookLM Enterprise** specifically (vs Gemini for Google Cloud broadly).
- Full list of GA third-party connectors and which support real-time ACL sync vs periodic.
- Whether SCIM provisioning is first-class for Gemini Enterprise user/license management (Workspace/Cloud Identity SCIM exists; confirm scope for this SKU).
- Precise boundary of Vault capture across all "Gemini in Workspace" surfaces — what is and isn't discoverable/retainable.
- Founding/launch date of the Agentspace product line (initial preview vs GA).

## Sources
- [Gemini Enterprise app — Best of Google AI for Business](https://cloud.google.com/gemini-enterprise) — fetched 2026-06-28 — supports: product framing, editions (Standard/Plus), residency/audit/CMEK marketing; confidence: med (vendor marketing).
- [Google folds Agentspace into Gemini Enterprise (The Register)](https://www.theregister.com/2025/10/09/google_rearranges_agentspace_into_gemini/) — fetched 2026-06-28 — supports: rebrand date 2025-10-09; confidence: med.
- [How Gemini for Google Cloud uses your data (data governance)](https://docs.cloud.google.com/gemini/docs/discover/data-governance) — fetched 2026-06-28 — supports: "doesn't use your prompts or responses to train its models," CDPA, encryption-in-transit; confidence: high (primary).
- [Data residency — Gemini Enterprise & NotebookLM Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations) — fetched 2026-06-28 — supports: DRZ us/eu + ca/in, MLP region binding, CMEK/global caveats; confidence: high (primary).
- [Gemini Enterprise Agent Platform — zero data retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention) — fetched 2026-06-28 — supports: no train/fine-tune without permission, GA + pre-GA models; confidence: high (primary).
- [Compliance certifications and security controls — Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/compliance-security-controls) — fetched 2026-06-28 — supports: SOC/ISO/PCI/C5/HIPAA/FedRAMP, VPC-SC, CMEK, Access Transparency; confidence: high (primary).
- [Configure access controls for custom data sources (identity/ACLs)](https://docs.cloud.google.com/gemini/enterprise/docs/identity) — fetched 2026-06-28 — supports: ACL filtering, Pure ACLs vs Identity Mapping, IdP/workforce pools; confidence: high (primary).
- [Introduction to connectors and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores) — fetched 2026-06-28 — supports: connectors ingest content+ACLs, WIF with Entra/Okta/Ping via OIDC/SAML; confidence: high (primary).
- [Google Vault now supports retention rules and litigation holds for Gemini app](https://workspaceupdates.googleblog.com/2026/06/google-vault-now-supports-retention-rules-and-litigation-holds-for-Gemini-app.html) — fetched 2026-06-28 — supports: Vault holds/retention for Gemini app (2026-06), precedence; confidence: high (primary).
- [Gemini audit logs via Reporting API / investigation tools](https://workspaceupdates.googleblog.com/2025/07/gemini-audit-logs-reporting-api-audit-and-security-invesitgation-tools.html) — fetched 2026-06-28 — supports: Gemini audit logging in Workspace; confidence: high (primary).
- [ISO/IEC 42001 for Gemini / Vertex AI Agents / Code Assist (compliance offerings)](https://cloud.google.com/security/compliance/iso-42001) — fetched 2026-06-28 — supports: ISO 42001 AI management cert (May 2025); confidence: med.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; corrected ownership independent->public (Google LLC / Alphabet, NASDAQ: GOOGL), high confidence; noted Agentspace->Gemini Enterprise rebrand (2025-10-09, Agentspace closed to new subs 2025-12-31); added entitlement-aware-rag as secondary category. Established: no-training/ZDR commitments, data residency zones (us/eu + ca/in) with global-feature caveats, CMEK/VPC-SC/Access Transparency, certs (SOC/ISO 27001-27701/PCI/C5/HIPAA/FedRAMP + ISO 42001 May-2025), ACL-honoring search (Pure ACLs vs Identity Mapping; WIF with Entra/Okta/Ping), and Google Vault eDiscovery/retention/holds for the Gemini app (2026-06) with the embedded-"Gemini in Workspace" capture gap. No HARD contradiction.
