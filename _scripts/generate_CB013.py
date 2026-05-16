"""CB-013 — Threshold Duality — Split layout: Outdated vs Modern website."""

from PIL import Image, ImageDraw, ImageFilter
import math
import os

FONT_DIR = r"C:\Users\jicoo\.claude\plugins\cache\anthropic-agent-skills\document-skills\f458cee31a75\skills\canvas-design\canvas-fonts"
OUT_PATH = r"c:\Users\jicoo\OneDrive\IGEN VERITAS TECHNOLOGIES\marketing_team\social-media\CB-013_education.png"

W, H = 1080, 1080

# Brand palette
DARK_BG      = (11, 11, 20)        # #0b0b14
LEFT_BG      = (18, 14, 38)        # deep near-black violet
VIOLET       = (123, 103, 209)     # #7b67d1
PURPLE       = (138, 93, 204)      # #8a5dcc
BLUE_MID     = (72, 143, 227)      # #488fe3
BLUE_BRIGHT  = (65, 150, 230)      # #4196e6
WHITE        = (255, 255, 255)
MUTED_RED    = (180, 70, 70)
BODY_GRAY    = (107, 114, 128)
DIVIDER_GLOW = (200, 185, 255)

# ── font loader ──────────────────────────────────────────────────────────────
def font(name, size):
    from PIL import ImageFont
    path = os.path.join(FONT_DIR, name)
    return ImageFont.truetype(path, size)

# ── helpers ──────────────────────────────────────────────────────────────────
def gradient_rect(draw, x0, y0, x1, y1, c_top, c_bot):
    for y in range(y0, y1):
        t = (y - y0) / max(y1 - y0 - 1, 1)
        r = int(c_top[0] + (c_bot[0] - c_top[0]) * t)
        g = int(c_top[1] + (c_bot[1] - c_top[1]) * t)
        b = int(c_top[2] + (c_bot[2] - c_top[2]) * t)
        draw.line([(x0, y), (x1, y)], fill=(r, g, b))

def gradient_rect_h(draw, x0, y0, x1, y1, c_left, c_right):
    for x in range(x0, x1):
        t = (x - x0) / max(x1 - x0 - 1, 1)
        r = int(c_left[0] + (c_right[0] - c_left[0]) * t)
        g = int(c_left[1] + (c_right[1] - c_left[1]) * t)
        b = int(c_left[2] + (c_right[2] - c_left[2]) * t)
        draw.line([(x, y0), (x, y1)], fill=(r, g, b))

def centered_text(draw, text, x_center, y, fnt, color):
    bb = draw.textbbox((0, 0), text, font=fnt)
    tw = bb[2] - bb[0]
    draw.text((x_center - tw // 2, y), text, font=fnt, fill=color)

def glow_text(img, draw, text, x_center, y, fnt, color, glow_color, radius=8):
    """Draw text with a soft glow behind it."""
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    bb = draw.textbbox((0, 0), text, font=fnt)
    tw = bb[2] - bb[0]
    ld.text((x_center - tw // 2, y), text, font=fnt, fill=(*glow_color, 140))
    glowed = layer.filter(ImageFilter.GaussianBlur(radius))
    img.alpha_composite(glowed)
    centered_text(draw, text, x_center, y, fnt, color)

def spinner_icon(draw, cx, cy, r, color, muted_color, segments=10):
    """Draw a circular loading spinner."""
    for i in range(segments):
        angle = (360 / segments) * i - 90
        a1 = math.radians(angle)
        a2 = math.radians(angle + 20)
        alpha = int(255 * (1 - i / segments))
        draw.arc(
            [cx - r, cy - r, cx + r, cy + r],
            start=angle, end=angle + 22,
            fill=(*muted_color[:3], max(40, alpha)),
            width=5
        )

def broken_image_icon(draw, x, y, sz, color):
    """Draw a broken image placeholder."""
    draw.rectangle([x, y, x+sz, y+sz], outline=color, width=2)
    draw.line([x, y, x+sz, y+sz], fill=color, width=2)
    draw.line([x+sz, y, x, y+sz], fill=color, width=2)
    # small mountain shape
    pts = [(x+8, y+sz-10), (x+sz//2-5, y+14), (x+sz//2+8, y+sz//2-4), (x+sz-8, y+10), (x+sz-8, y+sz-10)]
    draw.polygon(pts, outline=color)

def checkmark_icon(draw, cx, cy, r, color, width=5):
    """Draw a checkmark inside a circle."""
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=color, width=3)
    draw.line([cx-r//2, cy, cx-r//8, cy+r//2, cx+r//2, cy-r//3], fill=color, width=width)

def mobile_icon(draw, x, y, w, h, color, filled=False):
    """Draw a phone outline."""
    draw.rounded_rectangle([x, y, x+w, y+h], radius=6, outline=color, width=3)
    draw.ellipse([x+w//2-3, y+h-10, x+w//2+3, y+h-4], fill=color)
    draw.line([x+6, y+12, x+w-6, y+12], fill=color, width=2)

def cta_button(draw, x, y, w, h, color, label, fnt):
    """Draw a modern CTA button shape."""
    draw.rounded_rectangle([x, y, x+w, y+h], radius=h//2, fill=color)
    bb = draw.textbbox((0,0), label, font=fnt)
    tw = bb[2]-bb[0]; th = bb[3]-bb[1]
    draw.text((x + (w-tw)//2, y + (h-th)//2 - 2), label, font=fnt, fill=WHITE)

def layout_lines(draw, x, y, w, color, alpha=80):
    """Abstract clean-layout grid lines."""
    for i, lw in enumerate([w, int(w*0.6), int(w*0.8), int(w*0.4)]):
        draw.line([(x, y + i*18), (x + lw, y + i*18)], fill=color, width=2)

def clutter_lines(draw, x, y, max_w, color):
    """Chaotic overlapping lines for cluttered feel."""
    import random
    rng = random.Random(42)
    for i in range(20):
        lx = x + rng.randint(0, 20)
        lw = rng.randint(10, max_w - 20)
        ly = y + i * 9
        draw.line([(lx, ly), (lx+lw, ly)], fill=color, width=rng.randint(1, 4))

# ── main ─────────────────────────────────────────────────────────────────────
def build():
    img = Image.new("RGBA", (W, H), DARK_BG + (255,))
    draw = ImageDraw.Draw(img, "RGBA")

    MID = W // 2
    FOOTER_H = 110
    HEADER_H = 220   # space for headline at bottom
    PANEL_TOP = 0
    PANEL_BOT = H - FOOTER_H - HEADER_H

    # ── LEFT PANEL (outdated) ─────────────────────────────────────────────
    gradient_rect(draw, 0, PANEL_TOP, MID, PANEL_BOT,
                  (22, 14, 44), (10, 8, 26))

    # subtle noise texture (dot grid)
    for gx in range(0, MID, 22):
        for gy in range(PANEL_TOP, PANEL_BOT, 22):
            draw.point((gx, gy), fill=(40, 30, 60, 60))

    # OUTDATED label
    f_label = font("WorkSans-Bold.ttf", 22)
    draw.text((38, 38), "OUTDATED", font=f_label, fill=MUTED_RED + (200,))
    # small underline
    draw.line([(38, 64), (38+130, 64)], fill=MUTED_RED + (80,), width=1)

    # broken image icon
    broken_image_icon(draw, 60, 100, 68, MUTED_RED + (160,))

    # clutter lines (simulating messy layout)
    clutter_lines(draw, 38, 190, 380, (80, 65, 110, 120))

    # spinner (loading…)
    cx_spin, cy_spin = 160, 340
    for i in range(12):
        angle = (360/12)*i - 90
        a_r = math.radians(angle)
        frac = 1 - i/12
        col_alpha = int(220 * frac)
        end_angle = angle + 25
        draw.arc([cx_spin-28, cy_spin-28, cx_spin+28, cy_spin+28],
                 start=angle, end=end_angle,
                 fill=(*MUTED_RED, col_alpha), width=5)

    f_tiny = font("WorkSans-Regular.ttf", 13)
    draw.text((cx_spin - 28, cy_spin + 35), "Loading…", font=f_tiny, fill=(130, 110, 160, 180))

    # unreadable tiny text blocks (decorative)
    f_micro = font("DMMono-Regular.ttf", 9)
    for row in range(10):
        draw.text((38, 410 + row * 14), "█" * (20 + (row % 3)*5), font=f_micro, fill=(55, 42, 80, 180))

    # no-mobile: crossed-out phone icon
    mobile_icon(draw, 62, 490, 34, 58, (130, 100, 160, 160))
    draw.line([(56, 484), (102, 556)], fill=MUTED_RED + (200,), width=3)

    # "last updated" stale badge
    f_stale = font("DMMono-Regular.ttf", 14)
    draw.rounded_rectangle([38, 565, 260, 593], radius=6, fill=(60, 40, 80, 140), outline=MUTED_RED + (100,), width=1)
    draw.text((50, 572), "Last updated: 2019", font=f_stale, fill=MUTED_RED + (200,))

    # "no SSL" warning
    draw.rounded_rectangle([38, 608, 220, 636], radius=6, fill=(60, 30, 30, 120), outline=(160, 60, 60, 120), width=1)
    draw.text((50, 615), "! Not secure", font=f_stale, fill=(200, 100, 100, 210))

    # "0 reviews" and "contact@hotmail" — dead trust signals
    f_dead = font("WorkSans-Regular.ttf", 13)
    draw.text((38, 650), "0 reviews  |  contact@hotmail.com", font=f_dead, fill=(100, 80, 130, 160))
    draw.text((38, 670), "No live chat  |  No mobile view", font=f_dead, fill=(90, 70, 120, 130))

    # ── RIGHT PANEL (modern) ──────────────────────────────────────────────
    # gradient: bright violet top-left → deep blue bottom-right
    # first fill with a vertical gradient
    gradient_rect(draw, MID, PANEL_TOP, W, PANEL_BOT,
                  (110, 70, 200), (40, 100, 210))
    # horizontal blend on top for richness
    for x in range(MID, W):
        t = (x - MID) / max(W - MID - 1, 1)
        # left side more violet, right more blue
        r = int(110 + (30 - 110) * t)
        g = int(70  + (110 - 70) * t)
        b = int(200 + (220 - 200) * t)
        # very light horizontal modulation
        draw.line([(x, PANEL_TOP), (x, PANEL_BOT)], fill=(r, g, b, 30))

    # dot grid (lighter)
    for gx in range(MID, W, 22):
        for gy in range(PANEL_TOP, PANEL_BOT, 22):
            draw.point((gx, gy), fill=(255, 255, 255, 18))

    # MODERN label
    draw.text((MID + 38, 38), "MODERN", font=f_label, fill=WHITE + (230,))
    draw.line([(MID+38, 64), (MID+38+108, 64)], fill=WHITE + (60,), width=1)

    # fast-load checkmark
    checkmark_icon(draw, MID + 100, 148, 36, WHITE, width=5)

    # layout lines (clean grid)
    layout_lines(draw, MID + 38, 210, 390, (255, 255, 255, 120))

    # mobile-friendly icon (phone, glowing)
    mobile_icon(draw, MID + 56, 290, 36, 60, (220, 210, 255, 220))
    f_tiny2 = font("WorkSans-Regular.ttf", 13)
    draw.text((MID + 100, 308), "Mobile-ready", font=f_tiny2, fill=(200, 190, 255, 200))

    # clean card hint — subtle wireframe card
    draw.rounded_rectangle([MID+38, 375, MID+400, 455],
                            radius=10, fill=(255, 255, 255, 14), outline=(255,255,255,50), width=1)
    layout_lines(draw, MID + 56, 395, 290, (255, 255, 255, 90))
    # small avatar circle in card
    draw.ellipse([MID+56, 405, MID+78, 427], outline=(255,255,255,90), width=2)

    # CTA button
    f_btn = font("WorkSans-Bold.ttf", 17)
    cta_button(draw, MID + 80, 475, 250, 46, (50, 30, 120, 230), "Get Started ->", f_btn)

    # fast stats row (bottom of modern panel)
    f_stat_n = font("BigShoulders-Bold.ttf", 36)
    f_stat_l = font("WorkSans-Regular.ttf", 13)
    stats = [("3s", "load time"), ("99%", "uptime"), ("2x", "conversions")]
    sx_start = MID + 42
    for i, (num, lbl) in enumerate(stats):
        sx = sx_start + i * 140
        draw.text((sx, 555), num, font=f_stat_n, fill=WHITE + (230,))
        draw.text((sx, 595), lbl, font=f_stat_l, fill=(200, 190, 255, 180))
    draw.line([(MID+38, 545), (W-38, 545)], fill=(255, 255, 255, 40), width=1)

    # ── DIVIDER LINE (glowing) ────────────────────────────────────────────
    # soft glow behind divider
    div_layer = Image.new("RGBA", (W, H), (0,0,0,0))
    dd = ImageDraw.Draw(div_layer)
    dd.line([(MID, 0), (MID, PANEL_BOT)], fill=(*DIVIDER_GLOW, 60), width=18)
    div_layer = div_layer.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(div_layer)

    draw = ImageDraw.Draw(img, "RGBA")
    draw.line([(MID, 0), (MID, PANEL_BOT)], fill=WHITE + (220,), width=2)

    # ── HEADLINE BAND ─────────────────────────────────────────────────────
    HB_TOP = PANEL_BOT
    HB_BOT = H - FOOTER_H
    gradient_rect(draw, 0, HB_TOP, W, HB_BOT, (14, 10, 32), DARK_BG)

    # thin separator line above headline
    draw.line([(60, HB_TOP + 16), (W-60, HB_TOP + 16)], fill=(80, 65, 120, 100), width=1)

    f_headline = font("BigShoulders-Bold.ttf", 52)
    f_sub      = font("InstrumentSans-Regular.ttf", 24)

    line1 = "Your website is either building trust"
    line2 = "— or costing you clients."
    line_sub = "There is no middle ground."

    hl_y = HB_TOP + 30
    glow_text(img, draw, line1, W//2, hl_y, f_headline, WHITE, DIVIDER_GLOW, radius=12)
    draw = ImageDraw.Draw(img, "RGBA")
    hl_y2 = hl_y + 62
    glow_text(img, draw, line2, W//2, hl_y2, f_headline, (*VIOLET, 255), DIVIDER_GLOW, radius=10)
    draw = ImageDraw.Draw(img, "RGBA")

    # subtext
    centered_text(draw, line_sub, W//2, hl_y2 + 72, f_sub, BODY_GRAY + (255,))

    # ── FOOTER ────────────────────────────────────────────────────────────
    FT = H - FOOTER_H
    draw.rectangle([0, FT, W, H], fill=DARK_BG + (255,))
    draw.line([(0, FT), (W, FT)], fill=(60, 48, 90, 200), width=1)

    f_brand = font("BigShoulders-Bold.ttf", 32)
    f_domain = font("InstrumentSans-Regular.ttf", 18)
    f_tagline = font("WorkSans-Regular.ttf", 14)

    # wordmark left-aligned
    draw.text((60, FT + 28), "IGEN VERITAS", font=f_brand, fill=WHITE + (240,))

    # violet accent dot between brand segments
    draw.ellipse([220, FT + 38, 228, FT + 46], fill=VIOLET)

    # domain right-aligned
    domain = "igenveritas.com"
    bb = draw.textbbox((0,0), domain, font=f_domain)
    dw = bb[2] - bb[0]
    draw.text((W - 60 - dw, FT + 36), domain, font=f_domain, fill=BODY_GRAY + (200,))

    # tagline below brand
    draw.text((60, FT + 70), "Intelligent Solutions · Web & Mobile · AI Automation", font=f_tagline, fill=BODY_GRAY + (160,))

    # ── SAVE ─────────────────────────────────────────────────────────────
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    final = img.convert("RGB")
    final.save(OUT_PATH, "PNG", quality=95)
    print(f"Saved: {OUT_PATH}")

if __name__ == "__main__":
    build()
