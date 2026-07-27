# HashiCorp / IBM — announced vs. closed dates and price (IBM 10-Q Note 5 + SEC 8-Ks + IBM newsroom)

- **URL (primary, close + consideration):** https://www.sec.gov/Archives/edgar/data/51143/000005114325000032/ibm-20250331.htm
- **URL (primary, close mechanics):** https://www.sec.gov/Archives/edgar/data/1720671/000119312525037910/d898526d8k.htm
- **URL (primary, signing):** https://www.sec.gov/Archives/edgar/data/1720671/000119312524114310/d804229d8k.htm
- **URL (IBM newsroom, announcement):** https://newsroom.ibm.com/2024-04-24-IBM-to-Acquire-HashiCorp-Inc-Creating-a-Comprehensive-End-to-End-Hybrid-Cloud-Platform
- **URL (IBM newsroom, completion):** https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform
- **URL (UK CMA case page):** https://www.gov.uk/cma-cases/ibm-slash-hashicorp-merger-inquiry
- **Filers:** International Business Machines Corp. (NYSE: IBM), CIK 0000051143; HashiCorp, Inc. (ex-NASDAQ: HCP), CIK 0001720671
- **Fetched:** 2026-07-27
- **Good for:** settling that **2025-02-27 is the CLOSE date, not the announcement date**. The deal was
  announced **2024-04-24** and closed **2025-02-27** — a ~10-month gap driven by a UK CMA merger
  inquiry. Also the authoritative consideration figures: **$35.00/share cash**, **$6.4B enterprise
  value** (the marketed headline, net of HashiCorp's cash), **~$7.2B equity value**, **$7,433M total
  consideration** as booked. Confidence: high (SEC EDGAR primary filings + both IBM press releases).

## The two dates, in one line

| Field | Value | Primary evidence |
|---|---|---|
| `announced` | **2024-04-24** | Merger Agreement dated April 24, 2024; HashiCorp 8-K (event date 2024-04-24); IBM press release ARMONK/SAN FRANCISCO, April 24, 2024 |
| `closed` | **2025-02-27** | HashiCorp 8-K Introductory Note ("Closing Date"); IBM 10-Q Note 5; IBM press release Feb. 27, 2025; XBRL `ibm:HashiCorpMember 2025-02-27` |

## Verbatim — IBM Form 10-Q (Q1 2025, period 2025-03-31, filed 2025-04-24), Note 5, Acquisitions

> **HashiCorp** — On February 27, 2025, the company completed the acquisition of all of the
> outstanding shares of HashiCorp. IBM's and HashiCorp's combined portfolios will help clients
> manage growing application and infrastructure complexity and create a comprehensive end-to-end
> hybrid cloud platform designed for the AI era. HashiCorp's shareholders on record immediately
> prior to the effective time on the closing date received $35 per share in cash, representing a
> total equity value of approximately $7.2 billion.

Consideration table (dollars in millions):

| Total Consideration | |
|---|---|
| Cash paid for outstanding HashiCorp common stock | $7,212 |
| Cash paid for HashiCorp equity awards | 178 |
| **Cash consideration** | **$7,390** |
| Fair value of stock-based compensation awards attributable to pre-acquisition services | 40 |
| Settlement of pre-existing relationships | 3 |
| **Total consideration** | **$7,433** |

> (1) As part of the assets acquired, the company received $929 million of cash and cash equivalents
> and $331 million of short-term marketable securities from HashiCorp.

> Goodwill of $4,531 million and $143 million was assigned to the Software and Consulting segments,
> respectively. … The overall weighted-average useful life of the identified amortizable intangible
> assets acquired was 9.8 years. In connection with the acquisition, the company issued and assumed
> 1.7 million stock awards with a fair value of $381 million. … The acquisition will be integrated
> into the Software segment.

XBRL contexts in the same filing tag the acquisition date explicitly:

```
0000051143 ibm:HashiCorpMember 2025-02-27
0000051143 ibm:HashiCorpMember us-gaap:CommonStockMember 2025-02-27 2025-02-27
0000051143 ibm:HashiCorpMember ibm:EquityAwardsMember 2025-02-27 2025-02-27
```

## Verbatim — HashiCorp Form 8-K filed 2025-02-27 (Introductory Note)

> This Current Report on Form 8-K is being filed in connection with the consummation on
> **February 27, 2025** (the "Closing Date") of the transaction contemplated by that certain
> Agreement and Plan of Merger, **dated April 24, 2024** (the "Merger Agreement"), by and among
> International Business Machines Corporation, a New York corporation ("IBM"), McCloud Merger Sub,
> Inc., a Delaware corporation and a wholly owned subsidiary of IBM ("Sub"), and HashiCorp, Inc., a
> Delaware corporation ("HashiCorp"). On the Closing Date, pursuant to the Merger Agreement, Sub
> merged with and into HashiCorp (the "Merger"), with HashiCorp surviving the Merger as a wholly
> owned subsidiary of IBM … each share … was automatically canceled and converted into the right to
> receive **$35.00 in cash**, without interest (the "Per Share Price") …

Item 3.01 of the same 8-K: Nasdaq trading in HCP was suspended before the open on the Closing Date;
Form 25-NSE was filed 2025-02-27 and Form 15-12G on 2025-03-10.

## Verbatim — HashiCorp Form 8-K filed 2024-04-25 (event date 2024-04-24), Item 1.01

> On **April 24, 2024**, HashiCorp, Inc. ("HashiCorp") entered into an Agreement and Plan of Merger
> (the "Merger Agreement") with International Business Machines Corporation ("IBM") and McCloud
> Merger Sub, Inc., a wholly owned subsidiary of IBM ("Merger Sub"). … **The Merger is expected to
> be completed by the end of 2024**, subject to the satisfaction or waiver of the closing conditions
> in the Merger Agreement.

## IBM press releases (both retrieved 2026-07-27)

- **Announcement**, dateline *ARMONK, N.Y. and SAN FRANCISCO, April 24, 2024* — "IBM to Acquire
  HashiCorp Inc, Creating a Comprehensive End-to-End Hybrid Cloud Platform." Terms: **$35 per share
  in cash, representing an enterprise value of $6.4 billion** (net of cash). "The transaction is
  expected to close by the end of 2024."
- **Completion**, dateline *ARMONK, N.Y., Feb. 27, 2025* — "IBM Completes Acquisition of HashiCorp,
  Creates Comprehensive, End-to-End Hybrid Cloud Platform." "IBM today announced it **has completed**
  its acquisition of HashiCorp." Restates $35/share and $6.4B enterprise value. (Also carried on
  PR Newswire: https://www.prnewswire.com/news-releases/ibm-completes-acquisition-of-hashicorp-creates-comprehensive-end-to-end-hybrid-cloud-platform-302387460.html)

## Why the 10-month gap — regulatory timeline

| Date | Event | Source |
|---|---|---|
| 2024-04-24 | Merger Agreement signed; announced by both parties | 8-Ks + IBM/HashiCorp press releases |
| 2024-07-15 | HashiCorp special meeting of stockholders adopts the Merger Agreement | HashiCorp 8-K, Item 5.07 (filed 2024-07-16) |
| 2024-08-01 | IBM and HashiCorp notified that the UK CMA **intends to begin a Phase 1 review** | HashiCorp 8-K, Item 8.01 (filed 2024-08-06) |
| 2024-12-30 | CMA formally launches the merger inquiry | gov.uk CMA case page |
| 2025-02-25 | CMA **clears** the deal at Phase 1 — no reference to Phase 2 | gov.uk CMA case page (full decision text published 2025-04-03) |
| 2025-02-27 | Deal closes; HCP delisted from Nasdaq | HashiCorp 8-K; IBM 10-Q; IBM press release |

## Notes / reconciliation for the wiki

- **The wiki frontmatter has the fields transposed.** `announced: 2025-02-27` is wrong — that is the
  close date. Correct values: `announced: 2024-04-24`, `closed: 2025-02-27`. With `closed` populated,
  `ownership_state: acquired-closed` is consistent (currently it is self-contradictory: state says
  closed but `closed: null`).
- **Which price to quote.** Three different-but-all-correct numbers circulate:
  - **$6.4B** — enterprise value net of HashiCorp's cash. This is the number IBM used in *both* press
    releases and the one nearly all press coverage repeats. Safe default for a one-line
    `ownership_note`.
  - **~$7.2B** — total *equity* value ($35 × shares), per IBM's own 10-Q language.
  - **$7,433M** — total consideration as actually booked under ASC 805.
  The gap between $6.4B and $7.2B is essentially the ~$929M of cash (plus $331M short-term
  securities) IBM picked up on HashiCorp's balance sheet. Not a contradiction — different measures.
- This is *not* a case like SPLX/Zscaler where the announcement post-dated the close. Here the normal
  ordering holds: signed and announced 2024-04-24, closed 2025-02-27, ten months apart.
- HashiCorp continues to operate as a wholly owned IBM subsidiary; the surviving corporation retained
  the HashiCorp name. Products (Terraform, Vault, Sentinel, Consul, Nomad, Boundary, Waypoint) were
  folded into IBM's Software segment.
