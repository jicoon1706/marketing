"""
IGEN VERITAS — Week 1 Social Media Visuals
Post 1: May 1 (Thu) — Awareness / Brand Intro (Instagram)
Post 2: May 3 (Sat) — Pain Point (Instagram)
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

OUT_DIR = os.path.join(os.path.dirname(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

# ─── Font helper ────────────────────────────────────────────────────────────

def font(size, weight="regular"):
    paths = {
        "black":   "C:/Windows/Fonts/segoeuib.ttf",
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    p = paths.get(weight, paths["regular"])
    try:
        return ImageFont.truetype(p, size)
    except:
        return ImageFont.load_default()

# ─── Gradient helpers ────────────────────────────────────────────────────────

def draw_vertical_gradient(draw, w, h, top_rgb, bot_rgb):
    for y in range(h):
        t = y / h
        r = int(top_rgb[0] + (bot_rgb[0] - top_rgb[0]) * t)
        g = int(top_rgb[1] + (bot_rgb[1] - top_rgb[1]) * t)
        b = int(top_rgb[2] + (bot_rgb[2] - top_rgb[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

def draw_diagonal_gradient(draw, w, h, tl_rgb, br_rgb):
    for y in range(h):
        for x in range(w):
            t = (x / w + y / h) / 2
            r = int(tl_rgb[0] + (br_rgb[0] - tl_rgb[0]) * t)
            g = int(tl_rgb[1] + (br_rgb[1] - tl_rgb[1]) * t)
            b = int(tl_rgb[2] + (br_rgb[2] - tl_rgb[2]) * t)
            draw.point((x, y), fill=(r, g, b, 255))

def draw_radial_glow(img, cx, cy, radius, color_rgb, max_alpha=80):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    steps = 40
    for i in range(steps, 0, -1):
        r_size = int(radius * i / steps)
        alpha = int(max_alpha * (1 - i / steps))
        d.ellipse([cx - r_size, cy - r_size, cx + r_size, cy + r_size],
                  fill=(*color_rgb, alpha))
    img.alpha_composite(overlay)

def centered_text(draw, y, text, fnt, fill, w=1080):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) / 2, y), text, font=fnt, fill=fill)

# ─── POST 1: Brand Awareness / Intro ────────────────────────────────────────

def post1_awareness():
    W, H = 1080, 1080
    img = Image.new("RGBA", (W, H), (11, 11, 20, 255))
    draw = ImageDraw.Draw(img)

    # Dark navy background with diagonal gradient overlay
    draw_vertical_gradient(draw, W, H, (11, 11, 20), (25, 18, 50))

    # Radial glow — violet at center
    draw_radial_glow(img, 540, 480, 520, (123, 103, 209), max_alpha=70)

    draw = ImageDraw.Draw(img)

    # ── Decorative geometric lines (circuit/tech feel) ──
    line_color = (123, 103, 209, 40)
    # Horizontal faint lines
    for y_pos in [220, 440, 660, 820]:
        draw.line([(60, y_pos), (1020, y_pos)], fill=line_color, width=1)
    # Corner accent lines top-left
    draw.line([(60, 60), (200, 60)], fill=(123, 103, 209, 100), width=2)
    draw.line([(60, 60), (60, 180)], fill=(123, 103, 209, 100), width=2)
    # Corner accent lines bottom-right
    draw.line([(880, 1020), (1020, 1020)], fill=(65, 150, 230, 100), width=2)
    draw.line([(1020, 860), (1020, 1020)], fill=(65, 150, 230, 100), width=2)

    # ── Logo badge ──
    # Hexagon-ish pill for brand mark
    draw.rounded_rectangle([420, 130, 660, 210], radius=16,
                            fill=(123, 103, 209, 200), outline=(255, 255, 255, 60), width=1)
    brand_f = font(32, "bold")
    centered_text(draw, 152, "IGEN VERITAS", brand_f, (255, 255, 255, 255))

    # ── Tagline badge / accent pill ──
    draw.rounded_rectangle([300, 250, 780, 310], radius=30,
                            fill=(65, 150, 230, 30), outline=(65, 150, 230, 80), width=1)
    tag_f = font(26, "regular")
    centered_text(draw, 265, "AI · Web · Mobile · Automation", tag_f, (65, 150, 230, 220))

    # ── Main headline ──
    h1 = font(100, "bold")
    h2 = font(96, "bold")

    # "Powering" in white
    centered_text(draw, 360, "Powering", h1, (255, 255, 255, 255))
    # "the Future" in violet accent
    centered_text(draw, 470, "the Future.", h1, (123, 103, 209, 255))

    # ── Subtext ──
    sub_f = font(36, "regular")
    centered_text(draw, 610, "One smart business at a time.", sub_f, (180, 180, 200, 220))

    # ── Separator line ──
    draw.line([(340, 680), (740, 680)], fill=(123, 103, 209, 120), width=2)

    # ── Value pills row ──
    pills = ["AI Chatbot", "Web Dev", "Mobile App"]
    pill_w, pill_h = 220, 56
    gap = 40
    total = len(pills) * pill_w + (len(pills) - 1) * gap
    px_start = (W - total) // 2
    pf = font(26, "bold")
    for i, label in enumerate(pills):
        px = px_start + i * (pill_w + gap)
        py = 720
        draw.rounded_rectangle([px, py, px + pill_w, py + pill_h], radius=28,
                                fill=(123, 103, 209, 160), outline=(255, 255, 255, 80), width=1)
        bbox = draw.textbbox((0, 0), label, font=pf)
        tw = bbox[2] - bbox[0]
        draw.text((px + (pill_w - tw) // 2, py + 14), label, font=pf, fill=(255, 255, 255, 255))

    # ── CTA bottom ──
    draw.rounded_rectangle([330, 820, 750, 890], radius=35,
                            fill=(123, 103, 209, 255), outline=(255, 255, 255, 30), width=1)
    cta_f = font(30, "bold")
    centered_text(draw, 839, "DM 'INFO' sekarang →", cta_f, (255, 255, 255, 255))

    # ── Website footer ──
    web_f = font(24, "regular")
    centered_text(draw, 950, "igenveritas.com  ·  +60 17 310 3966", web_f, (107, 114, 128, 200))

    out = os.path.join(OUT_DIR, "20260501_awareness_brand_intro.png")
    img.save(out, "PNG")
    print(f"Saved: {out}")


# ─── POST 2: Pain Point ───────────────────────────────────────────────────────

def post2_pain():
    W, H = 1080, 1080
    img = Image.new("RGBA", (W, H), (11, 11, 20, 255))
    draw = ImageDraw.Draw(img)

    # Dark navy base
    draw_vertical_gradient(draw, W, H, (8, 8, 16), (18, 12, 36))

    # Soft violet glow upper-left (competitor's side)
    draw_radial_glow(img, 200, 350, 400, (123, 103, 209), max_alpha=55)
    # Warm red glow upper-right (your business side — off/dark)
    draw_radial_glow(img, 880, 350, 380, (180, 40, 40), max_alpha=35)

    draw = ImageDraw.Draw(img)

    # Corner accents
    draw.line([(60, 60), (200, 60)], fill=(123, 103, 209, 120), width=2)
    draw.line([(60, 60), (60, 180)], fill=(123, 103, 209, 120), width=2)
    draw.line([(880, 1020), (1020, 1020)], fill=(65, 150, 230, 100), width=2)
    draw.line([(1020, 860), (1020, 1020)], fill=(65, 150, 230, 100), width=2)

    # Brand label
    bf = font(28, "bold")
    draw.text((60, 70), "IGEN VERITAS", font=bf, fill=(255, 255, 255, 180))
    wf = font(22, "regular")
    draw.text((60, 108), "igenveritas.com", font=wf, fill=(107, 114, 128, 180))

    # ── Main headline — 2 lines ──
    h1 = font(98, "bold")
    h2 = font(94, "bold")

    # Line 1: "Your business" white
    centered_text(draw, 190, "Your business", h1, (255, 255, 255, 255))
    # Line 2: "closes at 6PM." red accent
    centered_text(draw, 300, "closes at 6PM.", h2, (220, 60, 60, 255))

    # ── Divider ──
    draw.line([(200, 420), (880, 420)], fill=(255, 255, 255, 20), width=1)

    # ── Split scenario cards ──
    # LEFT card — "Your Business" (dark/off)
    lx1, ly1, lx2, ly2 = 60, 450, 500, 750
    draw.rounded_rectangle([lx1, ly1, lx2, ly2], radius=20,
                            fill=(255, 255, 255, 6), outline=(180, 40, 40, 80), width=1)
    label_f = font(24, "bold")
    draw.text((lx1 + 24, ly1 + 20), "YOUR BUSINESS", font=label_f, fill=(180, 40, 40, 220))

    # Clock — left card
    clock_f = font(52, "bold")
    clock_text = "6:00 PM"
    cb = draw.textbbox((0, 0), clock_text, font=clock_f)
    tw = cb[2] - cb[0]
    draw.text((lx1 + (lx2 - lx1 - tw) // 2, ly1 + 70), clock_text, font=clock_f, fill=(220, 60, 60, 255))

    closed_f = font(28, "bold")
    c1 = "Kedai tutup."
    c2 = "WhatsApp: offline."
    c3 = "0 leads captured."
    for i, line in enumerate([c1, c2, c3]):
        cb2 = draw.textbbox((0, 0), line, font=closed_f)
        tw2 = cb2[2] - cb2[0]
        draw.text((lx1 + (lx2 - lx1 - tw2) // 2, ly1 + 165 + i * 55), line,
                  font=closed_f, fill=(255, 180, 180, 230))

    # RIGHT card — "Competitor" (glowing/active)
    rx1, ry1, rx2, ry2 = 580, 450, 1020, 750
    draw.rounded_rectangle([rx1, ry1, rx2, ry2], radius=20,
                            fill=(123, 103, 209, 20), outline=(123, 103, 209, 120), width=1)
    draw.text((rx1 + 24, ry1 + 20), "COMPETITOR", font=label_f, fill=(123, 103, 209, 220))

    clock_text2 = "2:47 AM"
    cb3 = draw.textbbox((0, 0), clock_text2, font=clock_f)
    tw3 = cb3[2] - cb3[0]
    draw.text((rx1 + (rx2 - rx1 - tw3) // 2, ry1 + 70), clock_text2,
              font=clock_f, fill=(123, 103, 209, 255))

    active_lines = ["Bot aktif 24/7.", "3 leads captured.", "Appointment booked. ✓"]
    for i, line in enumerate(active_lines):
        ab = draw.textbbox((0, 0), line, font=closed_f)
        tw4 = ab[2] - ab[0]
        draw.text((rx1 + (rx2 - rx1 - tw4) // 2, ry1 + 165 + i * 55), line,
                  font=closed_f, fill=(210, 220, 255, 245))

    # ── VS divider ──
    vs_f = font(52, "bold")
    vs_b = draw.textbbox((0, 0), "VS", font=vs_f)
    vw = vs_b[2] - vs_b[0]
    draw.text(((W - vw) // 2, 560), "VS", font=vs_f, fill=(255, 255, 255, 80))

    # ── Stat card ──
    draw.rounded_rectangle([160, 790, 920, 890], radius=20,
                            fill=(255, 255, 255, 6), outline=(255, 255, 255, 20), width=1)
    stat_f = font(30, "bold")
    stat_text = "Businesses lose up to 40% of leads after hours."
    sb = draw.textbbox((0, 0), stat_text, font=stat_f)
    stw = sb[2] - sb[0]
    draw.text(((W - stw) // 2, 828), stat_text, font=stat_f, fill=(200, 200, 220, 220))

    # ── CTA pill ──
    draw.rounded_rectangle([320, 920, 760, 990], radius=35,
                            fill=(123, 103, 209, 255))
    cta_f = font(30, "bold")
    centered_text(draw, 940, "Automate your business →", cta_f, (255, 255, 255, 255))

    out = os.path.join(OUT_DIR, "20260503_pain_business_closes_6pm.png")
    img.save(out, "PNG")
    print(f"Saved: {out}")


# ─── Run ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Generating Week 1 visuals...")
    post1_awareness()
    post2_pain()
    print("Done.")
