# Beyond Biomes — CANONICAL FACTS (single source of truth for script + voice + handout)
_Distilled from EVIDENCE_LEDGER (docs) + REPO_LEDGER (measured code) + FEATURE_TREE + DEEP_ADDENDUM, with DECISIONS.md applied. Confidence: **S**=solid/sourced, **T**=target/projection (must be said as target), **E**=internal estimate._

## The one sentence
**Beyond Biomes is precision medicine for the soil — an AI-native platform that reads what soil microbes are *doing* (not just who's there), prescribes a living consortium tailored to that field, and learns from every result — built on an agentic engine that already spins up new verticals beyond soil.**

## NOW (the proven flagship) — BeyondBiomes
- **Published proof (S):** +396% Mn, +309% P, +366% Si nutrient mobilization — Schwabe et al. 2021, *Chemosphere* (IF 8.8). **Greenhouse, n=5, p<0.05.** (Field is what the seed funds.)
- **Live platform, measured (S):** 696 commits · ~890 working API endpoints (Zod-typed) · 221 ML models (17 algorithms × 13 targets) · 16 DVC pipeline stages · 15,231 samples × 9,460 ASVs · 27 dockerized agents · CNN disease detection 38 classes / 14 crops / **97.1%** (162,916 PlantVillage images) · 6 UI languages · 65 Postgres tables · ~445 React components / ~127 pages · Stripe + Google OAuth · live at **review.beyondbiomes.de**.
- **In-app voice already exists (S):** RhizoNarrator + Gemini Live (de/en/es) — the farmer talks to the system.
- **Model accuracy (S→T):** R² **0.68** demonstrator (achieved) → **0.81** benchmark on EMP500 (achieved) → **0.85** field (TARGET, what the trial funds).
- **The 7-model chain (S):** M1 functional transfer (16S→KO) · M2 qPCR imputer · M3 consortium optimizer (NSGA-III) · M4 yield predictor · M5 active learner · M6 flywheel/drift · M7 producer intelligence.
- **Honest framing:** patent **PCT FILED, not granted** (DPMA first filing in EXIST; PCT/EP deferred to seed). Field yield/success are **targets**. No published OpenAPI contract yet — ~890 working endpoints today; the formal open contract is the near-term step.

## FUTURE (the "with us" punch) — the agentic layer
- **The engine (S):** agentic-layer = **1,505 commits**, 208 Skills, 233 agent definitions, 257 enforcement hooks, 172 ADW (autonomous dev workflow) scripts. A "system that builds systems."
- **Operating loop:** voice/text idea → router → CEO agents (strategy/risk/market) → Lead agents (build) → UI agents (the app) → ADWs (test, score, self-improve, writer≠reviewer enforced) → dashboard.
- **Per-farmer app:** the layer assembles, for each field, a custom report + a site-specific product recipe — effectively a unique app per farm.
- **Multi-vertical proof (S/E):** already produced BeyondBiomes (flagship) + SCHWABE UG e-learning (€270k Yr3 @ >80% margin, ~€10k capital) + SENCE + LeadGen + **ErnieBauMEistER** (construction/Bauleiter, complete, 16 kernels). Soil is the first machine off the line; the factory makes the next.
- **Reliability credo:** *eyes before muscle · read the system before you change it · never let a process grade its own work* (DNA proofreading: 1-in-10⁵ → 1-in-10⁹). Why-now: Gartner — **>40% of agentic AI projects cancelled by 2027** (cost, unclear value, weak risk controls).

## THE FOUR CONNECTIONS (the Skool-meta thesis, with a simple example each)
1. **Human ↔ human** — farmer ↔ producer ↔ scientist in one loop. *Scheffler sends soil → the scientist's knowledge becomes a prediction → Cavalcante's product is tailored to that exact field.*
2. **Human ↔ agent** — plain-language voice journey (de/en/es); ask two questions, get an R²/p-value soil verdict in seconds.
3. **Agent ↔ environment** — software observes the real field before acting; dual-hemisphere (DE/CL/ES) retrains every **6 months**, "we bend time."
4. **Agent ↔ bacteria** — NSGA-III designs living consortia (286 strategies → ~15 optimal); the ATW2 siderophore + Chilean PGPR synergy.

## BUSINESS MODEL
- **Spine:** two-sided — **the farmer gets the benefit, the producer pays.** Producer pays ~**€800/ha @ ~84% margin (T)** to validate & tailor product; farmer gets **+20–25% yield / −30% fertilizer (T)**; every paid field feeds the flywheel.
- **3 customers:** Farmers ~65% (Diagnostik €490 / Rezept €850 / Therapie €1,200 yr; SaaS €29/mo) · Research ~20% (€299–399/sample; institute €2k–12k/yr) · Producers ~15% (data license €15k–50k/yr; **white-label €8–15/ha**; QC €199/batch).
- **White-label = Cyro Cavalcante / 7Rocks ⭐ (S):** biofertilizer producer in **35+ countries since 1999**, signed LOI **31.10.2025** — integrate his portfolio for co-validation + joint EU+LATAM go-to-market. (Signed letter is qualitative; €/ha in internal structure doc.)
- **Margin engine (E):** 29% → 86% as diagnostics in-source (shotgun €213 → own metagenomics → qPCR €35/sample).
- **Market (handout shows BOTH):** **€12.5B** broad biostimulant/soil market vs **~€3.5B** serviceable intersection (bottom-up); SAM ~€150M; SOM ~€15M @ ~375 farms by GJ5. Stage stays "billions."
- **Trajectory (T):** €7M ARR (GJ3) → €15M (GJ5, base, 50% prob); break-even **M36–42**.
- **Unit economics:** CAC ~€3k, CLV ~€32.4k, **CLV:CAC ~10:1** (conservative operating; cover figure 7.7×→19× is target).

## THE ASK
**€1.5M seed — "buys an industry its eyes."** 40% producer pilots · 30% the **625-metagenome** field-validation trial (R² 0.68→0.85 across **DE + CL + ES**, 3 climate zones) · 20% GTM · 10% regulatory.
- Behind it (Q&A only): EXIST grant **~€1.04M** (canonical €1,041,856; minor doc variance ±€60) → ladder Seed €1.5M @ €8–10M pre → Series A €3M @ €20–25M → Series B €5M @ €100M; founders retain ~48%; exit €30–50M to BASF / Bayer / Corteva / dsm-firmenich.

## MOAT & DEFENSIBILITY
- **Regulatory tailwind (S):** EU 2019/1009 — only **4 microorganism types** CE-approved → **88% of biostimulant makers excluded** (EBIC). FPR forces producers to *evidence* claims = exactly what BB sells.
- **Replication barrier (E):** **45–66 months / ≥€1.3M** to rebuild the dataset; 150+ patent families analyzed, no blockers (FTO).
- **Data flywheel (S):** every paid field sharpens the model → fast-followers start from zero. Risk register total **18.1% ("moderate")**.

## TEAM (current 4 FTE + advisors)
- **Dr. Ringo Schwabe** — Founder/CEO; inventor of the method; lead author Schwabe 2021 *Chemosphere*; 9 yrs publicly-funded R&D.
- **Dr. Anna C.R. Ngo** — CSO; lead author **Nature Communications 2025**; synthetic-consortia method.
- **Prem K. Tiwari** — CTO; built the 17-agent / 221-model platform; 6+ yrs MLOps.
- **María-Paz Flores** — CMO/CCO; ex-founder IVAMA; **120+ B2B agri-deals in LATAM**; trilingual DE/ES bridge.
- **Advisors:** Prof. Dr. Dirk Tischler (RUB, h-index 33, BSL-2 infra), Reuben Rego (GTM, Gulf/MENA), Dr. Cyro Cavalcante (7Rocks). **Do NOT list Christopher Bohring (placeholder).**

## THE PITCH APP (to fix/fold into)
- GitHub **beyondbiomes-os-pitch** = single `index.html` (822 KB) — currently OS-pitch only; **Beyond Biomes pitch missing.**
- Base **bb-pitch-show** = Next.js 14, ~2,088 LOC, port 4001; RhizoGenie as a live speech-to-speech "5th teammate"; **ElevenLabs hard-capped ≤5 uses** (why the voice is "horrible"/limited). New voice + BB pitch script fold in here.
