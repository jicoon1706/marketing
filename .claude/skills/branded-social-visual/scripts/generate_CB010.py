"""CB-010 — Education Carousel Cover: 5 Things AI Chatbot Does"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260518_education_CB010_5things_chatbot_does.png"

VIOLET      = (123, 103, 209)
PURPLE      = (138, 93, 204)
BLUE_MID    = (72, 143, 227)
BLUE_BRIGHT = (65, 150, 230)
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

# Background: purple-violet gradient
for y in range(1080):
    t = y / 1079
    c = lerp((80, 45, 155), (35, 20, 90), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 110))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igenveritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# "1 of 6" badge
img = alpha_rect(img, [888, 34, 1026, 68], radius=16,
                 fill_rgba=(255, 255, 255, 30), outline_rgba=(255, 255, 255, 61), width=1)
draw = ImageDraw.Draw(img)
draw.text((957, 51), "1 of 6", fill=(*WHITE, 214), font=get_font(22, "regular"), anchor="mm")

# Headline
draw.text((540, 148), "5 THINGS AN", fill=(*WHITE, 255), font=get_font(82, "bold"), anchor="mm")
draw.text((540, 248), "AI CHATBOT", fill=(*VIOLET, 255), font=get_font(88, "bold"), anchor="mm")
draw.text((540, 344), "DOES THAT YOUR", fill=(*WHITE, 255), font=get_font(68, "bold"), anchor="mm")
draw.text((540, 424), "STAFF CANNOT.", fill=(*WHITE, 255), font=get_font(64, "bold"), anchor="mm")

# Thin divider
draw.line([(160, 460), (920, 460)], fill=(*VIOLET, 120), width=2)

# Sub-label
draw.text((540, 488), "Swipe to see each one →", fill=(*BODY_GRAY, 220), font=get_font(26, "regular"), anchor="mm")

# 5 feature cards
features = [
    ("01", "⏰", "24/7 Response", "Always on, never sleeps"),
    ("02", "🎯", "Instant Lead Qualify", "Filters serious buyers"),
    ("03", "🔄", "Auto Follow-Up", "No lead left behind"),
    ("04", "📊", "Multi-Lead Handling", "Infinite conversations"),
    ("05", "📋", "Google Sheets Sync", "Auto-saves every lead"),
]
CARD_Y = 530
CARD_H = 88
GAP = 12
for i, (num, icon, title, sub) in enumerate(features):
    y1 = CARD_Y + i * (CARD_H + GAP)
    y2 = y1 + CARD_H
    num_color = VIOLET if i % 2 == 0 else BLUE_MID
    img = alpha_rect(img, [60, y1, 1020, y2], radius=14,
                     fill_rgba=(255, 255, 255, 12), outline_rgba=(255, 255, 255, 30), width=1)
    draw = ImageDraw.Draw(img)
    draw.text((90, (y1 + y2) // 2), num, fill=(*num_color, 255), font=get_font(22, "bold"), anchor="lm")
    draw.text((138, (y1 + y2) // 2 - 14), f"{icon} {title}", fill=(*WHITE, 255), font=get_font(24, "bold"), anchor="lm")
    draw.text((138, (y1 + y2) // 2 + 16), sub, fill=(*BODY_GRAY, 220), font=get_font(20, "regular"), anchor="lm")

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
