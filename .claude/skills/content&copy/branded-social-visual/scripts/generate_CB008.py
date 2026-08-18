"""CB-008 — Education Carousel Cover: Auto-Reply vs AI Chatbot"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260513_education_CB008_autoreply_vs_chatbot.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
RED         = (220, 50, 50)

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

# Background: purple to blue-mid gradient
BG_TOP    = (80, 40, 140)
BG_BOTTOM = (40, 80, 160)
for y in range(1080):
    t = y / 1079
    c = lerp(BG_TOP, BG_BOTTOM, t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Dark overlay 47%
overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 120))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# ── Brand Watermark (top-left) ─────────────────────────────────────────────────
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# ── Carousel Badge (top-right) ────────────────────────────────────────────────
img = alpha_rect(img, [860, 34, 1040, 68], radius=16,
                 fill_rgba=(*VIOLET, 199), outline_rgba=None)
draw = ImageDraw.Draw(img)
draw.text((950, 51), "CAROUSEL ▶", fill=(*WHITE, 255), font=get_font(15, "bold"), anchor="mm")

# ── Headline Block (y: 120–476) ───────────────────────────────────────────────
draw.text((540, 160), "Auto-Reply", fill=(*BODY_GRAY, 255), font=get_font(78, "bold"), anchor="mm")
draw.text((540, 258), "vs", fill=(*WHITE, 255), font=get_font(96, "bold"), anchor="mm")
draw.text((540, 360), "AI Chatbot", fill=(*VIOLET, 255), font=get_font(78, "bold"), anchor="mm")
draw.text((540, 430), "The difference will surprise you.", fill=(*WHITE, 255), font=get_font(34, "regular"), anchor="mm")

# Thin divider
draw.line([(160, 462), (920, 462)], fill=(*WHITE, 102), width=1)

# ── Split Comparison Panel (y: 500–900) ───────────────────────────────────────
MID = 540

# Left column — Auto-Reply (red tint)
img = alpha_rect(img, [60, 500, MID - 20, 900], radius=16,
                 fill_rgba=(220, 50, 50, 20), outline_rgba=(220, 50, 50, 80), width=1)
draw = ImageDraw.Draw(img)
draw.text((300, 540), "❌ Auto-Reply", fill=(255, 100, 100, 255), font=get_font(28, "bold"), anchor="mm")

auto_points = [
    "Fixed responses only",
    "Cannot qualify leads",
    "No follow-up logic",
    "Confuses off-script queries",
]
for i, pt in enumerate(auto_points):
    draw.text((80, 590 + i * 68), f"• {pt}", fill=(*BODY_GRAY, 255), font=get_font(22, "regular"), anchor="lt")

# Right column — AI Chatbot (violet tint)
img = alpha_rect(img, [MID + 20, 500, 1020, 900], radius=16,
                 fill_rgba=(*VIOLET, 20), outline_rgba=(*VIOLET, 100), width=1)
draw = ImageDraw.Draw(img)
draw.text((780, 540), "✅ AI Chatbot", fill=(*VIOLET, 255), font=get_font(28, "bold"), anchor="mm")

ai_points = [
    "Learns your business",
    "Qualifies leads live",
    "Sends follow-ups auto",
    "Handles any question",
]
for i, pt in enumerate(ai_points):
    draw.text((MID + 40, 590 + i * 68), f"• {pt}", fill=(*WHITE, 255), font=get_font(22, "regular"), anchor="lt")

# ── Swipe Prompt (y: 940) ─────────────────────────────────────────────────────
draw.text((540, 940), "SWIPE TO SEE THE FULL BREAKDOWN →",
          fill=(*BODY_GRAY, 199), font=get_font(22, "regular"), anchor="mm")

# ── Bottom Gradient Strip ─────────────────────────────────────────────────────
strip = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
sd = ImageDraw.Draw(strip)
for x in range(1080):
    t = x / 1079
    c = lerp(VIOLET, BLUE_BRIGHT, t)
    sd.line([(x, 1024), (x, 1080)], fill=(*c, 255))
img = Image.alpha_composite(img, strip)
draw = ImageDraw.Draw(img)
draw.text((540, 1052), "Intelligent Solutions  ·  Cutting-Edge Technology",
          fill=(*WHITE, 220), font=get_font(19, "regular"), anchor="mm")

# Save
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.convert("RGB").save(OUTPUT_PATH, "PNG")
print(f"Saved: {OUTPUT_PATH}")
