# ▶ SESSION PRIME (THIS Claude Code env) — Beyond Biomes Wave 16, dynamic-workflow build
_Paste the block below into a fresh session HERE. It implements ALL open items using the dynamic Workflow (parallel-agent) approach. Human-in-loop items (NotebookLM / Google Flow web apps, final picks) are flagged, not blocked._

```
Continue the Beyond Biomes pitch build (Wave 16) in THIS Claude Code environment. Use the dynamic WORKFLOW tool
to run the build as parallel phases (the same approach used to build everything so far). Work from WSL.

READ FIRST (pitch-content/ on branch feat/bb-pitch-content-2026-06-21, mirror E:\WSL\shared\BeyondBiomes_Pitch_2026-06-21\):
NEXT_SESSION_PASTE.md, CANONICAL_FACTS.md, DECISIONS.md, PITCH_MASTER_v3.md, PERSONA_SCRIPTS.md, QA_MURDER_BOARD.md,
VIDEO_STORYBOARD.md, PITCH_APP_INTEGRATION.md, TRAINING_APP_SPEC.md, AUDIENCE_SCORING.md, VOICE_API_COMMANDS.md,
nlm_sources/BB_NLM_brief.md, skill/pitch-factory/SKILL.md.

ENV READY: venv ~/.venvs/bbmedia; keys ~/.gemini/.env (Gemini+Veo) & ~/.elevenlabs/.env (131k); scripts gen_images.py
(Nano Banana 2 + REF style-transfer), gen_voice.py, run_gemini_api.py, composite_logo.py, list_voices.py, credits.py.
PDF via Edge headless. Git push works (GCM). WSL gotchas: prefix MSYS_NO_PATHCONV=1 for /home paths via wsl.exe;
inside WSL drop the `wsl -d` wrapper; scripts read dotted keys from .env directly. (Git Bash .bashrc UTF-16 error is fixed.)

DONE (don't redo): evidence ledgers; PITCH_MASTER v1/v2/v3 + personas + Q&A; voices (Old Wizard JoYo65swyP8hH6fVMeTO)
EN+DE+ES in media/voice/ (pitch 3min+4min, v1, personas); branded hero map (media/handout_map_hero.jpg: green+orange,
deep-tech loop, nature=deeptech mapping, real LOGNEU logo); handout FINAL pdf; voice_scripts.html; nlm_sources/ pack.

HONESTY LOCKED: patent-pending (not granted); yields/field=TARGET; TAM show both 12.5B/3.5B; ask 1.5M; track-record≠clients.

IMPLEMENT — author ONE Workflow with these phases (parallelize within each; commit+push after each phase):
  PHASE A "Assets" (parallel agents):
    - Subtitles: generate SRT+VTT (EN/DE/ES) from voice_text/*.txt aligned to the MP3 durations (ffprobe).
    - Map final: refit real LOGNEU logo into its box (gen_images.py REF or composite_logo.py precise) + add the
      nature-deep-tech principle line + next verticals (education, construction, facility management); print-upscale.
    - Handout: re-render handout16x9.html with the final map (Edge headless) -> BeyondBiomes_Handout_FINAL.pdf.
  PHASE B "Slide video" (parallel per language EN/DE/ES):
    - Build the ANIMATED PRESENTATION / hyperframe-motion video of the locked 12 slides
      (shared/pitches/BeyondBiomes_SoilIntelligence_FINAL.pdf -> per-slide PNGs) with Ken-Burns/Framer-style motion +
      the Old Wizard MP3 per language (ffmpeg; per-slide timing from PITCH_MASTER timing map) + burned-in subtitles.
      Output media/video/slidevid_{en,de,es}.mp4.
  PHASE C "App" (one worktree, careful):
    - Full-clone beyondbiomes-os-pitch; merge feat/perfect-pitch-3min -> main PRESERVING the ?k= QR login (PR, no force).
    - Brand with the round LOGNEU logo + green/orange. Fold in PITCH_MASTER_v3 text + the voice MP3s (per-section slots,
      OFF by default for investors) + the slide video. Build /train route end-to-end per TRAINING_APP_SPEC:
      teleprompter + version/language selector (listen/watch ALL -> pick) + delivery scoring (WPM/timing/pauses) +
      Q&A drills (qa.json from QA_MURDER_BOARD). Deploy; verify ?k= login.
  PHASE D "Sync": copy all to outputs + commit + push + open the PR.

HUMAN-IN-LOOP (flag clearly; do the scriptable parts, queue the rest):
  - NotebookLM 3-min ANIME video: Ringo runs NLM on nlm_sources/ (web app) -> hand back; then OVERLAY our Old Wizard
    voice (EN/DE/ES) via ffmpeg.
  - Google Flow / Veo cinematic per VIDEO_STORYBOARD: Veo via API is scriptable (try gen_videos.py); the Flow web app is
    Ringo's; overlay our voice.
  - Ringo provides: final app/demo URLs (QR), pick of voice/video winners, drop-team_christopher confirm.
  After picks -> wire winners into the pitch app + training app + reference in the handoff, all 3 languages.

CLOSE: run cockpit /retrospective /dream /skillify /session-superclose. Stamp Wave 16 done; hand remaining planned
waves to Pi as orchestrator (see NEXT_SESSION_PASTE.md "after this wave").
```

---
## The wave-after handoff (Pi orchestrator)
Once Wave 16 ships, the remaining planned work (app verticals, federation, the broader BBOS roadmap) runs in its own
Pi-orchestrated sessions per the operator runbook. This paste finishes the pitch package + apps so those can start clean.
