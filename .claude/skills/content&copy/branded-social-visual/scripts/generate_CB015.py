"""CB-015 — Consideration Carousel Cover: 3 Questions to Find Your Plan"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260525_consideration_CB015_3questions_find_your_plan.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
BLUE_MID    = (72, 143, 227)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)

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

# Background: deep navy to violet
for y in range(1080):
    t = y / 1079
    c = lerp((10, 8, 24), (50, 30, 100), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 100))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igenveritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# "1 of 3" badge
img = alpha_rect(img, [888, 34, 1026, 68], radius=16,
                 fill_rgba=(255, 255, 255, 30), outline_rgba=(255, 255, 255, 60), width=1)
draw = ImageDraw.Draw(img)
draw.text((957, 51), "1 of 3", fill=(*WHITE, 214), font=get_font(22, "regular"), anchor="mm")

# Hook question headline
draw.text((540, 140), "Not Sure Which", fill=(*WHITE, 255), font=get_font(72, "bold"), anchor="mm")
draw.text((540, 226), "Chatbot Solution", fill=(*VIOLET, 255), font=get_font(72, "bold"), anchor="mm")
draw.text((540, 312), "Fits Your Business?", fill=(*WHITE, 255), font=get_font(62, "bold"), anchor="mm")

# Sub-label
img = alpha_rect(img, [160, 348, 920, 392], radius=18,
                 fill_rgba=(*BLUE_MID, 40), outline_rgba=(*BLUE_MID, 100), width=1)
draw = ImageDraw.Draw(img)
draw.text((540, 370), "Answer these 3 questions first.", fill=(*WHITE, 255), font=get_font(28, "bold"), anchor="mm")

# 3 question framework cards (large, visual)
questions = [
    ("01", "🏢", "Business Size", "Startup / SME / Growing brand?"),
    ("02", "📈", "Lead Volume", "How many enquiries per week?"),
    ("03", "⚡", "Current Reply Speed", "Instant / Within hours / Often missed?"),
]
CARD_Y = 420
CARD_H = 148
GAP = 18
colors = [VIOLET, BLUE_MID, VIOLET]

for i, (num, icon, q_title, q_sub) in enumerate(questions):
    y1 = CARD_Y + i * (CARD_H + GAP)
    y2 = y1 + CARD_H
    col = colors[i]
    img = alpha_rect(img, [60, y1, 1020, y2], radius=18,
                     fill_rgba=(255, 255, 255, 12), outline_rgba=(*col, 80), width=1)
    draw = ImageDraw.Draw(img)

    # Number circle
    num_layer = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    nd = ImageDraw.Draw(num_layer)
    nd.ellipse([80, y1 + 30, 140, y1 + 90], fill=(*col, 200))
    img = Image.alpha_composite(img, num_layer)
    draw = ImageDraw.Draw(img)
    draw.text((110, y1 + 60), num, fill=(*WHITE, 255), font=get_font(26, "bold"), anchor="mm")

    draw.text((170, y1 + 44), f"{icon}  {q_title}", fill=(*WHITE, 255), font=get_font(32, "bold"), anchor="lt")
    draw.text((170, y1 + 92), q_sub, fill=(*BODY_GRAY, 220), font=get_font(26, "regular"), anchor="lt")

# CTA slide preview
draw.text((540, 916), "Slide 3 tells you exactly which plan fits.",
          fill=(*BODY_GRAY, 220), font=get_font(24, "regular"), anchor="mm")
img = alpha_rect(img, [240, 942, 840, 986], radius=24, fill_rgba=(*VIOLET, 255))
draw = ImageDraw.Draw(img)
draw.text((540, 964), "Swipe → or DM us 'PLAN' to skip ahead",
          fill=(*WHITE, 255), font=get_font(22, "bold"), anchor="mm")

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
