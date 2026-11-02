# HOMEGUARD AI — Software Architecture

HOMEGUARD AI is the evidence-driven software platform. HOMEGUARD AI NOMAD is a proposed physical product that may consume platform reports and provide additional mobile observations after hardware integration is separately designed and validated.

The platform's differentiator is traceable multi-modal evidence, explicit uncertainty, spatial context, safe escalation and reproducible verification. The current architecture does not implement robot navigation, motor control or hardware actuation.

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
