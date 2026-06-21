# ▶ SESSION PRIME — Beyond Biomes Wave 16 (paste this to start the next session)

```
You are continuing the Beyond Biomes pitch build (Wave 16), working from WSL, with Pi as the orchestrator
for follow-on waves. Read pitch-content/ first: NEXT_SESSION_PASTE.md (the full plan), CANONICAL_FACTS.md,
DECISIONS.md, PITCH_MASTER_v3.md, PERSONA_SCRIPTS.md, QA_MURDER_BOARD.md, VIDEO_STORYBOARD.md,
PITCH_APP_INTEGRATION.md, TRAINING_APP_SPEC.md, VOICE_API_COMMANDS.md, AUDIENCE_SCORING.md, and the skill at
pitch-content/skill/pitch-factory/SKILL.md.

ENV READY: venv ~/.venvs/bbmedia; keys in ~/.gemini/.env (Gemini + Veo, valid) and ~/.elevenlabs/.env (reset,
131k chars); scripts gen_images.py (Nano Banana 2 + REF style-transfer), gen_voice.py, run_gemini_api.py,
composite_logo.py, list_voices.py, credits.py. WSL gotchas: prefix MSYS_NO_PATHCONV=1 for /home paths via wsl.exe;
inside WSL drop the `wsl -d` wrapper; scripts read the dotted keys from .env directly.

ALREADY DONE (don't redo): evidence ledgers; PITCH_MASTER v1/v2/v3 + personas + Q&A; voices (Old Wizard
JoYo65swyP8hH6fVMeTO) in media/voice/ for EN+DE+ES (pitch v3_3min, v1, 4-min, farmer/scientist/producer);
branded hero map (green+orange, deep-tech loop, nature=deeptech mapping, real LOGNEU logo); handout FINAL pdf;
voice_scripts.html; NotebookLM source pack in nlm_sources/.

HONESTY LOCKED: patent-pending (not granted); yields/field = TARGET; TAM show both 12.5B/3.5B; ask 1.5M EUR;
"founder track record" ≠ paying clients.

DO (parallel where possible; commit+push each):
 1. VIDEOS in EN+DE+ES, in this order:
    (a) ANIMATED PRESENTATION / "hyperframe-motion" video of the locked 12 slides (BeyondBiomes_SoilIntelligence_FINAL.pdf),
        narrated by the Old Wizard MP3s (per-slide timing). Wire this into the pitch app FIRST.
    (b) NOTEBOOKLM 3-min anime video from nlm_sources/ → overlay our Old Wizard voice (EN/DE/ES).
    (c) GOOGLE FLOW / Veo cinematic per VIDEO_STORYBOARD → overlay our voice.
 2. SUBTITLES (SRT/VTT) for the 4-min audio (and the videos), EN/DE/ES.
 3. MAP FINAL: refit the real LOGNEU logo into its box (Nano Banana reference or precise PIL); add the
    nature-based deep-tech principle line + next verticals (education · construction · facility management).
 4. APP: merge Miguel branch feat/perfect-pitch-3min → main preserving the ?k= QR login; BRAND the app with the
    round LOGNEU logo + green/orange; fold in PITCH_MASTER_v3 + the voices + the slide video.
 5. TRAINING APP /train end-to-end: teleprompter + version/lang selector (listen/watch ALL → Ringo picks) +
    delivery scoring + Q&A drills. After Ringo picks → wire the winners into the pitch app + reference in handoff.
 6. SYNC everything to shared/pitches + BeyondBiomes_Pitch_2026-06-21/ + push the branch; open the PR.

DELIVER: working pitch app + working training app (3 languages) + handout FINAL (round-logo branded) + all videos,
all synced — so subsequent open plans can run in their own Pi-orchestrated sessions.

CLOSE: run cockpit /retrospective /dream /skillify /session-superclose. Stamp Wave 16 done.
```

_After this wave: hand off to Pi as orchestrator for the remaining planned waves (app verticals, federation, etc.)._
