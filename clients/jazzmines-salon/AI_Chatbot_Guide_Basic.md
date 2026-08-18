# Jazzmine's Salon — AI Chatbot Build Guide (BASIC Package)

> **Package:** Basic — RM500 setup + RM150/mo · Botpress only, no n8n
> **Target build time:** 4–6 hours from the template bot
> **Prepared:** 2026-08-02 by IGEN VERITAS
> ⚠️ All salon service prices in this guide are **estimates** — confirm with the owner before the KB goes live.

---

## 1. Client Snapshot

| | |
|---|---|
| **Salon** | Jazzmine's Salon |
| **Specialty** | Curly hair · Hair coloring · Scalp issues · Hair strengthening |
| **Taglines** | "The Eye Is Sharper Than The Scissors" · "Beauty Through Science" |
| **Location** | Shop H @ PJ Sport Centre 1, Lorong Sultan, 46200 Petaling Jaya |
| **Phone** | +6012 2209 601 (WhatsApp) · +603 7955 4668 (shop) |
| **Socials** | FB: JAZZMINE'S SALON · IG: @jazzminessalonpj |
| **Extra** | GHD Approved Stockist |

**Why the bot fits them:** a colour/curly specialist gets long, question-heavy enquiries ("can you fix my brassy balayage", "is keratin safe on curly hair", "how much for highlights on long hair"). Those DMs arrive after hours and go cold. The bot answers from the KB 24/7 and converts the visitor into a booking enquiry with name + phone + email before they leave.

---

## 2. Package Scope — What They Get

| Included in Basic | |
|---|:---:|
| Web widget chatbot on the salon website | ✅ |
| FAQ answers from a knowledge base (AI) | ✅ |
| Full booking flow with service → sub-service selection | ✅ |
| Lead capture: name, phone, email | ✅ |
| 2× email on every booking (owner + customer) | ✅ |
| "Hubungi Kami" contact branch | ✅ |
| BM + English | ✅ |
| Brand-matched widget colours + logo | ✅ |
| Mandarin, WhatsApp alerts, Google Sheets, follow-ups | ❌ (Growth) |

**Not included — flag it in the sales call:** the Basic bot does **not** send WhatsApp to the owner and does **not** log to Google Sheets. The owner gets an email per booking. If they want WhatsApp + a lead sheet + auto follow-up, that's the **Growth** upgrade (RM1,000 setup + RM300/mo).

---

## 3. Pricing

### 3.1 What we charge Jazzmine's

| Item | Amount |
|---|---|
| Setup fee (one-off) | **RM500** |
| Monthly maintenance | **RM150/mo** |
| **First payment** | **RM650** |
| Ongoing from month 2 | RM150/mo |

**Terms to quote:** RM500 setup payable before build starts, RM150/mo billed monthly from go-live. Monthly covers hosting of the bot, KB updates (service/price changes), and minor flow tweaks.

### 3.2 Our cost & margin

| Item | Cost |
|---|---|
| Botpress free plan (500 conv/mo) | RM0 |
| Botpress AI spend at salon volume | ~RM0–30/mo |
| SMTP (client's own Gmail) | RM0 |
| n8n / WABlas | RM0 — not used in Basic |
| **Net profit** | **~RM120–150/mo + RM500 upfront** |

> If the salon ever exceeds 500 conversations/month, that's the trigger to move them to Growth (and onto your Botpress Team plan).

### 3.3 Estimated salon service prices — ⚠️ FOR THE KB, CONFIRM BEFORE LIVE

The flyer carries no prices. These are typical PJ specialist-salon bands, used as **placeholders** so the KB can be drafted now. **Replace every figure with the owner's real price list before go-live.**

| Service | Estimate (RM) |
|---|---|
| Haircut & restyle | 60 – 120 |
| Curly / wavy / frizzy cut (dry cut) | 90 – 180 |
| Volume cut | 80 – 150 |
| Wash & blow / styling | 40 – 80 |
| Root touch-up colour | 120 – 220 |
| Full colour | 180 – 400 |
| Highlights | 250 – 600 |
| Balayage | 350 – 800 |
| Foilyage | 400 – 850 |
| Keratin treatment | 350 – 900 |
| Relaxer / rebonding | 300 – 700 |
| Perm (incl. curly perm) | 250 – 600 |
| Hair strengthening treatment | 150 – 400 |
| Scalp treatment (scalp issues) | 120 – 350 |
| Waxing (per area) | 30 – 150 |
| Makeup for events | 150 – 450 |
| GHD tools (retail) | at GHD RRP |

> Price bands vary with hair length and thickness. In the KB, always phrase as **"from RM X"** and end with *"exact quote confirmed at consultation."* Never let the bot commit to a fixed price.

---

## 4. Service Tree (5 branches)

Mapped directly from the flyer's service list.

| Branch | `user_service` | Sub-services (`user_subservice`) |
|---|---|---|
| 1 | **Hair Coloring** | Highlights · Balayage · Foilyage · Full Colour · Root Touch-Up · Colour Correction |
| 2 | **Cuts & Styling** | Haircut & Restyle · Volume Cut · Curly / Wavy / Frizzy Cut · Wash & Blow |
| 3 | **Hair Treatments** | Keratin Treatment · Relaxer · Perm · Hair Strengthening Treatment |
| 4 | **Scalp Care** | Scalp Analysis · Treatment for Scalp Issues · Anti-Hair-Fall / Dandruff |
| 5 | **Beauty & Extras** | Waxing · Makeup for Events · GHD Products |

> Curly hair is their differentiator — keep "Curly / Wavy / Frizzy Cut" visible in Cuts & Styling and mention curly expertise in the Greeting and AutonomousNode instructions.

---

## 5. Conversation Flow

```
[Greeting]
"Hai! 👋 Selamat datang ke Jazzmine's Salon PJ —
 pakar curly hair, coloring & scalp care. Macam mana boleh kami bantu?"
↓
[MenuChoice] — Single Choice
├── Tanya Soalan / FAQ    ──→ [AutonomousNode]
│                                (KB + transition "user wants to book" → BookSession)
├── Hubungi Kami          ──→ [ContactInfo] → AnotherQuestion
└── Tempah / Book Appointment ──→ [BookSession]
                                    ├── Capture: user_name
                                    ├── Capture: user_phone
                                    ├── Capture: user_email
                                    ↓
                               [ChooseServices] — Single Choice (user_service)
                                    ├── Hair Coloring    → [ServColoring]   (user_subservice → always)
                                    ├── Cuts & Styling   → [ServCuts]       (user_subservice → always)
                                    ├── Hair Treatments  → [ServTreatments] (user_subservice → always)
                                    ├── Scalp Care       → [ServScalp]      (user_subservice → always)
                                    └── Beauty & Extras  → [ServBeauty]     (user_subservice → always)
                                            ↓ (all merge)
                               [SubServiceExplanation]
                                    ├── AI card: KB lookup (what it is, duration, from-RM)
                                    ├── Text: @workflow.nextMessage
                                    └── Single Choice:
                                        ├── Ya, book sekarang!  ──→ [BookServices]
                                        ├── Pilih servis lain   ──→ [ChooseServices]
                                        └── Tanya soalan lain   ──→ [AutonomousNode]
                                                 ↓
                                          [BookServices]
                                            ├── Insert Record
                                            ├── Confirmation text
                                            ├── Send Email (owner)
                                            └── Send Email (customer)
                                                 ↓
                                          [AnotherQuestion]
                                            ├── Ya, ada soalan lain ──→ [MenuChoice]
                                            └── Tak, terima kasih   ──→ [End]
```

---

## 6. Node-by-Node Build

| Node | Cards / Config |
|---|---|
| **Greeting** | Text: `Hai! 👋 Selamat datang ke @workflow.greeting_translated` — set business name to `Jazzmine's Salon` |
| **MenuChoice** | Single Choice: `Tanya Soalan / FAQ` \| `Hubungi Kami` \| `Tempah / Book Appointment` |
| **AutonomousNode** | Instructions (below) · KB: 1 attached · Transition: `"user wants to book"` → BookSession |
| **ContactInfo** | Text card with phone, address, hours, IG/FB → `always` → AnotherQuestion |
| **BookSession** | Capture: `user_name` → `user_phone` → `user_email` (in that order) |
| **ChooseServices** | Single Choice → `user_service`, 5 options (§4) |
| **ServColoring** | Capture `user_subservice` (6 options) → `always` → SubServiceExplanation |
| **ServCuts** | Capture `user_subservice` (4 options) → `always` → SubServiceExplanation |
| **ServTreatments** | Capture `user_subservice` (4 options) → `always` → SubServiceExplanation |
| **ServScalp** | Capture `user_subservice` (3 options) → `always` → SubServiceExplanation |
| **ServBeauty** | Capture `user_subservice` (3 options) → `always` → SubServiceExplanation |
| **SubServiceExplanation** | AI card (KB lookup on `@workflow.user_subservice`) + Text `@workflow.nextMessage` + Single Choice (book / pilih lain / tanya lain) |
| **BookServices** | Insert Record + confirmation text + Send Email ×2 (owner + customer) |
| **AnotherQuestion** | Single Choice: Ya → MenuChoice \| Tak → End |

### Variables

```
workflow.greeting_translated
workflow.user_name
workflow.user_phone
workflow.user_email
workflow.user_service
workflow.user_subservice
workflow.nextMessage
```

### AutonomousNode — instructions to paste

```
You are the assistant for Jazzmine's Salon, a specialist hair salon at
Shop H @ PJ Sport Centre 1, Lorong Sultan, 46200 Petaling Jaya.

Specialties: curly hair, hair coloring (highlights, balayage, foilyage),
scalp issue treatment, and hair strengthening. The salon's philosophy is
"Beauty Through Science" — cuts and colour are prescribed to the client's
hair type, not one-size-fits-all. Jazzmine's is a GHD Approved Stockist.

Rules:
- Reply in the same language the customer uses — Bahasa Malaysia or English.
- Warm, professional, salon-consultant tone. Short answers, 2–4 sentences.
- Answer only from the knowledge base. If the answer is not there, say you
  will have the team confirm and offer to take their details.
- NEVER quote a fixed price. Always say "from RM X" and add that the exact
  price is confirmed at consultation because it depends on hair length,
  thickness and current colour.
- If the customer shows any intent to book, ask for an appointment and let
  the booking flow take over.
- Do not give medical advice for scalp conditions — recommend an in-salon
  scalp analysis instead.
```

### SubServiceExplanation — AI card prompt

```
Using the knowledge base, explain "@workflow.user_subservice" at Jazzmine's Salon
in 2–3 sentences: what it is, roughly how long it takes, and the starting price
as "from RM X". Note that the final price is confirmed at consultation.
Reply in the customer's language. End by asking if they'd like to book it.
```

---

## 7. Knowledge Base — What to Upload

Build one document, upload to the AutonomousNode KB.

1. **About** — name, taglines, specialties, address, "Beauty Through Science" philosophy, GHD stockist
2. **Full service list with "from RM" prices** — §4 tree + §3.3 figures, **replaced with the owner's real prices**
3. **Opening hours + rest day** ⚠️ to collect
4. **How to find us** — Shop H @ PJ Sport Centre 1, Lorong Sultan; parking notes ⚠️ to collect
5. **Contact** — 012-2209 601 (WhatsApp), 03-7955 4668, IG @jazzminessalonpj, FB JAZZMINE'S SALON
6. **Booking policy** — deposit required?, cancellation window, walk-ins accepted? ⚠️ to collect
7. **FAQ — draft 15 Q&A, e.g.:**
   - Do you do dry cuts for curly hair?
   - I have frizzy/wavy hair — which service suits me?
   - Can you fix a colour done elsewhere? (colour correction)
   - Is keratin treatment safe for curly hair? Will it straighten my curls?
   - How long does balayage take?
   - What's the difference between highlights, balayage and foilyage?
   - Do you treat dandruff / itchy scalp / hair fall?
   - How long does a keratin treatment last?
   - Do you sell GHD tools? Warranty?
   - Do you do bridal / event makeup?
   - What waxing services do you offer?
   - Do I need an appointment or can I walk in?
   - Do you have parking?
   - How much does highlights cost for long hair?
   - Which stylist specialises in curly hair?

---

## 8. Emails on Booking

**To owner** — subject: `🔔 New Booking Enquiry — Jazzmine's Salon`

```
New enquiry from the website chatbot.

Name:        @workflow.user_name
Phone:       @workflow.user_phone
Email:       @workflow.user_email
Service:     @workflow.user_service
Sub-service: @workflow.user_subservice

Call them back to confirm the slot.
```

**To customer** — subject: `Terima kasih! Tempahan anda di Jazzmine's Salon`

```
Hi @workflow.user_name,

Terima kasih kerana menghubungi Jazzmine's Salon! 💇‍♀️

Servis diminta: @workflow.user_service — @workflow.user_subservice

Team kami akan hubungi anda tidak lama lagi untuk confirm slot dan
harga sebenar (bergantung pada panjang & jenis rambut).

📍 Shop H @ PJ Sport Centre 1, Lorong Sultan, 46200 Petaling Jaya
📞 012-2209 601  |  03-7955 4668
📷 @jazzminessalonpj

— Jazzmine's Salon | "Beauty Through Science"
```

---

## 9. Widget Styling

| Setting | Value |
|---|---|
| Primary colour | `#FF2D4E` (flyer red/pink) |
| Accent colour | `#FF7A1A` (orange) |
| Bot avatar | Jazzmine's logo (request a PNG from the owner) |
| Widget title | `Jazzmine's Salon` |
| Subtitle | `Curly hair · Colour · Scalp care` |
| Position | Bottom-right |
| Welcome bubble | `Nak tanya pasal curly cut atau balayage? Tanya kami 👋` |

---

## 10. Build Checklist

```
BOTPRESS — CONVERSATION NODES
□ Greeting              — business name = Jazzmine's Salon
□ MenuChoice            — 3 options (FAQ | Hubungi Kami | Tempah)
□ AutonomousNode        — KB attached, instructions pasted, "user wants to book" → BookSession
□ ContactInfo           — phone / address / hours / socials
□ BookSession           — Capture user_name, user_phone, user_email
□ ChooseServices        — Single Choice (user_service), 5 options
□ ServColoring          — Capture user_subservice (6) → always → SubServiceExplanation
□ ServCuts              — Capture user_subservice (4) → always → SubServiceExplanation
□ ServTreatments        — Capture user_subservice (4) → always → SubServiceExplanation
□ ServScalp             — Capture user_subservice (3) → always → SubServiceExplanation
□ ServBeauty            — Capture user_subservice (3) → always → SubServiceExplanation
□ SubServiceExplanation — AI card (KB) + @workflow.nextMessage + Single Choice
□ BookServices          — Insert Record + confirmation + Send Email ×2
□ AnotherQuestion       — Ya → MenuChoice | Tak → End

CONFIGURATION
□ SMTP configured with the salon's Gmail
□ Knowledge Base uploaded (§7) with REAL prices confirmed by owner
□ Widget colours + logo applied (§9)
□ Embed <script> tag pasted into the salon website

TESTING
□ FAQ branch — ask a curly-hair question, confirm KB answer
□ FAQ → booking transition ("I want to book") jumps to BookSession
□ Hubungi Kami branch shows correct phone + address
□ Full booking: Hair Coloring → Balayage → confirm → both emails arrive
□ Repeat for one more branch (e.g. Scalp Care)
□ Test in BM and in English
□ Test on mobile

NOT IN BASIC: ❌ n8n  ❌ Google Sheets  ❌ WhatsApp alerts  ❌ Mandarin
```

---

## 11. Deployment

```
□ Duplicate the salon template bot in Botpress
□ Rename → "Jazzmine's Salon — Basic"
□ Upload KB, update Greeting + AutonomousNode with salon details
□ Load all 5 service nodes with their sub-services
□ Configure SMTP (owner + customer emails)
□ Style the webchat (§9)
□ Send the <script> tag to whoever manages the salon website
□ End-to-end test on the live site
□ Walkthrough call with the owner — show where booking emails land
□ Client sign-off → start the RM150/mo billing cycle
```

---

## 12. Before You Build — Collect From the Owner

1. ✅ **Website URL** — the widget needs a site to sit on. *(If they have no website, that's a Landing Page project: RM700–1,500 — see the Web Development tier.)*
2. ✅ **Gmail address** for SMTP + booking notifications
3. ✅ **Real service price list** — replaces every estimate in §3.3
4. ✅ **Opening hours + rest day**
5. ✅ **Booking policy** — deposit, cancellation, walk-ins
6. ✅ **Logo PNG** (transparent background) for the widget
7. ✅ **Who updates the website** — owner, or a web person we send the script tag to
8. ✅ **Stylist names** if they want the bot to mention the curly-hair specialist

---

## 13. Upsell Path

| Trigger | Offer |
|---|---|
| Owner says "I keep missing the emails" | **Growth** — WhatsApp alert on every booking |
| Owner wants to see all leads in one place | **Growth** — Google Sheets lead log |
| Leads enquire but never show up | **Growth** — 24hr auto follow-up |
| Chinese-speaking walk-ins in PJ | **Growth** — Mandarin support |
| No website at all | **Landing Page** — RM700–1,500 |
| Wants full funnel + lead scoring + Day 1/3/7 follow-up | **Pro** — RM2,000 + RM500/mo |

---

*© 2026 IGEN VERITAS. Prepared for Jazzmine's Salon.*
