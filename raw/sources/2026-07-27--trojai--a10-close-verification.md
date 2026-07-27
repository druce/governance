# TrojAI / A10 Networks — acquisition close re-verification (2026-07-27)

- Primary URL: https://www.a10networks.com/news/press-releases/a10-networks-acquires-trojai-inc-expanding-ai-roadmap/
- Corroborating: https://www.businesswire.com/news/home/20260615349365/en/A10-Networks-Acquires-TrojAI-Inc.-Expanding-AI-Roadmap
- Corroborating: https://www.stocktitan.net/news/ATEN/a10-networks-acquires-troj-ai-inc-expanding-ai-vtaqdena2rao.html
- Live site checked: https://troj.ai (200, no redirect)
- EDGAR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001580808 (A10 Networks, CIK 0001580808)
- Fetched / checked: 2026-07-27
- Good for: settling whether `ownership_state: acquired-closed` is actually supported, exchange/ticker
  correction, and the absence of any disclosed price.

## The question this file answers

The 2026-06-28 pass recorded `acquisition: {announced: 2026-06-15, closed: 2026-06-15}` — a `closed`
value identical to `announced` with no separate citation. That is the exact shape of the defect found
on `natoma.md` and `symmetry-systems.md` in this sweep, so it had to be re-checked rather than trusted.

**Verdict: the closed state holds.** Unlike those two cases, the evidence here affirmatively supports
completion and there is no evidence of pendency anywhere.

## Verbatim primary-source language

A10's own press release, dateline and lead sentence (confirmed identically via two independent
retrievals — a10networks.com and StockTitan's reproduction of the wire copy):

> "SAN JOSE, Calif., June 15, 2026 – A10 Networks (NYSE: ATEN) today announced that it has acquired
> TrojAI, an AI security company focused on helping organizations secure, test and govern AI
> applications and agentic workflows."

**"has acquired"** — completed-transaction grammar. Not "has entered into a definitive agreement to
acquire," not "expects to close." There is **no closing-conditions, regulatory-approval, or
expected-close language anywhere in the release**. Contrast Zscaler/Symmetry, where the 10-Q
explicitly said "expected to close ... subject to the satisfaction of closing conditions."

Materiality statement (verbatim):

> "A10 does not expect the acquisition to have a material impact on its financial results for fiscal
> year 2026."

## Corroborating operational evidence: the brand integration is already live

troj.ai (checked 2026-07-27, HTTP 200, no redirect) carries:
- a banner: **"New! A10 Networks Acquires TrojAI"**, linking to the 2026-06-15 BusinessWire release;
- a logo that reads **"TrojAI by A10 Networks"**.

This matters as evidence, not just branding. An acquirer putting its own name into the target's logo
and product masthead is post-close behaviour: pre-close, that degree of brand and go-to-market
integration is the sort of thing antitrust gun-jumping rules exist to prevent. Symmetry Systems, by
contrast, is still on its own domain with a "Zscaler *to acquire*" banner — the pending-deal pattern
looks visibly different.

Products listed on the post-acquisition site: TrojAI Detect, TrojAI Defend, **TrojAI Defend for MCP**,
**TrojAI Defend for Employees**. Solution pages segment by industry (Financial Services, Insurance,
Technology, Manufacturing, Public Sector) and by agent type (Custom Agents, Third-Party Agents,
Desktop Agents).

## SEC evidence — negative, and consistent with a closed immaterial tuck-in

Checked EDGAR directly rather than relying on the press release:

- **A10 Networks, CIK 0001580808. `exchanges: ["NYSE"], tickers: ["ATEN"]`** per
  `data.sec.gov/submissions/CIK0001580808.json`. A10 trades on the **NYSE**, not NASDAQ. The
  press release's "NYSE: ATEN" is correct.
- **No 8-K was filed for the TrojAI acquisition.** A10's only 8-Ks since 2026-05-01 are 2026-05-01 and
  2026-05-07, both Item 5.02 (officer/director changes). No Item 2.01 (completion of acquisition).
- **EDGAR full-text search for "TrojAI" across all 10-K/10-Q/8-K returns zero hits.** The only three
  EDGAR hits for the string anywhere are TrojAI, Inc.'s own Form D filings (CIK 0002019012,
  all 2024-04-24) — its seed round, not an A10 filing.

The absence of an 8-K is **not** evidence against closing. Item 2.01 is only triggered by acquisition
of a *significant* amount of assets, and A10 stated the deal is immaterial to FY2026 — so no filing
obligation arises. The absence is exactly what a closed-but-immaterial tuck-in looks like.

- **No 10-Q covers the deal yet.** A10's most recent 10-Q is for the quarter ended 2026-03-31 (filed
  2026-05-07), which predates the acquisition. The quarter ended **2026-06-30** is the first period
  containing it; that 10-Q is expected **early August 2026** and is the first filing that could carry
  a business-combination note, purchase-price allocation, or a cash-paid-for-acquisition line.
  → this is what `verify_after: 2026-08-15` is queued against.

## Price

**Undisclosed, and not derivable.** Terms were not disclosed in the release, and unlike the F5/SurePath
case there is no filed cash-flow statement covering the period from which to bound the payment. Stays
`null` per CLAUDE.md §7 rather than being guessed at. The Q2 10-Q may or may not break it out given
A10 has already called it immaterial.

## Company background (carried forward, HQ re-confirmed against SEC)

- Founded 2019 (incorporated 2020) by **James Stewart** (CTO) and **Stephen Goddard**. CEO since 2024:
  **Lee Weiner** (ex-Rapid7).
- HQ **Saint John, New Brunswick, Canada** — independently confirmed by TrojAI, Inc.'s SEC Form D
  business address: 14 King St., Suite 102, Saint John, NB E2L 1G2. Boston office.
- Pre-acquisition funding ~$9.65M USD disclosed (~$3M seed early 2022; $5.75M seed April 2024 —
  Flying Fish Partners, Build Ventures, Techstars Ventures; plus NBIF).

## Strategic read (for the body copy)

A10 is a networking vendor — application delivery controllers, load balancers, DDoS protection, ~$250M
revenue. TrojAI is its move up the stack from packet/flow security into **model- and prompt-layer**
security, which is a genuine diversification rather than an adjacent bolt-on: red teaming and runtime
prompt inspection share almost no engineering substrate with ADC hardware. The stated thesis is
"sovereign AI security" — pairing A10's on-box/hardware AI firewall with TrojAI's software Detect +
Defend so the whole thing can run inside a customer's own boundary. That self-hosted/sovereign posture
is the part of the rationale most relevant to regulated and non-US buyers.
