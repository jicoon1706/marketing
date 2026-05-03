from PIL import Image, ImageDraw, ImageFont
import os

def get_font(size, weight="regular"):
    font_map = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    return ImageFont.truetype(path, size) if os.path.exists(path) else ImageFont.load_default()

W, H = 1080, 1080
img = Image.new("RGBA", (W, H), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# Violet → blue gradient
for y in range(H):
    t = y / H
    r = int(123 + (65 - 123) * t)
    g = int(103 + (150 - 103) * t)
    b = int(209 + (230 - 209) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# Dark overlay for depth
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
od.rectangle([0, 0, W, H], fill=(11, 11, 20, 110))
img = Image.alpha_composite(img, ov)
draw = ImageDraw.Draw(img)

# Decorative diagonal stripe top-right
for i in range(6):
    offset = 80 * i
    draw.line([(W - offset, 0), (W, offset)], fill=(255, 255, 255, 15), width=18)

# Brand watermark
draw.text((48, 38), "IGEN VERITAS", fill=(255, 255, 255, 195), font=get_font(20))
draw.text((48, 64), "igenveritas.com", fill=(255, 255, 255, 135), font=get_font(15))

# "1 of 4" pill top-right
pill1 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
p1d = ImageDraw.Draw(pill1)
p1d.rounded_rectangle([852, 34, 1026, 70], radius=14, fill=(255, 255, 255, 30), outline=(255, 255, 255, 60), width=1)
img = Image.alpha_composite(img, pill1)
draw = ImageDraw.Draw(img)
draw.text((939, 52), "1 of 4", fill=(255, 255, 255, 215), font=get_font(20), anchor="mm")

# WHO ARE WE? label
draw.text((540, 196), "WHO ARE WE?", fill=(255, 255, 255, 175), font=get_font(36), anchor="mm")

# Main headline stacked
draw.text((540, 310), "4 THINGS TO", fill=(255, 255, 255, 255), font=get_font(100, "bold"), anchor="mm")
draw.text((540, 420), "KNOW ABOUT", fill=(255, 255, 255, 255), font=get_font(100, "bold"), anchor="mm")

# IGEN VERITAS in large accent
draw.text((540, 512), "IGEN VERITAS", fill=(255, 255, 255, 255), font=get_font(72, "bold"), anchor="mm")

# Underline
draw.rounded_rectangle([198, 546, 882, 551], radius=2, fill=(255, 255, 255, 175))

# 4 cards preview
cards = [("01", "Who we are"), ("02", "What we do"), ("03", "Who we help"), ("04", "Our promise")]
cw, cy_base = 222, 598
cx_start = 76
for i, (num, label) in enumerate(cards):
    cx = cx_start + i * (cw + 14)
    card_ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cad = ImageDraw.Draw(card_ov)
    cad.rounded_rectangle([cx, cy_base, cx+cw, cy_base+138], radius=16,
                           fill=(255, 255, 255, 22), outline=(255, 255, 255, 58), width=1)
    img = Image.alpha_composite(img, card_ov)
    draw = ImageDraw.Draw(img)
    draw.text((cx + cw//2, cy_base + 48), num, fill=(255, 255, 255, 215),
              font=get_font(38, "bold"), anchor="mm")
    draw.text((cx + cw//2, cy_base + 106), label, fill=(255, 255, 255, 175),
              font=get_font(20), anchor="mm")

# Swipe CTA
draw.text((540, 796), "Swipe to learn more →", fill=(255, 255, 255, 195), font=get_font(28, "bold"), anchor="mm")

# Bottom fade + brand line
for y in range(948, H):
    t = (y - 948) / (H - 948)
    draw.line([(0, y), (W, y)], fill=(11, 11, 20, int(185 * t)))
draw.text((540, 1008), "Intelligent Solutions  ·  Cutting-Edge Technology",
          fill=(255, 255, 255, 195), font=get_font(20), anchor="mm")
draw.text((540, 1048), "igenveritas.com", fill=(255, 255, 255, 155), font=get_font(18), anchor="mm")

os.makedirs("social-media", exist_ok=True)
img.convert("RGB").save("social-media/20260505_awareness_CB003_who_we_are.png", "PNG")
print("Saved: social-media/20260505_awareness_CB003_who_we_are.png")
