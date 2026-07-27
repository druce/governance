# SailPoint / Entro Security — announce-date correction + brand-persistence check (2026-07-27)

- URLs:
  - Intent-to-acquire PR (primary, acquirer): https://www.globenewswire.com/news-release/2026/06/15/3311837/0/en/sailpoint-announces-intent-to-acquire-entro-to-accelerate-and-enhance-agentic-fabric-and-secure-the-future-of-ai-driven-enterprises.html
  - Same PR on SailPoint IR: https://investor.sailpoint.com/news-releases/news-release-details/sailpoint-announces-intent-acquire-entro-accelerate-and-enhance
  - Close PR (primary, acquirer): https://www.globenewswire.com/news-release/2026/06/29/3318987/0/en/sailpoint-completes-acquisition-of-entro-security-to-secure-agentic-identities.html
  - Live site checked: https://entro.security/
- Fetched: 2026-07-27
- Good for: **correcting the announced date from 2026-06-18 to 2026-06-15**, confirming the 2026-06-29 close, confirming price was never officially disclosed, and confirming the **Entro brand and domain persist** post-acquisition.

## Announce date — correction (the load-bearing finding)

The wiki previously recorded `announced: 2026-06-18`. That is the **publication date of the
SecurityWeek article**, not the announcement date.

- SailPoint's own intent-to-acquire press release carries the dateline
  **"AUSTIN, Texas, June 15, 2026 (GLOBE NEWSWIRE)"**; GlobeNewswire's own URL path is
  `/news-release/2026/06/15/3311837/...`. SailPoint's IR listing also dates it **June 15, 2026**.
- SecurityWeek's "SailPoint to Acquire Entro in Reported $200 Million Deal" is dated
  **2026-06-18** and never states the announcement date itself — it only says "SailPoint has
  announced an agreement to acquire Entro." The 06-18 in the wiki was the trade-press
  publication date misread as the announce date.
- **Corrected: announced 2026-06-15.** Confidence: high (acquirer PR dateline + newswire URL date
  + IR listing date, three-way consistent).

## Close date

- **Closed 2026-06-29**, per SailPoint's own release: "SailPoint, Inc. (Nasdaq: SAIL) ... today
  announced it has completed its acquisition of Tel Aviv-based Entro Security." Dateline
  **June 29, 2026, 09:00 ET**. Confidence: high.
- The intent PR had guided to a close in **Q3 of SailPoint's fiscal 2027**; the deal actually closed
  2026-06-29, which falls in **Q2 FY2027** (SailPoint's FY ends Jan 31, so Q2 FY27 = May 1 – Jul 31
  2026). i.e. it closed **ahead of the guided timeframe**, not late.

## Price

- **Not officially disclosed.** Close PR: "Financial terms of this transaction were not disclosed."
- **~$200M reported by Calcalist** and relayed by SecurityWeek; explicitly not company-confirmed.
  Confidence: medium, single press source.

## SEC filings — checked, nothing yet (per the "prefer filings over blogs" rule)

SailPoint, Inc. CIK **0002030781** (note: the pre-2025 entity "Sailpoint Technologies Holdings, Inc."
is CIK 0001627857 — do not use).

- EDGAR full-text search for `"Entro"` restricted to CIK 0002030781 returns **0 hits** as of
  2026-07-27. Control query `"Agentic Fabric"` returns 1 hit, so FTS is working — the zero is real,
  not a broken query.
- Filing history: the most recent 10-Q was **filed 2026-06-10 for the period ended 2026-04-30**
  (Q1 FY2027) — i.e. filed *before* the 06-15 announcement, so it cannot mention Entro. No 8-K was
  filed for the deal (consistent with terms being undisclosed / the acquisition being immaterial for
  Item 2.01 purposes).
- **Therefore no SEC filing corroborates the dates yet.** The first filing expected to carry the
  business-combination footnote is the **Q2 FY2027 10-Q (period ending 2026-07-31), due ~Sept 2026**.
  Until then the acquirer press releases are the best available primary source. Worth re-checking
  after that 10-Q lands for an official purchase price.

## Brand persistence — Entro brand is NOT retired

Checked https://entro.security/ on 2026-07-27:

- HTTP **200, no redirect** (final URL `https://entro.security/`).
- `<title>` = **"Agentic AI & Non-Human Identity Security Platform | Entro Security"** — still the
  Entro brand, not a SailPoint product name.
- Footer: **"© 2026 SailPoint Technologies, Inc. All Rights Reserved."**
- Site assets include a co-branded lockup image `SailPoint-Entro.png` (and `SailPoint.png`),
  i.e. the site presents as **SailPoint | Entro**, not as a generic SailPoint page.
- Privacy policy link now points to `sailpoint.com/legal/privacy` — corporate plumbing has moved to
  SailPoint while the product-facing brand stayed.

This contrasts with other deals in this sweep where the acquired brand was fully retired and the
domain 301'd to the acquirer's product page. Entro is a **surviving sub-brand** — keep
`website: https://entro.security` and keep "Entro Security" as the shoppable name.

Consistent with the close PR: "Entro's NHI and credentials security solutions are available now to
SailPoint customers as **standalone offerings** ... as native platform integration continues."
