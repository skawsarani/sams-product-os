# Internationalization (i18n) Best Practices

Comprehensive guide for implementing internationalization and localization in software products.

## Table of Contents

1. [Core i18n Principles](#core-i18n-principles)
2. [Technical Implementation](#technical-implementation)
3. [String Management](#string-management)
4. [Locale-Specific Formatting](#locale-specific-formatting)
5. [Translation Workflow](#translation-workflow)
6. [Quality Assurance](#quality-assurance)
7. [Common Pitfalls](#common-pitfalls)
8. [Cultural Adaptation](#cultural-adaptation)
9. [Compliance & Regulations](#compliance--regulations)

## Core i18n Principles

### 1. Design for i18n from Day One

**Why:** Retrofitting i18n is expensive and error-prone

**How:**
- Externalize all strings from code
- Design flexible UIs that adapt to text expansion
- Use locale-aware date/time/number formatting from the start
- Plan for RTL (right-to-left) languages if targeting those markets
- Avoid hardcoded assumptions about language structure

**Example:**
```javascript
// ❌ Bad: Hardcoded strings
<button>Sign in</button>

// ✅ Good: Externalized strings
<button>{t('auth.signIn.button')}</button>
```

### 2. Separate Content from Code

**Why:** Translators shouldn't need to edit code

**How:**
- Store all user-facing text in resource files (JSON, YAML, etc.)
- Use structured keys: `feature.component.element`
- Keep translations separate from application logic
- Use translation management systems (TMS)

**Example structure:**
```
/locales
  /en
    common.json
    auth.json
    dashboard.json
  /fr-CA
    common.json
    auth.json
    dashboard.json
  /fr-FR
    common.json
    auth.json
    dashboard.json
```

### 3. Provide Context to Translators

**Why:** Same English word can translate differently based on context

**How:**
- Add comments/descriptions to translation keys
- Provide screenshots or design mocks
- Document where/when strings appear
- Explain technical constraints (character limits)
- Share glossaries and style guides

**Example:**
```json
{
  "auth.signIn.button": {
    "message": "Sign in",
    "description": "Primary button on login page - action to authenticate",
    "maxLength": 20
  }
}
```

### 4. Test with Real Translations Early

**Why:** Catch layout issues and cultural problems early

**How:**
- Use pseudo-localization in development
- Test with actual translations, not just English
- Check longest translations (German, French often 30% longer)
- Test with non-Latin scripts (if applicable)
- Validate with native speakers

## Technical Implementation

### i18n Frameworks

**JavaScript/TypeScript:**
- `react-i18next` (React)
- `vue-i18n` (Vue)
- `i18next` (framework-agnostic)
- `FormatJS` (React Intl)
- `LinguiJS` (React)

**Backend:**
- `gettext` (PHP, Python, C)
- `i18n` gem (Ruby on Rails)
- `java.util.ResourceBundle` (Java)
- `fluent-rs` (Rust)

**Mobile:**
- Native iOS localization (`.strings` files)
- Native Android localization (`strings.xml`)
- React Native: `react-i18next`
- Flutter: `intl` package

### Recommended Architecture

```
┌─────────────┐
│   User      │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Language Detector  │ ← Detect from: browser, IP, user preference
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  i18n Framework     │ ← Load appropriate locale
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Translation Files  │ ← JSON/YAML per locale
└─────────────────────┘
```

### Locale Detection Priority

1. **Explicit user selection** (user chose language in settings)
2. **Stored preference** (cookie, local storage, account setting)
3. **Browser language** (Accept-Language header)
4. **IP-based detection** (geolocation)
5. **Fallback to default** (usually English)

**Special case - Quebec compliance:**
For Quebec users, French MUST be default regardless of browser settings to comply with Law 101.

### Code Organization

**Key naming convention:**
```
[namespace].[feature].[component].[element]

Examples:
- auth.signIn.button
- dashboard.sidebar.navigation
- errors.validation.email.invalid
- notifications.success.saveComplete
```

**Benefits:**
- Organized and scalable
- Easy to find related translations
- Clear context from key name
- Can load by namespace for code-splitting

## String Management

### 1. Never Concatenate Strings

**Why:** Word order, grammar, gender vary by language

**❌ Bad:**
```javascript
const message = "You have " + count + " new messages";
// Breaks in many languages with different word order
```

**✅ Good:**
```javascript
const message = t('inbox.messageCount', { count });
// Translation: "You have {{count}} new messages"
// French: "Vous avez {{count}} nouveaux messages"
```

### 2. Handle Pluralization Properly

**Why:** Pluralization rules vary wildly across languages

- English: 1, 2+ (two forms)
- French: 0-1, 2+ (two forms)
- Polish: 1, 2-4, 5+ (three forms)
- Arabic: six different forms!

**❌ Bad:**
```javascript
const text = count === 1 ? 'message' : 'messages';
// Only works for English
```

**✅ Good:**
```javascript
// Use ICU MessageFormat or i18next plural syntax
const text = t('message', { count });

// Translation file (i18next):
{
  "message_one": "{{count}} message",
  "message_other": "{{count}} messages"
}

// Or ICU MessageFormat:
{
  "message": "{count, plural, =0{no messages} =1{one message} other{# messages}}"
}
```

### 3. Handle Gender and Context

**Some languages require gender agreement:**

```javascript
// ICU MessageFormat with gender support
{
  "welcomeUser": "{gender, select, male{Welcome, Mr. {name}} female{Welcome, Ms. {name}} other{Welcome, {name}}}"
}
```

**French example:**
```json
{
  "connected": "{gender, select, male{Connecté} female{Connectée} other{Connecté·e}}"
}
```

### 4. Keep Strings Complete

**❌ Bad:**
```javascript
// Split string - translator can't see full context
<p>{t('errors.prefix')} {errorMessage} {t('errors.suffix')}</p>
```

**✅ Good:**
```javascript
// Complete string with placeholder
<p>{t('errors.message', { error: errorMessage })}</p>
// "An error occurred: {{error}}. Please try again."
```

### 5. Avoid String Reuse When Context Differs

**Problem:**
The word "Save" means different things:
- Save a file: "Enregistrer"
- Save money: "Économiser"
- Save for later: "Sauvegarder"

**❌ Bad:**
```json
{
  "save": "Save" // Used everywhere
}
```

**✅ Good:**
```json
{
  "file.save": "Save",          // "Enregistrer"
  "cart.saveForLater": "Save",  // "Sauvegarder"
  "pricing.savings": "Save"     // "Économiser"
}
```

## Locale-Specific Formatting

### Date & Time Formatting

**Use native Intl API or libraries (date-fns, moment.js with locales):**

```javascript
// ❌ Bad: Hardcoded format
const date = '12/31/2024'; // Ambiguous: MM/DD or DD/MM?

// ✅ Good: Locale-aware
const date = new Intl.DateTimeFormat(locale, {
  year: 'numeric',
  month: 'long',
  day: 'numeric'
}).format(new Date());

// Results:
// en-US: "December 31, 2024"
// fr-FR: "31 décembre 2024"
// fr-CA: "31 décembre 2024"
```

**Common date formats by locale:**
- `en-US`: MM/DD/YYYY (12/31/2024)
- `en-GB`: DD/MM/YYYY (31/12/2024)
- `fr-FR`: DD/MM/YYYY (31/12/2024)
- `fr-CA`: YYYY-MM-DD (2024-12-31) - ISO 8601 preferred
- `de-DE`: DD.MM.YYYY (31.12.2024)
- `ja-JP`: YYYY年MM月DD日 (2024年12月31日)

**Time formats:**
- `en-US`: 12-hour (11:30 PM)
- `fr-FR`: 24-hour (23:30)
- `fr-CA`: 24-hour (23 h 30)

### Number & Currency Formatting

**Numbers:**
```javascript
// ❌ Bad: Hardcoded
const price = "1,234.56";

// ✅ Good: Locale-aware
const price = new Intl.NumberFormat(locale, {
  minimumFractionDigits: 2
}).format(1234.56);

// Results:
// en-US: "1,234.56"
// fr-FR: "1 234,56"
// de-DE: "1.234,56"
```

**Currency:**
```javascript
const price = new Intl.NumberFormat(locale, {
  style: 'currency',
  currency: currencyCode
}).format(1234.56);

// Results:
// en-US, USD: "$1,234.56"
// fr-FR, EUR: "1 234,56 €"
// fr-CA, CAD: "1 234,56 $"
```

**Key locale differences:**
- Decimal separator: `.` (US/UK) vs `,` (FR/DE)
- Thousands separator: `,` (US) vs ` ` (FR) vs `.` (DE)
- Currency position: before (US) vs after (FR)
- Currency symbol spacing: no space (US) vs space (FR)

### Relative Time

```javascript
// "2 hours ago", "in 3 days"
const rtf = new Intl.RelativeTimeFormat(locale, { numeric: 'auto' });

rtf.format(-2, 'hour');
// en-US: "2 hours ago"
// fr-FR: "il y a 2 heures"
```

### Units & Measurements

**Use `Intl.NumberFormat` with units:**
```javascript
const distance = new Intl.NumberFormat(locale, {
  style: 'unit',
  unit: 'kilometer'
}).format(42);

// en-US: "42 km" (if not converted to miles)
// fr-FR: "42 km"
```

**Remember:**
- US uses imperial (miles, pounds, Fahrenheit)
- Most of world uses metric (kilometers, kilograms, Celsius)
- Convert values appropriately for locale

## Translation Workflow

### 1. Development Phase

```
Developer writes feature
       ↓
Add strings with keys to code
       ↓
Extract strings to source file (en.json)
       ↓
Add context/comments for translators
       ↓
Continue development
```

### 2. Translation Phase

```
Source file ready
       ↓
Upload to TMS (Translation Management System)
       ↓
Assign to translators
       ↓
Translators translate with context
       ↓
Review by native speakers
       ↓
Download translated files
```

### 3. Integration Phase

```
Import translated files
       ↓
Test in UI (check for overflow, errors)
       ↓
QA by native speakers
       ↓
Fix issues
       ↓
Deploy
```

### Translation Management Systems (TMS)

**Popular options:**
- **Lokalise** - Developer-friendly, good integrations
- **Crowdin** - Good for open source, community translations
- **Phrase** - Enterprise-focused
- **POEditor** - Simple, affordable
- **Transifex** - Good for continuous localization

**Features to look for:**
- Integration with your repo (GitHub, GitLab)
- Context screenshots
- Translation memory (reuse past translations)
- Glossaries and style guides
- Plural/variable support
- Quality checks (missing placeholders, etc.)
- Collaboration features

### Continuous Localization

**For agile teams:**
1. New strings added to code
2. Automated extraction to TMS (CI/CD)
3. Translators notified automatically
4. Translations reviewed
5. Automated import back to repo
6. QA testing
7. Deploy

**Benefits:**
- Always up-to-date translations
- No translation debt
- Faster time to market

## Quality Assurance

### Automated Checks

**Implement pre-commit hooks or CI checks:**

```javascript
// Check all keys have translations
function checkMissingTranslations(locales) {
  const sourceKeys = getKeys('en.json');
  locales.forEach(locale => {
    const targetKeys = getKeys(`${locale}.json`);
    const missing = sourceKeys.filter(k => !targetKeys.includes(k));
    if (missing.length > 0) {
      throw new Error(`Missing translations in ${locale}: ${missing}`);
    }
  });
}

// Check for unused keys
function checkUnusedKeys() {
  const keysInCode = extractKeysFromCode();
  const keysInFile = getKeys('en.json');
  const unused = keysInFile.filter(k => !keysInCode.includes(k));
  if (unused.length > 0) {
    console.warn(`Unused keys: ${unused}`);
  }
}

// Check for placeholder mismatches
function checkPlaceholders(source, target) {
  const sourcePlaceholders = extractPlaceholders(source);
  const targetPlaceholders = extractPlaceholders(target);
  return sourcePlaceholders.every(p => targetPlaceholders.includes(p));
}
```

### Manual QA Checklist

**For each locale:**
- [ ] All strings translated (no English fallbacks shown)
- [ ] Placeholders work correctly (names, numbers, dates)
- [ ] Pluralization works (test with 0, 1, 2, many)
- [ ] Text fits in UI (no overflow or truncation)
- [ ] Date/time formats correct for locale
- [ ] Number/currency formats correct for locale
- [ ] No encoding issues (special characters display correctly)
- [ ] RTL layout correct (if applicable)
- [ ] Navigation/buttons in correct language
- [ ] Error messages helpful and correct
- [ ] Consistent terminology throughout
- [ ] Appropriate formality level
- [ ] Cultural appropriateness verified

### Pseudo-Localization

**During development, test with pseudo-localized strings:**

```javascript
// Pseudo-localization transforms English:
"Hello" → "[ĤéļļÕ··]"

// Benefits:
// - Spots untranslated strings (will show in English)
// - Tests text expansion (~30% longer)
// - Tests encoding (accented characters)
// - Tests for concatenation issues
```

**Generate pseudo-localized strings:**
- Add accents to letters
- Expand length by ~30%
- Add brackets to see truncation
- Include special characters

### Testing with Real Users

**Beta testing:**
- Recruit native speakers from target markets
- Have them use the product in their language
- Collect feedback on:
  - Translation quality and naturalness
  - Cultural appropriateness
  - Any confusion or unclear wording
  - Missing translations or fallbacks

## Common Pitfalls

### 1. Hardcoded Strings

**Problem:** Text in code instead of translation files

```javascript
// ❌ Bad
<button>Sign in</button>

// ✅ Good
<button>{t('auth.signIn.button')}</button>
```

### 2. String Concatenation

**Problem:** Building sentences from parts

```javascript
// ❌ Bad
const msg = t('you.have') + ' ' + count + ' ' + t('new.messages');
// Word order varies! French: "Vous avez 5 nouveaux messages"

// ✅ Good
const msg = t('inbox.messageCount', { count });
```

### 3. Ignoring Text Expansion

**Problem:** UI designed for English, breaks with longer languages

**Text expansion by language (average):**
- German: +30%
- French: +15-25%
- Spanish: +15-30%
- Italian: +15-25%
- Portuguese: +15-30%

**Solutions:**
- Design flexible layouts (CSS flexbox/grid)
- Test with longest language
- Set max-widths and overflow handling
- Consider shorter translations for tight spaces

### 4. Assuming English Grammar

**Problems:**
- Pluralization (varies by language)
- Gender agreement (not in English, critical in Romance languages)
- Word order (varies significantly)
- Articles (English has "the", many languages have multiple)

**Solution:** Use ICU MessageFormat or similar for complex strings

### 5. Not Handling Missing Translations Gracefully

**Problem:** App crashes or shows keys instead of text

**✅ Good fallback strategy:**
1. Try exact locale: `fr-CA`
2. Try language: `fr`
3. Fallback to default: `en`
4. Show key as last resort: `[auth.signIn.button]`
5. Log missing translations for fixing

### 6. Embedding Formatting in Translations

**❌ Bad:**
```json
{
  "welcome": "<strong>Welcome</strong> to our app!"
}
// HTML in translation file - hard to maintain
```

**✅ Good:**
```javascript
<p>
  <strong>{t('welcome.greeting')}</strong> {t('welcome.message')}
</p>
```

### 7. Translating Technical Terms Unnecessarily

**Problem:** Some terms are universal and shouldn't be translated

**Keep in English (usually):**
- Brand names: "iPhone", "Google"
- Technical acronyms: "HTTP", "API", "CSS"
- Universal terms: "email" (though "courriel" in Quebec!), "WiFi"

**Translate:**
- UI actions and labels
- Error messages
- Help text
- Feature names (usually)

### 8. Not Considering Cultural Differences

**Examples:**
- Colors: White = purity (West), death (East)
- Gestures: Thumbs up offensive in some cultures
- Images: People, clothing, food vary by culture
- Symbols: Check mark vs different symbols
- Dates: Week starts Sunday vs Monday

## Cultural Adaptation

### Beyond Translation: Transcreation

**When to transcreate (not just translate):**
- Marketing copy and slogans
- Humor and wordplay
- Cultural references
- Metaphors and idioms
- Brand voice and personality

**Example:**
```
English slogan: "Think different"
French literal: "Pensez différemment" (loses impact)
Transcreated: "Pensez autrement" (captures spirit)
```

### Cultural Considerations by Element

**Images:**
- People: Diverse representation appropriate for market
- Gestures: Avoid potentially offensive gestures
- Clothing: Culturally appropriate dress
- Food: Relevant to local cuisine
- Settings: Recognizable environments

**Colors:**
- Red: Love (West), luck (China), danger (universal)
- White: Purity (West), death (East Asia)
- Green: Nature (universal), Islam (Middle East)
- Research color meanings in target culture

**Examples:**
- Use local currency symbols in examples
- Use local names in sample data
- Use local phone number formats
- Use local address formats
- Reference local holidays, not just Western ones

**Tone:**
- Formal vs informal varies by culture
- Directness: US direct, Japan indirect
- Humor: Varies wildly, test carefully
- Time: Some cultures more time-conscious than others

### Regional Variants

**When to create separate variants:**
- Significant terminology differences (en-US vs en-GB, fr-CA vs fr-FR)
- Different regulatory requirements
- Cultural sensitivities differ
- Different market expectations

**When one translation works:**
- Minor differences only
- Budget/resource constraints
- Small user base in one region
- Use neutral terminology that works everywhere

## Compliance & Regulations

### Quebec (Canada)

**Law 101 (Charter of the French Language):**
- French must be default for Quebec users
- French version must be equal or superior quality to English
- Interface must be fully available in French
- French trademarks must be used if they exist

**Law 25 (Privacy):**
- Privacy policies must be in French
- Consent forms must be in French
- Data breach notifications must be in French

**OQLF (Office québécois de la langue française):**
- Enforces French language requirements
- Maintains official terminology database
- Provides guidelines for software
- Can fine companies for non-compliance

**Implementation:**
```javascript
// Detect Quebec users and set French as default
if (userRegion === 'QC' || userIP inQuebec) {
  defaultLocale = 'fr-CA';
}
```

### European Union

**GDPR (General Data Protection Regulation):**
- Privacy policies must be in user's language
- Consent must be informed (user's language)
- Right to access data in user's language

**Accessibility:**
- Web Content Accessibility Guidelines (WCAG)
- Ensure translations work with screen readers
- Provide language alternatives

### Other Regulations

**US (Federal level):**
- No federal language requirement
- ADA requires accessibility, including language access for some services
- Some states have language access requirements

**Switzerland:**
- Officially multilingual (German, French, Italian, Romansh)
- Federal services must be in all official languages

**Belgium:**
- Three official languages (Dutch, French, German)
- Regional requirements vary

**China:**
- Websites must be in Simplified Chinese
- Cybersecurity laws require data localization
- Content censorship regulations

## Checklist: i18n Readiness

**Before launching in a new locale:**

**Technical:**
- [ ] All strings externalized
- [ ] Translation files complete
- [ ] Placeholders work correctly
- [ ] Pluralization implemented
- [ ] Date/time formatting locale-aware
- [ ] Number/currency formatting locale-aware
- [ ] Language selector implemented and works
- [ ] Fallback strategy in place
- [ ] No hardcoded strings
- [ ] No string concatenation
- [ ] Text expansion handled
- [ ] RTL support if needed

**Content:**
- [ ] All UI strings translated
- [ ] Help documentation translated
- [ ] Error messages translated
- [ ] Email templates translated
- [ ] Legal pages translated (terms, privacy)
- [ ] Marketing pages translated
- [ ] Consistent terminology
- [ ] Appropriate formality level
- [ ] Cultural adaptation done

**Quality:**
- [ ] Native speaker review completed
- [ ] QA testing in target language
- [ ] UI tested with actual translations
- [ ] No overflow or truncation
- [ ] Placeholders work correctly
- [ ] Date/time display correctly
- [ ] Numbers/currency display correctly
- [ ] Images culturally appropriate
- [ ] Colors culturally appropriate

**Compliance:**
- [ ] Regulatory requirements met
- [ ] Privacy policy in target language
- [ ] Terms of service in target language
- [ ] Accessibility requirements met
- [ ] Default language set correctly (Quebec!)
- [ ] Language switching accessible

**Business:**
- [ ] Local payment methods supported
- [ ] Local currency supported
- [ ] Customer support in target language
- [ ] Marketing materials ready
- [ ] Local partnerships in place (if applicable)
- [ ] Legal entity if required

## Resources & Tools

### i18n Libraries & Frameworks
- react-i18next, vue-i18n, angular-i18n
- FormatJS (React Intl)
- i18next (framework-agnostic)
- ICU MessageFormat

### Translation Management
- Lokalise, Crowdin, Phrase, POEditor
- Google Translate API (machine translation)
- DeepL API (better quality machine translation)

### Testing Tools
- Pseudo-localization tools
- BrowserStack (test in different locales)
- Accessibility checkers

### Standards & Guidelines
- Unicode CLDR (Common Locale Data Repository)
- ICU (International Components for Unicode)
- W3C Internationalization Guidelines
- ISO 639 (language codes)
- ISO 3166 (country codes)

### Learning Resources
- W3C i18n Tutorial
- Mozilla i18n Guide
- Phrase Localization Blog
- r/localization (Reddit)

---

**Remember:** Good i18n is about more than just translation - it's about creating an authentic experience for users in every market you serve.
