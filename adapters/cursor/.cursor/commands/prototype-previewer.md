Create an interactive prototype reviewer for this project.

Use these files as the source of truth:
- @prototype-previewer/SKILL.md
- @prototype-previewer/references/previewer-spec.md
- @prototype-previewer/references/adaptation-checklist.md

Prefer these outputs:
- index.html
- figma_capture_index.html

If the project does not already contain a reviewer shell, start from:
- @prototype-previewer/assets/index.template.html
- @prototype-previewer/assets/figma_capture_index.template.html

Defaults:
- use English for both interface copy and review notes
- if another language is required, the prompt must state it explicitly
- every independent page or state gets its own `data-screen`
- keep interactions local-only unless the project already needs a real backend
