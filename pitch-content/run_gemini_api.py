#!/usr/bin/env python3
"""Call Gemini text API directly with the VALID key from ~/.gemini/.env (bypasses the CLI's stale key).
Usage: python run_gemini_api.py PROMPT_FILE OUT_FILE [model]
"""
import os, re, sys
from google import genai

def load_key():
    k = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if k and not k.startswith("AIza") is False:  # prefer .env value regardless
        pass
    # always prefer the .env value (the validated AQ.A key)
    try:
        m = re.search(r'GEMINI_API_KEY=(\S+)', open(os.path.expanduser("~/.gemini/.env")).read())
        if m: return m.group(1).strip().strip('"').strip("'")
    except Exception: pass
    return k

prompt_file, out_file = sys.argv[1], sys.argv[2]
models = [sys.argv[3]] if len(sys.argv) > 3 else ["gemini-2.5-pro","gemini-3-pro","gemini-flash-latest","gemini-2.5-flash"]
prompt = open(prompt_file, encoding="utf-8").read()
client = genai.Client(api_key=load_key())

for M in models:
    try:
        r = client.models.generate_content(model=M, contents=prompt)
        txt = r.text or ""
        if txt.strip():
            open(out_file, "w", encoding="utf-8").write(txt)
            print(f"OK via {M}: {len(txt)} chars -> {out_file}")
            sys.exit(0)
    except Exception as e:
        print(f"{M} failed: {str(e)[:140]}")
sys.exit("all models failed")
