# Build Checklist — Jazzmine's Salon | BASIC

> Target: 4–6 hours from the salon template bot
> Full detail → [AI_Chatbot_Guide_Basic.md](AI_Chatbot_Guide_Basic.md)

---

## Pre-Build — Collect From Owner
- [ ] Website URL (widget needs somewhere to live)
- [ ] Gmail for SMTP + booking notifications
- [ ] **Real service price list** (guide currently uses estimates)
- [ ] Opening hours + rest day
- [ ] Booking policy — deposit / cancellation / walk-ins
- [ ] Logo PNG (transparent)
- [ ] Website admin contact (who pastes the script tag)

## Botpress — Conversation Nodes
- [ ] Greeting — business name = Jazzmine's Salon, curly-hair angle in copy
- [ ] MenuChoice — Tanya Soalan / FAQ | Hubungi Kami | Tempah / Book Appointment
- [ ] AutonomousNode — KB attached + instructions pasted, "user wants to book" → BookSession
- [ ] ContactInfo — phone, address, hours, IG/FB → always → AnotherQuestion
- [ ] BookSession — Capture: user_name, user_phone, user_email
- [ ] ChooseServices — Single Choice (user_service), 5 options
- [ ] ServColoring — 6 sub-services → always → SubServiceExplanation
- [ ] ServCuts — 4 sub-services → always → SubServiceExplanation
- [ ] ServTreatments — 4 sub-services → always → SubServiceExplanation
- [ ] ServScalp — 3 sub-services → always → SubServiceExplanation
- [ ] ServBeauty — 3 sub-services → always → SubServiceExplanation
- [ ] SubServiceExplanation — AI card (KB) + @workflow.nextMessage + Single Choice
- [ ] BookServices — Insert Record + confirmation + Send Email ×2
- [ ] AnotherQuestion — Ya → MenuChoice | Tak → End

## Configuration
- [ ] SMTP configured (salon Gmail) — owner + customer emails firing
- [ ] Knowledge Base uploaded — About, services + real prices, hours, location, policy, 15 FAQs
- [ ] Widget styled — `#FF2D4E` primary, `#FF7A1A` accent, logo, welcome bubble
- [ ] Embed `<script>` tag pasted into the salon website

## Testing
- [ ] FAQ branch — curly-hair question answered from KB
- [ ] FAQ → booking transition works ("I want to book")
- [ ] Hubungi Kami shows correct phone + address
- [ ] Full booking: Hair Coloring → Balayage → confirm → both emails arrive
- [ ] Second branch tested (Scalp Care)
- [ ] Tested in BM and English
- [ ] Tested on mobile
- [ ] Bot never quotes a fixed price — always "from RM X"

## Sign-Off
- [ ] Walkthrough call with owner
- [ ] Client sign-off received
- [ ] RM500 setup collected
- [ ] RM150/mo billing cycle started

**NOT IN BASIC:** ❌ n8n ❌ Google Sheets ❌ WhatsApp alerts ❌ Mandarin ❌ auto follow-up
