# Information architecture

## Goal

Make the product's structure match the user's concepts, priorities, and vocabulary closely enough that finding and understanding information requires little translation.

## Start from objects and tasks

Identify:

- primary domain objects,
- actions users perform on them,
- relationships between objects,
- lifecycle/status of each object,
- cross-cutting tasks such as search, settings, billing, help.

Do not expose backend tables, route names, or organizational structure unless they match the user's mental model.

## Hierarchy before navigation

For each surface, rank content:

1. **Primary:** needed to understand or complete the current task.
2. **Secondary:** useful context or common adjacent action.
3. **Tertiary:** rare detail, settings, or supporting metadata.
4. **Noise:** no demonstrated purpose on this surface.

Navigation should follow this hierarchy; it cannot compensate for an undefined one.

## Labels

Good labels are:

- user vocabulary, not implementation vocabulary,
- specific enough to predict destination/action,
- stable across surfaces,
- distinguishable from sibling labels,
- concise without becoming cryptic.

Avoid clever labels that require interpretation. Do not rely on icons to resolve ambiguous wording.

## Recognition over recall

Keep relevant choices, context, recent items, states, and constraints visible when that helps the user decide. Do not force users to remember identifiers, previous screens, hidden requirements, or what an unlabeled icon meant.

## Discoverability tradeoff

Every layer of disclosure hides information. Hide low-priority complexity, not high-priority capability.

Before collapsing content into a menu, accordion, hover affordance, overflow button, or secondary screen, ask:

- How often is it needed?
- How costly is failure to discover it?
- Does hiding it meaningfully reduce complexity?
- Can the label accurately summarize what is hidden?

## Navigation tests

A navigation structure is suspect when:

- multiple destinations could plausibly contain the same task,
- labels mirror team ownership rather than user concepts,
- users must repeatedly bounce between sibling sections to complete one job,
- global navigation is used for object-local actions,
- a tab set contains unrelated destinations,
- navigation state disappears at narrow widths with no equivalent orientation cues.

## Validation methods

When possible:

- card sorting helps explore how users group/label content,
- tree testing validates whether a proposed hierarchy supports findability,
- task-based usability testing validates the entire navigation interaction,
- search/support logs reveal vocabulary mismatches and missing pathways.

Do not treat card sorting as an automatic sitemap generator; synthesize it with task needs and product constraints.

## Related evidence

See S014, S018-S021, S027, S040, S063-S069, S090-S094 in `sources.md`.
