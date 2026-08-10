# frontend-design

A research-backed Agent Skill for designing, implementing, and reviewing high-quality frontend interfaces.

It treats frontend design as a product/UX decision process rather than an aesthetic prompt. The skill covers product context, information architecture, flows, interaction patterns, forms, visual hierarchy, responsive design, accessibility, states, motion, data-dense UI, design systems, implementation, and rendered critique.

## Why

Generative models often know individual UX principles but still produce average interfaces when the relevant context and decision process are not active at generation time. This repository packages a compact operating procedure plus progressively loaded references so an agent is forced to reason through the task instead of jumping directly to styling.

The research corpus in `references/sources.md` contains more than the requested minimum of 75 sources. It prioritizes normative standards, official platform/design-system guidance, usability research, and real product case studies. General blog advice is used only as supporting material.

## Structure

```text
frontend-design/
├── SKILL.md
├── README.md
├── references/
│   ├── 01-product-context.md
│   ├── 02-information-architecture.md
│   ├── 03-interaction-and-flows.md
│   ├── 04-visual-hierarchy.md
│   ├── 05-typography-and-spacing.md
│   ├── 06-color-and-tokens.md
│   ├── 07-forms-and-input.md
│   ├── 08-navigation-and-disclosure.md
│   ├── 09-states-feedback-errors.md
│   ├── 10-mobile-responsive.md
│   ├── 11-accessibility.md
│   ├── 12-motion.md
│   ├── 13-data-dense-ui.md
│   ├── 14-design-systems.md
│   ├── 15-implementation-audit.md
│   ├── 16-craft-and-polish.md
│   ├── anti-patterns.md
│   ├── audit-rubric.md
│   └── sources.md
├── templates/
│   ├── design-brief.md
│   └── ui-audit.md
└── scripts/
    └── validate_skill.py
```

## Design philosophy

The skill intentionally avoids universal aesthetic commandments. A serious enterprise tool, a checkout, a mechanic's mobile workflow, and an editorial landing page should not converge on the same typography, density, cards, navigation, or motion.

Its hard requirements are instead about process quality:

- understand the user and job before choosing UI,
- make assumptions explicit,
- model the full task and states,
- choose interaction patterns for task reasons,
- establish a coherent visual system,
- treat accessibility and responsive behavior as design constraints,
- implement the actual states and semantics,
- render and critique the real result when tools allow it,
- fix material problems before finishing.

## Research method

Sources were selected using this order of preference:

1. normative standards and official accessibility guidance,
2. official platform guidelines,
3. established usability research organizations,
4. mature public design systems,
5. real-world product/design case studies,
6. specialist practitioner material when it adds a distinct rule.

Rules are included when they can change a concrete design decision or provide a quality test. The skill avoids turning correlations, heuristics, or aesthetic opinions into universal laws.

## Validation

Run:

```bash
python scripts/validate_skill.py
```

The validator checks the skill frontmatter, referenced local files, and the minimum research-corpus size.

## Status

Initial research synthesis, 2026-08-10. The skill should evolve as standards, platform conventions, and high-quality research change.
