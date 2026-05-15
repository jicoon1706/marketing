"""CB-026 — Template A (Pain Point) | Jun 1 | Leads Cool Down. Fast."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "social-media/CB-026_pain.png"
os.makedirs("social-media", exist_ok=True)

W, H = 1080, 1080
img = Image.new("RGBA", (W, H), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# --- Background: dark navy with violet radial glow (center-left) ---
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for r in range(440, 0, -1):
    alpha = int(60 * (1 - r / 440) ** 1.5)
    gd.ellipse([280 - r, 500 - r, 280 + r, 500 + r], fill=(123, 103, 209, alpha))
img = Image.alpha_composite(img, glow)
draw = ImageDraw.Draw(img)

# subtle top-right blue secondary glow
glow2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd2 = ImageDraw.Draw(glow2)
for r in range(260, 0, -1):
    alpha = int(22 * (1 - r / 260) ** 2)
    gd2.ellipse([W - 240 - r, 220 - r, W - 240 + r, 220 + r], fill=(65, 150, 230, alpha))
img = Image.alpha_composite(img, glow2)
draw = ImageDraw.Draw(img)

def font(size, weight="regular"):
    m = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    p = m.get(weight, m["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

# --- Brand label top-left ---
draw.text((60, 58),  "IGEN VERITAS",  fill=(255, 255, 255, 180), font=font(22, "bold"))
draw.text((60, 86),  "igenveritas.com", fill=(107, 114, 128, 255), font=font(18))

# --- Main headline ---
f_xl = font(104, "bold")

# Line 1: "Leads Cool Down." — white
draw.text((540, 290), "Leads Cool Down.", fill=(255, 255, 255, 255), font=f_xl, anchor="mm")
# Line 2: "Fast." — violet accent
draw.text((540, 405), "Fast.", fill=(123, 103, 209, 255), font=f_xl, anchor="mm")

# --- Glassmorphism stat card ---
card = Image.new("RGBA", (W, H), (0, 0, 0, 0))
cd = ImageDraw.Draw(card)
cd.rounded_rectangle([170, 480, 910, 730], radius=28,
    fill=(255, 255, 255, 13), outline=(255, 255, 255, 30))
img = Image.alpha_composite(img, card)
draw = ImageDraw.Draw(img)

# Time pill — 2:17 AM
draw.rounded_rectangle([200, 508, 410, 560], radius=14,
    fill=(255, 255, 255, 20), outline=(255, 255, 255, 40))
draw.text((305, 534), "2:17 AM", fill=(255, 255, 255, 220), font=font(27, "bold"), anchor="mm")

# Red "0 Replies" badge
draw.rounded_rectangle([435, 508, 680, 560], radius=14, fill=(220, 38, 38, 210))
draw.text((557, 534), "0 Replies", fill=(255, 255, 255, 255), font=font(25, "bold"), anchor="mm")

# Unread chat icon indicator
draw.ellipse([700, 510, 730, 540], fill=(123, 103, 209, 255))
draw.text((715, 525), "4", fill=(255, 255, 255, 255), font=font(18, "bold"), anchor="mm")
draw.text((745, 525), "unread", fill=(107, 114, 128, 200), font=font(20), anchor="lm")

# 4 unanswered message rows
messages = [
    ("Boleh tolong saya tak?",              "2:03 AM"),
    ("Hi, nak tanya pasal servis you...",   "2:09 AM"),
    ("Hello? Anyone there?",                "2:11 AM"),
    ("Ok I'll find someone else.",          "2:17 AM"),
]
msg_bg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
mb = ImageDraw.Draw(msg_bg)
mb.rounded_rectangle([200, 575, 880, 715], radius=18,
    fill=(255, 255, 255, 8), outline=(255, 255, 255, 16))
img = Image.alpha_composite(img, msg_bg)
draw = ImageDraw.Draw(img)

for i, (msg, t) in enumerate(messages):
    y = 597 + i * 32
    # last message in red — the "I'll find someone else"
    msg_color = (220, 100, 100, 230) if i == 3 else (200, 200, 220, 190)
    draw.text((225, y), f"💬  {msg}", fill=msg_color, font=font(19))
    draw.text((860, y), t,           fill=(107, 114, 128, 180), font=font(17), anchor="ra")

# --- Subtext ---
draw.text((540, 775),
    "Every hour without a reply is a customer choosing someone else.",
    fill=(107, 114, 128, 255), font=font(25), anchor="mm")

# --- CTA pill button ---
draw.rounded_rectangle([330, 835, 750, 900], radius=32, fill=(123, 103, 209, 255))
draw.text((540, 867), "DM 'INFO' sekarang  →",
    fill=(255, 255, 255, 255), font=font(28, "bold"), anchor="mm")

# --- Bottom brand strip ---
draw.line([(60, 948), (1020, 948)], fill=(255, 255, 255, 22), width=1)
draw.text((540, 982),
    "IGEN VERITAS  |  AI Automation for Malaysian SMEs  |  igenveritas.com",
    fill=(107, 114, 128, 190), font=font(17), anchor="mm")

img.save(OUT, "PNG")
print(f"Saved: {OUT}")
