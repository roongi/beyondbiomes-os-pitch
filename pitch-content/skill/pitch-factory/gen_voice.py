#!/usr/bin/env python3
"""Generate Beyond Biomes pitch narration via the ElevenLabs API.
Key: ELEVENLABS_API_KEY in env or ~/.elevenlabs/.env. Voice: VOICE_ID env or --voice.
Usage:
  ~/.venvs/bbmedia/bin/python gen_voice.py TEXT_FILE OUT_MP3 [--voice VOICE_ID] [--model eleven_v3]
Splits the text on lines containing only '---' into segments -> OUT_MP3 (or _01/_02 per segment).
"""
import os, re, sys, json, pathlib, urllib.request, urllib.error

def load_key():
    k = os.environ.get("ELEVENLABS_API_KEY") or os.environ.get("ELEVEN_API_KEY")
    if k: return k
    try:
        m = re.search(r'ELEVENLABS_API_KEY=(\S+)', open(os.path.expanduser("~/.elevenlabs/.env")).read())
        if m: return m.group(1).strip().strip('"').strip("'")
    except Exception: pass
    return None

args = sys.argv[1:]
def opt(flag, default):
    return args[args.index(flag)+1] if flag in args else default
text_file = args[0]; out_mp3 = args[1]
VOICE = opt("--voice", os.environ.get("VOICE_ID", ""))           # your Old Wizard PVC voice id
MODEL = opt("--model", os.environ.get("ELEVEN_MODEL", "eleven_multilingual_v2"))  # or eleven_v3
KEY = load_key()
if not KEY: sys.exit("No ELEVENLABS_API_KEY (env or ~/.elevenlabs/.env).")
if not VOICE: sys.exit("No VOICE_ID. Pass --voice <id> or set VOICE_ID. List voices: see README cmd.")

# pitch-tuned settings derived from your reference (Old Wizard: stability 71, style/boost 75)
SETTINGS = {"stability": float(os.environ.get("V_STAB","0.6")),
            "similarity_boost": float(os.environ.get("V_SIM","0.8")),
            "style": float(os.environ.get("V_STYLE","0.7")),
            "use_speaker_boost": True}

raw = open(text_file, encoding="utf-8").read()
segments = [s.strip() for s in re.split(r'(?m)^\s*-{3,}\s*$', raw) if s.strip()]
base = pathlib.Path(out_mp3)

def tts(text, dst):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128"
    body = json.dumps({"text": text, "model_id": MODEL, "voice_settings": SETTINGS}).encode()
    req = urllib.request.Request(url, data=body, method="POST",
        headers={"xi-api-key": KEY, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            dst.write_bytes(r.read()); print("  saved", dst, dst.stat().st_size, "bytes")
    except urllib.error.HTTPError as e:
        print("  HTTP", e.code, e.read().decode()[:200])

if len(segments) <= 1:
    tts(raw.strip(), base)
else:
    for i, seg in enumerate(segments, 1):
        tts(seg, base.with_name(f"{base.stem}_{i:02d}{base.suffix}"))
print("done. model:", MODEL, "voice:", VOICE[:6]+"...")
