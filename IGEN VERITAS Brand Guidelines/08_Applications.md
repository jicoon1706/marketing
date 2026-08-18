# 08 · Applications

> Channel-by-channel specs. When in doubt, this file wins over improvisation.

---

## 8.1 Instagram — Primary Channel

**Cadence:** 3–4 posts per week
**Best times:** Tue–Thu, 8–10am or 7–9pm MYT

### Weekly Rhythm

| Day | Post type | Template | Goal |
|---|---|---|---|
| Monday | Pain point | A | Stop the scroll, name the problem |
| Wednesday | Education | B | Teach one thing |
| Friday | Proof / demo | C | Show it working |
| Saturday | Offer / CTA | D | Convert |

### Post Specs

| | |
|---|---|
| Feed post | 1080 × 1080 PNG |
| Carousel | 1080 × 1350 PNG, 5–8 slides |
| Story / Reel | 1080 × 1920 PNG/MP4 |
| Logo | Top-left, 60px inset, or white pill badge on gradients |
| Caption | Caption formula (see `05_Voice_and_Tone.md`) |
| Hashtags | 5–10, always including `#IGenVeritas` |

### Carousel Structure

```
Slide 1  → Hook. Headline only. Make them swipe.
Slide 2  → The problem, made concrete
Slide 3–6 → One idea per slide, numbered
Slide 7  → The solution, named
Slide 8  → CTA + logo + igen-veritas.com
```

---

## 8.2 LinkedIn

**Cadence:** 2 posts per week
**Tone:** professional, insightful, thought leadership

| | |
|---|---|
| Image | 1200 × 627 PNG |
| Banner | 1584 × 396 PNG |
| Post length | 150–300 words |
| Hashtags | Max 3 |
| Emoji | None |
| Hook | First line must work as a standalone — LinkedIn truncates at ~140 chars |

**What performs:** a specific client problem and how it was solved · a number with context · a short technical explainer · a lesson from a build that went wrong.
**What doesn't:** reposted Instagram captions with BM slang · pure promotion · motivational quotes.

---

## 8.3 Website

| Section | Treatment |
|---|---|
| Hero | Hero Gradient background, ExtraBold 48–72px headline, one accent word, single primary CTA |
| Section headers | Bold 32px, Dark Navy on white / White on navy |
| Feature cards | White on light, or glassmorphism on dark, 24px radius |
| Pricing table | Three columns, Growth highlighted with Violet border + "Most Popular" |
| Body copy | Body Gray `#6B7280`, 16px, 1.6 line height, max 75 characters per line |
| Buttons — primary | Violet `#7B67D1` fill, white SemiBold text, 12px radius, 14px 28px padding |
| Buttons — secondary | Transparent, 1px Violet border, Violet text |
| Footer | Dark Navy `#0B0B14`, white logo, contact block, `© 2026 IGEN VERITAS` |
| Chat widget | Bottom-right — see `07_Services_and_Offerings.md` §7.9 |

**Every page** carries one primary CTA above the fold and one repeated in the footer.

---

## 8.4 Email

### Signature

```
[Logo — 140px wide]

Name
Role · IGEN VERITAS
+60 17 310 3966 · igenveritas@gmail.com
igen-veritas.com
```

Inter or Arial fallback, 14px, links in Violet `#7B67D1`. No quotes, no images beyond the logo, no "sent from my iPhone".

### Marketing Email

| Element | Spec |
|---|---|
| Header | 600 × 200 PNG, Hero Gradient + logo |
| Subject line | 6–9 words, no emoji, no ALL CAPS, no "RE:" tricks |
| Body width | 600px max |
| Body copy | 16px, Dark Navy on white |
| CTA button | Violet fill, white text, 8px radius, centred |
| Footer | Address, unsubscribe, `© 2026 IGEN VERITAS` |

Tone: warm, helpful, responsive. One ask per email.

---

## 8.5 WhatsApp

| | |
|---|---|
| Broadcast image | 1080 × 1080 JPG, compressed under 300KB |
| Message length | Under 5 lines — WhatsApp truncates with "Read more" |
| Tone | Warm, conversational, fast |
| Formatting | `*bold*` for one key phrase only |
| Links | Always last line |
| Response target | Under 5 minutes during business hours |

Never send an unsolicited broadcast to a contact who hasn't opted in.

---

## 8.6 Proposals & Documents

| Element | Spec |
|---|---|
| Cover | Hero Gradient full-bleed, logo top-centre, project title ExtraBold white, client name + date |
| Page margins | 25mm all sides |
| Headings | Inter Bold, Dark Navy, Violet rule underneath |
| Body | Inter Regular 11pt, 1.5 line spacing |
| Tables | Violet header row, white text, alternating `#F9FAFB` rows |
| Page numbers | Bottom-right, Body Gray, 9pt |
| Footer | Small logo bottom-left, `igen-veritas.com` bottom-right |

Standard proposal structure:
`Cover → Understanding of the problem → Proposed solution → Scope & deliverables → Timeline → Pricing → Next steps`

---

## 8.7 Slide Decks

| | |
|---|---|
| Ratio | 16:9 |
| Title slide | Hero Gradient, logo, ExtraBold title |
| Section dividers | Solid Violet or Purple, white ExtraBold text, centred |
| Content slides | White background, Dark Navy text, one idea per slide |
| Max bullets | 5 per slide, max 8 words each |
| Charts | Brand palette only — Violet, Blue Mid, Purple, Blue Bright in that order |
| Logo | Bottom-right, small, every slide except the title |
| Font | Inter throughout |

---

## 8.8 Client Deliverables

Every handover pack contains:

- Chatbot flow diagram (branded)
- Knowledge-base source list
- Google Sheets CRM link (Growth & Pro)
- One-page quick reference, branded per §8.6
- Loom or recorded walkthrough
- 30-day support terms

Filename convention: `ClientName_Deliverable_YYYYMMDD.ext`

---

## 8.9 Merchandise & Print

| Item | Treatment |
|---|---|
| Business card | Dark Navy front with logo only; back with Hero Gradient edge, name + contact in white |
| Roll-up banner | Hero Gradient, headline top third, QR to igen-veritas.com bottom |
| T-shirt | Icon only, left chest, white on navy or navy on white |
| Sticker | Icon in a circle, die-cut |
| Notebook | Dark Navy cover, foil or white logo centred |

Print: CMYK conversions must be proofed — Violet `#7B67D1` shifts noticeably. Prefer Pantone matching for volume runs.

---

## 8.10 Content Pipeline Integration

Assets flow through the workspace's two-layer system:

```
content/plans/YYYY-MM_plan.md      ← Layer 1: approved monthly calendar
        ↓
content/pipeline/CB-XXX.md         ← Layer 2: post in production
        ↓
social-media/CB-XXX_[type].png     ← Generated visual
        ↓
content/ready-to-post/             ← Approved, awaiting publish
        ↓
content/posted/YYYY-MM/            ← Archive
```

New CB numbers are assigned during monthly planning (CB-001–CB-023 are legacy). Use the `/social-pipeline` skill for all pipeline operations and `branded-social-visual` to generate the graphic.

---

## 8.11 Pre-Publish Checklist

- [ ] Correct canvas size for the channel
- [ ] Logo present, correct version, clear space respected
- [ ] Headline 4–6 words, exactly one accent word
- [ ] No text under 24px (social) or 11pt (print)
- [ ] Brand gradient visible at thumbnail size
- [ ] One CTA, no competing asks
- [ ] Caption follows the formula, hashtags in range
- [ ] All claims verifiable, all PII redacted
- [ ] Filed to the right pipeline folder with the right CB number

---

*Back to [00_README.md](00_README.md)*
