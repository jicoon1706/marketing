"""CB-013 — Education Carousel Cover: 5 Things to Check Before Investing"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260522_education_CB013_5things_check_before_invest.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
BLUE_MID    = (72, 143, 227)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
GREEN       = (34, 197, 94)
RED         = (239, 68, 68)

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

# Background: deep navy to purple
for y in range(1080):
    t = y / 1079
    c = lerp((12, 8, 28), (45, 25, 80), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 90))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# "1 of 5" badge
img = alpha_rect(img, [888, 34, 1026, 68], radius=16,
                 fill_rgba=(255, 255, 255, 30), outline_rgba=(255, 255, 255, 60), width=1)
draw = ImageDraw.Draw(img)
draw.text((957, 51), "1 of 5", fill=(*WHITE, 214), font=get_font(22, "regular"), anchor="mm")

# Headline block
draw.text((540, 138), "Before You Invest", fill=(*WHITE, 255), font=get_font(72, "bold"), anchor="mm")
draw.text((540, 222), "In A Chatbot,", fill=(*WHITE, 255), font=get_font(72, "bold"), anchor="mm")
draw.text((540, 306), "Check These", fill=(*VIOLET, 255), font=get_font(80, "bold"), anchor="mm")
draw.text((540, 388), "5 Things.", fill=(*VIOLET, 255), font=get_font(80, "bold"), anchor="mm")

# Warning hook
img = alpha_rect(img, [120, 420, 960, 464], radius=16,
                 fill_rgba=(239, 68, 68, 30), outline_rgba=(239, 68, 68, 80), width=1)
draw = ImageDraw.Draw(img)
draw.text((540, 442), "⚠️  Most businesses skip slide 4.", fill=(*WHITE, 255), font=get_font(26, "bold"), anchor="mm")

# 5 checklist items
checks = [
    ("01", "Can it qualify leads automatically?"),
    ("02", "Does it send follow-ups on its own?"),
    ("03", "Can it handle after-hours traffic?"),
    ("04", "Is it trained on YOUR business?"),
    ("05", "Does it integrate with your CRM?"),
]
CARD_Y = 490
CARD_H = 86
GAP = 8
for i, (num, question) in enumerate(checks):
    y1 = CARD_Y + i * (CARD_H + GAP)
    y2 = y1 + CARD_H
    is_slide4 = (i == 3)
    fill = (*VIOLET, 40) if is_slide4 else (255, 255, 255, 12)
    border = (*VIOLET, 180) if is_slide4 else (255, 255, 255, 30)
    img = alpha_rect(img, [60, y1, 1020, y2], radius=12, fill_rgba=fill, outline_rgba=border, width=1)
    draw = ImageDraw.Draw(img)
    draw.text((96, (y1 + y2) // 2), num, fill=(*VIOLET, 255) if not is_slide4 else (*VIOLET, 255), font=get_font(22, "bold"), anchor="lm")
    draw.text((148, (y1 + y2) // 2), question, fill=(*WHITE, 255) if not is_slide4 else (*WHITE, 255), font=get_font(26, "regular"), anchor="lm")
    # Yes / No pills
    draw.text((960, (y1 + y2) // 2 - 10), "✓ Yes", fill=(*GREEN, 220), font=get_font(18, "bold"), anchor="rm")
    draw.text((960, (y1 + y2) // 2 + 14), "✗ No", fill=(*RED, 200), font=get_font(18, "regular"), anchor="rm")

# Bottom CTA
draw.text((540, 960), "Swipe to get your yes/no guide →", fill=(*BODY_GRAY, 200), font=get_font(26, "regular"), anchor="mm")

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
