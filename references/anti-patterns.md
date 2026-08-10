# Anti-patterns

These are warning signs, not universal bans. Each can be justified by context; the burden is to explain the benefit.

## Product/IA

### Component-first design
Starting from “add cards, chart, tabs” before defining the task.

**Why it fails:** structure becomes a reflection of UI primitives rather than user intent.

### Dashboard syndrome
Adding KPI cards and charts because the surface is called a dashboard.

**Exception:** users genuinely need cross-cutting monitoring/decision signals.

### Internal-language IA
Navigation mirrors database/services/team names.

**Fix:** use user concepts and task vocabulary.

## Layout and visual hierarchy

### Card soup
Every section is a rounded bordered/shadowed card, often nested.

**Why it fails:** enclosure loses meaning and creates visual noise.

### Pillification
Unrelated controls/statuses/labels are all pills.

**Why it fails:** affordances and semantics blur together.

### Equal-emphasis actions
Primary, secondary, destructive, and rare actions all use prominent styling.

### Center-everything composition
Long-form or task-heavy content is centered regardless of scanning needs.

### Decoration as hierarchy
Gradients, glows, shadows, and badges compensate for weak structure.

### Arbitrary over-rounding
Every rectangle has a large radius independent of brand, density, or nesting.

## Interaction

### Overflow burial
Frequent/critical actions hidden in kebab menus to make the UI look clean.

### Modal reflex
Every create/edit/confirm flow becomes a dialog.

### Confirmation fatigue
Harmless reversible actions trigger confirmation dialogs.

### Accordion camouflage
Important content is hidden because the page looked too long.

### Icon guessing game
Unfamiliar icon-only controls with no visible/accessibility support.

### Drag-only essential action
No keyboard/tap alternative.

## Forms

### Placeholder labels
The label disappears when users type.

### Premature errors
An error appears while a user is still entering a plausible value.

### Split-field tax
Phone/card/date/name/etc. split into multiple fields without task benefit.

### “Invalid input”
Error does not say what is wrong or how to recover.

### Data-loss retry
Server failure clears valid user input.

## States

### Empty/error conflation
Failure to load is rendered as “Nothing here yet.”

### Spinner everywhere
Tiny async actions block whole screens.

### Toast as permanent truth
Important errors/conditions live only in a disappearing toast.

### Invisible remote update
Critical state changes somewhere outside current attention.

## Responsive

### Shrunken desktop
Same composition compressed until everything is tiny.

### Silent feature removal
Controls/columns disappear at narrow widths without equivalent access.

### Breakpoints by folklore
Layout changes at standard device widths instead of actual content failure.

### Disabled zoom
Prevents users from magnifying content.

## Accessibility

### Div-button
Clickable `div` replaces native control without complete semantics/keyboard behavior.

### Color-only meaning
Status is understandable only from red/green/etc.

### Focus erasure
Focus outline removed without an accessible replacement.

### Visual/source order divergence
CSS reorders content while keyboard/screen-reader sequence remains confusing.

## Motion

### Choreography tax
Users must wait for decorative transitions.

### Motion without reduced mode
Large/looping/panning/scaling animation ignores user preference.

## AI-specific failure modes

### Template convergence
The model defaults to familiar generated aesthetics without connecting them to product character.

### Fake product evidence
Invented testimonials, metrics, analytics, “user research,” or performance claims used to justify design.

### Screenshot-only completeness
Produces a beautiful populated state while loading, errors, keyboard, overflow, and responsive behavior are absent.

### Framework-default masquerading as design
A component library's defaults are assembled without hierarchy, product character, or task reasoning.

### Overcorrection against common patterns
Avoids familiar fonts/cards/sidebars solely to appear original, damaging usability.
