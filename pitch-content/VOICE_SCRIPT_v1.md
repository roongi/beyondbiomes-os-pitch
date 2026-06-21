# Beyond Biomes — ElevenLabs Voice Script · v1
_For generating the pitch-app narration. Mirrors PITCH_MASTER_v1 but rewritten for text-to-speech: numbers as words, phonetic spellings, pacing via punctuation + v3 audio tags._

## Recommended voice settings
- **Voice:** your cloned **"Old Wizard – Deep, Engaging Storyteller"** (PVC). It's the right timbre for "letting them in on something true."
- **Model:** **Eleven v3** (best at audio tags + emotion) for the hero take; **v2 / Multilingual v2** as a fallback if you want the *exact* reference sound.
- **Settings (start from your reference, nudged for a pitch):**
  - Reference was `speed 100 · stability 71 · style 75` (sb = style boost). 
  - **For the pitch use: Speed 96–100 (slightly slower = more authority) · Stability 60–65 (a touch more expressive than 71 so the "blind" / "we bend time" beats land) · Similarity 80 · Style 65–75.**
  - Keep **Speaker Boost ON.**
- **Why lower stability a little:** higher stability = flatter/safer; a pitch needs the emotional swings (quiet open → punch on numbers → intimate close). If it gets wobbly, raise back toward 70.
- **Generate in 3 segments** (open / body / close) so you can re-roll one part without redoing all — and because `bb-pitch-show` currently hard-caps ElevenLabs at ≤5 calls. Generate offline, save the MP3s, then drop them into the app (see PITCH_APP_INTEGRATION).

## Pronunciation cheat-sheet (set these as ElevenLabs pronunciation dictionary or spell inline)
- RhizoGenie → **Rhizo-Genie** ("RYE-zoh-jee-nee")
- Cavalcante → **Cah-val-CAHN-teh**
- Bochum → **BOH-hum**
- Beyond Biomes → keep as is ("By-omes")
- EXIST → say **"the EXIST programme"** (reads as the word "exist")
- R² → write **"R-squared zero point six eight"** / **"zero point eight five"**
- microbiome → "MY-kro-by-ome"

---

## THE TTS SCRIPT (paste this; tags in [brackets] are v3 audio tags)

[warm]
I'm Doctor Ringo Schwabe. [pause] And — what a time to be alive.

The machines around us get smarter every month, and the whole world is racing for the best model. [pause] But Gartner says over forty percent of A-I projects will be cancelled by twenty twenty-seven. Not because the models are weak. [slow] Because they're … blind.

[firm] So our rule is one line. Eyes before muscle. [pause] Read the system before you change it.

[pause]

Start with the oldest system we farm — the soil. The whole industry treats a living microbiome as flat chemistry. Nitrogen, phosphorus, potassium, p-H. That tells you what's there … never what's missing. So billions in biological products get applied … blind.

[pause]

And three people stand around every field who have never been in the same conversation. [warm] The farmer — who knows his land by hand, but cannot see the biology beneath it. [pause] The scientist — who knows exactly what's failing … but is nowhere near the field. [pause] The producer — who sells a cure … and prays it works.

[pause]

Beyond Biomes puts all three in one loop. The farmer sends soil; our platform reads not who is living in it … but what they're doing. Seventeen A-I agents. Two hundred twenty-one models. Running on our own servers for thirty euros a month. [excited] And it's already live — fifteen thousand real samples, crop-disease detection at ninety-seven percent. [warm] Like a doctor for the soil. We diagnose, we prescribe, and we treat.

[pause]

Here's the part everyone fails at. Sixty to seventy percent of single strains die in the field. [firm] We don't guess. We measure the field's stress first … then design the exact living consortium built to survive it. Our published strains lifted nutrient uptake over three hundred percent. [slow] Peer-reviewed.

[pause]

And the value splits cleanly. The farmer gets the yield — a target of twenty to twenty-five percent more, with a third less fertiliser. The producer pays us to prove and tailor his product. One of them — Doctor Cah-val-CAHN-teh, who sells biofertiliser in thirty-five countries — just signed to white-label through us. And every paid field sends data back … that sharpens the next.

[pause]

This is real today. Five signed letters of intent. A twelve-hundred-hectare German cooperative. And because we run fields in both hemispheres — winter here, summer there — our system re-trains every six months … not once a year. [slow] We bend time.

[pause]

But soil is only the first system. The engine underneath it — our agentic layer — is a system that builds systems. Fifteen hundred commits of infrastructure that has already spun up four other businesses … from lab science to construction. [warm] Soil is the first machine off the line. The same factory builds the next.

[pause]

The team to do it: the scientist who invented the method, a Nature Communications lead author, the engineer who built the platform, and an operator who has closed a hundred and twenty agri-deals in Latin America. Out of Ruhr-University Bochum. EXIST-funded.

[pause]

And we're honest about proof. Our model is at R-squared zero point six eight today. This round funds the exact six-hundred-metagenome trial — across Germany, Chile, and Spain — to reach the zero point eight five field standard. [firm] We fund the proof. We don't assume it.

[pause]

[slow] So the ask. One … and a half … million euros. To buy an industry its eyes.

[pause]

[whispers] Read the system before you change it.

[pause] Thank you.

---

## Segment split for generation (re-roll friendly)
- **Segment A (open):** from "I'm Doctor Ringo Schwabe" → "…and prays it works." (~0:00–1:00)
- **Segment B (body):** "Beyond Biomes puts all three…" → "…The same factory builds the next." (~1:00–2:34)
- **Segment C (close):** "The team to do it…" → "Thank you." (~2:34–3:00)

## After you generate
Save as `bb_pitch_v1_full.mp3` (and A/B/C parts) in `shared/pitches/`. Hand them back and I'll wire them into the pitch app. If a beat sounds off, tell me the exact line and I'll adjust the tag/pacing — that's a 1-line change in this file.
