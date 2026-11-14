# PUI89 AI NOMAD — Compact Layout and 7 kg Target Mass Plan

**Status:** Preliminary design study only. No components are selected, purchased, assembled, weighed or validated.  
**Revised body envelope:** 30–33 cm wide × 35–40 cm long/deep × 35–40 cm high, including wheels and fixed sensor housings; retractable handle excluded from body height.  
**Complete robot mass target:** 7.00 kg, including battery and handle.  
**Maximum design ceiling:** 10.00 kg; this is not the desired build mass.  
**Operating concept:** compact, owner-supervised four-wheel mobile assistant for suitable indoor/outdoor everyday environments.

## 1. Design rules

1. The revised mass target is 7.00 kg complete, including battery, handle and all installed parts.
2. The 10.00 kg value is the maximum design ceiling, not the target. The earlier 8 kg target is superseded by this 7 kg target.
3. Total mass includes chassis, enclosure, wheels, motors, battery/BMS, computer, sensors, handle, wiring, connectors, fasteners, guards and accessories.
4. Payload is separate from robot mass; payload capacity remains TBD until stability, wheel loading, drive torque, braking and endurance are calculated and tested.
5. Do not invent subsystem mass allocations before exact candidate components and mechanical architecture are selected.
6. Keep heavy components low and near the centreline; minimise top-heavy sensor structures and unnecessary decorative or duplicated parts.
7. Do not sacrifice wheel guarding, braking, battery protection, electrical isolation, structural strength, weather-related protection or safe stopping to meet the weight target.

## 2. Preliminary packaging envelope

| Parameter | Proposed range | Initial CAD envelope |
|---|---:|---:|
| Width | 300–330 mm | 330 mm maximum |
| Length / depth | 350–400 mm | 400 mm maximum |
| Body height | 350–400 mm | 400 mm maximum |

Body height excludes the extended pull handle; total robot mass includes the handle. CAD must include the wheel sweep, ground clearance, handle attachment, service access, cable bend radius, ventilation and sensor field of view.

## 3. Component-level mass ledger — required before design freeze

| Subsystem / item | Manufacturer and exact model | Quantity | Datasheet mass (g) | Measured mass (g) | Mounts / wiring allowance (g) | Evidence / status |
|---|---|---:|---:|---:|---:|---|
| Chassis and frame | TBD | TBD | TBD | TBD | TBD | Pending |
| Enclosure and access panels | TBD | TBD | TBD | TBD | TBD | Pending |
| Wheels, motors and drive | TBD | TBD | TBD | TBD | TBD | Pending |
| Battery, BMS and containment | TBD | TBD | TBD | TBD | TBD | Pending |
| Compute and control electronics | TBD | TBD | TBD | TBD | TBD | Pending |
| Sensors and mounts | TBD | TBD | TBD | TBD | TBD | Pending |
| Pull handle and attachment | TBD | TBD | TBD | TBD | TBD | Pending |
| Power conversion, fuses and protection | TBD | TBD | TBD | TBD | TBD | Pending |
| Wiring, connectors, guards and fasteners | TBD | TBD | TBD | TBD | TBD | Pending |
| **Complete robot mass** |  |  | **TBD** | **TBD** | **TBD** | Target 7.00 kg; must not exceed 10.00 kg ceiling |

Use official datasheet masses for preliminary comparison and weigh every physical component and the assembled robot before claiming the target is achieved. Record scale resolution, configuration, battery state and included accessories.

## 4. Weight-reduction and cost-control priorities

- Optimise frame geometry around calculated load paths rather than simply choosing thinner material.
- Select motors from required wheel torque, gradient, rolling resistance, speed and duty cycle; avoid arbitrary oversizing.
- Select wheel diameter/tread for the validated terrain envelope; do not over-specify all-terrain capability.
- Consolidate controllers and power conversion only where thermal, electrical and fault-isolation requirements remain satisfied.
- Remove redundant brackets, duplicate enclosures, decorative panels and unused sensors.
- Use lightweight engineering polymers or aluminium only after strength, impact, UV, temperature, ingress and repairability requirements are checked.
- Keep the battery low and central; do not reduce cell quality, BMS protection or containment to save mass.
- Compare total landed cost in Thailand, not only component unit price.

## 5. Engineering gates before design freeze

- [ ] CAD confirms the body envelope is within 330 × 400 × 400 mm, excluding the extended handle.
- [ ] Complete component-level mass ledger targets 7.00 kg and remains at or below 10.00 kg.
- [ ] Physical weighing confirms the complete assembled mass.
- [ ] Centre-of-gravity, tip resistance and handle-load analysis are documented.
- [ ] Wheel torque, drive duty, braking, stopping distance, ground clearance and turning clearance are calculated.
- [ ] Payload and endurance targets are defined from the intended use and tested separately.
- [ ] Battery energy, peak/continuous current, BMS, charging and thermal limits are documented.
- [ ] Electrical protection, wiring, connector ratings and service isolation are reviewed.
- [ ] Environmental exposure limits are specified and tested; no waterproof or all-terrain claim is made without evidence.
- [ ] Sensor placement, field of view, calibration and localisation failure handling are documented.
- [ ] Supervised bench and controlled-route tests define pass/fail criteria and safe abort conditions.

## 6. Explicit limitations

This document does not establish that the proposed dimensions or 7 kg target are mechanically feasible. It does not establish a built robot, selected components, payload capacity, runtime, all-terrain operation, stair climbing, deep-water operation, waterproofing, IP rating, certified safety or field validation. Unknown values remain TBD.

## 7. Review record

Record each revision, reviewer, exact changed values, datasheets, calculations, physical weighing records, test conditions and unresolved risks. Distinguish target, estimate, datasheet mass and measured assembled mass.
