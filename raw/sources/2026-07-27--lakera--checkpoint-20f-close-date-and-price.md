# Check Point / Lakera — closed 2025-10-22, total consideration ~$201.8M (per 20-F)

- URLs:
  - https://www.sec.gov/Archives/edgar/data/1015922/000117891326001932/zk2634942.htm
    (Check Point Software Technologies Ltd., Form **20-F** for FY2025, filed 2026-03-31 —
    Note 3: Acquisitions, item (f))
  - https://www.sec.gov/Archives/edgar/data/1015922/000117891325003335/exhibit_99-1.htm
    (Form **6-K**, filed 2025-09-16 — the acquisition announcement furnished to the SEC)
  - https://www.sec.gov/Archives/edgar/data/1015922/000117891325003565/2533887.htm
    (Form **6-K**, filed 2025-10-28 — Q3 2025 results, CEO commentary on the Lakera deal)
  - https://www.checkpoint.com/press-releases/check-point-acquires-lakera-to-deliver-end-to-end-ai-security-for-enterprises/
    (Check Point press release, 2025-09-16)
  - https://www.lakera.ai/ (live-site brand check)
- Fetched: 2026-07-27
- Good for: the **audited** closing date and purchase price of Check Point's Lakera
  acquisition, which correct the "expected Q4 2025 close / ~$300M reported" placeholders;
  purchase-price allocation (including the intangible useful lives, which signal brand
  intent); and the current status of the Lakera brand.

## The load-bearing passage (20-F FY2025, Note 3: Acquisitions, item (f))

> "f. On **October 22, 2025**, the Company **completed the acquisition** of all outstanding
> shares of **Lakera AI AG** ("Lakera"), a privately-held Swiss company. Lakera is a
> specialized AI-security company focused on protecting generative AI applications - like
> large language models, chatbots, autonomous AI agents, and multimodal systems - from
> advanced cyber threats unique to AI environments. […] Rather than bolting AI onto
> traditional cybersecurity tools, Lakera builds its technology from the ground up
> specifically for AI threats, such as prompt injections, data leakage, model manipulation,
> and autonomous agent risks. This would enable the Company to expand its product portfolio.
> The Company acquired Lakera for **total consideration of approximately $201.8** [million]."

The XBRL contexts in the same filing corroborate the date: the `chkp:LakeraAiAgMember`
acquisition-date context is tagged `2025-10-01 – 2025-10-22`.

## Dates

- **Announced: 2025-09-16** — Check Point press release, furnished the same day as
  Exhibit 99.1 to a Form 6-K. Framed as an agreement to acquire, "expected to close in
  Q4 2025, subject to customary closing conditions."
- **Closed: 2025-10-22** — stated in the audited FY2025 financial statements (20-F Note 3(f))
  as the date Check Point "completed the acquisition of all outstanding shares." **High
  confidence**; this is the issuer's own audited filing, not press.
- Elapsed sign-to-close: 36 days. All-cash purchase of 100% of shares of a Swiss AG.

## Price — the audited number is ~$201.8M, not the widely reported ~$300M

- **20-F (audited): total consideration ≈ $201.8 million.**
- Press at announcement (Calcalist and others, since repeated widely) reported **~$300M**.
- These are reconcilable rather than contradictory, and the difference is the usual one:
  the accounting "total consideration" figure is the amount allocated to the business
  combination, and it **excludes** amounts that must be expensed as post-close compensation —
  employee retention/earn-out packages tied to continued service, which are routinely folded
  into the headline number journalists are briefed on. Check Point does not break out any
  retention pool for Lakera in the filing, so the ~$100M gap is **not itemized in a primary
  source** and should not be asserted as retention with confidence. Treat **$201.8M as the
  authoritative purchase price** and ~$300M as an unofficial, larger press figure of
  uncertain composition. Classified as a **soft / scope-mismatch** contradiction (different
  measures), not a hard one.

## Purchase price allocation (in $ millions)

| Component | Weighted avg. useful life | Amount |
|---|---|---|
| Goodwill | — | 150.1 |
| Core technology | 7 years | 44.0 |
| Customer relationship | **1 year** | 4.4 |
| Trademark | **1 year** | 0.3 |
| Net assumed assets | — | 3.0 |
| **Total** | | **201.8** |

Two things a buyer should read off this table:

1. **Goodwill is 74% of the price** and is "primarily attributed to synergies" — this was
   bought for the technology and the team's fit with Check Point's platform, not for a
   revenue stream.
2. **The Lakera trademark and customer relationships were each assigned a one-year useful
   life, versus seven years for the core technology.** Check Point's own accounting
   assumption is that the *brand* and the *standalone customer base* have roughly a year of
   remaining economic value from October 2025, while the *technology* has seven. That is the
   fingerprint of a plan to absorb the product into Check Point's platform and retire the
   standalone identity, keeping the engine. (The useful lives are filing facts; the
   inference about intent is this wiki's reading, though it is a conventional one.)

## Q3 2025 6-K (2025-10-28) — CEO framing

Nadav Zafrir, CEO: "We also advanced our AI First strategy through the strategic acquisition
of Lakera, strengthening our position to deliver a comprehensive, full-stack AI-powered
security platform and expand our leadership in next-generation cyber defense."

## Brand status as of 2026-07-27

- `https://www.lakera.ai/` returns **HTTP 200 with no redirect** to checkpoint.com.
- Page title is still **"Lakera: The AI-Native Security Platform to Accelerate GenAI"** —
  independent-vendor marketing, no Check Point co-branding above the fold.
- The footer, however, reads **"©1994-2026 Check Point Software Technologies Ltd. All rights
  reserved."** — 1994 is Check Point's founding year, three decades before Lakera existed, so
  the copyright line is Check Point's corporate boilerplate applied to a property it owns.
  This is the tell that ownership has changed even though the marketing site has not.
- Conclusion: **Lakera is a live operating brand under Check Point ownership.** Per this
  sweep's rule (rename only when the old brand is retiring *and* the new brand is
  distinctive), **no rename** — `website` stays `https://www.lakera.ai`, the wiki slug stays
  `lakera`, and the survey option stays "Lakera (Check Point)". Given the one-year trademark
  life, expect this to be worth re-checking within the year.

## Confidence

**High** on: closed date 2025-10-22, purchase price $201.8M, announced date 2025-09-16,
100%-of-shares all-cash structure, purchase price allocation, brand still live — all from
Check Point's own SEC filings plus a direct site check.
**Medium** on: the reconciliation of $201.8M vs. the ~$300M press figure (the gap is
unexplained in any primary source).
**Inference, not fact:** that the 1-year trademark/customer-relationship lives imply a
planned brand retirement.
