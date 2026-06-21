#!/usr/bin/env bash
# Re-exporta el deck Marp a PPTX (usa el Chromium de puppeteer, sin sudo).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
CHROME="$(ls -d "$HOME"/.cache/puppeteer/chrome/*/chrome-linux64/chrome 2>/dev/null | head -1)"
[ -z "$CHROME" ] && { echo "Falta Chromium de puppeteer. Corre: cd ~/tools/marp && npx puppeteer browsers install chrome"; exit 1; }
CHROME_PATH="$CHROME" npx --prefix "$HOME/tools/marp" marp "$HERE/pitch.md" --theme "$HERE/theme/beyondbiomes.css" --pptx --allow-local-files -o "$HERE/BeyondBiomes-Pitch.pptx"
echo "✓ $HERE/BeyondBiomes-Pitch.pptx"
