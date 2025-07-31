#!/usr/bin/env python3
"""Move task files from legacy 'docs/agile/Tasks' into 'docs/agile/tasks'.
Regenerates the kanban board if any files were moved."""

from __future__ import annotations

import os
from pathlib import Path
import shutil

LEGACY_DIR = Path("docs/agile/Tasks")
TASKS_DIR = Path("docs/agile/tasks")
BOARD_PATH = Path("docs/agile/boards/kanban.md")


def move_tasks() -> bool:
    """Move markdown files from legacy location to new tasks directory."""
    if not LEGACY_DIR.exists():
        return False
    TASKS_DIR.mkdir(exist_ok=True)
    moved = False
    for file in LEGACY_DIR.glob("*.md"):
        target = TASKS_DIR / file.name
        if target.exists():
            print(f"Skipping move of {file} -> {target}: target exists")
            continue
        shutil.move(str(file), str(target))
        moved = True
    try:
        LEGACY_DIR.rmdir()
    except OSError:
        pass
    return moved


def regenerate_board() -> None:
    os.system(f"python scripts/hashtags_to_kanban.py > {BOARD_PATH}")


def main() -> None:
    if move_tasks():
        regenerate_board()


if __name__ == "__main__":
    main()
