"""CB-007 — Reel Hook Card: POV 2AM, Nobody Replied"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260511_pain_CB007_pov_2am_no_reply.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
WA_GREEN    = (37, 211, 102)

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

# Background: black-violet-blue moody gradient
BG_TOP    = (12, 8, 30)
BG_BOTTOM = (20, 30, 60)
for y in range(1080):
    t = y / 1079
    c = lerp(BG_TOP, BG_BOTTOM, t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Diagonal blue accent bottom-right
for x in range(1080):
    t = x / 1079
    alpha = int(30 * t)
    draw.line([(x, 0), (x, 1080)], fill=(*VIOLET, alpha))

# Dark overlay
overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 120))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# ── Brand Watermark (above top bar) ──────────────────────────────────────────
draw.text((54, 20), "IGEN VERITAS", fill=(*WHITE, 160), font=get_font(18, "regular"), anchor="lt")
draw.text((54, 44), "igen-veritas.com", fill=(*BODY_GRAY, 200), font=get_font(13, "regular"), anchor="lt")

# ── Cinematic Letterbox Bars ──────────────────────────────────────────────────
# Top bar
top_bar = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
tb = ImageDraw.Draw(top_bar)
tb.rectangle([0, 0, 1080, 80], fill=(0, 0, 0, 200))
img = Image.alpha_composite(img, top_bar)

# Bottom bar
bot_bar = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
bb = ImageDraw.Draw(bot_bar)
bb.rectangle([0, 1000, 1080, 1080], fill=(0, 0, 0, 200))
img = Image.alpha_composite(img, bot_bar)
draw = ImageDraw.Draw(img)

# "P O V" in top bar
draw.text((540, 40), "P  O  V", fill=(*BODY_GRAY, 255), font=get_font(28, "bold"), anchor="mm")

# ── Clock (y: 220) ─────────────────────────────────────────────────────────────
# Violet radial glow behind clock
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(280, 0, -1):
    alpha = int(55 * (1 - r / 280))
    gd.ellipse([540 - r, 220 - r, 540 + r, 220 + r], fill=(*VIOLET, alpha))
img = Image.alpha_composite(img, glow)
draw = ImageDraw.Draw(img)

draw.text((540, 220), "2:17 AM", fill=(*WHITE, 255), font=get_font(140, "bold"), anchor="mm")

# ── Main Text Block (y: 370–644) ──────────────────────────────────────────────
draw.text((540, 390), "A hot lead just messaged", fill=(*BODY_GRAY, 255), font=get_font(38, "regular"), anchor="mm")
draw.text((540, 450), "your business.", fill=(*WHITE, 255), font=get_font(52, "bold"), anchor="mm")

# Gut-punch words
draw.text((540, 558), "Nobody.", fill=(*VIOLET, 255), font=get_font(108, "bold"), anchor="mm")
draw.text((540, 658), "Replied.", fill=(*WHITE, 255), font=get_font(108, "bold"), anchor="mm")

# ── Sub-line (y: 746) ─────────────────────────────────────────────────────────
draw.text((540, 750), "This happens every night in Malaysian businesses.",
          fill=(*BODY_GRAY, 255), font=get_font(28, "regular"), anchor="mm")

# ── WhatsApp Notification Strip (y: 792–870) ──────────────────────────────────
img = alpha_rect(img, [140, 792, 940, 870], radius=16,
                 fill_rgba=(255, 255, 255, 14), outline_rgba=(255, 255, 255, 30), width=1)
draw = ImageDraw.Draw(img)

# WhatsApp icon square
wa_icon = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
wi = ImageDraw.Draw(wa_icon)
wi.rounded_rectangle([160, 806, 202, 848], radius=8, fill=(*WA_GREEN, 255))
img = Image.alpha_composite(img, wa_icon)
draw = ImageDraw.Draw(img)

# WA icon text
draw.text((181, 827), "W", fill=(*WHITE, 255), font=get_font(20, "bold"), anchor="mm")

# Notification content
draw.text((218, 815), "New Message", fill=(*BODY_GRAY, 255), font=get_font(18, "regular"), anchor="lt")
draw.text((218, 840), "\"Nak tanya pasal servis korang...\"", fill=(*WHITE, 255), font=get_font(22, "regular"), anchor="lt")
draw.text((920, 827), "2:17 AM", fill=(*BODY_GRAY, 255), font=get_font(18, "regular"), anchor="rm")

# ── Reel-Style Footer (y: 960) ────────────────────────────────────────────────
draw.text((540, 960), "Automate your replies — 24/7.  igen-veritas.com",
          fill=(*BODY_GRAY, 199), font=get_font(22, "regular"), anchor="mm")

# Save
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.convert("RGB").save(OUTPUT_PATH, "PNG")
print(f"Saved: {OUTPUT_PATH}")
