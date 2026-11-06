# PUI89 Advanced Technology Implementation Plan

**Project:** HOMEGUARD AI NOMAD  
**Scope:** all four PUI89 applications, coordinated through one shared AI Core contract  
**Priority:** core first  
**Cost policy:** strict zero-paid-services, local-first, no automatic downloads  
**Status:** implementation plan and evidence index; not a claim that every advanced capability is implemented.

## 1. Architecture decision

PUI89 already contains reusable intelligence foundations. Do not create a second world-state engine, observation evaluator, report generator or simulation framework inside Homeguard. Reuse the current implementation and make Homeguard a domain adapter to the shared PUI89 report contract.

The cross-project contract is `schemas/pui89-intelligence-report.schema.json`. It is byte-identical across all four repositories and covers all four project identifiers. Homeguard's existing `schemas/finding-report.schema.json` remains in place as a domain-specific extension.

## 2. Existing foundations to reuse

- `src/homeguard_ai/core.py` — observation and baseline records, evidence evaluation, stale/quality/calibration checks, limitations and findings.
- `src/homeguard_ai/simulator.py` — deterministic scenario simulation.
- `schemas/finding-report.schema.json` — Homeguard-specific finding report.
- `tests/test_core.py` — existing regression tests for evidence quality, baselines, timestamps and simulation output.

## 3. Domain adapter responsibilities

- Multi-sensor observation and evidence quality.
- Local mapping and supervised navigation.
- Hazard/event anomaly triage.
- Battery, connectivity and safe-return state estimation.
- Owner-approved task planning and human-reviewed alerts.

Translate Homeguard observations into the shared world-state, evidence, uncertainty, risk, recommendation, safety-gate and verification fields. Preserve timestamps, sensor identity, calibration, quality, uncertainty and limitations. Do not infer certified protection or real-world hazard detection from a simulated finding.

## 4. Core-first implementation sequence

1. **Contract convergence:** keep the same report schema in all four projects; validate JSON syntax and project identifiers.
2. **Core reuse:** extend the current observation evaluator only where a missing shared contract field requires it. Do not create another world-state or confidence engine.
3. **Adapter conformance:** map Homeguard findings into the shared report while preserving the existing finding-report schema.
4. **Evidence and uncertainty:** record provenance, timestamps, calibration state, stale data, limitations and conflicting inputs.
5. **Safety and human review:** fail closed on missing safety signals; require owner approval for consequential tasks; prohibit CI and report tooling from issuing hardware commands.
6. **Deterministic regression:** test normal, missing, stale, malformed, conflicting, fault and recovery cases with fixed scenarios.
7. **Simulation integration:** reuse the current simulator and its test suite before introducing a heavier robotics simulator.
8. **Optional advanced adapters:** evaluate local models, SLAM, navigation, predictive monitoring and supervised agents individually after licence and resource checks.

## 5. Technology adoption gates

Candidates include OpenCV, ONNX Runtime, PyTorch, ROS 2, Nav2, Gazebo and optional local vector retrieval. They are not mandatory dependencies and are not installed by this plan.

Before adoption, record exact version and licence, commercial-use and redistribution terms, local CPU/RAM/disk requirements, offline behaviour, provenance, acceptance metrics and safe fallback behaviour.

For ROS 2 simulation, the official compatibility pairing for ROS 2 Jazzy is Gazebo Harmonic. Use the existing project's supported environment rather than upgrading blindly. See https://gazebosim.org/docs/latest/ros_installation/ and https://gazebosim.org/docs/harmonic/install/.

## 6. Strict execution policy

- No paid APIs, subscriptions, cloud GPU or paid hosted databases.
- No automatic model or dataset downloads.
- No dependency installation in the lightweight registry audit.
- Prefer existing code and Python standard library where sufficient.
- Review model, dataset and package licences before use.
- No physical actuator commands from CI, tests, agents or report generation.
- Unknown or conflicting evidence must produce an explicit review/hold state.

## 7. Automated verification and evidence

Retain existing HOMEGUARD CI, shared-contract and security workflows. The advanced-technology audit checks registry integrity and cost/safety policy. Shared-report contract tests check schema validity and project coverage. Existing Homeguard tests remain the source of domain-specific verification.

Each report should record project, commit, schema version, capability status, evidence references, test conditions, limitations and result. A capability is `FOUNDATION` when supporting code exists, `PROTOTYPE` when an executable prototype exists, and `VERIFIED` only when defined acceptance criteria pass with reproducible evidence. Documentation or a passing registry audit alone never qualifies as verification.

## 8. Release gates

A change is ready for merge only when:
- shared schema is valid and byte-identical to the other project copies;
- audit and shared-contract tests pass;
- existing Homeguard tests pass;
- no paid service, automatic download or unreviewed dependency was introduced;
- all safety and performance claims remain within the evidence.

## 9. Current limitations

Homeguard remains an evidence-driven monitoring demonstrator. It does not establish certified alarm capability, real-world hazard detection, physical protection, autonomous roaming or safe-return performance.
