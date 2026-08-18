"""CB-004 — Engagement Post: Reply Time Poll"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260509_engagement_CB004_reply_time.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
LAVENDER    = (196, 181, 253)
GREEN       = (34, 197, 94)
AMBER       = (251, 191, 36)
RED         = (239, 68, 68)

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
img = Image.new("RGBA", (1080, 1080), (0, 0, 0, 255))
draw = ImageDraw.Draw(img)

# Background: deep purple to near-black navy diagonal
TOP_COLOR    = (45, 25, 106)   # #2D196A
BOTTOM_COLOR = (11, 11, 30)    # #0B0B1E
for y in range(1080):
    t = y / 1079
    c = lerp(TOP_COLOR, BOTTOM_COLOR, t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Radial violet glow top-right
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(350, 0, -1):
    alpha = int(50 * (1 - r / 350))
    gd.ellipse([1080 - r, -r, 1080 + r, r], fill=(*VIOLET, alpha))
img = Image.alpha_composite(img, glow)

# Blue glow bottom-left
glow2 = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd2 = ImageDraw.Draw(glow2)
for r in range(280, 0, -1):
    alpha = int(40 * (1 - r / 280))
    gd2.ellipse([-r, 1080 - r, r, 1080 + r], fill=(*BLUE_BRIGHT, alpha))
img = Image.alpha_composite(img, glow2)
draw = ImageDraw.Draw(img)

# ── Brand Tag (top-left) ───────────────────────────────────────────────────────
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 160), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# ── "Quick question:" Label Pill ───────────────────────────────────────────────
label_w = 260
label_x1 = (1080 - label_w) // 2
img = alpha_rect(img, [label_x1, 140, label_x1 + label_w, 182], radius=20,
                 fill_rgba=(*VIOLET, 204), outline_rgba=(*VIOLET, 255), width=1)
draw = ImageDraw.Draw(img)
draw.text((540, 161), "Quick question:", fill=(*WHITE, 255), font=get_font(20, "regular"), anchor="mm")

# ── Main Question (4 lines, y:260–530) ────────────────────────────────────────
font_q = get_font(76, "bold")
questions = [
    ("How long does", WHITE),
    ("your team take", WHITE),
    ("to reply to a", WHITE),
    ("new enquiry?", VIOLET),
]
q_y = 290
for text, color in questions:
    draw.text((540, q_y), text, fill=(*color, 255), font=font_q, anchor="mm")
    q_y += 100

# ── Subtitle ───────────────────────────────────────────────────────────────────
draw.text((540, 640), "Be honest. 👀", fill=(*LAVENDER, 200), font=get_font(32, "regular"), anchor="mm")

# ── Thin Divider ──────────────────────────────────────────────────────────────
draw.line([(120, 690), (960, 690)], fill=(*VIOLET, 80), width=1)

# ── Poll Cards ────────────────────────────────────────────────────────────────
poll_options = [
    ("⚡ Under 5 minutes", GREEN, (34, 197, 94, 30), (34, 197, 94, 100)),
    ("⏰ Within the hour", VIOLET, (123, 103, 209, 30), (123, 103, 209, 100)),
    ("🌙 A few hours later", AMBER, (251, 191, 36, 30), (251, 191, 36, 100)),
    ("❌ We miss some enquiries", RED, (239, 68, 68, 30), (239, 68, 68, 100)),
]

card_y = 712
for text, text_color, bg_rgba, border_rgba in poll_options:
    img = alpha_rect(img, [120, card_y, 960, card_y + 54], radius=14,
                     fill_rgba=bg_rgba, outline_rgba=border_rgba, width=1)
    draw = ImageDraw.Draw(img)
    draw.text((540, card_y + 27), text, fill=(*WHITE, 230), font=get_font(22, "regular"), anchor="mm")
    card_y += 66

# ── Bottom CTAs ────────────────────────────────────────────────────────────────
draw.text((540, 990), "Comment your answer below ⬇",
          fill=(*WHITE, 200), font=get_font(24, "regular"), anchor="mm")
draw.text((540, 1040), "Or DM us — we'll show you a better way.",
          fill=(*VIOLET, 255), font=get_font(22, "bold"), anchor="mm")

# Save
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.convert("RGB").save(OUTPUT_PATH, "PNG")
print(f"Saved: {OUTPUT_PATH}")
