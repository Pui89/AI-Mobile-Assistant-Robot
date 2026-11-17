# PUI89 AI NOMAD — Carry-on Suitcase-Style Mobile AI Assistant


## Public privacy boundary

This public README is limited to the project overview, approved concept material and evidence that can be shared openly. Do not publish API keys, passwords, private tokens, Wi-Fi or internal network settings, private camera footage, personal or precise location data, detailed security configurations, unreleased engineering specifications, or confidential commercial plans. Keep sensitive material in an appropriately access-controlled private location. If a credential may have been exposed, revoke it; removing it from the latest commit does not remove it from Git history.

<!-- PUI89_PINNED_CONCEPT_ILLUSTRATION:START -->
![PUI89 AI NOMAD — carry-on suitcase-style mobile assistant with four spinner wheels and telescopic handle](docs/images/ai-nomad-compact-four-wheel.svg)

*Concept illustration built as an embedded SVG. Proposed design only; physical construction and validation remain pending.*

*Conceptual design illustration — not a built or validated robot. Dimensions, weight, mobility, endurance, weather resistance and field performance remain design targets pending engineering and physical validation.*
<!-- PUI89_PINNED_CONCEPT_ILLUSTRATION:END -->



## Product identity — PUI89 AI NOMAD, four-wheel carry-on suitcase-style mobile AI assistant

**PUI89 AI NOMAD is a carry-on-suitcase-style mobile AI assistant with exactly four luggage-style swivel caster wheels at the base and a retractable telescopic pull handle.** Its upright, compact rectangular luggage body is intended to look and be handled like a premium travel suitcase. The four base wheels are caster wheels, not legs. NOMAD must never be depicted or described as a dog, quadruped, four-legged robot or animal-shaped machine. The final powered-wheel arrangement, steering, braking and caster configuration remain engineering decisions. The suitcase-inspired form does not establish airline cabin-baggage approval.

NOMAD is deliberately different from **PUI89 Sentinel**, which is the separate four-legged quadruped exploration and inspection robot. Sentinel uses articulated legs; NOMAD uses four luggage-style caster wheels at the bottom of a carry-on suitcase body. Never transfer Sentinel's animal-like or legged design language to NOMAD.

Both products may share PUI89 Shared AI Core interfaces and evidence standards, but their chassis, locomotion, sensors, safety cases and validation plans remain product-specific. NOMAD's physical capabilities remain proposed until a prototype is built and tested.

## Product purpose — a multifunctional travel companion, not a security robot

**PUI89 AI NOMAD is designed first as useful carry-on luggage and a personal travel assistant. Security awareness is a supporting safety function, not the product's identity or primary purpose.** The product combines a practical storage compartment, an upright carry-on suitcase form, four base wheels and a proposed AI-assisted mobility and travel-support system.

### User needs and proposed functions

| User need | Proposed NOMAD support | Evidence boundary |
|---|---|---|
| Carry belongings with less effort | Practical luggage storage, manual pull handle and future motor-assisted rolling | Storage layout and motorised assistance require prototype validation |
| Move through a journey more easily | Travel-context information, route guidance and permitted-area navigation assistance | Depends on reliable data, maps, location inputs and venue rules |
| Keep track of the trip | Itinerary, schedule, checklist and reminder support | External flight/booking data requires an authorised integration; no live feed is assumed |
| Find and organise belongings | User-defined packing lists, compartment organisation and optional item-location aids | Item detection or tracking requires suitable sensors/tags and privacy review |
| Interact naturally | Voice and text interaction, multilingual assistance and clear status feedback | Language quality and offline coverage require evaluation |
| Reduce physical effort | Supervised follow-me and motor-assisted movement research | Future capability; not available or validated today |
| Travel with confidence | Obstacle/person awareness, separation alerts, battery status and emergency stop | Safety functions require independent engineering and physical tests |
| Stay useful without connectivity | Local checklists, reminders, status and other essential offline functions | Exact offline feature set depends on local software and storage |

### Proposed user modes

1. **Luggage Mode:** a conventional manually handled suitcase; the user can pull, park and access belongings.
2. **Assist Mode:** future motor assistance for rolling on a validated surface, with owner supervision.
3. **Follow Mode:** future owner-following in a defined, permitted environment after navigation, privacy and safety validation.
4. **Travel Assistant Mode:** itinerary, reminders, packing checklist, destination notes and travel information from authorised sources.
5. **Navigation Support Mode:** route and wayfinding suggestions for human review; autonomous movement is restricted to separately validated areas.
6. **Manual / Recovery Mode:** direct human handling and a clear way to stop, isolate or recover the unit.
7. **Safe Mode:** stop or hold position when obstacle, localisation, communication, battery or sensor conditions are unsafe or uncertain.

### Product boundaries

- NOMAD is not primarily a security guard, patrol robot, surveillance platform or emergency responder. Security-related sensing is optional and subordinate to travel assistance and safe mobility.
- No unrestricted autonomous movement in airports, hotels, streets or other public spaces is claimed. Venue permission and operating-domain validation are required.
- It does not replace airline staff, airport security, travel agents, emergency services or accessibility professionals.
- Flight status, booking, maps, translation and messaging integrations are proposed only where a reliable, authorised source and suitable privacy controls exist; no paid API or cloud service is assumed.
- Airline cabin-baggage acceptance is not established. Dimensions, total mass and battery transport rules must be checked with each carrier.
- Every capability in this section is a product requirement or research direction unless a separate implementation record and validation evidence explicitly establish it.

## Compact product specification — 8–10 kg target, 10 kg maximum

| Specification | Proposed engineering target |
|---|---:|
| Complete robot mass | **8–10 kg target; 10 kg maximum**, including battery, handle, wiring and installed sensors |
| Payload | **TBD**; define only after stability, traction and total-mass analysis within the 10 kg design limit |
| Body width | **30–33 cm** |
| Body length / depth | **35–40 cm** |
| Body height | **35–40 cm**, excluding the extended handle |
| Mobility | Four luggage-style swivel caster wheels at the base; powered-wheel arrangement, steering and braking to be selected after engineering analysis |
| First operating domain | Indoor, flat, controlled surfaces; owner-supervised |
| Later operating domain | Selected outdoor surfaces only after separate validation |
| Compute direction | CPU-first, low-power, local/offline-capable AI; no automatic model or package downloads |
| Human control | Manual override, physical emergency stop and conservative safe-stop behaviour |

The 10 kg maximum is the complete robot design-mass limit, including the battery, handle, wiring and installed hardware. Payload capacity is not yet specified and must be established through structural, traction, braking and stability analysis; do not add an assumed payload above the 10 kg limit. The handle's extended height is excluded from body height, but its mass is included in the complete robot mass.

**Status: PROPOSED / NOT MEASURED / NOT VALIDATED.** These are design targets, not measured prototype specifications. No physical NOMAD robot, payload rating, runtime, speed, braking distance, obstacle-clearance limit, ingress rating or field reliability is established.

### Preliminary 10 kg complete-robot mass-allocation budget

| Assembly | Planning allocation |
|---|---:|
| Frame and enclosure | 2.2 kg |
| Wheels, motors and drivetrain | 2.0 kg |
| Battery and power protection | 1.5 kg |
| Compute and control electronics | 0.8 kg |
| Cameras and other sensors | 0.6 kg |
| Handle, wiring and safety hardware | 1.0 kg |
| Engineering allowance / mass reserve | 1.9 kg |
| **Complete robot mass budget** | **10.0 kg** |

This is a top-down planning allocation only. It is not a supplier-based bill of materials or measured component inventory. The engineering allowance is reserved within the 10.0 kg ceiling; it must not be treated as extra mass above the limit. Component selection must be supported by exact part numbers, verified mass, origin evidence, availability, compatibility and dated sourcing records before design freeze.

### First buildable product: NOMAD Carry-on Prototype 1

The first physical prototype should prioritise a dependable supervised carry-on-luggage-style rolling platform over complex autonomy:

- Carry-on suitcase-style upright enclosure with four protected swivel caster wheels at the bottom corners, a low-mounted battery and a stable internal payload area.
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
2. **Mass closure:** maintain a part-by-part mass ledger, including fasteners, wiring, connectors, guards, handle and battery; demonstrate a design total at or below 10.0 kg with the stated reserve.
3. **Mechanical and drive analysis:** calculate static/dynamic wheel loads, motor torque, traction, turning clearance, slope limits, braking and stopping distance within the 10.0 kg maximum complete-robot mass; payload remains TBD.
4. **Electrical and thermal safety:** define battery chemistry/capacity only after runtime and power budgeting; verify fusing, isolation, charge protection, wiring, thermal limits and emergency stop.
5. **Software-in-the-loop:** test command limits, stale/missing sensors, communication loss, low battery, obstacle states, safe hold and recovery using deterministic tests and documented simulation.
6. **Controlled physical trials:** begin unloaded at low speed in a closed, flat indoor area; then increase payload and test braking, stability, turning, thresholds and endurance under supervision.
7. **Operating-domain expansion:** different floor surfaces, thresholds, ramps, rain/splash and dust each require their own acceptance criteria and evidence before being described as supported.

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

### Prototype materials & cost snapshot

**Planning allowance for one research prototype: ฿36,000–107,000.** This is a preliminary estimate from the [PUI89 project-specific BOM](https://pui89.github.io/materials.html#project-boms), not a supplier quotation or verified current market price.

Compact carry-on suitcase-style mobile assistant with four base caster wheels and a retractable telescopic handle; 8–10 kg target and 10 kg maximum complete-robot design mass.

| Main item | Prototype quantity | Purpose |
|---|---:|---|
| Carry-on suitcase shell and internal frame | 1 set | Upright luggage body structure |
| Powered wheel/motor modules | TBD | Select only after comparing powered-wheel and passive-caster layouts; do not assume four drive motors |
| Spinner caster wheels | 4 | Luggage-style swivel wheels at the four base corners; final load rating and wheel material TBD |
| Retractable handle | 1 | Manual handling |
| RGB-D camera + 2D LiDAR | 1 each shared | Perception and navigation |
| IMU/position sensors | 1 set | Motion and location |
| Battery/BMS | 1 set | Protected power |
| Compute/motor control | 1 set | Reuse shared compute where suitable |

**Special engineering / purchase gate:** Validate luggage-shell strength, centre of gravity, handle locking, four caster mounts/load ratings, rolling stability, braking/holding, battery safety and low-speed supervised stop behaviour. The 8–10 kg target and 10 kg maximum are design targets, not verified payload or performance.

**Shared engineering bench (tracked separately):** approximately ฿16,500–46,000 if the existing development computer is reused. This is a portfolio-level allowance for reusable compute, one RGB-D camera, bench power supply/multimeter, two microcontroller boards and reusable tools/wiring/adapters; it is not added to each project total. Allocate each shared item once, not once per product.

**Cost status:** exact manufacturer/model, manufacturing origin, supplier, stock, lead time and dated prices remain to be verified. Freight, insurance, duty, VAT, brokerage, local delivery, custom fabrication labour and certification are not priced here; calculate Thai landed cost only from dated quotations. Quantities are for one prototype; no purchase or supplier commitment is authorised. Software-first work can continue with available computing and appropriately licensed open-source tools before hardware procurement.

## Perception & Task Intelligence (PTI)

**Role in this product:** support supervised luggage-style rolling mobility and travel assistance for the compact four-wheel NOMAD assistant. PTI is the shared PUI89 perception-and-task framework; the tasks below are research priorities, not validated travel-ready or autonomous capability.

**Priority perception tasks**
- Check camera/depth/IMU input quality, timestamps, calibration state and sensor availability.
- Detect people, objects, path boundaries and obstacles relevant to the planned route.
- Estimate floor-surface changes, thresholds, ramp limits and obstacle clearance only when suitable depth/spatial inputs and validation evidence are available.
- Fuse localisation, inertial and perception observations; detect stale data, sensor disagreement and localisation loss.
- Identify routes or surfaces outside the validated operating envelope and request human guidance.
- Propose only bounded routes in a defined, supervised operating area; safe-hold when conditions are uncertain.

**Task flow:** OBSERVE → PERCEIVE → ASSESS → DECIDE → RESPOND → LEARN FROM EVIDENCE. Outputs support a human supervisor; they do not authorise unrestricted navigation or physical movement beyond separately validated safeguards.

**First evidence gate:** controlled indoor travel-route datasets and synthetic obstacle/threshold cases, then supervised low-speed trials only after independent hardware safety provisions exist. Measure obstacle misses, localisation error, stop response, recovery behaviour and compute/resource use.

**Not established:** stair/escalator traversal, public-road autonomy, payload or mobility limits, airline acceptance, or field-validated navigation. See the [shared PTI specification](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/perception/PUI89_PERCEPTION_TASK_INTELLIGENCE_V1.0.md) (maintainer repository access required).

## Six Core Intelligence Groups — Product Allocation

PUI89 uses six shared intelligence groups across its six active products. This product allocation is a target architecture and capability map; it does not claim that every model, sensor, integration or physical function is implemented or validated.

- Vision Intelligence — image/video understanding, detection, classification, segmentation, tracking, depth and spatial cues.
- Audio Intelligence — speech recognition, sound/event perception, speaker diarisation where justified, audio-visual association, acoustic diagnostics and speech response.
- Multimodal Intelligence — context-aware fusion of vision, audio, text, video and authorised sensor/time-series data with provenance and uncertainty.
- Robotics Intelligence — robot/environment understanding, localisation, navigation, motion planning and manipulation where the product has suitable hardware.
- Action & Reaction Intelligence — task planning, bounded proposals, event response, prediction, recovery and escalation.
- Safety & Control Intelligence — independent permissions, operating limits, verification, human approval, fault handling, safe hold and emergency-stop boundaries.

### PUI89 AI NOMAD capability allocation

- **Vision:** Travel environments, people, luggage, doors, walkways, floor surfaces, thresholds and obstacles.
- **Audio:** Voice interaction and relevant travel-environment sound awareness, subject to privacy and validation.
- **Multimodal:** Camera/depth/IMU and optional LiDAR, GNSS or audio context fusion when justified by the travel scenario.
- **Robotics:** Supervised low-speed rolling mobility, route awareness and manual recovery planning; owner-following remains a future research topic requiring separate validation.
- **Action & Reaction:** Obstacle alerts, route-context changes, localisation loss, low-battery and motor/system anomaly reporting.
- **Safety & Control:** Owner supervision, validated-area limits, obstacle stop, manual pull/recovery and safe hold.

**Integration rule:** each product uses only the modules justified by its mission, data rights, hardware, compute budget and validation evidence. Model outputs remain observations or bounded proposals. Safety policy is product-specific and independent of model confidence. Unknown, stale, conflicting or out-of-scope inputs must be surfaced rather than guessed.

**Evidence status:** proposed capability allocation unless a separate implementation record, reproducible test or domain-specific validation explicitly says otherwise. Audio models, speaker diarisation, sound classifiers, VLM/VLA policies and robotics stacks require separate provenance, licence, compute, privacy and suitability review before adoption. No automatic model download or installation is authorised.

### Six-intelligence concept visual

![PUI89 AI NOMAD six-group AI architecture concept](docs/images/nomad-six-intelligence-concept.svg)

*Concept diagram only: it illustrates intended software intelligence domains, not a built product, installed model stack, integrated sensor suite or validated capability.*

## Development stage

**Current stage:** Early software foundation & design targets  
**ขั้นการพัฒนา:** พื้นฐานซอฟต์แวร์และเป้าหมายการออกแบบระยะแรก

**Evidence:** Concept requirements, architecture and early deterministic software foundations are documented.

**Limitations:** No built robot, validated four-wheel mobility, endurance, weather protection or field performance is established.

**Next milestone:** Complete a software-only mission and hazard-state demonstrator.


## Project website QR codes

<table><tr><td align="center"><strong>English website</strong><br><a href="https://pui89.github.io/nomad.html"><img src="https://pui89.github.io/qr/nomad-en.png" width="160" alt="PUI89 AI Mobile Assistant Robot English website QR code"></a><br><a href="https://pui89.github.io/nomad.html">Open English website</a></td><td align="center"><strong>เว็บไซต์ภาษาไทย</strong><br><a href="https://pui89.github.io/nomad-th.html"><img src="https://pui89.github.io/qr/nomad-th.png" width="160" alt="QR Code เว็บไซต์ภาษาไทย PUI89 AI Mobile Assistant Robot"></a><br><a href="https://pui89.github.io/nomad-th.html">เปิดเว็บไซต์ภาษาไทย</a></td></tr></table>
### A Multifunctional Carry-on Travel Companion

**A mobile companion designed to help people indoors and outdoors.**

PUI89 AI NOMAD is an early-stage, owner-supervised mobile AI assistant in an upright carry-on suitcase form, with four spinner caster wheels at the base and a retractable telescopic pull handle. It is intended to support supervised luggage carrying, travel and environmental awareness. These are design goals, not validated capabilities; airline cabin-baggage acceptance is not established.

- **Repository:** https://github.com/Pui89/AI-Mobile-Assistant-Robot
- **Website:** [English](https://pui89.github.io/nomad.html) · [ภาษาไทย](https://pui89.github.io/nomad-th.html)
- **Separate indoor home-safety product:** [PUI89 AI HOME](https://github.com/Pui89/AI-Home-Safety-Robot) · [English website](https://pui89.github.io/home.html) · [ภาษาไทย](https://pui89.github.io/home-th.html)


> **Product boundary:** AI NOMAD is a carry-on suitcase-style mobile assistant concept for supervised travel, luggage carrying and suitable everyday mobility. HOME is a separate four-wheel indoor home-safety robot. The products may share versioned PUI89 AI Core contracts, but they are not one robot and do not share physical operating assumptions.

## PUI89 AI NOMAD purpose

AI NOMAD is intended as a practical carry-on suitcase and owner-supervised personal travel companion—not merely a security or surveillance robot. Proposed research areas include:
- Rolling and carrying personal belongings in a compact upright luggage body
- Four-wheel spinner-caster handling and supervised movement in suitable indoor environments
- Travel assistance and environmental awareness in stations, terminals and other permitted settings, subject to access rules and validation
- Optional owner-accompaniment research only after separate safety, privacy and navigation validation concepts
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

AI Mobile Assistant Robot may reuse PUI89 AI Core contracts (WorldState, Observation, ActionProposal and FailureReport), evidence provenance, uncertainty handling, safety gates, benchmark records and report formats. Its four-wheel spinner-caster layout, any powered-wheel arrangement, travel-context perception, environmental protection and risk assessment remain AI NOMAD-specific.

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

**Project-specific priority:** Keep AI NOMAD distinct from indoor HOME as a compact carry-on suitcase-style travel assistant. Prioritise luggage-like handling, four spinner caster mounting, stability, obstacle awareness, battery isolation, offline behaviour, handle durability, serviceability and supervised operation; dimensions, weight, powered-wheel architecture, endurance and weather protection remain design targets until measured.

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

## AI Engineering Intelligence & Carry-on Travel-Assistant Design

NOMAD uses a staged, owner-supervised engineering approach. Its current product target is 8–10 kg complete robot mass, with a 10 kg maximum including battery, handle and installed hardware. Payload capacity remains TBD and must not be assumed above this design limit. The proposed body envelope is 30–33 cm wide × 35–40 cm deep × 35–40 cm high, excluding the extended handle. These are design targets only and do not establish compliance with any airline's carry-on baggage limits.

**Project-specific priorities:** stable load distribution and low centre of gravity; four spinner caster mounts; suitable powered-wheel decision (if required); controlled rolling, turning and braking; protected battery and thermal design; durable telescopic handle; manual pull/recovery; obstacle awareness; offline operation; maintainable luggage-style enclosure; and clear safe-stop behaviour. Indoor controlled operation is the first physical validation domain. Outdoor use is a later, separately gated objective.

**Evidence gates:** CAD and mass ledger → mechanical/electrical analysis → deterministic software tests and documented simulation → supervised low-speed closed-area trials → payload, stability, braking, endurance and environmental validation. Proposed mobility limits are not established capabilities.

---

## Preliminary Prototype Cost Estimate (15 November 2026)

**Indicative one-unit engineering prototype planning range: ฿150,000–฿450,000 (THB).**

**Included at a planning level:** A compact four-wheel mobile platform, drive/braking system, battery, perception/navigation sensors, handle and integration. This is a separate cost target from the current 8–10 kg target (10 kg maximum) and payload requirements, subject to mass-ledger validation; mass and payload must be reconciled before procurement.

**Estimate status:** preliminary internal planning estimate only; not a supplier quotation, purchase commitment, verified bill of materials, fixed project budget or claim that a prototype exists. The range depends on final requirements, component selection, non-Chinese-origin supplier availability, compatibility, import/shipping costs and test scope. Obtain current written quotations and verify country of manufacture/origin, exact model/part number, specifications, warranty and lead time before any procurement.

**Generally excluded:** engineering labour, research salaries, facilities, taxes/VAT, import duties, shipping unless stated in a supplier quotation, certification/regulatory approvals, production tooling, mass production, long-term maintenance and contingency. Project-specific exclusions: any major custom manufacturing or certification not specified in the prototype scope.

**Lower-cost development path:** continue software-first development, open-source tools and simulation before purchasing physical hardware. Shared AI Core software and reusable development equipment may reduce duplicated costs; savings are not yet quantified. No purchase or installation is authorised by this estimate.


### Prototype hardware, materials and component budget breakdown

**Planning scope:** one engineering prototype; total planning range remains **฿150,000–฿450,000 THB**. The following subsystem allowances are preliminary engineering estimates, not supplier quotes. Individual ranges are not a promise of purchase price and must be reconciled against exact selected parts and written quotations before procurement.

| Subsystem / component type | Qty per prototype | Material / specification and function | Indicative allowance (THB) |
|---|---:|---|---:|
| Carry-on suitcase shell + caster mounting | 1 set | Upright luggage enclosure, internal frame, corner protection and four caster mounts | ฿25,000–฿75,000 |
| Optional powered-wheel modules + encoders | TBD | Motorisation and motor count remain undecided; compare passive caster handling and powered-wheel options before estimating | TBD |
| Wheels + brakes + bearings | 1 set | Four swivel spinner casters, bearings, mounting plates and replaceable wear parts | ฿10,000–฿35,000 |
| RGB-D / camera + LiDAR + IMU | 1 set | Travel-scene perception selected for indoor terminal lighting, movement and vibration | ฿25,000–฿75,000 |
| Edge computer + motor controller | 1 set | CPU-first edge computer, MCU and protected motor-control electronics | ฿20,000–฿60,000 |
| Battery + BMS + power | 1 set | Protected battery pack, BMS, fuse, isolation and DC/DC conversion | ฿15,000–฿40,000 |
| Handle, enclosure + environmental protection | 1 set | Retractable telescopic pull handle, luggage-style housing, seals and strain relief | ฿10,000–฿35,000 |
| Harness, fabrication + integration tests | 1 lot | Wiring, brackets, assembly, low-speed stability/braking/endurance tests | ฿25,000–฿70,000 |

**Material families:** aluminium alloy or stainless-steel structural members where suitable; engineering polymer covers; corrosion-resistant fasteners; rated cables/connectors; protective enclosures; and product-specific seals, guards or vibration isolation. Exact alloy/grade, IP rating, load rating and country of manufacture remain unselected until engineering calculations and supplier evidence are available.

**Shared hardware accounting:** Shared AI Core software is not a product BOM. Reusable development computers, cameras or bench instruments must be listed as shared assets and allocated once; do not duplicate their full purchase cost across all six active products. Product-specific mounts, wiring, protection and integration remain in each product allowance.

**Sourcing controls:** prefer non-Chinese-origin candidates only when the exact manufacturing origin is evidenced. Record legal manufacturer, brand, exact model/part number, manufacturing country, evidence URL/document, authorised supplier, dated price/currency, stock, MOQ, lead time, warranty and landed-cost assumptions. Brand headquarters or seller location is not proof of manufacturing origin. Unknown origin = **UNVERIFIED**.

**Prototype boundary:** the allowance is for a controlled engineering prototype, not a certified commercial product or production-ready system. It excludes labour, research salaries, facilities, VAT/tax, import duties, freight/insurance unless explicitly quoted, certification, production tooling, mass production, maintenance and contingency. No purchase, download, installation or supplier commitment is authorised by this documentation.

## Shared Interaction Intelligence — AI NOMAD

AI NOMAD selects a mobile-assistant interaction profile from the [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core):

- Operator/resident voice commands and spoken status reports.
- Thai/English speech recognition and speech response, subject to measured language quality.
- Voice activity detection; optional wake phrase with an explicit microphone/privacy state.
- Environmental sound-event awareness for selected alarms, calls for help and unusual events.
- Optional visual question answering to help an operator interpret a current camera observation.

Interaction is subordinate to safe mobility. Voice commands cannot bypass obstacle avoidance, safe-stop, manual recovery or the independent action gate. Security-patrol events must be described as observations with timestamps, evidence and uncertainty; the AI must not label a person a criminal or intruder based only on appearance or a model score.

**Recommended model candidates for AI NOMAD (not approved or integrated):**

| Model/tool | Role in NOMAD | Status |
|---|---|---|
| [openai/whisper-small](https://huggingface.co/openai/whisper-small) | Thai/English operator and resident speech-to-text; evaluate outdoor noise and CPU/RAM | PENDING_REVIEW |
| [microsoft/Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) | Optional dialogue and instruction clarification; higher-resource candidate, not assumed to run on-device | PENDING_REVIEW |
| [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | English spoken status reports; Thai TTS is not established | PENDING_REVIEW |
| [qualcomm/YamNet](https://huggingface.co/qualcomm/YamNet) | Selected alarm / environmental sound-event classification, advisory only | PENDING_REVIEW |
| [Silero VAD](https://github.com/snakers4/silero-vad) | Speech-segment detection for push-to-talk or bounded listening | PENDING_REVIEW |
| [HuggingFaceTB/SmolVLM2-500M-Video-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct) | Optional bounded camera-scene descriptions for operator assistance, not identity or threat decisions | PENDING_REVIEW |

Do not add openWakeWord's included pretrained weights at this stage: their CC BY-NC-SA 4.0 terms require separate review. Thai speech generation remains an open candidate-research task.

**Maturity:** proposed configuration only. No interaction model is approved, downloaded, installed, integrated or validated for NOMAD.

## World-Class Engineering Standard v1.0

This product follows the proposed [PUI89 World-Class Engineering Standard v1.0](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_WORLD_CLASS_ENGINEERING_STANDARD_V1.0.md), alongside the [PUI89 Simple, Safe & Professional Engineering Standard](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_SIMPLE_SAFE_PROFESSIONAL_STANDARD.md). The shared standard defines requirements traceability, Shared AI Core contracts, PTI evaluation, simulation, safety, hardware provenance, cost engineering, verification and release gates. Product capabilities remain subject to their stated evidence and validation boundaries; this reference does not imply that a gate has been passed.


## PUI89 Technical Visual — AI workflow

![AI NOMAD carry-on suitcase-style mobile assistant workflow with travel-context perception, four spinner caster wheels and supervised rolling mobility.](docs/images/pui89-technical-visual.svg)

*Proposed carry-on suitcase-style mobile assistant workflow. Caster configuration, powered-wheel design, payload, battery endurance and travel-environment limits require staged testing.*

This diagram follows the [PUI89 Technical Visual Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/PUI89_TECHNICAL_VISUAL_STANDARD_V1.0.md). It explains the proposed product-specific AI workflow and does not imply unverified implementation or physical capability.

## Portfolio consistency and founder-approved requirements

**PUI89 AI NOMAD**

Product identity: a **ground-use four-wheel mobile assistant robot**, not a suitcase, luggage product, airline cabin bag or checked baggage. The compact upright enclosure may use a convenient carry-handle, but storage is secondary to supervised mobility and assistance. Do not describe or market NOMAD as aircraft luggage. Physical mobility remains unvalidated until supported by test evidence.

**ข้อกำหนดภาษาไทย**

อัตลักษณ์ผลิตภัณฑ์: **หุ่นยนต์ผู้ช่วยเคลื่อนที่ภาคพื้นดินแบบ 4 ล้อ** ไม่ใช่กระเป๋าเดินทาง สินค้าสัมภาระ หรือกระเป๋าสำหรับนำขึ้นห้องโดยสาร/โหลดใต้ท้องเครื่องบิน รูปทรงตัวถังและพื้นที่จัดเก็บเป็นองค์ประกอบรองจากการเคลื่อนที่และการช่วยเหลือภายใต้การกำกับดูแล

**Portfolio boundary:** PUI89 has exactly six active products. Shared AI Core is infrastructure, not a product. Extreme Flood Rescue AI is inactive as a standalone product; preserve historical records but do not present it as an active product.
