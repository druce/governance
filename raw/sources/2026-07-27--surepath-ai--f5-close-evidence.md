# SurePath AI × F5 — close evidence as of 2026-07-27 (F5 press release + SEC cash-flow arithmetic + surepath.ai banner)

- **Fetched:** 2026-07-27
- **Good for:** establishing that the F5 → SurePath AI deal is **closed** (not pending), bounding the
  close inside F5's fiscal Q3 2026 (2026-04-01 → 2026-06-30), and the only public number attached to
  it (~$47.6M cash, net of cash acquired, **inferred** — F5 has not itemized it). Also: SurePath's
  brand and standalone product survive, unlike CalypsoAI's.
- **Confidence:** high on "closed"; **medium** on the $47.6M attribution (arithmetic inference from
  F5's own GAAP cash-flow statement, not an F5 statement naming SurePath).

---

## 1. F5 press release — "F5 launches AI Security Platform…" (published 2026-06-22)

- **URL:** https://www.f5.com/company/news/press-releases/f5-ai-security-platform-control-enterprise-risk
- Fetched 2026-07-27 (also fetched 2026-07-13).

Subhead:

> F5 acquires SurePath AI to enhance new AI Security Platform, tackle shadow AI risks, and deliver
> continuous visibility, governance, and protection for enterprise AI

Body:

> F5 also announced the acquisition of SurePath AI, a pioneer in network-based AI discovery, intent
> classification, and shadow AI detection, as a key component in the launch of the new F5 AI Security
> Platform to safeguard enterprise AI deployments.

> The addition of SurePath AI powers the F5 AI Security Platform's approach to network-based AI
> discovery, identifying AI usage across the enterprise, including shadow AI, without requiring direct
> application integrations. With frictionless deployment through network redirects and out-of-band
> analysis, SurePath AI gives security teams a unified visibility layer that detects unauthorized AI
> activity, classifies the intent behind each workflow, and continuously traces agent tool calls and
> MCP server connections. This visibility feeds directly into the F5 AI Security Platform, informing
> the risks to be tested by F5 AI Red Team and mitigated by F5 AI Guardrails.

**Note on tense:** the release uses completed-transaction language throughout ("F5 acquires…",
"announced the acquisition of…", "The addition of SurePath AI powers…"). There is **no** "definitive
agreement", "subject to customary closing conditions", or "expected to close" language anywhere — the
pattern F5 used for CalypsoAI's *pending* phase in its 2025-09-11 release. **Terms are not disclosed
and no separate closing date is given.**

## 2. surepath.ai homepage banner (live, HTTP 200, no redirect, 2026-07-27)

> SurePath AI is now a part of F5

Links from the banner: the press release above, and https://www.f5.com/products/ai-security-platform.
The site is otherwise intact and still SurePath-branded (product/solution pages, blog, `/demo`,
`admin.surepath.ai` login). Contrast: `calypsoai.com` 301-redirects to F5's AI Guardrails page.

## 3. SEC: F5 Q3 FY2026 earnings release (Form 8-K Ex-99.1, filed 2026-07-27)

- **URL:** https://www.sec.gov/Archives/edgar/data/1048695/000104869526000063/ex991-q326earningsreleasef.htm
- Form 8-K, accession 0001048695-26-000063, filed 2026-07-27, for the quarter ended 2026-06-30.

Condensed consolidated statements of cash flows, **nine months ended June 30**:

> Acquisition of businesses, net of cash acquired **(47,619)** [FY2026] … (24,170) [FY2025]

Compare the same line in F5's Q2 FY2026 Form 10-Q (accession 0001048695-26-000051, filed 2026-05-05,
period 2026-03-31), **six months ended March 31**:

> Acquisition of businesses, net of cash acquired **—** [FY2026] … (10,100) [FY2025]

**Arithmetic:** nine-month FY2026 $47.619M − six-month FY2026 $0 = **$47.619M of acquisition cash paid
inside fiscal Q3 2026 (2026-04-01 → 2026-06-30)**. SurePath AI is the only acquisition F5 announced in
that window. Two conclusions:

1. The deal **closed on or before 2026-06-30** — cash actually changed hands in the quarter. Combined
   with the 2026-06-22 press release's completed-transaction language, announce and close are
   effectively simultaneous.
2. Cash consideration was **~$47.6M net of cash acquired** — *if* no other acquisition landed in the
   quarter. F5 does not name SurePath in the earnings release; this is an inference, flagged as such.

Also note: **CalypsoAI's $145.2M does not appear here.** It closed 2025-09-26, inside F5's fiscal 2025
(FY ends September 30), so it sits in FY2025 cash flows — the FY2026 line is uncontaminated by it.

## 4. What is *not* yet available

EDGAR full-text search for the phrase "SurePath AI" (2026-07-27) returns exactly **one** hit across all
filers: SurePath AI, Inc.'s own Form D (CIK 0002030853, filed 2024-08-27, the seed round). **No F5
10-Q, 10-K or 8-K mentions SurePath AI by name yet**, and F5 filed no 8-K for the transaction —
consistent with a tuck-in below the materiality threshold. F5's **Q3 FY2026 Form 10-Q** (period
2026-06-30) had not been filed as of 2026-07-27; on F5's normal cadence it lands in early August 2026
and, if the deal is material enough for a Note 4 business-combination disclosure, that filing is where
the exact close date and purchase-price allocation will appear. **Re-check EDGAR after 2026-08-10.**

## 5. Corroboration on brand survival

Security Boulevard, "F5 Acquires SurePath AI to Extend Reach of Cybersecurity Portfolio"
(https://securityboulevard.com/2026/06/f5-acquires-surepath-ai-to-extend-reach-of-cybersecurity-portfolio/),
published 2026-06-22, fetched 2026-07-27 — quotes F5 CTO Jimmy White that "in addition to continuing to
offer SurePath AI as an independent platform, the capabilities enabled by the company will also be
integrated into the F5 Application Delivery and Security Platform (ADSP)." Confidence: medium (trade
press paraphrase of a vendor executive), but it matches the observable evidence that surepath.ai is
still live and still selling.

## 6. F5 AI Security Platform product page (fetched 2026-07-27)

- **URL:** https://www.f5.com/products/ai-security-platform

Four pillars — AI governance, **AI discovery**, AI security testing, AI runtime protection — plus an AI
observability layer. The **AI discovery** pillar is the SurePath capability set (shadow-AI detection,
"Agent & MCP visibility", intent classification), but F5's product navigation lists only two named
products under the platform: **Guardrails** and **Red teaming** (both ex-CalypsoAI). **There is no F5-
branded "AI Discovery" SKU as of 2026-07-27** — SurePath's technology is described as a platform
capability while the product itself is still sold under the SurePath AI name.
