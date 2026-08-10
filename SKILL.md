---
name: frontend-design
description: Design, implement, review, and refine high-quality web and mobile frontends using evidence-backed UX, information architecture, interaction design, accessibility, responsive behavior, visual hierarchy, and coherent visual systems. Use for product screens, dashboards, forms, onboarding, navigation, landing pages, design systems, redesigns, and visual/UX audits. Requires context-first design, explicit UI states, implementation-aware decisions, and a rendered critique-and-fix pass when rendering tools are available.
compatibility: Agent Skills open standard; intended for Codex and portable to compatible agents.
metadata:
  version: "0.1.0"
  research-date: "2026-08-10"
  minimum-source-corpus: "75"
---

# Frontend Design

Build interfaces that are useful before they are beautiful, understandable before they are clever, and coherent before they are distinctive.

This skill is a decision process, not an aesthetic preset. Do not blindly reproduce any visual trend, design system, example product, or rule from this repository. Resolve conflicts using product context, user evidence, platform conventions, accessibility requirements, and the hierarchy in **Evidence and conflict resolution** below.

## Core operating rule

Never jump directly from a feature request to JSX/CSS/UI code when the task materially involves design.

Use this loop:

`context -> task model -> information architecture -> interaction model -> visual system -> states -> implementation -> render -> critique -> fix`

For a tiny local change, compress the loop. For a new screen, flow, redesign, or product surface, execute it explicitly.

## 1. Establish context

Before choosing layout or styling, determine what is actually known.

Capture, explicitly or internally:

- **User:** who uses this surface, including expertise and likely constraints.
- **Job:** the concrete task they came to accomplish.
- **Outcome:** what successful completion means.
- **Frequency:** one-off, occasional, or repeated expert workflow.
- **Risk:** cost of a mistake; higher risk requires stronger confirmation, explanation, and reversibility.
- **Environment:** web/mobile/native, device sizes, input methods, likely connectivity, language, and platform conventions.
- **Product state:** new surface, existing design system, legacy constraints, or deliberate redesign.
- **Evidence:** supplied research, analytics, screenshots, codebase conventions, user statements, or only inference.

Do not invent personas, research findings, conversion data, or user needs. Label meaningful assumptions as assumptions.

For existing products, inspect the existing implementation and design language before changing them. Preserve established conventions unless the task is a redesign or a convention is demonstrably harmful.

Read `references/01-product-context.md` when the product purpose or user is not trivial.

## 2. Model the task before the screen

Define the smallest complete flow that lets the user finish the job.

Identify:

1. Entry condition.
2. Primary task.
3. Required information and decisions.
4. Completion condition.
5. Recovery routes.

Account for relevant alternate states before implementation:

- empty / first-use,
- loading / refreshing,
- partial data,
- success,
- validation error,
- system/server error,
- permission denied,
- destructive confirmation,
- offline / reconnecting when applicable,
- stale/conflicting data when applicable.

A screen is not complete if its happy path is the only designed state.

Read `references/02-information-architecture.md`, `references/03-interaction-and-flows.md`, and `references/09-states-feedback-errors.md` for non-trivial flows.

## 3. Build the information hierarchy

The hierarchy must reflect user importance, not backend structure.

For each screen, decide:

- What must be understood first?
- What action is primary now?
- What information is supporting context?
- What can be deferred, collapsed, or moved to a secondary surface?
- What should not exist at all?

Use user-facing language. Prefer recognition to recall. Keep labels stable across screens.

For task-focused screens, make the next meaningful action obvious without turning every action into a prominent button. Destructive, secondary, and rare actions should not compete visually with the primary task.

Do not create a dashboard, card, tab, modal, dropdown, accordion, sidebar, or wizard merely because that pattern is common. Choose it because it reduces complexity for this content and task.

## 4. Choose interaction patterns deliberately

Prefer familiar platform controls and native semantics when they solve the problem.

Before introducing a pattern, ask what cost it creates:

- **Dropdown/select:** hides choices and increases interaction cost; use when the option set or space tradeoff justifies it.
- **Accordion/disclosure:** reduces visible complexity but lowers discoverability; do not hide critical or frequently needed content.
- **Modal/dialog:** interrupts context; reserve for focused, bounded tasks that benefit from blocking the background.
- **Tabs:** use for peer sections within one context, not arbitrary navigation or sequential steps.
- **Wizard:** use when sequencing genuinely reduces complexity or dependencies exist between steps.
- **Infinite scroll:** avoid when users need orientation, comparison, return-to-position, or a sense of completion.
- **Drag and drop:** never make dragging the sole method for an essential operation.
- **Icon-only action:** require a highly familiar symbol or an accessible label/tool tip; add visible text when interpretation risk is meaningful.

Read `references/08-navigation-and-disclosure.md` and `references/07-forms-and-input.md`.

## 5. Define a visual system before decorating

Visual design must communicate structure and brand character, not merely make the screenshot busier.

Define a small coherent system:

- type roles and hierarchy,
- spacing rhythm,
- content width and density,
- color roles,
- surfaces and boundaries,
- corner-radius policy,
- elevation/shadow policy,
- icon style,
- motion language,
- responsive behavior.

Use design tokens or existing theme primitives instead of scattered magic values when the codebase supports them.

### Visual hierarchy rules

- Create a small number of clearly differentiated emphasis levels.
- Use proximity and spacing to express relationships before adding borders or containers.
- Use contrast intentionally; do not make everything loud.
- Prefer alignment and rhythm over decorative separators.
- Keep text line lengths readable; do not stretch prose across large screens.
- Avoid nested containers and “card soup.” A card needs a semantic grouping reason.
- Avoid indiscriminate rounded rectangles. Shape should communicate grouping, affordance, or brand language.
- Do not center all content by default. Alignment should serve scanning and content structure.
- Distinctiveness should come from coherent typography, composition, color, imagery, content, and interaction—not random novelty.

There is no forbidden font, radius, gradient, or layout. Generic output is a consequence of unexamined defaults, not the mere presence of a particular primitive.

Read `references/04-visual-hierarchy.md`, `references/05-typography-and-spacing.md`, `references/06-color-and-tokens.md`, and `references/16-craft-and-polish.md`.

## 6. Make forms low-friction and recoverable

For forms:

- Ask only for information needed now.
- Prefer fewer fields over artificially fewer steps.
- Use persistent visible labels; placeholders are examples/hints, not labels.
- Group fields by meaning and task sequence.
- Use the correct input type, autocomplete, keyboard/input mode, and semantic element.
- Mark optional/required status consistently and unambiguously.
- Avoid splitting one conceptual value into multiple fields without a concrete reason.
- Validate at a useful time: not so early that users are scolded while typing, not so late that recovery becomes expensive.
- Put actionable error guidance next to the problem; for long forms, also provide an error summary that links/focuses to invalid fields.
- Preserve entered data after recoverable failures.
- Make success and next steps explicit.

Read `references/07-forms-and-input.md`.

## 7. Design states and system feedback

Every user action that changes state needs perceivable feedback.

Use the least intrusive feedback that remains clear:

- immediate visual state change for near-instant actions,
- local pending state for short asynchronous actions,
- skeleton/loading structure when it helps users anticipate content,
- determinate progress when progress can be meaningfully measured,
- non-blocking transient confirmation for low-risk completed actions,
- persistent inline/banner guidance for states that remain relevant,
- modal interruption only when the user must resolve something before continuing.

Never use a spinner, toast, banner, or modal as a reflex. Match feedback scope to the scope and persistence of the state.

Empty states must distinguish at least when relevant:

- no data exists yet,
- filters/search produce no matches,
- data cannot be loaded,
- user lacks permission.

Read `references/09-states-feedback-errors.md`.

## 8. Treat responsive design as re-composition

Do not shrink desktop layouts into narrow screens.

At smaller widths:

- preserve task priority,
- reflow rather than crop or hide essential information,
- change grouping when the content requires it,
- keep controls reachable and sufficiently separated,
- avoid horizontal scrolling except where two-dimensional structure is essential,
- provide an alternative presentation for dense data when practical,
- do not encode instructions such as “on the left” when position changes responsively.

Choose breakpoints from content failure points, not from a remembered device list.

For touch-heavy interfaces, prefer comfortably large targets. WCAG 2.2 Level AA sets a 24×24 CSS-pixel minimum target-size rule with defined exceptions; use larger practical targets when density and context permit.

Read `references/10-mobile-responsive.md`.

## 9. Accessibility is a design constraint, not a finishing pass

At minimum, verify applicable requirements from `references/11-accessibility.md`:

- semantic structure and landmarks,
- programmatic labels and relationships,
- keyboard operation and logical focus order,
- visible focus,
- no focus traps outside intentional accessible modal behavior,
- contrast for text and meaningful non-text UI,
- information not encoded by color alone,
- target size/spacing,
- zoom/reflow,
- orientation flexibility unless essential,
- error identification and recovery,
- alternatives to drag/complex gestures,
- reduced-motion preference,
- accessible names for icon-only controls,
- dynamic status announcements where necessary.

Prefer native HTML controls over recreating their behavior unless a custom control provides necessary value and implements equivalent semantics and interaction.

## 10. Use motion to explain, not distract

Motion may communicate continuity, hierarchy, causality, feedback, or spatial relationships.

- Keep routine transitions subtle and fast enough not to impede repeated work.
- Avoid animation that competes with task content.
- Avoid large unnecessary scaling/panning motion.
- Respect reduced-motion preferences and provide a reduced experience rather than assuming all motion must remain.
- Never delay task completion for decorative choreography.

Read `references/12-motion.md`.

## 11. Implement the whole behavior

While coding:

- reuse existing components and tokens where they are suitable,
- keep component boundaries aligned to behavior and reuse, not arbitrary visual fragments,
- preserve semantic HTML and platform accessibility,
- avoid unnecessary state, duplicated derived state, and fake interactions,
- make responsive rules explicit,
- implement keyboard and focus behavior alongside pointer behavior,
- implement all relevant states identified earlier,
- keep motion and visual effects performance-conscious,
- do not add dependencies for trivial styling/behavior already supported by the stack.

For data-dense software, read `references/13-data-dense-ui.md`.
For design-system work, read `references/14-design-systems.md`.

## 12. Render, inspect, critique, fix

A code review is not a visual review.

When the available environment can render the interface:

1. Render the actual implementation.
2. Inspect at representative narrow and wide widths.
3. Exercise important states, not only pristine fixture data.
4. Inspect keyboard/focus behavior when applicable.
5. Compare the result against the task hierarchy and visual system.
6. Fix observed issues.
7. Re-render after meaningful fixes.

When rendering is impossible, say so and perform a code-level/design-spec audit instead. Do not pretend that unrendered UI has been visually verified.

Use `references/15-implementation-audit.md` and `references/audit-rubric.md`.

## Final critique gate

Before declaring a design complete, answer these questions:

### Comprehension
- Can the intended user understand the screen's purpose and current state within a few seconds?
- Is the most likely next action apparent?
- Are labels in the user's language rather than the implementation's language?

### Task and IA
- Does every visible section support the task, context, trust, or recovery?
- Is any important information hidden behind interaction for no good reason?
- Can anything be removed without harming the task?

### Interaction
- Are controls recognizable and predictable?
- Are destructive actions separated and recoverable where possible?
- Are loading, empty, error, success, disabled, and permission states handled where relevant?

### Visual hierarchy
- Can a user scan the page without reading every word?
- Are spacing, typography, alignment, and contrast doing most of the grouping work?
- Are there too many cards, borders, pills, shadows, icons, colors, or competing emphasis levels?
- Does the visual character fit the product instead of resembling a generic template?

### Responsive and accessibility
- Does the task survive narrow widths without loss of essential functionality?
- Is keyboard/focus behavior sane?
- Are labels, target sizes, contrast, semantics, motion preferences, and error recovery handled?

### Evidence
- Which decisions came from supplied evidence, standards, established product conventions, or inference?
- Is a heuristic being presented as if it were user research? If so, correct the claim.

Fix material failures before finishing.

## Evidence and conflict resolution

Use this priority order when guidance conflicts:

1. **Safety, law, and normative accessibility requirements.**
2. **Direct evidence about the actual users and task** (research, observed behavior, analytics interpreted carefully).
3. **Platform conventions and the product's established design system** when users benefit from consistency.
4. **High-quality domain research and tested patterns** applicable to the same task/context.
5. **General usability heuristics and cognitive principles.**
6. **Aesthetic conventions and stylistic preferences.**

Heuristic evaluation complements user research; it does not replace it. A polished interface can still be wrong for the user.

## Reference map

Load only the references needed for the task:

- `references/01-product-context.md` — jobs, context, evidence, product sense
- `references/02-information-architecture.md` — hierarchy, labels, navigation structure
- `references/03-interaction-and-flows.md` — task flows and interaction decisions
- `references/04-visual-hierarchy.md` — composition, grouping, hierarchy, anti-generic design
- `references/05-typography-and-spacing.md` — text systems, measure, rhythm, density
- `references/06-color-and-tokens.md` — semantic color, contrast, tokens, surfaces
- `references/07-forms-and-input.md` — forms, validation, inputs, field reduction
- `references/08-navigation-and-disclosure.md` — tabs, menus, accordions, modals, progressive disclosure
- `references/09-states-feedback-errors.md` — loading, empty, errors, success, feedback
- `references/10-mobile-responsive.md` — touch, reflow, mobile composition
- `references/11-accessibility.md` — WCAG-centered implementation and audit
- `references/12-motion.md` — motion purpose and reduced motion
- `references/13-data-dense-ui.md` — tables, dashboards, expert density
- `references/14-design-systems.md` — tokens, components, consistency, escape hatches
- `references/15-implementation-audit.md` — rendered inspection loop
- `references/16-craft-and-polish.md` — visual craft, pruning, optical polish, controlled distinctiveness
- `references/audit-rubric.md` — severity-weighted design audit
- `references/anti-patterns.md` — common failure modes and contextual exceptions
- `references/sources.md` — research corpus and provenance

The repository's reference material is synthesis, not a substitute for checking a current normative specification when exact conformance matters.
