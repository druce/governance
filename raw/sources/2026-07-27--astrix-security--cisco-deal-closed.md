# Cisco/Astrix Security acquisition CLOSED 2026-06-29; standalone sales ended 2026-06-30

- URLs:
  - https://blogs.cisco.com/news/cisco-announces-intent-to-acquire-astrix-security
    (Cisco Blogs, Peter Bailey SVP/GM Security, published 2026-05-04, **updated
    2026-06-29 with completion note**) — primary
  - https://astrix.security (Astrix homepage, live under Astrix branding with a
    "now part of Cisco" banner) — primary
  - https://astrix.security/learn/blog/a-new-chapter-astrix-security-is-joining-cisco/
    (Astrix's own announcement, 2026-05-04) — primary, previously cached
    2026-06-28
  - https://www.calcalistech.com/ctechnews/article/dy5obf581 (Calcalist/Ctech) —
    press report of ~$400M price; **not** an official figure
- Fetched: 2026-07-27
- Good for: confirming the Cisco/Astrix deal **closed** (announced 2026-05-04,
  completed 2026-06-29), the end of standalone Astrix license sales
  (2026-06-30), and Cisco's stated integration targets.

## Facts

### Deal closed 2026-06-29
- Cisco's original 2026-05-04 "announces intent to acquire" blog post now carries
  a dated update banner at the top, verbatim:

  > *June 29, 2026 Update: We have completed the acquisition of Astrix Security.
  > Welcome to Cisco!*

  This is Cisco's own primary confirmation of close. → `announced: 2026-05-04`,
  `closed: 2026-06-29`. This resolves the "deal close" open question and the
  soft contradiction flagged 2026-06-28 (which was correct as of that date —
  the deal genuinely had not closed yet).

### Standalone sales ended 2026-06-30
- `https://astrix.security` still resolves live under the **Astrix brand**
  (page title: "Identity Security for AI Agents & NHIs | Astrix Security"), but
  displays a prominent banner:

  > "Astrix Security is now part of Cisco. This marks an exciting new chapter,
  > bringing our AI Agent and Non-human Identity security capabilities to a
  > broader range of organizations."

  plus: **"Astrix has ended standalone sales of new licenses effective June 30th,
  2026."** Existing customers keep service and support per their current
  agreements; Astrix capabilities are to be integrated into Cisco over time.
  Customer questions route to an Astrix representative or an Astrix email alias.
- Practical read for buyers: Astrix is **no longer a buying unit**. New-license
  procurement stopped 2026-06-30; the brand and site survive as a transition
  landing page for existing customers, not as a shopping destination.

### Integration targets (Cisco's own statement)
- Cisco plans to integrate Astrix capabilities into **Cisco Identity
  Intelligence**, and extend them across **Cisco Secure Access**, **Duo Identity
  and Access Management**, and **Splunk** (agent activity feeding SIEM).
- Cisco frames the acquired capability set as four legs: discovery & governance
  for AI agents; agentic access & lifecycle management; agentic threat detection
  & response; and secrets management across multiple vaults/clouds.
- As of 2026-07-27 there is **no named Cisco product page** that has absorbed
  Astrix — no Cisco URL to point the wiki `website:` field at. Astrix's own
  domain remains the authoritative page. (Cisco's corporate-development
  acquisitions pages return HTTP 403 to automated fetches, so the Cisco-side
  acquisition listing could not be read directly; the blog update banner is the
  load-bearing primary confirmation.)

### Price
- **Not officially disclosed.** Cisco's announcement states no terms. Press
  (Calcalist/Ctech and downstream coverage) reports **~$400M**; earlier reporting
  during talks cited "up to $350M." Keep `price: null` in frontmatter and cite
  the press figure as unofficial in prose.

## Assessment

`ownership_state: acquired-pending` is stale. Correct state is
**acquired-closed**, announced 2026-05-04, closed 2026-06-29, with standalone
new-license sales ended 2026-06-30 and integration into Cisco Identity
Intelligence / Secure Access / Duo / Splunk pending. Brand and domain are
**not** yet retired — unlike the Aim/Cato or Normalyze/Proofpoint pattern.
