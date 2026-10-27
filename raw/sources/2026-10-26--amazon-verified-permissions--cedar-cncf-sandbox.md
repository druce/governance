# Cedar joins CNCF as a Sandbox project (AWS Open Source Blog) + CNCF project page + Cedar GitHub

- URLs: https://aws.amazon.com/blogs/opensource/cedar-joins-cncf-as-a-sandbox-project ; https://www.cncf.io/projects/cedar/ ; https://github.com/cedar-policy/cedar ; (secondary) https://infoq.com/news/2026/01/cedar-joins-cncf-sandbox/
- Fetched: 2026-10-26
- Good for: Cedar's governance (CNCF Sandbox), formal-verification claim, named adopters, license.

## CNCF project page
- "Cedar was accepted to CNCF on October 8, 2025 at the Sandbox maturity level."

## AWS Open Source Blog (2025-12-15, Lara Langdon)
- Cedar is a CNCF Sandbox project; next steps described as moving to Incubation and then Graduated.
- "AWS architected Cedar from the beginning with the vision of foundation stewardship."
- "The language specification has been formally verified using the Lean theorem prover"; the Rust implementation "undergoes differential random testing against the formal specification".
- Adopters/maintainers named: Cloudflare, MongoDB, StrongDM, Cloudinary, and AWS services including **Bedrock AgentCore Policy** and AWS Systems Manager. Linux Foundation Janssen Project integration; Kubernetes-Cedar-Authorizer (Lucas Käldström).
- Verified Permissions not mentioned in the post. No MCP mention.

## GitHub cedar-policy/cedar
- Apache-2.0. Written in Rust ("you will typically depend on Cedar via Cargo"). ~1.8k stars. "Cedar is designed for analysis using Automated Reasoning."

## InfoQ (secondary, 2026-01)
- Cedar expresses RBAC, ABAC and ReBAC concepts; architected by AWS; aims to be vendor-neutral.
