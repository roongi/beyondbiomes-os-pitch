# ▶ NEXT-SESSION MASTER PLAN & PASTE — Beyond Biomes (Wave 16: voices→videos→app)
_Paste the block at the bottom into a fresh WSL session. Everything below is the state + the plan agreed 2026-06-21._

## ✅ DONE this session (don't redo — saved in `shared/pitches/` + outputs `BeyondBiomes_Pitch_2026-06-21/`, pushed to branch `feat/bb-pitch-content-2026-06-21`/`pitch-content/`)
- **Evidence + scripts:** EVIDENCE/REPO/DEEP ledgers · CANONICAL_FACTS · DECISIONS · PERSONALITY_NARRATIVE · REPLIES_KPIS · AUDIENCE_SCORING · PITCH_MASTER v1/v2/v3 · PERSONA_SCRIPTS · QA_MURDER_BOARD · GEMINI_NUANCES · SCRIPT_VARIANTS · voice_scripts.html (beautiful all-scripts page).
- **Voices (ElevenLabs "Old Wizard" `JoYo65swyP8hH6fVMeTO`, multilingual_v2)** in `media/voice/`: bb_v3 (4-min, parts+full), **bb_v3_3min** (pitch), bb_v1 (what-a-time-to-be-alive), bb_farmer / bb_scientist / bb_producer. Pipeline: gen_voice.py · list_voices.py · VOICE_API_COMMANDS.md. Key in `~/.elevenlabs/.env`.
- **HERO MAP** `media/handout_map_hero.jpg` — antique, green+orange (no blue), deep-tech loop (PLAN→IMPLEMENT→REVIEW→VERIFY→SHIP→LEARN), "NATURE'S RULE = DEEP-TECH RULE" mapping, real LOGNEU logo composited. Pipeline: gen_images.py (Nano Banana 2 + reference-image transfer; refs = JACK_REF_MAP.jpeg/ref_jack.png), composite_logo.py.
- **HANDOFF** `handout/BeyondBiomes_Handout_FINAL.pdf` (7-page 16:9 English, hero-map cover). Source `handout16x9.html`.

## 🔧 OPEN — do next session (in parallel where possible)
**A · MAP FINAL polish** — refit the real **LOGNEU** logo so it sits *just below the intended logo position* and *fits inside* its frame (use Nano Banana 2 with LOGNEU as a reference, OR precise PIL composite into that exact box). Add one short line of **nature-based deep-tech principles** ("we connect agents, data, humans and companies the way nature does — observe, verify, then act") and name the **next verticals: education · construction · facility management**. Then the map is READY.

**B · 3-min vs 4-min** — pitch uses **bb_v3_3min** (3 min). Keep the 4-min **bb_v3_full** for the app's "listen" mode **with subtitles** (generate SRT/VTT from voice_text). Don't delete anything.

**VIDEOS — 3 LANGUAGES (EN · DE · ES) and this ORDER:**
- Voices already generated (Old Wizard, `media/voice/`): **EN** bb_v3_3min_full · **DE** bb_v3_de_full · **ES** bb_v3_es_full (+ v1, 4-min EN, personas). Translations in `voice_text/v3_de.txt`, `v3_es.txt`.
- ⚠ ElevenLabs credits ~1,594 left → use the **2nd API key** for persona-DE/ES or more languages.

**C · (do FIRST) ANIMATED PRESENTATION / "HYPERFRAME MOTION" video** — render the **locked 12 slides** (BeyondBiomes_SoilIntelligence_FINAL.pdf) as an animated (Framer-Motion / Ken-Burns) video, narrated by the Old Wizard voice, per-slide timing from the script timing map. Make EN + DE + ES. **Wire this one into the pitch app first.**

**D · (second) NOTEBOOKLM video** — feed the voice scripts to **NotebookLM** → **3-min ANIME-style** video; overlay **our Old Wizard voice** (EN/DE/ES). 

**E · (last) GOOGLE FLOW (Veo, Ultra Gemini)** — the full cinematic "living pitch" per VIDEO_STORYBOARD (12 clips + sizzle), our voice on top, EN/DE/ES.

→ Wire all into the **training app** (listen/watch all → Ringo selects) → then the chosen one(s) into the **pitch app** + referenced in the **handoff**, in all 3 languages.

**SKILL:** reusable **`pitch-factory`** skill captured at `pitch-content/skill/pitch-factory/SKILL.md` (the whole pipeline + bundled scripts) — install into `.claude/skills/` to re-run this for any pitch.

**F · TRAINING APP end-to-end** — make `/train` work fully: teleprompter + per-slide voice + **version selector (listen all → pick)** + delivery scoring + Q&A drills (QA_MURDER_BOARD). Wire the **presentation-based slide video** in first. After Ringo selects, wire the **best voice + video** into: the **pitch app**, the **training app**, and reference in the **handoff**.

**G · APP BRANDING** — brand the pitch/training app with the **round LOGNEU logo** + brand colors (the app still lacks branding). Merge Miguel's branch `feat/perfect-pitch-3min` → main preserving `?k=` QR login (per PITCH_APP_INTEGRATION).

**From Ringo:** final app/demo URLs (QR); confirm drop team_christopher; listen to all voices/videos and pick winners.

```
ROLE: Continue Beyond Biomes (Wave 16) from WSL. Read pitch-content/ (NEXT_SESSION_PASTE.md first, then CANONICAL_FACTS,
DECISIONS, PITCH_MASTER_v3, PERSONA_SCRIPTS, QA_MURDER_BOARD, VIDEO_STORYBOARD, PITCH_APP_INTEGRATION, TRAINING_APP_SPEC,
VOICE_API_COMMANDS). Tools ready: venv ~/.venvs/bbmedia; keys in ~/.gemini/.env (Gemini+Veo) & ~/.elevenlabs/.env;
gen_images.py (Nano Banana 2 + REF style-transfer), gen_voice.py, composite_logo.py. Honesty locked (patent-pending,
yield=target, TAM both, ask 1.5M).
DO, in parallel: (A) finalize hero map — refit LOGNEU logo into its box + add nature-deep-tech principle line + next
verticals (education/construction/facility-mgmt); (B) make SRT subtitles for the 4-min audio; (C) build the 12-slide
narrated video (Old Wizard voice) per voice variant; (D) NotebookLM 3-min anime video, then overlay our Old Wizard voice;
(E) Google Flow/Veo cinematic video per VIDEO_STORYBOARD; (F) wire /train end-to-end (listen-all + select) and brand the
app with the round LOGNEU logo + merge Miguel branch preserving ?k= login; (G) after Ringo picks, wire best voice+video
into pitch app + training app + reference in handoff. Commit+push each. Then run cockpit /retrospective /dream /skillify
/session-superclose. Stamp Wave 16.
```
