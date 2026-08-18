# CB-023 — CTA: Setup Complete in 5–7 Days. No Technical Knowledge Needed.

| Field | Value |
|---|---|
| **Brief ID** | CB-023 |
| **Date** | May 31, 2026 |
| **Platform** | Instagram |
| **Post Type** | CTA / Conversion |
| **Service** | AI Chatbot |
| **Template** | B — Education (violet→blue gradient, checklist rows) |

---

## Visual Prompt

**Background:** Vertical gradient — violet (`#7b67d1`) at top transitioning to blue bright (`#4196e6`) at bottom. Dark navy overlay on top ~300px for contrast.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igen-veritas.com" — body gray, 22px

**Headline (centered, large bold white):**
- Line 1: "Setup Complete in 5–7 Days."
- Line 2: "No Technical Knowledge Needed."

**Feature rows (4 rows — process steps, each with blue circle "v" icon left + white text):**
```
Day 1 — Brief: Tell us about your business
Days 2–4 — Build: We configure & train the AI
Day 5 — Test: Every scenario thoroughly covered
Days 6–7 — Launch: Script embedded in your site. Done.
```

**Subtext (pricing tier summary):**
"Basic RM500+RM150/mo  ·  Growth RM1,000+RM300/mo  ·  Pro RM2,000+RM500/mo"

**CTA pill button (dark navy):**
"DM 'START' to lock in your June slot"

**Footer:**
"igen-veritas.com  ·  igenveritas@gmail.com"

---

## Generation Call

```python
tmpl_edu(
    "CB023_May31_cta_setup_process.png",
    headline_lines=["Setup Complete in 5–7 Days.", "No Technical Knowledge Needed."],
    points=[
        "Day 1 — Brief: Tell us about your business",
        "Days 2–4 — Build: We configure & train the AI",
        "Day 5 — Test: Every scenario thoroughly covered",
        "Days 6–7 — Launch: Script embedded in your site. Done.",
    ],
    subtext="Basic RM500+RM150/mo  ·  Growth RM1,000+RM300/mo  ·  Pro RM2,000+RM500/mo",
    cta="DM 'START' to lock in your June slot"
)
```
