# CB-019 — Education: Bad Design Is Costing Your Business Money

| Field | Value |
|---|---|
| **Brief ID** | CB-019 |
| **Date** | May 27, 2026 |
| **Platform** | Instagram |
| **Post Type** | Education |
| **Service** | UI/UX Design |
| **Template** | B — Education (violet→blue gradient, checklist rows) |

---

## Visual Prompt

**Background:** Vertical gradient — violet (`#7b67d1`) at top transitioning to blue bright (`#4196e6`) at bottom. Dark navy overlay on top ~300px for contrast.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igenveritas.com" — body gray, 22px

**Service badge (top-right):**
Blue pill badge: "UI/UX"

**Headline (centered, large bold white):**
- Line 1: "Bad Design Is Costing"
- Line 2: "Your Business Money."

**Feature rows (5 rows, each with blue circle "v" icon left + white text):**
```
94% of first impressions are design-related
Guides visitors to act — contact, book, or buy
Reduces the time it takes to understand your offer
Increases conversion without spending more on ads
Makes your brand look like it belongs in 2026
```

**Subtext:**
"We design in Figma. Build in React & Flutter."

**CTA pill button (dark navy):**
"DM 'DESIGN' for a free website review"

**Footer:**
"igenveritas.com  ·  info@igenveritas.com"

---

## Generation Call

```python
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
```
