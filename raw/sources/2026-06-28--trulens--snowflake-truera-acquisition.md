# TruLens / TruEra — Snowflake acquisition + open-source status

- URLs: https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/ ; https://www.snowflake.com/en/blog/trulens-open-source-ai/ ; https://github.com/truera/trulens ; https://www.trulens.org/
- Fetched: 2026-06-28
- Good for: confirming TruLens ownership (Snowflake via TruEra), what TruLens is, OSS status.

## Key extracted facts
- M&A CONFIRMED: Snowflake announced a definitive agreement to acquire the TruEra AI Observability platform on **2024-05-22** (primary source: Snowflake blog). TruEra are the creators of TruLens. No financial terms disclosed.
- TruEra co-founders joined Snowflake: Anupam Datta (President & Chief Scientist), Shayak Sen (CTO), Will Uppington (CEO).
- TruLens is an **open-source** Python library for evaluating and tracing LLM / RAG / agent applications (feedback functions, the "RAG triad": context relevance, groundedness, answer relevance; tracing). Apache-licensed, on GitHub at truera/trulens, thousands of developers.
- Snowflake committed to keeping TruLens open source and now stewards it; post-acquisition added parallelized feedback eval, LangChain compatibility, dashboard speedups (4–32x). Integrates with Snowflake Cortex / Streamlit / Arctic but remains usable standalone with any model provider.
- TruLens itself is a free OSS library (SDK / self-hosted); the commercial productized observability lives inside Snowflake (e.g., Cortex AI Observability) rather than a separately-sold "TruLens" product.
