# 07 · Services and Offerings

> How we present what we sell. Full technical detail lives in `services/ai-chatbot/AI_Chatbot_Packages.md` and `services/IGEN_Veritas_Services Master Reference.md`.

---

## 7.1 What We Sell

| # | Offering | Model |
|---|---|---|
| 1 | **Website AI Chatbot Packages** | Setup fee + monthly retainer |
| 2 | **Web Development** | One-time project |
| 3 | **Mobile App Development** | One-time project |
| 4 | **Domain & Hosting** | Resell margin, recurring |

---

## 7.2 Core Positioning — AI Chatbot

> A chatbot embedded directly on the client's website. **Not** a standalone sales agent. **Not** a WhatsApp inbox tool.

The primary job is capturing and converting website visitors who would otherwise leave without making contact. The target client already has a website and has no AI chatbot on it.

**Say this:** "It sits on your website and answers visitors instantly, day or night."
**Not this:** "It's an omnichannel conversational AI platform."

---

## 7.3 Package Tiers

| | **Basic** | **Growth** | **Pro** |
|---|---|---|---|
| **Setup** | RM 500 | RM 1,000 | RM 2,000 |
| **Monthly** | RM 150/mo | RM 300/mo | RM 500/mo |
| **Tools** | Botpress | Botpress + n8n | Botpress + n8n (full) |
| **Best for** | Small businesses starting with automation | Growing businesses needing WhatsApp + CRM sync | Full AI funnel, lead scoring, multi-step follow-up |

**Growth is the hero tier.** In any three-card layout, Growth carries the Violet glow border and the "Most Popular" badge.

### Feature Ladder

| Feature | Basic | Growth | Pro |
|---|:---:|:---:|:---:|
| 24/7 AI chatbot on website | ✓ | ✓ | ✓ |
| FAQ answering from knowledge base | ✓ | ✓ | ✓ |
| Lead capture (name, phone, email) | ✓ | ✓ | ✓ |
| Booking & appointment flow | ✓ | ✓ | ✓ |
| BM + English support | ✓ | ✓ | ✓ |
| Mandarin support | — | ✓ | ✓ |
| WhatsApp integration | — | ✓ | ✓ |
| Google Sheets lead sync | — | ✓ | ✓ |
| Lead scoring & hot-lead alerts | — | — | ✓ |
| Multi-step follow-up (Day 1 / 3 / 7) | — | — | ✓ |
| Weekly performance dashboard | — | — | ✓ |

---

## 7.4 Pricing Presentation Rules

1. **Pricing is fixed and public.** Never quote outside these tiers without explicit confirmation from leadership.
2. **Always show setup and monthly together.** `RM 1,000 setup · RM 300/mo` — never a monthly figure alone.
3. **Never discount the price.** Adjust the scope instead.
4. **Anchor with three tiers**, always in Basic → Growth → Pro order, left to right.
5. **Never hide the price** behind "contact us for a quote" on a package we've already priced.
6. Format: `RM` + space + comma separator → `RM 2,000` ✓ · `RM2000` ✗

---

## 7.5 Web & Mobile Development

| Service | What it is | Stack |
|---|---|---|
| **Website Development** | Responsive, fast, modern websites for businesses | React / Laravel |
| **Mobile App Development** | Native iOS & Android plus cross-platform apps | Flutter / Firebase |
| **Design** | UI/UX for both | Figma |

Priced per project after scoping. Present as a **process**, not a price list:

```
Discovery → Design → Build → Test → Launch → Support
```

---

## 7.6 Tech Stack (Client-Facing)

Name these openly — transparency is a differentiator, not a risk.

| Tool | Purpose |
|---|---|
| **Botpress** | AI chatbot builder — flows, knowledge base, autonomous nodes |
| **n8n** | Workflow automation — webhooks, follow-ups, Google Sheets |
| **WABlas** | WhatsApp Business API |
| **Google Sheets** | Lead CRM for Growth & Pro |
| **OpenAI API** | AI task cards inside Botpress |
| **Fonnte / Meta Cloud API** | WhatsApp delivery (optional) |
| **React / Laravel** | Web development |
| **Flutter / Firebase** | Mobile development |
| **Figma** | Design & UI |

---

## 7.7 How to Talk About Each Package

### Basic — "Get answering"
> For a business that just needs the website to stop going silent. The chatbot answers FAQs, captures contact details, and books appointments. BM and English.

**Lead with:** the setup speed and the price floor.

### Growth — "Get organised"
> Everything in Basic, plus WhatsApp and automatic lead sync to Google Sheets. Every enquiry lands in one sheet, so nothing gets lost between the website and your phone.

**Lead with:** WhatsApp + no leads falling through cracks.

### Pro — "Get a funnel"
> Everything in Growth, plus lead scoring, hot-lead alerts, automated Day 1 / 3 / 7 follow-up, and a weekly performance dashboard. It doesn't just capture — it follows up.

**Lead with:** follow-up automation and the dashboard.

---

## 7.8 Deliverables & Timeline

| Package | Typical setup time |
|---|---|
| Basic | 3–5 days |
| Growth | 5–7 days |
| Pro | 7–10 days |

Every setup includes: knowledge-base training on the client's own content, brand-matched chat widget styling, a handover walkthrough, and 30 days of post-launch adjustments.

**Build order for Pro bots:**
`QualifyNode → ReturningCheck → GoalSelection → SmartRecommend → UpsellNode → BundleSummary → BookSession → n8n webhooks`

---

## 7.9 The Chatbot Widget — Brand Application

The widget is a brand surface. It follows the same rules as everything else.

| Element | Spec |
|---|---|
| Launcher bubble | 60px circle, Hero Gradient fill, white icon, `0 8px 24px rgba(123,103,209,0.4)` |
| Position | Bottom-right, 24px inset |
| Header | Hero Gradient, white Inter SemiBold 16px, bot name + status dot |
| Bot bubbles | `#F3F4F6` fill, `#0B0B14` text, 16px radius |
| User bubbles | Violet `#7B67D1` fill, white text, 16px radius |
| Input field | White, 1px `#E5E7EB` border, 12px radius |
| Footer | `Powered by IGEN VERITAS` — 11px `#6B7280` |
| Typing indicator | Three Violet dots |

**Custom-styled to the client's brand** where the client requests it — the IGEN VERITAS footer label stays regardless.

---

## 7.10 Revenue Model (Internal)

| Stream | Type |
|---|---|
| Chatbot setup fee | One-time |
| Monthly chatbot retainer | Recurring |
| Web / app development | One-time project |
| Domain & hosting resell margin | Recurring |

Tool running cost across multiple clients: **RM 375–470/mo**. At 20 Growth clients → roughly **RM 4,800/month recurring profit**.

> Internal figures. Never publish margin numbers in client-facing material.

---

## 7.11 Client Data Rules

- Lead data (names, phones, emails) stays in client-specific folders and that client's Google Sheet. **Never mixed across clients.**
- Never screenshot a real client conversation without redacting PII and getting permission.
- Never name a client in marketing without written approval.
- Results shared publicly must be numbers we can evidence.

---

*Next: [08_Applications.md](08_Applications.md)*
