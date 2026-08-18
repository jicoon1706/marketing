# CB-021 — Education: Flutter vs Native App — What Should Your Biz Actually Build?

| Field | Value |
|---|---|
| **Brief ID** | CB-021 |
| **Date** | May 29, 2026 |
| **Platform** | Instagram |
| **Post Type** | Education / Awareness |
| **Service** | Mobile App Development |
| **Template** | B — Education (violet→blue gradient, checklist rows) |

---

## Visual Prompt

**Background:** Vertical gradient — violet (`#7b67d1`) at top transitioning to blue bright (`#4196e6`) at bottom. Dark navy overlay on top ~300px for contrast.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igen-veritas.com" — body gray, 22px

**Service badge (top-right):**
Blue pill badge: "Mobile App"

**Headline (centered, large bold white):**
- Line 1: "Flutter vs Native App —"
- Line 2: "What Should Your Biz Actually Build?"

**Feature rows (5 rows, each with blue circle "v" icon left + white text):**
```
Flutter: 1 codebase → iOS + Android
70–80% lower cost vs full native build
Near-native performance for most SME apps
Faster to build, faster to update
Right choice for 90% of SME projects
```

**Subtext:**
"Booking, loyalty, catalogue, or client portal — Flutter wins."

**CTA pill button (dark navy):**
"DM 'APP' to discuss your project"

**Footer:**
"igen-veritas.com  ·  igenveritas@gmail.com"

---

## Generation Call

```python
tmpl_edu(
    "CB021_May29_edu_flutter_vs_native.png",
    headline_lines=["Flutter vs Native App —", "What Should Your Biz Actually Build?"],
    points=[
        "Flutter: 1 codebase → iOS + Android",
        "70–80% lower cost vs full native build",
        "Near-native performance for most SME apps",
        "Faster to build, faster to update",
        "Right choice for 90% of SME projects",
    ],
    subtext="Booking, loyalty, catalogue, or client portal — Flutter wins.",
    cta="DM 'APP' to discuss your project",
    service_badge="Mobile App"
)
```
