# Implementation and visual audit

## Why render

Source code can look tidy while the UI is visually broken. Text wrapping, font metrics, actual data, viewport constraints, browser defaults, focus styling, scroll behavior, and asynchronous states only become obvious in a rendered environment.

## Recommended loop

### 1. Inspect before changing

For an existing codebase:

- identify framework and routing structure,
- locate design tokens/theme,
- inspect reusable components,
- find existing patterns for loading/errors/forms/navigation,
- check accessibility utilities and motion conventions,
- understand current responsive breakpoints.

Do not create a parallel mini-design-system in one screen.

### 2. Implement the behavior

Implement realistic state and content lengths. Use actual component semantics, not inert mock buttons.

### 3. Render

At minimum inspect:

- narrow viewport,
- representative desktop viewport,
- long labels/content,
- empty state,
- loading/pending state,
- representative error,
- populated state.

Add high-risk states specific to the task.

### 4. Visual critique

Inspect:

- hierarchy at first glance,
- alignment/baselines,
- spacing groups,
- unexpected wrapping/truncation,
- target crowding,
- sticky/scroll interactions,
- dialogs/menus overflowing viewport,
- focus visibility,
- color/contrast,
- icon/text optical alignment,
- density and whitespace balance,
- inconsistent border/radius/elevation,
- accidental horizontal overflow.

### 5. Interaction critique

Exercise:

- keyboard traversal,
- back/cancel,
- repeated submission,
- disabling/pending behavior,
- error correction,
- filter reset/search clear,
- resize/reflow,
- reduced-motion mode when motion exists.

### 6. Fix and re-render

Do not merely list obvious defects when the task is to build/refine the UI and tools permit fixing them. Fix material problems and inspect again.

## Screenshot critique heuristic

When a screenshot is available, do not ask only “does this look good?” Decompose it:

1. **Purpose:** what task does this screen appear to optimize?
2. **Hierarchy:** where does the eye go first/second/third?
3. **Grouping:** which elements appear related and why?
4. **Actions:** which action seems primary; are any hidden or over-prominent?
5. **Density:** is space proportional to task frequency and content?
6. **Consistency:** do controls and surfaces obey one visual grammar?
7. **Edge cases:** what breaks with longer text, errors, keyboard, or narrow width?
8. **Character:** does styling express the product or only framework defaults?

## Do not fake verification

If no renderer/browser/device is available, explicitly distinguish:

- **code-level verified**,
- **reasoned design inference**,
- **rendered/interaction verified**.

## Related evidence

See S011-S013, S030-S033, S095-S099, S110-S114, S124-S125 in `sources.md`.
