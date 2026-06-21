#!/bin/bash
PY=/home/ringo007/.venvs/bbmedia/bin/python
G=/mnt/e/WSL/shared/pitches/_pitch_build/gen_voice.py
T=/mnt/e/WSL/shared/pitches/_pitch_build/voice_text
O=/mnt/e/WSL/shared/pitches/media/voice
V=JoYo65swyP8hH6fVMeTO
mkdir -p "$O"
for n in v3_3min v1 farmer scientist producer; do
  echo "=== $n ==="
  $PY "$G" "$T/$n.txt" "$O/bb_$n.mp3" --voice "$V" --model eleven_multilingual_v2
done
# concat the multi-segment ones
for n in v3_3min v1; do
  if ls "$O/bb_${n}_"*.mp3 >/dev/null 2>&1; then
    : > "$O/${n}_list.txt"
    for f in "$O/bb_${n}_"*.mp3; do echo "file '$f'" >> "$O/${n}_list.txt"; done
    ffmpeg -y -f concat -safe 0 -i "$O/${n}_list.txt" -c copy "$O/bb_${n}_full.mp3" 2>/dev/null && echo "concat $n OK"
  fi
done
echo "ALL DONE"; ls -la "$O"/*.mp3 | awk '{print $5,$9}'
