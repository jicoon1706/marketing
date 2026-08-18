# 03 · Colour Palette

---

## 3.1 Primary Colours

| Name | Hex | RGB | Usage |
|---|---|---|---|
| **Violet** | `#7B67D1` | 123, 103, 209 | Hero backgrounds, primary CTA buttons, key accents |
| **Purple** | `#8A5DCC` | 138, 93, 204 | Dark sections, footer, depth layers |

Violet is the signature. If someone remembers one colour, it should be this one.

---

## 3.2 Accent Colours

| Name | Hex | RGB | Usage |
|---|---|---|---|
| **Blue Mid** | `#488FE3` | 72, 143, 227 | Cards, highlights, secondary buttons, section labels |
| **Blue Bright** | `#4196E6` | 65, 150, 230 | Data visuals, hover states, mobile card accents |

---

## 3.3 Neutrals

| Name | Hex | RGB | Usage |
|---|---|---|---|
| **Dark Navy** | `#0B0B14` | 11, 11, 20 | Page background, dark overlays, primary text on light |
| **White** | `#FFFFFF` | 255, 255, 255 | Text on dark backgrounds, clean sections |
| **Body Gray** | `#6B7280` | 107, 114, 128 | Paragraph text, secondary descriptions, captions |

---

## 3.4 Functional Colours

Used sparingly, only for status and UI feedback — never as decoration.

| Name | Hex | Usage |
|---|---|---|
| Success / WhatsApp Green | `#25D366` | WhatsApp references, "delivered", positive stats |
| Warning | `#F5A524` | Attention states, "before" scenarios |
| Error / Urgency | `#E5484D` | Missed leads, "0 replies", pain-point indicators |

---

## 3.5 Gradient Recipes

| Name | Recipe | Angle | Usage |
|---|---|---|---|
| **Hero Gradient** | `#7B67D1` → `#4196E6` | 135° (top-left → bottom-right) | Main hero sections, large backgrounds |
| **Card Gradient** | `#8A5DCC` → `#488FE3` | 135° | Feature cards, highlight elements |
| **Purple Blend** | `#7B67D1` → `#8A5DCC` | 90° | Buttons, pills, badges |
| **Blue Blend** | `#488FE3` → `#4196E6` | 90° | Secondary CTA, data elements |
| **Night Glow** | `#0B0B14` base + radial `#7B67D1` at 30% | radial, centre-left | Pain-point posts, dramatic dark layouts |

### CSS

```css
--hero-gradient:  linear-gradient(135deg, #7B67D1 0%, #4196E6 100%);
--card-gradient:  linear-gradient(135deg, #8A5DCC 0%, #488FE3 100%);
--purple-blend:   linear-gradient(90deg,  #7B67D1 0%, #8A5DCC 100%);
--blue-blend:     linear-gradient(90deg,  #488FE3 0%, #4196E6 100%);
--night-glow:     radial-gradient(circle at 30% 45%, rgba(123,103,209,0.35) 0%, #0B0B14 65%);
```

### Python (Pillow / generation scripts)

```python
VIOLET      = "#7B67D1"
PURPLE      = "#8A5DCC"
BLUE_MID    = "#488FE3"
BLUE_BRIGHT = "#4196E6"
DARK_NAVY   = "#0B0B14"
WHITE       = "#FFFFFF"
BODY_GRAY   = "#6B7280"

HERO_GRADIENT = ("#7B67D1", "#4196E6")
CARD_GRADIENT = ("#8A5DCC", "#488FE3")
DARK_OVERLAY  = "rgba(11,11,20,0.85)"
```

---

## 3.6 Choosing a Gradient

Generate gradients from the recipes above — don't keep a library of pre-rendered background images. Rendering at the target canvas size avoids resampling artefacts and lets one recipe serve every aspect ratio.

| Post type | Gradient | Why |
|---|---|---|
| Pain point (Template A) | Night Glow | Dark and dramatic; the glow isolates the stat card |
| Education (Template B) | Hero Gradient | Bright and open; pills read clearly on it |
| Proof / demo (Template C) | Hero Gradient | Neutral enough that the UI mockup stays the focus |
| Offer / CTA (Template D) | Purple Blend | Deeper, heavier — signals the close |
| Website hero | Hero Gradient | The signature look |
| LinkedIn banner / reel cover | Blue Blend into Dark Navy | Wide formats need the darker end for text |
| Quote card / testimonial | Violet fading to White | Keeps long text legible |

**Direction:** 135° (top-left → bottom-right) for square and landscape; 180° (top → bottom) for stories and reels.

---

## 3.7 Glassmorphism Surfaces

The house card style. Used on every dark layout.

| Token | Value |
|---|---|
| Fill (light card on dark) | `rgba(255,255,255,0.05)` |
| Fill (emphasised card) | `rgba(255,255,255,0.08)` |
| Border | `1px solid rgba(255,255,255,0.10)` |
| Border (highlighted / "Most Popular") | `1px solid #7B67D1` + `0 0 32px rgba(123,103,209,0.45)` |
| Border radius | 24px (large cards) · 16px (small cards) · 12px (pills) |
| Backdrop blur | 16px |
| Shadow | `0 8px 32px rgba(11,11,20,0.35)` |

---

## 3.8 Usage Ratio

Aim for roughly this balance in any single composition:

```
Brand gradient / Violet family  ████████████████████████████  60%
Neutral (navy or white)         ████████████                  30%
Accent blue                     ███                            8%
Functional (green/red/amber)    █                              2%
```

**Rule of thumb:** if you can't see brand colour in a thumbnail, the design has failed.

---

## 3.9 Accessibility

Contrast ratios against common pairings (WCAG AA needs 4.5:1 for body text, 3:1 for large text ≥24px):

| Foreground | Background | Ratio | Verdict |
|---|---|---|---|
| White `#FFFFFF` | Dark Navy `#0B0B14` | 19.4:1 | ✅ Pass everywhere |
| White `#FFFFFF` | Violet `#7B67D1` | 4.0:1 | ⚠️ Large text only (≥24px, bold) |
| White `#FFFFFF` | Purple `#8A5DCC` | 4.3:1 | ⚠️ Large text only |
| Dark Navy `#0B0B14` | White `#FFFFFF` | 19.4:1 | ✅ Pass everywhere |
| Body Gray `#6B7280` | White `#FFFFFF` | 4.8:1 | ✅ Pass |
| Body Gray `#6B7280` | Dark Navy `#0B0B14` | 4.0:1 | ⚠️ Large text only |
| Violet `#7B67D1` | Dark Navy `#0B0B14` | 4.8:1 | ✅ Pass — use for accent words |

**Practical rules**

- Body copy on a gradient: always White, always ≥18px, always SemiBold or heavier
- Never set Body Gray at small sizes on Violet or Purple
- Never rely on colour alone to carry meaning — pair with an icon or label

---

## 3.10 Don'ts

- ✗ Don't introduce colours outside this palette (no teal, no orange, no pink)
- ✗ Don't use more than two gradient stops in a single surface
- ✗ Don't put a gradient behind body text — use a solid or a scrim
- ✗ Don't use pure black `#000000` — always Dark Navy `#0B0B14`
- ✗ Don't tint photography with brand colours to the point that detail is lost

---

*Next: [04_Typography.md](04_Typography.md)*
