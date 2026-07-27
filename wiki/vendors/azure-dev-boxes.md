---
title: Azure Dev Box
type: vendor
name: Azure Dev Box
slug: azure-dev-boxes
aka: [Microsoft Dev Box, Azure Dev Boxes]
primary_category: ephemeral-environments
also_listed_in: []
website: https://azure.microsoft.com/en-us/products/dev-box
founded: 2023
hq: Redmond, WA, USA
ownership_state: public
owner: null
ownership_note: 'First-party Microsoft Azure service (Microsoft Corp, NASDAQ: MSFT); GA July 2023. No ownership change — but the product is being sunset: closed to new sign-ups 2025-11-01 and in maintenance mode, with capabilities consolidating into Windows 365. End-of-service date not announced as of 2026-07-27.'
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
tags: [first-party, dev-environments, microsoft, azure, maintenance-mode, closed-to-new-customers]
sources:
  - {claim: closed-to-new-signups, url: "https://azure.microsoft.com/en-us/products/dev-box", date: 2026-07-27, confidence: high}
  - {claim: maintenance-mode, url: "https://learn.microsoft.com/en-us/azure/dev-box/dev-box-windows-365-announcement", date: 2026-07-27, confidence: high}
  - {claim: windows-365-successor-capabilities, url: "https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/", date: 2026-07-27, confidence: high}
  - {claim: frontline-licensing-requirement, url: "https://www.directionsonmicrosoft.com/in-brief/dev-box-merges-into-windows-365/", date: 2026-07-27, confidence: medium}
---

# Azure Dev Box

> **Closed to new customers.** Microsoft stopped accepting Dev Box sign-ups on **2025-11-01** and the service is in **maintenance mode** — no new features. Existing deployments keep running and stay supported; the end-of-service date has not been announced. New buyers are directed to **Windows 365**. This is a product sunset, not an ownership change. Verified 2026-07-27.

**One-liner** — Microsoft's managed, cloud-hosted developer workstations — preconfigured Windows (or Linux) cloud PCs developers self-serve on demand and tear down, keeping dev work off local endpoints. **No longer purchasable**; superseded by Windows 365.

**What it does** — Azure Dev Box gives a developer a full cloud workstation (typically a Windows dev VM with tooling, source, and entitlements baked in) provisioned through self-service and governed centrally via Microsoft Intune and Azure networking. Built on the Windows 365 / Cloud PC platform. In an AI context it serves the same role as [github-codespaces](github-codespaces.md) — an isolated, ephemeral place to run development work, agents, and untrusted tooling.

**Where it sits in the stack** — [ephemeral-environments](../categories/ephemeral-environments.md), governance layer; an enabler of [trust-zone-segmentation](../categories/trust-zone-segmentation.md). It contains the execution of untrusted code and content inside an isolated workstation and constrains outbound data flows through Azure network controls. Heavier-weight than a container (full OS workstation), which matters for Windows-centric or regulated shops that need a managed, auditable desktop.

**Deployment & architecture** — SaaS / managed Azure service. Integrates with Microsoft Entra ID, Intune, Azure Virtual Network (bring-your-own-network for egress control), and the Microsoft Dev Center governance model. GA July 2023. Architecturally it was always a layer on the Windows 365 / Cloud PC platform, which is why the consolidation is a capability merge rather than a migration to something unrelated.

**Product status & the Windows 365 transition** — Microsoft's Azure product page states, verbatim: *"Capabilities of Microsoft Dev Box are transitioning to Windows 365. Existing customers can continue using Dev Box, but new sign-ups will no longer be accepted as of November 1, 2025."* The Dev Box roadmap page on Microsoft Learn has been replaced in place with a maintenance-mode notice: *"Dev Box is now in maintenance mode, with no additional features planned. Microsoft's investments for developer cloud environments are focused on Windows 365."* Existing dev boxes, pools, and configurations "remain fully functional and supported"; no end-of-service date has been published.

This is a **merge into a separate, still-sold product, not a rename** — Windows 365 predates Dev Box, has its own SKUs and licensing, and is administered through Intune / the Microsoft 365 admin center rather than the Azure Dev Center resource model. Two Windows 365 capabilities announced at Build 2026 (2026-06-02) carry the successor role, at different maturities:

- **Windows 365 with Developer configuration** (*public preview*) — the direct replacement for a Dev Box pool image: a preconfigured Windows 11 image with VS Code, Git, GitHub CLI, and WSL set up from first sign-in, extensible with further SDKs and CLIs, under organizational policy.
- **Windows 365 for Agents** (*GA*, delivered within Agent 365) — Intune-managed Cloud PCs where AI agents execute multi-step workflows (opening apps, navigating interfaces, entering inputs) fully separate from the user's own machine. This is an explicit containment boundary for computer-using agents, which Dev Box never shipped as a distinct offering.

Note the status asymmetry: the *developer* image is still preview while the *agent* Cloud PC is GA — Microsoft's investment is visibly weighted toward the agent use case.

Licensing is the open commercial question. Independent licensing analysts (Directions on Microsoft; Licensing Lore & Law) report that developer scenarios in Windows 365 are enabled via **Windows 365 Frontline**, at roughly a 50% premium over Windows 365 Enterprise but with one license covering up to three Cloud PCs per user. Neither Microsoft source consulted names a required SKU, so treat the Frontline requirement and the price delta as analyst reporting (medium confidence), not vendor-confirmed. Analysts also report an exception process letting organizations that evaluated Dev Box before the cutoff still onboard — again not restated by Microsoft.

Several governance features were cancelled before GA as part of the freeze, and are worth knowing if you inherited a Dev Box estate: firewall **Service Tags** (traffic rules by Service Tag), automatic **developer offboarding** on leaver/transfer, **on-behalf creation**, and SSO for pre-existing dev box machines. The first two are egress-control and joiner-mover-leaver gaps that will not be filled in this product.

**Positioning & differentiators** — Historically: full managed Windows workstations vs. [github-codespaces](github-codespaces.md)' Linux devcontainers; the natural fit for Microsoft-centric enterprises already on Entra/Intune; adjacent to VDI but developer-tuned. As of 2025-11-01 that positioning is retrospective — Dev Box is not a competitive option because it cannot be bought. `market_position` stays `null`: none of the schema's labels (leader, challenger, legacy-incumbent, platform-module, niche-specialist…) honestly describes a product withdrawn from sale, and inventing one would mislead.

**Ownership, funding & M&A** — First-party Microsoft Azure service (Microsoft Corp, public, NASDAQ: MSFT). No standalone funding or M&A, and the Windows 365 transition is **not** an ownership event — Microsoft owned it before and owns the successor. Confidence: high.

**CTO / hedge-fund lens** — **Not a buying decision any more.** Three cases:

- **New evaluation.** Do not shortlist Dev Box; you cannot sign up. Evaluate **Windows 365** instead, and budget on the assumption that developer Cloud PCs need Frontline licensing (verify with your Microsoft account team — the analyst reporting above is not vendor-confirmed) and that the Developer configuration image is still preview-quality. If your interest was specifically *sandboxing AI agents away from user endpoints*, Windows 365 for Agents is the GA piece and is the more mature half of the offering.
- **Existing Dev Box estate.** Nothing breaks and support continues, but you are running a frozen product with an unannounced end date and a known set of cancelled governance features (egress Service Tags, automatic offboarding). Treat migration planning as a scheduled Day-2 item rather than an emergency, and get the end-of-service date from your account team rather than waiting for a public notice.
- **Microsoft-shop framing generally.** The underlying thesis is unchanged — centrally-governed ephemeral cloud workstations remain a sound way to keep developer and agent work off local endpoints, and are a configuration/governance decision rather than a security product. Only the SKU you buy has moved.

**Competitors / alternatives** — **Windows 365** (the designated successor; no wiki page yet), [github-codespaces](github-codespaces.md), [cloudflare-workers](cloudflare-workers.md) (different shape), classic VDI/AVD.

**Open questions / to verify** — (1) When does Dev Box actually stop running? No end-of-service date announced as of 2026-07-27. (2) Does Windows 365 developer usage genuinely require Frontline licensing, and at what price? Analyst-reported only. (3) Does Windows 365 with Developer configuration reach GA, and does it restore the egress/offboarding controls cancelled on Dev Box? (4) Practicality of running headless AI agents on full Windows Cloud PCs vs. lighter container sandboxes — now partly answered by Windows 365 for Agents, but unverified in practice. (5) Windows 365 has no vendor page in this wiki; consider creating one, since it is now the live product in this slot.

## Sources
- [Azure Dev Box product page](https://azure.microsoft.com/en-us/products/dev-box) — fetched 2026-06-28, re-fetched 2026-07-27 — supports: product description, Microsoft ownership, GA date, and the new-sign-up closure notice dated 2025-11-01; confidence: high
- [Microsoft Dev Box — maintenance mode (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/dev-box/dev-box-windows-365-announcement) — fetched 2026-07-27 (page `ms.date` 2026-05-01) — supports: maintenance-mode status, continued support for existing deployments, Windows 365 as recommended path, list of cancelled pre-GA features; confidence: high
- [Build 2026: Furthering Windows as the trusted platform for development (Windows Developer Blog, 2026-06-02)](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/) — fetched 2026-07-27 — supports: Windows 365 with Developer configuration (public preview) and Windows 365 for Agents (GA within Agent 365); confidence: high
- [Dev Box merges into Windows 365 (Directions on Microsoft)](https://www.directionsonmicrosoft.com/in-brief/dev-box-merges-into-windows-365/) — fetched 2026-07-27 — independent licensing analysis; supports: characterization as a capability merge rather than a rename, Frontline licensing and ~50% premium, end date TBD; confidence: medium (not vendor-confirmed)
- [Dev Box capabilities coming to Windows 365 (Licensing Lore & Law, 2025-11-04)](https://www.licensingschool.co.uk/licensing-blog/2025/11/04/dev-box-capabilities-coming-to-windows-365/) — fetched 2026-07-27 — independent licensing analysis; supports: Frontline enablement, onboarding-exception process for prior evaluators; confidence: medium
- Cached: `raw/sources/2026-07-27--azure-dev-boxes--windows-365-transition.md`

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched (light); established first-party Microsoft Azure service (ownership public/MSFT, high confidence), positioned as ephemeral-environments enabler.
- [2025-11-01] **Closed to new customers.** Microsoft stopped accepting new Dev Box sign-ups; existing customers unaffected. (Date of the event, recorded here 2026-07-27.)
- [2026-05-01] **Maintenance mode.** Microsoft Learn replaced the Dev Box roadmap with a maintenance-mode notice — no further features, investment redirected to Windows 365; seven previously planned features (incl. firewall Service Tags and automatic developer offboarding) cancelled before GA. (Page `ms.date`; recorded here 2026-07-27.)
- [2026-06-02] Build 2026: Windows 365 with Developer configuration announced in public preview; Windows 365 for Agents GA within Agent 365 — the two successor shapes.
- [2026-07-27] Researched; confirmed the sunset from two Microsoft primary sources. `last_verified` → 2026-07-27; `verify_after` set to 2027-01-31 to re-check for an announced end-of-service date. `ownership_state` unchanged (`public`) — this is a product sunset, not M&A; detail added to `ownership_note` and `maintenance-mode` / `closed-to-new-customers` tags added (following the `helicone` precedent of tagging frozen status rather than overloading `ownership_state`). "Windows 365" deliberately **not** added to `aka` — it is a distinct pre-existing product absorbing the capability, not a rename. Body rewritten around buying-relevance: page now leads with the closure, and the CTO lens splits new-evaluation / existing-estate / general guidance.
