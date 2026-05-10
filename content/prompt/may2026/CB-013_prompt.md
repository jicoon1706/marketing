# CB-013 — Education: Your Website Is Either Building Trust — Or Costing You Clients

| Field | Value |
|---|---|
| **Brief ID** | CB-013 |
| **Date** | May 20, 2026 |
| **Platform** | Instagram |
| **Post Type** | Education |
| **Service** | Web Development |
| **Template** | B — Education (violet→blue gradient, checklist rows) |

---

## Visual Prompt

**Background:** Vertical gradient — violet (`#7b67d1`) at top transitioning to blue bright (`#4196e6`) at bottom. Dark navy overlay on top ~300px for contrast.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igenveritas.com" — body gray, 22px

**Service badge (top-right):**
Blue pill badge: "Web Dev"

**Headline (centered, large bold white):**
- Line 1: "Your Website Is Either"
- Line 2: "Building Trust — Or Costing You Clients."

**Feature rows (5 rows, each with blue circle "v" icon left + white text):**
```
Loads fast on mobile (80%+ of Malaysians browse on phone)
Answers questions before a customer has to ask
Makes it easy to contact or book in 2 clicks
Builds credibility with first-time visitors
Works as your 24/7 sales rep when you're unavailable
```

**Subtext:**
"We build in React & Laravel — responsive, clean, built to convert."

**CTA pill button (dark navy):**
"DM 'WEB' to get started"

**Footer:**
"igenveritas.com  ·  info@igenveritas.com"

---

## Generation Call

```python
tmpl_edu(
    "CB013_May20_edu_website_trust.png",
    headline_lines=["Your Website Is Either", "Building Trust — Or Costing You Clients."],
    points=[
        "Loads fast on mobile (80%+ of Malaysians browse on phone)",
        "Answers questions before a customer has to ask",
        "Makes it easy to contact or book in 2 clicks",
        "Builds credibility with first-time visitors",
        "Works as your 24/7 sales rep when you're unavailable",
    ],
    subtext="We build in React & Laravel — responsive, clean, built to convert.",
    cta="DM 'WEB' to get started",
    service_badge="Web Dev"
)
```
