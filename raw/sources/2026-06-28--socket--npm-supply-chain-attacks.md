URL: https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack ; https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem
fetched: 2026-06-28
Good for: Socket's track record disclosing real-world npm supply-chain attacks (credibility on malicious-package detection).

# Socket — npm supply chain attack disclosures

- Socket disclosed/analyzed major 2025 npm compromises:
  - "Qix" maintainer phishing compromise (Sep 2025) affecting widely-used packages.
  - "Shai-Hulud" self-propagating worm (disclosed Sep 15, 2025) — credential theft + automated package publishing; 500+ packages affected. Also referenced by CISA alert (2025-09-23).
  - "SANDWORM_MODE" campaign (codenamed by Socket) — malicious packages siphoning system info, tokens, env secrets, API keys; auto-propagating via stolen npm/GitHub identities (covered by thehackernews Feb 2026).
- Establishes Socket as a primary source/first-responder on malicious-package (vs known-CVE) supply-chain threats — distinct from CVE-based SCA tools.
