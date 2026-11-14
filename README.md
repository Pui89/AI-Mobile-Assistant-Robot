# PUI89 AI Mobile Assistant Robot


## Public privacy boundary

This public README is limited to the project overview, approved concept material and evidence that can be shared openly. Do not publish API keys, passwords, private tokens, Wi-Fi or internal network settings, private camera footage, personal or precise location data, detailed security configurations, unreleased engineering specifications, or confidential commercial plans. Keep sensitive material in an appropriately access-controlled private location. If a credential may have been exposed, revoke it; removing it from the latest commit does not remove it from Git history.

<!-- PUI89_PINNED_CONCEPT_ILLUSTRATION:START -->
![PUI89 AI NOMAD — compact mobile assistant with telescopic pull handle](docs/images/ai-nomad-compact-four-wheel.svg)

*Concept illustration built as an embedded SVG. Proposed design only; physical construction and validation remain pending.*

*Conceptual design illustration — not a built or validated robot. Dimensions, weight, mobility, endurance, weather resistance and field performance remain design targets pending engineering and physical validation.*
<!-- PUI89_PINNED_CONCEPT_ILLUSTRATION:END -->


## Compact product specification — proposed 6 kg design

| Specification | Proposed engineering target |
|---|---:|
| Complete robot mass | **Maximum 6.0 kg**, including battery, retractable handle, wiring and fixed sensors |
| Payload | **1.0 kg initial target**, carried separately from the robot's own mass |
| Body width | **30–33 cm** |
| Body length / depth | **35–40 cm** |
| Body height | **35–40 cm**, excluding the extended handle |
| Mobility | Four protected/recessed wheels; drive arrangement to be selected after torque, traction and braking analysis |
| First operating domain | Indoor, flat, controlled surfaces; owner-supervised |
| Later operating domain | Selected outdoor surfaces only after separate validation |
| Compute direction | CPU-first, low-power, local/offline-capable AI; no automatic model or package downloads |
| Human control | Manual override, physical emergency stop and conservative safe-stop behaviour |

The 6.0 kg limit is the complete robot mass, not the robot-plus-payload mass. The initial 1.0 kg payload target is additional; the design must therefore be engineered and tested for a total moving mass of up to 7.0 kg. The handle's extended height is excluded from body height, but its mass is included in the 6.0 kg robot limit.

**Status: PROPOSED / NOT MEASURED / NOT VALIDATED.** These are design targets, not measured prototype specifications. No physical NOMAD robot, payload rating, runtime, speed, braking distance, obstacle-clearance limit, ingress rating or field reliability is established.

### Preliminary 6 kg mass-allocation budget

| Assembly | Planning allocation |
|---|---:|
| Frame and enclosure | 1.4 kg |
| Wheels, motors and drivetrain | 1.2 kg |
| Battery and power protection | 1.0 kg |
| Compute and control electronics | 0.7 kg |
| Cameras and other sensors | 0.4 kg |
| Handle, wiring and safety hardware | 0.5 kg |
| Engineering allowance / mass reserve | 0.8 kg |
| **Complete robot mass budget** | **6.0 kg** |

This is a top-down planning allocation only. It is not a supplier-based bill of materials or measured component inventory. The engineering allowance is reserved within the 6.0 kg ceiling; it must not be treated as extra mass above the limit. Component selection must be supported by exact part numbers, verified mass, origin evidence, availability, compatibility and dated sourcing records before design freeze.

### First buildable product: NOMAD Prototype 1

The first physical prototype should prioritise a dependable supervised mobile base over complex autonomy:

- Four-wheel chassis with guarded wheels, low-mounted battery and a stable payload area.
- Appropriately sized motor/drive system, wheel encoders and a controller; final drive layout and torque remain to be calculated.
- Protected battery, fuse/over-current protection, accessible isolation, thermal monitoring and safe wiring.
- Physical emergency stop and manual recovery/control method.
- Basic camera observation and obstacle alerts; optional depth sensing only after compute, power, cost and provenance review.
- Battery/state telemetry and clear owner-facing status.
- CPU-first local software, with deterministic control and safety functions kept separate from AI perception.
- AI outputs are observations or bounded recommendations; they are not direct authority to drive actuators.

**Not in Prototype 1:** unsupervised owner-following, public-space autonomy, stair climbing, all-terrain travel, water crossing, waterproof claims, emergency response or autonomous road operation. These require separate engineering, risk assessment and validation.

### Engineering and validation gates

1. **Requirements and CAD packaging:** confirm body envelope, access for service, handle loads, payload location, centre of gravity and wheel guarding.
2. **Mass closure:** maintain a part-by-part mass ledger, including fasteners, wiring, connectors, guards, handle and battery; demonstrate a design total at or below 6.0 kg with the stated reserve.
3. **Mechanical and drive analysis:** calculate static/dynamic wheel loads, motor torque, traction, turning clearance, slope limits, braking and stopping distance for the 6.0 kg robot plus up to 1.0 kg payload.
4. **Electrical and thermal safety:** define battery chemistry/capacity only after runtime and power budgeting; verify fusing, isolation, charge protection, wiring, thermal limits and emergency stop.
5. **Software-in-the-loop:** test command limits, stale/missing sensors, communication loss, low battery, obstacle states, safe hold and recovery using deterministic tests and documented simulation.
6. **Controlled physical trials:** begin unloaded at low speed in a closed, flat indoor area; then increase payload and test braking, stability, turning, thresholds and endurance under supervision.
7. **Operating-domain expansion:** outdoor surfaces, rain/splash, dust, slopes and uneven ground each require their own acceptance criteria and evidence before being described as supported.

**Release rule:** do not publish a measured weight, payload rating, runtime, speed, slope limit, ingress rating or safety claim until the method, conditions, results and supporting evidence are recorded. Simulation and software tests do not prove physical performance.

## Open-source-first engineering

PUI89 prioritises open-source software, transparent licensing, reproducible workflows and evidence-led collaboration. Model weights, datasets, hosted services and hardware are assessed separately for provenance, licence terms, security, data handling, resource requirements and intended use. Public availability alone does not establish permission for reuse or commercial deployment.


> **PUI89 engineering standard:** [Simple, Safe and Professional](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_SIMPLE_SAFE_PROFESSIONAL_STANDARD.md) — shared guidance for usability, safety, evidence, privacy and maintainable engineering.

> **PUI89 | Intelligent Systems. Verifiable Decisions. Safer Outcomes.**
> 
> **Project:** PUI89 AI Mobile Assistant Robot  
> **Focus:** Owner-supervised compact four-wheel mobile assistant robot concept  
> **Development stage:** Early software foundation and design targets; locomotion, endurance and field performance are not validated.
> 
> **Project website:** [English](https://pui89.github.io/nomad.html) · [ภาษาไทย](https://pui89.github.io/nomad-th.html) · [PUI89 portfolio](https://pui89.github.io/)
> 
> **Validation boundary:** Proposed dimensions and weight are design targets, not measured prototype specifications; AI Mobile Assistant Robot is not an emergency responder or unsupervised roaming system.

## Hardware & Materials Sourcing

PUI89 uses a traceable sourcing workflow for materials, mechanical parts, sensors, compute, power and control components. See the [bilingual Hardware & Materials Sourcing guide](https://pui89.github.io/materials.html) for the process covering exact manufacturer/model identification, Thailand and international supplier discovery, country-of-origin evidence, dated pricing and availability, lead times, shipping, compatibility checks and verification gates. Product-specific candidates are added only when supported by evidence; research candidates are not purchases or validated hardware.

## Perception & Task Intelligence (PTI)

**Role in this product:** support supervised outdoor and mixed-environment mobility for the compact four-wheel NOMAD assistant. PTI is the shared PUI89 perception-and-task framework; the tasks below are research priorities, not validated all-terrain or autonomous capability.

**Priority perception tasks**
- Check camera/depth/IMU input quality, timestamps, calibration state and sensor availability.
- Detect people, objects, path boundaries and obstacles relevant to the planned route.
- Estimate terrain changes, slopes and traversability only when suitable depth/spatial inputs and validation evidence are available.
- Fuse localisation, inertial and perception observations; detect stale data, sensor disagreement and localisation loss.
- Identify routes or surfaces outside the validated operating envelope and request human guidance.
- Propose only bounded routes in a defined, supervised operating area; safe-hold when conditions are uncertain.

**Task flow:** OBSERVE → PERCEIVE → ASSESS → DECIDE → RESPOND → LEARN FROM EVIDENCE. Outputs support a human supervisor; they do not authorise unrestricted navigation or physical movement beyond separately validated safeguards.

**First evidence gate:** controlled indoor/outdoor route datasets and synthetic obstacle/terrain cases, then supervised low-speed trials only after independent hardware safety provisions exist. Measure obstacle misses, localisation error, stop response, recovery behaviour and compute/resource use.

**Not established:** all-terrain operation, stair traversal, public-road autonomy, payload or mobility limits, or field-validated navigation. See the [shared PTI specification](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/perception/PUI89_PERCEPTION_TASK_INTELLIGENCE_V1.0.md) (maintainer repository access required).

## Development stage

**Current stage:** Early software foundation & design targets  
**ขั้นการพัฒนา:** พื้นฐานซอฟต์แวร์และเป้าหมายการออกแบบระยะแรก

**Evidence:** Concept requirements, architecture and early deterministic software foundations are documented.

**Limitations:** No built robot, validated four-wheel mobility, endurance, weather protection or field performance is established.

**Next milestone:** Complete a software-only mission and hazard-state demonstrator.


## Project website QR codes

<table><tr><td align="center"><strong>English website</strong><br><a href="https://pui89.github.io/nomad.html"><img src="https://pui89.github.io/qr/nomad-en.png" width="160" alt="PUI89 AI Mobile Assistant Robot English website QR code"></a><br><a href="https://pui89.github.io/nomad.html">Open English website</a></td><td align="center"><strong>เว็บไซต์ภาษาไทย</strong><br><a href="https://pui89.github.io/nomad-th.html"><img src="https://pui89.github.io/qr/nomad-th.png" width="160" alt="QR Code เว็บไซต์ภาษาไทย PUI89 AI Mobile Assistant Robot"></a><br><a href="https://pui89.github.io/nomad-th.html">เปิดเว็บไซต์ภาษาไทย</a></td></tr></table>
### A Compact Four-Wheel Assistant for Home, Travel and Everyday Life

**A mobile companion designed to help people indoors and outdoors.**

PUI89 AI NOMAD is an early-stage, owner-supervised compact four-wheel mobile-assistant concept with a rounded suitcase-style body. It is intended to support supervised everyday use, carrying belongings, travel and environmental awareness. These are design goals, not validated capabilities.

- **Repository:** https://github.com/Pui89/AI-Mobile-Assistant-Robot
- **Website:** [English](https://pui89.github.io/nomad.html) · [ภาษาไทย](https://pui89.github.io/nomad-th.html)
- **Separate indoor home-safety product:** [PUI89 AI HOME](https://github.com/Pui89/AI-Home-Safety-Robot) · [English website](https://pui89.github.io/home.html) · [ภาษาไทย](https://pui89.github.io/home-th.html)


> **Product boundary:** AI Mobile Assistant Robot is a mobile assistant concept for indoor and outdoor everyday use, travel and carrying assistance. HOME is a separate four-wheel indoor home-safety robot. The products may share versioned PUI89 AI Core contracts, but they are not one robot and do not share physical operating assumptions.

## AI Mobile Assistant Robot purpose

AI Mobile Assistant Robot is intended as an owner-supervised mobile companion. Proposed research areas include:
- Carrying shopping, luggage and personal belongings within a validated payload limit
- Owner-supervised accompaniment in suitable indoor and outdoor environments
- Travel, walking, park, station and campsite assistance concepts
- Indoor/outdoor scene and obstacle awareness
- Mapping and localization research, with safe-stop behaviour when uncertain
- Environmental observations when suitable sensors are selected and validated
- Offline-first operation and clear owner-facing reports

AI Mobile Assistant Robot is not an emergency responder or an unsupervised roaming machine. It must not enter hazardous areas merely to investigate. Carrying capacity, following behaviour, accessibility support and safe operation remain unvalidated design goals.

## Proposed operating workflow

Observe → check evidence quality → understand location and context → assess uncertainty and risk → choose a safe movement state → report to the owner.

The owner remains responsible for decisions. If localization, route safety or battery reserve is insufficient, the robot should stop safely rather than attempt an unsafe return or continue moving.

## Safety and resilience requirements

- Define and test separate limits for indoor floors, thresholds, stairs, people, pets, rain, dust, temperature, slopes, loose ground, water exposure, darkness, battery endurance and connectivity.
- Prioritize battery protection, electrical isolation, overcurrent protection, thermal monitoring and guarded wiring.
- Treat weather resistance, water resistance and fire performance as engineering requirements requiring specified tests; do not claim waterproof or fireproof performance.
- Never delay emergency response or substitute for certified alarms and qualified responders.
- Use human supervision, safe-stop defaults and clear uncertainty reporting.
- Protect location data and avoid unnecessary recording of people.

## Shared intelligence, separate product engineering

AI Mobile Assistant Robot may reuse PUI89 AI Core contracts (WorldState, Observation, ActionProposal and FailureReport), evidence provenance, uncertainty handling, safety gates, benchmark records and report formats. Its four-wheel mobility, indoor/outdoor navigation, sensor layout, environmental protection and risk assessment remain AI NOMAD-specific.

## Current development status

**FOUNDATION / SIMULATION-ONLY / CONCEPT.** The repository contains an early deterministic software foundation, documentation and automated tests. It does not establish a built robot, real sensor integration, trained AI model, validated locomotion, indoor/outdoor reliability, certified safety or real-world hazard-detection performance.

## local-first and supply-chain policy

External services and model downloads require prior origin, licensing, security and resource review. PUI89 excludes Chinese-origin AI models, providers and model-hosting services from its approved stack.

## Evidence labels

PROPOSED = planned; IMPLEMENTED = code exists; TESTED = automated test passed; SIMULATION-ONLY = synthetic inputs only; MEASURED = quantitative result with method; VERIFIED = reproducibly checked; NOT_VALIDATED = real-world performance not established.

See [Architecture](docs/ARCHITECTURE.md), [Safety Case](docs/SAFETY_CASE.md), [Intelligence Catalogue](docs/INTELLIGENCE_CATALOGUE.md), [Supply-chain Policy](docs/MODEL_AND_SUPPLY_CHAIN_POLICY.md), [Roadmap](docs/ROADMAP.md), [Water Resilience Standard](docs/PUI89_WATER_RESILIENCE_STANDARD.md) and [Resilience Standard](docs/PUI89_RESILIENCE_STANDARD.md).

**PUI89 — Intelligent Systems. Verifiable Decisions. Safer Outcomes.**


## Hugging Face vision models — opt-in local integration

This repository now includes real Hugging Face checkpoint adapters in [`pui89_models/hf_vision.py`](pui89_models/hf_vision.py), with project-specific usage boundaries in [`docs/HUGGING_FACE_MODEL_INTEGRATION.md`](docs/HUGGING_FACE_MODEL_INTEGRATION.md).

- **OWLv2:** `google/owlv2-base-patch16-ensemble` for text-conditioned object proposals.
- **Intel DPT-Hybrid:** `Intel/dpt-hybrid-midas` for relative scene depth where appropriate; not calibrated distance or physical depth.
- **local-first default:** no packages or model weights are installed/downloaded automatically; CPU-only inference, local cache only by default, no hosted inference API or cloud GPU.
- **Evidence status:** adapter code is added; model inference and project-specific accuracy are NOT YET TESTED. Outputs remain uncertain observations for human review, never actuator commands.




---

## Security, malware and supply-chain protection

Security policy: [SECURITY.md](SECURITY.md). Report suspected vulnerabilities privately; do not post travel routes, precise locations, credentials or private sensor records publicly.

Project-specific controls and review requirements:
- Treat GPS, location, environmental sensors, camera/audio, maps, downloaded files and external messages as untrusted inputs.
- Validate timestamps, source provenance, ranges, replay/stale data and offline behaviour.
- Never commit credentials, private travel histories, home addresses or identifiable recordings.
- Review packages, model files, simulator plugins and GitHub Actions for provenance, licence and vulnerability risks before adoption.
- AI suggestions must not directly control mobility, locks or safety-critical hardware; require human approval and safe-stop behaviour.
- Keep CI permissions minimal and never expose secrets to untrusted pull-request code.

A scan or passing test is evidence only for the checks actually run; it does not establish whether the repository contains malware or vulnerabilities.

## PUI89 seven-dimension quality recommendations

**Last reviewed: 8 November 2026 · Review month: November 2026**

This project uses the shared PUI89 quality framework. The indicators are guidance/status labels, not scores, certification or proof that work is complete.

| Dimension | Recommendation for this project | Indicator |
|---|---|---|
| Brand identity | Maintain the PUI89 Deep Navy + Electric Cyan system, consistent project naming and the approved project accent. | 🔵 Guidance |
| Website and accessibility | Keep English and Thai pages aligned, responsive, accessible, correctly linked and date-stamped. | 🔵 Guidance |
| AI software and applications | Version contracts, preserve provenance, propagate uncertainty, abstain on insufficient evidence and test safe human-review boundaries. | 🟢 Quality target |
| Physical products and robotics | Define measurable structural, power, thermal, water-ingress, fire-risk, maintenance and emergency-stop requirements; do not claim untested ratings. | 🟠 Evidence required |
| Documentation and research evidence | Maintain architecture, requirements, reproducible tests, data/model licences, limitations and traceable evidence links. | 🔵 Guidance |
| Product and commercial readiness | Validate the user problem, intended operator, value, support model, lawful IP/data position and release gates before commercial claims. | 🟠 Evidence required |
| Professional environment and presentation | Use consistent technical diagrams, demonstrations and partner-facing materials; do not imply facilities or partnerships without evidence. | ⚪ Not assessed |

**Project-specific priority:** Keep AI NOMAD distinct from indoor HOME as a compact portable/outdoor mobile assistant. Prioritise stability, obstacle handling, battery isolation, offline behaviour, enclosure drainage/sealing strategy, serviceability and supervised operation; dimensions, weight, locomotion, endurance and weather protection remain design targets until measured.

**Status legend:** 🔵 framework guidance added · 🟢 engineering quality target · 🟠 evidence or validation still required · ⚪ not assessed. These labels describe the review state of recommendations, not overall project maturity. Project maturity changes only when supported by verified repository evidence, reproducible tests or controlled validation.


<!-- PUI89_PROJECT_STRENGTH_SCORECARD:START -->
## PUI89 Project Strength Scorecard | เกณฑ์ประเมินความแข็งแกร่งของโครงการ

**Current review status: Not yet scored · Completed evidence-backed strength reviews: 0.** This is a recordkeeping status, not a claim that no development or testing exists.

**สถานะการประเมิน: ยังไม่มีคะแนน · รายงานประเมินที่เสร็จสมบูรณ์และมีหลักฐาน: 0 รายการ** ตัวเลขนี้หมายถึงจำนวนรายงานที่บันทึกครบตามเกณฑ์ ไม่ได้หมายความว่าไม่มีการพัฒนาหรือทดสอบ

### Four Project Indicators | ตัวชี้วัดโครงการ 4 ด้าน

| Indicator / ตัวชี้วัด | What it measures / สิ่งที่ประเมิน | Current status / สถานะ |
|---|---|---|
| Engineering Strength / ความแข็งแกร่งทางวิศวกรรม | Verified technical capability and system integration / ความสามารถทางเทคนิคและการเชื่อมต่อระบบที่ตรวจสอบได้ | Not yet assessed / ยังไม่ได้ประเมิน |
| Evidence Confidence / ความเชื่อมั่นของหลักฐาน | Evidence traceability, reproducibility and validation quality / การตรวจสอบย้อนกลับ การทำซ้ำ และคุณภาพการตรวจสอบ | Not yet assessed / ยังไม่ได้ประเมิน |
| Implementation Level / ระดับการพัฒนาที่ดำเนินการแล้ว | Work actually implemented, separated from proposed work / งานที่พัฒนาแล้วจริง แยกจากงานที่เป็นข้อเสนอ | Not yet assessed / ยังไม่ได้ประเมิน |
| Project Maturity / ความสมบูรณ์ของโครงการ | Evidence-based development stage, from concept to operational demonstration / ระยะการพัฒนาที่อ้างอิงหลักฐาน ตั้งแต่แนวคิดถึงการสาธิตการใช้งานจริง | Formal stage assessment pending / รอการประเมินระดับอย่างเป็นทางการ |

These four indicators are separate from the weighted 100-point score below. No score, percentage or maturity stage is assigned until a dated evidence-backed review is completed.

ตัวชี้วัดทั้ง 4 ด้านนี้แยกจากคะแนนถ่วงน้ำหนัก 100 คะแนนด้านล่าง จะไม่กำหนดคะแนน เปอร์เซ็นต์ หรือระดับความสมบูรณ์จนกว่าจะมีรายงานประเมินที่ลงวันที่และมีหลักฐานครบถ้วน

| Dimension / ด้านประเมิน | Weight / น้ำหนัก |
|---|---:|
| Technical capability / ความสามารถทางเทคนิค | 25 |
| Testing and evidence / การทดสอบและหลักฐาน | 25 |
| Safety and reliability / ความปลอดภัยและความน่าเชื่อถือ | 20 |
| Engineering maturity / วุฒิภาวะทางวิศวกรรม | 15 |
| Documentation and reproducibility / เอกสารและการทำซ้ำผล | 10 |
| Real-world validation / การตรวจสอบในโลกจริง | 5 |
| **Total / รวม** | **100** |

Scores are awarded only through a dated review with a defined scope, version/commit, evidence links, findings, limitations and next actions. Concepts, planned features, concept images, unrun tests and tool inventories do not earn implementation or test credit. Simulation results do not prove physical-world performance.

จะให้คะแนนเมื่อมีรายงานที่ระบุวันที่ ขอบเขต เวอร์ชัน/commit ลิงก์หลักฐาน ข้อค้นพบ ข้อจำกัด และขั้นตอนถัดไปเท่านั้น แนวคิด ฟีเจอร์ที่วางแผน ภาพแนวคิด การทดสอบที่ยังไม่ได้รัน และรายการเครื่องมือ จะไม่ได้คะแนนว่าเป็นการพัฒนาหรือการทดสอบที่เสร็จแล้ว ผลจำลองไม่ใช่หลักฐานยืนยันประสิทธิภาพในโลกจริง

**Scoring method / รายละเอียดเกณฑ์:** [English](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PROJECT_STRENGTH_SCORECARD.md) · [ภาษาไทย](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PROJECT_STRENGTH_SCORECARD_TH.md)

This project-strength review is separate from the documented development stage; it is not certification, safety approval or an investment rating.
<!-- PUI89_PROJECT_STRENGTH_SCORECARD:END -->




## Spatial Intelligence integration

See [the project-specific spatial integration profile](docs/spatial-intelligence/README.md). Runtime sensor integration and physical validation remain pending.

<!-- PUI89_EVIDENCE_BACKED_REVIEW:START -->
## Evidence-backed project review status

**Project:** PUI89 AI NOMAD  
**README snapshot (13 November 2026): 0 completed evidence-backed reviews.** This snapshot is not auto-synchronised; the live [PUI89 portfolio review register](https://pui89.github.io/#evidence-backed-project-reviews) is the source of truth.

This is a review-record count, not a statement that development or testing has not occurred. Engineering work, CI runs, test results and simulation evidence may support a review, but do not automatically count as a completed review.

A review is counted only when its record includes all required fields: **completed status, review date, defined scope, reviewer role, outcome, and at least one supporting evidence reference**. Drafts, ratings, stars, page views and comments are excluded.

The portfolio-wide count is published on the [PUI89 website](https://pui89.github.io/#evidence-backed-project-reviews). Refresh this README snapshot when the shared register changes.

**สถานะการทบทวนโครงการที่มีหลักฐาน**  
**จำนวนการทบทวนที่เสร็จสมบูรณ์: 0** — ยังไม่มีบันทึกการทบทวนที่ผ่านเกณฑ์สำหรับโครงการนี้ในทะเบียนกลาง PUI89

ตัวเลขนี้เป็นจำนวนบันทึกการทบทวน ไม่ได้หมายความว่าไม่มีการพัฒนาหรือทดสอบ งานวิศวกรรม ผล CI การทดสอบ และหลักฐานจากการจำลองอาจใช้ประกอบการทบทวน แต่ไม่นับเป็นการทบทวนที่เสร็จสมบูรณ์โดยอัตโนมัติ

จะนับเมื่อมีสถานะเสร็จสมบูรณ์ วันที่ ขอบเขต บทบาทผู้ทบทวน ผลการทบทวน และหลักฐานอ้างอิงอย่างน้อยหนึ่งรายการครบถ้วนเท่านั้น รายการร่าง คะแนน ดาว ยอดเข้าชม และความคิดเห็นจะไม่นับ
<!-- PUI89_EVIDENCE_BACKED_REVIEW:END -->

## AI Engineering Intelligence & Outdoor-Robot Design

NOMAD uses a staged, owner-supervised engineering approach. Its current product target is a complete robot mass of no more than 6.0 kg including battery and handle, with a separate initial payload target of 1.0 kg. The proposed body envelope is 30–33 cm wide × 35–40 cm long/deep × 35–40 cm high, excluding the extended handle. All figures remain proposed and unvalidated.

**Project-specific priorities:** stable load distribution and low centre of gravity; guarded wheels; appropriate motor torque and braking; protected battery and thermal design; manual recovery; obstacle awareness; offline operation; maintainable enclosure; and clear safe-stop behaviour. Indoor controlled operation is the first physical validation domain. Outdoor use is a later, separately gated objective.

**Evidence gates:** CAD and mass ledger → mechanical/electrical analysis → deterministic software tests and documented simulation → supervised low-speed closed-area trials → payload, stability, braking, endurance and environmental validation. Proposed mobility limits are not established capabilities.
