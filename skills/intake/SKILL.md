---
name: intake
description: Opens an item's artifact for a stage from the stage template and bounds the work with what the previous gate fixed. In 01-backlog it registers the opportunity itself. Runs first in every stage.
---

# Intake

## Purpose
Create `lifecycle/<stage>/<item>.yaml` from `states/<stage>/template.yaml`, fill the header, and
write down what the item enters this stage with: the previous gate's outcome, its deadline, its
scope. In 01-backlog, register the opportunity from the request that raised it. Nothing else is
decided here.

## Parameters
`item`, `stage`.

## Entry conditions
- For 01-backlog: a request exists with an identifiable origin, who asked, when, through which
  channel, and a requester who can be named.
- For every other stage: the previous stage's artifact has `status: exited` and `exited_to` equal
  to this stage, or a `correction-required` line in some artifact names this stage as `return_to`.
- The item has an ID issued by the product repository. The harness does not issue IDs.

## Reads
- `skills/constitution/SKILL.md`, `states/schema.yaml`, `states/<stage>/definition.yaml`,
  `states/<stage>/template.yaml`.
- The previous stage's artifact for this item, if any.
- For 01-backlog: the request documents in the track repository, `data/discovery/stakeholder-requests/`,
  the item's row in `data/product-tracker.xlsx`, and the opportunity brief if one exists.

## Prohibited context
- Held-out course material, including `SEED-MANIFEST.md` and anything under `course-shared/`.
- Any path outside `track.yaml` `context_repository` and this repository.
- Other items' artifacts, unless they are linked through `links`.

## Writes
`lifecycle/<stage>/<item>.yaml`: the header, `sources`, `status_log` line 1 with `status: open`,
and `entry_ticket`. In 01-backlog, the `opportunity` section except `type_hypothesis`.

## Never writes
`gate.signature`, `gate.outcome`, any section another skill owns, anything in the track repository.

## Procedure
1. Read the stage definition. Check each entry condition and write the result of each check in
   `status_log[1].reason`. If one fails, go to the stop conditions.
2. Copy `states/<stage>/template.yaml` to `lifecycle/<stage>/<item>.yaml`. Do not remove keys.
   Keys with no value stay empty.
3. Fill the header. `item`, `type` and `links` come from the previous artifact. `entered` is
   today's date. `entered_from` is the previous stage or null. `owner` comes from the definition.
4. Fill `entry_ticket` with what the previous gate fixed: its signature date, its outcome, the
   deadline it set and the deadline's source, the scope or the DECISION reference. Copy values.
   Do not summarise them.
5. In 01-backlog, fill `opportunity` from the request documents: `origin.who`, `origin.when`,
   `origin.channel`, `requester`, `scope_hypothesis`, `out_of_scope`, `deadline` with its source.
   Attach every related request under `attached_requests` with ID, sender, date received, what it
   asks, and path. Any field with no source is the literal `unknown`.
6. List every document read under `sources` with path, author, dated and revised.
7. Append `status_log` line 1: `n: 1`, `status: open`, `since` today, `reason` "entered from
   <stage> on outcome <outcome>" or "registered from <request>".
8. Propose the next skill in the definition's `skills_sequence`.

## Evidence produced
The artifact exists, with header, `entry_ticket` or `opportunity`, `sources` and one status line.
A reader can tell from it alone why the item is in this stage and what it must produce here.

## Proposed transition
None between stages. Intake proposes the next skill of the sequence.

## Stop and escalation conditions
- The previous artifact is not exited, or its `exited_to` is another stage: stop, do not create
  the artifact, report the mismatch to the stage owner.
- The previous gate has no signature on record, which is the case for every item that predates
  the harness: create the artifact, write under `unknowns` "gate <id> signature: not on record",
  set `status_log[1].reason` to "entered without gate record", and ask the stage owner in writing
  to ratify the entry. Legacy onboarding rule: the evidence-gathering skills, context, route, act
  and verify, may run, because they only read and record. approve may prepare the pack. handoff
  may not move the item, and no gate may be signed, until the ratification is on record. The
  artifact of the stage the item skipped is also created, open, with its gate unsigned, so the
  board shows the item in two columns. That is the finding, not an error to hide.
- Origin or requester cannot be identified in 01-backlog: write `unknown` in those fields and ask
  the product lead who raised it. Do not register a substitute.
- The item has no ID from the product repository: stop and ask. Never coin an ID.

## Human judgment boundary
Whether an item that predates the harness may enter a stage without its gate record. Who raised
an opportunity when no document says so. Issuing identifiers.

## Worked example
OPPORTUNITY-04 in 02-discovery: there is no G1 record. Intake creates the artifact, writes the
unknown, sets the G2 deadline to 2026-08-31 from `2026-08-13-ana-fialho.docx`, and asks Ana Fialho
whether the item may proceed on that basis.
