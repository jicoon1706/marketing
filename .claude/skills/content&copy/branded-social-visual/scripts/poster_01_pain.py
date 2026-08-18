"""Poster 1 — Template A (Pain Point) | Mon Apr 28 | Leads Masuk. Kau Tidur."""
from PIL import Image, ImageDraw, ImageFont
import os, math

OUT = "social-media/20260428_pain_leads-masuk-kau-tidur.png"
os.makedirs("social-media", exist_ok=True)

W, H = 1080, 1080
img = Image.new("RGBA", (W, H), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# --- Background: dark navy with violet radial glow ---
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(420, 0, -1):
    alpha = int(55 * (1 - r / 420) ** 1.6)
    cx, cy = 300, 480
    gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(123, 103, 209, alpha))
img = Image.alpha_composite(img, glow)
draw = ImageDraw.Draw(img)

# subtle top-right secondary glow (blue)
glow2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd2 = ImageDraw.Draw(glow2)
for r in range(280, 0, -1):
    alpha = int(25 * (1 - r / 280) ** 2)
    gd2.ellipse([W - 280 - r, 200 - r, W - 280 + r, 200 + r], fill=(65, 150, 230, alpha))
img = Image.alpha_composite(img, glow2)
draw = ImageDraw.Draw(img)

def font(size, weight="regular"):
    m = {"bold": "C:/Windows/Fonts/segoeuib.ttf",
         "regular": "C:/Windows/Fonts/segoeui.ttf",
         "light": "C:/Windows/Fonts/segoeuil.ttf"}
    p = m.get(weight, m["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

# --- Brand label top-left ---
draw.text((60, 58), "IGEN VERITAS", fill=(255, 255, 255, 180), font=font(22, "bold"))
draw.text((60, 86), "igen-veritas.com", fill=(107, 114, 128, 255), font=font(18))

# --- Main headline ---
f_xl = font(100, "bold")
f_lg = font(90, "bold")

# Line 1: "Leads Masuk." — white
draw.text((540, 310), "Leads Masuk.", fill=(255, 255, 255, 255), font=f_xl, anchor="mm")
# Line 2: "Kau Tidur." — violet accent
draw.text((540, 420), "Kau Tidur.", fill=(123, 103, 209, 255), font=f_xl, anchor="mm")

# --- Glassmorphism stat card ---
cx1, cy1, cx2, cy2 = 180, 490, 900, 720
card = Image.new("RGBA", (W, H), (0, 0, 0, 0))
cd = ImageDraw.Draw(card)
cd.rounded_rectangle([cx1, cy1, cx2, cy2], radius=28,
    fill=(255, 255, 255, 13), outline=(255, 255, 255, 28))
img = Image.alpha_composite(img, card)
draw = ImageDraw.Draw(img)

# Time pill
draw.rounded_rectangle([210, 520, 420, 570], radius=14, fill=(255, 255, 255, 20), outline=(255, 255, 255, 40))
draw.text((315, 545), "3:14 AM", fill=(255, 255, 255, 220), font=font(26, "bold"), anchor="mm")

# Red "0 Leads" badge
draw.rounded_rectangle([450, 520, 680, 570], radius=14, fill=(220, 38, 38, 200))
draw.text((565, 545), "0 Leads Captured", fill=(255, 255, 255, 255), font=font(22, "bold"), anchor="mm")

# Unread message block
draw.rounded_rectangle([210, 590, 870, 700], radius=18, fill=(255, 255, 255, 8), outline=(255, 255, 255, 18))
for i, (msg, t) in enumerate([
    ("Saya nak tahu lebih lanjut tentang pakej you...", "3:01 AM"),
    ("Hello? Ada orang tak?", "3:14 AM"),
]):
    y = 613 + i * 40
    draw.text((240, y), f"💬  {msg}", fill=(200, 200, 220, 200), font=font(20))
    draw.text((840, y), t, fill=(107, 114, 128, 200), font=font(18), anchor="ra")

# --- Subtext ---
draw.text((540, 760), "Setiap minit tanpa jawapan = lead yang hilang.",
    fill=(107, 114, 128, 255), font=font(26), anchor="mm")

# --- CTA pill button ---
draw.rounded_rectangle([340, 820, 740, 884], radius=32, fill=(123, 103, 209, 255))
draw.text((540, 852), "DM 'INFO' sekarang  →", fill=(255, 255, 255, 255), font=font(28, "bold"), anchor="mm")

# --- Bottom brand strip ---
draw.line([(60, 940), (1020, 940)], fill=(255, 255, 255, 25), width=1)
draw.text((540, 975), "IGEN VERITAS  |  AI Automation for Malaysian SMEs  |  igen-veritas.com",
    fill=(107, 114, 128, 200), font=font(18), anchor="mm")

img.save(OUT, "PNG")
print(f"Saved: {OUT}")
