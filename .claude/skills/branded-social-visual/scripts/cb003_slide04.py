from PIL import Image, ImageDraw, ImageFont
import os, math

W, H = 1080, 1080
output_path = r"c:\Users\jicoo\OneDrive\Documents\Claude\marketing_team\social-media\CB-003_carousel\slide_04.png"

# ── fonts ──────────────────────────────────────────────────────────────────
def font(size, weight="regular"):
    paths = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    p = paths.get(weight, paths["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

# ── helpers ────────────────────────────────────────────────────────────────
def lerp(a, b, t): return int(a + (b - a) * t)

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# ── canvas ─────────────────────────────────────────────────────────────────
img = Image.new("RGBA", (W, H), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# gradient background: #0b0b14 → #1a1535
c1 = hex_to_rgb("#0b0b14")
c2 = hex_to_rgb("#1a1535")
for y in range(H):
    t = y / H
    r, g, b = lerp(c1[0], c2[0], t), lerp(c1[1], c2[1], t), lerp(c1[2], c2[2], t)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# ghosted large circle (matches slides 2–3 style)
ghost = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(ghost)
gd.ellipse([W // 2 - 20, -180, W + 180, H - 200], fill=(123, 103, 209, 18))
img = Image.alpha_composite(img, ghost)
draw = ImageDraw.Draw(img)

# dot grid
DOT_SPACING = 54
DOT_R = 2
DOT_COLOR = (255, 255, 255, 45)
dot_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
dd = ImageDraw.Draw(dot_layer)
for gx in range(DOT_SPACING // 2, W, DOT_SPACING):
    for gy in range(DOT_SPACING // 2, H, DOT_SPACING):
        dd.ellipse([gx - DOT_R, gy - DOT_R, gx + DOT_R, gy + DOT_R], fill=DOT_COLOR)
img = Image.alpha_composite(img, dot_layer)
draw = ImageDraw.Draw(img)

# ── header ─────────────────────────────────────────────────────────────────
VIOLET = "#7B67D1"
VIOLET_RGB = hex_to_rgb(VIOLET)

draw.text((60, 48), "IGEN VERITAS", font=font(22, "bold"), fill=(255, 255, 255, 255))
draw.text((60, 76), "igenveritas.com", font=font(17, "regular"), fill=(180, 170, 220, 180))

# page counter "4 / 4" — muted violet, right-aligned
counter_text = "4 / 4"
ct_font = font(18, "regular")
ct_bbox = draw.textbbox((0, 0), counter_text, font=ct_font)
ct_w = ct_bbox[2] - ct_bbox[0]
draw.text((W - 60 - ct_w, 58), counter_text, font=ct_font, fill=(160, 145, 210, 200))

# thin horizontal rule
rule_y = 118
draw.line([(60, rule_y), (W - 60, rule_y)], fill=(255, 255, 255, 35), width=1)

# ── violet pill label ───────────────────────────────────────────────────────
pill_text = "03 — OUR PROMISE"
pill_font = font(19, "bold")
pill_bbox = draw.textbbox((0, 0), pill_text, font=pill_font)
pill_w = (pill_bbox[2] - pill_bbox[0]) + 36
pill_h = 38
pill_x, pill_y = 60, 148
draw.rounded_rectangle([pill_x, pill_y, pill_x + pill_w, pill_y + pill_h],
                        radius=pill_h // 2, fill=(*VIOLET_RGB, 255))
draw.text((pill_x + 18, pill_y + pill_h // 2), pill_text,
          font=pill_font, fill=(255, 255, 255, 255), anchor="lm")

# ── headline block ──────────────────────────────────────────────────────────
line1_y = 248
draw.text((60, line1_y), "We don't just", font=font(66, "bold"), fill=(180, 175, 210, 160))

draw.text((60, line1_y + 72), "build software.", font=font(72, "bold"), fill=(255, 255, 255, 255))

draw.text((60, line1_y + 72 + 80), "We build results.", font=font(66, "bold"),
          fill=(*VIOLET_RGB, 255))

# thin divider below headline
div_y = line1_y + 72 + 80 + 70
draw.line([(60, div_y), (W - 60, div_y)], fill=(255, 255, 255, 35), width=1)

# ── single CTA card ─────────────────────────────────────────────────────────
CARD_PAD = 60
card_x1 = 60
card_x2 = W - 60
card_y1 = div_y + 32
card_y2 = card_y1 + 230
card_cx = (card_x1 + card_x2) // 2

# white card
card_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
cl = ImageDraw.Draw(card_layer)
cl.rounded_rectangle([card_x1, card_y1, card_x2, card_y2],
                     radius=20, fill=(255, 255, 255, 255))
img = Image.alpha_composite(img, card_layer)
draw = ImageDraw.Draw(img)

# "Ready to automate?" — violet, large, centred
cta_head_font = font(52, "bold")
draw.text((card_cx, card_y1 + 68), "Ready to automate?",
          font=cta_head_font, fill=(*VIOLET_RGB, 255), anchor="mm")

# body lines — dark gray
body_font = font(26, "regular")
DARK_GRAY = (80, 80, 100, 255)
draw.text((card_cx, card_y1 + 134), "5–7 day build. No tech knowledge needed.",
          font=body_font, fill=DARK_GRAY, anchor="mm")
draw.text((card_cx, card_y1 + 170), "Your chatbot goes live — fast.",
          font=body_font, fill=DARK_GRAY, anchor="mm")

# ── bottom CTA button ───────────────────────────────────────────────────────
BTN_Y1 = H - 110
BTN_Y2 = H - 42
BTN_X1 = 60
BTN_X2 = W - 60
btn_cx = (BTN_X1 + BTN_X2) // 2

# violet gradient button
btn_c1 = hex_to_rgb("#8A5DCC")
btn_c2 = hex_to_rgb("#7B67D1")
btn_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bl = ImageDraw.Draw(btn_layer)

# draw gradient by columns
for x in range(BTN_X1, BTN_X2):
    t = (x - BTN_X1) / (BTN_X2 - BTN_X1)
    r = lerp(btn_c1[0], btn_c2[0], t)
    g = lerp(btn_c1[1], btn_c2[1], t)
    b = lerp(btn_c1[2], btn_c2[2], t)
    bl.line([(x, BTN_Y1), (x, BTN_Y2)], fill=(r, g, b, 255))

# mask to rounded rectangle
btn_mask = Image.new("L", (W, H), 0)
bm = ImageDraw.Draw(btn_mask)
bm.rounded_rectangle([BTN_X1, BTN_Y1, BTN_X2, BTN_Y2], radius=34, fill=255)
btn_layer.putalpha(btn_mask)
img = Image.alpha_composite(img, btn_layer)
draw = ImageDraw.Draw(img)

# button text
btn_font = font(32, "bold")
btn_cy = (BTN_Y1 + BTN_Y2) // 2
draw.text((btn_cx, btn_cy), "DM 'INFO' to get started  →",
          font=btn_font, fill=(255, 255, 255, 255), anchor="mm")

# ── save ───────────────────────────────────────────────────────────────────
os.makedirs(os.path.dirname(output_path), exist_ok=True)
img.convert("RGB").save(output_path, "PNG")
print(f"Saved -> {output_path}")
