# Bifrost — benchmark methodology, and audit logs vs request logs

- URL: https://www.getmaxim.ai/bifrost/resources/benchmarks
  + https://docs.getbifrost.ai/benchmarking/getting-started
  + https://github.com/maximhq/bifrost-benchmarking
  + https://docs.getbifrost.ai/enterprise/ (index)
  + https://docs.getbifrost.ai/enterprise/audit-logs
- Fetched: 2026-08-22
- Good for: (a) why the latency claims are unfalsifiable, (b) the difference
  between Bifrost's **request logs** (OSS) and its enterprise **Audit Logs**.

## A. Benchmark methodology — everything is a mock

Docs, verbatim: **"All benchmarks are on mocked OpenAI calls, whose latency and
payload size are mentioned in the respective analysis pages."**

The `bifrost-benchmarking` repo confirms the harness: **"run the mocker as a
stand-in provider, point the gateways at it, and drive load with benchmark.go"**,
because **"Using the mocker isolates gateway overhead from provider latency and
keeps runs free and reproducible."** The mocker has "configurable latency,
failures, and rate limits".

There is **no real provider, no real network path and no token streaming**
anywhere in the numbers.

### The headline numbers measure three different things

| Number | What it actually is | Conditions |
|---|---|---|
| **0.99 ms** Bifrost vs **40 ms** LiteLLM → **"40.4x faster"** | gateway overhead, *comparative* | against a **60 ms mock OpenAI response** |
| **1.68 s** Bifrost vs **90.72 s** LiteLLM → **"54.0x faster"** | **P99 latency**, not overhead | at 500 RPS |
| **11 µs** (t3.xlarge) / **59 µs** (t3.medium) | Bifrost-only **internal** overhead — no LiteLLM comparison | 5,000 RPS stress test, ~10 KB response payloads on t3.xlarge (~1 KB on t3.medium) |

Docs also state **"Less than 15µs added latency per request on average"** — a
fourth figure.

**The point:** the microsecond figures are internal-queue overhead from a
Bifrost-only stress run; the comparative claim against LiteLLM is ~1 ms vs 40 ms;
and "54x" is a P99 latency ratio, a different metric again. Marketing presents
them as one story. Against a 60 ms canned mock response, a ~1 ms difference is
~1.6% of one call — and with a real provider (300 ms–3 s, streaming) it is noise.

## B. Audit Logs (enterprise) are NOT the request log (OSS)

**Docs index, verbatim:** *"Immutable, timestamped audit trails for every
configuration change. SOC 2, GDPR, HIPAA, ISO 27001 friendly."*

**The audit-logs page itself** says they *"record administrative activity so
operators can review who changed what, when it happened, and which resource was
affected"* — event actions are create, update, delete, authenticate, authorize,
export, import. **Configuration and access changes. Not prompts, not responses.**

- HMAC signing: *"Configure an HMAC key so audit entries can be verified"*
  (minimum 32-byte key).
- Immutability: the page makes **no built-in immutability guarantee**. Database
  is "source of truth" governed by `retention_days` (default 365); object storage
  is a "durable archive" whose retention is "governed by your bucket's lifecycle
  rules". The only immutability mention is a *recommendation*: *"Use S3 Object
  Lock / WORM and bucket lifecycle rules to govern how long the archive is kept."*
- The audit-logs page makes **no SOC 2 / GDPR / HIPAA / ISO 27001 claim at all**.

### Contradiction between the two vendor pages

The docs **index** asserts "Immutable ... audit trails" and names four compliance
regimes. The audit-logs **detail page** guarantees no immutability and names no
regime, making WORM the customer's job via S3 Object Lock. Same vendor, same doc
set. This is a hard contradiction on a compliance-relevant property.

### Consequence for the wiki page

The artefact a fund needs for comms-surveillance-style review of *what people
asked models* is the **request log**, which the OSS build produces. The
enterprise **Audit Logs** feature is change history for the gateway's own
configuration — a different artefact answering a different question. Conflating
them is an error.
