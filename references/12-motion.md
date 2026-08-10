# Motion

## Motion needs a job

Good motion can explain:

- where content came from/went,
- relationship between states,
- action feedback,
- hierarchy and focus,
- progress or continuity.

If removing an animation loses no meaning, feedback, or brand value, it is decorative. Decorative motion should remain subordinate to task performance.

## Routine interaction

Repeated product work benefits from subtle, quick transitions. Do not force users to wait for choreography before they can continue.

Avoid animating many unrelated elements at once; it creates competing attention and can hide what changed.

## Spatial continuity

Use consistent spatial relationships when they help users track an object or navigation transition. Do not invent dramatic movement unrelated to the product's mental model.

## Reduced motion

Respect `prefers-reduced-motion` on the web and equivalent platform settings. A reduced-motion mode can:

- replace large movement with opacity/state changes,
- remove parallax and decorative loops,
- shorten or remove non-essential transitions,
- keep essential progress/feedback in a non-triggering form.

Reduced motion does not mean removing all feedback.

## Performance

An animation that causes jank or delayed input is a UX regression. Prefer techniques that keep interaction responsive and avoid expensive continuous layout/paint work.

## Related evidence

See S044, S076, S087-S088, S115, S126-S127 in `sources.md`.
