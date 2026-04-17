---
name: prototype-previewer
description: Creates a polished interactive web prototype previewer for new or existing products. Use when the user asks for an HTML prototype, a clickable multi-screen flow preview, a reviewable app mock, a screen-by-screen web prototype, or a Figma-ready capture page. Produces a three-panel reviewer with flow navigation, a device viewport, editable review notes, and an optional figma_capture_index.html derived from the interactive source.
---

# Prototype Previewer

## Overview

This skill creates a reusable prototype review surface instead of a throwaway mock. The default output is a desktop review page with a left-side flow navigator, a center device or viewport preview, and a right-side review notes panel that stays synchronized with the active screen.

The same source material in this repo can also be reused in Cursor and Claude Code through the adapter files under [`adapters/`](../adapters).

Use this skill when the goal is fast product review, flow validation, or Figma handoff from a local web prototype.

## Workflow

1. Inspect the repo or brief before writing anything.
   Infer the product type, primary entry screen, major branches, detail pages, empty states, loading states, and any bottom-nav or tab structure. Every independent page or state counts as its own `data-screen`.

2. Build or update `index.html` as the interactive reviewer.
   The default structure should be:
   - left: clickable flow list with short summaries
   - center: mobile device shell or browser viewport with stateful screens
   - right: editable review notes for the active screen

3. Preserve the stable behavior recovered from prior sessions.
   - Use English for visible UI labels and review notes by default.
   - If another language is needed, require it explicitly in the prompt.
   - Interactions are local-only JavaScript. Do not depend on a backend.
   - Important states should be reviewable inside the preview itself: loading, empty vs filled, drill-down detail, tab switches, and one or two key CTA transitions.
   - The notes panel should auto-switch with the active screen and save edits to `localStorage`.
   - Resizable vertical dividers between columns are allowed and may be enabled by default.

4. Build or update `figma_capture_index.html` when the prototype may be captured into Figma.
   That page should fetch `/index.html`, parse the source HTML, clone the preview device once per screen, disable motion, and render one static section per `data-screen`. Mark readiness with `document.body.dataset.captureReady = "true"`.

5. Validate before finishing.
   - Every screen block has `data-screen` and `data-screen-label`.
   - The interactive preview has a visible default entry state.
   - The PRD panel follows screen changes and the Save action persists.
   - The capture page can derive one section per screen from `index.html`.
   - If needed, run `python3 scripts/check_previewer.py <project-root>`.

## Adaptation Rules

- If the product is mobile-first, keep a phone shell by default.
- If the product is desktop-first, replace the phone shell with a browser frame, but keep the same three-panel reviewer shell.
- If the repo already has a previewer, extend it instead of replacing working patterns.
- If copy is missing, prefer realistic placeholders over blocking on clarification.
- If the repo is React, Next, or another framework, it is still acceptable to create a standalone `index.html` review surface for rapid iteration.

## Load These Resources

- Read [references/previewer-spec.md](references/previewer-spec.md) first for the stable contract.
- Read [references/adaptation-checklist.md](references/adaptation-checklist.md) when mapping a new product into screens and notes.
- Use [assets/index.template.html](assets/index.template.html) and [assets/figma_capture_index.template.html](assets/figma_capture_index.template.html) as the default starter pair when the repo has no existing prototype shell.
- Use [scripts/check_previewer.py](scripts/check_previewer.py) for deterministic validation.

## Primary Files To Edit

When you want to change the behavior or look of the generated reviewer, edit these files first:

- `assets/index.template.html`
  This is the main interactive reviewer template. Change layout, dividers, resizing behavior, panel widths, interactions, default screen list, and default notes here.
- `assets/figma_capture_index.template.html`
  Change this when the Figma capture output should behave differently from the interactive reviewer.
- `SKILL.md`
  Change this when you want the assistant to follow different rules, defaults, or workflows.
- `references/previewer-spec.md`
  Change this when the stable contract should evolve.

## Output Contract

The preferred baseline output is:

- `index.html`
- `figma_capture_index.html`

You may add small supporting files if the project truly needs them, but keep the default prototype reviewer self-contained and easy to hand off.
