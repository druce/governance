# Inedo ProGet — SCA (vulnerability + license), SBOM, edition gating, pricing, company

- URLs:
  - https://inedo.com/proget/software-composition-analysis (fetched; VENDOR MARKETING)
  - https://inedo.com/proget/software-bill-of-materials (fetched; VENDOR MARKETING)
  - https://docs.inedo.com/docs/proget/administration/license (fetched; vendor docs — edition restrictions)
  - https://inedo.com/proget/pricing and https://blog.inedo.com/inedo/proget-pricing-changes-2024 (via search)
  - https://en.wikipedia.org/wiki/ProGet and Inedo wiki mirrors; https://craft.co/inedo (via search)
  - https://forums.inedo.com/ (via search; user reports)
- Fetched: 2026-10-24
- Good for: answering "does ProGet genuinely claim supply-chain security?" — yes: SCA, license blocking, CycloneDX SBOM, build re-analysis, though gated to paid editions.

## Extract
- **Vulnerability scanning:** scans third-party packages and Docker images against NVD and Inedo's own vulnerability database; findings scored against a Risk Profile into 1–5 categories (monitor / remediate / contain). Packages can be blocked automatically by CVE score or manual assessment.
- **License policy:** detects package licenses, shows which applications use which licenses, rules to block unwanted licenses (e.g. GPL-3), registry- or feed-level.
- **SBOM:** OWASP **CycloneDX**; import/export via UI and API; SBOMs generated at build/CI time; ProGet "routinely analyzes builds and projects, both in-flight and in production, for new vulnerabilities or unwanted licenses" and raises issues. Cites Executive Order 14028. Flags packages pulled direct from the internet instead of via ProGet. No malicious-package detection claimed on these pages. SPDX not mentioned.
- **Positioning:** Inedo pitches SCA as built into ProGet vs Sonatype, where SCA is a separate Lifecycle product; also "a free, lightweight alternative to Artifactory".
- **Edition gating (docs):** Free — no vulnerability assessments, no SBOM generation, no package compliance policies, no blocking. Basic — project vulnerability identification, build SBOMs, blocking noncompliant packages, but one shared policy, 3 rule exceptions, global (not project-scoped) assessments. Enterprise — container vulnerability scanning, full policies, advanced project compliance, HA cluster + multi-site replication.
- **Pricing (2024-08-01):** Basic $2,395/yr; Enterprise $11,995/yr; per-server annual licence incl. support. Free edition usable commercially, unlimited users.
- **Forum caveats:** packages that bypass ProGet's proxy are not scanned (unanswered thread); Python SBOM license fields sometimes "unknown".
- **Company:** Inedo, private, founded 2007, Berea, Ohio (plus Tokyo office ~2017). Products: BuildMaster (2010), ProGet (2012), Otter (2016). CEO Alex Papadimoulis (also runs The Daily WTF). No outside funding found (wiki mirrors / Craft; low-medium confidence).
