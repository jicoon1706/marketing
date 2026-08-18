"""CB-002 — Pain Point: Your Business Closes at 6PM"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260506_pain_CB002_business_closes_6pm.png"

VIOLET      = (123, 103, 209)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
RED         = (255, 75, 75)
RED_DARK    = (185, 48, 48)
GREEN       = (34, 197, 94)
LAVENDER    = (196, 181, 253)

def get_font(size, weight="regular"):
    from PIL import ImageFont
    m = {"bold": "C:/Windows/Fonts/segoeuib.ttf", "regular": "C:/Windows/Fonts/segoeui.ttf",
         "light": "C:/Windows/Fonts/segoeuil.ttf"}
    p = m.get(weight, m["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

def lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def alpha_rect(img, box, radius, fill_rgba, outline_rgba=None, width=1):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(box, radius=radius, fill=fill_rgba,
                        outline=outline_rgba, width=width)
    return Image.alpha_composite(img, layer)

# Canvas
img = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 255))
draw = ImageDraw.Draw(img)

# Background gradient
for y in range(1080):
    t = y / 1079
    c = lerp(DARK_NAVY, (6, 5, 14), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# ── Headline ──────────────────────────────────────────────────────────────────
font_h1 = get_font(44, "bold")
font_h2 = get_font(40, "bold")
draw.text((540, 80), "Your business closes at 6PM.", fill=(*WHITE, 255), font=font_h1, anchor="mm")
draw.text((540, 148), "Your competitor's doesn't.", fill=(*VIOLET, 255), font=font_h2, anchor="mm")

# ── LEFT PANEL: Your Business (x:40–492) ─────────────────────────────────────
L = [40, 198, 492, 862]
img = alpha_rect(img, L, radius=18, fill_rgba=(18, 16, 10, 255))
draw = ImageDraw.Draw(img)

# CLOSED badge
img = alpha_rect(img, [80, 218, 220, 256], radius=14,
                 fill_rgba=(100, 20, 20, 255), outline_rgba=(*RED, 200), width=1)
draw = ImageDraw.Draw(img)
font_badge = get_font(18, "bold")
draw.text((150, 237), "CLOSED", fill=(*RED, 255), font=font_badge, anchor="mm")

# 3×3 grid of dark office windows
WIN_W, WIN_H = 80, 60
WIN_START_X, WIN_START_Y = 92, 290
for row in range(3):
    for col in range(3):
        wx = WIN_START_X + col * (WIN_W + 18)
        wy = WIN_START_Y + row * (WIN_H + 18)
        img = alpha_rect(img, [wx, wy, wx + WIN_W, wy + WIN_H], radius=6,
                         fill_rgba=(8, 6, 4, 255), outline_rgba=(40, 35, 25, 255), width=2)
        draw = ImageDraw.Draw(img)
        # Faint cross divider
        mid_x = (wx + wx + WIN_W) // 2
        mid_y = (wy + wy + WIN_H) // 2
        draw.line([(mid_x, wy), (mid_x, wy + WIN_H)], fill=(30, 25, 18, 255), width=1)
        draw.line([(wx, mid_y), (wx + WIN_W, mid_y)], fill=(30, 25, 18, 255), width=1)

# Timestamp
font_ts = get_font(42, "bold")
draw.text((266, 660), "6:00 PM", fill=(*RED_DARK, 255), font=font_ts, anchor="mm")
font_sub = get_font(20, "regular")
draw.text((266, 708), "Office closed.", fill=(*BODY_GRAY, 255), font=font_sub, anchor="mm")

# "0 new leads today" badge
img = alpha_rect(img, [80, 730, 452, 772], radius=12,
                 fill_rgba=(80, 15, 15, 220), outline_rgba=(*RED, 120), width=1)
draw = ImageDraw.Draw(img)
font_leads = get_font(18, "regular")
draw.text((266, 751), "0 new leads today", fill=(*RED, 220), font=font_leads, anchor="mm")

# YOUR BUSINESS label
font_lbl = get_font(17, "regular")
draw.text((266, 838), "YOUR BUSINESS", fill=(*BODY_GRAY, 255), font=font_lbl, anchor="mm")

# ── RIGHT PANEL: Competitor (x:588–1040) ─────────────────────────────────────
R = [588, 198, 1040, 862]
# Violet glow behind
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(200, 0, -1):
    alpha = int(35 * (1 - r / 200))
    gd.ellipse([814 - r, 530 - r, 814 + r, 530 + r], fill=(*VIOLET, alpha))
img = Image.alpha_composite(img, glow)
img = alpha_rect(img, R, radius=18, fill_rgba=(20, 14, 40, 230),
                 outline_rgba=(*VIOLET, 110), width=2)
draw = ImageDraw.Draw(img)

# ONLINE 24/7 badge
img = alpha_rect(img, [628, 210, 800, 248], radius=14,
                 fill_rgba=(20, 80, 40, 255), outline_rgba=(*GREEN, 180), width=1)
draw = ImageDraw.Draw(img)
# Green dot
draw.ellipse([638, 224, 650, 236], fill=(*GREEN, 255))
draw.text((730, 229), "ONLINE 24/7", fill=(*GREEN, 255), font=get_font(16, "bold"), anchor="mm")

# Chat bubbles
bubbles = [
    ("Hi, are you open? 👋", "customer"),
    ("Yes! How can I help you?", "bot"),
    ("I need a website quote", "customer"),
    ("Got it! Sending details now ✅", "bot"),
    ("Another lead incoming...", "bot"),
]
font_chat = get_font(17, "regular")
bubble_y = 270
for text, role in bubbles:
    is_bot = role == "bot"
    bg_color = (60, 30, 100, 220) if not is_bot else (*VIOLET, 220)
    bx1 = 600 if not is_bot else 700
    bx2 = 990 if not is_bot else 1030
    by2 = bubble_y + 38
    img = alpha_rect(img, [bx1, bubble_y, bx2, by2], radius=10, fill_rgba=bg_color)
    draw = ImageDraw.Draw(img)
    cx = (bx1 + bx2) // 2
    draw.text((cx, bubble_y + 19), text, fill=(*WHITE, 230), font=font_chat, anchor="mm")
    bubble_y += 52

# Leads counter card
img = alpha_rect(img, [610, 598, 1020, 658], radius=12,
                 fill_rgba=(255, 255, 255, 12), outline_rgba=(*VIOLET, 200), width=1)
draw = ImageDraw.Draw(img)
draw.text((814, 618), "Leads captured tonight:", fill=(*BODY_GRAY, 255), font=get_font(16, "regular"), anchor="mm")
draw.text((814, 642), "12 and counting 🚀", fill=(*WHITE, 255), font=get_font(19, "bold"), anchor="mm")

# Timestamp
draw.text((814, 726), "11:47 PM", fill=(*VIOLET, 255), font=get_font(38, "bold"), anchor="mm")
draw.text((814, 784), "Still working for you.", fill=(*LAVENDER, 255), font=get_font(20, "regular"), anchor="mm")
draw.text((814, 838), "YOUR COMPETITOR", fill=(*VIOLET, 255), font=get_font(17, "regular"), anchor="mm")

# ── VS Badge (center) ─────────────────────────────────────────────────────────
vs_layer = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
vd = ImageDraw.Draw(vs_layer)
vd.ellipse([515, 505, 565, 555], fill=(*VIOLET, 255))
img = Image.alpha_composite(img, vs_layer)
draw = ImageDraw.Draw(img)
draw.text((540, 530), "VS", fill=(*WHITE, 255), font=get_font(22, "bold"), anchor="mm")

# ── Bottom Section ────────────────────────────────────────────────────────────
draw.line([(40, 878), (1040, 878)], fill=(*VIOLET, 180), width=1)
draw.text((540, 912), "AI chatbot — your business stays open long after you clock out.",
          fill=(*LAVENDER, 255), font=get_font(22, "regular"), anchor="mm")

# CTA button
img = alpha_rect(img, [282, 948, 798, 994], radius=24, fill_rgba=(*VIOLET, 255))
draw = ImageDraw.Draw(img)
draw.text((540, 971), "DM us — find out how it works", fill=(*WHITE, 255), font=get_font(22, "bold"), anchor="mm")

# Brand footer
draw.text((54, 1040), "IGEN VERITAS", fill=(*WHITE, 160), font=get_font(16, "regular"), anchor="lm")
draw.text((1026, 1040), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="rm")

# Save
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.convert("RGB").save(OUTPUT_PATH, "PNG")
print(f"Saved: {OUTPUT_PATH}")
