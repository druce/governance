# Taxonomy — canonical category set

Source of truth for category **slugs**, layer mapping, and priority. The
**layer-cake blog doc is the spine** (Foundation → Data → Model/Prompt → Retrieval →
UX → Governance → Policy/Process). The **CSV survey categories map into it.** Where the
two disagree or a cleaner cut exists, the decision is recorded here and in
[taxonomy-gaps.md](taxonomy-gaps.md) + `log.md`.

Legend — **Priority**: `day-1` (stand up before go-live) · `day-2` (after the basics) ·
`optional` · `process` (a practice, not a product). **Seed-doc row** = the layer-cake
table row this reconciles. **Seed-CSV** = the survey question it reconciles (`—` = not in
that seed).

Counts: **42 canonical categories** across 7 layers. 23 CSV survey questions + 40 doc rows
reconciled. `Other (Please Specify)` rows are survey UI, not vendors — excluded.

---

## Foundation layer

| slug | display name | priority | seed-doc row | seed-CSV | notes |
|---|---|---|---|---|---|
| `identity-access` | Identity & Access (IdP/SSO) | day-1 | Identity & Access | General Identity | Entra, Okta, Ping, ForgeRock. The human+agent front door. |
| `non-human-identity` | Non-Human / Agent Identity Governance | day-2 | (folded into Identity & Access + Tool Identity) | Non-Human Identity / Agent Identity Governance | NHI: secrets-less workload+agent identity. CyberArk, Astrix, Aembit, Oasis, Token, Natoma, Entro, Clutch. |
| `identity-governance` | Identity Governance & Visibility (IGA / ISPM) | day-2 | (folded into Identity & Access + Data Access Gov) | Identity Governance & Visibility (IGA / ISPM) | Joiner/mover/leaver, access certs. SailPoint, Saviynt, Veza, CyberArk, ConductorOne, Lumos, Linx, Hydden. |
| `secrets-management` | Secrets Manager | day-1 | Secrets Manager | Secrets Manager | Vaulting + rotation. Key Vault, HashiCorp Vault, AWS/GCP, Conjur, 1Password/Doppler/Infisical. |
| `siem-soc` | Enterprise Logging / SIEM / SOC | day-1 | Enterprise logging / SIEM / SOC | SIEM/SOAR/SecOps | Sentinel, Splunk, Cortex XSIAM, Sumo, ELK, Google SecOps, LogScale. |
| `ai-soc-analysts` | AI SecOps / Agentic SOC analysts | day-2 | AI SecOps, Security Automation | AI SOC analysts | Merges doc "AI SecOps" + CSV "AI SOC analysts" (same vendors). Prophet, Dropzone, 7AI, Radiant, Simbian, Charlotte, Cortex AgentiX, Jazz, Torq. |
| `edr-xdr` | EDR / XDR | day-1 | EDR / XDR | EDR | CrowdStrike, Defender, SentinelOne, Cortex XDR. Usually already deployed. |
| `network-security-sase` | Network Security / SASE (SSE) | day-1 | Network Security / SASE | AI-aware Network Security (SSE/SASE) | TLS-inspecting man-in-the-middle. Palo Alto, Zscaler, Netskope, Cloudflare, Cisco, Cato, Forcepoint. |
| `sspm` | SaaS Security Posture Management | day-2 | SaaS Security Posture (SSPM) | — (doc-only) | AppOmni, Obsidian, Adaptive Shield, Grip, Valence, Wing, DoControl. |
| `software-supply-chain` | Software Supply Chain & Coding Security | day-2 | Software Supply Chain & Coding Security | Software supply chain | Day-1 if shipping AI-generated code. Snyk, Semgrep, Endor, Socket, Apiiro, Legit, Aikido, Sonatype, JFrog, GitHub AS, GitLab. |
| `anti-deepfake` | Security Awareness / Anti-Deepfake | day-2 | Security Awareness / Anti-Deepfake | AI Antiphishing/deepfake/social engineering defense | Adaptive, Doppel, Reality Defender, GetReal, Pindrop. |

## Data layer

| slug | display name | priority | seed-doc row | seed-CSV | notes |
|---|---|---|---|---|---|
| `dspm` | Data Classification & DSPM | day-1 | Data Classification & DSPM | DSPM / Data Governance / DLP (split) | Purview, BigID, Securiti, Cyera, Sentra, Normalyze, Wiz DSPM, Concentric, Bedrock, Immuta, Collibra. |
| `dlp` | Data Loss Prevention (DLP) | day-1 | Data Loss Prevention (DLP) | DSPM / Data Governance / DLP (split) | Cyberhaven, Nightfall, MIND, Prompt Security, Lasso, Netskope/Purview DLP. CSV merges DSPM+DLP; we keep split per spine. |
| `data-access-governance` | Data Access Governance | day-2 | Data Access Governance | (overlaps IGA) | Day-1 if doing RAG. Varonis, SailPoint DAS, Cyera, Sentra, Concentric, Veza, ConductorOne, Silverfort, Netwrix. |

## AI model & prompt layer

| slug | display name | priority | seed-doc row | seed-CSV | notes |
|---|---|---|---|---|---|
| `ai-runtime-security` | AI Runtime Security (AI Firewall) | day-1 | AI Runtime Security (AI Firewall) | AI Runtime Security / AI Firewall | Prisma AIRS, HiddenLayer, WitnessAI, Pillar, Cisco AI Defense, SplxAI, Aim, Lasso, Enkrypt, CalypsoAI, Lakera, Prompt Security, TrojAI. |
| `ai-gateway` | AI Gateway | day-1 | AI Gateway | AI Gateway | Single exit door for model traffic. Portkey, LiteLLM, Kong, F5, Cloudflare, TrueFoundry, OpenRouter. |
| `llm-observability` | LLM Observability & Evaluation | day-1 | LLM Observability & Evaluation | LLM Observability & Eval | Langfuse, LangSmith, Arize Phoenix, Helicone, Braintrust, Datadog, W&B Weave, Comet Opik, Fiddler, TruLens. |
| `ai-red-teaming` | AI Red Teaming / Guardrails | day-2 | (folded into LLM Obs "red-teaming") | AI Red Teaming / Guardrails | CSV-only cut. Mindgard, SplxAI, Promptfoo, HiddenLayer, Lakera, Guardrails AI, NeMo Guardrails, Galileo, Patronus, Pangea, Maxim, Haize. |
| `ai-access-governance` | AI Access Governance (CASB for AI) / Shadow-AI | day-1 | AI Access Governance (CASB for AI) | Shadow-AI / Insider risk | Merges doc + CSV (same job, two names). WitnessAI, Harmonic, Aurascape, Nudge, Lanai, Cyberhaven, Wald.ai, Portal26, Zscaler AI Guard, Netskope One, Reco. |
| `ai-spm` | AI-SPM (AI Security Posture Mgmt) | day-2 | AI-SPM / Agent Governance | AI-SPM | Discover/inventory/govern AI assets & agents. Noma, Wiz AI-SPM, Prisma AIRS, Cranium, Quilr, Zenity, Reco, Nudge, Torq. |
| `agent-runtime-security` | Agent Security (runtime) | day-2 | (folded into AI-SPM / Agent Gov) | Agent Security | CSV-only cut; runtime protection of agentic apps. Zenity, Lasso, Operant, Apex (acq. Tenable), Straiker. |
| `authorization-engine` | Authorization Engine (Agent / Tool) | day-2 | Authorization Engine (Agent / Tool) | MCP / Agent Gateway & Tool Access (split) | Fine-grained externalized authz. Cerbos, OPA, Styra, Permit.io, AuthZed/SpiceDB, Oso. |
| `mcp-gateway` | MCP Gateway / Tool Access Control | day-2 | MCP Gateway / Tool Access Control | MCP / Agent Gateway & Tool Access (split) | Kong MCP, agentgateway (Solo.io), Arcade, TrueFoundry MCP, Obot, MintMCP, IBM ContextForge, Docker MCP, Pomerium, Prisma AIRS Agent Gw. |
| `tool-identity-integration` | Tool Identity & Integration | day-2 | Tool Identity & Integration Layer | MCP / Agent Gateway & Tool Access (split) | Managed agent→SaaS connectors + agent auth. Composio, StackOne, Arcade, CyberArk, Descope, Stytch, WorkOS. |

## Retrieval layer

| slug | display name | priority | seed-doc row | seed-CSV | notes |
|---|---|---|---|---|---|
| `content-sources` | Enterprise Content Sources | day-1* | Content Sources | (in Enterprise Chat & RAG) | *if doing RAG. SharePoint, OneDrive, Confluence, Google Drive. Infra, not a survey shortlist. |
| `vector-retrieval` | Vector Retrieval | day-1* | Vector Retrieval | — (doc-only) | *if doing RAG. Azure AI Search, Pinecone, Weaviate, OpenSearch. |
| `entitlement-aware-rag` | Entitlement-Aware RAG | day-1* | Entitlement-Aware RAG | (in Enterprise Chat & RAG) | *non-negotiable if doing RAG. Glean, Microsoft Graph, Knostic. |

## User experience layer

| slug | display name | priority | seed-doc row | seed-CSV | notes |
|---|---|---|---|---|---|
| `enterprise-ai-assistant` | Enterprise AI Assistant | day-1 | Enterprise AI Assistant | Enterprise Chat & RAG | ChatGPT Enterprise, Claude Enterprise, M365 Copilot, Gemini Enterprise, Amazon Q, Perplexity, Glean. The chatbot people actually use. |
| `third-party-ai-apps` | Third-Party AI Apps | optional | Third-Party AI Apps | — (doc-only) | Domain AI tools routed via the gateway. Process/architecture, not a single shortlist. |
| `enterprise-browser` | Enterprise Browser | optional | Enterprise Browser | Enterprise Browser | Island, Prisma Access Browser, Menlo, Seraphic, Red Access, Chrome Enterprise Premium, Edge for Business. |
| `browser-security-extension` | Browser Security Extension | optional | Browser Security Extension | (in Enterprise Browser) | Bolt-on to existing Chrome. LayerX, Material, Grip. Often either/or with enterprise browser. |

## Governance layer

| slug | display name | priority | seed-doc row | seed-CSV | notes |
|---|---|---|---|---|---|
| `ai-governance-platform` | AI Governance / Model Risk & Compliance | day-2 | AI Governance Platform | AI Governance, Model Risk & Compliance | Day-1 under SR 11-7. Credo AI, Holistic AI, ModelOp, Fairly AI, Monitaur, IBM watsonx.governance, Vanta, CalypsoAI, GovernGPT. |
| `enterprise-grc` | Enterprise GRC | day-1 | Enterprise GRC | Enterprize GRC | ServiceNow GRC, Archer, LogicGate, AuditBoard, OneTrust, Onspring. Usually already owned. |
| `vendor-risk` | Third-Party / Vendor Risk + Cyber Ratings | day-1 | Third-Party / Vendor Risk + Cyber Ratings | Vendor Risk | ProcessUnity, SecurityScorecard, BitSight, Black Kite, UpGuard. Extend TPRM to AI vendors. |
| `comms-surveillance` | Comms Surveillance | day-2 | Comms Surveillance | (in AI Governance, Model Risk) | Hedge-fund-critical (MAR/MNPI). Behavox, SteelEye, NICE Actimize, Theta Lake, Shield, Relativity Trace. |
| `ephemeral-environments` | Ephemeral Environments | day-2 | Ephemeral Environments | — (doc-only) | GitHub Codespaces, Azure Dev Boxes, Terraform Cloud, Cloudflare Workers. Underpins trust-zone design. |
| `policy-as-code` | Policy-as-Code | day-2 | Policy-as-Code | (OPA appears in MCP/Agent) | OPA, HashiCorp Sentinel, Kyverno. Guardrails as software. |

## Policy / process layer

These are practices, not products. Thin pages; **no survey scaffolding** for pure-process rows.

| slug | display name | priority | seed-doc row | seed-CSV | notes |
|---|---|---|---|---|---|
| `trust-zone-segmentation` | Trust Zone Segmentation | process | Trust Zone Segmentation | — | Red/yellow/green zones break the lethal trifecta. The spine's organizing idea. |
| `risk-tiers` | Risk Tiers | process | Risk Tiers | — | Classify AI use cases by stakes. |
| `promotion-gates` | Promotion Gates | process | Promotion Gates | — | CI/CD sign-off between experiment and production. |
| `hitl-approvals` | HITL Approvals | process | HITL Approvals | — | Human-in-the-loop on consequential agent actions. |
| `acceptable-use-policies` | Acceptable Use Policies | process | Acceptable Use Policies | — | The cheapest control there is. |

---

## Bundled CSV entries split into separate vendor pages

Per CLAUDE.md §3. Recorded in `log.md`.

- `1Password / Doppler / Infisical` → `1password`, `doppler`, `infisical`
- `OPA / Styra` → `open-policy-agent` (project) + `styra` (commercial company)
- `Immuta / Collibra` → `immuta`, `collibra`
- `Obot / MintMCP` → `obot`, `mintmcp`
- `Promptfoo (acq. by OpenAI)` → `promptfoo`

## Cross-listed vendors (one page, multiple categories)

Notable multi-category vendors (full list emerges in Phase 2): Palo Alto Networks
(Prisma AIRS, Cortex, Prisma Access, Portkey, CyberArk), CyberArk (NHI, IGA, secrets,
tool-identity), HiddenLayer (runtime + red-teaming), Cyberhaven (DLP + shadow-AI),
WitnessAI (runtime + access-governance), Lasso (runtime + agent + DLP), Zenity (AI-SPM +
agent-runtime), Veza (IGA + data-access-governance), OneTrust (GRC + governance + DSPM),
Reco / Nudge Security (AI-SPM + shadow-AI), Wiz (DSPM + AI-SPM), Glean (assistant +
entitlement-aware-RAG).
