# DeepKeep — AI Agent Scanner (2026-03) and Vibe AI Red Teaming (2026-04)

- URL: https://www.prnewswire.com/il/news-releases/deepkeep-launches-ai-agent-attack-surface-mapping-and-discovery-solution-302702359.html
  + https://siliconangle.com/2026/04/20/deepkeep-rolls-vibe-ai-red-teaming-test-ai-apps-agents/
- Fetched: 2026-08-22
- Good for: the two 2026 launches that moved DeepKeep from model-security into
  agent security — and the framework list that shows how it hooks in.

## AI Agent Scanner — released 2026-03-03

Three functions:
1. **Discovery & mapping** — finds connected tools, data sources and
   vulnerabilities inside agent workflows.
2. **Attack-surface analysis** — visual risk map of how those elements could be
   exploited.
3. **Runtime protection** — places AI firewalls/guardrails based on observed
   agent behaviour and data exposure — **"for select frameworks"** only.

Supported agent frameworks: Microsoft-based frameworks, **Agentforce**,
**OpenAI Agents**, **CrewAI**, **Amazon Bedrock AgentCore**, **n8n**, **Make**,
"and others".

Risk scoring is mapped to the **OWASP Top 10 for Agentic Applications**.

Threat model, verbatim: "Unlike standalone AI applications, which have a
relatively limited attack surface, these agents can autonomously interact with
external tools, applications, and knowledge bases – including collaboration
platforms, operational systems, finance systems, cloud services, and other AI
agents."

Distribution: offered **free** to enterprises at `agentscanner.deepkeep.ai` —
i.e. a land-and-expand funnel into the paid platform, not a priced SKU.

Release does not state deployment architecture or integration requirements for
the scanner.

## Vibe AI Red Teaming — released 2026-04-20

Human-steered red teaming: an agent executes the attack campaign, but security
staff "intervene at key decision points, adapt plans in real time based on
intermediate findings, and introduce custom scenarios or prompts mid-execution."
Pitched against both fully-manual red teaming (doesn't scale) and fully-automated
red teaming (lacks depth). CTO Yossi Altevet quoted.

**Caveat on sourcing:** the SiliconANGLE piece carries no independent commentary,
no customers and no third-party validation — it restates the vendor release. The
"first-of-its-kind" claim is marketing; interactive/steerable red teaming is not
obviously novel versus peers.
