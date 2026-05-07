"""CB-018 — Conversion: Setup in 5-7 Days — Process Timeline"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260528_conversion_CB018_setup_57days_timeline.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
BLUE_MID    = (72, 143, 227)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
LAVENDER    = (196, 181, 253)
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

# Dark navy to violet gradient
for y in range(1080):
    t = y / 1079
    c = lerp((10, 8, 22), (40, 25, 90), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 80))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igenveritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# Headline
draw.text((540, 148), "Setup Complete In", fill=(*WHITE, 255), font=get_font(70, "bold"), anchor="mm")
draw.text((540, 236), "5–7 Days.", fill=(*VIOLET, 255), font=get_font(88, "bold"), anchor="mm")
draw.text((540, 306), "No technical knowledge needed.", fill=(*LAVENDER, 255), font=get_font(34, "regular"), anchor="mm")

# Timeline connector line
draw.line([(540, 380), (540, 860)], fill=(*VIOLET, 60), width=3)

# 4 process steps as timeline cards
steps = [
    ("01", "📋", "Brief", "Day 1", "Share your business goals,\ntarget audience & FAQ content"),
    ("02", "🔧", "Build", "Days 2–4", "We configure your AI chatbot,\nflows & integrations"),
    ("03", "🧪", "Test", "Days 5–6", "End-to-end testing across\nall conversation scenarios"),
    ("04", "🚀", "Launch", "Day 7", "Your chatbot goes live &\nstarts capturing leads"),
]

STEP_Y_START = 378
STEP_GAP = 122
step_colors = [BLUE_MID, VIOLET, BLUE_MID, GREEN]
CARD_W = 820

for i, (num, icon, title, day, desc) in enumerate(steps):
    cy = STEP_Y_START + i * STEP_GAP
    col = step_colors[i]
    is_last = (i == 3)

    # Timeline dot
    dot_layer = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    dl = ImageDraw.Draw(dot_layer)
    dl.ellipse([527, cy - 16, 553, cy + 16], fill=(*col, 255))
    img = Image.alpha_composite(img, dot_layer)
    draw = ImageDraw.Draw(img)
    draw.text((540, cy), num, fill=(*WHITE, 255), font=get_font(16, "bold"), anchor="mm")

    # Card (alternates left/right feel — all centered here)
    cx1 = (1080 - CARD_W) // 2
    cx2 = cx1 + CARD_W
    card_y1 = cy - 50
    card_y2 = cy + 58
    fill_col = (*GREEN, 40) if is_last else (255, 255, 255, 12)
    border_col = (*GREEN, 150) if is_last else (*col, 70)
    img = alpha_rect(img, [cx1, card_y1, cx2, card_y2], radius=16,
                     fill_rgba=fill_col, outline_rgba=border_col, width=1)
    draw = ImageDraw.Draw(img)

    # Icon + title + day
    draw.text((cx1 + 36, cy - 16), f"{icon}  {title}", fill=(*WHITE, 255), font=get_font(28, "bold"), anchor="lt")
    draw.text((cx2 - 20, cy - 16), day, fill=(*col, 255), font=get_font(22, "bold"), anchor="rt")
    # Description (split at \n)
    for j, line in enumerate(desc.split("\n")):
        draw.text((cx1 + 36, cy + 10 + j * 26), line, fill=(*BODY_GRAY, 210), font=get_font(20, "regular"), anchor="lt")

# "Your chatbot goes live fast." callout
img = alpha_rect(img, [160, 882, 920, 928], radius=24,
                 fill_rgba=(*GREEN, 50), outline_rgba=(*GREEN, 150), width=1)
draw = ImageDraw.Draw(img)
draw.text((540, 905), "✅  Your chatbot goes live fast.", fill=(*GREEN, 255), font=get_font(26, "bold"), anchor="mm")

# CTA
draw.text((540, 960), "DM us 'START' — let's build yours this week.",
          fill=(*LAVENDER, 255), font=get_font(24, "regular"), anchor="mm")

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
