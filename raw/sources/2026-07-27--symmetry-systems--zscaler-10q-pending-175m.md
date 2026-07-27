# Zscaler Form 10-Q (quarter ended 2026-04-30) — Note 17 Subsequent Event: Symmetry Systems

- URL: https://www.sec.gov/Archives/edgar/data/1713683/000171368326000096/zs-20260430.htm
- Filed: 2026-05-26 (accession 0001713683-26-000096), Zscaler, Inc. CIK 0001713683
- Fetched: 2026-07-27
- Good for: PRIMARY, authoritative proof that the Zscaler/Symmetry Systems deal was **signed but NOT closed** as of
  the filing date, plus the previously-undisclosed price. Corrects an `acquired-closed` error on the wiki page.

## Verbatim quote — Note 17. Subsequent Event

> On May 19, 2026, we entered into a definitive agreement to acquire Symmetry Systems, Inc. ("Symmetry"), a
> cybersecurity company specializing in data and identity mapping for AI security. Under the terms of the purchase
> agreement, we will acquire Symmetry for total consideration of $175.0 million, consisting of cash and restricted
> shares subject to future employment services. We expect this acquisition to enhance our AI security offerings and
> our Zero Trust Exchange™ platform. The transaction is expected to close in the fourth quarter of fiscal 2026,
> subject to the satisfaction of closing conditions.

XBRL tagging corroborates: `zs:SymmetrySystemsIncMember us-gaap:SubsequentEventMember 2026-05-19 2026-05-19`.

## What this establishes

| Fact | Value | Note |
|---|---|---|
| Definitive agreement signed | **2026-05-19** | per 10-Q Note 17 |
| Public announcement | **2026-05-21** | Zscaler IR press release, "Zscaler **to Acquire** Symmetry Systems" |
| Total consideration | **$175.0M** | cash + restricted shares subject to future employment services |
| Close status | **NOT CLOSED** as of filing | "expected to close in the fourth quarter of fiscal 2026, subject to the satisfaction of closing conditions" |

Zscaler's fiscal year ends **July 31**, so fiscal Q4 2026 = 2026-05-01 → 2026-07-31. Expected close is therefore on
or before 2026-07-31 — four days after this verification date.

## Negative evidence — no close confirmed as of 2026-07-27

- EDGAR full-text search for "Symmetry" restricted to CIK 0001713683 returns exactly **2 hits**, both dated
  2026-05-26: this 10-Q and the Q3 FY2026 earnings 8-K (items 2.02/9.01). **No completion 8-K.**
- Zscaler's EDGAR submissions feed shows nothing but Forms 4 and 144 between 2026-05-26 and 2026-07-27 — no 8-K of
  any kind, so no Item 2.01 completion-of-acquisition report has been filed.
- Web search finds no "Zscaler completes acquisition of Symmetry Systems" press release; every headline still reads
  "to acquire" / "announces intent to acquire".
- symmetry-systems.com remains live on its own domain (no redirect to zscaler.com) and, per the 2026-07-27 URL
  audit, still displays a "Zscaler to acquire Symmetry Systems" banner plus a 2026-05-21 post titled "A New Chapter
  for Symmetry Systems: Joining Forces with Zscaler". The Symmetry post's forward-looking-statements section refers
  to "the proposed acquisition" — pending language. (Direct curl fetch on 2026-07-27 returns Cloudflare 403 to
  non-browser agents; status per the audit's browser fetch.)

**Conclusion: `acquired-pending`, not `acquired-closed`.** Announced 2026-05-21 (signed 2026-05-19), closed = null,
price $175.0M. Re-verify after Zscaler's FY2026 Form 10-K (FY ends 2026-07-31; the FY2025 10-K was filed
2025-09-11), which will state whether the deal closed inside fiscal Q4 2026.

## Contrast with the sibling Zscaler deal (SPLX)

SplxAI is genuinely `acquired-closed` — Zscaler's 10-Q for the quarter ended 2025-10-31 (Note 6, Business
Combinations) says "On October 31, 2025, we acquired all the equity of SPLXAI Inc." for $40.6M cash, and that deal
was announced 2025-11-03 *after* it closed. Symmetry is the opposite shape: signed and announced first, close still
pending. Both land at Zscaler, but only one is done.
