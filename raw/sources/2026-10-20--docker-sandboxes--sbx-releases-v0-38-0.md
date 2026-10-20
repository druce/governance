# Docker Sandboxes (sbx) — v0.38.0 release notes, release cadence, README and licence

- URL: https://github.com/docker/sbx-releases/releases/tag/v0.38.0
- URL: https://api.github.com/repos/docker/sbx-releases (and /releases, /contents/README.md, /contents/LICENSE)
- URL: https://github.com/docker/sbx-releases/releases/tag/v0.49.1
- Fetched: 2026-10-20
- Good for: what changed in v0.38.0 and when, how stale v0.38.0 is, licence (proprietary), supported agents and install channels. Vendor-published (Docker) plus GitHub API metadata.

## Repo metadata (GitHub API, 2026-10-20)
- Repo `docker/sbx-releases` created 2026-03-03. Description: "Docker Sandboxes run AI coding agents in isolated environments on your machine or on Docker-managed cloud infrastructure". ~462 stars.
- Licence: GitHub reports "Other"/NOASSERTION. LICENSE file: "Copyright (c) 2026 Docker Inc. All rights reserved." README: "License: Proprietary — Docker Inc." The repo hosts release artifacts, not source.
- README claims: "YOLO mode by default: agents work without asking permission"; private Docker daemon for test containers; file access controls; network access control; "Works with Claude Code, Codex, Gemini CLI, OpenCode, and more". Install via Homebrew (`docker/tap/sbx`), WinGet (`Docker.sbx`), APT (`docker-sbx`, user added to `kvm` group), .deb for Ubuntu, .rpm for Rocky Linux 8, MSI for Windows. RC (`vX.Y.Z-rcN`) and nightly channels.

## Stable release dates (GitHub API published_at)
- v0.38.0 2026-08-06 (rc4 2026-08-04); v0.39.0 2026-08-19; v0.42.0 2026-09-07; v0.42.1 2026-09-07; v0.43.0 2026-09-15; v0.45.0 2026-09-21; v0.45.1 2026-09-22; v0.46.0 2026-09-28; v0.47.0 2026-10-05; v0.48.0 2026-10-13; v0.49.1 2026-10-20 (v0.49.0 skipped). Roughly weekly stable releases.

## v0.38.0 (published 2026-08-06T09:00:25Z, not a prerelease) — summary of release notes
Highlights:
- Kit spec v2: new kit authoring schema (setup, permissions, agent instructions, networking, credentials). v1 kits still load via a legacy path.
- MCP management: register remote or local MCP servers once with `sbx mcp` and reuse across supported agents and sandboxes through a built-in gateway. OAuth credentials stay on the host; organizations can govern registration and tool calls with Cedar policies. Dynamic tools `mcp-find`, `mcp-add`, `mcp-config-set`.
Networking and policy:
- `--deny-network HOST` on `sbx run`/`sbx create`; `sbx policy allow network` explains when org policy overrides a local allow; sign-in refreshes org policies in the running daemon; IP-literal destinations blocked by CIDR rules fail fast; blocked HTTPS proxy connections appear in `sbx policy log` even if TLS handshake aborted.
Secrets: service and custom secrets global by default, `--sandbox` for sandbox scope; older forms deprecated; sandbox-scoped GitHub credentials added after creation work without recreating.
Agents: Docker Agent and OpenCode sandboxes can authenticate GitHub Copilot via proxy-managed GitHub credentials; Codex sandboxes prefer stored OpenAI OAuth credentials over API keys; shared agent skills resolve symlinks.
CLI: structured startup progress; `sbx daemon restart`; `sbx inspect` lists custom secrets; workspace-volume size env var.
Packaging: Homebrew installs from stapled .dmg; Windows daemon stops during WinGet/MSI upgrades.
Security:
- Claude Desktop SSH sessions no longer expose Desktop OAuth access tokens inside sandboxes.
- Fixed destination-escape flaw in `sbx cp` copy-out: CVE-2026-17106 (GHSA-hfg8-hc9c-6c3h).
- Daemon's loopback egress proxy serves only the daemon's own traffic (other local users on a multi-user host can no longer reach the upstream proxy through it).
Bug fixes include: sandboxd hang needing SIGKILL; startup failures; host `.git/config` corruption with `includeIf` (git identity now written only to the container's gitconfig); goroutine/endpoint leak from hijacked CONNECT tunnels; PTR lookup fix.
Experimental: enterprise networking (settings-driven upstream proxy; Windows NTLM/Kerberos integrated proxy auth); NVIDIA VFIO GPU passthrough on Linux (`sbx run --gpu`); Claude Code against a local GGUF/Ollama model (`sbx run --model`).

## v0.49.1 (2026-10-20) — selected items for currency
- `sbx policy refresh` immediately refreshes policy "for example after an AI Governance change" instead of waiting for the polling interval.
- Explicit CIDR deny rules take precedence over matching domain allow rules.
- `sbx policy ls` shows `default-deny-all`; a `balanced` network policy is referenced.
- Cloud commands, `sbx move`, cloud SSH honour configured proxies including PAC.
- Daemon log size/retention settings; `browser.enabled` setting; kit signing (`sbx kit sign`, `kit.trustedSigners`, `kit.allowedSources`).
- MCP gateway code-mode tools work on Windows hosts.
