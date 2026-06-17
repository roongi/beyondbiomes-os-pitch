# Beyond Biomes OS — Interactive Investor Pitch

A self-contained, light, **animated scrollytelling** web app that delivers the Beyond Biomes / BeyondBiomesOS pitch in **3 minutes** — built for the Bochum ecosystem jury (Wirtschaftsentwicklung · VC · Volksbank · Aulinger · Bryck).

**Live:** https://beyondbiomes-os-pitch.vercel.app/ — private preview; sign-in credentials are shared separately with invited guests.

## What it is
- A premium one-page site: animated hero node-network, reveal-on-scroll sections, count-up KPIs, a hand-drawn animated market-growth chart, an animated federation map, and a live **1000× operator** simulator.
- A **"▶ Play the 3-minute pitch"** mode that auto-scrolls through the story **and narrates it** (browser voice, optional 🔊/🔇), showing the **full script as on-screen subtitles** — it doubles as the video.
- A username + password sign-in gate, and a closing **Ask** with four switchable funding versions (€750K · €500K · €1.5M · Traction-first).

## Run locally
Double-click `index.html` — it opens in any browser, fully offline (all images embedded). Best voice quality in **Google Chrome**.

## Controls
| Action | How |
|---|---|
| Play / pause narrated pitch | ▶ button, or **Space** |
| Voice on / off | 🔊 toggle in the play bar |
| Next / previous (during play) | ‹ › buttons |
| Funding versions | Ask section — tabs |
| 1000× simulator | "＋ Deploy a vertical" / "↺ Reset" |
| Download PowerPoint | "⬇ PowerPoint" (hero) — exports a 5-slide .pptx with a QR to the app on the last slide |

## Sections (soil-first)
1. Hero — precision medicine for living soil
2. Soil — the product: sample → read → custom biome → deliver (RhizoGenie + Biomizer)
3. Business model — $1.8B→$3.08B by 2030, EU FPR 2019/1009; €300/mo → €5–15k → €1–5k/mo; €1–2M / operator
4. The method — *eyes before muscle*
5. The output — the OS / 1000× operator + live simulator (the reveal)
6. The federation — one method, many verticals, one Holding
7. Market signal — community validation
8. Team — a federation of operators
9. The ask — 4 switchable funding versions + QR to the app

## Files
- `index.html` — the complete app (self-contained)
- `script.html` — full 3-minute pitch script (readable / printable)
- `one_sentence.html` — the one-sentence pitch
- `PITCH_SCRIPT.md` — timed script / teleprompter
- `assets/` — source logo + team photos (also embedded)

## Deploy
- **Vercel** (current): auto-deploys from `main` on every push → the live URL above.
- **GitHub Pages** (optional): Settings → Pages → Deploy from branch `main` / root.

## Sources
Europe biostimulants market size & CAGR: MarketsandMarkets, Mordor Intelligence, Precedence Research (2025). Regulation: EU Fertilising Products Regulation (EU) 2019/1009 — biostimulants gain a CE-mark pathway (PFC 6), in force since July 2022.

## Brand
Light "bone" palette · forest green `#2C5F2D` · logo orange `#D9531E` · lime `#86AC36`. Headings **Fraunces**, body **Inter**.
