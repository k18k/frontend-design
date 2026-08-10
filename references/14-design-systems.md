# Design systems

## Purpose

A design system reduces repeated decisions and inconsistency. It should encode intent, not merely provide a component gallery.

## Layers

A useful hierarchy is:

1. foundations/primitives — color, typography, spacing, shape, motion,
2. semantic tokens — intent-based roles,
3. components — reusable interaction contracts,
4. patterns — combinations solving recurring tasks,
5. product-specific compositions — local solutions using the system.

## Tokens

Tokens should make global decisions changeable and semantic.

Prefer:

`color.text.danger` over `red500` in product code.

Primitive values may still exist underneath. Components can have dedicated tokens when their contract requires them, but avoid creating hundreds of aliases that make the system harder to understand than direct values.

## Component contract

A component should specify:

- purpose and when to use/not use,
- content rules,
- variants with semantic reason,
- states,
- keyboard/focus behavior,
- accessibility semantics,
- responsive behavior,
- composition constraints,
- escape hatch or extension strategy.

## Consistency versus fit

Reuse a component when it solves the same problem. Do not force a product requirement into the wrong component merely to achieve 100% reuse.

When deviation is needed:

1. check whether the existing component can support the case without harming its API,
2. determine whether the use case recurs enough to deserve a new pattern,
3. keep one-off exceptions explicit rather than silently forking styles.

## Governance through code

For implementation-oriented agents:

- inspect existing tokens/components before inventing new ones,
- avoid near-duplicate variants,
- use semantic names,
- document breaking visual/interaction changes,
- include states and accessibility in component examples,
- keep design and code sources synchronized where practical.

## Related evidence

See S076-S109 in `sources.md`.
