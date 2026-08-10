# Data-dense UI

## Density is not clutter

Expert tools may legitimately show more information than consumer onboarding screens. The goal is high information utility per unit of attention, not maximal whitespace or maximal compression.

## Tables

Use a table when users need to compare values across rows/columns, scan repeated attributes, sort/filter, or perform row-oriented work.

Consider:

- meaningful column order,
- stable headers,
- numeric alignment,
- units and precision,
- sorting state that is visible and keyboard-accessible,
- filters with clear active state and reset,
- selection state independent from hover,
- bulk actions appearing in a predictable location,
- pagination/virtualization behavior that preserves orientation,
- loading/empty/error states,
- responsive handling based on comparison needs.

Do not place a wide operational table inside a cramped dialog merely because the initiating action came from a modal.

## Dashboards

A dashboard earns its existence when users need a cross-cutting status/decision surface.

Avoid “dashboard syndrome”:

- arbitrary KPI cards because dashboards are expected to have them,
- charts without a decision they support,
- duplicated metrics available elsewhere with no reason for aggregation,
- decorative trends with no scale/context,
- equal prominence for every metric.

For each metric/chart, identify the question it answers and the action it can trigger.

## Charts

- Use chart form suited to comparison/trend/distribution/relationship.
- Label units and timeframe.
- Avoid unnecessary 3D, gradients, and decorative ink that obscures data.
- Do not encode essential distinctions by color only.
- Provide exact values/accessible equivalents when users need precision.
- Keep zero baselines/axis decisions honest for the comparison being made.

## Expert acceleration

For repeated workflows consider:

- keyboard shortcuts with discoverable documentation,
- command/search interfaces where object/action scale justifies them,
- multi-select and bulk operations,
- remembered filters/views,
- density controls,
- inline editing where error risk is manageable,
- undo for reversible changes.

Do not add power features before the core model is understandable.

## Related evidence

See S060, S084, S086, S090, S092, S096-S099, S108 in `sources.md`.
