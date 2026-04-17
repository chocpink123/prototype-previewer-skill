# Adaptation Checklist

## Before writing

- Infer whether the product is mobile-first or desktop-first.
- Identify the default entry screen.
- List the minimum reviewable screens in order.
- Separate major app sections from branch screens and detail screens.

## For each screen

- Pick a stable `data-screen` id.
- Add a human-readable `data-screen-label`.
- Define one short flow summary for the left nav.
- Write two PRD note blocks:
  - `UI`: layout, hierarchy, component emphasis
  - `Page`: purpose, logic, transition behavior

## Behavior checklist

- At least one main CTA goes forward.
- At least one path goes back.
- If there is a loading state, make it legible and deterministic.
- If there is a list, include one detail drill-down.
- If there is a collection or dashboard concept, consider showing both filled and empty states.

## Capture checklist

- The interactive page and capture page must agree on screen ids.
- The source order of screens should match the intended Figma section order.
- The capture page should not depend on runtime-only state that never exists in source HTML.
- Prefer meaningful default markup for loading or detail states so static capture still looks correct.

## When information is missing

- Make reasonable product-shaped assumptions.
- Use believable placeholder copy instead of asking for every missing sentence.
- Keep the shell generic and reusable.
- If the user later provides stricter requirements, update the screen list and PRD docs without rebuilding the whole structure from scratch.
