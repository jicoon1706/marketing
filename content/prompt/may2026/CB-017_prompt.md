# CB-017 — Education: Your Customers Are on Their Phones 6+ Hours a Day

| Field | Value |
|---|---|
| **Brief ID** | CB-017 |
| **Date** | May 26, 2026 |
| **Platform** | Instagram |
| **Post Type** | Education |
| **Service** | Mobile App Development |
| **Template** | B — Education (violet→blue gradient, checklist rows) |

---

## Visual Prompt

**Background:** Vertical gradient — violet (`#7b67d1`) at top transitioning to blue bright (`#4196e6`) at bottom. Dark navy overlay on top ~300px for contrast.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igenveritas.com" — body gray, 22px

**Service badge (top-right):**
Blue pill badge: "Mobile App"

**Headline (centered, large bold white):**
- Line 1: "Your Customers Are on Their"
- Line 2: "Phones 6+ Hours a Day."

**Feature rows (5 rows, each with blue circle "v" icon left + white text):**
```
Direct channel — no algorithm, no ad spend needed
Push notifications for promos, appointments & updates
Customers browse, book, or order without calling
Builds brand loyalty through a product they use daily
iOS + Android from one codebase (Flutter)
```

**Subtext:**
"Built with Flutter + Firebase. Fast, scalable, built for Malaysian users."

**CTA pill button (dark navy):**
"DM 'APP' to discuss your idea"

**Footer:**
"igenveritas.com  ·  info@igenveritas.com"

---

## Generation Call

```python
tmpl_edu(
    "CB017_May26_edu_mobile_app.png",
    headline_lines=["Your Customers Are on Their", "Phones 6+ Hours a Day."],
    points=[
        "Direct channel — no algorithm, no ad spend needed",
        "Push notifications for promos, appointments & updates",
        "Customers browse, book, or order without calling",
        "Builds brand loyalty through a product they use daily",
        "iOS + Android from one codebase (Flutter)",
    ],
    subtext="Built with Flutter + Firebase. Fast, scalable, built for Malaysian users.",
    cta="DM 'APP' to discuss your idea",
    service_badge="Mobile App"
)
```
