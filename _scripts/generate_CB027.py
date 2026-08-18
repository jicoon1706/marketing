from PIL import Image, ImageDraw, ImageFont

FONT_DIR = r"C:\Users\jicoo\.claude\plugins\cache\anthropic-agent-skills\document-skills\f458cee31a75\skills\canvas-design\canvas-fonts"
OUT = r"c:\Users\jicoo\OneDrive\IGEN VERITAS TECHNOLOGIES\marketing_team\social-media\CB-027_pain.png"

BG      = (11, 11, 20)
WHITE   = (255, 255, 255)
VIOLET  = (123, 103, 209)
GRAY    = (107, 114, 128)
MUTED   = (180, 180, 195)

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


def add_glow(img):
    from PIL import ImageFilter
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy = W // 2, 460
    layers = [
        (700, 420, 14),
        (560, 340, 11),
        (420, 260, 8),
        (280, 180, 5),
        (140, 100, 3),
    ]
    for ew, eh, alpha in layers:
        gd.ellipse(
            [cx - ew // 2, cy - eh // 2, cx + ew // 2, cy + eh // 2],
            fill=(123, 103, 209, alpha),
        )
    glow = glow.filter(ImageFilter.GaussianBlur(radius=40))
    base = img.convert("RGBA")
    return Image.alpha_composite(base, glow).convert("RGB")


# ── canvas ──────────────────────────────────────────────────────────────────
img = Image.new("RGB", (W, H), BG)
img = add_glow(img)
draw = ImageDraw.Draw(img)

# fonts
headline_path = f"{FONT_DIR}/BigShoulders-Bold.ttf"

# fit to widest line
widest = max(["YOUR ADS ARE", "WORKING.", "YOUR WEBSITE", "ISN'T."], key=len)
f_hl, hl_size = fit_font(headline_path, widest, USABLE_W - 20)

f_sub  = load("InstrumentSans-Regular.ttf", 27)
f_cta  = load("Outfit-Bold.ttf", 22)
f_mono = load("DMMono-Regular.ttf", 15)

# ── top rule ─────────────────────────────────────────────────────────────────
draw.line([(MARGIN, 68), (W - MARGIN, 68)], fill=(*VIOLET, 90), width=1)

# ── headline block ────────────────────────────────────────────────────────────
hl_line_h = text_h(draw, "A", f_hl)
hl_gap    = 6
separator_gap = 18  # extra gap around the divider line

lines_white  = ["YOUR ADS ARE", "WORKING."]
lines_violet = ["YOUR WEBSITE", "ISN'T."]

total_block_h = (
    len(lines_white) * hl_line_h
    + (len(lines_white) - 1) * hl_gap
    + separator_gap * 2 + 1      # divider line
    + len(lines_violet) * hl_line_h
    + (len(lines_violet) - 1) * hl_gap
)

# vertically center block, biased upward
y = (H - total_block_h) // 2 - 40

for line in lines_white:
    draw_centered(draw, line, y, f_hl, WHITE)
    y += hl_line_h + hl_gap

y += separator_gap - hl_gap
# thin violet separator
draw.line([(MARGIN, y), (W - MARGIN, y)], fill=(*VIOLET, 70), width=1)
y += 1 + separator_gap

for line in lines_violet:
    draw_centered(draw, line, y, f_hl, VIOLET)
    y += hl_line_h + hl_gap

y += 44  # space after headline

# ── subtext ───────────────────────────────────────────────────────────────────
subtext = "Every click you're paying for is leaving without a reply."
sw = text_w(draw, subtext, f_sub)
draw.text(((W - sw) // 2, y), subtext, font=f_sub, fill=GRAY)
y += text_h(draw, subtext, f_sub) + 40

# ── CTA pill ─────────────────────────────────────────────────────────────────
cta_text  = "DM 'INFO' sekarang"
cta_tw    = text_w(draw, cta_text, f_cta)
cta_th    = text_h(draw, cta_text, f_cta)
pad_x, pad_y = 36, 13
pill_w    = cta_tw + pad_x * 2
pill_h    = cta_th + pad_y * 2
pill_x    = (W - pill_w) // 2
draw.rounded_rectangle(
    [pill_x, y, pill_x + pill_w, y + pill_h],
    radius=pill_h // 2,
    fill=VIOLET,
)
draw.text((pill_x + pad_x, y + pad_y), cta_text, font=f_cta, fill=WHITE)
y += pill_h

# ── bottom rule & brand ───────────────────────────────────────────────────────
bottom_rule_y = H - 76
draw.line([(MARGIN, bottom_rule_y), (W - MARGIN, bottom_rule_y)], fill=(*VIOLET, 55), width=1)

brand_y = H - 52
draw.text((MARGIN, brand_y), "IGEN VERITAS", font=f_mono, fill=MUTED)

site = "igen-veritas.com"
draw.text((W - MARGIN - text_w(draw, site, f_mono), brand_y), site, font=f_mono, fill=MUTED)

img.save(OUT, "PNG", dpi=(300, 300))
print(f"Saved → {OUT}")
