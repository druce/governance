---
title: "Taxonomy"
---

# Taxonomy — canonical category set

**GENERATED from `taxonomy.yaml` by `scripts/gen_taxonomy_md.py` — do not edit by hand.**

`taxonomy.yaml` is the machine source of truth for category slugs, layers,
adoption tiers, and controlled vocabularies (see `SCHEMA.md`). The layer-cake
blog doc remains the spine (Foundation → Data → Model/Prompt → Retrieval → UX →
Governance → Policy/Process); the survey categories map into it.

Legend — **Tier**: `day-1` (before any AI in production) · `day-2` (once
scaling/agents) · `situational` (depends on deployment pattern; see trigger) ·
`firm-type-specific` · `practice` (a process, not a purchase). **Agent-sec** =
`agent_security_context`: the lethal trifecta is a core concern for this
category (SCHEMA.md §0); trifecta framing elsewhere fails editorial lint.

Counts: **42 canonical categories** across 7 layers.

---

## Foundation layer

| slug | display name | tier | agent-sec | trigger | survey question | notes |
|---|---|---|---|---|---|---|
| `identity-access` | Identity & Access (IdP/SSO) | day-1 | — | any users at all — the human + agent front door | General Identity | Entra, Okta, Ping, ForgeRock. |
| `non-human-identity` | Non-Human / Agent Identity Governance | day-2 | — | agents and workloads hold their own credentials and call tools | Non-Human Identity / Agent Identity Governance | NHI: secrets-less workload + agent identity. CyberArk, Astrix, Aembit, Oasis, Token, Natoma, Entro, Clutch. |
| `identity-governance` | Identity Governance & Visibility (IGA / ISPM) | day-2 | — | enough headcount/apps that joiner-mover-leaver and access certs need automation | Identity Governance & Visibility (IGA / ISPM) | SailPoint, Saviynt, Veza, CyberArk, C1 (ex-ConductorOne), Lumos, Linx, Hydden. |
| `secrets-management` | Secrets Manager | day-1 | — | any code or agent that authenticates to anything | Secrets Manager | Vaulting + rotation. Key Vault, HashiCorp Vault, AWS/GCP, Conjur, 1Password, Doppler, Infisical. |
| `siem-soc` | Enterprise Logging / SIEM / SOC | day-1 | — | table stakes — you cannot investigate what you did not log | SIEM/SOAR/SecOps | Sentinel, Splunk, Cortex XSIAM, Sumo, ELK, Google SecOps, LogScale. |
| `ai-soc-analysts` | AI SecOps / Agentic SOC Analysts | day-2 | — | SOC alert volume outgrows analyst headcount | AI SOC analysts | Merges doc 'AI SecOps' + CSV 'AI SOC analysts' (same vendors). Prophet, Dropzone, 7AI, Radiant, Simbian, Charlotte, Cortex AgentiX, Jazz, Torq. |
| `edr-xdr` | EDR / XDR | day-1 | — | table stakes — usually already deployed | EDR / XDR | CrowdStrike, Defender, SentinelOne, Cortex XDR. |
| `network-security-sase` | Network Security / SASE (SSE) | day-1 | — | table stakes — the TLS-inspecting egress path AI traffic rides on | AI-aware Network Security (SSE/SASE) | Palo Alto, Zscaler, Netskope, Cloudflare, Cisco, Cato, Forcepoint. |
| `sspm` | SaaS Security Posture Management (SSPM) | day-2 | — | SaaS sprawl — many third-party apps with OAuth grants into your tenant | SaaS Security Posture Management (SSPM) | AppOmni, Obsidian, Adaptive Shield, Grip, Valence, Wing, DoControl. |
| `software-supply-chain` | Software Supply Chain & Coding Security | day-2 | — | shipping code; day-1 if shipping AI-generated code | Software supply chain | Snyk, Semgrep, Endor, Socket, Apiiro, Legit, Aikido, Sonatype, JFrog, GitHub AS, GitLab. |
| `anti-deepfake` | Security Awareness / Anti-Deepfake | day-2 | — | wire-transfer authority + voice/video approval workflows = deepfake exposure | AI Antiphishing/deepfake/social engineering defense | Adaptive, Doppel, Reality Defender, GetReal, Pindrop. |

## Data layer

| slug | display name | tier | agent-sec | trigger | survey question | notes |
|---|---|---|---|---|---|---|
| `dspm` | Data Classification & DSPM | day-1 | — | before AI touches internal data you must know what/where the sensitive data is | DSPM / Data Security Posture | Purview, BigID, Securiti, Cyera, Sentra, Normalyze, Wiz DSPM, Concentric, Bedrock, Immuta, Collibra. |
| `dlp` | Data Loss Prevention (DLP) | day-1 | — | employees can paste sensitive data into anything with a text box | Data Loss Prevention (DLP) | Cyberhaven, Nightfall, MIND, Prompt Security, Lasso, Netskope/Purview DLP. CSV merged DSPM+DLP; we keep the split. |
| `data-access-governance` | Data Access Governance | day-2 | — | day-1 if doing RAG over internal permissioned data | Data Access Governance | Varonis, SailPoint DAS, Cyera, Sentra, Concentric, Veza, C1 (ex-ConductorOne), Silverfort, Netwrix. |

## AI model & prompt layer

| slug | display name | tier | agent-sec | trigger | survey question | notes |
|---|---|---|---|---|---|---|
| `ai-runtime-security` | AI Runtime Security (AI Firewall) | day-1 | ✓ | any self-built LLM app in front of users or data (governed vendor assistants can lag slightly) | AI Runtime Security / AI Firewall | Prisma AIRS, HiddenLayer, WitnessAI, Pillar, Cisco AI Defense, SplxAI, Aim, Lasso, Enkrypt, CalypsoAI, Lakera, Prompt Security, TrojAI. |
| `ai-gateway` | AI Gateway | day-1 | — | any LLM API traffic beyond a single vendor SDK | AI Gateway | Single exit door for model traffic. Portkey, LiteLLM, Kong, F5, Cloudflare, TrueFoundry, OpenRouter. |
| `llm-observability` | LLM Observability & Evaluation | day-1 | — | any LLM feature you need to debug, evaluate, or show evidence for | LLM Observability & Eval | Langfuse, LangSmith, Arize Phoenix, Helicone, Braintrust, Datadog, W&B Weave, Comet Opik, Fiddler, TruLens. |
| `ai-red-teaming` | AI Red Teaming / Guardrails | day-2 | — | self-built AI apps worth adversarially testing before and after launch | AI Red Teaming / Guardrails | Offensive testing vs runtime guardrails bundled here — scope-boundary note required. Mindgard, SplxAI, Promptfoo, HiddenLayer, Lakera, Guardrails AI, NeMo Guardrails, Galileo, Patronus, Pangea, Maxim, Haize. |
| `ai-access-governance` | AI Access Governance (CASB for AI) / Shadow-AI | day-1 | — | employees using third-party AI tools (i.e., immediately) | Shadow-AI / Insider risk | Governs employees using AI; runtime security protects AI you build. WitnessAI, Harmonic, Aurascape, Nudge, Lanai, Cyberhaven, Wald.ai, Portal26, Zscaler AI Guard, Netskope One, Reco. |
| `ai-spm` | AI-SPM (AI Security Posture Management) | day-2 | — | enough AI assets/agents that you need an inventory and posture view | AI-SPM (AI estate inventory & posture) | Discover/inventory/govern AI assets & agents. Noma, Wiz AI-SPM, Prisma AIRS, Cranium, Quilr, Zenity, Reco, Nudge, Torq. |
| `agent-runtime-security` | Agent Security (Runtime) | day-2 | ✓ | agents act autonomously with tool access — untrusted input meets real permissions | Agent Security (runtime protection of agents) | Runtime protection of agentic apps. Zenity, Lasso, Operant, Apex (acq. Tenable), Straiker, Knostic (repositioned 2026). |
| `authorization-engine` | Authorization Engine (Agent / Tool) | day-2 | ✓ | agents or apps need fine-grained, externalized authorization decisions | Authorization Engine (Agent / Tool) | Fine-grained externalized authz. Cerbos, OPA, Styra, Permit.io, AuthZed/SpiceDB, Oso. |
| `mcp-gateway` | MCP Gateway / Tool Access Control | day-2 | ✓ | agents call tools via MCP; the tool path needs a policy choke point | MCP Gateway / Tool Access Control | Kong MCP, agentgateway (Solo.io), Arcade, TrueFoundry MCP, Obot, MintMCP, IBM ContextForge, Docker MCP, Pomerium, Prisma AIRS Agent Gw. |
| `tool-identity-integration` | Tool Identity & Integration | day-2 | ✓ | agents authenticate to SaaS on users' behalf — managed connectors + agent auth | Tool Identity & Integration (Agent Auth) | Composio, StackOne, Arcade, CyberArk, Descope, Stytch, WorkOS. |

## Retrieval layer

| slug | display name | tier | agent-sec | trigger | survey question | notes |
|---|---|---|---|---|---|---|
| `content-sources` | Enterprise Content Sources | situational | — | doing RAG over internal documents | — | SharePoint, OneDrive, Confluence, Google Drive. Infra, not a survey shortlist. |
| `vector-retrieval` | Vector Retrieval | situational | — | doing RAG | — | Azure AI Search, Pinecone, Weaviate, OpenSearch. |
| `entitlement-aware-rag` | Entitlement-Aware RAG | situational | — | non-negotiable if doing RAG over internal permissioned data | Entitlement-Aware RAG / Retrieval Permissions | Glean, Microsoft Graph, Knostic. |

## User experience layer

| slug | display name | tier | agent-sec | trigger | survey question | notes |
|---|---|---|---|---|---|---|
| `enterprise-ai-assistant` | Enterprise AI Assistant | day-1 | — | the chatbot people actually use — first AI purchase for most firms | Enterprise AI Assistant | ChatGPT Enterprise, Claude Enterprise, M365 Copilot, Gemini Enterprise, Amazon Q, Perplexity, Glean. |
| `third-party-ai-apps` | Third-Party AI Apps | practice | — | domain AI tools adopted outside the core assistant — route via the gateway | — | Process/architecture pattern, not a single shortlist. |
| `enterprise-browser` | Enterprise Browser | situational | ✓ | BYOD / contractor access, or browser-level AI controls beyond SASE | Enterprise Browser Security | Island, Prisma Access Browser, Menlo, Seraphic, Red Access, Chrome Enterprise Premium, Edge for Business. |
| `browser-security-extension` | Browser Security Extension | situational | ✓ | want browser-level AI/data controls without replacing Chrome | Enterprise Browser Security | Bolt-on to existing Chrome. LayerX, Material, Grip. Often either/or with enterprise browser. |

## Governance layer

| slug | display name | tier | agent-sec | trigger | survey question | notes |
|---|---|---|---|---|---|---|
| `ai-governance-platform` | AI Governance / Model Risk & Compliance | firm-type-specific | — | day-1 for bank-affiliated / model-validation-mandated (SR 11-7) firms; day-2 otherwise | AI Governance, Model Risk & Compliance | Credo AI, Holistic AI, ModelOp, Fairly AI (now Asenion), Monitaur, IBM watsonx.governance, Vanta, CalypsoAI, GovernGPT. |
| `enterprise-grc` | Enterprise GRC | day-1 | — | usually already owned — extend existing GRC to AI risk | Enterprise Governance, Risk & Compliance | ServiceNow GRC, Archer, LogicGate, Optro (ex-AuditBoard), OneTrust, Onspring, Vanta, Drata. |
| `vendor-risk` | Third-Party / Vendor Risk + Cyber Ratings | day-1 | — | extend existing TPRM to AI vendors and AI features of existing vendors | Vendor Risk Rating & Monitoring | ProcessUnity, SecurityScorecard, BitSight, Black Kite, UpGuard, Venminder, Whistic. |
| `comms-surveillance` | Comms Surveillance | firm-type-specific | — | registered advisers / regulated comms (MAR/MNPI) — hedge-fund-critical | Comms Surveillance | Surveillance/analysis, NOT capture/archival — scope-boundary note required. Behavox, SteelEye, NICE Actimize, Theta Lake, Shield, Relativity Trace. |
| `ephemeral-environments` | Ephemeral Environments | practice | — | underpins trust-zone design — disposable compute for risky AI work | — | GitHub Codespaces, Azure Dev Boxes, Terraform Cloud, Cloudflare Workers. |
| `policy-as-code` | Policy-as-Code | day-2 | — | guardrails you want enforced by software, not documents | — | OPA, HashiCorp Sentinel, Kyverno. |

## Policy / process layer

| slug | display name | tier | agent-sec | trigger | survey question | notes |
|---|---|---|---|---|---|---|
| `trust-zone-segmentation` | Trust Zone Segmentation | practice | ✓ | the organizing idea — red/yellow/green zones for agentic AI | — | Zone design keeps untrusted input, sensitive data, and egress from combining in one agent context. |
| `risk-tiers` | Risk Tiers | practice | — | classify AI use cases by stakes before controls can be proportionate | — | Classify AI use cases by stakes. |
| `promotion-gates` | Promotion Gates | practice | — | CI/CD sign-off between experiment and production | — | Sign-off between experiment and production. |
| `hitl-approvals` | HITL Approvals | practice | — | human-in-the-loop on consequential agent actions | — | Human sign-off on consequential agent actions. |
| `acceptable-use-policies` | Acceptable Use Policies | practice | — | the cheapest control there is — write it down first | — | The cheapest control there is. |

---

## Bundled CSV entries split into separate vendor pages

Per CLAUDE.md §3. Recorded in `log.md`.

- `1Password / Doppler / Infisical` → `1password`, `doppler`, `infisical`
- `OPA / Styra` → `open-policy-agent` (project) + `styra` (commercial company)
- `Immuta / Collibra` → `immuta`, `collibra`
- `Obot / MintMCP` → `obot`, `mintmcp`
- `Promptfoo (acq. by OpenAI)` → `promptfoo`

## Cross-listed vendors (one page, multiple categories)

Notable multi-category vendors: Palo Alto Networks (Prisma AIRS, Cortex, Prisma
Access, Portkey), CyberArk (NHI, IGA, secrets, tool-identity), HiddenLayer
(runtime + red-teaming), Cyberhaven (DLP + shadow-AI), WitnessAI (runtime +
access-governance), Lasso (runtime + agent + DLP), Zenity (AI-SPM +
agent-runtime), Veza (IGA + data-access-governance), OneTrust (GRC + governance
+ DSPM), Reco / Nudge Security (AI-SPM + shadow-AI), Wiz (DSPM + AI-SPM), Glean
(assistant + entitlement-aware-RAG).
