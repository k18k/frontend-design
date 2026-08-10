# Craft and polish

## Craft is coherence under real use

“Polished” is not a list of effects. It is the absence of distracting inconsistencies plus deliberate control of hierarchy, density, alignment, typography, states, and motion.

A visually sophisticated surface can still feel amateur when:

- the same structural role changes position between screens,
- icon sizes/weights are inconsistent,
- baselines are almost but not quite aligned,
- content density changes without a task reason,
- radius, border, and shadow rules drift component by component,
- text styles multiply as one-off exceptions,
- long content exposes brittle fixed dimensions,
- empty/loading/error states look like a different product.

## Periodically prune accumulated UI

Products often become noisy one locally reasonable feature at a time. When extending an existing product, do not only ask “where can this new control fit?” Ask:

- Can an existing action absorb this capability?
- Is the same command already represented elsewhere?
- Does adding this create a second pattern for the same concept?
- What can be removed or consolidated as part of the change?
- Will the location remain predictable across related screens?

Linear's redesign retrospectives are useful evidence for this maintenance problem: structural consistency, alignment, density, and reduced noise can matter more than adding visual novelty.

## Optical quality

Code-perfect geometry is not always visually balanced. During rendered inspection, check:

- icon optical centering inside controls,
- cap-height/baseline relationship between icon and label,
- perceived rather than merely numeric spacing around uneven shapes,
- asymmetric glyph/illustration balance,
- border and shadow visibility against actual backgrounds,
- rhythm after text wraps to two or three lines.

Do not “fix” optical issues by scattering arbitrary offsets. Prefer correcting the component/icon/token so the rule remains coherent.

## Density is designed, not defaulted

A calmer interface is not necessarily a sparse interface. Productive expert software can be dense while remaining calm when:

- chrome is visually quieter than content,
- recurring structural controls are predictable,
- typography has clear but restrained hierarchy,
- alignment is strong,
- status color is reserved for meaning,
- spacing distinguishes groups without wasting travel distance.

Conversely, generous whitespace is appropriate when content comprehension, brand expression, or infrequent decision-making benefits from it.

## Explore before converging

For a new visual direction, avoid locking onto the first plausible generated composition.

Explore a small number of meaningfully different concepts, for example:

- dense/utilitarian,
- editorial/content-led,
- warm/service-oriented,
- technical/precision-led,
- expressive/brand-led.

The concepts should differ in composition and system logic, not only background color. Select based on product fit, then converge into one coherent system.

Do not force concept exploration for a tiny maintenance change inside a mature design system.

## Distinctiveness budget

Put distinctiveness where users can absorb it without paying a task penalty:

Good candidates:

- typography,
- brand color relationships,
- illustration/photography,
- empty/celebratory moments,
- composition on low-frequency marketing surfaces,
- micro-motion that explains state,
- shape/icon language.

Use more conventional patterns for high-frequency controls, navigation, data entry, destructive actions, and accessibility-critical interaction unless a new pattern is demonstrably better.

## Design-system inventory before invention

When a visual system already exists, inventory what is actually used before adding foundations. Figma's own website-system case study found that cataloging fonts, sizes, colors, widths, layouts, and repeated structures exposed near-duplicates that should be unified.

For an agent this means:

1. search the codebase for theme/tokens/components,
2. inspect multiple real screens,
3. identify repeated primitives and inconsistencies,
4. reuse or consolidate before adding variants,
5. render the result to catch hidden drift.

## Polish pass

After the functional UI is correct, run one dedicated craft pass:

- remove redundant borders/containers,
- normalize alignment and control heights,
- inspect text wrapping and line lengths,
- make iconography consistent,
- reduce competing emphasis,
- verify hover/focus/pressed/disabled states,
- inspect scrollbars/sticky edges/overlays,
- inspect transition continuity,
- check both light/dark themes if supported,
- verify actual content density rather than demo placeholders.

Polish should make the product clearer and more coherent. If a polish change reduces clarity, it is not polish.

## Related evidence

See S035, S076-S109, S119-S121, and S145-S154 in `sources.md`.
