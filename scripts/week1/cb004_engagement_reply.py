from PIL import Image, ImageDraw, ImageFont
import os

img = Image.new("RGBA", (1080, 1080), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

def get_font(size, weight="regular"):
    font_map = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    return ImageFont.truetype(path, size) if os.path.exists(path) else ImageFont.load_default()

# Dark violet-to-navy diagonal gradient
for y in range(1080):
    t = y / 1080
    r = int(45 + (11 - 45) * t)
    g = int(25 + (11 - 25) * t)
    b = int(90 + (30 - 90) * t)
    draw.line([(0, y), (1080, y)], fill=(r, g, b, 255))

# Top-right violet glow
glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for i in range(22, 0, -1):
    alpha = int(10 * (i / 22))
    rs = i * 22
    gd.ellipse([950 - rs, 130 - rs, 950 + rs, 130 + rs], fill=(123, 103, 209, alpha))
img = Image.alpha_composite(img, glow)

# Bottom-left blue glow
glow2 = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
gd2 = ImageDraw.Draw(glow2)
for i in range(18, 0, -1):
    alpha = int(8 * (i / 18))
    rs = i * 20
    gd2.ellipse([130 - rs, 950 - rs, 130 + rs, 950 + rs], fill=(65, 150, 230, alpha))
img = Image.alpha_composite(img, glow2)
draw = ImageDraw.Draw(img)

# Brand tag top-left
draw.text((60, 58), "IGEN VERITAS", fill=(255, 255, 255, 160), font=get_font(20, "regular"))
draw.text((60, 86), "igen-veritas.com", fill=(107, 114, 128, 255), font=get_font(15, "regular"))

# "Quick question:" label
draw.rounded_rectangle([60, 160, 310, 200], radius=16, fill=(123, 103, 209, 80),
                        outline=(123, 103, 209, 120))
draw.text((185, 180), "Quick question:", fill=(255, 255, 255, 230),
          font=get_font(20, "regular"), anchor="mm")

# Main bold question — centered, large
q_lines = [
    "How long does",
    "your team take",
    "to reply to a",
    "new enquiry?",
]
line_y = 260
for i, line in enumerate(q_lines):
    col = (255, 255, 255, 255) if i < 3 else (123, 103, 209, 255)
    draw.text((540, line_y + i * 90), line, fill=col, font=get_font(76, "bold"), anchor="mm")

# Subtitle
draw.text((540, 640), "Be honest. 👀", fill=(180, 180, 200, 200), font=get_font(32, "regular"), anchor="mm")

# Thin divider
draw.line([(200, 690), (880, 690)], fill=(123, 103, 209, 80), width=1)

# Poll options — glassmorphism cards
options = [
    ("⚡ Under 5 minutes", (40, 200, 100, 60), (40, 200, 100, 120)),
    ("⏰ Within the hour", (123, 103, 209, 50), (123, 103, 209, 100)),
    ("🌙 A few hours later", (200, 150, 50, 40), (200, 150, 50, 90)),
    ("❌ We miss some enquiries", (180, 50, 50, 40), (180, 50, 50, 80)),
]
opt_y = 715
for text, fill, outline in options:
    card = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle([120, opt_y, 960, opt_y + 54], radius=14, fill=fill, outline=outline)
    img = Image.alpha_composite(img, card)
    draw = ImageDraw.Draw(img)
    draw.text((540, opt_y + 27), text, fill=(255, 255, 255, 230),
              font=get_font(22, "regular"), anchor="mm")
    opt_y += 66

# Bottom CTA
draw.text((540, 1000), "Comment your answer below ⬇",
          fill=(255, 255, 255, 200), font=get_font(24, "regular"), anchor="mm")
draw.text((540, 1044), "Or DM us — we'll show you a better way.",
          fill=(123, 103, 209, 220), font=get_font(22, "bold"), anchor="mm")

os.makedirs("social-media", exist_ok=True)
img = img.convert("RGB")
img.save("social-media/20260506_engagement_CB004_reply_time.png", "PNG")
print("Saved: social-media/20260506_engagement_CB004_reply_time.png")
