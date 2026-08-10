# Navigation and disclosure

## Navigation answers three questions

Users should be able to infer:

1. Where am I?
2. What can I reach from here?
3. How do I get back or move up a level?

Do not remove orientation cues purely to make the interface look minimal.

## Pattern choice

### Tabs
Use when:

- views are peers within one context,
- users may switch between them repeatedly,
- labels fit and remain understandable.

Avoid when:

- the flow is sequential,
- destinations belong to different global areas,
- there are too many items to remain scannable,
- tab state would unexpectedly hide unsaved work.

### Breadcrumbs
Useful as secondary orientation in deeper hierarchies, especially on wide/desktop information spaces. Do not treat them as the only navigation.

### Sidebar
Useful when persistent access to several destinations benefits repeated work and there is sufficient space. At narrow widths, transform deliberately rather than simply hiding it.

### Menus/overflow
Good for secondary/rare actions. Poor for critical or frequent actions whose invisibility harms discoverability.

### Accordion/disclosure
Use for secondary detail that benefits from compression. The heading should predict the hidden content. Keep frequent/critical information visible.

### Modal/dialog
Use for bounded tasks that require attention without permanently leaving context. Avoid nesting dialogs. Provide an obvious accessible escape/cancel route unless the user truly cannot continue safely.

### Sheet/drawer
Useful when preserving context matters and platform conventions support it. The same interrupt-cost rules as dialogs apply.

## Progressive disclosure test

Hiding content is justified when all are true enough:

- the hidden information/action is lower priority in the current task,
- the trigger label is discoverable and descriptive,
- revealing it does not create surprising context/state loss,
- the complexity saved outweighs the interaction cost.

## Mobile navigation

Do not assume a desktop sidebar maps automatically to a hamburger menu. Consider frequency, destination count, hierarchy depth, and need for persistent state.

A mobile navigation redesign may prioritize the few highest-frequency destinations and place secondary destinations elsewhere, provided all necessary capabilities remain accessible.

## Related evidence

See S024-S027, S061-S075, S089-S094, S119-S120 in `sources.md`.
