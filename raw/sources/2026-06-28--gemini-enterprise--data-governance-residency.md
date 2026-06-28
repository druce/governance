URL: https://docs.cloud.google.com/gemini/docs/discover/data-governance ; https://docs.cloud.google.com/gemini/enterprise/docs/locations ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention
Fetched: 2026-06-28
Note: Primary Google Cloud docs for the no-training commitment, zero-data-retention, and data residency zones. Core governance evidence for a hedge-fund CTO.

Key extracted text:

No-training / data use (Gemini for Google Cloud data governance doc):
- "Gemini doesn't use your prompts or its responses as data to train its models."
- Google follows "robust data governance practices, which include reviews of the data that Google Cloud uses in the development of its products."
- "When you submit prompts to Gemini, your data is encrypted in-transit as input to the underlying model in Gemini."
- Google Cloud "handles your prompts in accordance with our terms of service and Cloud Data Processing Addendum" (CDPA).

Gemini Enterprise Agent Platform — zero data retention (ZDR):
- "Google won't use your data to train or fine-tune any AI/ML models without your prior permission or instruction" — applies to all managed models on the Gemini Enterprise Agent Platform, including GA and pre-GA models.

Data residency (Gemini Enterprise Standard/Plus + NotebookLM Enterprise):
- At-rest Data Residency Zones (DRZ) supported in multi-regions `us` and `eu`, and in-country regions `ca` (Canada) and `in` (India) (GA with allowlist), subject to limitations.
- "For Gemini Enterprise, MLP [machine learning processing], such as training, prediction, and model tuning, occur within the `us` multi-region when requests are made to regionally-available APIs in the US, or within the `eu` multi-region when requests are made to regionally-available APIs in Europe."
- CMEK: at-rest DRZ + MLP supported in US/EU multi-regions; NOT available in in-country regions; CMEK NOT available in the `global` region.
- "Dynamic facets" and "Grounding with Google Search" are only available in the `global` region (so DRZ/CMEK don't apply when those are used).
