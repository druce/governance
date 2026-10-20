# NVIDIA OpenShell — docs: architecture and security best practices

- URL: https://docs.nvidia.com/openshell/v0.1.3/about/architecture.md
- URL: https://docs.nvidia.com/openshell/security/best-practices.md
- Fetched: 2026-10-20
- Good for: isolation mechanism, policy engine (OPA), credential placeholder model, defaults, documented limitations and footguns.

## Architecture (v0.1.3 docs; same text in v0.1.0–v0.1.3)
- Gateway: control plane — sandbox lifecycle, identity checks, state, policy/settings delivery, provider attachment, connection coordination.
- Supervisor: trusted side of boundary; evaluates requests against policy, supplies credentials, resolves DNS, opens approved connections, holds gateway link.
- Sandbox: untrusted side with the agent; launches agent, handles exec/terminal, identifies calling program; "never makes policy decisions."
- Providers map a service name to a stored credential. Policy prover runs in gateway (also standalone `openshell-prover`); flags new credentialed reach, new HTTP methods, cloud-metadata access; any finding blocks auto-approval.
- Compute drivers: Docker/Podman (supervisor in own container; workload container networking off); Kubernetes (supervisor in own pod; NetworkPolicy allowing only supervisor service); VM/MicroVM (supervisor as host process over authenticated vsock; guest has no network device). "The runtime's job is to build the boundary and prove it's in place. It never decides whether a request is allowed."
- Linux backend: workload runs as single non-root identity with no capabilities. "Landlock limits filesystem access; seccomp user notification stages network operations." seccomp intercepts TCP opens and DNS queries and hands them to the supervisor; outer network fence denies other egress.
- Auth: gateway-minted JWTs bound to one sandbox and one generation; "A new supervisor can't take over a running sandbox, even with valid credentials."; on Kubernetes the driver verifies pod ServiceAccount token before issuing JWTs; shared deployments should set gateway_jwt.ttl_secs.

## Security best practices page
- Network egress deny-by-default: "All egress denied. Only endpoints listed in `network_policies` can receive traffic." Operator approval enabled; unlisted endpoints blocked and surfaced for review.
- Network path: CONNECT proxy + OPA policy engine; each sandbox in own network namespace (veth pair; proxy at host-side 10.200.0.1) so a process ignoring proxy env vars can still only reach the proxy. Every network_policies entry requires a `binaries` list. L7 protocol inspection optional; without `protocol` only host/port/binary checked. L7 enforcement defaults to `audit` ("The proxy logs violations but forwards traffic").
- Filesystem: Landlock; mandatory baseline needs Landlock ABI 3 (Linux 6.2+); extra filesystem policy defaults to `best_effort` (hard_requirement available). Docs: investigate High-severity Landlock findings rather than treating them as supported degraded mode.
- Process: non-root, privilege drop, core-dump hardening; seccomp blocks mount, ptrace, bpf etc.; root rejected; seccomp/namespace settings not user-configurable.
- Static controls (filesystem, process) locked at sandbox creation; network and provider controls change at runtime.
- Inference: no model-provider access by default; must attach provider and allow endpoint + binary.
- Credentials: "The agent receives an opaque placeholder, not the real API key or access token." Placeholder resolves only for authorised host/port/path.
- Footguns: `tls: skip` disables placeholder rewriting, token injection and L7 inspection; `allow_uninspected_credentials` removes L7 visibility; "Approving an endpoint permanently widens the running sandbox's policy" (resets only on sandbox recreation); gateway unauthenticated mode "must not be exposed to shared or public networks"; loopback service URLs reachable by any local process; "The sandbox does not scrub application-level output"; broad binary globs such as `/**` defeat binary-scoped enforcement.
- Kubernetes: user namespaces off by default (Helm toggle); needs K8s 1.33+, containerd 2.0+ or CRI-O 1.25+; "NVIDIA device plugin compatibility with user namespaces is unverified."
