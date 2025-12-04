# Tutorial 4: Training Your AI to Write in Your Voice

**Time**: 30 minutes  
**Goal**: Make AI draft documents that sound like you, not a generic AI

---

## The Problem

When AI drafts your emails, updates, or docs, they often sound:
- Too formal
- Too generic
- Like an AI wrote them

**Solution**: Train AI on your actual writing samples so it matches your voice.

---

## How Voice Training Works

```
Your Writing Samples → AI Analyzes Patterns → Voice Guide → AI Drafts in Your Voice
```

**AI learns**:
- Your sentence structure
- Phrases you use/avoid
- Tone by audience
- How you open and close
- Your level of formality

---

## Step 1: Collect Writing Samples (10 min)

### What to Collect

Gather **5-10 samples** of your real writing across different contexts:

**Professional**:
- Email to peer (casual)
- Email to executive (formal)
- Slack messages (very casual)
- Product spec intro (technical)

**External**:
- LinkedIn post (public voice)
- Blog post excerpt (teaching)
- Customer email (warm, helpful)

### Where to Find Samples

- ✅ Recent sent emails (last 3 months)
- ✅ Slack messages that got good responses
- ✅ LinkedIn posts with engagement
- ✅ Docs you're proud of

### What Makes Good Samples

✅ **Include**:
- Writing you're proud of
- Natural, unedited messages
- Mix of formal and casual
- Different audiences

❌ **Avoid**:
- Heavily edited/templated docs
- Writing you copied from others
- Samples that don't feel like "you"

---

## Step 2: Save Samples with Context (5 min)

Save to `knowledge/voice-samples/` with metadata:

### Example: email-to-peer.md

```markdown
# Email to Peer - Feature Delay

**Context**: Telling teammate about timeline change  
**Audience**: Engineering lead (peer)  
**Tone**: Casual, direct  
**Date**: 2024-11-15

---

Hey Alex,

Quick heads up - pushing mobile redesign to next sprint.

Reason: QA found 3 P0 bugs in checkout. Need to fix those first. Makes more sense to do it right than rush.

New timeline:
- Bugs fixed by Friday
- Redesign starts Monday  
- Should still hit Q1 launch

Let me know if this breaks anything on your end.

Sam
```

**See `examples/voice-samples/` for more formatted examples.**

---

## Step 3: Analyze Your Voice (10 min)

### Run Voice Analysis

Ask AI:

```
"Read all files in @knowledge/voice-samples/ and analyze my writing style.

Extract patterns for:
1. Sentence structure and length
2. How I open and close messages
3. Phrases I use frequently
4. Words/phrases I never use
5. Tone by audience (peer vs exec vs public)
6. How I structure information

Create a voice guide I can add to AGENTS.md"
```

### What AI Will Find

AI analyzes patterns like:

**Sentence Style**:
- Average length (you use short: 10-15 words)
- Punctuation (you prefer periods over semicolons)
- Fragments (you use them in casual contexts)

**Vocabulary**:
- Common openers: "Quick heads up", "Here's the thing"
- Closers: First name only, or "Let me know"
- Avoided phrases: "I hope this finds you well", "please don't hesitate"

**Structure**:
- Peer emails: Direct, problem → reason → solution
- Exec emails: Recommendation first, data in bullets, clear ask
- Public posts: Hook first line, numbered lists, question at end

**Tone by Audience**:
- Peers: Very casual, humor OK, can be blunt
- Executives: Concise, data-first, respectful of time
- Public: Confident, teaching tone, vulnerable about mistakes

---

## Step 4: Create Your Voice Guide (5 min)

AI will generate something like:

```markdown
## My Writing Voice

### Sentence Style
- Short sentences. Punchy. Rarely over 15 words.
- Use questions to transition: "So what does this mean?"
- Prefer periods over semicolons or em-dashes

### Opening Patterns
**Peer emails**: Jump straight to point
- "Quick heads up"
- "FYI on [topic]"
- Never: "Hope you're well"

**Exec emails**: Lead with recommendation
- "[Recommendation] - here's why"
- Subject line contains the ask
- Never: Pleasantries or long context

**Public posts**: Bold, specific hook
- Lead with surprising fact or timeline
- Promise value in first line
- End with engagement question

### Phrases I Use
- "Here's the thing..."
- "The short version:"
- "Let me know if this breaks anything"
- "Should still hit [deadline]"

### Phrases I Never Use
- "I hope this email finds you well"
- "Please don't hesitate to reach out"
- "Key insights" or "learnings"
- "Synergy", "leverage" (as verb), "circle back"

### Tone Calibration

**To Peers**:
- Very casual ("Hey", "FYI")
- Humor welcome
- Direct, can be blunt
- Incomplete sentences OK

**To Executives**:
- Data-first, bullets
- Recommendation up front
- Clear ask/decision needed
- No fluff

**Public (LinkedIn/Blog)**:
- Confident but not arrogant
- Numbered lists, scannable
- Self-aware (admit mistakes)
- Teaching, not preaching

### Formatting
- Short paragraphs (2-3 sentences max)
- Bullets for options/lists
- Bold for **key points**
- Numbers when relevant (40%, 3 bugs, $50K)
```

---

## Step 5: Add to AGENTS.md

Add your voice guide to AGENTS.md:

```markdown
## My Writing Voice

[Paste your voice guide here]

### When Drafting

When you draft any communication for me:
1. Apply these patterns consistently
2. Reference @knowledge/voice-samples/ if unsure
3. Match formality to audience context
4. Ask me to review before finalizing
```

---

## Step 6: Test Your Voice (5 min)

### Test 1: Peer Email

```
"Draft an email to my engineering lead about delaying a feature by one week.
Use my voice from @knowledge/voice-samples/email-to-peer.md"
```

**Look for**:
- ✅ Opens directly (no pleasantries)
- ✅ Problem → reason → solution structure
- ✅ Casual tone
- ✅ Uses your typical phrases

### Test 2: Executive Update

```
"Draft a status update for my VP about Q4 launch risks.
Use my exec communication style from @knowledge/voice-samples/"
```

**Look for**:
- ✅ Recommendation/ask in first line
- ✅ Data in bullets
- ✅ Concise, no fluff
- ✅ Clear decision needed

### Test 3: Public Post

```
"Draft a LinkedIn post about lessons from our mobile launch.
Use my public voice from @knowledge/voice-samples/"
```

**Look for**:
- ✅ Hook in first line
- ✅ Numbered list format
- ✅ Ends with engagement question
- ✅ Confident but self-aware tone

---

## Refining Your Voice

### Give Feedback

When AI drafts don't match:

```
"Good start, but I wouldn't say 'I wanted to reach out' - 
I'd just say 'Quick update on launch timing.'

Also too many bullet points. I usually write in short paragraphs for peer emails.

Try again."
```

### Context-Specific Adjustments

```
"This is for a customer, not internal team.
Make it warmer and more helpful. Check my customer email samples."
```

### Iterate

First draft → feedback → second draft → feedback → ...

AI learns from your corrections.

---

## Voice Maintenance

### Monthly: Update Samples

Your voice evolves. Add new samples:

```
"That email I just sent to Sarah was good - save it as a sample.
Add to @knowledge/voice-samples/email-to-exec-2.md"
```

### Quarterly: Refresh Guide

```
"Read my recent writing samples and update my voice guide.
What patterns have changed since last update?"
```

---

## Advanced: Multi-Context Voice

Document different voices for different contexts:

```markdown
## Voice by Context

### Internal (Very Casual)
- Incomplete sentences fine
- Lowercase OK in Slack
- Humor and sarcasm welcome
- Emojis sparingly (🙏, 🎉, 👍)

### Customer-Facing (Warm Professional)
- Complete sentences
- Acknowledge their concern first
- Clear next steps
- Warmer language
- No jargon

### Board/Investor (Executive)
- Data-heavy
- Strategic framing
- Confidence without arrogance
- Clear business impact
- Forward-looking
```

---

## Common Issues

**"Still sounds too formal"**
- Add more casual samples (Slack, quick emails)
- Be explicit about phrases to avoid
- Tell AI: "Write like texting a smart colleague"

**"Doesn't match my structure"**
- Add structural notes to voice guide
- Example: "I always open emails with the ask, not context"
- Show before/after examples

**"Uses phrases I hate"**
- Create explicit blocklist in voice guide
- Call them out every time: "Never say 'leverage' as a verb"
- Add to AGENTS.md permanently

---

## Quick Start (20 minutes)

### Minimal Setup

1. **Collect 3 samples** (5 min)
   - One peer email
   - One exec email  
   - One public post or Slack thread

2. **Run analysis** (5 min)
   ```
   "Analyze these 3 samples and create a basic voice guide"
   ```

3. **Add to AGENTS.md** (2 min)
   Paste the guide

4. **Test** (8 min)
   Have AI draft something and refine

---

## Examples

See **`examples/voice-samples/`** for:
- ✅ 6 formatted voice sample files
- ✅ Different contexts and audiences
- ✅ Analysis annotations
- ✅ Pattern breakdowns

Copy the format, replace with your writing.

---

## Next Tutorial

**Tutorial 5**: Advanced Workflows
- Initiative expansion workflow
- Research synthesis
- Decision documentation
- Complex multi-step workflows

---

**Key Takeaway**: Voice training is like giving AI your writing DNA. Invest 30 minutes once, get drafts that sound like you forever. Update quarterly to stay current.

