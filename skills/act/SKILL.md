---
name: act
description: Produces the stage's work product from the manifest and nothing else. The experiment registration and the decision draft in discovery, the readiness checklist rows in review, the release log entries in release. Every statement cites a manifest entry.
---

# Act

## Purpose
Write the thing the stage exists to produce, in the form the company already uses, with every
statement traceable to the manifest. A draft is not a decision. A registration is not frozen until
a person signs it. A checklist row is what its owner's evidence says, not what the row owner
believes.

## Parameters
`item`, `stage`. Runs in 02-discovery, 05-review and 06-release.

## Entry conditions
- Context and route have run in this stage, or, in 06-release, intake has run and G3 is signed.
- `states/types.yaml` lists what the item's proposed type requires at the next gate.

## Reads
- `evidence_manifest`, `route_note`, `stakeholder_positions`, `states/types.yaml`.
- For form: `data/decisions/DECISION-0031-cycle-count-module-deprecation.docx` as the example of
  a complete DECISION record, and `data/experiments/EXPERIMENT-02-design-and-result.docx` as the
  example of a registration.
- In 05-review: `data/launch/launch-readiness-checklist.xlsx` and the documents its rows cite.
- In 06-release: engineering's written confirmation of what was enabled.

## Prohibited context
- Anything not in the manifest. If a statement needs a fact the manifest lacks, the fact is added
  through context first or written as `unknown`.
- The model's opinion of what the decision should be.

## Writes
In 02-discovery: `experiment_registration` for poc and pilot, `decision_draft`. In 05-review:
`readiness_checklist`. In 06-release: `release_log` entries.

## Never writes
`experiment_registration.frozen`, `frozen_on`, `frozen_by`. `decision_draft.reference`, which the
product repository issues. Any checklist row `status: yes` without an `evidence.path`. Any
`release_log` entry from the plan rather than from engineering's confirmation.

## Procedure
1. Read `types.yaml` for the proposed type. Each element under `g2_requires` or `g3_requires`
   maps to a field in what you are about to write. Where the manifest has no fact for an element,
   the field is `unknown` and the element goes under `unknowns`.
2. Experiment registration, poc and pilot only. Copy question, method, accounts, period and
   thresholds from the source, with the source's date. If the source was last edited after the
   run ended and the thresholds it shows may not be the registered ones, record the registered
   values as `unknown` and add a contradiction citing the edit date and any statement about the
   change. Leave `frozen: false`.
3. Decision draft. Use the DECISION-0031 form: decision, rationale, scope, out of scope, evidence,
   constraints, review date, type. Every sentence in `rationale` ends with the manifest IDs it
   rests on. `evidence` is a list of manifest IDs, not prose. `review_date` is required; if no
   source gives one, `unknown`, flagged for the decider. `reference` stays null.
4. Readiness checklist, 05-review only. One row per item of the company's checklist. For each,
   find the row owner's written evidence. `status: yes` only with an `evidence.path` that
   resolves to a dated document. A tick with no link is `yes-without-evidence`. A cited file that
   does not exist is recorded as such in `evidence.path` with a note. Never move a row to yes on
   the strength of a conversation.
5. Release log, 06-release only. One entry per wave, from engineering's confirmation: date,
   accounts, regions, who enabled, communications with dates and senders, rollback test date or
   `unknown`. `matches_g3_wave` is left for verify.
6. Propose the next skill in the sequence.

## Evidence produced
A registration, a draft or a checklist that a reviewer can check line by line against the
manifest, with every gap visible.

## Proposed transition
None between stages. Proposes verify.

## Stop and escalation conditions
- A required element has no fact behind it and the gate cannot be signed without it: write
  `unknown`, name who can supply it, propose correction-required.
- The registered thresholds cannot be recovered: stop. The decider decides whether the experiment
  is re-registered or its verdict is taken as contested. Do not write the current document's
  values as if they were registered.
- The draft would need a number nobody recorded, such as a baseline for one account: `unknown`.
- Engineering's confirmation for a wave does not exist: no release log entry is written.

## Human judgment boundary
The content of the decision. Freezing a registration. Ticking a checklist row. Accepting a risk
through a waiver.

## Worked example
OPPORTUNITY-04. `EXPERIMENT-02-design-and-result.docx` was last edited 2026-07-21, six days after
the run ended, and its author said on 2026-08-12 that a threshold "was adjusted". The registration
records the thresholds the document shows, marks the registered values `unknown`, and adds the
contradiction. The decision draft's rationale cannot cite the experiment as a clean pass.
