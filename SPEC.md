# LogDoc Loop System Specification
Version: 0.1


## 1. Definition
**LogDoc Loop** is a human-in-the-loop AI-assisted engineering protocol for maintaining a living operational context document during complex technical work.

A **LogDoc** is the document.

The **Loop** is the repeated process of:

1. attempting a bounded step
2. observing the result
3. recording the state change
4. updating knowns, blockers, risks, and next actions
5. creating breakpoints at stable handoff moments

The purpose of the protocol is to keep technical work reproducible, restartable, auditable, and safe to resume after interruption.

---

## 2. Design goals
LogDoc Loop is designed to support:

- long-running technical iteration
- human-led AI-assisted engineering
- unstable debugging sessions
- project handoff across time
- reproducible builds
- clear risk boundaries
- publication-quality reconstruction
- assistant context restoration
- reduced dependency on chat history
- reduced dependency on human memory

---


## 3. Non-goals
LogDoc Loop is not designed to be:

- a full project management system
- an issue tracker replacement
- a test framework
- a formal proof system
- an autonomous-agent protocol
- a substitute for source control
- a substitute for engineering review
- a substitute for security review
- a substitute for documentation written for end users

A LogDoc may feed into these systems, but it does not replace them.

---

## 4. Required concepts

### 4.1 LogDoc
A living operational context document for a technical project.

It records what is known, what has changed, what has been validated, what remains risky, and what should happen next.


### 4.2 Loop
The repeated cycle of:

Attempt → Observe → Interpret → Record → Decide Next Step
The loop should continue until the project reaches a breakpoint, milestone, abandonment point, or publication state.


### 4.3 Definitive Known
A fact that should be treated as stable until contradicted.

Examples:

 - operating system version
 - target architecture
 - installed tool path
 - validated command
 - current repo branch
 - confirmed dependency version
 - known device state
 - known unsafe action

Definitive knowns should be explicit, not implied, and should be project-context dependent.


### 4.4 Scope
The current active work.

Scope should answer:

 - What are we doing now?
 - What are we not doing now?
 - What counts as success?
 - What is intentionally deferred?



### 4.5 Non-Scope
Work that may be historically related but is not allowed to drive the current task.
This prevents old project goals from contaminating the active plan.


### 4.6 Risk Boundary
A point where the cost of being wrong increases.

Examples:

 - moving from host-side tests to device installs
 - deleting generated files
 - restoring a device
 - publishing compatibility claims
 - running destructive commands
 - touching production data
 - changing security-sensitive configuration

Crossing a risk boundary should require a breakpoint or explicit validation step.



### 4.7 Validation Ladder
A staged proof sequence.

Instead of jumping from “it compiled once” to “it works,” a validation ladder defines progressive evidence.

Example:

1. Source builds.
2. Binary is generated.
3. Binary has correct architecture.
4. Package is generated.
5. Package contents inspect correctly.
6. Package installs in a safe test environment.
7. Runtime behavior is validated.
8. Uninstall/recovery path is validated.


### 4.8 Breakpoint
A stable handoff snapshot.

A breakpoint records enough context for the project to be safely resumed later.

Breakpoints are mandatory before high-risk transitions and strongly recommended before stopping work.


### 4.9 Current State
The latest accurate summary of the project.

Current State should separate:

- validated facts
- partial results
- failures
- blockers
- unknowns
- next actions


### 4.10 Assistant Notes
Instructions for a future assistant or future session.

This section should include:

- what not to assume
- what not to repeat
- known traps
- preferred working style
- next commands
- important files
- active constraints

### 4.12 Current Breakpoint State

LogDoc V2 introduces an optional machine-readable state file: `CURRENT_BREAKPOINT_STATE.json`.

The Current Breakpoint State is a compact continuity packet derived from the latest LogDoc breakpoint.

It is not an independent competing source of truth. The human-readable LogDoc remains the narrative and decision record. The JSON file exposes the latest safe state in a format that humans, assistants, scripts, dashboards, and team workflows can consume quickly.

A session cannot be closed until:

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


---

## 5. Required LogDoc sections
A full LogDoc should contain these sections.


### 5.1 Header
Must include:

 - project name
 - last updated date/time
 - owner/operator
 - current phase
 - current version/checkpoint


### 5.2 Project Goal
Must include:

 - active goal
 - non-goals
 - success criteria
 - failure criteria


### 5.3 Definitive Knowns
Must include the stable facts required to avoid repeated rediscovery.

Recommended subsections:

 - environment
 - target
 - repository state
 - artifact state
 - dependency state


### 5.4 Current State
Must separate:

 - validated
 - partially validated
 - not validated
 - blocked
 - deferred


### 5.5 Risk Model
Must include:

 - high-risk actions
 - safe assumptions
 - recovery paths
 - preservation notes


### 5.6 Current Plan
Must include:

 - current phase
 - immediate next step
 - expected result
 - versioning data (project and implimentation dependent)
 - follow-up if it succeeds


### 5.7 Iteration Notes
Must record meaningful attempts.

Each entry should include:

 - timestamp
 - action
 - command/change
 - result
 - interpretation
 - next action


### 5.8 Timeline
Must summarize major events and milestones in order, covering events in series with minimal discontinuity.
The timeline should avoid excessive raw logs. It should compress the project history into useful operational memory.


### 5.9 Validation Ladder
Must define the staged validation path.
The ladder should prevent overclaiming.


### 5.10 Breakpoints
Must preserve handoff snapshots, with a LogDoc versioning update (v1.12 -> v1.13)
Should occur while the project is at a neutral state, or at a milestone achievement 


### 5.11 Notes for Future Assistant / Future Operator
Must include context restoration instructions and the project's last-state and last-neutral working state dependent information.


---

## 6. Update cadence
During active technical iteration, update the LogDoc every 5–15 minutes or after any meaningful state change.

Meaningful state changes include:

 - a new error signature
 - a fix
 - a failed fix
 - a changed scope boundary
 - a generated artifact
 - a validation pass
 - a validation failure
 - a risk boundary change
 - a handoff point
 - a stop/pause/branch decision (breakpoint)

The cadence is flexible. The purpose is continuity, not paperwork.


## 7. Classification of results
Each major result across all check, hygine, breakpoint, and workflow fields should be classified.
Recommended classifications:

 - VALIDATED
 - PARTIAL
 - FAILED
 - BLOCKED
 - DEFERRED
 - UNSAFE
 - UNKNOWN
 - SUPERSEDED

### 7.1 Classification definitions
The result has been tested enough to rely on for the current phase.

VALIDATED

> The result has been tested, matching the full claim

PARTIAL

> The result shows progress but does not prove the full claim.

FAILED

> The attempt did not work.

BLOCKED

> The work cannot continue without resolving a dependency, missing fact, or external constraint.

DEFERRED

> The work is intentionally postponed.

UNSAFE

> The action or result carries unacceptable risk for the current phase.

UNKNOWN

> The result is not yet understood, or is lacking context required for a concrete approximation of expected behavior

SUPERSEDED

> The result was once relevant but has been replaced by newer information.


---

## 8. Breakpoint requirements
A breakpoint within the timeline should include (immediately proceeding current timeline information):

Breakpoint label, LogDoc version:
Date/time:
Current state:
Validated:
Not validated:
Known risks:
Artifacts:
Important commands:
Next safest action:
Do not do next:
Safe to pause here:

Breakpoints should be concise but complete.


---

## 9. Validation language, informal schema suggestions
LogDocs should avoid overclaiming.

Use precise language:

Preferred:

>- Host-side package generation is validated.
- Device-side runtime behavior is not validated.
- The current no-op package proves packaging mechanics only.
- The compatibility scope is limited to the tested target.<

Avoid:

>- It works.
- Fully supported.
- Production ready.
- Compatible with everything.
- Safe.
- Done.<

Unless those claims are actually proven.

### 9.1: LogDoc Hygiene Practices
- Perform manual or git-based stale wording scans 
- Generate artifact "sanity check" scans for local environment sanity checking pre-push 
- Move obsolete artifacts (scripts, documentation, etc) into a centralized git directory (Recommended: /docs/obsolete/*)
- Use sanity scripts and hygiene practices alongside LogDoc breakpoints, milestones, and updates

---

## 10. Safety rules
When a project includes fragile devices, production systems, user data, or irreversible operations, the LogDoc must explicitly separate:

 - safe host-side actions
 - risky target-side actions
 - destructive operations
 - recovery paths
 - actions that must not be taken casually

High-risk actions should not be hidden inside general task lists.


---

## 11. Source control relationship
A LogDoc is not a replacement for Git.

### Recommended relationship:
Git records exact source changes.
The LogDoc records why changes happened, what was tried, what failed, and what is safe to do next.
README files describe the final public state.
The LogDoc preserves the working process and handoff state.

For public projects, the LogDoc may be trimmed, redacted, summarized, or split into an attached operations log.


---

## 12. Publication model
A project developed with LogDoc Loop may publish:

 - the final README
 - the reproducibility guide
 - selected LogDoc excerpts
 - a milestone map
 - a case study
 - a redacted full LogDoc

The raw LogDoc may contain private paths, secrets, device details, passwords, or unsafe commands. It should be reviewed and sanitized before publication.


---

## 13. Minimal compliance
A minimal LogDoc Loop project should have filled sections for the:

- active goal
- definitive knowns
- current state
- current blocker
- next safe action
- timeline
- breakpoints

A full LogDoc Loop project should have all sections defined in this specification.


---
## 14. Philosophy
LogDoc Loop does not replace engineering judgment.

It is a compression and continuity layer for human-led technical work.

The human remains responsible for deciding:

 - what to run
 - what to trust
 - what to publish
 - what to delete
 - what to install
 - what to claim
 - what risks are acceptable