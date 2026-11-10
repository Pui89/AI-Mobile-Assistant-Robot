# AI NOMAD: Spatial Intelligence integration profile

## Intended use
Advisory indoor/outdoor obstacle geometry and spatial context.

## Planned tasks
- Obstacle-relative geometry and room/area context
- Coordinate-frame and timestamp consistency checks
- Evidence records for future mobility evaluation

## Safety boundaries
- No localization integrity, weather resistance or mobility safety is validated.
- No autonomous movement or physical control is enabled.
- Outdoor GNSS and environmental degradation require separate testing.

The common interfaces are under development in [Shared AI Core PR #26](https://github.com/Pui89/PUI89-Shared-AI-Core/pull/26), which remains draft and unmerged. This profile documents the intended integration contract only; no runtime import, sensor driver or physical integration is claimed.

Require lawful data provenance, calibration, synchronized timestamps, sensor-health checks, uncertainty handling, synthetic fault tests and human review before runtime use. No physical actuation is enabled.

**Status:** profile documentation added; runtime adapter, real sensor integration, accuracy and field validation pending. No paid services or hardware purchase required.
