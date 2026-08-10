# States, feedback, and errors

## Visibility of system status

Users should be able to tell whether an action was received, what is happening now, and what they can do next.

Feedback should be scoped to the thing that changed. A row update usually needs row/local feedback, not a page-blocking overlay.

## Loading strategy

Do not show a loading indicator for every tiny delay; flicker can be more distracting than waiting.

Use:

- immediate state change for effectively instant operations,
- local pending state for short asynchronous work,
- skeleton when content structure is predictable and revealing it improves perceived continuity,
- determinate progress when meaningful completion can be estimated,
- indeterminate progress only when the wait is real but progress cannot be measured.

Never use fake progress that communicates precision the system does not know.

## Empty-state taxonomy

### First use / no data yet
Explain what belongs here and provide the relevant first action when one exists.

### No search/filter results
Keep the user's query/filters visible, explain no matches, and offer the most useful adjustment/reset.

### Permission-limited
Say access is restricted and give the appropriate request/contact route if one exists.

### Load failure
Do not masquerade as empty. Explain failure and recovery/retry.

## Errors

Match error scope:

- field error -> near field,
- section-level problem -> section,
- page-level persistent condition -> page banner/notice,
- blocking decision -> dialog only when resolution is required.

Do not rely on toast-only errors for important failures; transient messages disappear and can be missed.

## Success

Do not celebrate routine actions so aggressively that repeated work becomes slower. Use stronger confirmation when:

- the action is infrequent,
- the result is consequential,
- the next step is not obvious,
- users need a receipt/reference/summary.

## Optimistic updates

Use optimistic UI only when failure is uncommon and rollback/reconciliation is understandable and safe. Do not temporarily show a high-stakes irreversible action as completed when the server may reject it without a clear recovery model.

## Change blindness

When content changes after an action, place feedback near the locus of attention or otherwise make the change perceivable. Do not update a distant counter and assume users will notice.

## Related evidence

See S010, S028, S036-S039, S060, S070-S075, S083, S105-S108 in `sources.md`.
