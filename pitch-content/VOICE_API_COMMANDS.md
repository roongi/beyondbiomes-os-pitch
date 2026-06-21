# ElevenLabs Voice API — integration & commands
_Generate the pitch narration from `gen_voice.py`. Settings tuned from your reference "Old Wizard – Deep, Engaging Storyteller" (stability 71 · style/boost 75)._

## STEP 1 — store the key securely (run in YOUR WSL terminal; do NOT paste the key into chat)
```bash
read -rs -p "Paste ELEVENLABS_API_KEY (hidden), then Enter: " ELEVENLABS_API_KEY; echo
umask 077; mkdir -p ~/.elevenlabs
printf 'export ELEVENLABS_API_KEY=%s\n' "$ELEVENLABS_API_KEY" > ~/.elevenlabs/.env; chmod 600 ~/.elevenlabs/.env
grep -q 'elevenlabs/.env' ~/.bashrc || printf '\n[ -f ~/.elevenlabs/.env ] && set -a && . ~/.elevenlabs/.env && set +a\n' >> ~/.bashrc
export ELEVENLABS_API_KEY
python3 -c 'import os,urllib.request as u;k=os.environ["ELEVENLABS_API_KEY"];r=u.urlopen(u.Request("https://api.elevenlabs.io/v1/user",headers={"xi-api-key":k}),timeout=20);print("KEY VALID ✅" if r.status==200 else "fail")'
unset ELEVENLABS_API_KEY
```

## STEP 2 — your "Old Wizard" voice_id (already found)
**`JoYo65swyP8hH6fVMeTO`** = Old Wizard – Deep, Engaging Storyteller (professional).
To re-list any time: `~/.venvs/bbmedia/bin/python list_voices.py`

> ⚠️ CONTEXT NOTE: the commands prefixed `wsl -d Ubuntu-new --` are for running **from Windows** (PowerShell / Git Bash). If you are **already inside the WSL Ubuntu shell** (`ringo007@...$`), DROP that wrapper and run the inner command directly (inside WSL, `wsl` is a different unrelated tool).

## STEP 3 — generate the narration (Claude or you can run this)
```bash
# the 3-min master pitch (v3), 3 segments -> bb_v3_01.mp3 / _02 / _03
MSYS_NO_PATHCONV=1 wsl -d Ubuntu-new -- /home/ringo007/.venvs/bbmedia/bin/python \
  /mnt/e/WSL/shared/pitches/_pitch_build/gen_voice.py \
  /mnt/e/WSL/shared/pitches/_pitch_build/voice_text/v3.txt \
  /mnt/e/WSL/shared/pitches/media/voice/bb_v3.mp3 \
  --voice <VOICE_ID> --model eleven_v3
```
- Other ready texts in `voice_text/`: `v1.txt`, `v2.txt`, `farmer.txt`, `scientist.txt`, `producer.txt`.
- Model: `eleven_v3` (best emotion/audio-tags) or `eleven_multilingual_v2` (closest to your reference). 
- Tune via env: `V_STAB` (0.6 default — lower = more expressive), `V_SIM` (0.8), `V_STYLE` (0.7).

## Notes
- `gen_voice.py` splits a text file on lines that are just `---` into segments (re-roll one without redoing all).
- Saves MP3s to `shared/pitches/media/voice/`. Hand them back and they wire into the app's per-section audio slots (PITCH_APP_INTEGRATION / TRAINING_APP_SPEC).
- The key never enters this chat or your shell history (`read -rs`; the command text holds no secret).
