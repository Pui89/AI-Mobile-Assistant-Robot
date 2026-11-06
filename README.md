# HOMEGUARD AI NOMAD
### Portable Outdoor Intelligent Guardian

**Your Intelligent Guardian. Wherever You Go.**

HOMEGUARD AI NOMAD is PUI89's independent outdoor mobile-robot concept: a compact quadruped robot dog for owner-supervised travel, camping and outdoor awareness.

- **Repository:** https://github.com/Pui89/Guard-Ai-Home-Nomad
- **Website:** [English](https://pui89.github.io/homeguard.html) · [ภาษาไทย](https://pui89.github.io/homeguard-th.html)
- **Separate indoor product:** [HOMEGUARD AI HOME](https://github.com/Pui89/HOMEGUARD-AI) · [English website](https://pui89.github.io/home.html) · [ภาษาไทย](https://pui89.github.io/home-th.html)

![HOMEGUARD AI NOMAD quadruped robot-dog concept](docs/images/homeguard-ai-nomad-concept.svg)

> **Product boundary:** NOMAD is for outdoor and travel contexts. HOME is a separate four-wheel indoor robot with its own repository, website pages, requirements and safety case. The products may share versioned PUI89 AI Core contracts, but they are not one robot and do not share physical operating assumptions.

## NOMAD purpose

NOMAD is intended as an owner-supervised outdoor companion and awareness platform. Proposed research areas include:
- Outdoor scene and obstacle awareness
- Owner-approved travel and campsite monitoring
- Mapping and localization research, with safe-stop behaviour when uncertain
- Environmental observations such as smoke, abnormal heat, sound and weather-related conditions when suitable sensors are selected and validated
- Wildlife/activity awareness for human review, not wildlife deterrence or guaranteed protection
- Offline-first operation and clear owner-facing reports

NOMAD is not a firefighting robot, emergency responder or unsupervised roaming machine. It must not enter hazardous areas merely to investigate.

## Proposed physical design targets

| Parameter | Proposed target |
|---|---:|
| Form | Four-legged quadruped robot dog |
| Height | 50–60 cm |
| Width | 30–36 cm |
| Depth | 20–25 cm |
| Complete weight target | 8–10 kg |
| Absolute maximum complete weight | 12 kg |
| Battery | Removable-battery concept |
| Structure | Lightweight protective shell; guarded joints and wiring |
| Environment | Outdoor travel and camping, within validated operating limits |

Weight includes battery, sensors, computer, enclosure and accessories. Dimensions and weight are design goals, not measured prototype specifications. Terrain, gait, endurance, weather limits and payload remain unvalidated.

## Proposed operating workflow

Observe → check evidence quality → understand location and context → assess uncertainty and risk → choose a safe movement state → report to the owner.

The owner remains responsible for decisions. Return-to-owner behaviour is only a future requirement: if localization, route safety or battery reserve is insufficient, the robot should stop safely rather than attempt an unsafe return.

## Safety and resilience requirements

- Define and test limits for rain, dust, temperature, slopes, loose ground, water exposure, darkness, battery endurance and connectivity.
- Prioritize battery protection, electrical isolation, overcurrent protection, thermal monitoring and guarded wiring.
- Treat weather resistance, water resistance, fire performance and any hazardous-atmosphere protection as engineering requirements requiring specified tests; do not claim waterproof, fireproof or explosion-proof performance.
- Never delay emergency response or substitute for certified alarms and qualified responders.
- Use human supervision, safe-stop defaults and clear uncertainty reporting.
- Protect location data and avoid unnecessary recording of people.

## Shared intelligence, separate product engineering

NOMAD may reuse PUI89 AI Core contracts (WorldState, Observation, ActionProposal and FailureReport), evidence provenance, uncertainty handling, safety gates, benchmark records and report formats. Its quadruped locomotion, outdoor navigation, sensor layout, environmental protection and risk assessment remain NOMAD-specific.

## Current development status

**FOUNDATION / SIMULATION-ONLY / CONCEPT.** The repository contains an early deterministic software foundation, documentation and automated tests. It does not establish a built robot, real sensor integration, trained AI model, validated locomotion, outdoor reliability, certified safety or real-world hazard-detection performance.

## Zero-cost and supply-chain policy

No paid API, subscription, cloud GPU or automatic model download is required for this project foundation. Do not add packages, models or external services without checking origin, licence, security, resource requirements and total cost. PUI89 excludes Chinese-origin AI models, providers and model-hosting services from its approved stack.

## Evidence labels

PROPOSED = planned; IMPLEMENTED = code exists; TESTED = automated test passed; SIMULATION-ONLY = synthetic inputs only; MEASURED = quantitative result with method; VERIFIED = reproducibly checked; NOT_VALIDATED = real-world performance not established.

See [Architecture](docs/ARCHITECTURE.md), [Safety Case](docs/SAFETY_CASE.md), [Intelligence Catalogue](docs/INTELLIGENCE_CATALOGUE.md), [Supply-chain Policy](docs/MODEL_AND_SUPPLY_CHAIN_POLICY.md), [Roadmap](docs/ROADMAP.md), [Water Resilience Standard](docs/PUI89_WATER_RESILIENCE_STANDARD.md) and [Resilience Standard](docs/PUI89_RESILIENCE_STANDARD.md).

**PUI89 — Intelligent Systems. Verifiable Decisions. Safer Outcomes.**
