"""Map NOMAD environmental observations to PUI89 Shared AI Core v0.1."""
from __future__ import annotations
from datetime import datetime

SCHEMA_VERSION = "0.1.0"

def _timestamp(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("timestamp must be a non-empty ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamp must be valid ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")
    return value

def build_nomad_v01_records(observation, finding, *, recorded_at=None):
    """Translate a validated software observation and finding; no actuation."""
    observation.validate()
    if not isinstance(finding, dict):
        raise ValueError("finding must be an object")
    observed_at = _timestamp(observation.timestamp)
    recorded_at = _timestamp(recorded_at or observed_at)
    source_id = observation.observation_id
    evidence_refs = [source_id, observation.sensor_id]

    shared_observation = {
        "schema_version": SCHEMA_VERSION,
        "observation_id": source_id,
        "observed_at": observed_at,
        "source": {
            "source_id": source_id,
            "source_type": "simulation",
            "device_or_system": "PUI89 AI NOMAD software observation baseline",
        },
        "modality": "other",
        "payload": {
            "domain": observation.domain,
            "metric": observation.metric,
            "value": observation.value,
            "unit": observation.unit,
            "location": observation.location,
            "quality_input": observation.quality,
            "calibrated_input": observation.calibrated,
            "finding": finding,
            "evidence_status": "SIMULATION-ONLY",
        },
        "quality": {
            "status": "unknown",
            "notes": "Current NOMAD test records are software/synthetic; real sensor integration is not established.",
        },
        "uncertainty": {
            "description": "Baseline deviations and software findings do not diagnose the cause or prove a physical hazard.",
            "value": observation.uncertainty if observation.uncertainty is not None and observation.uncertainty <= 1 else None,
            "method": "Caller-supplied uncertainty field; calibration not independently verified.",
        },
        "provenance": {"recorded_at": recorded_at, "dataset_or_file": "synthetic-or-caller-supplied NOMAD observation"},
    }
    world_state = {
        "schema_version": SCHEMA_VERSION,
        "state_id": f"nomad-world-state:{source_id}",
        "updated_at": recorded_at,
        "evidence_refs": evidence_refs,
        "entities": [{
            "entity_id": observation.sensor_id,
            "category": observation.metric,
            "state": {
                "value": observation.value,
                "unit": observation.unit,
                "finding_status": finding.get("status", "UNKNOWN"),
            },
            "evidence_refs": [source_id],
        }],
        "unknowns": list(finding.get("limitations", [])) + [
            "Physical sensor health and real-world building conditions are not established by this software record."
        ],
        "notes": "Advisory software state only; not a diagnosis or certified alarm.",
    }
    proposal = {
        "schema_version": SCHEMA_VERSION,
        "proposal_id": f"nomad-human-review:{source_id}",
        "created_at": recorded_at,
        "objective": "Request human review of the NOMAD environmental observation and evidence quality.",
        "world_state_ref": world_state["state_id"],
        "actions": [{
            "action_id": f"review:{source_id}",
            "description": "Review the observation, sensor provenance, freshness and baseline before deciding whether further inspection is needed.",
            "risk_level": "unknown",
            "preconditions": [
                "Verify the physical sensor, calibration and location independently.",
                "Use certified smoke, fire, carbon-monoxide and electrical protection devices as primary safeguards.",
            ],
            "expected_effect": "A human reviewer confirms evidence quality or requests further inspection.",
            "hazards": [
                "A baseline deviation is not proof of damage, danger or root cause.",
                "Do not operate locks, breakers, valves, appliances or emergency systems from this proposal.",
            ],
            "evidence_refs": evidence_refs,
        }],
        "authority": {
            "mode": "advisory_only",
            "human_approval_required": True,
            "execution_authorized": False,
        },
        "uncertainties": [
            "Software-only evidence; real sensor integration and field validation are not established.",
            "The result must not be used as a substitute for certified safety equipment.",
        ],
    }
    return {"observation": shared_observation, "world_state": world_state, "action_proposal": proposal}
