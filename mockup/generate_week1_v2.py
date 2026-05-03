"""
IGEN VERITAS — Week 1 Social Media Mockups (v2)
Posts: CB-001 (Instagram Awareness), CB-002 (LinkedIn Awareness), CB-003 (Instagram Pain)
Metrics drawn from monthly-report-template.md proof points.
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Brand palette ────────────────────────────────────────────
VIOLET      = (123, 103, 209)
PURPLE      = (138,  93, 204)
BLUE_MID    = ( 72, 143, 227)
BLUE_BRIGHT = ( 65, 150, 230)
DARK_NAVY   = ( 11,  11,  20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)
GREEN       = ( 34, 197, 94)
RED_SOFT    = (239,  68,  68)

def font(size, w="regular"):
    paths = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
        "italic":  "C:/Windows/Fonts/segoeuii.ttf",
    }
    p = paths.get(w, paths["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

def v_gradient(draw, w, h, top, bot):
    for y in range(h):
        t = y / h
        r = int(top[0] + (bot[0] - top[0]) * t)
        g = int(top[1] + (bot[1] - top[1]) * t)
        b = int(top[2] + (bot[2] - top[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

def d_gradient(draw, w, h, tl, br):
    """Diagonal gradient (sampled every 2px for speed)."""
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            t = (x + y) / (w + h)
            r = int(tl[0] + (br[0] - tl[0]) * t)
            g = int(tl[1] + (br[1] - tl[1]) * t)
            b = int(tl[2] + (br[2] - tl[2]) * t)
            draw.rectangle([x, y, x + 1, y + 1], fill=(r, g, b, 255))

def glow(img, cx, cy, radius, color, alpha_max=60):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    steps = 28
    for i in range(steps, 0, -1):
        ri = int(radius * i / steps)
        a  = int(alpha_max * (steps - i) / steps)
        d.ellipse([cx - ri, cy - ri, cx + ri, cy + ri],
                  fill=(*color, a))
    img.alpha_composite(layer)

def glass_card(draw, x1, y1, x2, y2, r=20, alpha_fill=13, alpha_border=50):
    draw.rounded_rectangle([x1, y1, x2, y2], radius=r,
                            fill=(255, 255, 255, alpha_fill),
                            outline=(255, 255, 255, alpha_border))

def pill(draw, cx, cy, text, txt_font, bg, txt_color=WHITE, pad_x=28, pad_y=14):
    tw = int(draw.textlength(text, font=txt_font))
    x1, y1 = cx - tw // 2 - pad_x, cy - pad_y
    x2, y2 = cx + tw // 2 + pad_x, cy + pad_y
    draw.rounded_rectangle([x1, y1, x2, y2], radius=y2 - y1,
                            fill=(*bg, 255))
    draw.text((cx, cy), text, fill=(*txt_color, 255),
              font=txt_font, anchor="mm")

def rule(draw, x1, y, x2, a=40):
    draw.line([(x1, y), (x2, y)], fill=(255, 255, 255, a), width=1)

def branding_top(draw, left_label="IGEN VERITAS", right_label="igenveritas.com"):
    draw.text((60, 52), left_label, fill=(*WHITE, 200), font=font(22, "bold"))
    draw.text((1020, 52), right_label, fill=(*BODY_GRAY, 180),
              font=font(20, "regular"), anchor="ra")
    rule(draw, 60, 90, 1020, a=35)

def dot_accent(draw, cx, cy, color=VIOLET, r=5):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, 255))


# ════════════════════════════════════════════════════════════
#  CB-001  Instagram 1080×1080 — AWARENESS / Brand Intro
#  Template H-style: dark navy, central logo mark, stat strip
#  Metrics from report: conversations, leads captured, bookings
# ════════════════════════════════════════════════════════════
def cb001():
    img = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 255))
    d   = ImageDraw.Draw(img)

    v_gradient(d, 1080, 1080, DARK_NAVY, (16, 12, 32))
    glow(img,  200, 500, 550, VIOLET,    alpha_max=60)
    glow(img,  950, 200, 380, BLUE_MID,  alpha_max=38)
    glow(img,  540, 1080, 300, PURPLE,   alpha_max=30)

    branding_top(d)

    # ── Logo mark ───────────────────────────────────────────
    cx, cy = 540, 370
    # Outer glow ring
    for ri, a in [(130, 18), (110, 28), (92, 12)]:
        d.ellipse([cx - ri, cy - ri, cx + ri, cy + ri],
                  fill=(123, 103, 209, a))
    # Ring border
    d.ellipse([cx - 92, cy - 92, cx + 92, cy + 92],
              outline=(*VIOLET, 200), width=2)
    # Diamond
    pts = [(cx, cy - 58), (cx + 50, cy), (cx, cy + 58), (cx - 50, cy)]
    d.polygon(pts, fill=(*PURPLE, 230))
    inner = [(cx, cy - 28), (cx + 24, cy), (cx, cy + 28), (cx - 24, cy)]
    d.polygon(inner, fill=(*BLUE_BRIGHT, 210))
    d.text((cx, cy), "IV", fill=(*WHITE, 255), font=font(42, "bold"), anchor="mm")

    # Orbit dots
    for deg in range(0, 360, 45):
        ang = math.radians(deg)
        ox = cx + int(120 * math.cos(ang))
        oy = cy + int(120 * math.sin(ang))
        dot_accent(d, ox, oy, VIOLET if deg % 90 == 0 else BLUE_MID, r=4)

    # ── Headline ────────────────────────────────────────────
    d.text((540, 512), "Powering the",   fill=(*WHITE, 255),  font=font(76, "bold"), anchor="mm")
    d.text((540, 600), "future,",        fill=(*VIOLET, 255), font=font(76, "bold"), anchor="mm")
    d.text((540, 686), "intelligently.", fill=(*WHITE, 200),  font=font(52, "regular"), anchor="mm")

    rule(d, 180, 730, 900, a=45)

    # ── Tagline ─────────────────────────────────────────────
    d.text((540, 766),
           "AI · Web · Mobile for Malaysian SMEs",
           fill=(*BODY_GRAY, 210), font=font(26, "regular"), anchor="mm")

    # ── Metric strip (from report template fields) ──────────
    # Three glassmorphism stat chips
    metrics = [
        ("1,200+", "Conversations\nHandled"),
        ("340",    "Leads\nCaptured"),
        ("88",     "Bookings\nMade"),
    ]
    chip_w, chip_h = 256, 118
    starts_x = [80, 412, 744]
    chip_y = 826

    for i, (val, lbl) in enumerate(metrics):
        x1 = starts_x[i]
        glass_card(d, x1, chip_y, x1 + chip_w, chip_y + chip_h, r=18, alpha_fill=16, alpha_border=55)
        # coloured accent bar top of chip
        bar_color = [VIOLET, BLUE_MID, GREEN][i]
        d.rounded_rectangle([x1 + 20, chip_y + 10, x1 + chip_w - 20, chip_y + 14],
                             radius=2, fill=(*bar_color, 200))
        d.text((x1 + chip_w // 2, chip_y + 44), val,
               fill=(*WHITE, 255), font=font(38, "bold"), anchor="mm")
        for j, line in enumerate(lbl.split("\n")):
            d.text((x1 + chip_w // 2, chip_y + 76 + j * 22), line,
                   fill=(*BODY_GRAY, 210), font=font(17, "regular"), anchor="mm")

    # ── Bottom CTA pill ─────────────────────────────────────
    pill(d, 540, 990, "DM 'INFO' sekarang  →", font(24, "bold"), VIOLET)

    img.save(os.path.join(OUTPUT_DIR, "CB-001_instagram_awareness_brand_intro.png"), "PNG")
    print("✓  CB-001 saved")


# ════════════════════════════════════════════════════════════
#  CB-002  LinkedIn 1080×1080 — AWARENESS / Thought Leadership
#  Template B-style: diagonal gradient, feature pills, report KPIs
# ════════════════════════════════════════════════════════════
def cb002():
    img = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 255))
    d   = ImageDraw.Draw(img)

    d_gradient(d, 1080, 1080, VIOLET, BLUE_BRIGHT)

    # Dark overlay for readability
    overlay = Image.new("RGBA", (1080, 1080), (11, 11, 20, 120))
    img.alpha_composite(overlay)
    d = ImageDraw.Draw(img)

    glow(img, 900, 120, 420, BLUE_MID, alpha_max=50)
    glow(img, 100, 960, 320, PURPLE,   alpha_max=40)

    # ── Top bar ──────────────────────────────────────────────
    branding_top(d, right_label="Thought Leadership")
    # LinkedIn badge
    d.rounded_rectangle([874, 40, 1020, 78], radius=19,
                         fill=(*BLUE_MID, 50), outline=(*BLUE_BRIGHT, 150))
    d.text((947, 59), "LinkedIn", fill=(*WHITE, 255), font=font(18, "bold"), anchor="mm")

    # ── Headline ─────────────────────────────────────────────
    headline_lines = [
        ("Malaysian SMEs deserve",  WHITE,   62, 176),
        ("the same tech as",         WHITE,   62, 250),
        ("big companies.",           VIOLET,  62, 324),   # accent
    ]
    for txt, col, sz, y in headline_lines:
        d.text((540, y), txt, fill=(*col, 255), font=font(sz, "bold"), anchor="mm")

    rule(d, 60, 380, 1020, a=50)

    # ── Sub-copy ─────────────────────────────────────────────
    d.text((540, 420),
           "We built IGEN VERITAS so every SME owner can",
           fill=(*WHITE, 210), font=font(28, "regular"), anchor="mm")
    d.text((540, 458),
           "automate, grow, and compete — without a full tech team.",
           fill=(*WHITE, 210), font=font(28, "regular"), anchor="mm")

    rule(d, 60, 496, 1020, a=30)

    # ── Report-style KPI grid (4 cards, 2×2) ─────────────────
    # Mirrors monthly report: Conversations / Leads / Bookings / Estimated Revenue
    kpis = [
        (VIOLET,    "1,200+",   "Total Conversations",    "This month"),
        (BLUE_MID,  "340",      "Leads Captured",         "Across all clients"),
        (GREEN,     "88",       "Bookings Made",          "Via chatbot alone"),
        (PURPLE,    "RM 4,800", "Monthly Recurring Rev.", "At 20 Growth clients"),
    ]
    card_w, card_h = 446, 148
    positions = [(60, 520), (574, 520), (60, 686), (574, 686)]

    for (x1, y1), (accent, val, lbl, sub) in zip(positions, kpis):
        glass_card(d, x1, y1, x1 + card_w, y1 + card_h, r=18,
                   alpha_fill=14, alpha_border=60)
        # Left accent bar
        d.rounded_rectangle([x1 + 16, y1 + 18, x1 + 20, y1 + card_h - 18],
                             radius=2, fill=(*accent, 220))
        # Value
        d.text((x1 + 50, y1 + 46), val,
               fill=(*WHITE, 255), font=font(40, "bold"), anchor="lm")
        # Label
        d.text((x1 + 50, y1 + 86), lbl,
               fill=(*WHITE, 210), font=font(22, "bold"), anchor="lm")
        # Sub
        d.text((x1 + 50, y1 + 116), sub,
               fill=(*BODY_GRAY, 200), font=font(17, "regular"), anchor="lm")

    rule(d, 60, 854, 1020, a=35)

    # ── Contact strip ────────────────────────────────────────
    contact_items = [
        ("🔗 igenveritas.com", 60),
        ("✉  info@igenveritas.com", 380),
        ("📞  +60 17-310 3966", 740),
    ]
    for txt, x in contact_items:
        d.text((x, 900), txt, fill=(*WHITE, 180), font=font(21, "regular"))

    rule(d, 60, 928, 1020, a=25)

    # ── CTA ──────────────────────────────────────────────────
    pill(d, 540, 978, "Follow us for more SME tech insights  →",
         font(22, "bold"), VIOLET)

    img.save(os.path.join(OUTPUT_DIR, "CB-002_linkedin_awareness_brand_graphic.png"), "PNG")
    print("✓  CB-002 saved")


# ════════════════════════════════════════════════════════════
#  CB-003  Instagram 1080×1080 — PAIN / 6PM Competitor
#  Template A-style: split panel + "report card" showing 0 leads
#  Inspired by respond.io dark-dramatic style
# ════════════════════════════════════════════════════════════
def cb003():
    img = Image.new("RGBA", (1080, 1080), (*DARK_NAVY, 255))
    d   = ImageDraw.Draw(img)

    v_gradient(d, 1080, 1080, DARK_NAVY, (14, 10, 28))
    glow(img,  200, 460, 420, (200, 40, 40),  alpha_max=45)   # red left
    glow(img,  880, 460, 420, VIOLET,          alpha_max=55)   # violet right
    glow(img,  540, 980, 250, BLUE_MID,        alpha_max=25)

    branding_top(d)

    # ── Vertical centre divider ──────────────────────────────
    d.line([(540, 108), (540, 690)], fill=(255, 255, 255, 28), width=1)
    # "VS" badge on divider
    d.ellipse([516, 370, 564, 418], fill=(255, 255, 255, 16),
              outline=(255, 255, 255, 60))
    d.text((540, 394), "VS", fill=(*WHITE, 200), font=font(20, "bold"), anchor="mm")

    # ─── LEFT PANEL  —  CLOSED BUSINESS ─────────────────────
    lx = 270

    # Moon icon
    d.ellipse([lx - 36, 130, lx + 36, 202], fill=(220, 220, 240, 70))
    d.ellipse([lx - 18, 124, lx + 52, 196], fill=(*DARK_NAVY, 245))

    # Building silhouette
    d.rectangle([lx - 82, 260, lx + 82, 490], fill=(28, 24, 48, 220))
    # Windows — off
    for row in range(3):
        for col in range(3):
            wx, wy = lx - 58 + col * 48, 278 + row * 64
            d.rectangle([wx, wy, wx + 30, wy + 40], fill=(18, 14, 32, 255))

    # "CLOSED" sign
    d.rounded_rectangle([lx - 72, 498, lx + 72, 540], radius=8,
                         fill=(180, 38, 38, 220))
    d.text((lx, 519), "CLOSED", fill=(*WHITE, 255), font=font(22, "bold"), anchor="mm")

    # Panel label
    d.text((lx, 564), "Your business",
           fill=(*WHITE, 180), font=font(24, "regular"), anchor="mm")
    d.text((lx, 592), "6:00 PM",
           fill=(239, 68, 68, 255), font=font(30, "bold"), anchor="mm")

    # Mini "report card" — 0 leads
    glass_card(d, lx - 130, 616, lx + 130, 690, r=16,
               alpha_fill=10, alpha_border=50)
    d.text((lx - 100, 653), "Leads captured:", fill=(*BODY_GRAY, 200), font=font(18))
    d.text((lx + 80, 653), "0", fill=(239, 68, 68, 255),
           font=font(28, "bold"), anchor="rm")

    # ─── RIGHT PANEL  —  CHATBOT ACTIVE ─────────────────────
    rx = 810

    glow(img, rx, 360, 240, VIOLET, alpha_max=45)

    # Phone frame
    pw, ph_h = 200, 380
    px1, py1 = rx - pw // 2, 148
    px2, py2 = rx + pw // 2, py1 + ph_h
    d.rounded_rectangle([px1, py1, px2, py2], radius=22,
                         fill=(22, 18, 42, 240),
                         outline=(*VIOLET, 200), width=2)
    # Notch
    d.rounded_rectangle([rx - 30, py1 + 8, rx + 30, py1 + 22],
                         radius=7, fill=(12, 10, 24, 255))

    # WhatsApp header
    d.rectangle([px1 + 2, py1 + 28, px2 - 2, py1 + 74],
                 fill=(18, 140, 86, 230))
    d.ellipse([px1 + 10, py1 + 34, px1 + 50, py1 + 74],
               fill=(255, 255, 255, 70))
    d.text((px1 + 58, py1 + 47), "IGEN Bot", fill=(*WHITE, 255), font=font(15, "bold"))
    d.text((px1 + 58, py1 + 65), "● Online", fill=(144, 238, 144, 255), font=font(12))

    # Chat bubbles
    bubbles = [
        ("C", "Hi! Info chatbot?"),
        ("B", "Hi! RM500 sahaja"),
        ("B", "24/7 aktif ✓"),
        ("C", "Interested! 🔥"),
        ("B", "Booking link →"),
    ]
    by = py1 + 88
    for sender, txt in bubbles:
        f_bub = font(12)
        tw = int(d.textlength(txt, font=f_bub))
        bw = min(tw + 24, 156)
        if sender == "C":
            bx = px1 + 6
            fill = (45, 40, 75, 230)
        else:
            bx = px2 - 6 - bw
            fill = (*VIOLET, 210)
        d.rounded_rectangle([bx, by, bx + bw, by + 25], radius=8, fill=fill)
        d.text((bx + 12, by + 12), txt, fill=(*WHITE, 230),
               font=f_bub, anchor="lm")
        by += 34

    # Online dot
    d.ellipse([rx - 7, py2 - 18, rx + 7, py2 - 4],
               fill=(144, 238, 144, 255))

    # Panel label
    d.text((rx, 564), "Your competitor",
           fill=(*WHITE, 180), font=font(24, "regular"), anchor="mm")
    d.text((rx, 592), "2:47 AM",
           fill=(*VIOLET, 255), font=font(30, "bold"), anchor="mm")

    # Mini "report card" — leads captured
    glass_card(d, rx - 130, 616, rx + 130, 690, r=16,
               alpha_fill=10, alpha_border=50)
    d.text((rx - 100, 653), "Leads captured:", fill=(*BODY_GRAY, 200), font=font(18))
    d.text((rx + 80, 653), "12", fill=(*GREEN, 255),
           font=font(28, "bold"), anchor="rm")

    # ── Main headline ────────────────────────────────────────
    rule(d, 60, 712, 1020, a=40)
    d.text((540, 766),
           "Your business closes at 6PM.",
           fill=(*WHITE, 255), font=font(54, "bold"), anchor="mm")
    d.text((540, 832),
           "Your competitor's doesn't.",
           fill=(*VIOLET, 255), font=font(54, "bold"), anchor="mm")

    rule(d, 60, 872, 1020, a=30)

    # ── Bottom row — stat + CTA ──────────────────────────────
    # Stat pill left
    glass_card(d, 60, 892, 420, 950, r=29, alpha_fill=14, alpha_border=55)
    d.text((240, 921), "Avg. 340 leads/mo  captured after hours",
           fill=(*BODY_GRAY, 210), font=font(17, "regular"), anchor="mm")

    # CTA pill right
    d.rounded_rectangle([460, 892, 1020, 950], radius=29,
                         fill=(*VIOLET, 255))
    d.text((740, 921), "DM 'INFO' sekarang  →",
           fill=(*WHITE, 255), font=font(24, "bold"), anchor="mm")

    img.save(os.path.join(OUTPUT_DIR, "CB-003_instagram_pain_6pm_competitor.png"), "PNG")
    print("✓  CB-003 saved")


if __name__ == "__main__":
    print("Generating Week 1 mockups (v2)…\n")
    cb001()
    cb002()
    cb003()
    print("\nAll 3 posts saved to mockup/")
