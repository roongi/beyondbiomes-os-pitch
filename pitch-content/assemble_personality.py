#!/usr/bin/env python3
import re, pathlib
B = pathlib.Path("/mnt/e/WSL/shared/pitches/Beyond_Biomes_Complete_Bundle")
OUT = pathlib.Path("/mnt/e/WSL/shared/pitches/_pitch_build/personality_prompt.txt")

def strip_html(t):
    t = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', t)
    t = re.sub(r'(?s)<[^>]+>', ' ', t)
    t = re.sub(r'&[a-z]+;', ' ', t)
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n\n', t)
    return t.strip()

def read(p, html=False, cap=None):
    try:
        t = pathlib.Path(p).read_text(encoding="utf-8", errors="ignore")
        if html: t = strip_html(t)
        return t[:cap] if cap else t
    except Exception as e:
        return f"[missing {p}: {e}]"

INSTR = """You are a brand-narrative strategist for Beyond Biomes, a deep-tech startup pitching investors (IDEA.2026 + VC seed).
From the raw materials below (founder conversation transcript, the Beyond Biomes story site, the existing illustrated "maps" incl. the antique 'Jack' style, the image prompts, and personalized outreach replies), extract the PERSONALITY and the NARRATIVE that takes an investor emotionally from NATURE to an AI-NATIVE COMPANY.

Output ONLY this, in Markdown:
1. BRAND PERSONALITY — voice, values, tone, what makes Dr. Ringo Schwabe and Beyond Biomes distinctive; 8-10 signature phrasings quoted verbatim from the transcript/replies.
2. THE NATURE -> AI-NATIVE ARC — 5-7 story beats (nature solved reliability -> we read it -> we built an AI-native platform that reads/acts like nature -> it builds systems) ready to thread through a 3-min pitch.
3. THE PERFECT INVESTOR STORY — the single emotional + logical throughline (one paragraph) + the 3 metaphors that make it click.
4. PERSONALITY STYLE-GUIDE for writing the 3 PLATFORM persona scripts (farmer / scientist / producer) and the voice: tone per persona, do/don't, signature words.
5. WHAT THE 'JACK' MAP STYLE + PROMPTS TELL US — the visual personality to keep.
Be specific and quote real phrasings. Do not invent facts; this is about voice/story, honesty rules still apply (patent-pending, targets are targets).

===== RAW MATERIALS =====
"""

parts = [INSTR]
parts.append("----- FOUNDER CONVERSATION TRANSCRIPT -----\n" + read(B/"source/Full_Conversation_Transcript.txt"))
parts.append("\n\n----- BEYOND BIOMES STORY (full) -----\n" + read(B/"html_artifacts/beyond_biomes_full.html", html=True))
parts.append("\n\n----- STORY INDEX -----\n" + read(B/"html_artifacts/index.html", html=True, cap=12000))
for m in ["map-antique-jack.html","map-strata.html","map-observability-os.html","prompts.html"]:
    parts.append(f"\n\n----- MAP/PROMPT: {m} -----\n" + read(B/"html_artifacts/maps"/m, html=True, cap=8000))
for r in ["jack-calibratedai.html","daniel-fazio.html","florian-rolke.html","sean-murphy.html"]:
    parts.append(f"\n\n----- REPLY: {r} -----\n" + read(B/"html_artifacts/replies"/r, html=True, cap=6000))

OUT.write_text("\n".join(parts), encoding="utf-8")
print("wrote", OUT, OUT.stat().st_size, "bytes")
