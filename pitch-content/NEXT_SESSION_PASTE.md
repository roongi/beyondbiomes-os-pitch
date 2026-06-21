# ▶ NEXT-SESSION MASTER PROMPT — Beyond Biomes (Wave 16: wire the app, ship it)
_Paste the block below into a fresh session (WSL). Content + visuals + the handoff are DONE; this session WIRES THE APP and ships. Use a comprehensive parallel workflow, evidence-grounded, honesty-locked, commit+push each step._

## STATE AS OF 2026-06-21 (done — don't redo)
- **Evidence:** EVIDENCE_LEDGER · REPO_LEDGER · DEEP_ADDENDUM · CANONICAL_FACTS · DECISIONS · PERSONALITY_NARRATIVE · REPLIES_KPIS · AUDIENCE_SCORING.
- **Pitch:** PITCH_MASTER_v1 / v2 (blend) / **v3 (nature→AI-native, recommended)** · codex_improved · SCRIPT_VARIANTS · GEMINI_NUANCES · VOICE_SCRIPT_v1 · QA_MURDER_BOARD · PERSONA_SCRIPTS (farmer/scientist/producer).
- **Visuals (in `shared/pitches/media/` + outputs `media/`):** hero = **handout_map_hero.jpg** ("Beyond Biomes — As Nature Intended"); also map_hub/map_layers/map_clean2/the_map/map_cycle/m_pairing/m_clean/page1 + English business images (openapi/eng_bmc/revenue/eng_journey/eng_org) + 2 QR codes.
- **Handoff:** **`shared/pitches/handout/BeyondBiomes_Handout_FINAL.pdf`** (7-page 16:9 English deck, hero-map cover) — editable source `handout16x9.html`. DONE.
- **Media pipeline:** venv `~/.venvs/bbmedia`; key in `~/.gemini/.env`; `gen_images.py` (Nano Banana 2 + reference-image style transfer via `REF`); `run_gemini_api.py` (text). All working.
- **Repo:** all of the above committed to `beyondbiomes-os-pitch` branch `feat/bb-pitch-content-2026-06-21` / `pitch-content/`.

```
ROLE: Wire the Beyond Biomes pitch into the app and ship (Wave 16). Work from WSL. Read pitch-content/ first
(NEXT_SESSION_PASTE.md, CANONICAL_FACTS.md, DECISIONS.md, PITCH_MASTER_v3.md, PERSONA_SCRIPTS.md,
QA_MURDER_BOARD.md, VOICE_SCRIPT_v1.md, PITCH_APP_INTEGRATION.md, TRAINING_APP_SPEC.md, AUDIENCE_SCORING.md).
HONESTY (locked): patent-PENDING; yield/field=TARGET; "120 B2B deals"=Maria Paz track record;
OpenAPI=~890 endpoints today + contract next; TAM show both 12.5B/3.5B; ask=1.5M EUR seed.

PARALLEL WORKSTREAMS (commit+push each):
 1. APP: full-clone beyondbiomes-os-pitch; merge Miguel's branch feat/perfect-pitch-3min -> main PRESERVING the
    ?k= QR auto-login (PR; no force-push). This styled app becomes the base.
 2. SCRIPT: put PITCH_MASTER_v3 into PITCH_SCRIPT.md + in-page text + marp decks; honesty pass on ALL copy.
 3. SYNTHESIZED ONE-VIEW (investor): the pitch (12 slides) + the handout visuals as a slideshow (hero map +
    English business images) + investor-stats/proof + team. Voice OFF by default for investors.
 4. /train route (TRAINING_APP_SPEC): teleprompter + version selector (listen/skip/decide across
    claude_v1/v2/v3, codex) + delivery scoring (WPM, timing-vs-map, pauses, energy) + Q&A drills (qa.json from
    QA_MURDER_BOARD, random-fire, self-score) + voice-analysis loop (record -> local metrics + Gemini multimodal
    report -> iterate; A/B own voice vs best voice).
 5. VOICE: wire Ringo's generated MP3s (local voice) as per-section audio slots.
 6. QR: handout->app + last-slide->app; generate QR PNGs from final URLs.
 7. DEPLOY; verify ?k= QR login still works.

ASSETS FROM RINGO: voice MP3s (from VOICE_SCRIPT_v1) · final app/demo URLs · confirm drop team_christopher.

CLOSE: run the operator cockpit commands /retrospective, /dream, /skillify, /session-superclose. Stamp Wave 16 done.
```

## Open items for Ringo
- Generate voice MP3s (VOICE_SCRIPT_v1) · provide final app/demo URLs · confirm drop `team_christopher` · (optional) print-grade upscale of hero map.
```
