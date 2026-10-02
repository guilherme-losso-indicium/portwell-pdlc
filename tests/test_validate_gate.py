"""Regression cases for lib/validate_gate.py. Run: python3 -m unittest discover tests"""
import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "lib"))
import validate_gate  # noqa: E402

REAL = ROOT / "lifecycle" / "02-discovery" / "OPPORTUNITY-04.yaml"
SIGNATURE = {
    "person": "Ana Fialho",
    "role": "product lead",
    "statement": "Build, as drafted.",
    "date": "2026-09-30",
}


def real_artifact():
    return yaml.safe_load(REAL.read_text())


def exit_attempt(outcome="build", exited_to="03-ready-for-development", signature=None):
    """The artifact as it stands today, with a handoff written on top."""
    artifact = copy.deepcopy(real_artifact())
    artifact["status"] = "exited"
    artifact["exited"] = "2026-09-30"
    artifact["exited_to"] = exited_to
    artifact["gate"]["outcome"] = outcome
    if signature:
        artifact["gate"]["signature"] = signature
    return artifact


def all_consented(artifact):
    for consent in artifact["gate"]["consents"]:
        consent["state"] = "consented"
        consent["response"] = "Agreed in writing."
        consent["responded_on"] = "2026-09-29"
    return artifact


class BeforeTheControl(unittest.TestCase):
    """The failures the trace shows. Each used to pass because only prose forbade it."""

    def test_unsigned_gate_cannot_exit(self):
        problems = validate_gate.validate(exit_attempt())
        self.assertTrue(any("is not signed" in p for p in problems), problems)

    def test_objection_cannot_be_overridden_by_signature_alone(self):
        problems = validate_gate.validate(exit_attempt(signature=SIGNATURE))
        self.assertTrue(any("Rui Bastos" in p and "objected" in p for p in problems), problems)
        self.assertTrue(any("Kofi Adjei" in p and "not-on-record" in p for p in problems), problems)

    def test_consented_without_words_is_refused(self):
        artifact = real_artifact()
        artifact["gate"]["consents"][0].update(state="consented", response="not on record")
        problems = validate_gate.validate(artifact)
        self.assertTrue(any("no written response" in p for p in problems), problems)

    def test_consented_without_date_is_refused(self):
        artifact = real_artifact()
        artifact["gate"]["consents"][0].update(state="consented", responded_on=None)
        problems = validate_gate.validate(artifact)
        self.assertTrue(any("no response date" in p for p in problems), problems)

    def test_wrong_target_for_outcome_is_refused(self):
        artifact = all_consented(exit_attempt(exited_to="05-review", signature=SIGNATURE))
        problems = validate_gate.validate(artifact)
        self.assertTrue(any("allows only '03-ready-for-development'" in p for p in problems), problems)

    def test_outcome_that_stays_in_stage_cannot_exit(self):
        artifact = exit_attempt(outcome="defer", exited_to="02-discovery", signature=SIGNATURE)
        problems = validate_gate.validate(artifact)
        self.assertTrue(any("cannot be exited" in p for p in problems), problems)

    def test_unknown_outcome_is_refused(self):
        problems = validate_gate.validate(exit_attempt(outcome="approve", signature=SIGNATURE))
        self.assertTrue(any("not one of gate.options" in p for p in problems), problems)


class AfterTheControl(unittest.TestCase):
    """What must still work."""

    def test_current_records_pass(self):
        for path in sorted(ROOT.glob("lifecycle/*/*.yaml")):
            self.assertEqual(validate_gate.check_file(path), [], path)

    def test_signed_and_consented_build_passes(self):
        artifact = all_consented(exit_attempt(signature=SIGNATURE))
        self.assertEqual(validate_gate.validate(artifact), [])

    def test_signed_reject_needs_no_consents(self):
        artifact = exit_attempt(outcome="reject", exited_to="terminal", signature=SIGNATURE)
        self.assertEqual(validate_gate.validate(artifact), [])


class HookProtocol(unittest.TestCase):
    def run_hook(self, tool_input):
        return subprocess.run(
            [sys.executable, str(ROOT / "lib" / "validate_gate.py"), "--hook"],
            input=json.dumps({"tool_input": tool_input}),
            capture_output=True,
            text=True,
        )

    def test_write_of_unsigned_exit_is_blocked_with_recovery(self):
        content = yaml.safe_dump(exit_attempt())
        result = self.run_hook({"file_path": str(REAL), "content": content})
        self.assertEqual(result.returncode, 2)
        self.assertIn("gate G2 is not signed", result.stderr)
        self.assertIn("Recovery:", result.stderr)
        self.assertIn("No file was written.", result.stderr)

    def test_edit_that_sets_exited_to_is_blocked(self):
        result = self.run_hook({
            "file_path": str(REAL),
            "old_string": "exited_to: null",
            "new_string": "exited_to: 03-ready-for-development",
        })
        self.assertEqual(result.returncode, 2, result.stderr)

    def test_files_outside_lifecycle_are_ignored(self):
        result = self.run_hook({"file_path": str(ROOT / "board.md"), "content": "x"})
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
