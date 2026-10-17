# Tetrate — Agent Router (ex-Envoy AI Gateway), commercial products, company

- URL: https://tetrate.io/blog/agent-router-joins-aaif
- URL: https://aaif.io/blog/agent-router-joins-aaif
- URL: https://tetrate.io/
- URL: https://tetrate.io/about
- URL: https://itbrief.news/story/tetrate-releases-envoy-ai-gateway-1-0-for-ai-traffic
- URL: https://itbrief.co.uk/story/tetrate-launches-tool-to-certify-enterprise-ai-agents
- URL: https://aigateway.envoyproxy.io/release-notes/v0.4
- URL: https://tetrate.io/learn/ai/best-enterprise-ai-gateway
- URL: https://tetrate.io/press/tetrate-joins-finos-to-break-the-ai-governance-stalemate-for-highly-regulated-environments
- URL: https://www.venturecapitaljournal.com/tetrate-inks-40m-series-b/
- URL: https://www.cbinsights.com/investor/tetrate
- URL: https://www.ai.engineer/nyc
- Fetched: 2026-10-16
- Good for: OSS project status/rename, Tetrate commercial offerings, deployment model, funding.

## OSS project
- Envoy AI Gateway: started by engineers at Bloomberg and Tetrate as an Envoy (Envoy Gateway) sub-project. MCP support (MCPRoute, streamable HTTP, OAuth 2.0/JWKS) added in v0.4.0 (2025-11-07).
- v1.0 released 2026-06-24 (IT Brief): stable v1 API (AIGatewayRoute, AIServiceBackend, BackendSecurityPolicy, GatewayConfig, MCPRoute, MCPRouteSecurityPolicy); OpenAI-compatible unified API over OpenAI, Anthropic, Gemini, Azure OpenAI, Bedrock, Groq, Mistral, Cohere, DeepSeek; MCP multiplexing, tool filtering, OAuth + JWT claim forwarding, CEL authz, tool-level observability; token-aware rate limits/budgets with cost attribution; OpenInference + OTel GenAI tracing. Contributors Bloomberg (runs in production), Nutanix, Tetrate. v1.1 Aug 2026 (AAIF).
- RENAME: 2026-09-09/10 — "Envoy AI Gateway becomes Agent Router and joins the Agentic AI Foundation (AAIF)", moving from Envoy sub-project to standalone AAIF project. Apache-2.0; Envoy remains the data plane; no migration needed; 1.x compatibility commitment kept. 132 contributors from 21 orgs; 11 public adopters incl. Bloomberg, Tencent Cloud, Nutanix, LY Corp, National Research Platform. AAIF: 9 maintainer seats across Bloomberg, Nutanix, AMD, Tetrate, Netflix — no company majority. Third-party (TrueFoundry): old aigateway.envoyproxy.io URLs redirect to theagentrouter.ai.

## Tetrate commercial (vendor)
- Agent Router Service: hosted/self-serve at router.tetrate.ai; free signup credit; usage = model cost + routing fee (tooldirectory.ai, third-party). Originally announced 2025 as "Tetrate Agent Router Service".
- Agent Router Enterprise: GA announced 2026-01-08 (IT Brief) — LLM gateway (approved model catalog, central keys, fallback, cost controls), MCP gateway (shared tool catalog, authN, tool filtering), AI guardrails, agent "certification" workflow with eval dashboards. Tetrate's comparison page (Oct 2026): data planes in customer AWS/Azure/GCP VPC or on-prem; Tetrate-run management plane (not in data path; >=99.9% uptime; SOC 2 Type II audited — vendor claim); flat license by capability/footprint. AAIF blog FAQ: "dedicated instance". Homepage: VPC, on-prem, air-gapped, "CVE-protected builds".
- Also: Agent Operations Director; legacy Tetrate Service Bridge (Istio-based service mesh) — not on current About page.
- Joined FINOS June 2025; mapping FINOS AI Governance Framework to EU AI Act, ISO 42001, FFIEC, NIST 800-53 (vendor).
- Comparison claims vs LiteLLM (self-hosted only, shared Postgres SPOF, 2026 security issues), Portkey (now in Palo Alto Prisma AIRS), Kong (API gateway with AI plugins, per-service pricing) — vendor marketing.

## Company
- Founded 2018 by Istio/Envoy contributors; CB Insights: Milpitas, CA; About page: "Silicon Valley" + remote; IT Brief: San Francisco. CEO Jeyappragash JJ, CTO/co-founder Varun Talwar.
- Funding: Series A 2019 ~$12.4M (PitchBook); Series B $40M 2021-03-10 led by Sapphire Ventures (Scale VP, NTTVC new; Dell Tech Capital, Intel Capital, 8VC, Samsung NEXT). No later round or M&A found. Latka estimate ~$11M 2024 revenue, ~121 staff (third-party estimate).
- Customers: "finance, government, global tech" — none named on site. Cloud partners AWS, Azure, GCP, OpenShift; Carahsoft listing (public sector).
- AIE NYC 2026: Silver sponsor; no Tetrate talk on schedule.
