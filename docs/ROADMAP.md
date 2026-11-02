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

## HOMEGUARD AI NOMAD — physical product roadmap (PROPOSED)

This is a separate hardware-development track. It does not change the current software status or imply that a physical robot exists.

### NOMAD Stage N0 — Requirements and product definition
- [ ] Confirm intended users, Home / Travel / Camping operating profiles and supervised-use boundaries.
- [ ] Validate portability goals: approximately 8 kg total mass and maximum 50 cm overall height.
- [ ] Define payload, runtime, charging, ground clearance, terrain, slope, weather and noise requirements.
- [ ] Complete preliminary hazard analysis for battery, heat, water ingress, tipping, pinch points, moving wheels, privacy and emergency stop.

### NOMAD Stage N1 — Mechanical and electrical feasibility
- [ ] Produce dimensioned CAD and mass budget for body, wheels, motors, battery, sensors and enclosure.
- [ ] Check centre of gravity, static/dynamic stability, wheel traction, braking and safe lifting.
- [ ] Review battery chemistry, cell protection, BMS, fusing, isolation, thermal monitoring and charging safety.
- [ ] Define weather-protection targets and test methods; do not claim fireproof or explosion-proof performance.

### NOMAD Stage N2 — Sensor and navigation bench tests
- [ ] Evaluate low-light camera, suitable thermal sensor, 360-degree obstacle detection and outdoor GPS.
- [ ] Test local navigation, offline operation, localization-loss detection and safe-stop behaviour.
- [ ] Measure sensor limitations, false alerts, missed events, power use and environmental operating range.

### NOMAD Stage N3 — Supervised prototype
- [ ] Build only after the mass, power, mechanical, safety and cost budgets are feasible.
- [ ] Test in controlled private areas with human supervision and physical emergency stop.
- [ ] Verify conditional return-to-owner and safe-stop behaviour under GPS loss, low battery, blocked routes and communication loss.
- [ ] Test Home, Travel and Camping modes separately and publish measured results with methods.

### NOMAD Stage N4 — Controlled field evaluation
- [ ] Conduct documented weather, terrain, endurance, noise, durability and privacy evaluations.
- [ ] Assess wildlife alerts as uncertain observations; never chase, approach, trap or deter animals.
- [ ] Obtain qualified engineering and regulatory review before any public or safety-critical deployment.
- [ ] Publish limitations and unresolved hazards before partner demonstrations.

**Release rule:** the 8 kg / 50 cm targets remain PROPOSED until a physical prototype is weighed and measured. No capability becomes TESTED, MEASURED or VERIFIED without reproducible evidence. Keep hardware purchases and paid services outside the plan until a separately approved funding source exists.
