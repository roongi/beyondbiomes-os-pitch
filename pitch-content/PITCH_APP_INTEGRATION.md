# Pitch App Integration Plan — beyondbiomes-os-pitch
_Target app (investor-facing; the handout QR + the last-slide QR both point here). Plan-first; build next session/wave._

## Repo state (verified 2026-06-21)
- Repo: `github.com/roongi/beyondbiomes-os-pitch`
- **`main`** (`d5e7072`): the OS-only deployed version. Its one unique feature = **QR auto-login (`?k=` magic-link bypass)** — MUST be preserved.
- **`feat/perfect-pitch-3min`** (`4474389`, "Uniform section tone + centered team photos") = **Miguel's branch = the real styled BeyondBiomes pitch app.** Contains: `index.html`, `DESIGN_SYSTEM.md`, `PITCH_RULES.md`, `PITCH_SCRIPT.md`, `README.md`, `assets/` (team photos ringo/anna/prem/maria/ernesto/reuben/paul/miguel/christopher + field/soil/microbiome/soilprofile + logo), `bg-lab.html`, `marp/` (DE+EN pptx + md + theme), `mockups/` (apple/starbucks/stripe variants), `one_sentence.html`, `script.html`. (38 files.)
- **Conclusion:** Miguel's branch is the design-correct base. The job = merge it to main (preserving QR login), then fold in the new evidence-rich script + voice + synthesized investor view.

## Build steps (next wave)
1. **Full clone** (not shallow): `git clone` + `git fetch origin main feat/perfect-pitch-3min`.
2. **Merge Miguel → main, preserving QR login.** Recommended: branch `feat/merge-perfect-pitch`; take `feat/perfect-pitch-3min` as the base for all UI files; **cherry-pick / re-apply the `?k=` magic-link auto-login** from `main`'s `index.html` into it. Open a PR `feat/perfect-pitch-3min` (+ QR login) → `main`. (Don't force-push main.)
3. **Swap in the new script.** Replace `PITCH_SCRIPT.md` body + the in-page pitch text with **PITCH_MASTER_v1** (evidence-rich, honest). Keep `PITCH_RULES.md` tone; update numbers to CANONICAL_FACTS. Update `marp/pitch.md` + `pitch.de.md`.
4. **Synthesized one-view (the user's core ask):** add/upgrade sections so the app shows, in one flow:
   - **The pitch** (slide-by-slide, matching the 12 locked deck slides + the new script).
   - **Handout visuals as a slideshow** (the generated hero map + the best IP/ANNEX visuals — see HANDOUT_PLAN best-visuals list).
   - **Investor statistics visuals** (KPIs, 3-customer revenue, TAM-both, unit economics, traction/LOIs incl. Cyro, the moat).
   - **Team** (Miguel's photos). Apply DECISIONS: keep Schwabe/Ngo/Tiwari/Flores + advisors Tischler/Rego/Cavalcante. **Confirm whether to drop `team_christopher.jpg`** (ledger flagged Christopher Bohring as placeholder).
5. **Voice wiring (local voice first).** Add per-section audio slots for the MP3s Ringo generates (local voice; quality was good). **Default OFF for the investor view** (investors don't want auto-voice — that lives in the real OS app); a "training mode" toggle plays the narration per slide for Ringo's rehearsal. Remove/raise the ElevenLabs ≤5 cap is N/A here (this app uses pre-generated MP3s, not live ElevenLabs).
6. **Two QR codes:** (a) handout → this app; (b) last deck slide → this app. Plus keep the live-demo QR (`review.beyondbiomes.de`).
7. **Apply honesty pass** (DECISIONS.md) to ALL app copy: patent-pending, yield/field as target, greenhouse proof + "we fund the proof", R² 0.68→0.85, OpenAPI = ~890 endpoints today + contract next, TAM show both.
8. **Deploy** + verify the `?k=` QR login still works.

## Assets the app will need from Ringo (hand back)
- Voice MP3s from `VOICE_SCRIPT_v1.md` (local voice; 3 segments or 1 full).
- Generated images from `IMAGE_PROMPTS.md` (hero map + supporting art).
- Final QR target URLs (deployed app URL, Drive folders for IP/AP + platform docs).

## Content pack committed into the repo
All evidence + scripts + plans are committed to branch **`feat/bb-pitch-content-2026-06-21`** under `pitch-content/` so the next wave has everything in-repo.
