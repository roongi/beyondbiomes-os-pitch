# BEYOND BIOMES — REPO EVIDENCE LEDGER

*Fused from four repo analyses: bb-clean (application, two passes), agentic-layer (meta-engine), os-pitch (the deck). All counts are measured against working trees; shallow-clone and aspirational items are flagged in §7.*

---

## 1. THE DEEP-TECH PROOF — 10 substantiated facts

Phrased so a credit committee sees *scale and engineering discipline*, and a VC sees *defensible depth*.

| # | Fact (banker + VC framing) | Value | How measured |
|---|---|---|---|
| 1 | **A real platform API surface, not a prototype** — hundreds of live, persona-segmented endpoints already serving three customer types | **~890 active backend endpoints** across 118 route modules (1,223 incl. archive) | Grep `(app\|router\|api)\.(get\|post\|put\|delete\|patch)(` across `backend/routes`, excluding `_archive` = 891 matches |
| 2 | **An industrial ML factory, not a single model** — breadth across algorithms and prediction targets | **221 ML models = 17 algorithms × 13 targets** | `backend/python/ml/train_221_models_real_data.py` docstring; corroborated by `train_221_models_comprehensive.py` |
| 3 | **A productized model chain** — diagnosis→prescription pipeline staged like a manufacturing line | **7-stage M1–M7 production chain** (functional transfer → qPCR imputer → consortium optimizer → yield predictor → active learner → flywheel → producer intelligence) | Counted `m1..m7` modules in `backend/python/ml`; each maps to a DVC train stage |
| 4 | **Reproducible, auditable data science** — the MLOps rigor regulators and acquirers ask for | **16 DVC pipeline stages** (8 analysis + 7 M1–M7 + drift detection) | `stages:` entries in `dvc.yaml` |
| 5 | **Real scientific dataset at scale** — the moat is the data, not just the code | **15,231 samples × 9,460 ASVs** (globe renders 27K+ EMP points) | `train_221_models_real_data.py` header; README cites EMP FTP 15,180 + DEMODATA |
| 6 | **Hybrid bioinformatics engine** — genuine wet-lab-grade compute, not generic SaaS | **202 Python files** (41 ML) + **211 R analysis scripts** in known dirs (496 repo-wide) | `find backend/python -name '*.py'`=202; `find backend/python/ml`=41; `find R_scripts backend/r_scripts -name '*.R'`=211 |
| 7 | **Containerized agent fleet** — multi-tier analysis automation, ops-ready | **27 dockerized agents** (tier1–tier4 + EMP downloader/merger/uploader) | `ls docker/agents` = 27 `agent_*` dirs |
| 8 | **The agentic meta-engine is substantial** — a system that builds systems, measured in real assets | **208 Skills, 233 agent defs, 257 enforcement hooks, 172 ADW scripts** | `find -name SKILL.md`; `find -path */agents/*.md`; `find -path */hooks/* -name *.py`; `find -name adw_*.py` |
| 9 | **Proven build velocity** — engineering throughput de-risks the roadmap | **~1,480 commits / 891+ merged PRs** (HEAD = merge of PR #891) | `git log HEAD` in agentic-layer shows "Merge pull request #891" |
| 10 | **Real voice + vision AI wired to live data** — not a demo stub | **8 voice-agent functions** on Gemini Live; **CNN, 38 disease classes** (178 MB keras) | `voice-agent-functions.ts` (8 tool fns); `disease_detection_service.py` class list |

**Supporting depth (bench):** 65 Postgres tables (`pgTable` count in `shared/schema.ts`); 445 React components / 110 pages; 7 UI languages; Stripe + Google OAuth live.

---

## 2. SYSTEM-THAT-BUILDS-SYSTEMS

The `agentic-layer` repo is **not** the soil app — it is the engine that *produces* apps. The operating loop (`SYSTEM-THAT-CREATES-SYSTEMS.md`):

> **voice/text idea → router brief → CEO Agents (strategy/risk/market) → Lead Agents (build tasks) → UI Agents (the app surface) → ADWs (test, score, self-improve) → dashboard.**

It runs Cole Medin's 5-pillar parallel dispatch: each task becomes a spec, runs in an isolated git worktree (its own port + database branch), gets built, then **adversarially reviewed by a different agent than the one who wrote it** ("writer ≠ reviewer" is enforced), and self-heals by updating its own rules — not just the code. It maps a *company* onto AI primitives: **Skills = employees, Resolvers = management, gBrain = 7-layer memory, API credits = capital.**

**The analogy for a non-technical juror:**

> It's a **robotic factory that builds custom machines**. You don't buy one fixed product off the shelf — you describe what you need out loud, and the factory designs, builds, stress-tests, and ships a machine tailored to you. Beyond Biomes (soil) is the **first machine off the line** — the one that's already funded, regulated, and in the field. The same factory can stamp out the next vertical, and the next.

Beyond Biomes is the **lead vertical instance**; the factory is designed to spin up further "countries" (verticals) beyond soil (13 active + 1 template today).

---

## 3. THREE-SIDED PRODUCT — what ships today

### Farmer (`ultimate-farmer-dashboard.tsx`)
- **TerraGlobe** 3D globe (11 views, 27K+ EMP sample points, mobile-optimized) with GLOBAL→PLANT→FIELD drill-down.
- **SmartPanel** 12-section accordion (Climate, Soil, Weather, Plants, Geochemical, Agricultural, Region, Risks, Microbiome, Economic, Satellite, Regulatory).
- **RhizoNarrator voice** (Gemini 3 Flash text + 2.5 Flash TTS, de/en/es) + PersistentChatBar.
- **CNN crop-disease detection** (38 classes) → recommended treatment → **Biomizer** prescription: the diagnose→prescribe→treat→learn loop.
- Backed by `farmer-dashboard-routes` (63 handlers): field data, weather polling, strain/biofertilizer recommendations. Biomizer ordering/cart/checkout.

### Producer (B2B, German UI)
- Dedicated `producer-routes`; **M7 Producer Intelligence** ML model with its own DVC train stage.
- `orders-cart-routes` + **Stripe**; subscription/tiered-access routes.
- **Strain library** ("252+ PGPB strains" — UI copy), product catalog/formulations, market-intelligence routes (8 handlers), formulation analysis + QC/batch release/viability.

### Scientist (`scientist-dashboard-v3.tsx`)
- **SciRAG suite** (data/training/hypothesis/output) — RAG over literature on pgvector.
- **Proposal Studio** (`proposal-routes`, 17 handlers) + `paper-idea` / `sciextract` literature ingestion.
- **Full bioinformatics pipeline:** QIIME2/DADA2 → PICRUSt2/FeGenie/antiSMASH → MICOM/COBRApy metabolic modeling → GNN/NSGA-III consortium design.
- **Tiered multi-agent engine** (tier1 functional/statistical/network/causal → tier2 mechanistic/spatial → tier3 ML → tier4 reporting), 27 dockerized agents.
- MLOps: DVC (16 stages), Snakemake, Airflow, drift detection, model registry, Optuna. Causal/Pareto/KEGG endpoints + branded scientist PDF reports.

---

## 4. OPENAPI PLATFORM — plain language

**What's true:** all three personas (farmer, producer, scientist) have **working, separate REST routes** — roughly **890 live endpoints** — plus a connective layer (`data-integration-routes`, `comprehensive-data-hub-routes`, `tool-bridge-routes`, `orchestrator-routes`, and unified analysis/ML/report/visualization/biofertilizer routes). Request validation is real: **Zod schemas** (`backend/schemas/api-schemas.ts`, drizzle-zod) type the inputs.

**What's aspirational:** there is **no published OpenAPI/Swagger contract** anywhere in any repo (zero `*openapi*` / `*swagger*` matches outside node_modules). The README documents only ~6 endpoints.

**The honest one-liner for the deck:** *"The plumbing that connects farmer, producer, and scientist already exists as ~890 working endpoints with typed validation. The next step is publishing it as a formal OpenAPI contract so outside developers can build on it."* That is a credible near-term roadmap item, not a fabrication — and it should be framed as **"build the contract on top of the working API,"** not "we have an open platform today."

---

## 5. PLASTIC PHRASES — the vivid lines worth keeping (or cutting)

Harvested verbatim — strong rhetoric, but several are unsubstantiated; use as *flavor*, not *proof*.

- **"The system that builds systems"** / "systems that create systems that create applications"
- **"Eyes before muscle: observe, verify against reality, then act"** — *never let a process grade its own work*
- **"An independent witness proves what actually happened"** / "every action leaves a receipt the operator never has to write"
- **"The 1000x operator"** (brand slogan; quantitatively unsubstantiated)
- **"One method, many verticals"** / "one brain: the Holding"
- **"The soil is listening"** / **"RhizoGenie, the 5th teammate"** / "the money-shot"
- **"Determinism replaces vibes"** / "Zero-Touch Engineering" / "Dark Factory / Citadelle countries"
- **"The funded, regulated wedge"** (how soil is framed inside the OS story)
- **"Read the living system, prove it, then scale it"** (closing line)
- **"KI-gestützte Pflanzendiagnose"** / "B2B-Partnerschaft — alles in einer Plattform"

**Caution words that signal layered rewrites, not distinct features:** *comprehensive / enhanced / ultimate / unified* recur as filename qualifiers (e.g. `farmer-dashboard` vs `-v2` vs `ultimate-`). Don't lean on them as feature counts.

---

## 6. PITCH-APP INTEGRATION PLAN — folding BeyondBiomes into `os-pitch`

Target: `E:\WSL\shared\pitches\_repos\os-pitch\index.html` (single 822 KB file, 540 source lines, vanilla JS, no build). Today it hard-codes **one linear 9-section OS script**; soil is a single "wedge" section (`sec-soil`, lines 262–283). There is no deck switch and no recorded audio.

**STEP 1 — Refactor to a multi-deck data model.** Replace the four parallel global arrays — `SECT` (line 390), `DUR` (391), `NAR` (392–402), `CAP` (403–413) — with a `DECKS` object:
```
DECKS = { os: {title, sections:[{id,dur,nar,cap,tone,rate,pitch}…]}, bb: {…} }
```
Move the existing 9 entries verbatim into `DECKS.os`. Author `DECKS.bb` soil-first: soil-microbiome blindness → RhizoGenie functional diagnostics → Biomizer treatment → farmer ROI → EU 2019/1009 regulatory tailwind + market size → the agentic OS as scaling engine → the OpenAPI farmer/producer/scientist platform → team/ask. Reuse `sec-soil` markup, `buildChart` (437–451), `buildFed` (452–462) as building blocks. Add a global `activeDeck`. Update every consumer: `speakIdx` (512), `gotoIdx` (513), `runIdx` (514), `startPresent` (515), and `pNext`/`pPrev` bounds (522–523) to read from the active deck.

**STEP 2 — Deck selector UI.** Add two buttons on `#login` (near line 380): "Beyond Biomes OS" and "BeyondBiomes (soil)". `enter()` (532) and the URL-bypass IIFE (538) set `activeDeck` before `init()`. Add `?deck=bb` so a QR/magic-link opens straight into the soil pitch (extends the existing `?k=` pattern). Gate section visibility with a body class (`body.deck-bb` shows `.bb-only`, hides `.os-only`) so IntersectionObservers only fire for the active deck.

**STEP 3 — New voice + recorded audio.** Add `audio/` folder beside `index.html` with `bb-0.mp3 … bb-8.mp3` (and optionally `os-*.mp3`). Add `AUDIO = { bb:[…], os:[…] }`. Rewrite `speakIdx` (512): if an mp3 exists for `activeDeck`/`pIdx`, play via one reused `HTMLAudioElement` and **advance `runIdx` on the `ended` event** instead of the fixed `DUR` `setTimeout`; else fall back to `speechSynthesis`. This replaces the robotic, browser-inconsistent Web Speech narration and fixes the desync where `DUR` cuts lines off. (Current narration is `window.speechSynthesis` only — confirmed, no mp3/ElevenLabs anywhere.)

**STEP 4 — Per-line tonalization/speed scoring.** Today every line uses one global `u.rate=1.04` (line 512), no pitch. Give each section object `tone`/`rate`/`pitch`/`emphasis`; in `speakIdx` set `u.rate`, `u.pitch`, `u.lang` from current section metadata. Add `scoreLine(text)` returning `{rate,pitch,pause}` heuristically (sentence length, `?`/`!`, ALL-CAPS, numbers) so each line auto-tonalizes. Surface as editable values in a hidden author panel toggled by `?edit=1`, written back into `DECKS`. When mp3 is used, derive `dur` from actual audio duration, not guessed seconds.

**STEP 5 — Add the platform section.** Add a `platform` section to `DECKS.bb` with a three-node SVG (Farmer / Producer / Scientist around a central "OpenAPI hub"), modeled on `buildFed` (452–462) — this tells the three-sided story the OS deck omits.

**Concrete edit list:**
- **EDIT** `index.html`: (1) lines 390–413 → `DECKS` object + `bb` deck + per-line tone/rate; (2) new `bb-*` `<section>` blocks cloning the `sec-*` pattern (199–378), gated by body deck class; (3) lines 507–512 add `AUDIO`+`activeDeck`, rewrite `speakIdx` to prefer mp3 + advance on `ended`; (4) lines 513–526 make `gotoIdx`/`runIdx`/`startPresent`/bounds deck-aware; (5) line 532 `enter()` + line 538 IIFE set `activeDeck` from toggle + `?deck=bb`; (6) deck-selector buttons in `#login` near line 380.
- **ADD** `E:\WSL\shared\pitches\_repos\os-pitch\audio\` with `bb-0.mp3 … bb-8.mp3`.
- **Ops note:** password `beyond2026` and key `Bochum-1000x` are hard-coded client-side (532–538) — fine for a demo, not security. Consider splitting `NAR`/`AUDIO` into a separate JSON to keep the 822 KB file reviewable.

---

## 7. CLAIMS TO VERIFY — drafts / aspirations, not yet proven

**Hard caveats (do not present as live fact):**
1. **No OpenAPI/Swagger spec exists** in any of the four repos. The "OpenAPI platform connecting farmer+producer+scientist" is aspirational; reframe as roadmap (§4).
2. **221 models / 15,231 samples are sourced from the training script's own docstrings.** Only ~13 model artifacts (joblib/keras/pkl) are committed in the working tree — the full 221 are presumably produced by DVC runs, not present. Verify before quoting "221 trained models" as shipped.
3. **Commit/velocity claims rest on external context.** bb-clean is a **shallow clone with 1 commit** — the ~695-commit history is *not* in the clone. agentic-layer's git log is flattened to 1 commit in the export, though HEAD references merged PR #891. The "~1,480 commits / 891 PRs" needs the live repo to confirm.
4. **Not local-first.** Depends on cloud Gemini/Anthropic + cloud Postgres (Supabase/Neon). Any "local-first compute" claim is unsupported (CLAUDE.md only *negates* Ollama: "NO Ollama").
5. **Marketing-derived numbers** — "252+ strains," "168 visualizations," "7 ML models," "44+ Python agents," "27K samples" — come from UI copy/docs, not all independently verified in the checkout. Use the *measured* numbers in §1 instead.

**Pitch KPIs that are presentation targets, not repo-substantiated facts** (from `bb-pitch-show` / os-pitch narration):
- **317% pilot ROI**, **47M sequences**, **€15M ARR yr5**, **+20–25% yield at −30% fertilizer** (named farmer "Matthias Scheffler"), **R²=0.85** prescription target.
- The os-pitch live "receipt/witness" simulation and "1000x" multiplier are **scripted animation**, not a real agent runtime.
- "The demand is already speaking / the market is naming our gap" (sec-proof) is asserted from **informal builder feedback**, not a measured market signal.

**Maturity / operational risks worth a one-line disclosure:**
- Much of the BB scientific stack in agentic-layer (metagenomes MLops engine, RhizoGenie integrator, simulations) is **seeded as idea YAMLs / planned**, not executable. `bb-pitch-show` README calls itself a **v1 skeleton** (Three.js viz, ROI calc, climate map still stubs).
- **Thin automated test coverage:** ~58–70 test files vs 445 components / 118+ active route modules; no committed coverage report; verification is manual Playwright against a single VPS.
- **Single-VPS fragility** (`review.beyondbiomes.de`, port 5001, kill-by-PID deploy via `deploy-webhook.cjs`) — no CI/CD container orchestration for the main app.
- **Multi-tenant licensing constraint:** agentic work runs on **one operator's Claude Max OAuth** subscription; ToS limits it to a single human, so serving multi-tenant traffic through the bridge requires switching to metered API — a real scaling cost.
- **Inconsistent AI-provider story:** CLAUDE.md says "NO Claude Sonnet," yet Anthropic SDK, OpenAI SDK, `claude-agent-sdk.ts` and `anthropic.ts` are all present.
- **Heavy duplication / dead code:** `_archive` route dir, `index-broken.ts`, `schema-backup.ts`, `farmer-dashboard` vs `-v2` vs `ultimate-`, rhizogenie v1/v2/v3 — maintenance/diligence risk.

**Relevant file paths:** application repo `E:/WSL/shared/pitches/_repos/bb-clean`; agentic meta-engine `E:/WSL/shared/pitches/_repos/agentic-layer`; pitch deck `E:\WSL\shared\pitches\_repos\os-pitch\index.html`.