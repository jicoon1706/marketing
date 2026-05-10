"""
IGEN VERITAS — May 2026 Instagram Visuals Generator
Generates all 14 Instagram post graphics from CB-006 to CB-023.
Output: content/prototype/may 2026/
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ─── Paths ────────────────────────────────────────────────────────────────────
OUTPUT_DIR = r"C:\Users\jicoo\OneDrive\Documents\Claude\marketing_team\content\prototype\may 2026"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Brand Colors (RGBA tuples) ───────────────────────────────────────────────
VIOLET       = (123, 103, 209, 255)
VIOLET_MID   = (123, 103, 209, 180)
PURPLE       = (138,  93, 204, 255)
BLUE_MID     = ( 72, 143, 227, 255)
BLUE_BRIGHT  = ( 65, 150, 230, 255)
DARK_NAVY    = ( 11,  11,  20, 255)
WHITE        = (255, 255, 255, 255)
WHITE_DIM    = (255, 255, 255, 200)
BODY_GRAY    = (107, 114, 128, 230)
GLASS_FILL   = (255, 255, 255,  18)
GLASS_BORDER = (255, 255, 255,  45)
DARK_CARD    = ( 11,  11,  20, 200)

# ─── Fonts ────────────────────────────────────────────────────────────────────
def fnt(size, weight="regular"):
    paths = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    p = paths.get(weight, paths["regular"])
    return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()

# ─── Gradient helpers ─────────────────────────────────────────────────────────
def draw_gradient(draw, w, h, c1, c2, diagonal=False):
    for i in range(h):
        t = i / h
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        draw.line([(0, i), (w, i)], fill=(r, g, b, 255))

def draw_radial_glow(draw, cx, cy, max_r, color_rgb, max_alpha=40):
    for r in range(max_r, 0, -12):
        a = int(max_alpha * (1 - r / max_r))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color_rgb, a))

# ─── Shared decorators ────────────────────────────────────────────────────────
def brand_top(draw):
    draw.text((60, 48), "IGEN VERITAS", fill=WHITE, font=fnt(30, "bold"))
    draw.text((60, 86), "igenveritas.com", fill=BODY_GRAY, font=fnt(22, "regular"))

def brand_bottom(draw):
    draw.text((540, 1048), "igenveritas.com  ·  info@igenveritas.com", fill=BODY_GRAY,
              font=fnt(22, "regular"), anchor="mm")

def pill_button(draw, cx, cy, w, h, color, text, font_size=28):
    x1, y1 = cx - w // 2, cy - h // 2
    draw.rounded_rectangle([x1, y1, x1 + w, y1 + h], radius=h // 2, fill=color)
    draw.text((cx, cy), text, fill=WHITE, font=fnt(font_size, "bold"), anchor="mm")

def glass_card(draw, x1, y1, x2, y2, r=24):
    draw.rounded_rectangle([x1, y1, x2, y2], radius=r,
                            fill=GLASS_FILL, outline=GLASS_BORDER, width=2)

def divider_line(draw, y, x1=80, x2=1000):
    draw.line([(x1, y), (x2, y)], fill=(255, 255, 255, 40), width=1)

def save(img, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    img.convert("RGB").save(path, "PNG")
    print(f"  OK  {filename}")

# ═════════════════════════════════════════════════════════════════════════════
# TEMPLATE A — Pain Point  (dark navy, violet glow)
# ═════════════════════════════════════════════════════════════════════════════
def tmpl_pain(filename, headline_lines, bullet_lines, subtext, cta="DM us 'BOT' to learn more"):
    img = Image.new("RGBA", (1080, 1080), DARK_NAVY)
    draw = ImageDraw.Draw(img, "RGBA")

    # Violet radial glow center-left
    draw_radial_glow(draw, 120, 500, 500, (123, 103, 209), max_alpha=50)
    # Faint blue glow right
    draw_radial_glow(draw, 980, 300, 300, (65, 150, 230), max_alpha=25)

    brand_top(draw)

    # Headline
    fh = fnt(84, "bold")
    y = 195
    for i, line in enumerate(headline_lines):
        col = VIOLET if i == 1 else WHITE
        draw.text((540, y), line, fill=col, font=fh, anchor="mm")
        y += 105

    # Glassmorphism card
    card_top = y + 30
    card_bot = card_top + len(bullet_lines) * 72 + 40
    glass_card(draw, 90, card_top, 990, card_bot, r=28)

    fb = fnt(34, "regular")
    by = card_top + 55
    for line in bullet_lines:
        draw.text((140, by), line, fill=WHITE_DIM, font=fb, anchor="lm")
        by += 72

    # Subtext
    draw.text((540, card_bot + 55), subtext, fill=BODY_GRAY, font=fnt(30, "regular"), anchor="mm")

    # CTA pill
    pill_button(draw, 540, card_bot + 120, 560, 62, VIOLET, cta, 26)

    brand_bottom(draw)
    save(img, filename)


# ═════════════════════════════════════════════════════════════════════════════
# TEMPLATE B — Education  (violet→blue gradient, checklist)
# ═════════════════════════════════════════════════════════════════════════════
def tmpl_edu(filename, headline_lines, points, subtext,
             cta="DM 'BOT' to get started", service_badge=None):
    img = Image.new("RGBA", (1080, 1080))
    draw = ImageDraw.Draw(img, "RGBA")

    draw_gradient(draw, 1080, 1080, (123, 103, 209), (65, 150, 230))

    # Top dark overlay for contrast
    draw.rectangle([0, 0, 1080, 300], fill=(11, 11, 20, 170))

    brand_top(draw)

    if service_badge:
        draw.rounded_rectangle([820, 44, 1020, 84], radius=20,
                                fill=(65, 150, 230, 200))
        draw.text((920, 64), service_badge, fill=WHITE, font=fnt(22, "bold"), anchor="mm")

    # Headline
    fh = fnt(78, "bold")
    y = 170
    for line in headline_lines:
        draw.text((540, y), line, fill=WHITE, font=fh, anchor="mm")
        y += 95

    # Feature rows
    fp = fnt(33, "regular")
    row_y = y + 20
    row_h = 90
    for point in points:
        glass_card(draw, 80, row_y - 32, 1000, row_y + 48, r=16)
        # Check icon circle
        draw.ellipse([106, row_y - 20, 148, row_y + 22], fill=(*BLUE_BRIGHT[:3], 220))
        draw.text((127, row_y + 1), "v", fill=WHITE, font=fnt(26, "bold"), anchor="mm")
        draw.text((178, row_y + 1), point, fill=WHITE_DIM, font=fp, anchor="lm")

        row_y += row_h

    # Subtext
    draw.text((540, row_y + 18), subtext, fill=WHITE_DIM,
              font=fnt(27, "regular"), anchor="mm")

    # CTA
    pill_button(draw, 540, row_y + 88, 640, 64, DARK_CARD, cta, 26)

    brand_bottom(draw)
    save(img, filename)


# ═════════════════════════════════════════════════════════════════════════════
# TEMPLATE C — Social Proof  (purple gradient, stats, story card)
# ═════════════════════════════════════════════════════════════════════════════
def tmpl_proof(filename, headline_lines, story_lines, stats, cta="DM us 'BOT'"):
    img = Image.new("RGBA", (1080, 1080))
    draw = ImageDraw.Draw(img, "RGBA")

    draw_gradient(draw, 1080, 1080, (138, 93, 204), (123, 103, 209))
    draw_radial_glow(draw, 900, 900, 400, (65, 150, 230), max_alpha=30)

    brand_top(draw)

    # Headline
    fh = fnt(78, "bold")
    y = 175
    for line in headline_lines:
        draw.text((540, y), line, fill=WHITE, font=fh, anchor="mm")
        y += 96

    # Story card
    card_h = len(story_lines) * 48 + 60
    glass_card(draw, 80, y + 20, 1000, y + 20 + card_h, r=24)
    ly = y + 50
    for sl in story_lines:
        draw.text((540, ly), sl, fill=WHITE_DIM, font=fnt(30, "regular"), anchor="mm")
        ly += 48
    y = y + 20 + card_h

    # Stats row
    y += 30
    sw = (1000 - 80) // len(stats) - 16
    sx = 80
    for label, val in stats:
        draw.rounded_rectangle([sx, y, sx + sw, y + 120], radius=16,
                                fill=GLASS_FILL, outline=GLASS_BORDER, width=1)
        draw.text((sx + sw // 2, y + 42), val, fill=WHITE,
                  font=fnt(38, "bold"), anchor="mm")
        draw.text((sx + sw // 2, y + 88), label, fill=BODY_GRAY,
                  font=fnt(22, "regular"), anchor="mm")
        sx += sw + 16
    y += 140

    # CTA
    pill_button(draw, 540, y + 40, 560, 64, DARK_CARD, cta, 27)

    brand_bottom(draw)
    save(img, filename)


# ═════════════════════════════════════════════════════════════════════════════
# TEMPLATE D — Package / CTA  (violet→purple, 3-column cards)
# ═════════════════════════════════════════════════════════════════════════════
def tmpl_pkg(filename, headline_lines, packages, cta, hl_font_size=72):
    img = Image.new("RGBA", (1080, 1080))
    draw = ImageDraw.Draw(img, "RGBA")

    draw_gradient(draw, 1080, 1080, (123, 103, 209), (138, 93, 204))

    brand_top(draw)

    fh = fnt(hl_font_size, "bold")
    y = 155
    for line in headline_lines:
        draw.text((540, y), line, fill=WHITE, font=fh, anchor="mm")
        y += hl_font_size + 14

    # Package cards
    n = len(packages)
    card_w = 305
    gap = 28
    total_w = n * card_w + (n - 1) * gap
    cx = (1080 - total_w) // 2
    card_top = y + 30
    card_bot = card_top + 420

    for i, pkg in enumerate(packages):
        x1 = cx + i * (card_w + gap)
        x2 = x1 + card_w
        featured = pkg.get("featured", False)

        if featured:
            # Glow border effect
            draw.rounded_rectangle([x1 - 3, card_top - 3, x2 + 3, card_bot + 3],
                                   radius=23, fill=(*BLUE_MID[:3], 100))
            # "POPULAR" badge
            bw, bh = 120, 30
            draw.rounded_rectangle([x1 + card_w // 2 - bw // 2, card_top - 18,
                                     x1 + card_w // 2 + bw // 2, card_top + 18],
                                    radius=14, fill=BLUE_MID)
            draw.text((x1 + card_w // 2, card_top), "POPULAR",
                      fill=WHITE, font=fnt(18, "bold"), anchor="mm")

        draw.rounded_rectangle([x1, card_top, x2, card_bot], radius=20,
                               fill=GLASS_FILL if not featured else (255, 255, 255, 28),
                               outline=GLASS_BORDER if not featured else BLUE_MID,
                               width=1 if not featured else 2)

        cy = card_top + 45
        draw.text((x1 + card_w // 2, cy), pkg["name"],
                  fill=WHITE, font=fnt(26, "bold"), anchor="mm")
        cy += 48
        draw.text((x1 + card_w // 2, cy), pkg["price"],
                  fill=WHITE, font=fnt(38, "bold"), anchor="mm")
        cy += 42
        draw.text((x1 + card_w // 2, cy), pkg["monthly"],
                  fill=BODY_GRAY, font=fnt(19, "regular"), anchor="mm")
        cy += 30
        divider_line(draw, cy, x1 + 20, x2 - 20)
        cy += 22

        for feat in pkg["features"]:
            draw.text((x1 + 22, cy), "+  " + feat,
                      fill=WHITE_DIM, font=fnt(18, "regular"), anchor="lm")
            cy += 36

    # CTA
    pill_button(draw, 540, card_bot + 58, 820, 66, BLUE_BRIGHT, cta, 26)

    brand_bottom(draw)
    save(img, filename)


# ═════════════════════════════════════════════════════════════════════════════
# GENERATE ALL 14 INSTAGRAM POSTS
# ═════════════════════════════════════════════════════════════════════════════
print("\n  Generating May 2026 Instagram visuals - IGEN VERITAS\n")

# CB-006  |  May 12  |  Pain Point
tmpl_pain(
    "CB006_May12_pain_5signs.png",
    headline_lines=["5 Signs Your Business", "Is Leaking Leads Right Now"],
    bullet_lines=[
        "  [x]  You reply to enquiries the next morning",
        "  [x]  Your website has no chat widget",
        "  [x]  New leads get buried in WhatsApp",
        "  [x]  You've never followed up twice",
        "  [x]  Unknown enquiry count last month",
    ],
    subtext="Spot 2 or more? You have a system problem — not a marketing one.",
    cta="DM 'LEADS' to see the fix"
)

# CB-007  |  May 12  |  Pain Point
tmpl_pain(
    "CB007_May12_pain_visitor_lost.png",
    headline_lines=["Every Visitor Who Leaves", "Is a Lead You Handed Away"],
    bullet_lines=[
        "  >>  Visited your website at 11:47 PM",
        "  >>  Had a question. Nobody there to answer.",
        "  >>  Googled the next option. Found your competitor.",
        "  >>  You never even knew they were there.",
    ],
    subtext="An AI chatbot replies in 3 seconds. Starts at RM500 setup.",
    cta="DM 'BOT' to get started"
)

# CB-008  |  May 13  |  Education
tmpl_edu(
    "CB008_May13_edu_2am_pov.png",
    headline_lines=["POV: It's 2AM.", "Someone Just Found Your Website."],
    points=[
        "Visitor lands on your site",
        "AI chatbot greets them in under 3 seconds",
        "Answers their questions about your service",
        "Qualifies them as a serious lead",
        "You wake up to a filled inbox — not a missed sale",
    ],
    subtext="Tanpa hire staff tambahan. Running every night on autopilot.",
    cta="DM 'BOT' — Basic from RM500 setup"
)

# CB-010  |  May 15  |  Education
tmpl_edu(
    "CB010_May15_edu_5things_chatbot.png",
    headline_lines=["5 Things an AI Chatbot Does", "That Your Staff Simply Cannot"],
    points=[
        "Reply to leads in under 3 seconds — every time",
        "Handle 20 enquiries simultaneously without slowing",
        "Auto follow-up on Day 1, Day 3, and Day 7",
        "Save every lead to Google Sheets in real time",
        "Work 365 days — no leave, no sick days, no delays",
    ],
    subtext="This is what automation looks like in a real business.",
    cta="DM 'BOT' to see which plan fits you"
)

# CB-011  |  May 16  |  Social Proof
tmpl_proof(
    "CB011_May16_proof_breakfast_leads.png",
    headline_lines=["3 Qualified Leads", "Before Breakfast."],
    story_lines=[
        "Beauty salon owner in KL — frustrated by ad spend leaking into",
        "unanswered after-hours enquiries. We set up her chatbot in 5 days.",
        "Week 1: 3 leads captured 10PM–7AM. All 3 booked a consultation.",
        "Zero staff hours used. Everything automated.",
    ],
    stats=[
        ("Setup Time", "5 Days"),
        ("Leads Wk 1", "3 Captured"),
        ("Staff Hours", "0 hrs"),
    ],
    cta="DM 'BOT' to get yours built"
)

# CB-013  |  May 20  |  Education — Web Dev
tmpl_edu(
    "CB013_May20_edu_website_trust.png",
    headline_lines=["Your Website Is Either", "Building Trust — Or Costing You Clients."],
    points=[
        "Loads fast on mobile (80%+ of Malaysians browse on phone)",
        "Answers questions before a customer has to ask",
        "Makes it easy to contact or book in 2 clicks",
        "Builds credibility with first-time visitors",
        "Works as your 24/7 sales rep when you're unavailable",
    ],
    subtext="We build in React & Laravel — responsive, clean, built to convert.",
    cta="DM 'WEB' to get started",
    service_badge="Web Dev"
)

# CB-014  |  May 21  |  Package Reveal
tmpl_pkg(
    "CB014_May21_package_reveal.png",
    headline_lines=["Basic. Growth. Pro.", "Full Pricing — No Hidden Fees."],
    packages=[
        {
            "name": "BASIC",
            "price": "RM500",
            "monthly": "+ RM150/month",
            "features": ["AI chatbot on website", "24/7 lead capture", "Trained on your biz", "Human handoff"],
            "featured": False,
        },
        {
            "name": "GROWTH",
            "price": "RM1,000",
            "monthly": "+ RM300/month",
            "features": ["Everything in Basic", "WhatsApp follow-ups", "Google Sheets CRM", "Owner notifications"],
            "featured": True,
        },
        {
            "name": "PRO",
            "price": "RM2,000",
            "monthly": "+ RM500/month",
            "features": ["Everything in Growth", "Full n8n automation", "Advanced lead logic", "Priority support"],
            "featured": False,
        },
    ],
    cta="DM 'PLAN' — We'll match you to the right tier"
)

# CB-016  |  May 25  |  Social Proof
tmpl_proof(
    "CB016_May25_proof_11leads_tuition.png",
    headline_lines=["Before: 0 Replies After Hours.", "After: 11 Leads in Week 1."],
    story_lines=[
        "Tuition centre in Selangor — parents enquired after dinner.",
        "By morning, half had enrolled elsewhere. We built a Growth chatbot.",
        "Week 1: 11 leads captured, 7 converted to consultations.",
        "0 staff hours used after hours. All on autopilot.",
    ],
    stats=[
        ("Leads Wk 1", "11"),
        ("Conversions", "7 / 11"),
        ("Staff Hours", "0 hrs"),
    ],
    cta="DM 'BOT' to get yours built this month"
)

# CB-017  |  May 26  |  Education — Mobile App
tmpl_edu(
    "CB017_May26_edu_mobile_app.png",
    headline_lines=["Your Customers Are on Their", "Phones 6+ Hours a Day."],
    points=[
        "Direct channel — no algorithm, no ad spend needed",
        "Push notifications for promos, appointments & updates",
        "Customers browse, book, or order without calling",
        "Builds brand loyalty through a product they use daily",
        "iOS + Android from one codebase (Flutter)",
    ],
    subtext="Built with Flutter + Firebase. Fast, scalable, built for Malaysian users.",
    cta="DM 'APP' to discuss your idea",
    service_badge="Mobile App"
)

# CB-019  |  May 27  |  Education — UI/UX
tmpl_edu(
    "CB019_May27_edu_uiux.png",
    headline_lines=["Bad Design Is Costing", "Your Business Money."],
    points=[
        "94% of first impressions are design-related",
        "Guides visitors to act — contact, book, or buy",
        "Reduces the time it takes to understand your offer",
        "Increases conversion without spending more on ads",
        "Makes your brand look like it belongs in 2026",
    ],
    subtext="We design in Figma. Build in React & Flutter.",
    cta="DM 'DESIGN' for a free website review",
    service_badge="UI/UX"
)

# CB-020  |  May 28  |  CTA / Conversion
tmpl_pkg(
    "CB020_May28_cta_this_is_the_week.png",
    headline_lines=["You've Been Thinking About This", "For Months. This Is the Week."],
    packages=[
        {
            "name": "BASIC",
            "price": "RM500",
            "monthly": "+ RM150/month",
            "features": ["Live in 5–7 days", "24/7 lead capture", "No tech skills needed"],
            "featured": False,
        },
        {
            "name": "GROWTH",
            "price": "RM1,000",
            "monthly": "+ RM300/month",
            "features": ["WhatsApp follow-ups", "Google Sheets CRM", "Owner notifications"],
            "featured": True,
        },
        {
            "name": "PRO",
            "price": "RM2,000",
            "monthly": "+ RM500/month",
            "features": ["Full n8n automation", "Advanced qualification", "Priority build slot"],
            "featured": False,
        },
    ],
    cta="DM 'START' — First 5 sign-ups get priority scheduling",
    hl_font_size=64
)

# CB-021  |  May 29  |  Education — Flutter vs Native
tmpl_edu(
    "CB021_May29_edu_flutter_vs_native.png",
    headline_lines=["Flutter vs Native App —", "What Should Your Biz Actually Build?"],
    points=[
        "Flutter: 1 codebase → iOS + Android",
        "70–80% lower cost vs full native build",
        "Near-native performance for most SME apps",
        "Faster to build, faster to update",
        "Right choice for 90% of SME projects",
    ],
    subtext="Booking, loyalty, catalogue, or client portal — Flutter wins.",
    cta="DM 'APP' to discuss your project",
    service_badge="Mobile App"
)

# CB-022  |  May 30  |  Social Proof — Month Recap
tmpl_proof(
    "CB022_May30_proof_may_recap.png",
    headline_lines=["May 2026 Recap:", "What Our Clients Experienced."],
    story_lines=[
        "F&B (KL): 18 leads captured in Week 1 after chatbot launch.",
        "Beauty salon (Selangor): 3 bookings before 8AM — overnight chatbot.",
        "Tuition centre: 7 out of 11 overnight leads → consultations.",
        "Website project: 5-day launch, fully responsive + mobile-first.",
    ],
    stats=[
        ("Leads Captured", "32+ Total"),
        ("Avg Setup", "5 Days"),
        ("After-hrs Revenue", "Running"),
    ],
    cta="DM 'START' — June build slots now open"
)

# CB-023  |  May 31  |  CTA — Process
tmpl_edu(
    "CB023_May31_cta_setup_process.png",
    headline_lines=["Setup Complete in 5–7 Days.", "No Technical Knowledge Needed."],
    points=[
        "Day 1 — Brief: Tell us about your business",
        "Days 2–4 — Build: We configure & train the AI",
        "Day 5 — Test: Every scenario thoroughly covered",
        "Days 6–7 — Launch: Script embedded in your site. Done.",
    ],
    subtext="Basic RM500+RM150/mo  ·  Growth RM1,000+RM300/mo  ·  Pro RM2,000+RM500/mo",
    cta="DM 'START' to lock in your June slot"
)

print(f"\n  DONE: 14 visuals saved to:\n  {OUTPUT_DIR}\n")
