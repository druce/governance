---
type: vendor
name: Seraphic Security
slug: seraphic
categories: [enterprise-browser]
layer: ux
aliases: [Seraphic, Seraphic Algorithms]
website: https://seraphicsecurity.com/
founded: 2020
hq: Herzliya, Israel (US office: Wilmington, MA)
ownership: acquired
ownership_detail: "Definitive agreement to be acquired by CrowdStrike for $420M announced 2026-01-13; expected to close in CrowdStrike's Q1 FY'27 (pending close as of 2026-06-28). CrowdStrike Falcon Fund was a prior Series A investor."
ownership_confidence: high
funding_total: $29M (Series A)
last_funding: Series A, $29M, 2025-01 (incl. CrowdStrike Falcon Fund)
deployment: [saas, sdk]
target_customer: enterprise (incl. regulated; managed + unmanaged/BYOD, contractors)
hedge_fund_fit: medium
priority: optional
trifecta_relevance: [untrusted-input, egress]
status: researched
confidence: high
sources_count: 2
last_updated: 2026-06-28
tags: [browser-security, secure-browsing, crowdstrike]
---

# Seraphic Security

> Browser-runtime security that turns **any** existing browser (Chrome, Edge, Safari, Firefox, agentic browsers) into a "secure enterprise browser" — no separate browser, no traffic rerouting. Primary category: [[enterprise-browser]].

**One-liner** — Adds enterprise security and governance *inside* the browsers employees already use, rather than making them switch to a dedicated secure browser.

## What it does

Seraphic injects protection into the browser runtime to deliver in-session visibility and control: defense against zero-day browser exploits, phishing and browser-based attacks, plus data-loss prevention, policy enforcement, and governance over web/SaaS/GenAI usage. Because it works within any standard browser and on managed *or* unmanaged devices, it is pitched as a lighter-weight alternative to deploying a full dedicated enterprise browser, and as a way to extend control to contractors and BYOD users ("agentless-style" coverage).

## Where it sits in the stack

[[enterprise-browser]] category, **UX layer**. Enterprise browsers/browser-security tools mainly control the **egress** and **untrusted-input** legs of the lethal trifecta at the point where the user meets the web: they govern what data can leave (copy/paste, download, upload, paste-into-GenAI) and filter hostile web/page content reaching the user. Sits in the boundary between the untrusted web (red zone) and corporate apps/data (green/yellow), enforcing policy at the last mile.

## Deployment & architecture

Delivered as a SaaS-managed capability that operates within the existing browser runtime (via extension/injected runtime rather than a separate browser binary), working across Chrome, Edge, Safari, Firefox and agentic browsers, on managed and unmanaged endpoints. No traffic rerouting through an inline proxy is required, distinguishing it from remote-browser-isolation/proxy designs. Post-acquisition, CrowdStrike intends to integrate Seraphic's in-session browser telemetry with the Falcon platform's endpoint telemetry and SGNL's continuous-authorization technology.

## Positioning & differentiators

Seraphic competes in the "secure any browser" segment rather than the "ship a custom Chromium browser" segment. Nearest neighbors:
- vs [[island]] and [[prisma-access-browser]] — those ship a dedicated managed Chromium browser; Seraphic instead secures the user's existing browser.
- vs [[layerx]] — closest analog (browser-extension-delivered security on existing browsers); compete directly.
- vs [[red-access]] — both pursue agentless/"any browser" secure browsing; Red Access leans on a session-based SSE-extension framing.
- vs [[menlo-security]] — Menlo's heritage is remote browser isolation (rendering/proxy); Seraphic avoids rerouting traffic.
- vs [[chrome-enterprise]] and [[microsoft-edge-business]] — native browser-management controls from the browser makers; Seraphic is browser-agnostic and adds deeper security/DLP.

## Ownership, funding & M&A

- **Confirmed acquisition (announced, pending close).** CrowdStrike announced a definitive agreement to acquire Seraphic on **2026-01-13** for **$420 million** (predominantly cash, partial stock subject to vesting), expected to close in CrowdStrike's **Q1 FY'27**. Source: CrowdStrike press release + SecurityWeek. As of 2026-06-28 the deal is announced but may not yet have legally closed; ownership marked `acquired` with `high` confidence on the agreement, with the close date as the open item.
- Founded **2020** by CEO **Ilan Yeshua** and CTO **Avihay Cohen** (legal entity Seraphic Algorithms Ltd.).
- **$29M Series A** in **January 2025**; investors included the **CrowdStrike Falcon Fund** (i.e. CrowdStrike was already a strategic investor before acquiring).

> Note: the research brief flagged checking for a possible SentinelOne acquirer. The confirmed acquirer is **CrowdStrike**, not SentinelOne; no competing acquirer claim exists, so this is **not** a contradiction.

## CTO / hedge-fund lens

**Priority: optional.** Browser-layer security is a real control point for a fund where most sensitive work happens in SaaS and the browser, and where contractors/BYOD are in scope. Seraphic's appeal is avoiding a forced browser switch. For a hedge-fund CTO the practical question post-acquisition is platform alignment: this becomes most attractive to shops already on (or moving to) **CrowdStrike Falcon** for endpoint, where browser telemetry folds into one console. Standalone buyers should weigh roadmap/independence risk while the deal integrates. No direct SR 11-7 / model-risk role; relevance is data egress and GenAI-usage governance, not model validation.

## Competitors / alternatives

[[layerx]], [[red-access]], [[island]], [[menlo-security]], [[prisma-access-browser]], [[chrome-enterprise]], [[microsoft-edge-business]]

## Open questions / to verify

- Confirm the legal **close** of the CrowdStrike acquisition (expected Q1 FY'27) and any change to standalone product availability/branding.
- Whether total funding beyond the $29M Series A exists (no earlier round confirmed).
- Exact runtime mechanism (extension vs deeper injection) per current technical docs.

## Sources
- [CrowdStrike to Acquire Seraphic, Turning Any Browser into a Secure Enterprise Browser](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-seraphic-security/) — fetched 2026-06-28 — supports: acquirer (CrowdStrike), announce date 2026-01-13, expected close Q1 FY'27, CEO Ilan Yeshua, prior $29M Series A incl. Falcon Fund, product description; confidence: high
- [CrowdStrike to Acquire Browser Security Firm Seraphic for $420 Million (SecurityWeek)](https://www.securityweek.com/crowdstrike-to-acquire-browser-security-firm-seraphic-for-420-million/) — fetched 2026-06-28 — supports: $420M price, cash+stock structure, product capabilities; confidence: high
- [Seraphic Security secures $29 million Series A (CTech/Calcalist)](https://www.calcalistech.com/ctechnews/article/s1rloxyujx) — fetched 2026-06-28 — supports: founded 2020, founders Yeshua/Cohen, Herzliya HQ + Wilmington MA office, $29M Series A 2025-01; confidence: medium

## History
- [2026-06-28] Stub created from seed registry.
- [2026-06-28] Researched; established founded 2020 (Herzliya, IL; US office Wilmington MA), founders Yeshua/Cohen, $29M Series A Jan-2025 (incl. CrowdStrike Falcon Fund). Confirmed CrowdStrike acquisition agreement ($420M, announced 2026-01-13, pending close Q1 FY'27) via acquirer press release; set ownership=acquired, confidence high. No HARD contradiction (acquirer is CrowdStrike, not the SentinelOne hint).
