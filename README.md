# HOMEGUARD AI NOMAD
### Portable Home-and-Outdoor Intelligent Guardian

**Your Intelligent Guardian. Wherever You Go.**

> **Product identity:** HOMEGUARD AI NOMAD is the proposed portable mobile-robot product within PUI89's HOMEGUARD AI concept. The repository name is `Homeguard-Ai-Nomad`.

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

## HOMEGUARD AI NOMAD — portable robot concept (PROPOSED)

<em>Physical design target — concept only, not a built or measured specification.</em>

| Design parameter | Proposed target |
|---|---:|
| Total height, including sensor unit | Up to 50 cm |
| Main body height | Approximately 30–35 cm |
| Body width | 30–35 cm |
| Body length | 40–45 cm |
| Target total weight | Approximately 8 kg |
| Wheels | Four all-terrain wheels, approximately 10–13 cm diameter |

The design priority is a low, wide, lightweight body that one person can lift and transport. The 8 kg target and dimensions are engineering goals, not verified performance. Final dimensions depend on battery capacity, sensor selection, stability, weather protection, payload and safety testing.

A future NOMAD robot may extend the software platform with these missions:

1. **Protect:** autonomously patrol approved indoor areas, identify unusual activity and report evidence for human review.
2. **Detect hazards:** collect and assess fire-related and explosion-related warning signals, such as smoke, abnormal heat, acoustic events or pressure changes, where suitable sensors are installed and validated. The robot is an awareness and reporting system; it is not a firefighting robot, does not handle explosive materials and does not cause or trigger explosions.
3. **Explore:** build and update maps, navigate around people and obstacles, inspect assigned areas and return to a charging dock when conditions permit.
4. **Travel and camping:** accompany its owner on trips and monitor an approved campsite while the owner rests, reporting possible movement, wildlife, smoke or environmental changes for human review. This is awareness support, not wildlife deterrence or guaranteed protection.

### Home, travel and camping operating profiles (PROPOSED)

- **Home mode:** indoor patrol, building-condition awareness, possible wildlife alerts and return to a home dock.
- **Travel mode:** owner-supervised outdoor movement in a defined operating area, with GPS outdoors and local navigation where GPS is unavailable or unsuitable.
- **Camping night mode:** quiet monitoring with reduced lighting and non-essential sound; alert the owner when a potentially relevant event is detected.
- **Outdoor hardware goals:** weather-resistant enclosure; all-terrain wheels; low-light camera and suitable thermal sensor; 360° obstacle detection; portable charging; offline-first local operation.
- **Safe return / safe stop:** return to its owner only when localization, route safety and battery reserve are sufficient. If safe return cannot be established, stop safely and alert the owner when communication is available.
- **Operating limits:** define and test limits for rain, dust, temperature, slopes, loose ground, water exposure, darkness, battery endurance and connectivity. Do not send the robot roaming into unknown wilderness without supervision.

### Robot safety and protective engineering

Safety is a design requirement, not a capability that can be claimed without testing.

- **Do not become an ignition source:** prioritize battery safety, thermal-runaway mitigation, electrical isolation, overcurrent protection, protected wiring and suitable component selection.
- **Fire resistance:** select enclosure and insulation materials for defined temperature and flame-exposure requirements, then verify them through appropriate independent testing. “Fire-resistant” does not mean fireproof.
- **Explosion protection:** distinguish preventing the robot from igniting a hazardous atmosphere from surviving an external blast. These are different engineering problems. Operation in a classified explosive atmosphere requires a design assessed and certified for the specific zone, gas/dust group and temperature class. No general blast-survival or explosion-proof claim is made.
- **Emergency behaviour:** on a suspected hazard, warn the responsible people, preserve available evidence and stop or retreat only when the route and robot state are assessed as safe. Never send the robot into a dangerous area merely to investigate.
- **Human safety first:** certified building alarms, emergency procedures and qualified responders remain authoritative. The robot must not delay evacuation or emergency response.

The HOMEGUARD AI NOMAD robot, its 8 kg / 50 cm design targets, outdoor mode and wildlife-awareness functions are **future proposals only**. They have not been built, integrated, certified or validated. Sensor performance, navigation, weather resistance, animal detection, battery protection, fire performance and any explosion-protection rating require separate requirements, engineering reviews and test evidence before deployment.

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