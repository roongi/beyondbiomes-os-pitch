# ▶ NEXT-SESSION MASTER PROMPT — Beyond Biomes Pitch (Wave 16)
_Paste the block below into the next session (Pi/Claude in WSL). It implements EVERYTHING using the same approach we used here: evidence-grounded, honesty-locked, multi-model reviewed, modular outputs, commit+push each step._

---
```
ROLE: Continue the Beyond Biomes pitch build (Wave 16). Work from WSL. Use the same method as the prep session: ground every claim in the evidence pack, obey the honesty rules, review with Codex (and Gemini once its key is renewed), keep outputs modular, commit+push after each workstream.

READ FIRST (all in beyondbiomes-os-pitch branch feat/bb-pitch-content-2026-06-21 /pitch-content/, mirror E:\WSL\shared\BeyondBiomes_Pitch_2026-06-21\):
NEXT_SESSION_PASTE.md, CANONICAL_FACTS.md, DECISIONS.md, PITCH_MASTER_v2.md (default), SCRIPT_VARIANTS.md, QA_MURDER_BOARD.md, TRAINING_APP_SPEC.md, HANDOUT_PLAN.md, IMAGE_PROMPTS.md, VIDEO_STORYBOARD.md, PITCH_APP_INTEGRATION.md, evidence (EVIDENCE_LEDGER/REPO_LEDGER/DEEP_ADDENDUM).

HONESTY (non-negotiable): patent-PENDING; yield/field=TARGET; "120 B2B deals"=Maria Paz track record; OpenAPI=~890 endpoints today+contract next; TAM show both 12.5B/3.5B; ask=1.5M EUR seed.

PREREQUISITES to unblock media (do these first, then tell the agent):
 (P1) Fresh GEMINI_API_KEY in WSL (current one EXPIRED) — needed for image + video + audio-analysis. aistudio.google.com.
 (P2) pip install google-genai  (SDK not installed in WSL python3).
 (P3) For video: confirm the key has Veo access (paid/preview). If not, use the Nano-Banana stills + Ken-Burns fallback (VIDEO_STORYBOARD §fallback).

WORKSTREAMS (commit+push each):
 1. APP: clone full beyondbiomes-os-pitch; merge Miguel's branch feat/perfect-pitch-3min -> main PRESERVING the ?k= QR auto-login (PR). Swap in PITCH_MASTER_v2 as the script; honesty pass on ALL copy.
 2. SYNTHESIZED ONE-VIEW (investor): pitch (12 slides) + handout-visual slideshow + investor-stats visuals + team. Voice OFF by default for investors. Two QR codes (handout->app, last-slide->app) + live-demo QR.
 3. TRAINING /train route (TRAINING_APP_SPEC T1-T6 + voice loop below).
 4. IMAGES: run gen_images.py (IMAGE_PROMPTS: hero map, doctor, factory, connections) + the LOGO; drop into handout + app. Nano Banana 2 (gemini-3.1-flash-image), 4K, aspect ratios.
 5. VIDEO: run gen_videos.py (VIDEO_STORYBOARD: 12 slide clips + 60s sizzle via Veo 3) OR stills+Ken-Burns fallback; embed as muted autoplay loops behind slides + sizzle on the hero/last-slide.
 6. HANDOUT: build BeyondBiomes_Handout_v1.pdf (HANDOUT_PLAN) once images + QR URLs ready.
 7. MULTI-MODEL: re-run Codex (Max, WSL: codex exec --skip-git-repo-check - < review_prompt.txt) AND Gemini (Ultra, after key renew: GEMINI_CLI_TRUST_WORKSPACE=true gemini < review_prompt.txt) on PITCH_MASTER_v2; synthesize v3 if better.

VOICE TRAINING LOOP (the core of /train):
 Ringo reads a section -> record mic -> analyze -> report -> iterate. Analysis = local metrics (WPM vs ~145-150, timing-vs-map, pauses, energy via Web Audio) + Gemini multimodal audio review (transcript vs script, pace, filler words, tonal variation, confidence) -> specific "improve this" report. A/B his recording against the BEST generated voice (ElevenLabs/local). Version selector to listen/skip/♥-pick across claude_v1, claude_v2, codex, (gemini), winner_soft, deck_180; export his personal blend. Persist progress.

DELIVERABLES FROM RINGO: fresh GEMINI_API_KEY (P1); voice MP3s per chosen variant; final QR URLs; decide drop team_christopher.jpg?; pick default variant (recommended claude_v2).

CLOSE: run /retrospective, /dream, /skillify, then /session-superclose (operator cockpit). Stamp Wave 16 done.
```
---

## Open-task ledger (mirrors the prompt)
**Ringo:** A1 voice · A2 images · A3 QR URLs · A4 christopher? · A5 score script · A6 renew GEMINI_API_KEY · A7 voice per variant · A8 confirm Veo access.
**Build:** B1 merge Miguel+QR · B2 script swap+honesty · B3 synthesized view · B4 voice slots · B5 QR · B6 Gemini nuances · B7 handout PDF · B8 deploy · B9 /train route · B10 scripts.json+qa.json · **B11 images (gen_images.py)** · **B12 LOGO** · **B13 videos (gen_videos.py / Veo or fallback)** · **B14 embed video loops + sizzle** · B15 voice-analysis (local + Gemini multimodal).
**Admin:** C1 open PR · C2 stamp Wave 16 · C3 re-review v2 (Codex+Gemini).
```
