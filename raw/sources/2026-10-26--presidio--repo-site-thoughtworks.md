# Presidio: repo, docs site, PyPI, Thoughtworks Radar

- URL (fetched): https://github.com/microsoft/presidio (-> data-privacy-stack/presidio)
- URL (fetched): https://presidio.dataprivacystack.org/
- URL (API): https://api.github.com/repos/data-privacy-stack/presidio/releases ; https://pypi.org/pypi/presidio-analyzer/json
- URL (fetched): https://www.thoughtworks.com/radar/languages-and-frameworks/presidio
- Fetched: 2026-10-26
- Good for: what Presidio does, components, deployment, LLM-guardrail usage, maturity, independent assessment.

## Facts
- MIT. Description: framework for detecting, redacting, masking, anonymizing PII across text, images, structured data; NLP + pattern matching + customizable pipelines.
- Components: Analyzer (PII detection in text), Anonymizer (de-identification operators), Image Redactor (OCR-based), Structured (structured/semi-structured data).
- NER/model backends: spaCy, transformers; external PII models (Flair, Span Marker, GLiNER); remote recognizers for Azure AI Language and Azure Health Data Services de-identification.
- Deployment: Python/PySpark, Docker, Kubernetes; pip/Docker/source; samples for App Service, Kubernetes, Spark, Fabric, Azure Data Factory, telemetry redaction.
- LLM samples: "PII Masking LLM calls using LiteLLM proxy"; protecting LLM requests with the AISIX AI Gateway; synthetic data with OpenAI.
- Disclaimer (verbatim): automated detection, so "no guarantee that Presidio will find all sensitive information"; recommends additional protections.
- Releases: 2.2.363 (2026-06-28), 2.2.364 (2026-07-22), 2.2.365 (2026-10-25). PyPI presidio-analyzer 2.2.365, homepage now github.com/data-privacy-stack/presidio.
- Top contributors (GitHub API): omri374, SharonHart, shiranr, balteravishay, navalev.

## Thoughtworks Technology Radar (independent)
- Assess (Apr 2025) -> Trial (Nov 2025). Notes teams use it where strict data-sharing controls apply when integrating with LLMs; caveat that it "isn't foolproof and may miss or misidentify entities" and teams "should exercise caution when relying on its results."
