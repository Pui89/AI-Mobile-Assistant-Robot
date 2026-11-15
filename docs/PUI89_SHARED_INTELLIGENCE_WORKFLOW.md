# PUI89 Shared Intelligence Workflow — AI NOMAD Profile

The common evidence-first workflow applies to NOMAD's travel-suitcase and future supervised mobile-assistant functions. It does not imply all listed capabilities are implemented.

## Workflow
1. Observe: accept only authorised local sensor and device inputs.
2. Validate: check source, timestamp, quality, calibration, freshness and mode.
3. Perceive: image quality, object/obstacle detection, classification, tracking and scene understanding.
4. Understand: maintain luggage, travel, environment and device WorldState.
5. Assess uncertainty: preserve missing, stale, conflicting and out-of-distribution inputs.
6. Assess risk: evaluate travel mode, battery state, area permission, obstacle and mobility constraints.
7. Propose: reminders, status notifications, evidence capture or bounded mobility proposals.
8. Safety gate: Travel/Flight mode disables drive; Robot Mode requires independent safety controls and human authorisation.
9. Verify: record reproducible software, simulation, bench and physical tests separately.
10. Report: preserve source, model/configuration, uncertainty, decision, operator review and limitations.

## Project-specific interpretation
- Travel Mode: luggage status, trip checklist, battery state and local travel assistance; manual pull only.
- Flight Mode: power off; removable battery and airline compliance requirements followed; no powered mobility.
- Robot Mode: future supervised movement in permitted controlled areas, outside aircraft and restricted areas.
- Shared AI Core: Observation, WorldState, ActionProposal and FailureReport.

## Human review
Human review is required for consequential travel, baggage, privacy and any future physical-mobility decision. The owner and operating airline retain authority over carriage and travel acceptance.

## Boundaries
- No autonomous movement onboard an aircraft.
- No airport/public-space autonomous following without explicit authorisation and validated safeguards.
- No face recognition, biometric identification or covert surveillance.
- No direct actuator commands from AI models or language models.
- Software tests and simulation do not establish airline acceptance or physical safety.
