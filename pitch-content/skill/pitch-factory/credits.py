import os,re,json,urllib.request
k=os.environ.get("ELEVENLABS_API_KEY") or re.search(r'ELEVENLABS_API_KEY=(\S+)',open(os.path.expanduser("~/.elevenlabs/.env")).read()).group(1).strip()
d=json.load(urllib.request.urlopen(urllib.request.Request("https://api.elevenlabs.io/v1/user/subscription",headers={"xi-api-key":k}),timeout=30))
used=d.get("character_count",0); lim=d.get("character_limit",0)
print(f"Tier: {d.get('tier')}")
print(f"Used: {used:,} / {lim:,} chars  ->  REMAINING: {lim-used:,} characters")
print(f"Resets: {d.get('next_character_count_reset_unix')}")
print(f"~{(lim-used)//900} more ~3-min narrations left (≈900 chars/min spoken)")
