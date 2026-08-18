from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

FONT_DIR = r"C:\Users\jicoo\.claude\plugins\cache\anthropic-agent-skills\document-skills\f458cee31a75\skills\canvas-design\canvas-fonts"
OUT = r"c:\Users\jicoo\OneDrive\IGEN VERITAS TECHNOLOGIES\marketing_team\social-media\CB-031_urgency.png"

VIOLET  = (123, 103, 209)
PURPLE  = (138, 93, 204)
BLUE    = (72, 143, 227)
WHITE   = (255, 255, 255)
MUTED   = (210, 205, 240)
SUBTLE  = (160, 155, 200)
DARK    = (11, 11, 20)

W, H = 1080, 1080
MARGIN = 80


def load(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def tw(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0]


def th(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[3] - bb[1]


def centered(draw, text, y, font, color):
    w = tw(draw, text, font)
    draw.text(((W - w) // 2, y), text, font=font, fill=color)


def make_dark_base():
    arr = np.full((H, W, 3), [11, 11, 20], dtype=np.uint8)
    return Image.fromarray(arr, "RGB")


def add_radial_glow(img, cx, cy, color, radius=420, alpha_peak=35):
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    steps = 6
    for i in range(steps, 0, -1):
        r = int(radius * i / steps)
        a = int(alpha_peak * (1 - i / (steps + 1)))
        gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, a))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=80))
    base = img.convert("RGBA")
    return Image.alpha_composite(base, glow).convert("RGB")


def add_noise(img, strength=5):
    arr = np.array(img, dtype=np.int16)
    noise = np.random.randint(-strength, strength + 1, arr.shape, dtype=np.int16)
    return Image.fromarray(np.clip(arr + noise, 0, 255).astype(np.uint8), "RGB")


# ── canvas ───────────────────────────────────────────────────────────────────
np.random.seed(31)
img = make_dark_base()
img = add_radial_glow(img, W // 2, 340, VIOLET[:3], radius=480, alpha_peak=42)
img = add_radial_glow(img, W - 100, H - 100, PURPLE[:3], radius=260, alpha_peak=20)
img = add_noise(img)
draw = ImageDraw.Draw(img)

# fonts
f_hl    = load("BigShoulders-Bold.ttf", 108)
f_sub   = load("InstrumentSans-Regular.ttf", 26)
f_label = load("DMMono-Regular.ttf", 15)
f_step  = load("Outfit-Bold.ttf", 13)
f_title = load("Outfit-Bold.ttf", 22)
f_desc  = load("InstrumentSans-Regular.ttf", 19)
f_cta   = load("BigShoulders-Bold.ttf", 38)
f_mono  = load("DMMono-Regular.ttf", 15)

# ── top label ────────────────────────────────────────────────────────────────
label = "AI CHATBOT  ·  IGENVERITAS.COM"
lw = tw(draw, label, f_label)
draw.text(((W - lw) // 2, 52), label, font=f_label, fill=(*SUBTLE, 160))
draw.line([(MARGIN, 82), (W - MARGIN, 82)], fill=(*WHITE, 18), width=1)

# ── headline ─────────────────────────────────────────────────────────────────
hl_y = 114
centered(draw, "LIVE IN", hl_y, f_hl, WHITE)
hl_y += th(draw, "A", f_hl) + 0
centered(draw, "5–7 DAYS.", hl_y, f_hl, VIOLET)
hl_y += th(draw, "A", f_hl) + 18

# ── subline ───────────────────────────────────────────────────────────────────
sub = "Setup starts the moment you DM us."
centered(draw, sub, hl_y, f_sub, MUTED)
hl_y += th(draw, sub, f_sub) + 44

# ── divider ───────────────────────────────────────────────────────────────────
draw.line([(MARGIN + 40, hl_y), (W - MARGIN - 40, hl_y)], fill=(*WHITE, 22), width=1)
hl_y += 44

# ── 4-step timeline ───────────────────────────────────────────────────────────
steps = [
    ("01", "YOU DM US",       "Tell us your business and goals."),
    ("02", "WE BUILD",        "Custom chatbot configured in 2–3 days."),
    ("03", "YOU REVIEW",      "Test it, approve it, request tweaks."),
    ("04", "GO LIVE",         "Embedded on your website. Done."),
]

# layout: 2 columns x 2 rows
col_w = (W - MARGIN * 2 - 40) // 2
row_h = 140
cols = [MARGIN, MARGIN + col_w + 40]
rows = [hl_y, hl_y + row_h + 24]

for i, (num, title, desc) in enumerate(steps):
    col = i % 2
    row = i // 2
    x = cols[col]
    y = rows[row]

    # step number chip
    chip_w = 42
    chip_h = 22
    draw.rounded_rectangle([x, y, x + chip_w, y + chip_h], radius=4,
                            fill=(*VIOLET, 60))
    num_w = tw(draw, num, f_step)
    draw.text((x + (chip_w - num_w) // 2, y + 3), num, font=f_step,
              fill=(*WHITE, 220))

    y_t = y + chip_h + 10
    draw.text((x, y_t), title, font=f_title, fill=WHITE)
    y_t += th(draw, title, f_title) + 6
    draw.text((x, y_t), desc, font=f_desc, fill=MUTED)

hl_y = rows[1] + row_h + 44

# ── divider ───────────────────────────────────────────────────────────────────
draw.line([(MARGIN + 40, hl_y), (W - MARGIN - 40, hl_y)], fill=(*WHITE, 22), width=1)
hl_y += 40

# ── CTA block ────────────────────────────────────────────────────────────────
cta_text = "DM 'BOT' TO START"
cta_w = tw(draw, cta_text, f_cta)
cta_x = (W - cta_w) // 2
cta_y = hl_y

# pill background
pad_x, pad_y = 36, 14
pill_x0 = cta_x - pad_x
pill_y0 = cta_y - pad_y
pill_x1 = cta_x + cta_w + pad_x
pill_y1 = cta_y + th(draw, cta_text, f_cta) + pad_y
draw.rounded_rectangle([pill_x0, pill_y0, pill_x1, pill_y1],
                        radius=8, fill=(*VIOLET, 200))
draw.text((cta_x, cta_y), cta_text, font=f_cta, fill=WHITE)

hl_y = pill_y1 + 18

# pricing note
note = "Packages from RM 500  ·  Setup in under a week"
nw = tw(draw, note, f_label)
draw.text(((W - nw) // 2, hl_y), note, font=f_label, fill=(*SUBTLE, 140))

# ── bottom rule & brand footer ────────────────────────────────────────────────
bottom_rule_y = H - 76
draw.line([(MARGIN, bottom_rule_y), (W - MARGIN, bottom_rule_y)],
          fill=(*WHITE, 22), width=1)

brand_y = H - 52
draw.text((MARGIN, brand_y), "IGEN VERITAS", font=f_mono, fill=MUTED)
site = "igen-veritas.com"
draw.text((W - MARGIN - tw(draw, site, f_mono), brand_y), site,
          font=f_mono, fill=MUTED)

img.save(OUT, "PNG", dpi=(300, 300))
print(f"Saved: {OUT}")
