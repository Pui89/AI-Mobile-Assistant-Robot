# PUI89 AI NOMAD — Preliminary Mechanical, Layout and Battery Requirements

**Status: PROPOSED ENGINEERING BASELINE — NOT A BUILD SPECIFICATION.** No components have been selected or purchased. No prototype measurements, runtime, drive performance, ingress rating, fire performance or physical safety validation are established.

## 1. Product envelope

| Item | Design target | Evidence status |
|---|---:|---|
| Width | 28 cm | Proposed; not measured |
| Depth / length | 22 cm | Proposed; not measured |
| Body height | 45 cm, excluding extended handle | Proposed; not measured |
| Complete mass | ≤ 8.00 kg including battery | Proposed; not measured |
| Mobility | Four protected wheels | Concept only |
| Initial environment | Smooth indoor floors and suitable paved paths | Proposed operating boundary; not validated |

The compact envelope is a design constraint, not proof that the required components fit. Handle extension, wheel guards, turning clearance, service access and sensor fields of view must be included in CAD packaging.

## 2. Recommended wheel architecture

**Preferred candidate: two powered drive wheels plus two passive swivel support wheels.**

- Place the two independently controlled powered wheels on a common left/right drive axis, provisionally near the loaded centre of mass.
- Use one passive swivel support wheel toward the front and one toward the rear to complete the four-point support arrangement.
- Differential drive provides forward/reverse travel and steering by changing left/right wheel speeds; it avoids a separate steering linkage.
- Recess and guard wheel openings to reduce accessible pinch points. Guards must not trap debris or prevent inspection.
- Keep the battery low and near the centreline to reduce the centre-of-gravity height and avoid excessive front/rear loading.
- Provide a manual, power-off pull/transport mode only after wheel drag, handle strength, stability and pinch risks are assessed.

**Why this candidate:** it is a relatively simple, low-part-count starting point for a lightweight compact robot. It is preferred over four powered wheels for initial mass, wiring and control simplicity, and over legged locomotion for this small-footprint everyday-assistant role.

**Known limitations:** passive casters can flutter, snag or lose stable orientation on seams and uneven surfaces. A two-drive/two-caster layout is not suitable evidence for stairs, kerbs, deep sand, mud, loose gravel, steep slopes or rough trails. If later tests show caster instability or poor traction, reassess a four-powered-wheel layout; do not silently change the design.

Wheel diameter, tread, material, axle position, caster offset, ground clearance, motor torque, gearing, speed, braking method, slope limit, turning radius and payload remain **TBD**. They must be calculated from the final loaded mass and tested surface envelope before hardware selection.

## 3. Packaging and component placement principles

1. **Lowest zone:** wheels, drive motors, guarded mechanical parts and structural chassis.
2. **Low central zone:** battery pack and battery protection, secured against movement and impact.
3. **Central protected zone:** compute board, motor controller, power distribution and serviceable connectors; separate noisy motor wiring from low-level sensor wiring.
4. **Upper zone:** cameras and other selected sensors, positioned only after field-of-view and privacy reviews; keep the centre of mass low.
5. **Top / handle zone:** status indicator and user controls; keep the handle retractable and prevent it from blocking sensors.

This is a placement strategy, not a dimensioned CAD layout. Thermal paths, ventilation, electromagnetic compatibility, connector access, drainage, cable strain relief and enclosure serviceability require detailed design. Do not seal an enclosure without a verified thermal plan.

## 4. Preliminary 8 kg mass allocation

| Subsystem | Planning allocation |
|---|---:|
| Outer enclosure and body panels | 0.95 kg |
| Structural chassis and brackets | 0.65 kg |
| Two drive motors, gearboxes and mounts | 0.90 kg |
| Four wheels / casters and hubs | 0.55 kg |
| Battery pack and BMS | 1.20 kg |
| Compute and control electronics | 0.45 kg |
| Sensors and sensor mounts | 0.55 kg |
| Fuses, power distribution and protection | 0.35 kg |
| Wiring and connectors | 0.25 kg |
| Thermal management | 0.15 kg |
| Retractable handle | 0.45 kg |
| Guards, fasteners and service features | 0.35 kg |
| User interface and audio | 0.25 kg |
| Unallocated engineering margin | 0.95 kg |
| **Total ceiling** | **8.00 kg** |

All values are **planning allocations only**, not measured component masses or a bill of materials. The 0.95 kg margin is not permission to exceed 8 kg. Replace every allocation with supplier-documented and then measured mass as design maturity increases. If the verified sum exceeds 8 kg, redesign; do not omit the battery, guards or safety components to meet the target.

## 5. Battery and electrical safety requirements

No battery chemistry, cell count, nominal voltage, capacity, connector, charger or runtime is selected in this document.

Before selection, define the required operating time and duty cycle, peak and continuous motor demand, compute/sensor load, reserve energy, charging interval, storage conditions and transport requirements. Then review a traceable battery pack and charger specification against those requirements.

Minimum design requirements:
- Use a traceable, appropriately documented battery pack with a compatible battery-management system (BMS); verify cell/pack protection limits against the selected cells and load.
- Provide appropriately rated overcurrent protection close to the battery, protected wiring/connectors, strain relief, polarity protection and a serviceable isolation method.
- Monitor battery and relevant power-electronics temperatures; define conservative derating and shutdown thresholds from component specifications and validation.
- Physically separate and protect the battery from wheel debris, impact, moisture paths and accessible user contact.
- Use a compatible charger and protected charge interface. Charging while operating is prohibited unless separately engineered and validated.
- Define abnormal-event handling for impact, swelling, unusual heat, odor, smoke, water ingress, undervoltage and BMS faults. Inhibit operation and require inspection after a suspected battery incident.
- A physical emergency-stop control and motor-power isolation must be designed independently of AI software and network availability. The actual stopping behaviour must be tested with the selected drive system and load.
- Do not charge unattended during development. Follow the battery and charger manufacturer's documented handling and storage instructions.

These are requirements, not evidence that protective hardware exists. Do not claim fireproof, fire-resistant, waterproof or IP-rated performance without appropriate tests of the complete assembly.

## 6. Safety and operating requirements

- Owner supervision is required; no unsupervised roaming or emergency-response use.
- Start in a restricted, low-speed, smooth-floor test envelope after an approved test plan exists. Numeric speed and stop-distance limits are TBD and must be justified by testing.
- Loss, staleness or conflict in localization, obstacle sensing, motor feedback or battery-health evidence must inhibit new movement proposals and request the validated safe state.
- Software safe-stop requests do not prove that the physical robot has stopped. Verify braking/coast behaviour, stopping distance and power-loss response on the actual configuration.
- No autonomous stair, kerb, road-traffic, water-entry, flood, steep-slope or unknown-terrain operation.
- Minimize camera/audio/location collection; provide clear sensing status, access controls and retention limits.
- No physical movement is authorized by this document. All software interfaces remain mock, proposal-only or simulation-only until separately reviewed and approved.

## 7. Engineering gates before component selection or physical trials

1. Freeze use cases, user supervision, payload target and the permitted floor/path conditions.
2. Produce dimensioned CAD including handle, wheels, guards, battery, service access and sensor fields of view.
3. Calculate loaded centre of mass, static tip margin, wheel loading, motor torque, gearing, traction, braking and thermal loads.
4. Complete a traceable component-level mass ledger and confirm the complete design remains ≤8.00 kg.
5. Review battery/charger/BMS documentation, electrical protection, wiring, thermal design and abnormal-event procedures.
6. Complete software-only fault tests and a documented hazard review.
7. Only after the above gates and explicit approval, plan guarded, instrumented bench tests and staged supervised trials in a controlled area.

Record design revision, component identifiers, mass measurements, calculation methods, test conditions, calibration, failures, reviewers and dates. Publish only the envelope actually demonstrated.

## 8. Explicit unknowns

Payload, runtime, battery capacity, voltage, wheel size, ground clearance, speed, stopping distance, turning radius, slope, surface compatibility, noise, weather exposure, water ingress, fire performance, sensor accuracy and field reliability are all **not established**.

**Decision recorded:** use the two-powered-wheel plus two-passive-caster layout as the preferred candidate for the next CAD and engineering study. This is a design recommendation, not a final hardware selection or authorization to build.
