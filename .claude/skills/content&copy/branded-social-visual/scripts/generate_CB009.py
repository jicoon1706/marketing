"""CB-009 — Engagement Post: Real Talk — Lost a Customer?"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260514_engagement_CB009_lost_customer_late_reply.png"

VIOLET      = (123, 103, 209)
PURPLE      = (138, 93, 204)
BLUE_MID    = (72, 143, 227)
BLUE_BRIGHT = (65, 150, 230)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)

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

# Background: violet to purple gradient
BG_TOP    = (80, 50, 160)
BG_BOTTOM = (50, 20, 100)
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
draw.text((54, 68), "igenveritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# ── "REAL TALK" Badge (y: 108–152) ────────────────────────────────────────────
badge_w = 240
img = alpha_rect(img, [(1080 - badge_w) // 2, 108, (1080 + badge_w) // 2, 152], radius=22,
                 fill_rgba=(*BLUE_MID, 181), outline_rgba=None)
draw = ImageDraw.Draw(img)
draw.text((540, 130), "REAL TALK", fill=(*WHITE, 255), font=get_font(26, "bold"), anchor="mm")

# ── Main Question (y: 190–570) ────────────────────────────────────────────────
draw.text((540, 230), "Have You Ever", fill=(*WHITE, 255), font=get_font(78, "bold"), anchor="mm")
draw.text((540, 328), "Lost a Customer", fill=(*VIOLET, 255), font=get_font(82, "bold"), anchor="mm")
draw.text((540, 426), "Because You", fill=(*WHITE, 255), font=get_font(78, "bold"), anchor="mm")
draw.text((540, 510), "Replied Too Late?", fill=(*WHITE, 255), font=get_font(54, "bold"), anchor="mm")

# ── Glassmorphism Context Card (y: 580–720) ────────────────────────────────────
img = alpha_rect(img, [140, 580, 940, 720], radius=20,
                 fill_rgba=(255, 255, 255, 14), outline_rgba=(255, 255, 255, 40), width=1)
draw = ImageDraw.Draw(img)
draw.text((540, 624), "Be honest with yourself.", fill=(*BODY_GRAY, 255), font=get_font(36, "regular"), anchor="mm")
draw.text((540, 676), "Most businesses have. Yours doesn't have to.", fill=(*WHITE, 255), font=get_font(28, "regular"), anchor="mm")

# ── Emoji Engagement CTA (y: 776) ─────────────────────────────────────────────
draw.text((540, 776), "Drop a 🙋 below if this has happened to you.",
          fill=(*WHITE, 255), font=get_font(36, "regular"), anchor="mm")

# ── Reaction Pill Row (y: 830–882) ────────────────────────────────────────────
pills = [
    ("🙋 Yes", (*VIOLET, 199)),
    ("🤔 Maybe", (*PURPLE, 199)),
    ("❌ Never", (60, 60, 80, 199)),
]
pill_w = 210
pill_h = 52
total_w = 3 * pill_w + 2 * 20
start_x = (1080 - total_w) // 2

for i, (label, fill) in enumerate(pills):
    px = start_x + i * (pill_w + 20)
    img = alpha_rect(img, [px, 830, px + pill_w, 882], radius=24, fill_rgba=fill)
    draw = ImageDraw.Draw(img)
    draw.text((px + pill_w // 2, 856), label, fill=(*WHITE, 255), font=get_font(26, "bold"), anchor="mm")

# ── Footer CTA (y: 940) ────────────────────────────────────────────────────────
draw.text((540, 940), "There's a better way. DM us 'BOT' to find out.",
          fill=(*BODY_GRAY, 255), font=get_font(24, "regular"), anchor="mm")

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
