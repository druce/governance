---
title: CyberArk Conjur
type: vendor
name: CyberArk Conjur
slug: conjur
aka: [Conjur, Conjur Open Source, CyberArk Secrets Manager, Idira Secrets Manager, Palo Alto Networks Secrets Manager]
primary_category: secrets-management
also_listed_in: []
website: https://www.paloaltonetworks.com/idira/machine/secrets-management
founded: 2011
hq: Newton/Waltham, Massachusetts, USA (origin)
ownership_state: acquired-closed
owner: Palo Alto Networks
ownership_note: 'Two-step chain. Conjur Inc. acquired by CyberArk May 2017 (~$42M) and turned into CyberArk''s secrets-management line; CyberArk then acquired by Palo Alto Networks (announced 2025-07-30, closed 2026-02-11, ~$25B). Since the May 2026 "Idira" rebrand of the CyberArk portfolio, the capability ships as Idira **Secrets Manager** under Machine Identity, and conjur.org 301s to the PANW page (verified 2026-07-27). "Conjur" survives only as the open-source project name.'
acquisition: {announced: 2025-07-30, closed: 2026-02-11, price: null}
funding_total: n/a (product within CyberArk)
last_funding: acquired by CyberArk 2017 (~$42M); CyberArk acquired by PANW 2026-02-11
market_position: null
deployment_model: [self-hosted, saas]
form_factor: [api, sdk]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [secrets, devops, machine-identity, cyberark, palo-alto, idira, renamed]
---

# CyberArk Conjur

> **Researched 2026-06-28; re-verified 2026-07-27.** Primary category: [secrets-management](../categories/secrets-management.md). Never a standalone company since 2017 — a product line, now inside [palo-alto-networks](palo-alto-networks.md). **The commercial brand is retired:** `conjur.org` 301-redirects to Palo Alto's **Idira → Machine Identity → Secrets Manager** page, with no Conjur or CyberArk branding left on it. What you buy today is **Idira Secrets Manager**. "Conjur" survives only as the open-source project.

**One-liner** — An open-source-rooted secrets management engine for DevOps and cloud-native workloads that injects credentials into pipelines and applications instead of hardcoding them; acquired by [cyberark](cyberark.md) in 2017, and since CyberArk's own acquisition by [palo-alto-networks](palo-alto-networks.md) it is sold as **Secrets Manager** under the **Idira** identity-security brand.

**What it does** — Conjur stores, rotates, and brokers machine secrets (API keys, DB credentials, tokens) for CI/CD pipelines, containers, and Kubernetes. Applications authenticate via machine identity and fetch secrets at runtime through an API/SDK, removing hardcoded credentials from code and config.

The naming has moved twice. CyberArk first renamed the commercial editions — **Conjur Cloud → Secrets Manager, SaaS** and **Conjur Enterprise → Secrets Manager, Self-Hosted**. Palo Alto's May 2026 **Idira** rebrand then folded that line into Idira's *Machine Identity* pillar, alongside Unified Secrets Governance, Application Credentials Delivery, and Certificate Manager. As of 2026-07-27 the Idira page markets **Secrets Manager** (SaaS or self-hosted) with centralized secret storage and retrieval, automated rotation and lifecycle control, SPIFFE-based cryptographic workload identity, audit trails, and native CI/CD, container, and application integrations. **Conjur Open Source** is a separate matter — see the ownership note below.

**Where it sits in the stack** — Foundation-layer [secrets-management](../categories/secrets-management.md), adjacent to [non-human-identity](../categories/non-human-identity.md). It controls access to sensitive data by keeping high-value credentials out of code and reachable only by authenticated workloads. In an AI context it secures the secrets agents and model-serving infra need.

**Deployment & architecture** — Self-hosted (the OSS lineage, now Secrets Manager Self-Hosted) or SaaS; API/SDK-driven secret retrieval; native integrations for Kubernetes, OpenShift, Ansible, and major CI/CD tools. A direct competitor in posture to [hashicorp-vault](hashicorp-vault.md).

**Positioning & differentiators** — The pitch was always DevOps-native secrets with CyberArk's enterprise governance behind it — bridging developer ergonomics and the audit/compliance posture regulated buyers expect. Under Idira that argument gets larger and more platform-shaped: secrets sit next to PAM, certificate lifecycle, and agentic-identity controls in one identity-security suite, and PANW is positioning the whole thing as the control plane for AI agents as well as humans and machines. The flip side is that the standalone, developer-tool framing is gone. Nearest neighbor is [hashicorp-vault](hashicorp-vault.md) (now part of IBM); cloud-native alternatives are [aws-secrets-manager](aws-secrets-manager.md), [azure-key-vault](azure-key-vault.md), [gcp-secret-manager](gcp-secret-manager.md); startup challengers include [doppler](doppler.md), [infisical](infisical.md), [entro-security](entro-security.md).

**Ownership, funding & M&A** — Two-step chain. Conjur Inc. (Newton/Waltham, MA) was **acquired by CyberArk in May 2017 for ~$42M** and turned into CyberArk's secrets-management product line; it has not been an independent vendor since. [cyberark](cyberark.md) was then **acquired by [palo-alto-networks](palo-alto-networks.md)** — announced 2025-07-30, **closed 2026-02-11**, ~$25B — and in **May 2026** PANW rebranded the acquired portfolio as **Idira**. PANW's own FAQ frames it as "the next-generation identity security platform, built on CyberArk's legacy and powered by Palo Alto Networks." Reporting on the rebrand notes the underlying platform and component names are unchanged; the commercial branding is what moved. The 2017 deal is confirmed via CyberArk's press release; the PANW chain and the Idira rename are confirmed via PANW's own pages and the live `conjur.org` redirect.

**Open source status** — `github.com/cyberark/conjur` is still public and **not archived** as of 2026-07-27, still LGPL v3.0, still under the `cyberark` GitHub org with no Idira or PANW branding. Its README now carries a "Migrating to CyberArk Secrets Manager, Self-Hosted" section pointing users to the commercial product. So the OSS project is alive but the marketing domain that fronted it is gone — read that as a soft push toward the commercial SKU rather than an announced end-of-life. Nothing PANW has published states a sunset date.

**CTO / hedge-fund lens** — Day-1 if you run your own CI/CD and need machine secrets governed centrally; a fund already standardized on CyberArk PAM gets this as the natural secrets layer, and that logic only strengthens under Idira, where PAM and secrets are sold as one platform. Two practical notes: (1) shop for it as **Idira Secrets Manager** — searching for "Conjur" will land you on OSS docs and stale collateral; (2) if you adopted **Conjur Open Source** specifically to avoid a commercial secrets contract, the disappearance of `conjur.org` is a signal worth tracking, even though the repo is still maintained. Otherwise, cloud-native secret managers remain lower-friction for teams already all-in on one cloud.

**Competitors / alternatives** — [hashicorp-vault](hashicorp-vault.md), [aws-secrets-manager](aws-secrets-manager.md), [azure-key-vault](azure-key-vault.md), [gcp-secret-manager](gcp-secret-manager.md), [doppler](doppler.md), [infisical](infisical.md), [1password](1password.md).

**Open questions / to verify**
- ~~Whether "Conjur" survives as a brand~~ — **resolved 2026-07-27:** the commercial brand is retired. Conjur Cloud/Enterprise became Secrets Manager SaaS/Self-Hosted, and the Idira rebrand carried that name forward. "Conjur" persists only as the OSS project and in SDK repo names (e.g. `conjur-api-go`, documented as the "Go client for the CyberArk Secrets Manager API").
- Continued investment in **Conjur Open Source** under PANW. Repo is live and unarchived, but the README steers users to the commercial product and no PANW statement addresses the OSS roadmap. Unresolved — not a contradiction, just an absence of evidence.
- Whether the `cyberark` GitHub org and `docs.cyberark.com` (which already serve "Idira Docs"-branded content) eventually move to PANW domains. Cosmetic, but it affects link rot here.

**Sources**
- [CyberArk Acquires Conjur (CyberArk press)](https://www.cyberark.com/press/cyberark-acquires-conjur-revolutionizing-devops-security-drive-greater-business-agility/) — fetched 2026-06-28 — supports: Conjur acquired by CyberArk 2017 (~$42M), DevOps secrets positioning; confidence: high
- [Idira — Secrets Manager (Palo Alto Networks)](https://www.paloaltonetworks.com/idira/machine/secrets-management) — fetched 2026-07-27, cached `raw/sources/2026-07-27--conjur--panw-idira-secrets-management.md` — supports: `conjur.org` 301 target, current product name "Secrets Manager", capability list, absence of Conjur/CyberArk branding; confidence: high
- [Idira platform overview (Palo Alto Networks)](https://www.paloaltonetworks.com/idira) — fetched 2026-07-27 — supports: Idira = rebranded CyberArk portfolio, Machine Identity module list, "built on CyberArk's legacy and powered by Palo Alto Networks"; confidence: high (vendor marketing, but primary for naming)
- [Palo Alto Networks rebrands CyberArk with Idira platform release (SDxCentral)](https://www.sdxcentral.com/news/palo-alto-networks-rebrands-cyberark-with-idira-platform-release/) — fetched 2026-07-27 — supports: May 2026 rebrand timing, ~$25B deal size, platform/component names unchanged; confidence: medium-high (trade press)
- [cyberark/conjur (GitHub)](https://github.com/cyberark/conjur) — fetched 2026-07-27 — supports: OSS repo live and unarchived, LGPL v3.0, README migration path to Secrets Manager Self-Hosted; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed Conjur is a CyberArk product line (acquired by CyberArk 2017, ~$42M), not an independent company; ownership chain to PANW established via the CyberArk acquisition (closed 2026-02-11). Set ownership=subsidiary, confidence high.
- [2026-07-27] URL audit found `conjur.org` 301-redirecting to `https://www.paloaltonetworks.com/idira/machine/secrets-management` — a Palo Alto Networks page with **zero Conjur or CyberArk branding**. Verified the redirect by curl and confirmed the cause: PANW rebranded the acquired CyberArk portfolio as **Idira** in **May 2026**, after the acquisition closed 2026-02-11. Repointed `website` to the Idira Secrets Manager page; corrected `owner` **CyberArk → Palo Alto Networks** and `acquisition.announced` **2026-02-11 → 2025-07-30** (the close date was wrongly duplicated into the announce field); added `Idira Secrets Manager` / `Palo Alto Networks Secrets Manager` to `aka`. **Brand open question resolved** (commercial brand retired; OSS project name survives). Added an open-source status section: repo live and unarchived, but README steers to the commercial SKU. Source cached at `raw/sources/2026-07-27--conjur--panw-idira-secrets-management.md`. See [cyberark](cyberark.md) for the parent deal.
