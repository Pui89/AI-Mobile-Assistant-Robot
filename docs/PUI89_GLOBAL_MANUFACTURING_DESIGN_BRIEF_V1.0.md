# PUI89 AI NOMAD — Global Manufacturing Design Brief v1.0

**Document status:** Preliminary engineering design brief — requirements and candidate trade studies only  
**Revision date:** 22 November 2026  
**Manufacturing intent:** Transferable design for qualified manufacturing partners in multiple countries  
**Important:** This is not a released production specification, approved BOM, CAD drawing set, certification or proof of tested performance.

## 1. Product identity and scope

Suitcase-form intelligent mobile assistant with upright luggage-inspired enclosure, telescopic pull handle and four luggage-style spinner casters.

**Current evidence status:** Concept and early software foundations; no completed physical product, integrated sensor suite, validated rolling performance, weather protection or airline acceptance is established.

## 2. Product envelope and dimensions

Existing preliminary total-mass target 8–10 kg, with 10 kg maximum design ceiling. External dimensions, wheelbase, wheel size, handle height/range, payload, centre of gravity and rolling resistance remain TBD. No cabin-baggage compliance claim.

All released drawings shall use SI units (mm, kg, N, N·m, °C) and identify datums, tolerances, revision, material, finish, drawing scale and inspection method. Dimension values must be derived from approved requirements, CAD, human-factors data, structural analysis and verification—not copied from concept images.

## 3. Candidate materials — not an approved material list

Candidate study only: PC/ABS or impact-modified polycarbonate shell; aluminium alloy telescopic handle tubes; reinforced polymer or aluminium wheel carriers; replaceable PU/TPE caster treads; stainless fasteners; EPDM seals and abrasion-resistant textile/trim where required. Exact grade and wall thickness require impact, creep, UV, abrasion and chemical testing.

For every final material, the controlled manufacturing package must specify the exact standard and grade, temper/heat treatment where applicable, thickness/section, coating/finish, supplier traceability, certificate requirements, joining process and acceptance criteria. Candidate families above are for engineering trade studies only. No material grade is released for procurement.

## 4. Component architecture — no parts selected

Suitcase shell/frame; telescopic handle and locking mechanism; four spinner casters; wheel bearings; optional powered wheel/drive module only if approved by the product architecture; compute and sensors; battery+BMS; charging interface; physical power/stop controls; display/audio/haptic indicators if justified; cable harness and service panels. Propulsion architecture and all electronics remain TBD.

For each selected component, the BOM must include: PUI89 part number; description; function; quantity; approved manufacturer and exact model; revision; critical ratings; interface/connector; operating and storage limits; country of manufacture; origin evidence; licence/provenance where relevant; approved alternatives; lifecycle status; inspection criteria; and verification record. Do not substitute a component based on name or appearance alone.

## 5. Global human factors and usability

Must remain easy to lift, pull, roll, store and service. Handle ergonomics for diverse user heights, curb/threshold handling, tip resistance, caster durability, luggage impact, pinch protection and airline-size rules by carrier. Essential handling and stop functions must work without app/cloud.

Use representative anthropometric datasets for intended markets and validate with users of different body sizes, ages, abilities, clothing and protective equipment. Provide clear physical controls, readable alerts, accessible service points and local-language/operator documentation where needed. Do not claim universal fit; document the tested user population and limitations.

### 5.1 Discreet public-space form and behaviour

- The canonical exterior is an upright, premium suitcase-style enclosure—not a low rover, dog-inspired body, quadruped or humanoid bodyguard form.
- Use four integrated luggage-style wheels and a retractable telescopic handle; detailed caster geometry, drive architecture and handle dimensions remain subject to engineering review.
- Deep Navy is the primary exterior direction, with restrained Electric Cyan accents. Avoid excessive glow, conspicuous light bars, exposed mechanical limbs, face-like displays or aggressive security styling.
- Integrate cameras and sensors into the enclosure with a clean luggage-like appearance while preserving required fields of view, serviceability and safety visibility.
- Target smooth, quiet, predictable movement and unobtrusive owner accompaniment. These are human-factors objectives requiring acoustic, motion, stability and user studies; they are not current performance claims.
- Public-space discretion must not conceal safety-critical status, bypass venue/security rules or mislead the owner or bystanders where disclosure is required.
- Evaluate luggage-like handling, wheel noise, turning behaviour, approach distance, stopping behaviour, visual salience and perceived comfort in representative user studies before making usability claims.

## 6. Extreme-environment design strategy

PUI89's programme-level study envelope is -50°C to +60°C. This is a design objective, not a blanket operating rating. Each subsystem must have separate operating, storage, transport, charging and survival limits.

Required design reviews:
- Cold start, cold soak, low-temperature seals, lubricants, cables, displays and connector behaviour.
- High-temperature heat soak, solar loading, electronics/actuator derating and thermal runaway prevention.
- Thermal cycling, condensation, humidity and freeze/thaw.
- Dust/sand ingress, abrasion and filter/service intervals.
- Rain/water exposure, drainage, pressure equalisation and corrosion.
- Salt/corrosion exposure where the mission warrants it.
- Vibration, shock, drop and transport loads appropriate to the product.
- Battery-specific charge/discharge limits, preconditioning/heating/cooling and safe shutdown.

Select IP ratings and environmental test severities per product risk and use case. An IP rating does not prove resistance to immersion, salt, chemicals, pressure washing or extreme temperature unless those conditions are separately covered.

## 7. Design for manufacturing, assembly and service

- Prefer common metric fasteners and documented torque/locking methods.
- Use datum-based drawings, GD&T where needed, and inspectable tolerances.
- Design modular subassemblies with replaceable wear parts and accessible connectors.
- Avoid single-source/custom components unless justified and approved.
- Define process capability, special processes, operator qualification and inspection points.
- Provide assembly sequence, fixtures, calibration, firmware loading and end-of-line tests.
- Provide repair instructions, diagnostic access, spare-parts list and safe battery/service procedures.
- Validate interchangeable parts and alternate suppliers before release; form/fit alone is insufficient.

## 8. Global manufacturing transfer package

A qualified manufacturing site must receive the controlled, revision-matched package:
1. Approved 3D CAD and neutral STEP export.
2. Dimensioned 2D PDF and DXF drawings.
3. Released BOM and approved-source/alternative register.
4. Exact material and process specifications.
5. Assembly work instructions and special-tool/fixture list.
6. Wiring diagrams, connector pinouts and software/firmware release identifiers.
7. Inspection plan, gauges, calibration and acceptance criteria.
8. End-of-line functional and safety test procedures.
9. Packaging, transport and storage requirements.
10. Maintenance, repair and spare-parts documentation.
11. Non-conformance, deviation and engineering-change process.
12. First-article inspection and manufacturing-site qualification records.

A second-country factory must complete first-article inspection and process validation before production approval. A transferred drawing set alone does not establish manufacturing equivalence.

## 9. Quality, safety and compliance

Create a product-specific compliance matrix for each destination country and exact product classification. Identify applicable legislation, standards, test laboratories, certification/approval route, importer/manufacturer obligations, language/label requirements and change-control duties. EU, US and Japan requirements are not interchangeable.

Quality records must be traceable by part, lot, serial number, software version, calibration status, inspection result and release approval. Do not publish or mark CE/FCC/PSE/UL/ISO/NASA compliance unless the relevant scope and evidence support the exact claim.

## 10. Required engineering release gates

| Gate | Required evidence |
|---|---|
| G1 Requirements | Approved users, mission, operating envelope, measurable requirements |
| G2 Preliminary design | Architecture, packaging, anthropometry, material/component trade studies |
| G3 Detailed design | Released CAD/drawings, calculations, interfaces, draft BOM and risk controls |
| G4 Prototype | Build record, configuration baseline, inspection and bench tests |
| G5 Verification | Requirements-linked test procedures, measured results and resolved failures |
| G6 Manufacturing validation | First-article inspection, process capability, supplier/site qualification |
| G7 Market release | Applicable conformity assessment, technical file, labels, manuals and release approval |

## 11. Open decisions register

Every unresolved dimension, tolerance, material grade, component model, supplier, power rating, battery limit, environmental rating, payload, performance value and acceptance threshold must remain **TBD / OPEN** with an owner and closure evidence. Do not fill gaps with invented values.

## 12. Evidence and configuration rules

Use four distinct labels: **Proposed**, **Specified**, **Tested**, and **Verified**. A design target is not a measured result. A simulation is not physical validation. A component datasheet is not system qualification. Preserve test failures and engineering evidence in controlled internal records; publish only approved summaries.

**PUI89 objective:** a competent engineer in another country can understand the product, identify every open decision, reproduce the approved configuration, build it using qualified processes, inspect it against explicit criteria and maintain it without relying on undocumented founder knowledge.


## Mandatory manufacturing handoff control

This brief must be used together with the [PUI89 Global Manufacturing Handoff System v1.0](PUI89_GLOBAL_MANUFACTURING_HANDOFF_SYSTEM_V1.0.md). That system defines the mandatory part/BOM fields, material and process definitions, interface controls, work instructions, inspection and acceptance records, stop-work/TQ/NCR rules, substitution approval, traceability, factory qualification and release authority. If a required value or acceptance criterion is missing, mark it **TBD / NOT RELEASED**; do not guess or procure/build against an assumption.
