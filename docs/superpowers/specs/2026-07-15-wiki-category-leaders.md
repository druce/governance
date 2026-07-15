# Governance-wiki product categories with leading examples

Extracted 2026-07-15 from the governance wiki's 42 category pages. "Leaders" are the
1–2 vendors **each category page itself identifies** (cues: "table-stakes,"
"incumbent," "most-recognized"), as of the wiki's last verification (mostly
2026-06-28). Six categories are practices with no products, by design.

Companion to `2026-07-15-citizen-dev-primer-design.md` — seed for Appendix D (dated
tool shortlist) and the Ch 7 / Ch 12 crosswalk.

## Foundation layer

| Category | Tier | Leading examples |
|---|---|---|
| Identity & Access (IdP/SSO) | day-1 | Microsoft Entra ID; Okta |
| Secrets Manager | day-1 | Azure Key Vault; HashiCorp Vault |
| SIEM / SOC | day-1 | Microsoft Sentinel; Splunk |
| EDR / XDR | day-1 | CrowdStrike; Microsoft Defender |
| Network Security / SASE | day-1 | Palo Alto Networks; Zscaler |
| Identity Governance (IGA/ISPM) | day-2 | SailPoint; Saviynt |
| Non-Human / Agent Identity | day-2 | CyberArk; Astrix Security |
| SSPM | day-2 | AppOmni; Obsidian Security |
| Software Supply Chain | day-2 | Snyk; GitHub Advanced Security |
| AI SecOps / Agentic SOC | day-2 | Prophet Security; CrowdStrike Charlotte AI |
| Anti-Deepfake / Awareness | day-2 | Adaptive Security; Reality Defender |

## Data layer

| Category | Tier | Leading examples |
|---|---|---|
| DSPM / Data Classification | day-1 | Microsoft Purview; Cyera |
| DLP | day-1 | Microsoft Purview; Cyberhaven |
| Data Access Governance | day-2 | Varonis (page names no clear #2 — "category archetype") |

## Model & prompt layer

| Category | Tier | Leading examples |
|---|---|---|
| AI Gateway | day-1 | LiteLLM (OSS default); Portkey |
| AI Runtime Security (AI Firewall) | day-1 | Prisma AIRS; HiddenLayer |
| AI Access Governance / Shadow-AI | day-1 | WitnessAI; Harmonic Security |
| LLM Observability & Eval | day-1 | Langfuse; LangSmith |
| AI Red Teaming / Guardrails | day-2 | Mindgard; Guardrails AI (weak cues — OSS-skewed, no anchor) |
| AI-SPM | day-2 | Noma; Wiz |
| Agent Security (Runtime) | day-2 | Zenity; Lasso Security (nascent) |
| Authorization Engine | day-2 | Open Policy Agent; Styra |
| MCP Gateway / Tool Access | day-2 | Solo.io agentgateway; Kong (very new, no production anchor) |
| Tool Identity & Integration | day-2 | Composio; Descope (nascent) |

## Retrieval layer

| Category | Tier | Leading examples |
|---|---|---|
| Entitlement-Aware RAG | situational | Glean; Microsoft Graph (as Copilot's substrate) |
| Enterprise Content Sources | situational | SharePoint; Google Drive (stub — infrastructure, not a shortlist) |
| Vector Retrieval | situational | Azure AI Search; Pinecone (stub) |

## UX layer

| Category | Tier | Leading examples |
|---|---|---|
| Enterprise AI Assistant | day-1 | ChatGPT Enterprise; Microsoft 365 Copilot |
| Enterprise Browser | situational | Island; Prisma Access Browser |
| Browser Security Extension | situational | LayerX; Grip Security |
| Third-Party AI Apps | practice | no products — process category |

## Governance layer

| Category | Tier | Leading examples |
|---|---|---|
| Enterprise GRC | day-1 | ServiceNow; Archer |
| Vendor Risk / Cyber Ratings | day-1 | BitSight; SecurityScorecard |
| AI Governance / Model Risk | firm-specific | Credo AI; ModelOp (fragmented, no dominant player) |
| Comms Surveillance | firm-specific | Behavox; NICE Actimize |
| Policy-as-Code | day-2 | Open Policy Agent; Styra |
| Ephemeral Environments | practice* | GitHub Codespaces; Azure Dev Boxes (*practice-tier but carries vendors) |

## Policy layer — practices, no products

Trust Zone Segmentation · Risk Tiers · Promotion Gates · HITL Approvals · Acceptable Use Policies

---

## Mapping to the citizen-dev primer

Not all 42 belong in the document at equal depth:

- **Load-bearing for Ch 7 (reference architecture):** identity-access,
  secrets-management, ai-gateway, llm-observability, dspm, dlp,
  data-access-governance, entitlement-aware-rag, software-supply-chain,
  ephemeral-environments — plus the five policy-layer practices, which are
  literally Ch 5.
- **Enters when citizen builds go agentic (Ch 9 Run/Fly stages):** mcp-gateway,
  authorization-engine, agent-runtime-security, tool-identity-integration,
  non-human-identity.
- **Background the program inherits rather than discusses:** EDR/XDR, SASE, SIEM,
  SSPM, GRC, vendor-risk, comms-surveillance, anti-deepfake, AI-SOC,
  enterprise-browser categories.

## Caveats

- Leaders reflect the wiki's June-2026 snapshot; **re-verify before names go in the
  published primer** (per the spec's verification flag).
- Several categories are explicitly nascent or M&A-churned: Portkey carries an
  unverified acquired-by-Palo-Alto flag; the wiki's M&A map notes much of the
  runtime/guardrail field is now inside platforms (Palo Alto, Cisco, CrowdStrike,
  SentinelOne, F5, Zscaler, Check Point, Cato).
- Weak-cue categories (page names no clear leader): anti-deepfake, ai-red-teaming,
  mcp-gateway, tool-identity-integration, agent-runtime-security,
  ai-governance-platform, ai-soc-analysts, ephemeral-environments.
