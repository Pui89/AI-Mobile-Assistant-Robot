# PUI89 AI NOMAD — Ground-Use Four-Wheel Mobile Assistant Robot

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
