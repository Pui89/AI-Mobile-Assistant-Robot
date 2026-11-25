# PUI89 AI NOMAD — 360° Intelligence Profile v1.0

**Status:** Proposed product-specific requirements; no physical prototype or integrated 360° sensor suite is established.

## Mission
Give the user a clear, local understanding of the immediate surroundings of the compact dog-inspired four-wheel assistant. The integrated handle and user-directed handling remain part of the product identity.

## Candidate workflow
1. Define supervised indoor and suitable outdoor operating zones.
2. Map candidate sensor fields of view around the body, handle, wheels and carried loads.
3. Detect relevant obstacles, people and environmental context; preserve object tracks only when continuity is verified.
4. Estimate local free/occupied/unknown space only when calibrated depth or range evidence exists.
5. Provide concise status and route-context advice; stop or request human input when coverage or localisation is uncertain.

## Candidate AI and sensing
RGB/depth object detection, segmentation, short-horizon tracking, optional visual-inertial/SLAM and sensor fusion. Select modalities only after mission, mass, power, weather exposure, privacy and compute budgets are defined.

## 360° requirements
- Define horizontal/elevation coverage at all expected body and handle configurations.
- Include wheel-level near-field blind zones, self-occlusion, user legs, handle, payload and environmental occlusion.
- Distinguish "not observed" from "clear"; loss of a sensor or localisation confidence must trigger a conservative degraded mode.
- No automatic follow-me, obstacle-avoidance or public-space autonomy claim follows from this document.
- Keep local operation and essential physical controls independent of app, internet and cloud connectivity.

## Safety and exclusions
NOMAD remains user-directed and supervised. AI outputs are advisory; no autonomous motion or unsafe manoeuvre is authorised by perception alone. Do not infer all-terrain, weatherproofing, payload or battery endurance.

## Evidence gates
User journey/operating envelope → sensor coverage and privacy review → synthetic obstacle and occlusion tests → bench calibration → controlled supervised mobility tests → independent validation.

Measure sector coverage, near-field blind zones, obstacle recall by size/range, false alerts, localisation drift, latency, RAM, energy and safe degradation only on a defined physical configuration.

**Shared architecture:** [PUI89 360° Intelligence Architecture v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/PUI89_360_DEGREE_INTELLIGENCE_V1.0.md)
