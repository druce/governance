---
type: vendor
name: Microsoft Purview
slug: microsoft-purview
categories: [dspm, dlp]
layer: data
aliases: [Purview, Microsoft 365 Compliance, Azure Purview]
website: https://www.microsoft.com/en-us/security/business/microsoft-purview
founded: 2022
hq: Redmond, WA, USA
ownership: public
ownership_detail: Product of Microsoft Corporation (NASDAQ: MSFT); not a standalone company. "Purview" brand consolidated the former Microsoft 365 Compliance + Azure Purview in 2022.
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas, api]
target_customer: enterprise (esp. Microsoft 365 E5 / regulated shops)
hedge_fund_fit: high
priority: day-1
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 1
last_updated: 2026-06-28
tags: [microsoft, dspm, dlp, data-governance, copilot]
---

# Microsoft Purview

> **One-liner** — Microsoft's bundled data-security/compliance suite (classification, DLP, sensitivity labels, insider risk, DSPM) that governs sensitive data across Microsoft 365, Azure, and increasingly third-party clouds — and the default way to keep data out of Copilot prompts.

**What it does** — Purview is the umbrella over Microsoft's data-protection stack: data discovery and classification, sensitivity labels (Information Protection), Data Loss Prevention (DLP), Insider Risk Management, eDiscovery/Data Security Investigations, and a newer **Data Security Posture Management (DSPM)** dashboard that sits on top of all of them. DSPM answers "what data do we have, where is it, who can access it, how is it protected" and now adds **DSPM for AI / AI observability** — tracking how Copilot and other AI apps/agents touch sensitive data, with ready-made policies to block sensitive content from AI prompts. For a Microsoft 365 shop it is the path of least resistance for both DSPM and DLP because the labels and policies travel natively through Office, SharePoint, OneDrive, Teams, and Copilot.

**Where it sits in the stack** — Primary: [[dspm]]; also [[dlp]]. Data layer. Lethal-trifecta role: protects the **sensitive-data** leg (classification + access posture) and helps choke the **egress** leg (endpoint/browser DLP blocking uploads to third-party gen-AI sites, and DLP on Copilot prompts). Trust zones: governs data in the green/yellow zones and controls what crosses into AI.

**Deployment & architecture** — SaaS, delivered through the Microsoft Purview portal and the M365/Entra control plane; API/Graph access for automation. Native coverage is Microsoft 365 first; the current DSPM extends to Azure, Fabric, and third-party SaaS/IaaS (Google Cloud Platform, Snowflake, Databricks) via Microsoft Sentinel data lake integration. Notably, Purview DSPM **integrates with partner DSPMs — Varonis, [[cyera]], [[bigid]], and OneTrust** — so it can coexist with or ingest from rival tools rather than fully replace them. AI remediation is driven by Security Copilot + triage agents under human approval; all actions audited.

**Positioning & differentiators** — Ubiquity and bundling, not best-of-breed depth. If you already own M365 E5, much of Purview is "free" (licensed) and natively wired into Copilot governance, which is why it's most shops' Day-1 DSPM/DLP. Weaknesses vs specialists: historically weaker outside the Microsoft estate (multi-cloud datastores, unstructured data at scale, agentless cloud discovery), more configuration-heavy, and label-dependent. Specialists like [[cyera]], [[bigid]], [[sentra]], [[securiti]], and [[concentric-ai]] compete on broader cloud coverage, agentless deployment, and ML classification that doesn't rely on hand-built labels/rules — and several now plug into Purview rather than rip it out.

**Ownership, funding & M&A** — Product of **Microsoft Corporation** (public, NASDAQ: MSFT). The Purview brand was formed in 2022 by merging Microsoft 365 Compliance and Azure Purview. No standalone funding/valuation. Ownership confidence: high. No seed M&A flag.

**CTO / hedge-fund lens** — **Day-1** for any M365-centric fund. If your sensitive data and your AI assistant both live in Microsoft 365, Purview is the cheapest, most native way to label data, run DLP, and govern what Copilot can see — directly relevant before turning on M365 Copilot. SR 11-7/model-risk: not a model-risk tool itself, but its data-classification and audit trails feed governance evidence. Caveats: real value needs E5-tier licensing and meaningful configuration effort, and coverage thins outside Microsoft — multi-cloud or heavy-unstructured shops often pair it with a specialist DSPM.

**Competitors / alternatives** — [[cyera]], [[bigid]], [[sentra]], [[securiti]], [[concentric-ai]], Varonis; in DLP also [[cyberhaven]], [[nightfall-ai]], [[forcepoint]], [[netskope]].

**Open questions / to verify**
- Real-world coverage quality of the third-party SaaS/IaaS connectors (GCP/Snowflake/Databricks) vs native M365.
- Exact licensing tiers required for DSPM for AI vs classic DLP.

## Sources
- [Learn about Microsoft Purview Data Security Posture Management (DSPM) — Microsoft Learn](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) — fetched 2026-06-28 — supports: what DSPM covers, M365/Azure/Fabric + 3rd-party SaaS, DLP/AI relationship, partner integrations (Varonis/Cyera/BigID/OneTrust); confidence: high (primary).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established Microsoft-owned product (public, MSFT), Day-1 DSPM/DLP for M365 shops, AI/Copilot governance via DSPM for AI, and that Purview integrates with partner DSPMs (Varonis/Cyera/BigID/OneTrust). Set ownership=public, confidence medium.
