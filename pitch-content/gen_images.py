#!/usr/bin/env python3
"""Generate Beyond Biomes handout/app images via Gemini image models.
Reads GEMINI_API_KEY from env (source ~/.gemini/.env first). Saves PNGs to OUTDIR.
Usage: ~/.venvs/bbmedia/bin/python gen_images.py [name1 name2 ...]   (default: all)
"""
import os, sys, mimetypes, pathlib
from google import genai
from google.genai import types

def _load_key():
    import re
    k = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if k: return k
    try:
        m = re.search(r'GEMINI_API_KEY=(\S+)', open(os.path.expanduser("~/.gemini/.env")).read())
        if m: return m.group(1).strip().strip('"').strip("'")
    except Exception: pass
    return None
KEY = _load_key()
if not KEY:
    sys.exit("No GEMINI_API_KEY found (env or ~/.gemini/.env).")
OUTDIR = pathlib.Path(os.environ.get("MEDIA_OUT", "/mnt/e/WSL/shared/pitches/media"))
OUTDIR.mkdir(parents=True, exist_ok=True)
client = genai.Client(api_key=KEY)

# try these image models in order; first that works is reused
MODELS = [m for m in os.environ.get("IMG_MODELS",
    "gemini-3-pro-image,gemini-3.1-flash-image,gemini-2.5-flash-image").split(",") if m]

STYLE = ("Hand-illustrated isometric infographic, warm storybook-meets-scientific style, clean vector-painterly, "
    "soft paper texture, premium investor-grade. Palette: deep navy #0B2545, teal #1B7F8C, gold #C9A227, "
    "leaf green #3E7C4F, warm soil brown #6B4F3A, light background #EAF1F4. Subtle gold glowing connection lines, "
    "crisp legible hand-lettered labels, lots of clean negative space. No photorealism, no neon, no dark theme, "
    "no stock-photo look, no gibberish text, no watermarks. ")

PROMPTS = {
 "p1_map": STYLE + ("Aspect 4:5 portrait, highest detail. A single isometric 'living world' map titled "
    "'The Beyond Biomes World'. Center: a cross-section of healthy farmland soil teeming with tiny stylized microbes, "
    "wrapped in a glowing circular loop labeled Diagnose -> Prescribe -> Treat -> Learn. Around the field three "
    "friendly characters joined by glowing gold paths: a Farmer (boots, tablet, green field), a Scientist (lab coat, "
    "DNA strand/microscope), a Producer (factory + product bottles). From the soil a beam rises to a calm glowing AI "
    "core labeled 'agentic layer' that sends a little personalized app to the farmer, watches two small globes "
    "(Germany sun / Chile-Spain snow), and arranges tiny glowing bacteria into a consortium. Back hills: a small "
    "'factory that builds factories' emitting little buildings (soil lab, construction site, classroom). Bottom "
    "ribbon: 'Read the system before you change it.' Clean top-left area for a logo."),
 "doctor": STYLE + ("Aspect 1:1. Soil as a patient: a friendly doctor with stethoscope listening to a cross-section "
    "of living soil on an exam table, a clipboard showing a prescription of beneficial bacteria, a small chart rising "
    "from 0.68 toward 0.85. Caption space: 'Precision medicine for the soil.'"),
 "factory": STYLE + ("Aspect 1:1. An isometric robotic 'factory that builds custom machines': a central glowing "
    "engine labeled 'agentic layer' on a conveyor producing distinct small machines, each a different vertical - a "
    "soil/leaf machine highlighted gold ('first off the line'), a construction-helmet machine, a classroom machine, "
    "a leads/magnet machine. Tiny gold gears and flowing data lines. Caption space: 'Soil is the first machine off the line.'"),
 "connections": STYLE + ("Aspect 16:5 wide banner. Four matching circular emblems in a row, gold-line on light: "
    "(1) two people shaking hands 'human <-> human'; (2) a person speaking to a friendly orb 'human <-> agent'; "
    "(3) an orb watching a field with sun and snow 'agent <-> environment'; (4) an orb arranging tiny bacteria into "
    "a ring 'agent <-> bacteria'. Evenly spaced, label beneath each."),
 "logo_mark": STYLE + ("Aspect 1:1. A clean modern LOGO MARK for 'Beyond Biomes': a stylized soil/root + microbe "
    "motif merging into a leaf, navy+teal+gold, minimal, vector, flat, works on light background, NO text."),
 "logo_wordmark": STYLE + ("Aspect 16:9. A clean modern LOGO with wordmark 'Beyond Biomes': the soil-root-leaf mark "
    "beside elegant sans-serif wordmark, navy+teal+gold on light, minimal vector, balanced."),
 "mappa": (
    "A hand-drawn antique treasure map in a warm aged-parchment style, 16:9 landscape, sepia and burnt-sienna ink on "
    "tea-stained, cracked vintage paper, Jumanji / old pirate-map aesthetic, ornate hand-lettered calligraphic labels, "
    "a decorative compass rose, scrollwork borders, faint topographic hatching and contour lines. A title banner across "
    "the top in elegant calligraphy reads: 'THE MAP OF THE LIVING AGENT'. The map depicts a single voyage across a "
    "continent: a coastal harbor labeled 'OBSERVATION' marked with a finely drawn human eye; a winding river flowing "
    "from a region labeled 'MEASURING OUTPUTS' into the interior; a mountain range labeled 'THE OVERNIGHT BRAIN'; a "
    "fertile valley of small labeled groves reading 'TRUST, TASTE, HONESTY, FEAR, INSTINCT, RESPECT', titled 'MENSCHLICH "
    "SIGNALS'; a living green hedge-gate (not a stone wall) labeled 'HONEST SIGNALING & GUARDRAILS', decorated with tiny "
    "drawings of ants, plant root nodules, a cleaner-fish, and bacteria; an archipelago of culturally diverse islands - "
    "one with a Shanghai paper lantern, one with an Arizona desert sun - joined by dotted trade routes labeled 'HARNESS "
    "THE GAPS', titled 'FEDERATION OF PERSPECTIVES'. At the center sits a large ornate brass astrolabe / armillary sphere "
    "labeled 'OBSERVABILITY'. "
    "AT THE FAR FRONTIER of the map, past the known coast, a richly drawn living landmass labeled 'BEYOND - THE BIOME "
    "KINGDOM' shows a cross-section of living soil teeming with glowing microbes, root nodules and fungal threads - the "
    "destination the whole voyage sails toward; a dotted route connects the OBSERVABILITY astrolabe to it, labeled 'READ "
    "THE SYSTEM BEFORE YOU CHANGE IT'. An ornate cartouche in a bottom corner bears the maker's mark 'BEYOND BIOMES'. "
    "A ribbon scroll along the bottom edge reads: 'WE GO FAR TOGETHER'. Small sea monsters and a sailing ship decorate "
    "the ocean margins. Legible antique serif and calligraphic lettering throughout, intricate fine-line detail, warm "
    "candle-lit color grade, high resolution."),
 "mappa_bb": (
    "A hand-drawn ANTIQUE TREASURE MAP, 16:9 landscape, warm aged-parchment, sepia and burnt-sienna ink on tea-stained "
    "cracked vintage paper, Jumanji / old pirate-map aesthetic, ornate hand-lettered calligraphic labels, a decorative "
    "compass rose, scrollwork borders, faint topographic hatching and contour lines, small sea monsters and a sailing "
    "ship in the ocean margins, warm candle-lit color grade. A title banner across the top in elegant calligraphy reads: "
    "'THE BEYOND BIOMES WORLD'. "
    "THE CONTENT is the Beyond Biomes story drawn as one voyage: "
    "(1) A coastal harbor labeled 'THE BLIND FIELD' with a farmer's field drawn as flat squares marked 'N P K pH - what "
    "is there, never what is missing', and a finely drawn human EYE nearby labeled 'EYES BEFORE MUSCLE'. "
    "(2) At the CENTER, a grand cross-section of LIVING SOIL teeming with tiny glowing microbes, roots and fungal "
    "threads - the heart of the map, labeled 'THE LIVING BIOME'; around it a circular route of four stages labeled "
    "'DIAGNOSE -> PRESCRIBE -> TREAT -> LEARN'. "
    "(3) Three islands joined by golden dotted trade routes: a FARMER island ('knows the land by hand'), a SCIENTIST "
    "island (microscope + DNA strand, 'knows what is failing'), and a PRODUCER island (little factory + product "
    "bottles, 'sells the cure'); a banner reads 'THREE PEOPLE, ONE FIELD - CONNECTED'. "
    "(4) A large ornate brass ASTROLABE / armillary sphere instrument labeled 'THE AGENTIC ENGINE' that hands a small "
    "rolled scroll/spyglass to the farmer labeled 'a living app for every field'. "
    "(5) Two small globes joined by a route: one with a sun labeled 'GERMANY', one with snow labeled 'CHILE & SPAIN', "
    "the route labeled 'WE BEND TIME - retrain every 6 months'. "
    "(6) At the far frontier, a glowing 'FACTORY THAT BUILDS FACTORIES' emitting little kingdoms - a soil/leaf one "
    "(highlighted, 'first off the line'), a construction site, a laboratory, a classroom - labeled 'BEYOND - THE SYSTEM "
    "THAT BUILDS SYSTEMS'. "
    "(7) A small antique wax SEAL stamp reading '+396% Mn  +309% P  - peer-reviewed' and an ornate cartouche maker's "
    "mark 'BEYOND BIOMES' in a bottom corner. "
    "A ribbon scroll along the bottom edge reads: 'READ THE SYSTEM BEFORE YOU CHANGE IT'. "
    "Legible antique serif and calligraphic lettering throughout, intricate fine-line detail, high resolution."),
 "onepager": (
    "A clean, modern SINGLE-PAGE INVESTOR ONE-PAGER infographic poster, portrait 3:4, designed to be understood at a "
    "glance in 10 seconds. Generous white space, flat vector illustration, crisp bold sans-serif, HIGH LEGIBILITY, only "
    "SHORT labels (no paragraphs). Warm brand palette: deep navy #0B2545, teal #1B7F8C, gold #C9A227, leaf green "
    "#3E7C4F, soil brown #6B4F3A, on a light cream background. A clear TOP-TO-BOTTOM flow of four stacked bands with big "
    "section headings: "
    "TITLE BAND (top): a small leaf-and-soil logo with the title 'BEYOND BIOMES' and subtitle 'Precision medicine for the soil'. "
    "BAND 1 'THE PROBLEM': left side shows dull grey cracked soil with big letters 'N P K' and a small blindfold icon, "
    "short caption 'soil read as dead chemistry = blind'; a large arrow points right. "
    "BAND 2 'WHAT WE DO': right side shows rich living soil full of colourful microbes and roots, caption 'we read what "
    "the living soil is DOING'; beneath it a clean circular loop of four simple icons labelled 'DIAGNOSE / PRESCRIBE / "
    "TREAT / LEARN'. "
    "BAND 3 'THREE CUSTOMERS, ONE PLATFORM': three simple flat character icons in a row, each connected by a line to a "
    "central glowing chip labelled 'AI PLATFORM' - a FARMER ('more yield'), a SCIENTIST ('powers the science'), a "
    "PRODUCER ('pays + white-label'). "
    "BOTTOM BAND 'PROOF & ASK': three bold stat badges reading '+396% nutrient uptake', '221 AI models live', '5 signed "
    "partners', then a gold call-to-action box 'Raising EUR 1.5M seed'. A thin ribbon at the very bottom: 'Read the "
    "system before you change it.' "
    "Minimal clean icons, no clutter, no photorealism, no gibberish text, perfectly legible short labels only."),
 "page1": (
    "A SIMPLE, elegant ANTIQUE illustration plate, 4:5 portrait, warm aged-parchment with sepia and burnt-sienna ink, "
    "hand-drawn, a single ornate compass rose in one corner and a thin scrollwork border, LOTS of empty parchment "
    "space, calm and UNCLUTTERED (this is a single-idea plate, NOT a busy map), candle-lit warm color grade. "
    "A title banner in elegant calligraphy across the top reads: 'READ THE SYSTEM BEFORE YOU CHANGE IT'. "
    "A small line of calligraphy beneath it reads: 'Nature solved reliability 3.5 billion years ago - eyes before muscle'. "
    "At the CENTER, large and clear, a beautifully drawn cross-section of LIVING SOIL with a single tree growing above "
    "and roots reaching below (the Beyond Biomes emblem), encircled by ONE clean four-step ring of four simple labelled "
    "icons: 'OBSERVE' with a finely drawn human eye, 'UNDERSTAND' with a tiny microbe-and-leaf, 'ACT' with a hand "
    "placing a seedling, 'LEARN' with a spiral arrow. "
    "At the bottom, a small ornate cartouche maker's mark reads: 'BEYOND BIOMES - precision medicine for the soil'. "
    "Only these few elements, big legible antique calligraphic lettering, generous negative space, intricate but "
    "uncrowded fine-line detail, high resolution."),
}

ASPECT = {"p1_map":"4:5","connections":"16:9","logo_wordmark":"16:9","mappa":"16:9","mappa_bb":"16:9","onepager":"3:4","page1":"4:5","doctor":"1:1","factory":"1:1","logo_mark":"1:1"}

def save_parts(resp, base):
    n = 0
    for cand in (resp.candidates or []):
        for part in (cand.content.parts or []):
            d = getattr(part, "inline_data", None)
            if d and d.data:
                ext = mimetypes.guess_extension(d.mime_type or "image/png") or ".png"
                p = OUTDIR / f"handout_{base}{ext}"
                p.write_bytes(d.data); print("  saved", p); n += 1
    return n

names = sys.argv[1:] or list(PROMPTS)
good_model = None
for name in names:
    if name not in PROMPTS: print("skip unknown", name); continue
    print(f"[{name}] generating...")
    tried = [good_model] if good_model else MODELS
    ar = ASPECT.get(name, "1:1")
    for M in tried:
        try:
            try:
                cfg = types.GenerateContentConfig(response_modalities=["IMAGE"],
                        image_config=types.ImageConfig(aspect_ratio=ar))
                resp = client.models.generate_content(model=M, contents=PROMPTS[name], config=cfg)
            except Exception:
                resp = client.models.generate_content(model=M, contents=PROMPTS[name],
                        config=types.GenerateContentConfig(response_modalities=["IMAGE"]))
            if save_parts(resp, name):
                good_model = M; print(f"  via {M} ({ar})"); break
        except Exception as e:
            print(f"  {M} failed: {str(e)[:120]}")
    else:
        print(f"  !! no model produced {name}")
print("done ->", OUTDIR)
