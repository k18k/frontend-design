# Mobile and responsive design

## Re-compose, do not shrink

Responsive design preserves task and information priority while changing composition.

At each meaningful width, ask:

- What must remain visible?
- What can wrap/reorder without changing meaning?
- Which controls require a different mobile pattern?
- Does source/focus order still match visual order?
- Can the user complete the entire task without horizontal panning?

## Content-driven breakpoints

Use breakpoints when content/layout stops working, not merely because a device category is familiar.

Test extremes:

- narrow phone,
- large phone/small tablet,
- common desktop,
- wide desktop,
- zoomed/large-text states.

## Reflow and zoom

Web content should remain usable when zoomed. WCAG 2.2 reflow requires applicable content to work at an equivalent 320 CSS-pixel viewport without two-dimensional scrolling, except where two-dimensional layout is essential.

Do not disable pinch zoom.

## Touch

WCAG 2.2 Level AA target-size minimum is 24×24 CSS pixels with exceptions. That is a conformance floor, not an aspirational mobile target. Use larger practical targets and sufficient separation for frequent touch interactions when density allows; 48px is a common accessible responsive-design recommendation.

## Orientation

Do not lock orientation unless the task genuinely requires it.

## Mobile context

Consider conditions beyond viewport width:

- one-handed use,
- imprecise touch,
- movement,
- bright light,
- intermittent/slow connectivity,
- soft keyboard covering content,
- interrupted sessions,
- platform back/navigation behavior.

Do not invent a “thumb zone” rule as universal; hand size, device size, grip, accessibility, and platform vary. Place frequent actions where the target platform and tested task make them easy to reach.

## Dense data

For tables on narrow screens choose deliberately among:

- preserve horizontal scroll when column relationships are inherently two-dimensional,
- prioritize/freeze key columns,
- provide row-detail drill-down,
- transform rows into labeled records/cards when comparison across columns is not central,
- offer a dedicated wide/data view.

Never silently drop essential columns.

## Responsive copy

Avoid instructions tied to spatial position such as “click the control on the left.” Refer to the control by its label.

## Related evidence

See S034, S049-S051, S076, S111-S113, S124-S130 in `sources.md`.
