# Beyond Biomes Pitch — Retrospective · Dream · Skillify
_Manual equivalents of /retrospective, /dream, /skillify (those are operator-cockpit commands, not available in this Claude Code instance — run the real ones next session to log them into the plan stack)._

## /retrospective — what happened
**Done:** full evidence extraction (2 doc passes + 3 repos via WSL: app 696 commits, agentic-layer 1505 commits) → EVIDENCE_LEDGER + REPO_LEDGER + DEEP_ADDENDUM. New master script v1→v2 (blend), voice script, Q&A murder board, handout plan, image prompts, video storyboard, training-app spec, pitch-app integration plan. Multi-model review: Codex ✅, Gemini ⛔(expired key). All committed+pushed to `feat/bb-pitch-content-2026-06-21`; mirror in `BeyondBiomes_Pitch_2026-06-21/`.
**Worked well:** parallel workflows for extraction; separating doc-evidence vs repo-reality then fusing; locking honesty forks early (patent-pending, yield=target); using the real WSL repos not stale clones; multi-model critique caught a real overclaim (slide-4 "treat").
**Friction / to improve:** Gemini API key expired; google-genai SDK not installed → media gen blocked; WSL bash quoting via `wsl.exe -- bash -lc` repeatedly mangled `$var` (use stdin/heredocs or `python3 -c` with single quotes); shallow clones complicate merges (full clone next time).
**Decisions stamped:** default script = claude_v2; investor app = beyondbiomes-os-pitch (Miguel branch → main + QR login); voice OFF for investors; show both TAMs; €1.5M ask.

## /dream — the vision (12 months)
A farmer scans a QR, talks to the app in his language, and sees his field's living soil diagnosed in seconds — then a producer's product, tailored to that exact field, arrives. Behind it, the **agentic layer** quietly spins up the next vertical (construction, lab science, education) the same way it built soil. The pitch itself is **alive**: Veo clips breathe behind every slide, the founder's best-take voice narrates, and a training loop has drilled Ringo until the Q&A defense is reflex. Investors don't just hear the story — they *touch* the live platform and *watch* the factory that builds factories. Soil is the first machine off the line; Beyond Biomes is the company that builds the rest.

## /skillify — the reusable skill we built
**Skill name:** `evidence-grounded-pitch` (propose adding to agentic-layer skills).
**What it does:** turns a messy corpus (docs + repos + prior drafts) into a defensible, honest, multi-format pitch.
**Pipeline (reusable):**
1. **Inventory** every source (numbered).
2. **Parallel deep extraction** (workflow): one agent per source cluster → structured evidence ledger (KPIs w/ confidence + investor-relevance, power-phrases, visuals, gaps-vs-deck).
3. **Reconcile + lock honesty forks** with the founder (canonical values; flag target vs solid vs estimate).
4. **Write** the script (now/future fusion), then **voice + handout + Q&A + training** as modular files.
5. **Multi-model review** (Codex + Gemini CLIs) → blend a vXX.
6. **Commit+push** a content pack into the target repo; produce a paste-ready next-session prompt.
**Inputs:** corpus paths, repo paths, audience, locked deck. **Outputs:** EVIDENCE_LEDGER, CANONICAL_FACTS, DECISIONS, PITCH_MASTER, VOICE_SCRIPT, QA_MURDER_BOARD, HANDOUT_PLAN, IMAGE_PROMPTS, VIDEO_STORYBOARD, TRAINING_APP_SPEC, NEXT_SESSION_PASTE.
**Guardrails:** never overclaim (patent/yield/market); separate built-reality from planned; cite source per KPI.
