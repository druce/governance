# Pydantic Logfire — product, pricing/hosting, funding, AI Gateway merge

- URL: https://pydantic.dev/logfire
- URL: https://pydantic.dev/pricing
- URL: https://techcrunch.com/2024/10/01/sequoia-backs-pydantic-to-expand-beyond-its-open-source-data-validation-framework (2024-10-01)
- URL: https://pydantic.dev/articles/logfire-announcement
- URL: https://pydantic.dev/articles/gateway-merging-into-logfire (2026-03-23)
- Fetched: 2026-10-16
- Good for: what Logfire is, deployment/compliance by tier, price points, ownership.

## Product (vendor)
- AI + general observability platform built on OpenTelemetry; one trace covers model calls,
  tool calls, API requests, DB queries. Agent/LLM views with token usage and cost.
- Integrations: Pydantic AI, OpenAI, Anthropic, LangChain, LlamaIndex, LiteLLM, Vercel AI SDK.
- Evals: programmatic checks, LLM judges, human review; offline on datasets or online on
  production traffic; scores stored as span attributes.
- Querying: Postgres-flavoured SQL ("FusionFire" engine on Apache DataFusion); Logfire MCP server.
- SDKs: Python, JS/TS, Rust first-party (MIT); other languages via standard OTel. Server closed source.
- Named customers (logos/testimonials): General Intelligence Company, Dosu, Boosted.ai, Airbyte,
  **Pictet**, Motorola, Vox Media, Weaviate, Nous Research, Sophos.

## Pricing & hosting (pricing page, no effective date shown)
- Personal free (10M records/mo, hard cap, 30-day retention); Team $49/mo (10M incl., $2/M extra,
  5 seats); Growth $249/mo (unlimited seats, up to 90-day retention); Enterprise custom.
- Hosting: Cloud (EU or US region); Dedicated single-tenant (any GCP region, CMEK); Self-hosted
  (Helm chart on your Kubernetes; needs Postgres + S3-compatible storage; data stays on-prem) — Enterprise.
- Compliance: SOC 2 Type II (Cloud, Dedicated); HIPAA BAAs (Growth, Enterprise); GDPR DPA, EU region.
- Enterprise: SSO (Okta, Entra ID, Keycloak, SAML), SCIM, custom roles, audit log API, SLA.
- Add-ons: AI Gateway full access; Data Loss Prevention.

## Company / funding (TechCrunch 2024-10-01; Pydantic announcement)
- Pydantic OSS library started 2017 by Samuel Colvin; company launched 2022; UK-based, team across
  US/Europe; 13 staff at the time.
- Seed $4.7M (Sequoia); Series A $12.5M led by Sequoia with Partech, Irregular Expression
  (2024-10-01). ~ $17.2M total disclosed. No later round found as of 2026-10-16.
- Logfire went GA on 2024-10-01 after ~5 months open beta.

## AI Gateway merge (2026-03-23)
- Pydantic AI Gateway folded into Logfire; gateway.pydantic.dev deprecated; gateway inherits
  Logfire SSO, custom roles, fine-grained permissions, group mapping; Playground requests traced.

## AIE NYC 2026
- Pydantic listed as Silver sponsor; no session found on agenda.
