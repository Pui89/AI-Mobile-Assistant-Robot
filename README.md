# PUI89 AI Mobile Assistant Robot


## Public privacy boundary

This public README is limited to the project overview, approved concept material and evidence that can be shared openly. Do not publish API keys, passwords, private tokens, Wi-Fi or internal network settings, private camera footage, personal or precise location data, detailed security configurations, unreleased engineering specifications, or confidential commercial plans. Keep sensitive material in an appropriately access-controlled private location. If a credential may have been exposed, revoke it; removing it from the latest commit does not remove it from Git history.

<!-- PUI89_PINNED_CONCEPT_ILLUSTRATION:START -->
![PUI89 AI NOMAD — compact four-wheel concept](docs/images/ai-nomad-compact-four-wheel.svg)

*Conceptual design illustration — not a built or validated robot. Dimensions, weight, mobility, endurance, weather resistance and field performance remain design targets pending engineering and physical validation.*
<!-- PUI89_PINNED_CONCEPT_ILLUSTRATION:END -->


## Compact product dimensions — proposed design target

| Specification | Proposed target |
|---|---:|
| Width (W) | **28 cm** |
| Length / depth (D) | **22 cm** |
| Height (H) | **45 cm** — body height, excluding the extended handle |
| Total mass | **Maximum 8 kg**, including battery |
| Mobility concept | **Four protected/recessed wheels** |
| Form | Rounded, suitcase-style compact body with retractable pull handle |

The 28 × 22 cm floor footprint is a compact-space design target. The proposed safety direction includes guarded/recessed wheels, rounded body edges, low-mounted battery mass, a physical emergency-stop control and conservative obstacle-aware stopping. These are requirements/proposals, not verified implemented safeguards.

**Status: PROPOSED / NOT MEASURED / NOT VALIDATED.** These dimensions and the 8 kg limit have not been demonstrated by a physical prototype. Internal packaging, wheel size, ground clearance, battery capacity, stability, payload, turning clearance, thermal performance and accessibility must be checked through engineering before the dimensions or weight are treated as final. The design is not claimed to climb stairs or traverse deep sand, mud or rough terrain.

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

This project adopts PUI89 Engineering Intelligence for outdoor scene understanding, route planning, mobility design, payload management, environmental protection and recovery. NOMAD remains distinct from indoor AI HOME: it is a compact, dog-inspired four-wheel outdoor/mobile assistant concept.

**Product-specific design priorities**
- **Outdoor mobility:** study wheel size, ground clearance, approach/departure angles, traction, slope limits, uneven terrain, curb/threshold negotiation and rollover margin.
- **Structure and payload:** retain 8–10 kg as the current target range and 10 kg maximum design limit; validate load distribution, centre of gravity, retention and braking/stopping envelope.
- **Environmental protection:** define rain, splash, dust, mud, humidity, corrosion and cleaning exposure separately; do not claim submersion or flood-crossing capability.
- **Navigation:** combine camera/depth/LiDAR or other approved sensing with odometry and IMU; detect stale maps, GNSS loss, low visibility, people, pets and moving obstacles.
- **Energy and recovery:** estimate terrain-dependent energy use, thermal limits, low-battery return/hold behaviour, stuck detection and safe manual recovery.
- **Human interaction:** provide an accessible handle/manual recovery method, clear status and emergency stop; avoid unsafe following or crowd movement.

**AI engineering methods to evaluate:** visual-inertial/odometric state estimation, terrain classification, traversability estimation, obstacle tracking, semantic mapping, route planning, task scheduling, anomaly detection and digital-twin mobility simulation.

**Evidence gates:** terrain and operating-domain specification → simulation with parameter sweeps → sensor and navigation tests → supervised low-speed closed-area trials → payload, slope, braking, ingress and recovery validation. Proposed mobility limits are not established capabilities.

## Global-by-Design Product Requirement

**Strategic target:** every PUI89 product is designed for potential international use and lawful purchase, not only for the Thai market. This is a development and market-readiness target; it does **not** mean the product is currently manufactured, orderable, shipped worldwide, certified, or approved in every country.

### Requirements for global usability and purchasing
- **International usability:** design clear workflows, accessible interfaces, metric and local-unit support where relevant, time-zone/date/number formatting, and language-ready UI/documentation. English is the initial shared documentation language; additional languages are added according to user and market evidence.
- **Regional configuration:** make country, region, voltage/frequency, radio bands, network connectivity, environmental conditions, plugs/connectors, and local operating constraints explicit where applicable. Never assume one configuration fits every market.
- **Compliance before sale:** identify destination-country laws, product classification, safety, EMC/radio, electrical, battery transport, privacy, cybersecurity, accessibility, import/export, labelling and sector-specific requirements. Use qualified local review and accredited testing where required. Standards references are design inputs, not certification claims.
- **Purchasing transparency:** future buyer information must state exact model/configuration, included items, exclusions, intended use, limitations, warranty, maintenance, support, software/data terms, taxes, shipping, import duties, delivery region and return process. Publish a price only when supported by a dated quote or approved live price source.
- **Global supply and service:** qualify suppliers in multiple regions where practical; document manufacturer and country of manufacture, authorised distributors, spare parts, repair routes, lead times, end-of-life notices and regional support. Do not imply worldwide shipping or service until confirmed.
- **Open-source and commercial rights:** separate open-source software from hardware, model weights, datasets, trademarks and third-party components. Verify each licence and commercial-use right individually.
- **Privacy and security:** minimise collected data, document retention and data location, provide secure update and vulnerability-handling processes, and review applicable privacy laws before deployment.
- **Human safety and local operating limits:** preserve product-specific human oversight and safety boundaries. AI advisory software must not be described as autonomous physical control unless separately engineered, tested and legally approved.

### Release gates
1. **Global design-ready:** requirements, user groups, languages, regions and operating environments documented.
2. **Market research verified:** target-market demand, alternatives, price evidence and channel assumptions documented.
3. **Compliance mapped:** destination-market obligations identified; gaps and required tests recorded.
4. **Prototype validated:** reproducible technical, usability, reliability and safety evidence exists for the stated conditions.
5. **Commercially orderable:** exact configuration, verified price, production capacity, warranty, logistics, returns and support are confirmed.
6. **Region released:** all required local approvals, labels, documentation, import arrangements and service readiness are complete for that region.

**Current status:** global readiness is a portfolio-wide design target. Each product must report its actual gate and evidence separately. No product is to be described as globally available or purchasable until the relevant commercial and regional release gates are met.

**Shared standard:** [PUI89 Global Product Readiness Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/product/PUI89_GLOBAL_PRODUCT_READINESS_STANDARD_V1.0.md).
