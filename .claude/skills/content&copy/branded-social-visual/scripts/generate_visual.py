"""
IGEN VERITAS — Branded Social Visual Generator
Usage: python generate_visual.py --type <pain|education|proof|cta> --week <1-4> --day <mon|wed|fri|sat>
Or import and call generate(config) directly.
"""
import os
import sys
import math
import argparse
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# ── Resolve workspace root ────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR  = os.path.dirname(SCRIPT_DIR)
WORKSPACE  = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUTPUT_DIR = os.path.join(WORKSPACE, "social-media")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Brand colors ──────────────────────────────────────────────────────────────
VIOLET      = (123, 103, 209, 255)
PURPLE      = (138,  93, 204, 255)
BLUE_MID    = ( 72, 143, 227, 255)
BLUE_BRIGHT = ( 65, 150, 230, 255)
DARK_NAVY   = ( 11,  11,  20, 255)
WHITE       = (255, 255, 255, 255)
BODY_GRAY   = (107, 114, 128, 255)
ACCENT_RED  = (239,  68,  68, 255)
GLASS_FILL  = (255, 255, 255,  18)
GLASS_BDR   = (255, 255, 255,  38)


# ── Font loader ───────────────────────────────────────────────────────────────
_FONT_PATHS = {
    "bold":    ["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/ariblk.ttf"],
    "regular": ["C:/Windows/Fonts/segoeui.ttf",  "C:/Windows/Fonts/arial.ttf"],
    "light":   ["C:/Windows/Fonts/segoeuil.ttf", "C:/Windows/Fonts/segoeui.ttf"],
}

def _font(size, weight="regular"):
    for path in _FONT_PATHS.get(weight, _FONT_PATHS["regular"]):
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


# ── Gradient fill ─────────────────────────────────────────────────────────────
def _gradient(draw, w, h, start, end, diagonal=False):
    steps = w + h if diagonal else h
    for i in range(steps):
        t = i / max(steps - 1, 1)
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        if diagonal:
            draw.line([(0, i), (i, 0)], fill=(r, g, b, 255))
        else:
            draw.line([(0, i), (w, i)], fill=(r, g, b, 255))


def _radial_glow(img, cx, cy, radius, color, alpha_max=80):
    """Soft radial glow overlay using a separate RGBA layer."""
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    steps = 40
    for i in range(steps, 0, -1):
        r_ = int(radius * i / steps)
        a  = int(alpha_max * (1 - i / steps) ** 2)
        gd.ellipse(
            [cx - r_, cy - r_, cx + r_, cy + r_],
            fill=(color[0], color[1], color[2], a)
        )
    return Image.alpha_composite(img, glow)


def _glass_card(draw, box, radius=24):
    draw.rounded_rectangle(box, radius=radius, fill=GLASS_FILL,
                            outline=GLASS_BDR, width=1)


def _wrap_text(text, font, max_width, draw):
    """Return list of lines that fit within max_width."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = (current + " " + word).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


# ═══════════════════════════════════════════════════════════════════════════════
# TEMPLATE A — PAIN POINT
# ═══════════════════════════════════════════════════════════════════════════════
def template_pain_point(headline, subtext, cta, filename):
    img  = Image.new("RGBA", (1080, 1080), DARK_NAVY)
    draw = ImageDraw.Draw(img)

    # Background gradient (dark navy → deep purple tint)
    _gradient(draw, 1080, 1080, DARK_NAVY, (25, 12, 48, 255))

    # Radial violet glow center-left
    img = _radial_glow(img, 360, 500, 520, VIOLET, alpha_max=70)
    draw = ImageDraw.Draw(img)

    # ── Brand label (top-left) ──────────────────────────────────────────────
    brand_font = _font(22, "bold")
    url_font   = _font(18, "light")
    draw.text((60, 58), "IGEN VERITAS", font=brand_font, fill=WHITE)
    draw.text((60, 88), "igen-veritas.com", font=url_font, fill=BODY_GRAY)

    # Thin accent line under brand
    draw.rectangle([60, 116, 260, 118], fill=(*VIOLET[:3], 180))

    # ── Main headline ───────────────────────────────────────────────────────
    h_font  = _font(96, "bold")
    h_lines = headline.split("/") if "/" in headline else [headline]
    y_start = 190
    for idx, line in enumerate(h_lines):
        line = line.strip()
        # Accent last word of first line in VIOLET
        if idx == 0 and " " in line:
            words = line.split()
            plain = " ".join(words[:-1]) + " "
            accent = words[-1]
            pw = draw.textlength(plain, font=h_font)
            aw = draw.textlength(accent, font=h_font)
            total_w = pw + aw
            x0 = (1080 - total_w) // 2
            draw.text((x0, y_start), plain,  font=h_font, fill=WHITE)
            draw.text((x0 + int(pw), y_start), accent, font=h_font,
                      fill=(*VIOLET[:3], 255))
        else:
            bbox = draw.textbbox((0, 0), line, font=h_font)
            tw   = bbox[2] - bbox[0]
            draw.text(((1080 - tw) // 2, y_start), line, font=h_font, fill=WHITE)
        y_start += 110

    # ── Glassmorphism stat card ─────────────────────────────────────────────
    card_x1, card_y1 = 160, 480
    card_x2, card_y2 = 920, 720
    _glass_card(draw, [card_x1, card_y1, card_x2, card_y2], radius=28)

    time_font  = _font(64, "bold")
    label_font = _font(22, "regular")
    stat_font  = _font(38, "bold")

    draw.text((540, 530), "2:47 AM", font=time_font,
              fill=(255, 255, 255, 220), anchor="mt")
    draw.text((540, 612), "Your business is offline.", font=label_font,
              fill=BODY_GRAY, anchor="mt")

    # Red "0 leads" badge
    draw.rounded_rectangle([330, 648, 570, 698], radius=22,
                            fill=(239, 68, 68, 200))
    draw.text((450, 673), "0 leads captured", font=_font(20, "bold"),
              fill=WHITE, anchor="mm")

    # "Competitor" badge (green tint)
    draw.rounded_rectangle([590, 648, 870, 698], radius=22,
                            fill=(16, 185, 129, 200))
    draw.text((730, 673), "Competitor: +12 leads", font=_font(20, "bold"),
              fill=WHITE, anchor="mm")

    # ── Subtext ─────────────────────────────────────────────────────────────
    sub_font = _font(32, "regular")
    sub_lines = _wrap_text(subtext, sub_font, 800, draw)
    sy = 760
    for sl in sub_lines[:2]:
        bbox = draw.textbbox((0, 0), sl, font=sub_font)
        tw   = bbox[2] - bbox[0]
        draw.text(((1080 - tw) // 2, sy), sl, font=sub_font, fill=BODY_GRAY)
        sy += 46

    # ── CTA pill ─────────────────────────────────────────────────────────────
    cta_font = _font(28, "bold")
    cta_bbox = draw.textbbox((0, 0), cta, font=cta_font)
    cta_w    = cta_bbox[2] - cta_bbox[0] + 80
    cta_x1   = (1080 - cta_w) // 2
    draw.rounded_rectangle([cta_x1, 880, cta_x1 + cta_w, 932], radius=26,
                            fill=VIOLET)
    draw.text((540, 906), cta, font=cta_font, fill=WHITE, anchor="mm")

    # ── Bottom brand strip ────────────────────────────────────────────────────
    draw.text((540, 990), "igen-veritas.com  •  Powering businesses with AI",
              font=_font(16, "light"), fill=BODY_GRAY, anchor="mm")

    out = os.path.join(OUTPUT_DIR, filename)
    img.save(out, "PNG")
    print(f"Saved: {out}")
    return out


# ═══════════════════════════════════════════════════════════════════════════════
# TEMPLATE B — EDUCATION
# ═══════════════════════════════════════════════════════════════════════════════
def template_education(headline, subtext, features, filename):
    img  = Image.new("RGBA", (1080, 1080), DARK_NAVY)
    draw = ImageDraw.Draw(img)

    # Diagonal gradient: Violet → Blue Bright
    _gradient(draw, 1080, 1080, VIOLET, BLUE_BRIGHT, diagonal=True)
    _gradient(draw, 1080, 1080,
              (*VIOLET[:3], 200), (*BLUE_BRIGHT[:3], 200), diagonal=False)

    # ── Brand label ──────────────────────────────────────────────────────────
    # White pill badge top-center
    badge_font = _font(22, "bold")
    badge_text = "IGEN VERITAS"
    bw = draw.textlength(badge_text, font=badge_font) + 56
    bx1 = (1080 - bw) // 2
    draw.rounded_rectangle([bx1, 52, bx1 + bw, 96], radius=22,
                            fill=(255, 255, 255, 220))
    draw.text((540, 74), badge_text, font=badge_font,
              fill=(30, 20, 60, 255), anchor="mm")

    # ── Headline ─────────────────────────────────────────────────────────────
    h_font = _font(80, "bold")
    lines  = headline.split("/") if "/" in headline else _wrap_text(headline, h_font, 900, draw)
    y_h    = 130
    for line in lines[:3]:
        line = line.strip()
        bbox = draw.textbbox((0, 0), line, font=h_font)
        tw   = bbox[2] - bbox[0]
        draw.text(((1080 - tw) // 2, y_h), line, font=h_font, fill=WHITE)
        y_h += 94

    # ── Central bot mascot (geometric) ──────────────────────────────────────
    cx, cy = 540, 580
    # Body
    draw.rounded_rectangle([cx - 70, cy - 80, cx + 70, cy + 80], radius=30,
                            fill=(255, 255, 255, 230))
    # Head
    draw.ellipse([cx - 55, cy - 160, cx + 55, cy - 60],
                 fill=(255, 255, 255, 230))
    # Eyes (glowing)
    draw.ellipse([cx - 28, cy - 130, cx - 10, cy - 112], fill=BLUE_BRIGHT)
    draw.ellipse([cx + 10, cy - 130, cx + 28, cy - 112], fill=BLUE_BRIGHT)
    # WhatsApp-style badge on body
    draw.ellipse([cx - 22, cy - 18, cx + 22, cy + 22],
                 fill=(37, 211, 102, 255))
    # Antenna
    draw.line([cx, cy - 160, cx, cy - 180], fill=WHITE, width=3)
    draw.ellipse([cx - 7, cy - 190, cx + 7, cy - 176], fill=VIOLET)

    # ── Feature pills ──────────────────────────────────────────────────────
    pill_font = _font(24, "bold")
    label_font = _font(18, "regular")
    pill_data  = features if features else [
        ("🌐", "Website"),
        ("📄", "PDF"),
        ("❓", "FAQ"),
        ("🧠", "Knowledge Base"),
    ]
    positions = [
        (cx - 280, cy - 110),  # top-left
        (cx + 160, cy - 110),  # top-right
        (cx - 280, cy + 50),   # bottom-left
        (cx + 160, cy + 50),   # bottom-right
    ]
    for (icon, label), (px, py) in zip(pill_data[:4], positions):
        pw = draw.textlength(f"{icon}  {label}", font=pill_font) + 40
        draw.rounded_rectangle([px, py, px + pw, py + 52], radius=14,
                                fill=(255, 255, 255, 200),
                                outline=(255, 255, 255, 180), width=1)
        draw.text((px + 20, py + 26), f"{icon}  {label}", font=pill_font,
                  fill=(30, 20, 60, 255), anchor="lm")
        # Connector line to bot
        mid_x = px + pw if px < cx else px
        draw.line([mid_x, py + 26, cx + (50 if px < cx else -50), cy],
                  fill=(255, 255, 255, 80), width=2)

    # ── Subtext ──────────────────────────────────────────────────────────────
    sub_font  = _font(30, "regular")
    sub_lines = _wrap_text(subtext, sub_font, 800, draw)
    sy = 800
    for sl in sub_lines[:2]:
        bbox = draw.textbbox((0, 0), sl, font=sub_font)
        tw   = bbox[2] - bbox[0]
        draw.text(((1080 - tw) // 2, sy), sl, font=sub_font,
                  fill=(255, 255, 255, 200))
        sy += 44

    # ── Bottom credibility ───────────────────────────────────────────────────
    draw.text((540, 990), "igen-veritas.com  •  AI that works while you sleep",
              font=_font(17, "light"), fill=(255, 255, 255, 150), anchor="mm")

    out = os.path.join(OUTPUT_DIR, filename)
    img.save(out, "PNG")
    print(f"Saved: {out}")
    return out


# ═══════════════════════════════════════════════════════════════════════════════
# TEMPLATE C — PROOF / DEMO
# ═══════════════════════════════════════════════════════════════════════════════
def template_proof(headline, subtext, chat_lines, stats, filename):
    img  = Image.new("RGBA", (1080, 1080), DARK_NAVY)
    draw = ImageDraw.Draw(img)

    # Gradient background
    _gradient(draw, 1080, 1080, VIOLET, BLUE_BRIGHT)

    # Dark overlay at bottom for stat/text readability
    overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for y in range(600, 1080):
        t = (y - 600) / 480
        a = int(200 * t)
        od.line([(0, y), (1080, y)], fill=(11, 11, 20, a))
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    # ── Brand badge (top-left) ────────────────────────────────────────────────
    badge_font = _font(20, "bold")
    bw         = draw.textlength("IGEN VERITAS", font=badge_font) + 48
    draw.rounded_rectangle([56, 52, 56 + bw, 94], radius=20,
                            fill=(255, 255, 255, 210))
    draw.text((56 + bw // 2, 73), "IGEN VERITAS", font=badge_font,
              fill=(30, 20, 60, 255), anchor="mm")

    # ── Headline ─────────────────────────────────────────────────────────────
    h_font = _font(84, "bold")
    lines  = headline.split("/") if "/" in headline else _wrap_text(headline, h_font, 940, draw)
    y_h    = 130
    for line in lines[:2]:
        line = line.strip()
        bbox = draw.textbbox((0, 0), line, font=h_font)
        tw   = bbox[2] - bbox[0]
        draw.text(((1080 - tw) // 2, y_h), line, font=h_font, fill=WHITE)
        y_h += 98

    # ── Floating chat mockup card ─────────────────────────────────────────────
    card_x1, card_y1 = 140, 370
    card_x2, card_y2 = 940, 780
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=24,
                            fill=(18, 18, 28, 230),
                            outline=(255, 255, 255, 30), width=1)

    # WhatsApp-style header bar
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y1 + 60],
                            radius=24, fill=(37, 211, 102, 220))
    wf = _font(22, "bold")
    draw.text((card_x1 + 24, card_y1 + 30), "AI Sales Agent — IGEN VERITAS",
              font=wf, fill=WHITE, anchor="lm")
    draw.ellipse([card_x2 - 52, card_y1 + 12,
                  card_x2 - 28, card_y1 + 36],
                 fill=(144, 238, 144, 255))

    # Chat bubbles
    bubble_font = _font(24, "regular")
    bub_data    = chat_lines if chat_lines else [
        ("customer", "Berapa harga pakej chatbot?"),
        ("bot",      "Pakej kami bermula dari RM 500 setup.\nBasic, Growth, atau Pro — mana satu sesuai?"),
        ("customer", "Boleh tolong explain Basic?"),
        ("bot",      "Basic: RM 500 setup + RM 150/bulan.\nChatbot 24/7 on website + WhatsApp ✓"),
    ]
    by = card_y1 + 80
    for who, text in bub_data[:4]:
        is_bot    = who == "bot"
        bg_color  = (72, 143, 227, 220) if is_bot else (255, 255, 255, 200)
        txt_color = WHITE if is_bot else (20, 20, 40, 255)
        lines     = text.split("\n")
        max_line_w = max(draw.textlength(l, font=bubble_font) for l in lines)
        tw        = min(int(max_line_w) + 36, 620)
        bx1       = (card_x2 - 40 - tw) if is_bot else (card_x1 + 40)
        bx2       = bx1 + tw
        bh        = 16 + len(lines) * 34
        draw.rounded_rectangle([bx1, by, bx2, by + bh], radius=14, fill=bg_color)
        for li, line in enumerate(lines):
            draw.text((bx1 + 14, by + 10 + li * 34), line,
                      font=bubble_font, fill=txt_color)
        by += bh + 12

    # ── Stat pills ────────────────────────────────────────────────────────────
    stat_data = stats if stats else [
        "24/7 Active", "< 3s Reply", "100% Auto", "0 Missed Leads"
    ]
    sf       = _font(22, "bold")
    pill_y   = 818
    total_w  = sum(draw.textlength(s, font=sf) + 48 for s in stat_data) + 24 * (len(stat_data) - 1)
    px       = (1080 - total_w) // 2
    for stat in stat_data:
        pw = draw.textlength(stat, font=sf) + 48
        draw.rounded_rectangle([px, pill_y, px + pw, pill_y + 48], radius=24,
                                fill=(*VIOLET[:3], 180))
        draw.text((px + pw // 2, pill_y + 24), stat, font=sf,
                  fill=WHITE, anchor="mm")
        px += pw + 24

    # ── Subtext ───────────────────────────────────────────────────────────────
    sub_font  = _font(28, "regular")
    sub_lines = _wrap_text(subtext, sub_font, 800, draw)
    sy        = 900
    for sl in sub_lines[:2]:
        bbox = draw.textbbox((0, 0), sl, font=sub_font)
        tw   = bbox[2] - bbox[0]
        draw.text(((1080 - tw) // 2, sy), sl, font=sub_font,
                  fill=(255, 255, 255, 180))
        sy += 42

    # ── Bottom ────────────────────────────────────────────────────────────────
    draw.text((540, 1010), "igen-veritas.com",
              font=_font(18, "light"), fill=BODY_GRAY, anchor="mm")

    out = os.path.join(OUTPUT_DIR, filename)
    img.save(out, "PNG")
    print(f"Saved: {out}")
    return out


# ═══════════════════════════════════════════════════════════════════════════════
# TEMPLATE D — PACKAGE / CTA
# ═══════════════════════════════════════════════════════════════════════════════
def template_cta(headline, subtext, cta, filename):
    img  = Image.new("RGBA", (1080, 1080), DARK_NAVY)
    draw = ImageDraw.Draw(img)

    # Purple-to-purple deep gradient
    _gradient(draw, 1080, 1080, VIOLET, PURPLE)

    # ── Top accent bar ────────────────────────────────────────────────────────
    draw.rectangle([0, 0, 1080, 8], fill=BLUE_MID)

    # ── Brand name ────────────────────────────────────────────────────────────
    brand_f = _font(24, "bold")
    draw.text((540, 58), "IGEN VERITAS", font=brand_f, fill=WHITE, anchor="mt")
    draw.text((540, 92), "AI Chatbot Packages", font=_font(18, "light"),
              fill=(*WHITE[:3], 160), anchor="mt")

    # ── Headline ─────────────────────────────────────────────────────────────
    h_font = _font(72, "bold")
    lines  = headline.split("/") if "/" in headline else _wrap_text(headline, h_font, 900, draw)
    y_h    = 136
    for idx, line in enumerate(lines[:2]):
        line = line.strip()
        color = BLUE_MID if idx == 1 else WHITE
        bbox  = draw.textbbox((0, 0), line, font=h_font)
        tw    = bbox[2] - bbox[0]
        draw.text(((1080 - tw) // 2, y_h), line, font=h_font, fill=color)
        y_h  += 84

    # ── Package cards ─────────────────────────────────────────────────────────
    packages = [
        {
            "name":    "Basic",
            "setup":   "RM 500",
            "monthly": "RM 150/mo",
            "features": ["AI chatbot 24/7", "Website + WhatsApp", "FAQ answering", "Lead capture"],
            "highlight": False,
        },
        {
            "name":    "Growth",
            "setup":   "RM 1,000",
            "monthly": "RM 300/mo",
            "features": ["Everything in Basic", "n8n automation", "Google Sheets CRM", "BM + English + Mandarin"],
            "highlight": True,
        },
        {
            "name":    "Pro",
            "setup":   "RM 2,000",
            "monthly": "RM 500/mo",
            "features": ["Everything in Growth", "Lead scoring + alerts", "Day 1/3/7 follow-up", "Weekly dashboard"],
            "highlight": False,
        },
    ]

    card_w   = 284
    card_h   = 460
    card_y1  = 330
    gap      = 28
    total_cw = card_w * 3 + gap * 2
    start_x  = (1080 - total_cw) // 2

    for i, pkg in enumerate(packages):
        cx1 = start_x + i * (card_w + gap)
        cx2 = cx1 + card_w

        if pkg["highlight"]:
            # Glow border for "Most Popular"
            for gp in range(4, 0, -1):
                draw.rounded_rectangle(
                    [cx1 - gp*2, card_y1 - gp*2, cx2 + gp*2, card_y1 + card_h + gp*2],
                    radius=28, fill=(*VIOLET[:3], 40 - gp * 8)
                )
            draw.rounded_rectangle([cx1, card_y1, cx2, card_y1 + card_h],
                                    radius=24, fill=(20, 14, 50, 230),
                                    outline=(*VIOLET[:3], 200), width=2)
            # "Most Popular" badge
            mp_f = _font(16, "bold")
            mp_w = draw.textlength("MOST POPULAR", font=mp_f) + 28
            mp_x = cx1 + (card_w - mp_w) // 2
            draw.rounded_rectangle([mp_x, card_y1 - 16, mp_x + mp_w, card_y1 + 16],
                                    radius=12, fill=VIOLET)
            draw.text((cx1 + card_w // 2, card_y1), "MOST POPULAR", font=mp_f,
                      fill=WHITE, anchor="mm")
        else:
            draw.rounded_rectangle([cx1, card_y1, cx2, card_y1 + card_h],
                                    radius=24, fill=(20, 14, 50, 200),
                                    outline=(255, 255, 255, 60), width=1)

        mid_x = cx1 + card_w // 2
        ty    = card_y1 + 32

        # Package name
        draw.text((mid_x, ty), pkg["name"], font=_font(28, "bold"),
                  fill=WHITE, anchor="mt")
        ty += 44

        # Setup price
        draw.text((mid_x, ty), pkg["setup"], font=_font(44, "bold"),
                  fill=BLUE_MID if pkg["highlight"] else WHITE, anchor="mt")
        ty += 56

        # Monthly
        draw.text((mid_x, ty), pkg["monthly"], font=_font(20, "regular"),
                  fill=BODY_GRAY, anchor="mt")
        ty += 36

        # Divider
        draw.line([cx1 + 24, ty, cx2 - 24, ty], fill=(*WHITE[:3], 40), width=1)
        ty += 20

        # Features
        feat_f = _font(18, "regular")
        for feat in pkg["features"]:
            draw.text((cx1 + 24, ty), f"✓  {feat}", font=feat_f,
                      fill=(255, 255, 255, 200))
            ty += 34

    # ── CTA button ───────────────────────────────────────────────────────────
    cta_f    = _font(30, "bold")
    cta_w    = draw.textlength(cta, font=cta_f) + 88
    cta_x1   = (1080 - cta_w) // 2
    draw.rounded_rectangle([cta_x1, 854, cta_x1 + cta_w, 910], radius=28,
                            fill=WHITE)
    draw.text((540, 882), cta, font=cta_f,
              fill=(*VIOLET[:3], 255), anchor="mm")

    # ── Subtext ───────────────────────────────────────────────────────────────
    sub_lines = _wrap_text(subtext, _font(24, "light"), 800, draw)
    sy = 930
    for sl in sub_lines[:1]:
        bbox = draw.textbbox((0, 0), sl, font=_font(24, "light"))
        tw   = bbox[2] - bbox[0]
        draw.text(((1080 - tw) // 2, sy), sl, font=_font(24, "light"),
                  fill=(*WHITE[:3], 160))

    # ── Bottom ────────────────────────────────────────────────────────────────
    draw.text((540, 1010), "igen-veritas.com  •  +60 17 310 3966",
              font=_font(17, "light"), fill=BODY_GRAY, anchor="mm")

    out = os.path.join(OUTPUT_DIR, filename)
    img.save(out, "PNG")
    print(f"Saved: {out}")
    return out


# ═══════════════════════════════════════════════════════════════════════════════
# CLI entry point
# ═══════════════════════════════════════════════════════════════════════════════
WEEK1_DEFAULTS = {
    "mon": dict(
        template  = "pain",
        headline  = "Ada website. / Takde leads.",
        subtext   = "You paid for a website. Visitors come. Nobody WhatsApp.",
        cta       = "DM 'INFO' untuk free audit",
    ),
    "wed": dict(
        template  = "education",
        headline  = "Train AI on your / Business Knowledge",
        subtext   = "Your chatbot learns from your website, PDF, FAQs, and more.",
        features  = [("🌐","Website"),("📄","PDF"),("❓","FAQ"),("🧠","Knowledge Base")],
    ),
    "fri": dict(
        template  = "proof",
        headline  = "From visitor to / booked lead. Auto.",
        subtext   = "Real chatbot flow — greeting, qualifying, booking. All automated.",
        chat_lines= None,
        stats     = ["24/7 Active","< 3s Reply","100% Auto","0 Missed Leads"],
    ),
    "sat": dict(
        template  = "cta",
        headline  = "Pick your / AI package.",
        subtext   = "Setup today. Leads tomorrow.",
        cta       = "DM 'INFO' sekarang",
    ),
}


def main():
    parser = argparse.ArgumentParser(description="IGEN VERITAS social visual generator")
    parser.add_argument("--type",    default="pain",
                        choices=["pain","education","proof","cta"],
                        help="Post template type")
    parser.add_argument("--week",    default="1", help="Content week (1-4)")
    parser.add_argument("--day",     default="mon",
                        choices=["mon","wed","fri","sat"],
                        help="Day of week")
    parser.add_argument("--headline",default=None)
    parser.add_argument("--subtext", default=None)
    parser.add_argument("--cta",     default="DM 'INFO' sekarang")
    args = parser.parse_args()

    stamp    = datetime.now().strftime("%Y%m%d")
    defaults = WEEK1_DEFAULTS.get(args.day, WEEK1_DEFAULTS["mon"])
    ttype    = args.type or defaults.get("template", "pain")
    headline = args.headline or defaults.get("headline", "AI that works / while you sleep.")
    subtext  = args.subtext  or defaults.get("subtext",  "IGEN VERITAS — Powering SMEs with intelligent automation.")
    cta      = args.cta      or defaults.get("cta",      "DM 'INFO' sekarang")
    day_map  = {"mon": "Mon", "wed": "Wed", "fri": "Fri", "sat": "Sat"}
    fname    = f"{stamp}_W{args.week}_{day_map[args.day]}_{ttype}.png"

    if ttype == "pain":
        template_pain_point(headline, subtext, cta, fname)
    elif ttype == "education":
        feats = defaults.get("features", None)
        template_education(headline, subtext, feats, fname)
    elif ttype == "proof":
        template_proof(headline, subtext, None, defaults.get("stats", None), fname)
    elif ttype == "cta":
        template_cta(headline, subtext, cta, fname)


if __name__ == "__main__":
    main()
