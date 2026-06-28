# Lasso Security — Platform / Deployment Overview (vendor + aggregated)

- URL: https://www.lasso.security/ (and /platform/lasso-for-employees, /platform/lasso-for-applications, docs.lassox.com)
- Fetched: 2026-06-28
- Good for: deployment modes, product modules, integrations, later funding signal.

## Key text (trimmed)

Positioning: "leading genAI security platform that autonomously monitors interactions,
detects risks in real-time, and empowers organizations to adopt AI safely."

Deployment options: "integrated in any environment with SDKs, reverse proxies, browser
extensions, or API-layer observability." Specifically pairs a **browser extension for
employee AI** (Lasso for Employees) with an **open-source MCP Gateway, SDK, and API
gateway for built AI** (Lasso for Applications).

Modules:
- Discover — maps all AI models, agents, applications across the org incl. shadow AI
  tools used without approval.
- Guardrails — analyzes user inputs and LLM responses; models trained on a large,
  frequently updated dataset of prompt-injection and jailbreak attempts. Enforced inline
  at the proxy, API, or AI Gateway layer; runtime protection adapts as the app evolves.
- Intent Security Framework — for agentic AI, establishes behavioral baselines for agents
  (expected actions, tools, data) then flags deviations in real time.

Vendor performance claims (marketing): <50ms decisions, 99.8% detection accuracy.

Integrations: Portkey AI gateway (Lasso guardrails integration documented in Portkey docs).

Funding signal (aggregators, lower confidence): seed $6M (Nov 2023); later SAFE/round
activity reported 2024-2025 (e.g. ~$10M SAFE June 2025 w/ Mindset Ventures, CyberArk
Ventures, Singtel Innov8; a Series A reported Oct 2025). Aggregators disagree on exact
totals (~$28M cited) — treat post-seed totals as unverified.
