# PUI89 AI NOMAD — Ground-Use Four-Wheel Mobile Assistant Robot

![PUI89 AI NOMAD ground-use four-wheel mobile assistant robot concept](docs/images/ai-nomad-compact-four-wheel.svg)

*Concept illustration only. It is not evidence of a built, integrated, tested or validated robot.*

## Official product identity

**PUI89 AI NOMAD is a ground-use four-wheel mobile assistant robot.** It is not luggage, a suitcase product, an airline cabin bag or checked baggage. Its compact upright enclosure and retractable handle are robot design features. Any storage compartment is secondary to supervised mobility and practical assistance.

NOMAD is distinct from:
- **PUI89 AI HOME:** an indoor home-assistance robot with a separate mission, enclosure and safety case.
- **PUI89 Sentinel:** a four-legged All-Terrain Exploration & Inspection Robot. NOMAD has four wheels, not articulated legs.

## Mission and intended use

NOMAD is intended to support people with supervised ground mobility and practical assistance in suitable, authorised environments. The first use cases must be defined with users before hardware is selected or physical capabilities are claimed.

Potential software and assistance functions are proposals until separately implemented and tested:
- Local environment and scene awareness.
- Obstacle and walkway awareness, with uncertainty and safe-stop proposals.
- Human-reviewed task and route assistance in supported environments.
- Contextual alerts for selected environmental or equipment conditions.
- User interaction and assistance requests.
- Battery, power and thermal status monitoring where supported by verified interfaces.
- Optional small-item storage as a secondary convenience, subject to measured payload and stability limits.

No unsupervised public-space autonomy, person identification, coercive enforcement or hazardous physical action is claimed.

## Physical design requirements

| Requirement | Current definition | Evidence status |
|---|---|---|
| Mobility architecture | Four-wheel ground robot | Design requirement |
| Enclosure | Compact upright robot enclosure | Concept |
| Handle | Retractable/manual handling feature | Concept |
| Complete robot mass | 8–10 kg design target; **10 kg maximum** including battery, handle, wiring and installed hardware | Not measured |
| Payload | TBD; must be established through structural, traction, braking and stability analysis | Unknown |
| Drive, steering and braking | To be selected after mission definition and engineering review | Not selected or validated |
| Environment limits | Floors, thresholds, ramps, slopes, outdoor surfaces, rain/splash, dust and temperature require defined limits | Not validated |

The mass limit is a design constraint, not a measured prototype result. Do not add an assumed payload above the 10 kg complete-robot maximum.

## Safety and human oversight

- Keep operation supervised and within a documented environment and operating envelope.
- Treat uncertain, stale, conflicting or missing sensor inputs as unknown.
- Propose a safe stop or request human review when the path, localisation, stability, battery or environment is uncertain.
- Keep safety control independent of AI model confidence.
- No autonomous physical action is authorised by this README.
- No stair/escalator traversal, public-road autonomy, waterproofing, outdoor endurance or field capability is claimed without direct evidence.

## Software-first development sequence

1. Define a narrow ground-use mission, user, environment and measurable acceptance criteria.
2. Specify observation, world-state, assistance proposal and failure-report interfaces using the shared PUI89 AI Core.
3. Build CPU-first software and synthetic regression tests without claiming real-world accuracy.
4. Use simulation only where a defined requirement justifies it; label simulation evidence separately.
5. Evaluate hardware candidates only after the mission and operating envelope are approved.
6. Conduct controlled bench and supervised field tests only after safety review and explicit approval.
7. Publish claims only with traceable, dated evidence.

Use open-source tools after checking licence, provenance, security, resource requirements and compatibility. Do not download models/data, install dependencies, purchase hardware or use paid APIs/services without explicit approval.

## Evidence maturity

Use only these labels, each backed by an appropriate record: **Proposed, Specified, Implemented, Simulated, Software-tested, Bench-tested, Field-tested, Validated, Certified, Unknown.**

The current physical product status is concept/requirements. A passing software test does not establish physical mobility, navigation quality, safety, endurance or field validation.

## Project links

- [English project website](https://pui89.github.io/nomad.html)
- [เว็บไซต์ภาษาไทย](https://pui89.github.io/nomad-th.html)
- [PUI89 portfolio](https://pui89.github.io/)
- [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core)

## Portfolio boundary

PUI89 has **exactly six active products**. Shared AI Core is shared infrastructure, not a seventh product. Extreme Flood Rescue AI is an inactive historical standalone project; preserve its repository and records, but do not present it as an active product.

**ข้อกำหนดภาษาไทย**

PUI89 AI NOMAD เป็น **หุ่นยนต์ผู้ช่วยเคลื่อนที่ภาคพื้นดินแบบ 4 ล้อ** ไม่ใช่กระเป๋าเดินทาง ไม่ใช่สินค้าสัมภาระ และไม่ใช่กระเป๋าสำหรับนำขึ้นห้องโดยสารหรือโหลดใต้ท้องเครื่องบิน ตัวถังทรงตั้งและด้ามจับเป็นองค์ประกอบการออกแบบของหุ่นยนต์ ส่วนพื้นที่จัดเก็บเป็นฟังก์ชันรองจากการเคลื่อนที่และการช่วยเหลือภายใต้การกำกับดูแล

NOMAD มีเป้าหมายเพื่อช่วยเหลือผู้ใช้ในการเคลื่อนที่ภาคพื้นดินและงานช่วยเหลือในสภาพแวดล้อมที่เหมาะสม โดยต้องมีมนุษย์กำกับดูแล กำหนดภารกิจและขอบเขตการใช้งานก่อนเลือกฮาร์ดแวร์ น้ำหนักรวมเป้าหมาย 8–10 กก. และสูงสุด 10 กก. รวมแบตเตอรี่ ด้ามจับ สายไฟ และอุปกรณ์ที่ติดตั้งทั้งหมด เป็นข้อกำหนดการออกแบบที่ยังไม่ได้วัดจากต้นแบบจริง

ความสามารถด้าน AI ทั้งหมดเป็นข้อเสนอจนกว่าจะมีการพัฒนาและทดสอบแยกต่างหาก เมื่อข้อมูลไม่ครบ ล้าสมัย ขัดแย้ง หรือไม่แน่นอน ต้องระบุว่าไม่ทราบและขอให้มนุษย์ตรวจสอบ ไม่กล่าวอ้างการทำงานอัตโนมัติในพื้นที่สาธารณะ การนำทางจริง ความปลอดภัยทางกายภาพ หรือสมรรถนะภาคสนามโดยไม่มีหลักฐาน
