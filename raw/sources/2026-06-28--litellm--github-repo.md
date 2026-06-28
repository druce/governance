URL: https://github.com/BerriAI/litellm
Fetched: 2026-06-28
Note: Primary source — open-source repo; proxy/gateway feature list, providers, licensing.

Key extracted text:
- Repo tagline: "Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native)
  format, with cost tracking, guardrails, loadbalancing and logging."
- Core (open source) under MIT; enterprise features under a separate LiteLLM Commercial License.
- AI Gateway = centralized service for a team/org; single unified OpenAI-compatible interface.
- Features: cost tracking & spend management (per-project logging/guardrails/caching), guardrails
  (policy enforcement on prompts/responses, PII masking, content filtering, integrations e.g. Pangea,
  Presidio, Bedrock guardrails), load balancing, fallbacks, caching, logging/observability, virtual
  keys, rate limiting (per user/project), admin dashboard.
- Providers: 100+ incl. OpenAI, Anthropic, Gemini, Bedrock, Azure, Cohere, Vertex AI, HuggingFace,
  VLLM, NVIDIA NIM; endpoints /chat/completions, /embeddings, /images, /audio.
- Enterprise: SSO/SAML (Okta, Azure AD), RBAC, audit logs, dedicated support, custom SLAs.
