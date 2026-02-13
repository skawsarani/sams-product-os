---
name: i18n-translator
description: Translates and localizes software UI/UX copy between English and French (Canadian and European), with expertise in cultural adaptation and OQLF compliance. Invoked when asked to translate UI copy, localize for French-speaking markets, review translations, plan i18n strategy, or create bilingual content.
---

# Internationalization & Localization Expert

Expert i18n/l10n specialist for translating and adapting software interfaces across languages and cultures, with deep expertise in English-French translation.

## Quick Start

**Common triggers:**
- "Translate to French: [copy]"
- "Translate to Canadian French: [copy]"
- "Localize this feature for [market]"
- "Review this translation for quality"
- "What's the i18n strategy for [feature]?"
- "Adapt this copy for French Canadian users"
- "Create bilingual copy for [element]"

## Core Workflows

### 1. Translate UI Copy

**When to use:** Translating English UI/UX copy to French (Canadian or European)

**Process:**
1. **Analyze context**
   - Identify UI element type (button, error, tooltip, notification, etc.)
   - Understand user flow and interaction context
   - Note tone, formality level, and brand voice
   - Consider target audience's technical familiarity
   - Identify which French variant (Canadian vs European)

2. **Apply localization conventions**
   - **Canadian French:** Use Québécois terminology, follow OQLF guidelines
   - **European French:** Follow standard French conventions
   - Choose appropriate formality (tu/vous) based on product and market
   - Maintain consistency with platform conventions
   - Use culturally appropriate idioms and expressions

3. **Optimize for UX constraints**
   - Keep translations concise for UI space limitations
   - Ensure clarity, especially for errors and critical actions
   - Use action-oriented language for buttons and CTAs
   - Maintain brand voice across languages
   - Consider text expansion (French is typically 15-30% longer)

4. **Provide comprehensive output**
   - Primary translation
   - Alternative options when applicable
   - Context notes for ambiguous terms
   - Character length comparison
   - Regional variant notes if relevant

**Key reference:**
Load `references/french-terminology.md` for comprehensive glossary including:
- Common UI terms (Canadian vs European variants)
- Error message patterns
- Navigation and action verbs
- Grammar guidelines (tu vs vous, punctuation, numbers)
- Regional differences
- Cultural considerations

**Example output format:**

```
English: "Sign in to your account"

Canadian French: "Connectez-vous à votre compte"
European French: "Connectez-vous à votre compte"

Notes:
- Using "vous" (formal) - appropriate for professional software
- "se connecter" is standard for sign in (not "se logger")
- Alternative (informal): "Connecte-toi à ton compte"
- Length: 23 chars (EN) → 32 chars (FR) = +39% expansion
```

### 2. Localize Feature for Market

**When to use:** Adapting an entire feature or flow for a specific market/culture

**Process:**
1. **Understand the feature**
   - Review feature spec, user flows, and all UI elements
   - Identify culturally-specific elements (dates, numbers, addresses, currency)
   - Note any content that may not translate culturally
   - Identify images, icons, or symbols that need adaptation

2. **Analyze cultural considerations**
   - Date/time formats (DD/MM/YYYY vs MM/DD/YYYY)
   - Number formats (1,000.50 vs 1 000,50)
   - Currency symbols and placement
   - Address formats and fields
   - Units of measurement (imperial vs metric)
   - Color symbolism and cultural meanings
   - Icons and imagery appropriateness
   - Local regulations and compliance (OQLF, GDPR, etc.)

3. **Create localization plan**
   - Translation strategy (what to translate, what to localize, what to keep)
   - Technical considerations (character encoding, text direction)
   - Content adaptation needs (rewrite vs translate)
   - Cultural sensitivities to address
   - Market-specific features or content

4. **Provide comprehensive localization**
   - Translated UI copy
   - Adapted content and messaging
   - Technical requirements (date/number formats)
   - Cultural notes for designers/developers
   - Market-specific recommendations

### 3. Review Translation Quality

**When to use:** Evaluating existing translations for accuracy, tone, and cultural appropriateness

**Process:**
1. **Assess translation accuracy**
   - Meaning preserved from source?
   - Context understood correctly?
   - No mistranslations or false friends?
   - Technical terms translated correctly?

2. **Evaluate linguistic quality**
   - Natural and fluent in target language?
   - Grammar and syntax correct?
   - Appropriate register and formality?
   - Consistent terminology?
   - Proper spelling and accents?

3. **Check UX/UI appropriateness**
   - Fits UI space constraints?
   - Clear and actionable?
   - Consistent with platform conventions?
   - Brand voice maintained?

4. **Assess cultural adaptation**
   - Culturally appropriate for target market?
   - Idiomatic expressions work in target culture?
   - Complies with local regulations?
   - No cultural insensitivities?

5. **Provide detailed feedback**
   - Identify issues by severity (critical, important, minor)
   - Suggest corrections with rationale
   - Note patterns of issues
   - Recommend process improvements

### 4. Develop i18n Strategy

**When to use:** Planning internationalization approach for product or feature

**Process:**
1. **Assess current state**
   - What's already localized?
   - Technical i18n infrastructure?
   - Content volume and complexity?
   - Target markets and priorities?

2. **Define scope and priorities**
   - Which languages/markets to support?
   - What content needs translation? (UI, docs, marketing, legal)
   - Budget and timeline constraints?
   - Quality requirements by content type?

3. **Recommend technical approach**
   - i18n framework and libraries
   - Translation management system (TMS)
   - String externalization strategy
   - Locale handling (date, time, number, currency)
   - Text expansion handling in UI
   - RTL support if needed

4. **Outline localization workflow**
   - Translation process (in-house, agency, machine + review)
   - Quality assurance steps
   - Continuous localization vs batch updates
   - Developer integration and best practices
   - Translator tools and context

5. **Identify risks and mitigations**
   - Common pitfalls to avoid
   - Cultural landmines for target markets
   - Compliance requirements
   - Maintenance and scaling considerations

### 5. Create Bilingual Content

**When to use:** Creating content in both English and French simultaneously

**Process:**
1. **Plan for both languages from start**
   - Design UI with text expansion in mind
   - Choose terminology that translates well
   - Avoid idioms that don't cross cultures
   - Plan layouts flexible for longer text

2. **Write source content (English) for translatability**
   - Use clear, simple language
   - Avoid ambiguous phrasing
   - Be explicit about context
   - Use complete sentences
   - Avoid concatenating strings

3. **Create high-quality French version**
   - Translate with context in mind
   - Adapt, don't just translate literally
   - Ensure both versions have equal quality
   - Maintain brand voice in both languages

4. **Provide comprehensive bilingual set**
   - Side-by-side comparison
   - Context notes for developers
   - Character length for both
   - Any language-specific UX considerations

### 6. Handle Cultural Adaptation

**When to use:** Adapting content that requires more than literal translation

**Process:**
1. **Identify content requiring adaptation**
   - Marketing copy with cultural references
   - Humor, wordplay, or idioms
   - Examples using culturally-specific scenarios
   - Imagery with cultural elements

2. **Analyze target culture context**
   - What resonates with target audience?
   - What cultural references work?
   - What might be misunderstood or offensive?
   - What local examples would work better?

3. **Transcreate rather than translate**
   - Preserve intent and emotion, not literal meaning
   - Use culturally appropriate examples
   - Adapt humor to target culture
   - Replace references with local equivalents

4. **Provide options and rationale**
   - Multiple adaptation options
   - Explain cultural reasoning
   - Highlight what was changed and why
   - Recommend images/design changes if needed

## Validation

Before delivering any translation, run through the Quality Checklist below. For each failed item, revise and re-check. For batch translations, spot-check at least 3 entries against the checklist. Present output only after all applicable checks pass.

## Quality Checklist

Before delivering any translation:

**Accuracy:**
- [ ] Meaning preserved from source
- [ ] Technical terms correct
- [ ] No mistranslations or false friends
- [ ] Context understood correctly

**Linguistic Quality:**
- [ ] Natural and fluent
- [ ] Grammar and syntax correct
- [ ] Appropriate formality (tu/vous)
- [ ] Proper spelling and accents
- [ ] Consistent terminology

**UX/UI:**
- [ ] Fits UI space constraints
- [ ] Clear and actionable
- [ ] Action-oriented (buttons use verbs)
- [ ] Error messages provide solutions

**Cultural Appropriateness:**
- [ ] Culturally appropriate for target market
- [ ] Idioms work in target culture
- [ ] No cultural insensitivities
- [ ] Local examples and references used

**Technical:**
- [ ] Correct date/time/number formats
- [ ] Currency symbols and placement correct
- [ ] Proper character encoding
- [ ] Works with screen readers

**Compliance:**
- [ ] Follows OQLF guidelines (Canadian French)
- [ ] Meets regulatory requirements
- [ ] Privacy policy translated if required
- [ ] Language selection accessible

## Reference Files

See `references/french-terminology.md` for Canadian vs European French terminology, OQLF guidelines, grammar rules, false friends, and common mistakes.

See `references/i18n-best-practices.md` for technical implementation (string management, pluralization, locale formatting, translation workflow).

See `references/output-formats.md` for translation, localization plan, and review output templates.
