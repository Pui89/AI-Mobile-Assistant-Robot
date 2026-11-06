# PUI89 AI NOMAD — Outdoor Mobile Assistant Robot
### Quadruped robot-dog concept for supervised travel and outdoor assistance

**A mobile assistant concept for carrying support, owner-supervised travel and outdoor awareness.**

PUI89 AI NOMAD is an early-stage software and robotics research project. Its proposed quadruped form is intended to accompany its owner outdoors, explore safe carrying assistance and provide useful environmental observations. This is a concept—not a completed or validated robot.

- **Repository:** https://github.com/Pui89/AI-NOMAD
- **Website:** [English](https://pui89.github.io/nomad.html) · [ภาษาไทย](https://pui89.github.io/nomad-th.html)
- **Separate indoor product:** [PUI89 AI HOME](https://github.com/Pui89/HOMEGUARD-AI) · [English](https://pui89.github.io/home.html) · [ภาษาไทย](https://pui89.github.io/home-th.html)

![PUI89 AI NOMAD quadruped outdoor mobile assistant concept](docs/images/homeguard-ai-nomad-concept.svg)

> **Product boundary:** AI NOMAD is the outdoor/travel assistant. AI HOME is a separate four-wheel indoor home-assistance and safety concept. They have separate repositories, physical requirements, safety cases and websites. They may reuse PUI89 AI Core software contracts, but they are not one product.

## Purpose and intended assistance

- **Carrying support:** explore a stable, secure way to carry selected travel belongings, subject to a separately tested payload and centre-of-gravity limit.
- **Owner-supervised following:** investigate controlled following and owner-approved movement, with obstacle checks and safe-stop behaviour.
- **Outdoor awareness:** observe terrain, obstacles and selected environmental conditions for owner review.
- **Travel and campsite support:** provide owner-approved observation and status reports; no unsupervised roaming.
- **Offline-first operation:** explain what is known, unknown, changed or potentially unsafe, with timestamps and evidence quality.
- **Agentic AI, VLM and VLA research:** start with deterministic workflows and mock action interfaces. Model outputs remain proposals behind safety gates.

NOMAD is not a firefighting robot, emergency responder, autonomous security guard or replacement for trained people and certified safety systems. It must not enter hazardous areas to investigate.

## Proposed physical design targets

| Parameter | Proposed target |
|---|---:|
| Form | Four-legged quadruped robot dog |
| Complete weight target | 8 kg |
| Maximum complete weight | 10 kg |
| Height | 50–60 cm |
| Width | 30–36 cm |
| Depth | 20–25 cm |
| Carrying payload | Not yet specified or validated |
| Battery | Removable-battery concept |
| Environment | Outdoor travel within a future validated operating envelope |

Weight includes battery, sensors, computing hardware, enclosure and accessories. Dimensions and mass are design targets, not measured prototype specifications. Payload, centre of gravity, gait, stability, speed, endurance, terrain limits and transport performance remain unvalidated. A payload limit must be established through structural, stability and safety tests before practical use.

## Proposed operating workflow

Observe → validate evidence → update world state → assess uncertainty and risk → propose a bounded action → apply safety gates → request owner approval where needed → verify and report.

If localization, route safety, battery reserve or sensor quality is insufficient, the system should enter a controlled safe stop and notify the owner rather than continue blindly.

## Safety and resilience requirements

- Define and test limits for rain, dust, temperature, slopes, loose terrain, water exposure, darkness, battery endurance and connectivity loss.
- Protect battery cells, electrical circuits, wiring and moving joints; include suitable overcurrent and thermal protections.
- Water resistance, weather resistance and fire performance are engineering requirements requiring defined tests. They are not current product claims.
- Do not claim waterproof, fireproof or explosion-proof performance without appropriate test evidence and applicable certification.
- Use conservative safe-stop defaults for uncertain perception, faults, unsafe terrain and low battery.
- Protect location and personal data; minimize unnecessary recording of bystanders.
- Never enter fire, floodwater, unstable structures or other hazardous areas to investigate. Do not replace emergency services, certified alarms or trained responders.

## Shared PUI89 AI Core

NOMAD may reuse versioned PUI89 contracts and evidence infrastructure: WorldState, Observation, ActionProposal and FailureReport; evidence provenance and timestamps; uncertainty propagation and conflict detection; safety gates and human-review routing; and reproducible benchmark records.

Quadruped locomotion, outdoor navigation, carrying limits, sensor placement, environmental protection and platform-specific safety validation remain NOMAD-specific.

## Current development status

**FOUNDATION / CONCEPT / SIMULATION-ONLY where explicitly labelled.** The repository contains an early software and documentation foundation. This does not establish a built robot, integrated sensors, trained AI model, validated locomotion, carrying performance, outdoor reliability, certified safety or commercial readiness.

## Zero-cost and supply-chain policy

No paid API, subscription, cloud GPU, hosted inference service or automatic model download is required for the project foundation. Do not introduce paid services, new packages, model weights or recurring-cost commitments without explicit approval. Check origin, licence, security, hardware requirements and total cost before adopting any dependency. PUI89 excludes Chinese-origin AI models, providers and model-hosting services from its approved stack.

## Evidence labels

- **PROPOSED** — planned design or capability.
- **IMPLEMENTED** — code or documentation exists.
- **TESTED** — an identified automated test passed.
- **SIMULATION-ONLY** — synthetic or simulated inputs only.
- **MEASURED** — quantitative result with method and conditions.
- **VERIFIED** — reproducibly checked against stated criteria.
- **NOT_VALIDATED** — real-world performance has not been established.

See [Architecture](docs/ARCHITECTURE.md), [Safety Case](docs/SAFETY_CASE.md), [Intelligence Catalogue](docs/INTELLIGENCE_CATALOGUE.md), [Supply-chain Policy](docs/MODEL_AND_SUPPLY_CHAIN_POLICY.md), [Roadmap](docs/ROADMAP.md), [Water Resilience Standard](docs/PUI89_WATER_RESILIENCE_STANDARD.md) and [Resilience Standard](docs/PUI89_RESILIENCE_STANDARD.md).

**PUI89 — Intelligent Systems. Verifiable Decisions. Safer Outcomes.**
