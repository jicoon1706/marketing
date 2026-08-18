"""
CB-003 Carousel — 4 slides
"Who are we? 4 things to know about IGEN VERITAS."
Awareness post | May 5 | Violet-navy palette
Saves to: social-media/CB-003_carousel/
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ── Constants ─────────────────────────────────────────────────────────────────
VIOLET      = (123, 103, 209)
PURPLE      = (138, 93, 204)
BLUE_MID    = (72, 143, 227)
BLUE_BRIGHT = (65, 150, 230)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
LIGHT_VIOLET= (180, 165, 240)

W, H = 1080, 1080
EDGE = 70

OUT_DIR = r"C:\Users\jicoo\OneDrive\Documents\Claude\marketing_team\social-media\CB-003_carousel"
os.makedirs(OUT_DIR, exist_ok=True)

# ── Fonts ──────────────────────────────────────────────────────────────────────
def font(size, weight="regular"):
    paths = {
        "black":   "C:/Windows/Fonts/segoeuib.ttf",
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    p = paths.get(weight, paths["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

# ── Helpers ────────────────────────────────────────────────────────────────────
def navy_to_violet_gradient(draw):
    """Diagonal gradient: dark navy top-left → violet bottom-right."""
    for i in range(1080):
        t = i / 1079
        r = int(DARK_NAVY[0] + (VIOLET[0] - DARK_NAVY[0]) * t * 0.55)
        g = int(DARK_NAVY[1] + (VIOLET[1] - DARK_NAVY[1]) * t * 0.55)
        b = int(DARK_NAVY[2] + (VIOLET[2] - DARK_NAVY[2]) * t * 0.55)
        draw.line([(0, i), (1080, i)], fill=(r, g, b, 255))


def add_glow(img, cx, cy, radius=360, color=(123, 103, 209)):
    """Soft radial glow overlay."""
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd   = ImageDraw.Draw(glow)
    steps = 40
    for s in range(steps, 0, -1):
        r2  = int(radius * s / steps)
        alpha = int(18 * s / steps)
        gd.ellipse([cx - r2, cy - r2, cx + r2, cy + r2],
                   fill=(color[0], color[1], color[2], alpha))
    return Image.alpha_composite(img, glow)


def draw_dot_grid(draw, color=(255, 255, 255, 18)):
    """Subtle dot-grid texture."""
    for x in range(0, W, 48):
        for y in range(0, H, 48):
            draw.ellipse([x-2, y-2, x+2, y+2], fill=color)


def branding(draw, slide_num, total=4):
    """Brand name top-left, slide counter top-right."""
    f_brand = font(22, "bold")
    f_url   = font(18, "regular")
    f_count = font(22, "regular")

    draw.text((EDGE, EDGE), "IGEN VERITAS", font=f_brand,
              fill=(*LIGHT_VIOLET, 230))
    draw.text((EDGE, EDGE + 28), "igen-veritas.com", font=f_url,
              fill=(*BODY_GRAY, 200))

    counter = f"{slide_num} / {total}"
    bbox = draw.textbbox((0, 0), counter, font=f_count)
    tw = bbox[2] - bbox[0]
    draw.text((W - EDGE - tw, EDGE + 10), counter, font=f_count,
              fill=(*BODY_GRAY, 200))


def accent_line(draw, y=140, alpha=80):
    draw.line([(EDGE, y), (W - EDGE, y)],
              fill=(*VIOLET, alpha), width=1)


def violet_pill(draw, text, x, y, fsize=20):
    f = font(fsize, "bold")
    bbox = draw.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad_x, pad_y = 24, 12
    rx1, ry1 = x, y
    rx2, ry2 = x + tw + pad_x * 2, y + th + pad_y * 2
    draw.rounded_rectangle([rx1, ry1, rx2, ry2], radius=30,
                            fill=(*VIOLET, 200), outline=(*LIGHT_VIOLET, 120), width=1)
    draw.text((rx1 + pad_x, ry1 + pad_y), text, font=f, fill=WHITE)


def wrap_text(draw, text, font_obj, max_width):
    """Return list of lines that fit within max_width."""
    words = text.split()
    lines, line = [], ""
    for w in words:
        test = (line + " " + w).strip()
        bbox = draw.textbbox((0, 0), test, font=font_obj)
        if bbox[2] - bbox[0] <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def draw_multiline(draw, lines, font_obj, cx, start_y, color=WHITE, line_height=None):
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font_obj)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        lh = line_height or (th + 12)
        draw.text((cx - tw // 2, start_y + i * lh), line, font=font_obj, fill=color)
    total = len(lines) * (line_height or (draw.textbbox((0,0), lines[0], font=font_obj)[3] + 12))
    return total


# ── SLIDE 1 — Bold Intro Hook ─────────────────────────────────────────────────
def slide_1():
    img  = Image.new("RGBA", (W, H), (*DARK_NAVY, 255))
    draw = ImageDraw.Draw(img)
    navy_to_violet_gradient(draw)
    draw_dot_grid(draw)
    img = add_glow(img, cx=W//2, cy=H//2 - 80, radius=420, color=VIOLET)
    draw = ImageDraw.Draw(img)

    branding(draw, 1)
    accent_line(draw)

    # Big slide number watermark
    f_num = font(340, "bold")
    draw.text((W//2, H//2 + 60), "01", font=f_num,
              fill=(*VIOLET, 18), anchor="mm")

    # Hook headline
    f_hook = font(90, "bold")
    hook_lines = ["Who are we?"]
    draw_multiline(draw, hook_lines, f_hook, W//2, 240, WHITE, line_height=100)

    # Sub-headline
    f_sub = font(44, "regular")
    sub_lines = ["4 things to know about"]
    draw_multiline(draw, sub_lines, f_sub, W//2, 360, (*LIGHT_VIOLET, 230), line_height=56)

    # Brand name accent
    f_brand_big = font(72, "bold")
    bbox = draw.textbbox((0, 0), "IGEN VERITAS", font=f_brand_big)
    tw = bbox[2] - bbox[0]
    draw.text((W//2 - tw//2, 430), "IGEN VERITAS", font=f_brand_big,
              fill=(*LIGHT_VIOLET, 255))

    # Swipe prompt at bottom
    f_swipe = font(26, "regular")
    draw.text((W//2, H - EDGE - 10), "Swipe to find out →",
              font=f_swipe, fill=(*BODY_GRAY, 200), anchor="mm")

    # Bottom accent bar
    draw.rectangle([0, H - 6, W, H], fill=(*VIOLET, 255))

    img.save(os.path.join(OUT_DIR, "slide_01.png"), "PNG")
    print("OK slide_01.png saved")


# ── SLIDE 2 — What We Do ──────────────────────────────────────────────────────
def slide_2():
    img  = Image.new("RGBA", (W, H), (*DARK_NAVY, 255))
    draw = ImageDraw.Draw(img)
    navy_to_violet_gradient(draw)
    draw_dot_grid(draw)
    img = add_glow(img, cx=200, cy=300, radius=340, color=BLUE_MID)
    draw = ImageDraw.Draw(img)

    branding(draw, 2)
    accent_line(draw)

    # Slide label pill
    violet_pill(draw, "01 — WHAT WE DO", EDGE, 160, fsize=22)

    # Headline
    f_h = font(78, "bold")
    h_lines = ["We build AI &", "digital tools that", "grow businesses."]
    y = 270
    for line in h_lines:
        bbox = draw.textbbox((0, 0), line, font=f_h)
        draw.text((EDGE, y), line, font=f_h, fill=WHITE)
        y += 88

    # Divider
    draw.line([(EDGE, 540), (W - EDGE, 540)], fill=(*VIOLET, 80), width=1)

    # Feature cards
    services = [
        ("🤖", "AI Chatbots",      "24/7 lead capture & auto-reply\nvia WhatsApp & website"),
        ("🌐", "Web Development",  "React & Laravel — fast,\nresponsive, conversion-ready"),
        ("📱", "Mobile Apps",      "Flutter & Firebase — iOS\nand Android, built to scale"),
    ]

    card_y = 570
    card_w = 290
    card_h = 190
    gap    = 35
    start_x = (W - (card_w * 3 + gap * 2)) // 2

    f_icon  = font(36, "regular")
    f_label = font(26, "bold")
    f_desc  = font(19, "regular")

    for i, (icon, label, desc) in enumerate(services):
        cx = start_x + i * (card_w + gap)
        # Card bg
        draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h],
                                radius=20,
                                fill=(255, 255, 255, 12),
                                outline=(*VIOLET, 70), width=1)
        # Icon
        draw.text((cx + 22, card_y + 18), icon, font=f_icon, fill=WHITE)
        # Label
        draw.text((cx + 22, card_y + 64), label, font=f_label, fill=(*LIGHT_VIOLET, 255))
        # Desc
        for j, dline in enumerate(desc.split("\n")):
            draw.text((cx + 22, card_y + 100 + j * 26), dline, font=f_desc,
                      fill=(*BODY_GRAY, 210))

    # Bottom bar
    draw.rectangle([0, H - 6, W, H], fill=(*VIOLET, 255))

    img.save(os.path.join(OUT_DIR, "slide_02.png"), "PNG")
    print("OK slide_02.png saved")


# ── SLIDE 3 — Who We Help ─────────────────────────────────────────────────────
def slide_3():
    img  = Image.new("RGBA", (W, H), (*DARK_NAVY, 255))
    draw = ImageDraw.Draw(img)
    navy_to_violet_gradient(draw)
    draw_dot_grid(draw)
    img = add_glow(img, cx=W - 200, cy=400, radius=360, color=PURPLE)
    draw = ImageDraw.Draw(img)

    branding(draw, 3)
    accent_line(draw)

    # Slide label pill
    violet_pill(draw, "02 — WHO WE HELP", EDGE, 160, fsize=22)

    # Headline
    f_h  = font(76, "bold")
    f_h2 = font(76, "regular")
    draw.text((EDGE, 270), "Built for", font=f_h2, fill=(*BODY_GRAY, 200))
    draw.text((EDGE, 360), "Malaysian SMEs", font=f_h, fill=WHITE)
    draw.text((EDGE, 450), "& entrepreneurs.", font=f_h2, fill=(*LIGHT_VIOLET, 230))

    # Divider
    draw.line([(EDGE, 555), (W - EDGE, 555)], fill=(*VIOLET, 80), width=1)

    # Target audience rows
    audiences = [
        ("🏪", "Business owners",      "who want leads 24/7 without hiring more staff"),
        ("🚀", "Growing SMEs",         "that need automation to keep up with demand"),
        ("💻", "Solo entrepreneurs",   "building an online presence from scratch"),
        ("📈", "Existing businesses",  "ready to go from manual to fully automated"),
    ]

    f_aud_icon  = font(32, "regular")
    f_aud_label = font(28, "bold")
    f_aud_desc  = font(22, "regular")

    row_y = 590
    for icon, label, desc in audiences:
        draw.text((EDGE, row_y), icon, font=f_aud_icon, fill=WHITE)
        draw.text((EDGE + 52, row_y + 2), label, font=f_aud_label, fill=(*LIGHT_VIOLET, 255))
        draw.text((EDGE + 52, row_y + 36), desc, font=f_aud_desc,
                  fill=(*BODY_GRAY, 200))
        row_y += 94

    # Bottom bar
    draw.rectangle([0, H - 6, W, H], fill=(*VIOLET, 255))

    img.save(os.path.join(OUT_DIR, "slide_03.png"), "PNG")
    print("OK slide_03.png saved")


# ── SLIDE 4 — Our Promise ─────────────────────────────────────────────────────
def slide_4():
    img  = Image.new("RGBA", (W, H), (*DARK_NAVY, 255))
    draw = ImageDraw.Draw(img)
    navy_to_violet_gradient(draw)
    draw_dot_grid(draw)
    img = add_glow(img, cx=W//2, cy=H//2, radius=500, color=VIOLET)
    draw = ImageDraw.Draw(img)

    branding(draw, 4)
    accent_line(draw)

    # Slide label pill
    violet_pill(draw, "03 — OUR PROMISE", EDGE, 160, fsize=22)

    # Headline
    f_h = font(80, "bold")
    draw.text((EDGE, 265), "We don't just", font=font(60, "regular"), fill=(*BODY_GRAY, 200))
    draw.text((EDGE, 335), "build software.", font=f_h, fill=WHITE)
    draw.text((EDGE, 425), "We build results.", font=f_h, fill=(*LIGHT_VIOLET, 255))

    # Divider
    draw.line([(EDGE, 530), (W - EDGE, 530)], fill=(*VIOLET, 80), width=1)

    # Promise pillars — 2×2 grid
    pillars = [
        ("🔒", "VERITAS",     "Transparency in everything\nwe deliver. No hidden costs."),
        ("⚡", "Speed",       "5–7 day build turnaround.\nYour chatbot goes live fast."),
        ("🎯", "Results-Led", "We measure success by\nyour leads and revenue."),
        ("🤝", "Partnership", "We grow when you grow.\nLong-term, not one-shot."),
    ]

    f_p_icon  = font(36, "regular")
    f_p_label = font(28, "bold")
    f_p_desc  = font(20, "regular")

    card_w, card_h = 430, 180
    gap_x, gap_y   = 30, 24
    start_x = (W - (card_w * 2 + gap_x)) // 2
    start_y = 560

    for i, (icon, label, desc) in enumerate(pillars):
        col = i % 2
        row = i // 2
        cx = start_x + col * (card_w + gap_x)
        cy = start_y + row * (card_h + gap_y)

        draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h],
                                radius=20,
                                fill=(255, 255, 255, 10),
                                outline=(*VIOLET, 70), width=1)
        draw.text((cx + 22, cy + 18), icon, font=f_p_icon, fill=WHITE)
        draw.text((cx + 68, cy + 20), label, font=f_p_label, fill=(*LIGHT_VIOLET, 255))
        for j, dline in enumerate(desc.split("\n")):
            draw.text((cx + 22, cy + 70 + j * 28), dline, font=f_p_desc,
                      fill=(*BODY_GRAY, 210))

    # CTA strip at bottom
    cta_y = H - 110
    draw.rounded_rectangle([EDGE, cta_y, W - EDGE, cta_y + 62],
                            radius=31, fill=(*VIOLET, 230))
    f_cta = font(28, "bold")
    draw.text((W//2, cta_y + 31), "DM 'INFO' to get started  →",
              font=f_cta, fill=WHITE, anchor="mm")

    # Bottom bar
    draw.rectangle([0, H - 6, W, H], fill=(*VIOLET, 255))

    img.save(os.path.join(OUT_DIR, "slide_04.png"), "PNG")
    print("OK slide_04.png saved")


# ── Run all ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    slide_1()
    slide_2()
    slide_3()
    slide_4()
    print(f"\nAll 4 slides saved to: {OUT_DIR}")
