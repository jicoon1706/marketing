"""CB-014 — Social Proof: Before/After — 0 Replies vs 11 Leads"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260523_proof_CB014_before_after_11leads.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
GREEN       = (34, 197, 94)
RED         = (239, 68, 68)
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

# Background: dark navy
for y in range(1080):
    t = y / 1079
    c = lerp((10, 8, 20), (5, 4, 12), t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Brand watermark
draw.text((54, 42), "IGEN VERITAS", fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 68), "igen-veritas.com", fill=(*BODY_GRAY, 255), font=get_font(15, "regular"), anchor="lt")

# "CLIENT RESULT" badge
img = alpha_rect(img, [330, 96, 750, 140], radius=22,
                 fill_rgba=(*GREEN, 60), outline_rgba=(*GREEN, 160), width=1)
draw = ImageDraw.Draw(img)
draw.text((540, 118), "📊  CLIENT RESULT", fill=(*GREEN, 255), font=get_font(24, "bold"), anchor="mm")

# Before/After split (y: 160–860)
MID = 540

# LEFT: Before (dark, dead)
img = alpha_rect(img, [40, 160, MID - 20, 860], radius=18,
                 fill_rgba=(20, 10, 10, 255), outline_rgba=(239, 68, 68, 60), width=1)
draw = ImageDraw.Draw(img)

# Dead phone screen (before)
img = alpha_rect(img, [80, 200, 496, 580], radius=14,
                 fill_rgba=(8, 6, 6, 255), outline_rgba=(50, 30, 30, 255), width=2)
draw = ImageDraw.Draw(img)
# Phone content - blank
draw.text((288, 330), "📵", fill=(*RED, 180), font=get_font(64, "regular"), anchor="mm")
draw.text((288, 420), "No chatbot active.", fill=(100, 60, 60, 255), font=get_font(20, "regular"), anchor="mm")
draw.text((288, 456), "No auto-replies.", fill=(80, 50, 50, 255), font=get_font(20, "regular"), anchor="mm")

# Before stats
draw.text((288, 630), "BEFORE", fill=(*RED, 200), font=get_font(28, "bold"), anchor="mm")
draw.text((288, 690), "0", fill=(*RED, 255), font=get_font(90, "bold"), anchor="mm")
draw.text((288, 760), "Replies after hours", fill=(*BODY_GRAY, 220), font=get_font(22, "regular"), anchor="mm")
draw.text((288, 800), "Leads: unknown (lost)", fill=(140, 80, 80, 255), font=get_font(20, "regular"), anchor="mm")

# Center violet divider
divider = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
dd = ImageDraw.Draw(divider)
for y in range(160, 860):
    t = (y - 160) / 700
    dd.line([(MID - 2, y), (MID + 2, y)], fill=(*VIOLET, 255))
img = Image.alpha_composite(img, divider)
draw = ImageDraw.Draw(img)

# "AFTER" arrow badge
img = alpha_rect(img, [MID - 40, 490, MID + 40, 540], radius=24,
                 fill_rgba=(*VIOLET, 255))
draw = ImageDraw.Draw(img)
draw.text((MID, 515), "→", fill=(*WHITE, 255), font=get_font(28, "bold"), anchor="mm")

# RIGHT: After (glowing, active)
# Violet glow behind right panel
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(200, 0, -1):
    alpha = int(35 * (1 - r / 200))
    gd.ellipse([790 - r, 510 - r, 790 + r, 510 + r], fill=(*VIOLET, alpha))
img = Image.alpha_composite(img, glow)
img = alpha_rect(img, [MID + 20, 160, 1040, 860], radius=18,
                 fill_rgba=(15, 10, 30, 255), outline_rgba=(*VIOLET, 120), width=2)
draw = ImageDraw.Draw(img)

# Glowing phone screen (after)
img = alpha_rect(img, [MID + 44, 200, 1000, 580], radius=14,
                 fill_rgba=(20, 14, 40, 255), outline_rgba=(*VIOLET, 80), width=1)
draw = ImageDraw.Draw(img)

# Chat bubbles in phone
chats = [
    ("Visitor: Hi, still open? 👋", False, 220),
    ("Bot: Yes! How can I help? 😊", True, 250),
    ("Visitor: I need a quote.", False, 220),
    ("Bot: Got it! Sending now ✅", True, 250),
]
chat_y = 230
for text, is_bot, opacity in chats:
    bg = (*VIOLET, 200) if is_bot else (50, 35, 80, 200)
    bx1 = MID + 60 if not is_bot else MID + 160
    bx2 = MID + 470 if not is_bot else MID + 520
    img = alpha_rect(img, [bx1, chat_y, bx2, chat_y + 46], radius=10, fill_rgba=bg)
    draw = ImageDraw.Draw(img)
    cx = (bx1 + bx2) // 2
    draw.text((cx, chat_y + 23), text, fill=(*WHITE, opacity), font=get_font(16, "regular"), anchor="mm")
    chat_y += 58

# After stats
draw.text((792, 630), "AFTER", fill=(*GREEN, 200), font=get_font(28, "bold"), anchor="mm")
draw.text((792, 690), "11", fill=(*GREEN, 255), font=get_font(90, "bold"), anchor="mm")
draw.text((792, 760), "Leads — first week", fill=(*WHITE, 220), font=get_font(22, "regular"), anchor="mm")
draw.text((792, 800), "All captured. Auto. 24/7.", fill=(*LAVENDER, 220), font=get_font(20, "regular"), anchor="mm")

# Footer CTA
draw.text((540, 900), "Your business can do this too.", fill=(*LAVENDER, 255), font=get_font(30, "regular"), anchor="mm")
img = alpha_rect(img, [280, 928, 800, 974], radius=24, fill_rgba=(*VIOLET, 255))
draw = ImageDraw.Draw(img)
draw.text((540, 951), "DM us 'RESULTS' to find out how", fill=(*WHITE, 255), font=get_font(22, "bold"), anchor="mm")

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
