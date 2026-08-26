# Competitor-discovery scan — scored candidates

**Date:** 2026-08-25 (sweep completed 2026-08-26)
**Method:** `METHOD.md` · **Plan:** `PLAN.md` · **Evidence:** one `<category>.jsonl` per category

## Coverage

All **236** vendor pages queried, one Google search each, Knowledge-Panel
"People also search for" carousel extracted from the DOM.

| Outcome | Vendors |
|---|---|
| No carousel at all | 198 (84%) |
| Company-panel carousel | 26 |
| Small 4-tile carousel | 7 |
| Carousel returned pure geographic/employer noise | 3 |
| **Produced any usable peer names** | **32 (14%)** |

119 distinct peer names surfaced. 55 were already wiki vendors (the technique
correctly re-identifies our own coverage). **64 were new**, of which most are
out-of-scope infrastructure; **13 score ≥8 and form the recommended research queue.**

## Scoring

Four axes, 0–3 each, total 0–12.

- **Freq** — co-mention count: 3 = 5+ wiki vendors surfaced it, 2 = 3–4, 1 = 2, 0 = 1
- **Fit** — maps to an existing taxonomy category and matters to the AI-governance thesis
- **Alive** — shipping and independent; penalised for acquired-and-folded
- **CTO** — would a mid-size hedge fund / asset manager plausibly shortlist it

## Tier A — recommended `wiki-research` queue (score ≥ 8)

| Score | Candidate | F/Fit/Alive/CTO | Proposed category | Surfaced by | Note |
|---|---|---|---|---|---|
| 10 | **Centraleyes** | 2/3/3/2 | `enterprise-grc` | credo-ai, drata, holistic-ai, onspring | Cyber risk & compliance management. Strongest signal in the whole scan — surfaced by four different wiki GRC vendors. |
| 10 | **Checkmarx** | 2/3/3/2 | `software-supply-chain` | aikido-security, jfrog, snyk, sonatype | AppSec/SAST incumbent. Surfaced by four; a clear category gap. |
| 10 | **Hyperproof** | 2/3/3/2 | `enterprise-grc` | drata, logicgate, vanta | Compliance operations; sits directly between Drata and LogicGate. |
| 9 | **Veracode** | 1/3/3/2 | `software-supply-chain` | aikido-security, snyk | AppSec incumbent, PE-owned. |
| 9 | **Black Duck** | 1/3/3/2 | `software-supply-chain` | jfrog, snyk | SCA; spun out of Synopsys — **verify current ownership**. |
| 9 | **Feedzai** | 0/3/3/3 | `comms-surveillance` / financial-crime | nice-actimize | AI financial-crime platform. Highest CTO relevance of any candidate. |
| 8 | **Verafin** | 0/3/2/3 | financial-crime | nice-actimize | AML/fraud; Nasdaq-owned — **verify**. Direct relevance to regulated financial firms. |
| 8 | **ThetaRay** | 0/3/3/2 | financial-crime | nice-actimize | AI AML/transaction monitoring. |
| 8 | **Panorays** | 0/3/3/2 | `vendor-risk` | onetrust | Third-party risk management. |
| 8 | **SAI360** | 0/3/3/2 | `enterprise-grc` | onspring | GRC suite. |
| 8 | **Sprinto** | 1/3/3/1 | `enterprise-grc` | drata, logicgate | Compliance automation; SMB-leaning, so lower CTO fit. |
| 8 | **Mend.io** | 0/3/3/2 | `software-supply-chain` | sonatype | SCA/AppSec. |
| 8 | **Imperva** | 2/2/2/2 | `network-security-sase` (adj. `dspm`) | cato-networks, cloudflare, f5 | WAF/data security; Thales-owned — **verify**. Adjacent rather than core to the AI thesis. |

**The three financial-crime names (Feedzai, Verafin, ThetaRay) are the most
interesting result of the scan for this wiki's audience.** They came from a single
source (NICE Actimize) so they score low on frequency, but they sit squarely in the
hedge-fund/asset-manager problem space and have no page today. Frequency
under-rates them because the wiki only has one vendor in that neighbourhood — a
known weakness of co-mention scoring on thin categories.

## Tier B — worth a look (6–7)

| Score | Candidate | Proposed category | Note |
|---|---|---|---|
| 7 | Alation | `data-access-governance` | Data catalog/governance; peer of Immuta and Collibra. |
| 7 | Langwatch | `llm-observability` | LLM observability; early-stage. |
| 7 | TrustArc | `enterprise-grc` | Privacy compliance. |
| 7 | Fortinet | `network-security-sase` | Incumbent; genuine category gap. |
| 7 | Trend Micro | `edr-xdr` | Incumbent; genuine category gap. |
| 7 | Dynatrace | `llm-observability` | APM/observability; overlaps the logging half of `siem-soc`. |
| 7 | New Relic | `llm-observability` | Same. |
| 6 | Aryaka | `network-security-sase` | SASE/SD-WAN. |
| 6 | Mimecast | `dlp` | Email security; PE-owned. |
| 6 | KnowBe4 | none (security awareness) | No current category; would need a taxonomy decision. |
| 6 | Code42 | `dlp` | Insider-risk DLP; folded into Mimecast — **verify**. |
| 6 | Langdock | `enterprise-ai-assistant` | German enterprise AI assistant. |
| 6 | SolarWinds | `siem-soc` (logging half) | Observability incumbent. |

## Tier C — rejected as out of scope

Domain registrars and CDN/hosting (Namecheap, GoDaddy, Hostinger, NameSilo, Network
Solutions, Netlify, Vercel, DigitalOcean, Fastly, Cloudinary, Sucuri, StackPath,
Quad9, OpenDNS), general infrastructure (RabbitMQ, NetApp, Nutanix, VMware, Arista,
Juniper, Citrix, Radware, SonicWall, Gen Digital), consumer AI (DeepSeek), legacy or
absorbed brands (IronPort, AppDynamics, Mandiant, OneLogin, Endpoint Protector /
CoSoSys, Cookiebot, K2view), and India-SaaS noise from the Portkey carousel
(Atomicwork, Gnani.ai, LimeChat).

**Dedupe misses corrected by hand:** "Collibra Belgium BV" → existing `collibra`;
"NICE Systems Ltd." → parent of existing `nice-actimize`.

## Reliability caveats — read before acting

1. **Nothing here is a source.** Per CLAUDE.md §7 a co-search carousel is a hint, not
   evidence. Every candidate needs its own `wiki-research` pass with a cached
   primary source before a page is created. All ownership notes above are flagged
   **verify**.
2. **Recall, not census.** The carousel is popularity-weighted co-search. The SIEM
   probes never surfaced Microsoft Sentinel, IBM QRadar, Securonix, Devo, Graylog,
   Panther or Hunters — all real players. Absence here means nothing.
3. **The AI-native half of the wiki is invisible to this method.** Every vendor in
   `agent-runtime-security`, `ai-red-teaming`, `ai-runtime-security`, `ai-spm`,
   `mcp-gateway`, `ai-soc-analysts` and most of `ai-access-governance` returned
   nothing — those companies have no Knowledge Graph entity. Coverage gaps in the
   categories that matter most to this wiki cannot be found this way.
4. **Google personalises the SERP.** "Palo Alto Networks" returned a *local* business
   pack (searcher located in Brooklyn), not a company panel. Several large vendors
   (CyberArk, Zscaler, Datadog, Varonis, GitLab) genuinely have no carousel —
   verified for CyberArk by direct DOM inspection, not a timing artifact.
5. **Query form matters.** Plain vendor names work; adding qualifiers suppresses the
   carousel ("Credo AI" returns peers, "Credo AI governance" returns none).
6. **Geographic noise.** For vendors without a company entity Google falls back to a
   local-business carousel listing physically nearby firms. Three vendors hit this
   (Lakera → Zürich companies, SailPoint → Austin employers, Black Kite → Turkish
   companies) and were discarded, not scored.

## One correction to check in the existing wiki

Google's carousel labels CalypsoAI **"Now part of F5"** (surfaced via Credo AI and
Holistic AI). `wiki/vendors/calypsoai.md` should be checked against a primary source
and updated if confirmed.
