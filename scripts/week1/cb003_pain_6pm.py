from PIL import Image, ImageDraw, ImageFont
import os

img = Image.new("RGBA", (1080, 1080), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# Full dark navy base
for y in range(1080):
    t = y / 1080
    r = int(11 + (8 - 11) * t)
    g = int(11 + (8 - 11) * t)
    b = int(20 + (25 - 20) * t)
    draw.line([(0, y), (1080, y)], fill=(r, g, b, 255))

def get_font(size, weight="regular"):
    font_map = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    return ImageFont.truetype(path, size) if os.path.exists(path) else ImageFont.load_default()

# LEFT PANEL — "Your business" (dark, closed office)
left_panel = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
ld = ImageDraw.Draw(left_panel)
# Dark panel with slight warm tint
for y in range(200, 860):
    alpha = 200
    ld.line([(40, y), (490, y)], fill=(20, 12, 8, alpha))
left_panel_rounded = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
lrd = ImageDraw.Draw(left_panel_rounded)
lrd.rounded_rectangle([40, 200, 490, 860], radius=20, fill=(18, 10, 8, 210))
img = Image.alpha_composite(img, left_panel_rounded)

# Right panel — "Competitor's" (glowing, active)
right_glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
rgd = ImageDraw.Draw(right_glow)
for i in range(25, 0, -1):
    alpha = int(14 * (i / 25))
    rs = i * 16
    rgd.ellipse([765 - rs, 530 - rs, 765 + rs, 530 + rs], fill=(123, 103, 209, alpha))
img = Image.alpha_composite(img, right_glow)

right_panel = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
rpd = ImageDraw.Draw(right_panel)
rpd.rounded_rectangle([590, 200, 1040, 860], radius=20, fill=(20, 15, 45, 220),
                       outline=(123, 103, 209, 100))
img = Image.alpha_composite(img, right_panel)
draw = ImageDraw.Draw(img)

# ---- LEFT PANEL CONTENT ----
# "CLOSED" sign
draw.rounded_rectangle([160, 270, 370, 310], radius=6, fill=(120, 40, 40, 200))
draw.text((265, 290), "CLOSED", fill=(255, 100, 100, 255), font=get_font(22, "bold"), anchor="mm")

# Office icon — simplified window/building
for row in range(3):
    for col in range(3):
        wx = 130 + col * 80
        wy = 360 + row * 90
        draw.rounded_rectangle([wx, wy, wx + 50, wy + 60], radius=4, fill=(30, 20, 15, 255),
                                outline=(50, 40, 35, 180))
        # Darker windows (office closed)
        draw.rectangle([wx + 8, wy + 8, wx + 42, wy + 52], fill=(15, 10, 8, 255))

# "6:00 PM" timestamp
draw.text((265, 650), "6:00 PM", fill=(150, 80, 80, 255), font=get_font(42, "bold"), anchor="mm")
draw.text((265, 702), "Office closed.", fill=(107, 114, 128, 255), font=get_font(20, "regular"), anchor="mm")

# Zero leads indicator
draw.rounded_rectangle([130, 740, 400, 790], radius=10, fill=(60, 20, 20, 180))
draw.text((265, 765), "0 new leads today", fill=(200, 80, 80, 255), font=get_font(22, "regular"), anchor="mm")

# Left label
draw.text((265, 835), "YOUR BUSINESS", fill=(107, 114, 128, 255), font=get_font(18, "regular"), anchor="mm")

# ---- RIGHT PANEL CONTENT ----
# "ONLINE 24/7" badge
draw.rounded_rectangle([640, 230, 820, 268], radius=14, fill=(40, 180, 100, 180))
draw.ellipse([648, 244, 660, 256], fill=(80, 255, 120, 255))
draw.text((740, 249), "ONLINE 24/7", fill=(255, 255, 255, 255), font=get_font(18, "bold"), anchor="mm")

# Chat bubbles — incoming leads
bubbles = [
    ("Hi, are you open? 👋", True, 300),
    ("Yes! How can I help you?", False, 370),
    ("I need a website quote", True, 440),
    ("Got it! Sending details now ✅", False, 510),
    ("Another lead incoming...", True, 580),
]
for text, is_customer, by in bubbles:
    bubble_font = get_font(17, "regular")
    bb = draw.textbbox((0, 0), text, font=bubble_font)
    tw = min(bb[2] - bb[0], 320)
    pad = 12
    if is_customer:
        bx = 620
        bfill = (40, 35, 70, 220)
        border = (123, 103, 209, 80)
    else:
        bx = 1020 - tw - pad * 2
        bfill = (123, 103, 209, 200)
        border = (0, 0, 0, 0)
    draw.rounded_rectangle([bx, by, bx + tw + pad * 2, by + 40],
                            radius=12, fill=bfill, outline=border)
    draw.text((bx + pad, by + 20), text[:40], fill=(255, 255, 255, 230),
              font=bubble_font, anchor="lm")

# Leads captured counter
draw.rounded_rectangle([620, 640, 1020, 720], radius=12, fill=(40, 30, 80, 180),
                        outline=(123, 103, 209, 100))
draw.text((820, 663), "Leads captured tonight", fill=(180, 180, 210, 255),
          font=get_font(17, "regular"), anchor="mm")
draw.text((820, 698), "12 and counting 🚀", fill=(123, 103, 209, 255),
          font=get_font(26, "bold"), anchor="mm")

# Time indicator
draw.text((820, 762), "11:47 PM", fill=(123, 103, 209, 255), font=get_font(38, "bold"), anchor="mm")
draw.text((820, 810), "Still working for you.", fill=(180, 180, 210, 255),
          font=get_font(20, "regular"), anchor="mm")

# Right label
draw.text((820, 840), "YOUR COMPETITOR", fill=(123, 103, 209, 200), font=get_font(18, "regular"), anchor="mm")

# ---- CENTER DIVIDER ----
draw.line([(530, 200), (560, 860)], fill=(123, 103, 209, 0))
# VS badge
vs_bg = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
vs_d = ImageDraw.Draw(vs_bg)
vs_d.ellipse([505, 505, 575, 555], fill=(123, 103, 209, 255))
img = Image.alpha_composite(img, vs_bg)
draw = ImageDraw.Draw(img)
draw.text((540, 530), "VS", fill=(255, 255, 255, 255), font=get_font(26, "bold"), anchor="mm")

# ---- TOP HEADLINE ----
draw.text((540, 110), "Your business closes at 6PM.", fill=(255, 255, 255, 255),
          font=get_font(44, "bold"), anchor="mm")
draw.text((540, 162), "Your competitor's doesn't.", fill=(123, 103, 209, 255),
          font=get_font(40, "bold"), anchor="mm")

# ---- BOTTOM CTA ----
draw.line([(100, 885), (980, 885)], fill=(123, 103, 209, 60), width=1)
draw.text((540, 920), "AI chatbot — your business stays open long after you clock out.",
          fill=(180, 180, 200, 255), font=get_font(22, "regular"), anchor="mm")

# CTA pill
btn_w = 380
btn_bg = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
btn_d = ImageDraw.Draw(btn_bg)
btn_d.rounded_rectangle([540 - btn_w // 2, 958, 540 + btn_w // 2, 1008],
                         radius=24, fill=(123, 103, 209, 255))
img = Image.alpha_composite(img, btn_bg)
draw = ImageDraw.Draw(img)
draw.text((540, 983), "DM us — find out how it works",
          fill=(255, 255, 255, 255), font=get_font(22, "bold"), anchor="mm")

# Brand tag
draw.text((60, 1042), "IGEN VERITAS", fill=(255, 255, 255, 140), font=get_font(16, "regular"))
draw.text((1020, 1042), "igen-veritas.com", fill=(107, 114, 128, 255), font=get_font(15, "regular"), anchor="ra")

os.makedirs("social-media", exist_ok=True)
img = img.convert("RGB")
img.save("social-media/20260503_pain_CB003_6pm.png", "PNG")
print("Saved: social-media/20260503_pain_CB003_6pm.png")
