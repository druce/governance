# LlamaFirewall: Meta paper and launch coverage

- URL (fetched): https://arxiv.org/abs/2505.03574 and https://arxiv.org/html/2505.03574v1
- URL (fetched): https://thehackernews.com/2025/04/meta-launches-llamafirewall-framework.html (2025-04-30)
- URL (fetched): https://www.infoq.com/news/2025/05/llamafirewall-agent-protection (2025-05-13)
- URL (search result): https://ai.meta.com/research/publications/llamafirewall-an-open-source-guardrail-system-for-building-secure-ai-agents/
- Fetched: 2026-10-26
- Good for: launch date, design intent, Meta's own benchmark numbers, stated limitations.

## Facts
- Announced by Meta on Tuesday 2025-04-29 (The Hacker News, 2025-04-30) alongside an updated Llama Guard, CyberSecEval 4 (AutoPatchBench) and the "Llama for Defenders" program. PyPI 1.0.0 published 2025-04-29.
- Paper "LlamaFirewall: An open source guardrail system for building secure AI agents", arXiv 2505.03574 v1 submitted 2025-05-06; 19 Meta authors (meta.com correspondence). Abstract: a real-time "final layer of defense" for agents; says LlamaFirewall "is utilized in production at Meta"; AlignmentCheck labelled experimental.
- Meta's AgentDojo results (vendor-reported): baseline ASR 17.6% / utility 47.7%; PromptGuard 2 86M ASR 7.5% / 47.0%; AlignmentCheck (Llama 4 Maverick) ASR 2.89% / 43.1%; combined ASR 1.75% / utility 42.7%. AlignmentCheck's judge LLM is configurable; Llama 3.3 70B also strong; small models (3.2 1B, 3.1 8B) caused significant utility loss.
- InfoQ: CodeShield "is not comprehensive and may miss nuanced or context-dependent vulnerabilities" (96% precision, 79% recall per paper); future work lists reduced latency, multimodal agents, broader threat coverage, more realistic benchmarking.
- Search 2026-10-26: no 2026 product news; only explainers.
