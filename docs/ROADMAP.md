# Roadmap

## Stage 0 — Foundation
- [x] Scope and safety boundary
- [x] Evidence and baseline contracts
- [x] Deterministic baseline-deviation engine
- [x] Synthetic three-floor scenario
- [x] JSON finding report and schema
- [x] Initial tests and CI workflow definition
- [ ] Execute CI and review results

## Stage 1 — Reliable evidence
Schema validation; UTC clock-skew and duplicate-event handling; checksums; baseline versioning; report provenance; missing-sensor and drift fault injection. Acceptance: malformed, stale, uncalibrated and missing data are never silently classified as normal.

## Stage 2 — Multi-sensor scenarios
Synthetic electrical, water, thermal, humidity, acoustic and structural channels; building/floor/room/component model; event correlation; alternative hypotheses and uncertainty.

## Stage 3 — Engineering analysis
Benchmark vibration/acoustic features; FFT/PSD and modal analysis against known synthetic signals; environmental confounder tests; report error and false-positive/negative metrics.

## Stage 4 — Partner demonstration
Dashboard, event timeline, evidence detail, sensor health and export; accessibility, localization and privacy review.

## Stage 5 — Bench and building pilot
Qualified sensor selection/calibration; professional installation; safety/privacy assessment; independent engineering review and pilot agreement. No real-world performance claim without measured, repeatable evidence.

Work one stage at a time. No paid services, subscriptions, cloud GPUs, physical purchases or unreviewed autonomous actions. Review licence, provenance and security before adding dependencies.
