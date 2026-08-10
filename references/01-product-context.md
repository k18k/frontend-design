# Product context

## Purpose

Prevent premature UI generation. A design is only good relative to a user, task, environment, and product strategy.

## Context card

For substantial work, establish:

| Dimension | Questions |
|---|---|
| User | Who is doing the task? Novice, occasional, or expert? |
| Trigger | What made them open this screen now? |
| Job | What concrete outcome are they trying to achieve? |
| Frequency | Once, monthly, daily, dozens of times per hour? |
| Stakes | What happens if they make a mistake? |
| Environment | Desktop/mobile, touch/keyboard, bright light, intermittent network, one-handed use? |
| Knowledge | What terminology and concepts can they reasonably recognize? |
| Evidence | What do we know from users versus infer from conventions? |
| Existing system | Which patterns, tokens, components, and mental models already exist? |

## Evidence labels

Use these mentally or in a design brief:

- **Observed:** direct research, testing, analytics, support evidence, or explicit user statement.
- **Established:** existing product convention or normative/platform rule.
- **Inferred:** reasoned assumption based on the task/domain.
- **Unknown:** consequential gap that should not be quietly invented.

Do not manufacture certainty. If an assumption can change navigation, data requested, terminology, or a critical workflow, surface it.

## Primary-task discipline

A product surface should have a reason to exist. Write the reason as a verb-oriented user outcome, not a component inventory.

Weak: `This page contains a chart, cards, filters, and a table.`

Better: `A store manager identifies which locations need attention and takes the next corrective action.`

The second statement can reject useless components; the first cannot.

## Frequency changes good design

Repeated expert tasks often benefit from:

- higher useful density,
- keyboard support/shortcuts,
- fewer confirmations for safe reversible actions,
- persistent controls and remembered preferences,
- reduced explanatory copy after concepts are learned.

Rare or high-risk tasks often benefit from:

- more explicit language,
- stronger previews and confirmation,
- examples and inline help,
- visible recovery routes,
- less reliance on memory.

Do not optimize all products for first-use simplicity at the expense of daily efficiency, or vice versa.

## Product sense tests

Before designing, ask:

1. Why would the intended user choose to do this here rather than elsewhere?
2. What is the minimum useful outcome?
3. What decision is the interface helping them make?
4. What information must be trusted for that decision?
5. What can safely be delayed until the user asks for it?
6. Which mistakes are cheap and reversible? Which are costly?
7. What would a successful user do immediately after this screen?

## Research is not optional forever

Heuristics help create and inspect a design before user evidence exists, but they cannot prove the design fits real users. For consequential product work, identify where usability testing, interviews, analytics, field observation, or other methods would resolve the largest uncertainty.

## Related evidence

See sources S010-S023, S029-S033, S110-S114 in `sources.md`.
