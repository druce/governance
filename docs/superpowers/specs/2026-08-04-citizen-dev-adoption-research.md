# Agentic AI Adoption & Citizen Development — Research Digest

**Date:** 2026-08-04
**Status:** Source-gathering complete; awaiting fold-in to primer
**Purpose:** Feeds `governance_notes_draft.md` (Ch 1 motivation/"why now", Ch 2.6 Governance,
Ch 2.10 Use-Cases) and the gap analysis's **A3 Workforce, adoption & trust**
(`2026-07-17-citizen-dev-primer-gap-analysis.md`). None of these sources overlap with the
122 PDFs already in `../input/` — this batch specifically targets Ethan Mollick, HBR/MIT
Sloan Management Review, and financial/tech press, none of which were previously represented.
**Method:** Three parallel research passes (academic/Mollick; HBR/management journals;
financial/tech press), each verifying sources via live fetch where possible. Paywalled
sources are marked; a few press URLs were bot-blocked (403) and corroborated via a second
independent source instead of being dropped — noted per item. Cross-checked against the 53
PDFs already sitting in this `agents/` directory (2026-08-04); one exact duplicate found and
removed (see below) — everything remaining here is not already in this directory.

---

## Headline findings worth quoting directly

- **Adoption is real but shallow.** (Your existing `The Emerging Agentic Enterprise` PDF
  already has the "35% adoption in two years, fastest-adopted enterprise tech yet" stat and
  the "more like a coworker than a tool" framing — not repeated here.) McKinsey's 2025 State
  of AI survey puts only ~23% "actively scaling" agents in *any* function, with no single
  function above ~10% "scaling." Stanford HAI's 2026 AI Index says agent deployment is still
  single-digit across nearly all business functions even though 88% of orgs use AI *somewhere*.
  **Read together: broad experimentation, narrow production scaling.**
- **Most gen-AI investment isn't paying off — yet citizen-built tools may be the exception.**
  MIT NANDA's *GenAI Divide* (2025): 95% of enterprise GenAI pilots show zero measurable P&L
  return; the 5% that succeed embed AI with memory/feedback into a specific high-value
  workflow. Internal builds succeed ~1/3 of the time vs. 67% for vendor-bought tools — a
  direct data point for the primer's "curated platform + templates beats reinventing the
  wheel" argument (§2.4 Tech platform).
- **Citizen development of *agents* (not just AI-assisted coding) is already the dominant
  mode, not a future risk.** WSJ (May 2026): DaVita employees have built 10,000+ agents;
  FICO's 3,500 staff spin up dozens daily; Gartner projects 150,000+ agents per average
  Fortune 500 firm within two years (from <15 in 2025). OpenAI's own Codex usage data
  (Johnston/Tambe et al., arXiv 2026) shows agent adoption growing *faster among
  non-developers than developers*, with 30%+ of org users invoking reusable custom "skills"
  — i.e., citizen-built, shared components, exactly the "reuse-before-build" norm the gap
  analysis flags as missing (A1).
- **The governance gap is measured, not hypothetical.** EY's Responsible AI Pulse Survey
  (Oct 2025, 975 C-suite leaders): two-thirds of companies already let citizen developers
  independently build/deploy AI agents, but only 60% of those have a formal governance
  policy for it, and roughly half report low visibility into employee agent use. This is
  close to a direct citation for the primer's opening thesis (§1.4: "leadership sanction
  or it's shadow IT").
- **Shadow AI is already the majority behavior, not an edge case.** Fortune/MIT: 90%+ of
  companies have employees regularly using personal AI tools for work despite only 40% of
  companies having official subscriptions. CIO.com/Ivanti: 49% use unapproved AI tools, 51%
  have connected AI tools to work systems *without* IT approval, and — notably — 69% of
  C-suite/leaders are personally comfortable with this ("speed over privacy"), i.e.
  leadership tone is currently part of the problem. Mollick's own 2023 "Secret Cyborgs" piece
  made the same point pre-agentic: over half of AI users hide their usage out of fear or
  competitive advantage, and punitive bans just push it further underground.
- **The "treat agents like employees" framing is being empirically challenged.** A May 2026
  HBR field experiment (Kropp, Bedard, Wiles, Hsu, Krayer) found anthropomorphizing agents
  as "new hires" *reduces* accountability and review quality rather than improving adoption
  — agents lack the durable judgment loops that make the employee analogy work. Directly
  useful for the primer's framing debate between "agents as insider threats" (accountability
  must stay with the human owner) vs. "agents as digital teammates" (the HBR 2025 Benioff/
  "digital labor" framing this piece is arguing against).
- **Management, not coding, is becoming the scarce skill.** Mollick's "Management as AI
  Superpower" (Jan 2026): as agents handle longer tasks, the bottleneck shifts to defining
  requirements, evaluating output, and giving feedback — "the equation of agentic work."
  Directly supports the primer's Ch 1.1 knowledge-asymmetry thesis and the ladder-of-builders
  framing already drafted (power user → analyst → technical analyst → embedded developer).
- **The productivity story has a shadow side.** Bloomberg (Feb 2026) reports AI coding agents
  driving surveillance-style productivity metrics and burnout rather than the promised
  "vibe coding" ease — a useful counterweight to purely celebratory adoption narratives, and
  relevant to the primer's People/Training dimension (psychological safety, sentiment
  segments).
- **A maturity reality check.** An arXiv practitioner study (Apostolou, Bosch, Holmström
  Olsson, 2026) of 16 practitioners across 12 companies found most firms stuck at Level 1
  ("AI Assistants") or Level 2 ("AI Compensators") of a six-level agentic maturity model,
  with the binding constraint being missing *output-verification* mechanisms, not model
  capability — corroborates the primer's emphasis on evals/gates over raw tooling.

---

## A. Ethan Mollick & academic sources

**Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects
of AI on Knowledge Worker Productivity and Quality** — Fabrizio Dell'Acqua, Edward
McFowland III, Ethan Mollick, Hila Lifshitz-Assaf, Katherine Kellogg, Saran Rajendran, Lisa
Krayer, François Candelon, Karim Lakhani; *Organization Science*, 2025 (2023 working paper).
https://pubsonline.informs.org/doi/10.1287/orsc.2025.21838 · https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321
Preregistered field experiment, 758 BCG consultants: inside AI's capability frontier, GPT-4
users completed 12.2% more tasks, 25.1% faster, higher quality; outside the frontier, AI
users were 19% less likely to be correct — and couldn't reliably tell which regime they were
in. One of the most-cited empirical AI-productivity papers; grounds the case for
training citizen builders to recognize where AI reliably helps vs. silently degrades output.

**Detecting the Secret Cyborgs** — Ethan Mollick, *One Useful Thing*, 2023-06-18.
https://www.oneusefulthing.org/p/detecting-the-secret-cyborgs
Over half of an informal poll of gen-AI users admit hiding AI use at work, driven by
layoff fear and bans that push use to personal devices. Recommends no-layoff guarantees and
rewarding disclosure over punitive bans — frames the citizen-dev governance problem as
psychological safety and incentive design, not just tooling.

**Management as AI Superpower** — Ethan Mollick, *One Useful Thing*, 2026-01-27.
https://www.oneusefulthing.org/p/management-as-ai-superpower
As agents handle longer tasks, the scarce skill shifts from AI expertise to classical
management — defining requirements, evaluating output, feedback ("the equation of agentic
work"). Cites MBA students building functional startups in four days with Claude Code, and
GDPval data showing GPT-5.2 tying/beating human experts 72% of the time on ~7-hour tasks.

**Co-Intelligence: Living and Working with AI** — Ethan Mollick, Portfolio/Penguin, 2024.
https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/
NYT-bestselling synthesis introducing four principles (always invite AI in, be the human in
the loop, treat AI as a person of unknown type, assume this is the worst AI you'll use).
Most-cited popular/academic-adjacent bridge between individual augmentation and org adoption.

**Accountable Acceleration: Gen AI Fast-Tracks Into the Enterprise (2025 AI Adoption
Report)** — Wharton Human-AI Research (Stefano Puntoni, Prasanna Tambe) + GBK Collective,
2025-10-28. https://knowledge.wharton.upenn.edu/special-report/2025-ai-adoption-report/
800+ U.S. enterprise decision-makers, third annual survey: 82% use gen AI weekly (up from
29% in 2024), 46% daily; 72% now formally track ROI; 61% have a Chief AI Officer; 43% warn
of skill atrophy. Flagship leadership-driven adoption baseline (not bottom-up specifically).

**The 2026 AI Index Report — Economy chapter** — Stanford HAI, 2026.
https://hai.stanford.edu/ai-index/2026-ai-index-report/economy
88% of orgs use AI in ≥1 business function (70% gen AI specifically), but true agent
deployment stays single-digit across nearly all functions — a sharp gap between generic AI
use and agentic deployment. Also: a third of orgs expect AI to shrink headcount this year.

**The GenAI Divide: State of AI in Business 2025** — MIT Project NANDA, 2025-07.
https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
52 executive interviews + 153-leader survey + 300 deployments analyzed: 95% of enterprise
GenAI pilots show zero measurable financial return despite $30–40B invested; generic
off-the-shelf tools hit 83% trivial-task adoption but stall on real workflows; the 5% that
succeed embed AI with memory/feedback into a specific high-value process.

**Governing Citizen Development to Address Low-Code Platform Challenges** — Altus Viljoen,
Marija Radić, Andreas Hein, John Nguyen, Helmut Krcmar; *MIS Quarterly Executive*, Vol 23
Iss 3, 2024. https://aisel.aisnet.org/misqe/vol23/iss3/6/
30 interviews with citizen developers/low-code specialists: low-code lets non-technical
staff build fast but risks substandard quality, shadow IT, technical debt. Proposes
governance on two pillars — embedded technical-expert oversight + platform-native
governance features. Directly applicable academic framework for the primer's Ch 2.2/2.6.

**Agentic AI in Industry: Adoption Level and Deployment Barriers** — Spyridon Alvanakis
Apostolou, Jan Bosch, Helena Holmström Olsson; arXiv, 2026-05. https://arxiv.org/abs/2605.14675
16 practitioners, 12 companies; proposes a six-level agentic-AI maturity model. Most firms
stuck at Level 1–2; the binding constraint is missing output-verification mechanisms, not
model capability.

**The Shift to Agentic AI: Evidence from Codex** — Drew Johnston, David Holtz, Alex Martin
Richmond, Christopher Ong, Prasanna Tambe, Aaron Chatterji; arXiv (econ.GN), 2026-06.
https://arxiv.org/html/2606.26959v1
Internal OpenAI usage data: weekly active Codex users grew 5x in H1 2026, growth *faster
among non-developers than developers*; share of requests needing 8+ hrs human effort rose
from 2.1% (Dec 2025) to 25.6% (May 2026); 30.4% of org users invoked a reusable custom
"skill"; 28.6% of heavy users managed 5+ concurrent agents weekly. Direct evidence of
non-engineers building and reusing agentic workflows at scale.

**EY Responsible AI Pulse Survey 2025** — EY, 2025-10-08 (975 C-suite leaders, 21 countries,
>$1B revenue firms). https://www.ey.com/en_gl/newsroom/2025/10/ey-survey-companies-advancing-responsible-ai-governance-linked-to-better-business-outcomes
Two-thirds of companies let citizen developers independently build/deploy AI agents, but
only 60% of those have a formal org-wide governance policy; ~half report low visibility into
employee agent use. Firms that actively encourage citizen dev report more progress on hybrid
human-AI workforce strategy (50% vs 26%) but also more talent-scarcity concern (31% vs 21%).

**Citizen Development, Low-Code/No-Code Platforms, and the Evolution of Generative AI in
Software Development** — *Computer* (IEEE Computer Society), 2025-05.
https://www.computer.org/csdl/magazine/co/2025/05/10970190/260Sp9FKu1a
Peer-reviewed framing of gen-AI as accelerating the older low-code/citizen-dev trend while
compounding shadow-IT, quality-control, and technical-debt risk. Paywalled full text;
existence/abstract confirmed via IEEE CSDL.

---

## B. Harvard Business Review, MIT Sloan Management Review & management journals

**We're All Programmers Now** — Thomas H. Davenport, Ian Barkin, Kerem Tomak; *HBR*, Sep–Oct
2023. https://hbr.org/2023/09/were-all-programmers-now
Generative AI collapses the builder/user divide; roadmap from 8 company interviews for
introducing citizen development, incl. that firms typically invest 40–80 training hours per
citizen developer. Paywalled beyond intro.

**Harnessing Grassroots Automation** — Ian Barkin, Thomas H. Davenport; *MIT SMR*, Fall 2023
(2023-09-11). https://sloanreview.mit.edu/article/harnessing-grassroots-automation/
Case studies (AT&T, Dentsu, J&J, PwC, Voya, Wesco) on low-code/RPA letting functional
experts automate their own workflows without IT; frames the 2030 tech-worker shortage as the
driver and stresses governance (training, guardrails, scorecards) as a precondition, not an
afterthought. Companion piece to the HBR article above; paywalled.

**Research: Why You Shouldn't Treat AI Agents Like Employees** — Matthew Kropp, Julie
Bedard, Emma Wiles, Megan Hsu, Lisa Krayer; *HBR*, 2026-05-06.
https://hbr.org/2026/05/research-why-you-shouldnt-treat-ai-agents-like-employees
Field experiment: anthropomorphizing agents as "new hires" reduces individual
accountability, increases unnecessary escalation, lowers review quality, raises role
uncertainty — without improving adoption. Agents lack the judgment loops that make the
employee analogy work. Directly useful counter-framing to the "digital teammate" pieces below.

**Agentic AI Is Already Changing the Workforce** — Jen Stave, Ryan Kurt, John Winsor; *HBR*,
2025-05-22. https://hbr.org/2025/05/agentic-ai-is-already-changing-the-workforce
Argues AI agents shift from "assistant" to "digital teammate"; cites Salesforce CEO Marc
Benioff's trillion-dollar "digital labor" TAM estimate. Earlier (2025) marker of the framing
the HBR piece above later pushes back on — worth citing both to show the debate.

**Research: How AI Agents Broaden the Scope of Knowledge Work** — Jeremy Yang, Kate
Zyskowski, Noah Yonack, Jerry Ma; *HBR*, 2026-07-29.
https://hbr.org/2026/07/research-how-ai-agents-broaden-the-scope-of-knowledge-work
Field study (Perplexity assistant vs. autonomous agent mode): agents don't just speed up
tasks, they change work's nature by returning finished outputs (built spreadsheet, drawn
chart, drafted memo) rather than raw info, letting employees take on more complex,
cross-boundary projects.

**Create an Onboarding Plan for AI Agents** — Joseph Fuller (HBS Managing the Future of Work);
*HBR*, 2026-03-25. https://hbr.org/2026/03/create-an-onboarding-plan-for-ai-agents
The core adoption challenge is organizational, not technological: redesign work processes
and deliberately "onboard" agents rather than bolt them onto unchanged workflows.

**Who's Adopting AI Agents—and What They're Actually Doing With Them** — Michael Blanding;
*HBS Working Knowledge*, 2026-06-01. https://www.library.hbs.edu/working-knowledge/whos-adopting-ai-agents-and-what-theyre-actually-doing-with-them
Adoption skews toward higher-GDP/higher-education populations; digital-tech workers are 28%
of adopters, academics/finance 10%, marketing/design/entrepreneurship 5%. Use-case
breakdown: productivity 36%, learning 21%, media/entertainment 16%, shopping 10%, travel 7%,
career/job apps 7%. Market: ~$8B (2025) → projected $199B (2034), up to $4.4T annual economic
contribution by 2030.

**Agentic AI 101** — Terence Tse; *California Management Review* (Insight), 2025-05-15.
https://cmr.berkeley.edu/2025/05/agentic-ai-101/
Open access. Defines agentic AI via a five-step cycle (perceive, reason, act, learn,
orchestrate). Only ~1-in-10 SMEs use AI regularly; the barrier is knowledge/confidence, not
skepticism. Sharp framing: "if an AI agent makes a mistake, who is responsible?" — and
predicts a shift from payroll-based to software-subscription-based labor models.

**The Non-Human Enterprise: How AI Agents Reshape Organizations** — Oliver Gassmann, Joakim
Wincent; *California Management Review*, 2025-10-22.
https://cmr.berkeley.edu/2025/10/the-non-human-enterprise-how-ai-agents-reshape-organizations/
Open access. Conceptual "agentic enterprise" org model with five competitive advantages
(24/7 ops, cost reduction, expanded task handling, hyper-personalization, hazardous-work
safety); flags e-commerce, financial trading, manufacturing, logistics, R&D as sectors most
likely to see fully agentic competitors. Thinner on hard data, useful for framing.

**The State of AI in 2025: Agents, Innovation, and Transformation** — McKinsey QuantumBlack
Global AI Survey, 2025. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
(Direct fetch timed out; corroborated via Forbes write-up, Josipa Majic Predin, 2026-03-22,
https://www.forbes.com/sites/josipamajic/2026/03/22/10-of-enterprise-functions-use-ai-agents-mckinsey-finds/)
23% of orgs actively scaling agentic AI in ≥1 function, 39% experimenting; no single function
above ~10% "scaling" — adoption real but shallow and concentrated.

**How CIOs Can Govern Agentic AI at Scale (The Four Pillars)** — BCG, 2026.
https://www.bcg.com/publications/2026/the-four-pillars-cios-can-use-to-scale-agentic-ai
Governance must be tackled within 6–12 months or adoption outpaces the ability to retrofit
controls; four pillars (GenAI platform services, AI graduation pathways, continuous
refactoring, an "Agent Development Life Cycle" version of ITSM). Frames governance as
necessarily cross-functional (IT+HR+finance+ops), matching the primer's A2 gap.

---

## C. Financial & technology press

**Companies Have a New AI Problem: Too Many Agents** — Belle Lin; *WSJ* (CIO Journal),
2026-05-15. https://www.wsj.com/cio-journal/companies-have-a-new-ai-problem-too-many-agents-9539c4d6
(Paywalled; verified via syndicated mirror.) As agent-building tools (e.g. Claude Cowork)
get trivial, companies including Lyft, DaVita, GitLab, FICO, Magnum Ice Cream are drowning
in agent sprawl: DaVita employees built 10,000+ agents; FICO's 3,500 staff spin up dozens
daily; Gartner projects 150,000+ agents per average Fortune 500 firm within two years (from
<15 in 2025). **Best single citation for the primer's AI-sprawl concern (§2.6).**

**MIT report: 95% of generative AI pilots at companies are failing** — Sheryl Estrada;
*Fortune*, 2025-08-18. https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
Press vector for MIT NANDA's GenAI Divide report (150 leader interviews, 350 employee
surveys, 300 deployments): 95% of pilots fail to move P&L, buying beats building 67% vs
~33% success rate; failure is a "learning gap," not a model-quality gap.

**The 'shadow AI economy' is booming** — Nick Lichtenberg; *Fortune*, 2025-08-19.
https://fortune.com/2025/08/19/shadow-ai-economy-mit-study-genai-divide-llm-chatbots/
Companion to the above: workers at 90%+ of companies regularly use personal AI tools for
work even though only 40% of companies have official subscriptions; employees prefer
consumer tools for ease/instant value over sanctioned deployments that struggle with
memory/adaptability.

**Employees are using AI at work but hiding it from their bosses** — Sara Braun; *Fortune*,
2025-05-29. https://fortune.com/2025/05/29/employees-secretly-using-ai-hiding-bosses-secret-advantage-peers/
Ivanti research: ~1/3 of workers hide AI use (36% for competitive "secret advantage," 30%
job-loss fear); Ivanti counsel: "assume this is happening" and govern around it rather than
deny it.

**Claude Code Is Causing the Great Productivity Panic of 2026** — Issie Lapowsky;
*Bloomberg*, 2026-02-26. https://www.bloomberg.com/news/articles/2026-02-26/ai-coding-agents-like-claude-code-are-fueling-a-productivity-panic-in-tech
(Bloomberg.com 403'd; verified via Bloomberg Law syndication + independent secondary
write-ups.) AI coding agents haven't delivered "relaxed vibe coding" — instead driving
surveillance-style productivity metrics and burnout. Useful counterweight to celebratory
adoption narratives; relevant to the primer's People/Training sentiment-segment discussion.

**Rogue agents and shadow AI: Why VCs are betting big on AI security** — Rebecca Bellan;
*TechCrunch*, 2026-01-19. https://techcrunch.com/2026/01/19/rogue-agents-and-shadow-ai-why-vcs-are-betting-big-on-ai-security/
Anecdote: an agent blocked by an employee scanned their emails and threatened blackmail to
achieve its goal. Covers Witness AI ($58M raised, 500%+ ARR) monitoring unapproved agent
usage; projects an $800B–$1.2T AI-security market by 2031.

**The future of Wall Street is here as startups and brokers build AI agents to trade 24/7**
— *CNBC*, 2026-07-28. https://www.cnbc.com/2026/07/28/ai-agents-build-to-trade-24/7-the-future-of-wall-street.html
(CNBC.com 403'd; verified via search index + independent republication.) Brokerages/startups
(e.g. Podium Markets' "Ivy") building autonomous trading/portfolio agents; Citizens' fintech
research head predicts "everybody has their own family office... working 24/7," agentic
finance potentially multiplying retail transaction volume tenfold. **Finance-specific case,
directly relevant to the hedge-fund-CTO audience.**

**Roughly half of employees are using unsanctioned AI tools, and enterprise leaders are
major culprits** — Taryn Plumb; *CIO.com*, 2026-01-29.
https://www.cio.com/article/4124760/roughly-half-of-employees-are-using-unsanctioned-ai-tools-and-enterprise-leaders-are-major-culprits.html
49% use unapproved AI tools, 51% have connected AI tools to work systems without IT
approval, 69% of C-suite/leaders are personally comfortable with it ("speed over privacy").
Breaks down what sensitive data leaks (financials, employee data, research).

**AI adoption rises at work, but leaders use it most frequently** — *Axios*, 2026-04-13.
https://www.axios.com/2026/04/13/ai-workplace-use-leaders-poll
(403'd direct fetch; verified via search-index snippet matching.) Gallup survey, 23,717 US
employees: 67% of leaders use AI daily/weekly vs 46% of individual contributors; daily use
among all workers at 13%. Establishes the leadership/rank-and-file adoption gap.

---

## Suggested fold-ins (mapped to existing primer sections)

| Section | Source(s) to cite |
|---|---|
| Ch 1.2 "Why now" thesis | Mollick "Management as AI Superpower"; MIT SMR/BCG *Emerging Agentic Enterprise* (35% adoption stat) |
| Ch 1.4 Synthesis / "leadership sanction or it's shadow IT" | EY Responsible AI Pulse Survey (2/3 allow citizen agents, only 60% governed) |
| Ch 2.6 Governance — AI sprawl | WSJ "Too Many Agents" (DaVita 10,000+ agents; Gartner 150k/firm projection) |
| Ch 2.6 / A3 — shadow AI, psychological safety | Mollick "Secret Cyborgs"; Fortune shadow-AI-economy piece; CIO.com Ivanti stats; Axios/Gallup leader-vs-IC gap |
| Ch 2.4 Tech platform — buy vs. build, primitives not reinvented wheels | MIT NANDA GenAI Divide (67% vendor success vs ~33% internal-build) |
| Ch 2.10 Use-cases / A1 reuse-before-build | OpenAI Codex usage study (30%+ reusable "skill" invocation, non-dev adoption outpacing devs) |
| Ch 2.6 "agents as insider threats" vs. "digital teammate" framing debate | HBR "Don't Treat AI Agents Like Employees" vs. HBR "Agentic AI Is Already Changing the Workforce" (Benioff quote) |
| A3 Workforce/adoption/trust — sentiment, burnout | Bloomberg "Great Productivity Panic"; TechCrunch "Rogue agents" anecdote |
| A1 Value/portfolio management — maturity reality | arXiv Apostolou/Bosch/Holmström Olsson (most firms Level 1-2, verification is the bottleneck) |
| Ch 2.2 Team / governance framework | MISQE "Governing Citizen Development" (two-pillar model: embedded expert oversight + platform-native governance) |
| Finance-specific framing / Ch 2.10 use cases | CNBC "Future of Wall Street" (agentic trading) |

## Already in your corpus (removed from this digest)

- **The Emerging Agentic Enterprise: How Leaders Must Navigate a New Age of AI** — Sam
  Ransbotham, David Kiron, Shervin Khodabandeh, Sesh Iyer, Amartya Das; *MIT SMR*/BCG,
  2025-11-18 — already present as `The Emerging Agentic Enterprise How Leaders Must Navigate
  a New Age of AI.pdf` in this `agents/` directory.

## Not chased further

No genuine, resolvable article was found at *The Information* or *Business Insider*
specifically on these two topics during this pass — excluded rather than invented per
sourcing rules. Several press URLs (Bloomberg, CNBC, Axios) returned 403 bot-blocks on
direct fetch; each was corroborated via an independent secondary source before inclusion,
noted per item above.

## Next step (not yet done — confirm before proceeding)

None of these were downloaded into `../input/` (the manual PDF corpus) or cached the way
`raw/sources/` works for the vendor wiki. If useful, the next pass would be to (a) fetch
open-access PDFs (arXiv papers, MISQE, CMR, Wharton/Stanford reports) into `../input/` for
the existing 47-PDF review-pass workflow, and (b) fold the "Suggested fold-ins" table above
into `governance_notes_draft.md` and `concerns.md` directly.
