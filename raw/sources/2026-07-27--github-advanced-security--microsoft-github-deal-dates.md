# Microsoft / GitHub acquisition — announced, closed, and price (primary sources)

- **URL (primary, close date + price):** https://www.sec.gov/Archives/edgar/data/789019/000156459019027952/msft-10k_20190630.htm
  (Microsoft Corp Form 10-K, FY ended 2019-06-30, Note 8 — Business Combinations)
- **URL (primary, close date + price, earlier):** https://www.sec.gov/Archives/edgar/data/789019/000156459019001392/msft-10q_20181231.htm
  (Microsoft Corp Form 10-Q, quarter ended 2018-12-31, Note 7 — Business Combinations)
- **URL (primary, announce date):** https://www.sec.gov/Archives/edgar/data/789019/000119312518182975/d600091d8k.htm
  (Form 8-K, date of earliest event 2018-06-04, filed 2018-06-04) and its press-release exhibit
  https://www.sec.gov/Archives/edgar/data/789019/000119312518182975/d600091dex991.htm
- **URL (Microsoft newsroom, announcement):** https://news.microsoft.com/source/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/
- **URL (Microsoft official blog, completion):** https://blogs.microsoft.com/blog/2018/10/26/microsoft-completes-github-acquisition/
- **URL (GitHub blog, completion):** https://github.blog/news-insights/company-news/github-and-microsoft/
- **Filer:** Microsoft Corporation (NASDAQ: MSFT), CIK 0000789019
- **Fetched:** 2026-07-27
- **Good for:** settling the exact **announced (2018-06-04)** and **closed (2018-10-25)** dates and the
  **$7.5B all-stock** price for Microsoft's acquisition of GitHub — the deal that puts GitHub Advanced
  Security under Microsoft ownership. Fixes a transposed/imprecise date pair on the wiki page.
  Confidence: **high** (SEC-filed 8-K for the announcement; audited 10-K business-combinations note
  for the close date and consideration).

## (a) ANNOUNCED — 2018-06-04

Form 8-K, Item 8.01, date of earliest event reported **June 4, 2018**, filed **2018-06-04**:

> On June 4, 2018, Microsoft Corporation ("Microsoft") issued a press release announcing that it had
> entered into a definitive agreement pursuant to which Microsoft will acquire GitHub for $7.5 billion.
> The full text of the press release is attached as Exhibit 99.1 and is incorporated by reference herein.

Exhibit 99.1 (the press release itself), headed **"For Release 6 a.m. PDT June 4, 2018"**:

> REDMOND, Wash. — June 4, 2018 — Microsoft Corp. on Monday announced it has reached an agreement to
> acquire GitHub, the world's leading software development platform where more than 28 million
> developers learn, share and collaborate to create the future.
>
> […]
>
> Under the terms of the agreement, Microsoft will acquire GitHub for $7.5 billion in Microsoft stock.
> Subject to customary closing conditions and completion of regulatory review, the acquisition is
> expected to close by the end of the calendar year.

The Microsoft newsroom post at news.microsoft.com carries the same text and the same 2018-06-04 date.

## (b) CLOSED — 2018-10-25

Form 10-K FY2019, **Note 8 — Business Combinations** (verbatim):

> **GitHub, Inc.**
>
> On October 25, 2018, we acquired GitHub, Inc. ("GitHub"), a software development platform, in a
> $7.5 billion stock transaction (inclusive of total cash payments of $1.3 billion in respect of
> vested GitHub equity awards and an indemnity escrow). The acquisition is expected to empower
> developers to achieve more at every stage of the development lifecycle, accelerate enterprise use
> of GitHub, and bring Microsoft's developer tools and services to new audiences. The financial
> results of GitHub have been included in our consolidated financial statements since the date of the
> acquisition. GitHub is reported as part of our Intelligent Cloud segment.

Same 10-K, MD&A/business section:

> On October 25, 2018, we completed our acquisition of GitHub, Inc. ("GitHub"), a service that
> millions of developers around the world rely on to write code together.

Form 10-Q for the quarter ended 2018-12-31 (Microsoft FY2019 Q2), **Note 7 — Business Combinations**,
says the same thing contemporaneously:

> **GitHub Inc.**
>
> On October 25, 2018, we acquired GitHub, Inc. in a $7.5 billion stock transaction (inclusive of
> total cash payments of $1.3 billion in respect of vested GitHub equity awards and an indemnity
> escrow). […]

## (c) PRICE — $7.5 billion, all-stock

- **As announced and as filed: $7.5 billion in Microsoft stock.** The commonly cited $7.5B figure is
  exactly what Microsoft said in the 2018-06-04 press release and what it repeated in the 10-Q and 10-K.
- Microsoft qualifies it in the filings: the $7.5B stock transaction is *"inclusive of total cash
  payments of $1.3 billion in respect of vested GitHub equity awards and an indemnity escrow."* So it
  is not literally 100% stock at the transaction level — there was a $1.3B cash component inside the
  headline number.
- **Purchase price actually allocated in purchase accounting: $6,924 million.** Approximately
  $600 million of the total was *"recognized separately from the purchase price allocation […]
  primarily related to equity awards recognized as expense over the related service period"* — i.e.
  post-combination compensation, not consideration. $6.924B + ~$0.6B ≈ $7.5B.

Final (FY2019 10-K) purchase price allocation, in millions:

```
Cash, cash equivalents, and short-term investments     234
Goodwill                                             5,497
Intangible assets                                    1,267
Other assets                                           143
Other liabilities                                     (217)
Total                                                6,924
```

Intangibles detail (FY2019 10-K): customer-related $648M (8 yr), technology-based $447M (5 yr),
marketing-related $170M (10 yr), contract-based $2M (2 yr); total $1,267M, 7-yr weighted average life.
Goodwill assigned to the Intelligent Cloud segment. (The 10-Q's preliminary allocation was goodwill
$5,441M / intangibles $1,298M against the same $6,924M total; the FY2019 10-K figures are final.)

## Notes / reconciliation — the 2018-10-25 vs 2018-10-26 discrepancy

Secondary coverage (TechCrunch, SiliconANGLE, Wikinews, etc.) routinely dates the close to
**2018-10-26**, because that is the day both companies *announced* completion:

- The Official Microsoft Blog, "Microsoft completes GitHub acquisition," dated **2018-10-26**:
  "Microsoft has completed its acquisition of GitHub. Nat Friedman […] is taking over as GitHub's
  CEO […]." The post states completion but gives no closing date.
- The GitHub Blog post by Nat Friedman, also **2018-10-26**: "I'm thrilled to share that the Microsoft
  acquisition of GitHub is complete. Monday is my first day as CEO."

Neither blog post asserts a close date. The SEC filings do, twice and consistently: **October 25, 2018**.
Use **2018-10-25** as the close date and treat 2018-10-26 as the completion-announcement date.

The prior wiki value (`announced: 2018-10-01, closed: 2018-06-01`) was a transposition: the correct
direction is announced 2018-06-04 → closed 2018-10-25, a roughly 4.7-month gap spent in regulatory
review, consistent with the press release's "expected to close by the end of the calendar year."
