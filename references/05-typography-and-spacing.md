# Typography and spacing

## Typography is structure

Define semantic text roles, not arbitrary one-off sizes:

- display/hero when the product needs it,
- page title,
- section heading,
- body,
- compact body/table,
- label,
- metadata/help,
- code/numeric specialized roles where relevant.

Keep the number of roles small enough that differences remain meaningful.

## Readability

- Keep long-form text at a comfortable measure rather than using the full viewport width.
- Use sufficient line height for multi-line text.
- Avoid all-caps for long text.
- Do not use tiny type to solve a layout problem.
- Preserve text zoom and responsive reflow.
- Choose weight and contrast that remain legible in real rendering, not only design mockups.

## Hierarchy

A heading should look like the level it represents. Do not rely on size alone; combine scale with spacing and weight deliberately.

Avoid microscopic differences such as many adjacent text sizes that are visually indistinguishable. A compact system with clear roles is easier to scan and maintain.

## Numeric/data typography

For dense numeric interfaces consider:

- tabular numerals when column alignment matters,
- units separated from values without competing visually,
- consistent decimal precision justified by the task,
- right alignment for comparable numeric columns where appropriate,
- monospace only when character alignment/code semantics actually help.

## Spacing is relational

Spacing communicates grouping. Define a small scale and use smaller distances within a group than between groups.

Do not mechanically use one gap everywhere. Relationships differ:

`label <-> control` should usually feel closer than `field group <-> next section`.

## Density modes

If a product genuinely serves both occasional and expert high-volume work, consider intentional density modes rather than accidental inconsistency. A dense mode must still preserve target size, readability, and focus visibility requirements.

## Responsive typography

- Let content define wrapping and breakpoint needs.
- Avoid fixed heights around variable text.
- Test long labels, localization expansion, large text, and dynamic data.
- Do not truncate important text without a way to access it.

## Related evidence

See S041-S043, S077, S084, S091-S093, S101, S104, S116 in `sources.md`.
