---
title: Fortra
type: vendor
name: Fortra
slug: fortra
aka: [Digital Guardian, Fortra DLP, Verdasys, HelpSystems, DG Agent, DGMC, Lookout Cloud Security, Clearswift, Titus]
primary_category: dlp
also_listed_in: [network-security-sase, dspm]
website: "https://www.fortra.com/platform/data-loss-prevention"
founded: 1982
hq: Eden Prairie, Minnesota, USA
ownership_state: pe-owned
owner: "TA Associates, Charlesbank Capital Partners, Harvest Partners (and HGGC; controlling holder undisclosed)"
ownership_note: "Fortra (HelpSystems until 2022-11-02) is private-equity owned: HGGC controlling interest 2018-04, TA Associates + Charlesbank 2019-10, Harvest Partners minority 2021-05. HelpSystems acquired Digital Guardian, announced as completed 2021-10-27, terms undisclosed. Digital Guardian brand retired: digitalguardian.com 301-redirects to Fortra DLP (checked 2026-10-24). No sale of Fortra found through 2026-10-24."
acquisition: {announced: null, closed: null, price: null}
funding_total: null
last_funding: null
market_position: {dlp: legacy-incumbent, network-security-sase: niche-specialist, dspm: niche-specialist}
deployment_model: [saas, on-prem]
form_factor: [agent, inline-proxy, api, platform]
data_leaves_tenancy: partial
integrations: [microsoft-365, box, citrix, aws]
mcp_support: unverified
certifications: []
pricing_model: "Subscription per endpoint or per user (Gartner Peer Insights listing); managed-service option; quote-based"
fs_traction: unverified
target_customer: mid-size to large enterprises with IP or regulated data to protect, including firms that want DLP run as a managed service
last_verified: 2026-10-24
verify_after: null
tags: [dlp, endpoint-dlp, managed-dlp, data-classification, genai-dlp, casb, sse, survey-write-in-2026-10]
sources:
  - {claim: "HelpSystems acquisition of Digital Guardian announced as completed 2021-10-27; terms undisclosed", url: "https://www.fortra.com/resources/press-releases/helpsystems-acquires-digital-guardian", date: 2021-10-27, confidence: medium-high}
  - {claim: "Deal reported as done late October 2021", url: "https://www.itjungle.com/2021/12/01/helpsystems-buys-another-dlp-firm", date: 2021-12-01, confidence: medium}
  - {claim: "HelpSystems renamed Fortra 2022-11-02", url: "https://www.fortra.com/resources/press-releases/helpsystems-is-now-fortra", date: 2022-11-02, confidence: high}
  - {claim: "digitalguardian.com 301-redirects to Fortra DLP; 'Digital Guardian is now Fortra DLP'", url: "https://www.fortra.com/platform/data-loss-prevention", date: 2026-10-24, confidence: high}
  - {claim: "PE owners: TA Associates, Charlesbank, Harvest Partners (2025 JAMS divestiture)", url: "https://www.lincolninternational.com/transactions/fortra-has-agreed-to-sell-jams-to-psg-equity-and-2ndwave-software/", date: 2026-10-24, confidence: medium}
  - {claim: "Product architecture, OS coverage, deployment options, GenAI content pack, Mac gaps (competitor blog citing Fortra docs)", url: "https://dope.security/post/digital-guardian-dlp-2026", date: 2026-10-24, confidence: medium}
  - {claim: "Generative AI Content Pack: block classified data via copy/paste, upload, form submit to AI sites (marketing)", url: "https://www.fortra.com/platform/data-loss-prevention/ai", date: 2026-10-24, confidence: medium}
  - {claim: "~600 customers, 5.5M+ users; ChatGPT policies (2023-10)", url: "https://www.fortra.com/resources/press-releases/fortra-achieves-key-customer-milestone-expanded-offerings-its-digital", date: 2023-10-01, confidence: medium}
  - {claim: "Lookout sells Cloud Security business (CASB, ZTNA, SWG) to Fortra, 2025-05-12", url: "https://www.businesswire.com/news/home/20250508462614/en/Lookout-Announces-Sale-of-Its-Cloud-Security-Business-to-Fortra", date: 2025-05-12, confidence: high}
  - {claim: "GoAnywhere MFT CVE-2025-10035 exploited as zero-day; CISA KEV 2025-09-29", url: "https://www.helpnetsecurity.com/2025/09/26/fortra-goanywhere-zero-day-cve-2025-10035/", date: 2025-09-26, confidence: high}
---

# Fortra

> Primary category: [dlp](../categories/dlp.md). Also listed in [network-security-sase](../categories/network-security-sase.md) and [dspm](../categories/dspm.md).

**One-liner** — Fortra is the private-equity-owned security vendor (formerly HelpSystems) that owns **Digital Guardian**, a long-standing endpoint-first enterprise DLP now sold as **Fortra DLP**, available as SaaS, on-prem, or fully managed by Fortra's own analysts.

**What it does** — The DLP product (still called Digital Guardian by most buyers) has four parts:
- **Endpoint agent (DG Agent).** A kernel-level agent that enforces policy before a file operation runs. It keeps enforcing when offline and has tamper resistance and an optional stealth mode. It runs on Windows, macOS, Linux and Citrix VDI. Its documented strength is classic endpoint egress: file activity, print, removable media, copy/paste, screen capture.
- **Classification.** Context-, content- and user-based tags that travel with the file. Fortra claims 300+ file types, 90 languages and database-record matching (vendor claims). Fortra's separate Data Classification Suite (from the Titus and Boldon James acquisitions) plugs in through an SDK.
- **Network and cloud.** A network DLP appliance (SPAN/TAP plus an inline mail transfer agent), and API-based Cloud Data Protection for services such as Office 365 and Box.
- **Managed Security Program.** Fortra analysts run the DLP programme for you: policy tuning, alert triage, reporting. Fortra claims production in 90 days or less (vendor claim). For a small security team this is the main reason to choose it.

**GenAI controls (vendor marketing, 2026-10-24).** A "Generative AI Content Pack" ships prebuilt policies that let users reach AI sites while blocking classified data from leaving by copy/paste, file upload or form submission, with reporting on the data types involved (PII, PCI). Modes run from full block to content-level block to monitor-only. A competitor's 2026 review (dope.security, citing Fortra documentation) found **no documented way to allow a corporate AI tenant while blocking a personal account on the same domain**, and no documented prompt inspection inside desktop AI apps. Treat both as questions for a POC, not as established facts.

Beyond DLP, Fortra bought **Lookout's Cloud Security business** (CASB, ZTNA, secure web gateway), announced 2025-05-12, and markets it as Fortra's SSE and as completing a DSPM offering. That is why it is cross-listed in [network-security-sase](../categories/network-security-sase.md) and [dspm](../categories/dspm.md). Fortra's other lines (GoAnywhere MFT, Clearswift email security, Tripwire, Cobalt Strike, among others) are not covered here.

**Naming / provenance** — Digital Guardian was founded in 2003 as **Verdasys** and renamed Digital Guardian in 2014. **HelpSystems** (founded 1982 as Help/38) acquired it, announced as completed **2021-10-27**, terms undisclosed. HelpSystems renamed itself **Fortra** on **2022-11-02**. The product brand has since been retired: as of 2026-10-24, digitalguardian.com 301-redirects to Fortra's DLP page, and Fortra's Japanese page reads "Digital Guardian is now Fortra DLP". The agent and console still carry the old names (DG Agent, DGMC). Do not confuse it with **FortiDLP**, which is Fortinet's product.

*Slug choice.* The page is slugged `fortra` (the company), not `digital-guardian`. The product brand is gone and the current product name is simply "Fortra DLP". The same company also sells the Lookout-derived SSE/CASB and the Titus classification products that a DLP buyer evaluates alongside it, so one company page covers all of them. `aka:` keeps "Digital Guardian" findable.

**Ownership & viability** — `pe-owned`, private. Investor history: **HGGC** took a controlling interest in April 2018. **TA Associates** and **Charlesbank Capital Partners** invested in October 2019. **Harvest Partners** led a minority investment in May 2021. A 2025 adviser note on Fortra's sale of its JAMS workload-automation unit (to PSG Equity and 2ndWave) calls Fortra "a portfolio company of TA Associates, Charlesbank Capital Partners and Harvest Partners". HGGC's own site still lists Fortra as a current holding. Who controls the company is undisclosed. Fortra is an active consolidator: it bought Digital Guardian, Lookout Cloud Security and many others, and it also sells units off (JAMS). No sale of Fortra itself was found through 2026-10-24. Sponsors that have held it since 2018–2019 are well into a normal hold period, so a sale or break-up within a few years is plausible. For DLP customers the main risk is a carve-out of the data-security business and the roadmap changes that would follow.

**Positioning & differentiators** — `legacy-incumbent` in DLP: a Gartner Enterprise DLP Magic Quadrant Leader in every edition through 2017, after which Gartner retired that Magic Quadrant. It has a large installed base (about 600 customers and 5.5M+ users, per Fortra in October 2023) and is now one product line inside a PE-built portfolio.
- **Against [forcepoint](forcepoint.md) and [microsoft-purview](microsoft-purview.md).** All three are classic content-inspection DLP. Digital Guardian's distinction has long been **endpoint depth** (kernel agent, offline enforcement, Linux and VDI coverage) and **managed DLP** as a standard offering. Purview wins in an all-Microsoft E5 estate because it is already licensed and native to M365. Forcepoint has broader SSE integration of its own.
- **Against AI-native DLP ([cyberhaven](cyberhaven.md), [nightfall-ai](nightfall-ai.md), [mind](mind.md)).** Its GenAI controls are pattern- and classification-based content packs applied to web channels. Cyberhaven's lineage model tracks where data came from, which suits "paste MNPI from a research note into ChatGPT" better than pattern matching does. That is an editorial judgment, not a tested result.
- **Against [netskope](netskope.md) and [zscaler](zscaler.md).** Their DLP is a function of the cloud proxy. Fortra's centre of gravity is the endpoint. The Lookout SSE purchase is Fortra's attempt to close that gap, and how far it has been integrated with Fortra DLP is unverified.

**Who should choose them / anti-fit** — Fits a firm that needs **strong endpoint DLP** (removable media, print, offline laptops, Linux or VDI desktops) and especially one that wants **someone else to run the DLP programme**. The managed service suits a hedge fund or asset manager without a dedicated data-protection analyst. **Anti-fit:** a Microsoft E5 shop that already holds Purview DLP licences. Also a firm whose main worry is prompt-level data leakage into AI tools: an AI-native or proxy-based tool such as [cyberhaven](cyberhaven.md), [nightfall-ai](nightfall-ai.md) or [netskope](netskope.md) is closer to that problem. And a Mac-heavy fleet that needs feature parity with Windows.

**Known weaknesses / gotchas** —
- **Brand churn.** Contracts, docs and console say "Digital Guardian"/"DG", while marketing says "Fortra DLP". Survey respondents will use either name.
- **macOS lag (competitor-reported).** Mac web inspection needed an explicit proxy until version 9.0 added a transparent proxy in March 2025, and that proxy covers only supported browsers and legacy Outlook. Mac controls for Bluetooth and Messages arrived only in 2026. Reviewers report Mac and Linux gaps against Windows.
- **Operational weight.** Reviewers (a small PeerSpot sample) say policy writing takes skill, initial setup is more complex than alternatives, and the agent's CPU and memory use is a concern. This is exactly what the managed service is meant to absorb.
- **Fortra vendor-risk signal.** Fortra's **GoAnywhere MFT** (a different product) had a maximum-severity zero-day, **CVE-2025-10035**, exploited from about 2025-09-10 before Fortra's 2025-09-18 advisory, used for Medusa ransomware and added to CISA KEV on 2025-09-29. An earlier GoAnywhere flaw (CVE-2023-0669) was mass-exploited by the Clop gang. This says nothing direct about the DLP code base, but it belongs in vendor due diligence on Fortra's secure-development and disclosure practices.
- **Thin hedge-fund evidence.** One survey respondent wrote it in (DLP, 1, in production, 2026-10).

**Deployment & data handling** — SaaS (cloud-delivered on AWS since 2017, per Fortra), on-prem, or managed. Enforcement happens locally on the endpoint agent and network appliance. Event data and analytics go to Fortra's Analytics and Reporting Cloud in SaaS deployments, and in the managed programme Fortra analysts see your alerts and the file metadata attached to them. Hence `data_leaves_tenancy: partial`. On-prem keeps it in-house. Hosting regions, retention and what content (as opposed to metadata) is uploaded with incidents are **unverified**. Inline on the endpoint and on the network MTA; out-of-band (API) for cloud apps.

**Integrations & partnerships** — Office 365 and Box via API, Citrix VDI, Fortra Data Classification Suite (Titus, Boldon James) via SDK, and the Lookout-derived CASB/SWG/ZTNA, which integrated with Fortra DLP through a partnership from 2024-03 before the acquisition. SIEM export targets, IdP integration and MCP or agent-framework support are unverified. MCP support is not expected for an endpoint DLP.

**Compliance & FS traction** — Certifications for the SaaS service (SOC 2 Type II, ISO 27001) are **unverified**. No named hedge-fund or asset-manager customers were found. Survey evidence: 1 in-production write-in (2026-10). Endpoint DLP of this kind is common in financial services, but that is not evidenced here.

**Commercial** — Annual subscription, priced per endpoint or per user according to the Gartner Peer Insights listing; the managed programme costs extra. No public price band.

## Open questions

- Which PE sponsor controls Fortra, and is HGGC still a holder?
- Has the Lookout CASB/SWG been integrated into Fortra DLP's policy engine and console, or is it still a separate product?
- GenAI: can it tell a corporate AI tenant from a personal account on the same domain? Does it inspect prompts in desktop AI apps (ChatGPT desktop, Claude desktop) or only in browsers?
- SaaS hosting regions, retention, and what incident content is uploaded to Fortra's cloud or seen by managed-service analysts.
- SOC 2 / ISO 27001 status. Named FS customers.
- Current customer count after 2023.

## Sources

- [HelpSystems Acquires Digital Guardian (Fortra press release)](https://www.fortra.com/resources/press-releases/helpsystems-acquires-digital-guardian) — headline/date via search 2026-10-24 (page returns 403) — supports: acquisition announced as completed 2021-10-27, terms undisclosed; confidence: medium-high
- [HelpSystems buys another DLP firm (IT Jungle, 2021-12-01)](https://www.itjungle.com/2021/12/01/helpsystems-buys-another-dlp-firm) — via search 2026-10-24 — supports: deal done late October 2021; confidence: medium
- [HelpSystems Is Now Fortra (Fortra press release)](https://www.fortra.com/resources/press-releases/helpsystems-is-now-fortra) — via search 2026-10-24 — supports: rename 2022-11-02; confidence: high
- [digitalguardian.com → Fortra DLP redirect](https://www.fortra.com/platform/data-loss-prevention) — checked 2026-10-24 (301) — supports: brand retired; confidence: high
- [Fortra sells JAMS (Lincoln International)](https://www.lincolninternational.com/transactions/fortra-has-agreed-to-sell-jams-to-psg-equity-and-2ndwave-software/) — via search 2026-10-24 — supports: current PE owners; confidence: medium
- [Digital Guardian DLP in 2026 (dope.security)](https://dope.security/post/digital-guardian-dlp-2026) — fetched 2026-10-24 — supports: architecture, deployment, GenAI pack, Mac gaps, reviewer complaints; confidence: medium (**competitor blog**, cites Fortra docs)
- [Block and Gain Visibility Around ChatGPT and AI (Fortra)](https://www.fortra.com/platform/data-loss-prevention/ai) — via search 2026-10-24 — supports: Generative AI Content Pack; confidence: medium (vendor marketing)
- [Fortra customer milestone for Digital Guardian (2023-10)](https://www.fortra.com/resources/press-releases/fortra-achieves-key-customer-milestone-expanded-offerings-its-digital) — via search 2026-10-24 — supports: 5.5M users, ChatGPT policies; confidence: medium
- [Lookout Announces Sale of Its Cloud Security Business to Fortra (Business Wire)](https://www.businesswire.com/news/home/20250508462614/en/Lookout-Announces-Sale-of-Its-Cloud-Security-Business-to-Fortra) — via search 2026-10-24 — supports: CASB/ZTNA/SWG acquisition, 2025-05-12; confidence: high
- [Fortra GoAnywhere zero-day CVE-2025-10035 (Help Net Security)](https://www.helpnetsecurity.com/2025/09/26/fortra-goanywhere-zero-day-cve-2025-10035/) — via search 2026-10-24 — supports: exploitation timeline, KEV; confidence: high
- Cached: `raw/sources/2026-10-24--fortra--digital-guardian-acquisition-and-rebrand.md`, `raw/sources/2026-10-24--fortra--dlp-product-genai-lookout.md`

## History

- [2026-10-24] Page created and researched. Added because of an October 2026 CTO survey write-in under DLP (Q52, "Digital Guardian (Fortra)", 1 respondent, in production). Slugged `fortra` (company) rather than `digital-guardian` because the product brand is retired (digitalguardian.com redirects to Fortra DLP). Primary dlp. Cross-listed network-security-sase (Lookout CASB/SWG/ZTNA, 2025) and dspm (Fortra's own DSPM claim), per the "if the vendor claims it, include it" rule. Ownership recorded as pe-owned. The 2021 Digital Guardian deal is product provenance, not an open M&A event, so it is not in `acquisition:`.
