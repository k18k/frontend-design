# UI/UX audit rubric

Use this rubric for a systematic review. Do not mechanically total a score if one severe problem blocks the primary task.

## Severity

- **P0 — Blocker:** user cannot complete a critical task; severe accessibility/safety failure; data loss or deceptive behavior.
- **P1 — Major:** substantial confusion, error risk, inaccessible important function, major responsive failure, or hidden primary capability.
- **P2 — Moderate:** meaningful friction, inconsistent hierarchy, recoverability issue, avoidable cognitive load.
- **P3 — Minor:** polish, spacing, microcopy, minor consistency, non-blocking visual quality.

## Dimensions

Score each 0–4 only when a numeric summary is useful:

### 1. Task clarity
- 0: purpose/action incomprehensible
- 1: major ambiguity
- 2: usable with thought
- 3: clear
- 4: immediately clear and efficient

### 2. Information architecture
Evaluate hierarchy, vocabulary, grouping, orientation, discoverability.

### 3. Interaction model
Evaluate predictability, control choice, reversibility, action hierarchy, unnecessary steps.

### 4. State completeness
Evaluate loading, empty, error, success, disabled, permission, offline/concurrency where applicable.

### 5. Forms/input
Evaluate field necessity, labels, grouping, validation, error recovery, input modes/autocomplete.

### 6. Visual hierarchy
Evaluate scan path, emphasis levels, alignment, grouping, density, container use.

### 7. Typography and readability
Evaluate role consistency, measure, wrapping, size, line-height, numeric treatment.

### 8. Color and contrast
Evaluate semantic color, contrast, non-color cues, focus/selection distinction.

### 9. Responsive/touch
Evaluate reflow, mobile composition, target spacing, keyboard overlay, orientation, dense data.

### 10. Accessibility
Evaluate semantics, names, keyboard, focus, contrast, errors, target size, motion, dynamic state.

### 11. Motion/feedback
Evaluate purpose, timing, progress/status, reduced motion, interruption level.

### 12. Product character
Evaluate coherence with audience/product/brand rather than trendiness alone.

### 13. Implementation consistency
Evaluate token/component reuse, behavior duplication, semantic controls, state architecture.

### 14. Rendered quality
Evaluate actual screenshots/device behavior, not intentions in source code.

## Audit output format

Prioritize findings, not prose volume.

For each material finding:

```text
[P1] Primary action is hidden in overflow
Evidence: ...
User impact: ...
Why it happens: ...
Fix: ...
Verification: ...
```

Separate facts observed in rendered UI/code from inferred user impact.
