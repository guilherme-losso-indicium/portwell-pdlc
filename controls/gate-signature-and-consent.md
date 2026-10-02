# Control candidate: no stage exit without a signed gate and documented consents

Module 3 control record. Implemented in `lib/validate_gate.py`, wired by `.claude/settings.json`
and `hooks/pre-commit`, covered by `tests/test_validate_gate.py`.

## 1. The rule and its current source

A stage artifact may be exited only when `gate.signature` is complete (person, role, statement,
date) and each required consent is a dated written response from that person.

Sources, all prose before this control:
- `skills/constitution/SKILL.md`, Article 3.
- `skills/handoff/SKILL.md`, procedure step 1: "If `gate.signature.person` is null, refuse".
- `lifecycle/02-discovery/OPPORTUNITY-04.yaml`, `controls_missing`: "a consent cannot be recorded
  as given without a dated written response from that person".

The handoff refusal is the model reading a sentence. Nothing stopped an edit that wrote
`exited_to` over a null signature.

## 2. Failure the fixture shows

- Launch readiness checklist row 2 reads as met. Rui Bastos, Support Manager, objected in
  writing on 2026-08-08. Who ticked the row and when is `unknown`.
- DECISION-0028 (2026-08-07): "Approver: Ana Fialho. No other signature." The pilot reached 28
  accounts, above the POLICY-08 threshold of 25.
- `docs/How we work today.docx`: "agreement means nobody objected in the meeting". Silence counted
  as consent.
- Trace steps 4, 5, 12 and 13: G1 and G2 reach handoff with `signature.person: null`. Handoff
  refused only because the skill obeyed its own text.

## 3. Invariant

A stage transition exists only when the artifact proves, in fields no skill writes, that a named
person decided and that every required consent has that person's literal, dated response. The
control checks presence and shape. It never judges whether an objection was addressed. That
stays with the person who raised it (Article 3).

## 4. Implementation form

| Layer | File | Role |
| :- | :- | :- |
| Guard | `lib/validate_gate.py` | Deterministic checks, no model. Exit code 2 blocks |
| Hook | `.claude/settings.json` | `PreToolUse` on `Write` and `Edit`. Checks the content that would be written to `lifecycle/<stage>/<ITEM>.yaml` |
| Pre-commit | `hooks/pre-commit` | Same guard outside Claude Code |
| Contract | `states/<stage>/definition.yaml` | `allowed_transitions` and `gate.options` are read, not copied |

Checks, in order:
1. A consent with `state: consented` has a response other than empty or "not on record", and an
   ISO `responded_on`. Applies on every write, not only on exit.
2. When the artifact exits (`status: exited`, `exited` or `exited_to` set) and has a gate:
   signature person, role, statement and date are all present.
3. `gate.outcome` is one of `gate.options` and maps to an `allowed_transitions` entry.
4. `exited_to` equals that entry's `to`. An outcome that keeps the item in the stage cannot exit.
5. When the exit advances to another stage, every consent is `consented`. A terminal reject
   needs none.

Not covered: stages without a gate (03, 04, 06, 08) and their `exit_conditions`. Whether the
person who signs is the decider named in the definition. Whether an edit to `gate.signature` was
made by a person and not by a skill. A `Bash` write bypasses the hook, and the pre-commit and
review are the net for that.

## 5. Failure message and recovery

```
BLOCKED: lifecycle/02-discovery/OPPORTUNITY-04.yaml cannot be written as an exit.
  - gate G2 is not signed: gate.signature.person, role, statement, date empty
  - advancing needs every consent: Rui Bastos is 'objected'
  - advancing needs every consent: Tomas Silva is 'objected'
  - advancing needs every consent: Kofi Adjei is 'not-on-record'
Recovery:
  1. Do not fill the signature or a consent yourself. Only the named person does.
  2. Ask the decider to sign the gate, or to record reject, more-discovery or defer in their own words.
  3. Ask each person above for a dated written response.
  4. Run the recover skill to log the episode in status_log (waiting_on, asks, escalate_to).
No file was written.
```

## 6. Portability

| Change | Survives | Why |
| :- | :- | :- |
| Model | Yes | Plain code. No model judgment in the check |
| Coding harness | Partly | The guard, schema reads and pre-commit are harness-free. `.claude/settings.json` is Claude Code only and needs an adapter elsewhere |
| Track repository | Partly | Signature and consent shape are generic. Who must consent comes from Portwell policy owners and IDs, derived by `route` |

Proposed split: `lib/` and `states/` are the portable core. `.claude/settings.json` is a
disposable adapter.

## Owner

To be named by the group. Proposed: the lifecycle owner, reviewed by the policy owners.

## Before and after

Before: `tests/test_validate_gate.py`, class `BeforeTheControl`, each case writes an exit that
the repository previously accepted. After: the same writes return exit code 2 with the message
above, and the current records plus a signed, fully consented `build` still pass.

Run: `python3 -m unittest discover tests`
