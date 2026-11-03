"""Tests for the free-first PUI89 technology registry audit."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("pui89_technology_audit", ROOT / "pui89_technology_audit.py")
if SPEC is None or SPEC.loader is None:
    raise ImportError("Could not load pui89_technology_audit.py")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)
audit_registry = AUDIT.audit_registry

class TechnologyAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "pui89_technology_capabilities.json").read_text(encoding="utf-8"))

    def test_current_registry_passes_policy_audit(self):
        self.assertEqual(audit_registry(self.data), [])

    def test_all_advanced_capability_groups_are_listed(self):
        ids = {item["id"] for item in self.data["capabilities"]}
        self.assertTrue({
            "multimodal_perception", "world_state_model", "uncertainty_calibration",
            "digital_twin_simulation", "slam_navigation", "motion_task_planning",
            "predictive_fault_detection", "agent_workflows", "multi_agent_coordination",
            "safety_verification", "local_inference", "evidence_provenance"
        }.issubset(ids))

    def test_paid_or_automatic_download_policy_fails_closed(self):
        bad = json.loads(json.dumps(self.data))
        bad["execution_policy"]["paid_apis_allowed"] = True
        self.assertTrue(audit_registry(bad))

    def test_verified_requires_evidence(self):
        bad = json.loads(json.dumps(self.data))
        bad["capabilities"][0]["status"] = "VERIFIED"
        bad["capabilities"][0]["implementation_evidence"] = []
        self.assertTrue(audit_registry(bad))

    def test_hardware_actuation_must_remain_disabled(self):
        bad = json.loads(json.dumps(self.data))
        bad["safety_boundary"]["no_hardware_actuation"] = False
        self.assertTrue(audit_registry(bad))

if __name__ == "__main__":
    unittest.main()
