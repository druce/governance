URL: https://docs.litellm.ai/docs/proxy/guardrails/pillar_security
Fetched: 2026-06-28
Note: LiteLLM proxy docs — primary, neutral source on HOW Pillar deploys (API guardrail behind an AI gateway) and what it scans.

Key extracted text:
- Deployment: integrates via API endpoint (Generic Guardrail API). api_base = https://api.pillar.security/api/v1/integrations/litellm . Configured as a guardrail in the LiteLLM proxy/AI gateway. Auth via PILLAR_API_KEY.
- Scans for: Prompt Injection, Jailbreak Detection, PII + PCI Detection, Secret Detection (API keys/tokens/credentials), Content Moderation, Toxic Language.
- Execution modes: pre_call (scan input before LLM), post_call (analyze full conversation after response), during_call (parallel, lower latency). Recommended [pre_call, post_call] for full coverage.
- Confirms Pillar runs as an API-based guardrail layer in front of / around model traffic via an AI gateway, not as its own inline TLS proxy.
