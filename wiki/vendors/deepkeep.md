---
title: DeepKeep
type: vendor
name: DeepKeep
slug: deepkeep
aka: [DeepKeep Ltd., DeepKeep.ai, DeepKeep for LLM, DeepKeep for Vision, DeepKeep for VLM]
primary_category: ai-runtime-security
also_listed_in: [ai-red-teaming, ai-spm, agent-runtime-security]
website: https://www.deepkeep.ai
founded: 2021
hq: Tel Aviv, Israel
ownership_state: independent
owner: null
ownership_note: Independent, VC-backed. $10M seed announced 2024-05-01, led by Awz Ventures. Aggregators (Tracxn/PitchBook/Crunchbase) claim ~$19M total across 4 rounds and a January 2026 round involving OurCrowd, but DeepKeep has issued no funding release since the 2024 seed and no primary source confirms either figure — see Open Questions. No M&A found as of 2026-08-22.
acquisition: {announced: null, closed: null, price: null}
funding_total: unverified (~$19M per aggregators; only the $10M seed is confirmed)
last_funding: Seed $10M, announced 2024-05-01, led by Awz Ventures
market_position: {ai-runtime-security: niche-specialist, ai-red-teaming: niche-specialist, ai-spm: niche-specialist, agent-runtime-security: niche-specialist}
deployment_model: [saas, on-prem, in-tenant, hybrid]
form_factor: [platform, api, inline-proxy]
data_leaves_tenancy: partial
integrations: [agentforce, openai-agents, crewai, amazon-bedrock-agentcore, n8n, make, microsoft-agent-frameworks]
mcp_support: unverified
certifications: [ISO 27001 (vendor-stated), ISO 9001 (vendor-stated), SOC 2 (vendor-stated; no Type marking), GDPR (vendor-stated)]
pricing_model: null
fs_traction: unverified
target_customer: Enterprise security teams securing self-built LLM *and computer-vision* systems across the full lifecycle, from one console
last_verified: 2026-08-22
verify_after: 2026-11-22
tags: [ai-security, ai-firewall, guardrails, red-teaming, model-scanning, mlbom, agent-security, computer-vision, ai-trism, israel]
sources:
  - {claim: platform-modules-deployment-logos, url: "https://www.deepkeep.ai/", date: 2026-08-22, confidence: medium}
  - {claim: founding-hq-seed-round, url: "https://www.securityweek.com/deepkeep-launches-ai-native-security-platform-with-10-million-in-seed-funding/", date: 2026-08-22, confidence: high}
  - {claim: agent-scanner-scope-frameworks, url: "https://www.prnewswire.com/il/news-releases/deepkeep-launches-ai-agent-attack-surface-mapping-and-discovery-solution-302702359.html", date: 2026-08-22, confidence: medium}
  - {claim: vibe-red-teaming, url: "https://siliconangle.com/2026/04/20/deepkeep-rolls-vibe-ai-red-teaming-test-ai-apps-agents/", date: 2026-08-22, confidence: low}
  - {claim: gartner-representative-provider, url: "https://www.prnewswire.com/il/news-releases/deepkeep-recognized-in-the-2026-gartner-competitive-landscape-ai-operations-management-302791556.html", date: 2026-08-22, confidence: medium}
---

# DeepKeep

> **Filing note.** DeepKeep is a five-module suite, not a single product, so no
> one category holds it cleanly. It is filed primary in
> [ai-runtime-security](../categories/ai-runtime-security.md) because the AI
> Firewall is the lead SKU and the thing a buyer would actually swap in, with
> cross-listings in [ai-red-teaming](../categories/ai-red-teaming.md),
> [ai-spm](../categories/ai-spm.md) and
> [agent-runtime-security](../categories/agent-runtime-security.md). Its Model
> Scanning module does MLBOM and CVE detection on *model artifacts*, which is ML
> supply chain — but not
> [software-supply-chain](../categories/software-supply-chain.md) as this wiki
> defines it (SAST/SCA/pipeline security for code you ship). DeepKeep does no
> code scanning, so it is deliberately **not** cross-listed there. Same shape as
> [hiddenlayer](hiddenlayer.md), which is filed the same way.

**One-liner** — An Israeli AI-security suite that puts runtime guardrails, red
teaming, AI discovery, agent attack-surface mapping and model scanning behind one
console — and is the rare vendor here that covers **computer vision** as well as
LLMs.

**What it does** — Five modules, sold as a lifecycle platform:

- **AI Firewall** — real-time detection and guardrails; the site claims **60+
  runtime guardrails** for apps and agents. The inline enforcement point.
- **AI Red Teaming** — automated adversarial evaluation and robustness tests,
  plus **Vibe AI Red Teaming** (launched 2026-04-20), a human-steered mode where
  an agent runs the campaign but staff intervene at decision points, adapt the
  plan on intermediate findings, and inject scenarios mid-run.
- **AI Lens** — discovery, visibility and access control over who is using what
  AI across teams; the shadow-AI / usage-control angle.
- **AI Agent Scanner** — launched 2026-03-03. Maps an agent's connected tools,
  data sources and reachable actions into a visual attack-surface graph, scores
  it against the **OWASP Top 10 for Agentic Applications**, and — *for select
  frameworks only* — places firewalls and guardrails based on observed behaviour.
- **Model Scanning** — static and dynamic checks on model artifacts, producing an
  **MLBOM** and CVE detection.

The suite is sold in two lines, **DeepKeep for LLM** and **DeepKeep for Vision**.
The vision half is genuinely differentiating: nearly every peer in
[ai-runtime-security](../categories/ai-runtime-security.md) is a text/prompt
inspector only.

**Naming / provenance** — Founded **2021** by **Rony Ohayon** (CEO); CTO is
**Yossi Altevet**. Tel Aviv. Launched publicly with the seed round in May 2024,
pitched as an "AI-native TRiSM" platform (Gartner's Trust, Risk and Security
Management framing). No renames or spinouts found. Do not confuse with
"Deepkeep Systems" as it appears in some funding aggregators — same company,
aggregator naming.

**Ownership & viability** — Independent and VC-backed. The only round with a
primary source is the **$10M seed announced 2024-05-01**, led by **Awz Ventures**.
Funding aggregators claim ~$19M total across four rounds including a January 2026
round involving OurCrowd, but DeepKeep has published nothing about it and no
primary source corroborates it, so this page does not assert it. At a confirmed
$10M seed and no confirmed Series A more than two years later, this is a **small
vendor in a consolidating category** — [prompt-security](prompt-security.md),
[aim-security](aim-security.md), [robust-intelligence](robust-intelligence.md)
and Protect AI have all been absorbed by platform vendors. Acquisition or
stall are both live outcomes; underwrite accordingly.

**Positioning & differentiators**

- **Multimodal, not just text.** DeepKeep for Vision covers computer-vision
  pipelines. If you have vision models — document/ID processing, surveillance,
  industrial inspection — almost nobody else on the
  [ai-runtime-security](../categories/ai-runtime-security.md) shortlist will
  cover them. For a hedge fund running text and tabular models only, this
  differentiator is worth nothing.
- **Breadth from one console.** Firewall + red team + discovery + agent mapping +
  model scanning in one contract is a real convenience versus assembling
  [lakera](lakera.md) + [splxai](splxai.md) + a posture tool. The tradeoff is the
  usual one: none of the five modules is the category's best.
- **Free agent scanner as the funnel.** The AI Agent Scanner is offered free at
  `agentscanner.deepkeep.ai`. That makes it cheap to trial and a genuinely useful
  way to see your agent attack surface before committing to anything.
- **Agent-framework coverage is broad and includes the low-code tier** —
  Agentforce, OpenAI Agents, CrewAI, Amazon Bedrock AgentCore, n8n and Make.
  Covering n8n and Make matters: that is where ungoverned business-built agents
  actually live, and it is the same ground [zenity](zenity.md) works.

**Who should choose them / anti-fit** — Best fit: an enterprise with a mixed
LLM-and-vision AI estate that wants one vendor and one console across the
lifecycle, and is comfortable buying from a small Israeli startup. **Anti-fit:**
a firm that already owns a platform with an AI-security module
([prisma-airs](prisma-airs.md), [cisco-ai-defense](cisco-ai-defense.md),
[wiz](wiz.md)) — DeepKeep has to beat something you already pay for. Also an
anti-fit if you need best-of-breed depth in exactly one slot: buy
[lakera](lakera.md) for prompt-injection detection or a red-teaming specialist
for red teaming. And an anti-fit for procurement teams that need a SOC 2 report
in hand before signing, since DeepKeep publishes badges but no retrievable
report — you will be waiting on the vendor to produce one (see below).

**Known weaknesses / gotchas**

- **Certifications are claimed on the website, not evidenced.** The footer
  carries four badge images — **ISO 27001, ISO 9001, SOC 2 and GDPR** — and
  nothing sits behind them: none of the badges is a hyperlink, there is no trust
  centre, compliance page or downloadable report, and no certificate number,
  auditor, audit period or scope statement appears anywhere. **The SOC 2 badge
  carries no Type marking**, which is the detail that matters — Type I is a
  point-in-time opinion on control *design*, Type II tests operating
  effectiveness over a period, and only the latter is worth much to a regulated
  buyer. For a product that sits inline on prompts and responses, ask for the
  report, the audit period, the auditor and the SOC 2 **Type** before treating
  any of these badges as evidence.
- **No public pricing at all**, and no published tier structure. Full sales cycle.
- **"For select frameworks" is doing work.** The Agent Scanner *discovers and
  maps* across the listed frameworks, but *runtime enforcement* on agents is
  limited to a subset the release does not name. Get the enumerated list in
  writing before assuming agent coverage.
- **Marketing claims outrun independent evidence.** "First-of-its-kind" Vibe red
  teaming has no third-party validation; the trade coverage restates the press
  release verbatim. The "60+ guardrails" count is a vendor number with no public
  benchmark behind it. Treat detection efficacy as untested until you test it.
- **Gartner mention is an inclusion, not a ranking.** DeepKeep is a
  *Representative Provider* in the 2026 Gartner *Competitive Landscape: AI
  Operations Management* (report May 2026, announced 2026-06-04). That is a
  listing, not a Magic Quadrant position, and it is in an **AI operations**
  landscape rather than an AI-security one.
- **No MCP story found.** Nothing on the site or in releases mentions Model
  Context Protocol, in a category where peers are racing to cover MCP tool calls.

**Deployment & data handling** — One SaaS console, with the platform deployable
in **SaaS, on-prem, your own VPC, or air-gapped**. The air-gapped and in-tenant
options are the reason to look at DeepKeep if prompt content cannot leave your
boundary. In default SaaS mode the firewall is inline on prompts and responses,
so `data_leaves_tenancy: partial` — inspected content transits DeepKeep unless
you self-deploy. Retention, training-use and latency numbers are **not published**;
all three are must-asks. The free hosted Agent Scanner at
`agentscanner.deepkeep.ai` is separate from your tenancy — do not point it at
production agents before you understand what it retains.

**Agent-security relevance** — The Agent Scanner is explicitly built for the case
where an agent's own permissions become the attack surface: it enumerates the
tools and reachable actions an agent has, which is exactly the mapping you need
before you can reason about whether untrusted input, sensitive data and an egress
path have collapsed into a single agent context (see
[overview](../overview.md) and
[agent-runtime-security](../categories/agent-runtime-security.md)). Mapping is
the strong half; enforcement is framework-limited.

**Integrations & partnerships** — Agent frameworks: Microsoft-based frameworks,
Agentforce, OpenAI Agents, CrewAI, Amazon Bedrock AgentCore, n8n, Make. No
published SIEM, IdP, gateway or observability integrations were found — notable
for a security product that should be feeding
[siem-soc](../categories/siem-soc.md). No marketplace listings found. No FS
channel partners found.

**Compliance & FS traction** — Four compliance badges (ISO 27001, ISO 9001,
SOC 2, GDPR) are displayed in the site footer as static images with no report,
trust centre or Type marking behind them; treat them as vendor-stated until you
hold the documents. Logos shown on the
site are **NTT Data, ST Engineering and EY** — systems integrators and a Big Four
firm, i.e. a partner/services motion, not named end-user references. **No
financial-services customer is named anywhere**, and nothing indicates
hedge-fund-scale deployment. For this wiki's reader, DeepKeep is currently an
unproven-in-FS vendor.

**Commercial** — No public pricing, no published packaging, no free tier for the
platform (the Agent Scanner alone is free). Assume enterprise annual contract and
a full sales cycle.

## Open questions

- **Funding since the 2024 seed.** Aggregators say ~$19M / 4 rounds and an
  OurCrowd round in January 2026; DeepKeep has announced nothing. Is there a
  Series A? Unresolved — aggregator-only, not asserted on this page.
- **What backs the four badges?** ISO 27001, ISO 9001, SOC 2 and GDPR are
  displayed, so audits are being asserted — but no report, certificate number,
  auditor, audit period or scope is published, and the SOC 2 badge shows no Type.
  Is the SOC 2 a Type I or a Type II? What is the ISO 27001 scope and which body
  issued it? A targeted search on 2026-08-22 retrieved nothing; **"not
  retrievable" is not "does not exist"** — these are the questions for the first
  call, not a conclusion.
- **Which frameworks get runtime enforcement**, as opposed to discovery/mapping
  only? The release says "select frameworks" without enumerating.
- **MCP support** — none found, but absence of evidence only. Unverified.
- **Latency and retention** for the inline AI Firewall — unpublished.
- **Headcount and FS references** — unverified.
- **Is DeepKeep for Vision a real, separately-supported line** or marketing
  packaging around the same scanners? Unverified.

## Sources

- [DeepKeep — product site](https://www.deepkeep.ai/) — fetched 2026-08-22 — supports: five modules, two product lines, deployment options, customer logos; confidence: medium (vendor marketing).
- [DeepKeep — About / site footer](https://www.deepkeep.ai/about) — re-fetched 2026-08-22 — supports: the four compliance badges (ISO 27001, ISO 9001, SOC 2, GDPR), their alt text, that none is a hyperlink, that the SOC 2 badge carries no Type marking, and that no trust centre or downloadable report is linked; confidence: high (primary, read directly).
- [SecurityWeek — DeepKeep Launches AI-Native Security Platform With $10 Million in Seed Funding](https://www.securityweek.com/deepkeep-launches-ai-native-security-platform-with-10-million-in-seed-funding/) — fetched 2026-08-22 — supports: founded 2021, Rony Ohayon, Tel Aviv, $10M seed 2024-05-01 led by Awz Ventures; confidence: high.
- [PR Newswire — DeepKeep Launches AI Agent Attack Surface Mapping and Discovery Solution](https://www.prnewswire.com/il/news-releases/deepkeep-launches-ai-agent-attack-surface-mapping-and-discovery-solution-302702359.html) — fetched 2026-08-22 — supports: Agent Scanner scope, framework list, OWASP Agentic Top 10 mapping, free hosted scanner, 2026-03-03 date; confidence: medium (vendor release).
- [SiliconANGLE — DeepKeep rolls out Vibe AI Red Teaming](https://siliconangle.com/2026/04/20/deepkeep-rolls-vibe-ai-red-teaming-test-ai-apps-agents/) — fetched 2026-08-22 — supports: Vibe red teaming, 2026-04-20, CTO name; confidence: low (restates vendor release, no independent commentary).
- [PR Newswire — DeepKeep Recognized in the 2026 Gartner Competitive Landscape: AI Operations Management](https://www.prnewswire.com/il/news-releases/deepkeep-recognized-in-the-2026-gartner-competitive-landscape-ai-operations-management-302791556.html) — fetched 2026-08-22 — supports: Representative Provider listing, May 2026 report, About-DeepKeep boilerplate; confidence: medium (vendor release about a paywalled report).
- Cached: `raw/sources/2026-08-22--deepkeep--platform-modules-and-founding.md`, `raw/sources/2026-08-22--deepkeep--agent-scanner-and-vibe-red-teaming.md`, `raw/sources/2026-08-22--deepkeep--footer-compliance-badges.md`

## History

- [2026-08-22] Page created and researched in one pass via wiki-create + wiki-research. Category call (`ai-runtime-security` primary, three cross-lists, no `software-supply-chain`) recorded in `log.md`.
- [2026-08-22] **Correction.** The page asserted in three places that DeepKeep publishes no certifications; `certifications: []` and an open question rested on the same claim. Wrong: the site footer carries ISO 27001, ISO 9001, SOC 2 and GDPR badges. Re-fetched https://www.deepkeep.ai/about and confirmed the badges exist, none is a hyperlink, the SOC 2 badge carries no Type marking, and no trust centre or report sits behind them. Reframed from "no certification is published" to "claimed on the website, not evidenced" (the idiom already used on [signoz](signoz.md)), `certifications:` set with the `(vendor-stated)` convention used on [hadrius](hadrius.md), and the procurement advice changed to ask for the report, period, auditor and SOC 2 Type. Source cached.
