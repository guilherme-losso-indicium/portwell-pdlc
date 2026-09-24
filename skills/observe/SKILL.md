---
name: observe
description: In monitoring, collects each measure with its source and metric version against criteria frozen before release, links incidents with their dates and what they invalidate, and fires the triggers that send an item to correction or to its outcome review.
---

# Observe

## Purpose
See what the release did, using the yardstick that existed before it. Count only what has a
source. Treat an incident as an event with a date that reaches back into the evidence. Say when
it is time to look again.

## Parameters
`item`, `stage`. Runs in 07-monitoring only.

## Entry conditions
- The 07-monitoring artifact exists with `entry_ticket.criteria_ref` pointing to criteria frozen
  before the wave was enabled: an experiment registration with `frozen: true`, or the DECISION
  record's review criteria.
- `active_scope` is written by context.

## Reads
- `entry_ticket.criteria_ref` and the document it names, as frozen.
- `data/launch/adoption-measures-draft.xlsx`, `data/experiments/EXPERIMENT-02-results.xlsx`, and
  whatever measure sources the DECISION names.
- `docs/incidents/`, every write-up, for written date, scope touched and what was checked.
- The DECISION record's `review_date`. Linked items' artifacts, to mark invalidated facts.

## Prohibited context
- Criteria edited after the run. If the only available criteria post-date the release, that is a
  contradiction, not a yardstick.
- A number without a source. It is recorded and not counted.
- Any external analytics system. In Module 1 the sources are documents in the track repository.

## Writes
`measures`, `wave_criteria`, `incidents`, `triggers`. Proposes `correction-required` and
`blocked` through recover. Proposes `invalidated_by` entries in linked items' manifests, which
context applies.

## Never writes
`incidents[].disposition`, which the owner chooses and signs. `gate.verdict`, which verify
writes. `gate.outcome`, `gate.signature`.

## Procedure
1. Criteria. Copy each criterion from `criteria_ref` as frozen: measure, operator, value, unit.
   If the registration's `frozen` is false or its registered values are `unknown`, write that
   under `contradictions` with `depends: G4` and continue. The verdict will read `cannot verify`.
2. Measures. For each criterion and each agreed adoption measure: `name`, `definition`,
   `target`, `source`, `metric_version`, `value`, `as_of`. `counted: true` only when source and
   metric version are on record. A measure the company lists with "Not measured" as its source
   is recorded with `counted: false` and a `controls_missing` entry.
3. Wave criteria. Where the G3 wave plan set `go_criteria` for the next wave, write each with its
   current status and `as_of`.
4. Incidents. For each write-up in `docs/incidents/` whose scope touches this item: `id`,
   `path`, `written`, `occurred` or `unknown`, `effect_on_item` in one sentence quoting the
   write-up, `invalidates` as the list of manifest IDs, in this item and in every linked item,
   dated before `written`. Leave `disposition` null. Name the `owner`.
5. Triggers. Fire one entry for each: an incident linked; the `review_date` passed; a fact
   invalidated. Each trigger names its `action`: propose `correction-required` for an incident or
   an invalidation, propose `blocked` reason awaiting review for a passed review date.
6. Propose verify for the verdict, then approve for G4. Where a trigger fired, propose recover
   first.

## Evidence produced
A monitoring block that separates what was measured from what was merely quoted, ties every
incident to the facts it undermines, and shows why the item is being looked at again.

## Proposed transition
None between stages. Proposes verify and approve. Through recover, `correction-required` or
`blocked`.

## Stop and escalation conditions
- The frozen criteria cannot be found: record it, `depends: G4`, and continue so the verdict
  shows `cannot verify`. Do not substitute the current document's values.
- An incident write-up states no occurrence date: `occurred: unknown`. Order by `written`.
- A measure the decider asks about has no source: report it as not counted. Never estimate it.
- An incident's `invalidates` list touches a linked item whose gate is pending: name that item
  and propose `correction-required` on it too.

## Human judgment boundary
The disposition of an incident: correct, escalate, or new item. Reaffirming an invalidated fact.
The outcome at G4.

## Worked example
The help portal pilot, if it had an item. Criteria from EXPERIMENT-02, registered 2026-05-28,
values as shown in a document last edited 2026-07-21, registered values unknown: contradiction,
`depends: G4`. Measures from `EXPERIMENT-02-results.xlsx`, compiled 2026-07-18, metric version
unknown. "Review load per engineer": source "Not measured", `counted: false`. INCIDENT-01,
written 2026-07-14, invalidates the brief of 2026-06-18 in OPPORTUNITY-04. INCIDENT-02, written
2026-07-29, occurred unknown. Two triggers fired. Disposition of both: null, owner Ana Fialho,
which is the state the repository records: "Nobody owns the follow-up."
