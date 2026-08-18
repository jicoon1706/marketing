"""CB-016 — Conversion: This Is the Week."""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260526_conversion_CB016_this_is_the_week.png"

VIOLET      = (123, 103, 209)
PURPLE      = (138, 93, 204)
BLUE_BRIGHT = (65, 150, 230)
BLUE_MID    = (72, 143, 227)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
LAVENDER    = (196, 181, 253)

def get_font(size, weight="regular"):
    from PIL import ImageFont
    m = {"bold": "C:/Windows/Fonts/segoeuib.ttf", "regular": "C:/Windows/Fonts/segoeui.ttf"}
    p = m.get(weight, m["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

def lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def alpha_rect(img, box, radius, fill_rgba, outline_rgba=None, width=1):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(box, radius=radius, fill=fill_rgba, outline=outline_rgba, width=width)
    return Image.alpha_composite(img, layer)

img = Image.new("RGBA", (1080, 1080), (0, 0, 0, 255))
draw = ImageDraw.Draw(img)

# Bold violet gradient background
for y in range(1080):
    t = y / 1079
    c = lerp((80, 50, 180), (30, 15, 80), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Subtle dark overlay
overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 60))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Decorative radial glow center-bottom
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(500, 0, -1):
    alpha = int(40 * (1 - r / 500))
    gd.ellipse([540 - r, 1080 - r, 540 + r, 1080 + r], fill=(*BLUE_BRIGHT, alpha))
img = Image.alpha_composite(img, glow)
draw = ImageDraw.Draw(img)

# Tech grid lines
for x in range(0, 1080, 120):
    draw.line([(x, 0), (x, 1080)], fill=(255, 255, 255, 8))
for y in range(0, 1080, 120):
    draw.line([(0, y), (1080, y)], fill=(255, 255, 255, 8))

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*LAVENDER, 180), font=get_font(15, "regular"), anchor="lt")

# Main CTA copy — stacked for impact
draw.text((540, 200), "You've Been Thinking", fill=(*WHITE, 255), font=get_font(66, "bold"), anchor="mm")
draw.text((540, 286), "About Automating", fill=(*WHITE, 255), font=get_font(66, "bold"), anchor="mm")
draw.text((540, 372), "Your Business", fill=(*WHITE, 255), font=get_font(66, "bold"), anchor="mm")
draw.text((540, 458), "For Months.", fill=(*LAVENDER, 255), font=get_font(60, "bold"), anchor="mm")

# Divider
draw.line([(160, 500), (920, 500)], fill=(255, 255, 255, 80), width=2)

# The week line — big impact
draw.text((540, 580), "THIS IS", fill=(*WHITE, 255), font=get_font(100, "bold"), anchor="mm")
draw.text((540, 690), "THE WEEK.", fill=(*BLUE_BRIGHT, 255), font=get_font(110, "bold"), anchor="mm")

# Urgency micro-copy
draw.text((540, 762), "Setup takes 5–7 days. No technical knowledge needed.", fill=(*LAVENDER, 220), font=get_font(26, "regular"), anchor="mm")

# 3 micro-stats
stats = ["⚡ 24/7 Active", "🤖 AI-Powered", "📊 Lead Tracking"]
stat_x = [220, 540, 860]
for sx, stat in zip(stat_x, stats):
    img = alpha_rect(img, [sx - 120, 800, sx + 120, 844], radius=22,
                     fill_rgba=(255, 255, 255, 20), outline_rgba=(255, 255, 255, 50), width=1)
    draw = ImageDraw.Draw(img)
    draw.text((sx, 822), stat, fill=(*WHITE, 240), font=get_font(20, "bold"), anchor="mm")

# Primary CTA button
img = alpha_rect(img, [180, 876, 900, 940], radius=32,
                 fill_rgba=(*BLUE_BRIGHT, 255), outline_rgba=None)
draw = ImageDraw.Draw(img)
draw.text((540, 908), "DM us 'START' to begin →", fill=(*WHITE, 255), font=get_font(30, "bold"), anchor="mm")

# Bottom strip
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

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.convert("RGB").save(OUTPUT_PATH, "PNG")
print(f"Saved: {OUTPUT_PATH}")
