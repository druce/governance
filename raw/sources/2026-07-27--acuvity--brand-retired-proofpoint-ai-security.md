# Acuvity brand retired → Proofpoint AI Security

- URL: https://www.proofpoint.com/us/platform/ai-security (301 redirect target of acuvity.ai)
  - plus product pages: https://www.proofpoint.com/us/products/ai-access-security ,
    https://www.proofpoint.com/us/products/agentic-ai-security ,
    https://www.proofpoint.com/us/products/ai-mcp-security (all HTTP 200)
- Fetched: 2026-07-27
- Good for: confirms the Acuvity brand and standalone site are gone; the technology now
  ships as three Proofpoint AI Security SKUs. Does NOT add new acquisition dates —
  those stay anchored to the 2026-02-12 Proofpoint press release
  (`raw/sources/2026-07-13--acuvity--proofpoint-acquisition-pr.md`).

## Facts

- **Redirect verified 2026-07-27**: `https://acuvity.ai` returns `HTTP/1.1 301 Moved
  Permanently`, `Location: https://www.proofpoint.com/us/platform/ai-security`. Hard
  redirect, no interstitial.
- The landing page is **100% Proofpoint-branded**: "Proofpoint AI Security" — "Only
  Proofpoint unifies AI runtime security with industry-leading data security to
  understand AI intent, govern every interaction, and build trust in enterprise AI."
  **Neither "Acuvity" nor "RYNO" appears anywhere on it.**
- Unlike Normalyze, there is **no "Acuvity is now Proofpoint" transition page**:
  `https://www.proofpoint.com/us/acuvity-is-now-proofpoint` returns 404 (checked
  2026-07-27). The brand was retired without a lineage landing page.
- The Acuvity capability set is now sold as **three product SKUs** under the AI
  Security platform:
  - **AI Access Security** — discover/inventory all AI apps (first-party, third-party,
    embedded) and AI agents; runtime observability; runtime inspection and enforcement
    with "18 built-in detectors"; forensic audit trails; SIEM/SOAR routing.
  - **Agentic AI Security** — governance of autonomous agent behavior.
  - **AI MCP Security** — MCP server discovery + risk classification (missing auth,
    missing encryption, unsanctioned remote hosts, local servers on employee machines);
    **gateway-style enforcement** (verifies identity, checks permissions, inspects
    content for sensitive data before a request reaches a server); "Transaction
    Forensics" reconstructing every MCP transaction (user → app → LLM → server);
    a "Trusted MCP Server Registry" of 800-plus pre-vetted open-source MCP servers.
  - None of the three product pages mentions Acuvity, RYNO or minibridge by name.
- Platform framing on the AI Security page ties AI security to Proofpoint's data
  security (DSPM/DLP) context — "intent-aware", data-context-informed.
- `docs.acuvity.ai` still resolves but is auth-gated (HTTP 401) — no public content.

## What this resolves / does not resolve

- **Resolves** the page's open question "whether RYNO survives as a product/brand":
  **no** — brand retired, capability re-badged into three Proofpoint SKUs.
- **Resolves** the MCP-depth open question: MCP support is **gateway-style inline
  enforcement**, not monitoring only.
- **Does not** disclose deal price (still undisclosed) or add a separate close date
  (the 2026-02-12 PR is past-tense/completed).
