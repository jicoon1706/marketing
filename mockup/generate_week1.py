from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Brand colors
VIOLET      = (123, 103, 209)
PURPLE      = (138, 93, 204)
BLUE_MID    = (72, 143, 227)
BLUE_BRIGHT = (65, 150, 230)
DARK_NAVY   = (11, 11, 20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
RED_ACCENT  = (239, 68, 68)

def get_font(size, weight="regular"):
    font_map = {
        "black":   "C:/Windows/Fonts/segoeuib.ttf",
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def draw_gradient_bg(draw, w, h, color_top, color_bottom):
    for y in range(h):
        t = y / h
        r = int(color_top[0] + (color_bottom[0] - color_top[0]) * t)
        g = int(color_top[1] + (color_bottom[1] - color_top[1]) * t)
        b = int(color_top[2] + (color_bottom[2] - color_top[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

def draw_diagonal_gradient(draw, w, h, color_tl, color_br):
    for y in range(h):
        for x in range(w):
            t = (x + y) / (w + h)
            r = int(color_tl[0] + (color_br[0] - color_tl[0]) * t)
            g = int(color_tl[1] + (color_br[1] - color_tl[1]) * t)
            b = int(color_tl[2] + (color_br[2] - color_tl[2]) * t)
            draw.point((x, y), fill=(r, g, b, 255))

def draw_radial_glow(img, cx, cy, radius, color, alpha_max=60):
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(glow)
    steps = 30
    for i in range(steps, 0, -1):
        r_i = int(radius * i / steps)
        a = int(alpha_max * (steps - i) / steps)
        d.ellipse([cx - r_i, cy - r_i, cx + r_i, cy + r_i],
                  fill=(color[0], color[1], color[2], a))
    img.alpha_composite(glow)

def draw_glass_card(draw, x1, y1, x2, y2, radius=24):
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius,
                            fill=(255, 255, 255, 13),
                            outline=(255, 255, 255, 40))

def draw_brand_badge(draw, img, x, y):
    badge_w, badge_h = 340, 52
    draw.rounded_rectangle([x, y, x + badge_w, y + badge_h],
                            radius=26,
                            fill=(255, 255, 255, 220),
                            outline=(255, 255, 255, 255))
    dot_x = x + 22
    dot_y = y + badge_h // 2
    draw.ellipse([dot_x - 10, dot_y - 10, dot_x + 10, dot_y + 10],
                 fill=VIOLET + (255,))
    font = get_font(18, "bold")
    draw.text((dot_x + 18, dot_y), "IGEN VERITAS", fill=(*DARK_NAVY, 255),
              font=font, anchor="lm")

def draw_divider_line(draw, x1, y, x2, alpha=60):
    draw.line([(x1, y), (x2, y)], fill=(255, 255, 255, alpha), width=1)


# ─────────────────────────────────────────────
# CB-001: Instagram Awareness — Brand Intro
# ─────────────────────────────────────────────
def generate_cb001():
    img = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 255))
    draw = ImageDraw.Draw(img)

    # Subtle gradient from center-left
    draw_radial_glow(img, 200, 540, 600, VIOLET, alpha_max=70)
    draw_radial_glow(img, 900, 200, 400, BLUE_MID, alpha_max=40)

    # Top branding bar
    font_small = get_font(22, "regular")
    draw.text((60, 58), "IGEN VERITAS", fill=(*WHITE, 200), font=font_small)
    draw.text((60, 84), "igenveritas.com", fill=(*BODY_GRAY, 200), font=font_small)

    # Decorative thin horizontal line under branding
    draw_divider_line(draw, 60, 118, 1020, alpha=40)

    # Central logo mark (geometric VI monogram)
    cx, cy = 540, 400
    # Outer ring
    draw.ellipse([cx - 110, cy - 110, cx + 110, cy + 110],
                 outline=(*VIOLET, 180), width=2)
    draw.ellipse([cx - 90, cy - 90, cx + 90, cy + 90],
                 fill=(255, 255, 255, 8), outline=(255, 255, 255, 30), width=1)
    # Inner diamond/star shape
    pts = [
        (cx, cy - 60),
        (cx + 52, cy),
        (cx, cy + 60),
        (cx - 52, cy),
    ]
    draw.polygon(pts, fill=(*VIOLET, 200))
    # Inner highlight
    inner_pts = [
        (cx, cy - 30),
        (cx + 26, cy),
        (cx, cy + 30),
        (cx - 26, cy),
    ]
    draw.polygon(inner_pts, fill=(*BLUE_BRIGHT, 180))
    # Company initial in center
    font_init = get_font(44, "bold")
    draw.text((cx, cy), "IV", fill=(*WHITE, 255), font=font_init, anchor="mm")

    # Decorative orbit dots around logo
    import math
    for angle_deg in range(0, 360, 45):
        angle_rad = math.radians(angle_deg)
        ox = cx + int(130 * math.cos(angle_rad))
        oy = cy + int(130 * math.sin(angle_rad))
        draw.ellipse([ox - 4, oy - 4, ox + 4, oy + 4],
                     fill=(*VIOLET, 120))

    # Main headline
    font_h1 = get_font(74, "bold")
    font_h2 = get_font(74, "bold")
    font_accent = get_font(74, "bold")
    draw.text((540, 580), "Powering the", fill=(*WHITE, 255),
              font=font_h1, anchor="mm")
    draw.text((540, 664), "future", fill=(*VIOLET, 255),
              font=font_accent, anchor="mm")

    # Divider
    draw_divider_line(draw, 240, 720, 840)

    # Tagline
    font_tag = get_font(28, "regular")
    draw.text((540, 760), "one smart business at a time.", fill=(*BODY_GRAY, 255),
              font=font_tag, anchor="mm")

    # Bottom CTA pill
    pill_x1, pill_y1, pill_x2, pill_y2 = 370, 840, 710, 896
    draw.rounded_rectangle([pill_x1, pill_y1, pill_x2, pill_y2],
                            radius=28,
                            fill=(*VIOLET, 255))
    font_cta = get_font(26, "bold")
    draw.text((540, 868), "Learn More →", fill=(*WHITE, 255),
              font=font_cta, anchor="mm")

    # Bottom watermark
    font_wm = get_font(20, "light")
    draw.text((540, 1030), "igenveritas.com  |  AI · Web · Mobile", fill=(*BODY_GRAY, 180),
              font=font_wm, anchor="mm")

    out_path = os.path.join(OUTPUT_DIR, "CB-001_instagram_awareness_brand_intro.png")
    img.save(out_path, "PNG")
    print(f"Saved: {out_path}")


# ─────────────────────────────────────────────
# CB-002: LinkedIn Awareness — Brand Graphic
# ─────────────────────────────────────────────
def generate_cb002():
    img = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 255))
    draw = ImageDraw.Draw(img)

    # Diagonal gradient top-right to bottom-left
    # Manually do a simpler left-to-right gradient with glow
    draw_gradient_bg(draw, 1080, 1080, DARK_NAVY, (18, 16, 38))
    draw_radial_glow(img, 900, 180, 500, VIOLET, alpha_max=55)
    draw_radial_glow(img, 200, 900, 400, BLUE_MID, alpha_max=35)

    # Top bar — company name left, platform right
    font_brand = get_font(24, "bold")
    font_small = get_font(20, "regular")
    draw.text((60, 58), "IGEN VERITAS", fill=(*WHITE, 230), font=font_brand)
    draw.text((60, 88), "Thought Leadership  ·  April 2026", fill=(*BODY_GRAY, 200), font=font_small)
    draw_divider_line(draw, 60, 126, 1020, alpha=35)

    # LinkedIn pill badge top-right
    draw.rounded_rectangle([880, 44, 1020, 82], radius=19,
                            fill=(*BLUE_MID, 40), outline=(*BLUE_MID, 120))
    font_li = get_font(18, "bold")
    draw.text((950, 63), "LinkedIn", fill=(*BLUE_BRIGHT, 255), font=font_li, anchor="mm")

    # Large headline
    font_h1 = get_font(66, "bold")
    font_h2 = get_font(66, "bold")
    lines = [
        ("Malaysian SMEs", WHITE),
        ("deserve the same", WHITE),
        ("tech as big companies.", VIOLET),
    ]
    y_start = 220
    for line_text, color in lines:
        draw.text((540, y_start), line_text, fill=(*color, 255),
                  font=font_h1, anchor="mm")
        y_start += 86

    draw_divider_line(draw, 60, 510, 1020, alpha=30)

    # Three stat/value cards in a row
    cards = [
        ("RM 500", "Chatbot Setup", "Entry-level"),
        ("24/7", "Always On", "No off-hours"),
        ("< 3s", "Response Time", "Instant replies"),
    ]
    card_w, card_h = 280, 160
    card_y = 560
    card_starts = [70, 400, 730]
    for i, (stat, label, sub) in enumerate(cards):
        cx = card_starts[i]
        draw_glass_card(draw, cx, card_y, cx + card_w, card_y + card_h, radius=20)
        font_stat = get_font(48, "bold")
        font_lbl = get_font(20, "bold")
        font_sub = get_font(17, "regular")
        draw.text((cx + card_w // 2, card_y + 52), stat,
                  fill=(*VIOLET, 255), font=font_stat, anchor="mm")
        draw.text((cx + card_w // 2, card_y + 96), label,
                  fill=(*WHITE, 230), font=font_lbl, anchor="mm")
        draw.text((cx + card_w // 2, card_y + 126), sub,
                  fill=(*BODY_GRAY, 200), font=font_sub, anchor="mm")

    # Pull quote / subtext
    font_quote = get_font(30, "regular")
    draw.text((540, 800),
              "We started IGEN VERITAS because every SME",
              fill=(*BODY_GRAY, 220), font=font_quote, anchor="mm")
    draw.text((540, 842),
              "deserves intelligent, affordable technology.",
              fill=(*BODY_GRAY, 220), font=font_quote, anchor="mm")

    draw_divider_line(draw, 60, 900, 1020, alpha=30)

    # Bottom CTA row
    font_cta = get_font(24, "bold")
    font_url = get_font(22, "regular")
    draw.text((60, 938), "🔗 DM us to learn more", fill=(*WHITE, 210), font=font_cta)
    draw.text((60, 978), "igenveritas.com  ·  info@igenveritas.com  ·  +60 17 310 3966",
              fill=(*BODY_GRAY, 180), font=font_url)

    out_path = os.path.join(OUTPUT_DIR, "CB-002_linkedin_awareness_brand_graphic.png")
    img.save(out_path, "PNG")
    print(f"Saved: {out_path}")


# ─────────────────────────────────────────────
# CB-003: Instagram Pain — 6PM Competitor Post
# ─────────────────────────────────────────────
def generate_cb003():
    img = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 255))
    draw = ImageDraw.Draw(img)

    # Glow from center, red-tinted on left (closed), violet on right (open)
    draw_radial_glow(img, 160, 540, 380, (200, 40, 40), alpha_max=45)
    draw_radial_glow(img, 920, 540, 380, VIOLET, alpha_max=55)

    # Top branding
    font_brand = get_font(22, "regular")
    draw.text((60, 54), "IGEN VERITAS", fill=(*WHITE, 180), font=font_brand)
    draw.text((1020, 54), "igenveritas.com", fill=(*BODY_GRAY, 160),
              font=get_font(20, "regular"), anchor="ra")
    draw_divider_line(draw, 60, 90, 1020, alpha=35)

    # SPLIT PANEL — left: closed, right: chatbot
    mid_x = 540

    # Vertical divider between panels
    draw.line([(mid_x, 130), (mid_x, 760)], fill=(255, 255, 255, 30), width=1)

    # LEFT PANEL — CLOSED OFFICE
    left_cx = 270

    # Dark overlay on left half
    draw.rectangle([0, 0, mid_x, 1080], fill=(0, 0, 0, 60))

    # Moon/night icon
    draw.ellipse([left_cx - 44, 160, left_cx + 44, 248],
                 fill=(200, 200, 220, 80))
    draw.ellipse([left_cx - 28, 155, left_cx + 60, 243],
                 fill=(*DARK_NAVY, 240))

    # Office building silhouette (simple rectangles)
    # Building body
    draw.rectangle([left_cx - 80, 310, left_cx + 80, 560],
                   fill=(30, 28, 50, 200))
    # Windows — dark/off
    for row in range(3):
        for col in range(3):
            wx = left_cx - 55 + col * 46
            wy = 328 + row * 62
            draw.rectangle([wx, wy, wx + 28, wy + 36],
                            fill=(22, 20, 35, 255))

    # "CLOSED" sign
    draw.rounded_rectangle([left_cx - 68, 572, left_cx + 68, 616],
                            radius=8, fill=(180, 40, 40, 200))
    font_sign = get_font(24, "bold")
    draw.text((left_cx, 594), "CLOSED", fill=(*WHITE, 255),
              font=font_sign, anchor="mm")

    # Time label
    font_time = get_font(28, "bold")
    draw.text((left_cx, 650), "6:00 PM", fill=(*WHITE, 200),
              font=font_time, anchor="mm")
    font_sub_l = get_font(20, "regular")
    draw.text((left_cx, 686), "Your business is offline", fill=(*BODY_GRAY, 200),
              font=font_sub_l, anchor="mm")

    # RIGHT PANEL — CHATBOT ACTIVE
    right_cx = 810

    # Subtle glow behind phone
    draw_radial_glow(img, right_cx, 380, 260, VIOLET, alpha_max=50)

    # Phone frame
    ph_x1, ph_y1, ph_x2, ph_y2 = right_cx - 100, 155, right_cx + 100, 570
    draw.rounded_rectangle([ph_x1, ph_y1, ph_x2, ph_y2],
                            radius=22, fill=(25, 22, 45, 240),
                            outline=(*VIOLET, 180), width=2)
    # Phone notch
    draw.rounded_rectangle([right_cx - 28, ph_y1 + 8, right_cx + 28, ph_y1 + 22],
                            radius=7, fill=(15, 12, 30, 255))

    # WhatsApp-style header bar inside phone
    draw.rectangle([ph_x1 + 2, ph_y1 + 28, ph_x2 - 2, ph_y1 + 72],
                   fill=(18, 140, 86, 220))
    draw.ellipse([ph_x1 + 10, ph_y1 + 34, ph_x1 + 46, ph_y1 + 70],
                 fill=(255, 255, 255, 80))
    font_chat_hdr = get_font(16, "bold")
    draw.text((ph_x1 + 55, ph_y1 + 44), "IGEN Bot", fill=(*WHITE, 255),
              font=font_chat_hdr)
    draw.text((ph_x1 + 55, ph_y1 + 62), "● Online", fill=(144, 238, 144, 255),
              font=get_font(13, "regular"))

    # Chat bubbles inside phone
    bubbles = [
        ("customer", "Hi, info pasal chatbot?"),
        ("bot",      "Hi! Chatbot kami dari"),
        ("bot",      "RM500 sahaja. 24/7 aktif!"),
        ("customer", "Best! Boleh demo?"),
        ("bot",      "Ya! DM kami sekarang ✓✓"),
    ]
    bub_y = ph_y1 + 85
    for sender, text in bubbles:
        font_bub = get_font(13, "regular")
        tw = draw.textlength(text, font=font_bub)
        bub_w = min(int(tw) + 20, 150)
        if sender == "customer":
            bx = ph_x1 + 8
            fill = (50, 50, 80, 220)
        else:
            bx = ph_x2 - 8 - bub_w
            fill = (*VIOLET, 200)
        draw.rounded_rectangle([bx, bub_y, bx + bub_w, bub_y + 26],
                                radius=8, fill=fill)
        draw.text((bx + 10, bub_y + 13), text, fill=(*WHITE, 235),
                  font=font_bub, anchor="lm")
        bub_y += 36

    # Active indicator at bottom of phone
    draw.ellipse([right_cx - 6, ph_y2 - 20, right_cx + 6, ph_y2 - 8],
                 fill=(144, 238, 144, 255))

    # Time label right panel
    font_time_r = get_font(28, "bold")
    draw.text((right_cx, 612), "2:47 AM", fill=(*VIOLET, 230),
              font=font_time_r, anchor="mm")
    draw.text((right_cx, 650), "Your competitor is live", fill=(*WHITE, 200),
              font=get_font(20, "regular"), anchor="mm")

    # MAIN HEADLINE
    draw_divider_line(draw, 60, 770, 1020, alpha=35)
    font_headline = get_font(60, "bold")
    draw.text((540, 832),
              "Your business closes at 6PM.", fill=(*WHITE, 255),
              font=font_headline, anchor="mm")
    font_headline2 = get_font(60, "bold")
    draw.text((540, 900),
              "Your competitor's doesn't.", fill=(*VIOLET, 255),
              font=font_headline2, anchor="mm")

    # Bottom CTA pill
    pill_x1, pill_y1, pill_x2, pill_y2 = 340, 940, 740, 994
    draw.rounded_rectangle([pill_x1, pill_y1, pill_x2, pill_y2],
                            radius=27, fill=(*VIOLET, 255))
    font_cta = get_font(24, "bold")
    draw.text((540, 967), "DM 'INFO' sekarang →", fill=(*WHITE, 255),
              font=font_cta, anchor="mm")

    out_path = os.path.join(OUTPUT_DIR, "CB-003_instagram_pain_6pm_competitor.png")
    img.save(out_path, "PNG")
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    print("Generating Week 1 social media mockups...")
    generate_cb001()
    generate_cb002()
    generate_cb003()
    print("Done. All 3 posts saved to mockup/")
