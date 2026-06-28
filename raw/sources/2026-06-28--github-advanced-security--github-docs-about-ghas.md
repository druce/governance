URL: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security
fetched: 2026-06-28
Note: Primary source (GitHub Docs) — defines GHAS components and current Secret Protection / Code Security packaging.

## Key extracted text

- GHAS = suite of paid security features for organizations on GitHub Team and Enterprise plans.
- Now reorganized into two products:
  - GitHub Secret Protection: "features that help you detect and prevent secret leaks, such as secret scanning and push protection."
  - GitHub Code Security: "features that help you find and fix vulnerabilities, like code scanning, premium Dependabot features, and dependency review."
- Component features:
  - Code Scanning (SAST): uses CodeQL or third-party tools to identify vulnerabilities and coding errors.
  - Secret Scanning: detects exposed credentials/keys/tokens; AI-powered detection of unstructured secrets.
  - Dependabot: dependency analysis, vulnerability alerts, automated security updates.
  - Dependency Review: assess impact of dependency changes before merging a PR.
  - Copilot Autofix: auto-generated remediation suggestions for identified vulnerabilities.
- Code/secret scanning enabled for public repos by default; private repo access requires purchasing the relevant product.
