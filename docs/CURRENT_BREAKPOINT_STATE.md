# Current Breakpoint State

`CURRENT_BREAKPOINT_STATE.json` is the LogDoc v2 machine-readable restart packet.

It is derived from the latest human-written LogDoc breakpoint. It is not a replacement for the LogDoc, README, issue tracker, test suite, or Git history.

## Purpose

The file answers the handoff questions that matter most after context loss:

- What project is this?
- What is the active goal?
- What is validated?
- What is partially validated?
- What is not validated?
- What is blocked or deferred?
- What risk boundaries must be respected?
- What commands and paths matter?
- What is the next safest action?
- What must not be done next?
- What claims are allowed?
- What claims are not allowed?

## Relationship to the LogDoc

LogDoc v2 uses this relationship:

- `LOGDOC.md` is the human-readable grind log, narrative, debugging trail, decision record, and validation history.
- `CURRENT_BREAKPOINT_STATE.json` is the machine-readable latest restart packet.
- Git is the historical record of exact file changes.
- README/docs are public or team-facing claims after cleanup.

The JSON file must be updated from the latest LogDoc breakpoint.

If the LogDoc breakpoint and JSON disagree, the session is not closed.

## Design rule

Keep the state file small.

It should summarize the latest safe restart state, not mirror the entire LogDoc.

## Recommended filename

Use:

```text
CURRENT_BREAKPOINT_STATE.json
```

The name is intentionally explicit for discoverability.
