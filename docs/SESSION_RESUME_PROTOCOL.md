# LogDoc v2 Session Resume Protocol

A LogDoc v2 session starts from the machine-readable state, then checks the human-readable breakpoint.

## Resume order

1. Read `CURRENT_BREAKPOINT_STATE.json`.
2. Read the latest LogDoc breakpoint.
3. Read README/docs only as needed for public-facing claims.
4. Read the full LogDoc only when provenance, caveats, or failure history are needed.
5. Start from `current_state.next_safest_action`.
6. Do not begin with anything listed under `current_state.do_not_do_next` or `next_session_bootstrap.do_not_start_with`.
7. Do not assume anything listed under `not_validated` or `not_allowed_claims`.

## Optional imported state section

When starting a fresh LogDoc from a prior state, add this near the top:

```markdown
## Imported Current Breakpoint State

Source: CURRENT_BREAKPOINT_STATE.json  
Imported at: YYYY-MM-DD HH:MM

### Active goal

### Validated

### Partially validated

### Not validated

### Current blocker

### Risk boundaries

### Next safest action

### Do not do next
```
