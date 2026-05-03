# Build Checklist — [CLIENT NAME] | [PACKAGE]

> Target completion: 4–6 hours (Basic) / 8–12 hours (Growth) / 16–24 hours (Pro)

---

## BASIC CHECKLIST

### Botpress — Conversation Nodes
- [ ] Greeting — Text: "Hai! 👋 Selamat datang ke @workflow.greeting_translated"
- [ ] MenuChoice — Single Choice: Tanya Soalan / FAQ | Hubungi Kami | Tinggalkan Maklumat
- [ ] AutonomousNode — KB attached, transition: "user wants to book" → BookSession
- [ ] BookSession — Capture: user_name, user_phone, user_email
- [ ] ChooseServices — Single Choice (user_service)
- [ ] Service Nodes (×n) — Capture user_subservice → always → SubServiceExplanation
- [ ] SubServiceExplanation — AI card (KB) + @workflow.nextMessage + Single Choice
- [ ] BookServices — Insert Record + confirmation + Send Email ×2
- [ ] AnotherQuestion — Single Choice: Yes → MenuChoice | No → End

### Configuration
- [ ] SMTP configured — Send Email cards working (owner + customer)
- [ ] Knowledge Base — Client FAQ + service list uploaded
- [ ] Webchat colors / logo customised to client brand
- [ ] Embed `<script>` tag copied → pasted into client website

### Testing
- [ ] FAQ branch tested
- [ ] Hubungi Kami branch tested
- [ ] Full booking flow tested (pick service → subservice → confirm → both emails arrive)

---

## GROWTH ADDITIONS

### Botpress — Extra Nodes
- [ ] Standard14 DetectLanguage — AI Task → user_language
- [ ] All nodes use greeting_translated (BM / English / Mandarin auto-detected)
- [ ] AI-generated dynamic menus (service_choices_raw, subservice_choices_raw)
- [ ] Standard12 BookServices — Execute Code webhook trigger to n8n

### n8n — Workflows
- [ ] Workflow 1: Webhook → Edit Fields → [Wait2 → WABlas (owner WA)] + [Google Sheets append]
- [ ] Workflow 2: Webhook1 → Wait (24hr) → Get Sheets → If (!=Converted) → WABlas (customer) → Update sheet

### Google Sheets
- [ ] Sheet created — columns A–J confirmed
- [ ] Connected to Workflow 1 (append) and Workflow 2 (read + update)

### WABlas
- [ ] API token configured in n8n Header Auth
- [ ] Owner WhatsApp notification tested
- [ ] 24hr customer follow-up tested

---

## PRO ADDITIONS

### Botpress — Extra Nodes
- [ ] QualifyNode — Capture customer_type
- [ ] ReturningCheck — Execute Code: lead_score + is_returning
- [ ] GoalSelection — Capture customer_goal
- [ ] SmartRecommend — AI Task → chosen_service
- [ ] UpsellNode — AI Task → upsell_choice
- [ ] BundleSummary — Final lead_score + lead_temp

### n8n — Workflows
- [ ] Workflow 1: Webhook3 → Lead scoring → If (hot) → WABlas HOT alert | If (warm) → WABlas WARM notify
- [ ] Workflow 2: Webhook4 → Day 1/3/7 follow-up sequence
- [ ] Workflow 3: Schedule Trigger (Mon 9am) → Get Sheets → JS → Gmail dashboard
- [ ] Workflow 4: Webhook5 → Update sheet (Converted) → WABlas confirmation

### Google Sheets
- [ ] Columns A–Q confirmed (extended from Growth)
- [ ] Lead Score, Temperature, Bundle Type, Upsell Choice, Customer Type, Revenue columns set

---

## Deployment

- [ ] Duplicate template bot in Botpress
- [ ] Upload client KB (FAQ + services)
- [ ] Update all business name variables
- [ ] Configure SMTP
- [ ] Embed webchat on client website
- [ ] Final end-to-end test with client
- [ ] Client sign-off received
