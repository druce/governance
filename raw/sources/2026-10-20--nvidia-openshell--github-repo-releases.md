# NVIDIA OpenShell — GitHub repo, README, releases; NemoClaw README

- URL: https://github.com/NVIDIA/OpenShell (README + GitHub API repo metadata)
- URL: https://github.com/NVIDIA/OpenShell/releases (v0.1.0 notes, vm-runtime prerelease notes)
- URL: https://github.com/NVIDIA/NemoClaw (README + API metadata)
- Fetched: 2026-10-20
- Good for: licence, repo creation date, star count, release cadence and current version, platform support, VM (libkrun) runtime, NemoClaw relationship and maturity label.

## Repo metadata (GitHub API, 2026-10-20)
- NVIDIA/OpenShell: created 2026-02-24; Apache-2.0; language Rust; ~16.8k stars, ~1.8k forks; not archived; last push 2026-10-20.
- Description: "OpenShell is the safe, private runtime for autonomous AI agents."

## Releases (GitHub API)
- v0.0.116 — 2026-08-28 (daily 0.0.x cadence preceded 0.1.0)
- v0.1.0 — 2026-09-25; v0.1.1 — 2026-09-26; v0.1.2 — 2026-09-28; v0.1.3 — 2026-10-09; v0.1.4 — 2026-10-13 (latest non-prerelease)
- Tags v0.1.5-pre.4 … pre.7 exist (prereleases).
- "vm-runtime" prerelease (2026-05-06, "development build"): kernel runtime artifacts "libkrunfw + libkrun + umoci" embedded in `openshell-driver-vm`; Linux arm64/x86_64, macOS arm64.
- v0.1.0 notes include: "feat!(ci): remove daily minor release automatic workflow"; "fix(tui): replace alpha badges with version"; "feat(vm): support corporate HTTP forward proxy egress for microVM sandboxes"; "feat(build): add defaults-without-telemetry feature alias"; "feat(helm): split gateway and workspace charts"; "test: backfill coverage for OCSF logging"; "feat(ci): add Codex Security release qualification"; "feat(server): add sandbox templates".

## README (2026-10-20)
- "the safe, private runtime for fleets of autonomous AI agents"; agents can read files, install packages, call APIs and use credentials without unrestricted access to data, secrets or network; operator declares policy, OpenShell enforces.
- Components: Gateway (control plane for sandboxes, policy, access), Sandbox (where each agent runs), Supervisor.
- "Agents never see real credentials; OpenShell adds them only to requests bound for approved endpoints."
- Policy covers filesystem, network, process; providers = credentials usable only at approved endpoints; inference routing section.
- Policy changes: an advisor and a prover flag risky new access (new host with credentials, new API method) for human review before approval.
- "New in OpenShell 0.1.x: a stable release cadence, new isolation primitives, an expanded extension surface, and new APIs."
- Platforms: Linux, macOS on Apple Silicon, Windows via WSL 2 (experimental); runtimes Docker, Podman, or host virtualization; Kubernetes via Helm (CNI must enforce NetworkPolicy).
- Telemetry: anonymous, operational categories and counts; disable with OPENSHELL_TELEMETRY_ENABLED=false on the gateway.
- Licence: Apache License 2.0; software provided "AS IS".
- Current README carries no alpha/beta label (the v0.1.0 release removed "alpha badges"). Tigera (2026-07-15) described the project as alpha before 0.1.0.

## NemoClaw (GitHub API + README, 2026-10-20)
- NVIDIA/NemoClaw: created 2026-03-15; Apache-2.0; ~22.8k stars.
- "NVIDIA NemoClaw is an open source reference stack for running supported AI agents more safely inside NVIDIA OpenShell sandboxes." Adds guided onboarding, managed inference, network policy, managed integrations, OpenShell-backed state persistence, lifecycle CLI.
- Repo description: "Run agents like Hermes, LangChain Deep Agents, and OpenClaw more securely inside NVIDIA OpenShell with managed inference."
- "NemoClaw is an alpha project, so maintainers review issues ... on a best effort basis."
- NemoClaw docs (ecosystem page, via search 2026-10-20): OpenShell is the execution environment; NemoClaw is the reference stack that sets up OpenClaw inside OpenShell; OpenShell can be used alone without NemoClaw.
