---
name: wiki-lint
description: Use when checking wiki health, before committing wiki page changes, after adding or migrating vendor/category pages, or when asked to lint, audit, or find stale/broken/inconsistent wiki content.
---

# Wiki Lint

Two-tier lint per `SCHEMA.md` §5: mechanical rules run as a script, editorial
rules run as an LLM pass. Output is one triaged report: **error** (fix before
commit) / **warn** (judgment call) / **research** (feeds `wiki-research`).

## Steps

1. **Mechanical pass** (rules 1–10 + trifecta scoping + commit gate):

   ```bash
   python3 scripts/wiki_lint.py --report          # writes reports/lint-YYYY-MM-DD.md
   ```

   Flags: `--online` adds URL-liveness/redirect checks (slow; run ~monthly or
   before survey pushes). `--write-index` regenerates `index.md` from page
   frontmatter — run after any batch of page changes. Exit 1 = errors exist.

2. **Editorial pass** (SCHEMA.md §5.2 rules 11–18). Scope = pages changed since
   the last lint entry in `log.md`, plus their link neighbors. For >10 pages,
   dispatch parallel subagents, ~10 pages each; each agent gets the rule list
   from SCHEMA.md §5.2 and returns findings as `(rule, file, severity, message)`.
   Judge against the page body, not just frontmatter — e.g. rule 12 fails if
   "Key differentiators" names no category peer; rule 14 fails if prose says
   "acquired by" for an `acquired-pending` vendor.

3. **Merge** editorial findings into the same report file under the same
   severity headings, marked `E` for editorial.

4. **Gate**: any `error` or `Status: Unresolved` blocks commit — surface these
   to the human rather than declaring a clean pass.

5. Append a `## [YYYY-MM-DD] lint | <summary>` entry to `log.md`.

## Notes

- Enum/schema truth lives in `taxonomy.yaml`; if a lint error says a value
  isn't in vocab, fix the page (or, rarely, propose a vocab change → `log.md`
  decision + regenerate `taxonomy.md` via `scripts/gen_taxonomy_md.py`).
- `research` items are not failures — hand the list to `wiki-research`.
- Never hand-edit `taxonomy.md` or the generated parts of `index.md`.
