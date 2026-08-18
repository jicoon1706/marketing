# IGEN VERITAS — Content Pipeline Guide

> How to plan, produce, caption, schedule, and archive Instagram content using the AI-assisted pipeline.

---

## Overview

The pipeline has two layers:

1. **Monthly Planning** — done once at the start of each month. AI suggests a full content calendar, you review and approve it.
2. **Post Production** — done post by post throughout the month. Each approved post goes through: content creation → approval → caption → schedule → archive.

---

## Skills Involved

| Skill | Role |
|-------|------|
| `social-pipeline` | Runs everything — planning, briefing, captions, scheduling, archiving |
| `branded-social-visual` | Called during image step — generates coded poster + outputs AI prompt |

Both skills are invoked by talking naturally. No slash commands needed.

---

## Layer 1 — Monthly Planning

### How to start

**Say:** `"plan June"` or `"suggest content for June"`

### What Claude does

1. Reads brand context (`brand/IGEN_VERITAS_Brand_Guidelines.md`, `CLAUDE.md`)
2. Reads caption and hashtag rules (`content/_templates/caption_formulas.md`, `content/_templates/hashtag_bank.md`)
3. Checks what was posted last month to avoid repeating topics
4. Finds the highest CB number used so far
5. Outputs a full calendar table for the month

### Output format

```
# Content Plan — June 2026
Status: Pending approval
Theme: "Smart Business, Real Results"
Total posts: 16 (Instagram only)

| CB     | Date   | Day | Type       | Format | Topic                           | Style      | Service    |
|--------|--------|-----|------------|--------|---------------------------------|------------|------------|
| CB-024 | Jun 2  | Mon | Pain Point | Image  | Losing leads overnight          | Template A | AI Chatbot |
| CB-025 | Jun 4  | Wed | Education  | Reel   | How n8n automates follow-ups    | Talking hd | AI Chatbot |
| CB-026 | Jun 7  | Sat | Offer      | Image  | Package reveal Basic/Growth/Pro | Template D | AI Chatbot |
...
```

### Review and approve

- Request changes freely: *"Change CB-025 to an image"*, *"Add a mobile app post in week 3"*, *"Move CB-026 to Friday"*
- Claude updates the table until you're happy
- **Say:** `"approve"` when ready

**Result:** Saved to `content/plans/2026-06_plan.md`. Nothing is produced yet — no images, no captions.

---

## Layer 2 — Post Production

### Step 1 — Start a post

**Say:** `"work on CB-024"`

Claude reads the approved plan, pulls the CB-024 row, creates `content/pipeline/CB-024.md`, then recommends a format:

```
For CB-024 (Losing leads overnight):
→ Recommended: Image
   Reason: Pain point posts hit harder as a dark static visual.

→ Alternative: Reel
   Works if you want to speak directly to camera.

Which format?
```

---

### Step 2 — Generate content

#### If Image

**Say:** `"image"`

Claude delivers **two things simultaneously:**

**1 — Coded image (instant, no API)**
Python + Pillow draws the poster using exact brand colors, gradients, and typography.
Saved to: `social-media/CB-024_pain.png`

**2 — AI prompt for external tools**
A ready-to-copy prompt you can paste into any AI image generator:

```
Instagram marketing poster for IGEN VERITAS, Malaysian AI tech company.
Square 1:1 format. Dark dramatic mood.

Background: Very dark navy, soft violet-purple radial glow at center-left.
Top-left: Small white label "IGEN VERITAS" and "igen-veritas.com".
Center-top: Bold white headline — "Pelanggan tunggu." / "You tidur."
one word highlighted violet.
Center: Dark frosted glass card — clock "2:47 AM", red dot "0 leads captured".
Bottom: Gray subtext. Violet pill CTA "DM 'INFO' sekarang".
Style: respond.io dark marketing. No people. High contrast. Typography-driven.

Suggested tools: Midjourney · DALL-E · Ideogram · Canva AI · Skywork AI
Aspect ratio: 1:1 (square)
Midjourney tip: add --ar 1:1 --style raw
```

**Your choice:**
- Keep the coded image → say `"approved"`
- Paste the AI prompt into your preferred tool → generate → save it to `social-media/CB-024_pain.png` (overwrite) → say `"approved"`
- Want changes to the coded image → describe what to change → Claude regenerates

#### If Reel

**Say:** `"reel"`

Claude writes a full production brief you can film yourself:

```
Concept: [what this video is and why it works]
Duration: 15 / 30 / 45 seconds
Style: Talking head / Screen record / Text-on-screen

Hook (first 3 seconds): [exact opening line]

Script:
[0–3s]   HOOK — what to say or show
[3–20s]  BODY — breakdown by section
[20–30s] CTA — closing line

Shot List:
| Shot | Duration | What to show | Text overlay |
...

Text Overlays: [list of on-screen text and timing]
Music vibe: [energy description]
```

You film and edit the Reel yourself (CapCut, Instagram editor, etc.).

---

### Step 3 — Approve the content

**Hard gate — nothing moves forward without this.**

- Happy with the image or done filming the Reel → **say:** `"approved"`
- Want changes → describe them → Claude adjusts → review again
- This gate exists so captions are never written for content you haven't seen

---

### Step 4 — Caption (automatic after approval)

The moment you say approved, Claude:
1. Reads `content/_templates/caption_formulas.md` → picks the right formula (Pain Point, Education, Proof, Package, CTA, or Engagement)
2. Reads `content/_templates/hashtag_bank.md` → picks the right pre-built set, checks recent posts to avoid repeating the same hashtags back-to-back

Writes and saves the caption inside `content/pipeline/CB-024.md`. Example:

```
Your business closes at 6PM. Your competitor's doesn't.

While you sleep, customers are texting, asking questions,
and clicking away when no one answers.

That's not a people problem — it's a systems problem.

✅ Replies to every enquiry instantly
✅ Qualifies leads before you wake up
✅ Sends follow-up messages automatically
✅ Works 24/7 without you lifting a finger

DM us "AUTOMATE" and we'll show you how it works for your business.

#AIchatbot #WebsiteChatbot #BusinessAutomation #MalaysiaTech
#MalaysiaSME #KualaLumpur #DigitalTransformation #IGenVeritas
```

No action needed from you — Claude shows it and waits for the next command.

---

### Step 5 — Schedule

**Say:** `"schedule CB-024"`

Claude checks:
- The intended date from the approved plan
- What's already in `content/ready-to-post/` (no stacking two posts on the same day)
- Best windows: Tue–Thu, 8–10am or 7–9pm MYT

Outputs a recommendation:

```
Recommended: Monday Jun 2 at 8:00am MYT
Reason: First post of the month. Pain point hooks perform better
in the morning feed before the workday starts.

Alternative: Monday Jun 2 at 7:30pm MYT
```

**You confirm** → file moves from `content/pipeline/CB-024.md` → `content/ready-to-post/CB-024.md`

---

### Step 6 — Post on Instagram (you do this)

Open `content/ready-to-post/CB-024.md` — everything is in one file:

| What | Where |
|------|-------|
| Image file | `social-media/CB-024_pain.png` |
| Caption | Inside `CB-024.md` — copy-paste ready |
| Post time | Listed in the Schedule section |

Upload the image, paste the caption, post or schedule it on Instagram.

---

### Step 7 — Archive

**Say:** `"mark CB-024 as posted"`

File moves to `content/posted/2026-06/CB-024.md`. Done.

---

## The Full Flow at a Glance

```
"plan June"
      ↓
Full calendar table → you edit → "approve"
      ↓
Saved: content/plans/2026-06_plan.md
      ↓

"work on CB-024"
      ↓
Brief pulled from plan → CB-024.md created in pipeline/
      ↓
Image or Reel? → you choose
      ↓

IF IMAGE:
  Coded poster generated (Pillow, instant) → social-media/CB-024_pain.png
  AI prompt also output → copy-paste into Midjourney/DALL-E/Canva AI/Skywork/etc
  Keep coded image OR replace with AI-generated one (same filename)
      ↓
IF REEL:
  Full script + shot list + text overlays + music vibe
  You film and edit it yourself
      ↓

"approved"  ← hard gate
      ↓
Caption auto-written (caption_formulas.md + hashtag_bank.md)
      ↓
"schedule CB-024" → slot recommended → file moves to ready-to-post/
      ↓
You post on Instagram manually
      ↓
"mark CB-024 as posted" → archived to posted/2026-06/
```

---

## Folder Structure

```
marketing_team/
├── content/
│   ├── plans/              ← approved monthly plans (source of truth)
│   │   └── 2026-06_plan.md
│   ├── pipeline/           ← posts being worked on right now
│   │   └── CB-024.md
│   ├── ready-to-post/      ← done, scheduled, waiting to post
│   │   └── CB-024.md
│   └── posted/             ← archive after publishing
│       └── 2026-06/
│           └── CB-024.md
│
├── social-media/           ← all generated PNG images
│   └── CB-024_pain.png
│
└── docs/
    └── content-pipeline-guide.md   ← this file
```

---

## Other Skills in the Repo

These are standalone tools — not part of the social-pipeline. Use them independently when needed.

| Skill | Use it when... |
|-------|---------------|
| `copywriting` | Writing website copy, landing pages, homepage text |
| `copy-editing` | Reviewing and improving existing copy |
| `cold-email` | Writing B2B outreach emails to prospects |
| `emails` | Designing drip sequences, welcome series, nurture flows |
| `social` | Getting social media strategy advice or content repurposing ideas |
| `image` | General guidance on AI image tools, Canva, product mockups |
| `marketing-ideas` | Brainstorming growth tactics when stuck |
| `marketing-psychology` | Applying psychology to messaging or pricing |
| `launch` | Planning a product or feature launch (GTM, Product Hunt, etc.) |
| `ads` | Running Google, Meta, or LinkedIn ad campaigns |
| `ad-creative` | Generating ad headlines and copy variations at scale |
| `analytics` | Setting up GA4, UTM tracking, event tracking |
| `ab-testing` | Designing and running A/B tests |
| `co-marketing` | Finding partners, planning joint campaigns |
| `free-tools` | Planning a free tool as a lead generation asset |

---

*Last updated: May 2026 | IGEN VERITAS internal use only*
