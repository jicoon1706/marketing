# CB-020 — CTA: You've Been Thinking About This For Months. This Is the Week.

| Field | Value |
|---|---|
| **Brief ID** | CB-020 |
| **Date** | May 28, 2026 |
| **Platform** | Instagram |
| **Post Type** | CTA / Conversion |
| **Service** | AI Chatbot |
| **Template** | D — Package / CTA (violet→purple flat, 3-column cards) |

---

## Visual Prompt

**Background:** Vertical gradient — violet (`#7b67d1`) to purple (`#8a5dcc`).

**Brand header (top-left):**
- "IGEN VERITAS" — white, bold, 30px
- "igen-veritas.com" — body gray, 22px

**Headline (centered, 64px bold white):**
- Line 1: "You've Been Thinking About This"
- Line 2: "For Months. This Is the Week."

**3-column package cards (white glassmorphic cards):**

| Column | BASIC | GROWTH (featured) | PRO |
|---|---|---|---|
| Setup Price | RM500 | RM1,000 | RM2,000 |
| Monthly | + RM150/month | + RM300/month | + RM500/month |
| Feature 1 | Live in 5–7 days | WhatsApp follow-ups | Full n8n automation |
| Feature 2 | 24/7 lead capture | Google Sheets CRM | Advanced qualification |
| Feature 3 | No tech skills needed | Owner notifications | Priority build slot |

- GROWTH card has blue border + "POPULAR" badge on top
- Headline uses smaller font (64px) to accommodate longer text

**CTA pill button (blue bright):**
"DM 'START' — First 5 sign-ups get priority scheduling"

**Footer:**
"igen-veritas.com  ·  igenveritas@gmail.com"

---

## Generation Call

```python
tmpl_pkg(
    "CB020_May28_cta_this_is_the_week.png",
    headline_lines=["You've Been Thinking About This", "For Months. This Is the Week."],
    packages=[
        {
            "name": "BASIC",
            "price": "RM500",
            "monthly": "+ RM150/month",
            "features": ["Live in 5–7 days", "24/7 lead capture", "No tech skills needed"],
            "featured": False,
        },
        {
            "name": "GROWTH",
            "price": "RM1,000",
            "monthly": "+ RM300/month",
            "features": ["WhatsApp follow-ups", "Google Sheets CRM", "Owner notifications"],
            "featured": True,
        },
        {
            "name": "PRO",
            "price": "RM2,000",
            "monthly": "+ RM500/month",
            "features": ["Full n8n automation", "Advanced qualification", "Priority build slot"],
            "featured": False,
        },
    ],
    cta="DM 'START' — First 5 sign-ups get priority scheduling",
    hl_font_size=64
)
```
