# PUI89 AI NOMAD — Indoor & Outdoor Mobile Assistant Robot

## Project website QR codes

<table><tr><td align="center"><strong>English website</strong><br><a href="https://pui89.github.io/homeguard.html"><img src="https://pui89.github.io/qr/nomad-en.png" width="160" alt="PUI89 AI NOMAD English website QR code"></a><br><a href="https://pui89.github.io/homeguard.html">Open English website</a></td><td align="center"><strong>เว็บไซต์ภาษาไทย</strong><br><a href="https://pui89.github.io/homeguard-th.html"><img src="https://pui89.github.io/qr/nomad-th.png" width="160" alt="QR Code เว็บไซต์ภาษาไทย PUI89 AI NOMAD"></a><br><a href="https://pui89.github.io/homeguard-th.html">เปิดเว็บไซต์ภาษาไทย</a></td></tr></table>

## PUI89 product maturity snapshot — 7 November 2026

**Strategic direction: From AI Projects to AI Products.**  
**Current maturity: Grade 1–2 — Product Definition and Early Engineering Foundation.** NOMAD has a defined quadruped mobile-assistant direction, proposed physical targets and an early deterministic software foundation. It is not a built or validated robot dog.

| Area | Verified position |
|---|---|
| Product definition | Separate quadruped indoor/outdoor mobile assistant for supervised travel, accompaniment and carrying concepts; HOME remains a separate four-wheel indoor product. |
| Physical requirements | Proposed 50–60 cm height, 30–36 cm width, 20–25 cm depth, 8 kg target and 10 kg maximum. These are design targets, not measured specifications. |
| Software and AI | Early deterministic software foundation, documentation and automated tests are present. Opt-in vision-model adapters are documented, but model inference and NOMAD-specific accuracy are not yet tested. |
| Physical product | No built robot, validated gait, payload, endurance, terrain capability, weather/water resistance or certified safety performance is established. |

**Next product gate:** produce a traceable mechanical/electrical requirements set and hazard analysis; assess centre of mass, joint protection, battery and thermal safety, safe-stop/recovery, payload stability and serviceability. Define separate indoor/outdoor simulation scenarios and measurable gait, endurance and obstacle tests before any hardware work.

**Product discipline:** water resistance, fire performance and outdoor reliability are requirements to test, not existing claims. Keep owner supervision, privacy and safe-stop behaviour central. No paid API, cloud GPU, automatic model download or physical robot actuation is part of this update.


### A Portable Quadruped Assistant for Home, Travel and Everyday Life

**A mobile companion designed to help people indoors and outdoors.**

PUI89 AI NOMAD is an early-stage mobile assistant robot concept with a quadruped, robot-dog form. It is intended to support people in everyday environments, including carrying belongings, supervised accompaniment, travel and outdoor awareness. These are design goals, not validated capabilities.

- **Repository:** https://github.com/Pui89/AI-NOMAD
- **Website:** [English](https://pui89.github.io/homeguard.html) · [ภาษาไทย](https://pui89.github.io/homeguard-th.html)
- **Separate indoor home-safety product:** [PUI89 AI HOME](https://github.com/Pui89/AI-HOME) · [English website](https://pui89.github.io/home.html) · [ภาษาไทย](https://pui89.github.io/home-th.html)

![PUI89 AI NOMAD quadruped robot-dog concept](docs/images/homeguard-ai-nomad-concept.svg)

> **Product boundary:** NOMAD is a mobile assistant concept for indoor and outdoor everyday use, travel and carrying assistance. HOME is a separate four-wheel indoor home-safety robot. The products may share versioned PUI89 AI Core contracts, but they are not one robot and do not share physical operating assumptions.

## NOMAD purpose

NOMAD is intended as an owner-supervised mobile companion. Proposed research areas include:
- Carrying shopping, luggage and personal belongings within a validated payload limit
- Owner-supervised accompaniment in suitable indoor and outdoor environments
- Travel, walking, park, station and campsite assistance concepts
- Indoor/outdoor scene and obstacle awareness
- Mapping and localization research, with safe-stop behaviour when uncertain
- Environmental observations when suitable sensors are selected and validated
- Offline-first operation and clear owner-facing reports

NOMAD is not an emergency responder or an unsupervised roaming machine. It must not enter hazardous areas merely to investigate. Carrying capacity, following behaviour, accessibility support and safe operation remain unvalidated design goals.

## Proposed physical design targets

| Parameter | Proposed target |
|---|---:|
| Form | Four-legged quadruped robot dog |
| Height | 50–60 cm |
| Width | 30–36 cm |
| Depth | 20–25 cm |
| Complete weight target | 8 kg |
| Absolute maximum complete weight | 10 kg |
| Battery | Removable-battery concept |
| Structure | Lightweight protective shell; guarded joints and wiring |
| Environment | Indoor and outdoor use, only within separately validated operating limits |

Weight includes battery, sensors, computer, enclosure and accessories. Dimensions and weight are design goals, not measured prototype specifications. Terrain, gait, endurance, weather limits, payload and indoor floor compatibility remain unvalidated.

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

NOMAD may reuse PUI89 AI Core contracts (WorldState, Observation, ActionProposal and FailureReport), evidence provenance, uncertainty handling, safety gates, benchmark records and report formats. Its quadruped locomotion, indoor/outdoor navigation, sensor layout, environmental protection and risk assessment remain NOMAD-specific.

## Current development status

**FOUNDATION / SIMULATION-ONLY / CONCEPT.** The repository contains an early deterministic software foundation, documentation and automated tests. It does not establish a built robot, real sensor integration, trained AI model, validated locomotion, indoor/outdoor reliability, certified safety or real-world hazard-detection performance.

## Zero-cost and supply-chain policy

No paid API, subscription, cloud GPU or automatic model download is required for this project foundation. Do not add packages, models or external services without checking origin, licence, security, resource requirements and total cost. PUI89 excludes Chinese-origin AI models, providers and model-hosting services from its approved stack.

## Evidence labels

PROPOSED = planned; IMPLEMENTED = code exists; TESTED = automated test passed; SIMULATION-ONLY = synthetic inputs only; MEASURED = quantitative result with method; VERIFIED = reproducibly checked; NOT_VALIDATED = real-world performance not established.

See [Architecture](docs/ARCHITECTURE.md), [Safety Case](docs/SAFETY_CASE.md), [Intelligence Catalogue](docs/INTELLIGENCE_CATALOGUE.md), [Supply-chain Policy](docs/MODEL_AND_SUPPLY_CHAIN_POLICY.md), [Roadmap](docs/ROADMAP.md), [Water Resilience Standard](docs/PUI89_WATER_RESILIENCE_STANDARD.md) and [Resilience Standard](docs/PUI89_RESILIENCE_STANDARD.md).

**PUI89 — Intelligent Systems. Verifiable Decisions. Safer Outcomes.**


## Hugging Face vision models — opt-in local integration

This repository now includes real Hugging Face checkpoint adapters in [`pui89_models/hf_vision.py`](pui89_models/hf_vision.py), with project-specific usage boundaries in [`docs/HUGGING_FACE_MODEL_INTEGRATION.md`](docs/HUGGING_FACE_MODEL_INTEGRATION.md).

- **OWLv2:** `google/owlv2-base-patch16-ensemble` for text-conditioned object proposals.
- **Intel DPT-Hybrid:** `Intel/dpt-hybrid-midas` for relative scene depth where appropriate; not calibrated distance or physical depth.
- **Zero-cost default:** no packages or model weights are installed/downloaded automatically; CPU-only inference, local cache only by default, no hosted inference API or cloud GPU.
- **Evidence status:** adapter code is added; model inference and project-specific accuracy are NOT YET TESTED. Outputs remain uncertain observations for human review, never actuator commands.
