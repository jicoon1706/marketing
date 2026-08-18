# Assets

## `logos/`

| File | Background | Use |
|---|---|---|
| `Logo Colour.png` | White / light | **Default** — documents, proposals, print |
| `Logo Black.png` | White / light | Mono and single-colour print |
| `Transparent Colour.png` | Any | Overlaying gradients, posters, photos |
| `Transparent Black.png` | Light only | Watermarks on light imagery |
| `Text.png` | Any | Wordmark only — narrow lockups, footers |

Rules: `../02_Logo_and_Identity.md`

## Gradients

Gradients are **generated from the recipes**, not stored as image files. Build them from the CSS or Python values in `../03_Color_Palette.md` §3.5 — that way they render at any size, any aspect ratio, without resampling.

---

**Fonts:** Inter is not bundled here — download from [Google Fonts](https://fonts.google.com/specimen/Inter). Windows generation scripts fall back to Segoe UI (`C:/Windows/Fonts/segoeuib.ttf`).

**Source of truth:** the logo files are copied from `marketing_team/brand/assets/`. If a logo is updated, update it there first, then re-copy here.
