# CB-007 — Pain Point: Every Visitor Who Leaves Is a Lead You Handed Away

| Field | Value |
|---|---|
| **Brief ID** | CB-007 |
| **Date** | May 12, 2026 (7:00 PM) |
| **Platform** | Instagram |
| **Post Type** | Pain Point |
| **Service** | AI Chatbot |
| **Template** | A — Pain Point (dark navy, violet glow, bullet card) |

---

## Visual Prompt

**Background:** Dark navy (`#0b0b14`), violet radial glow center-left, faint blue glow top-right.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igenveritas.com" — body gray, 22px

**Headline (centered, large bold):**
- Line 1: "Every Visitor Who Leaves" — white
- Line 2: "Is a Lead You Handed Away" — violet (`#7b67d1`)

**Glassmorphism card (center):**
White semi-transparent rounded card containing 4 scenario lines:
```
>>  Visited your website at 11:47 PM
>>  Had a question. Nobody there to answer.
>>  Googled the next option. Found your competitor.
>>  You never even knew they were there.
```

**Subtext (below card):**
"An AI chatbot replies in 3 seconds. Starts at RM500 setup."

**CTA pill button (violet):**
"DM 'BOT' to get started"

**Footer:**
"igenveritas.com  ·  info@igenveritas.com"

---

## Generation Call

```python
tmpl_pain(
    "CB007_May12_pain_visitor_lost.png",
    headline_lines=["Every Visitor Who Leaves", "Is a Lead You Handed Away"],
    bullet_lines=[
        "  >>  Visited your website at 11:47 PM",
        "  >>  Had a question. Nobody there to answer.",
        "  >>  Googled the next option. Found your competitor.",
        "  >>  You never even knew they were there.",
    ],
    subtext="An AI chatbot replies in 3 seconds. Starts at RM500 setup.",
    cta="DM 'BOT' to get started"
)
```
