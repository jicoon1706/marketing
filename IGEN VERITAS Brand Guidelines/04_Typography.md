# 04 · Typography

---

## 4.1 Font Family

**Primary: Inter**
Free on Google Fonts and available in Canva. Neutral, highly legible, excellent at small sizes and in ExtraBold display weights.

**Alternative: Poppins** — use only where a rounder, friendlier feel is needed (rarely). Never mix Inter and Poppins in the same composition.

**Windows generation fallback** — for Pillow/script-generated graphics on the local machine:

```python
FONT_BOLD    = "C:/Windows/Fonts/segoeuib.ttf"   # Segoe UI Bold
FONT_REGULAR = "C:/Windows/Fonts/segoeui.ttf"    # Segoe UI
FONT_LIGHT   = "C:/Windows/Fonts/segoeuil.ttf"   # Segoe UI Light
```

**Web stack:**

```css
font-family: 'Inter', 'Poppins', -apple-system, 'Segoe UI', Roboto, sans-serif;
```

---

## 4.2 Weights In Use

| Weight | Value | Where |
|---|---|---|
| ExtraBold | 800 | Display / hero headlines only |
| Bold | 700 | H1, section headers, stat numbers |
| SemiBold | 600 | H2, buttons, labels, package names |
| Regular | 400 | Body copy, captions |
| Italic | 400i | Pull quotes, testimonials |

Weights 100–300 and 900 are **not** used.

---

## 4.3 Type Scale — Desktop / Print

| Role | Weight | Size | Line height | Tracking |
|---|---|---|---|---|
| **Display / Hero** | ExtraBold 800 | 48–72px | 1.05 | −2% |
| **Heading (H1)** | Bold 700 | 32px | 1.15 | −1% |
| **Subheading (H2)** | SemiBold 600 | 24px | 1.25 | 0 |
| **Section Header** | Bold 700 | 20px | 1.3 | 0 |
| **Body Text** | Regular 400 | 16px | 1.6 | 0 |
| **Caption / Label** | Regular 400 | 12–14px | 1.4 | +2% |
| **Quote / Italic** | Italic 400 | 14px | 1.5 | 0 |
| **Eyebrow / Overline** | SemiBold 600 | 12px, UPPERCASE | 1.2 | +8% |

---

## 4.4 Type Scale — Social (1080 × 1080)

Social graphics need much larger type than web. Anything under 28px is unreadable in an Instagram feed.

| Role | Weight | Size | Notes |
|---|---|---|---|
| Poster headline | ExtraBold 800 | 76–96px | 2–3 lines max |
| Poster subheadline | SemiBold 600 | 34–40px | 1 line |
| Card title | Bold 700 | 30–36px | |
| Card body / bullets | Regular 400 | 24–28px | Never below 24px |
| Stat number | ExtraBold 800 | 60–80px | |
| Stat label | Regular 400 | 22–24px | Body Gray |
| Brand badge text | SemiBold 600 | 26–30px | |
| Footer / URL | Regular 400 | 22px | Body Gray |

---

## 4.5 Headline Rules

These are the rules that make an asset look like ours.

1. **Max 4–6 words**, broken across 2–3 lines. If it needs more, it isn't a headline — it's a caption.
2. **Exactly one accent word.** One key word gets Violet `#7B67D1` or Blue Mid `#488FE3`. Never two. Never zero.
3. **Break lines on meaning**, not on width. `Your business /  closes at 6pm.` — not `Your business closes / at 6pm.`
4. **Sentence case or title case** — never ALL CAPS for a full headline (caps are for eyebrows and the wordmark only).
5. **Max two font sizes** in any single design element.
6. **No hyphenation.** Ever.
7. **No orphans** — never leave a single short word alone on the last line.

### Accent Word Examples

> Your business closes at **6pm.**
> Leads masuk. **Kau tidur.**
> 11 leads before **breakfast.**
> Stop losing customers at **2AM.**

---

## 4.6 Body Copy Rules

- Body text is **White `#FFFFFF`** on dark backgrounds, **Body Gray `#6B7280`** on light
- Line length: 45–75 characters on web, 30–40 on social
- Paragraphs: max 3 lines on social, max 4 on web
- Left-aligned on web and documents; **centre-aligned on posters**
- Never justify text
- Bullets use `•` or `✓` — never `-` or `*` in final output

---

## 4.7 Numbers, Prices & Data

| Item | Format | Example |
|---|---|---|
| Currency | `RM` + space + thousands separator | `RM 1,000` |
| Monthly retainer | `RM XXX/mo` | `RM 300/mo` |
| Percentages | No space before `%` | `73%` |
| Time | 12-hour with AM/PM for emotional copy | `2:47 AM` |
| Time | 24-hour in UI and data | `14:30` |
| Phone | International format | `+60 17 310 3966` |
| Big stat numbers | ExtraBold, one accent colour, unit at 50% size | **24**/7 |

---

## 4.8 Bilingual Typesetting (BM + English)

Mixed BM/English is on-brand — see `05_Voice_and_Tone.md` for when to use it.

- Set both languages in Inter at the same weight and size
- **Do not** italicise BM words — they're not foreign, they're the audience's language
- Never mix languages mid-word or mid-phrase awkwardly (`your bisnes` ✗)
- Clean switch points are fine: `Leads masuk. You tidur.` ✓

---

## 4.9 Don'ts

- ✗ No decorative, script, serif, or condensed fonts
- ✗ No text with drop shadows or outlines (use a scrim instead)
- ✗ No letter-spacing on body copy
- ✗ No text smaller than 24px on a 1080×1080 social graphic
- ✗ No more than two weights in one card or module
- ✗ No text set directly over a busy image without a scrim at ≥60% opacity

---

*Next: [05_Voice_and_Tone.md](05_Voice_and_Tone.md)*
