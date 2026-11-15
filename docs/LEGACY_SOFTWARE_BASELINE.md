# Legacy Software Baseline — Scope and Reuse Boundary

**Purpose:** make the repository's earlier software lineage explicit during the transition to the suitcase-form PUI89 AI NOMAD product.

## Current product scope

PUI89 AI NOMAD is an AI travel suitcase: upright hard-shell luggage form, four protected wheels, retractable manual pull handle, internal storage and removable battery. Its primary operating mode is manual luggage handling. Flight Mode powers the system off. Any future powered Robot Mode is supervised and restricted to permitted controlled areas outside aircraft and restricted airport zones.

## Existing software lineage

The repository contains a small, dependency-light evidence evaluator and synthetic building-condition simulation under the historical Python namespace homeguard_ai. These files were created for an earlier Homeguard/building-monitoring direction. They provide generic examples of timestamp validation, evidence quality checks, baseline comparison and structured findings.

They are **not** the active AI NOMAD travel, luggage, vision, spatial, battery, airline-compliance or mobile-robot software stack. They do not implement:
- suitcase or luggage management;
- camera acquisition or object detection;
- travel itinerary or airline rule checking;
- removable-battery management;
- wheel odometry, motor control or navigation;
- Flight/Travel/Robot mode interlocks;
- obstacle avoidance, following or autonomous mobility.

## Migration policy

1. Preserve the existing module and Git history; do not silently delete or rename it.
2. Treat its output as a legacy synthetic evidence-evaluation demonstration only.
3. Do not describe its test results as NOMAD travel or robotics validation.
4. Reuse generic timestamp, provenance or uncertainty helpers only after product-specific review and tests.
5. New NOMAD features should be implemented in clearly named product modules with tests and documented evidence.
6. The homeguard_ai import namespace is retained temporarily for compatibility; it does not define the product's public identity.
7. Update or replace the old building-monitoring simulator only through a separate reviewed migration plan.

## Acceptance rule

A software component becomes part of the active NOMAD baseline only when its purpose is mapped to the current Product Definition, it has a defined interface, tests, privacy/safety review and traceable evidence. No physical device or AI capability is implied by this document.
