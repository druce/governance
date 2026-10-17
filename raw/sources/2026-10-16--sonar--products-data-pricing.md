# Sonar — products (AI Code Assurance, AI CodeFix, Vortex, agents, MCP), data handling, certifications, pricing

- URL: https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview
- URL: https://docs.sonarsource.com/sonarqube-server/2026.4/instance-administration/ai-features/enable-ai-codefix
- URL: https://www.sonarsource.com/company/press-releases/sonar-launches-sonar-vortex-and-sonarqube-remediation-agent/
- URL: https://www.sonarsource.com/company/newsroom/
- URL: https://docs.sonarsource.com/sonarqube-mcp-server
- URL: https://sonarsource.com/trust-center/
- URL: https://www.sonarsource.com/company/press-releases/sonar-achieves-soc-2-type-ii-compliance/
- URL: https://www.sonarsource.com/plans-and-pricing/
- Fetched: 2026-10-16
- Good for: what the AI-code features actually are, where code goes, certs, price points.

## AI Code Assurance (docs)
- Project-level setting "This project contains AI-generated code" (manual flag in project Administration; no auto-detection described on the overview page) -> AI code label.
- Recommended quality gate "Sonar way for agentic AI" + quality profile "Sonar agentic AI"; externally publishable AI Code Assurance badge only if labelled + AI-qualified gate.
- First announced Oct 2024 alongside AI CodeFix.

## AI CodeFix (docs, Server 2026.x)
- LLM-generated fix suggestions for issues. Sonar-hosted option sends the affected code snippet to the selected LLM (OpenAI GPT-5.1 / GPT-4o listed); Sonar says its LLM agreements bar training on customer code.
- Bring-your-own: Azure OpenAI, AWS Bedrock, or self-hosted gateway (Ollama, LiteLLM, vLLM). Docs say fully self-hosted config needs no outbound internet; community threads report older versions fetching prompts online — version-dependent.

## 2026 agentic products
- 2026-06-30 (AIE World's Fair SF): Sonar Vortex — gives coding agents org standards/quality profiles/rules before they write, verifies output in real time, delivers "governed context" in one call; vendor benchmark claims up to 36% fewer tokens on refactoring tasks. SonarQube Remediation Agent — background agent that fixes assigned issues, re-verifies with Sonar analysis, opens PRs.
- SonarQube Hunter Agent ("logic-based security flaws") — launched 2026 (press release exists; date not extracted).
- 2026-09-29: SonarQube Server 2026.5 LTA extends "agentic code governance and verification" to self-managed.
- 2026-10-13: joined OpenAI "Daybreak" Cyber Partner Program.
- Site navigation lists Sonar MCP plus plugins for Claude Code, Cursor, Codex, Antigravity, GitHub Copilot CLI.
- SonarQube MCP Server docs: tools to analyze code, retrieve issues, check quality gates, inspect hotspots/coverage for AI coding agents.

## Certifications / hosting (trust center)
- ISO 27001:2022 certified; SOC 2 Type II (announced Feb 2025; scope Server, Cloud, IDE; report under NDA).
- SonarQube Cloud on AWS; default EU (Frankfurt); US region (N. Virginia) available.

## Pricing (vendor page, Oct 2026)
- SonarQube Cloud: Free (private projects up to 50k LOC); Team from $34/mo (100k LOC; FAQ says $32 — inconsistent), includes Advanced Security; Enterprise custom (includes Advanced Security, Gitar, Vortex, Remediation Agent, Hunter Agent). Gitar add-on $20/user/month annual on Team.
- SonarQube Server: Community Build (open source, free); Developer/Enterprise/Data Center priced per instance per year by LOC.

## Channel
- URL: https://www.intelligentcio.com/north-america/2026/09/14/carahsoft-and-sonar-expand-ai-code-verification-across-north-america/
- 2026-09-14 (trade press, via search summary): expanded Carahsoft agreement takes Sonar's AI code verification technology into commercial markets across North America.
