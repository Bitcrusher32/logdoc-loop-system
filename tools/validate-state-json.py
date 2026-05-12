#!/usr/bin/env python3
"""
Validate a LogDoc CURRENT_BREAKPOINT_STATE.json file.

Usage:
  python tools/validate-state-json.py CURRENT_BREAKPOINT_STATE.json
  python tools/validate-state-json.py path/to/state.json --schema schema/current-breakpoint-state.schema.json

This validator is intentionally small. If the optional `jsonschema` package is
installed, it performs full schema validation. Without jsonschema, it still runs
basic structural checks so the tool remains usable on minimal systems.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL = [
    "schema_version",
    "project",
    "mission",
    "current_state",
    "validated",
    "partially_validated",
    "not_validated",
    "blocked",
    "deferred",
    "risk_boundaries",
    "important_artifacts",
    "important_paths",
    "known_good_commands",
    "diagnostic_commands",
    "dangerous_commands",
    "open_blockers",
    "next_session_bootstrap",
    "allowed_claims",
    "not_allowed_claims",
]

ARRAY_FIELDS = [
    "validated",
    "partially_validated",
    "not_validated",
    "blocked",
    "deferred",
    "risk_boundaries",
    "important_artifacts",
    "important_paths",
    "known_good_commands",
    "diagnostic_commands",
    "dangerous_commands",
    "open_blockers",
    "allowed_claims",
    "not_allowed_claims",
]


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"ERROR: file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {path}: {exc}")


def basic_validate(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Top-level JSON value must be an object."]

    for field in REQUIRED_TOP_LEVEL:
        if field not in data:
            errors.append(f"Missing required top-level field: {field}")

    if data.get("schema_version") != "logdoc-state/v0.1":
        errors.append("schema_version must be 'logdoc-state/v0.1'.")

    for field in ARRAY_FIELDS:
        if field in data and not isinstance(data[field], list):
            errors.append(f"Field must be an array: {field}")

    project = data.get("project")
    if isinstance(project, dict):
        for field in ["name", "repo", "logdoc_version", "phase", "last_updated"]:
            if field not in project:
                errors.append(f"Missing project.{field}")
        if not str(project.get("name", "")).strip():
            errors.append("project.name must not be empty.")
    elif "project" in data:
        errors.append("project must be an object.")

    mission = data.get("mission")
    if isinstance(mission, dict):
        if not str(mission.get("active_goal", "")).strip():
            errors.append("mission.active_goal must not be empty.")
        for field in ["non_goals", "success_criteria"]:
            if field in mission and not isinstance(mission[field], list):
                errors.append(f"mission.{field} must be an array.")
    elif "mission" in data:
        errors.append("mission must be an object.")

    current_state = data.get("current_state")
    if isinstance(current_state, dict):
        if not isinstance(current_state.get("safe_to_pause"), bool):
            errors.append("current_state.safe_to_pause must be a boolean.")
        if not str(current_state.get("next_safest_action", "")).strip():
            errors.append("current_state.next_safest_action must not be empty.")
        if not str(current_state.get("do_not_do_next", "")).strip():
            errors.append("current_state.do_not_do_next must not be empty.")
    elif "current_state" in data:
        errors.append("current_state must be an object.")

    bootstrap = data.get("next_session_bootstrap")
    if isinstance(bootstrap, dict):
        read_first = bootstrap.get("read_first")
        if not isinstance(read_first, list) or not read_first:
            errors.append("next_session_bootstrap.read_first must be a non-empty array.")
        if not str(bootstrap.get("do_not_start_with", "")).strip():
            errors.append("next_session_bootstrap.do_not_start_with must not be empty.")
    elif "next_session_bootstrap" in data:
        errors.append("next_session_bootstrap must be an object.")

    if not data.get("risk_boundaries"):
        errors.append("risk_boundaries should contain at least one explicit boundary.")
    if not data.get("not_allowed_claims"):
        errors.append("not_allowed_claims should contain at least one explicit forbidden claim.")

    return errors


def jsonschema_validate(data: Any, schema_path: Path) -> list[str] | None:
    try:
        import jsonschema  # type: ignore
    except Exception:
        return None

    schema = load_json(schema_path)
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    return [f"{'.'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in errors]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("state", nargs="?", default="CURRENT_BREAKPOINT_STATE.json")
    parser.add_argument("--schema", default="schema/current-breakpoint-state.schema.json")
    args = parser.parse_args()

    state_path = Path(args.state)
    schema_path = Path(args.schema)
    data = load_json(state_path)

    errors = None
    if schema_path.exists():
        errors = jsonschema_validate(data, schema_path)

    if errors is None:
        errors = basic_validate(data)
        mode = "basic structural validation"
    else:
        basic_errors = basic_validate(data)
        errors.extend(e for e in basic_errors if e not in errors)
        mode = "JSON Schema + basic structural validation"

    if errors:
        print(f"FAIL: {state_path} did not pass {mode}.", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"OK: {state_path} passed {mode}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
