from PIL import Image, ImageDraw, ImageFont
import os, math

img = Image.new("RGBA", (1080, 1080), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# Dark navy gradient background
for y in range(1080):
    t = y / 1080
    r = int(11 + (25 - 11) * t)
    g = int(11 + (8 - 11) * t)
    b = int(20 + (40 - 20) * t)
    draw.line([(0, y), (1080, y)], fill=(r, g, b, 255))

# Radial violet glow at center-upper
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for i in range(30, 0, -1):
    alpha = int(12 * (i / 30))
    rs = i * 18
    gd.ellipse([540 - rs, 340 - rs, 540 + rs, 340 + rs], fill=(123, 103, 209, alpha))
img = Image.alpha_composite(img, glow)

# Blue accent glow bottom-right
glow2 = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd2 = ImageDraw.Draw(glow2)
for i in range(20, 0, -1):
    alpha = int(8 * (i / 20))
    rs = i * 20
    gd2.ellipse([900 - rs, 850 - rs, 900 + rs, 850 + rs], fill=(65, 150, 230, alpha))
img = Image.alpha_composite(img, glow2)
draw = ImageDraw.Draw(img)

# Subtle grid lines
for i in range(0, 1080, 90):
    draw.line([(i, 0), (i, 1080)], fill=(255, 255, 255, 6))
    draw.line([(0, i), (1080, i)], fill=(255, 255, 255, 6))

# Diagonal accent lines
draw.line([(0, 600), (500, 100)], fill=(123, 103, 209, 35), width=1)
draw.line([(580, 1080), (1080, 200)], fill=(65, 150, 230, 25), width=1)

def get_font(size, weight="regular"):
    font_map = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    return ImageFont.truetype(path, size) if os.path.exists(path) else ImageFont.load_default()

# Top-left brand tag
draw.text((60, 58), "IGEN VERITAS", fill=(255, 255, 255, 160), font=get_font(20, "regular"))
draw.text((60, 86), "igen-veritas.com", fill=(107, 114, 128, 255), font=get_font(15, "regular"))

# Logo mark — outer ring
cx, cy = 540, 360
draw.ellipse([cx-115, cy-115, cx+115, cy+115], outline=(123, 103, 209, 160), width=2)
# Inner filled circle
inner = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
inner_d = ImageDraw.Draw(inner)
inner_d.ellipse([cx-88, cy-88, cx+88, cy+88], fill=(123, 103, 209, 55))
img = Image.alpha_composite(img, inner)
draw = ImageDraw.Draw(img)

# Dot ring around logo
for i in range(12):
    angle = i * 30 * math.pi / 180 - math.pi / 2
    dx = int(cx + 108 * math.cos(angle))
    dy = int(cy + 108 * math.sin(angle))
    col = (123, 103, 209, 220) if i % 3 == 0 else (255, 255, 255, 50)
    draw.ellipse([dx-4, dy-4, dx+4, dy+4], fill=col)

# IV monogram
draw.text((cx, cy), "IV", fill=(255, 255, 255, 255), font=get_font(70, "bold"), anchor="mm")

# Main company name
draw.text((540, 530), "IGEN", fill=(123, 103, 209, 255), font=get_font(80, "bold"), anchor="mm")
draw.text((540, 615), "VERITAS", fill=(255, 255, 255, 255), font=get_font(80, "bold"), anchor="mm")

# Thin divider
draw.line([(300, 668), (780, 668)], fill=(123, 103, 209, 80), width=1)

# Tagline line 1 (violet)
draw.text((540, 710), "Powering the future —", fill=(123, 103, 209, 255), font=get_font(30, "regular"), anchor="mm")
# Tagline line 2 (white)
draw.text((540, 755), "one smart business at a time.", fill=(210, 210, 210, 255), font=get_font(28, "regular"), anchor="mm")

# Services row
services = ["AI Chatbot", "·", "Web Dev", "·", "Mobile App", "·", "Automation"]
colors = [(255,255,255,200), (123,103,209,180), (255,255,255,200), (123,103,209,180),
          (255,255,255,200), (123,103,209,180), (255,255,255,200)]
total_w = 0
widths = []
sfont = get_font(20, "regular")
for s in services:
    bb = draw.textbbox((0, 0), s, font=sfont)
    w = bb[2] - bb[0]
    widths.append(w)
    total_w += w + 18
start_x = 540 - total_w // 2
cur_x = start_x
for s, c, w in zip(services, colors, widths):
    draw.text((cur_x, 830), s, fill=c, font=sfont)
    cur_x += w + 18

# Bottom accent strip gradient
strip_img = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
strip_d = ImageDraw.Draw(strip_img)
for y in range(1000, 1080):
    t = (y - 1000) / 80
    r = int(123 + (65 - 123) * t)
    g = int(103 + (150 - 103) * t)
    b = int(209 + (230 - 209) * t)
    alpha = int(220 * t)
    strip_d.line([(0, y), (1080, y)], fill=(r, g, b, alpha))
img = Image.alpha_composite(img, strip_img)
draw = ImageDraw.Draw(img)

# Bottom text on strip
draw.text((540, 1048), "Intelligent Solutions · Cutting-Edge Technology",
          fill=(255, 255, 255, 230), font=get_font(19, "regular"), anchor="mm")

os.makedirs("social-media", exist_ok=True)
img = img.convert("RGB")
img.save("social-media/20260501_awareness_CB001_brand_intro.png", "PNG")
print("Saved: social-media/20260501_awareness_CB001_brand_intro.png")
