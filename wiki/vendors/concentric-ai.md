---
type: vendor
name: Concentric AI
slug: concentric-ai
categories: [dspm, data-access-governance]
layer: data
aliases: [Concentric]
website: "https://concentric.ai"
founded: 2018
hq: San Mateo, CA, USA
ownership: independent
ownership_detail: Privately held, VC-backed. >$67M raised total; $45M Series B (2024-10, led by Top Tier Capital Partners & HarbourVest).
ownership_confidence: high
funding_total: ">$67M"
last_funding: $45M Series B (2024-10, Top Tier Capital Partners & HarbourVest Partners)
deployment: [saas]
target_customer: mid-market to enterprise (Microsoft 365 / unstructured-data heavy)
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [dspm, data-access-governance, unstructured-data, oversharing]
---

# Concentric AI

> **One-liner** — DSPM built on deep-learning "Semantic Intelligence" that autonomously classifies data and fixes oversharing/permissions without writing rules or regexes.

**What it does** — Concentric's pitch is *autonomous* data security posture management: rather than hand-built rules, regex, or labels, it uses deep-learning/NLP ("Semantic Intelligence") to categorize structured and unstructured data, assess risk, and remediate — especially **oversharing and risky permissions** on documents and messages. It's strongest on the unstructured-data problem (files in Microsoft 365/SharePoint/OneDrive, Google Drive, etc.): finding sensitive content, seeing who can access it, and fixing exposure. You buy it to cut oversharing risk before turning on AI assistants that would otherwise surface that data.

**Where it sits in the stack** — Primary: [dspm](../categories/dspm.md); also [data-access-governance](../categories/data-access-governance.md). Data layer. Lethal-trifecta role: the **sensitive-data** leg — classify sensitive content and constrain who/what can access it (oversharing remediation), which directly limits what a Copilot/RAG system can surface. Trust zones: green/yellow unstructured-data plane.

**Deployment & architecture** — SaaS; connects to data repositories (M365/SharePoint/OneDrive, Google Workspace, file shares, cloud stores, messaging) to discover, classify, and remediate access. Agentless/API-connector model. Emphasis on autonomous classification + access remediation rather than appliance/agent deployment.

**Positioning & differentiators** — Differentiates on "no rules, no config" autonomous classification and on **oversharing/access remediation** for unstructured data — adjacent to what Varonis is known for, but ML-classification-led. Smaller and more focused than the category leaders: versus [cyera](cyera.md)/[sentra](sentra.md) (broad agentless *cloud* DSPM) Concentric leans into unstructured-content + permissions; versus [bigid](bigid.md) it's lighter and more autonomous but narrower; versus [microsoft-purview](microsoft-purview.md) it spans beyond Microsoft and avoids label/rule heavy lifting.

**Ownership, funding & M&A** — **Independent**, privately held. Founded **2018** by Karthik Krishnan (CEO); HQ San Mateo, CA. Funding: **$45M Series B (Oct 2024)** led by Top Tier Capital Partners and HarbourVest Partners (Ballistic Ventures, Engineering Capital, Clear Ventures, Citi Ventures participating), total **>$67M**. No acquisition; no seed M&A flag. Ownership confidence: high.

**CTO / hedge-fund lens** — **Day-1** if your biggest data risk is unstructured-file oversharing in Microsoft 365/Google Workspace — exactly the exposure that lights up when you enable Copilot/RAG. Its autonomous-classification model means lower config burden than rule-based tools, attractive to a small security team. SR 11-7: supports AI-governance/data-exposure evidence indirectly. Caveat: smaller vendor (concentration/longevity risk); narrower than the cloud-datastore-broad leaders, so a multi-cloud-database-heavy fund may still need a [cyera](cyera.md)/[bigid](bigid.md)-class tool alongside it.

**Competitors / alternatives** — [cyera](cyera.md), [sentra](sentra.md), [bigid](bigid.md), [securiti](securiti.md), [microsoft-purview](microsoft-purview.md), Varonis.

**Open questions / to verify**
- Breadth of cloud/database (structured) coverage vs its unstructured-data strength.
- Customer scale and any newer funding since the Oct 2024 Series B.

## Sources
- [Concentric AI Secures $45M Series B (BusinessWire, 2024-10-23)](https://www.businesswire.com/news/home/20241023142039/en/) + [SecurityWeek coverage](https://www.securityweek.com/concentric-ai-secures-45m-series-b-funding-to-expand-dspm-tech/) — fetched 2026-06-28 — supports: founding 2018, San Mateo HQ, $45M Series B / >$67M total, Semantic Intelligence DSPM, oversharing/access focus; confidence: high.

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established independent (>$67M raised; $45M Series B Oct 2024), founded 2018, San Mateo, autonomous "Semantic Intelligence" DSPM focused on unstructured-data oversharing/access remediation. Raised ownership_confidence to high. No M&A.
