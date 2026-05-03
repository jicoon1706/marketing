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

# Deep purple → near-black navy diagonal
for y in range(H):
    t = y / H
    r = int(45 + (11 - 45) * t)
    g = int(25 + (11 - 25) * t)
    b = int(106 + (30 - 106) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# Radial glow top-right violet
glow1 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd1 = ImageDraw.Draw(glow1)
for r in range(320, 0, -2):
    a = int(38 * (1 - r/320))
    gd1.ellipse([920-r, 80-r, 920+r, 80+r], fill=(123, 103, 209, a))
img = Image.alpha_composite(img, glow1)

# Radial glow bottom-left blue
glow2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd2 = ImageDraw.Draw(glow2)
for r in range(260, 0, -2):
    a = int(28 * (1 - r/260))
    gd2.ellipse([100-r, 960-r, 100+r, 960+r], fill=(65, 150, 230, a))
img = Image.alpha_composite(img, glow2)
draw = ImageDraw.Draw(img)

# Brand tag
draw.text((48, 38), "IGEN VERITAS", fill=(255, 255, 255, 155), font=get_font(20))
draw.text((48, 64), "igenveritas.com", fill=(107, 114, 128, 155), font=get_font(15))

# "Quick question:" pill
qpill = Image.new("RGBA", (W, H), (0, 0, 0, 0))
qpd = ImageDraw.Draw(qpill)
qpd.rounded_rectangle([338, 138, 742, 183], radius=20, fill=(123, 103, 209, 205), outline=(123, 103, 209, 255), width=1)
img = Image.alpha_composite(img, qpill)
draw = ImageDraw.Draw(img)
draw.text((540, 160), "Quick question:", fill=(255, 255, 255, 255), font=get_font(22), anchor="mm")

# Main question — 4 lines, last line in violet
lines = ["How long does", "your team take", "to reply to a", "new enquiry?"]
colors = [(255,255,255,255),(255,255,255,255),(255,255,255,255),(123,103,209,255)]
y_pos  = [276, 361, 446, 531]
for line, col, yp in zip(lines, colors, y_pos):
    draw.text((540, yp), line, fill=col, font=get_font(76, "bold"), anchor="mm")

# "Be honest. 👀"
draw.text((540, 618), "Be honest. 👀", fill=(200, 190, 240, 195), font=get_font(32), anchor="mm")

# Divider
draw.line([(118, 668), (962, 668)], fill=(123, 103, 209, 170), width=1)

# Poll cards
poll_data = [
    ("⚡  Under 5 minutes",        (18, 78, 38, 182), (28, 115, 56, 150)),
    ("⏰  Within the hour",         (58, 38, 118, 182), (88, 58, 148, 150)),
    ("🌙  A few hours later",       (98, 68, 18, 182), (138, 98, 28, 150)),
    ("❌  We miss some enquiries",  (98, 18, 18, 182), (148, 28, 28, 150)),
]
py_start, ph, pgap = 692, 62, 8
for i, (text, fill, outline) in enumerate(poll_data):
    py = py_start + i * (ph + pgap)
    pov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pd = ImageDraw.Draw(pov)
    pd.rounded_rectangle([118, py, 962, py+ph], radius=14, fill=fill, outline=outline, width=1)
    img = Image.alpha_composite(img, pov)
    draw = ImageDraw.Draw(img)
    draw.text((540, py + ph//2), text, fill=(255, 255, 255, 228), font=get_font(22), anchor="mm")

# Bottom CTAs
draw.text((540, 1002), "Comment your answer below ⬇", fill=(255, 255, 255, 195), font=get_font(24), anchor="mm")
draw.text((540, 1046), "Or DM us — we'll show you a better way.", fill=(123, 103, 209, 255), font=get_font(22, "bold"), anchor="mm")

os.makedirs("social-media", exist_ok=True)
img.convert("RGB").save("social-media/20260506_engagement_CB004_reply_time.png", "PNG")
print("Saved: social-media/20260506_engagement_CB004_reply_time.png")
