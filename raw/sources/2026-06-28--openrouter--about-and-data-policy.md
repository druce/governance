URL: https://openrouter.ai/about ; https://openrouter.ai/docs/guides/features/zdr ; https://openrouter.ai/docs/guides/privacy/data-collection ; https://openrouter.ai/blog/insights/ai-data-residency/
Fetched: 2026-06-28
Note: OpenRouter's own about page + privacy/data-policy docs — good for scale metrics, deployment model, and the data-egress/residency story that matters for a regulated fund.

## About page (vendor, marketing)
- Founded early 2023. Describes itself as "the largest and most popular AI gateway," eliminating vendor lock-in.
- Scale: 400+ models; 70+ providers; 100T monthly tokens; 10M+ global users.
- Access model: cloud-based API service with a web chat interface (hosted aggregator).

## Data policy / privacy (vendor docs)
- ZDR: By default OpenRouter does NOT log prompts or completions; stores request metadata (timestamps, model, token counts, latency) for billing/ops. Conversation content not retained unless you opt in to prompt logging.
- Prompt logging is opt-in (1% usage discount in exchange). When on, OpenRouter stores prompts + completions.
- Privacy controls: can restrict routing to endpoints with a Zero Data Retention policy; enforce ZDR globally, per model group, per guardrail, or per request. `data_collection: deny` blocks providers that store/train on inputs.
- Routing layer: retention/training behavior depends on the DOWNSTREAM provider you route to. OpenRouter forwards requests to dozens of providers (Anthropic, OpenAI, Mistral, Groq, open-weight hosts).
- Enterprise: EU in-region routing — prompts/completions processed within the EU via eu.openrouter.ai, only EU-eligible providers serve them. Enterprise quickstart exists for organizations.
