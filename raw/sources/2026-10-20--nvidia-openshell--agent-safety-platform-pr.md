# NVIDIA Open Agent Safety Platform press release (OpenShell + Sentry), 2026-09-28

- URL: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Open-Agent-Safety-Platform-to-Secure-Agents-From-Testing-to-Deployment/default.aspx
- URL: https://thenextweb.com/news/nvidia-open-agent-safety-platform
- Fetched: 2026-10-20
- Good for: 0.1.0-era positioning, Sentry/BlueField-4, partner roster (incl. FS names), Open Secure AI Alliance governance. Vendor press release — partner roles are NVIDIA's description.

## Press release (Santa Clara, 2026-09-28)
- NVIDIA Open Agent Safety Platform = open software platform + reference system design.
- OpenShell (available now via NVIDIA developer resources and GitHub): open-source runtime enforcing policy on agents outside the model and harness; traces agent actions; runs on NVIDIA Vera CPUs "with minimal overhead"; works across open and closed models; extensible to Arm and Intel.
- Sentry (reference design, no availability date): out-of-band watchdog on BlueField-4 DPUs built on DOCA; inspects agent requests/responses, attested telemetry, agent identity verification, zero-trust access policies; quarantines agents leaving boundaries "in milliseconds".
- Open Secure AI Alliance: initiated by NVIDIA (July 2026) with 120+ orgs, governed by the Linux Foundation; includes Shared AI Findings Exchange (SAFE). (OpenShell itself remains an NVIDIA repo.)
- Partner roles described: Anthropic (Claude Managed Agents integrate with OpenShell and BlueField to control agent access to sandboxes); SpaceXAI (Cursor coding agents, Grok); Salesforce (OpenShell ↔ Slack for viewing agent activity and approving/rejecting permission requests); SAP (embedding OpenShell in Joule Studio runtime, contributing engineering); Scale AI; Red Hat (OpenShell + DOCA on Red Hat AI Factory); Figure, Gecko Robotics, Skild AI.
- JPMorganChase named as "a financial services leader collaborating with NVIDIA on shared open-source agent safety technologies" — no statement or deployment detail. Citi also named in partner list without detail.
- Other named: Cisco, CrowdStrike, Microsoft, Palantir, Palo Alto Networks, Dell, HPE, Hugging Face, Perplexity, ServiceNow, Canonical, SUSE, Accenture, Deloitte, EY, IBM, Cognition, OpenClaw, Irregular, CoreWeave, Nebius, OCI, Together AI and others. No version numbers in release.
- TNW (2026-09-28): more than 100 organizations already using the platform per NVIDIA; OpenShell "broadly available on GitHub", tuned for Vera, runs on Arm and Intel. Secondary coverage (SecurityWeek via search) says the platform ships OpenShell 0.1.0 with a formal policy prover; supported agents include Codex, Claude Code, Pi, Hermes.
