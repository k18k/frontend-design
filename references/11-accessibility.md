# Accessibility

## Baseline

Use WCAG 2.2 as the current normative web baseline in this research corpus. Exact conformance decisions should be checked against the current W3C specification, not against a paraphrase in this skill.

## Semantic structure

- Use native semantic elements and controls whenever possible.
- Preserve heading hierarchy and landmarks.
- Associate labels, descriptions, errors, and groups programmatically.
- Do not use visual position as the only expression of relationships.

## Keyboard and focus

- All actionable functionality must be operable without a pointer when the platform expects keyboard access.
- Follow logical focus order that matches reading/task order.
- Keep focus visibly apparent.
- Avoid positive `tabindex` ordering hacks.
- Do not leave hidden/offscreen interactive content focusable.
- Dialogs may manage focus intentionally, but always provide an accessible escape unless safety truly prevents cancellation.

## Names and labels

- Icon-only controls need accessible names.
- The accessible name should include the visible label text when there is visible text.
- Do not make users infer unlabeled controls from shape/color alone.

## Contrast and color

- Meet current WCAG text contrast criteria.
- Meet applicable non-text contrast for meaningful controls, states, and focus indicators.
- Do not convey status/error/selection solely by color.

## Size and input

- WCAG 2.2 AA includes a 24×24 CSS-pixel minimum target-size criterion with exceptions.
- Provide alternatives to dragging for functionality that uses drag.
- Do not require complex pointer gestures when a simpler input can perform the same function unless essential.
- Support multiple input modalities where the platform does.

## Reflow, zoom, orientation

- Support text zoom and layout reflow.
- Applicable web content should not lose functionality at equivalent 320 CSS-pixel reflow.
- Do not lock device orientation unless essential.

## Errors and help

- Identify errors in text, not color alone.
- Associate errors with the relevant control.
- Give correction guidance when useful.
- Keep repeated help mechanisms consistent where WCAG's consistent-help criterion applies.

## Dynamic content

When a state changes without moving focus, ensure critical status is perceivable by assistive technology. Use platform-appropriate live/status semantics; do not announce every cosmetic change.

## Motion

Respect user reduced-motion preferences. Remove or replace non-essential motion that could cause discomfort, while preserving needed state/meaning.

## Testing

Automation is not sufficient. For substantial UI, combine:

- semantic/accessibility tooling,
- keyboard-only pass,
- focus order/visibility pass,
- zoom/reflow pass,
- screen-reader spot checks for critical flows when feasible,
- touch target/input testing on relevant devices.

## Related evidence

See S077-S083, S095, S103, S106-S109, S111-S113, S124-S130 in `sources.md`.
