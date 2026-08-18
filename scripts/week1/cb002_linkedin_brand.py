from PIL import Image, ImageDraw, ImageFont
import os, textwrap

img = Image.new("RGBA", (1080, 1080), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# Violet-to-navy diagonal gradient
for y in range(1080):
    t = y / 1080
    r = int(50 + (11 - 50) * t)
    g = int(30 + (11 - 30) * t)
    b = int(120 + (40 - 120) * t)
    draw.line([(0, y), (1080, y)], fill=(r, g, b, 255))

# Diagonal stripe accent (top-right)
stripe = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
sd = ImageDraw.Draw(stripe)
sd.polygon([(700, 0), (1080, 0), (1080, 380)], fill=(123, 103, 209, 30))
img = Image.alpha_composite(img, stripe)

# Bottom-left dark panel
panel = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
pd = ImageDraw.Draw(panel)
pd.polygon([(0, 650), (0, 1080), (1080, 1080), (1080, 800)], fill=(11, 11, 20, 180))
img = Image.alpha_composite(img, panel)
draw = ImageDraw.Draw(img)

def get_font(size, weight="regular"):
    font_map = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    return ImageFont.truetype(path, size) if os.path.exists(path) else ImageFont.load_default()

# LinkedIn badge top-right
draw.rounded_rectangle([820, 48, 1022, 88], radius=20, fill=(255, 255, 255, 25))
draw.text((921, 68), "LinkedIn", fill=(255, 255, 255, 200), font=get_font(18, "regular"), anchor="mm")

# Top brand label
draw.text((60, 58), "IGEN VERITAS", fill=(255, 255, 255, 200), font=get_font(22, "bold"))
draw.text((60, 88), "igen-veritas.com", fill=(107, 114, 128, 255), font=get_font(15, "regular"))

# Violet accent bar left edge
draw.rounded_rectangle([58, 160, 66, 420], radius=4, fill=(123, 103, 209, 255))

# Headline — large bold
draw.text((100, 180), "We started", fill=(255, 255, 255, 255), font=get_font(68, "bold"))
draw.text((100, 258), "IGEN VERITAS", fill=(123, 103, 209, 255), font=get_font(68, "bold"))
draw.text((100, 336), "because", fill=(255, 255, 255, 255), font=get_font(68, "bold"))

# Subheadline
sub_lines = [
    "Malaysian SMEs deserve the same",
    "technology as large corporations.",
]
for i, line in enumerate(sub_lines):
    draw.text((100, 440 + i * 52), line, fill=(200, 200, 220, 255), font=get_font(38, "regular"))

# Divider
draw.line([(100, 570), (700, 570)], fill=(123, 103, 209, 120), width=1)

# Quote / mission text
mission = "That gap closes now."
draw.text((100, 600), mission, fill=(123, 103, 209, 255), font=get_font(44, "bold"))

# Value pills row
values = ["Transparent", "Innovative", "Reliable"]
pill_x = 100
for val in values:
    vfont = get_font(20, "regular")
    bb = draw.textbbox((0, 0), val, font=vfont)
    w = bb[2] - bb[0]
    pad = 20
    draw.rounded_rectangle([pill_x, 685, pill_x + w + pad * 2, 720],
                            radius=16, fill=(123, 103, 209, 60), outline=(123, 103, 209, 120))
    draw.text((pill_x + pad + w // 2, 702), val, fill=(255, 255, 255, 230),
              font=vfont, anchor="mm")
    pill_x += w + pad * 2 + 16

# Stats row — glassmorphism cards
stats = [("24/7", "Availability"), ("3x", "Faster Response"), ("RM500", "Starting Setup")]
card_w, card_h = 280, 130
card_y = 770
total_cards = len(stats)
gap = 30
start_x = (1080 - (total_cards * card_w + (total_cards - 1) * gap)) // 2

for i, (num, label) in enumerate(stats):
    cx = start_x + i * (card_w + gap)
    card = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h],
                          radius=16, fill=(255, 255, 255, 18), outline=(255, 255, 255, 35))
    img = Image.alpha_composite(img, card)
    draw = ImageDraw.Draw(img)
    draw.text((cx + card_w // 2, card_y + 42), num,
              fill=(123, 103, 209, 255), font=get_font(38, "bold"), anchor="mm")
    draw.text((cx + card_w // 2, card_y + 90), label,
              fill=(180, 180, 200, 255), font=get_font(18, "regular"), anchor="mm")

# Bottom CTA
draw.text((540, 955), "Ready to close the gap?",
          fill=(255, 255, 255, 200), font=get_font(26, "regular"), anchor="mm")

# CTA pill button
btn_w = 340
draw.rounded_rectangle([540 - btn_w // 2, 990, 540 + btn_w // 2, 1040],
                        radius=24, fill=(123, 103, 209, 255))
draw.text((540, 1015), "DM 'INFO' to get started", fill=(255, 255, 255, 255),
          font=get_font(22, "bold"), anchor="mm")

os.makedirs("social-media", exist_ok=True)
img = img.convert("RGB")
img.save("social-media/20260501_awareness_CB002_linkedin_brand.png", "PNG")
print("Saved: social-media/20260501_awareness_CB002_linkedin_brand.png")
