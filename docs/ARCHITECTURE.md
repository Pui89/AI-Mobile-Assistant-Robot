# Architecture

HOMEGUARD's differentiator is traceable multi-modal evidence, explicit uncertainty, spatial context, safe escalation and reproducible verification.

## Domains
Structural health; electrical condition and safety indicators; fire/life-safety status visibility; water and moisture; environmental and air quality; acoustic, light, thermal and multi-sensor intelligence.

## Layers
1. Vendor-neutral acquisition adapters (no hardware assumed initially).
2. Evidence contract: sensor, domain, metric, units, timestamp, location, quality, calibration and uncertainty.
3. Quality gate: missing/stale data, invalid values, unit mismatch, clock problems and calibration status.
4. Baseline/change engine with documented baseline periods.
5. Spatial world model connecting buildings, floors, rooms, components, sensors and events.
6. Explanation layer distinguishing observation, inference and unknowns.
7. JSON reporting; dashboard and APIs later.
8. Verification loop: synthetic tests, fault injection, regression corpus and reviewed releases.

Start with deterministic rules, signal-quality checks, baseline statistics and transparent feature extraction. Deep learning is not required for the first demonstrator.

Deployment stages: synthetic simulation → offline evaluation → bench-tested calibrated sensors → supervised building pilot → independent validation.


## Physical camera privacy boundary

Camera privacy is a physical, owner-controlled boundary, not an AI feature. NOMAD requires a manual-only opaque sliding lens cover, mechanically visible OPEN/CLOSED state and a hardware capture inhibit when closed. No powered actuator or software, network, voice or AI command may move the cover. Uncertain state disables capture. Product-specific mechanical and environmental requirements are defined in [Manual Physical Privacy Shutter Requirements](MANUAL_PHYSICAL_PRIVACY_SHUTTER_REQUIREMENTS.md). This is a proposed requirement; no hardware implementation is claimed.
