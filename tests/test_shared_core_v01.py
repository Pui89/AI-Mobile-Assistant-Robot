import json
import os
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from homeguard_ai.core import Baseline, Observation, evaluate
from homeguard_ai.pui89_shared_core_v01 import build_nomad_v01_records

class NomadSharedCoreV01Tests(unittest.TestCase):
    def make_bundle(self):
        now = datetime(2026, 11, 1, 0, 0, 1, tzinfo=timezone.utc)
        obs = Observation(
            observation_id="nomad-fixture-001", sensor_id="synthetic-sensor-1",
            domain="water_moisture", metric="humidity", value=58.0, unit="%RH",
            timestamp="2026-11-01T00:00:00Z", location="synthetic-room",
            quality="VALID", calibrated=True, uncertainty=0.1,
        )
        baseline = Baseline("humidity", "%RH", 55.0, 12.0, 120, "synthetic-room")
        finding = evaluate(obs, baseline, now=now)
        return build_nomad_v01_records(obs, finding, recorded_at="2026-11-01T00:00:01Z")

    def test_maps_observation_world_state_and_advisory_proposal(self):
        bundle = self.make_bundle()
        self.assertEqual(bundle["observation"]["schema_version"], "0.1.0")
        self.assertEqual(bundle["observation"]["source"]["source_type"], "simulation")
        self.assertEqual(bundle["observation"]["quality"]["status"], "unknown")
        self.assertEqual(bundle["world_state"]["evidence_refs"][0], "nomad-fixture-001")
        self.assertEqual(bundle["action_proposal"]["authority"]["mode"], "advisory_only")
        self.assertIs(bundle["action_proposal"]["authority"]["execution_authorized"], False)

    def test_rejects_bad_timestamp_and_keeps_safety_boundaries(self):
        obs = Observation("x", "s1", "environment", "temperature", 25.0, "degC",
                          "2026-11-01T00:00:00", "room")
        with self.assertRaises(ValueError):
            build_nomad_v01_records(obs, {})
        serialized = json.dumps(self.make_bundle()).lower()
        self.assertIn("simulation-only", serialized)
        self.assertIn("not a diagnosis", serialized)

    def test_shared_core_schema_required_fields_match(self):
        core_dir = os.environ.get("PUI89_SHARED_CORE_DIR")
        if not core_dir:
            self.skipTest("Shared AI Core checkout is supplied by GitHub Actions")
        schema_dir = Path(core_dir) / "schemas" / "v0.1"
        bundle = self.make_bundle()
        for key, filename in (
            ("observation", "observation.schema.json"),
            ("world_state", "world-state.schema.json"),
            ("action_proposal", "action-proposal.schema.json"),
        ):
            schema = json.loads((schema_dir / filename).read_text(encoding="utf-8"))
            self.assertEqual(schema["properties"]["schema_version"]["const"], "0.1.0")
            self.assertTrue(set(schema["required"]).issubset(bundle[key].keys()))

if __name__ == "__main__":
    unittest.main()
