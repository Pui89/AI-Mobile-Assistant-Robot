# HOMEGUARD AI
### Evidence-Driven Multi-Modal Predictive Building Intelligence

**Detect Early. Locate Precisely. Protect Better.**

<p align="center"><img src="docs/images/homeguard-ai-mark.svg" alt="HOMEGUARD AI geometric building intelligence mark" width="310" /></p>

![HOMEGUARD AI — Building intelligence concept](docs/images/homeguard-ai-building-concept.svg)

> **How it works:** Observe building conditions → locate each observation → verify evidence quality → understand the building's changing state → recommend human-reviewed action → measure whether the improvement worked.

HOMEGUARD AI is a software-first building-condition intelligence platform. It organizes observations from structural, electrical, fire/life-safety, water, environmental, acoustic, light and thermal sources; compares them with documented baselines; exposes uncertainty; and helps people prioritize verification.

> **Current status: FOUNDATION / SIMULATION-ONLY.** This is an initial deterministic software demonstrator, not a deployed building-monitoring product. No real sensor integration, trained AI model, certified alarm, structural certification or real-world hazard-detection performance is claimed.

## Initial implementation
- Typed, provenance-aware sensor observations and baselines
- Quality checks for stale, missing, invalid and uncalibrated evidence
- Transparent baseline-deviation detection
- Deterministic synthetic three-floor scenario
- Machine-readable JSON findings
- Automated tests and GitHub Actions CI

The 29-capability catalogue is a roadmap, not 29 implemented models. No trained model is required for the first demonstrator.

## Future mobile robot concept (PROPOSED)

<p align="center">
  <img src="docs/images/homeguard-ai-robot-concept.svg" alt="3D-style PUI89 Homeguard AI robot concept with rounded navy and electric-cyan body, protected cameras and sensors, concealed wheels and automatic charging dock" width="100%" />
</p>

<p align="center"><em>Concept illustration only — proposed design, not a built or certified robot.</em></p>

A future Homeguard AI mobile robot may extend the platform with four missions:

1. **Protect:** autonomously patrol approved indoor areas, identify unusual activity and report evidence for human review.
2. **Detect building hazards:** collect and assess fire-related and explosion-related warning signals, such as smoke, abnormal heat, acoustic events or pressure changes, where suitable sensors are installed and validated. The robot is an awareness and reporting system; it is not a firefighting robot, does not handle explosive materials and does not cause or trigger explosions.
3. **Explore:** build and update an indoor map, navigate around people and obstacles, inspect assigned areas and return to a charging dock when conditions permit.
4. **Wildlife intrusion detection:** detect and report possible snakes and other reptiles inside the home, including geckos, lizards and monitor lizards. Estimate their location and movement, preserve a visual evidence snapshot where privacy settings permit, and send an alert for human review. Species identification and confidence must be treated cautiously; an uncertain snake sighting should be handled as potentially dangerous.

### Wildlife safety behaviour (PROPOSED)

- Keep a safe distance; do not touch, chase, corner, scare, trap or attempt to remove an animal.
- Do not block its escape route or move closer to obtain a better image.
- Stop movement or retreat only when the robot can do so without approaching the animal; otherwise remain at a safe distance and alert the homeowner.
- Notify people to keep children and pets away. For a suspected snake, advise contacting a qualified local wildlife or snake-rescue service.
- Report the sighting location, time, direction of travel, image evidence (if permitted) and model confidence. Clearly label uncertain classifications.
- Avoid unnecessary indoor recording; process locally where feasible and apply privacy-by-design controls.

### Robot safety and protective engineering

Safety is a design requirement, not a capability that can be claimed without testing.

- **Do not become an ignition source:** prioritize battery safety, thermal-runaway mitigation, electrical isolation, overcurrent protection, protected wiring and suitable component selection.
- **Fire resistance:** select enclosure and insulation materials for defined temperature and flame-exposure requirements, then verify them through appropriate independent testing. “Fire-resistant” does not mean fireproof.
- **Explosion protection:** distinguish preventing the robot from igniting a hazardous atmosphere from surviving an external blast. These are different engineering problems. Operation in a classified explosive atmosphere requires a design assessed and certified for the specific zone, gas/dust group and temperature class. No general blast-survival or explosion-proof claim is made.
- **Emergency behaviour:** on a suspected hazard, warn the responsible people, preserve available evidence and stop or retreat only when the route and robot state are assessed as safe. Never send the robot into a dangerous area merely to investigate.
- **Human safety first:** certified building alarms, emergency procedures and qualified responders remain authoritative. The robot must not delay evacuation or emergency response.

The mobile robot and wildlife-detection capability are **future proposals only**. They have not been built, integrated, certified or validated. Sensors, animal detection, species classification, mobility, battery protection, fire performance and any explosion-protection rating require separate requirements, engineering reviews and test evidence before deployment.

## Quick start
Requires Python 3.11+.
```bash
python -m pip install -e ".[dev]"
pytest
homeguard-simulate --seed 89 --output report.json
```

## Safety and privacy
Decision support only. The current software demonstrator does not operate breakers, valves, lifts, doors or alarms; certify a building; or replace qualified professionals. Certified smoke, fire, CO and electrical protection devices remain primary. Never wait for AI analysis before following a certified alarm or established emergency procedure. Minimize personal data; prefer acoustic features over recording conversations; avoid unnecessary indoor video, face recognition and profiling.

## Procurement policy
The initial foundation has no remote inference, model download, paid API, subscription or cloud-GPU dependency. This project excludes Chinese-origin AI models, providers and model-hosting services from its approved stack. Future dependencies require provenance, ownership, licence, security, privacy, network, resource and cost review.

## Evidence labels
PROPOSED = planned; IMPLEMENTED = code exists; TESTED = automated test passed; SIMULATION-ONLY = synthetic inputs only; MEASURED = quantitative result with method; VERIFIED = reproducibly checked; NOT_VALIDATED = real-world performance not established.

See [Architecture](docs/ARCHITECTURE.md), [Safety Case](docs/SAFETY_CASE.md), [Intelligence Catalogue](docs/INTELLIGENCE_CATALOGUE.md), [Supply-chain Policy](docs/MODEL_AND_SUPPLY_CHAIN_POLICY.md) and [Roadmap](docs/ROADMAP.md).

**PUI89 — Intelligent Systems. Verifiable Decisions. Safer Outcomes.**