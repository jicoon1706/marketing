# CB-011 — Social Proof: 3 Qualified Leads Before Breakfast

| Field | Value |
|---|---|
| **Brief ID** | CB-011 |
| **Date** | May 16, 2026 |
| **Platform** | Instagram |
| **Post Type** | Social Proof |
| **Service** | AI Chatbot |
| **Template** | C — Social Proof (purple gradient, story card + stats row) |

---

## Visual Prompt

**Background:** Vertical gradient — purple (`#8a5dcc`) to violet (`#7b67d1`). Faint blue radial glow bottom-right.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igen-veritas.com" — body gray, 22px

**Headline (centered, large bold white):**
- Line 1: "3 Qualified Leads"
- Line 2: "Before Breakfast."

**Story card (glassmorphism, centered):**
White semi-transparent rounded card with 4 lines of story text:
```
Beauty salon owner in KL — frustrated by ad spend leaking into
unanswered after-hours enquiries. We set up her chatbot in 5 days.
Week 1: 3 leads captured 10PM–7AM. All 3 booked a consultation.
Zero staff hours used. Everything automated.
```

**Stats row (3 cards below story):**
| Card | Value | Label |
|---|---|---|
| 1 | "5 Days" | Setup Time |
| 2 | "3 Captured" | Leads Wk 1 |
| 3 | "0 hrs" | Staff Hours |

**CTA pill button (dark navy):**
"DM 'BOT' to get yours built"

**Footer:**
"igen-veritas.com  ·  igenveritas@gmail.com"

---

## Generation Call

```python
tmpl_proof(
    "CB011_May16_proof_breakfast_leads.png",
    headline_lines=["3 Qualified Leads", "Before Breakfast."],
    story_lines=[
        "Beauty salon owner in KL — frustrated by ad spend leaking into",
        "unanswered after-hours enquiries. We set up her chatbot in 5 days.",
        "Week 1: 3 leads captured 10PM–7AM. All 3 booked a consultation.",
        "Zero staff hours used. Everything automated.",
    ],
    stats=[
        ("Setup Time", "5 Days"),
        ("Leads Wk 1", "3 Captured"),
        ("Staff Hours", "0 hrs"),
    ],
    cta="DM 'BOT' to get yours built"
)
```
