# HOMEGUARD AI NOMAD — Concept Design

**Status:** PROPOSED / VISUAL CONCEPT ONLY  
**Implementation status:** the existing software foundation is a simulation-only building-condition demonstrator. The mobile robot is not built, integrated, field-tested or certified.

## 1. Design intent

NOMAD is a compact, owner-supervised mobile awareness platform that may extend HOMEGUARD from a fixed building evidence system into selected indoor and outdoor environments.

The design direction is a low, wide four-wheel rover with:
- a protected central chassis for battery and compute hardware;
- guarded all-terrain wheel modules;
- a raised sensor mast for a planned 360-degree awareness view;
- a forward sensor pod for obstacle awareness;
- visible status lighting and an accessible emergency stop;
- modular, replaceable sensor mounts;
- a sealed enclosure concept with serviceable access panels.

The SVG in [homeguard-ai-nomad.svg](images/homeguard-ai-nomad.svg) is an illustrative engineering concept. It is not a manufacturing drawing or proof of physical performance.

## 2. Intended operating profiles

| Profile | Intended role | Boundary |
|---|---|---|
| Home | Supervised patrol of approved rooms and routes; report relevant changes | Not a certified alarm, access-control system or replacement for residents |
| Travel | Accompany the owner in a defined, permitted area | Owner supervision and local rules apply |
| Campsite | Quiet environmental awareness and event reporting | No guarantee against wildlife, intrusion, fire or other hazards |
| Return / safe stop | Return to a known safe point when route confidence and battery reserve permit | If safety cannot be established, stop and alert rather than continue blindly |

## 3. Proposed sensing architecture

Sensor choices depend on validated hardware, privacy review and operating conditions. Candidate inputs may include:
- RGB or low-light imaging for navigation and scene context;
- range/depth sensing for obstacle distance;
- thermal sensing for temperature patterns;
- inertial sensing and wheel odometry for motion estimation;
- GNSS outdoors where available;
- environmental sensing where a specific sensor has a defined and validated purpose.

A sensor reading is evidence, not a diagnosis. Each observation should retain source, timestamp, location, quality, calibration state and uncertainty. Missing, stale or conflicting evidence must not silently become a normal/clear state.

## 4. Safe automation concept

1. **Observe:** collect only the approved sensor streams for the selected profile.
2. **Validate:** check timestamps, sensor health, calibration, range and data quality.
3. **Localise:** estimate position and confidence within the permitted map or operating boundary.
4. **Assess:** compare observations with documented baselines and explain uncertainty.
5. **Recommend:** create a human-readable event with evidence and limitations.
6. **Escalate:** notify the owner or responsible person where communication is available.
7. **Stop or return:** choose a safe stop or return only when localisation, route and battery conditions meet explicit thresholds.

No autonomous physical intervention, firefighting, door control, electrical switching, confrontation or emergency-response substitution is in scope for this concept.

## 5. Protective engineering requirements to investigate

- Battery cell selection, battery-management system, fusing, current limits, thermal monitoring and safe charging.
- Electrical isolation, wiring protection, connector retention and fault containment.
- Enclosure material selection for specified temperature, flame and ingress requirements.
- Mechanical guards, pinch-point control, tip-over stability and low-speed collision-energy limits.
- Emergency stop, watchdog, manual recovery and safe-state behaviour.
- Defined operating limits for rain, dust, heat, cold, slopes, loose ground and water exposure.

“Fire-resistant” is not “fireproof”. Preventing the robot from becoming an ignition source is different from surviving an external fire. Explosion protection and blast survival are different engineering problems. No such rating is claimed. Operation in a classified hazardous atmosphere would require a design assessed and certified for the exact environment.

## 6. Development gates

| Gate | Evidence required before proceeding |
|---|---|
| A — software concept | Requirements, simulation scenarios, safety hazards and traceable reports |
| B — digital simulation | Repeatable navigation, obstacle and fault-injection tests with recorded failure cases |
| C — bench prototype | Reviewed components, battery safety plan, emergency stop and supervised bench tests |
| D — controlled pilot | Site permission, privacy review, risk assessment, trained supervisor and independent checks |
| E — field claims | Measured repeatable evidence for each claimed environment and capability |

Do not skip gates. Simulation success is not proof of real-world safety or reliability.

## 7. Non-goals

NOMAD is not designed as a weapon, explosive device, firefighting robot, hazardous-material handler, law-enforcement system or guaranteed wildlife deterrent. It must not approach a suspected fire, explosion, gas leak or other dangerous area merely to investigate. People should follow certified alarms and established emergency procedures without waiting for NOMAD or AI analysis.

## 8. Evidence labels

- **PROPOSED:** design or capability idea only.
- **IMPLEMENTED:** source code exists.
- **TESTED:** an identified automated test passed.
- **SIMULATION-ONLY:** evaluated only with synthetic or simulated inputs.
- **MEASURED:** quantitative result with a documented method.
- **VERIFIED:** reproducibly checked against stated criteria.
- **NOT_VALIDATED:** real-world performance has not been established.
