# CB-022 — Social Proof: May 2026 Recap — What Our Clients Experienced

| Field | Value |
|---|---|
| **Brief ID** | CB-022 |
| **Date** | May 30, 2026 |
| **Platform** | Instagram |
| **Post Type** | Social Proof / Month-End |
| **Service** | AI Chatbot (primary) + All Services |
| **Template** | C — Social Proof (purple gradient, story card + stats row) |

---

## Visual Prompt

**Background:** Vertical gradient — purple (`#8a5dcc`) to violet (`#7b67d1`). Faint blue radial glow bottom-right.

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igen-veritas.com" — body gray, 22px

**Headline (centered, large bold white):**
- Line 1: "May 2026 Recap:"
- Line 2: "What Our Clients Experienced."

**Story card (glassmorphism, centered):**
White semi-transparent rounded card with 4 lines:
```
F&B (KL): 18 leads captured in Week 1 after chatbot launch.
Beauty salon (Selangor): 3 bookings before 8AM — overnight chatbot.
Tuition centre: 7 out of 11 overnight leads → consultations.
Website project: 5-day launch, fully responsive + mobile-first.
```

**Stats row (3 cards below story):**
| Card | Value | Label |
|---|---|---|
| 1 | "32+ Total" | Leads Captured |
| 2 | "5 Days" | Avg Setup |
| 3 | "Running" | After-hrs Revenue |

**CTA pill button (dark navy):**
"DM 'START' — June build slots now open"

**Footer:**
"igen-veritas.com  ·  igenveritas@gmail.com"

---

## Generation Call

```python
tmpl_proof(
    "CB022_May30_proof_may_recap.png",
    headline_lines=["May 2026 Recap:", "What Our Clients Experienced."],
    story_lines=[
        "F&B (KL): 18 leads captured in Week 1 after chatbot launch.",
        "Beauty salon (Selangor): 3 bookings before 8AM — overnight chatbot.",
        "Tuition centre: 7 out of 11 overnight leads → consultations.",
        "Website project: 5-day launch, fully responsive + mobile-first.",
    ],
    stats=[
        ("Leads Captured", "32+ Total"),
        ("Avg Setup", "5 Days"),
        ("After-hrs Revenue", "Running"),
    ],
    cta="DM 'START' — June build slots now open"
)
```
