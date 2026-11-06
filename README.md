# PUI89 AI NOMAD — Indoor & Outdoor Mobile Assistant Robot
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

## Real Hugging Face model integration — offline OWL-ViT

This repository now contains an executable inference adapter for the real Hugging Face checkpoint **[google/owlvit-base-patch32](https://huggingface.co/google/owlvit-base-patch32)**. It runs zero-shot, text-conditioned object detection against a local image and writes a JSON evidence report with image SHA-256, model ID/revision, candidate labels, scores and bounding boxes.

**Run after manually preparing a compatible local environment and caching the checkpoint:**

```bash
python tools/huggingface_local_vision_demo.py path/to/local-image.jpg --json-out reports/hf-owlvit-report.json
```

- Default device is CPU; CUDA is opt-in with `--device cuda`.
- Both model and processor use `local_files_only=True`; safetensors are required. The model revision is pinned to `cbc355fb364588351c5d51c7f74465e8e7ec6f72`. The safetensors weights are approximately 613 MB; check disk/RAM before any manual download. The script does not download weights, install packages, call hosted inference, or upload images.
- Candidate labels are configured for this project's domain and can be overridden with repeated `--label` arguments.
- The model card declares Apache-2.0 and describes OWL-ViT as zero-shot text-conditioned object detection. Review the exact checkpoint files, upstream licence and data disclosures before commercial release.
- **Status:** executable integration code added; model inference has not been run because weights and optional dependencies were not downloaded or installed. No accuracy, safety or field-performance claim is made.
- Output is an uncertain observation for human review only. It cannot authorize robot/vehicle actuation or consequential decisions.

The report builder is covered by standard-library tests in `tests/test_huggingface_local_vision_demo.py`; these tests validate report/safety metadata, not model accuracy.
