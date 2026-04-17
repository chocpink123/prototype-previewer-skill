# Prototype Previewer Skill

A reusable Codex skill for generating polished interactive web prototype reviewers.

It is designed for the workflow we recovered from prior sessions:

- left-side flow navigation
- center interactive device or viewport preview
- right-side editable PRD notes
- optional `figma_capture_index.html` for Figma capture workflows

## What it builds

When invoked, the skill guides Codex to create a prototype reviewer that usually includes:

- `index.html`
- `figma_capture_index.html`

The default reviewer pattern is:

- English UI labels
- Chinese PRD logic notes
- local-only JavaScript interactions
- one `data-screen` per independent page or state

## Repository Layout

```text
prototype-previewer/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── assets/
└── scripts/
```

The actual skill lives in [`prototype-previewer/`](./prototype-previewer).

## Install

Copy the skill folder into your local Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R prototype-previewer ~/.codex/skills/prototype-previewer
```

## Use

Example prompt:

```text
Use $prototype-previewer to create an interactive index.html prototype reviewer and a matching figma_capture_index.html for this project.
```

Chinese example:

```text
用 $prototype-previewer 为这个新项目创建一个原型预览器，输出 index.html 和 figma_capture_index.html。
```

## Included Resources

- `SKILL.md`: trigger description and workflow
- `references/previewer-spec.md`: stable behavior contract
- `references/adaptation-checklist.md`: screen mapping and product adaptation checklist
- `assets/index.template.html`: interactive reviewer starter template
- `assets/figma_capture_index.template.html`: static Figma capture starter template
- `scripts/check_previewer.py`: validation helper

## Validation

Run the checker inside a project that already contains `index.html` and `figma_capture_index.html`:

```bash
python3 prototype-previewer/scripts/check_previewer.py /path/to/project
```

## Publishing Notes

This repository keeps GitHub-facing documentation at the repo root, while the skill itself stays clean inside `prototype-previewer/`.

## License

MIT
