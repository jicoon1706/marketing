"""Poster 4 — Template B-variant (Flow/Education) | Fri May 2 | Lead Masuk, Sheet Update Sendiri"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "social-media/20260502_education_lead-auto-google-sheets.png"
os.makedirs("social-media", exist_ok=True)

W, H = 1080, 1080
img = Image.new("RGBA", (W, H), (123, 103, 209, 255))
draw = ImageDraw.Draw(img)

# --- Gradient #7B67D1 → #488FE3 (vertical) ---
for y in range(H):
    t = y / H
    r = int(123 + (72 - 123) * t)
    g = int(103 + (143 - 103) * t)
    b = int(209 + (227 - 209) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

def font(size, weight="regular"):
    m = {"bold": "C:/Windows/Fonts/segoeuib.ttf",
         "regular": "C:/Windows/Fonts/segoeui.ttf",
         "light": "C:/Windows/Fonts/segoeuil.ttf"}
    p = m.get(weight, m["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

# --- Brand label ---
draw.text((60, 58), "IGEN VERITAS", fill=(255, 255, 255, 200), font=font(22, "bold"))
draw.text((60, 86), "igenveritas.com", fill=(255, 255, 255, 130), font=font(18))

# --- Headline ---
draw.text((540, 178), "Lead Masuk,", fill=(255, 255, 255, 255), font=font(82, "bold"), anchor="mm")
draw.text((540, 278), "Sheet Update", fill=(11, 11, 20, 230), font=font(82, "bold"), anchor="mm")
draw.text((540, 368), "Sendiri.", fill=(255, 255, 255, 255), font=font(82, "bold"), anchor="mm")

# ============================================================
# Flow diagram: 4 nodes connected by arrows
# ============================================================
nodes = [
    {"emoji": "💬", "label": "WhatsApp\nLead", "color": (37, 211, 102, 230)},
    {"emoji": "🤖", "label": "Botpress\nQualify", "color": (123, 103, 209, 230)},
    {"emoji": "⚡", "label": "n8n\nWebhook", "color": (245, 158, 11, 230)},
    {"emoji": "📊", "label": "Google\nSheets", "color": (52, 168, 83, 230)},
]

node_w, node_h = 180, 160
gap = 40
total_w = len(nodes) * node_w + (len(nodes) - 1) * gap
start_x = (W - total_w) // 2
node_y = 450

for i, node in enumerate(nodes):
    nx = start_x + i * (node_w + gap)
    ny = node_y
    # Shadow
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([nx + 4, ny + 4, nx + node_w + 4, ny + node_h + 4], radius=22, fill=(0, 0, 0, 50))
    img = Image.alpha_composite(img, shadow)
    draw = ImageDraw.Draw(img)
    # Node card
    draw.rounded_rectangle([nx, ny, nx + node_w, ny + node_h], radius=22, fill=node["color"])
    # Emoji
    draw.text((nx + node_w // 2, ny + 48), node["emoji"], fill=(255, 255, 255, 255),
        font=font(38), anchor="mm")
    # Label
    for j, line in enumerate(node["label"].split("\n")):
        draw.text((nx + node_w // 2, ny + 98 + j * 28), line,
            fill=(255, 255, 255, 240), font=font(20, "bold"), anchor="mm")
    # Arrow to next node
    if i < len(nodes) - 1:
        ax = nx + node_w + 6
        ay = ny + node_h // 2
        draw.line([(ax, ay), (ax + gap - 12, ay)], fill=(255, 255, 255, 180), width=3)
        # Arrowhead
        draw.polygon([(ax + gap - 12, ay - 8), (ax + gap - 12, ay + 8),
                       (ax + gap, ay)], fill=(255, 255, 255, 180))

# --- Automation label below diagram ---
draw.text((540, 640), "Automatik. 24/7. Tanpa sentuh apa-apa.",
    fill=(255, 255, 255, 230), font=font(30, "bold"), anchor="mm")

# --- n8n + Botpress stack pill ---
draw.rounded_rectangle([250, 690, 830, 740], radius=20, fill=(255, 255, 255, 20))
draw.text((540, 715), "Powered by  Botpress  +  n8n  +  Google Sheets",
    fill=(255, 255, 255, 200), font=font(22), anchor="mm")

# --- Feature list cards ---
features = [
    "✓  Lead captured instantly",
    "✓  Name, phone & intent logged",
    "✓  Follow-up triggered auto",
    "✓  Zero manual data entry",
]
fy = 770
for feat in features:
    fx1, fy1, fx2, fy2 = 130, fy, 950, fy + 44
    draw.rounded_rectangle([fx1, fy1, fx2, fy2], radius=12, fill=(255, 255, 255, 15))
    draw.text((fx1 + 24, (fy1 + fy2) // 2), feat, fill=(255, 255, 255, 220), font=font(22), anchor="lm")
    fy += 52

# --- CTA ---
draw.rounded_rectangle([330, 995, 750, 1045], radius=26, fill=(11, 11, 20, 200))
draw.text((540, 1020), "DM 'INFO' sekarang  →", fill=(255, 255, 255, 255), font=font(26, "bold"), anchor="mm")

img.save(OUT, "PNG")
print(f"Saved: {OUT}")
