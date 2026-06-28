---
type: category
name: Security Awareness / Anti-Deepfake
slug: anti-deepfake
layer: foundation
priority: day-2
trifecta_role: none-detection
maps_to_seed_doc: Security Awareness / Anti-Deepfake
maps_to_seed_csv: AI Antiphishing/deepfake/social engineering defense
vendor_count: 5
status: drafted
last_updated: 2026-06-28
---

# Security Awareness / Anti-Deepfake

## Business objective

Defend the **human layer** against AI-era social engineering. The seed doc frames
it as **training and tripwires for AI-powered social engineering** — deepfake
voices, cloned executives on video calls, AI-written spear-phishing, and impersonated
brands/domains. The category spans two jobs that are often bought separately:
(1) the established security-awareness/anti-phishing training motion, now updated
for AI-generated lures, and (2) emerging AI-detection tooling that flags synthetic
audio, video, and images, or takes down impersonation domains and fake accounts.

## When you need it

**Day 2 — with a Day-1 caveat.** Anti-phishing training is usually already
deployed, so the *new* spend is the AI-specific detection layer, which is still an
emerging market. For a hedge fund the threat is concrete and high-stakes: a cloned
CFO voice authorizing a wire, a deepfaked partner on a Zoom call, or AI phishing
targeting traders. The exposure is acute for firms that move money on verbal/video
instruction, so some funds will pull deepfake detection forward to Day 1 for
finance and treasury workflows even while general awareness training stays routine.

## Lethal-trifecta role

Not a trifecta control at all — it defends people, not the prompt/data/egress path
of an AI application. Its job is **detection and human resilience** against
synthetic-media and AI-phishing attacks that target employees. Lives at the human
perimeter, outside the trust-zone model; included in the foundation layer because
it backstops every other control (the strongest technical stack still fails if an
employee is talked into bypassing it by a convincing deepfake).

## Vendors

- [[adaptive-security]] — AI-driven security-awareness training and simulated AI/deepfake phishing.
- [[doppel]] — digital-risk protection: detection and takedown of impersonation domains, brands, and social accounts.
- [[reality-defender]] — real-time deepfake detection across audio, video, and images.
- [[getreal]] — synthetic-media / deepfake detection aimed at enterprise comms and meetings.
- [[pindrop]] — voice authentication and deepfake-voice detection (call centers, phone channels).

## Consolidation / M&A dynamics

No specific seed M&A flags for this category. It's an emerging, fragmented space
split between two motions — awareness/training (an established market being
re-tooled for AI) and pure-play synthetic-media detection (newer, venture-funded).
Detection accuracy and false-positive rates are unproven and vendor-claimed;
expect rapid change and likely future consolidation into broader email-security,
fraud, or identity-verification platforms.

## Adjacent categories

- [[identity-access]] — strong identity/MFA reduces reliance on humans spotting fakes; deepfakes increasingly target identity-verification flows.
- [[comms-surveillance]] — both touch the comms channel, but surveillance hunts MNPI/conduct in archives rather than detecting synthetic media live.
- [[vendor-risk]] — impersonation/business-email-compromise risk overlaps with third-party trust.

## Survey

**Question:** Which AI anti-phishing / deepfake / social-engineering defense tool
does your firm use or evaluate?

**Answer options (multi-select):**
- Adaptive Security
- Doppel
- Reality Defender
- GetReal
- Pindrop
- Other (Please Specify)

**Response scale:** multi-select; Interested; Considering/evaluating;
Pilot/implementing; In production; Would recommend; Would not recommend.

**Notes for survey design:** Emerging category — expect more "Interested" and
"Considering" than "In production," and many respondents covering only the
awareness-training half via incumbents (KnowBe4, Proofpoint) that aren't on this
AI-specific list, so "Other" will be heavily used. The options span different jobs
(training vs domain takedown vs media detection vs voice auth), which may confuse
respondents — consider splitting "deepfake detection" from "AI phishing/awareness
training" if responses cluster oddly. Pindrop is voice-channel specific (most
relevant to firms with phone-based operations).

## Open taxonomy questions

- The category bundles distinct jobs: awareness training, impersonation/domain
  takedown, synthetic-media detection, and voice auth. If buyers shop these
  separately, consider splitting deepfake-detection from awareness-training.
- Incumbent awareness vendors (KnowBe4, Proofpoint, Mimecast) aren't in the seed
  list but dominate the training half; decide whether to add them or keep this an
  AI-native shortlist.
