# PUI89 AI NOMAD — Indoor & Outdoor Mobile Assistant Robot

> **PUI89 engineering standard:** [Simple, Safe and Professional](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_SIMPLE_SAFE_PROFESSIONAL_STANDARD.md) — shared guidance for usability, safety, evidence, privacy and maintainable engineering.

> **PUI89 | Intelligent Systems. Verifiable Decisions. Safer Outcomes.**
> 
> **Project:** PUI89 AI NOMAD  
> **Focus:** Owner-supervised quadruped mobile assistant robot concept  
> **Development stage:** Early software foundation and design targets; locomotion, endurance and field performance are not validated.
> 
> **Project website:** [English](https://pui89.github.io/homeguard.html) · [ภาษาไทย](https://pui89.github.io/homeguard-th.html) · [PUI89 portfolio](https://pui89.github.io/)
> 
> **Validation boundary:** Proposed dimensions and weight are design targets, not measured prototype specifications; NOMAD is not an emergency responder or unsupervised roaming system.

## Commercial readiness progress

**30% — evidence-based commercial-readiness estimate**  
**Target: 100% = ready for an appropriately scoped commercial release or formal commercial procurement submission.** This is not a code-completion percentage, a sales forecast, or a claim of product certification. Scores are provisional and based on the evidence currently documented in this repository; they must be revised when new evidence is verified.

The repository contains concept requirements, architecture, early deterministic software foundation and automated tests. No built robot, validated locomotion, real sensor integration, endurance, weather protection or field performance is established.

| Readiness gate | Weight | Evidence credit |
|---|---:|---:|
| Product purpose & requirements | 10 | 8 |
| Architecture & engineering design | 10 | 8 |
| Working software baseline | 15 | 5 |
| Reproducible tests & evaluation | 15 | 4 |
| Integrated product prototype | 15 | 0 |
| Safety, reliability & real-world validation | 15 | 1 |
| Licensing, IP & regulatory readiness | 10 | 3 |
| Commercial release package & support | 10 | 1 |
| **Total** | **100** | **30** |

**What 100% requires:** a defined product and acceptance criteria; integrated release candidate; reproducible performance and reliability evidence; appropriate safety and real-world validation; verified rights/licences and applicable regulatory conformity; manufacturing/deployment, pricing, warranty, maintenance, user documentation and support arrangements. A score of 100% is awarded only after all applicable release gates are evidenced and reviewed. Partner or research discussions may happen earlier, but must be labelled as development-stage collaboration—not a ready-to-sell product.

**Next commercial-readiness gate:** close the missing evidence above, beginning with project-specific working-product validation and safety evidence. Never count a planned feature, concept image, tool inventory, synthetic-only result or unrun test as a completed gate.

_Last readiness review: 7 November 2026. This estimate can rise or fall as evidence changes._


## Project website QR codes

<table><tr><td align="center"><strong>English website</strong><br><a href="https://pui89.github.io/homeguard.html"><img src="https://pui89.github.io/qr/nomad-en.png" width="160" alt="PUI89 AI NOMAD English website QR code"></a><br><a href="https://pui89.github.io/homeguard.html">Open English website</a></td><td align="center"><strong>เว็บไซต์ภาษาไทย</strong><br><a href="https://pui89.github.io/homeguard-th.html"><img src="https://pui89.github.io/qr/nomad-th.png" width="160" alt="QR Code เว็บไซต์ภาษาไทย PUI89 AI NOMAD"></a><br><a href="https://pui89.github.io/homeguard-th.html">เปิดเว็บไซต์ภาษาไทย</a></td></tr></table>
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

<!-- PUI89_DAILY_PROGRESS:START -->
## Daily project progress

**🟠 30% — Foundation and prototype stage**  
**Evidence score:** 30/100 · **Review date:** 7 November 2026 (Asia/Bangkok)  
**Progress graph:** 🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 30%

This is an evidence-weighted commercial-readiness estimate, not a code-completion percentage, sales forecast, certification, or measured real-world performance. Scores change only when repository evidence is reviewed and the evidence credits below are updated. The daily run refreshes the review date; it never increases the score merely because time has passed.

| Readiness gate | Evidence credit | Visual score |
|---|---:|---|
| Purpose & requirements | 8/10 | 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜ |
| Architecture & engineering | 8/10 | 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜ |
| Working software baseline | 5/15 | 🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| Reproducible tests & evaluation | 4/15 | 🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| Integrated product prototype | 0/15 | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| Safety & real-world validation | 1/15 | 🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| Licensing & regulatory readiness | 3/10 | 🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜ |
| Release package & support | 1/10 | 🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| **Total** | **30/100** | **🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜** |

**Next milestone:** Improve the lowest-scoring applicable gate with reproducible project-specific evidence. Planned work, concept artwork, unrun tests, synthetic-only results and tool inventories do not earn evidence credit.

**Status boundary:** Software tests and simulations do not establish a built, certified, field-tested or commercially validated physical product. Real-world claims require separate, traceable validation.

<!-- PUI89_DAILY_PROGRESS:END -->


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

A scan or passing test is evidence only for the checks actually run; it does not prove the repository is absence of malware or vulnerabilities.

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

**Project-specific priority:** Keep NOMAD distinct from indoor HOME as a portable/outdoor mobile assistant. Prioritise stability, obstacle handling, battery isolation, offline behaviour, enclosure drainage/sealing strategy, serviceability and supervised operation; dimensions, weight, locomotion, endurance and weather protection remain design targets until measured.

**Status legend:** 🔵 framework guidance added · 🟢 engineering quality target · 🟠 evidence or validation still required · ⚪ not assessed. These labels describe the review state of recommendations, not overall project maturity. Project maturity changes only when supported by verified repository evidence, reproducible tests or controlled validation.
