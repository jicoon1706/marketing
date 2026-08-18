# NUVENA Web Design Carousel — copy pack
5 slides · 1080 × 1350 (4:5) · Instagram carousel (standard post, not Reel)

Source: `Product Images/Web Design/Saloon_Website/Website 5` (NUVENA — Muslimah medispa, Gombak).
Every screen is the real build. Demo build — never present as a live client site.

---

## ✅ PRIMARY CAPTION (Blotato-ready)

```
Most salon websites make her work for it. This one doesn't. ✨

A women-only Muslimah medispa in Gombak — and four design decisions that turn a scroll into a booking. No hidden prices, no dead ends, no hunting for a phone number.

📍 Gombak, Selangor
🎯 The headline names the audience, not the salon
💛 Every treatment shows a starting price — no "call for price"
🔒 100% Muslimah, female therapists, private room
📲 Building for your salon or clinic? DM us.

Demo build · one of 7 salon directions in our portfolio.

#WebDesignMalaysia #SalonWebsite #MuslimahBusiness #KualaLumpur #IGenVeritas
```

**Why it's built this way**
- Hook lands in 59 characters — well inside Instagram's ~125-char truncation
- Exactly 5 hashtags (Blotato API hard limit)
- Emoji used as scannable line markers, not decoration
- Demo-build disclosure kept in-caption (VERITAS · integrity)

---

## Caption variant — EN + BM mix (Malaysian audience)

```
Website salon kau cantik. Tapi dia boleh book ke? 🤔

NUVENA — medispa Muslimah khas untuk wanita di Gombak. Empat keputusan design yang tukar scroll jadi booking, bukan sekadar "nice to look at".

📍 Gombak, Selangor
🎯 Headline terus cakap ini untuk siapa
💛 Setiap treatment ada harga — takde "PM for price"
🔒 100% Muslimah, therapist wanita, bilik private
📲 Nak macam ni untuk salon anda? DM kami.

Demo build · 1 daripada 7 design salon dalam portfolio kami.

#WebDesignMalaysia #SalonWebsite #MuslimahBusiness #KualaLumpur #IGenVeritas
```

---

## First comment (extra reach — hashtags here don't hit the 5 cap)

```
Slide by slide 👇
01 · The hook
02 · Above the fold — one promise, one button
03 · The treatment menu — RM 45 to RM 200, all on the page
04 · Trust — four numbered claims, not a paragraph
05 · The close — same yellow booking block on every page

Seven salon directions ready to show: Aluria · Verdel · AURELO · Delora · NUVENA · Rasmia · Snipwell. Tell us the vibe, we'll show you the two closest.

#WebDevelopment #UIUXDesign #MedispaMalaysia #SalonMalaysia #Gombak #WebsiteDesign #SmallBusinessMalaysia #DigitalTransformation
```

---

## Alternate hooks (A/B the first line)

| # | Hook | Angle |
|---|---|---|
| 1 | Most salon websites make her work for it. This one doesn't. ✨ | *In use* — problem/relief |
| 2 | Your salon website has one job. Most of them fail it. 👇 | Confrontational |
| 3 | "PM for price" is quietly costing you bookings. 💸 | Loss aversion |
| 4 | RM 45 to RM 200 — all on the page, before she has to ask. 💛 | Specificity |
| 5 | We designed a women-only medispa site. Every decision, explained. 🔎 | Curiosity / authority |

---

## Slide-by-slide

| # | Kicker | Headline | On-slide points |
|---|---|---|---|
| 01 | WEB DESIGN · CASE STUDY | 4 things this medispa site gets **right** | Hook + full homepage in browser frame |
| 02 | 01 · ABOVE THE FOLD | One promise. One **button**. | Headline names the audience · one loud CTA · rating + branch count beneath it |
| 03 | 02 · THE TREATMENT MENU | Prices **upfront**. Filters that work. | RM 45–RM 200 stated · 5 category filters · no "call for price" |
| 04 | 03 · TRUST | Proof, not **adjectives**. | Four numbered claims · female therapists, private room, halal · real testimonials |
| 05 | 04 · THE CLOSE | Every page ends with a **booking**. | Gallery → yellow CTA block · book or call · CTA to DM |

---

## Alt text (per slide)

1. Cream slide, headline "4 things this medispa site gets right" with "right" highlighted yellow, above a browser mockup of the NUVENA homepage.
2. Browser mockup of the NUVENA hero section — headline, two buttons and a 4.9 star rating — under the headline "One promise. One button."
3. Browser mockup of the NUVENA treatments page showing category filter pills and six treatment cards with starting prices, under the headline "Prices upfront. Filters that work."
4. Black slide, headline "Proof, not adjectives," above the site's four numbered trust claims and three customer testimonials.
5. Cream slide showing the NUVENA gallery strip and the yellow "Ready to glow?" booking block, under the headline "Every page ends with a booking."

---

## Publishing notes

**Blotato payload** (once an Instagram account is connected at my.blotato.com):

```json
{
  "accountId": "<from blotato_list_accounts, platform: instagram>",
  "platform": "instagram",
  "mediaUrls": [
    "<public URL slide 01>", "<02>", "<03>", "<04>", "<05>"
  ],
  "text": "<primary caption above>"
}
```

- Omit `mediaType` — this is a 4:5 carousel, not a Reel or Story.
- Blotato needs **publicly accessible URLs**; the PNGs are local files, so upload them (or host them) first.
- Best window: Tue–Thu, 8–10am or 7–9pm MYT (brand guidelines §10).
- LinkedIn cut: keep slides 1–5, swap the caption for the "thought leadership" angle — lead with hook #5.
