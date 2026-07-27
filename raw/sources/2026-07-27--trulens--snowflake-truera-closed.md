# TruEra → Snowflake: deal structure and close evidence (TruLens OSS stewardship)

- URLs (all fetched/checked 2026-07-27):
  - https://www.trulens.org (HTTP 200, no redirect) — OSS project site
  - https://www.sec.gov/Archives/edgar/data/1640147/000164014724000122/fy2025q1earnings.htm
    — Snowflake Q1 FY2025 earnings release, Form 8-K EX-99.1, filed 2024-05-22
  - https://www.sec.gov/Archives/edgar/data/1640147/000164014724000207/snow-20240731.htm
    — Snowflake Form 10-Q, quarter ended 2024-07-31 (Note 7, Business Combinations)
  - https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/
    — Snowflake blog, 2024-05-22
  - https://www.snowflake.com/en/blog/trulens-open-source-ai/ — Snowflake blog, 2024-06-24
  - https://truera.com/ (HTTP 200) — frozen 2024-era TruEra landing page
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability
  - https://docs.snowflake.com/en/release-notes/2025/other/2025-07-31-ai-observability-ga
  - https://api.github.com/repos/truera/trulens , https://pypi.org/pypi/trulens/json
- Good for: (a) correcting `ownership_state: acquired-pending` → `acquired-closed` on
  `wiki/vendors/trulens.md`; (b) establishing that this was an **asset + acqui-hire**
  deal, not a stock purchase of TruEra, Inc.; (c) the license correction (MIT, not
  Apache); (d) evidence TruLens is still independently released OSS in 2026.

## Facts

### Deal structure — assets + team, not the company

Snowflake's own Q1 FY2025 earnings press release (SEC EX-99.1, filed 2024-05-22) is
explicit about the structure:

> "Snowflake today also announced its **intent to acquire certain technology assets and
> hire key employees from TruEra**, an AI observability platform. TruEra provides
> capabilities to evaluate and monitor large language model (LLM) applications and
> machine learning models in production."

The same-day Snowflake blog frames it as a definitive agreement to "acquire the TruEra
AI observability platform" — i.e. the platform, not the corporate entity. Terms were not
disclosed in either. Press coverage (SiliconANGLE, VentureBeat, 2024-05-22/23) reports
~37 TruEra employees joining Snowflake, including co-founders Will Uppington (CEO),
Anupam Datta (Chief Scientist) and Shayak Sen (CTO).

### Close evidence

1. **Snowflake 10-Q, quarter ended 2024-07-31 (Note 7, Business Combinations, Fiscal
   2025)** — verbatim:

   > "During the three months ended July 31, 2024, the Company **acquired certain
   > technology assets and hired key employees from a privately-held company for
   > $10.8 million in cash**. The Company has accounted for this transaction as a
   > business combination. … $2.5 million as a developed technology intangible asset
   > (to be amortized over an estimated useful life of five years), and $8.3 million as
   > goodwill…"

   Snowflake does **not name** the counterparty. But the phrasing is a verbatim match
   for the TruEra press-release language ("acquire certain technology assets and hire
   key employees from TruEra"), it falls in the quarter immediately following the
   2024-05-22 announcement, and no other Snowflake deal of that description was
   announced in the window. **Inference, high confidence but not confirmed by name.**
   Neither the FY2025 10-K (period 2025-01-31) nor any Snowflake 8-K names TruEra —
   EDGAR full-text search for "TruEra" across 8-K/10-Q/10-K returns exactly one hit,
   the 2024-05-22 EX-99.1 above. The deal was immaterial, so no completion 8-K was
   required and none exists.

2. **Snowflake blog, 2024-06-24 ("TruLens ❤️ Snowflake OSS")** — past-tense throughout:
   "When Snowflake acquired the TruEra AI Observability platform…" and "**In the weeks
   since the acquisition**" Snowflake had already shipped groundedness-feedback
   parallelization, LangChain compatibility updates and dashboard query optimizations to
   TruLens. This bounds the close at **on or before 2024-06-24**; combined with the
   10-Q it lands in the 2024-05-22 → 2024-06-24 window. **Exact close date never
   disclosed.**

3. **trulens.org, checked 2026-07-27** — settled past tense, two years on:
   "Originally created by TruEra" … "**Since TruEra's acquisition by Snowflake,
   Snowflake now actively oversees and supports the development of TruLens in open
   source.**" Also: "TruLens is a community-driven open source project."

4. **truera.com is a frozen 2024 landing page**, not evidence of a live pending deal:
   it still reads "TruEra **has agreed to** join Snowflake!" with an auto-redirect to
   the Snowflake blog post. Unmaintained since 2024 — its stale forward-looking phrasing
   is what makes the deal *look* pending if you read only that page.

### TruEra (commercial) vs TruLens (OSS) — what happened to each

- **TruEra** was the commercial ML/LLM observability company (founded 2019 by Uppington,
  Datta, Sen; HQ Redwood City, CA). Its commercial platform was absorbed into Snowflake;
  there is no TruEra-branded product for sale today and truera.com is a parked
  transition page. The TruEra brand is retired.
- **TruLens** was TruEra's open-source Python evaluation/tracing library and survived as
  an independent OSS project under Snowflake's stewardship.
- The commercial successor is **AI Observability in Snowflake Cortex**, which reached
  **general availability on 2025-07-31** (Snowflake release notes). Snowflake's docs
  state plainly: "**TruLens is the platform that Snowflake uses to track your
  applications**," and require `trulens-core`, `trulens-connectors-snowflake` and
  `trulens-providers-cortex` ≥ 2.1.2. So Cortex AI Observability is a *managed
  deployment of* TruLens with Snowflake-table-backed storage, not a fork or replacement.

### TruLens OSS is alive and independently released (checked 2026-07-27)

- GitHub repo is still **`truera/trulens`** (org name unchanged; no `snowflakedb/trulens`
  — that path 404s). Not archived. Last push 2026-07-27. ~3,466 stars.
- **License is MIT**, copyright "Truera, Inc." — *not* Apache-2.0. (The wiki page
  previously said Apache; corrected 2026-07-27.)
- PyPI `trulens` latest **2.9.0, uploaded 2026-07-23**; steady cadence through 2026
  (2.7.0 2026-02-19, 2.8.0 2026-04-30, 2.8.1 2026-05-14, 2.9.0 2026-07-23). So Snowflake
  has **not** folded TruLens into Cortex-only distribution — it still ships standalone.

## Bottom line for the wiki

`ownership_state: acquired-pending` was wrong. Set `acquired-closed`, owner Snowflake,
announced 2024-05-22, closed 2024-06 (on/before 2024-06-24; exact date undisclosed),
price undisclosed (~$10.8M cash inferred from the unnamed 10-Q line). Slug stays
`trulens` — the OSS project is the live artifact; TruEra is the retired parent brand and
belongs in `aka`.
