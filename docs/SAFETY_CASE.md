# PUI89 AI NOMAD — Initial Safety Case and Validation Gates

**Status: PROPOSED / DOCUMENTARY BASELINE ONLY. This is not a completed hazard analysis, a verified safety system, a certification, or permission to operate a physical robot.**

## Intended use and boundaries

PUI89 AI NOMAD is an early-stage, owner-supervised compact four-wheel mobile-assistant concept for suitable indoor and outdoor everyday environments. Intended research areas include supervised accompaniment, carrying items within a future validated payload envelope, environmental observation and navigation assistance.

NOMAD is not an emergency responder, mobility aid, security/enforcement device, child or pet caretaker, or unsupervised roaming robot. It must not enter hazardous areas, approach road traffic, enter water, climb stairs, cross unverified terrain, or continue a mission merely to complete a task. A person remains responsible for supervision and decisions.

The current compact design targets are **28 cm wide × 22 cm long/deep × 45 cm high** (body height excluding the extended handle), with a maximum total mass of **8 kg including battery** and four protected wheels. These are proposed targets only, not measured operating limits. Payload, wheel diameter, ground clearance, speed, braking/stop distance, turning clearance, slope, terrain, weather and endurance limits remain undefined or unvalidated. The current repository does not establish a built or field-validated robot, real sensor integration, verified emergency stop, battery protection hardware, ingress rating or fire performance.

## Safety principles

1. **No motion by default in software tests.** All movement interfaces remain mock, proposal-only or simulation-only unless a separately reviewed physical test plan is approved.
2. **Human supervision.** Movement, following, carrying, recovery and restart require an accountable operator and a clearly defined supervision boundary.
3. **Fail closed on uncertainty.** Missing, stale, conflicting, implausible or uncalibrated inputs must not be interpreted as a safe path or safe operating condition.
4. **Safe stop is context-specific.** A stop request must be designed and tested for the actual wheel-drive configuration and braking behaviour, terrain and load; software alone cannot guarantee a physical stop or prevent a fall.
5. **Independent protection.** Motor-current/thermal limits, battery protection, physical emergency stop and electrical isolation must not depend solely on an AI model or network connection.
6. **No unsupported claims.** Do not claim safe stair climbing, obstacle avoidance, child/pet safety, all-weather operation, waterproofing, fire resistance, payload capacity, endurance or autonomous navigation without appropriate evidence.

## Hazard register and required controls

| Hazard area | Foreseeable failure or harm | Required design and validation controls |
|---|---|---|
| Locomotion, balance and falls | Trip, stumble, collapse, tip-over, unstable recovery, loss of balance under load or on uneven ground | Define a bounded operating envelope by wheel configuration, speed, steering, braking, slope, surface, step/threshold, payload and centre of mass. Test tip-over, wheel obstruction, braking/stop distance, recovery and fault transitions with an instrumented test setup before any supervised physical trial. No stairs, edges, steep slopes or loose/unknown terrain until separately assessed. |
| People, children and animals | Collision, fright, trapping, paw/hand injury, unexpected approach or movement near a vulnerable person | Define separation distances, speed/force limits, approach and retreat rules, visibility and human override. Test representative contact and avoidance cases with safe surrogates before people or animals are present. Never rely on AI perception alone for protective separation. |
| Joints, limbs and payload | Pinch, crush, shear, entanglement, dropped load, overload or limb obstruction | Guard accessible pinch/shear zones; define mechanical stops and torque/current limits; secure payload and prevent load shift. Validate worst-case load, wheel-drive state transition, jam, obstruction and power-loss cases. Do not carry people, animals, hazardous materials or unrestrained loads. |
| Navigation and environment | Stairs, ledges, glass, reflective surfaces, darkness, rain, puddles, mud, dust, loose ground, slopes, heat/cold or GPS/network loss cause unsafe movement | Keep the permitted environment explicit and conservative. Validate each sensor and operating condition independently; unknown or out-of-envelope terrain triggers a supervised stop/abort. GPS is not a safety sensor; loss or spoofing must not create an unsafe route. No water entry or operation in flood/current. |
| Battery, charging, electrical and fire | Cell damage, short circuit, overcurrent, overheating, charging fault, thermal runaway, electric shock or fire | Use a separately engineered battery pack, BMS, fuse/overcurrent protection, temperature monitoring, protected wiring/connectors and safe charging/storage procedure. Validate cell/pack, charger and assembled system with qualified methods. Isolate damaged or abnormal batteries; do not charge unattended or after impact/water ingress until inspected. No fire-resistant/fireproof claim without exact-system testing. |
| Water, dust and weather | Ingress through seams/connectors, condensation, corrosion, wet-ground damage, short circuit or loss of traction | Define separate exposure limits for rain, splash, puddles, humidity, dust and temperature. Design sealing, drainage, corrosion control and service access for the actual configuration. Test components and complete assembly, including joints, connectors and service panels. No IP rating or waterproof/weatherproof claim until tested. |
| Communications, software and security | Lost link, stale/replayed command, compromised update, sensor spoofing, unsafe restart or unauthorized movement | Local safety behavior must not depend on cloud or continuous network. Authenticate and validate commands; expire stale proposals; use least privilege and reviewed updates. On loss of required communications or localization, inhibit new movement proposals and request the validated local safe state. No remote movement without explicit owner authorization and safeguards. |
| Privacy, misuse and recovery | Unnecessary recording, location disclosure, unauthorized following, unsafe manual lifting/towing or restart after a fault | Minimize camera/audio/location collection; provide visible sensing status, access controls, retention limits and deletion. Require owner authorization and manual inspection for recovery after a fall, impact, ingress, battery fault or emergency stop. Provide a documented carry/lift/tow method that avoids pinch and load hazards. |

## Required operating states

The software and future hardware design must distinguish at least:

- **SUPERVISED_READY:** required checks pass within a specifically validated operating envelope; operator is present and supervising.
- **ADVISORY:** non-critical maintenance or environmental deviation; operator is informed.
- **RESTRICTED:** a bounded function or area is unavailable; no proposal may exceed the remaining verified envelope.
- **SAFE_STOP_REQUESTED:** request the project-specific stop behavior; this label does not prove that physical motion has stopped.
- **UNKNOWN_DEGRADED:** required localization, sensing, communication, battery or actuator-health evidence is missing, stale, invalid or conflicting.
- **EMERGENCY:** operator or independently validated protective system initiates the documented emergency procedure.
- **RECOVERY_REQUIRED:** movement remains inhibited pending human inspection and authorized reset.

Do not report a global NORMAL or SAFE state when a safety-relevant subsystem is unknown. Do not automatically resume after a fall, collision, emergency stop, sensor fault, loss of localization or power interruption.

## Minimum validation sequence before physical trials

1. **Requirements and hazard analysis:** define intended users, supervision, excluded environments, operating envelope, payload, foreseeable misuse and risk controls.
2. **Software-only tests:** deterministic tests for invalid/stale/conflicting observations, command expiry, lost link, localization uncertainty, emergency-stop requests, restart lockout and safe-state transitions. No hardware commands.
3. **Component evidence:** review actuator, gearbox, joint, battery, BMS, charger, wiring, connector, enclosure and sensor specifications and licences.
4. **Bench and surrogate tests:** independently approved, guarded and instrumented tests for joint limits, torque/current, thermal behavior, contact forces, braking/stop distance, power loss, falls and payload retention. Keep people and animals out of the test area.
5. **Environmental tests:** controlled ingress, humidity/condensation, dust, temperature, corrosion and post-exposure electrical/function checks for the exact assembly. No exposure beyond an approved test plan.
6. **Supervised mobility trials:** only after prior gates pass; use a controlled closed test area, trained operators, independent emergency stop, spotters where appropriate, exclusion zones, staged speed/terrain/load increments and a documented abort plan.
7. **Evidence review:** record exact hardware/software revision, method, calibration, conditions, sample counts, failures, stop performance, recovery, reviewer and date. Publish only the tested envelope.

## Mandatory abort and inspection triggers

Stop the trial and inhibit restart after unexpected motion, loss of balance, collision, joint/actuator fault, abnormal noise or temperature, battery swelling/damage, smoke/odor, water ingress, exposed wiring, sensor disagreement, localization loss, emergency-stop activation or loss of operator supervision. A qualified person must inspect and authorize recovery where risk warrants it.

## Evidence and status policy

Use **PROPOSED**, **IMPLEMENTED**, **TESTED**, **MEASURED**, **SIMULATION-ONLY**, **NOT VERIFIED** and **NOT VALIDATED** precisely. A passing software test proves only the tested software behavior. Simulation, component datasheets and concept artwork do not prove assembled-robot or field safety.

**Current conclusion:** NOMAD remains an early software/design concept. The hazards and gates in this document are requirements for future work; physical safeguards, locomotion, stability, payload, emergency stopping, battery safety, environmental protection and real-world performance remain **NOT VERIFIED / NOT VALIDATED**.

_Last reviewed: 8 November 2026 (Asia/Bangkok)._
