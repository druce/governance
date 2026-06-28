---
type: vendor
name: Azure Dev Box
slug: azure-dev-boxes
categories: [ephemeral-environments]
layer: governance
aliases: [Microsoft Dev Box, Azure Dev Boxes]
website: "https://azure.microsoft.com/en-us/products/dev-box"
founded: 2023
hq: Redmond, WA, USA
ownership: public
ownership_detail: "First-party Microsoft Azure service (Microsoft Corp, NASDAQ: MSFT); GA July 2023"
ownership_confidence: high
funding_total:
last_funding:
deployment: [saas]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [untrusted-input, egress]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [first-party, dev-environments, microsoft, azure]
---

# Azure Dev Box

**One-liner** — Microsoft's managed, cloud-hosted developer workstations — preconfigured Windows (or Linux) cloud PCs developers self-serve on demand and tear down, keeping dev work off local endpoints.

**What it does** — Azure Dev Box gives a developer a full cloud workstation (typically a Windows dev VM with tooling, source, and entitlements baked in) provisioned through self-service and governed centrally via Microsoft Intune and Azure networking. Built on the Windows 365 / Cloud PC platform. In an AI context it serves the same role as [github-codespaces](github-codespaces.md) — an isolated, ephemeral place to run development work, agents, and untrusted tooling.

**Where it sits in the stack** — [ephemeral-environments](../categories/ephemeral-environments.md), governance layer; an enabler of [trust-zone-segmentation](../categories/trust-zone-segmentation.md). Lethal-trifecta role: contains **untrusted-input** execution and constrains **egress** through Azure network controls. Heavier-weight than a container (full OS workstation), which matters for Windows-centric or regulated shops that need a managed, auditable desktop.

**Deployment & architecture** — SaaS / managed Azure service. Integrates with Microsoft Entra ID, Intune, Azure Virtual Network (bring-your-own-network for egress control), and the Microsoft Dev Center governance model. GA July 2023.

**Positioning & differentiators** — Full managed Windows workstations vs. [github-codespaces](github-codespaces.md)' Linux devcontainers; the natural fit for Microsoft-centric enterprises already on Entra/Intune. Adjacent to VDI but developer-tuned.

**Ownership, funding & M&A** — First-party Microsoft Azure service (Microsoft Corp, public, NASDAQ: MSFT). No standalone funding/M&A. Confidence: high.

**CTO / hedge-fund lens** — Day-2 infrastructure. Useful for funds that want developers (and AI coding agents) operating on centrally-governed, ephemeral cloud workstations rather than on local machines — strong fit if you are already a Microsoft 365 / Intune shop. A configuration/governance decision, not a security product.

**Competitors / alternatives** — [github-codespaces](github-codespaces.md), [cloudflare-workers](cloudflare-workers.md) (different shape), Windows 365, VDI.

**Open questions / to verify** — Practicality of running headless AI agents on full Dev Box workstations vs. lighter container sandboxes.

## Sources
- [Azure Dev Box product page](https://azure.microsoft.com/en-us/products/dev-box) — fetched 2026-06-28 — supports: product description, Microsoft ownership, GA date; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); established first-party Microsoft Azure service (ownership public/MSFT, high confidence), positioned as ephemeral-environments enabler.
