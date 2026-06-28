---
type: comparison
name: AI-Security M&A Map (2023–2026)
slug: ai-security-m-and-a-map
status: drafted
last_updated: 2026-06-28
confidence: medium
sources_count: 25
---

# The AI-security M&A map (2023–2026)

Who bought whom in the AI governance/security landscape, **verified against primary sources**
(acquirer press releases, SEC filings) during the Phase 3 research pass. Dates and confidence
are explicit. This page is the filed-back answer to "which of these vendors is still
independent, and who owns the rest?" — the question that dates half a survey's answer options.

> Convention: **closed** = completion confirmed by a primary source with a date. **announced /
> pending** = agreement public but no completion source found as of 2026-06-28. Deal values are
> marked *reported* when press-sourced rather than officially disclosed.

## The platform roll-ups (who is consolidating)

### Palo Alto Networks — building the AI-security platform by acquisition
| Target | What it brought | Status | Date | Value |
|---|---|---|---|---|
| [cyberark](../vendors/cyberark.md) | Privileged access + machine/NHI identity | **Closed** | 2026-02-11 | ~$25B |
| [portkey](../vendors/portkey.md) | AI gateway (now the Prisma AIRS gateway component) | **Closed** | 2026-05-29 | undisclosed |
| Protect AI → [prisma-airs](../vendors/prisma-airs.md) | Model scanning, red-teaming, posture, runtime | **Closed** | 2025-07-22 | reported ~$650–700M |
| Talon → [prisma-access-browser](../vendors/prisma-access-browser.md) | Enterprise browser | **Closed** | 2023-12-28 | reported ~$625M |

PANW is assembling identity ([cyberark](../vendors/cyberark.md)) + AI gateway ([portkey](../vendors/portkey.md)) + AI runtime/posture
([prisma-airs](../vendors/prisma-airs.md)) + browser under one roof. For a CTO this means several formerly-independent
"best of breed" tools now arrive as one suite — fewer throats to choke, more lock-in.

### Cisco — buying the AI trust & SOC layer
| Target | What it brought | Status | Date | Value |
|---|---|---|---|---|
| [splunk](../vendors/splunk.md) | SIEM / observability | **Closed** | 2024-03-18 | $28B |
| Robust Intelligence → [cisco-ai-defense](../vendors/cisco-ai-defense.md) | AI runtime security / validation | **Closed** | ~2024-09-24 | undisclosed |
| [galileo](../vendors/galileo.md) | LLM eval / guardrails | Closed (reported) | ~2026-05-22 | undisclosed |
| [astrix-security](../vendors/astrix-security.md) | Non-human / agent identity | **Announced intent — pending** | 2026-05-04 | reported ~$400M |

> Note: the seed listed Astrix as "acquired"; as of 2026-06-28 it is **announced intent, not
> closed**. Treat as pending.

### CrowdStrike — adding SaaS posture + AI detection/response
| Target | What it brought | Status | Date | Value |
|---|---|---|---|---|
| [pangea](../vendors/pangea.md) | AI detection & response (AIDR) / guardrails | **Closed** | ~2025-09 (announced 2025-09-16) | reported ~$260M |
| [adaptive-shield](../vendors/adaptive-shield.md) | SaaS security posture (SSPM) | **Closed** | ~2025-01 (announced 2024-11-06) | reported ~$300M |
| Charlotte AI | Agentic SOC (built in-house, not acquired) | — | — | — |

### SentinelOne
| Target | What it brought | Status | Date | Value |
|---|---|---|---|---|
| [prompt-security](../vendors/prompt-security.md) | Prompt-layer DLP / AI runtime | **Closed** | ~2025-11 (announced 2025-08-05) | reported ~$250M |

### F5
| Target | What it brought | Status | Date | Value |
|---|---|---|---|---|
| [calypsoai](../vendors/calypsoai.md) | AI guardrails + red-team (now F5 AI Guardrails / AI Red Team) | **Closed** | 2025-10-08 | reported ~$180M |

### Other notable AI-security tuck-ins
| Target | Acquirer | What it brought | Status | Date | Value |
|---|---|---|---|---|---|
| [aim-security](../vendors/aim-security.md) | [cato-networks](../vendors/cato-networks.md) | AI/agent security (Cato's first acquisition) | Announced | 2025-09-03 | reported ~$350M |
| [lakera](../vendors/lakera.md) | Check Point | AI guardrails / prompt-injection defense | Announced (close exp. Q4 2025) | 2025-09-16 | reported ~$300M |
| [apex-security](../vendors/apex-security.md) | Tenable | Agent/AI security → Tenable One | Announced/integrating | 2025-05-29 | reported >$105M |
| [promptfoo](../vendors/promptfoo.md) | OpenAI | Open-source eval/red-team → OpenAI Frontier | **Closed** | 2026-03-09 | undisclosed |
| [trojai](../vendors/trojai.md) | A10 Networks | AI detect (red-team) + defend (runtime firewall) | **Announced** | 2026-06-15 | undisclosed |

> **TrojAI→A10 Networks was NOT in the seed CSV** — surfaced during research. A recent (2026-06-15)
> deal; confirm completion.

## Deals surfaced *during research* — NOT in the seed CSV

These were not flagged in the seed; the research pass found and verified them. They materially
date several survey answer options.

| Target | Acquirer | What/why | Status | Date |
|---|---|---|---|---|
| [veza](../vendors/veza.md) | ServiceNow | Identity/data-access governance | **Closed** | 2026-03-02 (~$1B) |
| [securiti](../vendors/securiti.md) | Veeam | DSPM / data+AI governance | **Closed** | 2025-12-11 ($1.725B) |
| [symmetry-systems](../vendors/symmetry-systems.md) | [zscaler](../vendors/zscaler.md) | DSPM / data-access graph for AI agents | Announced | 2026-05-21 |
| [splxai](../vendors/splxai.md) | [zscaler](../vendors/zscaler.md) | AI red-team + runtime | Closed | 2025-11-03 (Q1 FY26) |
| [stytch](../vendors/stytch.md) | Twilio | Agent/auth identity | **Closed** | 2025-11-14 |
| [natoma](../vendors/natoma.md) | Snowflake | MCP-native NHI/agent governance | Announced (intent) | 2026-05-27 |
| [trulens](../vendors/trulens.md) (TruEra) | Snowflake | LLM eval (TruLens stays OSS) | **Closed** | 2024-05-22 |
| [langfuse](../vendors/langfuse.md) | ClickHouse | LLM observability (core stays OSS) | Announced | 2026-01-26 |
| [helicone](../vendors/helicone.md) | Mintlify | LLM observability (now maintenance mode) | Announced | 2026-03-03 |
| [whylabs](../vendors/whylabs.md) | Apple | ML monitoring (acqui-hire; product wound down) | ~2025 (med conf.) | — |
| [seraphic](../vendors/seraphic.md) | CrowdStrike | Enterprise browser security | Announced | 2026-01-13 ($420M) |
| [layerx](../vendors/layerx.md) | Akamai | Browser security extension | Announced | 2026-05-14 (~$205M) |
| [styra](../vendors/styra.md) / OPA team | Apple | Authorization (acqui-hire; OPA stays CNCF) | ~2025-08 (med conf.) | — |

> **Snowflake and Zscaler are each running two-deal AI roll-ups** here (Snowflake: TruEra +
> Natoma; Zscaler: SplxAI + Symmetry Systems). Apple quietly absorbed two open-source-adjacent
> teams (WhyLabs, Styra/OPA) as acqui-hires.

### Independents that are themselves *acquirers* (consolidating, not consolidated)
[1password](../vendors/1password.md) → Apono (2026-06, JIT/agent access); [cranium](../vendors/cranium.md) → Aiceberg (2026-05);
[varonis](../vendors/varonis.md) → Cyral (2025-03); [menlo-security](../vendors/menlo-security.md) → Votiro (2025-02); [bitsight](../vendors/bitsight.md) → Cybersixgill
(2024); [securityscorecard](../vendors/securityscorecard.md) → HyperComply (2025); [workos](../vendors/workos.md) → Warrant/FGA (2024); [snyk](../vendors/snyk.md) →
Probely + Invariant Labs (2024–25); [okta](../vendors/okta.md) → Auth0 (2021). These remain independent.

## Big-platform / infrastructure M&A (context, not AI-native)
| Target | Acquirer | Status | Date | Value |
|---|---|---|---|---|
| [wiz](../vendors/wiz.md) | Google / Alphabet | **Closed** | 2026-03-11 | $32B (largest Google deal) |
| HashiCorp ([hashicorp-vault](../vendors/hashicorp-vault.md)) | IBM | **Closed** | 2025-02-27 | $6.4B |
| [normalyze](../vendors/normalyze.md) | Proofpoint | Closed (reported) | ~2024-11/12 | undisclosed |
| [sumo-logic](../vendors/sumo-logic.md) | Francisco Partners (take-private) | **Closed** | 2023-05-12 | ~$1.7B |
| [forgerock](../vendors/forgerock.md) | Thoma Bravo → merged into Ping Identity | **Closed** | 2023-08-23 | ~$2.3B |
| [weights-and-biases](../vendors/weights-and-biases.md) | CoreWeave | **Closed** | 2025-05-05 | reported ~$1.7B |

## Still independent (verified, as of 2026-06-28)
- [hiddenlayer](../vendors/hiddenlayer.md) — AI model security; $50M Series A (2023), M12 + Moore. Independent.
- [witnessai](../vendors/witnessai.md) — AI access governance + runtime; $86.5M total, Series B 2026-01. Independent.
- (more confirmed as research waves complete — see each vendor page)

## What it means for a hedge-fund CTO
- **Half the AI-runtime/guardrail field has been acquired** by platform vendors (PANW, Cisco,
  CrowdStrike, SentinelOne, F5, Check Point, Cato) in 2025–2026. If you standardize on a platform
  you already own, you may get an AI-firewall/guardrail capability "for free" — check before buying
  a standalone.
- **The independents that remain** ([hiddenlayer](../vendors/hiddenlayer.md), [witnessai](../vendors/witnessai.md), [pillar-security](../vendors/pillar-security.md), and
  others pending research) are the ones to diligence on viability vs acquisition risk.
- **Survey implication:** several answer options are now product lines inside a suite, not
  companies. The [survey-blueprint](survey-blueprint.md) and each category's Survey notes flag these.

## Sources
Per-deal primary sources are cached under `raw/sources/` (acquirer press releases + SEC filings),
cited on each vendor page's Sources section. This map aggregates those; see the vendor pages for
the specific citation + confidence per claim.

## History
- [2026-06-28] Created from Phase 3 Wave 1 verified M&A research (33 vendors). Pending-deal and
  reported-value caveats preserved. To extend as later waves surface more deals.
