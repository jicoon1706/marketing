# Client Onboarding SOP — IGEN VERITAS

---

## Step 1 — Sales & Close

- [ ] Demo the chatbot (use existing test bot or Loom recording)
- [ ] Send package comparison (Basic / Growth / Pro)
- [ ] Confirm package chosen and collect payment (setup fee)
- [ ] Send invoice / receipt

## Step 2 — Create Client Folder

- [ ] Duplicate `clients/_template/` → rename to `clients/[client-slug]/`
- [ ] Fill in `brief.md` with all client details
- [ ] Create Google Sheet (Growth/Pro) — name it `[Client Name] Leads`

## Step 3 — Onboarding Call (30–45 min)

Topics to cover:
- [ ] Business name, address, hours
- [ ] Services offered (get full list + descriptions + pricing)
- [ ] FAQ list (minimum 10 questions)
- [ ] Owner WhatsApp number for notifications
- [ ] Owner SMTP email for booking alerts
- [ ] Preferred bot language(s)
- [ ] Brand colors / logo for webchat widget

## Step 4 — Build the Bot

- [ ] Duplicate template bot in Botpress
- [ ] Upload Knowledge Base (FAQ + service list)
- [ ] Configure all nodes per package checklist
- [ ] Set up n8n workflows (Growth / Pro)
- [ ] Configure WABlas (Growth / Pro)
- [ ] Test all flows end-to-end

See: `clients/[client-slug]/build-checklist.md`

## Step 5 — Deploy

- [ ] Get website admin access from client
- [ ] Embed webchat `<script>` tag
- [ ] Run final test on live site
- [ ] Record Loom walkthrough for client

## Step 6 — Handover

- [ ] Send client the Loom + simple user guide
- [ ] Add client to WhatsApp support group
- [ ] Set calendar reminder for first monthly report
- [ ] Mark client as Active in tracker

## Step 7 — Monthly Maintenance (recurring)

- [ ] Review bot performance (conversations, leads captured)
- [ ] Update KB if client adds new services
- [ ] Send monthly performance report (Pro: auto-generated via n8n)
- [ ] Collect monthly retainer payment
