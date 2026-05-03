from PIL import Image, ImageDraw, ImageFont
import os

def get_font(size, weight="regular"):
    font_map = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    return ImageFont.truetype(path, size) if os.path.exists(path) else ImageFont.load_default()

W, H = 1080, 1080
img = Image.new("RGBA", (W, H), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# Dark navy background
for y in range(H):
    t = y / H
    draw.line([(0, y), (W, y)], fill=(int(11+6*t), int(11+4*t), int(20+12*t), 255))

# Brand watermark
draw.text((48, 38), "IGEN VERITAS", fill=(255, 255, 255, 175), font=get_font(18))
draw.text((48, 62), "igenveritas.com", fill=(107, 114, 128, 160), font=get_font(14))

# Headline
draw.text((540, 110), "Your business closes at 6PM.", fill=(255, 255, 255, 255), font=get_font(44, "bold"), anchor="mm")
draw.text((540, 162), "Your competitor's doesn't.", fill=(123, 103, 209, 255), font=get_font(40, "bold"), anchor="mm")

# LEFT PANEL — "Your Business" (closed)
panel_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
pdl = ImageDraw.Draw(panel_l)
pdl.rounded_rectangle([40, 198, 492, 862], radius=20, fill=(18, 16, 10, 210))
img = Image.alpha_composite(img, panel_l)
draw = ImageDraw.Draw(img)

# CLOSED badge
draw.rounded_rectangle([178, 228, 354, 266], radius=10, fill=(110, 18, 18, 230))
draw.text((266, 247), "CLOSED", fill=(255, 75, 75, 255), font=get_font(18, "bold"), anchor="mm")

# 3x3 dark office windows
for row in range(3):
    for col in range(3):
        wx = 100 + col * 112
        wy = 300 + row * 105
        draw.rounded_rectangle([wx, wy, wx+82, wy+72], radius=6, fill=(6, 5, 4, 255), outline=(38, 28, 18, 200), width=1)

# 6:00 PM
draw.text((266, 648), "6:00 PM", fill=(185, 48, 48, 255), font=get_font(42, "bold"), anchor="mm")
draw.text((266, 696), "Office closed.", fill=(107, 114, 128, 220), font=get_font(20), anchor="mm")

# 0 leads badge
draw.rounded_rectangle([148, 732, 384, 772], radius=12, fill=(75, 14, 14, 200))
draw.text((266, 752), "0 new leads today", fill=(205, 78, 78, 255), font=get_font(18, "bold"), anchor="mm")

draw.text((266, 834), "YOUR BUSINESS", fill=(107, 114, 128, 190), font=get_font(17), anchor="mm")

# Violet glow behind right panel
glow_r = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gr = ImageDraw.Draw(glow_r)
for rad in range(220, 0, -2):
    a = int(45 * (1 - rad/220))
    gr.ellipse([816-rad, 530-rad, 816+rad, 530+rad], fill=(123, 103, 209, a))
img = Image.alpha_composite(img, glow_r)

# RIGHT PANEL — "Your Competitor"
panel_r = Image.new("RGBA", (W, H), (0, 0, 0, 0))
pdr = ImageDraw.Draw(panel_r)
pdr.rounded_rectangle([588, 198, 1040, 862], radius=20, fill=(20, 14, 36, 205), outline=(123, 103, 209, 110), width=2)
img = Image.alpha_composite(img, panel_r)
draw = ImageDraw.Draw(img)

# ONLINE 24/7 badge
draw.rounded_rectangle([638, 216, 836, 256], radius=10, fill=(18, 95, 48, 225))
draw.ellipse([650, 230, 664, 244], fill=(48, 195, 78, 255))
draw.text((746, 236), "ONLINE 24/7", fill=(195, 255, 195, 255), font=get_font(17, "bold"), anchor="mm")

# Chat bubbles
bubbles = [
    ("Hi, are you open? 👋", False, 296),
    ("Yes! How can I help you?", True, 354),
    ("I need a website quote", False, 412),
    ("Got it! Sending details now ✅", True, 470),
    ("Another lead incoming...", False, 528),
]
for text, is_bot, yp in bubbles:
    if is_bot:
        bx1, bx2 = 720, 1022; bg = (88, 58, 176, 205); tc = (222, 212, 255, 255)
    else:
        bx1, bx2 = 602, 892; bg = (38, 28, 58, 205); tc = (200, 195, 220, 255)
    draw.rounded_rectangle([bx1, yp-18, bx2, yp+22], radius=10, fill=bg)
    draw.text(((bx1+bx2)//2, yp+2), text, fill=tc, font=get_font(17), anchor="mm")

# Leads counter
draw.rounded_rectangle([608, 600, 1022, 658], radius=12, fill=(48, 28, 78, 185), outline=(123, 103, 209, 140), width=1)
draw.text((815, 622), "Leads captured tonight:", fill=(178, 158, 228, 255), font=get_font(16), anchor="mm")
draw.text((815, 646), "12 and counting 🚀", fill=(198, 178, 255, 255), font=get_font(18, "bold"), anchor="mm")

# 11:47 PM timestamp
draw.text((815, 726), "11:47 PM", fill=(123, 103, 209, 255), font=get_font(38, "bold"), anchor="mm")
draw.text((815, 776), "Still working for you.", fill=(178, 168, 218, 228), font=get_font(20), anchor="mm")

draw.text((815, 834), "YOUR COMPETITOR", fill=(123, 103, 209, 195), font=get_font(17), anchor="mm")

# VS badge center
draw.ellipse([498, 498, 582, 562], fill=(123, 103, 209, 255))
draw.text((540, 530), "VS", fill=(255, 255, 255, 255), font=get_font(26, "bold"), anchor="mm")

# Bottom section
draw.line([(78, 878), (1002, 878)], fill=(123, 103, 209, 140), width=1)
draw.text((540, 915), "AI chatbot — your business stays open long after you clock out.",
          fill=(178, 168, 220, 215), font=get_font(22), anchor="mm")

cta = Image.new("RGBA", (W, H), (0, 0, 0, 0))
cd = ImageDraw.Draw(cta)
cd.rounded_rectangle([282, 948, 798, 994], radius=22, fill=(123, 103, 209, 235))
img = Image.alpha_composite(img, cta)
draw = ImageDraw.Draw(img)
draw.text((540, 971), "DM us — find out how it works", fill=(255, 255, 255, 255), font=get_font(22, "bold"), anchor="mm")

draw.text((60, 1038), "IGEN VERITAS", fill=(255, 255, 255, 175), font=get_font(17))
draw.text((862, 1038), "igenveritas.com", fill=(107, 114, 128, 175), font=get_font(16))

os.makedirs("social-media", exist_ok=True)
img.convert("RGB").save("social-media/20260503_pain_CB002_business_closes_6pm.png", "PNG")
print("Saved: social-media/20260503_pain_CB002_business_closes_6pm.png")
