#!/usr/bin/env python3
"""Generate Beyond Biomes 'living pitch' clips via Veo (Gemini API).
Reads GEMINI_API_KEY from env. Saves MP4s to MEDIA_OUT/video. Polls operations.
If Veo is not enabled on the key (403/permission), prints a clear message -> use stills fallback.
Usage: ~/.venvs/bbmedia/bin/python gen_videos.py [n1 n2 ...]   (default: all)
"""
import os, sys, time, pathlib
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
if not KEY: sys.exit("No GEMINI_API_KEY found (env or ~/.gemini/.env).")
OUT = pathlib.Path(os.environ.get("MEDIA_OUT", "/mnt/e/WSL/shared/pitches/media")) / "video"
OUT.mkdir(parents=True, exist_ok=True)
client = genai.Client(api_key=KEY)
MODEL = os.environ.get("VEO_MODEL", "veo-3.0-generate-001")

STYLE = ("Cinematic, warm documentary-meets-scientific, golden-hour light, brand navy/teal/gold accents, "
    "slow push-in, shallow depth of field, NO on-screen text, 5-8s loopable, hopeful tone, not corporate stock. ")

CLIPS = {
 "01_title": "Aerial dawn over a patchwork of European farm fields, mist lifting, a single tractor, soft golden light, cinematic slow push-in.",
 "02_problem": "Macro of dry cracked soil, then the same soil revealing subtle glowing microbial life beneath - dead vs living contrast.",
 "03_landscape": "Intercut three people in separate scenes: a farmer kneeling in a field, a scientist at a microscope, a producer in a bright lab - never together.",
 "04_tech": "Abstract elegant soil microbes lighting up like a constellation/network, data threads weaving, calm and beautiful, no UI.",
 "05_bridge": "A single microbe entering harsh cracked drought soil, then a coordinated consortium thriving - a hopeful turn.",
 "06_model": "Split energy: a farmer smiling at a healthy green field and a producer's hands holding a product bottle, value flowing between them.",
 "07_traction": "A large green German cooperative field from above, then a Chilean summer field - two hemispheres, sun and seasons turning.",
 "08_scale": "A glowing engine/factory of light producing small luminous seeds that grow into different scenes - soil, lab, construction site.",
 "10_team": "Warm portraits-in-motion of scientists and operators at work in a university lab setting, confident and human.",
 "11_validation": "A clean rising accuracy curve rendered as light over a field, sober and honest.",
 "12_close": "Sunrise over a thriving field, a hand pressing into rich living soil, hopeful resolution that loops to the opening.",
}

def gen(name, prompt):
    print(f"[{name}] starting Veo...")
    op = client.models.generate_videos(
        model=MODEL, prompt=STYLE + prompt,
        config=types.GenerateVideosConfig(aspect_ratio="16:9", number_of_videos=1))
    while not op.done:
        time.sleep(12); op = client.operations.get(op); print("  ...rendering")
    res = op.response or op.result
    vids = getattr(res, "generated_videos", None) or []
    for i, gv in enumerate(vids):
        f = client.files.download(file=gv.video)
        p = OUT / f"{name}.mp4"
        p.write_bytes(gv.video.video_bytes if getattr(gv.video, "video_bytes", None) else f)
        print("  saved", p)
    return bool(vids)

names = sys.argv[1:] or list(CLIPS)
for n in names:
    if n not in CLIPS: print("skip", n); continue
    try:
        gen(n, CLIPS[n])
    except Exception as e:
        msg = str(e)
        if "403" in msg or "permission" in msg.lower() or "not" in msg.lower() and "enabled" in msg.lower():
            sys.exit(f"!! Veo not available on this key: {msg[:160]}\n   -> use stills + Ken-Burns fallback (gen_images.py + app motion).")
        print(f"  {n} failed: {msg[:160]}")
print("done ->", OUT)
