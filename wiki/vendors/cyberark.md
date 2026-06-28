---
title: CyberArk
type: vendor
name: CyberArk
slug: cyberark
categories: [non-human-identity, secrets-management, identity-governance, tool-identity-integration]
layer: foundation
aliases: [CyberArk Software, CYBR]
website: "https://www.cyberark.com"
founded: 1999
hq: "Petah Tikva, Israel (US ops: Newton, Massachusetts)"
ownership: acquired
ownership_detail: "Acquired by Palo Alto Networks — announced 2025-07-30 (~$25B: $45 cash + 2.2005 PANW shares per CYBR share), closed 2026-02-11. Was public (NASDAQ: CYBR, IPO 2014) until close."
ownership_confidence: high
funding_total: "n/a (was public, NASDAQ: CYBR)"
last_funding: IPO 2014; acquired by Palo Alto Networks 2026-02-11
deployment: [saas, self-hosted, on-prem, api]
target_customer: enterprise
hedge_fund_fit: high
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [pam, identity, secrets, machine-identity, acquired]
---

# CyberArk

> Primary category: [non-human-identity](../categories/non-human-identity.md). The privileged-access-management (PAM) incumbent, now Palo Alto Networks' Identity Security pillar.

**One-liner** — The market-leading privileged access management vendor — vaults, rotates, and brokers access to the most powerful human, machine, and (increasingly) AI-agent credentials — acquired by [palo-alto-networks](palo-alto-networks.md) in a ~$25B deal that closed February 2026.

**What it does** — CyberArk started in privileged access management (vaulting admin/root credentials, session isolation and recording, just-in-time elevation) and expanded across the identity spectrum: secrets management for DevOps/cloud ([conjur](conjur.md)), machine/non-human identity, workforce and customer identity, and identity governance. For an AI buyer, the relevant frontier is **identity security for agentic AI** — treating autonomous agents as a new class of privileged identity that needs least-privilege, just-in-time access and credential governance. That framing is the explicit rationale for the PANW acquisition.

**Where it sits in the stack** — Foundation-layer identity. Tagged [non-human-identity](../categories/non-human-identity.md) (primary), [secrets-management](../categories/secrets-management.md) (via [conjur](conjur.md) and CyberArk Secrets Manager), [identity-governance](../categories/identity-governance.md) (access certs / lifecycle), and [tool-identity-integration](../categories/tool-identity-integration.md) (brokering agent->tool credentials). Lethal-trifecta role: limits the blast radius on the **sensitive-data** and **egress** legs by controlling which identities can reach which secrets/systems.

**Deployment & architecture** — Self-hosted vault, SaaS (Privilege Cloud / Identity Security Platform), and hybrid. Conjur provides API-driven secrets injection for CI/CD and cloud-native workloads. Integrates with IdPs, SIEM, cloud providers, and Kubernetes.

**Positioning & differentiators** — Known as the PAM gold standard for regulated enterprises (banks, funds, governments). Differentiator vs. cloud-native secrets ([hashicorp-vault](hashicorp-vault.md), [aws-secrets-manager](aws-secrets-manager.md), [azure-key-vault](azure-key-vault.md)) is breadth: session controls, recording, and an enterprise governance wrapper rather than just key storage. Vs. NHI startups ([astrix-security](astrix-security.md), [aembit](aembit.md), [oasis-security](oasis-security.md), [token-security](token-security.md)) it is the incumbent with the install base. Post-acquisition, identity becomes a fourth PANW platform pillar alongside Strata/Cortex/Prisma.

**Ownership, funding & M&A** — Founded 1999 (Udi Mokady, Alon N. Cohen); HQ Petah Tikva, Israel, with major US ops in Newton, MA. Public on NASDAQ (CYBR) from its 2014 IPO. **Acquired by [palo-alto-networks](palo-alto-networks.md) — VERIFIED:** announced 2025-07-30 at ~$25B equity value ($45.00 cash + 2.2005 PANW shares per CyberArk share, 26% premium); transaction **closed 2026-02-11** after US/EU/UK/Israel regulatory clearance and shareholder approval. The seed flag "acq by Palo Alto" is **confirmed against PANW's own press release and corroborating SEC filings (PANW 8-K, CyberArk 6-K/425).** CyberArk itself was an acquirer: it bought Conjur (2017, ~$42M), Idaptive, Venafi (machine identity), and Zilla Security among others.

**CTO / hedge-fund lens** — Day-2 in this taxonomy, but effectively Day-1 for a regulated fund that already needs PAM for its privileged human admins; AI/agent governance is an extension of controls you should already have. SR 11-7 relevance is indirect (credential governance for model-serving and agent infrastructure). The ownership change matters for procurement: a CyberArk renewal now routes through Palo Alto Networks and may be bundled with Strata/Cortex.

**Competitors / alternatives** — [astrix-security](astrix-security.md), [aembit](aembit.md), [oasis-security](oasis-security.md), [token-security](token-security.md), [entro-security](entro-security.md), [silverfort](silverfort.md) (NHI/identity); [sailpoint](sailpoint.md), [saviynt](saviynt.md), [veza](veza.md) (IGA); [hashicorp-vault](hashicorp-vault.md) (secrets).

**Open questions / to verify**
- Integration roadmap of CyberArk into Cortex/Strata and how licensing is repackaged.
- Whether Conjur remains separately marketed or is folded into a unified Secrets Manager SKU.

**Sources**
- [Palo Alto Networks to Acquire CyberArk](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-announces-agreement-to-acquire-cyberark--the-identity-security-leader) — fetched 2026-06-28 — supports: acquirer, $25B terms, 2025-07-30 announce, agentic-identity rationale; confidence: high
- [CyberArk Acquires Conjur (CyberArk press)](https://www.cyberark.com/press/cyberark-acquires-conjur-revolutionizing-devops-security-drive-greater-business-agility/) — fetched 2026-06-28 — supports: Conjur acq 2017, founding, HQ; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; **CONFIRMED** seed M&A flag: acquired by Palo Alto Networks (announced 2025-07-30, ~$25B; closed 2026-02-11) against PANW press release + SEC filings. Raised ownership_confidence low->high. Established founded 1999, HQ Petah Tikva (US: Newton MA), formerly NASDAQ: CYBR. Noted CyberArk's own acquisitions (Conjur 2017, Venafi, Idaptive, Zilla).
