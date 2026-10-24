URL: https://www.zscaler.com/products-and-solutions/ai-guardrails
URL: https://docs.litellm.ai/docs/proxy/guardrails/zscaler_ai_guard
Fetched: 2026-10-23
Note: Zscaler AI Guard — vendor product page (marketing) plus LiteLLM integration docs (third-party, technical). Good for: AI Guard exists as an API guardrail service called by AI gateways; AI Guard for Users/Apps naming.

## Zscaler product page (marketing)
- Page covers "AI Guard for Users": "Access decided per user, per app, per risk, across 3500+ AI tools, approve, isolate, or block." Access "enforced inline on every AI interaction."
- Related "AI Guard for Apps": "prompts and responses inspected in real time inside the tools you approve."
- Lists AI Gateway and AI Endpoint Security as related products. No mention of SPLX on the page.

## LiteLLM docs — Zscaler AI Guard guardrail
- Zscaler AI Guard described as "a single platform for visibility, control, and deep packet inspection of AI prompts"; example detectors include prompt injection and toxicity.
- Supported modes: pre_call (scan prompt) and post_call (scan response). Configure with an API key + policy ID created in the Zscaler AI Guard dashboard; optional api_base. Default 5-second timeout per scan.
- Blocked requests return "Content blocked by Zscaler AI Guard" with a transactionId and blockingDetectors.
- Search results also show equivalent Zscaler AI Guard integrations documented by Portkey and TrueFoundry (not separately fetched).
