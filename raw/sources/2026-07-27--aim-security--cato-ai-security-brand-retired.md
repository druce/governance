# Aim Security fully absorbed into Cato Networks — brand retired, deal closed

- URLs:
  - https://www.catonetworks.com/news/cato-introduces-first-gpu-powered-sase-platform-with-native-ai-security/ (Cato press release, 2026-03-17) — primary
  - https://www.catonetworks.com/platform/ai-security-aisec/ (Cato "AI Security (AISEC)" product hub) — primary
  - https://www.catonetworks.com/news/cato-acquires-aim-security-to-extend-sase-leadership-and-secure-enterprise-ai-transformation/ (Cato press release, 2025-09-03) — primary, re-checked
  - https://www.securityweek.com/cato-networks-acquires-ai-security-firm-aim-security/ (SecurityWeek, 2025-09-03) — independent corroboration
- Fetched: 2026-07-27
- Good for: confirming the Cato/Aim deal **closed** (not merely announced), that the
  Aim brand and domain are retired, and the successor Cato product name/URL.

## Facts

### Deal closed, not pending
- Cato's own 2025-09-03 press release is written in the past tense — "Cato Networks
  **Acquires** Aim Security" / "Cato has acquired Aim Security" — with no
  "definitive agreement," no expected-close language, and no regulatory-approval
  condition. Independent coverage the same day (SecurityWeek, CyberScoop,
  SiliconANGLE, Help Net Security, Network World, all 2025-09-03/04) likewise
  reports the acquisition as done.
- The PR states existing Aim customers "can deploy the solution today" as a
  standalone offering, with convergence into the Cato SASE Cloud Platform "in
  early 2026" and a migration path for standalone-Aim customers — a
  post-close integration plan, not a pre-close one.
- No separate "completion of acquisition" announcement exists; for a private
  cash+stock deal of this size that is the norm. → **closed: 2025-09-03**
  (same day as announced).
- **Price**: never officially disclosed by Cato. Press reports ~$350M (Calcalist);
  other reports put the range at $350–400M. Keep as unofficial/`null` in
  frontmatter, cite the report in prose.

### Brand and domain retired (verified 2026-07-27)
- `https://www.aim.security` → **HTTP 301** → `https://www.catonetworks.com/`
  (Cato's generic SASE homepage). `https://aim.security` chains to the same place.
  Zero Aim branding survives at the destination — the whole domain, not just the
  root path, folds into Cato.
- Cato's AI-security product pages carry **no "Aim" branding at all**. The
  capabilities are marketed as **"Cato AI Security"**.

### Successor product
- 2026-03-17 Cato press release: "Cato Networks Introduces the Industry's First
  GPU-Powered SASE Platform with Native AI Security" — Cato is "launching **Cato
  AI Security**, converging advanced AI governance and protection capabilities
  from its recent acquisition of Aim Security into the Cato SASE Platform."
  Cato AI Security is **generally available to customers worldwide** as of that
  announcement. Also introduced: **Cato Neural Edge**, the GPU-accelerated
  inspection layer (NVIDIA GPUs deployed across Cato's private backbone) that
  runs the AI inspection inline.
- Product hub: `https://www.catonetworks.com/platform/ai-security-aisec/`
  ("AI Security (AISEC)"). Sub-pages, all live 2026-07-27:
  - `/platform/ai-security-for-end-users/` — shadow-AI discovery + policy on
    employee use of public GenAI (Aim's CASB-for-AI leg)
  - `/platform/agentic-ai-security/` — visibility/logging of agent↔model↔MCP-server
    interactions, tool calls, APIs
  - AI Security for Applications — runtime defense for private AI apps/agents
    against prompt injection, data leakage, runtime attacks (Aim's AI Firewall leg)
  - AI-SPM — continuous discovery/remediation of AI security + compliance risk;
    tests against EU AI Act and ISO 42001.
    (`/platform/ai-security-posture-management-spm/` currently 301s to the
    end-users page — AI-SPM has no standalone page as of 2026-07-27.)
- The three-leg Aim product structure (shadow AI / AI firewall / AI-SPM) survives
  functionally inside Cato AI Security; only the name is gone.

## Assessment

`ownership_state: acquired-pending` is stale. The correct state is
**acquired-closed**, closed 2025-09-03, with the brand retired and the technology
GA inside Cato as of 2026-03-17. Aim Security is no longer a buying unit; the
shopping unit is Cato AI Security on the Cato SASE Platform.
