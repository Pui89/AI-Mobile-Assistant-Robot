# PUI89 AI NOMAD — Product Definition v1.0

## Product identity

**Name:** PUI89 AI NOMAD  
**Category:** AI-enabled smart travel luggage / suitcase-form mobile assistant  
**Form factor:** Upright hard-shell suitcase, four compact wheels, telescopic pull handle, removable battery and internal storage  
**Primary role:** Carry personal travel items and provide local AI travel/environment awareness.  
**Secondary future role:** Supervised low-speed mobility assistance in permitted controlled areas outside aircraft and restricted spaces.  
**Stage:** Concept and requirements definition only.

## User problem

Travelers need one portable object that combines conventional luggage handling with useful, privacy-conscious local intelligence: status awareness, trip reminders, nearby obstacle awareness, device/battery monitoring and clear evidence of events. The product should remain practical when all AI and powered mobility functions are switched off.

## Form and industrial design

The first visual impression must be a premium carry-on-style suitcase, not a robot chassis:
- upright rectangular/rounded hard-shell body with a luggage-like front, side panels, corner protection and secure storage;
- four compact protected wheels integrated into the base;
- retractable telescopic manual pull handle and a separate carry grip;
- clean luggage seams, serviceable panels, lockable storage and protected sensor windows;
- PUI89 deep navy, electric cyan and titanium/silver detailing;
- sensors are discreet and do not make the product look like a surveillance device.

### Preliminary package envelope
- Width: 30–33 cm.
- Depth: 35–40 cm.
- Body height: 35–40 cm, excluding an extended handle.
- Final external dimensions must include wheel housings, feet, corner guards, handle recesses and every protrusion.
- The proposed overall envelope is cabin-size-oriented and designed to remain within a commonly referenced 56 × 45 × 25 cm example by dimensions only. It is not a certified cabin-baggage size; carrier rules differ and mass remains a separate constraint.

### Mass and storage
- Complete robot target: 8–10 kg.
- Absolute design ceiling: 12 kg, including battery, wheels, handle, wiring, compute, sensors, enclosure and fasteners.
- Payload and internal usable volume: TBD after packaging and structural design.
- Do not market the device as lightweight until the assembled product is weighed.

## Operating modes

| Mode | Intended behaviour | Drive state |
|---|---|---|
| Travel | Owner pulls or pushes it like ordinary luggage; status and reminders available where permitted | Disabled |
| Flight | Device fully powered off; comply with carrier battery/baggage instructions | Disabled and isolated |
| Robot | Future supervised mobility in an approved controlled area outside aircraft/restricted spaces | Only through independent safety controller |

A physical selector/interlock should make mode unambiguous. Software mode labels alone are not sufficient protection. Power restoration, reboot, network reconnect or charging must never cause unexpected motor movement.

## Capability scope

### Essential first release
1. Suitcase body, four passive/rolling wheels, carry grip and telescopic pull handle.
2. Secure luggage compartment and service access.
3. Removable battery architecture and clear power isolation.
4. Local device status: battery, temperature, mode and fault.
5. Camera input and image-quality assessment.
6. Object/obstacle detection and indoor scene awareness as advisory outputs.
7. Local dashboard, trip checklist, reminders and event log.
8. Explicit uncertainty, privacy controls and human oversight.

### Later / optional
- Calibrated depth or stereo perception.
- Local voice interaction.
- Outdoor location context / GNSS.
- Tamper or luggage-separation sensing.
- Supervised low-speed movement in a private, controlled environment.
- Owner-following research only after consent, identity-safe pairing and crowd/collision validation.
- Additional travel services only where data is lawful and available offline.

### Explicitly excluded
- Autonomous movement in an aircraft, airport security zone, boarding bridge or other restricted area.
- Ride-on or passenger-carrying function.
- Unsupervised public-space following or roaming.
- Facial recognition, biometric identification, covert recording or person scoring.
- Claim of universal cabin baggage acceptance or airline/IATA certification.
- Claim of a built prototype, validated navigation, obstacle avoidance or battery safety before evidence.

## Air-travel requirements

The product is designed to resemble travel luggage, but shape alone does not guarantee acceptance. Airline rules vary by carrier, route, cabin class and aircraft. The design must be reviewed against a named carrier/route and the actual baggage allowance.

- Record measured external dimensions and mass, including wheels, handle and all protrusions.
- Record battery chemistry, rated Wh, voltage, cell configuration, protection and pack markings.
- Battery must be removable and safely isolated; define tool-free or tool-light removal and terminal protection.
- Define separate procedures for cabin carriage and checked baggage.
- If checked, the battery may need to be removed and carried in the cabin; verify current carrier rules.
- Power off completely for flight. Do not charge, drive or operate motors onboard.
- Confirm whether a powered smart bag or self-propelled luggage is accepted at all by each operating carrier.
- Some cabin baggage allowances are below the proposed 8–10 kg mass target; the product may need to travel as checked baggage or may not be accepted on a given itinerary.
- Do not claim approval from generic guidance. Obtain carrier confirmation for the exact itinerary and product configuration.

## AI architecture

Sensors and device telemetry → provenance/quality gate → local perception → travel/luggage WorldState → task intelligence → independent safety supervisor → bounded proposal → dashboard/evidence.

Shared AI Core contracts: Observation, WorldState, ActionProposal, FailureReport. Every input must carry source, timestamp, quality, calibration (where relevant), uncertainty and explicit missing/stale/conflict state.

## Development sequence

Requirements and airline target → suitcase CAD and mass closure → software-first local perception/dashboard → simulation and negative tests → bench integration with drive disabled → independent motion-safety design → controlled low-speed prototype → airline-specific baggage review and supervised travel validation.

## Evidence status

Everything in this definition is proposed. No hardware selected, bought or integrated; no measured dimensions or mass; no airline approval; no physical robot; no field or safety validation is claimed.
