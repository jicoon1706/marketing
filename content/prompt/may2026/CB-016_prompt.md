# CB-016 — Social Proof: Before: 0 Replies After Hours. After: 11 Leads in Week 1.

| Field | Value |
|---|---|
| **Brief ID** | CB-016 |
| **Date** | May 25, 2026 |
| **Platform** | Instagram |
| **Post Type** | Social Proof |
| **Service** | AI Chatbot |
| **Template** | C — Social Proof (purple gradient, story card + stats row) |

---

## Visual Prompt

**Background:** Vertical gradient — purple (`#8a5dcc`) to violet (`#7b67d1`). Faint blue radial glow bottom-right.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igenveritas.com" — body gray, 22px

**Headline (centered, large bold white):**
- Line 1: "Before: 0 Replies After Hours."
- Line 2: "After: 11 Leads in Week 1."

**Story card (glassmorphism, centered):**
White semi-transparent rounded card with 4 lines:
```
Tuition centre in Selangor — parents enquired after dinner.
By morning, half had enrolled elsewhere. We built a Growth chatbot.
Week 1: 11 leads captured, 7 converted to consultations.
0 staff hours used after hours. All on autopilot.
```

**Stats row (3 cards below story):**
| Card | Value | Label |
|---|---|---|
| 1 | "11" | Leads Wk 1 |
| 2 | "7 / 11" | Conversions |
| 3 | "0 hrs" | Staff Hours |

**CTA pill button (dark navy):**
"DM 'BOT' to get yours built this month"

**Footer:**
"igenveritas.com  ·  info@igenveritas.com"

---

## Generation Call

```python
tmpl_proof(
    "CB016_May25_proof_11leads_tuition.png",
    headline_lines=["Before: 0 Replies After Hours.", "After: 11 Leads in Week 1."],
    story_lines=[
        "Tuition centre in Selangor — parents enquired after dinner.",
        "By morning, half had enrolled elsewhere. We built a Growth chatbot.",
        "Week 1: 11 leads captured, 7 converted to consultations.",
        "0 staff hours used after hours. All on autopilot.",
    ],
    stats=[
        ("Leads Wk 1", "11"),
        ("Conversions", "7 / 11"),
        ("Staff Hours", "0 hrs"),
    ],
    cta="DM 'BOT' to get yours built this month"
)
```
