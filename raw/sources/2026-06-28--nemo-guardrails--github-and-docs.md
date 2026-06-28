# NVIDIA NeMo Guardrails — GitHub + docs

- URL: https://github.com/NVIDIA-NeMo/Guardrails ; https://docs.nvidia.com/nemo/guardrails/home ;
  arXiv https://arxiv.org/abs/2310.10501
- Fetched: 2026-06-28
- Good for: what it is, license, maintainer (NVIDIA), features, deployment.

## Extracted

NeMo Guardrails = open-source toolkit by NVIDIA for adding programmable guardrails
("rails") to LLM-based conversational apps. Open-source Python package; intercepts
inputs/outputs, applies configurable safety checks, blocks/modifies content per policy.

- Maintainer: NVIDIA (NASDAQ: NVDA). License: Apache 2.0. Not a standalone company —
  an NVIDIA-owned open-source project; commercial NeMo microservices / NIM also exist.
- Five rail types: input rails, dialog rails, retrieval rails (RAG), execution rails
  (tool calls), output rails.
- Colang: a python-like modeling language for dialogue flows.
- Safety: jailbreak detection, prompt-injection resistance, hallucination detection,
  input/output moderation, fact-checking; pairs with NeMo Guard / Aegis content-safety
  models (NIM).
- Integrations: OpenAI, LLaMa-2, Falcon, others; optional LangChain integration.
- Latest version: 0.22.0 (May 2026).
- Deployment: self-hosted Python library / SDK; can run as a server.
- Ownership: part of NVIDIA (public company).
