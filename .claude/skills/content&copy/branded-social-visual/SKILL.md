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
- Bottom-right: `igen-veritas.com` in small Body Gray

**Vibe reference**: WhatChimp "24/7 AI Agent Available" with feature pills

---

## Execution Instructions

Follow these steps exactly every time.

### Step 1 — Parse the brief
Extract from the brief (or user's message):
- **Post type**: pain_point / education / proof / cta
- **Headline**: main text (short, punchy, 4–6 words, English/BM mix ok)
- **Subtext**: 1 supporting sentence
- **CTA**: call to action (default: `DM 'INFO' sekarang`)
- **CB number**: for the output filename

### Step 2 — Pick template
Use A/B/C/D based on post type. Default to the one that best matches the headline emotion.

### Step 3 — Generate the coded image (Pillow)

Write a complete, self-contained Python script using **Pillow (PIL)** to draw the graphic. The script must:

1. **Draw background**: `ImageDraw` with gradient fills (horizontal or diagonal bands)
2. **Draw shapes**: Rounded rectangles via `ImageDraw.rounded_rectangle()`, circles, lines
3. **Render text**: Use system font Segoe UI (Windows) — bold for headlines, regular for body
4. **Compose layers**: Background → shapes → cards → text → icons → branding
5. **Save**: Output to `social-media/CB-XXX_[type].png`

Font paths on Windows:
```python
FONT_BOLD    = "C:/Windows/Fonts/segoeuib.ttf"
FONT_REGULAR = "C:/Windows/Fonts/segoeui.ttf"
FONT_LIGHT   = "C:/Windows/Fonts/segoeuil.ttf"
```

Execute from the `marketing_team/` workspace root using PowerShell:
```powershell
py -c "[inline script here]"
# or save to a temp file and run:
py social-media/gen_CB-XXX.py
```

Output filename format: `social-media/CB-XXX_[type].png`
where `[type]` = `pain` / `edu` / `proof` / `cta`

### Step 3b — Generate via ChatGPT Image API (DALL-E 3)

After writing the Pillow script (or as the primary generation method), use the OpenAI images API to generate a high-quality version of the poster. This gives better visual results than the coded approach.

**API Key**: Set `OPENAI_API_KEY` as an environment variable — do not hardcode it in this file.

**Python code to generate and save the image:**

```python
import openai, os, requests

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]  # set in env, never hardcode
OUTPUT_DIR = "social-media"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_image(prompt, output_filename):
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    image_url = response.data[0].url
    # Download and save
    img_data = requests.get(image_url).content
    with open(os.path.join(OUTPUT_DIR, output_filename), "wb") as f:
        f.write(img_data)
    print(f"Saved: {output_filename}")
    return output_filename

# Usage:
# generate_image("[THE PROMPT]", "CB-028_pain.png")
```

**Execute via PowerShell from `marketing_team/` root:**
```powershell
$env:OPENAI_API_KEY="your-key-here"; py -c "import openai, os, requests; openai.OpenAI(api_key=os.environ['OPENAI_API_KEY']).images.generate(model='dall-e-3', prompt='YOUR PROMPT HERE', size='1024x1024', quality='standard', n=1)"
```

**Download the image from the returned URL** — save to `social-media/CB-XXX_[type].png`

> **Note:** If the API call fails or the key is invalid, fall back to the Pillow-coded image as a backup. Always save something to `social-media/` regardless of which path succeeds.

### Step 4 — Output the AI prompt for external tools

Immediately after the coded image is generated, output a ready-to-copy prompt the user can paste into any AI image tool (Midjourney, DALL-E, Ideogram, Canva AI, Skywork, Adobe Firefly, etc.).

Present it in a clearly labelled copyable block:

---

**AI Image Prompt — copy and paste into your preferred tool:**

```
[FILLED PROMPT — use the matching template below, all placeholders replaced with actual content]
```

**Suggested tools:** Midjourney, DALL-E (ChatGPT), Ideogram, Canva AI, Skywork AI, Adobe Firefly
**Aspect ratio to set:** 1:1 (square)
**If using Midjourney:** add `--ar 1:1 --style raw` at the end

---

#### AI Prompt Template A — Pain Point
```
Instagram marketing poster for IGEN VERITAS, a Malaysian AI tech company. Square 1:1 format.

Mood: Dark, dramatic, emotionally urgent. Modern tech startup aesthetic.
Background: Very dark navy almost black, with a soft violet-purple radial glow at center-left.
Top-left: Small white label "IGEN VERITAS" and "igen-veritas.com".
Center-top: Bold white sans-serif headline 2 lines, one keyword highlighted violet-purple:
"[HEADLINE_LINE_1]"
"[HEADLINE_LINE_2]"
Center: Dark frosted glass card, rounded corners, subtle white border glow. Inside: [STAT_DETAIL].
Bottom: Short gray subtext "[SUBTEXT]". Small violet pill CTA button "[CTA_TEXT]".
Style: respond.io dark marketing, Intercom dark mode. No people. Typography-driven. High contrast.
```

#### AI Prompt Template B — Education
```
Instagram marketing poster for IGEN VERITAS, a Malaysian AI tech company. Square 1:1 format.

Mood: Clean, bright, informative. Modern SaaS product marketing.
Background: Smooth diagonal gradient, violet-purple top-left to bright blue bottom-right.
Top: Bold headline "[HEADLINE]". Smaller subheadline "[SUBTEXT]".
Center: Simple geometric AI chatbot mascot, circular head, glowing eyes, floating center stage.
Around mascot: 4 white rounded feature pill badges in arc layout — icons + labels: "[FEATURE_1]", "[FEATURE_2]", "[FEATURE_3]", "[FEATURE_4]".
Bottom-right: Small brand text "IGEN VERITAS".
Style: WhatChimp, Tidio, Landbot marketing. Flat illustration, no photos. Clean and vibrant.
```

#### AI Prompt Template C — Proof / Demo
```
Instagram marketing poster for IGEN VERITAS, a Malaysian AI tech company. Square 1:1 format.

Mood: Confident, product-forward, results-focused.
Background: Smooth top-to-bottom gradient, violet to bright blue.
Top-left: White rounded pill badge "IGEN VERITAS".
Center-top: Bold white headline: "[HEADLINE]"
Center: Floating white rounded card — mobile chat UI mockup. Green WhatsApp-style header "[BOT_NAME]". Chat bubbles: customer asks "[CUSTOMER_MSG]", bot replies "[BOT_REPLY]". Footer: "Powered by IGEN VERITAS".
Bottom: Row of stat pill badges — "[STAT_1]", "[STAT_2]", "[STAT_3]".
Style: respond.io, Intercom product demos. Drop shadow on card. Professional SaaS.
```

#### AI Prompt Template D — Offer / CTA
```
Instagram marketing poster for IGEN VERITAS, a Malaysian AI tech company. Square 1:1 format.

Mood: Conversion-focused, clear value, pricing reveal.
Background: Deep purple gradient, violet to dark purple.
Top: Bold white headline 2 lines, one word bright blue: "[HEADLINE_LINE_1]" / "[HEADLINE_LINE_2]"
Center: Three pricing cards side by side, dark frosted glass style:
  Left — "Basic" / "RM 500 setup" / "RM 150/mo" / [BASIC_FEATURES]
  Middle — "Growth" / "RM 1,000 setup" / "RM 300/mo" / [GROWTH_FEATURES] — glowing violet border, "Most Popular" badge
  Right — "Pro" / "RM 2,000 setup" / "RM 500/mo" / [PRO_FEATURES]
Bottom: Large violet rounded pill button "[CTA_TEXT]". Small "igen-veritas.com" bottom-right.
Style: SaaS pricing page aesthetic, WhatChimp packages. Clean, high contrast, scannable.
```

### Step 5 — Wait for user to approve the image

After the DALL-E image is generated and saved to `social-media/CB-XXX_[type].png`, show the user the image path and say:

> "Image saved to `social-media/CB-XXX_[type].png` (generated via DALL-E 3).
> If you'd like a different version, tell me what to change.
> Say **'approved'** when you're happy with the image to proceed to caption writing."

**Stop here.** Do not write the caption or proceed until the user explicitly says the image is approved.

---

### AI Prompt Fallback (Manual Tools)

If the DALL-E API call fails or you want to manually generate elsewhere, also output the filled prompt below for manual copy-paste:

---
**AI Image Prompt — copy and paste into your preferred tool:**
```
[FILLED PROMPT — use the matching template below, all placeholders replaced with actual content]
```
**Suggested tools:** Midjourney, DALL-E (ChatGPT), Ideogram, Canva AI, Skywork AI, Adobe Firefly
**Aspect ratio to set:** 1:1 (square)
**If using Midjourney:** add `--ar 1:1 --style raw` at the end
---

---

## Quality Checklist

Before reporting the image as done:
- [ ] File saved to `social-media/CB-XXX_[type].png` via DALL-E 3 download
- [ ] Image is 1024x1024 (square 1:1)
- [ ] IGEN VERITAS branding visible on the image
- [ ] Brand colors used (Violet `#7B67D1`, Purple `#8A5DCC`, Blue `#488FE3`, Navy `#0B0B14`)
- [ ] Headline is bold and readable
- [ ] Fallback AI prompt output only if DALL-E API fails

---

## Example Invocations

**User**: "Create a pain point post about businesses losing leads at 2AM"
→ Template A. Headline: "Pelanggan tunggu." / "You tidur." Stat card: clock 2:47 AM, 0 leads.

**User**: "Make an education post about the 5 things AI chatbot does"
→ Template B. Headline: "5 Things Your AI Chatbot Does While You Sleep". Pills: Auto-Reply, Lead Capture, Follow-Up, 24/7 Active.

**User**: "Proof post — 11 leads at breakfast"
→ Template C. Headline: "11 Leads Before Breakfast." Chat mockup showing morning messages. Stats: 24/7 Active, <3s Reply, 100% Auto.

**User**: "Package reveal post"
→ Template D. Three cards: Basic/Growth/Pro with pricing. CTA: "DM 'INFO' sekarang".
