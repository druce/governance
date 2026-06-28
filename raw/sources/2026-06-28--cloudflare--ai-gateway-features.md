URL: https://developers.cloudflare.com/ai-gateway/features/
Fetched: 2026-06-28
Note: Cloudflare's own docs — authoritative list of AI Gateway features (vendor primary source; feature claims are vendor marketing/docs).

Key extracted text:
- AI Gateway = control plane / "single exit door" sitting between your app and AI providers. One line of code / change base URL to route LLM traffic through Cloudflare's edge.
- Caching: serve identical requests from Cloudflare's global cache, "reducing latency by up to 90%" and cutting provider API costs.
- Rate limiting: sliding or fixed-window request limits to cap cost / suspicious activity.
- Spend limits: budget tracking by model/provider/custom metadata with automatic blocking.
- Dynamic Routing: visual config for routing by user-segment/geography, A/B testing; fallbacks via dynamic routing; request retries and model fallback.
- Guardrails: real-time content moderation on prompts and responses (harmful-content moderation).
- Data Loss Prevention (DLP): scans prompts/completions for PII, financial, healthcare data.
- Authentication: token-based access control to the gateway.
- BYOK: encrypted management of 20+ provider API keys.
- Analytics: real-time usage, cost tracking, error monitoring via GraphQL API.
- Logging: request/response capture, Logpush export, retention policies. Logs show user prompt, model response, provider, timestamp, status, token usage, cost, duration.
- Custom metadata + custom costs (override pricing with negotiated rates).
- Supported providers: Workers AI, Anthropic, OpenAI, Google Gemini, Replicate, and more (20+).
- Pricing: core features (dashboard analytics, caching, rate limiting) free; just need a Cloudflare account.
