# IGEN VERITAS — AI Marketing Team Workspace

> This workspace is the operational hub for IGEN VERITAS's AI-powered marketing and client delivery team.

---

## Company at a Glance

| | |
|---|---|
| **Company** | IGEN VERITAS |
| **Tagline** | Powering the future with intelligent solutions and cutting-edge technology |
| **Industry** | AI, Web & Mobile App Development |
| **Location** | Batu Caves, Selangor, Malaysia |
| **Website** | igenveritas.com |
| **Email** | info@igenveritas.com / igenveritas@gmail.com |
| **Phone** | +60 17 310 3966 |

**IGEN** = New generation spirit — curious, adaptive, innovative.
**VERITAS** = Latin for *truth* — honesty, integrity, transparency in everything.

---

## Services

### 1. AI Chatbot Packages

| Package | Setup | Monthly | Tools |
|---|---|---|---|
| **Basic** | RM 500 | RM 150/mo | Botpress only |
| **Growth** | RM 1,000 | RM 300/mo | Botpress + n8n |
| **Pro** | RM 2,000 | RM 500/mo | Botpress + n8n (full) |

Full feature matrix and build checklists → [`services/ai-chatbot/AI_Chatbot_Packages.md`](services/ai-chatbot/AI_Chatbot_Packages.md)

### 2. Web & Mobile Development
- Responsive websites (React / Laravel)
- Native iOS & Android + cross-platform apps (Flutter / Firebase)
- Domain/hosting reselling margin included

---

## Tech Stack

| Tool | Purpose |
|---|---|
| **Botpress** | AI chatbot builder (conversation flows, KB, autonomous nodes) |
| **n8n** | Workflow automation (webhooks, follow-ups, Google Sheets) |
| **WABlas** | WhatsApp Business API (`deu.wablas.com`) |
| **Google Sheets** | Lead CRM for Growth & Pro clients |
| **OpenAI API** | AI task cards inside Botpress |
| **Fonnte / Meta Cloud API** | WhatsApp delivery (optional) |
| **React / Laravel** | Web development |
| **Flutter / Firebase** | Mobile development |
| **Figma** | Design & UI |

---

## Target Customers

- Malaysian SMEs
- Solo entrepreneurs & freelancers needing online presence
- Existing businesses with no website or an outdated one
- Business owners who want leads but can't afford a full marketing team

---

## Brand Snapshot

### Voice
- Confident but not arrogant
- Clear and direct — no fluff
- Forward-thinking, solution-oriented
- Mix of English and occasional BM references for the Malaysian market

### Tone by Platform
| Platform | Tone |
|---|---|
| Instagram | Bold, punchy, visual-first |
| LinkedIn | Professional, insightful, thought leadership |
| Website | Clean, confident, conversion-focused |
| WhatsApp/Email | Warm, helpful, responsive |

### Primary Colors
| Name | Hex |
|---|---|
| Violet | `#7b67d1` |
| Purple | `#8a5dcc` |
| Blue Mid | `#488fe3` |
| Blue Bright | `#4196e6` |
| Dark Navy | `#0b0b14` |
| White | `#ffffff` |
| Body Gray | `#6b7280` |

Full brand guidelines → [`brand/IGEN_VERITAS_Brand_Guidelines.md`](brand/IGEN_VERITAS_Brand_Guidelines.md)

---

## Workspace Folder Structure

```
marketing_team/
├── CLAUDE.md                          ← You are here
├── brand/                             ← Brand identity & assets
│   ├── IGEN_VERITAS_Brand_Guidelines.md
│   └── assets/                        ← Logos, color swatches, fonts
├── services/                          ← Service documentation
│   ├── ai-chatbot/
│   │   └── AI_Chatbot_Packages.md
│   └── web-mobile/                    ← Web & mobile dev SOPs
├── clients/                           ← One folder per client
│   └── _template/                     ← Copy this for each new client
│       ├── brief.md
│       ├── build-checklist.md
│       └── assets/
├── content/                           ← Social media & marketing content
│   ├── instagram/
│   ├── linkedin/
│   ├── captions/
│   └── _templates/                    ← Caption formula, hashtag banks
├── operations/                        ← Internal SOPs & processes
│   ├── onboarding/                    ← Client onboarding workflow
│   ├── deployment/                    ← Deployment checklists
│   └── reporting/                     ← Monthly report templates
├── business/                          ← Business strategy documents
│   └── IGen Veritas Business Model.pdf
└── memory/                            ← AI persistent memory (auto-managed)
```

---

## Social Media Strategy

### Posting Schedule
- **Instagram**: 3–4x per week
- **LinkedIn**: 2x per week
- **Best times**: Tue–Thu, 8–10am or 7–9pm MYT

### Launch Content Sequence
1. Brand Intro — Who is IGEN VERITAS? *(Awareness)*
2. Pain Point — "Your business is losing leads at 2AM" *(Pain)*
3. Solution — AI Chatbot that works 24/7 *(Education)*
4. Packages Reveal — Basic / Growth / Pro *(Consideration)*
5. CTA — "Ready to automate your business?" *(Conversion)*

### Caption Formula
```
[Bold hook — 1 sentence]

[2–3 lines explaining the value]

[Bullet points of key features/benefits]

[CTA — DM us / Link in bio / Comment below]

[Hashtags — 5–10 tags]
```

### Hashtags
`#AIchatbot #MalaysiaTech #WebDevelopment #MobileApp #BusinessAutomation`
`#KualaLumpur #IGenVeritas #WhatsAppBot #DigitalTransformation #StartupMalaysia`

---

## Revenue Model

| Stream | Type |
|---|---|
| AI Agent setup fee | One-time |
| Monthly chatbot retainer | Recurring |
| Web/app development | One-time project |
| Domain/hosting resell margin | Recurring |

**Realistic tool running cost (multiple clients): RM 375–470/mo**
> At 20 Growth clients → **RM 4,800/month recurring profit**

---

## Key Operating Rules for AI Agents

1. **Brand voice first** — all content must reflect the personality traits: Innovative, Trustworthy, Professional, Approachable.
2. **Language** — default English + BM mix; Mandarin only for Growth & Pro clients.
3. **Pricing is fixed** — never quote outside the defined package tiers without confirmation.
4. **Client data privacy** — lead data (names, phones, emails) stays in client-specific folders and Google Sheets. Never mix across clients.
5. **Build order for Pro bots** — QualifyNode → ReturningCheck → GoalSelection → SmartRecommend → UpsellNode → BundleSummary → BookSession → n8n webhooks.
6. **n8n webhook references after Wait nodes** — always use `$('Get row(s) in sheet').item.json['Field']`, NOT the original webhook reference (it fails after Wait).

---

## Vision & Mission

**Vision:** A future where businesses operate with clarity, confidence, and control through intelligent technology.

**Mission:** Design powerful, user-focused software that simplifies operations, accelerates growth, and enables smarter decisions.

---

*© 2026 IGEN VERITAS. All rights reserved.*
