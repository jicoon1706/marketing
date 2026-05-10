# CB-006 — Pain Point: 5 Signs Your Business Is Leaking Leads

| Field | Value |
|---|---|
| **Brief ID** | CB-006 |
| **Date** | May 12, 2026 (8:00 AM) |
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
- Line 1: "5 Signs Your Business" — white
- Line 2: "Is Leaking Leads Right Now" — violet (`#7b67d1`)

**Glassmorphism card (center):**
White semi-transparent rounded card containing 5 bullet lines:
```
[x]  You reply to enquiries the next morning
[x]  Your website has no chat widget
[x]  New leads get buried in WhatsApp
[x]  You've never followed up twice
[x]  Unknown enquiry count last month
```

**Subtext (below card):**
"Spot 2 or more? You have a system problem — not a marketing one."

**CTA pill button (violet):**
"DM 'LEADS' to see the fix"

**Footer:**
"igenveritas.com  ·  info@igenveritas.com"

---

## Generation Call

```python
tmpl_pain(
    "CB006_May12_pain_5signs.png",
    headline_lines=["5 Signs Your Business", "Is Leaking Leads Right Now"],
    bullet_lines=[
        "  [x]  You reply to enquiries the next morning",
        "  [x]  Your website has no chat widget",
        "  [x]  New leads get buried in WhatsApp",
        "  [x]  You've never followed up twice",
        "  [x]  Unknown enquiry count last month",
    ],
    subtext="Spot 2 or more? You have a system problem — not a marketing one.",
    cta="DM 'LEADS' to see the fix"
)
```
