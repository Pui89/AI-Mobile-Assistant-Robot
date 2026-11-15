# PUI89 AI NOMAD — Spatial Intelligence Profile

## Intended use
Local spatial context for luggage awareness and future supervised low-speed movement in approved areas. Travel Mode remains manual; Flight Mode disables powered movement.

## Planned tasks
- Camera image-quality checks and scene context.
- Object/obstacle geometry and free-space cues.
- Calibrated depth or stereo range where selected sensors support it.
- Wheel odometry and IMU state.
- Indoor/outdoor context and localisation confidence where lawful and available.
- Luggage separation/tamper events only with reviewed sensors and privacy controls.
- Evidence references, uncertainty and human review.

## Safety boundaries
- Spatial estimates do not authorise movement.
- No movement in aircraft, restricted airport areas or unapproved public environments.
- No localisation integrity, obstacle avoidance, braking, travel safety or mobility is validated.
- Monocular depth is not metric range.
- No facial recognition or biometric tracking.
- Missing, stale, uncalibrated or conflicting observations remain UNKNOWN/CONFLICT.

This profile documents proposed integration only. No runtime sensor driver, real sensor integration or physical mobility is claimed.
