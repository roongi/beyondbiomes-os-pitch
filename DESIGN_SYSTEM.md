<!-- Frozen pitch design source: roongi/beyondbiomes-os-pitch main @ 4370a05 -->
<!-- Feed THIS file to any UI/slide generation (web app, Clean port, PptxGenJS). It is the single source of truth. -->

# Beyond Biomes — Design System

**Why this file exists:** AI design tools carry an embedded "sameness / newspaper" bias and default to generic AI-slop **unless you hand them your own design system, brand colors, and references every time** (source: Claude Design system-prompt leak, Mark Kashef · Early-AI-dopters L04). Load this `.md` before generating or editing any UI so output is on-brand and one-shot-quality.

## Brand tokens (exact)

| Token | Hex | Role |
|---|---|---|
| Forest green | `#2C5F2D` | Primary — headings, key marks |
| Orange | `#D9531E` | Accent — one highlight per view, CTAs |
| Lime | `#86AC36` | Secondary accent — supporting marks |
| Bone | `#F5F2EA` | Background |
| Background 2 | `#0e2418` / `#173322` | Dark forest sections only |
| Ink | `#3A3A36` | Body text |

**Type:** Fraunces (headings, serif display) · Inter (body, UI). Big bold titles, minimal body text.

## Layout principles (Salvatore workshop, see PITCH_RULES.md)

- Tidy, clean, **high-contrast, readable from the back of the room**. Don't be artsy.
- Big titles, almost no body text. One accent (orange) per view — not three.
- 3–5 light slides / sections per minute. Whitespace is a feature.

## Anti-slop rules (banned — these read as "AI-generated, didn't do the work")

- ❌ **No gradient blobs** (decorative `radial-gradient(circle, …)` + `filter:blur`).
- ❌ **No floating orbs.**
- ❌ **No glassmorphism** (`backdrop-filter:blur`).
- ❌ No purple gradients on white/dark, generic system fonts (Inter is our chosen body font — that's intentional, not the slop default), cookie-cutter SaaS layouts.
- ✅ Brand gradients are fine when subtle and on-palette (e.g. `linear-gradient(90deg, lime, orange)` for an underline). The ban is on *decorative ambient blobs/glass*, not all gradients.

## How to use (operationalizes the leak)

1. **Bring references.** Pull patterns from real, hand-crafted sites — not AI defaults. Inspiration: [Dribbble](https://dribbble.com) · [godly.website](https://godly.website/) · [land-book.com](https://land-book.com/) · [21st.dev/community/components](https://21st.dev/community/components).
2. **Override AI defaults explicitly** — state how many variations you want (it defaults to 3) and how many questions (it's told to "ask 10+").
3. **Verify with fresh eyes** — review the render in a *separate* context (a fresh agent / a real browser screenshot), never let the generator grade its own design. (Same "eyes before muscle" rule the pitch itself sells.)
4. **Hand-coded > AI-deck.** A generic Gamma/Canva deck reads as "AI-generated, low effort" to a jury. Our hand-built `index.html` + PptxGenJS export is a *differentiator* — keep it bespoke and on-brand.

## Applies to

- `index.html` (the pitch webapp) — this repo, frozen design.
- The PptxGenJS export block in `index.html` (slides must match these tokens — they already use BONE/GREEN/ORANGE/INK).
- BeyondBiomes-Clean frontend — port these tokens as theme variables (not one-off copies).
- beyondbiome2 platform app — align the soil-first hero to this palette.

## Build method — Figma → Claude Code (pixel-perfect, free)

Source: Niko Rockensüß guide, Early-AI-dopters L22 ("Figma Designs → perfect Landing Pages"). The highest-quality path is to design in Figma, then have Claude Code rebuild it 1:1 via the **Figma Desktop MCP**:

1. Use the **Figma *desktop* app's** local MCP (free) — NOT the remote MCP (rate-limited to ~50/mo even on paid). Figma desktop must be **running**.
2. Add it: `claude mcp add --transport http figma https://mcp.figma.com` (desktop local server; see figma.com/docs figma-mcp-server local-server-installation).
3. In Figma **Dev Mode (Ctrl+D)** → side panel → click a **section** → it gives the exact MCP node prompt to paste.
4. **Extract section by section, not the whole page** — a full page ≈ 41k tokens (too big for one MCP call); a section ≈ 1.8k. Tell CC: "use the Figma desktop MCP, extract this section 1:1" + paste the node URL. CC pulls structure, text, and **assets** (auto-downloads/renames images for SEO).
5. Give CC a short guide `.md` so it works in small parts, step by step, and **asks you to review** each section before moving on → pixel-perfect.

## Message levers (pitch/sell — Early-AI-dopters L21, reinforce PITCH_RULES.md)

- **Open on pain/goal** in the first 30s (matches Salvatore A2).
- **Loss aversion** — frame degraded soil as money actively *lost*, not just upside ("farms lose billions" already does this).
- **Social proof** — "others already validate this" (the "signal is already there" beat).
- **Show, don't tell** — a live demo / branded app beats slides. Our pitch webapp + the live beyondbiome2 app *is* this lever — lead with it.

## Level-up — beyond "too simple" (imagery + cinematic)

Source: AI Automations by Jack L07 ("Claude Fable Just Changed Website Design", "$10k Cinematic Websites"). Core thesis: **design can be codified** — typography scales, spacing, color tokens, grids. Explain "great" to Claude once, reproduce on demand for web, HTML decks, *and* slides. The reason most AI output looks "too simple / same" is missing **custom imagery + a real brand system**, not missing effort. Tools to go further (most need Miguel to set up / fund — flagged):

- **`awesome-design-md`** (github.com/VoltAgent/awesome-design-md) — 55+ brand design systems (Stripe, Linear, Spotify, Apple…) as plain `design.md`. Install the repo, point Claude at one, build in that calibre one-shot. *Free.* Use it to lift our pitch/web above generic.
- **FireCrawl (MCP)** — scrape brand identity (logo, accent colors, typography, HTML) from any URL, so generated UIs/slides stay brand-consistent. *Free tier / API key.*
- **Nano Banana 2** (Gemini-class image gen) via **Keya API** (~6¢/image) — *this is the missing piece for "too simple."* Generate custom soil/microbiome/field visuals instead of generic stock or ChatGPT images: slide backgrounds, hero imagery, section art. **Needs Miguel: Keya API key + credits.**
- **SeedDance 2.0 / Higgsfield** — cinematic hero video backgrounds for the web app ("visual premium"). Optional, paid.
- **Method (5 steps):** pick format → equip Claude (FireCrawl + image gen) → give references (godly.website, 21st.dev, Midjourney styles) → generate 80% → refine + codify into a reusable skill.

**For the PPTX specifically:** the export is now branded (forest spine, logo, page numbers, accent underline). The next jump to "not simple" is **one custom Nano Banana image per slide** (soil macro, microbiome, field) embedded as a side panel or muted background — do this once a Keya key exists.
