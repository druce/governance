# Palo Alto Networks / Talon Cyber Security — announced date, close date, and filed purchase price

- **Primary URL (close + price):** https://www.sec.gov/Archives/edgar/data/1327567/000132756724000005/panw-20240131.htm
- **Primary URL (announced/signing date + signing-date estimate):** https://www.sec.gov/Archives/edgar/data/1327567/000132756723000032/panw-20231031.htm
- **Announcement press release:** https://www.paloaltonetworks.com/company/press/2023/palo-alto-networks--announces-intent-to-acquire-enterprise-browser-start-up-talon-cyber-security
- **Close press release:** https://www.paloaltonetworks.com/company/press/2023/palo-alto-networks--closes-talon-cyber-security-acquisition-and-will-offer-complimentary-enterprise-browser-to-qualified-sase-ai-customers
- **Filer:** Palo Alto Networks, Inc. (NASDAQ: PANW), CIK 0001327567. Fiscal year ends July 31.
- **Fetched:** 2026-07-27
- **Good for:** settling three things the wiki page previously got wrong or left null: (a) the
  **announced** date is **2023-11-06**, *not* a copy of the close date — PANW's own Q1 FY2024 10-Q
  names 2023-11-06 as the definitive-agreement date and the newsroom "Announces Intent to Acquire"
  release carries the same dateline; (b) the **closed** date **2023-12-28** is correct and is
  independently confirmed by the Q2 FY2024 10-Q text *and* by PANW's XBRL acquisition-date tags;
  (c) the **price** as actually filed is **$458.6M total purchase consideration**, not the
  widely-reported "~$625M". Confidence: high (two SEC primary filings + two issuer press releases).

## Timeline (all issuer-primary)

| Event | Date | Source |
|---|---|---|
| Definitive agreement entered / publicly announced | **2023-11-06** | Q1 FY2024 10-Q Note 15 (Subsequent Events); PANW newsroom "Announces Intent to Acquire" |
| Acquisition completed (closed) | **2023-12-28** | Q2 FY2024 10-Q Note 7 (Acquisitions); PANW newsroom "Closes Talon Cyber Security Acquisition"; XBRL `panw:TalonCyberSecurityLtdMember 2023-12-28` |

Announcement and close sit in different PANW fiscal quarters: Q1 FY2024 ended 2023-10-31 (so Talon
appeared there only as a subsequent event), Q2 FY2024 ran 2023-11-01 → 2024-01-31 (where the
completed business combination is booked).

## Verbatim extract — Form 10-Q, quarter ended 2023-10-31 (filed 2023-11-17), Note 15. Subsequent Events

> On November 6, 2023, we entered into a definitive agreement to acquire Talon Cyber Security Ltd.,
> a privately-held cyber security company ("Talon"), for total consideration of approximately
> $550.0 million, including approximately $434.9 million in cash and approximately $115.1 million
> in replacement awards, subject to adjustment. We expect the acquisition will support Prisma
> SASE's approach to provide secure access to business applications for unmanaged and personal
> devices with an enterprise browser.
>
> The proposed acquisitions of Dig and Talon are expected to close during our second quarter of
> fiscal 2024, subject to the satisfaction of customary closing conditions.

This is the authoritative anchor for the **announced** date. Note the "subject to the satisfaction
of customary closing conditions" language — proof the deal was genuinely pending on 2023-11-06 and
did not close the same day.

## Verbatim extract — Form 10-Q, quarter ended 2024-01-31 (filed 2024-02-21), Note 7. Acquisitions

> **Talon Cyber Security Ltd.**
>
> On December 28, 2023, we completed our acquisition of Talon Cyber Security Ltd. ("Talon"), a
> privately-held cyber security company. We expect the acquisition will support Prisma SASE's
> approach to provide secure access to business applications for unmanaged and personal devices
> with an enterprise browser. The total purchase consideration for the acquisition of Talon was
> $458.6 million, which consisted of the following (in millions):
>
> | | Amount |
> |---|---|
> | Cash | $439.0 |
> | Fair value of replacement awards | 19.6 |
> | **Total** | **$458.6** |
>
> As part of the acquisition, we issued replacement equity awards, which included 0.3 million
> shares of our restricted common stock. The total fair value of the replacement equity awards was
> $109.6 million, of which the portion attributable to services performed prior to the acquisition
> date was allocated to purchase consideration. The remaining fair value was allocated to future
> services and will be expensed over the remaining service periods as share-based compensation.

Purchase price allocation (preliminary, in millions): Goodwill $253.7, Identified intangible assets
$131.4, Cash and restricted cash $53.9, Net assets acquired $19.6, Total $458.6. The single
identified intangible is developed technology, $131.4M over a 5-year estimated useful life.
Goodwill is not expected to be deductible for income tax purposes.

## Corroborating XBRL contexts (machine-tagged acquisition dates)

From the Q2 FY2024 filing's XBRL context definitions — the dates PANW itself tagged as the
business-combination acquisition dates for the two deals that closed in that quarter:

```
0001327567 panw:DigSecuritySolutionsLtdMember    2023-12-05 2023-12-05
0001327567 panw:DigSecuritySolutionsLtdMember    2023-12-05
0001327567 panw:TalonCyberSecurityLtdMember      2023-12-28 2023-12-28
0001327567 panw:TalonCyberSecurityLtdMember      2023-12-28
```

Dig closed 2023-12-05 ($255.4M) and Talon closed 2023-12-28 ($458.6M) — two separate closings in
PANW's Q2 FY2024. Combined goodwill acquired in the six months ended 2024-01-31: $445.9M
(balance $2,926.8M → $3,372.7M).

## Press releases (issuer newsroom, corroborating)

- **2023-11-06** — "Palo Alto Networks® Announces Intent to Acquire Enterprise Browser Start-up
  Talon Cyber Security." Dateline Nov 06, 2023. **No purchase price is disclosed in this release.**
- **2023-12-28** — "Palo Alto Networks® Closes Talon Cyber Security Acquisition and Will Offer
  Complimentary Enterprise Browser to Qualified SASE AI Customers." Dateline: "SANTA CLARA, Calif.,
  Dec. 28, 2023 /PRNewswire/ -- Palo Alto Networks (NASDAQ: PANW), the global cybersecurity leader,
  today announced that it has completed the acquisition of Talon Cyber Security, a pioneer of
  enterprise browser technology." **No purchase price is disclosed in this release either.**

## Notes / reconciliation

- **The "~$625M" figure is press estimate, not a filed number, and no PANW source supports it.**
  It traces to Israeli/Bloomberg reporting around 2023-11-06 (Bloomberg, Calcalist and successors),
  which used deal-value conventions that fold in retention and unvested equity. PANW never
  published a price in either press release. The two numbers PANW *did* file are:
  - **~$550.0M** — the signing-date estimate of *total consideration* (approx. $434.9M cash +
    $115.1M replacement awards), disclosed 2023-11-17 as a subsequent event, explicitly "subject to
    adjustment."
  - **$458.6M** — the final GAAP *total purchase consideration* at close ($439.0M cash + $19.6M
    fair value of replacement awards attributable to pre-combination service).
  The gap between the two is mostly an accounting split, not a renegotiation: of the $109.6M total
  fair value of replacement awards, only $19.6M was allocated to purchase consideration and the
  remaining ~$90.0M is post-combination share-based comp. $458.6M + $90.0M ≈ $548.6M, i.e. ~$550M —
  which reconciles the signing estimate almost exactly. Neither figure reaches $625M.
  **Recommended for the wiki:** `price: $458.6M` (as filed at close), with the ~$550M announced
  headline and the ~$625M press figure noted as estimates rather than filed values.
- **Announced ≠ closed here:** 53 days elapsed between signing (2023-11-06) and close
  (2023-12-28). The prior wiki frontmatter, which carried `announced: 2023-12-28` identical to
  `closed: 2023-12-28`, was wrong — the close date had been duplicated into the announced field.
- The 2023-11-06 announcement **predates** PANW's Ignite '23 conference (mid-November 2023); the
  deal was announced ahead of the show, not at it.
- Product lineage: Talon Enterprise Browser → **Prisma Access Browser** (later marketed as
  **Prisma Browser**), sold as part of the Prisma SASE line.
