"""CB-019 — Social Proof: Real Results This Month"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260530_proof_CB019_real_results_this_month.png"

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

# Violet-navy background
for y in range(1080):
    t = y / 1079
    c = lerp((30, 18, 70), (8, 6, 18), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Violet glow center
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(380, 0, -1):
    alpha = int(45 * (1 - r / 380))
    gd.ellipse([540 - r, 400 - r, 540 + r, 400 + r], fill=(*VIOLET, alpha))
img = Image.alpha_composite(img, glow)
draw = ImageDraw.Draw(img)

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# Month label badge
img = alpha_rect(img, [280, 100, 800, 146], radius=24,
                 fill_rgba=(*VIOLET, 60), outline_rgba=(*VIOLET, 180), width=1)
draw = ImageDraw.Draw(img)
draw.text((540, 123), "📊  MAY 2026 — CLIENT RESULTS", fill=(*WHITE, 255), font=get_font(22, "bold"), anchor="mm")

# Main headline
draw.text((540, 210), "Real Results.", fill=(*WHITE, 255), font=get_font(86, "bold"), anchor="mm")
draw.text((540, 300), "Real Businesses.", fill=(*VIOLET, 255), font=get_font(70, "bold"), anchor="mm")

# Divider
draw.line([(120, 344), (960, 344)], fill=(*VIOLET, 100), width=2)

# 3 result cards
results = [
    {
        "emoji": "🍜",
        "client": "F&B Business, KL",
        "stat": "18",
        "unit": "leads captured",
        "detail": "First week after chatbot launch",
        "sub": "All after business hours — zero manual effort",
    },
    {
        "emoji": "🏠",
        "client": "Property Agency, Selangor",
        "stat": "94%",
        "unit": "reply rate",
        "detail": "vs 23% before automation",
        "sub": "Response time: instant (was 4+ hours)",
    },
    {
        "emoji": "💆",
        "client": "Beauty & Wellness, PJ",
        "stat": "6",
        "unit": "bookings via bot",
        "detail": "In first 3 days",
        "sub": "Owner didn't touch the phone once",
    },
]

CARD_Y = 372
CARD_H = 162
GAP = 14

for i, r in enumerate(results):
    y1 = CARD_Y + i * (CARD_H + GAP)
    y2 = y1 + CARD_H
    col = [VIOLET, BLUE_MID, VIOLET][i]
    img = alpha_rect(img, [60, y1, 1020, y2], radius=18,
                     fill_rgba=(255, 255, 255, 12), outline_rgba=(*col, 70), width=1)
    draw = ImageDraw.Draw(img)

    # Emoji circle
    circ_layer = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    cl = ImageDraw.Draw(circ_layer)
    cl.ellipse([76, y1 + 26, 140, y1 + 90], fill=(*col, 80))
    img = Image.alpha_composite(img, circ_layer)
    draw = ImageDraw.Draw(img)
    draw.text((108, y1 + 58), r["emoji"], fill=(*WHITE, 255), font=get_font(30, "regular"), anchor="mm")

    # Client label
    draw.text((166, y1 + 30), r["client"], fill=(*BODY_GRAY, 220), font=get_font(19, "regular"), anchor="lt")

    # Big stat
    draw.text((166, y1 + 66), r["stat"], fill=(*col, 255), font=get_font(44, "bold"), anchor="lt")
    # Measure unit & detail on same line
    stat_w_bbox = draw.textbbox((0, 0), r["stat"], font=get_font(44, "bold"))
    stat_w = stat_w_bbox[2] - stat_w_bbox[0]
    draw.text((166 + stat_w + 12, y1 + 78), r["unit"], fill=(*WHITE, 220), font=get_font(24, "regular"), anchor="lt")

    draw.text((166, y1 + 116), r["detail"], fill=(*WHITE, 200), font=get_font(20, "bold"), anchor="lt")
    draw.text((166, y1 + 142), r["sub"], fill=(*BODY_GRAY, 180), font=get_font(18, "regular"), anchor="lt")

# Green results summary stat
draw.text((540, 920), "3 businesses. Automated. Growing.",
          fill=(*GREEN, 240), font=get_font(28, "bold"), anchor="mm")

# CTA
draw.text((540, 960), "Ready to be next? DM us 'BOT' to get started.",
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
