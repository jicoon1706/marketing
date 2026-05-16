"""
CB-014 Carousel Generator — IGEN VERITAS AI Chatbot Package Reveal
5 slides, 1080x1080 px — v2 rework

Fixes vs v1:
- Slide 1: "Pro." no longer overlaps subtext; pricing teaser added
- Slides 2-4: Pricing box added; vertical space filled properly
- Slide 5: Logo fixed on gradient; 3-tier summary row added above CTA
"""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = r"C:\Users\jicoo\.claude\plugins\cache\anthropic-agent-skills\document-skills\f458cee31a75\skills\canvas-design\canvas-fonts"
OUT_DIR  = r"C:\Users\jicoo\OneDrive\IGEN VERITAS TECHNOLOGIES\marketing_team\social-media\CB-014_carousel"
os.makedirs(OUT_DIR, exist_ok=True)

# -- Brand colors -------------------------------------------------------------
NAVY        = (11,  11,  20)
VIOLET      = (123, 103, 209)
PURPLE      = (138,  93, 204)
BLUE_MID    = (72,  143, 227)
BLUE_BRIGHT = (65,  150, 230)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
SILVER      = (178, 183, 198)

SIZE = 1080

F_BOLD   = "BricolageGrotesque-Bold.ttf"
F_REG    = "WorkSans-Regular.ttf"
F_SEMIB  = "InstrumentSans-Bold.ttf"
F_ITALIC = "WorkSans-Italic.ttf"

def fnt(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

def new_canvas():
    return Image.new("RGBA", (SIZE, SIZE), (*NAVY, 255))

def lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

# -- Drawing helpers ----------------------------------------------------------

def h_gradient(img, x, y, w, h, c1, c2, radius=0):
    tmp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    td  = ImageDraw.Draw(tmp)
    for i in range(w):
        c = lerp(c1, c2, i / max(w - 1, 1))
        td.line([(i, 0), (i, h - 1)], fill=(*c, 255))
    if radius:
        mask = Image.new("L", (w, h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
        tmp.putalpha(mask)
    img.paste(tmp, (x, y), tmp)

def pill(img, x, y, w, h, c1, c2=None, radius=18):
    h_gradient(img, x, y, w, h, c1, c2 or c1, radius)

def glass_card(img, x, y, w, h, radius=28):
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    cd   = ImageDraw.Draw(card)
    cd.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=(255, 255, 255, 12))
    cd.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, outline=(255, 255, 255, 28), width=1)
    img.paste(card, (x, y), card)

def v_accent(img, x, y, h, c1, c2, width=5):
    acc = Image.new("RGBA", (width, h), (0, 0, 0, 0))
    ad  = ImageDraw.Draw(acc)
    for yy in range(h):
        c = lerp(c1, c2, yy / max(h - 1, 1))
        ad.line([(0, yy), (width - 1, yy)], fill=(*c, 255))
    img.paste(acc, (x, y), acc)

def glow(img, cx, cy, max_r, color, max_a=14, step=5):
    g  = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    gd = ImageDraw.Draw(g)
    for r in range(max_r, 0, -step):
        a = int(max_a * (1 - r / max_r))
        gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, a))
    return Image.alpha_composite(img, g)

def get_tw(draw, text, f):
    bb = draw.textbbox((0, 0), text, font=f)
    return bb[2] - bb[0]

def get_th(draw, text, f):
    bb = draw.textbbox((0, 0), text, font=f)
    return bb[3] - bb[1]

def text_cx(draw, text, y, f, color):
    w = get_tw(draw, text, f)
    draw.text(((SIZE - w) // 2, y), text, font=f, fill=color)

def pill_cx(img, draw, text, y, f, c1, c2, ph=44, pad=24, r=22):
    w = get_tw(draw, text, f) + pad * 2
    x = (SIZE - w) // 2
    pill(img, x, y, w, ph, c1, c2, r)
    draw = ImageDraw.Draw(img)
    text_cx(draw, text, y + (ph - get_th(draw, text, f)) // 2 - 1, f, WHITE)
    return draw

def dot(draw, x, y, color, r=5):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=color)

def logo(draw, img, x=52, y=44, on_grad=False):
    r = 16
    cx, cy = x + r, y + r
    c1 = WHITE if on_grad else VIOLET
    c2 = (190, 210, 255) if on_grad else BLUE_BRIGHT
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=c1, width=3)
    draw.ellipse([cx - r + 6, cy - r + 6, cx + r - 6, cy + r - 6], outline=c2, width=2)
    draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=WHITE)
    draw.text((x + r * 2 + 10, y + 6), "IGEN VERITAS", font=fnt(F_BOLD, 20), fill=WHITE)

def footer(draw):
    f = fnt(F_REG, 22)
    w = get_tw(draw, "igenveritas.com", f)
    draw.text((SIZE - w - 52, SIZE - 52), "igenveritas.com", font=f, fill=BODY_GRAY)

def slide_num(draw, label):
    f = fnt(F_REG, 22)
    text_cx(draw, label, SIZE - 60, f, BODY_GRAY)

def price_strip(img, draw, ix, iy, bw, setup, monthly, accent):
    """Two-cell pricing row: [setup | monthly] with tinted glass bg."""
    BH = 76
    gb  = Image.new("RGBA", (bw, BH), (0, 0, 0, 0))
    gbd = ImageDraw.Draw(gb)
    gbd.rounded_rectangle([0, 0, bw - 1, BH - 1], radius=14, fill=(*accent, 18))
    gbd.rounded_rectangle([0, 0, bw - 1, BH - 1], radius=14, outline=(*accent, 55), width=1)
    img.paste(gb, (ix, iy), gb)
    draw = ImageDraw.Draw(img)

    half = bw // 2
    pf = fnt(F_BOLD, 30)
    lf = fnt(F_REG, 17)

    draw.text((ix + 20, iy + 12), setup,   font=pf, fill=WHITE)
    draw.text((ix + 20, iy + 48), "one-time setup", font=lf, fill=BODY_GRAY)

    draw.line([(ix + half, iy + 14), (ix + half, iy + BH - 14)],
              fill=(255, 255, 255, 30), width=1)

    draw.text((ix + half + 20, iy + 12), monthly, font=pf, fill=(*accent,))
    draw.text((ix + half + 20, iy + 48), "per month",     font=lf, fill=BODY_GRAY)

    return draw, iy + BH


# ============================================================================
# SLIDE 1 — COVER
# ============================================================================
def slide1():
    img = new_canvas()

    # Vertical gradient bg (navy → deep purple-navy)
    ov  = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    ovd = ImageDraw.Draw(ov)
    for yy in range(SIZE):
        c = lerp(NAVY, (20, 14, 42), yy / (SIZE - 1))
        ovd.line([(0, yy), (SIZE, yy)], fill=(*c, 255))
    img = Image.alpha_composite(img, ov)

    img = glow(img, SIZE, 0,      540, VIOLET,   max_a=20, step=4)
    img = glow(img, 0,    SIZE,   440, BLUE_MID,  max_a=13, step=4)
    img = glow(img, SIZE // 2, SIZE // 2, 280, PURPLE, max_a=6, step=5)

    draw = ImageDraw.Draw(img)
    logo(draw, img)

    # Category badge
    draw = pill_cx(img, draw, "AI CHATBOT PACKAGES", 162,
                   fnt(F_SEMIB, 20), VIOLET, BLUE_MID, ph=44)

    # 3-line headline — 92 px, 110 px step (no overlap with subtext)
    hf = fnt(F_BOLD, 92)
    hy = 248
    for word, color in [("Basic.", BLUE_MID), ("Growth.", VIOLET), ("Pro.", WHITE)]:
        text_cx(draw, word, hy, hf, color)
        hy += 110
    # hy = 578 after loop

    # Subtext — clear gap below "Pro."
    hy += 30  # 608
    text_cx(draw, "No fluff. No guessing. Real pricing inside.",
            hy, fnt(F_REG, 27), BODY_GRAY)

    # Pricing teaser strip
    hy += 60  # 668
    tf       = fnt(F_SEMIB, 21)
    teaser   = "From RM 500 setup  ·  Monthly from RM 150"
    tw_val   = get_tw(draw, teaser, tf)
    tx       = (SIZE - tw_val) // 2
    sw, sh   = tw_val + 52, 46
    strip    = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    sd       = ImageDraw.Draw(strip)
    sd.rounded_rectangle([0, 0, sw - 1, sh - 1], radius=23, fill=(255, 255, 255, 10))
    sd.rounded_rectangle([0, 0, sw - 1, sh - 1], radius=23, outline=(255, 255, 255, 22), width=1)
    img.paste(strip, (tx - 26, hy), strip)
    draw = ImageDraw.Draw(img)
    draw.text((tx, hy + 12), teaser, font=tf, fill=SILVER)

    text_cx(draw, "Swipe to see each plan  →", SIZE - 74, fnt(F_REG, 22), BODY_GRAY)
    footer(draw)

    img.convert("RGB").save(os.path.join(OUT_DIR, "CB-014_slide1_cover.png"), "PNG", quality=98)
    print("Slide 1 done")


# ============================================================================
# SLIDE 2 — BASIC
# ============================================================================
def slide2():
    img = new_canvas()
    img = glow(img, SIZE // 2, SIZE // 2, 400, BLUE_MID, max_a=9, step=5)

    PAD, CY, CW, CH = 80, 108, 920, 790
    glass_card(img, PAD, CY, CW, CH)

    draw = ImageDraw.Draw(img)
    logo(draw, img)

    IX = PAD + 52
    IY = CY + 44
    BW = CW - 52 - 52  # 816 — price strip width

    # Package name
    draw.text((IX, IY), "BASIC", font=fnt(F_BOLD, 86), fill=BLUE_MID)
    IY += 104

    # Pricing strip
    draw, IY = price_strip(img, draw, IX, IY, BW,
                           "RM 500", "RM 150", BLUE_MID)
    IY += 20

    # Divider
    draw.line([(IX, IY), (PAD + CW - 52, IY)], fill=(255, 255, 255, 30), width=1)
    IY += 22

    # Tool pill
    tf = fnt(F_SEMIB, 20)
    pw = get_tw(draw, "Botpress", tf) + 36
    pill(img, IX, IY, pw, 38, BLUE_MID, BLUE_BRIGHT, radius=19)
    draw = ImageDraw.Draw(img)
    draw.text((IX + 18, IY + 9), "Botpress", font=tf, fill=WHITE)
    IY += 56

    # Features
    ff = fnt(F_REG, 28)
    for feat in [
        "Web chatbot on your website",
        "AI-powered FAQ from knowledge base",
        "Lead capture — name, phone, email",
        "Email notification to owner",
        "Bahasa Melayu + English support",
    ]:
        dot(draw, IX + 9, IY + 15, BLUE_MID)
        draw.text((IX + 26, IY), feat, font=ff, fill=WHITE)
        IY += 56

    IY += 8
    draw.text((IX, IY), "Best for: Small businesses starting with automation",
              font=fnt(F_ITALIC, 22), fill=BODY_GRAY)

    slide_num(draw, "1 of 3  ›")
    footer(draw)

    img.convert("RGB").save(os.path.join(OUT_DIR, "CB-014_slide2_basic.png"), "PNG", quality=98)
    print("Slide 2 done")


# ============================================================================
# SLIDE 3 — GROWTH
# ============================================================================
def slide3():
    img = new_canvas()
    img = glow(img, SIZE // 2, SIZE // 2, 400, VIOLET, max_a=9, step=5)

    PAD, CY, CW, CH = 80, 108, 920, 810
    glass_card(img, PAD, CY, CW, CH)
    v_accent(img, PAD, CY + 30, CH - 60, VIOLET, BLUE_MID, width=5)

    draw = ImageDraw.Draw(img)
    logo(draw, img)

    # "MOST POPULAR" badge top-right
    mp_f = fnt(F_SEMIB, 17)
    mp_t = "MOST POPULAR"
    mp_w = get_tw(draw, mp_t, mp_f) + 28
    mp_x = PAD + CW - mp_w - 20
    mp_y = CY + 18
    pill(img, mp_x, mp_y, mp_w, 34, VIOLET, BLUE_MID, radius=17)
    draw = ImageDraw.Draw(img)
    draw.text((mp_x + 14, mp_y + 8), mp_t, font=mp_f, fill=WHITE)

    IX = PAD + 60
    IY = CY + 44
    BW = CW - 60 - 52

    draw.text((IX, IY), "GROWTH", font=fnt(F_BOLD, 86), fill=VIOLET)
    IY += 104

    draw, IY = price_strip(img, draw, IX, IY, BW,
                           "RM 1,000", "RM 300", VIOLET)
    IY += 20

    draw.line([(IX, IY), (PAD + CW - 52, IY)], fill=(255, 255, 255, 30), width=1)
    IY += 22

    # Tool pills
    tf  = fnt(F_SEMIB, 20)
    px_ = IX
    for label, c1, c2 in [("Botpress", VIOLET, PURPLE), ("n8n", BLUE_MID, BLUE_BRIGHT)]:
        pw = get_tw(draw, label, tf) + 36
        pill(img, px_, IY, pw, 38, c1, c2, radius=19)
        draw = ImageDraw.Draw(img)
        draw.text((px_ + 18, IY + 9), label, font=tf, fill=WHITE)
        px_ += pw + 12
    IY += 54

    draw.text((IX, IY), "Everything in Basic, plus:",
              font=fnt(F_ITALIC, 21), fill=BODY_GRAY)
    IY += 38

    ff = fnt(F_REG, 28)
    for feat in [
        "WhatsApp notification to owner",
        "Google Sheets CRM integration",
        "24-hour automated follow-up",
        "Mandarin language support",
        "Monthly performance report",
    ]:
        dot(draw, IX + 9, IY + 15, VIOLET)
        draw.text((IX + 26, IY), feat, font=ff, fill=WHITE)
        IY += 56

    IY += 8
    draw.text((IX, IY), "Best for: Growing businesses wanting WhatsApp + CRM",
              font=fnt(F_ITALIC, 22), fill=BODY_GRAY)

    slide_num(draw, "2 of 3  ›")
    footer(draw)

    img.convert("RGB").save(os.path.join(OUT_DIR, "CB-014_slide3_growth.png"), "PNG", quality=98)
    print("Slide 3 done")


# ============================================================================
# SLIDE 4 — PRO
# ============================================================================
def slide4():
    img = new_canvas()
    img = glow(img, SIZE // 2, 100, 440, BLUE_BRIGHT, max_a=11, step=5)

    PAD, CY, CW, CH = 80, 92, 920, 860
    glass_card(img, PAD, CY, CW, CH)
    v_accent(img, PAD, CY + 28, CH - 56, VIOLET, BLUE_BRIGHT, width=5)

    draw = ImageDraw.Draw(img)
    logo(draw, img)

    # "MOST POWERFUL" badge
    mp_f = fnt(F_SEMIB, 17)
    mp_t = "MOST POWERFUL"
    mp_w = get_tw(draw, mp_t, mp_f) + 28
    mp_x = PAD + CW - mp_w - 20
    mp_y = CY + 18
    pill(img, mp_x, mp_y, mp_w, 34, VIOLET, BLUE_BRIGHT, radius=17)
    draw = ImageDraw.Draw(img)
    draw.text((mp_x + 14, mp_y + 8), mp_t, font=mp_f, fill=WHITE)

    IX = PAD + 60
    IY = CY + 38
    BW = CW - 60 - 52

    draw.text((IX, IY), "PRO", font=fnt(F_BOLD, 86), fill=BLUE_BRIGHT)
    IY += 102

    draw, IY = price_strip(img, draw, IX, IY, BW,
                           "RM 2,000", "RM 500", BLUE_BRIGHT)
    IY += 18

    draw.line([(IX, IY), (PAD + CW - 52, IY)], fill=(255, 255, 255, 30), width=1)
    IY += 20

    tf  = fnt(F_SEMIB, 20)
    px_ = IX
    for label, c1, c2 in [("Botpress", VIOLET, PURPLE), ("n8n (full)", BLUE_MID, BLUE_BRIGHT)]:
        pw = get_tw(draw, label, tf) + 36
        pill(img, px_, IY, pw, 38, c1, c2, radius=19)
        draw = ImageDraw.Draw(img)
        draw.text((px_ + 18, IY + 9), label, font=tf, fill=WHITE)
        px_ += pw + 12
    IY += 52

    draw.text((IX, IY), "Everything in Growth, plus:",
              font=fnt(F_ITALIC, 21), fill=BODY_GRAY)
    IY += 36

    ff = fnt(F_REG, 26)
    for feat in [
        "Full AI sales funnel (qualify → book)",
        "Lead scoring — hot / warm / cold",
        "Smart product recommendations",
        "Multi-step follow-up: Day 1, 3, 7",
        "Hot lead alert — respond within 15 min",
        "Weekly performance dashboard",
        "Priority support",
    ]:
        dot(draw, IX + 9, IY + 14, BLUE_BRIGHT)
        draw.text((IX + 26, IY), feat, font=ff, fill=WHITE)
        IY += 50

    IY += 6
    draw.text((IX, IY), "Best for: Businesses serious about converting every lead",
              font=fnt(F_ITALIC, 21), fill=BODY_GRAY)

    slide_num(draw, "3 of 3  ›")
    footer(draw)

    img.convert("RGB").save(os.path.join(OUT_DIR, "CB-014_slide4_pro.png"), "PNG", quality=98)
    print("Slide 4 done")


# ============================================================================
# SLIDE 5 — CTA
# ============================================================================
def slide5():
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))

    # Diagonal gradient bg (violet → blue-bright)
    bg  = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    bgd = ImageDraw.Draw(bg)
    for yy in range(SIZE):
        for xx in range(SIZE):
            t = (yy / (SIZE - 1) + xx / (SIZE - 1)) / 2
            bgd.point((xx, yy), fill=(*lerp(VIOLET, BLUE_BRIGHT, t), 255))
    img = Image.alpha_composite(img, bg)

    # Decorative rings
    rings = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    rd    = ImageDraw.Draw(rings)
    rd.ellipse([SIZE - 340, -180, SIZE + 100, 300], outline=(255, 255, 255, 28), width=2)
    rd.ellipse([SIZE - 290, -140, SIZE + 50,  250], outline=(255, 255, 255, 16), width=1)
    rd.ellipse([-120, SIZE - 320, 320, SIZE + 120], outline=(255, 255, 255, 22), width=2)
    rd.ellipse([-80,  SIZE - 270, 270, SIZE + 80],  outline=(255, 255, 255, 14), width=1)
    img = Image.alpha_composite(img, rings)

    draw = ImageDraw.Draw(img)
    logo(draw, img, on_grad=True)

    # Headline
    hf = fnt(F_BOLD, 66)
    text_cx(draw, "Which plan fits",    174, hf, WHITE)
    text_cx(draw, "your business?",     254, hf, WHITE)

    # Subtext
    text_cx(draw, "No hidden fees. No confusion. Just results.",
            352, fnt(F_REG, 26), (228, 228, 255))

    # 3-tier summary cards
    tiers = [
        ("Basic",  "RM 500 + RM 150/mo",  BLUE_MID),
        ("Growth", "RM 1k + RM 300/mo",   VIOLET),
        ("Pro",    "RM 2k + RM 500/mo",   BLUE_BRIGHT),
    ]
    CW_, CH_ = 270, 86
    gap_     = 15
    row_x    = (SIZE - (CW_ * 3 + gap_ * 2)) // 2
    row_y    = 402
    for i, (name, price, color) in enumerate(tiers):
        cx = row_x + i * (CW_ + gap_)
        c  = Image.new("RGBA", (CW_, CH_), (0, 0, 0, 0))
        cd = ImageDraw.Draw(c)
        cd.rounded_rectangle([0, 0, CW_ - 1, CH_ - 1], radius=14, fill=(11, 11, 20, 170))
        cd.rounded_rectangle([0, 0, CW_ - 1, CH_ - 1], radius=14, outline=(*color, 110), width=2)
        img.paste(c, (cx, row_y), c)
        draw = ImageDraw.Draw(img)
        nf  = fnt(F_BOLD, 24)
        pf_ = fnt(F_REG, 17)
        nw  = get_tw(draw, name, nf)
        pw_ = get_tw(draw, price, pf_)
        draw.text((cx + (CW_ - nw) // 2, row_y + 13), name,  font=nf,  fill=(*color,))
        draw.text((cx + (CW_ - pw_) // 2, row_y + 47), price, font=pf_, fill=WHITE)

    # CTA box
    BX, BY = 100, 516
    BW_, BH_ = SIZE - 200, 276
    cta  = Image.new("RGBA", (BW_, BH_), (0, 0, 0, 0))
    ctad = ImageDraw.Draw(cta)
    ctad.rounded_rectangle([0, 0, BW_ - 1, BH_ - 1], radius=24, fill=(11, 11, 20, 168))
    ctad.rounded_rectangle([0, 0, BW_ - 1, BH_ - 1], radius=24, outline=(255, 255, 255, 45), width=1)
    img.paste(cta, (BX, BY), cta)
    draw = ImageDraw.Draw(img)

    sf = fnt(F_REG, 26)
    text_cx(draw, "DM us the word", BY + 40, sf, WHITE)

    plan_f = fnt(F_BOLD, 52)
    plan_t = "  'PLAN'  "
    plan_w = get_tw(draw, plan_t, plan_f) + 16
    plan_h = 68
    plan_x = (SIZE - plan_w) // 2
    plan_y = BY + 88
    pill(img, plan_x, plan_y, plan_w, plan_h, VIOLET, PURPLE, radius=16)
    draw = ImageDraw.Draw(img)
    text_cx(draw, plan_t, plan_y + 10, plan_f, WHITE)

    text_cx(draw, "and we’ll match you to the right tier.", BY + 184, sf, WHITE)

    text_cx(draw, "igenveritas.com  ·  +60 17 310 3966",
            SIZE - 78, fnt(F_REG, 23), (222, 226, 255))

    img.convert("RGB").save(os.path.join(OUT_DIR, "CB-014_slide5_cta.png"), "PNG", quality=98)
    print("Slide 5 done")


# -- Run all ------------------------------------------------------------------
if __name__ == "__main__":
    print("Generating CB-014 carousel v2...")
    slide1()
    slide2()
    slide3()
    slide4()
    slide5()
    print("Done →", OUT_DIR)
