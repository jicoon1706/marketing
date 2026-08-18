"""CB-006 — Pain: Every Unanswered WhatsApp"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260509_pain_CB006_unanswered_whatsapp.png"

VIOLET      = (123, 103, 209)
BLUE_MID    = (72, 143, 227)
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

# Background: black to deep purple
BG_TOP    = (8, 5, 16)
BG_BOTTOM = (45, 20, 70)
for y in range(1080):
    t = y / 1079
    c = lerp(BG_TOP, BG_BOTTOM, t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Dark overlay to deepen contrast
overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 120))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# ── Brand Watermark (top-left) ─────────────────────────────────────────────────
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# ── Headline Block (y: 100–480) ────────────────────────────────────────────────
draw.text((540, 130), "Every Unanswered", fill=(*WHITE, 255), font=get_font(72, "bold"), anchor="mm")
draw.text((540, 230), "WhatsApp", fill=(*VIOLET, 255), font=get_font(88, "bold"), anchor="mm")
draw.text((540, 330), "Is a Lead You", fill=(*WHITE, 255), font=get_font(62, "bold"), anchor="mm")
draw.text((540, 420), "Handed Away.", fill=(*BLUE_MID, 255), font=get_font(62, "bold"), anchor="mm")

# ── WhatsApp Mockup Card (y: 490–840) ─────────────────────────────────────────
img = alpha_rect(img, [200, 490, 880, 840], radius=20,
                 fill_rgba=(255, 255, 255, 14), outline_rgba=(255, 255, 255, 40), width=1)
draw = ImageDraw.Draw(img)

# Header bar (WhatsApp green)
layer = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
ld = ImageDraw.Draw(layer)
ld.rounded_rectangle([200, 490, 880, 552], radius=20,
                     fill=(*WA_GREEN, 220), outline=None)
# Cover bottom corners to make top-only rounded
ld.rectangle([200, 530, 880, 552], fill=(*WA_GREEN, 220))
img = Image.alpha_composite(img, layer)
draw = ImageDraw.Draw(img)

# Green dot + name
draw.ellipse([222, 510, 236, 524], fill=(*WHITE, 200))
draw.text((248, 521), "● Potential Customer", fill=(*WHITE, 255), font=get_font(20, "bold"), anchor="lm")
draw.text((858, 521), "Online", fill=(180, 255, 200, 255), font=get_font(18, "regular"), anchor="rm")

# Chat bubble (white card)
img = alpha_rect(img, [224, 568, 700, 640], radius=14,
                 fill_rgba=(255, 255, 255, 240), outline_rgba=None)
draw = ImageDraw.Draw(img)
draw.text((240, 600), "Hi, are you still open? 👋", fill=(*DARK_NAVY, 255), font=get_font(22, "regular"), anchor="lm")
draw.text((685, 630), "8:47 PM", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="rm")

# Read receipt
draw.text((540, 680), "Seen ✓✓  No reply.", fill=(*BODY_GRAY, 255), font=get_font(20, "regular"), anchor="mm")

# Red stat pill
img = alpha_rect(img, [340, 714, 740, 764], radius=24,
                 fill_rgba=(220, 50, 50, 199), outline_rgba=None)
draw = ImageDraw.Draw(img)
draw.text((540, 739), "0 replies sent", fill=(*WHITE, 255), font=get_font(20, "bold"), anchor="mm")

# ── CTA Block (y: 876–958) ─────────────────────────────────────────────────────
draw.text((540, 874), "Don't let silence cost you your next client.",
          fill=(*BODY_GRAY, 255), font=get_font(22, "regular"), anchor="mm")

img = alpha_rect(img, [200, 904, 880, 954], radius=24,
                 fill_rgba=(*VIOLET, 229), outline_rgba=None)
draw = ImageDraw.Draw(img)
draw.text((540, 929), "DM us 'BOT' — automate your replies",
          fill=(*WHITE, 255), font=get_font(22, "bold"), anchor="mm")

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
