"""
CB-005 Carousel Cover — 5 Signs Your Business Is Leaking Money
Slide 1 / Cover
No top-left brand watermark, no top-right carousel badge.
"""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260508_pain_CB005_5signs_leaking_money.png"

# Colors
VIOLET      = (123, 103, 209)
BLUE_MID    = (72, 143, 227)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
BLUE_BRIGHT = (65, 150, 230)

def get_font(size, weight="regular"):
    font_map = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

# Canvas
img = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 255))
draw = ImageDraw.Draw(img)

# --- Background gradient: dark purple to near-black ---
BG_TOP    = (38, 18, 70)   # deep purple
BG_BOTTOM = (8, 8, 16)     # near-black
for y in range(1080):
    t = y / 1079
    color = lerp_color(BG_TOP, BG_BOTTOM, t)
    draw.line([(0, y), (1080, y)], fill=(*color, 255))

# Radial violet glow at center-top
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(520, 0, -1):
    alpha = int(55 * (1 - r / 520))
    gd.ellipse([540 - r, -60 - r, 540 + r, -60 + r], fill=(*VIOLET, alpha))
img = Image.alpha_composite(img, glow)
draw = ImageDraw.Draw(img)

# --- Headline (y: 130–470) ---
font_h  = get_font(86, "bold")
font_sub = get_font(38, "regular")

HEADLINE_CX = 540
# Line 1: "5 Signs Your" — white
draw.text((HEADLINE_CX, 170), "5 Signs Your", fill=(*WHITE, 255), font=font_h, anchor="mm")
# Line 2: "Business Is" — Violet
draw.text((HEADLINE_CX, 280), "Business Is", fill=(*VIOLET, 255), font=font_h, anchor="mm")
# Line 3: "Leaking Money" — white
draw.text((HEADLINE_CX, 390), "Leaking Money", fill=(*WHITE, 255), font=font_h, anchor="mm")
# Sub-label: "Right Now"
draw.text((HEADLINE_CX, 462), "Right Now", fill=(*BODY_GRAY, 255), font=font_sub, anchor="mm")

# --- 5 Sign Cards (y: 520–895) ---
CARD_X1 = 60
CARD_X2 = 1020
CARD_H  = 64
CARD_GAP = 14
CARD_START_Y = 520

signs = [
    "Leads go unanswered after hours",
    "No follow-up system in place",
    "Slow reply time (>30 mins)",
    "Leads fall through the cracks",
    "Zero automation = zero growth",
]
number_colors = [VIOLET, BLUE_MID, VIOLET, BLUE_MID, VIOLET]

font_num  = get_font(24, "bold")
font_sign = get_font(24, "regular")

for i, (sign, num_color) in enumerate(zip(signs, number_colors)):
    y1 = CARD_START_Y + i * (CARD_H + CARD_GAP)
    y2 = y1 + CARD_H

    # Glassmorphism card
    card_img = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card_img)
    cd.rounded_rectangle(
        [CARD_X1, y1, CARD_X2, y2],
        radius=12,
        fill=(255, 255, 255, 12),
        outline=(255, 255, 255, 30),
    )
    img = Image.alpha_composite(img, card_img)
    draw = ImageDraw.Draw(img)

    num_str = f"{i+1:02d}"
    # Number prefix
    draw.text((CARD_X1 + 28, (y1 + y2) // 2), num_str, fill=(*num_color, 255), font=font_num, anchor="lm")
    # Sign text
    draw.text((CARD_X1 + 90, (y1 + y2) // 2), sign, fill=(*WHITE, 230), font=font_sign, anchor="lm")

# --- Swipe prompt ---
font_swipe = get_font(22, "regular")
draw.text((540, 925), "SWIPE TO SEE EACH SIGN →", fill=(*BODY_GRAY, 200), font=font_swipe, anchor="mm")

# --- Bottom gradient strip (y: 1024–1080) ---
strip = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
sd = ImageDraw.Draw(strip)
for x in range(1080):
    t = x / 1079
    color = lerp_color(VIOLET, BLUE_BRIGHT, t)
    sd.line([(x, 1024), (x, 1080)], fill=(*color, 255))
img = Image.alpha_composite(img, strip)
draw = ImageDraw.Draw(img)

# Tagline on strip
font_tag = get_font(20, "regular")
draw.text((540, 1052), "Intelligent Solutions · Cutting-Edge Technology", fill=(*WHITE, 220), font=font_tag, anchor="mm")

# Save
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
final = img.convert("RGB")
final.save(OUTPUT_PATH, "PNG")
print(f"Saved: {OUTPUT_PATH}")
