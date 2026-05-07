# LogDoc Loop — Minimum Standards Template

A human-in-the-loop AI-assisted engineering protocol. This is a minimum viable LogDoc template that preserves both usability and systemic rigor. It avoids maximalist friction and the need for customization present in the maximal LogDoc template.

Adherence to proper logdoc hygiene, update cadence, and systems fundamentals will produce significantly higher quality LogDocs than more verbose LogDocs.

---

# [Project Name] LogDoc v[MAJOR].[MINOR]

**Last updated:** YYYY-MM-DD HH:MM  
**Owner/operator:**  
**Assistant/model:**  
**Current phase:**  
**Version schema:** v[scope].[timeline] — see §Versioning below

---

## 1. Project Goal

**Active goal:** One sentence. What are we doing *right now*?

**Explicit non-goals / out of scope:** What are we *not* doing? What would be scope creep?

**Success criteria:** How do we know this phase is done?

**Failure criteria:** When should we abandon or pivot?

**Historical context:** Why does this project exist? What came before?

---

## 2. Definitive Knowns

Stable facts. Treat as true until contradicted. Update when invalidated.

### 2.1 Environment
- Host OS / version:
- Shell / runtime:
- Key tools / versions:
- Important paths:
- Environment variables:

### 2.2 Target
- Target platform / version / architecture:
- Known compatibility limits:
- What has been proven to work:
- What has been proven *not* to work:

### 2.3 Repository State
- Repo / branch / commit:
- Important tracked files:
- Important untracked/generated files:
- Files that must *never* be committed:

### 2.4 Dependency State
- Confirmed installed:
- Confirmed missing:
- Version-sensitive:
- Unverified:

---

## 3. Current State

Classify each item. Use the classification system from §8.

| Classification | Items |
|---|---|
| **VALIDATED** | |
| **PARTIAL** | |
| **NOT VALIDATED** | |
| **BLOCKED** | |
| **DEFERRED** | |

---

## 4. Risk Model

### 4.1 High-Risk Actions
What could break something irreversibly?

### 4.2 Safe Assumptions
What can we rely on for now?

### 4.3 Unsafe Assumptions
What are we guessing? What would hurt if wrong?

### 4.4 Recovery Paths
If something goes wrong, how do we get back?

---

## 5. Current Plan

**Current phase:**

**Immediate next step:**

**Expected result:**

**If it succeeds:**

**If it fails:**

**What should NOT be done next:**

---

## 6. Validation Ladder

Staged proof. Do not overclaim. Each rung must be earned.

| Rung | Description | Status | Evidence |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Allowed claims after current validation:**

**Not allowed claims:**

---

## 7. Active Iteration Notes

The working log. Update every 5–15 minutes during active debugging, or after any meaningful state change.

### Entry [N] — YYYY-MM-DD HH:MM

**Action:** What was attempted?

**Command / change:** Exact command or code change.

**Result:** What happened? Paste relevant output.

**Interpretation:** What does this mean? Not just "it failed" — *why*?

**Classification:** [VALIDATED / PARTIAL / FAILED / BLOCKED / DEFERRED / UNSAFE / UNKNOWN / SUPERSEDED]

**Next action:**

---

## 8. Classification System

Use these precisely. Do not inflate.

| Label | Meaning |
|---|---|
| **VALIDATED** | Tested enough to rely on for the current phase. |
| **PARTIAL** | Shows progress but does not prove the full claim. |
| **FAILED** | The attempt did not work. |
| **BLOCKED** | Cannot continue without resolving a dependency or external constraint. |
| **DEFERRED** | Intentionally postponed. |
| **UNSAFE** | Carries unacceptable risk for the current phase. |
| **UNKNOWN** | Not yet understood or lacks context. |
| **SUPERSEDED** | Was relevant but replaced by newer information. |

---

## 9. Milestone Timeline

Major events in order. Compress history into operational memory.

### Milestone [N]: [Name] — YYYY-MM-DD

**Status:** [COMPLETE / PARTIAL / FAILED / ABANDONED]

**Evidence:** What proves this milestone?

**Caveats:** What does this *not* prove?

**Repo implications:** What needs to change in the repo because of this?

**Things to avoid:** Anti-patterns discovered during this milestone.

---

## 10. Breakpoint: YYYY-MM-DD HH:MM — [Label] v[X.Y]

Insert at stable handoff points: end of day, before risk boundaries, before publishing, before device work.

**Current state:**

**Validated:**

**Not validated:**

**Known risks:**

**Important artifacts:**

**Important commands:**

**Next safest action:**

**Do NOT do next:**

**Safe to pause here:** [Yes / No]

---

## 11. Notes for Future Assistant / Future Operator

**Do not skip:**

**Do not assume:**

**Known traps:**

**Preferred working style:**

**Important files:**

**Important context:**

**Next command to consider:**

---

## Appendix A: Versioning Schema

Use `v[MAJOR].[MINOR]` where:
- **MAJOR** = project scope / identity change
- **MINOR** = timeline continuity within that scope

Examples:
- v1.21 = scope 1 (toolchain recovery), timeline entry 21
- v2.00 = scope 2 (new project identity), reset minor
- v2.23 = same scope 2, timeline entry 23

---

## Appendix B: Hygiene Rules

1. **Generated artifacts never committed.** Add `.theos/`, `packages/`, `*.deb`, `*.log`, `__pycache__/`, `.tar` to `.gitignore`.
2. **Stale wording scans.** Before push, grep for outdated claims.
3. **Obsolete artifacts quarantined.** Move old patches/sketches to `docs/obsolete-*/` with README explaining status.
4. **Sanity before push.** Run syntax checks, artifact scans, and validation scripts.
5. **Repo truth ≠ LogDoc truth.** Sync repo docs after major milestones.

---

## Appendix C: When to Update This LogDoc

Update after any of these:
- New error signature
- Confirmed fix or failed fix
- Changed scope boundary
- Generated artifact
- Validation pass or failure
- Risk boundary crossed
- Handoff point reached
- Decision to pause, stop, or branch

---