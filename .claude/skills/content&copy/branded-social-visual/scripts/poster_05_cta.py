"""Poster 5 — Template D (CTA/Packages) | Sat May 3 | Pilih Pakej. Automate Sekarang."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "social-media/20260503_cta_pakej-ai-chatbot-reveal.png"
os.makedirs("social-media", exist_ok=True)

W, H = 1080, 1080
img = Image.new("RGBA", (W, H), (123, 103, 209, 255))
draw = ImageDraw.Draw(img)

# --- Gradient #7B67D1 → #8A5DCC (purple-to-purple deeper) ---
for y in range(H):
    t = y / H
    r = int(123 + (138 - 123) * t)
    g = int(103 + (93 - 103) * t)
    b = int(209 + (204 - 209) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# Dark overlay at bottom for depth
for y in range(700, H):
    t = (y - 700) / (H - 700)
    alpha = int(80 * t)
    draw.line([(0, y), (W, y)], fill=(11, 11, 20, alpha))

def font(size, weight="regular"):
    m = {"bold": "C:/Windows/Fonts/segoeuib.ttf",
         "regular": "C:/Windows/Fonts/segoeui.ttf",
         "light": "C:/Windows/Fonts/segoeuil.ttf"}
    p = m.get(weight, m["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

# --- Brand label ---
draw.text((60, 52), "IGEN VERITAS", fill=(255, 255, 255, 210), font=font(22, "bold"))
draw.text((60, 80), "igen-veritas.com", fill=(255, 255, 255, 130), font=font(18))

# --- Headline ---
draw.text((540, 156), "Pilih Pakej.", fill=(255, 255, 255, 255), font=font(84, "bold"), anchor="mm")
draw.text((540, 252), "Automate", fill=(72, 143, 227, 255), font=font(84, "bold"), anchor="mm")
draw.text((540, 348), "Sekarang.", fill=(255, 255, 255, 255), font=font(84, "bold"), anchor="mm")

# ============================================================
# 3 Package Cards
# ============================================================
packages = [
    {
        "name": "Basic",
        "setup": "RM 500",
        "monthly": "RM 150 / bulan",
        "features": ["AI chatbot (Botpress)", "Website integration", "FAQ knowledge base", "Email leads alert"],
        "highlight": False,
        "color": (255, 255, 255, 20),
        "border": (255, 255, 255, 40),
    },
    {
        "name": "Growth",
        "setup": "RM 1,000",
        "monthly": "RM 300 / bulan",
        "features": ["Everything in Basic", "n8n automation flows", "Google Sheets CRM", "WhatsApp follow-up"],
        "highlight": True,
        "color": (123, 103, 209, 180),
        "border": (123, 103, 209, 255),
    },
    {
        "name": "Pro",
        "setup": "RM 2,000",
        "monthly": "RM 500 / bulan",
        "features": ["Everything in Growth", "Full n8n workflows", "Custom AI logic", "Priority support"],
        "highlight": False,
        "color": (255, 255, 255, 20),
        "border": (255, 255, 255, 40),
    },
]

card_w = 300
card_h = 390
gap = 30
total_w = 3 * card_w + 2 * gap
start_x = (W - total_w) // 2
card_y = 390

for i, pkg in enumerate(packages):
    cx = start_x + i * (card_w + gap)
    cy = card_y

    # Glow for highlighted card
    if pkg["highlight"]:
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        for offset in range(18, 0, -1):
            alpha = int(30 * (1 - offset / 18))
            gd.rounded_rectangle([cx - offset, cy - offset,
                                   cx + card_w + offset, cy + card_h + offset],
                radius=24 + offset, fill=(123, 103, 209, alpha))
        img = Image.alpha_composite(img, glow)
        draw = ImageDraw.Draw(img)

    # Card background
    draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=22,
        fill=pkg["color"], outline=pkg["border"], width=2 if not pkg["highlight"] else 3)

    # Popular badge
    if pkg["highlight"]:
        draw.rounded_rectangle([cx + 80, cy - 18, cx + 220, cy + 18], radius=12,
            fill=(255, 255, 255, 255))
        draw.text((cx + 150, cy), "MOST POPULAR", fill=(123, 103, 209, 255),
            font=font(14, "bold"), anchor="mm")

    # Package name
    draw.text((cx + card_w // 2, cy + 42), pkg["name"],
        fill=(255, 255, 255, 255), font=font(28, "bold"), anchor="mm")

    # Divider line
    draw.line([(cx + 20, cy + 64), (cx + card_w - 20, cy + 64)],
        fill=(255, 255, 255, 50), width=1)

    # Setup price
    draw.text((cx + card_w // 2, cy + 102), pkg["setup"],
        fill=(255, 255, 255, 255), font=font(40, "bold"), anchor="mm")
    draw.text((cx + card_w // 2, cy + 136), "setup fee",
        fill=(200, 200, 220, 160), font=font(17), anchor="mm")

    # Monthly
    draw.rounded_rectangle([cx + 20, cy + 155, cx + card_w - 20, cy + 185], radius=10,
        fill=(255, 255, 255, 15))
    draw.text((cx + card_w // 2, cy + 170), pkg["monthly"],
        fill=(200, 220, 255, 220), font=font(17, "bold"), anchor="mm")

    # Features
    for j, feat in enumerate(pkg["features"]):
        fy = cy + 205 + j * 38
        draw.text((cx + 20, fy), f"✓  {feat}",
            fill=(255, 255, 255, 200), font=font(16), anchor="lm")

# --- CTA button ---
draw.rounded_rectangle([280, 820, 800, 888], radius=34, fill=(255, 255, 255, 255))
draw.text((540, 854), "DM 'INFO' sekarang  →", fill=(123, 103, 209, 255), font=font(30, "bold"), anchor="mm")

# --- Bottom strip ---
draw.line([(60, 920), (1020, 920)], fill=(255, 255, 255, 30), width=1)
draw.text((540, 950), "📱  +60 17 310 3966", fill=(255, 255, 255, 180), font=font(22, "bold"), anchor="mm")
draw.text((540, 988), "igenveritas@gmail.com  |  igen-veritas.com",
    fill=(255, 255, 255, 120), font=font(18), anchor="mm")
draw.text((540, 1030), "IGEN VERITAS — Powering businesses with intelligent solutions",
    fill=(255, 255, 255, 100), font=font(16), anchor="mm")

img.save(OUT, "PNG")
print(f"Saved: {OUT}")
