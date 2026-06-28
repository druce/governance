---
type: comparison
name: Survey Blueprint — 42 categories → ~16 questions
slug: survey-blueprint
status: drafted
last_updated: 2026-06-28
confidence: medium
sources_count: 0
---

# Survey blueprint: collapsing 42 categories into a fielding instrument

The wiki keeps **42 fine-grained categories** (good for a buyer's map). A CTO usage/evaluation
survey can't ask 42 questions — respondents fatigue and overlap confuses them. This page is the
**real instrument**: ~16 questions, each mapping to one or more wiki categories, with the answer
shortlist and design notes. Reuse the standard scale on every question:

> **Scale (multi-select per option):** Interested · Considering/evaluating · Pilot/implementing ·
> In production · Would recommend · Would not recommend.

Design rule: **ask about what a fund buys as one decision.** Where the wiki splits for precision
(DSPM vs DLP; the five agent rows), the survey merges or gates with a screener.

## Screener (route the respondent)
- **S1.** Do staff use public/enterprise AI tools today? (yes → everyone gets the core)
- **S2.** Do you do **RAG** over internal data? (gates the retrieval/data questions)
- **S3.** Do you build/run **agents** that take actions? (gates the agent-security questions)
- **S4.** Are you under **SR 11-7 / formal model risk** or heavy allocator DD? (gates governance depth)

## Core questions (everyone)

| # | Question (category) | Maps to wiki | Shortlist (answer options) |
|---|---|---|---|
| Q1 | Enterprise AI assistant | [enterprise-ai-assistant](../categories/enterprise-ai-assistant.md) | ChatGPT Enterprise, Claude Enterprise, M365 Copilot, Gemini Enterprise, Amazon Q, Glean, Perplexity, Other |
| Q2 | AI gateway | [ai-gateway](../categories/ai-gateway.md) | Portkey (Palo Alto), LiteLLM, Kong, TrueFoundry, Cloudflare, F5, OpenRouter, Other |
| Q3 | AI access governance / shadow-AI + prompt DLP | [ai-access-governance](../categories/ai-access-governance.md) + [dlp](../categories/dlp.md) | WitnessAI, Harmonic, Aurascape, Cyberhaven, Nightfall, Prompt Security (SentinelOne), Zscaler/Netskope-native, Other |
| Q4 | AI runtime security (firewall) | [ai-runtime-security](../categories/ai-runtime-security.md) | Prisma AIRS (Palo Alto), HiddenLayer, WitnessAI, Pillar, Cisco AI Defense, Lakera (Check Point), Lasso, Other |
| Q5 | LLM observability & eval | [llm-observability](../categories/llm-observability.md) | Langfuse (ClickHouse), LangSmith, Arize, Braintrust, Datadog, Helicone, Fiddler, Other |
| Q6 | AI governance / model risk | [ai-governance-platform](../categories/ai-governance-platform.md) (+[comms-surveillance](../categories/comms-surveillance.md) sub-q) | Credo AI, Holistic AI, ModelOp, IBM watsonx.governance, OneTrust, Vanta, Monitaur, Other |
| Q7 | AI-aware network security / SASE | [network-security-sase](../categories/network-security-sase.md) | Palo Alto, Zscaler, Netskope, Cloudflare, Cisco, Cato, Forcepoint, Other |

## Data & retrieval (gated by S2 = RAG)

| # | Question | Maps to | Shortlist |
|---|---|---|---|
| Q8 | DSPM + DLP + data-access governance *(one question, note overlap)* | [dspm](../categories/dspm.md) + [dlp](../categories/dlp.md) + [data-access-governance](../categories/data-access-governance.md) | Microsoft Purview, Varonis, Cyera, BigID, Securiti (Veeam), Sentra, Concentric, Immuta, Other |
| Q9 | Entitlement-aware RAG | [entitlement-aware-rag](../categories/entitlement-aware-rag.md) | Glean, Microsoft Graph/Copilot, Knostic, Gemini Enterprise, Amazon Q, Other |

## Agent stack (gated by S3 = agents)

| # | Question | Maps to | Shortlist |
|---|---|---|---|
| Q10 | AI-SPM / agent security *(merges 2 wiki rows)* | [ai-spm](../categories/ai-spm.md) + [agent-runtime-security](../categories/agent-runtime-security.md) | Zenity, Noma, Prisma AIRS, Cranium, Lasso, Operant, Straiker, Other |
| Q11 | Agent authorization & tool/MCP access *(merges 3 wiki rows)* | [authorization-engine](../categories/authorization-engine.md) + [mcp-gateway](../categories/mcp-gateway.md) + [tool-identity-integration](../categories/tool-identity-integration.md) | Cerbos, OPA/Styra, Permit.io, Oso, Kong MCP, Solo.io agentgateway, Arcade, Composio, Other |
| Q12 | Non-human / agent identity | [non-human-identity](../categories/non-human-identity.md) | CyberArk (Palo Alto), Astrix (Cisco, pending), Aembit, Oasis, Token, Natoma (Snowflake), Entro, Clutch, Other |

## Foundation & governance (gated / as relevant)

| # | Question | Maps to | Shortlist |
|---|---|---|---|
| Q13 | Identity & IGA | [identity-access](../categories/identity-access.md) + [identity-governance](../categories/identity-governance.md) | Entra, Okta, Ping, SailPoint, Saviynt, Veza, ConductorOne, Other |
| Q14 | AI SOC / security automation | [ai-soc-analysts](../categories/ai-soc-analysts.md) | Prophet, Dropzone, 7AI, Radiant, Simbian, CrowdStrike Charlotte, Palo Alto AgentiX, Torq, Other |
| Q15 | Comms surveillance (AI-prompt capture) | [comms-surveillance](../categories/comms-surveillance.md) | Behavox, SteelEye, NICE Actimize, Theta Lake, Shield, Relativity Trace, Other |
| Q16 | Enterprise browser / extension | [enterprise-browser](../categories/enterprise-browser.md) + [browser-security-extension](../categories/browser-security-extension.md) | Island, Prisma Access Browser, Menlo, Seraphic, Chrome Enterprise, Edge for Business, LayerX, Other |

## Categories intentionally NOT given their own question
Folded into the above or out of scope for a usage survey:
- **Foundation incumbents** (EDR, SIEM, secrets, SSPM, supply-chain, vendor-risk, GRC, anti-deepfake)
  — mostly "already owned"; ask only if the survey's scope includes the general security estate.
- **AI red-teaming** ([ai-red-teaming](../categories/ai-red-teaming.md)) — fold into Q4/Q5 unless surveying AI *builders*; it's a
  low-fit, developer-tool category for most funds.
- **Retrieval infra** ([content-sources](../categories/content-sources.md), [vector-retrieval](../categories/vector-retrieval.md)) — plumbing, not a governance choice.
- **Process rows** (trust zones, risk tiers, promotion gates, HITL, AUP) — better as maturity
  questions ("do you have a written AUP? risk-tiering? trust-zone design?") than vendor questions.

## Cross-cutting design notes
- **Label acquired options with their parent** — many answer options are now product lines, not
  companies (see [ai-security-m-and-a-map](ai-security-m-and-a-map.md)). A bare "Lakera" or "Portkey" dates the survey.
- **Expect double-counting** where one vendor answers several questions (Palo Alto, Microsoft,
  Cyberhaven, WitnessAI, Lasso, Glean) — reconcile in analysis, not by forcing single-select.
- **Overlap traps to pre-empt:** DSPM↔DLP↔access-governance (Q8); runtime↔red-team (Q4/Q5);
  the five agent rows (Q10/Q11/Q12); assistant↔entitlement-RAG (Q1/Q9).

## History
- [2026-06-28] Created in Phase 4 per taxonomy-gaps Q4 — the fielding instrument behind the 42-category wiki.
