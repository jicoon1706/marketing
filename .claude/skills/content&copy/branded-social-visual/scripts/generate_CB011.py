"""CB-011 — Social Proof: 3 Qualified Leads Before Breakfast"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260519_proof_CB011_leads_before_breakfast.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
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

# Dark navy background with violet glow
for y in range(1080):
    t = y / 1079
    c = lerp((14, 10, 30), (6, 5, 14), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Violet glow center
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(420, 0, -1):
    alpha = int(50 * (1 - r / 420))
    gd.ellipse([540 - r, 480 - r, 540 + r, 480 + r], fill=(*VIOLET, alpha))
img = Image.alpha_composite(img, glow)
draw = ImageDraw.Draw(img)

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# "CLIENT RESULT" badge
img = alpha_rect(img, [330, 106, 750, 150], radius=22,
                 fill_rgba=(*VIOLET, 180), outline_rgba=(*VIOLET, 255), width=1)
draw = ImageDraw.Draw(img)
draw.text((540, 128), "✅  CLIENT RESULT", fill=(*WHITE, 255), font=get_font(24, "bold"), anchor="mm")

# Large stat
draw.text((540, 260), "3", fill=(*VIOLET, 255), font=get_font(220, "bold"), anchor="mm")

# Stat label
draw.text((540, 378), "Qualified Leads", fill=(*WHITE, 255), font=get_font(52, "bold"), anchor="mm")
draw.text((540, 444), "Before Breakfast", fill=(*LAVENDER, 255), font=get_font(42, "regular"), anchor="mm")

# Divider
draw.line([(200, 490), (880, 490)], fill=(*VIOLET, 100), width=2)

# Pull-quote card
img = alpha_rect(img, [80, 516, 1000, 700], radius=20,
                 fill_rgba=(255, 255, 255, 12), outline_rgba=(255, 255, 255, 35), width=1)
draw = ImageDraw.Draw(img)
draw.text((540, 556), "\"I woke up to 3 new lead messages.", fill=(*WHITE, 255), font=get_font(30, "bold"), anchor="mm")
draw.text((540, 604), "The bot had already replied to all of them", fill=(*WHITE, 255), font=get_font(28, "regular"), anchor="mm")
draw.text((540, 648), "and collected their contact details.\"", fill=(*WHITE, 255), font=get_font(28, "regular"), anchor="mm")
draw.text((540, 686), "— F&B Business Owner, KL", fill=(*BODY_GRAY, 255), font=get_font(22, "regular"), anchor="mm")

# How it works mini strip
draw.text((540, 740), "HOW IT HAPPENED", fill=(*VIOLET, 200), font=get_font(20, "bold"), anchor="mm")

steps = ["Visitor landed at 2AM", "Bot replied instantly", "Lead captured & saved"]
step_x = [200, 540, 880]
for x, step in zip(step_x, steps):
    img = alpha_rect(img, [x - 130, 764, x + 130, 820], radius=12,
                     fill_rgba=(*VIOLET, 40), outline_rgba=(*VIOLET, 100), width=1)
    draw = ImageDraw.Draw(img)
    draw.text((x, 792), step, fill=(*WHITE, 220), font=get_font(19, "regular"), anchor="mm")

# Arrow connectors
draw.text((370, 790), "→", fill=(*VIOLET, 180), font=get_font(24, "bold"), anchor="mm")
draw.text((710, 790), "→", fill=(*VIOLET, 180), font=get_font(24, "bold"), anchor="mm")

# CTA
draw.text((540, 876), "Want results like this?", fill=(*LAVENDER, 255), font=get_font(30, "regular"), anchor="mm")
img = alpha_rect(img, [300, 906, 780, 954], radius=24, fill_rgba=(*VIOLET, 255))
draw = ImageDraw.Draw(img)
draw.text((540, 930), "DM us 'BOT' to get started", fill=(*WHITE, 255), font=get_font(24, "bold"), anchor="mm")

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
