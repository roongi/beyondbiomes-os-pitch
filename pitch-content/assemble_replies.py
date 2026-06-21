#!/usr/bin/env python3
import re, glob, pathlib
R = "/mnt/e/WSL/shared/pitches/files (8)/Beyond_Biomes_Complete_Bundle/html_artifacts/replies"
OUT = pathlib.Path("/mnt/e/WSL/shared/pitches/_pitch_build/replies_prompt.txt")
def strip(t):
    t=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',t); t=re.sub(r'(?s)<[^>]+>',' ',t)
    t=re.sub(r'&[a-z]+;',' ',t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n\n',t); return t.strip()
parts=["""You are analyzing 13 personalized outreach replies/conversations between the Beyond Biomes founder (Dr. Ringo Schwabe) and people in his network/Skool community (each file named after a person).
Extract investor-grade SOCIAL PROOF and KPIs we can put on a handout - be HONEST, count only what is actually present, do not invent numbers.
Output Markdown:
1. SOCIAL-PROOF KPIs - countable signals (e.g. number of substantive expert conversations, breadth of roles/industries engaged, how many show clear interest/validation).
2. THEMES - the recurring reasons people find this compelling (the hooks that land).
3. TOP 6 VERBATIM QUOTES/signals of demand or validation (with the person's name).
4. ONE-LINE social-proof statement for the handout (honest, specific).
===== REPLIES ====="""]
for f in sorted(glob.glob(R+"/*.html")):
    parts.append(f"\n\n----- {pathlib.Path(f).stem} -----\n"+strip(open(f,encoding='utf-8',errors='ignore').read())[:6000])
OUT.write_text("\n".join(parts),encoding="utf-8"); print("wrote",OUT,OUT.stat().st_size,"bytes")
