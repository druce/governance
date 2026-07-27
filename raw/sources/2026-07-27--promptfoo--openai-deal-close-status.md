# OpenAI ← Promptfoo: announcement vs. close status (no public close confirmation)

- **Primary URL (acquirer):** https://openai.com/index/openai-to-acquire-promptfoo/
- **Primary URL (target):** https://www.promptfoo.dev/blog/promptfoo-joining-openai/
- **Corroborating:** https://techcrunch.com/2026/03/09/openai-acquires-promptfoo-to-secure-its-ai-agents/
  · https://www.cnbc.com/2026/03/09/open-ai-cybersecurity-promptfoo-ai-agents.html
  · https://news.crunchbase.com/ma/data-openai-2023-2026-acquisitions-open-source-astral-promptfoo/
- **Fetched:** 2026-07-27
- **Good for:** settling whether the OpenAI/Promptfoo deal has **closed**. Answer: **announced
  2026-03-09 as a *pending* transaction, and no public close has ever been confirmed** — not by
  OpenAI, not by Promptfoo, not by any trade press through 2026-07-27. Both parties are private,
  so there is no SEC filing to force disclosure. Any `closed:` date on the wiki page is
  unsupported. Confidence: high on "announced pending"; high on "no public close confirmation
  found" (this is a *searched-and-not-found*, not a claim that closing did not occur).

## The crux: both principals used pending language, and both carry a closing-conditions rider

OpenAI's post is literally titled **"OpenAI to acquire Promptfoo"** — future/intent, not
"has acquired". Verbatim, from the OpenAI newsroom post (2026-03-09):

> We're acquiring Promptfoo, an AI security platform that helps enterprises identify and remediate
> vulnerabilities in AI systems during development. **Once the acquisition is finalized** we will
> integrate Promptfoo's technology directly into **OpenAI Frontier,** our platform for building and
> operating AI coworkers.

and the closing line of that same post, set in italics:

> *The closing of the acquisition is subject to customary closing conditions.*

Promptfoo's own post, "Promptfoo is joining OpenAI" (published 2026-03-09T00:00:00Z), verbatim:

> Today we are announcing that Promptfoo **has agreed to be acquired** by OpenAI.
>
> Promptfoo will remain open source and we will continue to serve users and customers.

and, again near the end:

> The closing of the acquisition is subject to customary closing conditions.

"has **agreed to be** acquired" + "**once** the acquisition is finalized" + an explicit
closing-conditions rider is signing language, not completion language. This is the opposite of the
Zscaler/SPLX pattern (see `2026-07-27--splxai--zscaler-10q-close-date-price.md`), where the press
release said "has acquired" and the deal had in fact closed three days *before* the announcement.

## Trade press tracked it as pending, and headlines are unreliable here

Note the split between headlines and body copy — several outlets wrote "OpenAI **acquires**
Promptfoo" in the headline while the body described a deal that had not closed. Do not take a
headline as evidence of closing.

- **TechCrunch** (2026-03-09, 10:49 AM PDT), headline "OpenAI acquires Promptfoo…", body:
  "**once the deal closes**, Promptfoo's technology will be integrated into OpenAI Frontier."
  No expected close date, no regulatory-review mention. "OpenAI did not disclose the value of the
  transaction." Context: Promptfoo raised ~$23M total, valued ~$86M post-money after a July 2025
  Series A (~$18.4M, Insight Partners lead, a16z participating), per PitchBook.
- **CNBC** (2026-03-09), headline "OpenAI **to buy** cybersecurity startup Promptfoo…" — pending
  framing in the headline itself. (Page returned HTTP 403 to direct fetch on 2026-07-27; status
  read from the headline and search-index summary, not the full body.)
- **SecurityWeek**, **Security MEA**, **PYMNTS**, **EdTech Innovation Hub**, **TechInformed** all
  used "to acquire" / "plans to acquire" / "agrees to be acquired" / "moves to bring… into
  Frontier" framing.
- **OpenAI on X** (@OpenAI, status 2031052793835106753): "We're acquiring Promptfoo." — present
  progressive, consistent with pending.
- **Crunchbase News** M&A roundup (2026-03-25) mentions OpenAI "snapped up Promptfoo" but
  **does not state a close date or a completed/pending status** — it is not evidence of closing.

## Searched for a close confirmation and found none

Queries run 2026-07-27, all returning only the 2026-03-09 announcement cluster and no
completion notice:

- `OpenAI Promptfoo acquisition "completed" OR "closed" deal April May June 2026`
- `OpenAI Promptfoo acquisition "has closed" OR "finalized" OR "completed the acquisition"`
- `"promptfoo" OpenAI acquisition close date "subject to customary closing conditions"`
- `"Promptfoo" OpenAI deal antitrust HSR review pending status update`
- `promptfoo.dev blog OpenAI Frontier promptfoo news July 2026`

No OpenAI newsroom follow-up post, no Promptfoo blog follow-up post, no trade-press item dated
after 2026-03-09 asserting the transaction completed. There is also no public reporting of an HSR
/ antitrust review on this deal one way or the other.

## Corporate-artifact checks — all still show a standalone Promptfoo (as of 2026-07-27)

These are *circumstantial* signals, not dispositive: an acquirer may leave artifacts untouched for
months after closing. But nothing here corroborates a close, and all of it is consistent with
either "not yet closed" or "closed quietly with no integration work done."

| Artifact | State on 2026-07-27 | Source |
|---|---|---|
| GitHub org `promptfoo` | Still exists, standalone, **not** transferred under an OpenAI org. `company: null`, `email: inquiries@promptfoo.dev`, `blog: https://promptfoo.dev`, `archived_at: null`, org `updated_at` 2026-06-23 | `api.github.com/orgs/promptfoo` |
| Org public members | `mldangelo` (Michael D'Angelo, co-founder) still listed | `api.github.com/orgs/promptfoo/public_members` |
| `promptfoo/promptfoo` LICENSE | `Copyright (c) Promptfoo 2025` — **unchanged**; last LICENSE-touching commit was 2025-01-16 ("chore: update year"). No post-announcement copyright reassignment to OpenAI | `raw.githubusercontent.com/promptfoo/promptfoo/main/LICENSE` |
| Repo activity | Actively developed under the promptfoo org; commits on 2026-07-27 itself (e.g. `fix(redteam): harden risk reports and WebSocket timeout tests (#10211)`) | `api.github.com/repos/promptfoo/promptfoo/commits` |
| Repo description | Unchanged marketing copy; no "part of OpenAI" notice, no pinned acquisition banner | same |
| promptfoo.dev footer | **"© 2026 Promptfoo, Inc."** — no OpenAI ownership notice, no "part of OpenAI" branding anywhere on the homepage | https://www.promptfoo.dev/ |

Note the mild irony that the repo description reads "Used by OpenAI and Anthropic" — that is a
*customer* reference predating the deal, not an ownership statement. Do not misread it.

## Bottom line for the wiki

- **Announced:** `2026-03-09` — solid, dual-confirmed by both parties' own posts.
- **Closed:** **no public confirmation exists.** Nothing found; no date can be sourced. The
  2026-03-09 value currently on the page is not attested by any source and appears to be the
  announced date duplicated into the `closed` field.
- **Ownership state:** the deal was explicitly pending at announcement and has never been publicly
  confirmed closed → `acquired-pending`, with a `verify_after` date, is the defensible value.
- **Price:** undisclosed by OpenAI; both parties private, so no filing will surface it. Keep
  `null`. (~$86M post-money valuation as of July 2025 is a *pre-deal valuation*, not a price —
  do not launder it into the `price` field.)
- **Genuinely unknowable caveat:** OpenAI and Promptfoo are both private, so there is no 10-Q/8-K
  path to a close date the way there was for Zscaler/SPLX. Absent a follow-up blog post, a
  copyright/org change, or a press mention, the close date may never become public even if the
  deal has in fact closed. Record this as "not publicly confirmed," **not** as "did not close."
