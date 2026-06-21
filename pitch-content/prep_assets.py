import os, pathlib
from PIL import Image
import qrcode
A = pathlib.Path("/mnt/e/WSL/shared/pitches/handout/assets"); A.mkdir(parents=True, exist_ok=True)
SH = "/mnt/e/WSL/shared"
def resize(src, dst, w=1600):
    try:
        im = Image.open(src); im=im.convert("RGB")
        if im.width>w: im=im.resize((w,int(im.height*w/im.width)))
        im.save(dst, quality=88); print("resized", dst, im.size)
    except Exception as e: print("skip", src, e)
for s,d in [("eng_org.jpg","eng_org.jpg"),("eng_BMC.jpg","eng_bmc.jpg"),("revenue.jpg","revenue.jpg"),
            ("eng_journey.jpg","eng_journey.jpg"),("openapi_eng.jpg","openapi.jpg")]:
    resize(f"{SH}/{s}", A/d)
resize("/mnt/e/WSL/shared/pitches/media/handout_page1.jpg", A/"page1.jpg", 1920)
# QR codes
def qr(data, dst):
    q=qrcode.QRCode(box_size=10,border=2); q.add_data(data); q.make()
    img=q.make_image(fill_color="#0B2545",back_color="white"); img.save(dst); print("qr",dst)
qr("https://review.beyondbiomes.de", A/"qr_demo.png")
qr("https://beyondbiomes.de", A/"qr_site.png")
print("done")
