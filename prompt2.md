# Bootstrap prompt — paste into Claude Code from the project directory

> Prereqs: this directory contains `CLAUDE.md` and the two seed files
> (the layer-cake blog `.md` and the survey `.csv`). Paste everything below as your
> first message to Claude Code.

---

Read `CLAUDE.md` fully — it is the contract for this wiki. Then read both seed files
in this directory (the layer-cake blog markdown and the survey CSV). Then bootstrap
the wiki from scratch, following the page schemas, conventions, and build discipline
in `CLAUDE.md`. Work autonomously through the phases below, committing as you go, and
only stop for a hard contradiction you can't resolve or a taxonomy decision you want
me to make. Use web search + fetch for research and cache what you rely on into
`raw/sources/` with dated filenames.

**Phase 0 — scaffold & taxonomy.**

1. `git init` if needed. Create the directory layout from `CLAUDE.md §2`.
2. Move the two seed files into `raw/seeds/` (immutable from here on).
3. Build `taxonomy.md`: reconcile the layer-cake doc (spine) with the CSV survey
   categories (mapped in) into ONE canonical category set, grouped by layer, each
   with a slug, priority, and the seed-doc row + seed-CSV category it reconciles.
   Where the two disagree or a cleaner cut exists, decide and record it in
   `taxonomy-gaps.md` and `log.md`. Split slash-bundled CSV entries; skip
   `Other (Please Specify)` as vendors.
4. Create skeleton `index.md`, `log.md`, and `wiki/overview.md` (thesis stub from
   the layer-cake doc: the layer cake, the red/yellow/green trust zones, the lethal
   trifecta).
5. **Pause and show me `taxonomy.md` + `taxonomy-gaps.md`** before building pages, so
   I can sanity-check the spine. (Wait for my OK.)

**Phase 1 — category pages.** One page per canonical category (schema in `CLAUDE.md
§4.2`), including the `## Survey` scaffolding (§6) with the reused response scale.

**Phase 2 — vendor stubs.** One stub per distinct vendor pulled from the CSV plus any
vendor named in the layer-cake doc but missing from the CSV. Full frontmatter,
`status: stub`, correct `categories` (multi-tag; one page per vendor even if it spans
categories). List each on its category page(s).

**Phase 3 — deep research (all vendors, one shot).** Going Day-1 layers first, then
Day-2, then optional, research every vendor: search + fetch + cache sources, fill the
full vendor page, verify ownership/M&A against primary sources with dates and
confidence, write the CTO/hedge-fund lens, link competitors, and update each vendor's
category page positioning. Update `index.md` and append `log.md` after each vendor;
**commit after each vendor** for resumability. If interrupted, resume from the next
unbuilt vendor per the log.

**Phase 4 — comparisons & overview.** Build the comparison pages suggested in
`CLAUDE.md §4.3` (AI gateways; runtime AI firewalls; the AI-security M&A map; "what's
actually Day-1 for a ~50-person hedge fund"; entitlement-aware RAG). Flesh out
`overview.md` into the real thesis with links into every category.

**Phase 5 — final taxonomy pass & lint.** Now that research is done, revisit
`taxonomy.md`: rename categories and move vendors where the research argues for it,
fix affected links and frontmatter, and log every change. Then run the full lint
checklist (`CLAUDE.md §10`), including the `Status: Unresolved` commit gate, and give
me a short report: what's built, counts by category, unresolved contradictions, low-
confidence M&A still needing a primary source, and your top taxonomy
recommendations.

Throughout: plain English, vendor-neutral, written for a CTO. Anchor claims to cached
sources, never invent, flag uncertainty, and keep `index.md` + `log.md` current so any
run is resumable.