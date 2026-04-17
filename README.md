# Prototype Previewer

A reusable prototype reviewer skill pack for Codex, Cursor, and Claude Code.

It is designed around a reusable reviewer workflow:

- left-side flow navigation
- center interactive device or viewport preview
- right-side editable review notes
- optional `figma_capture_index.html` for Figma capture workflows
- optional resizable vertical dividers between columns

## What it builds

When invoked, the skill guides the assistant to create a prototype reviewer that usually includes:

- `index.html`
- `figma_capture_index.html`

The default reviewer pattern is:

- English UI labels
- English review notes
- local-only JavaScript interactions
- one `data-screen` per independent page or state

If another language is required, specify it in the prompt.

## Repository Layout

```text
adapters/
├── claude/
└── cursor/
prototype-previewer/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── assets/
└── scripts/
```

The actual skill lives in [`prototype-previewer/`](./prototype-previewer).

## Supported Tools

- `Codex`: use the skill directly from `prototype-previewer/`
- `Cursor`: use the adapter files under [`adapters/cursor/`](./adapters/cursor)
- `Claude Code`: use the adapter files under [`adapters/claude/`](./adapters/claude)

## Install In Codex

Copy the skill folder into your local Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R prototype-previewer ~/.codex/skills/prototype-previewer
```

## Install In Cursor

Copy these files into your project:

- `adapters/cursor/.cursor/commands/prototype-previewer.md`
- optionally `adapters/cursor/.cursor/rules/prototype-previewer.mdc`

Then run:

```text
/prototype-previewer
```

## Install In Claude Code

Copy these files into your project:

- `adapters/claude/.claude/commands/prototype-previewer.md`
- optionally merge `adapters/claude/CLAUDE.md` into your project-level `CLAUDE.md`

Then run:

```text
/prototype-previewer
```

## Use

Example prompt:

```text
Use $prototype-previewer to create an interactive index.html prototype reviewer and a matching figma_capture_index.html for this project.
```

## Included Resources

- `SKILL.md`: trigger description and workflow
- `references/previewer-spec.md`: stable behavior contract
- `references/adaptation-checklist.md`: screen mapping and product adaptation checklist
- `assets/index.template.html`: interactive reviewer starter template
- `assets/figma_capture_index.template.html`: static Figma capture starter template
- `scripts/check_previewer.py`: validation helper
- `adapters/`: tool-specific wrappers for Cursor and Claude Code

## Which File Should I Edit?

- `prototype-previewer/SKILL.md`
  Change the assistant behavior, defaults, and workflow rules here.
- `prototype-previewer/assets/index.template.html`
  Change the generated reviewer layout, interactions, divider behavior, panel widths, example screens, and default notes here.
- `prototype-previewer/assets/figma_capture_index.template.html`
  Change the Figma capture behavior here.
- `prototype-previewer/references/*.md`
  Change the stable design contract and adaptation guidance here.

Example:

- If you want draggable adaptive dividers between the three columns, edit `prototype-previewer/assets/index.template.html`.
- This repository already includes that behavior in the default template.

## Validation

Run the checker inside a project that already contains `index.html` and `figma_capture_index.html`:

```bash
python3 prototype-previewer/scripts/check_previewer.py /path/to/project
```

## Publishing Notes

This repository keeps GitHub-facing documentation at the repo root, while the skill itself stays clean inside `prototype-previewer/`.

## License

MIT
