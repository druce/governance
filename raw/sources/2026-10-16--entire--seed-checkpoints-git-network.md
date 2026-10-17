# Entire (entire.io) — seed round, Checkpoints CLI, distributed git network

- URL: https://techcrunch.com/2026/02/10/former-github-ceo-raises-record-60m-dev-tool-seed-round-at-300m-valuation/
- URL: https://github.com/entireio/cli (README) and https://api.github.com/orgs/entireio/repos
- URL: https://siliconangle.com/2026/07/08/ex-github-chiefs-entire-opens-distributed-git-network-agent-era/
- URL: https://www.axios.com/2026/02/10/former-github-ceo-ai-coding-startup (search result only)
- Fetched: 2026-10-16
- Good for: founding, funding, product mechanics (what is recorded and where), licence, team size, roadmap.

## Funding (TechCrunch, 2026-02-10)
- $60M seed at $300M valuation, led by Felicis ("largest-ever seed round for a dev tool startup", per Felicis).
- Others: Madrona, M12 (Microsoft), Basis Set, Harry Stebbings, Jerry Yang, Olivier Pomel. (Garry Tan named in some secondary coverage — not confirmed in TechCrunch.)
- Founder: Thomas Dohmke, GitHub CEO ~4 years, left August 2025.
- First release: open-source "Checkpoints" — links agent-written code to prompts and transcripts.
- Planned: Git-compatible database; "universal semantic reasoning layer"; AI-native UI.

## Entire CLI (GitHub, MIT licence; repo created 2026-01-02, active 2026-10-16, ~5.2k stars)
- Hooks into git; captures AI agent sessions: transcripts, prompts, files touched (with content hashes),
  token usage, **tool calls**, subagent task records.
- On commit, condenses session into a checkpoint linked by an `Entire-Checkpoint: <id>` commit trailer.
- Storage: in the repo's own git object store as refs `refs/entire/checkpoints/<shard>/<id>`, not on the branch.
- Best-effort secret redaction; opt-in PII redaction; transcripts are visible to anyone if the repo is public.
- README pitches "Maintain traceability — support audit and compliance requirements".
- Supported agents: Claude Code, Codex, Cursor, Antigravity, Pi, OpenCode, + external-agent plugins
  (SiliconANGLE adds Factory AI, GitHub Copilot).
- Other MIT repos: entire-brain (repo memory layer), entire-graph (code map), skills, git-sync, pgr (MCP code-search server).

## Git network preview (SiliconANGLE, 2026-07-08)
- Waitlist preview of distributed Git network; regions US, EU, Australia; mirror a GitHub repo in one step.
- Company benchmarks: ~570k clones/h from one repo; 586 pushes/s.
- Features: Entire Blame (session/prompt behind a line), Entire Review (multi-agent review), semantic search.
- Plans: native hosting; full decentralisation for data residency.
- >40 employees across nine countries; target 60 by year-end. No new funding reported. Pricing unpublished.
