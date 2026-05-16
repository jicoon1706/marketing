"""CB-013 v2 — Website mockup version with browser window UI in both panels."""

from PIL import Image, ImageDraw, ImageFilter
import os

FONT_DIR = r"C:\Users\jicoo\.claude\plugins\cache\anthropic-agent-skills\document-skills\f458cee31a75\skills\canvas-design\canvas-fonts"
OUT_PATH = r"c:\Users\jicoo\OneDrive\IGEN VERITAS TECHNOLOGIES\marketing_team\social-media\CB-013_education_v2.png"

W, H = 1080, 1080

DARK_BG     = (11, 11, 20)
VIOLET      = (123, 103, 209)
PURPLE      = (138, 93, 204)
BLUE_MID    = (72, 143, 227)
WHITE       = (255, 255, 255)
MUTED_RED   = (190, 65, 65)
BODY_GRAY   = (107, 114, 128)
LIGHT_GRAY  = (200, 200, 210)


def font(name, size):
    from PIL import ImageFont
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def centered_text(draw, text, x_center, y, fnt, color):
    bb = draw.textbbox((0, 0), text, font=fnt)
    tw = bb[2] - bb[0]
    draw.text((x_center - tw // 2, y), text, font=fnt, fill=color)


def gradient_v(draw, x0, y0, x1, y1, c_top, c_bot):
    for y in range(y0, y1):
        t = (y - y0) / max(y1 - y0 - 1, 1)
        r = int(c_top[0] + (c_bot[0] - c_top[0]) * t)
        g = int(c_top[1] + (c_bot[1] - c_top[1]) * t)
        b = int(c_top[2] + (c_bot[2] - c_top[2]) * t)
        draw.line([(x0, y), (x1, y)], fill=(r, g, b))


def gradient_h(draw, x0, y0, x1, y1, c_l, c_r):
    for x in range(x0, x1):
        t = (x - x0) / max(x1 - x0 - 1, 1)
        r = int(c_l[0] + (c_r[0] - c_l[0]) * t)
        g = int(c_l[1] + (c_r[1] - c_l[1]) * t)
        b = int(c_l[2] + (c_r[2] - c_l[2]) * t)
        draw.line([(x, y0), (x, y1)], fill=(r, g, b))


# ── BROWSER CHROME (top bar with dots + url bar) ─────────────────────────────
def draw_browser_chrome(draw, x, y, w, bg, dot_colors, url_text, url_bg, f_url):
    bar_h = 36
    draw.rounded_rectangle([x, y, x+w, y+bar_h], radius=6, fill=bg)
    # traffic light dots
    for i, dc in enumerate(dot_colors):
        cx = x + 14 + i * 18
        cy = y + bar_h // 2
        draw.ellipse([cx-5, cy-5, cx+5, cy+5], fill=dc)
    # url bar
    ub_x = x + 68
    ub_w = w - 80
    draw.rounded_rectangle([ub_x, y+6, ub_x+ub_w, y+bar_h-6], radius=4, fill=url_bg)
    bb = draw.textbbox((0,0), url_text, font=f_url)
    tw = bb[2]-bb[0]
    draw.text((ub_x + (ub_w - tw)//2, y + 10), url_text, font=f_url, fill=BODY_GRAY)
    return y + bar_h


# ── OUTDATED WEBSITE MOCKUP ───────────────────────────────────────────────────
def draw_outdated_site(draw, img, x, y, w, h, fonts):
    f_sm, f_md, f_lg, f_btn = fonts

    # body bg — off-white/grey
    draw.rectangle([x, y, x+w, y+h], fill=(235, 232, 228))

    # -- nav bar: clunky, too many items
    nav_h = 28
    draw.rectangle([x, y, x+w, y+nav_h], fill=(60, 60, 70))
    nav_items = ["Home", "About", "Services", "Gallery", "Products", "News", "FAQ", "Contact"]
    ni_x = x + 4
    for item in nav_items:
        bb = draw.textbbox((0,0), item, font=f_sm)
        iw = bb[2]-bb[0]
        draw.text((ni_x, y + 7), item, font=f_sm, fill=(200,200,200))
        ni_x += iw + 8

    # -- hero: bad centred text on ugly gradient
    hero_h = 80
    gradient_v(draw, x, y+nav_h, x+w, y+nav_h+hero_h, (100, 40, 40), (60, 30, 80))
    draw.text((x+10, y+nav_h+8), "WELCOME TO OUR WEBSITE!!!", font=f_sm, fill=(255, 255, 0))
    draw.text((x+10, y+nav_h+26), "We provide the BEST services in town", font=f_sm, fill=(255,255,255))
    # ugly button
    draw.rectangle([x+10, y+nav_h+50, x+110, y+nav_h+68], fill=(255,165,0))
    draw.text((x+14, y+nav_h+54), "CLICK HERE NOW!!", font=f_sm, fill=(0,0,0))

    # -- body: three misaligned columns
    col_y = y + nav_h + hero_h + 6
    col_h = 140
    col_w = (w - 16) // 3

    for ci in range(3):
        cx = x + 4 + ci*(col_w+4)
        # box with different colored borders (mismatched)
        bcolors = [(200,0,0),(0,0,200),(0,150,0)]
        draw.rectangle([cx, col_y, cx+col_w, col_y+col_h], fill=(248,245,240), outline=bcolors[ci], width=2)
        # fake image placeholder (grey box)
        draw.rectangle([cx+4, col_y+4, cx+col_w-4, col_y+50], fill=(180,175,170))
        draw.line([cx+4, col_y+4, cx+col_w-4, col_y+50], fill=(150,145,140), width=1)
        draw.line([cx+col_w-4, col_y+4, cx+4, col_y+50], fill=(150,145,140), width=1)
        # mismatched font sizes
        draw.text((cx+4, col_y+54), f"Product {ci+1}", font=f_sm, fill=(0,0,128))
        # walls of tiny text
        for row in range(5):
            draw.text((cx+4, col_y+70+row*12), "Lorem ipsum dolor sit amet consectetur", font=f_sm, fill=(60,60,60))

    # -- enquiry / contact section: ugly form
    form_y = col_y + col_h + 8
    draw.rectangle([x, form_y, x+w, form_y+60], fill=(220, 215, 205))
    draw.text((x+6, form_y+4), "ENQUIRY FORM", font=f_sm, fill=(100,0,0))
    # fake form fields
    for fi, lbl in enumerate(["Name:", "Email:", "Message:"]):
        fy = form_y + 16 + fi*14
        draw.text((x+4, fy), lbl, font=f_sm, fill=(60,60,60))
        draw.rectangle([x+44, fy, x+w-4, fy+11], fill=WHITE, outline=(160,155,150), width=1)

    # -- visitor counter + animation notice
    ctr_y = form_y + 68
    draw.rectangle([x, ctr_y, x+w, ctr_y+22], fill=(200,195,185))
    draw.text((x+4, ctr_y+5), "Visitor #00047821  |  Best viewed in Internet Explorer 8", font=f_sm, fill=(80,80,80))

    # -- ugly news ticker
    ticker_y = ctr_y + 26
    draw.rectangle([x, ticker_y, x+w, ticker_y+18], fill=(255,200,0))
    draw.text((x+4, ticker_y+4), "*** SPECIAL PROMO *** CALL NOW *** LIMITED TIME ***", font=f_sm, fill=(150,0,0))

    # -- pop-up overlay (simulating annoying popup)
    popup_y = ticker_y + 24
    draw.rectangle([x+30, popup_y, x+w-30, popup_y+50], fill=(255,252,240), outline=(180,40,40), width=2)
    draw.rectangle([x+30, popup_y, x+w-30, popup_y+14], fill=(180,40,40))
    draw.text((x+34, popup_y+2), "SUBSCRIBE TO OUR NEWSLETTER!!!", font=f_sm, fill=WHITE)
    draw.text((x+34, popup_y+18), "Enter your email to win a FREE gift!", font=f_sm, fill=(60,60,60))
    draw.rectangle([x+34, popup_y+32, x+w-70, popup_y+44], fill=WHITE, outline=(180,180,180), width=1)
    draw.rounded_rectangle([x+w-66, popup_y+32, x+w-34, popup_y+44], radius=3, fill=(40,100,200))
    draw.text((x+w-64, popup_y+34), "Submit", font=f_sm, fill=WHITE)

    # -- footer: ugly, cluttered
    ft_y = y + h - 28
    draw.rectangle([x, ft_y, x+w, y+h], fill=(40,40,40))
    draw.text((x+4, ft_y+6), "Copyright 2009 | All Rights Reserved | Tel: 03-12345678 | info@mybiz.net", font=f_sm, fill=(160,160,160))

    # -- NOT SECURE badge overlaid on browser chrome area
    draw.rounded_rectangle([x+4, y+nav_h+hero_h+8, x+90, y+nav_h+hero_h+22], radius=3, fill=(180,40,40))
    draw.text((x+8, y+nav_h+hero_h+10), "! NOT SECURE", font=f_sm, fill=WHITE)


# ── MODERN WEBSITE MOCKUP ─────────────────────────────────────────────────────
def draw_modern_site(draw, img, x, y, w, h, fonts):
    f_sm, f_md, f_lg, f_btn = fonts

    # body bg — clean white
    draw.rectangle([x, y, x+w, y+h], fill=(252, 252, 255))

    # -- nav bar: clean minimal
    nav_h = 30
    draw.rectangle([x, y, x+w, y+nav_h], fill=WHITE)
    draw.line([(x, y+nav_h), (x+w, y+nav_h)], fill=(230,230,240), width=1)
    # logo mark
    draw.rounded_rectangle([x+8, y+7, x+30, y+23], radius=4, fill=VIOLET)
    draw.text((x+10, y+9), "IV", font=f_sm, fill=WHITE)
    # minimal nav items
    nav_items = ["Home", "Services", "Work", "Contact"]
    ni_x = x + 40
    for item in nav_items:
        bb = draw.textbbox((0,0), item, font=f_sm)
        draw.text((ni_x, y+9), item, font=f_sm, fill=(60,60,80))
        ni_x += bb[2]-bb[0] + 16
    # CTA button in nav
    draw.rounded_rectangle([x+w-62, y+7, x+w-6, y+23], radius=8, fill=VIOLET)
    draw.text((x+w-58, y+9), "Get Started", font=f_sm, fill=WHITE)

    # -- hero section: clean gradient + headline
    hero_h = 88
    gradient_v(draw, x, y+nav_h, x+w, y+nav_h+hero_h, (245, 240, 255), (232, 225, 255))
    draw.text((x+12, y+nav_h+10), "Grow Your Business", font=f_lg, fill=(30,20,60))
    draw.text((x+12, y+nav_h+36), "with intelligent technology.", font=f_md, fill=VIOLET)
    draw.text((x+12, y+nav_h+58), "AI · Web · Mobile — built for Malaysian SMEs", font=f_sm, fill=BODY_GRAY)
    # small CTA
    draw.rounded_rectangle([x+12, y+nav_h+72, x+100, y+nav_h+86], radius=6, fill=VIOLET)
    draw.text((x+16, y+nav_h+74), "Explore Now", font=f_sm, fill=WHITE)

    # -- 3 feature cards
    card_y = y + nav_h + hero_h + 8
    card_h = 72
    card_labels = ["AI Chatbot", "Website", "Mobile App"]
    card_descs  = ["24/7 lead capture", "Fast & mobile-ready", "iOS & Android"]
    card_colors = [VIOLET, PURPLE, BLUE_MID]
    card_w = (w - 16) // 3

    for ci, (lbl, desc, cc) in enumerate(zip(card_labels, card_descs, card_colors)):
        cx = x + 4 + ci*(card_w+4)
        draw.rounded_rectangle([cx, card_y, cx+card_w, card_y+card_h], radius=8, fill=WHITE, outline=(230,225,245), width=1)
        # colour accent bar at top
        draw.rounded_rectangle([cx, card_y, cx+card_w, card_y+4], radius=2, fill=cc)
        draw.text((cx+8, card_y+10), lbl, font=f_md, fill=(30,20,60))
        draw.text((cx+8, card_y+30), desc, font=f_sm, fill=BODY_GRAY)
        # mini icon circle
        draw.ellipse([cx+8, card_y+44, cx+22, card_y+58], fill=(*cc, 40), outline=cc, width=1)
        draw.text((cx+10, card_y+45), ">>", font=f_sm, fill=cc)

    # -- testimonial / social proof strip
    proof_y = card_y + card_h + 8
    draw.rounded_rectangle([x+4, proof_y, x+w-4, proof_y+44], radius=8, fill=(248,246,255), outline=(220,215,240), width=1)
    draw.text((x+12, proof_y+6), "* * * * *", font=f_sm, fill=(255,180,0))
    draw.text((x+12, proof_y+22), '"Got 11 leads in the first week. Game changer."', font=f_sm, fill=(50,40,80))
    draw.text((x+w-70, proof_y+18), "— Amir, KL", font=f_sm, fill=BODY_GRAY)

    # -- stats section
    stats_y = proof_y + 52
    draw.rounded_rectangle([x+4, stats_y, x+w-4, stats_y+52], radius=8, fill=(30,20,60))
    for si, (num, lbl) in enumerate([("3s", "Load Time"), ("99%", "Uptime"), ("2x", "Conversions")]):
        sx = x + 20 + si * ((w - 24) // 3)
        draw.text((sx, stats_y+6), num, font=f_lg, fill=WHITE)
        draw.text((sx, stats_y+30), lbl, font=f_sm, fill=(180,170,210))
    # dividers
    for si in range(1, 3):
        dx = x + 4 + si * ((w - 8) // 3)
        draw.line([(dx, stats_y+8), (dx, stats_y+44)], fill=(80,70,120), width=1)

    # -- live chat widget
    chat_y = stats_y + 60
    draw.rounded_rectangle([x+4, chat_y, x+w-4, chat_y+40], radius=8, fill=(255,255,255), outline=(220,215,240), width=1)
    draw.ellipse([x+14, chat_y+10, x+30, chat_y+30], fill=VIOLET)
    draw.text((x+14, chat_y+12), "IV", font=f_sm, fill=WHITE)
    draw.text((x+36, chat_y+8), "Hi! How can we help you today?", font=f_sm, fill=(40,30,70))
    draw.text((x+36, chat_y+22), "Typically replies in under 3 seconds", font=f_sm, fill=BODY_GRAY)

    # -- process steps
    proc_y = chat_y + 48
    draw.text((x+8, proc_y), "How it works:", font=f_md, fill=(40,30,70))
    steps = ["01  Discovery Call", "02  Design & Build", "03  Launch & Grow"]
    for si, step in enumerate(steps):
        sy = proc_y + 16 + si * 18
        draw.rounded_rectangle([x+4, sy, x+w-4, sy+14], radius=4, fill=(245,242,255))
        draw.text((x+10, sy+2), step, font=f_sm, fill=(80,60,160))

    # -- CTA bar
    cta_y = proc_y + 76
    draw.rounded_rectangle([x+4, cta_y, x+w-4, cta_y+28], radius=8, fill=VIOLET)
    centered_text(draw, "DM us 'WEBSITE' to get started", (x + x+w)//2, cta_y+8, f_sm, WHITE)

    # -- footer: clean
    ft_y = y + h - 22
    draw.rectangle([x, ft_y, x+w, y+h], fill=(30,20,60))
    draw.text((x+8, ft_y+4), "IGEN VERITAS  ·  igenveritas.com  ·  +60 17 310 3966", font=f_sm, fill=(180,170,210))


# ── MAIN ─────────────────────────────────────────────────────────────────────
def build():
    img = Image.new("RGBA", (W, H), DARK_BG + (255,))
    draw = ImageDraw.Draw(img, "RGBA")

    MID = W // 2
    PANEL_TOP = 0
    FOOTER_H  = 110
    HEADLINE_H = 210
    PANEL_BOT = H - FOOTER_H - HEADLINE_H

    # fonts
    f_label    = font("WorkSans-Bold.ttf", 22)
    f_headline = font("BigShoulders-Bold.ttf", 52)
    f_sub      = font("InstrumentSans-Regular.ttf", 24)
    f_sm_site  = font("WorkSans-Regular.ttf", 9)
    f_md_site  = font("WorkSans-Bold.ttf", 12)
    f_lg_site  = font("BigShoulders-Bold.ttf", 18)
    f_btn_site = font("WorkSans-Bold.ttf", 9)
    site_fonts = (f_sm_site, f_md_site, f_lg_site, f_btn_site)

    f_url = font("DMMono-Regular.ttf", 10)
    f_domain = font("InstrumentSans-Regular.ttf", 18)
    f_brand  = font("BigShoulders-Bold.ttf", 32)
    f_tagline = font("WorkSans-Regular.ttf", 14)

    # ── PANEL BACKGROUNDS ─────────────────────────────────────────────────
    # Left: dark navy-purple
    gradient_v(draw, 0, PANEL_TOP, MID, PANEL_BOT, (22, 14, 44), (10, 8, 26))
    # Right: violet → blue
    gradient_h(draw, MID, PANEL_TOP, W, PANEL_BOT, (95, 55, 180), (38, 110, 220))

    # subtle dot grids
    for gx in range(0, W, 24):
        for gy in range(PANEL_TOP, PANEL_BOT, 24):
            alpha = 25 if gx < MID else 18
            draw.point((gx, gy), fill=(255, 255, 255, alpha))

    # ── PANEL LABELS ─────────────────────────────────────────────────────
    draw.text((36, 26), "OUTDATED", font=f_label, fill=(*MUTED_RED, 220))
    draw.line([(36, 52), (182, 52)], fill=(*MUTED_RED, 80), width=1)

    draw.text((MID + 36, 26), "MODERN", font=f_label, fill=(*WHITE, 230))
    draw.line([(MID+36, 52), (MID+36+108, 52)], fill=(*WHITE, 60), width=1)

    # ── BROWSER CHROME — LEFT (outdated look: dark grey, no SSL) ─────────
    BROWSER_MARGIN = 28
    BROWSER_X_L  = BROWSER_MARGIN
    BROWSER_W_L  = MID - BROWSER_MARGIN * 2
    CHROME_Y_L   = 68
    dot_colors_old = [(200,50,50), (200,150,40), (80,80,80)]

    chrome_bot_l = draw_browser_chrome(
        draw, BROWSER_X_L, CHROME_Y_L, BROWSER_W_L,
        bg=(55, 50, 65),
        dot_colors=dot_colors_old,
        url_text="http://mybusiness.net (Not Secure)",
        url_bg=(38, 34, 48),
        f_url=f_url
    )

    # site content area
    SITE_H_L = PANEL_BOT - chrome_bot_l - 14
    draw.rectangle([BROWSER_X_L, chrome_bot_l, BROWSER_X_L+BROWSER_W_L, chrome_bot_l+SITE_H_L],
                   fill=(235, 232, 228))
    draw_outdated_site(draw, img,
                       BROWSER_X_L, chrome_bot_l,
                       BROWSER_W_L, SITE_H_L,
                       site_fonts)

    # browser drop shadow
    shadow = Image.new("RGBA", (W, H), (0,0,0,0))
    sd = ImageDraw.Draw(shadow)
    sd.rectangle([BROWSER_X_L+4, CHROME_Y_L+4,
                  BROWSER_X_L+BROWSER_W_L+4, chrome_bot_l+SITE_H_L+4],
                 fill=(0, 0, 0, 60))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    img.alpha_composite(shadow)
    draw = ImageDraw.Draw(img, "RGBA")

    # browser border
    draw.rounded_rectangle([BROWSER_X_L, CHROME_Y_L,
                             BROWSER_X_L+BROWSER_W_L, chrome_bot_l+SITE_H_L],
                            radius=6, outline=(80, 70, 100, 180), width=1)

    # ── BROWSER CHROME — RIGHT (modern: light, green lock) ───────────────
    BROWSER_X_R = MID + BROWSER_MARGIN
    BROWSER_W_R = MID - BROWSER_MARGIN * 2
    CHROME_Y_R  = 68
    dot_colors_new = [(255,90,80), (255,185,0), (40,200,70)]

    chrome_bot_r = draw_browser_chrome(
        draw, BROWSER_X_R, CHROME_Y_R, BROWSER_W_R,
        bg=(245, 244, 248),
        dot_colors=dot_colors_new,
        url_text="https://igenveritas.com",
        url_bg=(255, 255, 255),
        f_url=f_url
    )

    SITE_H_R = PANEL_BOT - chrome_bot_r - 14
    draw.rectangle([BROWSER_X_R, chrome_bot_r, BROWSER_X_R+BROWSER_W_R, chrome_bot_r+SITE_H_R],
                   fill=(252, 252, 255))
    draw_modern_site(draw, img,
                     BROWSER_X_R, chrome_bot_r,
                     BROWSER_W_R, SITE_H_R,
                     site_fonts)

    # browser drop shadow
    shadow2 = Image.new("RGBA", (W, H), (0,0,0,0))
    sd2 = ImageDraw.Draw(shadow2)
    sd2.rectangle([BROWSER_X_R+4, CHROME_Y_R+4,
                   BROWSER_X_R+BROWSER_W_R+4, chrome_bot_r+SITE_H_R+4],
                  fill=(0, 0, 0, 80))
    shadow2 = shadow2.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(shadow2)
    draw = ImageDraw.Draw(img, "RGBA")

    draw.rounded_rectangle([BROWSER_X_R, CHROME_Y_R,
                             BROWSER_X_R+BROWSER_W_R, chrome_bot_r+SITE_H_R],
                            radius=6, outline=(180, 170, 220, 120), width=1)

    # ── CENTRE DIVIDER ────────────────────────────────────────────────────
    div_layer = Image.new("RGBA", (W, H), (0,0,0,0))
    dd = ImageDraw.Draw(div_layer)
    dd.line([(MID, 0), (MID, PANEL_BOT)], fill=(200, 185, 255, 50), width=16)
    div_layer = div_layer.filter(ImageFilter.GaussianBlur(8))
    img.alpha_composite(div_layer)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.line([(MID, 0), (MID, PANEL_BOT)], fill=(*WHITE, 200), width=2)

    # ── HEADLINE BAND ─────────────────────────────────────────────────────
    HB_TOP = PANEL_BOT
    gradient_v(draw, 0, HB_TOP, W, H - FOOTER_H, (14, 10, 32), DARK_BG)
    draw.line([(60, HB_TOP + 14), (W-60, HB_TOP + 14)], fill=(80, 65, 120, 80), width=1)

    hl_y = HB_TOP + 28
    line1 = "Your website is either building trust"
    line2 = "— or costing you clients."
    line_sub = "There is no middle ground."

    centered_text(draw, line1, W//2, hl_y, f_headline, WHITE)
    centered_text(draw, line2, W//2, hl_y + 62, f_headline, VIOLET)
    centered_text(draw, line_sub, W//2, hl_y + 132, f_sub, (*BODY_GRAY, 255))

    # ── FOOTER ────────────────────────────────────────────────────────────
    FT = H - FOOTER_H
    draw.rectangle([0, FT, W, H], fill=DARK_BG + (255,))
    draw.line([(0, FT), (W, FT)], fill=(60, 48, 90, 200), width=1)

    draw.text((60, FT + 26), "IGEN VERITAS", font=f_brand, fill=(*WHITE, 240))
    draw.ellipse([224, FT + 36, 232, FT + 44], fill=VIOLET)
    bb = draw.textbbox((0,0), "igenveritas.com", font=f_domain)
    draw.text((W - 60 - (bb[2]-bb[0]), FT + 34), "igenveritas.com", font=f_domain, fill=(*BODY_GRAY, 200))
    draw.text((60, FT + 70), "Intelligent Solutions  ·  Web & Mobile  ·  AI Automation", font=f_tagline, fill=(*BODY_GRAY, 160))

    # ── SAVE ─────────────────────────────────────────────────────────────
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    img.convert("RGB").save(OUT_PATH, "PNG", quality=95)
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    build()
