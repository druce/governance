# Hadrius — Claude Compliance API integration (AI chat as a surveilled channel)

- URL: https://www.prnewswire.com/news-releases/hadrius-adds-claude-to-its-communications-archive-bringing-enterprise-ai-under-compliance-oversight-302835563.html + https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations (Anthropic help center, partner list)
- Fetched: 2026-08-18
- Good for: the one fact that makes Hadrius interesting to this wiki — capture of
  employee **generative-AI conversations** as a books-and-records channel.

## Facts

**Announcement 2026-07-28.** Hadrius added **Claude** to its communications archive.
Firms on **Claude Enterprise** can archive employees' Claude conversations inside
Hadrius alongside email, chat and text, with automated surveillance applied to them.

**Mechanics.** Built on **Anthropic's Claude Compliance API**. **Agentless** — no
software installed on employee devices, no change to how employees use Claude; capture
runs in the background on **Hadrius infrastructure**. Requires the **Claude Enterprise**
tier (per Anthropic, the Compliance API serves Claude Enterprise — conversation content
plus activity feed — and Claude Platform customers — activity-feed events only).

**Prior coverage.** **ChatGPT archiving was already supported** before this; the Claude
addition gives "coverage across two of the most widely used AI assistants in financial
services."

**Corroboration.** Hadrius **is named** in Anthropic's own Claude Compliance API
integration-partner list ("the agentic compliance infrastructure for SEC- and
FINRA-regulated firms"). Anthropic announced the Compliance API with 28 launch partners
on **2026-05-21**; the help-center list had grown to ~80+ partners across DLP, SASE,
SIEM, eDiscovery, AI-SPM and AI observability by 2026-08-18. **Greenboard is not on
that list** as of the same date.

**Regulatory framing (from the release).** SEC recordkeeping rules attach to any channel
where employees conduct business, whether or not the channel was built for work — so
adviser/BD use of AI assistants to draft communications and work through decisions
carries the same recordkeeping and supervision obligations as email.

**Not stated.** The release gives no retention periods, no data-handling detail beyond
"on Hadrius infrastructure," and no statement about whether archived AI conversations
are used for model training.

## Confidence

- Integration exists, is agentless, requires Claude Enterprise: **high** (vendor PR
  corroborated independently by Anthropic's own partner list).
- ChatGPT support predating it: **med** (vendor claim only, not separately verified).
