# 02 · Logo and Identity

> Files live in `assets/logos/`.

---

## 2.1 Logo Anatomy

The IGEN VERITAS logo has two components:

| Component | Description |
|---|---|
| **Icon** | Circular orbital ring graphic in blue/purple tones — represents intelligence in motion and the "generation" idea |
| **Wordmark** | "IGEN VERITAS" set in ExtraBold uppercase |

They may be used together (preferred) or the icon alone where space is tight and the brand is already established in context (favicon, app icon, watermark).

---

## 2.2 Logo Files

| File | Format | Background it's for | Use case |
|---|---|---|---|
| `assets/logos/Logo Colour.png` | PNG, opaque | White / light | **Default.** Documents, proposals, print, light web sections |
| `assets/logos/Logo Black.png` | PNG, opaque | White / light | Mono contexts, faxable docs, single-colour print |
| `assets/logos/Transparent Colour.png` | PNG, alpha | Any | Overlaying gradients, posters, photos |
| `assets/logos/Transparent Black.png` | PNG, alpha | Light only | Overlaying light photography, watermarks |
| `assets/logos/Text.png` | PNG, alpha | Any | Wordmark only — narrow lockups, footers, banners |

> **On dark and gradient backgrounds** use `Transparent Colour.png`, or the wordmark reversed to pure white `#FFFFFF`. Never place the black logo on a brand gradient.

---

## 2.3 Clear Space

Maintain clear space on **all four sides equal to the cap-height of the "I" in IGEN.**

```
        ┌─────────────────────────┐
        │        ↕ = height of "I"│
        │   ┌─────────────────┐   │
   ←→   │   │  ◯ IGEN VERITAS │   │   ←→
        │   └─────────────────┘   │
        │        ↕                │
        └─────────────────────────┘
```

Nothing enters this zone — no text, no icon, no card edge, no image crop.

---

## 2.4 Minimum Sizes

| Context | Minimum |
|---|---|
| Digital — full lockup | 120 px wide |
| Digital — icon only | 32 × 32 px |
| Print — full lockup | 25 mm wide |
| Favicon | 32 × 32 px (icon only) |
| Instagram post watermark | 140 px wide at 1080 × 1080 |

Below these sizes, drop the wordmark and use the icon alone.

---

## 2.5 Placement Rules

| Surface | Position |
|---|---|
| Instagram post (1080×1080) | Top-left, 60 px inset — or a white rounded pill badge top-left for gradient backgrounds |
| Instagram story / reel (1080×1920) | Top-left, 80 px inset, below the safe area |
| Promotional poster | Bottom-centre, paired with `igen-veritas.com` |
| Formal document / proposal | Top-centre or top-left of the cover page |
| Website header | Top-left, links to homepage |
| Email signature | Left of the contact block, 140 px wide |
| Slide deck | Bottom-right corner, small, every slide |

---

## 2.6 The Brand Badge (Social)

For gradient backgrounds, the standard treatment is a **white rounded pill**:

```
Background:    #FFFFFF
Border-radius: 999px (fully rounded)
Padding:       12px 20px
Contents:      icon (20px) + "IGEN VERITAS" in Inter SemiBold 14px, #0B0B14
Shadow:        0 4px 16px rgba(11,11,20,0.12)
```

On dark backgrounds, use the inverse: `rgba(255,255,255,0.08)` fill, `1px rgba(255,255,255,0.15)` border, white text.

---

## 2.7 Misuse — Never Do These

| ✗ | Why |
|---|---|
| Stretch or squash | Breaks the orbital geometry |
| Rotate at an angle | The ring reads as a mistake |
| Recolour to non-brand colours | Colour carries the identity |
| Apply gradients *to* the logo | The logo sits *on* gradients, not the reverse |
| Add drop shadows, glows, bevels, or outlines | We are flat and modern |
| Place on a busy photo without a scrim | Illegible |
| Place the black logo on a dark or gradient background | No contrast |
| Rebuild the wordmark by typing it in a different font | It's a fixed lockup |
| Enclose in an unapproved shape or box | Only the approved pill badge |
| Use at less than the minimum size | Detail disappears |

---

## 2.8 Co-Branding (Client Work)

When the logo appears alongside a client's:

- Separate with a 1px vertical rule at 40% opacity, with clear space on both sides
- Match **optical** weight, not pixel height — visually balance the two marks
- IGEN VERITAS sits on the right in "built by" lockups, on the left in partnership lockups
- Standard product footer: `Powered by IGEN VERITAS` — wordmark only, 12px, `#6B7280`

---

## 2.9 Favicon & App Icon

| Asset | Spec |
|---|---|
| Favicon | Icon only, 32×32 and 16×16 PNG, transparent |
| App icon | Icon centred at 66% of the canvas, on a Violet→Blue gradient square, rounded per platform |
| Social avatar | Icon centred on Dark Navy `#0B0B14`, no wordmark (illegible at avatar size) |

---

*Next: [03_Color_Palette.md](03_Color_Palette.md)*
