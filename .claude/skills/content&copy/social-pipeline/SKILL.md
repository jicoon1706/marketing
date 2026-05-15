---
name: social-pipeline
description: "Full Instagram content production pipeline for IGEN VERITAS — from monthly planning to archive. Use this skill for: 'plan [month]', 'suggest content for June', 'monthly content plan', 'work on CB-XXX', 'create CB-XXX', 'let's do CB-XXX', 'write caption for CB-XXX', 'schedule CB-XXX', 'mark CB-XXX as posted', or 'where are we on CB-XXX'. The pipeline has two layers: (1) Monthly Planning — AI suggests a full month calendar, user reviews and approves it; (2) Post Production — one post at a time from the approved plan: create content (image or Reel) → approve → caption → schedule → archive."
metadata:
  version: 2.0.0
---

# Social Media Pipeline — IGEN VERITAS

You manage Instagram content from monthly planning through to archive. Two layers: plan the month first, then produce each post one at a time. **Never produce content for posts that aren't in an approved monthly plan.**

---

## The Two-Layer System

```
LAYER 1 — MONTHLY PLANNING (once per month, early in the month)
  "plan June" → full calendar table → user reviews & edits → user approves
  → plan saved as content/plans/YYYY-MM_plan.md
  → no post files created yet

LAYER 2 — POST PRODUCTION (one post at a time, from the approved plan)
  "work on CB-XXX" → CB-XXX.md created in pipeline/ from the plan
       ↓
  Recommend: image or Reel? → user picks
       ↓
  Image → branded-social-visual → PNG saved
  Reel  → script + shot list → user produces it
       ↓
  User approves content → caption written → schedule → archive
```

---

## How to Invoke

| User says | What happens |
|-----------|-------------|
| "plan [month]" / "monthly content plan" / "suggest content for June" | Layer 1 — generate monthly plan |
| "work on CB-XXX" / "create CB-XXX" / "let's do CB-XXX" | Layer 2 — start production for that post |
| "image for CB-XXX" / "reel for CB-XXX" | Layer 2 — skip format question, go straight to that format |
| "approved" / "content looks good" | Tick content approved → write caption |
| "write caption for CB-XXX" | Write caption (check content is approved first) |
| "schedule CB-XXX" | Recommend slot, move to ready-to-post/ |
| "mark CB-XXX as posted" | Archive to posted/YYYY-MM/ |
| "where are we on CB-XXX" / "status CB-XXX" | Read the file, report current stage |

---

# LAYER 1 — Monthly Planning

## Trigger

"plan [month]" / "suggest content for [month]" / "monthly content plan" / "it's the start of the month"

## Step 1: Read context

Before generating anything, read ALL of these files:

**Brand & voice (read every time):**
1. `brand/IGEN_VERITAS_Brand_Guidelines.md` — brand personality, colors, tone per platform
2. `CLAUDE.md` — services, pricing tiers, target customers, posting cadence

**Content rules (read every time):**
3. `content/_templates/caption_formulas.md` — 6 proven caption formulas with real IGEN VERITAS examples; use these as the basis for all caption writing
4. `content/_templates/hashtag_bank.md` — 8 pre-built hashtag sets (A–H) + rotation strategy; always pick from here, never invent hashtags

**Planning context:**
5. `content/may_2026_content_calendar.md` — reference structure and themes from the previous month
6. `content/plans/` — existing monthly plans (check the latest approved month for continuity)
7. `content/pipeline/` + `content/ready-to-post/` + `content/posted/` — find highest CB number used

## Step 2: Generate the monthly plan

Output a complete calendar table for the month. Assign CB numbers starting from (highest existing CB + 1).

### Plan output format

```
# Content Plan — [Month YYYY]

**Status:** Pending approval
**Theme:** [Monthly campaign theme — 1 sentence]
**Total posts:** [N] (all Instagram)
**Service split:** AI Chatbot [X]% | Web Dev [X]% | Mobile App [X]% | UI/UX [X]%

---

## Content Calendar

| CB | Date | Day | Type | Format | Topic | Template / Style | Service |
|----|------|-----|------|--------|-------|------------------|---------|
| CB-XXX | [Date] | Mon | Pain Point | Image | [Topic] | Template A | AI Chatbot |
| CB-XXX | [Date] | Wed | Education | Reel | [Topic] | Talking head + text | AI Chatbot |
...

---

## Rationale
[3–5 bullet points explaining the month's strategy — why these topics, this distribution, this sequence]
```

### Column guide

| Column | What to put |
|--------|-------------|
| **Type** | Pain Point / Education / Proof / Offer / CTA / Thought Leadership |
| **Format** | Image / Reel |
| **Template / Style** | For images: A / B / C / D (from branded-social-visual). For Reels: brief description of video style |
| **Service** | AI Chatbot / Web Dev / Mobile App / UI-UX |

### Posting cadence rules
- 3–4 posts per week, Instagram only
- Best days: Mon, Wed, Fri, Sat
- Best times: 8–10am or 7–9pm MYT
- Post type rhythm: Pain early week → Education mid-week → Proof/Demo late week → Offer/CTA weekend

### Content type distribution (per month)
- 25% Pain Point — lead loss, no automation, competitors getting ahead
- 28% Education — how chatbot/web/app/uiux works, feature breakdowns
- 12% Proof/Demo — client results, chatbot conversations, before/after
- 15% Offer/CTA — pricing, "DM INFO", booking push
- 10% Thought Leadership — why AI matters for SMEs, digital future
- 10% Other CTA / Re-engagement

### Service distribution
- AI Chatbot: 50% of posts
- Web Dev: 20%
- Mobile App: 15%
- UI/UX: 15%

### Format recommendation by post type
- **Image** → Pain Point, Offer/CTA, Proof (stat-heavy), Thought Leadership
- **Reel** → Education (how-to, feature walkthroughs), Proof (demo walkthroughs), CTA (talking-to-camera)

## Step 3: Review loop

Present the full table and say: **"Review this plan — let me know what to change (topics, dates, types, formats) and I'll update it. Say 'approve' when it's ready."**

Make any changes the user requests. Never save the plan until explicitly approved.

## Step 4: Save the approved plan

When user says "approve" / "approved" / "looks good":
1. Add `**Status:** Approved — YYYY-MM-DD` to the plan header
2. Save as `content/plans/YYYY-MM_plan.md`
3. Tell the user: "Plan saved as `content/plans/YYYY-MM_plan.md` — [N] posts planned. When you're ready to produce a post, say 'work on CB-XXX' with the CB number from the plan."

**Do not create individual CB-XXX.md files yet.** They are created on demand in Layer 2.

---

# LAYER 2 — Post Production

## Trigger

"work on CB-XXX" / "create CB-XXX" / "let's do CB-XXX" / "start CB-XXX"

## Step 1: Read the approved plan

1. Find the monthly plan file in `content/plans/` that contains CB-XXX
2. Pull the row for CB-XXX: date, type, format recommendation, topic, template/style, service
3. Create `content/pipeline/CB-XXX.md` using the Post Brief Template below with Stage 1 filled in

## Step 2: Recommend format

Tell the user what format you recommend and why, then ask them to confirm:

```
For CB-XXX ([Topic]):
→ Recommended: [Image / Reel]
   Reason: [1 sentence — e.g., "Pain point posts hit harder as static images — dark visual + bold headline"]

→ Alternative: [Image / Reel]
   [1 sentence on when this would work instead]

Which format do you want to go with?
```

After user confirms, proceed to the relevant production section.

---

## Production — Image

1. Read the brief from `content/pipeline/CB-XXX.md`
2. Invoke the **branded-social-visual** skill with:
   - Post type → Template A/B/C/D
   - Headline, Subtext, CTA from the brief
   - CB number for the filename
3. The branded-social-visual skill will:
   - Generate a coded Pillow image → saved to `social-media/CB-XXX_[type].png`
   - Output a ready-to-copy AI prompt the user can paste into Midjourney, DALL-E, Canva AI, Skywork, etc.
4. After both are delivered:
   - Fill in the Content section of CB-XXX.md (filename, date, format: Image)
   - Tick `[x] Stage 2: Content created`
5. Remind the user: **"Coded image is at `social-media/CB-XXX_[type].png`. If you prefer an AI-generated version, use the prompt above, generate it in your tool, and save it to the same filename. Say 'approved' when happy."**

**Wait here.** Do not write the caption until the user explicitly says approved.

---

## Production — Reel

For Reels, produce a complete production brief the user can film and edit themselves.

Output format:

```
## Reel Brief — CB-XXX

**Concept:** [1 sentence — what this video is and why it works]
**Duration:** [15 / 30 / 45 seconds]
**Style:** [Talking head / Screen record / Text-on-screen / Voiceover / Demo walkthrough]
**Hook (first 3 seconds):** [Exact opening line or action — this must stop the scroll]

---

### Script

[0–3s]  [HOOK] — what to say or show
[3–Xs]  [BODY] — breakdown by section, time-stamped
[Xs–end] [CTA] — closing line

---

### Shot List

| Shot | Duration | What to show | Text overlay |
|------|----------|-------------|--------------|
| 1 | 3s | [description] | "[text]" |
...

---

### Text Overlays
[List of on-screen text and when to show each]

### Music vibe
[Describe the energy — e.g., "upbeat tech-forward, no vocals, builds with momentum"]

### Caption hook (first line for IG caption)
[Write the first line of the caption here — matches the Reel's opening]
```

After presenting the Reel brief:
- Fill in the Content section of CB-XXX.md (format: Reel, notes: brief provided)
- Tick `[x] Stage 2: Content created`
- Say: **"Reel brief saved to CB-XXX.md. Film and edit this, then say 'approved' when you're happy with the video."**

Wait for explicit approval before writing the caption.

---

## Stage 3 — Content Approval (user step)

When user says "approved" / "looks good" / "go ahead" / "approve CB-XXX":
- Tick `[x] Stage 3: Content approved` in the brief
- Immediately write the caption (Stage 4)

If user requests changes:
- For image: adjust generation and regenerate
- For Reel: update the script/shot list
- Never write captions until explicitly approved

---

## Stage 4 — Write Caption

Before writing, re-read:
- `content/_templates/caption_formulas.md` — pick the matching formula for this post type (Formula 1–6)
- `content/_templates/hashtag_bank.md` — pick the correct pre-built set (A–H) and check rotation

Write the Instagram caption following the formula from `caption_formulas.md` that matches the post type:
- Pain Point → Formula 1
- Education → Formula 2
- Proof/Results → Formula 3
- Package Reveal → Formula 4
- Direct CTA → Formula 5
- Engagement → Formula 6

Use the BM/English mix examples from `caption_formulas.md` as tone reference. The hook must feel like a natural continuation of the image or Reel — not a separate piece of writing.

Pick hashtags from the pre-built sets in `hashtag_bank.md`. Follow the rotation strategy — check what set was used on the most recent posts in `content/posted/` and `content/ready-to-post/` to avoid repeating the same set back-to-back.

**After writing:**
1. Save caption inside `content/pipeline/CB-XXX.md` under the Caption section
2. Tick `[x] Stage 4: Caption written`
3. Show the full caption to the user
4. Say: **"Caption saved. Say 'schedule CB-XXX' when you're ready to set the post date."**

---

## Stage 5 — Schedule

Recommend the best posting slot by:
1. Checking the intended date from the approved plan
2. Checking `content/ready-to-post/` to avoid stacking posts on the same day
3. Applying the cadence: 3–4x/week, Tue–Thu 8–10am or 7–9pm MYT preferred

Output:
```
Recommended: [Day] [Date] at [Time] MYT
(Matches your plan — [brief reason])

Alternative: [Day] [Date] at [Time] MYT
```

After user confirms:
1. Fill in Schedule section of the brief
2. Tick `[x] Stage 5: Scheduled`
3. Move file from `content/pipeline/CB-XXX.md` → `content/ready-to-post/CB-XXX.md`
4. Tell the user: "CB-XXX is ready to post on [Date] at [Time]. Find it in `content/ready-to-post/CB-XXX.md`"

---

## Stage 6 — Archive After Posting

When user says "posted" / "mark CB-XXX as posted" / "CB-XXX went live":
1. Tick `[x] Stage 6: Posted` in the brief
2. Move file from `content/ready-to-post/CB-XXX.md` → `content/posted/YYYY-MM/CB-XXX.md`
   (Use the month from the post date in the Schedule section. Create the folder if needed.)
3. Tell the user: "Archived to `content/posted/YYYY-MM/CB-XXX.md`"

---

## Post Brief Template

Every `content/pipeline/CB-XXX.md` uses this structure:

```markdown
# CB-XXX — [Post Type] — [Topic, 4–6 words]

## Pipeline Status
- [x] Stage 1: Brief created — YYYY-MM-DD
- [ ] Stage 2: Content created
- [ ] Stage 3: Content approved
- [ ] Stage 4: Caption written
- [ ] Stage 5: Scheduled
- [ ] Stage 6: Posted

---

## Brief (from monthly plan)

| Field | Value |
|-------|-------|
| Post type | Pain Point / Education / Proof / Offer / CTA |
| Format | Image / Reel |
| Template / Style | A / B / C / D (image) or [Reel style] |
| Topic | [Topic from plan] |
| Target emotion | [what the audience should feel] |
| Headline | [4–6 words for image / hook line for Reel] |
| Subtext | [1 supporting sentence] |
| CTA | DM 'INFO' sekarang / [custom] |
| Service | AI Chatbot / Web Dev / Mobile App / UI-UX |

---

## Content

| Field | Value |
|-------|-------|
| Format | Image / Reel |
| File / Output | `social-media/CB-XXX_[type].png` or [Reel brief saved here] |
| Created | YYYY-MM-DD |
| Notes | [special instructions or changes made] |

[For Reel: paste the full Reel Brief here]

---

## Caption

[Written in Stage 4 — after content is approved]

---

## Schedule

| Field | Value |
|-------|-------|
| Platform | Instagram |
| Post date | YYYY-MM-DD |
| Post time | HH:MM MYT |
| Slot reason | [why this date/time] |
```

---

## Folder Structure

```
content/
├── plans/                  ← monthly content plans (Layer 1)
│   ├── _template.md
│   └── YYYY-MM_plan.md     ← approved plan, source of truth for the month
│
├── pipeline/               ← posts being produced (Stages 1–4)
│   ├── _template.md
│   └── CB-XXX.md
│
├── ready-to-post/          ← scheduled, waiting to publish (Stage 5)
│   └── CB-XXX.md
│
└── posted/                 ← archive after publishing (Stage 6)
    └── YYYY-MM/
        └── CB-XXX.md

social-media/               ← all generated PNGs (unchanged)
```

---

## Quick Reference

| What you say | What Claude does |
|-------------|-----------------|
| "plan June" | Generate full month calendar table → you review → you approve → plan saved |
| "work on CB-XXX" | Create CB-XXX.md from plan → recommend image or Reel → produce it |
| "approved" | Tick content approved → write caption immediately |
| "schedule CB-XXX" | Recommend slot → move to ready-to-post/ |
| "mark CB-XXX as posted" | Archive to posted/YYYY-MM/ |
| "where are we on CB-XXX" | Read file → report current stage |
