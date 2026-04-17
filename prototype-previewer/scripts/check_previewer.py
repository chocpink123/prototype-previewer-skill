#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


INDEX_MARKERS = [
    "prototype-shell",
    "preview-device",
    'data-screen="',
    "prd-save-button",
    "localStorage",
]

CAPTURE_MARKERS = [
    'fetch("/index.html"',
    "DOMParser",
    "capture-canvas",
    'dataset.captureReady = "true"',
    "preview-device",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"[FAIL] Missing file: {path}")
        sys.exit(1)


def require_markers(name: str, text: str, markers: list[str]) -> None:
    missing = [marker for marker in markers if marker not in text]
    if missing:
        print(f"[FAIL] {name} is missing markers:")
        for marker in missing:
            print(f"  - {marker}")
        sys.exit(1)


def main() -> None:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    index_path = root / "index.html"
    capture_path = root / "figma_capture_index.html"

    index_text = read_text(index_path)
    capture_text = read_text(capture_path)

    require_markers("index.html", index_text, INDEX_MARKERS)
    require_markers("figma_capture_index.html", capture_text, CAPTURE_MARKERS)

    screen_ids = re.findall(r'data-screen="([^"]+)"', index_text)
    labels = re.findall(r'data-screen-label="([^"]+)"', index_text)

    if not screen_ids:
        print("[FAIL] index.html has no data-screen entries.")
        sys.exit(1)

    if len(screen_ids) != len(labels):
        print("[FAIL] Each screen should have a matching data-screen-label.")
        print(f"  screens={len(screen_ids)} labels={len(labels)}")
        sys.exit(1)

    unique_ids = list(dict.fromkeys(screen_ids))
    if len(unique_ids) != len(screen_ids):
        print("[FAIL] Duplicate data-screen ids found.")
        sys.exit(1)

    print("[OK] Prototype previewer markers look good.")
    print(f"[OK] Found {len(screen_ids)} screens: {', '.join(screen_ids)}")
    print(f"[OK] Checked files: {index_path} and {capture_path}")


if __name__ == "__main__":
    main()
