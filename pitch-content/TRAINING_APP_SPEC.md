# Beyond Biomes — Pitch TRAINING App Spec
_Ringo's private rehearsal tool (NOT the investor app). Goal: train delivery + defend Q&A until automatic. Listen to multiple script versions, skip, and choose the winner._

## Where it lives
- `bb-pitch-show` (Next.js, agentic-layer base, port 4001) "literally doesn't work" today → **Recommended: build training as a `/train` route inside the same `beyondbiomes-os-pitch` app** (one codebase; investor view stays clean and voice-off, `/train` is voice-on + drills). Alternative: revive `bb-pitch-show`. Decide next session.
- Local-only (no auth, not deployed publicly) — it's for Ringo.

## Modes

### 1. REHEARSE (teleprompter + voice)
- 12-slide flow; each slide shows the spoken lines + stage directions + the **target clock** from PITCH_MASTER_v1's timing map.
- **Version selector (A/B/C…) to listen, skip, decide** — play each version's audio per section, mark a preference. Versions to load:
  - `master` = PITCH_MASTER_v1 (Claude)
  - `gemini` = Gemini improved
  - `codex` = Codex improved
  - `winner-soft` = "Eyes before muscle" (BeyondBiomes_Pitch_FINAL_draft)
  - `deck-180` = lastpitchsession 180s
  - Per-section "♥ pick" buttons → exports a **chosen blend** (your personal best-of) to a new script file.
- Audio: `<audio>` elements per version/segment (the local-voice MP3s). Speed control 0.8–1.3×. Auto-advance on segment end.

### 2. DELIVERY SCORING (tonalization + speed)
- Mic via `getUserMedia`; record Ringo reading a section.
- **Speed:** live WPM vs target (≈145–150); per-slide timing vs the timing map; red/green if over/under the slide's clock. Total-time gauge against 3:00.
- **Tonalization (lightweight, no cloud):** Web Audio analyser → energy/volume envelope + pause detection; flag the 3 non-negotiable silences (after "eyes before muscle", after "we bend time", before "Thank you"); show an energy curve vs the target shape (quiet→punch→intimate). Optional pitch (autocorrelation) for monotone warning.
- Score card per run: pace, pauses-hit, energy-variation, time. Keep a history to see improvement.

### 3. Q&A MURDER BOARD (defend & convince)
- Source: `QA_MURDER_BOARD.md` (parse Q/A by category).
- **Drill modes:** by category · **random-fire** (shuffled) · "weak only" (spaced repetition on missed).
- For each card: show **Q** → Ringo answers aloud (optional mic record) → reveal **model answer** → self-score **Got it / Shaky / Missed**. Shaky/Missed re-queue sooner.
- **Timer:** 30s answer cap (forces tight answers). Show the "bridge-back line" hint.
- Progress: % mastered per category; the "5 lines you must never fumble" pinned at top.
- Optional later: speech-to-text the answer + auto-check it contains the key number/reframe.

### 4. PROGRESS
- LocalStorage: sections rehearsed, best times, Q&A mastery, chosen version per section.

## Data the app reads (drop-in JSON, easy to update)
- `train/scripts.json` — `[{id, label, slides:[{n,title,text,directions,clock,audio}]}]` (one entry per version).
- `train/qa.json` — `[{id, category, q, a, bridge, seat}]` (generated from QA_MURDER_BOARD).
- `train/audio/*.mp3` — voice takes per version/segment.

## Build tasks (fold into Wave 16)
- [ ] T1 · `/train` route + version selector + teleprompter (reads scripts.json).
- [ ] T2 · audio player per version/segment + speed control + "♥ pick" → export chosen blend.
- [ ] T3 · delivery scoring (WPM, timing-vs-map, pause + energy via Web Audio).
- [ ] T4 · Q&A drill (qa.json, random-fire, self-score, spaced repetition, 30s timer).
- [ ] T5 · generate `scripts.json` (all versions) + `qa.json` from QA_MURDER_BOARD; wire the local-voice MP3s.
- [ ] T6 · progress (localStorage) + the "5 never-fumble lines" banner.
