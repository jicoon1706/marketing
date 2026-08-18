# 06 · Photography and Art Direction

> Reference examples of approved output live in `Product Images/`.

---

## 6.1 Visual North Star

Our reference points are **respond.io**, **WhatChimp**, **Intercom**, **Tidio** and **Landbot** — modern SaaS product marketing. Confident, typographic, gradient-led, product-forward. Never stock-photo corporate, never crowded, never gimmicky.

**In one line:** a bold headline, a floating piece of product UI, brand gradient behind it, and nothing else.

---

## 6.2 Layout Principles

```
┌─────────────────────────────┐
│  Brand badge (top-left)     │
│                             │
│  HEADLINE                   │  ← 30–40% of canvas
│  Accent word in violet      │
│                             │
│  ┌───────────────────┐      │
│  │   Visual / UI     │      │  ← centre, floating
│  │   mockup / card   │      │
│  └───────────────────┘      │
│                             │
│  Subtext · CTA pill         │  ← bottom
│  igen-veritas.com            │
└─────────────────────────────┘
```

- **Headline top → visual centre → brand bottom.** This order, every time.
- Centre-aligned text on posters
- Generous whitespace — never fill every corner
- One big idea per asset
- Safe margin: 60px on a 1080×1080 canvas; 80px top/bottom on 1080×1920

---

## 6.3 Visual Elements

### Use

- Smooth gradient backgrounds — no textures, no noise, no busy patterns
- Floating glassmorphism cards with soft drop shadows
- Product UI in floating phone or browser frames
- 3D-style robot or AI mascot illustrations — friendly geometric shapes, glowing eyes, never corporate-mascot creepy
- Floating icon accents: WhatsApp, AI brain, charts, calendars, chat bubbles
- Chat-bubble mockups showing a real conversation
- Stat pills — small rounded badges with a number + label

### Avoid

- ✗ Stock photos of people in suits shaking hands
- ✗ Generic "AI" imagery: glowing brains, binary rain, circuit boards, blue hologram hands
- ✗ Clip art, drop-shadowed emoji, WordArt
- ✗ More than 3 icons in one composition
- ✗ Anything that looks like a Canva template with the placeholder text swapped

---

## 6.4 Photography

We use photography rarely. When we do:

| Rule | Detail |
|---|---|
| **Subject** | Real Malaysian small-business settings — a café counter, a clinic reception, a shop lot, a phone in hand |
| **People** | Real business owners, natural, working — never posed, never in suits |
| **Lighting** | Natural, slightly warm, soft shadows |
| **Colour treatment** | Slight cool grade to sit next to Violet; never heavy filters |
| **Composition** | Leave 40% negative space for the headline |
| **Overlay** | Always a scrim — `rgba(11,11,20,0.55)` minimum — before text goes on top |
| **Crop** | 1:1 for feed, 9:16 for stories/reels, 16:9 for web hero |

**Never** use images we don't have rights to, and never present a stock photo as a real client.

---

## 6.5 Screenshots & Mockups

Screenshots are our strongest proof asset. Treat them carefully.

- Always show **real** product UI — never a fabricated conversation presented as real
- Frame in a floating rounded card: white fill, 24px radius, `0 20px 60px rgba(11,11,20,0.35)` shadow
- Redact all client PII: blur phone numbers, surnames, addresses — always
- Show 2–3 chat bubbles maximum; crop the rest
- Add a `Powered by IGEN VERITAS` footer label in 12px `#6B7280`
- Device frames: generic rounded rectangle, not a branded iPhone outline

---

## 6.6 Post Templates (Social)

Four templates cover almost everything. Full specs are implemented in the `branded-social-visual` skill.

### Template A — Pain Point
*Dark, dramatic, emotionally urgent.*

- Background: Dark Navy `#0B0B14` + Violet radial glow at centre-left
- Top-left: brand name + URL in small white caps
- Centre-top: bold white headline, 3–5 words, 2 lines, one word in Violet
- Centre: dark glassmorphism card showing the "before" scenario — a timestamp (`2:47 AM`), a red indicator (`0 leads`), unread messages
- Bottom: short Body Gray subtext + subtle CTA pill
- Reference: respond.io dark marketing

### Template B — Education
*Clean gradient, feature-rich, informative.*

- Background: `#7B67D1` → `#4196E6`, diagonal
- Centre: AI mascot or chatbot icon in simple geometric shapes
- Around it: 4 white rounded pill badges in a 2×2 or arc — icon + label
- Bold headline top, subtext below
- Reference: WhatChimp "Train AI on your Website, PDF, FAQs"

### Template C — Proof / Demo
*Gradient with a floating UI mockup.*

- Background: `#7B67D1` → `#4196E6`
- Top-left: white pill brand badge
- Bold white headline, centred, top 35%
- Centre: floating white card — chat UI mockup, green WhatsApp-style header, 2–3 bubbles
- Bottom: 3–4 stat pills (`24/7 Active`, `< 3s Reply`, `100% Auto`)
- Reference: respond.io product demos

### Template D — Offer / Package CTA
*Conversion-focused, price-anchored.*

- Background: `#7B67D1` → `#8A5DCC`
- Top: bold white headline, 2 lines, accent word in Blue Mid
- Centre: three glassmorphism package cards (Basic / Growth / Pro), Growth highlighted with a Violet glow + "Most Popular"
- Bottom: Violet pill CTA + `igen-veritas.com` bottom-right
- Reference: SaaS pricing page aesthetic

---

## 6.7 Canvas Specs

| Asset | Size | Format |
|---|---|---|
| Instagram feed post | 1080 × 1080 | PNG |
| Instagram carousel slide | 1080 × 1350 | PNG |
| Instagram story / Reel cover | 1080 × 1920 | PNG |
| LinkedIn post | 1200 × 627 | PNG |
| LinkedIn banner | 1584 × 396 | PNG |
| Website hero | 1920 × 1080 | WebP / JPG |
| Email header | 600 × 200 | PNG |
| WhatsApp broadcast image | 1080 × 1080 | JPG (compressed) |

Output goes to `social-media/` as `CB-XXX_[type].png` where `[type]` is `pain` / `edu` / `proof` / `cta`.

---

## 6.8 AI Image Generation

When generating with DALL·E, Midjourney, Ideogram, Firefly or Canva AI, every prompt should carry these constants:

```
Brand: IGEN VERITAS, a Malaysian AI tech company.
Palette: violet #7B67D1, purple #8A5DCC, blue #488FE3, bright blue #4196E6,
         dark navy #0B0B14, white.
Style: modern SaaS marketing (respond.io, WhatChimp, Intercom).
       Flat, typographic, high contrast, generous whitespace.
No: stock photos of people, glowing brains, circuit boards, binary code, clutter.
Aspect ratio: 1:1 (add --ar 1:1 --style raw for Midjourney).
```

Then add the template-specific block from `branded-social-visual`. Always review generated text in the image — AI tools routinely misspell headlines; if the text is wrong, regenerate or overlay real type.

---

## 6.9 Motion & Video

| Element | Spec |
|---|---|
| Reel length | 15–30 seconds |
| Hook | First 2 seconds — text on screen, no intro logo |
| Captions | Always burned in, white, ExtraBold, bottom third |
| Transitions | Simple cuts and fades. No spins, no zoom bounces. |
| End card | 2 seconds — logo + `igen-veritas.com` + CTA on brand gradient |
| Music | Trending but neutral; never overpowering the voiceover |
| Logo animation | Fade in only. The orbital ring may rotate once, slowly. |

---

## 6.10 Quality Checklist

Before an asset ships:

- [ ] Brand gradient or Violet visible in the thumbnail
- [ ] Headline is 4–6 words with exactly one accent word
- [ ] No text below 24px
- [ ] Logo present, correct version for the background, clear space respected
- [ ] All client PII redacted
- [ ] Canvas is the correct size for its channel
- [ ] Legible at thumbnail size (shrink to 15% and check)
- [ ] Nothing in the composition we can't back up as true

---

*Next: [07_Services_and_Offerings.md](07_Services_and_Offerings.md)*
