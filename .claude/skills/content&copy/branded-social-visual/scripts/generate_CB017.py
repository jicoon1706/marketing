"""CB-017 — Consideration Carousel Cover: Basic. Growth. Pro. Package Comparison"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260527_consideration_CB017_basic_growth_pro.png"

VIOLET      = (123, 103, 209)
PURPLE      = (138, 93, 204)
BLUE_BRIGHT = (65, 150, 230)
BLUE_MID    = (72, 143, 227)
DARK_NAVY   = (11, 11, 20)
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

# Purple-to-purple deeper gradient
for y in range(1080):
    t = y / 1079
    c = lerp((60, 35, 130), (20, 10, 55), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 80))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# "1 of 4" badge
img = alpha_rect(img, [888, 34, 1026, 68], radius=16,
                 fill_rgba=(255, 255, 255, 30), outline_rgba=(255, 255, 255, 60), width=1)
draw = ImageDraw.Draw(img)
draw.text((957, 51), "1 of 4", fill=(*WHITE, 214), font=get_font(22, "regular"), anchor="mm")

# Headline
draw.text((540, 128), "Basic. Growth. Pro.", fill=(*WHITE, 255), font=get_font(72, "bold"), anchor="mm")
draw.text((540, 208), "Here's how to know which", fill=(*LAVENDER, 255), font=get_font(38, "regular"), anchor="mm")
draw.text((540, 258), "plan is right for you.", fill=(*WHITE, 255), font=get_font(44, "bold"), anchor="mm")
draw.line([(120, 292), (960, 292)], fill=(255, 255, 255, 60), width=1)

# 3 Package cards side by side
packages = [
    {
        "name": "Basic",
        "emoji": "🌱",
        "tag": "Getting Started",
        "features": ["AI chatbot (Botpress)", "Basic lead capture", "WhatsApp integration", "3-day response SLA"],
        "ideal": "Solo / new SME",
        "highlight": False,
    },
    {
        "name": "Growth",
        "emoji": "🚀",
        "tag": "Most Popular",
        "features": ["Everything in Basic", "n8n automation", "Google Sheets CRM", "Auto follow-up flows"],
        "ideal": "Active SME, 10+ leads/wk",
        "highlight": True,
    },
    {
        "name": "Pro",
        "emoji": "💎",
        "tag": "Full Power",
        "features": ["Everything in Growth", "Full n8n workflows", "Multi-channel support", "Priority build & support"],
        "ideal": "High-volume business",
        "highlight": False,
    },
]

CARD_Y1 = 312
CARD_Y2 = 920
CARD_W = 316
GAP = 16
START_X = (1080 - 3 * CARD_W - 2 * GAP) // 2

for i, pkg in enumerate(packages):
    cx1 = START_X + i * (CARD_W + GAP)
    cx2 = cx1 + CARD_W
    is_hi = pkg["highlight"]
    fill = (*VIOLET, 35) if not is_hi else (*VIOLET, 60)
    border = (*VIOLET, 80) if not is_hi else (*VIOLET, 255)
    bw = 1 if not is_hi else 3

    # Glow for Growth card
    if is_hi:
        glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        for r in range(80, 0, -1):
            alpha = int(30 * (1 - r / 80))
            mid_x = (cx1 + cx2) // 2
            mid_y = (CARD_Y1 + CARD_Y2) // 2
            gd.ellipse([mid_x - r, mid_y - r, mid_x + r, mid_y + r], fill=(*VIOLET, alpha))
        img = Image.alpha_composite(img, glow)

    img = alpha_rect(img, [cx1, CARD_Y1, cx2, CARD_Y2], radius=18,
                     fill_rgba=fill, outline_rgba=border, width=bw)
    draw = ImageDraw.Draw(img)

    # Tag pill
    tag_fill = (*VIOLET, 200) if is_hi else (255, 255, 255, 40)
    img = alpha_rect(img, [cx1 + 16, CARD_Y1 + 14, cx2 - 16, CARD_Y1 + 46], radius=12,
                     fill_rgba=tag_fill)
    draw = ImageDraw.Draw(img)
    draw.text(((cx1 + cx2) // 2, CARD_Y1 + 30), pkg["tag"],
              fill=(*WHITE, 255), font=get_font(16, "bold"), anchor="mm")

    # Emoji + name
    draw.text(((cx1 + cx2) // 2, CARD_Y1 + 88), pkg["emoji"],
              fill=(*WHITE, 255), font=get_font(36, "regular"), anchor="mm")
    draw.text(((cx1 + cx2) // 2, CARD_Y1 + 140), pkg["name"],
              fill=(*WHITE, 255), font=get_font(38, "bold"), anchor="mm")

    # Divider
    draw.line([(cx1 + 20, CARD_Y1 + 168), (cx2 - 20, CARD_Y1 + 168)],
              fill=(255, 255, 255, 50), width=1)

    # Features
    for j, feat in enumerate(pkg["features"]):
        fy = CARD_Y1 + 192 + j * 52
        tick_col = VIOLET if is_hi else BLUE_MID
        text_col = (*WHITE, 220) if is_hi else (*BODY_GRAY, 220)
        draw.text((cx1 + 22, fy), "✓", fill=(*tick_col, 255),
                  font=get_font(18, "bold"), anchor="lt")
        draw.text((cx1 + 44, fy), feat, fill=text_col,
                  font=get_font(18, "regular"), anchor="lt")

    # Ideal client
    draw.line([(cx1 + 20, CARD_Y2 - 68), (cx2 - 20, CARD_Y2 - 68)],
              fill=(255, 255, 255, 40), width=1)
    ideal_col = (*LAVENDER, 220) if is_hi else (*BODY_GRAY, 220)
    draw.text(((cx1 + cx2) // 2, CARD_Y2 - 40), f"Ideal: {pkg['ideal']}",
              fill=ideal_col, font=get_font(17, "regular"), anchor="mm")

# Bottom CTA
draw.text((540, 952), "DM us 'PLAN' — we'll match you to the right fit.",
          fill=(*LAVENDER, 255), font=get_font(24, "bold"), anchor="mm")

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
