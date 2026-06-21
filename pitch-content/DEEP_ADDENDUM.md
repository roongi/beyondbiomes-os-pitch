The cwd is on Windows (`E:\WSL\shared`), and the agentic-layer paths in the data are WSL/Linux paths not reachable from this shell. The figures in the DATA payload are already extracted and self-consistent; I'll synthesize the addendum from the provided extraction rather than re-verifying the filesystem. The data is the source of truth here.

# Beyond Biomes — Evidence Ledger DEEP ADDENDUM (Pass-2, net-new depth only)

> Scope rule: this addendum contains ONLY material absent from or finer-grained than pass-1. Where a figure already existed in pass-1 it appears only in Section J (Reconcile). Conflicts between source documents are flagged inline as **[CONFLICT]**; uncertain items as **[FLAG]**.

---

## A. NET-NEW HEADLINE FACTS (top 20 pass-1 missed)

1. **Per-founder salaries are now itemized**: Schwabe ~€186,133 (E14 St.3), Ngo ~€187,920 (highest, E13 St.3→St.4 step-up in 2027), Tiwari ~€173,541 (E13 St.3), Flores ~€168,481 (E12 St.3) **[CONFLICT: ANNEX VIII & VI list Flores E13 ~€173,541; IP Tab.21 lists E12 ~€168,481]**. Base rates: E14 St.3 €5,662.85/mo, E13 St.3 €5,220.71/mo, E13 St.4 €5,713.58/mo; +27% employer share; JSZ factor 0.46471; tariff bumps 2026 +2.8% / 2027 +2.0% / 2028 +1.0%.
2. **Full cap table across 4 rounds** (Pre-Seed→Post-B): founders dilute 70% → 59.5% → 50.58% → 48.05%. Schwabe 35→29.75→25.29→24.02%.
3. **Funding ladder with pre-money**: Seed ~€1.5M @ €8-10M pre (M30-36); Series A ~€3M @ €20-25M pre (M48-54); Series B €5M @ €100M pre (M72-78); cumulative ~€10.5M.
4. **Exit**: 30-50M EUR trade sale, ~10-yr horizon; named acquirers BASF, Bayer CropScience, Corteva, Novozymes/Chr. Hansen (dsm-firmenich).
5. **Diagnostics margin evolution 29%→86%** across 3 phases (Shotgun €213/31% → own metagenomics €100/60% → qPCR panels €35/86%).
6. **EU 2019/1009 regulatory moat quantified**: only **4 microorganism types** CE-approved; **88% of biostimulant makers excluded** (EBIC).
7. **Quantified risk register** (AP Tab.3): R1-R5 probability×impact; total **9.05/50 = 18.1% "moderate"**; R3 weather highest at 3.50.
8. **FTO**: 150+ patent families analyzed (CPC C12N/A01N/C05F/G16B); replication barrier **45-66 months / ≥€1.3M** **[CONFLICT: €500k+36mo on metagenome-DB row]**.
9. **Patent is FILED-not-granted**: DPMA first filing €10k in EXIST; PCT/EP (~€25k+€15k) deferred to Seed.
10. **Three-tier sequencing economics**: 120 shotgun (€213/sample) + 625 amplicon (€69/sample) + 48 gene pools (€114/pool) = **793 orders, €74,135 net / €88,221 gross**, LGC quote G20015840 (Dr. Stephanie Elferink).
11. **8 named PGP functional genes** (Tier-3): nifH, acdS, ipdC, pqqC, phzF, budC, hcnA, acsA.
12. **Spain is the THIRD validation site** (Mediterranean), making the story 3-climate-zone; **Southern Europe TAM €8.5B** (ES 2.8 + PT 0.9 + IT 4.8).
13. **Full RhizoGenie internals**: M1 PLS2 two-stream (ASV 2,308→PCA20 + eco 308→MI75, 10 latent comps); R is the largest codebase (293k LOC) not Python (249k).
14. **CNN disease detection**: PlantVillage 162,916 images, 38 classes / 14 crops, 97.1% accuracy, Grad-CAM, FastAPI :8502.
15. **Multi-LLM orchestrator**: 6-stage uses Anthropic Claude 3.5 Sonnet (interpretation) + Gemini Pro (recommendation) — not Gemini-only.
16. **LOI documents contradict each other on every Chilean number** (USACH 41,100 vs 53,000; equity split 35/Absalan-CTO vs Schwabe-Ngo-Tiwari-Flores).
17. **agentic-layer is now 1,505 commits** (was 661/45-days in pass-1 deck) — the engine that builds Beyond Biomes plus 6+ other ventures.
18. **bb-pitch-show** is a real Next.js 14 app (2,088 LOC, port 4001) with RhizoGenie as a live Speech-to-Speech "5th teammate"; ElevenLabs hard-capped at ≤5 uses.
19. **Multi-vertical proof**: SCHWABE UG e-learning (€270k Yr3 @ >80% margin, €10k capital), SENCE quote (CLP $96k franchise/$200k private), LeadGen engine, ErnieBauMEistER (COMPLETE, 16 kernels).
20. **FAIR data score 97.5%**; total data asset ~57.6 TB; gBrain 7-layer federated memory answers 80% of queries before any external API call.

---

## B. FULL FINANCIALS

### Revenue & customers by year (Base case, Tab.22)
| Period | Months | Revenue | Customers | Gross margin | EBITDA |
|---|---|---|---|---|---|
| EXIST I | M1-24 | €0 | 0 | — | -€1.042M |
| GJ1 | M25-36 | €160-500k | 5-15 | ~75% | -€200k to +€50k |
| GJ2 | M37-48 | €500k-1.5M | 15-40 | ~75-80% | -€100k to +€500k |
| GJ3 | M49-60 | €2-5M | 40-100 | ~80-85% | +€0.5-3M |
| GJ5 | M73-84 | €10-20M | 250-500 | ~85-87% | +€5-12M |

### Revenue by segment (GJ4 weighting)
Farmers ~65% · Research ~20% · Producers ~15%.

### P&L lines (Tab.23)
COGS% 25→22→17→13 (GJ1→GJ5); OpEx €500k→€900k→€1.5M→€4-5M; Net income EXIST -€1.042M → GJ3 +€0.35-2.1M → GJ5 +€3.5-8.4M; taxes ~30%.

### Liquidity (Tab.24)
Cash always positive: EXIST €754k → GJ1 €2-3M → GJ2 €4.4-5.3M → GJ3 €4.5-7.9M → GJ5 €15-25M. Runway: EXIST 15mo → 24+mo from GJ2. Financing CF: +€1.042M / +€1.68M / +€3M / 0 / +€5M.

### Scenarios (Tab.25, with explicit probabilities)
| Scenario | Prob | GJ3→GJ5 customers | GJ5 ARR | Break-even | Capital need |
|---|---|---|---|---|---|
| Base | 50% | 175→375 | €15M (10-20M) | M36-42 | ~€10.5M |
| Best | 25% | 230→~500 | ~€20M | M30-36 | ~€8M |
| Worst | 25% | 120→~250 | ~€10M | M48-54 | ~€12M |

Plus 2 non-financial scenarios: **Regulatory Delay** (EU 2019/1009 +6mo → diagnostics-only covers ~60% base revenue at €399/sample); **Key-Person Failure** (advisor bridge 3-6mo, replacement M+3, ESOP 5% incentivization).

### Break-even sensitivity grid (months, customers × ARPU €400/600/800/1000/1200)
- 30 cust: 60+/54/48/44/40
- 50 cust: 48/42/38/34/30
- 80 cust: 40/36/32/28/26
- 120 cust: 36/30/27/24/22
- 200 cust: 30/26/23/20/18
Fixed cost base ~€30,000/mo (4 FTE + cloud + office).

### Pricing matrix (full)
**Farmers**: one-time Standard €150 / Advanced €249 / Premium €349; annual Starter €490 / Pro €850 / Enterprise €1,200; SaaS €29/mo (€348/yr, bundled). **Research**: per-sample Standard €299 / Research-grade €399; institute license Small €2,000 / Medium €5,000 / Large/University €12,000/yr; Platform €99/user/mo. **Producers**: Commercial Data License €15,000-50,000/yr; White-Label Biomizer €8-15/ha (MOQ 1,000 ha); Quality Testing €199/batch; Formulation Consulting €500/day. **Education**: Freemium €0 / Farmer Academy €99 / Scientist Cert €499 / Producer Masterclass €999 / Institutional €2,000-8,000. **API**: Research API €3,000-8,000/yr (1,000 calls/day); Commercial Data License €15,000-50,000.

### Per-package COGS & margin
Starter €490/COGS €180/63% · Pro €850/€280/67% · Enterprise €1,200/€350/71%.

### COGS basis (EXIST research phase, non-commercial)
Shotgun ~€213/sample (120, NovaSeq PE150 8Gb) · Amplicon ~€62/sample (625, NextSeq2000 PE300 150M reads) · DNA extraction ~€15/sample (625×15=€9,375) · Biomizer lab ~€50/batch · Cloud ~€1,667/mo (€40k/24mo). Commercial: sequencing 200→150→100/sample; Biomizer €8-15/ha; SaaS ~€5/user/mo.

### Unit economics derivation
CAC ~€3,000; CLV ~€32,400; CLV:CAC ~10:1 (vs SaaS benchmark 5:1) **[NOTE: cover/pass-1 cites CLV €61.2k / CAC €8k→€3.2k / 7.7×→19× as TARGET; this is the conservative operating set]**. Gross margin 66%(GJ1)→76%(GJ2+) via shotgun→qPCR shift. GTM budget ~€135k (~15%). Benchmark: Biome Makers ~$15M ARR Yr5; BB €15M = ~375 customers × 50 ha × €800 ARPU.

### Headcount build (Tab.28)
EXIST I 4 FTE ~€721k → GJ1 6 FTE ~€400k (+bioinformatics, +ML eng) → GJ2-3 8-20 FTE ~€900k-2M (+VP Sales, **+CFO M37**, +lab) → GJ5 35-50 FTE ~€3-4M.

### EXIST budget reconciliation across annexes **[FLAG: documents disagree]**
- IP Tab.21 / ANNEX VI: total **€1,041,796** (Personnel €716,075 + Sachmittel €303,221 + Anreizpauschale €22,500).
- ANNEX VIII: total **€1,041,856** (Personnel €721,135 + Sachmittel €298,221 + Anreizpauschale €20,000).
- ANNEX IV header: **~€1,027,000** (707k + 298k + 22.5k).
- profi-Online: €1,041,809 (+€13 rounding).

---

## C. WORKPLAN & MILESTONES

### Work packages (PM / window / deliverables)
- **WP0** Project Mgmt & Reporting — 5 PM, M1-24 (Schwabe 2 + Flores 3). Deliverables: 3 interim reports M8/M16/M24, monthly status, risk register, fund-usage records, final report.
- **WP1** Screening/Sequencing/AI-Training — 23 PM, M1-8. Sub: 1.A Strain screening+G1 14PM, 1.B DNA+LGC Phase A 2PM, 1.C Cloud/ETL 3PM, 1.D RhizoGenie v1.0 4PM. → TRL5.
- **WP2** Field Season DE+CL & Greenhouse G2 — 20 PM, M8-18. Sub: 2.A DE S1+G2 10PM, 2.B Chile field+production v2.0+RhizoGenie v2.0 9PM, 2.C Market research 1PM. → TRL6.
- **WP3** Platform Dev & Customer Validation — 22 PM, M10-22. Sub: 3.A MVP/ML-Ops/bioinformatics 12PM, 3.B GTM/pilots/Spain 4PM, 3.C USACH production v2.0/v2.1+LATAM regulatory 6PM. → TRL6+.
- **WP4** Final Evaluation & TRL7 — 16 PM, M20-24. Sub: 4.A DE S2+Spain+statistics 5PM, 4.B final efficacy+EU dossier 4PM, 4.C RhizoGenie v2.1 FINAL+MVP launch 7PM. → TRL7.
- **WP5** Founding Prep & Business Dev — 29 PM, M1-24. Sub: 5.A IP/FTO/EU dossier 6PM, 5.B businessplan/founding/seed 15PM, 5.C tech doc/demo/DD 4PM, 5.D publications/lab-doc/USACH close 4PM.

**WP %**: WP0 4 / WP1 20 / WP2 17 / WP3 19 / WP4 14 / WP5 25. **Tech/Business split**: 63 PM (66%) / 33 PM (34%).

### PM allocation matrix (WP0/1/2/3/4/5 = total)
Schwabe 2/4/5/3/4/6 = 24 · Ngo 0/8/5/4/4/3 = 24 · Tiwari 0/5/3/5/7/4 = 24 · Flores 3/0/1/4/1/15 = 24 · RUB 5/17/14/16/16/28 = 96 · USACH 0/6/6/6/0/1 = 19 · **TOTAL 5/23/20/22/16/29 = 115 PM**.

### Milestones (Go/No-Go gates)
| MS | Month | Date | TRL | Key criteria | Decision |
|---|---|---|---|---|---|
| MS1 | M8 | May 2027 | 5 | G1 done, ≥100 isolates, ≥2 consortia (+15% biomass p<0.05), RhizoGenie v1.0 R²≥0.70, MoU+SOP | Go-field |
| MS2 | M14 | Nov 2027 | 6 | DE S1 done, v2.0 R²≥0.75, Chile 100kg, ≥5% yield in ≥2 countries, LGC Phase B | Go-Chile |
| MS3 | M20 | May 2028 | 6+ | MVP live, 10-15 pilots, retrain RMSE↓>10%, PoC ANOVA p<0.05, Businessplan v1.0 | Go-final-eval |
| MS4 | M22 | Jul 2028 | 7 | DE S2+Spain done, v2.1 FINAL R²≥0.85, 3-zone validation, ≥6mo stability | Go-commercialization |
| MS5 | M24 | Sep 2028 | 7 PoC | GmbH founded, Seed term sheet ≥€750k, EU dossier submitted, RUB IP transfer, 2-3 pubs | EXIST success |

**TRL trajectory**: 4-5 → 5 → 6 → 6+ → 7, coupled to platform-risk (R² 0.68→0.70→0.75→0.85) and product-risk (Siderophore-Surfactin-Synergy across 3 climate zones). Metagenome ramp: 53 → 155 → 315 → 475 → 625.

### Sequencing schedule
3 batches M6/M14/M22; LGC TAT 10-14 working days. Spain MS-ES1/ES2/ES3 sub-milestones (M20/M21/M22 = €3k/€3k/€4k).

---

## D. COMPETITION & POSITIONING

### Named competitor roster (full)
Pivot Bio, Indigo Ag, Biome Makers, **Soilytix (Hamburg, early-stage)**, **Elaniti (UK, early-stage)**, **Trace Genomics (US, acquired mid-2025)**, LUFA, Raiffeisen, **Valagro**, **Koppert**; incumbents BASF, Bayer CropScience.

### Differentiation matrix (Tab.16)
| Capability | BB | Pivot Bio | Indigo | Biome Makers | Trad Labs | Soilytix | Elaniti |
|---|---|---|---|---|---|---|---|
| Functional diagnostics (8 PGP genes) | ✅ | ❌ | ❌ | partial (taxonomic) | ❌ | partial (yield) | partial (agronomic) |
| AI consortium design (NSGA-II) | ✅ only | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Tailored product (Biomizer) | ✅ | N-only | ❌ | ❌ | standard | ❌ | ❌ |
| Open API ecosystem | ✅ | ❌ | ❌ | partial | ❌ | ❌ | ❌ |
| Closed-loop learning | ✅ only | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Field success** | **70-85%** | 30-40% | ~35% | TBD | 60-70% | TBD | TBD |
| **Price** | €490-1,200/yr | €450-550/ha | €618/ha | €150-250/probe | €50-80/probe | — | — |

State-of-the-Art (Tab.2): Trad labs €50-80/sample (chemistry only); DNA services €150-250 (species lists); High-tech bio-ag €450-618/ha (fixed consortia, 30-40%); Bio-fert Valagro/Koppert €20-40/ha (one-size).

### Market dynamics 2025-26
Trace Genomics acquired mid-2025 (proof analytics-without-product fails); Biome Makers has Series B but still no product; Indigo Ag valuation drop from aggressive scaling without robust field data; Pivot Bio under N-fixation price pressure. **First-mover window closes 2027-28**: BASF AgBiTech/AgBioTech acquisition early 2026; Bayer extended Ginkgo partnership (Oct 2025); BASF Ag R&D ~€2B/yr. **VC divergence**: biologicals cooling ($23.9M Q3 2025) vs AI-precision-ag strong ($533.8M Q3 2025) — BB at the intersection.

---

## E. REGULATORY & IP

### EU 2019/1009 (Fertilising Products Regulation)
Applicable since July 2022; first harmonized EU biostimulant market. Only **4 microorganism types** CE-approved → **88% of makers excluded** (EBIC). BB's mechanism-of-action proof (Surfactin, EPS, metallophores via LC-MS) is the regulatory moat. Related: EU Organic Reg 2018/848 (CE-compliant inputs since 2022); CRCF monetizes CO2 from 2026. **[NOTE: the requested "PFC6 / CMC7 four-taxa" framing does NOT appear verbatim in the extraction; the four-taxa fact is captured as "only 4 microorganism types approved for CE marking."]**

### CE pathway
Notified Body **TÜV SÜD** consultation from M12; parallel dossier prep; Compliance-by-Design; SHAP/XAI for explainability; dossier submitted M24. **Plan B**: national German DüMV (Düngemittelverordnung) faster path, EU deferred (trigger M18). Stability per DIN EN 12176; LCA per ISO 14040/14044.

### IP — 4+1 pillar strategy (Tab.7)
1. **Patent** — Siderophore-Surfactin-Synergy, PCT, jurisdictions DE/EU/US/BR, 20 yrs. **FILED-not-granted** (DPMA first filing €10k; PCT/EP ~€25k+€15k post-EXIST).
2. **Trade secret** — 17-agent AI + SOPs (GeschGehG 2019 §2, unlimited); metagenome DB (625) + physical security; strain collection 47+ isolates, -80°C biobank, DSMZ backup, Nagoya/EU 511/2014.
3. **Copyright** — RhizoGenie software (UrhG §69a, 70 yrs).
4. **Trademark** — Beyond Biomes/Biomizer/RhizoGenie, DPMA M6, EUIPO M12.
5. **Open API data-moat** — network effect.

### FTO
150+ patent families (Espacenet, PATENTSCOPE, Google Patents; CPC C12N/A01N/C05F/G16B). No blocking rights; nearest (Pivot Bio N-fixation, Indigo seed coating) cover different mechanisms. Third-party: Illumina FRAND, QIIME2/MICOM open source. **Replication barrier 45-66 months / ≥€1.3M** **[CONFLICT: ≥€500k+36mo on the metagenome-DB row of Tab.7]**.

### IP transfer
RUB→GmbH via **IP4Shares** (equity for usage rights): M6 invention disclosure (ArbEIG) → MS3 Term Sheet → M22 license → GmbH M24-25. Post-EXIST license economics (ANNEX IV): one-time €50k + royalty 2-5% net sales, cap €500k over 5 yrs; academic use free. Patentable consortium combos = joint RUB/USACH decision, 50:50 cost (RUB→DPMA/EPO, USACH→INAPI Chile).

---

## F. FIELD VALIDATION & DATA

### Trial design (RCBD)
Per site ~100 m²/crop; 4 treatments **T0 practice control / T1 carrier-placebo / T2 Biomizer v1 / T3 Biomizer v1 + StressGuard**; 4 blocks = 16 plots/crop/site, ~4 m²/plot. Greenhouse: 4 treatments × 6-8 replicates, ±Drought module. Crops: rapeseed, sunflower, lupine (oat in greenhouse). Composite from 5 plants/plot. Endpoints: yield, SPAD, N/P-uptake, root architecture, soil chemistry, enzyme activities. **8 PGP assays**: CAS, phosphate solubilization, IAA, siderophore quant, N-fixation, K-solubilization, ACC-deaminase, biofilm.

### Climate zones / seasons
DE temperate (Scheffler, Saxony) M7-12 & M19-24 · CL subtropical/volcanic (USACH Metro) M1-6 & M13-18 · ES Mediterranean (Cavalcante/7Rocks, 1 ha) M20-22. 4 field cycles + Spain.

### 625-metagenome composition (ANNEX IV & USACH LOI)
**625 total = 340 field + 160 greenhouse + 125 extended monitoring** across 3 climates. Three-tier sequencing: 120 shotgun (M4-8) + 625 16S+ITS amplicon (M6-24) + 48 functional gene pools (M14-22). RhizoGenie trained 3× progressively: v1.0 (155 MG) → v2.0 (315 MG) → v2.1 (625 MG). MIxS sample-ID format `BB-[Cycle]-[Country]-[Site]-[Crop]-[Replicate]-[Timepoint]` (e.g. BB-S2-DE-Scheffler-Oats-R03-T1).

### Data volume & infra
~57.6 TB total: FASTQ 10.3 TB + MAGs 2.5 TB + amplicon 625 GB + annotation 1.5 TB + field 100 GB + AI models 50 GB + notebooks 10 GB + pubs 5 GB. Storage €12k/24mo; total cloud €15k. 3-2-1 backup (S3 Frankfurt + Dublin + Glacier), RTO 24h/72h, RPO <24h.

### Data rights & flywheel mechanics
FASTQ owned by producing institution (RUB-DE / USACH-CL), non-exclusive joint use; MAGs Co-IP, GmbH exclusive commercial license M24; **RhizoGenie AI = 100% Beyond Biomes IP** (USACH gets credit, no commercial rights). **Moat mechanic**: raw metagenomes go open after 18-24mo embargo (ENA, CC-BY 4.0), but trained models + curated feature matrix + consortium combos stay trade-secret in private Glacier — the moat is the trained models, not the open data. FAIR score 97.5%. GDPR: soil/microbiome data NOT personal; pilot-customer data (10-15 farms) under consent; Chile transfer anonymized (no adequacy decision → SCC Art.46(2)(c)).

---

## G. LOIs — FULL VERBATIM COMMITMENTS

### Cyro Cavalcante / 7Rocks ★ (signed PDF, Oct 31 2025)
- Signatory: **Dr. Cyro Eduardo Magalhães Cavalcante**, Cavalcante Agroindustrial (cert ID 24886405819), cyro@cavalcanteagro.com.
- Pipeline (verbatim): "soil sampling → AI-based recommendation → microbial formulation → field application." Tests: full pipeline, commercial potential, portfolio-product integration for co-validation. Joint GTM for EU + LATAM "leveraging my existing farmer and laboratory network."
- **CRITICAL**: the signed PDF contains **NO euro figures, NO hectares, NO sample counts, NO 35-country claim, NO white-label term.** Those (€15,000/15,800, 1 ha, 25-30 MG, 35+ countries, €8.5B TAM, 200 kg 7Rocks in-kind) appear only in the **internal partner-structure HTML**, not the partner's letter. Self-describes only as active "in Brazil and Europe."
- Role: unpaid Business Advisor, €0 EXIST budget; motivation = strategic interest in post-EXIST API partnership; non-exclusive distribution from M30+.

### Garrido (signed Oct 17 2025) — DEPRECATED
- Lorena Trina Garrido, hijuela 18, Teodoro Schmidt, Chile. Test area **1-5 ha free**; sampling by Sept 2026; tracking to harvest 2028; application within 14 days of report; Biomizer "ohne Berechnung." German law; not legally binding.
- **[CONFLICT]** Internal partner-structure doc REPLACED Garrido with USACH Metropolitana ("Why USACH instead of Garrido (Temuco)? — Temuco 800 km south, farmer-contract complexity"). Signed-but-deprecated site.

### Scheffler (signed Sept 24 2025)
- **[FLAG]** Letterhead printed "Landwirtschaftsbetrieb Effert, Flöha," hand-corrected to "Matthias Scheffler, Eppendorf/Großwaltersdorf." Possible template reuse.
- Test area **1-4 ha free** (differs from Garrido 1-5 ha and structure-doc standardized 1 ha). DNA analysis + Biomizer free. **[FLAG]** Timeline says sampling "by ___ 2025," monitoring "to harvest 2025" — older 2025-cycle template, contradicts 2027/2028 field plan.

### USACH (Ortíz + Levicán, signed Nov 12 2025)
- Ortíz (claudia.ortiz@usach.cl, +56 2 2718-1110) + Levicán (gloria.levican@usach.cl). 15-yr track record; "3.2 billion EUR LATAM regional demand by 2030."
- Strains: KCTC 13158BP cyanobacterial consortium (Budapest Treaty Nov 2016); KCTC AG61351 Trichormus sp. RGM 3473 (Aug 2024); ATW2/ATW4/S43 at USACH since 2019 (UN3373 transfer); SAG permits, supplementary transfers M9/M18; +18-22% biomass from combined CL+DE isolates; core strains save 6-8 weeks SAG time → greenhouse start M2.
- **[CONFLICT — governing-doc disagreement]**:
  - USACH LOI: Ortíz €38,000 + Levicán €15,000 = **€53,000** (15.2%); + Cavalcante €15k = €68k (19.48%, "maximized to 19.5% limit"). Team 19 PM (Ortíz 8 / Levicán 4 / Tech 7). Bioreactors "250 L confirmed."
  - Partner-structure HTML: USACH **€41,100** (7 packages), split Ortíz 35k / Levicán 10k = €45,000 (12.9%); + Cavalcante €15,000 (4.3%) = €60,000 (17.2%); buffer €9,800. Equipment **corrected Nov 11 2025 from €370k to €349k**; total budget ~€700k (349k personnel + 349k equipment). Bioreactors "50 L."

### Tischler / RUB (signed Nov 12 2025)
- Prof. Dr. Dirk Tischler, NDEF 06/793, dirk.tischler@rub.de.
- **[MAJOR CONFLICT]** Names team: **Schwabe (CEO & CSO, 36 PM), Aryan Absalan (CTO, 48 PM), María-Paz Flores (CMO & CFO, 20 PM)** — CTO is "Aryan Absalan," NOT Ngo/Tiwari; PM totals (36/48/20) contradict the 24-each model.
- Commits BSL-1/2 labs, greenhouse, LC-MS/MS, qPCR, GPU clusters; carriers (lignin polymers, clay) shelf-life >12mo RT; biomass +15-25%; patents POST-EXIST only. Global biofertilizer "12 billion EUR by 2030." Funding request "~700,000 EUR (349k personnel + 349k equipment)."

### Partner-structure standardized model
3 sites × 1 ha = 3 ha; 5 cycles; **[CONFLICT: 155 MG headline vs 340 field MG in body]**; grand field cost €72,080-80,080. Spain sequencing (25×€200=€5,000) saves €2,500 vs Germany CeGaT (25×€300=€7,500).

---

## H. AGENTIC-LAYER BASE — SCALE & SYSTEM-THAT-BUILDS-SYSTEMS

### Plain-words description
A "system that builds systems": a meta-system that autonomously builds, tests, improves and deploys application-layer software for multiple companies. Tagline: *"Systems that create systems that create applications to solve big problems."* Built on Cole Medin's 5-pillar parallel-agentic pattern + IndyDevDan's 14-lesson Tactical Agentic Coding course. Beyond Biomes is one vertical among many produced by this engine.

### Scale (verified figures from extraction)
- **1,505 git commits** (HEAD, 2026-06-21) over ~10 weeks from 2026-04-09; ~150 commits/week solo pace. **Contributors include autonomous agents**: Ringo Schwabe 1,354, roongi 141, ernie-lab 9, Orchestrator-W3 1.
- 308 git branches; 4 active parallel worktrees (orchestrator-s20, peer-1/2/3-lesson-12/13/14).
- **~185,932 own Python LOC** across 691 modules (R/Python/TS split when vendored: TS 15,814 / Python 249,315 / R 293,198) + 239 shell scripts. 24,710 git-tracked files; 151,561 markdown; 9,659 HTML deliverables; 711 spec files.
- **156 skills, 123 commands, 143 hooks, 64 agent definitions, 2,221 adw_*.sh scripts, 738 distinct problem-classes** (across 1,012 tagged commits), 80 vertical kernel files, 48-69 shared-lib modules.

### The builder mechanism (plain words)
5 pillars: (1) issue-as-spec, (2) isolated worktrees (port 4000+N, Neon branch), (3) plan/build/validate with TDD enforced, (4) adversarial review (writer ≠ reviewer via Codex), (5) self-healing (divergence updates CLAUDE.md/hook/skill, not just code). ADW trust ladder: IN_LOOP → OUT_LOOP → ZTE (zero-touch). PITER→PETE graduation at ≥90% trust. Daily 07:30 cron DMs operator P0 gaps. Dispatch: 12 max parallel workers; token caps 120K/session, 2M/day, 35M/month. Cost discipline: free-model routing (Groq/Gemini/Ollama/OpenRouter), Anthropic reserved for hard-builder+synthesis = "80% off Anthropic"; Hermes brain $0/mo.

### Multi-vertical proof (headline numbers)
- **ErnieBauMEistER** (construction SaaS) — COMPLETE: 16 kernels, 1,223 corpus chunks, 353 VOB clauses, 54+21 tests passing.
- **SCHWABE UG** (e-learning) — Yr1 €30k / Yr2 €150k / Yr3 €270k; >80% gross margin; €10k capital, no debt; break-even Yr1; Chile 934 vocational schools, ~18% dual-model gap.
- **SENCE quote** (Virtual Planet OTEC, Curicó) — "IA Aplicada: Creación de Prompts," 24h, CLP $96,000 franchise / $200,000 private per participant.
- **LeadGen engine** — ≥200 enriched Chilean leads/week, pitch <5min/lead, free→paid 40-60%, audit offer $2.5K-5K, implementation $10K+.
- **Hermes** — live 24/7 across Slack/Telegram/Discord/WhatsApp, 204 skills, self-healing, $0/mo on free MiniMax-M2.7 brain.
- **Builder Layer v3** — 39 skills, 110 commands, 517 files, 26/26 + 55/55 tests pass.
- **Census** — 84 GitHub repos, 13 Citadelle "countries" (incl. beyond-biomes-bioinformatics, startup-funding, financial-trading-islands, university), 12-14 plugins, Archon 10 packages.
- **Per-customer generation** — /starterpakete auto-produces bespoke business plans + Jobcenter forms for Flores/Schwabe/Ernie/Paul.
- **KPI trajectory** — bugs 14→3→1; autonomous streak 2-3→~11; attempts/task ~3→~1.3; cumulative tests 30→~826; presence HIGH→LOW.

---

## I. PITCH-APP (bb-pitch-show) INTEGRATION NOTES

- **App**: Next.js 14.2.5 / React 18.3.1, TypeScript 5.6.2, iron-session 8 + bcryptjs, three 0.169 + react-three-fiber (3D Genie orb). No DB. Package `bb-pitch-show` v0.1.0, **port 4001**, **2,088 LOC, 4 commits**. Intentional v1 skeleton; polish via overnight agent loop.
- **Show**: 9 sections, ~660s (11-min budget, marketed 10-min). Sections (id·title·sec·hero KPI): 1 cold-open €12B (45s) · 2 diagnose 47M sequences (105s) · 3 prescribe 317% ROI (90s) · 4 proof 0.85 R² (90s) · 5 team 50% female (90s) · 6 geography DE+CL+ES (60s) · 7 ask €15M ARR (90s) · 8 Q&A 25 prewarmed (60s) · 9 close (30s).
- **Genie voice wiring**: PRIMARY = pre-recorded NotebookLM/Gemini DE narration (free). ElevenLabs RESERVED for live STS surprises only, **HARD CAP ≤5 uses** (file-tracked /tmp/bb-pitch-elevenlabs-usage.txt). **Anthropic NEVER on STS path** (token-discipline Law 1). STS flow: mic webm → Whisper STT → Hermes-VPS brain (MiniMax-M2.7, free) → ElevenLabs DE TTS, 5s hard timeout → text-only fallback. ElevenLabs model eleven_multilingual_v2, stability 0.45 / similarity 0.75.
- **4 prewarmed Q&A** (DE+EN): MONEY-SHOT (Genie = 5th teammate), Genie-helps-farmer, competition, moat. Competition reply: *"Indigo Ag and Pivot Bio sell generic mixes with under 40% field efficacy. I deliver site-specific therapy based on functional diagnosis. That's the delta."* Moat: *"Three moats: data flywheel — every harvest retrains me. IP on Siderophore-Surfactin synergy via RUB. Regulatory headstart via EU 2019/1009."* Backlog bb-003 expands 3→25 cards.
- **Auth**: master password (bcrypt vs SHOW_PASSWORD_BCRYPT), iron-session cookie 4h, SESSION_PASSWORD ≥32 chars, 401 +600ms delay, BYPASS_AUTH=1 escape hatch.
- **/learn route**: script-rehearsal trainer, 4 modes (read_along/shadow/spaced/full_180), 4 ElevenLabs voice presets (bella_warm_en, seraphina_warm_de [default], old_wizard_deep [cloned 2026-06-18], ringo_clone). 7-script catalog; default v06_3_canonical_12slide (425w, 142wpm, 180s, 12 slides, "fully compliant").
- **Overnight loop**: bb_overnight_orchestrator.py, 30-min cron 22:00-06:00 Berlin, 3 free-tier agents (Hermes brain floor 0.80 / Space-Agent UI floor 0.75 / Agent-Zero build floor 0.85), 25-item backlog, PETE graduation at trust floor.
- **Path safety**: NEVER writes to read-only originals (BeyondBiomes-Clean-Fresh, input_BB_OS, exist-transfer-navigator); writable dev copy at projects/BeyondBiomesOS-dev/. Pitch app is a parallel build, not the original demo.
- **NLM bundle skill** (.claude/skills/bb-pitch-multi-nlm-bundle): generates N parallel NotebookLM notebooks (Master/Investor/EXIST/Show/FAQ × generic+founder-voice), 8 artifact types each. Proven 2026-05-07: 10 notebooks, 86+ artifacts, $0. This is how Genie's narration MP3s are produced free instead of via ElevenLabs. Pitfall: only 8 of 9 artifact types work (infographic broken, RPCError 8); cookies expire ~30min; 3-5 sources/notebook.
- **QR demonstrator**: canonical target **review.beyondbiomes.de** (explicitly NOT infinite.beyondbiomes.life). Scan→2 questions→instant real R²/p-value→aggregate live demand stat to Ringo's phone. The GitHub single-file pitch app is the lightweight public QR demonstrator; bb-pitch-show is the heavier operator-only stage app. **[FLAG: no copy of the GitHub single-file app exists in the agentic-layer tree; the relationship is conceptual — folding means porting the 12-slide narrative into narrative.ts + /learn catalog.]**
- **Honesty reframes baked into v06.3**: TAM €12.5B→€1.8B documented EU biostimulant (target €15M = 0.8%); "153% First-Year ROI"→3-yr compounded; "120+ B2B"→Flores LATAM resume + USACH channel; "filed synergy"→"potentially patentable"; R² ladder adds 0.81 (EMP500) rung between 0.68 and 0.85.
- **In-app financials**: EXIST €1,027,477 (721k+298k+22k); Biomizer = B.subtilis HDB1 + P.fluorescens HDB7 @ 2.4×10⁹ CFU/g; EXIST AKZ **03EFNW0447**; contact@beyondbiomes.de.

---

## J. RECONCILE / UPDATE — overrides to pass-1 canonical values

| Field | Pass-1 value | Pass-2 override / note |
|---|---|---|
| agentic-layer commits | "661 commits in 45 days" | **1,505 total commits** (HEAD, 2026-06-21). 661 was a point-in-time deck snapshot. |
| Codebase LOC | "558k / 570k LOC" | **558,327 LOC** (demonstrator); per-language TS 15,814 / Python 249,315 / **R 293,198 (largest)**. RhizoGenie v1.1 pre-EXIST = 570,000 LOC. |
| ML models | "221 models" | 221 = 17 algorithms × 13 targets instantiated; ANNEX-b logical count = **7 models (M1-M7)**. Both true at different granularity. |
| DB tables | (n/a) | **93 (ANNEX-a) vs 48 in 12 categories (ANNEX-b)** — reconcile before pitch. |
| Agents in pipeline | "17-agent" | 17 (ANNEX-a) vs **19-agent analysis pipeline + separate 6-stage orchestrator** (ANNEX-b). |
| Frontend pages | "106 / 109" | 106 (IP) / 109 (ANNEX-a) / "100+" (ANNEX-b). |
| API endpoints | "141+" | 141+ (IP) / 200+ & 123 route files (ANNEX-a) / 96 route files (ANNEX-b). |
| CNN accuracy | "94%" (that was MAG assembly) | CNN disease = **97.1%**; 94% = MAG-assembly accuracy (distinct metric). |
| Schwabe citations | "268" | 268 (IP/Scopus 2026) vs **338 (ANNEX VI)** vs 343+ team total. |
| Schwabe metallophores | (n/a) | 28 metallophores, **23 novel** (Gordonia rubripertincta CWB2). |
| 5th greenhouse metric | "+396% Mn / +309% P" | add **+366% Si** (full triad). |
| CLV / CAC | TARGET CLV €61.2k / CAC €8k→3.2k / 7.7×→19× | operating set: **CLV ~€32,400 / CAC ~€3,000 / 10:1**. |
| EXIST total | €1,041,856 | three figures coexist: **€1,041,796** (IP/VI), €1,041,856 (VIII), ~€1,027,000 (IV). Profi-Online €1,041,809. |
| Sachmittel | €298k | €303,221 (IP Tab.21 / ANNEX VI) vs €298,221 (VIII header). |
| Anreizpauschale | €22.5k | €22,500 (IP/VI) vs €20,000 (VIII). |
| TAM | "€12.5B" / "€3.5B" | **TAM >€3.5B** (sum of 4 segments) is the documented bottom-up; €12.5B is the loose framing; honesty-reframe target uses **€1.8B EU biostimulant**. |
| CTO identity | Tiwari (Prem) | **[UNRESOLVED CONFLICT]** Tischler LOI names CTO **"Aryan Absalan" (48 PM)**; all other docs name Tiwari. Flag for diligence. |
| RUB budget framing | EXIST €1.042M | Partner-structure/Tischler LOI frame a **~€700k (349k personnel + 349k equipment)** RUB-only envelope; equipment corrected €370k→€349k Nov 11 2025. |
| USACH subcontract | "€53k (Ortíz 38 + Levicán 15)" | **[CONFLICT]** ANNEX figures €53k; partner-structure HTML says €41,100 (Ortíz 35 + Levicán 10 = €45k). |
| Strain identity | ATW2/ATW4 (generic) | ATW2 = *Arthrobacter oxydans*, ATW4 = *Kocuria rosea*, S43 = *Rhodococcus erythropolis*; from Wismut GmbH Bad Schlema mine water. |
| Pre-money/exit | (n/a) | Seed €8-10M, Series A €20-25M, Series B €100M pre; exit 30-50M EUR trade sale. |

**Unresolved conflicts to settle before any external use**: (1) EXIST total & Sachmittel/Anreizpauschale line totals across 4 annexes; (2) CTO identity (Tiwari vs Absalan) and founder PM model (24-each vs 36/48/20); (3) USACH subcontract €41,100 vs €53,000 and equity 35/20/10/5/5/5/15 vs Tischler-LOI three-founder split; (4) replication barrier €500k vs €1.3M; (5) field-MG count 155 vs 340; (6) bioreactor 50 L vs 250 L; (7) Garrido (signed) vs USACH-Metro (deprecating doc) as the Chile site; (8) Scheffler letter's 2025 timeline and "Effert" template artifact.