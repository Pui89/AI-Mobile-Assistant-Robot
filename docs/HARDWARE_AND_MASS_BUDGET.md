# PUI89 AI NOMAD — Hardware, Packaging & Mass Budget

**Status:** candidate subsystem requirements only. No part numbers, suppliers, country-of-origin evidence, prices or purchases are confirmed.

## Mechanical package

| Subsystem | Function | Design questions / evidence |
|---|---|---|
| Hard-shell enclosure | Protect luggage and electronics | Shell material, impact, scratch, corner, service and repair tests |
| Four wheels | Manual luggage rolling; possible future powered mode | Diameter, bearings, tread, noise, load rating, wheel guards, swivel/drive arrangement |
| Telescopic pull handle | Manual pull and steering | Handle lock, extension, fatigue, grip ergonomics, side-load and pull-force tests |
| Carry grip | Lift by one person | Grip position, structural load, balance and drop/impact testing |
| Storage cavity | Hold travel belongings | Usable litres, divider, restraint, access, privacy and load distribution |
| Battery bay | Removable battery | Wh, chemistry, BMS, connector, isolation, terminal cover, retention and thermal tests |
| Compute bay | Local AI processing | CPU/RAM, thermal, serviceability, power and vibration |
| Sensor windows | RGB/depth sensing | Field of view, protection, cleaning, calibration and privacy indicator |
| Base structure | Carry and wheel loads | Centre of gravity, wheel load, tipping, handle load and impact analysis |

## Preliminary mass budget

| Assembly | Planning allowance |
|---|---:|
| Shell, frame, internal storage and corner protection | 2.0 kg |
| Four wheels, wheel modules and possible drive allowance | 2.0 kg |
| Removable battery and protection | 1.5 kg |
| Compute and control electronics | 0.8 kg |
| Cameras and other sensors | 0.6 kg |
| Telescopic handle, carry grip, wiring and safety hardware | 1.0 kg |
| Fasteners, guards, connectors and engineering reserve | 2.1 kg |
| **Total planning ceiling** | **10.0 kg target budget** |

This is an initial allocation, not a supplier-based bill of materials or measured component inventory. The absolute product design ceiling is 12 kg complete, but the target is to close the design at 8–10 kg. Any mass above the 10 kg planning budget requires an explicit trade-off review; do not treat the 12 kg ceiling as a target.

## Candidate electronics and sensing

- CPU-first local compute; optional accelerator only after measured resource and power need.
- RGB camera; optional depth/stereo camera only after calibration and power review.
- IMU and wheel encoders for movement-state observation if Robot Mode is developed.
- Battery voltage/current/temperature telemetry from a properly protected BMS.
- Motor current/temperature and wheel-jam sensors only if powered wheels are selected.
- Optional GNSS for outdoor context; no assumption of indoor positioning accuracy.
- Microphone/speaker and wireless radios are optional and require privacy, security and airline review.

## Sourcing gates

For every candidate record exact manufacturer, brand, model/part number, country of manufacture and origin evidence, datasheet, interface, dimensions, mass, voltage/current, operating temperature, licence/firmware terms, supplier, Thailand/international availability, dated price, lead time, warranty, shipping and compatibility.

Prefer verifiable non-Chinese-origin options where suitable. Unknown origin, unclear licence, incompatible interfaces or unverified prices remain UNVERIFIED — DO NOT USE. No procurement is authorised by this document.
