#!/usr/bin/env python3
import os, re, json, urllib.request
def key():
    k=os.environ.get("ELEVENLABS_API_KEY")
    if k: return k
    return re.search(r'ELEVENLABS_API_KEY=(\S+)', open(os.path.expanduser("~/.elevenlabs/.env")).read()).group(1).strip().strip('"').strip("'")
req=urllib.request.Request("https://api.elevenlabs.io/v1/voices", headers={"xi-api-key":key()})
data=json.load(urllib.request.urlopen(req, timeout=30))
for v in data.get("voices",[]):
    print(f'{v["voice_id"]}  -  {v["name"]}  [{v.get("category","")}]')
