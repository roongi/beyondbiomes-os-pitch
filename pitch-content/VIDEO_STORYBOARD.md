# Beyond Biomes — "Living Pitch" Video Storyboard (Veo / Google Flow)
_To make the pitch app alive: short generated clips behind each of the 12 slides + a 60s sizzle. Provider: Google Veo 3 (via Flow app OR Veo API). Note: Flow = web app (interactive); Veo API = scriptable from WSL (needs API key + Veo access)._

## Style bible (every clip)
Cinematic, warm documentary-meets-scientific, golden-hour palette + the brand navy/teal/gold. Slow push-ins, shallow depth of field, no on-screen text (we overlay text in the app). 5–8s loopable clips, 16:9, 1080p+. Quiet, hopeful tone — never corporate stock.

## Clip list (slide → prompt)
1. **Title** — "Aerial dawn over a patchwork of European farm fields, mist lifting, a single tractor, soft golden light, cinematic slow push-in."
2. **Problem** — "Macro shot of dry cracked soil, then the same soil alive with subtle glowing microbial activity beneath — contrast dead vs living."
3. **Landscape** — "Three people in separate scenes: a farmer kneeling in a field, a scientist at a microscope, a producer in a bright lab — intercut, never together."
4. **Technology** — "Abstract elegant visualization of soil microbes lighting up like a network/constellation, data threads weaving, calm and beautiful (no UI screens)."
5. **Bridge** — "A single microbe entering harsh cracked drought soil (the 'warzone'), then a coordinated consortium thriving — hopeful turn."
6. **Business model** — "Split-energy: a farmer smiling at a healthy green field / a producer's hands holding a product bottle — value flowing between them."
7. **Traction** — "A large green German cooperative field from above, then a Chilean summer field — two hemispheres, sun and seasons turning."
8–9. **Scale** — "A glowing engine/'factory of light' producing small luminous seeds that grow into different scenes — soil, lab, construction site — the system that builds systems."
10. **Team** — "Warm portraits-in-motion of scientists and operators at work, Ruhr-University setting, confident and human."
11. **Validation** — "A clean rising accuracy curve rendered as light over a field, honest and sober, 0.68 → 0.85."
12. **Ask / close** — "Sunrise over a thriving field, a hand pressing into rich living soil, hopeful resolution; loops back to the opening."
**+ Sizzle (60s):** stitch the strongest 8 beats with the voice track for the app's hero loop and the last-slide QR landing.

## Pipeline (next session, once key+access ready)
1. `gen_videos.py` — Veo API (`veo-3.0-generate-*`) per prompt → MP4s in `shared/pitches/video/`.
2. Stitch/caption with **ffmpeg** (already in agentic-layer base) or **Remotion** for the sizzle + overlays.
3. Embed: each slide in the pitch app gets a muted autoplay loop background; the voice track plays over the sizzle. Training mode lets Ringo watch + rehearse to it.

## ⚠ Honest constraints
- **Google Flow (labs.google/flow) is a browser app — not headless.** I cannot operate it for you. Veo **API** is scriptable from WSL but needs a Gemini API key with **Veo access** (often paid/preview; Ultra's Flow quota ≠ API quota).
- Veo clips are short (5–8s) — we loop/stitch for length.
- Fallback if Veo API isn't enabled: generate stills with Nano Banana (image API) and use Ken-Burns motion in the app (still looks "alive," no Veo needed).
