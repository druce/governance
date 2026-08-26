# Competitor-discovery scan — plan

**Date:** 2026-08-25
**Goal:** Mine Google's Knowledge-Graph "People also search for" (PASF) carousel for
every wiki vendor, to surface market peers that have no page in `wiki/vendors/`.
Output is a scored candidate queue for `wiki-research`, not new pages.

## Method (validated 2026-08-25)

Googling a company with a Knowledge Panel yields a `People also search for` carousel
(4 visible, ~30 behind "See more"). Validated on three vendors:

| Probe | Result |
|---|---|
| Sumo Logic (`siem-soc`) | ~29 peers; ~60% observability/APM noise because Sumo straddles logging+SIEM |
| Exabeam (pure-play SIEM) | ~18 peers, clean cluster; surfaced 10 genuine gaps (Exabeam, LogRhythm, Rapid7, LevelBlue/AlienVault, ArcSight, NetWitness, Anomali, Darktrace, Vectra AI, Cynet, Recorded Future) |
| Lakera (young private) | **No company panel** — Google returned a Zürich *local business* listing; PASF gave geographically co-located firms (Assaia, Modulos, Cerrion, Veezoo). Pure noise. |

**Known blind spots.** PASF is popularity-weighted co-search, not a market map. The
SIEM probes never surfaced Microsoft Sentinel, IBM QRadar, Securonix, Devo, Graylog,
Panther or Hunters. Treat output as a *recall aid*, never as a category census.

## Decisions (confirmed with the human, 2026-08-25)

- **Scope:** all 236 vendor pages across 36 categories. Misses are cheap and
  self-evident; record them rather than pre-filtering.
- **Concurrency:** serial, single Chrome tab. Chrome tabs are shared state and
  parallel bursts risk Google rate-limiting/CAPTCHA (which must not be solved).
  Parallelism is deferred to the scoring phase, which touches no browser.
- **Output:** `reports/competitor-scan-2026-08-25/` — one file per category plus
  `candidates.md`. Derived artifact, so `reports/`, not `raw/sources/`.
- **Scoring:** all four axes — co-mention frequency, category fit + AI relevance,
  alive-and-independent, hedge-fund CTO relevance.

## Phases

### Phase 0 — Prototype extraction (2 vendors, ~6 calls)

Establish a repeatable, screenshot-free extraction. Screenshots at 236 vendors are
prohibitively expensive; use `javascript_tool` to read the carousel from the DOM.

1. Navigate to `google.com/search?q=<vendor>`.
2. JS-extract: (a) whether a company Knowledge Panel exists (vs. a local-business
   listing — the Lakera failure mode), (b) the PASF entries present in the DOM,
   (c) the `See more` href if one exists.
3. **Decision point:** if the initial DOM already carries the full ~30-entry list,
   the run is 1 call/vendor. If it carries only the 4 visible, follow the `See more`
   URL for a second extraction — 2 calls/vendor. Record which, and set the budget.

Abort criteria: if the DOM shape can't be extracted reliably in 3 attempts, stop and
report rather than falling back to 236 screenshots.

### Phase 1 — Sweep (serial, category by category)

For each category in `taxonomy.yaml`, for each vendor with `primary_category` = that
category, query and extract. Append to
`reports/competitor-scan-2026-08-25/<category>.md`:

```
## <vendor-slug>  (query: "<query string>")
panel: company | local-business | none
peers: Name A; Name B; ...
```

Write after each category, not at the end — the run must be resumable. On resume,
skip categories whose file already exists and is complete.

**Guardrails.**
- Pace queries; if Google serves a CAPTCHA or "unusual traffic" page, **stop
  immediately**, record progress, and report. Do not attempt to solve it.
- `panel: local-business` ⇒ discard peers entirely (geographic noise).
- Query string = vendor display name from frontmatter `name:`, disambiguated where
  the slug is a product not a company.

### Phase 2 — Dedupe and classify

1. Union all peer names; normalize (case, `Inc.`/`AG`/`Ltd.` suffixes, aliases —
   LogsHero≡Logz.io, AlienVault≡LevelBlue, LogDNA≡Mezmo, Chronicle≡Google SecOps).
2. Subtract names already in `wiki/vendors/` (match on slug *and* on display name and
   known product names — e.g. Cortex XSIAM ⇒ `palo-alto-networks`).
3. Count co-mention frequency and record which wiki vendors surfaced each name.
4. Fan out to subagents (no browser) to classify the survivors: proposed taxonomy
   category, alive/acquired/dead status, one-line what-it-is.

### Phase 3 — Score and write `candidates.md`

Score 0–3 on each axis, sum to 0–12:

| Axis | 3 | 0 |
|---|---|---|
| Co-mention frequency | surfaced by 5+ wiki vendors | surfaced once |
| Category fit + AI relevance | maps to an existing category and matters to the AI thesis | no category, legacy infra |
| Alive and independent | shipping, independent or actively-invested product line | brand retired / folded into a parent |
| Hedge-fund CTO relevance | a mid-size asset manager would plausibly shortlist it | hyperscale-only or SMB-only |

Output `candidates.md` ranked by total, grouped by proposed category, each row
carrying: name, score breakdown, co-mention count, surfacing vendors, proposed
category, status note. Anything scoring ≥8 is the recommended `wiki-research` queue.

**No claims are written into `wiki/` by this run.** Per CLAUDE.md §7, PASF is not a
source — every candidate needs its own verification pass before it becomes a page.

### Phase 4 — Log

Append a `research` entry to `log.md` recording the method, date, coverage
(categories/vendors actually queried), and the candidate count.

## Estimated size

236 vendors × 1–2 calls = 236–472 browser calls, plus ~40 file writes and a scoring
fan-out. Serial, so wall-clock is the binding constraint, not correctness.
