# PUI89 AI NOMAD — Intelligence Catalogue

**Status: proposed capability catalogue. Listing a function does not mean it is implemented, integrated, airline-approved or validated.**

## 1. Luggage and travel intelligence
- Trip checklist, packing/reminder workflow and journey timeline.
- Luggage/device status, mode, battery and thermal state.
- Optional local location context and owner-initiated lost-item assistance.
- Tamper/opening or separation events only with appropriate sensors and privacy review.
- Airline-rule checklist prompts; the app must not present generic rules as a guarantee of acceptance.

## 2. Vision and scene intelligence
- Image quality and camera-health checks.
- Object detection and classification for luggage, people, carts, doors and visible obstacles.
- Short-lived object tracking for scene understanding; no identity inference.
- Segmentation and scene understanding where models and compute are validated.
- Change/anomaly cues with evidence and uncertainty.

## 3. Spatial and mobility intelligence
- Calibrated depth or stereo geometry where supported by selected sensors.
- Free-space and obstacle-clearance estimates.
- Wheel odometry and IMU state fusion.
- Turning/clearance and route-context proposals.
- Mobility-state monitoring, wheel jam/slip cues and safe-stop proposals.
- Any path proposal is bounded by a separately validated operating envelope.

## 4. Device and battery intelligence
- Battery voltage/current/temperature/state-of-charge telemetry if available.
- BMS and protection-state observation; no bypass of battery protections.
- Wheel/motor temperature/current and encoder fault monitoring if integrated.
- Handle lock, enclosure access and mode-state monitoring if designed.
- Fault/event timeline and service diagnostics.

## 5. Human interaction intelligence
- Owner-controlled dashboard and clear status indicators.
- Optional local voice commands and travel assistance, subject to consent and privacy review.
- Explicit mode selection, manual override, stop and operator review.
- Accessibility and multilingual interface research.

## 6. Safety and trust intelligence
- Input freshness, provenance, quality and uncertainty.
- Travel/Robot/Flight mode interlocks.
- Geofence/area restriction proposals and independent enforcement.
- Fail-safe stop on sensor, communication, localisation, battery or controller faults.
- Human-reviewed event and evidence reports.

## Implementation order

Start with luggage form, manual pull function, local dashboard, battery/device status and offline scene awareness. Defer powered movement and following until a complete independent safety case and physical validation exist.
