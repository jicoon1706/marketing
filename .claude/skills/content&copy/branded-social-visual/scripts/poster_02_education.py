"""Poster 2 — Template B (Education) | Tue Apr 29 | Bot Ini Belajar Dari Bisnes Kau"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "social-media/20260429_education_bot-train-sources.png"
os.makedirs("social-media", exist_ok=True)

W, H = 1080, 1080
img = Image.new("RGBA", (W, H), (123, 103, 209, 255))
draw = ImageDraw.Draw(img)

# --- Diagonal gradient: #7B67D1 → #4196E6 ---
for y in range(H):
    for x in range(0, W, 4):
        t = (x + y) / (W + H)
        r = int(123 + (65 - 123) * t)
        g = int(103 + (150 - 103) * t)
        b = int(209 + (230 - 209) * t)
        draw.line([(x, y), (min(x + 3, W - 1), y)], fill=(r, g, b, 255))

def font(size, weight="regular"):
    m = {"bold": "C:/Windows/Fonts/segoeuib.ttf",
         "regular": "C:/Windows/Fonts/segoeui.ttf",
         "light": "C:/Windows/Fonts/segoeuil.ttf"}
    p = m.get(weight, m["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

# --- Brand label ---
draw.text((60, 58), "IGEN VERITAS", fill=(255, 255, 255, 200), font=font(22, "bold"))
draw.text((60, 86), "igen-veritas.com", fill=(255, 255, 255, 130), font=font(18))

# --- Headline ---
draw.text((540, 185), "Bot Ini Belajar", fill=(255, 255, 255, 255), font=font(82, "bold"), anchor="mm")
draw.text((540, 280), "Dari Bisnes", fill=(255, 255, 255, 255), font=font(82, "bold"), anchor="mm")
draw.text((540, 375), "Kau.", fill=(11, 11, 20, 255), font=font(82, "bold"), anchor="mm")

# --- Central AI bot icon (geometric) ---
cx, cy = 540, 590
# Body circle
draw.ellipse([cx-90, cy-90, cx+90, cy+90], fill=(255, 255, 255, 230))
# Eyes
draw.ellipse([cx-30, cy-25, cx-10, cy-5], fill=(123, 103, 209, 255))
draw.ellipse([cx+10, cy-25, cx+30, cy-5], fill=(123, 103, 209, 255))
# Eye glow dots
draw.ellipse([cx-24, cy-21, cx-16, cy-13], fill=(255, 255, 255, 255))
draw.ellipse([cx+16, cy-21, cx+24, cy-13], fill=(255, 255, 255, 255))
# Mouth smile arc (approximated with rounded rect)
draw.rounded_rectangle([cx-22, cy+12, cx+22, cy+28], radius=8, fill=(123, 103, 209, 200))
# Antenna
draw.line([(cx, cy-90), (cx, cy-115)], fill=(255, 255, 255, 200), width=4)
draw.ellipse([cx-8, cy-128, cx+8, cy-112], fill=(65, 150, 230, 255))
# WhatsApp green dot accent
draw.ellipse([cx+62, cy+50, cx+82, cy+70], fill=(37, 211, 102, 255))

# --- 4 knowledge source pills arranged around the bot ---
pills = [
    (220, 460, "🌐", "Website"),
    (720, 460, "📄", "PDF"),
    (220, 700, "❓", "FAQ"),
    (720, 700, "📱", "WhatsApp"),
]

for px, py, icon, label in pills:
    pw, ph = 220, 72
    # Shadow
    draw.rounded_rectangle([px - 2, py + 4, px + pw + 2, py + ph + 4],
        radius=16, fill=(0, 0, 0, 40))
    # White card
    draw.rounded_rectangle([px, py, px + pw, py + ph], radius=16, fill=(255, 255, 255, 240))
    draw.text((px + 30, py + ph // 2), icon, fill=(0, 0, 0, 255),
        font=font(28), anchor="lm")
    draw.text((px + 68, py + ph // 2), label, fill=(11, 11, 20, 220),
        font=font(24, "bold"), anchor="lm")

# --- Connector lines from pills to bot ---
line_color = (255, 255, 255, 60)
draw.line([(330, 496), (cx - 80, cy - 60)], fill=line_color, width=2)
draw.line([(730, 496), (cx + 80, cy - 60)], fill=line_color, width=2)
draw.line([(330, 736), (cx - 80, cy + 60)], fill=line_color, width=2)
draw.line([(730, 736), (cx + 80, cy + 60)], fill=line_color, width=2)

# --- Subtext ---
draw.text((540, 830), "AI yang faham bisnes kau — train dalam minit.",
    fill=(255, 255, 255, 200), font=font(26), anchor="mm")

# --- CTA pill ---
draw.rounded_rectangle([340, 890, 740, 954], radius=32, fill=(11, 11, 20, 200))
draw.text((540, 922), "DM 'INFO' sekarang  →", fill=(255, 255, 255, 255), font=font(28, "bold"), anchor="mm")

# --- Bottom strip ---
draw.line([(60, 980), (1020, 980)], fill=(255, 255, 255, 40), width=1)
draw.text((540, 1010), "IGEN VERITAS  |  AI Automation for Malaysian SMEs  |  igen-veritas.com",
    fill=(255, 255, 255, 140), font=font(17), anchor="mm")

img.save(OUT, "PNG")
print(f"Saved: {OUT}")
