# Forms and input

## Reduce work, not merely screens

Users experience form complexity largely through the information they must understand and enter. Reduce unnecessary fields before splitting a form into extra steps.

Ask of every field:

- Why is this needed now?
- Can the system derive it?
- Can it be requested later?
- Can a safe default remove the decision?
- Can browser/platform autofill reduce entry cost?

## Labels

Use persistent labels. Placeholders can provide examples or formatting hints but must not be the sole label.

Labels should answer what the field means. Help text should explain unusual requirements before error occurs.

## Grouping

Group by user meaning and natural completion order. Keep related labels, controls, and error text visually and programmatically associated.

Long forms may need section headings, progress/context, or multiple pages. Do not use a wizard only to make each screenshot sparse.

## Field structure

Avoid splitting a single conceptual value into multiple controls unless it materially improves the task. Splitting increases navigation and formatting burden.

Use appropriate controls:

- free text only when the value is genuinely free-form,
- radio buttons for a small mutually exclusive set that benefits from visibility,
- checkbox for independent boolean/multiple selection,
- select/combobox when option scale/search needs justify hiding choices,
- date/time controls appropriate to precision and platform,
- numeric/tel/email input modes and autocomplete where relevant.

## Required and optional

Communicate required/optional status consistently. Do not make users infer it from missing asterisks or error messages.

## Validation timing

Validate when the system has enough information to judge the value and the feedback can still prevent expensive rework.

Avoid showing an error while the user is still entering a plausible value. Common strategies include validation on blur, on submit, or after a field has first failed and the user edits it again.

## Error message anatomy

An error should:

1. identify the affected field/task,
2. say what is wrong in plain language,
3. say how to fix it when not obvious,
4. preserve the user's valid work,
5. support focus/navigation to the problem on long forms.

Avoid blame, codes without explanation, and vague “Invalid input” messages.

## Submission

- prevent accidental duplicate destructive/financial submissions,
- keep the submit action visibly pending while processing,
- do not erase the form on recoverable system failure,
- make success explicit and indicate the next step,
- ensure keyboard submit behavior is expected and accessible.

## Mobile entry

- use the appropriate virtual keyboard/input mode,
- avoid tiny controls and tightly packed targets,
- keep labels and errors visible when the keyboard is open,
- do not force horizontal panning,
- preserve orientation flexibility unless essential.

## Related evidence

See S045-S059, S083, S093, S102-S103, S107, S121-S123 in `sources.md`.
