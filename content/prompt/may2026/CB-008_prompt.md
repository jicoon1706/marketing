# CB-008 — Education: POV: It's 2AM. Someone Just Found Your Website.

| Field | Value |
|---|---|
| **Brief ID** | CB-008 |
| **Date** | May 13, 2026 |
| **Platform** | Instagram |
| **Post Type** | Education |
| **Service** | AI Chatbot |
| **Template** | B — Education (violet→blue gradient, checklist rows) |

---

## Visual Prompt

**Background:** Vertical gradient — violet (`#7b67d1`) at top transitioning to blue bright (`#4196e6`) at bottom. Dark navy overlay on top ~300px for contrast.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igenveritas.com" — body gray, 22px

**Headline (centered, large bold white):**
- Line 1: "POV: It's 2AM."
- Line 2: "Someone Just Found Your Website."

**Feature rows (5 rows, each with blue circle "v" icon left + white text):**
```
Visitor lands on your site
AI chatbot greets them in under 3 seconds
Answers their questions about your service
Qualifies them as a serious lead
You wake up to a filled inbox — not a missed sale
```

**Subtext:**
"Tanpa hire staff tambahan. Running every night on autopilot."

**CTA pill button (dark navy):**
"DM 'BOT' — Basic from RM500 setup"

**Footer:**
"igenveritas.com  ·  info@igenveritas.com"

---

## Generation Call

```python
tmpl_edu(
    "CB008_May13_edu_2am_pov.png",
    headline_lines=["POV: It's 2AM.", "Someone Just Found Your Website."],
    points=[
        "Visitor lands on your site",
        "AI chatbot greets them in under 3 seconds",
        "Answers their questions about your service",
        "Qualifies them as a serious lead",
        "You wake up to a filled inbox — not a missed sale",
    ],
    subtext="Tanpa hire staff tambahan. Running every night on autopilot.",
    cta="DM 'BOT' — Basic from RM500 setup"
)
```
