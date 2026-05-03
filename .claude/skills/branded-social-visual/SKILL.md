---
name: branded-social-visual
description: Generate on-brand social media graphics (1080×1080 PNG) for IGEN VERITAS. Use this skill whenever the user asks to create, design, or generate a social media post, Instagram graphic, promotional visual, content graphic, or any image for IGEN VERITAS. Also triggers when the user mentions a post type (pain point, education, proof, CTA, package reveal) or references the weekly content plan. Outputs a ready-to-post PNG saved to the /social-media/ folder — no design philosophy files, no markdown reports, just the visual.
---

# Branded Social Visual — IGEN VERITAS

Generate production-ready 1080×1080 PNG social media graphics that match IGEN VERITAS brand identity and are inspired by WhatChimp and respond.io visual style.

**Go straight to canvas — skip all design philosophy steps.**

---

## Brand Constants

Always embed these values directly in every generated graphic:

### Colors
```python
VIOLET      = "#7B67D1"   # Hero backgrounds, primary CTA
PURPLE      = "#8A5DCC"   # Dark sections, depth layers
BLUE_MID    = "#488FE3"   # Cards, highlights, accent
BLUE_BRIGHT = "#4196E6"   # Data visuals, mobile accents
DARK_NAVY   = "#0B0B14"   # Dark background, overlays
WHITE       = "#FFFFFF"
BODY_GRAY   = "#6B7280"
```

### Gradients
```python
HERO_GRADIENT  = ("#7B67D1", "#4196E6")  # Main backgrounds
CARD_GRADIENT  = ("#8A5DCC", "#488FE3")  # Feature cards
DARK_OVERLAY   = "rgba(11,11,20,0.85)"   # Dark glassmorphism
```

### Typography
- **Primary font**: Inter (weight 800 for headlines, 600 for subheadings, 400 for body)
- **Fallback**: Poppins
- **Headline rules**: Max 4–6 words, broken across 2–3 lines. One key word gets accent color.
- **Body text**: Always White on dark backgrounds

### Canvas
- **Size**: 1080 × 1080 px
- **Format**: PNG
- **Output folder**: `social-media/` (relative to the `marketing_team/` workspace root)

---

## Post Types & Visual Templates

Choose the template based on the post type. If not specified, infer from the headline/content.

### Template A — Pain Point (Monday posts)
*Dark, dramatic, emotionally resonant.*

**Layout:**
- Background: Dark Navy `#0B0B14` with a subtle radial gradient glow in Violet `#7B67D1` at center-left
- Top-left: IGEN VERITAS brand name in small white caps + website URL
- Center-top: Bold WHITE headline (3–5 words, 2 lines), one word in Violet `#7B67D1`
- Center: A simple stat or "before" scenario in a glassmorphism dark card (`rgba(255,255,255,0.05)`, 24px border-radius, 1px border `rgba(255,255,255,0.1)`)
  - Card shows: time (e.g. "2:47 AM"), red indicator ("0 leads"), unread messages icon
- Bottom: A short subtext line in Body Gray `#6B7280`, plus a subtle CTA pill button

**Vibe reference**: respond.io "AI that cuts through the noise" — dark, confident, minimal

---

### Template B — Education (Wednesday posts)
*Clean gradient, feature-rich, informative.*

**Layout:**
- Background: Gradient `#7B67D1` → `#4196E6` (diagonal top-left to bottom-right)
- Center: AI mascot or chatbot icon (draw with simple geometric shapes — circular head, glowing eyes, WhatsApp-green accent)
- Surrounding icon pills (rounded white cards, 12px border-radius, subtle shadow):
  - Each pill: flag/icon on left + label text (e.g. "🌐 Website", "📄 PDF", "❓ FAQ", "🧠 Knowledge Base")
  - Arrange in a 2×2 or arc pattern around the mascot
- Bold dark headline at top (`#07254d` or White depending on contrast)
- Subtext below headline: DM Sans equivalent, 20px

**Vibe reference**: WhatChimp "Train AI on your Website, PDF, FAQs or Knowledge Base"

---

### Template C — Proof / Demo (Friday posts)
*Gradient with floating UI mockup — shows the product in action.*

**Layout:**
- Background: Gradient `#7B67D1` → `#4196E6`
- Top-left: Brand badge — rounded pill card, white background, "IGEN VERITAS" text + small logo
- Bold white headline (2–3 lines), centered, top 35% of canvas
- Center: Floating white rounded card (mockup) showing a chat conversation
  - Header: green WhatsApp-style bar with contact name
  - 2–3 chat bubbles: customer question, bot answer with feature highlight
  - Bottom of card: small "Powered by IGEN VERITAS" label
- Bottom: Stat strip — 3–4 micro-stats in separate pill badges (e.g. "24/7 Active", "< 3s Reply", "100% Auto")

**Vibe reference**: respond.io "Voice notes. Now readable." with UI mockup center

---

### Template D — Offer / Package CTA (Saturday posts)
*Clean, conversion-focused, price-anchored.*

**Layout:**
- Background: Gradient `#7B67D1` → `#8A5DCC` (purple-to-purple, deeper)
- Top: Bold white headline (2 lines), accent word in Blue Mid `#488FE3`
- Center: 3 package cards side-by-side (Basic / Growth / Pro), each as a dark glassmorphism card:
  - Card: `rgba(255,255,255,0.08)` bg, 16px border-radius
  - Package name (white, bold, 18px)
  - Setup price (white, ExtraBold, 28px) + monthly retainer (Body Gray, 14px)
  - 3–4 feature bullet points (white, 13px, checkmark prefix ✓)
  - Highlight the **Growth** card with a Violet `#7B67D1` glow border as "Most Popular"
- Bottom: CTA button — Violet pill, "DM 'INFO' sekarang" in white bold text
- Bottom-right: `igenveritas.com` in small Body Gray

**Vibe reference**: WhatChimp "24/7 AI Agent Available" with feature pills

---

## Execution Instructions

Follow these steps exactly every time:

### Step 1 — Parse the brief
Extract from the user's message:
- **Post type**: pain_point / education / proof / cta (infer if not stated)
- **Headline**: the main text (use as-is or write a short punchy version in BM/English mix if needed)
- **Subtext**: supporting sentence or tagline
- **CTA**: call to action line (default: "DM 'INFO' sekarang")
- **Week**: optional (Week 1–4 from content plan)

### Step 2 — Pick template
Use A/B/C/D based on post type. If multiple types could fit, default to the one that best matches the headline emotion.

### Step 3 — Generate Python script
Write a complete, self-contained Python script using **Pillow (PIL)** to draw the graphic. The script must:

1. **Install check**: Begin with a `pip install Pillow` guard if needed, but assume Pillow is available
2. **Draw background**: Use `ImageDraw` with gradient fills (draw horizontal or diagonal bands)
3. **Draw shapes**: Rounded rectangles via `ImageDraw.rounded_rectangle()`, circles, lines
4. **Render text**: Download Inter font from Google Fonts or use system default (Segoe UI on Windows), apply bold/regular weights
5. **Compose layers**: Background → shapes → cards → text → icons → branding
6. **Save**: Output to `social-media/<filename>.png` where filename = `YYYYMMDD_<post_type>_<slug>.png`

Key Pillow patterns to use:
```python
from PIL import Image, ImageDraw, ImageFont
import os

# Canvas
img = Image.new("RGBA", (1080, 1080), (11, 11, 20, 255))
draw = ImageDraw.Draw(img)

# Gradient background (vertical or diagonal)
for y in range(1080):
    t = y / 1080
    r = int(123 + (65 - 123) * t)   # #7B67D1 → #4196E6
    g = int(103 + (150 - 103) * t)
    b = int(209 + (230 - 209) * t)
    draw.line([(0, y), (1080, y)], fill=(r, g, b, 255))

# Glassmorphism card
draw.rounded_rectangle([x1, y1, x2, y2], radius=24,
    fill=(255, 255, 255, 13), outline=(255, 255, 255, 26))

# Bold headline text
font_headline = ImageFont.truetype("segoeui.ttf", 96)  # adjust path
draw.text((540, 200), "LINE ONE", fill=(255, 255, 255, 255),
    font=font_headline, anchor="mm")

# Save
os.makedirs("social-media", exist_ok=True)
img.save("social-media/output.png", "PNG")
```

### Step 4 — Execute the script
Run the Python script from the `marketing_team/` workspace directory using PowerShell:
```powershell
$py = "C:\Program Files\Python312\python.exe"
$script = "C:\Users\jicoo\OneDrive\Documents\Claude\marketing_team\.claude\skills\branded-social-visual\scripts\generate_visual.py"
Set-Location "C:\Users\jicoo\OneDrive\Documents\Claude\marketing_team"
& $py $script --type <type> --week <1-4> --day <mon|wed|fri|sat>
```

Available arguments:
- `--type`: `pain` / `education` / `proof` / `cta`
- `--week`: `1` to `4`
- `--day`: `mon` / `wed` / `fri` / `sat`
- `--headline`: override headline text (use `/` as line break)
- `--subtext`: override subtext
- `--cta`: override CTA text

Or write a custom inline script using `brand_constants.py` helpers and one of the four template functions.

### Step 5 — Report output
Tell the user the filename and confirm it was saved to `social-media/`. Do NOT produce a markdown file, design philosophy doc, or any other output file. Only the PNG.

---

## Font Handling on Windows

On Windows (Segoe UI available system-wide):
```python
import os

def get_font(size, weight="regular"):
    font_map = {
        "bold":    "C:/Windows/Fonts/segoeuib.ttf",
        "regular": "C:/Windows/Fonts/segoeui.ttf",
        "light":   "C:/Windows/Fonts/segoeuil.ttf",
    }
    path = font_map.get(weight, font_map["regular"])
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()
```

For better brand match, also try downloading Inter via:
```python
import urllib.request
# Download Inter-Bold.ttf from Google Fonts CDN if not cached
FONT_CACHE = os.path.join(os.path.dirname(__file__), "assets", "fonts")
```
Font assets can be stored in `.claude/skills/branded-social-visual/assets/fonts/`.

---

## Quality Checklist

Before saving, mentally verify:
- [ ] All text is fully within the canvas (no clipping)
- [ ] Minimum padding 60px from canvas edges
- [ ] Headline readable at thumb size (simulate 375px width)
- [ ] Brand colors match the palette — no generic blues or greens
- [ ] IGEN VERITAS name or `igenveritas.com` appears somewhere on every post
- [ ] CTA is clear and visible
- [ ] No element is placed behind another in a way that reduces readability
- [ ] File saves correctly to `social-media/` folder

---

## Example Invocations

**User**: "Create a Monday pain point post about businesses losing leads at 2AM"
→ Use Template A, dark navy background, headline: "Pelanggan tunggu. / You tidur.", stat card showing "2:47 AM — 0 leads captured"

**User**: "Make a Wednesday education post about the AI chatbot features"
→ Use Template B, gradient background, mascot center, pills: Website / PDF / FAQ / WhatsApp

**User**: "Design the Saturday package reveal for Week 3"
→ Use Template D, 3 package cards, Growth highlighted, CTA: "DM 'INFO' sekarang"

**User**: "Generate all 4 posts for Week 1"
→ Run all 4 templates sequentially, save as separate files with day prefix (Mon_, Wed_, Fri_, Sat_)
