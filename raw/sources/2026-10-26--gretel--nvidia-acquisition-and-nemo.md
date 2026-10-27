# Gretel: NVIDIA acquisition (reported), domain redirect, archived repos, NeMo successors

- URL (fetched): https://techcrunch.com/2025/03/19/nvidia-reportedly-acquires-synthetic-data-startup-gretel
- URL (search snippets): https://www.benzinga.com/25/03/44414790/nvidia-acquires-synthetic-data-firm-gretel-to-train-ai-models-report
- URL (checked via curl): https://gretel.ai -> https://www.gretel.ai/ -> 301 to https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/
- URL (fetched): https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/
- URL (API): https://api.github.com/repos/gretelai/gretel-synthetics ; https://api.github.com/repos/NVIDIA-NeMo/DataDesigner ; https://api.github.com/repos/NVIDIA-NeMo/Safe-Synthesizer
- URL (search snippets): https://developer.nvidia.com/blog/author/aligolshan/
- URL (fetched, secondary): https://testdatatools.com/en/tools/gretel-nvidia/
- URL (search snippets): https://docs.nvidia.com/nemo/microservices/latest/safe-synthesizer/about/index.html ; https://docs.nvidia.com/nemo-platform/latest/documentation/synthesize-safe-data/about
- Fetched: 2026-10-26
- Good for: Gretel ownership, what happened to the product, NVIDIA successor products.

## Acquisition (reported)
- TechCrunch 2025-03-19, citing Wired: "Nvidia has reportedly acquired Gretel"; price "said to be nine figures", above Gretel's last $320M valuation; ~80 employees to fold into NVIDIA generative-AI developer services. NVIDIA declined to comment. No NVIDIA press release found.
- Gretel: founded 2019 by Alex Watson, Laszlo Bock, John Myers, Ali Golshan (CEO); San Diego; raised >$67M (Crunchbase via TechCrunch) from Anthos Capital, Greylock, Moonshots Capital and others.
- NVIDIA author bio: Ali Golshan, senior director of AI software at NVIDIA (leads product on OpenShell; privacy/data infrastructure), "Before joining NVIDIA in 2025, Ali cofounded several startups" (Gretel among them).

## Product status
- gretel.ai and www.gretel.ai 301-redirect to an NVIDIA synthetic-data use-case page (checked 2026-10-26); console.gretel.ai and docs.gretel.ai did not respond.
- GitHub gretelai/gretel-synthetics: archived=True, last push 2025-06-24. Secondary source (testdatatools.com) says the gretelai org was archived 2026-02-18 and standalone Gretel SaaS availability is unconfirmed.
- NVIDIA use-case page (no mention of Gretel): NeMo Data Designer (synthetic data from scratch or seed data; previews, evaluation) and NeMo Safe Synthesizer ("privacy-safe versions of sensitive data", defaults intended to help meet HIPAA/GDPR).
- NVIDIA-NeMo/DataDesigner: Apache-2.0, created 2025-10-16, active (push 2026-10-26), `pip install data-designer`.
- NVIDIA-NeMo/Safe-Synthesizer: Apache-2.0, created 2026-01-20, active; "creates private, safe versions of sensitive tabular datasets -- entirely synthetic data with no one-to-one mapping"; workflow includes PII replacement, differential-privacy training, quality/privacy evaluation; needs NVIDIA GPU (A100+), Linux.
- NeMo Microservices docs banner (search snippet): NeMo Microservices retired 2026-10-01, successor "NeMo Platform"; Safe Synthesizer and Data Designer appear under "Design Synthetic Data" in NeMo Platform docs.
- Data Designer previously launched as an early preview inside Gretel Navigator (pre-acquisition). Lineage of Safe Synthesizer from Gretel's privacy/synthetics stack is asserted by secondary sources, not by NVIDIA.
