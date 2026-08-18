"""CB-003 — Awareness Carousel Slide 1: Who Are We?"""

from PIL import Image, ImageDraw
import os

OUTPUT_PATH = r"c:\Users\MuhammadSyarifuddinA\marketing\social-media\20260507_awareness_CB003_who_we_are.png"

VIOLET      = (123, 103, 209)
BLUE_BRIGHT = (65, 150, 230)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)

def get_font(size, weight="regular"):
    from PIL import ImageFont
    m = {"bold": "C:/Windows/Fonts/segoeuib.ttf", "regular": "C:/Windows/Fonts/segoeui.ttf",
         "light": "C:/Windows/Fonts/segoeuil.ttf"}
    p = m.get(weight, m["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

def lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def alpha_rect(img, box, radius, fill_rgba, outline_rgba=None, width=1):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(box, radius=radius, fill=fill_rgba,
                        outline=outline_rgba, width=width)
    return Image.alpha_composite(img, layer)

# Canvas
img = Image.new("RGBA", (1080, 1080), (*VIOLET, 255))
draw = ImageDraw.Draw(img)

# Diagonal gradient: violet top to blue bottom
for y in range(1080):
    t = y / 1079
    c = lerp(VIOLET, BLUE_BRIGHT, t)
    draw.line([(0, y), (1080, y)], fill=(*c, 255))

# Dark navy overlay at ~43%
overlay = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 110))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Diagonal white stripe lines top-right (6 lines)
for i in range(6):
    off = i * 40
    x1 = 780 + off
    draw.line([(x1, 0), (1080, 1080 - x1 + 780)], fill=(*WHITE, 38), width=15)

# ── Brand Watermark (top-left) ─────────────────────────────────────────────────
draw.text((54, 34), "IGEN VERITAS", fill=(*WHITE, 196), font=get_font(20, "regular"), anchor="lt")
draw.text((54, 60), "igen-veritas.com", fill=(*WHITE, 135), font=get_font(15, "regular"), anchor="lt")

# ── "1 of 4" Pill (top-right) ─────────────────────────────────────────────────
img = alpha_rect(img, [930, 34, 1046, 70], radius=18,
                 fill_rgba=(255, 255, 255, 30), outline_rgba=(255, 255, 255, 61), width=1)
draw = ImageDraw.Draw(img)
draw.text((988, 52), "1 of 4", fill=(*WHITE, 214), font=get_font(22, "regular"), anchor="mm")

# ── Label ─────────────────────────────────────────────────────────────────────
draw.text((540, 196), "WHO ARE WE?", fill=(*WHITE, 176), font=get_font(36, "regular"), anchor="mm")

# ── Main Headline ─────────────────────────────────────────────────────────────
font_h = get_font(100, "bold")
draw.text((540, 310), "4 THINGS TO", fill=(*WHITE, 255), font=font_h, anchor="mm")
draw.text((540, 420), "KNOW ABOUT", fill=(*WHITE, 255), font=font_h, anchor="mm")
draw.text((540, 512), "IGEN VERITAS", fill=(*WHITE, 255), font=get_font(72, "bold"), anchor="mm")

# Underline accent
draw.line([(198, 548), (882, 548)], fill=(*WHITE, 176), width=5)

# ── 4 Preview Cards ────────────────────────────────────────────────────────────
cards = [("01", "Who we are"), ("02", "What we do"), ("03", "Who we help"), ("04", "Our promise")]
card_w = 222
card_h = 138
gap = 20
total_w = 4 * card_w + 3 * gap
start_x = (1080 - total_w) // 2
card_y1 = 598

for i, (num, label) in enumerate(cards):
    cx1 = start_x + i * (card_w + gap)
    cx2 = cx1 + card_w
    cy2 = card_y1 + card_h
    img = alpha_rect(img, [cx1, card_y1, cx2, cy2], radius=16,
                     fill_rgba=(255, 255, 255, 23), outline_rgba=(255, 255, 255, 59), width=1)
    draw = ImageDraw.Draw(img)
    mid_x = (cx1 + cx2) // 2
    draw.text((mid_x, card_y1 + 44), num, fill=(*WHITE, 214), font=get_font(38, "bold"), anchor="mm")
    draw.text((mid_x, card_y1 + 100), label, fill=(*WHITE, 176), font=get_font(20, "regular"), anchor="mm")

# ── Swipe CTA ─────────────────────────────────────────────────────────────────
draw.text((540, 796), "Swipe to learn more →", fill=(*WHITE, 194), font=get_font(28, "bold"), anchor="mm")

# ── Bottom Fade + Brand Strip ─────────────────────────────────────────────────
fade = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
fd = ImageDraw.Draw(fade)
for y in range(948, 1080):
    t = (y - 948) / (1080 - 948)
    fd.line([(0, y), (1080, y)], fill=(*DARK_NAVY, int(255 * t)))
img = Image.alpha_composite(img, fade)
draw = ImageDraw.Draw(img)

draw.text((540, 1008), "Intelligent Solutions  ·  Cutting-Edge Technology",
          fill=(*WHITE, 200), font=get_font(20, "regular"), anchor="mm")
draw.text((540, 1048), "igen-veritas.com", fill=(*WHITE, 180), font=get_font(18, "regular"), anchor="mm")

# Save
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.convert("RGB").save(OUTPUT_PATH, "PNG")
print(f"Saved: {OUTPUT_PATH}")
