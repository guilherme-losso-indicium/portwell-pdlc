---
name: recover
description: Opens, tracks and closes the blocked, escalated and correction-required episodes of an artifact. Counts asks against the limit, names who is waited on and where the item returns, and reopens an earlier stage when a correction requires it. Never declares a disagreement resolved.
---

# Recover

## Purpose
Give failure a record. When an item cannot advance, say why, who is waited on, since when, how
many times they were asked, and where the item goes when the wait ends. When work must be redone,
say what and from where. Recover is how "ask again" becomes a process.

## Parameters
`item`, `stage`, and the trigger: the skill and condition that called it.

## Entry conditions
- One of the definition's `failure_paths` or a universal stop condition was reached by another
  skill, and that skill wrote the reason in the artifact.
- `states/statuses.yaml` is readable.

## Reads
- `states/statuses.yaml`, the stage definition's `failure_paths` and `allowed_transitions`.
- The artifact's `status_log`, `gate.consents`, `unknowns`, `contradictions`, `verification`.
- For asks and dates: the tracker row, stakeholder requests, interview lines. Nothing verbal.
- `data/people/headcount.xlsx`, to write the role of an escalation target a person has named.

## Prohibited context
- Any claim that a matter was "considered" or "discussed" as grounds to close an episode.
- Any escalation target the model would pick. A target is named by a person or is
  `not named`.

## Writes
`status`, `status_since`, and appended `status_log` lines. On a correction whose `return_to` is
an earlier stage: one appended `status_log` line in that stage's artifact reopening it. On an
incident disposition `new-item`: a proposed backlog entry, pending an ID.

## Never writes
Any earlier `status_log` line. Any `gate` field. `contradictions[].resolved_by`.
`consents[].state` for anyone but the person who responded.

## Procedure
1. Identify the trigger and the status it maps to in `statuses.yaml`: a pending input or a
   passed deadline maps to `blocked`; a `blocked` at its limit or a disputed classification maps
   to `escalated`; a failed check, a linked incident, an invalidated fact, a contested verdict or
   a scope deviation maps to `correction-required`.
2. Open the episode. Append a `status_log` line with `n`, `status`, `since`, `reason` quoting the
   calling skill's note, `waiting_on`, `owner`, `asks` as a list of dates on record, `limit: 3`,
   `escalate_to` as a person has named it or `not named`, `return_to` as the stage and status the
   item goes back to. Set `status` and `status_since` in the header.
3. Asks. Each further ask is a date appended to `asks`, with the document that records it. If
   the record says a number without dates, write the number as `unknown` dates and cite the
   record. When `asks` reaches `limit`, close the line with `until` today and open an `escalated`
   line.
4. Escalation. If `escalate_to` is `not named`, the episode cannot advance. Write under
   `unknowns` "escalation target for <reason>: not named", ask the process owner in writing to
   name one, and end. When a target is named, the target's decision is recorded verbatim under
   the line and the item returns per `return_to`, or ends rejected or retired.
5. Resolution of a block. Only a written, dated input from the person waited on closes the line:
   copy it verbatim into `reason` continuation, set `until`, set `status: open`. A consent
   objected stays objected unless the objector writes otherwise.
6. Correction. Write what must change, citing the failed check or the incident ID, and the
   `return_to` stage from the definition. If `return_to` is an earlier stage, append to that
   stage's artifact a line "reopened by correction from <stage>, <reason>" and set its `status:
   open`. Do not edit anything already in that artifact. The current artifact keeps
   `correction-required` until the earlier stage exits again.
7. New linked item. When an incident disposition is `new-item`, or a correction needs a control
   the item cannot deliver, write the proposed backlog entry with `links.spawned_by`, and stop
   for an ID from the product repository.
8. Report to the trace: the episode, the person it waits on, and the question they must answer.

## Evidence produced
A status log in which every stall has a start, a reason, a person, a count and an exit, and every
correction says what was wrong and where the work went back to.

## Proposed transition
Back to `open` in `return_to` when the input arrives. `escalated` at the limit. `rejected` or
`retired` when an escalation target signs so.

## Stop and escalation conditions
- No escalation target is named: stop. The process has no next step, and the artifact says so.
- The resolution offered is not in writing, or is written by someone other than the person
  waited on: the episode stays open.
- A correction requires a decision above the item owner: `escalated`.
- An ID is needed for a new linked item: stop and ask.

## Human judgment boundary
Naming the escalation target. Choosing an incident's disposition. Closing an objection, which only
the objector does. Deciding that a correction is complete, which verify confirms and a person
signs at the next gate.

## Worked example
OPPORTUNITY-04, 02-discovery. Line 1: `blocked`, since 2026-07-11, reason "POLICY-03 sign-off for
LATAM accounts", waiting on Tomas Silva, owner Ana Fialho, asks three per the interview of
2026-08-12 and the tracker of 2026-08-22 with dates unknown, limit 3, escalate_to `not named`,
return_to 02-discovery open. The limit is reached. Line 2: `escalated`, target not named. Unknown
added: "escalation target for POLICY-03 sign-off: not named". Line 3: `blocked`, since
2026-09-01, reason "G2 deadline 2026-08-31 passed without signature", waiting on Ana Fialho. The
skill stops and asks Ana Fialho to name an escalation target.
