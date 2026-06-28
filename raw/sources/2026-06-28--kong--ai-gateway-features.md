# Kong AI Gateway — features & architecture

URL: https://developer.konghq.com/ai-gateway/
Also: https://konghq.com/blog/product-releases/ai-gateway-3-8
Fetched: 2026-06-28
Good for: Kong AI Gateway technical capabilities, deployment, guardrails, semantic caching.

## Key extracted text
- AI Gateway is a "connectivity and governance layer for modern AI-native applications built on top of Kong Gateway," implemented as specialized plugins on the existing Kong Gateway data plane.
- AI Proxy / AI Proxy Advanced plugins = provider-agnostic "Universal API": configure once, access any model. Providers: OpenAI, Anthropic, Azure AI, AWS Bedrock, GCP Vertex/Gemini, Cohere, Mistral, Llama, etc.
- Load balancing across models: consistent hashing, lowest-latency, usage-based, round-robin, and semantic matching; retries and fallback.
- Security/guardrails: built-in PII sanitization (AI PII Sanitizer) detecting/redacting across 20 categories and 9 languages; AI Prompt Guard (regex allow/deny); AI Semantic Prompt Guard (block by intent/meaning); integrations with Azure Content Safety, AWS Guardrails, Lakera Guard.
- AI Semantic Cache plugin: caches responses by similarity threshold to cut cost/latency.
- Prompt templates, decorators, compression; automated RAG injection; semantic routing.
- MCP traffic gateway and A2A protocol support; observability via OpenTelemetry + Konnect dashboards.
- Deployment: Konnect (SaaS), self-hosted traditional, hybrid, DB-less, Kubernetes.
- Semantic caching + AI security added in AI Gateway 3.8.
