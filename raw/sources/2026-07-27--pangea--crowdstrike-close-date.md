# CrowdStrike Holdings, Inc. SEC filings — Acquisitions note: Pangea Cyber Corporation

- **URL (10-K, primary):** https://www.sec.gov/Archives/edgar/data/1535527/000153552726000010/crwd-20260131.htm
- **URL (10-Q, first disclosure):** https://www.sec.gov/Archives/edgar/data/1535527/000153552725000033/crwd-20251031.htm
- **URL (announcement press release):** https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-pangea-to-secure-every-layer-of-enterprise-ai/
- **Filer:** CrowdStrike Holdings, Inc. (NASDAQ: CRWD), CIK 0001535527
- **Forms:** 10-K, FY2026, period of report 2026-01-31, filed 2026-03-05 (Note 12, Acquisitions);
  10-Q, Q3 FY2026, period of report 2025-10-31, filed 2025-12-03 (Note 11, Acquisitions)
- **Fetched:** 2026-07-27
- **Good for:** the *authoritative* close date and the *as-filed* purchase consideration. Settles two
  things the wiki page previously got wrong: (a) the close date is **2025-09-26**, ten days after the
  2025-09-16 Fal.Con announcement — it is **not** a same-day close, and (b) the widely-quoted
  "~$260M" is **press reporting, not a filed figure**; CrowdStrike discloses total consideration
  transferred of **$222.7M** ($212.1M cash net of cash acquired + $0.3M + $10.3M replacement awards).
  Confidence: high (audited 10-K, corroborated by the 10-Q and by CrowdStrike's own XBRL tagging).

## Verbatim extract — 10-K (FY2026), Note 12. Acquisitions

> **Pangea Cyber Corporation**
>
> On September 26, 2025, the Company acquired 100% of the equity interest of Pangea Cyber
> Corporation ("Pangea"), a company that offers AI detection and response solutions. The acquisition
> has been accounted for as a business combination. The total consideration transferred consisted of
> $212.1 million in cash, net of $9.4 million of cash and restricted cash acquired, and $0.3 million
> and $10.3 million representing the fair value of replacement equity and liability awards,
> respectively, attributable to pre-acquisition service. The remaining fair value of these
> replacement awards attributed to post-combination service was excluded from the purchase price.
> The cash consideration included (i) cash held back in an escrow fund for a partial security for
> post-closing true-up adjustments, which was released from escrow in January 2026, and (ii) cash
> held back in an escrow fund for a partial security for post-closing indemnification claims.
> Amounts reflected in restricted cash at January 31, 2026 are expected to be released in fiscal
> year 2028.
>
> The purchase price was allocated on a preliminary basis, subject to working capital adjustment and
> continuing management analysis, to developed technology of $13.2 million with a useful life of 72
> months, net tangible liabilities of $0.4 million, and goodwill of $209.9 million, which was
> allocated to the Company's one reporting unit and represents the excess of the purchase price over
> the fair value of net tangible and intangible assets acquired. The fair value of the developed
> technology was estimated using the relief-from-royalty method under the income approach. The
> goodwill was primarily attributable to the assembled workforce of Pangea, planned growth in new
> markets, and synergies expected to be achieved from the integration of Pangea. Goodwill is not
> deductible for income tax purposes.
>
> Per the terms of the merger agreement with Pangea, certain unvested stock options held by Pangea
> employees were canceled and exchanged for replacement stock options under the 2019 Plan.
> Additionally, certain shares of Pangea stock held by Pangea employees were exchanged for the right
> to receive shares of the Company's common stock, subject to service-based vesting conditions.
> Further, the Company granted RSUs and PSUs under the 2019 Plan to certain continuing employees. […]
>
> Acquisition costs incurred during the fiscal year ended January 31, 2026 were $3.1 million. The
> results of operations for the acquisition have been included in the Company's consolidated
> financial statements from the date of acquisition. The acquisition of Pangea did not have a
> material impact on the Company's consolidated financial statements, and therefore historical and
> pro forma disclosures have not been presented.

## Verbatim extract — 10-Q (Q3 FY2026, quarter ended 2025-10-31), Note 11. Acquisitions

Identical opening sentence and consideration figures. Only the *preliminary* allocation differs
slightly (later trued up in the 10-K):

> On September 26, 2025, the Company acquired 100% of the equity interest of Pangea Cyber
> Corporation ("Pangea") […] The total consideration transferred consisted of $212.1 million in
> cash, net of $9.4 million of cash and restricted cash acquired, and $0.3 million and $10.3 million
> representing the fair value of replacement equity and liability awards, respectively, attributable
> to pre-acquisition service. […] allocated on a preliminary basis […] to developed technology of
> $13.2 million with a useful life of 72 months, net tangible liabilities of $0.7 million, and
> goodwill of $210.2 million […] Acquisition costs incurred during the nine months ended October 31,
> 2025 were $2.8 million.

(10-Q → 10-K allocation drift: net tangible liabilities $0.7M → $0.4M; goodwill $210.2M → $209.9M.
Consideration and acquisition date are unchanged.)

## Corroborating XBRL contexts (machine-tagged acquisition dates, FY2026 10-K)

These are the dates CrowdStrike itself tagged as the business-combination acquisition dates:

```
0001535527 crwd:PangeaCyberCorporationMember   2025-09-26
0001535527 crwd:PangeaCyberCorporationMember   2025-09-26 2025-09-26
0001535527 crwd:OnumTechnologyInc.Member       2025-09-12
0001535527 crwd:OnumTechnologyInc.Member       2025-09-12 2025-09-12
```

Pangea and Onum are two separate FY2026 Q3 closings; do not conflate them. The FY2026 cash-flow
statement lumps them: "business acquisitions, net of cash acquired, of $382.3 million, which was
related to the Onum Technology Inc. and Pangea Cyber Corporation acquisitions" ($212.1M Pangea +
$252.7M Onum are each *net of cash acquired*; the $382.3M is the cash-flow-statement figure for the
year, not the sum of the two purchase prices).

## Verbatim extract — announcement press release (2025-09-16)

> AUSTIN, Texas and Fal.Con 2025, Las Vegas – September 16, 2025 — CrowdStrike (NASDAQ: CRWD) today
> announced it has signed a definitive agreement to acquire Pangea, a leader in AI security.

The release discloses **no purchase price** and **no expected closing date**; it refers only to
"satisfaction of conditions to closing." So on 2025-09-16 this was a *signed but unclosed* deal.

## Notes / reconciliation

- **Announced 2025-09-16, closed 2025-09-26 — ten days apart.** The prior wiki value of
  `closed: 2025-09-16` (identical to `announced`) is contradicted by both the 10-Q and the 10-K,
  and by the press release's own "signed a definitive agreement … conditions to closing" language.
- **Filed price:** total consideration transferred = $212.1M cash (net of $9.4M cash and restricted
  cash acquired) + $0.3M replacement equity awards + $10.3M replacement liability awards =
  **$222.7 million**. Gross cash out the door was ~$221.5M before netting acquired cash.
- **The ~$260M figure is press-sourced, not filed.** It appears in SecurityWeek, TechRadar,
  BankInfoSecurity and others on/around 2025-09-16; CrowdStrike never published it. The gap versus
  the filed $222.7M is *consistent with* headline deal value including replacement/retention equity
  attributed to post-combination service — which the filing explicitly says was "excluded from the
  purchase price" and is instead expensed as stock-based compensation. The filing does not quantify
  that excluded amount, so the bridge from $222.7M to ~$260M is **inference, not confirmed**. Cite
  $222.7M as the verified number and label ~$260M as a press-reported deal value.
