# README v2 Insert

Suggested section to merge into `README.md` after the core idea or loop section.

```markdown
## LogDoc v1 and v2

LogDoc Loop has two intended usage levels.

### LogDoc v1

LogDoc v1 is the lean Markdown-only workflow. It is suited to solo developers, personal projects, and human-in-loop AI-assisted iteration where a structured LogDoc is enough.

### LogDoc v2

LogDoc v2 keeps the human-readable LogDoc, but adds enhanced handoff state definitions through a machine-readable `CURRENT_BREAKPOINT_STATE.json` file.

The split is:

- Markdown for the grind.
- JSON for the handoff.
- Git for history.
- README/docs for public claims.

`CURRENT_BREAKPOINT_STATE.json` is derived from the latest LogDoc breakpoint. It records the current validated state, partial state, not-validated state, blockers, risk boundaries, important commands, allowed claims, not-allowed claims, and next safest action.

A LogDoc v2 session is not closed until the latest LogDoc breakpoint and `CURRENT_BREAKPOINT_STATE.json` agree.
```
