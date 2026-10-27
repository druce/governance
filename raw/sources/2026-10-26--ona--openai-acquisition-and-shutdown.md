# Ona (formerly Gitpod) — rename, Classic sunset, OpenAI acquisition, Ona Cloud shutdown

- URL: https://ona.com/stories/gitpod-is-now-ona (Johannes Landgraf, 2025-09-02)
- URL: https://www.theregister.com/2025/09/03/gitpod_rebrands_as_ona/ (2025-09-03)
- URL: https://ona.com/stories/gitpod-classic-payg-sunset (2025-09-02)
- URL: https://ona.com/stories/ona-joins-openai (2026-06-11, with closing update)
- URL: https://openai.com/index/openai-to-acquire-ona/ (403 on fetch; title confirms "OpenAI to acquire Ona")
- URL: https://ona.com/stories/anthropic-model-access-in-ona (2026-08-05)
- URL: https://ona.com/stories/ona-core-shutdown (Aaron Woods, 2026-10-13)
- URL: https://ona.com/ (homepage, fetched 2026-10-26)
- URL: https://ona.com/stories/introducing-veto-security-for-the-next-era-of-software and https://ona.com/docs/ona/guardrails/veto.md (via search summary)
- URL: https://api.github.com/repos/gitpod-io/gitpod
- Fetched: 2026-10-26
- Good for: rename date, legacy product sunset, M&A announced/closed dates, the hosted-service shutdown,
  current positioning. Mostly vendor-published (acquiree); The Register is independent coverage.

## Rename
- Ona post dated 2025-09-02: Gitpod re-founded as Ona, "mission control for software engineering agents".
  The Register covered it 2025-09-03. Components: Ona Agents, environments, guardrails (short-lived cloud
  access, command deny list, audit logs). Deployment: Ona multi-tenant cloud (US, EU) or customer AWS VPC.
- The Register: Ona requests full read/write access to GitHub repos and workflows; prompt-injection risk remains.

## Gitpod Classic sunset (post 2025-09-02)
- "Gitpod Classic will sunset on October 15th" [2025]; "Pay-as-you-go users will not be able to login or
  start new environments after October 15th." Enterprise customers on custom timelines via account managers.
  `.gitpod.yml` deprecated in favour of devcontainer.json + automations.yml. Self-hosting only on
  Enterprise ("deploy Ona entirely within their own VPC"); Free and Core hosted-only.
- The post does not mention "Flex" or "Dedicated" by name. Third-party comparison sites (morphllm.com)
  describe Gitpod Flex as the self-hosted successor (AWS first) — vendor-competitor source, low confidence.
- GitHub gitpod-io/gitpod: AGPL-3.0, not archived, but last tagged release 2022.11.3 (2023-06-05); README
  says Gitpod (Classic) no longer recommended.

## OpenAI acquisition
- 2026-06-11 Ona post "Ona is joining OpenAI": "Ona has entered into an agreement to join OpenAI as part of
  the Codex team." Terms undisclosed; subject to customary conditions incl. regulatory approvals. Until
  closing, the companies remain separate and Ona "will continue supporting customers under our existing
  commitments". Unnamed customers: "the oldest bank in the US", "one of Europe's largest pharma
  companies", "one of Asia's largest sovereign wealth funds".
- Update appended to that post: "The transaction officially closed on August 10, 2026 and Ona is now part
  of OpenAI." (Acquiree statement; OpenAI page could not be fetched to cross-check.)
- Secondary coverage (TNW, TechTimes 2026-06-13, others) agrees on 2026-06-11 announcement and undisclosed terms;
  a Notion blog's $450–500M figure is unsourced — not used.

## Anthropic model access (2026-08-05)
- Anthropic ended Ona's Ona-managed access to its models, linked to the OpenAI deal. Ona-managed Anthropic
  harness removed from Ona Cloud; automations auto-moved to nearest OpenAI model. Enterprise BYOK Anthropic
  keys still worked "today" but Ona "not confident that will remain the case"; recommends Codex harness.

## Ona Cloud shutdown (2026-10-13)
- "we will be winding down Ona Cloud on October 31, 2026." New signups already closed. Users told to push
  code and back up files; migrate to Codex Cloud (ChatGPT account; environments do not transfer).
  October payments and unused credits refunded. Page does not mention Enterprise / customer-VPC deployments.

## Homepage (2026-10-26)
- Header "Part of OpenAI". "The Enterprise software factory"; "Run background agents in the cloud";
  "Runs in your VPC with complete network control"; audit trails, scoped credentials; "kernel-level policy
  enforcement"; "Give teams one governed way to run Ona, Codex, and other agents." Contact sales only.

## Veto (vendor docs / launch post, via search)
- Kernel-level enforcement as a Linux Security Module inside the environment kernel; identifies binaries by
  SHA-256 hash, not path. Early access. Origin: Ona reported Claude Code bypassing a path-based denylist via
  /proc/self/root; a later third-party write-up reports a bypass through the ELF dynamic linker and Ona
  extending Veto to network/file/memory. Medium/low confidence on details.
