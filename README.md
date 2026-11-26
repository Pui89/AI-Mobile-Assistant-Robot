# PUI89 AI NOMAD — Suitcase-Style Four-Wheel Mobile Assistant

[English](README.md) · [ภาษาไทย](README.th.md)

![PUI89 AI NOMAD suitcase-style four-wheel mobile assistant concept](docs/images/ai-nomad-concept.svg)



**A compact suitcase-style mobile assistant with four wheels and an integrated pull handle.**

[English project page](https://pui89.github.io/nomad.html) · [ภาษาไทย](https://pui89.github.io/nomad-th.html) · [PUI89 portfolio](https://pui89.github.io/)

*Concept illustration only. It is not evidence of a built, integrated, tested or validated product.*

## Product identity

PUI89 AI NOMAD is a **suitcase-style four-wheel mobile assistant with an integrated pull handle**. Its enclosure resembles a compact suitcase, and it moves on four wheels. It is a mobile-assistance robot, not a four-legged robot or ordinary luggage. Its defining product identity is a small, mobile assistant platform distinct from the indoor AI HOME robot. The handle supports user-directed handling; it does not imply autonomous following or unsupervised operation.

## Intended role

NOMAD is intended to explore helpful, user-directed mobile assistance in suitable supervised environments. Candidate functions may include:
- Context-aware user assistance and information.
- Obstacle and surrounding-environment awareness.
- Status, safety and battery-related notifications where supported by verified hardware.
- Local-first interaction and privacy-conscious data handling.
- Optional connectivity features that do not replace essential local controls.

These are proposed product directions, not verified or implemented capabilities.

## Physical design direction

| Element | Design direction | Evidence status |
|---|---|---|
| Form | Compact suitcase-style mobile assistant with four wheels and an integrated pull handle | Design direction |
| Handling | Integrated user-handling handle | Design direction |
| Mobility | Four-wheel mobile base; layout and drive system to be engineered | Design direction |
| Intelligence | Discreet embedded sensing and user interaction | Concept |
| Total mass | Preliminary target 8–10 kg; 10 kg maximum | Target only; not measured |
| Dimensions, payload and wheel layout | To be defined through product and user research | Not established |

The 10 kg figure is a preliminary complete-product design ceiling, not a measured prototype result. Dimensions, stability, handling, terrain limits and mobility performance remain to be engineered and validated.

## Safety, privacy and evidence

- Keep essential handling, power and stop functions available without an app or internet connection.
- Use human-reviewed assistance and clearly communicate uncertainty and sensor limitations.
- Do not claim autonomous travel, obstacle avoidance, follow-me operation, weather resistance, airline approval or any physical performance without repeatable evidence.
- Distinguish design proposals, implemented software, test results and validated physical capabilities.

## Development status

**Concept and early software foundations.** No completed physical product, integrated sensor suite, validated mobility performance or certification is claimed.

**Next evidence gate:** confirm the primary user journey, body dimensions, handle ergonomics, wheel layout, stability, supervised operating envelope, complete mass budget, sensor placement, power budget and measurable acceptance criteria before hardware selection.

## Shared PUI89 engineering

NOMAD may reuse versioned interfaces and evidence practices from the [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core). Its body structure, handling, four-wheel mobility, stability, power, sensors, privacy and product safety require NOMAD-specific engineering and validation.



## Latest engineering progress — 22 November 2026

**Maturity:** Implemented — early software foundation. **Evidence status:** PARTIAL. The product remains a compact suitcase-style four-wheel mobile-assistant concept; this status does not imply a built or integrated robot.

**Recent verified repository progress:**
- The suitcase-style body is the canonical product direction; references to a dog-inspired or four-legged form are incorrect and superseded.
- The intended form is a compact suitcase-style four-wheel assistant with an integrated pull handle; the 8–10 kg target and 10 kg maximum remain design targets, not measured prototype values.

**Not established:** a physical prototype, integrated sensor suite, validated mobility/stability performance, environmental protection, battery endurance or field reliability.

**Next evidence gate:** validate the primary user journey and ergonomic requirements; baseline external dimensions, handle geometry, four-wheel arrangement, stability, complete mass budget, sensor placement, power budget, privacy controls and measurable acceptance criteria before selecting hardware.

**Last reviewed:** 26 November 2026. See the [suitcase-style four-wheel identity correction PR](https://github.com/Pui89/AI-Mobile-Assistant-Robot/pull/135).

## Global manufacturing engineering

The product-specific [PUI89 Global Manufacturing Design Brief v1.0](docs/PUI89_GLOBAL_MANUFACTURING_DESIGN_BRIEF_V1.0.md) defines the preliminary product envelope, candidate material families, component architecture, global human-factors requirements, extreme-environment design strategy, manufacturing transfer package, quality gates and unresolved specifications. It distinguishes proposed targets from tested or verified performance. Candidate materials and component types are not an approved BOM; exact grades, models, dimensions and tolerances remain open until engineering analysis and validation.

## Global engineering and manufacturing control

For international engineering, factory and worker handoff, use the controlled PUI89 documents:
- [PUI89 Global Engineering & Manufacturing Portal](https://pui89.github.io/global-engineering.html)
- [PUI89 Global Manufacturing Handoff System v1.0](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_GLOBAL_MANUFACTURING_HANDOFF_SYSTEM_V1.0.md)

**Production rule:** Build, buy, substitute, inspect or release only against the exact approved product configuration, revision, drawing, BOM and work instruction. Missing or conflicting values are **STOP — DO NOT GUESS**; raise a Technical Query (TQ). The shared blank manufacturing templates are being reviewed in [PUI89 website PR #639](https://github.com/Pui89/Pui89.github.io/pull/639) and are not yet production authority.

## Future-Ready Technology Policy

This product follows the portfolio-wide [PUI89 Future-Ready Technology Policy v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/architecture/PUI89_FUTURE_READY_TECHNOLOGY_POLICY_V1.0.md). The policy requires upgradeable interfaces, evidence-based technology selection, provenance/licence review, local-first resource discipline, compatibility testing, safe fallback and controlled release scope. Technology candidates are reviewed monthly and architecture decisions quarterly. This link records policy adoption intent; it does **not** claim that model switching, hardware abstraction, sensor adapters, automated monitoring or product-level validation are already implemented.

## Product-Specific Technology Upgrade Plan

**Gartner 2026 alignment:** Physical AI, Domain-Specific Models, hybrid compute and Digital Provenance. See the [canonical portfolio policy](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/architecture/PUI89_FUTURE_READY_TECHNOLOGY_POLICY_V1.0.md).

| Upgrade area | Planned sequence (not yet a capability claim) |
|---|---|
| Context-aware assistance | Define supported contexts and conservative fallback; use traceable task/domain knowledge rather than unrestricted generic agent behaviour. |
| Vision & edge intelligence | Benchmark low-power perception and inference; measure latency, memory, energy and thermal limits on intended hardware. |
| Navigation & localisation | Specify indoor/outdoor operating envelope, localisation inputs and loss-of-localisation response; test in controlled environments. |
| Offline resilience | Define which functions remain available without network access and how stale/uncertain context is disclosed. |

**First gate:** verify the physical mobility concept and safety boundaries before integrating higher-level AI. **Status:** Planned roadmap only.


## Long-Term Technology Evolution & Anti-Obsolescence Strategy (2027–2030+)

This forward-looking roadmap extends the current P1–P4 development sequence beyond the 2026 trend baseline. It identifies evaluation horizons, not guaranteed future capabilities or fixed adoption dates. Each technology remains conditional on verified user value, provenance and licensing, target-hardware fit, safety, maintainability and reproducible evidence.

| Horizon | Product evolution focus |
|---|---|
| 2027 | Stabilize the physical mobility concept, operating envelope, low-power compute budget, offline feature set and safe human-override behaviour. |
| 2028 | Evaluate efficient vision/context models, localisation and navigation assistance; quantify battery, thermal, latency and connectivity trade-offs. |
| 2029 | Explore context continuity, adaptive route/obstacle awareness and privacy-preserving personalisation with explicit user controls. |
| 2030+ | Keep compute, battery-management, sensor and AI modules replaceable; preserve useful offline operation and avoid dependence on continuous cloud access. |

**Continuous anti-obsolescence rule:** review technology signals monthly, architecture quarterly and the full roadmap annually; trigger an out-of-cycle review when a critical dependency is unsupported, a security issue emerges, or measured performance/resource limits are breached. Keep a verified baseline, migration and rollback path, compatibility/regression tests and a documented decision for every upgrade. Do not adopt a trend solely because it is new. **Status:** Planned roadmap; no future capability is claimed as implemented or validated.


---

## Academic Research Direction — Q1-Targeted Study (Proposed)

**Research topic:** Adaptive Edge AI for Mobile Assistant Robotics  
**Working title:** *Resource-Adaptive Hybrid Edge Intelligence for Reliable Perception and Navigation in Compact Outdoor Mobile Assistants*

**Status:** Proposed for lecturer review. Research novelty, data access, hardware assumptions and physical validation remain unverified. No integrated robot or measured field capability is claimed.

### Problem and motivation
A compact mobile assistant has limited compute, memory, battery energy and thermal capacity. A large vision-language model may be too costly to run continuously, while a small detector may fail to interpret unfamiliar situations. This study investigates adaptive inference according to scene complexity, sensor quality, uncertainty and available resources.

### Candidate research gaps
- Fixed model selection may waste resources in easy scenes or underperform in difficult ones.
- Accuracy-only evaluations often omit latency, RAM, energy and thermal constraints.
- Model switching may create inconsistent outputs or delays.
- Generalisation across independent routes, lighting, weather and terrain requires testing.

### Research questions and hypotheses
- **RQ1:** Can adaptive selection between lightweight specialist models and a larger semantic model improve the accuracy–resource trade-off over fixed-model baselines?
- **RQ2:** How should scene complexity, uncertainty and compute headroom govern model selection and inference frequency?
- **RQ3:** Does degraded-mode and safe-stop logic improve reliability during overload, sensor dropout or model failure?
- **H1:** Adaptive inference will improve a predeclared accuracy/latency or accuracy/energy trade-off over always-small and always-large baselines.
- **H2:** Reliability gates will reduce unsupported navigation outputs under resource or sensor degradation.

### Proposed hybrid-AI method
1. Run a compact specialist detector/segmenter for continuous perception.
2. Estimate scene complexity, ambiguity, sensor quality, uncertainty and compute headroom.
3. Trigger a higher-capacity vision/foundation model only when justified and available.
4. Evaluate quantization/distillation where model and hardware support reproducible measurement.
5. Retain conventional geometry, localisation, mapping and obstacle checks.
6. Use a resource-aware scheduler to select model, resolution and inference frequency under measured budgets.
7. On overload, missing evidence or model failure, degrade conservatively, request human input or stop.

### Candidate datasets and original evidence
- **RELLIS-3D** for off-road perception, **TartanAir** for simulation/visual robustness, and **OpenLORIS-Scene** for long-term RGB-D perception may be considered after licence and suitability review.
- Original authorised outdoor-route data should include RGB/depth where available, IMU/odometry where available, route/session identity, lighting, weather, terrain and obstacle labels.
- Record target CPU/GPU/NPU, RAM, energy-measurement method and thermal conditions. Report simulation, desktop and embedded-device results separately.

### Experiments and evaluation
- Baselines: always-small, always-large, fixed cascade, adaptive scheduler and conventional navigation/perception.
- Compare model-selection decisions across scene complexity and ambiguity.
- Profile latency distributions, throughput, peak RAM, model size, energy/inference and thermal throttling on declared hardware.
- Test low light, glare, moving obstacles, terrain changes, unfamiliar routes, sensor dropout, delayed observations and compute saturation.
- Compare fixed and adaptive inference under equal compute/energy budgets.

**Primary outcome:** pre-register task success at a fixed energy/latency budget or accuracy at a fixed compute budget.  
**Secondary metrics:** detection/segmentation F1, path completion, intervention/stuck rate, safe-stop response, latency, RAM, energy, thermal behaviour and model-switch overhead.

### Expected contribution
A reproducible resource-aware inference policy showing when lightweight specialist perception is sufficient, when semantic escalation is useful, and how uncertainty and compute constraints should govern degraded operation.

### Product and publication boundaries
AI NOMAD is a compact suitcase-style four-wheel mobile assistant with an integrated pull handle; its 8–10 kg mass target and 10 kg maximum design limit are unvalidated. It is distinct from indoor AI HOME. Check model/data provenance, licence and non-Chinese origin before use. Do not claim outdoor navigation, payload, runtime or safe operation without measured tests. Q1 publication is a target, not a guarantee.

## 360° Intelligence

The [360° Intelligence Profile v1.0](docs/PUI89_360_DEGREE_INTELLIGENCE_PROFILE_V1.0.md) defines supervised surround awareness for the user-directed four-wheel assistant, including handle, wheel, user and payload occlusion. **Status: Proposed**; no physical prototype or validated 360° sensor suite is established.


## Environmental, Material & Safety Qualification

This product follows the [PUI89 Six-Product Environmental, Material & Safety Qualification Framework](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/standards/PUI89_SIX_PRODUCT_ENVIRONMENTAL_MATERIAL_SAFETY_QUALIFICATION_V1.0.md). NOMAD-specific candidate requirements cover a suitcase-style four-wheel shell, reinforced impact corners, replaceable wheel modules, protected handle mounts, separated internal storage and battery/power compartments, rain/dust exposure, vibration, payload restraint and safe-stop behaviour. Candidate enclosure ratings are zone-specific and remain TBD pending design/testing. NOMAD must not be treated as ordinary passenger cabin luggage; air cargo requires carrier approval and applicable battery/dangerous-goods compliance. All requirements remain proposed; no payload, ingress, impact or fire qualification is claimed.


## Vibration Detection & Console Classification

**Status: Proposed / Not implemented / Not tested.** Live vibration monitoring requires physical sensing hardware plus embedded acquisition and software/AI analysis; it is not AI-only. Candidate hardware: chassis-mounted IMU/accelerometer, with optional wheel-hub or motor-mount sensors after design review. Candidate analysis: rolling/wheel vibration, loose cargo or shell resonance, threshold impacts and drivetrain trends, accounting for payload.

The console must separate **Hardware** (sensor presence/type/location/connection/calibration), **Embedded & Signal Processing** (acquisition, RMS/peak/FFT and data quality), **AI/Analytics** (anomaly/trend model and confidence), **Integration** (module mapping and maintenance workflow), and **Overall capability** (Hardware required / AI-Software only / Hardware + AI / Not available). Show Not installed, No live data, Not tested and TBD explicitly. Do not invent live metrics or show healthy status without sensor data. Sensor selection, mounting, calibration, baseline, thresholds, false alarms and detection latency require evidence. AI diagnosis is advisory; independent safety controls retain stop authority. See the [shared vibration and console framework](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/feature/vibration-detection-console-v1/docs/standards/PUI89_SIX_PRODUCT_ENVIRONMENTAL_MATERIAL_SAFETY_QUALIFICATION_V1.0.md).


## Local Product Console — Proposed

**Status: Proposed / Not implemented / Not tested.** No physical NOMAD console, selected display hardware or live console integration is established.

The NOMAD console is intended for its distinct compact mobile-assistant/suitcase role: local assistant status, movement and navigation state, battery, storage/compartment state where instrumented, local alerts, diagnostics and a proposed Return-to-Owner status when that feature is implemented. It must remain distinct from the indoor AI HOME interface.

- Essential local use must not require a phone application, remote control, cloud account or internet.
- Return-to-Owner is not a verified capability; console labels must show NOT IMPLEMENTED until built and tested. Provide manual recovery and a safe stop.
- Display sensor measurements, AI estimates, uncertainty and stale/missing data separately.
- Any future mobile prototype needs an independent physical stop path, motion limits, obstacle response and safe-state behavior. A touchscreen shutdown is not an emergency stop.
- Use POWER OFF → POWER ON/SELF-CHECK → NOT READY/READY → OPERATING → STOPPING → SHUTDOWN, with FAULT/RECOVERY handling.

See the [PUI89 Universal Local Console Architecture v1.0 — Draft PR](https://github.com/Pui89/PUI89-Shared-AI-Core/pull/210). This is a proposed product requirement, not evidence of a working NOMAD or console.
