"""CB-001 — Brand Intro Poster (Awareness)"""

from PIL import Image, ImageDraw
import os, math

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260505_awareness_CB001_brand_intro.png"

VIOLET      = (123, 103, 209)
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

# Canvas
img = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 255))
draw = ImageDraw.Draw(img)

# Background: dark navy deepening toward bottom
for y in range(1080):
    t = y / 1079
    c = lerp(DARK_NAVY, (6, 5, 12), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Radial violet glow centered at upper-mid (~y:340)
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(480, 0, -1):
    alpha = int(60 * (1 - r / 480))
    gd.ellipse([540 - r, 340 - r, 540 + r, 340 + r], fill=(*VIOLET, alpha))
img = Image.alpha_composite(img, glow)

# Blue-violet accent glow bottom-right
glow2 = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd2 = ImageDraw.Draw(glow2)
for r in range(300, 0, -1):
    alpha = int(40 * (1 - r / 300))
    gd2.ellipse([1080 - r, 1080 - r, 1080 + r, 1080 + r], fill=(*BLUE_BRIGHT, alpha))
img = Image.alpha_composite(img, glow2)
draw = ImageDraw.Draw(img)

# Tech-grid lines (faint white, 90px intervals)
for x in range(0, 1080, 90):
    draw.line([(x, 0), (x, 1080)], fill=(*WHITE, 15))
for y in range(0, 1080, 90):
    draw.line([(0, y), (1080, y)], fill=(*WHITE, 15))

# Diagonal accent lines top-right
for i in range(6):
    off = i * 30
    draw.line([(900 + off, 0), (1080, 180 - off)], fill=(*VIOLET, 25), width=2)

# ── Logo Mark (center-upper, y:360) ──────────────────────────────────────────
CX, CY = 540, 360
R_OUTER = 110

# Semi-transparent filled inner circle
circle_img = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
ci = ImageDraw.Draw(circle_img)
ci.ellipse([CX - R_OUTER + 10, CY - R_OUTER + 10, CX + R_OUTER - 10, CY + R_OUTER - 10],
           fill=(*VIOLET, 140))
img = Image.alpha_composite(img, circle_img)
draw = ImageDraw.Draw(img)

# Outer thin ring
draw.ellipse([CX - R_OUTER, CY - R_OUTER, CX + R_OUTER, CY + R_OUTER],
             outline=(*VIOLET, 255), width=2)

# Dot ring: 12 evenly-spaced dots
R_DOT = R_OUTER + 18
for k in range(12):
    angle = math.radians(k * 30 - 90)
    dx = CX + int(R_DOT * math.cos(angle))
    dy = CY + int(R_DOT * math.sin(angle))
    if k % 3 == 0:
        draw.ellipse([dx - 5, dy - 5, dx + 5, dy + 5], fill=(*VIOLET, 255))
    else:
        draw.ellipse([dx - 4, dy - 4, dx + 4, dy + 4], fill=(*WHITE, 60))

# "IV" monogram
font_iv = get_font(70, "bold")
draw.text((CX, CY), "IV", fill=(*WHITE, 255), font=font_iv, anchor="mm")

# ── Typography ────────────────────────────────────────────────────────────────
# Top-left brand watermark
font_wm = get_font(20, "regular")
font_wm_sm = get_font(15, "regular")
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 255), font=font_wm, anchor="lt")
draw.text((54, 68), "igenveritas.com", fill=(*BODY_GRAY, 255), font=font_wm_sm, anchor="lt")

# "IGEN" violet
font_name = get_font(80, "bold")
draw.text((540, 530), "IGEN", fill=(*VIOLET, 255), font=font_name, anchor="mm")

# "VERITAS" white
draw.text((540, 615), "VERITAS", fill=(*WHITE, 255), font=font_name, anchor="mm")

# Thin violet divider
draw.line([(200, 660), (880, 660)], fill=(*VIOLET, 180), width=2)

# Tagline
font_tag1 = get_font(30, "regular")
font_tag2 = get_font(28, "regular")
draw.text((540, 710), "Powering the future —", fill=(*VIOLET, 255), font=font_tag1, anchor="mm")
draw.text((540, 755), "one smart business at a time.", fill=(*BODY_GRAY, 255), font=font_tag2, anchor="mm")

# Services strip (y:830)
font_svc = get_font(20, "regular")
services = "AI Chatbot  ·  Web Dev  ·  Mobile App  ·  Automation"
draw.text((540, 840), services, fill=(*WHITE, 200), font=font_svc, anchor="mm")

# ── Bottom Gradient Strip ─────────────────────────────────────────────────────
strip = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
sd = ImageDraw.Draw(strip)
for x in range(1080):
    t = x / 1079
    c = lerp(VIOLET, BLUE_BRIGHT, t)
    sd.line([(x, 1000), (x, 1080)], fill=(*c, 255))
img = Image.alpha_composite(img, strip)
draw = ImageDraw.Draw(img)

font_strip = get_font(19, "regular")
draw.text((540, 1040), "Intelligent Solutions  ·  Cutting-Edge Technology",
          fill=(*WHITE, 220), font=font_strip, anchor="mm")

# Save
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.convert("RGB").save(OUTPUT_PATH, "PNG")
print(f"Saved: {OUTPUT_PATH}")
