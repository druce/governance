# Chainguard — products (Containers, Libraries, VMs, Agent Skills, AI images), FS, compliance, pricing

- URL: https://www.chainguard.dev/solutions/financial-services
- URL: https://www.chainguard.dev/unchained/announcing-chainguard-libraries-for-python-malware-resistant-dependencies-built-securely-from-source
- URL: https://www.chainguard.dev/unchained/introducing-chainguard-agent-skills
- URL: https://www.chainguard.dev/unchained/chainguard-agent-skills-is-now-open-to-everyone-with-a-private-registry-to-manage-your-internal-skills
- URL: https://thenewstack.io/chainguard-launches-cpu-gpu-containers-for-ai-frameworks/
- URL: https://chainguard.dev/unchained/key-takeaways-from-chainguard-assemble-2025
- URL: https://www.chainguard.dev/pricing
- URL: https://edu.chainguard.dev/chainguard/containers/about/catalog-starter/
- URL: https://safeguard.sh/resources/blog/soc-2-and-the-hardened-software-supply-chain
- URL: https://www.ai.engineer/nyc
- Fetched: 2026-10-16
- Good for: product scope, AI angle, FS positioning, pricing posture.

## Product lines (FS solutions page, Oct 2026)
- Chainguard Containers (aka Images), Libraries, VMs, OS Packages, Actions, Agent Skills, Workspaces, Harness, Checks; Chainguard Factory (build system), Guardener, Image Directory.
- Claims: reduces CVEs in production by 98% (vendor). FIPS-certified images, daily rebuilds, SBOMs, signed artifacts. Helps with PCI DSS, NYDFS, DORA, SOC 2 (customer-compliance claim). Claims Leader in 2026 Gartner MQ for Software Supply Chain Security (vendor claim, not independently checked).
- FS segments served: G-SIBs, fintech, wealth management, PE, VC, crypto. No named FS customers on the page; featured story is Anduril (defense).

## Libraries
- Libraries (Java) launched at Assemble 2025; Libraries for Python announced 2025-05-14: Python packages rebuilt from source on SLSA L2 infrastructure, incl. wheels with native code; aimed at malware/build-and-distribution attacks (cites Ultralytics, PyTorch incidents). 13,000+ Python libraries built (blog). Vendor test: ~98% of ~3,000 known malicious packages would have been avoided.

## AI images
- CPU and GPU AI container images (PyTorch, Conda, etc.), announced Aug 2024 (The New Stack). PyTorch image FIPS-enabled, STIG-hardened (vendor).

## Agent Skills
- Announced 2026-03-17 at Chainguard Assemble (NYC): catalog of hardened AI agent skills (reviewed, permission-scoped, integrity-checked, audit trail), 1,000+ hardened community skills at launch, installed via chainctl into Claude Code, Cursor, GitHub Copilot, Gemini CLI. Later opened to all users plus private registry for internal skills; closed beta for hardening first-party skills; auto re-hardening on upstream change.

## Compliance
- Chainguard SOC 2 Type II: only third-party assertion found (Safeguard blog); Chainguard case study describes its own SOC 2 Type II prep. Trust center not fetched. Treat as unverified.
- FedRAMP: Chainguard markets images that help customers reach FedRAMP; no Chainguard authorization status found.

## Pricing
- Free Starter / Catalog Starter (beta: any five non-FIPS images; business email). Paid per-image/catalog pricing not public; rfp.wiki claims ~$19k/yr floor for a team of 10 (third-party, unverified).

## AIE NYC 2026
- Listed as Silver sponsor on ai.engineer/nyc. No Chainguard talk found on the conference schedule (2026-10-16).

## Misc
- Assemble 2025 keynote (Key Takeaways post): introduced Chainguard Libraries (Java) and Chainguard VMs, and a Datadog partnership; 300+ attendees, San Francisco.
- Autobound company feed (secondary, unverified): "Chainguard Named a CVE Numbering Authority" 2026-09-22.
- Free "Starter Images" on pricing page: select unguarded containers, no SLA, :latest only.
