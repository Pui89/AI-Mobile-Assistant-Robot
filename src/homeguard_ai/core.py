"""Dependency-free observation contracts and transparent evidence evaluation."""
from __future__ import annotations
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib

def parse_timestamp(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return dt.astimezone(timezone.utc)

@dataclass(frozen=True)
class Observation:
    observation_id: str
    sensor_id: str
    domain: str
    metric: str
    value: float
    unit: str
    timestamp: str
    location: str
    quality: str = "VALID"
    calibrated: bool = True
    uncertainty: float | None = None

    def validate(self) -> None:
        if not all((self.observation_id, self.sensor_id, self.domain, self.metric, self.unit, self.location)):
            raise ValueError("identity, domain, metric, unit and location are required")
        if self.quality not in {"VALID", "DEGRADED", "INVALID"}:
            raise ValueError("invalid quality state")
        if self.uncertainty is not None and self.uncertainty < 0:
            raise ValueError("uncertainty cannot be negative")
        parse_timestamp(self.timestamp)

@dataclass(frozen=True)
class Baseline:
    metric: str
    unit: str
    mean: float
    tolerance: float
    sample_count: int
    location: str

    def validate(self) -> None:
        if self.tolerance < 0 or self.sample_count < 1:
            raise ValueError("invalid baseline tolerance or sample count")
        if not all((self.metric, self.unit, self.location)):
            raise ValueError("baseline metric, unit and location are required")

def evaluate(observation: Observation, baseline: Baseline, now: datetime | None = None,
             max_age_seconds: int = 3600) -> dict:
    observation.validate()
    baseline.validate()
    if (observation.metric, observation.unit, observation.location) != (
        baseline.metric, baseline.unit, baseline.location
    ):
        raise ValueError("observation and baseline metric/unit/location must match")
    current = now or datetime.now(timezone.utc)
    age = (current - parse_timestamp(observation.timestamp)).total_seconds()
    digest = hashlib.sha256(observation.observation_id.encode()).hexdigest()[:12]
    limitations = []
    deviation = None
    if age < -60:
        status, severity, summary = "DATA_QUALITY", "REVIEW", "Observation timestamp is in the future"
        limitations.append("Check clock synchronization")
    elif age > max_age_seconds:
        status, severity, summary = "STALE", "REVIEW", "Observation is outside the freshness window"
        limitations.append("Stale evidence cannot establish current building condition")
    elif observation.quality != "VALID" or not observation.calibrated:
        status, severity, summary = "DEGRADED_EVIDENCE", "REVIEW", "Evidence quality or calibration is insufficient"
        limitations.append("Do not interpret this input as a normal or abnormal state")
    else:
        deviation = observation.value - baseline.mean
        if abs(deviation) > baseline.tolerance:
            status, severity, summary = "BASELINE_DEVIATION", "REVIEW", "Observation differs from the documented baseline"
            limitations.append("A deviation is not proof of damage, danger or root cause")
        else:
            status, severity, summary = "WITHIN_BASELINE", "INFO", "Observation is within configured baseline tolerance"
    return {
        "finding_id": f"HG-{digest}", "observation_id": observation.observation_id,
        "status": status, "severity": severity, "summary": summary,
        "observed_value": observation.value, "baseline_value": baseline.mean,
        "deviation": deviation, "uncertainty": observation.uncertainty,
        "evidence": [observation.observation_id, observation.sensor_id],
        "limitations": limitations,
        "recommended_action": "Check sensor health, calibration and source evidence" if status in
            {"DATA_QUALITY", "STALE", "DEGRADED_EVIDENCE"} else
            "Human review if deviation is persistent or safety-relevant",
        "evidence_status": "SIMULATION-ONLY"
    }
