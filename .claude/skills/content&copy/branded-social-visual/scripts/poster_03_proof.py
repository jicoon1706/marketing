"""Poster 3 — Template C (Proof/Demo) | Wed Apr 30 | Bot Jawab. Lead Selamat."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "social-media/20260430_proof_bot-jawab-lead-selamat.png"
os.makedirs("social-media", exist_ok=True)

W, H = 1080, 1080
img = Image.new("RGBA", (W, H), (123, 103, 209, 255))
draw = ImageDraw.Draw(img)

# --- Gradient background ---
for y in range(H):
    t = y / H
    r = int(123 + (65 - 123) * t)
    g = int(103 + (150 - 103) * t)
    b = int(209 + (230 - 209) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

def font(size, weight="regular"):
    m = {"bold": "C:/Windows/Fonts/segoeuib.ttf",
         "regular": "C:/Windows/Fonts/segoeui.ttf",
         "light": "C:/Windows/Fonts/segoeuil.ttf"}
    p = m.get(weight, m["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

# --- Brand badge top-left ---
draw.rounded_rectangle([50, 48, 310, 90], radius=20, fill=(255, 255, 255, 230))
draw.text((180, 69), "IGEN VERITAS", fill=(11, 11, 20, 220), font=font(20, "bold"), anchor="mm")

# --- Headline ---
draw.text((540, 168), "Bot Jawab.", fill=(255, 255, 255, 255), font=font(88, "bold"), anchor="mm")
draw.text((540, 268), "Lead Selamat.", fill=(11, 11, 20, 230), font=font(88, "bold"), anchor="mm")

# ============================================================
# WhatsApp chat card
# ============================================================
card_x1, card_y1, card_x2, card_y2 = 100, 320, 980, 870
# Drop shadow
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle([card_x1 + 8, card_y1 + 8, card_x2 + 8, card_y2 + 8], radius=28, fill=(0, 0, 0, 60))
img = Image.alpha_composite(img, shadow)
draw = ImageDraw.Draw(img)

draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=28, fill=(255, 255, 255, 255))

# WhatsApp header bar
draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y1 + 76], radius=0, fill=(37, 211, 102, 255))
# Clip top corners
draw.rectangle([card_x1, card_y1, card_x1 + 28, card_y1 + 76], fill=(37, 211, 102, 255))
draw.rectangle([card_x2 - 28, card_y1, card_x2, card_y1 + 76], fill=(37, 211, 102, 255))
draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y1 + 76], radius=28, fill=(37, 211, 102, 255))

# Avatar circle
draw.ellipse([120, card_y1 + 14, 168, card_y1 + 62], fill=(255, 255, 255, 200))
draw.text((144, card_y1 + 38), "S", fill=(37, 211, 102, 255), font=font(26, "bold"), anchor="mm")
draw.text((185, card_y1 + 30), "IGEN AI Bot", fill=(255, 255, 255, 255), font=font(22, "bold"))
draw.text((185, card_y1 + 54), "● Online", fill=(144, 238, 144, 255), font=font(17))

# --- Chat bubbles ---
bubble_y = card_y1 + 100

def customer_bubble(draw, y, text, time_txt):
    bw = min(len(text) * 13 + 40, 620)
    x1, y1 = card_x1 + 30, y
    x2, y2 = x1 + bw, y + 56
    draw.rounded_rectangle([x1, y1, x2, y2], radius=18, fill=(240, 240, 245, 255))
    draw.text((x1 + 16, (y1 + y2) // 2), text, fill=(30, 30, 40, 220), font=font(21), anchor="lm")
    draw.text((x2 - 8, y2 + 6), time_txt, fill=(150, 150, 160, 200), font=font(16), anchor="rm")
    return y2 + 20

def bot_bubble(draw, y, text, time_txt, badge=None):
    bw = min(len(text) * 13 + 40, 650)
    x2, y1 = card_x2 - 30, y
    x1, y2 = x2 - bw, y + 56
    draw.rounded_rectangle([x1, y1, x2, y2], radius=18, fill=(123, 103, 209, 220))
    draw.text((x1 + 16, (y1 + y2) // 2), text, fill=(255, 255, 255, 255), font=font(21), anchor="lm")
    if badge:
        bx1, by1 = x1 + 12, y2 + 4
        bx2, by2 = bx1 + len(badge) * 10 + 30, by1 + 26
        draw.rounded_rectangle([bx1, by1, bx2, by2], radius=10, fill=(37, 211, 102, 200))
        draw.text((bx1 + 10, (by1 + by2) // 2), badge, fill=(255, 255, 255, 255), font=font(14, "bold"), anchor="lm")
        draw.text((x2 - 8, by2 + 4), time_txt, fill=(200, 200, 220, 200), font=font(16), anchor="rm")
        return by2 + 16
    draw.text((x2 - 8, y2 + 6), time_txt, fill=(200, 200, 220, 200), font=font(16), anchor="rm")
    return y2 + 20

bubble_y = customer_bubble(draw, bubble_y, "Helo, saya nak tanya pasal pakej chatbot...", "3:01 AM")
bubble_y = bot_bubble(draw, bubble_y + 4, "Hi! Saya AI IGEN VERITAS. Boleh bantu 24/7!", "3:01 AM")
bubble_y = customer_bubble(draw, bubble_y + 4, "Berapa harga pakej Basic?", "3:02 AM")
bubble_y = bot_bubble(draw, bubble_y + 4, "Basic: RM 500 setup + RM 150/bulan ✓", "3:02 AM",
    badge="✅ Lead saved to Google Sheets")

# Powered by label
draw.text((card_x2 - 20, card_y2 - 18), "Powered by IGEN VERITAS",
    fill=(150, 150, 170, 180), font=font(16), anchor="rm")

# --- Stat strip ---
stats = [("24/7", "Active"), ("< 3s", "Reply"), ("100%", "Auto"), ("0", "Missed Leads")]
strip_y = 890
sw = (W - 120) // 4
for i, (val, lbl) in enumerate(stats):
    sx = 60 + i * sw + sw // 2
    draw.rounded_rectangle([60 + i * sw + 10, strip_y, 60 + (i + 1) * sw - 10, strip_y + 80],
        radius=16, fill=(255, 255, 255, 30))
    draw.text((sx, strip_y + 26), val, fill=(255, 255, 255, 255), font=font(26, "bold"), anchor="mm")
    draw.text((sx, strip_y + 58), lbl, fill=(255, 255, 255, 160), font=font(18), anchor="mm")

# --- Bottom brand ---
draw.text((540, 1010), "IGEN VERITAS  |  igen-veritas.com  |  +60 17 310 3966",
    fill=(255, 255, 255, 140), font=font(17), anchor="mm")

img.save(OUT, "PNG")
print(f"Saved: {OUT}")
