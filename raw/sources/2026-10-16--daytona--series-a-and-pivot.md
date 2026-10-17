# Daytona — Series A, pivot from dev environments, isolation architecture

- URL: https://pulse2.com/daytona-24-million-series-a/ (republishes the 2026-02-05 PR Newswire release; streetinsider copy 403'd)
- URL: https://latent.space/p/daytona (Latent Space podcast, "Giving Agents Computers", CEO Ivan Burazin, 2026-05-21)
- Fetched: 2026-10-16
- Good for: funding round, investors, HQ, team size, named customers; founder's own account of the
  January 2025 pivot from human dev environments to agent sandboxes; isolation tech (Sysbox);
  licence history. Podcast content is founder self-description (medium confidence).

## Series A (press release via Pulse 2.0, 2026-02-05)
- $24M Series A, led by FirstMark Capital; Pace Capital; existing investors Upfront Ventures, E2VC, Darkmode;
  strategic investments from Datadog and Figma Ventures. Matt Turck (FirstMark) joined board; Kevin Zhang (Upfront) on board.
- HQ: New York. Team: 20 people (at announcement).
- Product: "programmatic, composable computers for AI agents" — stateful sandbox configurable across CPU,
  memory, storage, GPU, networking and OS; start, pause, snapshot, fork into parallel branches.
  Targets code execution, computer use, reinforcement learning.
- Named customers: LangChain, Turing, Writer, SambaNova; "early-stage YC startups to Fortune 100".
- $1M forward revenue run rate in <3 months, doubled ~6 weeks later (company claim).
- Use of funds: compute capacity, new regions, sales/marketing. Constrained by hardware availability.
- Release does not mention the dev-environment past.
- Unverified secondary claim: total funding ~$31M incl. a $7M seed (not confirmed from primary source).

## Latent Space episode (2026-05-21)
- Daytona started ~3 years earlier as automation of human dev environments, descended from Burazin's
  earlier browser IDE Codeanywhere. Hard pivot to AI-agent sandboxes in **January 2025**, after looking
  at Devin / OpenDevin (now OpenHands) in late 2024.
- Isolation: default is Docker containers hardened with **Sysbox** ("VM-level security while staying a
  container", founder's claim); other isolation layers exist. Competitors often use Firecracker/VMs.
- Runs on **bare metal** with its own scheduler (rejected Kubernetes and Nomad); snapshots on local NVMe.
- ~60 ms single-sandbox start; 50,000 concurrent in ~75 s. Windows sandboxes feature-flagged; macOS planned.
- 74% MoM growth; largest customer ~850,000 sandboxes/day. RL/eval workloads ~50% of usage.
- Named users: Cognition, Lovable, Harvey (background agents); Harbor/Terminal Bench for evals.
- ~25 employees.
- Licence: old Codeanywhere/Daytona dev-env product Apache 2.0 open core; new sandbox product **AGPL-3.0**
  (feature-flagged Windows/GPU not in OSS).
- Billing per second of vCPU/RAM/disk; network not currently charged.
