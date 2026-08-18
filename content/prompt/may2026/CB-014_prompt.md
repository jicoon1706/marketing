# CB-014 — Package Reveal: Basic. Growth. Pro. Full Pricing — No Hidden Fees.

| Field | Value |
|---|---|
| **Brief ID** | CB-014 |
| **Date** | May 21, 2026 |
| **Platform** | Instagram |
| **Post Type** | Package Reveal / Consideration |
| **Service** | AI Chatbot |
| **Template** | D — Package / CTA (violet→purple flat, 3-column cards) |

---

## Visual Prompt

**Background:** Vertical gradient — violet (`#7b67d1`) to purple (`#8a5dcc`).

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igen-veritas.com" — body gray, 22px

**Headline (centered, large bold white):**
- Line 1: "Basic. Growth. Pro."
- Line 2: "Full Pricing — No Hidden Fees."

**3-column package cards (white glassmorphic cards):**

| Column | BASIC | GROWTH (featured) | PRO |
|---|---|---|---|
| Setup Price | RM500 | RM1,000 | RM2,000 |
| Monthly | + RM150/month | + RM300/month | + RM500/month |
| Feature 1 | AI chatbot on website | Everything in Basic | Everything in Growth |
| Feature 2 | 24/7 lead capture | WhatsApp follow-ups | Full n8n automation |
| Feature 3 | Trained on your biz | Google Sheets CRM | Advanced lead logic |
| Feature 4 | Human handoff | Owner notifications | Priority support |

- GROWTH card has blue border + "POPULAR" badge on top
- All cards have white glassmorphic fill with rounded corners

**CTA pill button (blue bright):**
"DM 'PLAN' — We'll match you to the right tier"

**Footer:**
"igen-veritas.com  ·  igenveritas@gmail.com"

---

## Generation Call

```python
tmpl_pkg(
    "CB014_May21_package_reveal.png",
    headline_lines=["Basic. Growth. Pro.", "Full Pricing — No Hidden Fees."],
    packages=[
        {
            "name": "BASIC",
            "price": "RM500",
            "monthly": "+ RM150/month",
            "features": ["AI chatbot on website", "24/7 lead capture", "Trained on your biz", "Human handoff"],
            "featured": False,
        },
        {
            "name": "GROWTH",
            "price": "RM1,000",
            "monthly": "+ RM300/month",
            "features": ["Everything in Basic", "WhatsApp follow-ups", "Google Sheets CRM", "Owner notifications"],
            "featured": True,
        },
        {
            "name": "PRO",
            "price": "RM2,000",
            "monthly": "+ RM500/month",
            "features": ["Everything in Growth", "Full n8n automation", "Advanced lead logic", "Priority support"],
            "featured": False,
        },
    ],
    cta="DM 'PLAN' — We'll match you to the right tier"
)
```
