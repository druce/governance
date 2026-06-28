# Introducing IsAgent (Stytch blog)

URL: https://stytch.com/blog/introducing-is-agent/
fetched: 2026-06-28
Good for: the agent-detection product (IsAgent) and the distinction vs Device Fingerprinting. Vendor blog.

## Key extracted text

- Publication date: 2025-08-01.
- IsAgent: a lightweight front-end component that identifies AI agents and programmatic traffic (bots, LLMs) so sites can route them to a tailored agent experience (LLMs.txt, MCP servers).
- How it works: front-end API analyzes User-Agent strings and TLS fingerprints, matched against known AI agents; works with Browserbase on optional agent self-identification via cryptographically-signed messages.
- Explicit limitation: "best-effort heuristics that may be incorrect at times"; a "client hint, not a security guarantee" — NOT for blocking malicious bots.
- For fraud prevention / deception detection, Stytch directs users to its Device Fingerprinting product (deeper backend integration).
- Integration: ~5 lines of code.
