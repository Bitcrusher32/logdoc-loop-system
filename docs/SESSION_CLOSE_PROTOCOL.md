# LogDoc v2 Session Close Protocol

A LogDoc v2 session is not closed until the human-readable breakpoint and machine-readable state agree.

## Close checklist

1. Update the active LogDoc notes.
2. Write or update the final breakpoint.
3. Update `CURRENT_BREAKPOINT_STATE.json` from that breakpoint.
4. Run the state validator.
5. Confirm `next_safest_action` is explicit.
6. Confirm `do_not_do_next` is explicit.
7. Confirm validated, partially validated, not validated, blocked, and deferred states are current.
8. Confirm risk boundaries are explicit.
9. Confirm allowed and not-allowed claims are current.
10. Update README/docs only if public claims changed.
11. Commit the LogDoc and state file together.

## Validation command

```bash
python tools/validate-state-json.py CURRENT_BREAKPOINT_STATE.json
```

## Optional archive command

Archive only at important milestones or handoffs:

```bash
python tools/archive-current-state.py --label milestone-label
```

## Failure condition

If `LOGDOC.md` says one thing and `CURRENT_BREAKPOINT_STATE.json` says another, do not treat the session as safely closed.
