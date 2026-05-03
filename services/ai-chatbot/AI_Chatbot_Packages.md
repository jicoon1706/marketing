# AI Chatbot Service Packages — Master Reference

> Last updated: April 2026 | All prices in MYR

---

## Package Overview

| | Basic | Growth | Pro |
|---|---|---|---|
| **Setup Fee** | RM500 | RM1,000 | RM2,000 |
| **Monthly** | RM150/mo | RM300/mo | RM500/mo |
| **Tools** | Botpress only | Botpress + n8n | Botpress + n8n (full) |
| **Your Profit/mo** | ~RM120 | ~RM240 | ~RM400 |

## Tool Cost Reference

| Tool | Cost |
|---|---|
| Botpress free plan | RM0 (500 conversations/mo) |
| Botpress Team plan | ~RM200/mo (for multiple clients) |
| n8n cloud | ~RM85/mo |
| VPS for self-hosting n8n | ~RM20–40/mo (Contabo / DigitalOcean) |
| WhatsApp API — WABlas (unofficial) | ~$2/mo per device (~RM9/client) |
| OpenAI API (per client usage) | ~RM20–50/mo depending on volume |

**Realistic total tool cost running multiple clients: RM375–470/mo**
> 💡 At 20 Growth clients: **RM4,800/month profit recurring**

## Full Feature Matrix

| Feature | Basic | Growth | Pro |
|---|:---:|:---:|:---:|
| Web widget chatbot | ✅ | ✅ | ✅ |
| FAQ (knowledge base) | ✅ | ✅ | ✅ |
| Lead capture (name, phone, email) | ✅ | ✅ | ✅ |
| Email notification to owner | ✅ | ✅ | ✅ |
| BM + English | ✅ | ✅ | ✅ |
| Mandarin support | ❌ | ✅ | ✅ |
| WhatsApp to owner | ❌ | ✅ | ✅ |
| Google Sheets sync | ❌ | ✅ | ✅ |
| 24hr follow-up (1 message) | ❌ | ✅ | ✅ |
| Monthly report | ❌ | ✅ | ✅ |
| Sales funnel (qualify → recommend → book) | ❌ | ❌ | ✅ |
| Lead scoring (hot/warm/cold) | ❌ | ❌ | ✅ |
| AI smart recommendations | ❌ | ❌ | ✅ |
| Upsell / bundle sequences | ❌ | ❌ | ✅ |
| Multi-step follow-up (Day 1/3/7) | ❌ | ❌ | ✅ |
| Conversion tracking | ❌ | ❌ | ✅ |
| Weekly performance dashboard | ❌ | ❌ | ✅ |
| Hot lead alert (15-min call prompt) | ❌ | ❌ | ✅ |
| Human handoff for hot leads | ❌ | ❌ | ✅ |
| Priority support | ❌ | ❌ | ✅ |

---
---

# 📦 BASIC PACKAGE

**RM500 setup + RM150/mo** | Tools: Botpress only

## Features

- Web widget chatbot on client website
- FAQ answers from knowledge base (AutonomousNode)
- Full service booking flow with sub-service selection
- Lead capture (name, phone, email) at booking step
- 2x Email notifications on booking (owner + customer)
- Hubungi Kami contact branch
- BM + English support
- ❌ n8n not needed — keep costs low

---

## Conversation Flow

```
[Greeting]
"Hai! 👋 Selamat datang ke @workflow.business_name"
↓
[MenuChoice] — Single Choice
├── Tanya Soalan / FAQ  ──→ [AutonomousNode]
│                              (Knowledge Base + "user wants to book" → BookSession)
├── Hubungi Kami
└── Tinggalkan Maklumat ──→ [BookSession]
                                ├── Capture: user_name
                                ├── Capture: user_phone
                                ├── Capture: user_email
                                ↓
                           [ChooseServices] — Single Choice (user_service)
                                ├── Servis Rambut  → [ServiceRambut]  (user_subservice → always)
                                ├── Servis Kuku    → [ServKuku]       (user_subservice → always)
                                ├── Eyelash & Brow → [EyelashBrow]    (user_subservice → always)
                                ├── Facial & Muka  → [FacialMuka]     (user_subservice → always)
                                └── Waxing         → [Waxing]         (user_subservice → always)
                                        ↓ (all merge here)
                           [SubServiceExplanation]
                                ├── AI card: KB lookup
                                ├── Text: @workflow.nextMessage
                                └── Single Choice:
                                    ├── Ya, book sekarang! ──→ [BookServices]
                                    ├── Pilih servis lain  ──→ [ChooseServices]
                                    └── Tanya soalan lain  ──→ [AutonomousNode]
                                             ↓
                                       [BookServices]
                                         ├── Insert Record
                                         ├── Confirmation text
                                         ├── Send Email (owner)
                                         └── Send Email (customer)
                                             ↓
                                       [AnotherQuestion]
                                         ├── Yes, I have another question! ──→ [MenuChoice]
                                         └── No, I'm all good. ─────────────→ [End]
```

---

## Node Details

| Node | Cards / Config |
|---|---|
| **Greeting** | Text: `"Hai! 👋 Selamat datang ke @workflow.greeting_translated"` |
| **MenuChoice** | Single Choice: Tanya Soalan / FAQ \| Hubungi Kami \| Tinggalkan Maklumat |
| **AutonomousNode** | Instructions: salon info \| KB: 1 attached \| Transition: "user wants to book" → BookSession |
| **BookSession** | Capture Cards: `user_name`, `user_phone`, `user_email` (in order) |
| **ChooseServices** | Single Choice → `user_service` \| 5 options |
| **Service Nodes** (×5) | Each: Capture `user_subservice` → `always` → SubServiceExplanation |
| **SubServiceExplanation** | AI card (KB) + Text `@workflow.nextMessage` + Single Choice (book / pilih lain / tanya lain) |
| **BookServices** | Insert Record + Confirmation text + Send Email ×2 (owner + customer) |
| **AnotherQuestion** | Single Choice: Yes → MenuChoice \| No → End |

## Variables Used

```
workflow.greeting_translated
workflow.user_name
workflow.user_phone
workflow.user_email
workflow.user_service
workflow.user_subservice
workflow.nextMessage
```

## Integrations

| Integration | Notes |
|---|---|
| Webchat (Built-in) | Web widget — embed with 1 `<script>` tag. Zero extra cost. |
| Email / SMTP | Fires on BookServices → owner + customer. Use client's Gmail. Free. |

> ⚙️ **Optional upsell:** WhatsApp via Meta Cloud API (free up to 1,000 conv/mo). Requires Meta Business verification.

---

## ✅ Build Checklist — Basic

```
BOTPRESS — CONVERSATION NODES
✅ Greeting             — Text: "Hai! 👋 Selamat datang ke @workflow.greeting_translated"
✅ MenuChoice           — Single Choice: Tanya Soalan / FAQ | Hubungi Kami | Tinggalkan Maklumat
✅ AutonomousNode       — KB attached (1x), transition: "user wants to book" → BookSession
✅ BookSession          — Capture: user_name, user_phone, user_email
✅ ChooseServices       — Single Choice (user_service): 5 options
✅ ServiceRambut        — Capture user_subservice → always → SubServiceExplanation
✅ ServKuku             — Capture user_subservice → always → SubServiceExplanation
✅ EyelashBrow          — Capture user_subservice → always → SubServiceExplanation
✅ FacialMuka           — Capture user_subservice → always → SubServiceExplanation
✅ Waxing               — Capture user_subservice → always → SubServiceExplanation
✅ SubServiceExplanation — AI card (KB) + @workflow.nextMessage + Single Choice
✅ BookServices         — Insert Record + confirmation text + Send Email ×2
✅ AnotherQuestion      — Single Choice: Yes → MenuChoice | No → End

CONFIGURATION
✅ SMTP configured      — Send Email cards in BookServices (owner + customer working)
✅ Knowledge Base       — Client FAQ + service list uploaded to AutonomousNode

NOTE: ❌ n8n NOT required for Basic — no webhooks, no Google Sheets, no Fonnte
```

## Deployment Checklist — Basic

```
□ Duplicate template bot in Botpress
□ Upload client FAQ + service list to Knowledge Base
□ Update Greeting text / business name variable
□ Update AutonomousNode instructions with client's business name & address
□ Add all sub-services to each Service node (ServiceRambut etc.)
□ Configure SMTP — Send Email cards in BookServices (owner + customer)
□ Customise webchat colors / logo to match client brand
□ Copy embed <script> tag → paste into client website
□ Test all 3 branches (FAQ / Hubungi Kami / Book flow)
□ Test full booking: pick service → subservice → confirm → check both emails arrive
□ Done ✅
```

> ⏱️ **Target time per client: 4–6 hours** (once you have a template bot to duplicate from)

---
---

# 📦 GROWTH PACKAGE

**RM1,000 setup + RM300/mo** | Tools: Botpress + n8n

## Features

Everything in Basic, plus:
- **Fully AI-translated flow** — all nodes use `greeting_translated` (BM, English, Mandarin auto-detected)
- **AI-generated dynamic menus** — service & subservice choices pulled from KB via AI Task + Execute Code (no hardcoded buttons)
- WhatsApp notification to owner on every booking via **Fonnte API** through n8n
- Lead data saved to Google Sheets automatically (appendOrUpdate)
- 24hr follow-up WhatsApp to customer if no action taken

---

## Conversation Flow

```
[Standard14] — DetectLanguage
  AI Task → workflow.user_language
↓
[Standard1] — Greeting
  AI Task → greeting_translated | Text: @workflow.greeting_translated
↓
[Standard2] — MenuChoice
  AI Task → menu_question | Text: @workflow.menu_question
  AI Task → menu_choices_raw | Execute Code (parse) | Single Choice (choice1/2/3)
↓
├── choice1 ──→ [Standard3] FAQ
│                 greeting_translated → Autonomous1
│                 Autonomous1: KB + "user wants to book" → Standard4
│
├── choice2 ──→ [Standard4] BookSession
│                 AI-prompted Capture: user_name, user_phone, user_email
│                 ↓
│             [Standard5] ChooseServices
│                 service_choices_raw → Execute Code → AI Task → Single Choice (service1/2)
│                 ↓
│             ┌── service1 → [Standard6] SubService Branch A
│             │               subservice_choices_raw → Execute Code → greeting_translated
│             │               Capture: user_subservice → always → Standard11
│             └── service2 → [Standard7] SubService Branch B
│                             subservice_choices_raw → Execute Code → greeting_translated
│                             Capture: user_subservice → always → Standard11
│                                       ↓
│                             [Standard11] SubServiceExplanation
│                               AI Task (KB) + @workflow.nextMessage + greeting_translated
│                               action_choices_raw → Execute Code → Single Choice (action1/2/3)
│                                       ↓
│                             [Standard12] BookServices
│                               Insert Record + greeting_translated + Send Email ×2
│                               Execute Code: "Send User Data to Webhook" → n8n
│                                       ↓
│                             [Standard13] AnotherQuestion
│                               greeting_translated + action_choices_raw + Execute Code
│                               Single Choice: Yes → Standard2 | No → End
│
└── choice3 ──→ [Hubungi Kami]
```

---

## Node Details

| Node | Role | Key Cards |
|---|---|---|
| **Standard14** | DetectLanguage | AI Task → `user_language` |
| **Standard1** | Greeting | AI Task `greeting_translated` + Text |
| **Standard2** | MenuChoice | `menu_question` + `menu_choices_raw` + Execute Code + Single Choice |
| **Standard3** | FAQ Branch | `greeting_translated` + routes to Autonomous1 |
| **Autonomous1** | FAQ AI | KB attached, "user wants to book" → Standard4 |
| **Standard4** | BookSession | AI-prompted captures: `user_name`, `user_phone`, `user_email` |
| **Standard5** | ChooseServices | `service_choices_raw` + Execute Code + AI Task + Single Choice |
| **Standard6** | SubService Branch A | `subservice_choices_raw` → Execute Code → `user_subservice` → always |
| **Standard7** | SubService Branch B | `subservice_choices_raw` → Execute Code → `user_subservice` → always |
| **Standard11** | SubServiceExplanation | AI Task (KB) + `nextMessage` + `action_choices_raw` + Execute Code + Single Choice |
| **Standard12** | BookServices | Insert Record + 2x Email + Execute Code webhook trigger |
| **Standard13** | AnotherQuestion | `action_choices_raw` + Execute Code + Single Choice (Yes → Standard2 \| No → End) |

## Variables Used

```
workflow.user_language
workflow.greeting_translated
workflow.menu_question / menu_choices_raw
workflow.user_choice1 / user_choice2 / user_choice3
workflow.user_name / user_phone / user_email
workflow.service_choices_raw
workflow.user_service / user_service1 / user_service2
workflow.subservice_choices_raw / user_subservice
workflow.nextMessage
workflow.action_choices_raw / action1 / action2 / action3
```

---

## n8n Workflows

### Workflow 1 — Instant WhatsApp + Google Sheets

```
Webhook (POST) ← triggered by Standard12
↓
Edit Fields (manual mapping)
↓ (parallel)
├── Wait2 → HTTP Request1 (WABlas POST → owner WhatsApp)
└── Append or update row in sheet (Google Sheets)
```

### Workflow 2 — 24hr Follow-up

```
Webhook1 (POST) ← triggered on booking
↓
Wait (24 hours)
↓
Get row(s) in sheet → filter by phone
↓
If (Status != Converted)
├── true  → Wait1 → HTTP Request3 (WABlas → customer) → Update row in sheet
└── false → No Operation
```

---

## Google Sheets — Growth Columns

| Col | Field | Default |
|---|---|---|
| A | Date & Time | — |
| B | Name | — |
| C | Phone | — |
| D | Email | — |
| E | Service | — |
| F | Subservice | — |
| G | Language | — |
| H | Source | — |
| I | Status | "New" |
| J | Notes | — |

## WABlas Setup

| Detail | Value |
|---|---|
| API endpoint | `https://deu.wablas.com/api/send-message` |
| Method | POST |
| Auth | Generic Credential Type → Header Auth |
| Header Name | Authorization |
| Header Value | TOKEN.SECRETKEY |

```json
{
  "phone": "{{ phone_number }}",
  "message": "your message here"
}
```

---

## ✅ Build Checklist — Growth

```
BOTPRESS — CONVERSATION NODES
✅ Standard14   — DetectLanguage: AI Task → user_language
✅ Standard1    — Greeting: AI Task greeting_translated + Text @workflow.greeting_translated
✅ Standard2    — MenuChoice: menu_question + menu_choices_raw + Execute Code + Single Choice
✅ Standard3    — FAQ branch: greeting_translated + routes to Autonomous1
✅ Autonomous1  — KB attached (1x), "user wants to book" → Standard4
✅ Standard4    — BookSession: greeting_translated prompts + Capture user_name, user_phone, user_email
✅ Standard5    — ChooseServices: service_choices_raw + Execute Code + AI Task + Single Choice
✅ Standard6    — SubService Branch A: subservice_choices_raw + Execute Code + user_subservice → always
✅ Standard7    — SubService Branch B: subservice_choices_raw + Execute Code + user_subservice → always
✅ Standard11   — SubServiceExplanation: AI Task (KB) + nextMessage + action_choices_raw + Execute Code + Single Choice
✅ Standard12   — BookServices: Insert Record + greeting_translated + 2x Send Email + Webhook Execute Code
✅ Standard13   — AnotherQuestion: action_choices_raw + Execute Code + Single Choice

N8N — WORKFLOWS
✅ Workflow 1   — Webhook → Edit Fields → [Wait2 → WABlas (owner WA)] + [Google Sheets append]
✅ Workflow 2   — Webhook1 → Wait → Get Sheets → If → [WABlas (customer WA) → Update sheet] | No Operation

GOOGLE SHEETS
✅ Sheet "Sofea Leads" created — columns A–J confirmed
✅ Connected to Workflow 1 (append) and Workflow 2 (read + update)

WABLAS SETUP
□ API token configured in HTTP Request1 (Workflow 1 — owner notification) — WABlas
□ API token configured in HTTP Request3 (Workflow 2 — customer follow-up) — WABlas
□ Target = owner phone in Workflow 1
□ Target = customer phone variable in Workflow 2
```

---
---

# 📦 PRO PACKAGE

**RM2,000 setup + RM500/mo** | Tools: Botpress + n8n (full)

## Features

Everything in Growth, plus:
- **Lead qualification** — first-time vs returning, routes differently
- **Lead scoring** — hot/warm/cold classification (ReturningCheck + BundleSummary)
- **Goal-based AI recommendation** — GoalSelection → SmartRecommend → chosen_service
- **Upsell/bundle flow** — UpsellNode suggests add-ons, BundleSummary calculates final score
- **Returning customer shortcut** — skips GoalSelection, goes straight to booking
- **Smart service pre-fill** — Standard16 sets `user_service` for returning customers
- **Hot lead WhatsApp alert** — fired immediately on booking (n8n If1)
- **Warm lead notification** — separate WABlas message (n8n If2)
- **Multi-step follow-up** — Day 1 / 3 / 7 WABlas messages
- **Weekly performance dashboard** — Schedule Trigger → Sheets → JS → Gmail
- **Conversion tracking** — Webhook5 → Update sheet + WABlas to owner
- Priority support

---

## Conversation Flow

```
[Standard8] — DetectLanguage → workflow.user_language
↓
[Standard10] — Greeting → greeting_translated
↓
[Standard9] — MenuChoice → menu_question + menu_choices_raw + Execute Code + Single Choice
↓
├── choice1 ──→ [Standard15] FAQ → Autonomous2 (KB, "book" → Standard16)
│
├── choice2 ──→ [QualifyNode] Capture customer_type (first-time / returning)
│                 ↓
│             [ReturningCheck] Execute Code: assign lead_score + is_returning
│                 ├── is returning ──→ [Standard16] (skip funnel)
│                 └── always      ──→ [GoalSelection] Capture customer_goal
│                                           ↓
│                                     [SmartRecommend] AI rec → chosen_service
│                                           ↓
│                                     [UpsellNode] AI upsell → upsell_choice
│                                           ↓
│                                     [BundleSummary] Lead score → lead_temp
│                                           ↓ (merges with returning path)
│                                     [Standard16] BookSession
│                                       AI-prompted: user_name, user_phone, user_email
│                                       Execute Code: "Set User Service" (returning pre-fill)
│                                           ↓
│                                     [Standard17] ChooseServices
│                                       service_choices_raw → Execute Code → Single Choice
│                                           ↓
│                                     ┌── service1 → [Standard18] SubService Branch A
│                                     │               subservice_choices_raw → Capture → always
│                                     └── service2 → [Standard19] SubService Branch B
│                                                     subservice_choices_raw → Capture → always
│                                                               ↓
│                                                     [Standard20] SubServiceExplanation
│                                                       Execute Code (KB) + nextMessage
│                                                       action_choices_raw → Single Choice
│                                                               ↓
│                                                     [Standard21] BookServices
│                                                       Insert Record + 2x Email
│                                                       Execute Code → fires Webhook3 + Webhook4
│                                                               ↓
│                                                     [Standard22] AnotherQuestion
│                                                       Yes → Standard9 | No → End
│
└── choice3 ──→ [Hubungi Kami]
```

---

## Node Details

| Node | Role | Key Cards |
|---|---|---|
| **Standard8** | DetectLanguage | AI Task → `user_language` |
| **Standard10** | Greeting | AI Task `greeting_translated` + Text |
| **Standard9** | MenuChoice | `menu_question` + `menu_choices_raw` + Execute Code + Single Choice |
| **Standard15** | FAQ Branch | `greeting_translated` → Autonomous2 |
| **Autonomous2** | FAQ AI | KB attached, "user wants to book" → Standard16 |
| **QualifyNode** | Lead Qualify | Capture: `customer_type` |
| **ReturningCheck** | Lead Score | Execute Code: assign `lead_score`, `is_returning` → routes |
| **GoalSelection** | Goal | Capture: `customer_goal` |
| **SmartRecommend** | AI Rec | AI Task `recommendation_raw` → Execute Code → Capture `chosen_service` |
| **UpsellNode** | Upsell | AI Task `upsell_raw` → Execute Code → Single Choice `upsell_choice` |
| **BundleSummary** | Score Final | Execute Code: final `lead_score` + `lead_temp` → Text summary |
| **Standard16** | BookSession | AI-prompted captures + Execute Code pre-fill for returning |
| **Standard17** | ChooseServices | `service_choices_raw` → Execute Code → Single Choice |
| **Standard18/19** | SubService A/B | `subservice_choices_raw` → Execute Code ×2 → Capture → always |
| **Standard20** | SubServiceExplanation | Execute Code (KB) + `nextMessage` + `action_choices_raw` + Single Choice |
| **Standard21** | BookServices | Insert Record + 2x Email + Execute Code (fires Webhook3 + Webhook4) |
| **Standard22** | AnotherQuestion | `action_choices_raw` + Execute Code + Single Choice |

## Variables Used

```
workflow.user_language
workflow.greeting_translated
workflow.menu_question / menu_choices_raw
workflow.user_choice1 / user_choice2 / user_choice3
workflow.customer_type / is_returning
workflow.lead_score / lead_temp
workflow.customer_goal
workflow.recommendation_raw / chosen_service
workflow.upsell_raw / upsell_choice / bundle_type
workflow.user_name / user_phone / user_email
workflow.user_service / user_service1 / user_service2
workflow.subservice_choices_raw / user_subservice
workflow.skip_service_selection
workflow.nextMessage
workflow.action_choices_raw / action1 / action2 / action3
```

---

## Lead Scoring System

| Trigger | Points |
|---|---|
| First-time visitor | +10 |
| Returning customer | +5 |
| Chose both add-ons (upsell) | +20 |
| Chose partial upsell | +10 |
| Responded in < 5 minutes | +15 |
| Mandarin language | +10 |
| **Hot threshold** | **≥ 40** |
| **Warm threshold** | **≥ 20** |
| **Cold** | **< 20** |

---

## n8n Workflows

### Workflow 1 — Lead Scoring & Hot/Warm Alert

```
Webhook3 (POST) ← Standard21 fires this
↓
Edit Fields1 (map payload fields)
↓
Append or update row in sheet1 (Google Sheets — Status = lead_temp)
↓
If1: Lead Temperature == "hot"?
├── true  → HTTP Request10 (WABlas → owner, HOT alert)
└── false → If2: Lead Temperature == "warm"?
               ├── true  → HTTP Request11 (WABlas → owner, warm notify)
               └── false → No Operation (cold leads, no WA sent)
```

**Webhook3 URL:** `https://cipud.app.n8n.cloud/webhook/4975c2d4-f0c0-4045-8510-be4fb427e411`

**WABlas setup for Workflow 1:**
```
HTTP Request10 + HTTP Request11:
  URL:    https://deu.wablas.com/api/send-message
  Method: POST
  Auth:   Generic Credential Type → Header Auth
  Header Name:  Authorization
  Header Value: TOKEN.SECRETKEY

HTTP Request10 JSON (HOT alert → owner):
{
  "phone": "60173103966",
  "message": "🔴 HOT LEAD ALERT - Sofea Beauty Salon!\n\n👤 Name: {{ $json['Name'] }}\n📞 Phone: {{ $json['Phone'] }}\n📧 Email: {{ $json['Email'] }}\n💆 Service: {{ $json['Service'] }}\n✨ Subservice: {{ $json['Subservice'] }}\n🛍 Add-on: {{ $json['Upsell Choice'] }}\n⭐ Score: {{ $json['Lead Score'] }}\n👥 Type: {{ $json['Customer Type'] }}\n\n⚡ Call within 15 minutes!"
}

HTTP Request11 JSON (WARM notify → owner):
{
  "phone": "60173103966",
  "message": "🔔 Warm Lead - Sofea Beauty Salon!\n\n👤 Name: {{ $json['Name'] }}\n📞 Phone: {{ $json['Phone'] }}\n📧 Email: {{ $json['Email'] }}\n💆 Service: {{ $json['Service'] }}\n✨ Subservice: {{ $json['Subservice'] }}\n🛍 Add-on: {{ $json['Upsell Choice'] }}\n⭐ Score: {{ $json['Lead Score'] }}\n👥 Type: {{ $json['Customer Type'] }}"
}
```

### Workflow 2 — Multi-Step Follow-up Day 1 / 3 / 7

```
Webhook4 (POST) ← Standard21 fires this (5s after Webhook3)
↓
Wait3 (1 day production / 1 min testing)
↓
Get row(s) in sheet2 — filter: Phone = webhook payload phone
↓
If3: Status != "Converted"
├── true  → HTTP Request6 (WABlas Day 1 WA → customer)
│            Update sheet: Status = "Day1Sent"
│            Wait4 (2 days / 2 mins)
│            Get row(s) in sheet3
│            If4: Status == "Day1Sent"
│            ├── true  → HTTP Request7 (WABlas Day 3 WA) → Update: "Day3Sent"
│            │            Wait5 (4 days / 4 mins)
│            │            HTTP Request8 (WABlas Day 7 WA) → Update: "FinalSent"
│            └── false → No Operation
└── false → No Operation (already converted)
```

**Webhook4 URL:** `https://cipud.app.n8n.cloud/webhook/55c03916-a079-4c31-8af2-17109427ebbf`

**WABlas setup for Workflow 2 (HTTP Request6, 7, 8):**
```
URL:    https://deu.wablas.com/api/send-message
Method: POST
Auth:   Generic Credential Type → Header Auth
Header Name:  Authorization
Header Value: TOKEN.SECRETKEY

HTTP Request6 JSON (Day 1 → customer):
{
  "phone": "{{ $json['Phone'] }}",
  "message": "Hi {{ $json['Name'] }}! 😊\n\nKami dari Sofea Beauty Salon.\nAnda berminat dengan {{ $json['Subservice'] }}.\n\nKami ada slot available this week!\nNak confirm appointment? 🗓\n\nReply YES untuk proceed 😊"
}

HTTP Request7 JSON (Day 3 → customer):
{
  "phone": "{{ $json['Phone'] }}",
  "message": "Hey {{ $json['Name'] }}! 🌸\n\nSlot untuk {{ $json['Subservice'] }} masih ada.\nJangan lepaskan peluang ini! ⏰\n\nReply YES untuk confirm 😊"
}

HTTP Request8 JSON (Day 7 → customer):
{
  "phone": "{{ $json['Phone'] }}",
  "message": "Hi {{ $json['Name'] }}, peringatan terakhir! 🙏\n\nSlot {{ $json['Subservice'] }} masih available.\nReply YES untuk confirm atau NO untuk cancel.\nSelepas hari ini slot akan dilepaskan 🙏"
}
```

> ⚠️ If3 uses "is NOT equal to Converted" — Pro Status starts as hot/warm/cold, not "New"
> ⚠️ Update row Phone match uses `$('Get row(s) in sheet2').item.json['Phone']` — NOT the webhook reference (fails after Wait node)
> ⚠️ No Filter 2 in Get row(s) nodes — let If nodes handle all conditional logic

### Workflow 3 — Weekly Performance Dashboard

```
Schedule Trigger1 (every Monday 9am)
↓
Get row(s) in sheet4 (ALL rows — no filter, JS filters internally)
↓
Code in JavaScript1 (filters this week, calculates all metrics)
↓
Send a message1 (Gmail → owner)
```

### Workflow 4 — Conversion Tracking

```
Webhook5 (POST) ← owner triggers manually when lead converts
↓
Update row in sheet4 — match Phone, set Status = "Converted", Revenue = amount
↓
HTTP Request9 (WABlas → owner, conversion confirmation)
```

**Webhook5 URL:** `https://cipud.app.n8n.cloud/webhook/6fee288f-964e-4b72-ac3b-35a1accf37c6`

**WABlas setup for Workflow 4 (HTTP Request9):**
```
URL:    https://deu.wablas.com/api/send-message
Method: POST
Auth:   Generic Credential Type → Header Auth
Header Name:  Authorization
Header Value: TOKEN.SECRETKEY

JSON:
{
  "phone": "60173103966",
  "message": "🎉 Conversion recorded!\n\n👤 {{ $('Webhook5').item.json.body.name }}\n📞 {{ $('Webhook5').item.json.body.phone }}\n💆 {{ $('Webhook5').item.json.body.service }}\n💰 Revenue: RM{{ $('Webhook5').item.json.body.revenue }}"
}
```

---

## Standard21 — Webhook Execute Code

```javascript
const webhookUrl1 = 'https://cipud.app.n8n.cloud/webhook/4975c2d4-f0c0-4045-8510-be4fb427e411'
const followupUrl1 = 'https://cipud.app.n8n.cloud/webhook/55c03916-a079-4c31-8af2-17109427ebbf'

const payload = {
  name: workflow.user_name || '',
  phone: workflow.user_phone || '',
  email: workflow.user_email || '',
  service: workflow.user_service || '',
  subservice: workflow.user_subservice || workflow.chosen_service || '',
  upsell: workflow.upsell_choice || 'none',
  bundle_type: workflow.bundle_type || 'none',
  lead_score: workflow.lead_score || 0,
  lead_temp: workflow.lead_temp || 'cold',
  language: workflow.user_language || 'english',
  customer_type: workflow.customer_type || '',
  timestamp: new Date().toISOString(),
  source: 'Website Chatbot',
  business: 'Sofea Beauty Salon'
}

try { await axios.post(webhookUrl1, payload) } catch (e) {}
await new Promise((resolve) => setTimeout(resolve, 5000))
try { await axios.post(followupUrl1, payload) } catch (e) {}
```

---

## Google Sheets — Pro Columns

| Col | Field | Notes |
|---|---|---|
| A | Date & Time | — |
| B | Name | — |
| C | Phone | — |
| D | Email | — |
| E | Service | — |
| F | Subservice | — |
| G | Language | — |
| H | Source | — |
| I | Status | hot/warm/cold → Day1Sent → Day3Sent → FinalSent → Converted |
| J | Lead Score | Number |
| K | Lead Temperature | hot / warm / cold |
| L | Bundle Type | full / partial / none |
| M | Upsell Choice | From workflow |
| N | Customer Type | First-time / Returning |
| O | Contacted | Yes / No (filled manually by owner) |
| P | Converted | Yes / No (filled by Workflow 4) |
| Q | Revenue | RM amount (filled by Workflow 4) |

> Growth uses columns A–J on the same sheet. Pro extends to column Q.

---

## ✅ Build Checklist — Pro

```
BOTPRESS — CONVERSATION NODES
✅ Standard8      — DetectLanguage: AI Task → user_language
✅ Standard10     — Greeting: AI Task greeting_translated + Text
✅ Standard9      — MenuChoice: menu_question + menu_choices_raw + Execute Code + Single Choice
✅ Standard15     — FAQ branch → Autonomous2
✅ Autonomous2    — KB attached, "book" transition → Standard16
✅ QualifyNode    — Capture customer_type
✅ ReturningCheck — Execute Code: lead_score + is_returning → routes
✅ GoalSelection  — Capture customer_goal
✅ SmartRecommend — AI Task recommendation_raw + Execute Code + Capture chosen_service
✅ UpsellNode     — AI Task upsell_raw + Execute Code + Single Choice upsell_choice
✅ BundleSummary  — Execute Code: final lead_score + lead_temp + summary text
✅ Standard16     — BookSession: AI-prompted name/phone/email + Execute Code pre-fill
✅ PickService    — service_choices_raw + Execute Code + greeting_translated + Single Choice (user_service)
✅ Standard20     — SubServiceExplanation: Dynamic Subservice Selection + Execute Code + nextMessage + action_choices_raw + Single Choice
✅ Standard21     — BookServices: Insert Record + greeting_translated + Generate Appointment Summary + 2x Send Email + Execute Code (Webhook3 + Webhook4)
✅ Standard22     — AnotherQuestion: action_choices_raw + Execute Code + Single Choice

N8N — WORKFLOWS
✅ Workflow 1 — Webhook3 → Edit Fields1 → Sheets append → If1 (hot) → HTTP Request10 (WABlas HOT alert to owner)
               If2 (warm) → HTTP Request11 (WABlas WARM notify to owner) | No Operation
✅ Workflow 2 — Webhook4 → Wait3 → Get row(s) sheet2 → If3 (!=Converted) → HTTP Request6 (Day 1 WABlas)
               → Update sheet1 → Wait4 → Get row(s) sheet3 → If4 (==Day1Sent) → HTTP Request7 (Day 3)
               → Update sheet2 → Wait5 → HTTP Request8 (Day 7) → Update sheet3 | No Operation
✅ Workflow 3 — Schedule Trigger1 → Get row(s) sheet4 → Code in JavaScript1 → Send a message1 (Gmail)
✅ Workflow 4 — Webhook5 → Update row sheet4 (Converted) → HTTP Request9 (WABlas conversion confirm to owner)

GOOGLE SHEETS (columns A–Q)
✅ A–I: base columns (same as Growth)
✅ J: Lead Score | K: Lead Temperature | L: Bundle Type
✅ M: Upsell Choice | N: Customer Type
✅ O: Contacted | P: Converted | Q: Revenue

WABLAS SETUP
✅ Account registered at deu.wablas.com
✅ Device Samsung #KU69UV — Connected (62173103966)
✅ Token + Secret Key configured in n8n Header Auth account 3
   Format: TOKEN.SECRETKEY
✅ API URL confirmed: https://deu.wablas.com/api/send-message
✅ HTTP Request10 (hot alert) — WABlas format, working
✅ HTTP Request11 (warm notify) — WABlas format, working
✅ HTTP Request6 (Day 1 follow-up) — WABlas format, confirmed
✅ HTTP Request7 (Day 3 follow-up) — WABlas format, confirmed
✅ HTTP Request8 (Day 7 follow-up) — WABlas format, confirmed
✅ HTTP Request9 (conversion confirm) — WABlas format, confirmed
```

> 💡 **Build order:** QualifyNode → ReturningCheck → GoalSelection → SmartRecommend → UpsellNode → BundleSummary → wire into Standard16 → then n8n webhooks
