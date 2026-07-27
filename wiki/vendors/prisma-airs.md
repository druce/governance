---
title: Prisma AIRS (Palo Alto)
type: vendor
name: Prisma AIRS (Palo Alto)
slug: prisma-airs
aka: [Prisma AIRS, Palo Alto AI Runtime Security]
primary_category: ai-runtime-security
also_listed_in: [ai-spm, mcp-gateway, ai-gateway]
website: https://www.paloaltonetworks.com/ai-security/prisma-airs
founded: 2025
hq: Santa Clara, California, USA (Palo Alto Networks)
ownership_state: acquired-closed
owner: Palo Alto Networks
ownership_note: 'Product platform of Palo Alto Networks. Built on acquisitions: Protect AI (closed 2025-07-22) for model scanning/red-teaming/posture; Portkey (closed 2026-05-29) as the AI Gateway component.'
acquisition: {announced: 2025-07-22, closed: 2026-05-29, price: null}
funding_total: n/a (PANW product)
last_funding: n/a
market_position: null
deployment_model: [saas]
form_factor: [api, inline-proxy, sdk]
data_leaves_tenancy: unverified
integrations: []
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: unverified
target_customer: enterprise
last_verified: 2026-07-27
verify_after: null
tags: [ai-runtime-security, ai-firewall, ai-spm, protect-ai, portkey, palo-alto]
---

# Prisma AIRS (Palo Alto)

> Primary category: [ai-runtime-security](../categories/ai-runtime-security.md). Palo Alto Networks' consolidated AI security platform — runtime firewall + posture + red-teaming + AI gateway.

**One-liner** — Palo Alto Networks' AI security platform (Prisma AI Runtime Security) that inspects AI traffic for prompt injection, data leakage and malicious responses, scans models, red-teams them, and now governs agents — assembled largely from the Protect AI and Portkey acquisitions.

**What it does** — Prisma AIRS aims to be end-to-end AI security across apps, agents, models, and data: **runtime protection** (an "AI firewall" inspecting prompts/responses for injection, jailbreaks, sensitive-data exfiltration, toxic/malicious output), **model scanning** (vulnerabilities in model artifacts), **AI red teaming** (automated adversarial testing), **AI security posture management** (discover/inventory AI assets), and **agent security** (governing autonomous agents). Much of the model-scanning/red-teaming/posture capability came from [palo-alto-networks](palo-alto-networks.md)'s acquisition of Protect AI; the gateway came from [portkey](portkey.md).

**Where it sits in the stack** — Model/prompt layer; tagged [ai-runtime-security](../categories/ai-runtime-security.md) (primary), [ai-spm](../categories/ai-spm.md), [mcp-gateway](../categories/mcp-gateway.md), and [ai-gateway](../categories/ai-gateway.md) (the Portkey component). It is one of the few products that touches all three legs of the lethal trifecta: untrusted-input inspection (prompt-injection defense), sensitive-data controls (DLP on prompts/responses), and egress control (gateway over model traffic). Lives at the boundary between the app/agent and the model.

**Deployment & architecture** — Multiple intercept modes: API-based inspection (apps call AIRS to scan prompts/responses), network/inline via the PANW SASE fabric, SDKs, and now the Portkey AI gateway sitting in front of model APIs. Integrates with the broader PANW platform (Strata, Cortex/XSIAM) and third-party AI stacks. Versions have iterated quickly: Prisma AIRS 2.0 completed native integration of Protect AI; Prisma AIRS 3.0 (~March 2026) targets the agentic AI lifecycle (from observing interactions to authorizing autonomous execution).

**Positioning & differentiators** — Pitched as "the most comprehensive AI security platform," the consolidation play: buy runtime + posture + red-teaming + gateway from one vendor instead of stitching point tools. Nearest neighbors are standalone AI runtime/firewall vendors — [hiddenlayer](hiddenlayer.md), [witnessai](witnessai.md), [pillar-security](pillar-security.md), [cisco-ai-defense](cisco-ai-defense.md) (Cisco's equivalent roll-up from Robust Intelligence), [lakera](lakera.md) (acq. Check Point), [aim-security](aim-security.md) (acq. Cato), [prompt-security](prompt-security.md) (acq. SentinelOne) — and gateway peers like [litellm](litellm.md) and [kong](kong.md).

**Ownership, funding & M&A** — A platform within [palo-alto-networks](palo-alto-networks.md), not an independent company. Built on **Protect AI** (acquisition completed **2025-07-22**; brought model scanning, AI red teaming, posture management, runtime protection, agent security) and **Portkey** (completed **2026-05-29**; the AI Gateway component). Both verified against PANW press releases. The seed flag "incl. former Protect AI" is **confirmed.**

**CTO / hedge-fund lens** — Day-1 if you are deploying customer-facing or agentic LLM apps and need a runtime guardrail / AI firewall. For SR 11-7 / model-risk programs, the model-scanning + red-teaming + posture pieces map to model validation and ongoing monitoring evidence. Strongest fit for shops already on the PANW platform; the consolidation convenience is real, but so is dependence on a single vendor and the integration maturity of recently-acquired components.

**Competitors / alternatives** — [hiddenlayer](hiddenlayer.md), [witnessai](witnessai.md), [pillar-security](pillar-security.md), [cisco-ai-defense](cisco-ai-defense.md), [lakera](lakera.md), [aim-security](aim-security.md), [prompt-security](prompt-security.md), [splxai](splxai.md), [enkrypt-ai](enkrypt-ai.md).

**Open questions / to verify**
- Exact native-integration maturity of Protect AI and Portkey components inside AIRS vs. separately licensed modules.
- Whether AIRS is purchasable standalone or requires broader PANW platform commitment.

**Sources**
- [PANW Completes Acquisition of Protect AI](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-completes-acquisition-of-protect-ai) — fetched 2026-06-28 — supports: Protect AI -> Prisma AIRS, capabilities, close 2025-07-22; confidence: high
- [PANW Completes Acquisition of Portkey](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents) — fetched 2026-06-28 — supports: Portkey is the AIRS AI Gateway, close 2026-05-29; confidence: high
- [Prisma AIRS docs](https://docs.paloaltonetworks.com/ai-runtime-security) — fetched 2026-06-28 — supports: product scope/positioning; confidence: medium (vendor docs/marketing)

## History
- [2026-06-28] Stub created from seed registry.
- [2026-07-27] URL fix: product page moved from `/prisma/prisma-airs` (now hard 404) to `/ai-security/prisma-airs`. Site-nav reorganization only — no rebrand, no ownership change; live page still "Prisma AIRS" with AI Gateway, Agent Security, AI Red Teaming, AI Runtime Security, AI Model Security, AI Posture Management (references AIRS 3.0). Verified 2026-07-27.
- [2026-06-28] Researched; **CONFIRMED** seed flag "incl. former Protect AI" — Protect AI acquisition completed 2025-07-22 and folded into Prisma AIRS (model scanning, red teaming, posture, runtime, agent security). Also established Portkey (closed 2026-05-29) as the AIRS AI Gateway. Set ownership=subsidiary (PANW product), confidence high. Noted version cadence (AIRS 2.0 integrated Protect AI; 3.0 ~Mar 2026 agentic).
