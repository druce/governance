---
type: vendor
name: CyberArk Conjur
slug: conjur
categories: [secrets-management]
layer: foundation
aliases: [Conjur, Conjur Open Source, CyberArk Secrets Manager]
website: https://www.conjur.org
founded: 2011
hq: Newton/Waltham, Massachusetts, USA (origin)
ownership: subsidiary
ownership_detail: "Product line of CyberArk (acquired by CyberArk 2017 for ~$42M). CyberArk in turn acquired by Palo Alto Networks (closed 2026-02-11), so Conjur is now part of PANW."
ownership_confidence: high
funding_total: n/a (product within CyberArk)
last_funding: acquired by CyberArk 2017 (~$42M); CyberArk acquired by PANW 2026-02-11
deployment: [self-hosted, saas, api, sdk]
target_customer: enterprise
hedge_fund_fit: medium
priority: day-1
trifecta_relevance: [sensitive-data]
status: researched
confidence: high
sources_count: 1
last_updated: 2026-06-28
tags: [secrets, devops, machine-identity, cyberark, palo-alto]
---

# CyberArk Conjur

> Primary category: [[secrets-management]]. CyberArk's DevOps/cloud-native secrets engine — not a standalone company.

**One-liner** — An open-source-rooted secrets management engine for DevOps and cloud-native workloads, owned by [[cyberark]] (and therefore now by [[palo-alto-networks]]), that injects credentials into pipelines and applications instead of hardcoding them.

**What it does** — Conjur stores, rotates, and brokers machine secrets (API keys, DB credentials, tokens) for CI/CD pipelines, containers, and Kubernetes. Applications authenticate to Conjur via machine identity and fetch secrets at runtime through an API/SDK, removing hardcoded credentials from code and config. It ships as **Conjur Open Source** plus commercial **Conjur Enterprise / CyberArk Secrets Manager**.

**Where it sits in the stack** — Foundation-layer [[secrets-management]], adjacent to [[non-human-identity]]. It addresses the **sensitive-data** leg of the lethal trifecta by keeping high-value credentials out of code and reachable only by authenticated workloads. In an AI context it secures the secrets agents and model-serving infra need.

**Deployment & architecture** — Self-hosted (the OSS lineage) or via CyberArk's SaaS Secrets Manager; API/SDK-driven secret retrieval; native integrations for Kubernetes, OpenShift, Ansible, and major CI/CD tools. A direct competitor in posture to [[hashicorp-vault]].

**Positioning & differentiators** — Conjur's pitch is DevOps-native secrets with CyberArk's enterprise governance behind it — bridging developer ergonomics and the audit/compliance posture regulated buyers expect. Nearest neighbor is [[hashicorp-vault]] (now part of IBM); cloud-native alternatives are [[aws-secrets-manager]], [[azure-key-vault]], [[gcp-secret-manager]]; startup challengers include [[doppler]], [[infisical]], [[entro-security]].

**Ownership, funding & M&A** — Conjur Inc. (Newton/Waltham, MA) was **acquired by CyberArk in May 2017 for ~$42M** and turned into CyberArk's secrets-management product line; it is not an independent vendor. With CyberArk's own acquisition by [[palo-alto-networks]] (closed 2026-02-11), Conjur is now part of PANW. Confirmed via CyberArk's press release; PANW chain confirmed via the CyberArk acquisition (see [[cyberark]]).

**CTO / hedge-fund lens** — Day-1 if you run your own CI/CD and need machine secrets governed centrally; a fund already standardized on CyberArk PAM gets Conjur as the natural secrets layer. Otherwise, cloud-native secret managers may be lower-friction. Watch the PANW reorganization for how Conjur is packaged going forward.

**Competitors / alternatives** — [[hashicorp-vault]], [[aws-secrets-manager]], [[azure-key-vault]], [[gcp-secret-manager]], [[doppler]], [[infisical]], [[1password]].

**Open questions / to verify**
- Whether "Conjur" survives as a brand or is fully merged into CyberArk/PANW Secrets Manager.
- Continued investment in the open-source edition post-PANW.

**Sources**
- [CyberArk Acquires Conjur (CyberArk press)](https://www.cyberark.com/press/cyberark-acquires-conjur-revolutionizing-devops-security-drive-greater-business-agility/) — fetched 2026-06-28 — supports: Conjur acquired by CyberArk 2017 (~$42M), DevOps secrets positioning; confidence: high

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; confirmed Conjur is a CyberArk product line (acquired by CyberArk 2017, ~$42M), not an independent company; ownership chain to PANW established via the CyberArk acquisition (closed 2026-02-11). Set ownership=subsidiary, confidence high.
