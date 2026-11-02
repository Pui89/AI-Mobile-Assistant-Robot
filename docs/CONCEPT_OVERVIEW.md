# HOMEGUARD AI — Platform and NOMAD Product Overview

HOMEGUARD AI is the evidence-driven software platform for organizing building and environmental observations, checking evidence quality, comparing readings with documented baselines and helping a responsible person decide what should be verified.

**HOMEGUARD AI NOMAD** is the proposed portable mobile-robot product that may extend this platform into owner-supervised home, travel and camping environments.

![HOMEGUARD AI software platform concept overview](images/homeguard-ai-overview.svg)

## NOMAD physical concept

![HOMEGUARD AI NOMAD compact portable robot concept](images/homeguard-ai-nomad-concept.svg)

The current physical design targets are approximately 8 kg total mass and no more than 50 cm overall height, with a 30–35 cm body height, 30–35 cm width and 40–45 cm length. These are preliminary design targets, not measured or verified specifications.

## How the platform works

1. **Sense:** structural, electrical, water, air/gas, acoustic, light and thermal sources provide different observations.
2. **Locate:** every usable observation should be connected to its building, floor, room, component and sensor.
3. **Check evidence:** check timestamps, freshness, calibration, sensor health, units, missing values, conflicts and uncertainty before relying on a reading.
4. **Understand:** maintain a world-state view of what is known, unknown, changed, conflicting or in need of review.
5. **Support people:** create an evidence report and a proposed verification priority for a responsible human.

## NOMAD operating profiles — PROPOSED

- **Home:** supervised indoor patrol, building-condition awareness, cautious wildlife alerts and return to the home dock.
- **Travel:** accompany the owner within a defined outdoor operating area using GPS where available, local navigation and obstacle detection.
- **Camping:** quiet campsite monitoring during rest, with reduced lighting and non-essential sound and owner alerts for potentially relevant events.

Shared outdoor design goals include a weather-resistant enclosure, four all-terrain wheels, low-light camera, suitable thermal sensor, 360-degree obstacle detection, portable charging and offline-first local operation. Return to the owner is allowed only when localization, route safety and battery reserve are sufficient; otherwise the robot should enter a safe-stop state.

## What the first software version actually does

The current repository contains a deterministic software foundation, typed observations and baselines, evidence quality/freshness checks, a synthetic three-floor scenario, JSON findings and automated tests. The illustrations describe intended product architecture; they do not mean every sensor channel, AI capability or robot function is implemented.

## What it does not do

- It does not currently connect to real building sensors or robot hardware.
- It does not diagnose a building, certify structural safety or guarantee hazard or wildlife detection.
- It does not replace certified fire, smoke, carbon-monoxide or electrical protection.
- It does not control breakers, valves, lifts, doors, alarms or evacuation systems.
- It does not infer a confirmed cause from one sensor or an uncertain pattern.
- It does not promise protection from wild animals, snakes, fire, explosions or other emergencies.

**Current evidence status: FOUNDATION / SIMULATION-ONLY.** Any real-building or physical-robot pilot requires suitable sensors, qualified engineering, safety and privacy review, controlled testing and independent validation.
