# Prototype Previewer Spec

## Stable requirements recovered from prior sessions

- This output is a review tool, not a marketing landing page.
- The preferred shell is three columns on desktop:
  - left: flow navigation
  - center: device or browser preview
  - right: review notes tied to the active screen
- Every independent page or state counts as its own screen.
  Detail pages, loading states, empty states, paywalls, scan tips, and branch screens should each have their own `data-screen`.
- Visible product UI text and review notes default to English.
- If another language is needed, the prompt should request it explicitly.
- Interactions are local and deterministic. Avoid backend dependencies.
- The notes panel should expose two editable sections for the active screen:
  - `UI`
  - `Page`
- The Save action should persist to `localStorage`.
- Resizable vertical dividers between columns are acceptable and can be part of the default shell.

## Interaction patterns to preserve

- At least one primary CTA should move the user through the main flow.
- If the product has tabs or core sections, make them clickable in the preview.
- If the product has stateful content, include at least one toggle such as:
  - empty vs filled
  - list vs detail
  - loading vs result
- Detail drill-down should be previewable without leaving the prototype shell.
- Some screens may intentionally hide bottom chrome such as paywall, scanner, or processing states.

## Figma capture contract

- Maintain a dedicated `figma_capture_index.html`.
- It should fetch `/index.html` with `cache: "no-store"`.
- It should parse the source document and clone the main preview device once per screen.
- It should disable animation, transition, and caret effects for capture output.
- It should render one capture section per `data-screen` in source order.
- It should mark readiness with `document.body.dataset.captureReady = "true"`.

## Visual direction

- Use CSS custom properties.
- Prefer a deliberate visual system with gradients, soft glows, layered surfaces, and clear depth.
- Avoid generic wireframe energy unless the user explicitly wants a low-fidelity prototype.
- Make the review shell feel intentional enough to support stakeholder review.

## Minimal markers worth keeping

- `.prototype-shell`
- `.preview-device` or another clearly named main viewport wrapper
- `data-screen`
- `data-screen-label`
- `data-nav-target`
- `data-go`
- `data-resizer`
- `#prd-content`
- `#prd-save-button`

If you rename these markers, update the capture page and validation script in the same pass.
