# PUI89 AI NOMAD — AI Carry-On Suitcase Robot

**Product identity:** suitcase-form AI mobile assistant  
**Design direction:** compact upright travel suitcase with four wheels, retractable pull handle and removable battery  
**Tagline:** Your Intelligent Guardian. Wherever You Go.  
**Status:** Stage 1 — product definition and engineering requirements. Concept only; no physical prototype, airline approval or validated mobility is claimed.

![PUI89 AI NOMAD — suitcase-form mobile assistant](docs/images/ai-nomad-compact-four-wheel.svg)

*Concept illustration only. It shows the intended suitcase form, not a built or tested product.*

## Product definition

**PUI89 AI NOMAD is a smart travel-suitcase-shaped AI assistant that can be manually pulled like luggage in Travel Mode and may provide supervised, low-speed mobile assistance in Robot Mode outside aircraft and restricted areas.**

It must look and behave first like a premium piece of travel luggage:
- upright, compact hard-shell suitcase body with protected corners and serviceable panels;
- four compact, recessed/protected wheels;
- telescopic retractable pull handle for ordinary manual luggage handling;
- secure storage compartment for personal travel items;
- removable, protected battery pack;
- local AI perception and travel-context assistance;
- clear Travel / Robot mode separation, with physical power/mode control and emergency stop for future prototype testing.

NOMAD is **not** a quadruped, dog-shaped robot, four-wheel cargo cart, rideable suitcase, autonomous airport vehicle or aircraft cabin robot. The four wheels are integrated into a luggage-style body. Sentinel is the separate four-legged quadruped product; AI HOME is a separate indoor assistant.

## Travel-first product direction

1. **TRAVEL MODE — luggage first.** Wheels roll only through manual pulling/pushing by the owner. The robot drive system is disabled; no autonomous following or powered movement in airport terminals, boarding areas, aircraft cabins or other restricted spaces. For air travel, power down and comply with airline smart-baggage and lithium-battery rules. If checked baggage is required, the battery must be removable and handled separately as required by the airline.
2. **ROBOT MODE — supervised assistance.** Outside aircraft and only in permitted, controlled areas, future prototypes may support owner-supervised low-speed movement, obstacle awareness and selected assistance tasks. This mode requires independent motion control, braking, emergency stop, obstacle/people protection, area limits, manual override and validated safety controls. It is not enabled or validated today.

Changing modes must be deliberate and visible. The default state is non-powered manual luggage mode. Loss of localisation, communication, sensor confidence, battery health or safety-controller status must cause a controlled stop/safe state, not continued movement.

## Proposed physical design targets

| Item | Current design target |
|---|---|
| Form | Upright hard-shell travel suitcase / smart luggage |
| Wheels | Four compact, recessed/protected wheels |
| Handle | Telescopic manual pull handle; lockable and load-rated |
| Body envelope | About 30–33 cm wide × 35–40 cm deep × 35–40 cm high; final dimensions TBD |
| Complete mass | **8–10 kg target; 12 kg absolute design ceiling**, including battery, handle, wiring, wheels, compute and installed sensors |
| Storage | Secure internal compartment; usable volume TBD after mechanical packaging |
| Battery | Removable, protected battery pack; Wh rating and chemistry TBD |
| Payload | TBD; do not assume a payload rating or exceed total mass ceiling |
| Compute | CPU-first local processing; optional accelerator only after resource and power review |
| Appearance | PUI89 deep navy, electric cyan and titanium/silver details |

All dimensions and mass figures are proposed targets, not measured specifications. The body envelope is a luggage-form design target, **not a promise that it meets every airline's cabin-baggage dimensions**. Airlines set their own size, weight, route and aircraft limits. The 8–10 kg target (12 kg ceiling) may exceed some cabin baggage weight allowances. A specific airline, route and cabin class must be selected before claiming carry-on acceptance. If the product cannot meet the applicable cabin limit, it must be treated as checked smart baggage or not carried, subject to airline approval.

## AI and assistance capabilities — proposed

### 1. Travel and luggage intelligence
- Trip and luggage status dashboard; battery, temperature, system health and mode.
- Owner-configured travel checklist, reminders and trip timeline.
- Local location/context awareness where a permitted positioning source is available.
- Luggage presence/status and tamper/event notifications using privacy-preserving sensors.
- Optional local voice interaction and multilingual travel assistance.
- Manual-pull mode with drive disabled and clear power-state indication.

### 2. Environmental perception
- RGB camera image-quality assessment.
- Object and obstacle detection/classification for luggage, people, carts, doors and visible hazards.
- Tracking of objects for short-lived scene understanding; no facial recognition or biometric identity.
- Depth/spatial estimation only with a calibrated depth sensor; monocular estimates must not be represented as exact distance.
- Indoor scene understanding, free-space and clearance cues.
- Change/anomaly cues with confidence, uncertainty and human review.

### 3. Supervised mobile assistance
- Low-speed motion proposals in approved, controlled areas only.
- Obstacle and dynamic-object awareness.
- Wheel odometry and IMU-based movement/state estimation.
- Optional owner-following research only after consent, robust identity-safe pairing and collision-risk validation; never assume it is safe in crowded public areas.
- Manual override, stop, safe hold and supervised recovery proposals.
- No autonomous movement in aircraft, airport security zones, boarding bridges, escalators, roads or other restricted/public spaces without explicit site/operator permission and validated safeguards.

### 4. Safety and device intelligence
- Battery management interface, temperature/current monitoring and fault alerts.
- Wheel/motor current, temperature, encoder and jam monitoring where hardware is installed.
- Tip/tilt, handle-lock and enclosure-state sensing where designed.
- Sensor health, stale data, confidence and fault reporting.
- Independent safety controller and physical emergency stop before powered movement.
- Evidence log with timestamps, source, model/software version and operator review.

Every capability above is a proposed requirement until implemented and supported by appropriate software, simulation, bench or physical evidence. A dashboard or concept diagram does not prove a sensor or feature is present.

## Technology architecture

Sensors → input validation/provenance → perception → luggage/travel WorldState → task intelligence → independent safety supervisor → human-authorised bounded proposal → local dashboard and evidence log.

Shared AI Core contracts:
- Observation — source, timestamp, modality, quality, calibration, confidence and uncertainty.
- WorldState — luggage, environment, device, travel mode and mobility state, including unknown/conflicting data.
- ActionProposal — advisory travel or movement proposal, never direct actuator authority.
- FailureReport — fault, severity, safe state, evidence and recovery request.

Candidate sensors: RGB camera, optional depth camera, IMU, wheel encoders, battery telemetry, temperature sensors and optional GNSS only where useful outdoors. Microphone, speaker, wireless radios, UWB/Bluetooth and other connectivity require separate privacy, security, airline and interference review. No sensor or radio is assumed installed.

## Air-travel, battery and airline constraints

- Airline rules vary by carrier, route, cabin class and aircraft. Verify the exact route's cabin size and weight allowance before travel.
- A removable battery is a core design requirement for smart-luggage compliance.
- Battery Wh rating, chemistry, cell configuration, protection, isolation and removal procedure must be documented on the pack.
- Battery carriage limits and approval depend on Wh and airline policy. Do not design around an assumed universal allowance.
- If the bag is checked, battery removal and cabin carriage of the battery may be required. A bag with a non-removable battery may be refused.
- The robot must be completely powered off for flight; no powered wheel movement, charging or autonomous operation onboard.
- Airport security may require inspection or removal of the battery/electronics. Provide tool-light or tool-free, secure battery access without exposing live conductors.
- A powered, self-propelled or rideable suitcase can be restricted or prohibited by individual airlines. NOMAD's powered mobility mode must be disabled for air travel; acceptance must be confirmed with the airline before each trip.
- Do not claim “airline approved”, “IATA certified” or “fits all aircraft” without formal, route-specific evidence.

Reference guidance: [IATA Passenger Baggage Rules](https://www.iata.org/en/programs/ops-infra/baggage/passenger-baggage-rules/), [IATA lithium-battery passenger guidance](https://www.iata.org/en/youandiata/travelers/batteries/). These are guidance sources; the operating airline's current conditions apply.

## Prototype 1 — build order

1. **Suitcase enclosure and manual luggage mechanics:** shell, internal storage, four passive/rolling wheels, retractable handle, corner protection, locks and service access.
2. **Mass and packaging closure:** complete CAD envelope and mass ledger including battery, wheels, handle, wiring, guards, sensors, fasteners and reserves. Target 8–10 kg; absolute ceiling 12 kg.
3. **Battery and travel compliance design:** removable battery, documented Wh rating, BMS, fuse, isolation, short-circuit protection, thermal monitoring and safe removal procedure.
4. **Local AI software foundation:** camera input, image quality, object detection, scene understanding, spatial awareness, confidence, event notification and dashboard. CPU-first; no hosted inference.
5. **Static/bench electronics:** verify sensors, power, thermal and telemetry with drive disabled.
6. **Controlled robot-mode prototype:** only after a separate safety review; low-speed closed-area trials, independent controller, braking, physical emergency stop, obstacle protection and manual override.
7. **Air-travel verification:** dimensions including wheels/handles, measured total mass, battery documentation, airline review and actual acceptance evidence for specific carriers/routes.

Do not start with autonomous following or public-area driving. The first useful product is a dependable travel suitcase with a verified local AI awareness system.

## Safety, privacy and exclusions

- Human owner remains in control; default is manual luggage mode.
- No autonomous driving in aircraft or restricted airport areas.
- No ride-on, passenger-carrying, child/pet transport or load carrying beyond a separately validated payload.
- No facial recognition, biometric identification, covert recording or unrestricted surveillance.
- Camera/microphone use must be visible, consent-based, minimised and locally processed by default.
- Do not obstruct aisles, exits, evacuation routes or cabin access.
- No charging or operating the robot in flight.
- No unsafe self-start after power restoration, fault or network reconnect.
- AI does not directly control motors or bypass independent safety controls.

## Development and evidence stages

1. Product definition, airline requirements and hazard analysis.
2. Suitcase CAD packaging, mass budget and removable-battery design.
3. Software-first perception and dashboard using synthetic or permission-cleared data.
4. Simulation of luggage handling, wheel geometry, obstacles, safe stop and mode transitions.
5. Bench testing of selected sensors, compute and battery-management interfaces.
6. Controlled low-speed physical prototype tests.
7. Airline/carrier-specific review and supervised travel trials, only after approval.
8. Release review for reliability, privacy, maintainability, service and regulatory obligations.

Software tests do not validate physical mobility. Simulation does not prove airline acceptance or real-world safety. No prototype, airline approval, battery certification, payload, speed, runtime, obstacle clearance or field performance is currently claimed.

## Project links

- [English product website](https://pui89.github.io/nomad.html)
- [เว็บไซต์ผลิตภัณฑ์ภาษาไทย](https://pui89.github.io/nomad-th.html)
- [PUI89 portfolio](https://pui89.github.io/)
- [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core)

**PUI89 | Intelligent Systems. Verifiable Decisions. Safer Outcomes.**
