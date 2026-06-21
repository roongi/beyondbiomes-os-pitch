from PIL import Image, ImageDraw
m = Image.open("/mnt/e/WSL/shared/pitches/media/handout_map_hero.jpg").convert("RGB")
lg = Image.open("/mnt/e/WSL/shared/LOGNEU.png").convert("RGBA")
W,H = m.size
d = int(W*0.135)                      # logo diameter ~13.5% of width
lg = lg.resize((d,d))
# circular mask (logo is a circle); honor existing alpha too
mask = Image.new("L",(d,d),0); ImageDraw.Draw(mask).ellipse((0,0,d,d),fill=255)
a = lg.split()[3]; mask = Image.composite(a, Image.new("L",(d,d),0), mask) if a else mask
mar = int(W*0.018)
m.paste(lg, (W-d-mar, H-d-mar), mask)
m.save("/mnt/e/WSL/shared/pitches/media/handout_map_hero.jpg", quality=90)
print("composited logo at", (W-d-mar, H-d-mar), "size", d)
