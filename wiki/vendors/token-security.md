---
type: vendor
name: Token Security
slug: token-security
categories: [non-human-identity]
layer: foundation
aliases: [Token, token.security]
website: https://www.token.security
founded: 2023
hq: Tel Aviv, Israel & New York, USA
ownership: independent
ownership_detail: Venture-backed and independent as of 2026-06; no acquisition found. CEO relocated to the US (Feb 2025); company describes itself as Tel Aviv & New York.
ownership_confidence: high
funding_total: $27M (Seed $7M + Series A $20M)
last_funding: Series A, $20M, 2025-01-28 (led by Notable Capital)
deployment: [saas, api]
target_customer: enterprise security / IAM teams (CISOs); cloud-heavy and AI-adopting orgs
hedge_fund_fit: medium
priority: day-2
trifecta_relevance: [sensitive-data, egress]
status: researched
confidence: medium
sources_count: 3
last_updated: 2026-06-28
tags: [non-human-identity, machine-identity, nhi, ai-agent-identity, secrets, agentless]
---

# Token Security

> A machine-first, agentless platform that discovers, owns, and right-sizes every non-human
> identity — service accounts, secrets, API keys, and now AI agents and MCP servers — across cloud,
> SaaS, and on-prem.

**One-liner** — Identity-first security for non-human and AI-agent identities: find every machine
credential, attach a human owner, and enforce least privilege from one dashboard.

**Categories** — [[non-human-identity]]

## What it does

Token Security tackles the problem that enterprises typically have far more machine identities than
human ones (the vendor cites ~45x), and almost no one owns or governs them. The platform discovers
non-human identities (NHIs) across the stack — cloud IAM roles and credentials, SaaS service accounts,
API tokens/keys, secrets, and increasingly AI agents, MCP servers, and custom GPTs — then builds a
unified graph correlating each identity with its secrets, permissions, usage, and a responsible human
owner. From there it supports lifecycle management (creation through retirement), least-privilege
"right-sizing," behavioral anomaly detection, and remediation workflows.

The pitch a CTO repeats: "Hackers don't break in; they log in." The value is removing the blind spot
around orphaned and over-privileged machine credentials — the kind that turn one leaked key into a
breach — and extending that same governance to the explosion of AI-agent identities.

## Where it sits in the stack

Primary category: [[non-human-identity]] (Foundation layer). Its job is discovery, ownership, and
least-privilege governance of machine and agent identities — the identity-plane control that sits
beneath secrets management and IGA. In lethal-trifecta terms it does not inspect prompts or content;
it constrains the **sensitive-data** and **egress** legs indirectly, by ensuring an agent or service
account can only reach the data and systems it is entitled to, and by killing orphaned/over-privileged
credentials an attacker (or a compromised agent) would otherwise use to exfiltrate. It does not address
the untrusted-input leg — that is the job of [[ai-runtime-security]] guardrails. Trust-zone relevance:
it polices who/what can cross zone boundaries at the identity layer.

## Deployment & architecture

- **SaaS, agentless.** Connects via API/cloud connectors to map credentials across AWS, Azure, GCP,
  SaaS apps, CI/CD (e.g., GitLab), and on-prem systems — no endpoint agent required.
- **Unified identity graph** correlating non-human identities, their secrets/permissions, usage
  patterns, and human owners; least-privilege right-sizing and lifecycle automation on top.
- **AI-agent / MCP coverage** — discovers and audits AI agents, MCP servers, and custom GPTs. Ships
  an MCP Server so third-party AI tools (Claude, ChatGPT, Gemini, Cursor) can query Token's NHI data,
  plus a native "Token AI Agent" in the platform UI.
- **Integrations** — major cloud providers, CI/CD, secrets managers, and identity providers; a
  centralized dashboard for posture, alerts, and remediation.

## Positioning & differentiators

Token positions as **machine-first / identity-first** — built natively for NHIs and agentic AI rather
than retrofitted from human IAM, and explicitly *not* a prompt/content guardrail. Its differentiator
claims (marketing) are the unified identity-secret-permission-owner graph ("deep identity
intelligence"), agentless deployment, and early moves into AI-agent and MCP governance (it markets an
"industry-first" MCP server for NHI security).

Versus nearest neighbors in [[non-human-identity]]: [[oasis-security]] is the closest peer — another
Israeli NHI-discovery/governance platform, better funded (raised ~$40M by 2024). [[astrix-security]]
came at NHI from the third-party app/OAuth-integration angle (and per the registry is flagged as
acquired by Cisco — verify). [[aembit]] is more of a workload IAM / access *issuer* (it brokers
secretless workload-to-service access) rather than a discovery/posture tool. [[entro-security]] leads
with secrets/NHI posture and secrets-security lineage. [[clutch-security]] is another NHI-lifecycle
entrant. [[cyberark]] is the incumbent — secrets/PAM plus its Venafi (machine-identity/certificates)
acquisition — and competes top-down from the enterprise PAM install base. Token's wedge is breadth of
agentless discovery plus the AI-agent identity story.

## Ownership, funding & M&A

Independent, venture-backed. Founded **2023** by Itamar Apelblat (Co-Founder & CEO) and Ido Shlomo
(Co-Founder & CTO), who met at Israel's Unit 8200. Emerged from stealth ~mid-2024 with a **$7M Seed**
(led by TLV Partners; angels including Shlomo Kramer). **Series A: $20M on 2025-01-28**, led by
**Notable Capital**, with existing investor TLV Partners and executives from Palo Alto Networks,
CrowdStrike, Check Point and Venafi — bringing **total funding to $27M**. HQ is Tel Aviv with a New
York/US presence (CEO relocated to the US in Feb 2025). **No acquisition found** — the seed registry
carried no M&A flag and research found none; ownership `independent`, confidence `high` for the
funding/founding facts (multiple corroborating sources incl. TechCrunch), though figures are as of the
Jan-2025 round and may be stale.

## CTO / hedge-fund lens

NHI governance is generally **Day-2** for a hedge fund — you stand up human SSO/MFA, secrets
management, and logging first — but it climbs toward Day-1 the moment you run cloud-native infra with
many service accounts/keys, or start deploying **AI agents** that hold their own credentials and act on
systems. For a fund worried about an over-privileged or orphaned key (or a rogue/compromised agent)
reaching positions, trade systems, or MNPI, Token's discovery-plus-ownership-plus-least-privilege loop
is the relevant control. It is not an SR 11-7 / model-risk tool and does not do comms surveillance or
content DLP — pair it with those. Fit is **medium**: most valuable to larger, cloud- and AI-heavy
shops; a small fund living mostly in SaaS with few machine identities may get enough from its IdP and
secrets manager. As a Series-A startup, weigh vendor maturity/longevity against incumbents like
[[cyberark]].

## Competitors / alternatives

[[oasis-security]], [[aembit]], [[astrix-security]], [[entro-security]], [[clutch-security]],
[[cyberark]], [[natoma]], [[silverfort]]

## Open questions / to verify

- Post-Series-A funding/round (figures are as of Jan-2025); current valuation and headcount.
- Whether the legal/operating HQ has formally moved to the US or remains Tel Aviv with a US office.
- Depth of AI-agent/MCP governance in production vs. roadmap (marketing vs. shipped).
- Vendor-confirmed customer count and any SOC 2 / compliance attestations.
- Whether deployment is fully agentless for on-prem coverage or needs collectors.

## Sources

- [Token Security raises $20M (PR Newswire)](https://www.prnewswire.com/news-releases/token-security-raises-20m-to-secure-enterprises-machine-identities--from-legacy-applications-to-ai-agents-302361620.html) — fetched 2026-06-28 — supports: $20M Series A (2025-01-28, Notable Capital), $27M total, founders/roles, HQ, agentless SaaS, customers (HPE, Hibob); confidence: high (vendor PR primary on funding).
- [Token Security (vendor site)](https://www.token.security/) — fetched 2026-06-28 — supports: current AI-agent + NHI product framing, identity types (service accounts, API keys, secrets, MCP servers, custom GPTs), agentless SaaS, integrations, MCP server, differentiators; confidence: med (marketing).
- [Hackers are targeting machine identities; Token Security raised $20M (TechCrunch)](https://techcrunch.com/2025/01/27/hackers-are-targeting-machine-identities-token-security-just-raised-20m-to-stop-them/) — fetched 2026-06-28 — supports: founded 2023, Unit 8200 founders, Apelblat CEO/Shlomo CTO, HQ/US relocation, competitor framing (Oasis, CyberArk); confidence: high (independent press).

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2023 (ex-Unit 8200 founders Itamar Apelblat CEO & Ido Shlomo CTO), HQ Tel Aviv + New York, $7M Seed (TLV Partners) + $20M Series A (2025-01-28, Notable Capital) = $27M total, independent/no M&A. Documented agentless SaaS NHI-discovery + AI-agent/MCP governance; positioned vs [[oasis-security]], [[aembit]], [[astrix-security]], [[entro-security]], [[clutch-security]], [[cyberark]]. Set status: researched, confidence medium. 3 sources cached.
