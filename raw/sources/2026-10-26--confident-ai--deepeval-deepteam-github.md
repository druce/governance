# Confident AI: DeepEval + DeepTeam open-source repos, data-privacy doc

- URL (fetched): https://github.com/confident-ai/deepeval
- URL (fetched): https://github.com/confident-ai/deepteam
- URL (fetched): https://deepeval.com/docs/data-privacy
- Fetched: 2026-10-26
- Good for: what DeepEval and DeepTeam do, licenses, adoption signal (stars), telemetry/data flows to Confident AI.

## DeepEval (github.com/confident-ai/deepeval)
- Apache 2.0. ~19.1k stars, ~2.1k forks (2026-10-26).
- "Pytest-like" open-source LLM evaluation framework: unit-test LLM apps, end-to-end, agent trajectories, individual agent steps.
- Metrics: G-Eval (LLM-as-judge with custom criteria), DAG; agent metrics (Task Completion, Tool Correctness, Step Efficiency, Plan Quality); multi-turn (Knowledge Retention, Turn Relevancy, Role Adherence); RAG (Answer Relevancy, Faithfulness, Contextual Precision/Recall/Relevancy); Hallucination, Bias, Toxicity, JSON Correctness; voice-agent metrics; multimodal; MCP metrics (MCP Task Completion, MCP Use, Multi-Turn MCP Use).
- Integrations listed: LangChain, LangGraph, Pydantic AI, CrewAI, Anthropic, OpenAI, OpenAI Agents, LlamaIndex, Google ADK, AWS AgentCore, AI SDK, Mastra, Strands.
- `deepeval login` connects to Confident AI (hosted platform); once logged in, test cases are logged to the cloud automatically.
- Confident AI offers an MCP server for inspecting failing traces/datasets from Claude Code / Cursor.
- Some metrics run local NLP models; LLM-judge metrics call whatever LLM you configure.

## DeepTeam (github.com/confident-ai/deepteam)
- Apache 2.0. ~3.1k stars (2026-10-26). "Built on DeepEval"; runs locally.
- Red-teaming framework for LLMs and agents: 50+ vulnerabilities (PII leakage, prompt leakage, bias, toxicity, BFLA/BOLA/RBAC, SQL/shell injection, SSRF, tool metadata poisoning, excessive agency, goal theft, etc.), 20+ attack methods (prompt injection, roleplay, encoding tricks, multilingual; multi-turn linear/tree/crescendo jailbreaking).
- Framework mappings: OWASP Top 10 for LLMs 2025, OWASP Top 10 for Agents 2026, NIST AI RMF, MITRE ATLAS, BeaverTails, Aegis.
- Also ships seven runtime "guards" (ToxicityGuard, PromptInjectionGuard, PrivacyGuard, IllegalGuard, HallucinationGuard, TopicalGuard, CybersecurityGuard).
- Confident AI (commercial) integrates: manages risk assessments, monitors production vulnerabilities, shares reports.

## Data privacy (deepeval.com/docs/data-privacy)
- Default anonymous telemetry via PostHog: event names, metric names, notebook flag, storage backend, anonymous ID, public IP (coarse region). Says it never sends stored results; PII excluded. Opt out: `DEEPEVAL_TELEMETRY_OPT_OUT=1`.
- Data sent to Confident AI is stored in Confident AI's private cloud on AWS (unless on the "VIP" plan); region and retention not stated.
