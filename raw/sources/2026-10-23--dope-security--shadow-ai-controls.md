# dope.security — shadow-AI discovery and tenant controls (vendor blog)

- URLs:
  - https://dope.security/post/shadow-ai-detection-governance (2026-06-25, Amar Jeer)
  - search snapshot of related dope.security posts (https://dope.security/post/best-shadow-ai-tools, /post/tools-for-shadow-ai, /post/shadow-ai)
- Fetched: 2026-10-23
- Good for: evidence dope.security sells AI-usage discovery + tenant restriction + prompt DLP (ai-access-governance functions). All vendor marketing; no independent testing found.

## Extracted

- 2026-06-25 post: per-user inventory of AI tools and accounts; argues network logs and SSO undercount (personal accounts in browser tabs produce no SSO event). Tenant control: force users onto corporate instance — allow corporate ChatGPT, block personal ChatGPT on the same domain (via ChatGPT workspace ID). Dopamine DLP ("Endpoint Data Loss Prevention Powered by AI") can "stop regulated data from leaving in a prompt." Works "from an agent on the endpoint with visibility inside sanctioned tenants," without "routing anyone's traffic through a data center first."
- Search snapshot (other posts): "AI Usage" analytics view — total AI requests, active AI users, distinct AI apps over a rolling 7-day window; personal vs enterprise-licensed account; Cloud Application Control restricts to approved enterprise tenants (blocks personal ChatGPT, Claude, Google, M365 logins by reading tenant identifier in decrypted traffic); CASB Neural scores OAuth-connected third-party apps in M365/Google tenants. The vendor also publishes self-serving competitor rankings (e.g., "Best Netskope Alternative for Shadow AI Governance in 2026").
