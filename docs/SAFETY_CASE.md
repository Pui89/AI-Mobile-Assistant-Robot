# PUI89 AI NOMAD — Travel, Battery and Mobile-Mode Safety Case

**Status: proposed documentary baseline only. This is not a completed hazard analysis, certified product, airline approval or permission to operate a physical robot.**

## Intended product

NOMAD is a compact suitcase-form AI mobile assistant with four protected wheels, a telescopic manual pull handle, internal luggage storage and a removable battery. Its primary use is ordinary manually handled luggage with local AI travel assistance. A future supervised Robot Mode may be researched for permitted controlled areas outside aircraft and restricted airport spaces.

## Design targets

- Body envelope: approximately 30–33 cm wide × 35–40 cm deep × 35–40 cm high; final external dimensions TBD.
- Complete mass: 8–10 kg target; 12 kg absolute ceiling including battery, handle, wiring, wheels, compute and sensors.
- Removable protected battery; Wh rating TBD.
- Four compact protected wheels and load-rated telescopic pull handle.
- Payload, storage volume, wheel/motor layout, speed, runtime, braking distance, turning clearance and environmental limits TBD.

These are design targets only. The dimensions are not a guarantee of cabin acceptance. Airline size and weight limits vary. The proposed mass may exceed some cabin allowances.

## Safety principles

1. Travel Mode is the default: owner pulls/pushes the suitcase manually; drive disabled.
2. Flight Mode means fully powered down. No charging, self-propelled movement or autonomous operation onboard.
3. Battery must be removable, protected against short circuit and accessible for inspection; record chemistry and Wh.
4. Follow the current airline, route and aircraft requirements. Airline acceptance is not inferred from generic IATA guidance.
5. Future Robot Mode is permitted only in defined, controlled and authorised areas with independent safety controls.
6. AI perception and language models do not directly command motors or override safety interlocks.
7. Fail safe on uncertain mode, obstacle, localisation, communication, battery, thermal or controller state.
8. No unsupported claims about cabin acceptance, battery certification, water resistance, payload, speed, endurance or safety.

## Hazard register

| Hazard | Required controls and evidence |
|---|---|
| Cabin baggage rejection | External dimensions include wheels, handle and protrusions; measure mass; confirm route, carrier, cabin and aircraft limits before travel. |
| Lithium battery restriction/fire | Removable pack, marked Wh, protected terminals, BMS, fuse, isolation, thermal monitoring, safe removal and airline review. |
| Accidental motor activation | Physical mode switch, drive disable in Travel/Flight mode, power-off state, startup interlock and fault-injection tests. |
| Uncommanded movement | Independent controller, watchdog, brakes/drive isolation, emergency stop, manual override and low-speed bounded tests. |
| Collision/pinch/entanglement | Guard wheels and pinch zones, set speed/force limits, proximity sensing and controlled surrogate tests. |
| Tip-over/load shift | Secure compartment, centre-of-gravity and handle-load analysis, payload definition and stability tests. |
| Battery overheating | Temperature/current monitoring, suitable enclosure, BMS and independent isolation; no charging onboard aircraft. |
| Privacy breach | Visible camera/microphone state, local-first processing, data minimisation, retention limits and no biometric identification. |
| Sensor/network loss | Stale-data rejection, UNKNOWN state, stop/safe-hold and manual recovery. |
| Airline/security inspection | Tool-light battery removal, clear battery labels, service access and no claim of guaranteed security-screening acceptance. |

## Air-travel rules — engineering implications

- Airline baggage dimensions and weight allowances differ by carrier, route, cabin class and aircraft.
- Smart-baggage rules may require a removable battery; when checked, the battery may need to be removed and carried in the cabin.
- Battery Wh thresholds and operator approval depend on applicable rules and airline policy.
- Some carriers restrict powered or self-propelled luggage even where batteries are removable.
- NOMAD must be powered off during flight and must not operate its motors onboard.
- Before each trip, check current rules with the operating airline and any connecting carriers.

References: IATA Passenger Baggage Rules and IATA Safe Travel with Lithium Batteries. These are guidance, not airline approval.

## Exclusions

NOMAD is not rideable, does not carry people or animals, is not an aircraft cabin robot, and is not an autonomous airport vehicle. No face recognition, covert recording, pursuit, enforcement or unrestricted following. No operation in flight, on roads, escalators, stairs or restricted areas without specific approval and validated controls.

## Validation gates

1. Requirements, airline target and hazard analysis.
2. CAD, handle loads, enclosure and mass budget.
3. Battery/BMS and electrical safety review.
4. Software mode-interlock and negative tests.
5. Bench sensor/power/thermal tests with drive disabled.
6. Controlled low-speed mobility tests after independent safety review.
7. Carrier-specific baggage/battery review and documented acceptance evidence.
8. Independent release review.

Passing software tests does not validate physical safety or airline acceptance.
