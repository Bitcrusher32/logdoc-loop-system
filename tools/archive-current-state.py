#!/usr/bin/env python3
"""
Archive CURRENT_BREAKPOINT_STATE.json to archive/breakpoints/.

Usage:
  python tools/archive-current-state.py --label v2.0-schema-added
  python tools/archive-current-state.py --state path/to/CURRENT_BREAKPOINT_STATE.json --label milestone-name
"""
from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime
from pathlib import Path


def slugify(label: str) -> str:
    label = label.strip().lower()
    label = re.sub(r"[^a-z0-9._-]+", "-", label)
    label = re.sub(r"-+", "-", label).strip("-")
    return label or "checkpoint"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", default="CURRENT_BREAKPOINT_STATE.json")
    parser.add_argument("--archive-dir", default="archive/breakpoints")
    parser.add_argument("--label", required=True)
    args = parser.parse_args()

    state_path = Path(args.state)
    if not state_path.exists():
        raise SystemExit(f"ERROR: state file not found: {state_path}")

    archive_dir = Path(args.archive_dir)
    archive_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    dest = archive_dir / f"{stamp}-{slugify(args.label)}.json"
    shutil.copy2(state_path, dest)
    print(f"Archived {state_path} -> {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
