"""CB-012 — Education Reel Hook: What Happens at 11PM With Our Chatbot"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260521_education_CB012_11pm_chatbot_flow.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
BLUE_MID    = (72, 143, 227)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
GREEN       = (34, 197, 94)

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

# Dark navy background
for y in range(1080):
    t = y / 1079
    c = lerp((10, 8, 24), (5, 5, 14), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Violet accent glow top-center
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(300, 0, -1):
    alpha = int(45 * (1 - r / 300))
    gd.ellipse([540 - r, -r, 540 + r, r], fill=(*VIOLET, alpha))
img = Image.alpha_composite(img, glow)
draw = ImageDraw.Draw(img)

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# Cinematic top bar (reel feel)
top_bar = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
tb = ImageDraw.Draw(top_bar)
tb.rectangle([0, 0, 1080, 76], fill=(0, 0, 0, 180))
img = Image.alpha_composite(img, top_bar)
draw = ImageDraw.Draw(img)
draw.text((540, 38), "11:00 PM  ·  YOUR WEBSITE", fill=(*BODY_GRAY, 220), font=get_font(24, "bold"), anchor="mm")

# Main headline
draw.text((540, 140), "THIS IS WHAT HAPPENS", fill=(*WHITE, 255), font=get_font(54, "bold"), anchor="mm")
draw.text((540, 204), "WHEN SOMEONE VISITS AT 11PM", fill=(*VIOLET, 255), font=get_font(42, "bold"), anchor="mm")
draw.text((540, 258), "— with our chatbot.", fill=(*WHITE, 200), font=get_font(34, "regular"), anchor="mm")

# Step-by-step flow cards
steps = [
    ("01", "🌐", "Visitor lands on your website", "11:03 PM — comes from Google search"),
    ("02", "💬", "Chatbot replies in 3 seconds", "\"Hi! How can I help you tonight?\""),
    ("03", "🎯", "Lead gets qualified", "Budget, timeline & needs captured"),
    ("04", "📋", "Contact saved automatically", "Name, number → Google Sheets"),
    ("05", "🌅", "Owner notified at 8AM", "\"You have 3 new qualified leads!\""),
]

CARD_Y = 296
CARD_H = 120
GAP = 10
step_colors = [VIOLET, BLUE_MID, GREEN, BLUE_MID, VIOLET]

for i, (num, icon, title, detail) in enumerate(steps):
    y1 = CARD_Y + i * (CARD_H + GAP)
    y2 = y1 + CARD_H
    col = step_colors[i]

    # Connector dot + line
    if i > 0:
        draw.line([(80, y1 - GAP), (80, y1)], fill=(*col, 120), width=2)
    draw.ellipse([68, (y1 + y2) // 2 - 12, 92, (y1 + y2) // 2 + 12], fill=(*col, 255))

    img = alpha_rect(img, [110, y1, 1020, y2], radius=14,
                     fill_rgba=(255, 255, 255, 12), outline_rgba=(*col, 60), width=1)
    draw = ImageDraw.Draw(img)
    draw.text((140, y1 + 30), f"{icon}  {title}", fill=(*WHITE, 255), font=get_font(26, "bold"), anchor="lt")
    draw.text((140, y1 + 74), detail, fill=(*BODY_GRAY, 220), font=get_font(22, "regular"), anchor="lt")
    draw.text((1000, y1 + 52), num, fill=(*col, 160), font=get_font(32, "bold"), anchor="rm")

# Result callout
draw.text((540, 960), "Result: Owner wakes up to warm leads. Zero effort.",
          fill=(*WHITE, 240), font=get_font(26, "bold"), anchor="mm")

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
