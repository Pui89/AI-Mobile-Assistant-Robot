# PUI89 AI NOMAD — Development Roadmap

## Stage 1 — Travel-suitcase product definition
- [x] Establish suitcase form factor, four wheels and retractable manual pull handle.
- [x] Define Travel Mode versus future supervised Robot Mode.
- [x] Set preliminary body envelope and complete-mass target/ceiling.
- [x] Define removable battery and airline-review requirement.
- [ ] Complete CAD packaging, storage volume, wheel/handle geometry and centre-of-gravity analysis.
- [ ] Confirm a target airline/route/cabin class and obtain current baggage/battery requirements.

## Stage 2 — Software-first luggage intelligence
- Camera input and image-quality validation.
- Object/obstacle detection and scene understanding.
- Local status dashboard, events and evidence log.
- Battery/device-state interfaces using mock data until hardware exists.
- Privacy, uncertainty and stale-data tests.

## Stage 3 — Mechanical and electrical bench
- Hard-shell enclosure, four protected wheels, handle, lock and storage.
- Removable battery architecture, BMS, fuse, isolation and thermal safety.
- Mass closure against 8–10 kg target and 12 kg absolute ceiling.
- Bench-only camera, compute and telemetry integration; no drive activation.

## Stage 4 — Robot Mode simulation and safety design
- Simulate wheel geometry, turning, braking, obstacles, mode transitions and faults.
- Independent motion controller, emergency stop, watchdog and manual override.
- Test safe stop under sensor loss, communication loss, low battery and wheel jam.
- No public-space or airport autonomous operation.

## Stage 5 — Controlled physical prototype
- Low-speed, unloaded, closed-area trials only after safety review.
- Measure braking, turning, stability, wheel obstruction, thermal, battery and runtime.
- Expand payload and environment only after acceptance criteria are approved and passed.

## Stage 6 — Air-travel and product validation
- Measure final external dimensions including wheels and all stowed protrusions.
- Measure total mass and battery Wh with traceable instruments.
- Review applicable airline and route-specific smart-baggage rules.
- Obtain written carrier confirmation where required; test no flight mode on board.
- Review privacy, reliability, maintenance, serviceability and release readiness.

No stage implies a physical prototype, airline approval or validated capability until evidence is attached and reviewed.
