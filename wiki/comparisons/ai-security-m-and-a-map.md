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
| [[cyberark]] | Privileged access + machine/NHI identity | **Closed** | 2026-02-11 | ~$25B |
| [[portkey]] | AI gateway (now the Prisma AIRS gateway component) | **Closed** | 2026-05-29 | undisclosed |
| Protect AI → [[prisma-airs]] | Model scanning, red-teaming, posture, runtime | **Closed** | 2025-07-22 | reported ~$650–700M |
| Talon → [[prisma-access-browser]] | Enterprise browser | **Closed** | 2023-12-28 | reported ~$625M |

PANW is assembling identity ([[cyberark]]) + AI gateway ([[portkey]]) + AI runtime/posture
([[prisma-airs]]) + browser under one roof. For a CTO this means several formerly-independent
"best of breed" tools now arrive as one suite — fewer throats to choke, more lock-in.

### Cisco — buying the AI trust & SOC layer
| Target | What it brought | Status | Date | Value |
|---|---|---|---|---|
| [[splunk]] | SIEM / observability | **Closed** | 2024-03-18 | $28B |
| Robust Intelligence → [[cisco-ai-defense]] | AI runtime security / validation | **Closed** | ~2024-09-24 | undisclosed |
| [[galileo]] | LLM eval / guardrails | Closed (reported) | ~2026-05-22 | undisclosed |
| [[astrix-security]] | Non-human / agent identity | **Announced intent — pending** | 2026-05-04 | reported ~$400M |

> Note: the seed listed Astrix as "acquired"; as of 2026-06-28 it is **announced intent, not
> closed**. Treat as pending.

### CrowdStrike — adding SaaS posture + AI detection/response
| Target | What it brought | Status | Date | Value |
|---|---|---|---|---|
| [[pangea]] | AI detection & response (AIDR) / guardrails | **Closed** | ~2025-09 (announced 2025-09-16) | reported ~$260M |
| [[adaptive-shield]] | SaaS security posture (SSPM) | **Closed** | ~2025-01 (announced 2024-11-06) | reported ~$300M |
| Charlotte AI | Agentic SOC (built in-house, not acquired) | — | — | — |

### SentinelOne
| Target | What it brought | Status | Date | Value |
|---|---|---|---|---|
| [[prompt-security]] | Prompt-layer DLP / AI runtime | **Closed** | ~2025-11 (announced 2025-08-05) | reported ~$250M |

### F5
| Target | What it brought | Status | Date | Value |
|---|---|---|---|---|
| [[calypsoai]] | AI guardrails + red-team (now F5 AI Guardrails / AI Red Team) | **Closed** | 2025-10-08 | reported ~$180M |

### Other notable AI-security tuck-ins
| Target | Acquirer | What it brought | Status | Date | Value |
|---|---|---|---|---|---|
| [[aim-security]] | [[cato-networks]] | AI/agent security (Cato's first acquisition) | Announced | 2025-09-03 | reported ~$350M |
| [[lakera]] | Check Point | AI guardrails / prompt-injection defense | Announced (close exp. Q4 2025) | 2025-09-16 | reported ~$300M |
| [[apex-security]] | Tenable | Agent/AI security → Tenable One | Announced/integrating | 2025-05-29 | reported >$105M |
| [[promptfoo]] | OpenAI | Open-source eval/red-team → OpenAI Frontier | **Closed** | 2026-03-09 | undisclosed |
| [[trojai]] | A10 Networks | AI detect (red-team) + defend (runtime firewall) | **Announced** | 2026-06-15 | undisclosed |

> **TrojAI→A10 Networks was NOT in the seed CSV** — surfaced during research. A recent (2026-06-15)
> deal; confirm completion.

## Big-platform / infrastructure M&A (context, not AI-native)
| Target | Acquirer | Status | Date | Value |
|---|---|---|---|---|
| [[wiz]] | Google / Alphabet | **Closed** | 2026-03-11 | $32B (largest Google deal) |
| HashiCorp ([[hashicorp-vault]]) | IBM | **Closed** | 2025-02-27 | $6.4B |
| [[normalyze]] | Proofpoint | Closed (reported) | ~2024-11/12 | undisclosed |
| [[sumo-logic]] | Francisco Partners (take-private) | **Closed** | 2023-05-12 | ~$1.7B |
| [[forgerock]] | Thoma Bravo → merged into Ping Identity | **Closed** | 2023-08-23 | ~$2.3B |
| [[weights-and-biases]] | CoreWeave | **Closed** | 2025-05-05 | reported ~$1.7B |

## Still independent (verified, as of 2026-06-28)
- [[hiddenlayer]] — AI model security; $50M Series A (2023), M12 + Moore. Independent.
- [[witnessai]] — AI access governance + runtime; $86.5M total, Series B 2026-01. Independent.
- (more confirmed as research waves complete — see each vendor page)

## What it means for a hedge-fund CTO
- **Half the AI-runtime/guardrail field has been acquired** by platform vendors (PANW, Cisco,
  CrowdStrike, SentinelOne, F5, Check Point, Cato) in 2025–2026. If you standardize on a platform
  you already own, you may get an AI-firewall/guardrail capability "for free" — check before buying
  a standalone.
- **The independents that remain** ([[hiddenlayer]], [[witnessai]], [[pillar-security]], and
  others pending research) are the ones to diligence on viability vs acquisition risk.
- **Survey implication:** several answer options are now product lines inside a suite, not
  companies. The [[survey-blueprint]] and each category's Survey notes flag these.

## Sources
Per-deal primary sources are cached under `raw/sources/` (acquirer press releases + SEC filings),
cited on each vendor page's Sources section. This map aggregates those; see the vendor pages for
the specific citation + confidence per claim.

## History
- [2026-06-28] Created from Phase 3 Wave 1 verified M&A research (33 vendors). Pending-deal and
  reported-value caveats preserved. To extend as later waves surface more deals.
