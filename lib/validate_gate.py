#!/usr/bin/env python3
"""Gate guard: no stage exit without a signed gate and documented consents.

Deterministic. No model judgment. It checks that fields exist and have the right shape.
It never decides whether an objection was addressed (constitution, Article 3).

Usage:
  validate_gate.py FILE [FILE ...]   validate artifacts on disk
  validate_gate.py --all             validate every lifecycle/*/*.yaml
  validate_gate.py --hook            Claude Code PreToolUse hook, JSON on stdin

Exit code 0 passes. Exit code 2 blocks (the code Claude Code hooks use to refuse a tool call).
"""
import datetime
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NO_RESPONSE = {"", "not on record", "unknown", "none", "null"}


def blank(value):
    return value is None or (isinstance(value, str) and value.strip().lower() in NO_RESPONSE)


def is_date(value):
    if isinstance(value, datetime.date):
        return True
    try:
        datetime.date.fromisoformat(str(value))
        return True
    except ValueError:
        return False


def load_definition(stage):
    path = ROOT / "states" / stage / "definition.yaml"
    if not path.exists():
        return None
    return yaml.safe_load(path.read_text())


def find_transition(definition, outcome):
    for transition in definition.get("allowed_transitions") or []:
        match = re.search(r"outcome (\S+?)(?:[,\s]|$)", str(transition.get("when", "")))
        if match and match.group(1) == outcome:
            return transition
    return None


def validate(artifact):
    """Return a list of violations. Empty means the artifact may be written."""
    problems = []
    if not isinstance(artifact, dict):
        return ["artifact is not a YAML mapping"]
    gate = artifact.get("gate")
    stage = artifact.get("stage")

    # A consent counts as given only with the person's own dated words.
    if isinstance(gate, dict):
        for consent in gate.get("consents") or []:
            if consent.get("state") == "consented":
                who = consent.get("person", "unknown person")
                if blank(consent.get("response")):
                    problems.append(f"consent of {who} is 'consented' with no written response")
                if not is_date(consent.get("responded_on")):
                    problems.append(f"consent of {who} is 'consented' with no response date")

    exiting = (
        artifact.get("status") == "exited"
        or artifact.get("exited") is not None
        or artifact.get("exited_to") is not None
    )
    if not exiting or not isinstance(gate, dict):
        return problems

    gate_id = gate.get("id", "gate")
    signature = gate.get("signature") or {}
    missing = [k for k in ("person", "role", "statement", "date") if blank(signature.get(k))]
    if missing:
        problems.append(
            f"gate {gate_id} is not signed: gate.signature.{', '.join(missing)} empty"
        )

    outcome = gate.get("outcome")
    if blank(outcome):
        problems.append(f"gate {gate_id} has no outcome")
    elif outcome not in (gate.get("options") or []):
        problems.append(f"outcome '{outcome}' is not one of gate.options {gate.get('options')}")

    definition = load_definition(stage)
    if definition is None:
        problems.append(f"no definition for stage '{stage}' in states/")
        return problems
    if blank(outcome):
        return problems

    transition = find_transition(definition, outcome)
    if transition is None:
        problems.append(f"no allowed transition for {gate_id} outcome '{outcome}' in stage {stage}")
        return problems
    target = transition.get("to")
    if artifact.get("exited_to") != target:
        problems.append(
            f"exited_to is '{artifact.get('exited_to')}' but outcome '{outcome}' allows only '{target}'"
        )
    if target == stage:
        problems.append(f"outcome '{outcome}' keeps the item in {stage}; it cannot be exited")

    # Advancing to another stage needs every required consent. A terminal reject does not.
    if target not in (stage, "terminal"):
        for consent in gate.get("consents") or []:
            if consent.get("state") != "consented":
                problems.append(
                    f"advancing needs every consent: {consent.get('person', 'unknown person')} "
                    f"is '{consent.get('state')}'"
                )
    return problems


def message(path, problems):
    lines = [
        f"BLOCKED: {path} cannot be written as an exit.",
        *[f"  - {p}" for p in problems],
        "Recovery:",
        "  1. Do not fill the signature or a consent yourself. Only the named person does.",
        "  2. Ask the decider to sign the gate, or to record reject, more-discovery or defer in their own words.",
        "  3. Ask each person above for a dated written response.",
        "  4. Run the recover skill to log the episode in status_log (waiting_on, asks, escalate_to).",
        "No file was written.",
    ]
    return "\n".join(lines)


def check_file(path):
    return validate(yaml.safe_load(Path(path).read_text()))


def lifecycle_path(file_path):
    try:
        relative = Path(file_path).resolve().relative_to(ROOT)
    except ValueError:
        return None
    parts = relative.parts
    if len(parts) == 3 and parts[0] == "lifecycle" and relative.suffix == ".yaml":
        return relative
    return None


def hook():
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path")
    relative = lifecycle_path(file_path) if file_path else None
    if relative is None:
        return 0
    if "content" in tool_input:
        text = tool_input["content"]
    else:
        current = Path(file_path).read_text() if Path(file_path).exists() else ""
        old, new = tool_input.get("old_string", ""), tool_input.get("new_string", "")
        text = current.replace(old, new) if tool_input.get("replace_all") else current.replace(old, new, 1)
    try:
        artifact = yaml.safe_load(text)
    except yaml.YAMLError as error:
        print(f"BLOCKED: {relative} would not be valid YAML: {error}", file=sys.stderr)
        return 2
    problems = validate(artifact)
    if problems:
        print(message(relative, problems), file=sys.stderr)
        return 2
    return 0


def main(argv):
    if argv[:1] == ["--hook"]:
        return hook()
    paths = sorted(ROOT.glob("lifecycle/*/*.yaml")) if argv[:1] == ["--all"] else [Path(a) for a in argv]
    if not paths:
        print(__doc__)
        return 1
    status = 0
    for path in paths:
        problems = check_file(path)
        if problems:
            print(message(path, problems), file=sys.stderr)
            status = 2
        else:
            print(f"ok  {path}")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
