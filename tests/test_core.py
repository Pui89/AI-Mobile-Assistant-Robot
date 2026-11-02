from datetime import datetime, timedelta, timezone
import pytest
from homeguard_ai.core import Baseline, Observation, evaluate
from homeguard_ai.simulator import run_scenario

def obs(**kw):
    d=dict(observation_id="o1",sensor_id="s1",domain="environment",metric="temperature",
           value=30.0,unit="degC",timestamp=datetime.now(timezone.utc).isoformat(),
           location="floor-1/room-1",quality="VALID",calibrated=True,uncertainty=.1)
    d.update(kw); return Observation(**d)
def base(): return Baseline("temperature","degC",25.0,2.0,30,"floor-1/room-1")
def test_deviation_is_not_a_diagnosis():
    f=evaluate(obs(),base()); assert f["status"]=="BASELINE_DEVIATION"
    assert "not proof" in f["limitations"][0]
def test_within_baseline():
    assert evaluate(obs(value=25.5),base())["status"]=="WITHIN_BASELINE"
def test_stale_is_not_normal():
    old=(datetime.now(timezone.utc)-timedelta(hours=3)).isoformat()
    f=evaluate(obs(timestamp=old),base()); assert f["status"]=="STALE" and f["deviation"] is None
def test_uncalibrated_is_degraded():
    assert evaluate(obs(calibrated=False),base())["status"]=="DEGRADED_EVIDENCE"
def test_bad_quality_is_degraded():
    assert evaluate(obs(quality="INVALID"),base())["status"]=="DEGRADED_EVIDENCE"
def test_unit_mismatch_rejected():
    with pytest.raises(ValueError): evaluate(obs(unit="F"),base())
def test_location_mismatch_rejected():
    with pytest.raises(ValueError): evaluate(obs(location="floor-2/room-2"),base())
def test_timezone_required():
    with pytest.raises(ValueError): obs(timestamp="2026-01-01T12:00:00").validate()
def test_simulation_label_and_channels():
    r=run_scenario(89); assert r["evidence_status"]=="SIMULATION-ONLY"
    assert len(r["findings"])==3
