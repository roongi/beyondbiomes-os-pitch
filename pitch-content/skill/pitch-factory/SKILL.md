---
name: pitch-factory
description: >
  End-to-end investor-pitch production from a messy corpus + code repos. Use when building or
  refreshing a deep-tech pitch: extract evidence → lock canonical facts + honesty rules → write the
  3-min script (+ variants & personas) → generate multilingual narration (ElevenLabs) → generate
  branded antique/infographic maps & a print-ready handout (Gemini Nano Banana 2 with reference-image
  style transfer) → plan slide/NLM/Veo videos. Built for Beyond Biomes; generalizes to any deep-tech pitch.
---

# Pitch Factory

Turns a corpus (docs, PDFs, repos, community threads) into a complete, honest, beautifully-branded
pitch package. Proven on Beyond Biomes (2026-06).

## Pipeline (run the phases you need)
1. **Inventory + parallel extraction** — one agent per source cluster → a structured *evidence ledger*
   (KPIs w/ confidence + investor-relevance, power-phrases, visuals, gaps-vs-deck). Use the repos' real
   state (clone or read via WSL UNC `\\wsl.localhost\<distro>\...`).
2. **Reconcile + lock decisions** with the founder — canonical values; flag target vs solid vs estimate.
   Persist `CANONICAL_FACTS.md` + `DECISIONS.md` (honesty rules — never overclaim patents/yields/market).
3. **Personality** — synthesize voice/narrative from founder transcript + community replies (Gemini).
   Extract the "nature → AI-native" arc and signature phrasings.
4. **Scripts** — `PITCH_MASTER` (12-slide mapped, ~3 min), variants, persona scripts, Q&A murder board.
   Multi-model review via Codex + Gemini CLIs; blend the best.
5. **Voice** — `gen_voice.py` (ElevenLabs). Pick a voice (`list_voices.py`), tune settings, generate per
   segment (split on `---`), concat with ffmpeg. Translate scripts via `run_gemini_api.py` for multilingual.
6. **Images/maps** — `gen_images.py` (Gemini **Nano Banana 2** `gemini-3.1-flash-image`). KEY TECHNIQUE:
   pass a **reference image** (`REF` dict) of the target style and "re-render in this style, keep all text
   exact" — this is what makes the antique/Jack style land with legible text. Short labels render clean;
   dense fine-print garbles → keep labels short or typeset in HTML. Composite the real logo with
   `composite_logo.py`. Aspect via `ASPECT` dict.
7. **Handout** — branded HTML (`handout16x9.html`) → PDF via Edge headless
   (`msedge --headless=new --print-to-pdf`). 16:9, one picture per page, QR via `qrcode`.
8. **Videos (plan)** — (a) animated presentation/slide video, (b) NotebookLM, (c) Google Flow/Veo —
   narrated by the same ElevenLabs voice; wire selected ones into the app.

## Bundled tools (in this skill dir / pitch_build)
`gen_images.py` · `gen_voice.py` · `run_gemini_api.py` (Gemini text) · `composite_logo.py` ·
`list_voices.py` · `credits.py` · `assemble_*.py` · workflow scripts (`extract/repos/deep.workflow.js`).

## Environment / setup
- venv `~/.venvs/bbmedia` (`pip install google-genai pillow qrcode[pil]`).
- Keys (chmod 600, sourced from rc): `~/.gemini/.env` (Gemini + Veo), `~/.elevenlabs/.env` (TTS).
- WSL gotchas: prefix `MSYS_NO_PATHCONV=1` when passing `/home/...` paths to `wsl.exe`; inside WSL drop the
  `wsl -d <distro> --` wrapper; the dotted Gemini API key breaks shell sourcing → scripts read the .env directly.

## Guardrails
- Honesty first: patent-PENDING (not granted), yields/field = TARGET, show both broad/serviceable TAM,
  "founder track record" ≠ "paying clients". Cite a source per KPI.
- Brand: keep one palette + the real logo; match the founder's existing document style (use it as the
  image reference). Every label exactly once (tell the model — it duplicates otherwise).

## Inputs → Outputs
**Inputs:** corpus paths, repo paths, audience, locked deck, brand assets, founder transcript.
**Outputs:** evidence ledgers · CANONICAL_FACTS · DECISIONS · PITCH_MASTER(+variants/personas) ·
QA_MURDER_BOARD · multilingual voice MP3s · branded maps + logo · handout PDF · voice_scripts.html ·
video plan/storyboard · next-session paste.
