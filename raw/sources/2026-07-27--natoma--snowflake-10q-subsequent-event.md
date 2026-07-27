# Snowflake 10-Q (Q1 FY2027) — Subsequent Events note on Natoma Labs, Inc.

- **URL:** https://www.sec.gov/Archives/edgar/data/1640147/000164014726000030/snow-20260430.htm
- **Filing:** Snowflake Inc. (NYSE: SNOW), CIK 0001640147, Form 10-Q for quarterly period ended 2026-04-30, filed **2026-05-29**, accession 0001640147-26-000030
- **Fetched:** 2026-07-27
- **Good for:** the authoritative, primary-source status of the Snowflake–Natoma deal — signing date, price, and the fact that it was **NOT closed** as of the filing date. Supersedes press-release and blog wording.

## Verbatim quote (Note: Subsequent Events → Business Combinations)

> On May 24, 2026, the Company entered into a definitive agreement to acquire all
> outstanding capital stock of Natoma Labs, Inc., an enterprise Model Context Protocol
> platform for AI agents, for total stated consideration of approximately $110.0 million,
> consisting primarily of the Company's common stock (Equity Consideration) with the
> remainder in cash. Based on the Company's preliminary estimates, approximately 30% of
> the Equity Consideration will be subject to certain vesting conditions, the
> acquisition-date fair value of which will be accounted for as post-combination
> stock-based compensation over a requisite service period. **The transaction is expected
> to close in June 2026, subject to satisfaction of certain closing conditions.**

## Corroborating XBRL context

The filing tags the Natoma disclosure as:

```
us-gaap:SubsequentEventMember srt:ScenarioForecastMember snow:NatomaLabsInc.Member 2026-06-01 2026-06-30
```

`srt:ScenarioForecastMember` is the XBRL member for a **forecast**, not an actual —
independent machine-readable confirmation that as of the 2026-05-29 filing the close
was projected (June 2026), not consummated.

## Key facts established

| Fact | Value |
|---|---|
| Legal target entity | Natoma Labs, Inc. |
| Definitive agreement signed | 2026-05-24 |
| Publicly announced | 2026-05-27 (Snowflake press release / BusinessWire) |
| Consideration | ~$110.0M, primarily SNOW common stock + remainder cash |
| Earn-out / retention | ~30% of equity consideration subject to vesting → post-combination SBC |
| Expected close | June 2026, subject to closing conditions |
| Actually closed? | **Not confirmed as of 2026-07-27** — see below |

## Close-status search (negative results, 2026-07-27)

Deliberate checks for a *completion* announcement distinct from the intent announcement:

1. **EDGAR full-text search** (`efts.sec.gov`, query `"Natoma"`, all forms) — only 5 hits
   corpus-wide. The Snowflake ones are the 2026-05-27 8-K (Item 2.02 earnings release)
   and this 2026-05-29 10-Q. **No 8-K Item 2.01 (completion of acquisition) exists.**
   Caveat: at ~$110M this deal is almost certainly below Snowflake's Reg S-X significance
   threshold, so no completion 8-K would be *required*. Absence is therefore weak evidence,
   not proof of non-close.
2. **Snowflake newsroom** — only "Snowflake Announces **Intent** to Acquire Natoma"
   (2026-05-27). No completion press release.
3. **natoma.ai** — live, HTTP 200, no redirect. Site banner reads "Natoma is joining
   forces with Snowflake"; blog post `/blog/natoma-snowflake` (dated 2026-05-27) still
   reads "Snowflake **has signed a definitive agreement to acquire** Natoma." Announcement
   language, unchanged, two months after signing. Natoma still operates its own domain and
   product site.
4. **Trade press** (Reuters/TradingView, The Register 2026-05-28, Forbes 2026-05-31,
   CIO, BigDATAwire, StorageNewsletter) — all report the *intent/definitive agreement*.
   None report consummation.

**Conclusion:** the deal is **signed but not verifiably closed**. The expected-close window
(June 2026) has elapsed without public confirmation either way. Per CLAUDE.md §7
("Announced ≠ closed") and the never-invent rule, the wiki records `acquired-pending`.

## Next authoritative checkpoint

Snowflake's **Q2 FY2027 Form 10-Q** (quarter ended 2026-07-31), normally filed late
August / early September. If the deal closed, Natoma will appear there in purchase-price
accounting / goodwill rather than as a forecast subsequent event. That filing is the
cheapest definitive resolution → drives `verify_after: 2026-09-15`.

## Other sources consulted

- Snowflake press release, "Snowflake Announces Intent to Acquire Natoma, Providing Secure
  Connectivity For The Agentic Enterprise" — https://www.snowflake.com/en/news/press-releases/snowflake-announces-intent-to-acquire-natoma-providing-secure-connectivity-for-the-agentic-enterprise/ (2026-05-27)
- Snowflake blog, "Snowflake to Acquire Natoma to Bring Governed Agentic Access to the
  Enterprise" — https://www.snowflake.com/en/blog/snowflake-acquire-natoma-governed-agentic-access/
- Natoma blog, "Natoma is Joining Snowflake" — https://natoma.ai/blog/natoma-snowflake (2026-05-27)
