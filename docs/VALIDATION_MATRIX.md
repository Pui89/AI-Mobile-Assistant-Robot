# PUI89 AI NOMAD — Validation Matrix

**Baseline:** Stage 1 product definition. All physical performance and airline acceptance remain unvalidated.

| ID | Requirement | Verification method | Evidence needed | Status |
|---|---|---|---|---|
| NOM-01 | Suitcase form and package envelope | CAD review and dimensional measurement | External dimensions including all protrusions | Target only |
| NOM-02 | Complete mass | Part-level mass ledger and calibrated weighing | BOM mass, measured prototype mass | Not measured |
| NOM-03 | Four-wheel manual luggage handling | Pull/roll, handle fatigue and load tests | Pull force, wheel durability, stability | Not tested |
| NOM-04 | Storage and load retention | Compartment and impact tests | Usable volume, retention and load limits | TBD |
| NOM-05 | Removable battery | Removal/reinstall and terminal protection tests | Wh marking, removal time, BMS and isolation evidence | Not selected |
| NOM-06 | Flight mode | Mode-interlock and fault-injection tests | Powered-off state, no unexpected drive activation | Requirements only |
| NOM-07 | Camera and perception | Annotated lawful dataset; varied lighting/occlusion | Precision/recall, class metrics, dataset provenance | Not measured |
| NOM-08 | Spatial awareness | Calibrated depth targets | Range/error distribution and calibration | No sensor selected |
| NOM-09 | Travel dashboard | Software and usability tests | Correct status, event and uncertainty records | Not validated |
| NOM-10 | Battery/thermal health | Bench test using selected protected battery system | Temperature/current logs and fault behaviour | No hardware |
| NOM-11 | Future powered movement | Closed-area supervised test after safety review | Speed, stopping distance, turning, obstacle and failure tests | Not implemented |
| NOM-12 | Airline baggage acceptance | Carrier review for named route/cabin/aircraft | Written carrier confirmation and measured package | Not checked |
| NOM-13 | Privacy | Data-flow and retention review | Local processing, visible indicators, retention/access policy | Requirements only |
| NOM-14 | Reliability/serviceability | Repeated travel and service-cycle tests | Failure rates, repair time, replacement parts | Not measured |

## Evidence classes

- Software tests: contracts, parsing, policy, UI and deterministic logic.
- Simulation: model, version, scenario, seed and logs.
- Bench: actual selected components, calibration and electrical measurements.
- Physical prototype: controlled handling, mobility, battery and safety tests.
- Airline: carrier-specific written confirmation and actual measured configuration.

Passing software or simulation tests does not prove physical performance or airline acceptance. Never publish metrics without test conditions, sample size, ground truth and limitations.
