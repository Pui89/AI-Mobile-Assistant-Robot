# PUI89 AI NOMAD — System Architecture

**Product:** suitcase-form AI mobile assistant; four compact wheels and retractable manual pull handle.  
**Status:** target architecture only; no complete robot, integrated sensor suite or autonomous mobility is claimed.

## Operating modes

### Travel Mode (default)
- Manual pulling/pushing by the owner.
- Powered drive disabled and positively indicated.
- Battery/air-travel status, luggage status and local AI assistance where permitted.
- No autonomous movement in airports, aircraft, security areas or restricted spaces.

### Robot Mode (future, supervised)
- Available only in permitted controlled areas outside aircraft.
- Low-speed movement proposal and control through a separately engineered motion controller.
- Independent emergency stop, braking, watchdog, manual override, obstacle protection and operating-area constraints.
- Any following/escort feature remains research-only until identity-safe consent, collision and crowd safety are validated.

Mode transitions require deliberate owner action, interlocks and a verified state. Loss of required safety signals must lead to a safe stop.

## Data flow

1. Sensor acquisition: RGB, optional depth, IMU, wheel encoders, battery/device telemetry and optional GNSS or audio.
2. Input validation: timestamp, source, quality, calibration, frame, freshness and permission checks.
3. Perception: image quality, object detection/classification, tracking, segmentation, scene understanding and spatial cues.
4. NOMAD WorldState: luggage state, travel context, visible obstacles, free-space, device health, mobility state, mode and uncertainty.
5. Task intelligence: reminders, travel assistance, inspection/status events and bounded mobility proposals.
6. Independent safety supervisor: mode interlocks, area restrictions, speed/torque limits, watchdog, stop and fault handling.
7. Operator interface: mode, battery, temperature, warnings, evidence, manual override and emergency-stop status.
8. Evidence: source/time/model/configuration, uncertainty, faults, operator review and test outcome.

## Shared AI Core contracts

- Observation
- WorldState
- ActionProposal
- FailureReport

All records preserve provenance, timestamp, quality and uncertainty. Missing, stale or conflicting information remains UNKNOWN/CONFLICT. AI and language models may recommend; they never directly authorise actuator commands.

## Compute strategy

Local-first, CPU-first and offline-capable. Optional accelerator only after RAM, latency, power, thermal and provenance checks. No cloud inference, paid API, metered service or automatic model download.

## Physical architecture candidates

Hard-shell travel enclosure; four compact protected wheels; retractable manual handle; secure storage cavity; removable battery; protected power distribution; optional RGB/depth camera, IMU, encoders and telemetry; local compute; physical emergency stop and independent motion controller required before powered mobility.

No manufacturer, part number, origin, supplier, price or hardware integration is confirmed. See Product Definition and Hardware & Mass Budget for the engineering gates.
