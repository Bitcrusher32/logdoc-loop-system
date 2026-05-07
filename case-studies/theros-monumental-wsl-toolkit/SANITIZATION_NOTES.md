# Sanitization Notes

This file describes the expected sanitization policy for the published LogDoc artifact.

## Purpose

The published LogDoc should preserve the engineering process while removing unnecessary private, sensitive, or device-specific details.

## Preserve

Keep:

- project scope
- non-scope decisions
- technical blockers
- error signatures
- patch timeline
- validation results
- breakpoint structure
- risk model shape
- reproducibility milestones
- public repo references
- general environment class

## Remove or generalize

Remove or generalize:

- passwords
- local usernames where unnecessary
- exact private machine names
- private home-directory paths where unnecessary
- personal device provenance where unnecessary
- private backup details
- private network details
- anything that could encourage unsafe device access
- any secrets, tokens, keys, or credentials
- any raw logs that contain unrelated personal data

## Keep with caution

Some details may be useful but should be reviewed carefully:

- target device model
- target OS version
- architecture
- package names
- installed tooling
- SSH workflow shape
- validation commands
- failure signatures

## Publication rule

The sanitized LogDoc should be useful as a process artifact, not a private operational dump.

When in doubt, preserve the lesson and remove the personal/local detail.