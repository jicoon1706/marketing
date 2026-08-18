from PIL import Image, ImageDraw, ImageFont
import os, math

def get_font(size, weight="regular"):
    font_map = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    return ImageFont.truetype(path, size) if os.path.exists(path) else ImageFont.load_default()

W, H = 1080, 1080
img = Image.new("RGBA", (W, H), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# Dark navy gradient deepening toward bottom
for y in range(H):
    t = y / H
    draw.line([(0, y), (W, y)], fill=(int(11+5*t), int(11+3*t), int(20+15*t), 255))

# Radial violet glow upper-center
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(420, 0, -2):
    a = min(int(55 * (1 - r/420) * (r/420) * 4.5), 38)
    gd.ellipse([540-r, 340-r, 540+r, 340+r], fill=(123, 103, 209, a))
img = Image.alpha_composite(img, glow)

# Bottom-right blue glow
glow2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd2 = ImageDraw.Draw(glow2)
for r in range(280, 0, -2):
    a = int(25 * (1 - r/280))
    gd2.ellipse([920-r, 920-r, 920+r, 920+r], fill=(65, 150, 230, a))
img = Image.alpha_composite(img, glow2)
draw = ImageDraw.Draw(img)

# Tech grid
for x in range(0, W, 90):
    draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 12))
for y in range(0, H, 90):
    draw.line([(0, y), (W, y)], fill=(255, 255, 255, 12))

# Diagonal accent lines
for offset, color, alpha in [(200, (123,103,209), 18), (400, (65,143,227), 12), (600, (123,103,209), 10)]:
    draw.line([(0, offset), (offset, 0)], fill=(*color, alpha), width=1)
draw.line([(W, 600), (W-500, H)], fill=(123, 103, 209, 10), width=1)

# Brand watermark top-left
draw.text((48, 38), "IGEN VERITAS", fill=(255, 255, 255, 190), font=get_font(20))
draw.text((48, 64), "igen-veritas.com", fill=(107, 114, 128, 190), font=get_font(15))

# Circular emblem at (540, 360)
cx, cy = 540, 360
draw.ellipse([cx-80, cy-80, cx+80, cy+80], outline=(123, 103, 209, 255), width=2)
inner = Image.new("RGBA", (W, H), (0, 0, 0, 0))
idraw = ImageDraw.Draw(inner)
idraw.ellipse([cx-74, cy-74, cx+74, cy+74], fill=(123, 103, 209, 135))
img = Image.alpha_composite(img, inner)
draw = ImageDraw.Draw(img)
for i in range(12):
    angle = (i * 30 - 90) * math.pi / 180
    dx = int(cx + 67 * math.cos(angle))
    dy = int(cy + 67 * math.sin(angle))
    if i % 3 == 0:
        draw.ellipse([dx-5, dy-5, dx+5, dy+5], fill=(123, 103, 209, 255))
    else:
        draw.ellipse([dx-3, dy-3, dx+3, dy+3], fill=(255, 255, 255, 90))
draw.text((cx, cy), "IV", fill=(255, 255, 255, 255), font=get_font(68, "bold"), anchor="mm")

# IGEN / VERITAS
draw.text((540, 528), "IGEN", fill=(123, 103, 209, 255), font=get_font(80, "bold"), anchor="mm")
draw.text((540, 614), "VERITAS", fill=(255, 255, 255, 255), font=get_font(80, "bold"), anchor="mm")

# Divider
draw.line([(330, 660), (750, 660)], fill=(123, 103, 209, 160), width=1)

# Tagline
draw.text((540, 706), "Powering the future —", fill=(123, 103, 209, 255), font=get_font(30), anchor="mm")
draw.text((540, 750), "one smart business at a time.", fill=(200, 200, 212, 255), font=get_font(28), anchor="mm")

# Services strip
draw.text((540, 826), "AI Chatbot  ·  Web Dev  ·  Mobile App  ·  Automation",
          fill=(255, 255, 255, 195), font=get_font(20), anchor="mm")

# Bottom accent strip
for y in range(1000, H):
    t = (y - 1000) / (H - 1000)
    r = int(123 + (65 - 123) * t)
    g = int(103 + (150 - 103) * t)
    b = int(209 + (230 - 209) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b, int(200 * t)))
draw.text((540, 1038), "Intelligent Solutions  ·  Cutting-Edge Technology",
          fill=(255, 255, 255, 215), font=get_font(19), anchor="mm")

os.makedirs("social-media", exist_ok=True)
img.convert("RGB").save("social-media/20260501_awareness_CB001_brand_intro.png", "PNG")
print("Saved: social-media/20260501_awareness_CB001_brand_intro.png")
