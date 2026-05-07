# Project Scope: Legacy iOS ARMv7 Toolchain Re-Pavement

## Project

`theros-monumental-wsl-toolkit`

## Public repo

https://git.bitcrusher32.win/bitcrusher32/theros-monumental-wsl-toolkit

## Active scope

The active project scope was to build, preserve, validate, and generalize a legacy iOS ARMv7 build environment for WSL/Linux.

The primary validation target was:

- iPhone 4s
- iOS 6.1.3
- ARMv7
- Cydia / MobileSubstrate-style environment
- Theos package workflow
- WSL Ubuntu host environment

## Non-scope

The project explicitly removed application-specific tweak behavior from active scope during toolchain recovery.

Out of active scope during the documented phase:

- FakeGPS as the primary project goal
- GPS spoofing MVP
- CoreLocation/locationd spoofing
- system-wide location spoofing
- preference UI work
- device-risky tweak behavior before host-side validation

## Why this mattered

The non-scope section prevented project drift.

Instead of jumping into risky runtime behavior, the project first validated:

1. toolchain build
2. toolchain install
3. ARMv7 Mach-O smoke tests
4. fresh reproducibility
5. Theos integration
6. no-op tweak package generation
7. safe host-side validation boundaries

## LogDoc Loop relevance

This project demonstrates several core LogDoc Loop concepts:

- definitive knowns
- current active scope
- explicit non-scope
- risk model
- validation ladder
- patch timeline
- breakpoint handoff
- publication caveats
- assistant/operator continuity

## Validation boundary

The case study should not be read as a blanket compatibility claim for all iOS versions, all ARMv7 devices, or all Theos tweak types.

The documented validation scope is limited to what the project actually tested.