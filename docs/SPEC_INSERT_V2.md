# SPEC v2 Insert

Suggested section to merge into `SPEC.md` after the Breakpoint concept or before Source Control Relationship.

```markdown
## Current Breakpoint State

LogDoc v2 introduces an optional machine-readable state file:

```text
CURRENT_BREAKPOINT_STATE.json
```

The Current Breakpoint State is a compact restart packet derived from the latest LogDoc breakpoint.

It must not become an independent competing source of truth. The human-readable LogDoc remains the narrative and decision record. The JSON file exposes the latest safe state in a format that humans, assistants, scripts, dashboards, and team workflows can consume quickly.

A session is not closed until:

1. The latest LogDoc breakpoint is written.
2. `CURRENT_BREAKPOINT_STATE.json` is updated from that breakpoint.
3. The JSON validates against the project schema.
4. `next_safest_action` is explicit.
5. `do_not_do_next` is explicit.
6. Validated, partially validated, not validated, blocked, and deferred state are current.
7. Allowed and not-allowed claims are current.

The Current Breakpoint State should include:

- project metadata
- active mission
- current status
- validated state
- partially validated state
- not validated state
- blocked/deferred state
- risk boundaries
- important paths and artifacts
- known-good commands
- diagnostic commands
- dangerous commands
- open blockers
- next-session bootstrap instructions
- allowed claims
- not-allowed claims
```
