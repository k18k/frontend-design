# Research corpus

Research snapshot: **2026-08-10**.

This corpus intentionally exceeds the requested minimum of 75 sources. Selection favors primary/normative standards, official platform guidance, established UX research, mature design systems, and concrete product case studies. Older design-system pages are retained only where they document a stable pattern clearly.

The summaries below are paraphrases used to derive design decisions; they are not quotations. A source's presence does not mean every recommendation is universal. Normative requirements, direct user evidence, platform conventions, and task context take precedence over generic heuristics.

## A. Agent-skill architecture and AI design context

- [S001] Agent Skills — Specification — https://agentskills.io/specification — Defines the portable skill folder model, required `SKILL.md`, and optional references/scripts/assets.
- [S002] OpenAI Academy — Using skills — https://academy.openai.com/public/clubs/work-users-ynjqu/resources/using-skills — Frames skills as reusable workflows with inputs, procedure, resources, and final checks.
- [S003] OpenAI Help — Skills in ChatGPT — https://help.openai.com/en/articles/20001070-skills-in-chatgpt — Confirms current OpenAI skill support and use of the Agent Skills standard.
- [S004] OpenAI Developers — Plugins in Codex — https://developers.openai.com/codex/plugins/ — Shows skills as distributable plugin capabilities in Codex.
- [S005] Anthropic Skills repository — https://github.com/anthropics/skills — Reference implementation of skills organized around a `SKILL.md` plus optional resources.
- [S006] Anthropic frontend-design skill — https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md — Useful benchmark for aesthetic-direction prompting, but not treated as a complete UX workflow.
- [S007] Anthropic knowledge-work-plugins frontend-design issue — https://github.com/anthropics/knowledge-work-plugins/issues/49 — Community discussion highlighting the difference between aesthetic guidance and broader frontend/product workflows.
- [S008] Nielsen Norman Group — UX-Context Design — https://www.nngroup.com/articles/ux-context-design/ — Argues that AI output quality depends heavily on curated UX context and on testing/refining that context.

## B. Usability, product thinking, IA, cognition, research — Nielsen Norman Group

- [S010] 10 Usability Heuristics for User Interface Design — https://www.nngroup.com/articles/ten-usability-heuristics/ — Visibility of status, real-world match, user control, consistency, prevention/recovery, recognition, efficiency, minimalist design, and help.
- [S011] How to Conduct a Heuristic Evaluation — https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/ — Heuristic review should be scoped and performed systematically; it complements rather than replaces user research.
- [S012] Usability Testing 101 — https://www.nngroup.com/articles/usability-testing-101/ — Direct observation uncovers behavior and usability problems that designer intuition cannot reliably predict.
- [S013] Why You Only Need to Test with 5 Users — https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ — Iterative small-sample testing can reveal major usability problems; not a universal sample-size rule for all research questions.
- [S014] User Journeys vs. User Flows — https://www.nngroup.com/articles/user-journeys-vs-user-flows/ — Distinguishes broad cross-channel journeys from concrete task-level interface flows.
- [S015] Empathy Mapping: The First Step in Design Thinking — https://www.nngroup.com/articles/empathy-mapping/ — Structures known/assumed user context while making knowledge gaps visible.
- [S016] Journey Mapping 101 — https://www.nngroup.com/articles/journey-mapping-101/ — Maps actors, scenarios, phases, actions, thoughts, emotions, and opportunities across a journey.
- [S017] When to Use Which User-Experience Research Methods — https://www.nngroup.com/articles/which-ux-research-methods/ — Select methods based on attitudinal/behavioral and qualitative/quantitative questions rather than using one research method for everything.
- [S018] Service Blueprints: Definition — https://www.nngroup.com/articles/service-blueprints-definition/ — Connects visible user experience with backstage processes and dependencies.
- [S019] Design Thinking 101 — https://www.nngroup.com/articles/design-thinking/ — Promotes iterative framing, ideation, prototyping, and testing rather than linear solution-first work.
- [S020] User Interviews: How, When, and Why to Conduct Them — https://www.nngroup.com/articles/user-interviews/ — Interviews are useful for attitudes and mental models but not substitutes for observing actual task behavior.
- [S021] Usability 101: Introduction to Usability — https://www.nngroup.com/articles/usability-101-introduction-to-usability/ — Establishes learnability, efficiency, memorability, errors, and satisfaction as distinct usability dimensions.
- [S022] Affinity Diagramming for Collaboratively Sorting UX Findings and Design Ideas — https://www.nngroup.com/articles/affinity-diagram/ — Supports synthesis of qualitative findings into themes without prematurely imposing a solution structure.
- [S023] UX Research Cheat Sheet — https://www.nngroup.com/articles/ux-research-cheat-sheet/ — Broad map of research methods across product-development stages.
- [S024] How Might We Questions — https://www.nngroup.com/articles/how-might-we-questions/ — Useful reframing technique when moving from research insight to solution space.
- [S025] Product Sense: What It Is and How to Develop It — https://www.nngroup.com/articles/product-sense-definition/ — Connects user value, business/product context, judgment, and evidence rather than treating design as visual styling.
- [S026] Dropdowns: Design Guidelines — https://www.nngroup.com/articles/dropdown-list/ — Dropdowns hide options and add interaction cost; visible alternatives can be better for small important sets.
- [S027] Accordions on Desktop: When and How to Use — https://www.nngroup.com/articles/accordions-on-desktop/ — Progressive disclosure reduces clutter but harms discoverability when critical content is hidden.
- [S028] Skeleton Screens 101 — https://www.nngroup.com/articles/skeleton-screens/ — Loading treatment should match wait duration and content predictability; skeletons can communicate upcoming structure.
- [S029] Card Sorting: Uncover Users' Mental Models for Better Information Architecture — https://www.nngroup.com/articles/card-sorting-definition/ — Card sorting can inform grouping/labels but must be synthesized with tasks and product constraints.
- [S030] 4 Principles for Reducing Cognitive Load in UI Design — https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/ — Remove unnecessary information, reduce unnecessary choices, use familiar patterns, and externalize memory where possible.
- [S031] Mental Models — https://www.nngroup.com/articles/mental-models/ — Interfaces are easier when conceptual models align with how users expect the domain/system to behave.
- [S032] Psychology for UX: Study Guide — https://www.nngroup.com/articles/psychology-study-guide/ — Consolidates cognitive/perceptual concepts relevant to interaction design while cautioning against simplistic “laws.”
- [S033] Change Blindness in UX — https://www.nngroup.com/articles/change-blindness/ — Users can miss even substantial state changes when attention is elsewhere; feedback placement matters.
- [S034] The Theory of User Delight — https://www.nngroup.com/articles/theory-user-delight/ — Delight should rest on functional, reliable, and usable foundations rather than compensate for broken basics.
- [S035] Principles of Visual Design — https://www.nngroup.com/articles/principles-visual-design/ — Scale, hierarchy, balance, contrast, and Gestalt principles are functional tools for directing attention and grouping.
- [S036] Form Design: Placeholders Are Not Labels — https://www.nngroup.com/articles/form-design-placeholders/ — Persistent labels reduce memory burden and preserve context while entering data.
- [S037] Error-Message Guidelines — https://www.nngroup.com/articles/error-message-guidelines/ — Errors should be visible, understandable, specific, constructive, and positioned near the problem.
- [S038] Indicators, Validations, and Notifications: Pick the Correct Communication Option — https://www.nngroup.com/articles/indicators-validations-notifications/ — System feedback should use a pattern whose scope and persistence fit the message.
- [S039] Website Response Times — https://www.nngroup.com/articles/website-response-times/ — Response latency changes perceived continuity and the need for explicit progress/status feedback.
- [S040] Information Scent: How Users Decide Where to Go Next — https://www.nngroup.com/articles/information-scent/ — Link/navigation cues should let users predict whether a path is likely to contain their goal.
- [S041] Horizontal Attention Leans Left — https://www.nngroup.com/articles/horizontal-attention-leans-left/ — Scanning behavior can influence placement, but locale, layout, and task context remain relevant.
- [S042] Legibility, Readability, and Comprehension: Making Users Read Your Words — https://www.nngroup.com/articles/legibility-readability-comprehension/ — Typography must first enable perception and comprehension; visual style cannot compensate for unreadable text.
- [S043] How Users Read on the Web — https://www.nngroup.com/articles/how-users-read-on-the-web/ — Web content is commonly scanned, supporting clear headings, front-loaded wording, and visible hierarchy.
- [S044] Paper Prototyping: Getting User Data Before You Code — https://www.nngroup.com/articles/mozilla-paper-prototype/ — Low-cost prototypes support early iteration before implementation hardens decisions.

## C. Forms, checkout, mobile input — Baymard Institute

- [S045] Current State of Checkout UX — https://baymard.com/blog/current-state-of-checkout-ux — Large-scale benchmark showing persistent checkout usability problems despite mature patterns.
- [S046] Checkout Flow: Average Form Fields — https://baymard.com/blog/checkout-flow-average-form-fields — Field count and entry burden matter more than merely minimizing the number of pages/steps.
- [S047] Mobile Commerce Design: 50+ UX Guidelines — https://baymard.com/blog/mobile-commerce-design — Mobile commerce needs deliberate touch, layout, navigation, form, and interruption handling.
- [S048] Checkout Flow UX Optimization — https://baymard.com/learn/checkout-flow-ux-optimization — Consolidates checkout principles around reducing friction and uncertainty.
- [S049] Mobile Checkout: 11 Common UX Pitfalls — https://baymard.com/blog/mobile-checkout — Mobile checkout amplifies input, keyboard, and viewport friction.
- [S050] Payment UX — https://baymard.com/learn/payment-ux — Payment interfaces need trust, clarity, input assistance, and recovery appropriate to high-stakes actions.
- [S051] One-Page Checkout: 6 UX Requirements — https://baymard.com/blog/one-page-checkout — A single page is not automatically simpler; sectioning, dependencies, and error handling matter.
- [S052] Marking Required and Optional Fields — https://baymard.com/blog/required-optional-form-fields — Required/optional status must be communicated consistently and unambiguously.
- [S053] Checkout UX 2024 Research Update — https://baymard.com/blog/checkout-2024-launch — Updated empirical benchmark for checkout flows and recurring failure patterns.
- [S054] Checkout Usability Research — https://baymard.com/research/checkout-usability — Research base behind checkout recommendations; use as domain evidence rather than universal UI law.
- [S055] Cart & Checkout UX Articles — https://baymard.com/blog/collections/cart-and-checkout — Collection used to cross-check repeated checkout/form findings.
- [S056] Mobile Form Usability: Place Labels Above Fields — https://baymard.com/blog/mobile-form-usability-label-position — Above-field labels generally support mobile scanning and avoid horizontal association problems.
- [S057] Mobile Form Usability: Avoid Splitting Single Input Entities — https://baymard.com/blog/mobile-form-usability-single-input-fields — Multiple fields for one conceptual value increase navigation and input effort unless there is a clear benefit.
- [S058] Form Design: 13 Empirical Guidelines — https://baymard.com/learn/form-design — Consolidates research-backed field, label, validation, and flow patterns.
- [S059] Checkout Optimization: From 16 Fields to 8 — https://baymard.com/blog/checkout-optimization-from-16-fields-to-8 — Demonstrates auditing whether requested data is genuinely needed and simplifying entry burden.
- [S060] Inline Form Validation — https://baymard.com/blog/inline-form-validation — Validation timing and message placement affect whether inline feedback helps or interrupts entry.

## D. Apple Human Interface Guidelines

- [S061] Apple Human Interface Guidelines — https://developer.apple.com/design/human-interface-guidelines — Platform-level foundation for Apple interface behavior and conventions.
- [S062] Design Principles — https://developer.apple.com/design/human-interface-guidelines/design-principles — Start with purpose, hierarchy, consistency, and platform-appropriate behavior rather than visual novelty alone.
- [S063] Layout — https://developer.apple.com/design/human-interface-guidelines/layout — Layout should adapt to device/context while preserving hierarchy and readability.
- [S064] Typography — https://developer.apple.com/design/human-interface-guidelines/typography — Type choices should preserve legibility, hierarchy, and Dynamic Type/platform behavior.
- [S065] Color — https://developer.apple.com/design/human-interface-guidelines/color — Use color semantically and maintain legibility across appearance modes and accessibility settings.
- [S066] Accessibility — https://developer.apple.com/design/human-interface-guidelines/accessibility — Accessibility is integrated into interaction, content, color, motion, and input decisions.
- [S067] Motion — https://developer.apple.com/design/human-interface-guidelines/motion — Motion should clarify state/relationships and respect user motion preferences.
- [S068] Inputs — https://developer.apple.com/design/human-interface-guidelines/inputs — Support platform input modalities and avoid assuming a single method of interaction.
- [S069] Menus — https://developer.apple.com/design/human-interface-guidelines/menus — Menus organize secondary actions; command labeling, hierarchy, and predictability matter.
- [S070] Sheets — https://developer.apple.com/design/human-interface-guidelines/sheets — Sheets are contextual modal surfaces and should be used for focused tasks.
- [S071] Lists and Tables — https://developer.apple.com/design/human-interface-guidelines/lists-and-tables — Repeated structured content should remain scannable, appropriately grouped, and interactive in platform-consistent ways.
- [S072] Pickers — https://developer.apple.com/design/human-interface-guidelines/pickers — Choice controls should fit option type/scale and platform conventions.
- [S073] Modality — https://developer.apple.com/design/human-interface-guidelines/modality — Modal experiences interrupt flow and should provide a clear benefit that justifies the interruption.
- [S074] Alerts — https://developer.apple.com/design/human-interface-guidelines/alerts — Alerts should be rare, specific, actionable, and reserved for information requiring immediate attention/decision.
- [S075] Onboarding — https://developer.apple.com/design/human-interface-guidelines/onboarding — Let people reach value quickly; teach in context and avoid unnecessary gates before use.

## E. Mature design systems and platform guidance

### Material Design 3

- [S076] Material Design 3 — https://m3.material.io/ — Current Material foundation for components, styles, layout, and adaptive/product expression.
- [S077] Material — Usability — https://m3.material.io/foundations/usability — Connects Material choices to perceivability, operability, clarity, and inclusive interaction.
- [S078] Material — Design Tokens — https://m3.material.io/foundations/design-tokens — Tokens encode reusable design decisions and enable coherent theming/system evolution.
- [S079] Material — Color Roles — https://m3.material.io/styles/color/roles — Semantic color roles separate meaning from raw palette values.
- [S080] Material — Applying Type — https://m3.material.io/styles/typography/applying-type — Type roles support visual hierarchy and consistent responsive text treatment.
- [S081] Material — Buttons — https://m3.material.io/components/buttons/overview — Button emphasis should correspond to action priority rather than style variety for its own sake.
- [S082] Material 2 — Understanding Typography — https://m2.material.io/design/typography/understanding-typography.html — Stable foundational treatment of readable typographic hierarchy and scale.

### GOV.UK Design System

- [S083] GOV.UK Design System — Components — https://design-system.service.gov.uk/components/ — Pragmatic accessible component patterns with explicit usage guidance.
- [S084] GOV.UK Design System — Patterns — https://design-system.service.gov.uk/patterns/ — Task-level patterns combine components into end-to-end interaction guidance.
- [S085] GOV.UK — Focus States — https://design-system.service.gov.uk/get-started/focus-states/ — Strong visible focus treatment is part of the system's interaction design, not optional polish.
- [S086] GOV.UK — Spacing — https://design-system.service.gov.uk/styles/spacing/ — A constrained spacing scale creates consistent relational rhythm.
- [S087] GOV.UK — Colour — https://design-system.service.gov.uk/styles/colour/ — Semantic palette usage and contrast considerations.
- [S088] GOV.UK — Layout — https://design-system.service.gov.uk/styles/layout/ — Mobile-first responsive layout and bounded text/content widths.
- [S089] GOV.UK — Type Scale — https://design-system.service.gov.uk/styles/type-scale/ — Small semantic type scale rather than arbitrary one-off sizes.
- [S090] GOV.UK — Error Message — https://design-system.service.gov.uk/components/error-message/ — Errors say what went wrong and how to fix it, located with the field.
- [S091] GOV.UK — Error Summary — https://design-system.service.gov.uk/components/error-summary/ — Long forms benefit from a focusable summary linking users to individual errors.
- [S092] GOV.UK — Validation Pattern — https://design-system.service.gov.uk/patterns/validation/ — Validation is a recovery flow involving message placement, focus, preserved data, and clear instructions.
- [S093] GOV.UK — Text Input — https://design-system.service.gov.uk/components/text-input/ — Input width/type/hints/errors should reflect expected data, not one generic field style.
- [S094] GOV.UK — Question Pages — https://design-system.service.gov.uk/patterns/question-pages/ — Ask focused questions, sequence them by dependency, and avoid unnecessary information collection.

### IBM Carbon

- [S095] Carbon — Data Table Usage — https://v10.carbondesignsystem.com/components/data-table/usage/ — Tables support comparison and operational work; density, actions, selection, and state need deliberate patterns.
- [S096] Carbon — Data Table Style — https://v10.carbondesignsystem.com/components/data-table/style/ — Table hierarchy depends on typography, spacing, row states, and alignment rather than enclosure alone.
- [S097] Carbon — Data Table Accessibility — https://v10.carbondesignsystem.com/components/data-table/accessibility/ — Keyboard/semantic behavior is part of the component contract.
- [S098] Carbon — Empty States Pattern — https://v10.carbondesignsystem.com/patterns/empty-states-pattern/ — Empty states differ by cause and should orient users toward the appropriate next step.
- [S099] Carbon — Loading Pattern — https://v10.carbondesignsystem.com/patterns/loading-pattern/ — Loading treatment should communicate system progress without unnecessarily blocking unrelated work.
- [S100] Carbon — Spacing Overview — https://v10.carbondesignsystem.com/guidelines/spacing/overview/ — Consistent spacing tokens communicate relationships and density.

### Atlassian Design System

- [S101] Atlassian Design — Foundations — https://atlassian.design/foundations — Mature foundation linking visual and interaction primitives across complex productivity software.
- [S102] Atlassian — Applying Typography — https://atlassian.design/foundations/typography/applying-typography — Semantic text roles and relative sizing improve consistency and accessibility.
- [S103] Atlassian — Spacing — https://atlassian.design/foundations/spacing — Spacing expresses grouping and hierarchy through a constrained scale.
- [S104] Atlassian — Accessibility — https://atlassian.design/foundations/accessibility — Accessibility requirements are embedded into foundations and components.
- [S105] Atlassian — Color — https://atlassian.design/foundations/color — Semantic color system supports state, themes, and accessible contrast.
- [S106] Atlassian — Design Tokens — https://atlassian.design/foundations/design-tokens — Tokens create a source of truth and decouple semantic roles from literal values.
- [S107] Atlassian — Elevation — https://atlassian.design/foundations/elevation — Elevation is a semantic layering signal rather than generic decoration.

### Microsoft Fluent 2

- [S108] Fluent 2 — Layout — https://fluent2.microsoft.design/layout — Proximity, spacing, alignment, and adaptation establish structure in productivity interfaces.
- [S109] Fluent 2 — Wait UX — https://fluent2.microsoft.design/wait-ux — Waiting experiences should communicate status accessibly and choose indicators according to duration/context.
- [S110] Fluent 2 — Tablist Usage — https://fluent2.microsoft.design/components/web/react/core/tablist/usage — Tabs are for related peer content and need clear selected/focus behavior.
- [S111] Fluent 2 — Breadcrumb Usage — https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage — Breadcrumbs are secondary hierarchical orientation, not a complete navigation replacement.
- [S112] Fluent 2 — Message Bar Usage — https://fluent2.microsoft.design/components/web/react/core/messagebar/usage — Persistent messages must be prioritized; too many simultaneous notices destroy salience.
- [S113] Fluent 2 — Combobox Usage — https://fluent2.microsoft.design/components/web/react/core/combobox/usage — Search/filterable choice controls are appropriate when option scale exceeds simple visible selection.

### U.S. Web Design System

- [S114] USWDS — Components Overview — https://designsystem.digital.gov/components/overview/ — Components target accessible, mobile-friendly government services and include explicit use guidance.
- [S115] USWDS — Form — https://designsystem.digital.gov/components/form/ — Favors straightforward vertical form structure, clear labels, and accessible grouping.
- [S116] USWDS — Accessibility — https://designsystem.digital.gov/documentation/accessibility/ — Accessibility requires implementation/testing beyond merely selecting compliant-looking components.
- [S117] USWDS — Patterns — https://designsystem.digital.gov/patterns/ — Patterns combine components, tokens, usability guidance, and task/user knowledge.
- [S118] USWDS — Validation — https://designsystem.digital.gov/components/validation/ — Validation feedback needs clear status and accessible semantics.

## F. Real-world design cases and specialist practitioner sources

- [S119] Google Design — Airbnb Invites You In — https://design.google/library/airbnb-invites-you-in — Case study on coherent typography, clearer text/icon choices, whitespace, imagery, and motion as a unified product language.
- [S120] Google Design — Connectivity, Culture, and Credit — https://design.google/library/connectivity-culture-and-credit — Product design must account for connectivity, device constraints, culture, and local context rather than assume high-end always-online use.
- [S121] Google Design — Exploring Color on Google Maps — https://design.google/library/exploring-color-google-maps — Demonstrates radical palette simplification to improve hierarchy and map readability.
- [S122] Smashing Magazine — Navigation Design for Mobile UX — https://www.smashingmagazine.com/2022/11/navigation-design-mobile-ux/ — Supporting practitioner synthesis on mobile navigation tradeoffs and reachable, contextual patterns.
- [S123] Smashing Magazine — Modern Fluid Typography Using CSS Clamp — https://www.smashingmagazine.com/2022/01/modern-fluid-typography-css-clamp/ — Implementation-oriented approach to fluid type while retaining bounded readable sizes.

## G. Web accessibility, responsive behavior, and motion — W3C/WAI, web.dev, MDN

- [S124] W3C — Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/ — Normative accessibility baseline used by this skill.
- [S125] W3C — Understanding WCAG 2.2 — https://www.w3.org/WAI/WCAG22/Understanding/ — Explanatory guidance for interpreting success criteria.
- [S126] W3C — Understanding Target Size (Minimum) — https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html — Level AA target-size criterion: 24×24 CSS pixels or permitted spacing/exception conditions.
- [S127] W3C — Understanding Reflow — https://www.w3.org/WAI/WCAG22/Understanding/reflow — Content should remain functional at equivalent 320 CSS-pixel width without two-dimensional scrolling except essential cases.
- [S128] W3C — Understanding Orientation — https://www.w3.org/WAI/WCAG21/Understanding/orientation — Do not lock orientation unless a specific orientation is essential.
- [S129] W3C — Mobile Accessibility at W3C — https://www.w3.org/WAI/standards-guidelines/mobile/ — Mobile accessibility is covered by WCAG and requires considering touch, small screens, multiple inputs, and varied contexts.
- [S130] W3C — Mobile Accessibility Mapping — https://www.w3.org/TR/mobile-accessibility-mapping/ — Practical mobile considerations including target spacing, gesture alternatives, orientation, consistency, and input assistance.
- [S131] W3C — Understanding Input Modalities — https://www.w3.org/WAI/WCAG21/Understanding/input-modalities.html — Touch is less precise than mouse input; pointer interactions need appropriate sizing and alternatives.
- [S132] W3C — Understanding Focus Appearance — https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html — Focus indication must be perceivable enough for keyboard users to locate interaction position.
- [S133] W3C — Understanding Contrast (Minimum) — https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html — Defines minimum text contrast requirements and rationale.
- [S134] W3C — Understanding Non-text Contrast — https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html — Meaningful graphical/control boundaries and states require adequate contrast where the criterion applies.
- [S135] W3C — Understanding Info and Relationships — https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html — Relationships communicated visually also need programmatic representation.
- [S136] W3C — Understanding Focus Order — https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html — Focus sequence must preserve meaning and operability.
- [S137] W3C — Understanding Dragging Movements — https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html — Drag interactions need a non-dragging alternative unless dragging is essential.
- [S138] W3C — Understanding Error Identification — https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html — Input errors need to be identified and described in text.
- [S139] W3C — Understanding Consistent Help — https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html — Repeated help mechanisms should remain predictably located/ordered where applicable.
- [S140] web.dev — Accessible Responsive Design — https://web.dev/articles/accessible-responsive-design — Responsive layouts improve both multi-device UX and accessibility; allows zoom, flexible content breakpoints, and recommends generous touch targets.
- [S141] web.dev — Accessibility — https://web.dev/articles/accessibility — Semantic HTML, labels, keyboard behavior, contrast, and robust native controls form the foundation of accessible web UI.
- [S142] web.dev — How to Review for Accessibility — https://web.dev/articles/how-to-review — Practical keyboard/focus audit: avoid positive tabindex, hidden focusable content, and keyboard traps.
- [S143] MDN — prefers-reduced-motion — https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion — Widely available mechanism for reducing/replacing non-essential motion based on user preference.
- [S144] MDN — Using Media Queries for Accessibility — https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility — Reduced-motion handling should remove non-essential movement while retaining necessary feedback.

## Source-quality notes

- **Normative:** S124-S139 are used for exact accessibility constraints; verify current wording when legal/conformance precision matters.
- **Platform:** S061-S082 are strong defaults within their ecosystems, but platform-specific conventions may legitimately differ.
- **Research:** S010-S060 informs heuristics and patterns; applicability depends on domain/task, and empirical commerce findings are not automatically universal.
- **Design systems:** S083-S118 demonstrate mature pattern decisions and implementation contracts; copying their visual style is not the goal.
- **Case/practitioner:** S119-S123 are supporting evidence/examples, not universal laws.
- **AI context:** S001-S008 informs how this knowledge should be packaged and activated for an agent.

## H. Product-design craft and real implementation retrospectives

- [S145] Linear — A Design Reset (Part I) — https://linear.app/now/a-design-reset — Treats redesign as maintenance of a product's foundational visual/interaction language rather than a cosmetic launch event.
- [S146] Linear — How We Redesigned the Linear UI (Part II) — https://linear.app/now/how-we-redesigned-the-linear-ui — Concrete redesign process focused on reducing visual noise, improving alignment, hierarchy, density, and shipping through staged feedback.
- [S147] Linear — A Calmer Interface for a Product in Motion — https://linear.app/now/behind-the-latest-design-refresh — Shows how individually reasonable feature additions accumulate inconsistency and why periodic pruning/structural normalization matters.
- [S148] Linear — How We Built Project Updates — https://linear.app/blog/how-we-built-project-updates — Starts from an observed coordination problem, rejects an over-quantified first idea, and integrates the new interaction into the user's existing work context.
- [S149] Figma — How We Built Our Website Design System — https://www.figma.com/blog/figma-on-figma-how-we-built-figma-dot-coms-design-system/ — Inventorying real pages exposed inconsistent fonts, sizes, colors, widths, layouts, and duplicated patterns; reusable foundations restored coherence.
- [S150] Figma — The New Business Case for Design Systems — https://www.figma.com/blog/the-new-business-case-for-design-systems/ — Current case material connecting design-system quality to customer outcomes, global scale, craft, and design/engineering collaboration.
- [S151] Figma — Design System 101: What Is a Design System? — https://www.figma.com/blog/design-systems-101-what-is-a-design-system/ — Design systems encode principles and interface language, not merely component files.
- [S152] Figma — Design System 102: How to Build a Design System — https://www.figma.com/blog/design-systems-102-how-to-build-your-design-system/ — Start with the problems and goals of the system before building components and foundations.
- [S153] Stripe — Design Your App — https://docs.stripe.com/stripe-apps/design — Shows deliberate constraints: platform consistency and accessibility can outweigh arbitrary brand customization inside an established host product.
- [S154] Stripe — Web Dashboard — https://docs.stripe.com/dashboard/basics — Real expert product example combining persistent object-oriented navigation, search, and keyboard acceleration for repeated work.
