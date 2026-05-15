"""
Week 2 (May 8–14) — Pain: The real cost of missed leads
Generates 5 poster cover images: CB-005 to CB-009
"""

from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR    = r"C:\Users\jicoo\OneDrive\Documents\Claude\marketing_team"
BG_DIR      = os.path.join(BASE_DIR, "IGEN_VERITAS_Gradient_Backgrounds")
OUT_DIR     = os.path.join(BASE_DIR, "social-media")
FONTS_WIN   = "C:/Windows/Fonts"
os.makedirs(OUT_DIR, exist_ok=True)

# ── brand colours ──────────────────────────────────────────────────────────
VIOLET      = (123, 103, 209)
PURPLE      = (138,  93, 204)
BLUE_MID    = ( 72, 143, 227)
BLUE_BRIGHT = ( 65, 150, 230)
DARK_NAVY   = ( 11,  11,  20)
WHITE       = (255, 255, 255)
BODY_GRAY   = (107, 114, 128)

def get_font(size, weight="regular"):
    m = {"bold": "segoeuib.ttf", "regular": "segoeui.ttf", "light": "segoeuil.ttf"}
    p = os.path.join(FONTS_WIN, m.get(weight, "segoeui.ttf"))
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

def load_bg(filename):
    path = os.path.join(BG_DIR, filename)
    bg = Image.open(path).convert("RGBA").resize((1080, 1080), Image.LANCZOS)
    overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 120))
    return Image.alpha_composite(bg, overlay)

def brand_watermark(draw):
    font_sm = get_font(20, "regular")
    font_xs = get_font(15, "regular")
    draw.text((54, 50), "IGEN VERITAS", fill=WHITE + (230,), font=font_sm)
    draw.text((54, 76), "igenveritas.com", fill=BODY_GRAY + (200,), font=font_xs)

def bottom_strip(img, draw):
    strip = Image.new("RGBA", (1080, 56), (0, 0, 0, 0))
    sd = ImageDraw.Draw(strip)
    for x in range(1080):
        t = x / 1080
        r = int(VIOLET[0] + (BLUE_BRIGHT[0] - VIOLET[0]) * t)
        g = int(VIOLET[1] + (BLUE_BRIGHT[1] - VIOLET[1]) * t)
        b = int(VIOLET[2] + (BLUE_BRIGHT[2] - VIOLET[2]) * t)
        sd.line([(x, 0), (x, 55)], fill=(r, g, b, 220))
    font_strip = get_font(17, "regular")
    sd.text((540, 28), "Intelligent Solutions · Cutting-Edge Technology",
            fill=WHITE + (220,), font=font_strip, anchor="mm")
    img.paste(strip, (0, 1024), strip)

def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# ──────────────────────────────────────────────────────────────────────────
# CB-005  May 8 Thu — Carousel cover — Pain
# "5 signs your business is leaking money right now."
# BG: 02_Purple_Black.jpg
# ──────────────────────────────────────────────────────────────────────────
def gen_cb005():
    img = load_bg("02_Purple_Black.jpg")
    draw = ImageDraw.Draw(img)
    brand_watermark(draw)

    # Carousel badge
    draw.rounded_rectangle([856, 44, 1026, 76], radius=14,
                            fill=(*VIOLET, 200), outline=(*WHITE, 60), width=1)
    draw.text((941, 60), "CAROUSEL  ▶", fill=WHITE, font=get_font(15, "bold"), anchor="mm")

    # Main headline
    font_lg = get_font(82, "bold")
    font_md = get_font(38, "regular")
    draw.text((540, 220), "5 Signs Your", fill=WHITE, font=font_lg, anchor="mm")
    draw.text((540, 316), "Business Is", fill=(*VIOLET, 255), font=font_lg, anchor="mm")
    draw.text((540, 412), "Leaking Money", fill=WHITE, font=font_lg, anchor="mm")

    # Sub label
    draw.text((540, 482), "Right Now", fill=BODY_GRAY, font=font_md, anchor="mm")

    # 5 numbered sign cards
    signs = [
        "01  Leads go unanswered after hours",
        "02  No follow-up system in place",
        "03  Slow reply time (>30 mins)",
        "04  Leads fall through the cracks",
        "05  Zero automation = zero growth",
    ]
    card_y = 530
    font_card = get_font(24, "regular")
    for i, sign in enumerate(signs):
        y = card_y + i * 72
        draw.rounded_rectangle([80, y, 1000, y + 56], radius=12,
                                fill=(255, 255, 255, 12), outline=(255, 255, 255, 30), width=1)
        # number accent
        num_color = (*VIOLET, 255) if i % 2 == 0 else (*BLUE_MID, 255)
        draw.text((104, y + 28), sign[:2], fill=num_color, font=get_font(24, "bold"), anchor="lm")
        draw.text((148, y + 28), sign[2:], fill=WHITE, font=font_card, anchor="lm")

    # Swipe CTA
    font_sm = get_font(22, "regular")
    draw.text((540, 910), "SWIPE TO SEE EACH SIGN →", fill=(*BODY_GRAY, 220), font=font_sm, anchor="mm")

    bottom_strip(img, draw)
    out = os.path.join(OUT_DIR, "20260508_pain_CB005_5signs_leaking_money.png")
    img.save(out, "PNG")
    print(f"Saved: {out}")

# ──────────────────────────────────────────────────────────────────────────
# CB-006  May 9 Fri — Single poster — Pain
# "Every unanswered WhatsApp is a lead you handed to your competitor."
# BG: 08_Black_Purple.jpg
# ──────────────────────────────────────────────────────────────────────────
def gen_cb006():
    img = load_bg("08_Black_Purple.jpg")
    draw = ImageDraw.Draw(img)
    brand_watermark(draw)

    font_xl  = get_font(72, "bold")
    font_lg  = get_font(62, "bold")
    font_md  = get_font(30, "regular")
    font_sm  = get_font(22, "regular")
    font_xs  = get_font(18, "regular")

    # Top headline block
    draw.text((540, 160), "Every Unanswered", fill=WHITE, font=font_xl, anchor="mm")
    draw.text((540, 252), "WhatsApp", fill=(*VIOLET, 255), font=get_font(88, "bold"), anchor="mm")
    draw.text((540, 348), "Is a Lead You", fill=WHITE, font=font_lg, anchor="mm")
    draw.text((540, 432), "Handed Away.", fill=(*BLUE_MID, 255), font=font_lg, anchor="mm")

    # Phone mockup card
    card_x1, card_y1, card_x2, card_y2 = 200, 490, 880, 840
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=20,
                            fill=(255, 255, 255, 14), outline=(255, 255, 255, 40), width=1)

    # WhatsApp header bar inside card
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y1 + 56], radius=20,
                            fill=(37, 211, 102, 220))
    draw.text((card_x1 + 26, card_y1 + 28), "●  Potential Customer", fill=WHITE,
              font=get_font(20, "bold"), anchor="lm")
    draw.text((card_x2 - 20, card_y1 + 28), "Online", fill=(200, 255, 200),
              font=get_font(16, "regular"), anchor="rm")

    # Chat bubble — customer message
    bx1, by1 = card_x1 + 24, card_y1 + 76
    bx2, by2 = bx1 + 440, by1 + 70
    draw.rounded_rectangle([bx1, by1, bx2, by2], radius=14, fill=(255, 255, 255, 220))
    draw.text((bx1 + 20, by1 + 35), "Hi, are you still open? 👋", fill=DARK_NAVY,
              font=get_font(22, "regular"), anchor="lm")
    draw.text((bx2 - 14, by2 - 12), "8:47 PM", fill=BODY_GRAY, font=get_font(14, "regular"), anchor="rm")

    # Seen / no reply indicator
    draw.text((card_x1 + 24, card_y1 + 176), "Seen  ✓✓   No reply.", fill=(*BODY_GRAY, 200),
              font=get_font(20, "regular"), anchor="lm")

    # Red "0 replies" stat
    draw.rounded_rectangle([card_x1 + 24, card_y1 + 216, card_x1 + 240, card_y1 + 268],
                            radius=10, fill=(220, 50, 50, 200))
    draw.text((card_x1 + 132, card_y1 + 242), "0 replies sent", fill=WHITE,
              font=get_font(20, "bold"), anchor="mm")

    # Subtext + CTA
    draw.text((540, 876), "Don't let silence cost you your next client.", fill=BODY_GRAY,
              font=font_sm, anchor="mm")
    draw.rounded_rectangle([330, 912, 750, 958], radius=24, fill=(*VIOLET, 230))
    draw.text((540, 935), "DM us 'BOT' — automate your replies", fill=WHITE,
              font=get_font(22, "bold"), anchor="mm")

    bottom_strip(img, draw)
    out = os.path.join(OUT_DIR, "20260509_pain_CB006_unanswered_whatsapp.png")
    img.save(out, "PNG")
    print(f"Saved: {out}")

# ──────────────────────────────────────────────────────────────────────────
# CB-007  May 11 Mon — Reel hook card — Pain
# "POV: It's 2AM. A hot lead just messaged your business. Nobody replied."
# BG: 05_Black_Violet_Blue.jpg
# ──────────────────────────────────────────────────────────────────────────
def gen_cb007():
    img = load_bg("05_Black_Violet_Blue.jpg")
    draw = ImageDraw.Draw(img)
    brand_watermark(draw)

    # Cinematic letterbox bars
    draw.rectangle([0, 0, 1080, 80], fill=(0, 0, 0, 200))
    draw.rectangle([0, 1000, 1080, 1080], fill=(0, 0, 0, 200))

    # POV label
    draw.text((540, 44), "P O V", fill=(*BODY_GRAY, 240), font=get_font(28, "bold"), anchor="mm")

    # Large clock
    draw.text((540, 220), "2:17 AM", fill=WHITE, font=get_font(140, "bold"), anchor="mm")

    # Violet glow behind clock (simulate with semi-transparent circle)
    glow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r_off in range(120, 0, -10):
        alpha = int(30 * (1 - r_off / 120))
        gd.ellipse([540 - r_off * 3, 220 - r_off, 540 + r_off * 3, 220 + r_off],
                   fill=(*VIOLET, alpha))
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)

    # Main text block
    draw.text((540, 370), "A hot lead just messaged", fill=(*BODY_GRAY, 240),
              font=get_font(38, "regular"), anchor="mm")
    draw.text((540, 430), "your business.", fill=WHITE, font=get_font(52, "bold"), anchor="mm")

    # Pause beat
    draw.text((540, 530), "Nobody.", fill=(*VIOLET, 255), font=get_font(108, "bold"), anchor="mm")
    draw.text((540, 644), "Replied.", fill=WHITE, font=get_font(108, "bold"), anchor="mm")

    # Sub-line
    draw.text((540, 746), "This happens every night in Malaysian businesses.",
              fill=BODY_GRAY, font=get_font(28, "regular"), anchor="mm")

    # Notification mockup strip
    draw.rounded_rectangle([140, 792, 940, 870], radius=16,
                            fill=(255, 255, 255, 14), outline=(255, 255, 255, 30), width=1)
    draw.rounded_rectangle([158, 810, 198, 852], radius=8, fill=(37, 211, 102, 255))
    draw.text((174, 831), "W", fill=WHITE, font=get_font(22, "bold"), anchor="mm")
    draw.text((218, 820), "New Message", fill=BODY_GRAY, font=get_font(18, "regular"), anchor="lm")
    draw.text((218, 845), '"Nak tanya pasal servis korang..."', fill=WHITE,
              font=get_font(22, "regular"), anchor="lm")
    draw.text((920, 831), "2:17 AM", fill=BODY_GRAY, font=get_font(16, "regular"), anchor="rm")

    # Reel-style bottom CTA
    draw.text((540, 960), "Automate your replies — 24/7. igenveritas.com",
              fill=(*BODY_GRAY, 200), font=get_font(22, "regular"), anchor="mm")

    out = os.path.join(OUT_DIR, "20260511_pain_CB007_pov_2am_no_reply.png")
    img.save(out, "PNG")
    print(f"Saved: {out}")

# ──────────────────────────────────────────────────────────────────────────
# CB-008  May 13 Wed — Carousel cover — Education
# "Basic auto-reply vs AI chatbot — the difference will surprise you."
# BG: 07_Purple_BlueMid.jpg
# ──────────────────────────────────────────────────────────────────────────
def gen_cb008():
    img = load_bg("07_Purple_BlueMid.jpg")
    draw = ImageDraw.Draw(img)
    brand_watermark(draw)

    # Carousel badge
    draw.rounded_rectangle([856, 44, 1026, 76], radius=14,
                            fill=(*VIOLET, 200), outline=(*WHITE, 60), width=1)
    draw.text((941, 60), "CAROUSEL  ▶", fill=WHITE, font=get_font(15, "bold"), anchor="mm")

    # Main headline
    font_xl = get_font(78, "bold")
    font_lg = get_font(62, "bold")
    draw.text((540, 180), "Auto-Reply", fill=(*BODY_GRAY, 220), font=font_xl, anchor="mm")
    draw.text((540, 272), "vs", fill=WHITE, font=get_font(96, "bold"), anchor="mm")
    draw.text((540, 372), "AI Chatbot", fill=(*VIOLET, 255), font=font_xl, anchor="mm")

    # Sub line
    draw.text((540, 444), "The difference will surprise you.", fill=WHITE,
              font=get_font(34, "regular"), anchor="mm")

    # Divider
    draw.line([200, 476, 880, 476], fill=(*WHITE, 40), width=1)

    # Split comparison preview
    mid = 540
    left_x, right_x = 200, mid + 30
    col_w = 290

    # Left block — Auto-reply
    draw.rounded_rectangle([left_x, 500, mid - 20, 900], radius=16,
                            fill=(220, 50, 50, 20), outline=(220, 50, 50, 80), width=1)
    draw.text((left_x + (mid - 20 - left_x) // 2 + left_x, 530),
              "❌ Auto-Reply", fill=(255, 100, 100), font=get_font(28, "bold"), anchor="mm")

    auto_points = [
        "Fixed responses only",
        "Cannot qualify leads",
        "No follow-up logic",
        "Confuses off-script queries",
    ]
    for i, pt in enumerate(auto_points):
        y = 590 + i * 72
        draw.text((left_x + 20, y), f"• {pt}", fill=(*BODY_GRAY, 220), font=get_font(22, "regular"), anchor="lm")

    # Right block — AI chatbot
    draw.rounded_rectangle([right_x, 500, right_x + col_w + 30, 900], radius=16,
                            fill=(*VIOLET, 20), outline=(*VIOLET, 100), width=1)
    draw.text((right_x + (col_w + 30) // 2 + right_x // 10, 530),
              "✅ AI Chatbot", fill=(*VIOLET, 255), font=get_font(28, "bold"), anchor="mm")

    ai_points = [
        "Learns your business",
        "Qualifies leads live",
        "Sends follow-ups auto",
        "Handles any question",
    ]
    for i, pt in enumerate(ai_points):
        y = 590 + i * 72
        draw.text((right_x + 20, y), f"• {pt}", fill=WHITE, font=get_font(22, "regular"), anchor="lm")

    # Swipe CTA
    draw.text((540, 940), "SWIPE TO SEE THE FULL BREAKDOWN →", fill=(*BODY_GRAY, 200),
              font=get_font(22, "regular"), anchor="mm")

    bottom_strip(img, draw)
    out = os.path.join(OUT_DIR, "20260513_education_CB008_autoreply_vs_chatbot.png")
    img.save(out, "PNG")
    print(f"Saved: {out}")

# ──────────────────────────────────────────────────────────────────────────
# CB-009  May 14 Thu — Engagement post — Pain
# "Real talk: have you ever lost a customer because you replied too late?"
# BG: 04_Violet_Purple.jpg
# ──────────────────────────────────────────────────────────────────────────
def gen_cb009():
    img = load_bg("04_Violet_Purple.jpg")
    draw = ImageDraw.Draw(img)
    brand_watermark(draw)

    font_xl = get_font(78, "bold")
    font_lg = get_font(54, "bold")
    font_md = get_font(36, "regular")
    font_sm = get_font(26, "regular")

    # Top tag
    draw.rounded_rectangle([380, 108, 700, 152], radius=20, fill=(*BLUE_MID, 180))
    draw.text((540, 130), "REAL TALK", fill=WHITE, font=get_font(26, "bold"), anchor="mm")

    # Main question
    draw.text((540, 240), "Have You Ever", fill=WHITE, font=font_xl, anchor="mm")
    draw.text((540, 336), "Lost a Customer", fill=(*VIOLET, 255), font=get_font(82, "bold"), anchor="mm")

    draw.text((540, 430), "Because You", fill=WHITE, font=font_xl, anchor="mm")
    draw.text((540, 524), "Replied Too Late?", fill=WHITE, font=font_lg, anchor="mm")

    # Glassmorphism card
    draw.rounded_rectangle([140, 580, 940, 720], radius=20,
                            fill=(255, 255, 255, 14), outline=(255, 255, 255, 40), width=1)
    draw.text((540, 620), "Be honest with yourself.", fill=BODY_GRAY, font=font_md, anchor="mm")
    draw.text((540, 680), "Most businesses have. Yours doesn't have to.",
              fill=WHITE, font=get_font(28, "regular"), anchor="mm")

    # Emoji engagement CTA
    draw.text((540, 776), "Drop a 🙋 below if this has happened to you.",
              fill=WHITE, font=font_md, anchor="mm")

    # Reaction pills
    pill_data = [("🙋 Yes", VIOLET), ("🤔 Maybe", PURPLE), ("❌ Never", (60, 60, 80))]
    px_starts = [200, 430, 660]
    for (label, color), px in zip(pill_data, px_starts):
        draw.rounded_rectangle([px, 830, px + 210, 882], radius=24, fill=(*color, 200))
        draw.text((px + 105, 856), label, fill=WHITE, font=get_font(26, "bold"), anchor="mm")

    # CTA strip
    draw.text((540, 940), "There's a better way. DM us 'BOT' to find out.",
              fill=BODY_GRAY, font=get_font(24, "regular"), anchor="mm")

    bottom_strip(img, draw)
    out = os.path.join(OUT_DIR, "20260514_engagement_CB009_lost_customer_late_reply.png")
    img.save(out, "PNG")
    print(f"Saved: {out}")

# ──────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating Week 2 posts…")
    gen_cb005()
    gen_cb006()
    gen_cb007()
    gen_cb008()
    gen_cb009()
    print("Done — all 5 Week 2 posters saved to social-media/")
