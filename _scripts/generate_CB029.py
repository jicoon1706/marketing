from PIL import Image, ImageDraw, ImageFont
import numpy as np

FONT_DIR = r"C:\Users\jicoo\.claude\plugins\cache\anthropic-agent-skills\document-skills\f458cee31a75\skills\canvas-design\canvas-fonts"
OUT = r"c:\Users\jicoo\OneDrive\IGEN VERITAS TECHNOLOGIES\marketing_team\social-media\CB-029_cta.png"

VIOLET  = (123, 103, 209)
PURPLE  = (138, 93, 204)
WHITE   = (255, 255, 255)
MUTED   = (220, 215, 245)
DARK    = (30, 22, 60)

W, H = 1080, 1080
MARGIN = 72
USABLE_W = W - MARGIN * 2


def load(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def text_w(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0]


def text_h(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[3] - bb[1]


def fit_font(path, text, max_w, start=220, min_s=40):
    dummy = Image.new("RGB", (1, 1))
    d = ImageDraw.Draw(dummy)
    s = start
    while s > min_s:
        f = ImageFont.truetype(path, s)
        bb = d.textbbox((0, 0), text, font=f)
        if bb[2] - bb[0] <= max_w:
            return f, s
        s -= 2
    return ImageFont.truetype(path, min_s), min_s


def draw_centered(draw, text, y, font, color):
    w = text_w(draw, text, font)
    draw.text(((W - w) // 2, y), text, font=font, fill=color)


def make_gradient():
    # Top: deep violet-purple. Bottom: slightly darker purple with blue tint.
    top    = np.array([100, 78, 180], dtype=np.float32)
    bottom = np.array([60,  40, 130], dtype=np.float32)
    arr = np.zeros((H, W, 3), dtype=np.uint8)
    for row in range(H):
        t = row / (H - 1)
        color = (top * (1 - t) + bottom * t).astype(np.uint8)
        arr[row, :] = color
    return Image.fromarray(arr, "RGB")


def add_noise_texture(img, strength=8):
    arr = np.array(img, dtype=np.int16)
    noise = np.random.randint(-strength, strength + 1, arr.shape, dtype=np.int16)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGB")


def add_radial_glow(img):
    from PIL import ImageFilter
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy = W // 2, H // 2 - 60
    layers = [
        (800, 500, 25),
        (600, 380, 18),
        (400, 260, 12),
        (220, 150, 7),
    ]
    for ew, eh, alpha in layers:
        gd.ellipse(
            [cx - ew // 2, cy - eh // 2, cx + ew // 2, cy + eh // 2],
            fill=(180, 160, 255, alpha),
        )
    glow = glow.filter(ImageFilter.GaussianBlur(radius=60))
    base = img.convert("RGBA")
    return Image.alpha_composite(base, glow).convert("RGB")


# ── canvas ──────────────────────────────────────────────────────────────────
np.random.seed(29)
img = make_gradient()
img = add_noise_texture(img)
img = add_radial_glow(img)
draw = ImageDraw.Draw(img)

# fonts
headline_path = f"{FONT_DIR}/BigShoulders-Bold.ttf"
f_sub   = load("InstrumentSans-Regular.ttf", 30)
f_sub_b = load("InstrumentSans-SemiBold.ttf", 30) if False else load("InstrumentSans-Regular.ttf", 30)
f_label = load("Outfit-Bold.ttf", 18)
f_cta   = load("Outfit-Bold.ttf", 24)
f_mono  = load("DMMono-Regular.ttf", 15)

# fit headline to widest line
widest = "JUNE STARTS IN"
f_hl, hl_size = fit_font(headline_path, widest, USABLE_W - 10)

# ── top label ────────────────────────────────────────────────────────────────
label_text = "AI CHATBOT  ·  MALAYSIAN SMES  ·  IGENVERITAS.COM"
lw = text_w(draw, label_text, f_mono)
draw.text(((W - lw) // 2, 52), label_text, font=f_mono, fill=(220, 215, 245, 140))

draw.line([(MARGIN, 84), (W - MARGIN, 84)], fill=(255, 255, 255, 40), width=1)

# ── countdown tag ─────────────────────────────────────────────────────────────
tag_text = "▶  3 DAYS LEFT"
tw = text_w(draw, tag_text, f_label)
th = text_h(draw, tag_text, f_label)
pad_x, pad_y = 20, 9
tag_w = tw + pad_x * 2
tag_h = th + pad_y * 2
tag_x = (W - tag_w) // 2
tag_y = 116
draw.rounded_rectangle(
    [tag_x, tag_y, tag_x + tag_w, tag_y + tag_h],
    radius=tag_h // 2,
    fill=(255, 255, 255, 30),
)
draw.text((tag_x + pad_x, tag_y + pad_y), tag_text, font=f_label, fill=WHITE)

# ── headline block ─────────────────────────────────────────────────────────────
hl_line_h = text_h(draw, "A", f_hl)
hl_gap = 4

lines = ["JUNE STARTS", "IN 3 DAYS."]

total_hl_h = len(lines) * hl_line_h + (len(lines) - 1) * hl_gap
y = tag_y + tag_h + 44

for line in lines:
    draw_centered(draw, line, y, f_hl, WHITE)
    y += hl_line_h + hl_gap

y += 28

# ── thin rule ─────────────────────────────────────────────────────────────────
draw.line([(MARGIN + 60, y), (W - MARGIN - 60, y)], fill=(255, 255, 255, 50), width=1)
y += 32

# ── subtext ───────────────────────────────────────────────────────────────────
sub1 = "Your chatbot could already be live."
sw = text_w(draw, sub1, f_sub)
draw.text(((W - sw) // 2, y), sub1, font=f_sub, fill=MUTED)
y += text_h(draw, sub1, f_sub) + 16

sub2 = "Setup takes 5–7 days. Start today."
f_sub2 = load("InstrumentSans-Regular.ttf", 22)
sw2 = text_w(draw, sub2, f_sub2)
draw.text(((W - sw2) // 2, y), sub2, font=f_sub2, fill=(200, 195, 235))
y += text_h(draw, sub2, f_sub2) + 52

# ── CTA pill ─────────────────────────────────────────────────────────────────
cta_text = "DM 'BOT' — start today"
cta_tw   = text_w(draw, cta_text, f_cta)
cta_th   = text_h(draw, cta_text, f_cta)
pad_cx, pad_cy = 44, 16
pill_w   = cta_tw + pad_cx * 2
pill_h   = cta_th + pad_cy * 2
pill_x   = (W - pill_w) // 2
draw.rounded_rectangle(
    [pill_x, y, pill_x + pill_w, y + pill_h],
    radius=pill_h // 2,
    fill=WHITE,
)
draw.text((pill_x + pad_cx, y + pad_cy), cta_text, font=f_cta, fill=DARK)
y += pill_h + 18

# ── price note ───────────────────────────────────────────────────────────────
price_text = "Packages from RM 500"
f_price = load("DMMono-Regular.ttf", 17)
pw = text_w(draw, price_text, f_price)
draw.text(((W - pw) // 2, y), price_text, font=f_price, fill=(200, 195, 235))

# ── bottom rule & brand ───────────────────────────────────────────────────────
bottom_rule_y = H - 76
draw.line([(MARGIN, bottom_rule_y), (W - MARGIN, bottom_rule_y)], fill=(255, 255, 255, 35), width=1)

brand_y = H - 52
draw.text((MARGIN, brand_y), "IGEN VERITAS", font=f_mono, fill=MUTED)
site = "igen-veritas.com"
draw.text((W - MARGIN - text_w(draw, site, f_mono), brand_y), site, font=f_mono, fill=MUTED)

img.save(OUT, "PNG", dpi=(300, 300))
print(f"Saved: {OUT}")
