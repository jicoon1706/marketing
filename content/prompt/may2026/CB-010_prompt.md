# CB-010 — Education: 5 Things an AI Chatbot Does That Your Staff Simply Cannot

| Field | Value |
|---|---|
| **Brief ID** | CB-010 |
| **Date** | May 15, 2026 |
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
- Line 1: "5 Things an AI Chatbot Does"
- Line 2: "That Your Staff Simply Cannot"

**Feature rows (5 rows, each with blue circle "v" icon left + white text):**
```
Reply to leads in under 3 seconds — every time
Handle 20 enquiries simultaneously without slowing
Auto follow-up on Day 1, Day 3, and Day 7
Save every lead to Google Sheets in real time
Work 365 days — no leave, no sick days, no delays
```

**Subtext:**
"This is what automation looks like in a real business."

**CTA pill button (dark navy):**
"DM 'BOT' to see which plan fits you"

**Footer:**
"igenveritas.com  ·  info@igenveritas.com"

---

## Generation Call

```python
tmpl_edu(
    "CB010_May15_edu_5things_chatbot.png",
    headline_lines=["5 Things an AI Chatbot Does", "That Your Staff Simply Cannot"],
    points=[
        "Reply to leads in under 3 seconds — every time",
        "Handle 20 enquiries simultaneously without slowing",
        "Auto follow-up on Day 1, Day 3, and Day 7",
        "Save every lead to Google Sheets in real time",
        "Work 365 days — no leave, no sick days, no delays",
    ],
    subtext="This is what automation looks like in a real business.",
    cta="DM 'BOT' to see which plan fits you"
)
```
