# PUI89 AI NOMAD — Ground-Use Four-Wheel Mobile Assistant Robot

[English](README.md) · [ภาษาไทย](README.th.md)


**A compact, dog-inspired four-wheel mobile assistant concept with a manual handling handle.**

[English project page](https://pui89.github.io/nomad.html) · [ภาษาไทย](https://pui89.github.io/nomad-th.html) · [PUI89 portfolio](https://pui89.github.io/)

![PUI89 AI NOMAD compact four-wheel mobile assistant robot concept](docs/images/ai-nomad-compact-four-wheel.svg)

*Concept illustration only. It is not evidence of a built, integrated, tested or validated robot.*

## What this product is

PUI89 AI NOMAD is a **ground-use four-wheel mobile assistant** intended for supervised assistance in suitable indoor and outdoor ground environments. Its actual operating envelope must be defined and validated before deployment. Its compact, dog-inspired form and handle are product-design features; it has four wheels, not articulated legs. It is not a suitcase, travel-luggage product or airline cabin-baggage product.

**NOMAD is different from:**
- **AI HOME:** an indoor home-awareness assistant with a separate home-focused mission.
- **Sentinel:** a four-legged quadruped for supervised exploration and inspection. NOMAD is a four-wheel mobile assistant.

**ผู้ใช้งาน:** ผู้ที่ต้องการหุ่นยนต์ผู้ช่วยเคลื่อนที่ภาคพื้นดินสำหรับงานช่วยเหลือในสภาพแวดล้อมที่กำหนด  
**ประโยชน์หลัก:** สนับสนุนงานช่วยเหลือและการเคลื่อนที่ภายใต้การกำกับ โดยไม่กล่าวอ้างการทำงานอัตโนมัติที่ยังไม่ได้ทดสอบ

## Product-specific functions

- Local environment and scene awareness for a defined operating area.
- Obstacle and walkway awareness, with uncertainty and safe-stop proposals.
- Human-reviewed task and route assistance in supported environments.
- Contextual alerts and user interaction for the selected mission.
- Battery, power and thermal status monitoring only where verified interfaces exist.
- A handle for manual handling; any storage is secondary to the mobile-assistant mission.

## Physical design constraints

| Requirement | Current definition | Evidence status |
|---|---|---|
| Mobility | Four-wheel ground robot | Design requirement |
| Form | Compact, dog-inspired mobile-assistant concept | Concept |
| Handle | Manual handling feature | Concept |
| Complete robot mass | **8–10 kg target; 10 kg maximum**, including battery, handle, wiring and installed hardware | Not measured |
| Payload and drive system | Must be defined after mission and safety analysis | Unknown / not validated |

The 10 kg limit applies to the complete robot. Do not add an assumed payload above that limit.

## What is not established

- No physical mobility, navigation, obstacle avoidance, outdoor endurance, weather resistance or field safety is validated; outdoor use remains a design intention, not a proven capability.
- No public-space unsupervised autonomy, person identification, pursuit, confrontation or enforcement is claimed.
- No stair/escalator traversal or waterproofing rating is claimed.
- A concept image or software test does not prove physical mobility or safety.

## Current development status

**Implemented — early software foundations.** This refers to software only; physical mobility and robot integration remain unvalidated.

**Next evidence gate:** define the first user mission, environment, operating envelope, payload, mobility constraints and measurable acceptance criteria before hardware selection.

## Product documentation

- [NOMAD development roadmap](docs/ROADMAP.md)
- [NOMAD concept illustration](docs/images/ai-nomad-compact-four-wheel.svg)

## Shared PUI89 engineering

Cross-product architecture, evidence contracts, safety, privacy, security, recovery, device interaction and localization requirements are maintained in the [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core). NOMAD's mobility, handling, payload and environment limits require separate product-specific validation.

Current maturity labels follow the [PUI89 Portfolio Alignment Register](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_PORTFOLIO_ALIGNMENT_REGISTER_2026-11-18.md) and [Evidence-Based Development Maturity Standard](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_DEVELOPMENT_STAGE_STANDARD.md).

## AI Model & Intelligence profile

**Candidate capability profile:** Object Detection, Image Segmentation, Object Tracking, SLAM and Sensor Fusion for supervised outdoor mobility research; Anomaly Detection for system/sensor faults; selected Predictive Models for condition and energy trends. Navigation and mobility performance remain unvalidated; no direct actuator authority is implied.

All nine shared capability families and their definitions, evaluation requirements, provenance/uncertainty rules and safety boundaries are maintained in the [PUI89 Shared AI Core Model Intelligence Framework](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/architecture/PUI89_MODEL_INTELLIGENCE_FRAMEWORK_V1.0.md). This product profile is a **candidate engineering allocation**, not evidence of model installation, runtime integration, benchmark results, field validation or certified performance. Select and enable each capability only after product-specific requirements, approved data, compute/energy budgets and verification gates are satisfied.

## Robot Capabilities & Functional Capacity

**Scope boundary:** AI NOMAD is a proposed compact, dog-inspired, four-wheel ground-use mobile assistant with a manual handling handle. It is not a quadruped and does not have articulated legs. Physical performance remains unvalidated.

### 1. Physical capacity
- Four-wheel ground platform with a manual handling handle.
- Complete robot mass: **8–10 kg target; 10 kg maximum**, including battery, handle, wiring and installed hardware.
- Payload: **TBD**; do not assume payload can be added above the complete-robot mass ceiling.
- Define dimensions, centre of gravity, structural strength, wheel loading, handle strength and stability after mission analysis.

### 2. Mobility capacity
- Intended for supervised ground operation in suitable, defined indoor/outdoor environments.
- Define supported surface types, slope, speed, turning radius, ground clearance, obstacle height, stopping distance and endurance through testing.
- No stair/escalator traversal, swimming, waterproofing rating or unrestricted off-road capability is claimed.
- **Validated terrain and mobility envelope:** TBD.

### 3. Perception capacity
- Architectural sensor groups may include Vision, Depth/3D, Audio, Tactile & Vibration/IMU, and Environmental & Safety.
- Detect and track relevant people, animals, vehicles, obstacles and ground features in permitted operating areas.
- Assess walkway boundaries, slopes, edges, surface changes and route context when supported by calibrated sensors.
- Fuse observations with timestamps, provenance, confidence and uncertainty; stop or request assistance when evidence is insufficient.
- Detection range, coverage, localisation accuracy and environmental limits remain TBD.

### 4. Computing capacity
- Prefer local edge AI and CPU-first development; select GPU/NPU resources only after workload, latency, RAM and thermal measurements.
- Define navigation, perception and control compute budgets separately.
- **Processor, memory, storage and measured performance:** TBD.

### 5. Power capacity
- Define battery energy, operating time by terrain/load, peak motor current, charging, battery protection and thermal envelope.
- Low-battery and power faults must trigger a safe, clearly reported state.
- **Battery and runtime values:** TBD.

### 6. Communication capacity
- Local operation and safe behaviour during communication loss are required design goals.
- Define authorised local control/telemetry, link range, pairing, data permissions and recovery after reconnection.
- No unapproved cloud dependency or remote control is assumed.
- **Protocols and range:** TBD.

### 7. Safety capacity
- Specify emergency stop, manual recovery, safe-stop conditions, wheel/motor fault response, obstacle response and supervised operating boundaries.
- Do not pursue, confront, restrain or autonomously enforce against people or animals.
- Loss of localisation, sensor disagreement, unsafe slope or uncertain obstacle clearance must cause a conservative response.

### 8. Maintenance capacity
- Plan for wheel/tyre, motor, handle, battery, connector and sensor inspection/replacement.
- Include sensor calibration, wheel/odometry checks, fault logs and accessible service points.
- **Service intervals and repair procedures:** TBD.

### 9. Operating limits
- Concept only; no physical mobility, navigation, obstacle avoidance, outdoor endurance, weather resistance or field safety is validated.
- Actual payload, terrain, slope, speed, obstacle clearance and runtime are unknown until measured.
- Do not describe the robot as a suitcase, luggage product, quadruped or stair-capable platform.

**Capacity evidence status:** 8–10 kg target and 10 kg maximum are design constraints, not measured prototype results; all other physical capacities remain TBD / not validated.


## Physical & Multimodal Sensor Privacy

PUI89 adopts the [Physical & Multimodal Sensor Privacy Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/privacy/PUI89_PHYSICAL_MULTIMODAL_SENSOR_PRIVACY_STANDARD_V1.0.md) as a shared engineering requirement. All cameras and microphones require physical controls. Location, route, movement and spatial histories are minimised and local. If privacy settings disable required navigation perception, movement is safely restricted or stopped.

**Evidence status:** requirements/specification only. No product-level hardware implementation or verification is claimed by this README section.


## Long-Life Battery & Energy Intelligence

PUI89 adopts the [Long-Life Battery & Energy Intelligence Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/energy/PUI89_LONG_LIFE_BATTERY_ENERGY_INTELLIGENCE_STANDARD_V1.0.md) as a shared engineering requirement. Prioritise efficient outdoor mobility, sensing and navigation, with energy reserve for uncertain terrain. Balance battery capacity against the 8–10 kg target / 10 kg maximum overall robot mass.

Battery runtime, chemistry, capacity, cycle life, charging performance and safety compliance remain **TBD until designed and evidenced**. No unverified runtime or battery-life claim is made. The design must include an energy budget, independent BMS protections, thermal/electrical safety, service strategy and representative runtime validation.


## Offline Independence & Connectivity Resilience

**The product must work without the app. Safety must work without connectivity.** Basic supported local operation, local status and safety controls must not require a smartphone, app, Wi-Fi, internet or cloud. The printed Quick Start and Safety Guide is supplied with the unit; the complete manual must be readable offline. QR and short URL are optional supplements. On link loss, remote commands are disabled and the product follows its own hazard-based safe state. See the [PUI89 Offline Independence & Connectivity Resilience Standard v1.0](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_OFFLINE_INDEPENDENCE_CONNECTIVITY_RESILIENCE_STANDARD_V1.0.md) and the [product manual/Remote Companion specification](docs/PRODUCT_MANUAL_AND_REMOTE_COMPANION_STANDARD_V1.md).

**Product-specific offline baseline:** Local power/stop, physical handling and transport use, local status and safe mobility control if a powered mobility version is implemented. Remote-link loss must not cause runaway movement: stop/hold or another validated safe response, while retaining local manual handling and safe shutdown. Location sharing and trip features are optional and permission-controlled. No unattended hazardous remote driving.

These are development requirements, not claims of implemented, tested or validated capability.
