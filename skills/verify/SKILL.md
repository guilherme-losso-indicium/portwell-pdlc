---
name: verify
description: Runs the stage's verify_checks from its definition and records each one with what it looked at and its result. A failed check is a valid outcome and sends the item to correction. Names every check that a later module should make executable.
---

# Verify

## Purpose
Answer, check by check, whether the stage's artifact is what the stage requires. Not whether the
work is good. Whether the evidence is present, current, sourced and consistent. Fail is an answer.

## Parameters
`item`, `stage`. Runs in 02-discovery, 04-in-development, 05-review, 06-release and
07-monitoring.

## Entry conditions
- The stage artifact has the sections the checks look at. In 02-discovery, `evidence_manifest`,
  `route_note`, `decision_draft`. In 05-review, `readiness_checklist`, `policy_check`,
  `rollback_plan`. In 07-monitoring, `measures`, `incidents`, and a `criteria_ref`.
- `states/<stage>/definition.yaml` lists the `verify_checks`.

## Reads
- The stage definition's `verify_checks` and `failure_paths`.
- The artifact sections named above, and the documents they cite, to confirm a path resolves and
  a date is what the manifest says.
- `docs/Policies.docx`, `docs/incidents/`, the experiment registration.

## Prohibited context
- Anything that would make a check pass on plausibility. A check passes on a document or fails.
- Any source outside the two repositories.

## Writes
`verification` in 02-discovery, `build_record[].status` in 04-in-development, `verification_v2`
in 05-review, `release_log[].matches_g3_wave` in 06-release, `gate.verdict` in 07-monitoring.
`controls_missing` in every stage.

## Never writes
Any gate `outcome` or `signature`. Any `waivers` entry. Any change to the section it is checking.

## Procedure
1. Copy each check from the definition into `checks[]` with the exact wording.
2. For each check, write `looked_at`: the path, the manifest ID or the field examined. Then apply
   the rule and write `result: pass` or `result: fail`, with a `note` that says what was found.
   A check whose input is missing gets `result: cannot verify` and counts as fail.
3. Deterministic checks are written as input and result only. Account count against 25. Policy
   status on the date of the check. Fact date against incident date. Presence of a link behind a
   yes. Equality of draft thresholds and registered thresholds.
4. In 04-in-development, mark each scope item of the DECISION built, partial or not built from
   engineering's report, and each deviation with its `needs_g2` value.
5. In 07-monitoring, fill `gate.verdict.results`: for each criterion as registered before
   release, the registered threshold, the observed value with its source, and `met` as a
   comparison. If the registered threshold is `unknown`, `met` is `cannot verify`.
6. Set `outcome: passed` only when every check passed. Otherwise `outcome: failed` and list, from
   the definition's `failure_paths`, the `return_to` stage for each failure.
7. For every check that should be enforced by a hook, a test or a schema rather than by reading,
   add a `controls_missing` entry: the check, and what it would protect. Article 8.
8. Propose approve when passed. Propose recover with `correction-required` when failed.

## Evidence produced
A verification block that another person can re-run by following `looked_at`, and a list of the
controls this module performed by hand.

## Proposed transition
None between stages. Passed proposes approve. Failed proposes correction-required with a
`return_to`.

## Stop and escalation conditions
- A check cannot be performed because the input does not exist: record `cannot verify`, fail,
  and name who can supply the input.
- A contradiction recorded by context bears on a check: the check fails and points to the
  contradiction. Verify does not choose a side.
- The section being checked was edited after the check began: stop, note it, re-run.

## Human judgment boundary
Waiving a failed check, which is a signed waiver in 05-review. Reaffirming an invalidated fact.
Deciding that a fail does not matter, which no skill does.

## Worked example
OPPORTUNITY-04 in 05-review, against the checklist of 2026-08-26. Row 2, review capacity: yes,
evidence empty, and a written objection from the row owner on 2026-08-08: fail. Row 4, rollback:
cites `assist-expansion-design.docx`, which does not exist in the repository: fail. Row 6: checks
POLICY-10, superseded 2026-07-01 by POLICY-11: fail. Row 7: "pre-registered threshold" while the
registration's values are unknown: fail. Account count: input 28, threshold 25, exceeds.
Outcome failed. Controls missing: a schema that refuses yes without a link, a lookup that refuses
a superseded policy, a count that runs on every scope change.
