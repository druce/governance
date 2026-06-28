---
type: category
name: AI Red Teaming / Guardrails
slug: ai-red-teaming
layer: model-prompt
priority: day-2
trifecta_role: none-detection (red-teaming) / untrusted-input + egress (guardrails)
maps_to_seed_doc: (folded into LLM Observability "red-teaming")
maps_to_seed_csv: AI Red Teaming / Guardrails
vendor_count: 16
status: drafted
last_updated: 2026-06-28
---

# AI Red Teaming / Guardrails

## Business objective

Two related jobs the CSV survey bundles together:

- **AI red-teaming** — adversarial testing that *finds* an AI app's weaknesses
  before attackers do: automated jailbreak/prompt-injection attempts, harmful-output
  probing, data-leakage tests, scanned against your model, prompts, and RAG setup.
  It is offensive QA for AI — the pentest you run pre-production and on a schedule.
- **Guardrails** — the runtime filters that *enforce* the rules once you ship:
  input/output validators that block disallowed content, injection attempts, PII
  leakage, hallucinated or off-policy responses.

The pairing is natural: red-teaming discovers the failure modes; guardrails (and the
[[ai-runtime-security]] firewall) block them. Many vendors sell both, and the
"evaluation" half overlaps with [[llm-observability]].

## When you need it

Day-2 for most shops — you stand up the gateway, firewall, and observability first,
then add systematic red-teaming and tuned guardrails as the app matters more. It
moves earlier (toward Day-1) for higher-stakes deployments: anything customer-facing,
anything touching MNPI or client data, or anything that must pass model-risk review.
For a hedge-fund CTO, red-team reports are useful evidence for
[[ai-governance-platform]] / SR 11-7 sign-off, and lightweight OSS guardrails
(Guardrails AI, NeMo) can be adopted early at low cost.

## Lethal-trifecta role

Two modes. **Red-teaming** is detection — it doesn't block in production; it
*reveals* which legs of the trifecta your app exposes (does untrusted input reach
sensitive data? can output exfiltrate?). **Guardrails** are enforcement — they break
the **untrusted-input** leg (reject injection/jailbreak prompts) and the **egress**
leg (filter leaky or unsafe output) at runtime. Red-teaming spans all zones as a
testing activity; guardrails sit at the same red/yellow boundary as the AI firewall.

## Vendors

**Red-teaming / adversarial testing-first**
- [[mindgard]] — automated AI red-teaming / offensive security testing.
- [[splxai]] — AI red-teaming and pentest; also offers runtime guardrails (cross-listed in [[ai-runtime-security]]).
- [[promptfoo]] — open-source eval and red-team tooling (flagged acquired by OpenAI, per seed).
- [[haize-labs]] — adversarial testing / automated red-teaming research.
- [[hiddenlayer]] — model scanning plus red-teaming (primary in [[ai-runtime-security]]).
- [[enkrypt-ai]] — red-teaming plus guardrails (cross-listed in [[ai-runtime-security]]).
- [[trojai]] — model scanning and red-teaming (cross-listed in [[ai-runtime-security]]).

**Guardrails / safety-filter-first**
- [[guardrails-ai]] — open-source guardrails framework (validators for I/O).
- [[nemo-guardrails]] — NVIDIA's open-source guardrails toolkit.
- [[lakera]] — prompt-injection/guardrail detection with strong research (cross-listed in [[ai-runtime-security]]).
- [[pangea]] — AI security guardrails / API-delivered controls (flagged acquired by CrowdStrike, per seed).

**Eval-and-guardrail platforms (overlap with observability)**
- [[galileo]] — safety/hallucination guardrails and evals (flagged acquired by Cisco, per seed).
- [[patronus-ai]] — LLM evaluation and guardrails (cross-listed in [[llm-observability]]).
- [[maxim-ai]] — eval + observability + red-teaming platform (cross-listed in [[llm-observability]]).
- [[braintrust]] — eval/experimentation platform used for red-team-style testing (primary in [[llm-observability]]).
- [[giskard]] — open-source testing/red-teaming for ML and LLMs (primary in [[llm-observability]]).

## Consolidation / M&A dynamics

Heavily consolidating. Per seed flags (unverified — to confirm in research):
Promptfoo flagged as acquired by OpenAI; Lakera flagged as acquired by Check Point;
Galileo flagged as acquired by Cisco; Pangea flagged as acquired by CrowdStrike. The
pattern mirrors [[ai-runtime-security]]: platform vendors (Cisco, Check Point,
CrowdStrike) and model labs (OpenAI) are buying the red-team/guardrail specialists.
The result is that several survey options now sit inside larger security suites or
model-provider stacks.

## Adjacent categories

- [[ai-runtime-security]] — the production firewall that enforces what guardrails define and red-teaming uncovers; large overlap (HiddenLayer, Lakera, SplxAI, Enkrypt, TrojAI appear in both).
- [[llm-observability]] — shares the "evaluation" surface; eval-platform vendors (Braintrust, Giskard, Patronus, Maxim, Galileo) span both.
- [[ai-governance-platform]] — consumes red-team reports as model-risk evidence.
- [[agent-runtime-security]] — red-teaming extends to multi-step agent behavior, not just single prompts.

## Survey

**Question:** Which AI red-teaming and guardrail tools are you using or evaluating to
test AI apps for vulnerabilities and to enforce input/output safety controls?

**Answer options:** Mindgard, SplxAI, Promptfoo, HiddenLayer, Lakera, Guardrails AI,
NeMo Guardrails, Galileo, Patronus, Pangea, Maxim AI, Haize Labs, Enkrypt AI, TrojAI,
Braintrust, Giskard, Other (Please Specify).

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:**
- This category bundles two distinct jobs (offensive red-teaming vs runtime guardrails). Consider splitting into two questions — respondents using NeMo Guardrails (a filter) and Mindgard (a pentest tool) are doing different things.
- Heavy cross-listing with [[ai-runtime-security]] (HiddenLayer, Lakera, SplxAI, Enkrypt, TrojAI) and [[llm-observability]] (Braintrust, Giskard, Patronus, Maxim) will cause double-placement; lead with a definition.
- OSS options (Guardrails AI, NeMo, Promptfoo, Giskard) will skew toward "in production" via low-friction adoption; commercial red-team platforms skew "evaluating."
- M&A dates several options: if confirmed, Promptfoo→OpenAI, Lakera→Check Point, Galileo→Cisco, Pangea→CrowdStrike. Show recognizable names.

## Open taxonomy questions

- Should this split into `ai-red-teaming` (offensive testing) and `ai-guardrails` (runtime filters)? The seed CSV merged them but they serve different buyers and lifecycle stages.
- Guardrails overlap so much with [[ai-runtime-security]] that the boundary is mostly "delivered as a framework/library" (here) vs "delivered as an inline firewall product" (there). Worth a stated rule.
- This is a CSV-only cut folded out of [[llm-observability]] in the doc; confirm the split survives the final taxonomy pass.
