# LlamaFirewall: README, PyPI release history, licenses

- URL (fetched): https://raw.githubusercontent.com/meta-llama/PurpleLlama/main/LlamaFirewall/README.md
- URL (fetched): https://raw.githubusercontent.com/meta-llama/PurpleLlama/main/LlamaFirewall/LICENSE
- URL (API): https://pypi.org/pypi/llamafirewall/json ; https://api.github.com/repos/meta-llama/PurpleLlama ; commits?path=LlamaFirewall ; https://huggingface.co/api/models/meta-llama/Llama-Prompt-Guard-2-86M
- Fetched: 2026-10-26
- Good for: components, how it runs, external dependencies, license, maintenance cadence.

## Facts
- Lives in Meta's PurpleLlama repo (meta-llama/PurpleLlama, ~4.4k stars; repo-level license is the Llama 3.2 Community License, but LlamaFirewall/LICENSE is MIT, "Copyright (c) Meta Platforms, Inc. and affiliates").
- Self-description: "framework designed to detect and mitigate AI centric security risks, supporting multiple layers of inputs and outputs, such as typical LLM chat and more advanced multi-step agentic operations. It consists of a set of scanners."
- Scanners: PromptGuard 2 (BERT-style classifier for direct prompt injection/jailbreak on user input and untrusted content such as web data), AlignmentCheck (few-shot chain-of-thought auditor of agent reasoning for goal hijacking / indirect injection), Regex + custom (regex or simple LLM-prompt scanners), CodeShield (static analysis of LLM-generated code, Semgrep + regex rules, 8 languages).
- Runs as a Python library (`pip install llamafirewall`, Python 3.10+) called from your own code: `LlamaFirewall(scanners={Role.USER: [...]}).scan(msg)` -> ScanResult(decision ALLOW/BLOCK, reason, score); `scan_replay(trace)` over a conversation trace.
- Requires guard models downloaded from Hugging Face (Meta Llama gated collections). AlignmentCheck setup instructs `export TOGETHER_API_KEY` — i.e. default path calls a hosted LLM via Together AI.
- Integration examples: OpenAI Agents SDK guardrail demo; LangChain/LangGraph agent demo.
- PyPI releases: 0.0.0 2025-04-23 ... 1.0.0 2025-04-29 ... 1.0.3 2025-05-29 (latest as of 2026-10-26). Commits touching LlamaFirewall in 2026 (Jun-Aug) are type-check/lint housekeeping ("Remove unused type error suppressions", "Enable Pyrefly").
- Llama-Prompt-Guard-2-86M on Hugging Face: created 2025-04-28, license "other" (Llama community license), gated (manual approval).
