# Color and tokens

## Semantic first

Define color by role rather than by component-specific arbitrary values:

- background/surface,
- foreground/text,
- muted/supporting text,
- border/divider,
- primary/brand action,
- success,
- warning,
- danger/error,
- information,
- focus,
- selected/active,
- disabled.

A semantic system supports dark themes, brand evolution, accessibility changes, and component consistency better than raw color literals scattered through code.

## Color is not enough

Never make color the only signal for status, validation, selection, or interactivity. Pair color with text, iconography, shape, state, or programmatic semantics as appropriate.

## Contrast

Check exact current WCAG requirements when conformance matters. At design time:

- body and control text need robust text contrast,
- meaningful boundaries/icons/focus indicators need non-text contrast where the criterion applies,
- placeholder/muted styling must not become unreadable,
- disabled styling should remain understandable even though disabled controls have different conformance treatment.

Do not treat a brand palette as automatically usable for UI roles.

## Palette economy

More colors increase interpretation cost. A system can be expressive with a small set of semantic roles and a coherent tonal scale.

Color reduction can improve map/data hierarchy when many hues previously compete equally; use category distinctions only when users need them.

## Design tokens

Tokens should encode decisions and semantics:

- primitive/base tokens: raw values,
- semantic tokens: role in the interface,
- component tokens only when a component needs a deliberate exception/contract.

Avoid a token layer that merely renames every magic number without adding semantics.

## Surfaces, borders, elevation

Use surfaces/elevation to communicate layering and interaction state. Do not stack shadows and borders purely for decoration.

If a visual hierarchy works only because every section has a different surface, reconsider spacing and typography first.

## Related evidence

See S042, S078-S082, S085-S088, S095-S109, S117 in `sources.md`.
