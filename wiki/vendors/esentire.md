---
title: eSentire
type: vendor
name: eSentire
slug: esentire
aka: [eSentire MDR, eSentire Atlas, Atlas XDR, Atlas AIDR, Atlas Preempt]
primary_category: ai-soc-analysts
also_listed_in: []
website: https://www.esentire.com/
founded: 2001
hq: Waterloo, Ontario, Canada (per Reuters, 2024-08-13)
ownership_state: pe-owned
owner: "Warburg Pincus (majority, as of 2022), with Georgian and CDPQ"
ownership_note: "Warburg Pincus bought a majority stake in 2017. In 2022 Georgian and CDPQ led a $325M investment, mostly buying existing shares, at a >$1B valuation, and Warburg remained majority holder. Reuters reported on 2024-08-13 that the owners were exploring a sale (~$1B incl. debt, Evercore advising). No completed sale found through 2026-10-24. New CEO James C. Foster from 2026-03."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: "$325M led by Georgian and CDPQ at >$1B valuation (2022-02; largely secondary)"
market_position: {ai-soc-analysts: challenger}
deployment_model: [saas]
form_factor: [platform, agent]
data_leaves_tenancy: "true"
integrations: [Microsoft, AWS, Amazon Bedrock]
mcp_support: unverified
certifications: []
pricing_model: null
fs_traction: claimed
target_customer: mid-market and enterprise organisations without a full in-house 24/7 SOC; lists finance, insurance, private equity and legal among its industries
last_verified: 2026-10-24
verify_after: null
tags: [mdr, managed-soc, agentic-soc, ai-observability, pe-owned, survey-write-in, security-operations]
sources:
  - {claim: "MDR 'that moves first'; MDR for Microsoft / AWS; Atlas platform, 300+ integrations, 'Controlled Autonomy SecOps', 'AI Operatives'; finance/PE among industries; founded 2001", url: "https://www.esentire.com/", date: 2026-10-24, confidence: medium}
  - {claim: "Acquired an unnamed stealth AI-security startup; Atlas AIDR GA (AI activity record, agent/MCP inventory, prompt-injection screening, PII redaction); >2,000 orgs in 80+ countries", url: "https://itbrief.co.uk/story/esentire-acquires-ai-security-startup-for-atlas-aidr", date: 2026-10-24, confidence: medium}
  - {claim: "Atlas runs multi-agent investigations on Claude Opus 4.6 via Amazon Bedrock and the Claude Agent SDK; 120,000+ investigations in 12 months; senior analysts review critical findings", url: "https://claude.com/customers/esentire", date: 2026-10-24, confidence: medium}
  - {claim: "James C. Foster (ZeroFox founder) named CEO, succeeding retiring Kerry Bailey", url: "https://www.techpartner.news/news/zerofox-founder-james-c-foster-becomes-ceo-of-esentire-624592", date: 2026-10-24, confidence: medium}
  - {claim: "Owners Warburg Pincus, CDPQ, Georgian exploring sale at ~$1B incl. debt; ARR ~$150M; Evercore; Waterloo, Ontario", url: "https://investing.com/news/stock-market-news/warburg-pincusbacked-cybersecurity-firm-esentire-explores-sale-sources-say-3569404", date: 2026-10-24, confidence: medium}
---

# eSentire

> Primary category: [ai-soc-analysts](../categories/ai-soc-analysts.md).

**One-liner** — A Canadian managed detection and response (MDR) provider, owned by Warburg Pincus since 2017. It runs a 24/7 SOC on its own Atlas platform, which now does much of the alert investigation with LLM agents. In 2026 it added a module that monitors a customer's own AI usage.

**What it does** — eSentire sells **MDR as a service**: 24/7 monitoring, threat hunting, and hands-on response (host isolation, account actions) across endpoint, network, log, identity and cloud signals. Packages include All-in-One MDR, MDR for Microsoft and MDR for AWS. Also on offer: digital forensics and incident response, and **Atlas Preempt** (autonomous pen testing / continuous exposure management). **Atlas** is the platform behind the service. It takes signals from "any vendor stack" (300+ integrations, vendor figure), and customers use the Atlas Operations Center to see SOC investigations. Logs are one signal type within MDR. **No standalone SIEM product** was found on its site, so it is not cross-listed in [siem-soc](../categories/siem-soc.md).

**What AI it claims (vendor marketing).** eSentire is more specific than most MDRs here:
- Its site describes "Controlled Autonomy SecOps" and adaptive "AI Operatives" (agents), and claims "95% Tier-3 Analyst Validation Alignment".
- An Anthropic customer story (co-marketing) says Atlas runs **multi-agent autonomous investigations on Claude Opus 4.6 via Amazon Bedrock and the Claude Agent SDK**. Per that story: about 44 tool calls and about 6 minutes per investigation, 120,000+ investigations in 12 months, and over 90% agreement with senior experts' verdicts across 500+ adjudicated cases. **Senior analysts still review and act on every critical finding.**
- **Atlas AIDR** (GA, announced 2026-09-29) came from buying an **unnamed stealth-mode AI-security startup** (price undisclosed). It gives the customer a record of *their own* AI use: conversation timelines, tool calls, and inventories of agents, models, providers and MCP servers. It adds prompt-injection screening, redaction of personal data before it reaches a model, custom rules, and alerts when an MCP server's tool descriptions change.

All of these figures are vendor-reported and not independently verified.

**Naming / provenance** — Founded 2001. Earlier based in Cambridge, Ontario, then moved its HQ to Waterloo, Ontario. Platform branding has moved from "Atlas XDR" (2022) to "Atlas". Acquired CyFIR (digital forensics) in 2021. CEO since March 2026: **James C. Foster**, who founded ZeroFox and took it public. He succeeded Kerry Bailey (CEO from 2018), who retired.

**Ownership & viability** — `pe-owned`. **Warburg Pincus** bought a majority stake in **2017**. In **February 2022**, **Georgian and CDPQ** led a **$325M** deal, largely a purchase of existing shares, at a valuation above **$1B**, and Warburg stayed majority holder. On **2024-08-13** Reuters reported that the owners were exploring a sale at about **$1B including debt**, with Evercore advising and **ARR of about $150M**. **No completed sale was found through 2026-10-24.** The 2026 CEO change and the AIDR acquisition suggest the owners are investing to grow rather than selling right away. A sale to a larger security or PE platform remains a live possibility, so customers should check contract-assignment and price-protection terms.

**Positioning & differentiators** —
- **Publishes how its AI works.** Most MDRs (e.g. [blackpoint-cyber](blackpoint-cyber.md), [adlumin](adlumin.md)) say "AI-enhanced" without detail. eSentire names its model stack and publishes investigation metrics, which is the closest any MDR here gets to the AI-SOC software vendors ([dropzone-ai](dropzone-ai.md), [prophet-security](prophet-security.md)). It still sells an outcome, not software you run.
- **Vendor-agnostic, unlike Microsoft-centred MDRs.** Atlas works across stacks. Compare [bluevoyant](bluevoyant.md), which is built around Microsoft, and [crowdstrike](crowdstrike.md) Falcon Complete, which runs on CrowdStrike's own stack.
- **Visibility into your AI.** Atlas AIDR monitors the customer's own AI agents and MCP use. That is unusual for an MDR and overlaps with dedicated AI-usage monitoring tools, so expect overlap if you already run one.
- **Versus [reliaquest](reliaquest.md):** both sell AI-agent-assisted SOC outcomes. ReliaQuest is larger (>$300M ARR) and markets itself as a platform. eSentire markets itself as MDR.

**Who should choose them / anti-fit** — Fits a **mid-sized fund or asset manager with a mixed tool estate and no 24/7 SOC** that wants managed response and some insight into how the AI triages. Finance, insurance and private equity are listed industries. **Anti-fit:** a firm that wants to own and tune detection in its own SIEM and only buy software. Also an all-Microsoft shop where E5 plus a Microsoft-focused MSSP is cheaper.

**Known weaknesses / gotchas** — Survey write-in (2026-10): written into **Q47 AI SOC** by **1 respondent, in production**. Ownership has been in play since the 2024 sale exploration. AI performance metrics come from the vendor and from Anthropic co-marketing. Customer telemetry is processed by a third-party LLM (Claude on Bedrock), so confirm the data-processing, residency and no-training terms. The AIDR startup's name and team size are undisclosed.

**Deployment & data handling** — SaaS platform plus eSentire sensors/agents and API integrations. Telemetry goes to eSentire's SOC and cloud (`data_leaves_tenancy: true`), and investigation data is processed by Claude via Amazon Bedrock. Retention, residency (it has North America, EMEA and APAC operations) and training-use terms are **unverified**. Atlas AIDR captures AI conversation content, so ask where those transcripts are stored and for how long.

**Integrations & partnerships** — 300+ integrations (vendor). Microsoft and AWS MDR packages. AWS/Bedrock for LLMs. AIDR inventories MCP servers, but eSentire's own MCP support is unverified (`mcp_support: unverified`). Sold direct and via partners (AIDR availability mentions "customers and partners").

**Compliance & FS traction** — Finance and private equity are listed target industries (`fs_traction: claimed`). No named hedge-fund customers found. Certifications not checked. Claims >2,000 customers in 80+ countries.

**Commercial** — Not public. Packaged MDR subscriptions.

## Open questions

- Whether the 2024 sale process concluded; current cap table.
- SOC 2 / ISO 27001; data residency and LLM no-training terms for telemetry sent to Bedrock.
- Name of the AIDR startup acquired (2026-09); price.
- Whether a log-retention / SIEM-like offering exists (would justify a siem-soc cross-list).

## Sources

- [eSentire homepage](https://www.esentire.com/) — fetched 2026-10-24 — supports: MDR packages, Atlas, AI Operatives / Controlled Autonomy claims, industries, founding; confidence: medium (marketing)
- [IT Brief UK: eSentire acquires AI security startup for Atlas AIDR (2026-09-29)](https://itbrief.co.uk/story/esentire-acquires-ai-security-startup-for-atlas-aidr) — fetched 2026-10-24 — supports: acquisition, AIDR capabilities, customer counts; confidence: medium
- [Anthropic customer story: eSentire](https://claude.com/customers/esentire) — fetched 2026-10-24 — supports: Claude/Bedrock/Agent SDK architecture and metrics; confidence: medium (co-marketing)
- [TechPartner News: James C. Foster becomes CEO of eSentire (2026-03-26)](https://www.techpartner.news/news/zerofox-founder-james-c-foster-becomes-ceo-of-esentire-624592) — fetched 2026-10-24 — supports: CEO change; confidence: medium
- [Reuters via Investing.com: Warburg Pincus-backed eSentire explores sale (2024-08-13)](https://investing.com/news/stock-market-news/warburg-pincusbacked-cybersecurity-firm-esentire-explores-sale-sources-say-3569404) — fetched 2026-10-24 — supports: owners, sale exploration, ARR, HQ; confidence: medium (anonymous sources)
- Cached: `raw/sources/2026-10-24--esentire--site-ownership-aidr.md`; also `raw/sources/2026-10-23--mdr-soc-writeins--one-liner-sources.md`

## History

- [2026-10-24] Page created and researched. Added because of an Oct-2026 CTO survey write-in under Q47 AI SOC (1 respondent, in production). Primary ai-soc-analysts. No siem-soc cross-list (no standalone SIEM/log platform found).
