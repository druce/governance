# Zscaler, Inc. Form 10-Q (quarter ended 2025-10-31) — Note 6, Business Combinations: SPLXAI Inc.

- **URL:** https://www.sec.gov/Archives/edgar/data/1713683/000171368325000205/zs-20251031.htm
- **Filing index:** https://www.sec.gov/Archives/edgar/data/1713683/000171368325000205/0001713683-25-000205-index.htm
- **Filer:** Zscaler, Inc. (NASDAQ: ZS), CIK 0001713683
- **Form:** 10-Q, Q1 fiscal 2026, period of report 2025-10-31, filed 2025-11-25
- **Fetched:** 2026-07-27
- **Good for:** the *authoritative* close date and the *SPLX-specific* purchase price. This is the
  filing that settles two things the wiki page previously got wrong: (a) the close date is
  **2025-10-31**, not the 2025-11-03 press-release date, and (b) the SPLX price **is** separately
  disclosed at **$40.6M cash** — it is not merely buried inside the $692.0M Red Canary + SPLX
  aggregate. Confidence: high (audited-basis primary filing, SEC EDGAR).

## Verbatim extract — Note 6. Business Combinations

> **SPLXAI Inc.**
>
> On October 31, 2025, we acquired all the equity of SPLXAI Inc. ("SPLX"), an early-stage
> technology company incorporated in the United States. We plan to integrate SPLX's technology
> with our AI Security offerings. We acquired SPLX for a total cash purchase price consideration
> of $40.6 million. In accordance with the purchase agreement, certain SPLX employees who became
> our employees are entitled to receive restricted shares of our common stock contingent upon
> their continued employment. The total grant-date fair value of these awards was $16.6 million.
> Since these awards are conditioned on future service, they are recognized as stock-based
> compensation expense over the post-combination requisite service period.
>
> As of October 31, 2025, we estimated the fair value of the acquired intangible assets using a
> benchmarking valuation approach, which relies on market data from comparable companies. Based on
> this valuation approach, we determined the fair value of the acquired developed technology and
> customer relationships to be $13.0 million and $1.1 million, respectively. These valuations may
> be subject to adjustment if we determine that using an alternate valuation methodology is more
> appropriate.

## Verbatim extract — Item 2, Unregistered Sales of Equity Securities

> On October 31, 2025, in connection with our acquisition of SPLX, we agreed to issue a total of
> 50,180 shares of our common stock as deferred consideration related to re-vesting of equity for
> certain key employees.

## Corroborating XBRL contexts (machine-tagged acquisition dates)

From the filing's XBRL context definitions — these are the dates Zscaler itself tagged as the
business-combination acquisition dates, and they distinguish the two Q1 FY2026 deals:

```
0001713683 zs:SPLXAIIncMember      2025-10-31 2025-10-31
0001713683 zs:SPLXAIIncMember      2025-10-31
0001713683 zs:RedCanaryIncMember   2025-08-01 2025-08-01
0001713683 zs:RedCanaryIncMember   2025-08-01
```

So Red Canary closed **2025-08-01** and SPLX closed **2025-10-31** — two separate closings inside
Zscaler's Q1 FY2026 (1 Aug – 31 Oct 2025). The widely-quoted **$692.0M aggregate** figure covers
**both** deals; Red Canary is the large component and SPLX is $40.6M of it.

## Notes / reconciliation

- **Closed before it was announced.** Zscaler's public press release is dated **2025-11-03** and
  reads "today announced it *has acquired*" — i.e. it announced an already-completed transaction
  three days after the fact. There is no separate publicly-announced *signing* date and no
  "subject to customary closing conditions" language, because there was nothing pending by the
  time the deal became public. This is why `announced` (2025-11-03) post-dates `closed`
  (2025-10-31) on the wiki page; that ordering is correct, not a typo.
- Closing on the last day of the fiscal quarter is consistent with the 10-Q's statement that
  SPLX's post-acquisition revenue and earnings "were not material for disclosure purposes."
- Goodwill acquired across both Q1 FY2026 deals: $576.7M (balance $417.7M → $994.5M).
