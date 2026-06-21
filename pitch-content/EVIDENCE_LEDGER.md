# Beyond Biomes — Master Evidence Ledger
### For IDEA.2026 (3-min pitch) + VC seed + laminated handout
*Synthesized from 14 source extractions. Confidence labels: **solid** (externally sourced / peer-reviewed / shipped), **estimate** (internal bottom-up), **target** (forward projection — must be spoken as such).*

> **Two governing rules carried from the locked deck + operator instructions:** (1) On stage the money stays a quiet "billions / seed round" — no TAM funnel, only farmer/producer/scientist carry the story. (2) NO patent granted, greenhouse-not-field, no field-proven yield yet — present unvalidated items as targets.

---

## 1. TOP 15 KPIs FOR STAGE / HANDOUT
Ranked by investor impact. ⚠ = must be spoken as **target/projection**, not fact.

| # | Metric | Value | Confidence | Investor relevance | Source |
|---|--------|-------|------------|--------------------|--------|
| 1 | Published nutrient mobilization (lead proof) | **+396% Mn, +309% P, +366% Si** | solid | high | Schwabe et al. 2021, *Chemosphere* (IF 8.8) |
| 2 | Producer price / gross margin | **€800/ha @ ~84% margin** ⚠ | target | high | Locked deck slide 6 |
| 3 | Model accuracy: now → target | **R² 0.68 (demo) → 0.81 (benchmark) → 0.85 (field target)** ⚠ | solid→target | high | ANNEX IX + deck slide 11 |
| 4 | Single-strain field failure vs our target | **60–70% fail → 70–85% success** ⚠ | estimate→target | high | Deck slide 5 / IP_01 |
| 5 | Agentic platform depth | **17 agents · 221 ML models · 156+ API endpoints** | solid | high | ANNEX IX, prior sessions (founder files) |
| 6 | Live demonstrator | **558k LOC · 860+ commits · 17,500 real samples · 97.1% CNN disease detection** | solid | high | ANNEX IX Platform Doc (live at review.beyondbiomes.de) |
| 7 | Signed LOIs | **5 signed** (DE 1,200-ha co-op + Chile + Brazil/7Rocks) | solid | high | LOIs annex |
| 8 | Dual-hemisphere retrain cadence | **every 6 months** (vs annual) | solid | high | Deck slide 7 / AP |
| 9 | Farmer outcome | **+20–25% yield, −30% fertilizer, 153% yr-1 ROI** ⚠ | target | high | Deck slide 6 |
| 10 | Data moat / replication barrier | **45–66 months, ~€1.3M; 625-metagenome DB across 3 climate zones** ⚠ | estimate | high | IP annex / Table A |
| 11 | Freedom-to-operate | **150+ patent families analyzed, no blockers** | solid | high | IP_03 / FTO analysis |
| 12 | Infrastructure cost (capital efficiency) | **~€30–60/month** to run the live platform | solid | high | ANNEX IX |
| 13 | Unit economics | **CLV €61.2k · CAC €8k→3.2k · CLV/CAC 7.7x→19x · payback 3.2→1.3 mo** ⚠ | target | high | ANNEX VIII p.12 |
| 14 | Revenue trajectory | **€7M ARR (GJ3) → €15M (GJ5, base), break-even M36–42** ⚠ | target | high | ANNEX VIII |
| 15 | Team credibility | **343+ citations; Ngo lead-author Nature Communications 2025; Tischler h-index 33** | solid | high | Team annexes |

---

## 2. THE ASK
**€1.5M Seed** (the stage ask) — *"€1.5M Seed buys an industry its eyes."*

**Use of funds (locked deck slide 12):**
- **40%** — producer pilots
- **30%** — the 625-metagenome field validation trial (the experiment that moves R² 0.68 → 0.85 across DE + CL + ES)
- **20%** — go-to-market
- **10%** — regulatory (EU 2019/1009 dossier)

**The full capital ladder behind it (ANNEX VIII, for Q&A — keep off stage):**
EXIST grant **€1,041,856** (non-dilutive R&D, 24 mo Oct 2026–Sep 2028: Personnel 721,135 / Material 298,221 / Incentive ~20–22.5k) → EXIST Phase II €180k → **Seed €1.5M @ €8–10M pre** → Series A €3M @ €20–25M pre → Series B €5M @ €100M pre = **~€10.5M cumulative**; founders retain ~48% through Series B. Exit: €30–50M trade sale (~10 yr) to BASF/Bayer/Corteva/dsm-firmenich.

---

## 3. BUSINESS MODEL

**Spine (deck slide 6):** Two-sided value split — **the farmer gets the benefit, the producer pays.** The producer (biostimulant maker) pays Beyond Biomes €800/ha at ~84% margin to *validate and tailor* their product; the farmer gets +20–25% yield / −30% fertilizer. Every paid field feeds the data flywheel.

**Three-customer revenue architecture (ANNEX VII):**
| Segment | ~% of revenue | What they buy | Price |
|---|---|---|---|
| **Farmers** | ~65% | Prescription card + monitoring (SaaS) | Starter €490 / Pro €850 / Enterprise €1,200 per yr; SaaS €29/mo bundled |
| **Science / Institutions** | ~20% | Premium analysis, DB access, co-publication | €299–399/sample; institute license €2k–12k/yr |
| **Producers (B2B)** | ~15% | Data license, white-label, formulation API, QC | Data license €15k–50k/yr; white-label €8–15/ha; QC €199/batch |

**White-label / Cyro Cavalcante (7Rocks):** A real biofertilizer producer in **35+ countries since 1999** committed (signed LOI Oct 31 2025) to *"integration of existing microbial products from my portfolio into the Beyond Biome recommendation system for co-validation"* and a *"joint go-to-market strategy in European and Latin American markets."* This is the producer-side white-label proof — products plug into the platform via the Open API.

**Margin engine:** gross margin climbs **66/75% → 87%** as diagnostics in-source (shotgun €213/sample → own metagenomics → qPCR panels €35/sample, i.e. 31% → 86% margin).

**Market sizing (handout/reference only — keep quiet on stage):**
- **TAM** ~€3.5B (intersection of 4 segments) — note deck states €12.5B; **reconcile (see §11)**
- **SAM** ~€150M (30,000 farms × 40 ha × 30% adoption × €800/ha)
- **SOM** €14.4–26.4M (deck: €15M @ ~375 farm-equivalents by GJ5)

**Benchmark verdict (ANNEX VIII):** B2B-SaaS scorecard **8.4/10 = Tier 1 / Series-A-ready.**

---

## 4. THE DEEP-TECH WORLD *(banker-legible)*

**The one-liner:** *"Precision medicine for the soil"* — read what the soil's microbes are actually **doing** (function, via RNA-seq), not just **who** is there, then prescribe the exact microbial mix and learn from the result. Diagnose → Prescribe → Therapy → Learn, closed loop.

**What's actually built and live** (review.beyondbiomes.de, inspectable via QR):
- A working platform: **558,000 lines of code, 860+ commits, 17,500 real soil samples, 221 trained ML models, 156+ API endpoints, 97.1% accuracy** on crop-disease photo detection.
- An **agentic layer of 17 specialized AI "agents"** — think of them as a team of digital specialists (one sequences, one assembles the genome, one profiles function, one designs the consortium). They run automatically and, for each farmer's field, assemble a **custom report + a site-specific product recipe** — effectively *a unique app per farm.*
- **Open API platform** = the plumbing that lets three outside groups (farmers, scientists, biostimulant producers) all plug into one shared brain. Producers integrate their products via the API without ever touching the secret core.
- **Local-first / closed-loop:** the heavy computing runs on the company's own cheap servers (**~€30–60/month**), not expensive cloud — so the data, and the moat, never leave the company's control, and margins stay software-like.
- **The economic trick (the moat in one sentence):** their core model predicts expensive functional-gene data (€250/sample shotgun) from cheap €15 sequencing — the cost arbitrage competitors can't match.

**Why a banker should care:** every paid field makes the prediction sharper → the next producer's product is more accurate → "fast-followers start from zero." That's a compounding data network effect, not a one-time product.

---

## 5. THE COMMUNITY-CONNECTION THESIS
*Three people stand around every field and have never been in the same conversation. Beyond Biomes connects them — and connects software to the living world.*

| Connection | Plain meaning | One concrete example |
|---|---|---|
| **Human ↔ human** (farmer ↔ producer ↔ scientist) | The platform puts all three in one loop | Scheffler the farmer sends soil → the scientist's knowledge becomes a prediction → Cavalcante the producer's product is tailored to that exact field |
| **Human ↔ agent** | A farmer talks to the system in plain language | The 10-step voice journey: farmer asks two questions, the AI answers with an R²/p-value soil verdict in his own language (DE/EN/ES) in <2 sec |
| **Agent ↔ environment** | Software observes the real field before acting | Dual-hemisphere: when it's winter in Germany the agents run a live field in Chile — "we bend time," retraining every 6 months |
| **Agent ↔ bacteria** | The AI designs living microbial consortia | RhizoGenie's NSGA-III optimizer takes 286 strategies down to ~15 optimal consortia (e.g. the ATW2 siderophore + Chilean PGPR synergy lifting biomass 18–22%) |

**Reliability credo that ties it together:** *"Eyes before muscle — build the observation layer before the autonomy layer. Never let a process grade its own work"* (the DNA-proofreading metaphor: fidelity 10⁻⁵ → 10⁻⁹).

---

## 6. PROOF & TRACTION

**Published science (solid):** Schwabe et al. 2021, *Chemosphere* (IF 8.8, 44–45 citations) — ATW2 strain **+396% Mn**, ATW4 **+309% P**, greenhouse n=5, p<0.05. This is the load-bearing peer-reviewed proof. Plus Ngo lead-author **Nature Communications 2025**.

**Field validation status (be honest):** current proof is **greenhouse (+15% biomass, p<0.05)**; field success (70–85%) and the Siderophore-Surfactin-Synergy are the **unvalidated hypotheses the seed funds** — the 625-metagenome trial across Germany / Chile / Spain. *"We fund the proof — we do not assume it."*

**Five signed LOIs** (total committed structure ~**€80k**, subcontracts ~€60k = 17.2% of equipment, under EXIST 20% cap):

| Partner | Country | Commitment |
|---|---|---|
| **Dr. Cyro Cavalcante / 7Rocks** ⭐ | BR/EU, 35+ countries | White-label B2B co-validation + joint GTM (signed 31.10.2025) |
| Matthias Scheffler | Germany | Free 1–4 ha organic oats, backed by 1,200-ha cooperative (24.09.2025) |
| Lorena Garrido | Chile | Free 1–5 ha, 6-month retrain cadence (17.10.2025) |
| USACH (Ortiz + Levican) | Chile | Field + production subcontract; core strains on-site since 2019 |
| Prof. Tischler (RUB) | Germany | Host endorsement, TRL 4-5 validation, infrastructure |

**Cyro's best verbatim quotes (handout-ready):**
- *"the full Beyond Biome pipeline — soil sampling → AI-based recommendation → microbial formulation → field application … and the integration of existing microbial products from my portfolio into the Beyond Biome recommendation system for co-validation."*
- *"I see Beyond Biome's approach as a major innovation in sustainable soil management and biofertilizer precision technology."*
- *"a strategic foundation for a joint go-to-market strategy in both European and Latin American agricultural markets."*

⚠ Cyro's signed letter is **qualitative** — all hectares/€/sample figures live only in the internal structure doc.

---

## 7. TEAM
| Member | Role | The one credibility-buying credential |
|---|---|---|
| **Dr. Ringo Schwabe** | Founder & CEO | Inventor of the method; lead author Schwabe 2021 *Chemosphere*; double doctorate; h-index 9, 268 cites; 9 yrs publicly-funded research |
| **Dr. Anna C.R. Ngo** | CSO | Lead-author **Nature Communications 2025**; 16 peer-reviewed; synthetic-consortia method (basis for the consortium optimizer) |
| **Prem K. Tiwari** | CTO | Built the 17-agent / 221-model platform; 482 commits; 6+ yrs industry MLOps (Tower Research, Elevait >95% acc @ 40k docs/day) |
| **María-Paz Flores** | CMO / CCO | Ex-founder IVAMA (120+ B2B customers); **120+ B2B agri-deals into LATAM**; trilingual bridge to USACH/SAG |
| **Reuben Rego** | Business/GTM Advisor (~5%) | CEO Code Orange Dubai; 25+ yrs Fortune-500 (Audi, Adidas, MARS); Gulf-MENA access |
| **Prof. Dr. Dirk Tischler** | Scientific Mentor (RUB) | 150+ publications, **h-index 33**; secures BSL-2 infrastructure |
| **Profs. Ortiz & Levican** | USACH partners | Field trials + extremophile screening; core strains on-site since 2019 |

⚠ Reuben Rego elsewhere appears "not yet secured (n. gef.)"; **Christopher Bohring is an unverified placeholder** — do not put on a team slide.

---

## 8. POWER-PHRASE BANK (25 best, deduped)
1. *Eyes before muscle. Read the system before you change it.*
2. *Never let a process grade its own work.*
3. *An agent you can't observe is not autonomous — it's just unsupervised.*
4. *We build the boring layer that makes the exciting layer reliable.*
5. *Like a doctor for the soil: the AI diagnoses, writes a prescription, and delivers the therapy.*
6. *Precision medicine for the soil.*
7. *Functional, not taxonomic: not WHO is there, but WHAT is missing.*
8. *Three people. One field. Never in the same conversation.* (farmer / producer / scientist)
9. *The farmer's need, the producer's pain, the scientist's idea — and we connect them.*
10. *We don't guess which strains survive — we measure the field first, then design the consortium built to survive it.*
11. *When it's winter here, we're in season there. We bend time.*
12. *Every field we read sharpens the prediction — fast-followers start from zero.*
13. *The 625-metagenome database is a growing moat — every new customer makes the AI more precise.*
14. *We fund the proof — we don't assume it.* (R² 0.68 → 0.85)
15. *€1.5M Seed buys an industry its eyes.*
16. *You cannot improve what you cannot read.*
17. *N, P, K, pH — that's chemistry, not biology. It tells you what's there, never what's missing.*
18. *No solution unites diagnosis and therapy — exactly this gap Beyond Biomes closes.*
19. *Open API ecosystem with a proprietary core.*
20. *Nature solved reliability four billion years ago — one mistake in a hundred thousand becomes one in a billion.*
21. *The first-mover window closes 2027–2028, when BASF and Bayer scale their closed-loop approaches.*
22. *Finally someone who tells me not just what's in my soil, but what to do.* — Scheffler
23. *55–58% would buy at €800/ha given university validation; without it, under 30%.*
24. *Pure analytics without a product is not a viable business model* (Trace Genomics acquired under pressure).
25. *Soil is only the first system. Build systems that build systems.*

---

## 9. BEST VISUALS FOR THE HANDOUT (ranked)
| Rank | Path | What | Why | Placement |
|---|---|---|---|---|
| 1 | `…/IP_Linked/IP_Linked/images/RS_26cycle2.jpg` *(Fig 1, closed loop)* | 5-phase Diagnose→Therapy→Learn loop | Clearest "doctor for the soil" story | Handout front, hero |
| 2 | `…/hires_2400px/IP_02_Beyond_Biomes_Platform.png` | Proprietary core + Open API → 3 customers w/ ARPUs | THE "two-worlds" fusion slide | Handout p.1 |
| 3 | `…/01_Einreichung/IP_Linked/images/qrcode.jpeg` | QR to live demo | Proof the platform is real & inspectable | Handout corner, every page |
| 4 | `…/ANNEX_IX_Platform_Documentation.pdf` p.2 | 6 hero KPI cards (558k LOC, 221 models, 97.1%) | Single strongest deep-tech credibility shot | Handout p.2 |
| 5 | `…/hires_2400px/IP_01_Labor-Erfolg.png` | Valley of Death: +396% lab vs field collapse | Strongest scientific moat / differentiation | Handout p.2 |
| 6 | `…/hires_2400px/IP_06_TAM…png` | TAM/SAM/SOM funnel with bottom-up math | Market credibility (reference, not stage) | Handout back |
| 7 | `…/hires_2400px/ANNEX_VII_06_Erlösarchitektur…png` | 3 segments × 5 revenue streams + prices | All monetization in one frame | Handout back |
| 8 | `…/ANNEX_VIII_Finanzplanung.pdf` p.12 | Unit-economics dashboard vs benchmarks | Textbook SaaS metrics bankers trust | Handout back / DD |
| 9 | `…/01_Einreichung/LOIs/Cyro_Calvacante_LOI.pdf` | Signed 7Rocks white-label LOI | Real producer in 35+ countries endorsing | Handout / appendix |
| 10 | `…/hires_2400px/IP_03…png` | 4+1 IP pillars + FTO (150+ patents, no blocks) | Defensibility for risk-focused VCs | Reference |

---

## 10. GAPS vs THE LOCKED DECK — what handout + voice MUST carry
The 12-slide deck under-shows the deep-tech half. Handout/voice must add:
1. **The agentic "app-per-farmer" layer** — the deck never states it; carry the 17-agent / persona-routing / per-field recipe story.
2. **The OpenAPI three-sided platform as architecture** — deck shows it commercially (two-sided) but not as API plumbing connecting farmer+producer+scientist.
3. **Engineering proof-of-work numbers** — 558k LOC, 860+ commits, 221 models, 156+ endpoints, 17,500 samples, 97.1% CNN — none on the slides.
4. **Live-demo capability** — deck only shows a QR; verbalize what the demo *does* (per-farmer generation, voice journey, 72-hr report).
5. **Richer team bios** — slides give one-liners; handout needs Nature Comms title, h-indices, 120+ deals, citation counts.
6. **IP / FTO specifics** — Siderophore-Surfactin PCT (filed, NOT granted), EU 2019/1009 head start, 9 yrs R&D, 45–66-mo replication barrier.
7. **Unit-economics derivation** — bridge €800/ha → ~€40k ARR/farm (hectares/farm × producers × take-rate); a banker will ask.
8. **Milestone/runway timeline** — when TRL 7 lands, burn, runway months — absent entirely.

---

## 11. OPEN QUESTIONS / NUMBERS TO RECONCILE
Pick ONE canonical value per item before printing:

1. **TAM: €12.5B (deck) vs €3.5B (IP intersection) vs €12B "market" — flagged unsourced by research dossier.** → On stage keep "billions"; in handout use the €3.5B bottom-up build (defensible) and drop €12.5B.
2. **EU crop loss €12B/yr — unattributed.** Defensible substitutes: JRC erosion €1.25B/yr; EEA/Panagos €40.9–72.7B/yr; FAO >$220B global. Say "around" / company estimate.
3. **Yield: +20–25% (deck) vs peer-reviewed 17.9% avg (commercial products only +14.4%).** → Always say "target."
4. **R²: 0.68 vs 0.81 vs 0.85** — be explicit: 0.68 demonstrator (achieved), 0.81 benchmark (achieved on EMP500), 0.85 field (target).
5. **EXIST total: ~€995k / €1,027k / €1,042k (€1,041,856)** across annexes; **personnel 693k/707k/716k/721k**; **Anreizpauschale 20k vs 22.5k**; **material 298k vs 303,221**. → Canonical = **€1,041,856** (Personnel 721,135 / Material 298,221 / Incentive ~20–22.5k).
6. **Seed ask: €750k (EXIST PoC criterion) vs €1.5M (capital plan) vs "no number" (winner script).** → Stage = **€1.5M**.
7. **Agents/endpoints/tables: 17 vs 19 agents; 96/123/156+/200+ endpoints; 48 vs 93 DB tables; 221 models vs "7 ML models."** → Canonical for pitch: **17 agents, 221 models, 156+ endpoints.**
8. **Strain count: 47+ vs 100+ isolates.** → "100+ isolates, 47+ proprietary."
9. **Codebase LOC: 558k vs 570k.** → Use **558k** (clean-repo figure from ANNEX IX).
10. **LOI sample counts: 155 vs 340 vs 625 field metagenomes; subcontracts €60k/68k/80k.** → Footnote: 625 total dataset (340 field + GH + extended); subcontracts €60k (17.2%).
11. **Team composition: 4 FTE founders, but Aryan Absalan (CTO in older LOIs) vs Prem Tiwari (CTO current); Rego "not secured"; Christopher Bohring placeholder.** → Use current 4: Schwabe/Ngo/Tiwari/Flores; advisors Rego/Tischler/Cavalcante.
12. **Status framing: NO patent (PCT filed only), greenhouse-not-field, light-not-dark theme** — confirm all handout/deck assets reflect the committed corrections (de3516fd).