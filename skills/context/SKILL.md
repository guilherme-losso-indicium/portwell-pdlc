---
name: context
description: Assembles the evidence manifest for an item in a stage, one entry per fact with source, date, metric version and validity, plus stakeholder positions, contradictions and unknowns. Never resolves a disagreement or fills a gap.
---

# Context

## Purpose
Put in front of the stage every fact it needs, with where it came from, how old it is, and whether
anything since has invalidated it. Record what people said in their own words. Record what is
unknown and what is contradictory as exactly that.

## Parameters
`item`, `stage`. Runs in 01-backlog, 02-discovery, 05-review and 07-monitoring.

## Entry conditions
- The stage artifact exists with `status: open` and intake has run.
- `states/<stage>/definition.yaml` lists context in `skills_sequence`.

## Reads
- The stage definition, for `required_evidence`.
- The track repository, through `track.yaml`: `docs/`, `data/`, and their subfolders. In
  particular `docs/Policies.docx` for supersession dates, `docs/incidents/` for incident dates,
  `docs/interviews/` for positions, `data/people/headcount.xlsx` for names and roles.
- The item's previous artifacts and every artifact of a linked item.

## Prohibited context
- Held-out material. `SEED-MANIFEST.md`, `course-shared/`.
- Any external source. No web, no network, no system outside the two repositories.
- The model's own recollection of a figure. A fact with no document behind it is not a fact here.

## Writes
In `lifecycle/<stage>/<item>.yaml`: `sources`, `evidence_manifest`, `stakeholder_positions`,
`contradictions`, `unknowns`. In 01-backlog, `opportunity.attached_requests`. In 05-review,
`rollback_plan` and `entry_ticket.incidents_since_g2`. In 07-monitoring, `active_scope`.

## Never writes
`evidence_manifest[].reaffirmed_by`, `contradictions[].resolved_by`, any `gate` field, any value
that no source states.

## Procedure
1. From the definition's `required_evidence`, list the facts the stage needs. Each becomes a
   manifest entry, even if it ends as `unknown`.
2. List the candidate documents: the ones named in the definition, the ones the previous
   artifact cites in `refs`, and the ones the tracker row points to. Read each. For each, add a
   `sources` entry with path, author, dated and revised. Where the document states no date,
   write `unknown`. Do not infer a date from a file name or from context.
3. For each fact, write one manifest entry: `fact`, `value` as the document states it, `source`,
   `metric_version` if the value is a number and the document states one, otherwise `unknown`,
   `verbal` with who and when if the fact was only spoken.
4. Validity pass. List every incident under `docs/incidents/` with its written date. For each
   manifest fact dated before an incident that touches the item's scope, set `invalidated_by` to
   the incident ID and date and `validity: invalidated`. For each fact whose source is marked
   superseded or replaced, do the same with the superseding document. Do not decide whether the
   invalidation matters. That is a person's call at the gate.
5. Positions. For each person the definition or the route note names as decider or consent, find
   a written position: a stakeholder request, an interview line, a decision record. Quote it
   verbatim with date and path under `stakeholder_positions`. Where none exists, write
   `position: not on record`.
6. Contradictions. Where two entries state the same fact with different values, or a document
   and an interview disagree, add a `contradictions` entry with both sources and what each says.
   Set `depends` to the gate that needs the fact, or `none`. Leave `resolved_by` null.
7. Unknowns. Every required fact with no source becomes an `unknowns` entry with `needed_for`.
   Where a person can be asked, write `asked_to` and `asked_on`.
8. Propose the next skill in the sequence.

## Evidence produced
A manifest in which every fact can be traced to a path and a date, a positions list in which every
required person is either quoted or marked absent, and explicit lists of what is unknown and what
is contradictory.

## Proposed transition
None between stages. Proposes route, or correction-required through recover when an essential
fact has no source.

## Stop and escalation conditions
- A fact the gate depends on has no source: write it under `unknowns`, name who can supply it,
  and propose `correction-required` with `return_to` this stage. Do not continue as if it existed.
- Two sources contradict a fact the gate depends on: record both, set `depends`, and name the
  decider. Continue to route so the pack shows it, but say in the artifact that the gate cannot
  be signed while `resolved_by` is null.
- A number is quoted without a version and another number for the same measure exists: record
  both. Do not decide which population each measures.
- A document is undated and the stage needs its age: `unknown`. Never estimate.

## Human judgment boundary
Resolving a contradiction. Reaffirming a fact an incident invalidated. Deciding that two numbers
measure different things.

## Worked example
OPPORTUNITY-04 in 02-discovery. The brief of 2026-06-18 quotes first response 22 minutes and
self-service 58 per cent, no metric version. EXPERIMENT-02 gives 72 minutes and 36.9 per cent for
six accounts. Both go in the manifest. A contradiction entry records both. INCIDENT-01, written
2026-07-14, invalidates the brief's figures. Rui Bastos's position is quoted from
`2026-08-08-rui-bastos.docx`. Kofi Adjei's position on capacity is `not on record`, because
DECISION-0028 cites only a verbal confirmation.
