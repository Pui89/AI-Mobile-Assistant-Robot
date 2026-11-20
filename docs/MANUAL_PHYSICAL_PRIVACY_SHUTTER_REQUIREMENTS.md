# PUI89 AI NOMAD — Manual Physical Camera Privacy Shutter Requirements v1.0

**Status:** PROPOSED / NOT IMPLEMENTED / NOT VERIFIED.  
**Scope:** Camera privacy for the PUI89 AI NOMAD mobile assistant.  
**Design principle:** The owner controls the physical camera aperture directly. Software may report state and enforce capture permissions, but it must never move or open the shutter.

## 1. Selected design

Use a **manual-only sliding opaque lens cover** mounted directly over each camera aperture. The owner or authorised person must move the cover by hand at the robot body.

- No motor, servo, solenoid, powered latch or other actuator may move the cover.
- No app, network, voice command, AI model or agent may open or close it.
- Use tactile OPEN/CLOSED end positions or detents and a high-contrast mechanical marker physically linked to the cover.
- The cover must be captive or otherwise retained so it cannot detach during normal supervised travel.
- The cover must fully block the relevant optical path when closed.
- Opening the cover by hand does not itself grant permission to capture; separate software permission and local operating policy still apply.
- If NOMAD has more than one camera or optical sensor, every aperture must have its own physical cover or be independently hardware-disabled in privacy mode. A single covered lens must never imply that all cameras are private.

## 2. NOMAD-specific mechanical requirements

Because NOMAD is a mobile product, the mechanism must be assessed for:
- Vibration and shock during rolling, handling, lifting and transport.
- Accidental contact with luggage, clothing, hands or stored objects.
- Slider retention, tactile detent strength, wear, contamination and jamming.
- Recessed or guarded slider geometry to reduce unintended movement.
- Dust, splash, cleaning fluids, humidity and condensation exposure.
- Seal geometry around the optical aperture without obstructing the field of view when open.
- Serviceability without exposing wiring or allowing the shutter to be bypassed accidentally.

Materials, dimensions, actuation force, cycle life, sealing design and environmental limits remain TBD until engineering selection and testing. Do not claim waterproofing, dustproofing, an IP rating or tamper-proof operation without evidence.

## 3. Electrical and software boundary

When the cover reaches the fully CLOSED position, a mechanically linked hardware interlock must disable camera power or the camera capture-enable path independently of the application. Software must not be able to override that inhibit.

A position sensor may report OPEN, CLOSED or UNKNOWN. It is supplementary to the visible mechanical marker and direct physical inspection; it does not replace them. Sensor disagreement, broken wiring, startup uncertainty, partial closure or a jam must report **UNKNOWN / CAMERA DISABLED** and keep capture inhibited.

No software-controlled mechanism may move the shutter. Remote, voice, agent and model requests to move it must be rejected. The physical shutter must not be presented as a microphone mute; audio capture requires its own independent physical control and state.

## 4. Required operating states

| State | Physical condition | Camera capture | User-facing status |
|---|---|---|---|
| PRIVACY_CLOSED | Opaque cover fully closed; mechanical marker indicates CLOSED; interlock valid | Hardware-inhibited | CAMERA PHYSICALLY COVERED |
| COVER_OPEN | Owner has manually opened the cover | Still disabled until separate permission is granted | CAMERA COVER OPEN — CAPTURE NOT YET AUTHORISED |
| CAMERA_AUTHORISED | Cover manually open and separate capture permission granted | May operate within approved local policy | CAMERA OPEN — CAPTURE AUTHORISED |
| UNKNOWN / FAULT | Partial closure, jam, sensor fault, mismatch or uncertain state | Disabled (fail-closed) | CAMERA STATE UNKNOWN — CAMERA DISABLED |
| STARTUP | State not yet verified | Disabled | VERIFYING PRIVACY SHUTTER |

Never infer physical closure solely from an app toggle, a stopped process, a dark LED or an unverified sensor value.

## 5. Privacy-first data handling

- Default to no persistent camera image or video recording.
- Any visual analysis must be explicitly enabled, local-first and transient in volatile memory where feasible.
- Do not persist routine frames in files, thumbnails, caches, logs, crash reports, telemetry, backups or cloud storage.
- Any future evidence-capture feature requires separate explicit owner opt-in, clear indication, narrow purpose, bounded retention and deletion controls.
- Text event logs are also personal data and require access, retention and deletion controls.
- Camera and microphone controls and status must remain distinct.

## 6. Threats and verification

Test at minimum:
1. Manual opening/closing and unambiguous marker operation.
2. Repeated-cycle wear, loose slider, detent failure and cover retention under representative vibration.
3. Partial closure, obstruction, jam, detached cover and contamination.
4. Position sensor stuck, disconnected, shorted or contradictory.
5. Hardware camera inhibit under closed, startup, reboot, brownout and power-restoration conditions.
6. Attempts by app, network, voice, AI agent or model to move the shutter or bypass capture inhibit.
7. Every camera and auxiliary optical aperture, including depth or secondary cameras.
8. Unintended frame persistence in caches, logs, crash reports, telemetry and backups.
9. Environmental exposure tests for the exact enclosure and sealing design.
10. Separate microphone behavior and status.

## 7. Release gates and non-claims

Progress through requirements review → mechanical/electrical design review → bench prototype → fault injection and repeated-cycle testing → data-flow verification → supervised NOMAD mobility trial → evidence review.

This document is a requirements baseline only. No shutter, interlock, sensor, camera integration, enclosure seal, prototype or test is claimed to exist. No component, supplier, CAD design, purchase or environmental rating is approved. Do not publish claims of guaranteed privacy, tamper-proof operation, waterproofing, dustproofing or certification without corresponding evidence.

## 8. PUI89 cross-product consistency

This NOMAD implementation follows the same manual-only privacy principle documented for [PUI89 AI HOME — PR #83](https://github.com/Pui89/AI-Home-Safety-Robot/pull/83): physical human control, no powered shutter actuation, no AI/app/network opening, visible mechanical state and hardware capture inhibit. Mechanical packaging and environmental validation remain product-specific.
