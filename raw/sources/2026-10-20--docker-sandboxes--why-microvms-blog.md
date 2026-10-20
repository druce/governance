# Why MicroVMs: The Architecture Behind Docker Sandboxes (Docker blog)

- URL: https://www.docker.com/blog/why-microvms-the-architecture-behind-docker-sandboxes/
- Fetched: 2026-10-20
- Good for: launch timing, hypervisor per OS, rationale vs containers/Firecracker/WASM, supported agents, standalone licensing. Vendor marketing/engineering blog.

- Published 2026-04-16; authors Srini Sekaran (Principal PMM, AI) and Craig Gumbley (Senior Software Engineer).
- Says Docker Sandboxes launched "last week" -> launch in the week before 2026-04-16 (exact date not given). (A third-party page says "released in March 2026"; the release repo was created 2026-03-03. Treat launch date as approximately March–April 2026.)
- Each agent session runs in a dedicated microVM with a private Docker daemon; "each sandbox gets its own kernel".
- Custom-built VMM using native hypervisors: macOS Hypervisor.framework; Windows Hypervisor Platform; Linux KVM. Firecracker rejected because no native macOS/Windows support.
- Containers rejected because agents that build containers need Docker-in-Docker with elevated privileges. WASM/V8 isolates rejected as not OS-level isolation.
- Supported agents named: Claude Code, Codex, OpenCode, GitHub Copilot, Gemini CLI, Kiro, Docker Agent, OpenClaw, NanoClaw.
- "Individual developers can install and run Docker Sandboxes today, standalone, no Docker Desktop license required." Central filesystem/network policy for teams via Docker sales.
- No performance benchmarks given.
- Secondary: Arm install guide (learn.arm.com/install-guides/sbx/) says sbx not available on Arm Linux; on Apple Silicon it launches Arm Linux microVMs.
