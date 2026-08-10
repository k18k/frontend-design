# Interaction and flows

## Flow first

A user flow describes concrete interactions needed to complete a task. A journey is broader and may span channels, time, emotions, and service touchpoints. Use the smallest tool that matches the problem.

For UI implementation, define:

`entry -> understand -> act -> system response -> continue/recover -> completion`

## Happy path is insufficient

For each state-changing action, enumerate:

- valid success,
- validation failure,
- server/system failure,
- cancellation/back,
- retry,
- duplicate/repeated action,
- concurrent/stale state when material,
- permission/auth change when material.

## Interaction-cost budget

Each extra action has cost: clicks/taps, context switches, memory, waiting, precision, interpretation. Remove interactions that do not protect the user, reduce complexity, or expose meaningful choice.

Examples:

- Do not put a single obvious action behind a kebab menu merely to make the layout clean.
- Do not make a modal ask for confirmation of a harmless reversible action.
- Do not split a short coherent form into steps solely to look simpler.
- Do sequence genuinely dependent or cognitively heavy decisions when one page would overwhelm the user.

## Control and reversibility

Prefer designs that let users safely explore and recover:

- back/cancel should not silently destroy expensive work,
- reversible actions can use undo instead of interruption,
- destructive actions need clear scope and consequence,
- confirmations should name what will happen rather than ask vague “Are you sure?” questions,
- preserve user input across recoverable failures.

## Match system behavior to intent

Controls should behave as their appearance and platform convention suggest. Do not create visually familiar controls with surprising semantics.

Examples:

- switch/toggle: immediate binary setting change, not “select then save” unless the product convention clearly says otherwise,
- button: action,
- link: navigation,
- checkbox: independent selection,
- radio: mutually exclusive choice,
- tabs: switch peer views within a context.

## Default decisions

A default is a recommendation and can influence behavior. Use defaults when there is a safe, evidence-backed/common choice; do not preselect consequential consent, irreversible decisions, or assumptions that hide user intent.

## Progressive complexity

Expose common paths directly. Defer rare configuration while keeping it discoverable. Expert capability can coexist with beginner clarity through sensible defaults, expandable advanced options, shortcuts, and remembered settings.

## Related evidence

See S010, S011, S014, S025-S027, S061-S075, S089-S094 in `sources.md`.
