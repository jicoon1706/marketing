from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

FONT_DIR = r"C:\Users\jicoo\.claude\plugins\cache\anthropic-agent-skills\document-skills\f458cee31a75\skills\canvas-design\canvas-fonts"
OUT = r"c:\Users\jicoo\OneDrive\IGEN VERITAS TECHNOLOGIES\marketing_team\social-media\CB-030_brand.png"

VIOLET  = (123, 103, 209)
PURPLE  = (138, 93, 204)
BLUE    = (72, 143, 227)
WHITE   = (255, 255, 255)
MUTED   = (210, 205, 240)
SUBTLE  = (160, 155, 200)
DARK    = (11, 11, 20)       # #0b0b14

W, H = 1080, 1080
MARGIN = 80
USABLE_W = W - MARGIN * 2


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


def add_noise(img, strength=6):
    arr = np.array(img, dtype=np.int16)
    noise = np.random.randint(-strength, strength + 1, arr.shape, dtype=np.int16)
    return Image.fromarray(np.clip(arr + noise, 0, 255).astype(np.uint8), "RGB")


# ── canvas ──────────────────────────────────────────────────────────────────
np.random.seed(30)
img = make_dark_base()
img = add_radial_glow(img, W // 2, H // 2 - 80, VIOLET[:3], radius=500, alpha_peak=40)
img = add_radial_glow(img, W // 2 - 160, H - 200, BLUE[:3], radius=280, alpha_peak=18)
img = add_noise(img)
draw = ImageDraw.Draw(img)

# fonts
f_hl     = load("BigShoulders-Bold.ttf", 96)
f_sub    = load("InstrumentSans-Regular.ttf", 28)
f_label  = load("Outfit-Bold.ttf", 16)
f_pillar = load("Outfit-Bold.ttf", 22)
f_body   = load("InstrumentSans-Regular.ttf", 22)
f_mono   = load("DMMono-Regular.ttf", 15)
f_name   = load("BigShoulders-Bold.ttf", 32)

# ── top label ─────────────────────────────────────────────────────────────────
label = "BEHIND THE BRAND  ·  IGENVERITAS.COM"
lw = tw(draw, label, f_mono)
draw.text(((W - lw) // 2, 52), label, font=f_mono, fill=(*SUBTLE, 160))
draw.line([(MARGIN, 84), (W - MARGIN, 84)], fill=(*WHITE, 18), width=1)

# ── headline ─────────────────────────────────────────────────────────────────
hl_y = 116
centered(draw, "THIS IS WHAT", hl_y, f_hl, WHITE)
hl_y += th(draw, "A", f_hl) + 4
centered(draw, "WE BUILD.", hl_y, f_hl, VIOLET)
hl_y += th(draw, "A", f_hl) + 24

# ── subline ───────────────────────────────────────────────────────────────────
sub = "And why we built it this way."
centered(draw, sub, hl_y, f_sub, MUTED)
hl_y += th(draw, sub, f_sub) + 44

# ── thin rule ─────────────────────────────────────────────────────────────────
draw.line([(MARGIN + 40, hl_y), (W - MARGIN - 40, hl_y)], fill=(*WHITE, 25), width=1)
hl_y += 36

# ── three service pillars ─────────────────────────────────────────────────────
pillars = [
    ("01", "AI CHATBOTS", "Capture & qualify leads 24/7 — no staff required."),
    ("02", "WEBSITES",    "Built to convert, not just look good."),
    ("03", "MOBILE APPS", "Put your business in your customer's pocket."),
]

f_num = load("DMMono-Regular.ttf", 14)

for num, title, desc in pillars:
    # number badge
    num_x = MARGIN
    draw.text((num_x, hl_y + 4), num, font=f_num, fill=(*VIOLET, 160))

    # title
    title_x = MARGIN + 44
    draw.text((title_x, hl_y), title, font=f_pillar, fill=WHITE)
    hl_y += th(draw, title, f_pillar) + 6

    # desc
    draw.text((title_x, hl_y), desc, font=f_body, fill=MUTED)
    hl_y += th(draw, desc, f_body) + 28

hl_y += 8

# ── thin rule ─────────────────────────────────────────────────────────────────
draw.line([(MARGIN + 40, hl_y), (W - MARGIN - 40, hl_y)], fill=(*WHITE, 25), width=1)
hl_y += 36

# ── IGEN / VERITAS meaning block ──────────────────────────────────────────────
def name_row(label_text, meaning, y):
    f_lbl_b = load("BigShoulders-Bold.ttf", 28)
    f_mean  = load("InstrumentSans-Regular.ttf", 20)
    draw.text((MARGIN, y), label_text, font=f_lbl_b, fill=VIOLET)
    lw_label = tw(draw, label_text, f_lbl_b)
    draw.text((MARGIN + lw_label + 16, y + 5), meaning, font=f_mean, fill=MUTED)
    return y + th(draw, label_text, f_lbl_b) + 10

hl_y = name_row("IGEN", "— new generation spirit. Curious. Adaptive. Always pushing.", hl_y)
hl_y = name_row("VERITAS", "— Latin for truth. We build what we say. No shortcuts.", hl_y)

# ── bottom rule & brand footer ────────────────────────────────────────────────
bottom_rule_y = H - 76
draw.line([(MARGIN, bottom_rule_y), (W - MARGIN, bottom_rule_y)], fill=(*WHITE, 22), width=1)

brand_y = H - 52
draw.text((MARGIN, brand_y), "IGEN VERITAS", font=f_mono, fill=MUTED)
site = "igen-veritas.com"
draw.text((W - MARGIN - tw(draw, site, f_mono), brand_y), site, font=f_mono, fill=MUTED)

img.save(OUT, "PNG", dpi=(300, 300))
print(f"Saved: {OUT}")
