# NVIDIA Security Bulletin: NemoClaw and OpenShell — August 2026 (bulletin 5872)

- URL: https://github.com/NVIDIA/product-security/tree/main/2026/5872 (5872.md, raw fetched via raw.githubusercontent.com)
- URL: https://app.opencve.io/cve/CVE-2026-65093 (CVE record mirror)
- URL: https://cyber.gc.ca/en/alerts-advisories/nvidia-security-advisory-av26-849 (Canadian Cyber Centre AV26-849, 2026-08-26; via search)
- Fetched: 2026-10-20
- Good for: primary-source vulnerability history, affected/fixed versions. Primary source (NVIDIA PSIRT).

## Bulletin (updated 2026-08-25). "These vulnerabilities were found externally."
OpenShell CVEs — all affect OpenShell 0 to 0.0.33, fixed in v0.0.34:
- CVE-2026-65093 — OpenShell for Linux sandbox escape; CVSS 3.1 9.9 Critical (AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H); CWE-427. Credited: Leo Lin.
- CVE-2026-65083 — sandbox provisioning API, incomplete list of disallowed inputs; 9.9 Critical; CWE-184.
- CVE-2026-65091 — malicious gateway could cause OS command injection (all platforms); 8.8 High; CWE-78.
- CVE-2026-65092 — OpenShell Sandbox path traversal bypass of L7 REST network policy; 8.5 High; CWE-22.
- CVE-2026-65086 — OS command injection (exec handler per stack.watch title); fixed v0.0.34.
- CVE-2026-65085 — improper output encoding in inference proxy; medium (5.2 per aggregators); fixed v0.0.34.
NemoClaw: 12 further CVEs (65081, 65082, 65084, 65087–65090, 65096–65099, 65105), mostly OS command injection, unsigned/unchecked installer downloads, weak auth in remote-access helper, unauthenticated inference service; highest 8.1.
Remediation: clone or update from the NVIDIA/NemoClaw and NVIDIA/OpenShell GitHub repos.
